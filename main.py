#!/usr/bin/env python3
"""One Line, Big Laugh — make.fun entry.

Writes a single funny line (1-200 chars) to the output file.
Stdlib only. No cwd dependence: the output path is resolved from
ENTRY_OUTPUT, then OUTPUT_DIR / MAKEFUN_OUTPUT_DIR, then
/output/entry.txt, falling back to the script's own directory.
"""

import os

LINE = "I proved I'm human by failing the CAPTCHA three times. The robot passed on the first try."


def resolve_output_path():
    explicit = os.environ.get("ENTRY_OUTPUT")
    if explicit:
        return explicit
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main():
    path = resolve_output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    os.chmod(path, 0o644)
    return path


if __name__ == "__main__":
    print(main())
