# ALP — OKF Compatibility Profile

ALP v0.1 is compatible with [OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) v0.1.

An ALP vault IS an OKF bundle. Every ALP file IS a valid OKF file.

## Type Mapping

| ALP Type | OKF Handling |
|----------|-------------|
| `alp-vault` | Treated as OKF bundle with custom type `alp-vault` |
| `alp-concept` | Treated as OKF concept with custom type `alp-concept` |
| `alp-practice` | Treated as OKF concept with custom type `alp-practice` |
| `alp-lab` | Treated as OKF concept with custom type `alp-lab` |
| `alp-cheatsheet` | Treated as OKF reference with custom type `alp-cheatsheet` |
| `alp-glossary` | Treated as OKF reference with custom type `alp-glossary` |

## Extended Fields

ALP adds these fields on top of OKF:

- **`alp-version`** (string) — ALP spec version
- **`curriculum`** (array) — Ordered learning path
- **`prerequisites`** (array at vault level) — Prerequisite vaults
- **`source`** (string) — Original content source URL
- **`source-type`** (enum) — Content type: `youtube`, `blog`, `doc`, `screencast`, `live-lecture`, `course`

OKF consumers that don't understand these fields simply ignore them.
The file is still valid OKF and can be indexed, searched, and retrieved.

## Conversion: OKF → ALP

To convert an OKF bundle to an ALP vault:

1. Add `alp.md` with `type: alp-vault` and a `curriculum` ordering
2. Set `alp-version: 0.1`
3. Existing OKF concept files remain unchanged
4. Add ALP-specific fields to frontmatter as desired

## Conversion: ALP → OKF

To use an ALP vault in an OKF-native tool:

1. Strip `alp-version`, `curriculum`, `prerequisites` from frontmatter
2. Change `type: alp-vault` to an OKF-compatible type
3. All concept content remains usable
