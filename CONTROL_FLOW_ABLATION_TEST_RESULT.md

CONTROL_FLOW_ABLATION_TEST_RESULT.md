# =============================================================================
# CONTROL FLOW ABLATION TEST
# =============================================================================

!apt-get -qq update
!apt-get -qq install git > /dev/null

!pip -q install numpy pandas tqdm scipy

import os
import re
import ast
import json
import math
import shutil
import subprocess
from collections import defaultdict

import numpy as np
import pandas as pd

from tqdm import tqdm
from scipy.stats import pearsonr, ks_2samp, mannwhitneyu

# =============================================================================
# CONFIG
# =============================================================================

REPO_URL = "https://github.com/django/django.git"
REPO_DIR = "/content/django"

COMMITS_TO_LOAD = 2500

WINDOW_SIZE = 25
WINDOW_STEP = 10

RESULT_DIR = "/content/CONTROL_FLOW_ABLATION_TEST/results"

CONTROL_FLOW_NODES = {
    ast.If,
    ast.For,
    ast.While,
    ast.Try,
    ast.Match if hasattr(ast, "Match") else ast.If,
    ast.BoolOp,
    ast.IfExp,
    ast.With,
    ast.AsyncFor,
    ast.AsyncWith,
}

NON_CONTROL_NODES = {
    ast.Assign,
    ast.Constant,
    ast.Name,
    ast.Import,
    ast.ImportFrom,
    ast.Expr,
}

# =============================================================================
# RESET
# =============================================================================

if os.path.exists(REPO_DIR):
    shutil.rmtree(REPO_DIR)

os.makedirs(RESULT_DIR, exist_ok=True)

print("=" * 80)
print("CONTROL FLOW ABLATION TEST")
print("=" * 80)

# =============================================================================
# CLONE
# =============================================================================

print("\nCloning repository...")

subprocess.run(
    ["git", "clone", "--quiet", REPO_URL, REPO_DIR],
    check=True
)

# =============================================================================
# COMMITS
# =============================================================================

print("Collecting commits...")

os.chdir(REPO_DIR)

commit_lines = subprocess.check_output([
    "git",
    "log",
    "--format=%H"
]).decode().splitlines()

commit_lines = commit_lines[:COMMITS_TO_LOAD]

print("Commits loaded:", len(commit_lines))

# =============================================================================
# HELPERS
# =============================================================================

def get_commit_diff(commit_hash):
    try:
        return subprocess.check_output([
            "git",
            "show",
            commit_hash,
            "--unified=0",
            "--no-color"
        ]).decode(errors="ignore")
    except:
        return ""

def extract_python_files(commit_hash):
    try:
        out = subprocess.check_output([
            "git",
            "diff-tree",
            "--no-commit-id",
            "--name-only",
            "-r",
            commit_hash
        ]).decode().splitlines()

        return [x for x in out if x.endswith(".py")]
    except:
        return []

def checkout_file(commit_hash, filepath):
    try:
        return subprocess.check_output([
            "git",
            "show",
            f"{commit_hash}:{filepath}"
        ]).decode(errors="ignore")
    except:
        return None

def ast_node_counter(code):
    counts = defaultdict(int)

    try:
        tree = ast.parse(code)
    except:
        return counts

    for node in ast.walk(tree):
        counts[type(node)] += 1

    return counts

# =============================================================================
# OMEGA PROXY
# =============================================================================

def compute_omega_proxy(diff_text):

    added = 0
    deleted = 0
    hunks = 0

    for line in diff_text.splitlines():

        if line.startswith("@@"):
            hunks += 1

        elif line.startswith("+") and not line.startswith("+++"):
            added += 1

        elif line.startswith("-") and not line.startswith("---"):
            deleted += 1

    total = added + deleted

    if total == 0:
        return 0.0

    omega = (
        math.log1p(total)
        + math.log1p(hunks)
        + (deleted / (total + 1e-9))
    )

    return float(omega)

# =============================================================================
# EVENTS
# =============================================================================

events = []

print("\nCollecting commit metrics...")

