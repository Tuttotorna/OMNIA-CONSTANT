import argparse
import sys
from pathlib import Path

from .core import analyze_observations, read_jsonl, write_all_reports


def main():
    parser = argparse.ArgumentParser(
        prog="omnia-constant-audit",
        description="Audit candidate constants across supplied observation contexts.",
    )

    parser.add_argument("--input", required=True, help="JSONL file with constant/context/value observations.")
    parser.add_argument("--out-dir", default="omnia_constant_report", help="Output directory.")
    parser.add_argument("--drift-threshold", type=float, default=0.05, help="Variation threshold above which a candidate is drift.")
    parser.add_argument("--rupture-threshold", type=float, default=0.40, help="Variation threshold above which a candidate is rupture.")
    parser.add_argument("--fail-on-drift", action="store_true", help="Exit with code 2 if drift appears, or 3 if rupture appears.")
    parser.add_argument("--fail-on-rupture", action="store_true", help="Exit with code 3 if rupture appears.")

    args = parser.parse_args()

    try:
        observations = read_jsonl(args.input)
        result = analyze_observations(
            observations=observations,
            drift_threshold=args.drift_threshold,
            rupture_threshold=args.rupture_threshold,
        )
        write_all_reports(args.out_dir, result)
    except Exception as e:
        print("ERROR:", str(e))
        sys.exit(4)

    s = result["summary"]

    print("")
    print("OMNIA CONSTANT AUDIT")
    print("====================")
    print(f"input:                 {args.input}")
    print(f"total_constants:       {s['total_constants']}")
    print(f"total_observations:    {s['total_observations']}")
    print(f"constant:              {s['constant']}")
    print(f"drift:                 {s['drift']}")
    print(f"rupture:               {s['rupture']}")
    print(f"constant_rate:         {s['constant_rate']:.6f}")
    print(f"drift_rate:            {s['drift_rate']:.6f}")
    print(f"rupture_rate:          {s['rupture_rate']:.6f}")
    print(f"mean_constancy_score:  {s['mean_constancy_score']:.6f}")
    print(f"worst_constant_id:     {s['worst_constant_id']}")
    print("")
    print(f"WROTE: {Path(args.out_dir) / 'report.json'}")
    print(f"WROTE: {Path(args.out_dir) / 'report.csv'}")
    print(f"WROTE: {Path(args.out_dir) / 'report.html'}")
    print(f"WROTE: {Path(args.out_dir) / 'drift_constants.jsonl'}")
    print(f"WROTE: {Path(args.out_dir) / 'rupture_constants.jsonl'}")
    print(f"WROTE: {Path(args.out_dir) / 'certificate.json'}")
    print("")

    if args.fail_on_rupture and s["rupture"] > 0:
        sys.exit(3)

    if args.fail_on_drift:
        if s["rupture"] > 0:
            sys.exit(3)
        if s["drift"] > 0:
            sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
