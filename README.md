## Folder Analyzer CLI

A simple Python command-line tool to count the total number of files in a folder.

### What this tool does
- Takes a folder path as input
- Counts all files inside that folder (including subfolders)
- Prints the total file count
- Prints the python file count and text file count with their extension as keyword.
- Recursively Counts the sub-folders files.

## Features

* Counts specific file types (user-defined)
* Supports JSON output for automation
* Validates folder path before processing

### JSON Output

You can get machine-readable output using the `--json` flag.

```bash
python analyze.py . --json


## How to run

```bash
python analyze.py <folder_path>
