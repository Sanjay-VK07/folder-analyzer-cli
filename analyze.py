import os
import json
import argparse


def analyze_folder(path, types):
    total_files = 0
    type_counts = {t: 0 for t in types}

    for _, _, files in os.walk(path):
        total_files += len(files)
        for f in files:
            for t in types:
                if f.endswith("." + t):
                    type_counts[t] += 1

    result = {"total_files": total_files}
    for t in types:
        result[f"{t}_files"] = type_counts[t]

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Analyze a folder and count files"
    )

    parser.add_argument(
        "path",help="Path of the folder to analyze"
    )

    parser.add_argument(
        "--types", nargs="+", default=["py", "txt"], help="File types to count (example: --types py txt md)"
    )

    parser.add_argument(
        "--json", action="store_true", help="Output result in JSON format"
    )

    args = parser.parse_args()

    if not os.path.isdir(args.path):
        print(f"Error: '{args.path}' is not a valid folder")
        return

    result = analyze_folder(args.path, args.types)


    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("Total files:", result["total_files"])
        for t in args.types:
            print(f".{t} files:", result.get(f"{t}_files", 0))



if __name__ == "__main__":
    main()
