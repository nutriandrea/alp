#!/usr/bin/env python3
"""alp-validate: Validate ALP vault structure and frontmatter."""

import sys, os, yaml, re
from pathlib import Path

errors = []
warnings = []

def err(msg, file=""):
    errors.append(f"{'['+file+']' if file else ''} {msg}")
def warn(msg, file=""):
    warnings.append(f"{'['+file+']' if file else ''} {msg}")

def reset():
    errors.clear()
    warnings.clear()

def check_frontmatter(content, path, required_type):
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        err("Missing or malformed YAML frontmatter", path)
        return None
    try:
        meta = yaml.safe_load(match.group(1))
    except yaml.YAMLError as e:
        err(f"YAML parse error: {e}", path)
        return None
    if not isinstance(meta, dict):
        err("Frontmatter is not a dictionary", path)
        return None
    if meta.get("type") != required_type:
        err(f"Expected type '{required_type}', got '{meta.get('type')}'", path)
    return meta

def validate_vault(root):
    root = Path(root)
    if not root.is_dir():
        err(f"Not a directory: {root}")
        return

    # 1. Check alp.md exists
    alp_file = root / "alp.md"
    if not alp_file.exists():
        err("Missing required file: alp.md", str(alp_file))
        return  # can't continue without syllabus
    meta = check_frontmatter(alp_file.read_text(), "alp.md", "alp-vault")
    if not meta:
        return

    # 2. Check required fields
    for field in ["name", "description"]:
        if not meta.get(field):
            err(f"Missing required field: {field}", "alp.md")
    if not meta.get("curriculum"):
        warn("No curriculum defined", "alp.md")
    else:
        # 3. Verify curriculum paths exist
        for item in meta["curriculum"]:
            if not item.get("id"):
                err("Curriculum item missing 'id'", "alp.md")
                continue
            cpath = item.get("path", "")
            if cpath:
                full_path = root / cpath
                if not full_path.exists():
                    err(f"Concept file not found: {cpath} (id: {item['id']})", "alp.md")
            else:
                err(f"Curriculum item '{item['id']}' missing 'path'", "alp.md")

    # 4. Validate all concept files
    concepts_dir = root / "concepts"
    if concepts_dir.exists():
        for f in sorted(concepts_dir.iterdir()):
            if f.suffix == ".md":
                check_frontmatter(f.read_text(), f.name, "alp-concept")

    # 5. Check practices
    practices_dir = root / "practices"
    if practices_dir.exists():
        for f in sorted(practices_dir.iterdir()):
            if f.suffix == ".md":
                check_frontmatter(f.read_text(), f.name, "alp-practice")

    # 6. Check labs
    labs_dir = root / "labs"
    if labs_dir.exists():
        for f in sorted(labs_dir.iterdir()):
            if f.suffix == ".md":
                check_frontmatter(f.read_text(), f.name, "alp-lab")

    # 7. Check optional files
    for opt in ["cheatsheet.md", "glossary.md"]:
        f = root / opt
        if f.exists():
            expected = "alp-cheatsheet" if opt == "cheatsheet.md" else "alp-glossary"
            check_frontmatter(f.read_text(), opt, expected)

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Validate an ALP vault")
    parser.add_argument("vault", nargs="?", default=".", help="Path to ALP vault")
    args = parser.parse_args()

    validate_vault(args.vault)

    if errors:
        print(f"❌ {len(errors)} error(s):")
        for e in errors:
            print(f"   {e}")
    if warnings:
        print(f"⚠️  {len(warnings)} warning(s):")
        for w in warnings:
            print(f"   {w}")
    if not errors and not warnings:
        print("✅ Vault is valid")
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