for i in tqdm(range(1, len(commit_lines))):

    commit_hash = commit_lines[i]
    parent_hash = commit_lines[i - 1]

    py_files = extract_python_files(commit_hash)

    if not py_files:
        continue

    control_delta = 0
    non_control_delta = 0

    for filepath in py_files[:20]:

        before = checkout_file(parent_hash, filepath)
        after = checkout_file(commit_hash, filepath)

        if before is None or after is None:
            continue

        before_counts = ast_node_counter(before)
        after_counts = ast_node_counter(after)

        for node_type in CONTROL_FLOW_NODES:
            control_delta += abs(
                after_counts[node_type]
                - before_counts[node_type]
            )

        for node_type in NON_CONTROL_NODES:
            non_control_delta += abs(
                after_counts[node_type]
                - before_counts[node_type]
            )

    diff_text = get_commit_diff(commit_hash)

    omega = compute_omega_proxy(diff_text)

    if control_delta > 0:
        group = "A_CONTROL_FLOW"
    else:
        group = "B_NON_CONTROL"

    events.append({
        "commit": commit_hash[:12],
        "omega": omega,
        "control_delta": control_delta,
        "non_control_delta": non_control_delta,
        "group": group,
    })

print("Events collected:", len(events))

# =============================================================================
# DATAFRAME
# =============================================================================

df = pd.DataFrame(events)

group_a = df[df["group"] == "A_CONTROL_FLOW"]
group_b = df[df["group"] == "B_NON_CONTROL"]

# =============================================================================
# STATS
# =============================================================================

print("\nComputing statistics...")

summary = {}

summary["group_counts"] = {
    "A_CONTROL_FLOW": int(len(group_a)),
    "B_NON_CONTROL": int(len(group_b)),
}

summary["group_means"] = {
    "A_CONTROL_FLOW": float(group_a["omega"].mean()),
    "B_NON_CONTROL": float(group_b["omega"].mean()),
}

summary["group_medians"] = {
    "A_CONTROL_FLOW": float(group_a["omega"].median()),
    "B_NON_CONTROL": float(group_b["omega"].median()),
}

summary["group_variances"] = {
    "A_CONTROL_FLOW": float(group_a["omega"].var()),
    "B_NON_CONTROL": float(group_b["omega"].var()),
}

summary["percentiles"] = {
    "A_p90": float(group_a["omega"].quantile(0.90)),
    "B_p90": float(group_b["omega"].quantile(0.90)),
    "A_p95": float(group_a["omega"].quantile(0.95)),
    "B_p95": float(group_b["omega"].quantile(0.95)),
}

# =============================================================================
# TESTS
# =============================================================================

ks_stat, ks_p = ks_2samp(
    group_a["omega"],
    group_b["omega"]
)

mw_stat, mw_p = mannwhitneyu(
    group_a["omega"],
    group_b["omega"],
    alternative="two-sided"
)

summary["distribution_tests"] = {
    "ks_statistic": float(ks_stat),
    "ks_pvalue": float(ks_p),
    "mannwhitney_statistic": float(mw_stat),
    "mannwhitney_pvalue": float(mw_p),
}

# =============================================================================
# TOP EVENTS
# =============================================================================

summary["top_control_flow_commits"] = (
    group_a
    .sort_values("omega", ascending=False)
    .head(20)
    .to_dict(orient="records")
)

summary["top_non_control_commits"] = (
    group_b
    .sort_values("omega", ascending=False)
    .head(20)
    .to_dict(orient="records")
)

# =============================================================================
# SAVE JSON
# =============================================================================

json_path = os.path.join(
    RESULT_DIR,
    "CONTROL_FLOW_ABLATION_TEST.json"
)

with open(json_path, "w") as f:
    json.dump(summary, f, indent=2)

# =============================================================================
# MARKDOWN
# =============================================================================

md = []

md.append("# CONTROL FLOW ABLATION TEST\n")

md.append("## Group Counts\n")
md.append("```json")
md.append(json.dumps(summary["group_counts"], indent=2))
md.append("```\n")

md.append("## Group Means\n")
md.append("```json")
md.append(json.dumps(summary["group_means"], indent=2))
md.append("```\n")

md.append("## Group Medians\n")
md.append("```json")
md.append(json.dumps(summary["group_medians"], indent=2))
md.append("```\n")

md.append("## Group Variances\n")
md.append("```json")
md.append(json.dumps(summary["group_variances"], indent=2))
md.append("```\n")

md.append("## Percentiles\n")
md.append("```json")
md.append(json.dumps(summary["percentiles"], indent=2))
md.append("```\n")

md.append("## Distribution Tests\n")
md.append("```json")
md.append(json.dumps(summary["distribution_tests"], indent=2))
md.append("```\n")

md_path = os.path.join(
    RESULT_DIR,
    "CONTROL_FLOW_ABLATION_TEST_RESULT.md"
)

with open(md_path, "w") as f:
    f.write("\n".join(md))

# =============================================================================
# PRINT
# =============================================================================

print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)

print(json.dumps(summary, indent=2))

print("\n" + "=" * 80)
print("RESULT FILES")
print("=" * 80)

print(json_path)
print(md_path)

print("\n" + "=" * 80)
print("DONE")
print("=" * 80)