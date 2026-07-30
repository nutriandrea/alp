#!/usr/bin/env python3
"""alp-learn: Guide an agent through an ALP vault. Loads syllabus, helps navigate."""

import sys, os, yaml, re
from pathlib import Path

def load_vault(path="."):
    vault_file = Path(path) / "alp.md"
    if not vault_file.exists():
        print("❌ No alp.md found in", path)
        sys.exit(1)

    content = vault_file.read_text()
    # parse frontmatter
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        print("❌ No frontmatter in alp.md")
        sys.exit(1)

    meta = yaml.safe_load(match.group(1))
    return meta

def show_syllabus(meta):
    print(f"📚 {meta['name']} v{meta.get('version', '?')}")
    print(f"   {meta.get('description', '')}")
    print()
    if meta.get('prerequisites'):
        print("📋 Prerequisites:")
        for p in meta['prerequisites']:
            print(f"   - {p}")
        print()
    curriculum = meta.get('curriculum', [])
    print(f"📖 Curriculum ({len(curriculum)} concepts):")
    for i, c in enumerate(curriculum, 1):
        status = "○"
        print(f"   {status} {i:02d}. {c['title']}")
    print()
    print("▶️  Start with:  alp-learn --concept 0")

def show_concept(meta, index):
    curriculum = meta.get('curriculum', [])
    if index < 0 or index >= len(curriculum):
        print(f"❌ Concept index {index} out of range (0-{len(curriculum)-1})")
        sys.exit(1)

    c = curriculum[index]
    print(f"📖 Concept {index+1}/{len(curriculum)}: {c['title']}")
    print(f"   File: {c['path']}")
    print()
    if meta.get('source'):
        print(f"   Source: {meta['source']}")
    print()
    if index > 0:
        prev_c = curriculum[index-1]
        print(f"⬅️  Previous: {prev_c['title']}  (alp-learn --concept {index-1})")
    if index < len(curriculum) - 1:
        next_c = curriculum[index+1]
        print(f"➡️  Next: {next_c['title']}  (alp-learn --concept {index+1})")
    print()
    print("💡 Read the concept file for content.")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Navigate an ALP vault")
    parser.add_argument("--vault", default=".", help="Path to ALP vault")
    parser.add_argument("--concept", type=int, default=None, help="Show specific concept by index")
    args = parser.parse_args()

    meta = load_vault(args.vault)
    if args.concept is not None:
        show_concept(meta, args.concept)
    else:
        show_syllabus(meta)

if __name__ == "__main__":
    main()
