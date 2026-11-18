"""
clear_practice.py: remove your solutions from a practice script so you can redo it.
 
What it does
    - every function body (including methods inside a class) is replaced by `...`
    - the def line, the docstring, and everything outside functions are kept
      (cell headers, comments, explanations, given variables, test calls)
    - lines between `# >>> solution` and `# <<< solution` are removed
      (use this for solution code that is NOT inside a function)
 
What it leaves alone
    - a function whose def line ends with `# keep`  (e.g. a helper you need)
    - a class whose class line ends with `# keep`   (e.g. ListNode)
 
Usage
    python clear_practice.py two-pointers-practice.py
        -> clears the file itself, after copying it to backups/
    python clear_practice.py --all
        -> clears every *-practice.py in this folder 
    python clear_practice.py two-pointers.py -o two-pointers-practice.py
        -> writes the cleared version to a new file, leaving the source as is
    add --keep-comments to keep the comment lines inside function bodies
    (useful when those comments are your step-by-step plan)
 
Backups go to the `backups` folder next to this script, named with the date
and time, e.g. backups/two-pointers-practice_2026-11-02_1704.py, so an older
backup is never overwritten. "This folder" for --all also means the folder
this script is in.
"""
 
import argparse
import ast
import shutil
import sys
from datetime import datetime
from pathlib import Path
 
HERE = Path(__file__).resolve().parent
BACKUP_DIR = HERE / "backups"
 
START_MARK = "# >>> solution"
END_MARK = "# <<< solution"
KEEP_MARK = "# keep"
 
 
def indent_of(line):
    return len(line) - len(line.lstrip())
 
 
def is_comment_or_blank(line):
    s = line.strip()
    return s == "" or s.startswith("#")
 
 
def has_docstring(node):
    first = node.body[0]
    return (isinstance(first, ast.Expr)
            and isinstance(first.value, ast.Constant)
            and isinstance(first.value.value, str))
 
 
def functions_to_clear(tree, lines):
    """Outermost functions (and methods) that should be emptied."""
    found = []
 
    def visit(node):
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                def_line = lines[child.lineno - 1]
                if not def_line.rstrip().endswith(KEEP_MARK):
                    found.append(child)
                # nested functions are inside this body, so don't go deeper
            elif isinstance(child, ast.ClassDef):
                if not lines[child.lineno - 1].rstrip().endswith(KEEP_MARK):
                    visit(child)
            else:
                visit(child)
 
    visit(tree)
    return found
 
 
def clear_functions(lines, keep_comments):
    tree = ast.parse("".join(lines))
    # edit from the bottom up so earlier line numbers stay valid
    for fn in sorted(functions_to_clear(tree, lines), key=lambda f: -f.lineno):
        if fn.body[0].lineno == fn.lineno:
            continue  # one-line def like `def f(x): return x`, leave it
        def_indent = indent_of(lines[fn.lineno - 1])
        body_indent = " " * (indent_of(lines[fn.body[0].lineno - 1]))
 
        if has_docstring(fn):
            if len(fn.body) == 1:
                continue  # already just a docstring
            start = fn.body[0].end_lineno  # first line after the docstring (0-based)
        else:
            # first line after the signature (handles multi-line signatures)
            start = fn.body[0].lineno - 1
            while start > fn.lineno and is_comment_or_blank(lines[start - 1]):
                start -= 1  # pull in comments between def and first statement
 
        end = fn.end_lineno  # 0-based exclusive end of the body
        # also swallow trailing comments that are still indented inside the body
        while end < len(lines) and is_comment_or_blank(lines[end]):
            if lines[end].strip() and indent_of(lines[end]) > def_indent:
                end += 1
            elif not lines[end].strip():
                # blank line: only swallow it if body comments follow it
                nxt = end
                while nxt < len(lines) and not lines[nxt].strip():
                    nxt += 1
                if (nxt < len(lines) and lines[nxt].lstrip().startswith("#")
                        and indent_of(lines[nxt]) > def_indent):
                    end = nxt
                else:
                    break
            else:
                break
 
        new_body = []
        if keep_comments:
            new_body = [l for l in lines[start:end] if l.lstrip().startswith("#")]
        new_body.append(body_indent + "...\n")
        lines[start:end] = new_body
    return lines
 
 
def clear_marked_blocks(lines):
    out, inside = [], False
    for line in lines:
        s = line.strip()
        if s.startswith(START_MARK):
            inside = True
            out.append(line[:indent_of(line)] + "...\n")
            continue
        if s.startswith(END_MARK):
            inside = False
            continue
        if not inside:
            out.append(line)
    if inside:
        raise ValueError(f"'{START_MARK}' has no matching '{END_MARK}'")
    return out
 
 
def clear_text(text, keep_comments):
    try:
        ast.parse(text)
    except SyntaxError as e:
        raise ValueError(f"does not run as Python (line {e.lineno}: {e.msg}). Fix that first.")
    lines = text.splitlines(keepends=True)
    if lines and not lines[-1].endswith("\n"):
        lines[-1] += "\n"
    lines = clear_marked_blocks(lines)
    lines = clear_functions(lines, keep_comments)
    result = "".join(lines)
    ast.parse(result)  # the cleared file must still run
    return result
 
 
def backup(path):
    BACKUP_DIR.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    dest = BACKUP_DIR / f"{path.stem}_{stamp}.py"
    n = 2
    while dest.exists():  # two runs in the same second
        dest = BACKUP_DIR / f"{path.stem}_{stamp}_{n}.py"
        n += 1
    shutil.copy(path, dest)
    return dest
 
 
def clear_file(src, output, keep_comments):
    result = clear_text(src.read_text(encoding="utf-8"), keep_comments)
    dest = Path(output) if output else src
    if dest.exists():
        print(f"backed up {dest.name} -> {backup(dest)}")
    dest.write_text(result, encoding="utf-8")
    print(f"cleared {src}" + (f" -> {dest}" if output else ""))
 
 
def main():
    p = argparse.ArgumentParser(description="Remove solutions from practice scripts.")
    p.add_argument("source", nargs="?", help="file to clear (cleared in place)")
    p.add_argument("--all", action="store_true",
                   help="clear every *-practice.py in this script's folder and subfolders")
    p.add_argument("-o", "--output", help="write the cleared version here instead")
    p.add_argument("--keep-comments", action="store_true")
    args = p.parse_args()
 
    if args.all:
        if args.source or args.output:
            sys.exit("--all takes no file name or -o")
        files = sorted(f for f in HERE.glob("*-practice.py") if BACKUP_DIR not in f.parents)
    elif args.source:
        files = [Path(args.source)]
    else:
        sys.exit("give a file name, or --all")
 
    failed = 0
    for f in files:
        try:
            clear_file(f, args.output, args.keep_comments)
        except ValueError as e:
            failed += 1
            print(f"SKIPPED {f}: {e}")
    if failed:
        sys.exit(f"{failed} file(s) skipped, nothing was changed in those")
 
 
if __name__ == "__main__":
    main()
 