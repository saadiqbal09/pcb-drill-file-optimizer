import argparse
from parser import parse_drill_file

def main():
    parser = argparse.ArgumentParser(
        description="PCB Drill File Optimizer"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to Excellon (.drl) file"
    )

    args = parser.parse_args()

    tools, points = parse_drill_file(args.input)

    print(f"Tools detected: {len(tools)}")
    print(f"Drill points: {len(points)}")

if __name__ == "__main__":
    main()
