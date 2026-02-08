# Implementation Plan: Roster File Parsing (v0.1.0)

**Spec Reference:** [spec.md](./spec.md)

---

## Proposed Changes

```
src/warscribe_parser/
├── __init__.py          # parse_file(), parse_string()
├── models.py            # ParseResult, ParseError
├── parsers/
│   ├── __init__.py      # Parser registry
│   ├── base.py          # BaseParser ABC
│   ├── battlescribe_xml.py  # .ros XML parser
│   ├── battlescribe_zip.py  # .rosz decompressor → XML parser
│   └── json_roster.py       # JSON roster parser
└── mapping/
    ├── __init__.py
    └── battlescribe.py  # XML element → Vindicta-Core model mapping
```

### Key Design Decisions

- **Parser Registry**: Auto-detect format from extension, dispatch to correct parser
- **Two-Phase**: Parse raw format → intermediate dict → Vindicta-Core models
- **Error Accumulation**: Parsers collect all errors, don't fail on first

### Tests

```
tests/
├── test_battlescribe_xml.py  # Sample .ros files
├── test_battlescribe_zip.py  # Sample .rosz files
├── test_json_roster.py       # JSON format
├── test_parse_api.py         # High-level API
└── fixtures/                 # Sample roster files
```

---

## Verification

```powershell
uv run pytest tests/ -v
uv run mypy src/warscribe_parser/ --strict
```
