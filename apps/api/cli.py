import json
from pathlib import Path
import argparse
from .main import jtr, plan

parser = argparse.ArgumentParser(description="apply-copilot CLI")
sub = parser.add_subparsers(dest="cmd")

jtr_p = sub.add_parser("jtr")
jtr_p.add_argument("--resume")
jtr_p.add_argument("--jd")
jtr_p.add_argument("--out", default="out")

plan_p = sub.add_parser("plan")
plan_p.add_argument("--fields")
plan_p.add_argument("--out", default="out")


def main():
    args = parser.parse_args()
    if args.cmd == "jtr":
        payload = json.load(open(args.resume))
        jd_text = Path(args.jd).read_text()
        payload["job"] = {"source": "mock", "company": "Acme", "title": "Analyst", "jd_html": jd_text}
        result = jtr(payload)
        Path(args.out).mkdir(parents=True, exist_ok=True)
        (Path(args.out) / "jtr.json").write_text(json.dumps(result, indent=2))
        print(f"Wrote {args.out}/jtr.json")
    elif args.cmd == "plan":
        field_list = json.load(open(args.fields))
        result = plan(field_list)
        Path(args.out).mkdir(parents=True, exist_ok=True)
        (Path(args.out) / "plan.json").write_text(json.dumps(result, indent=2))
        print(f"Wrote {args.out}/plan.json")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
