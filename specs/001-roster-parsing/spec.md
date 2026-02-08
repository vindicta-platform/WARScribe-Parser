# Specification: Roster File Parsing (v0.1.0)

**Feature ID:** 001-roster-parsing
**Milestone:** v0.1.0 — Roster File Parsing
**Priority:** P1
**Status:** Specified
**Target Date:** Feb 17, 2026

---

## 1. Problem Statement

Players use tools like BattleScribe to create army rosters, exporting as
`.ros`, `.rosz` (XML), and `.json` files. The Vindicta Platform needs to
ingest these rosters and convert them into canonical Vindicta-Core `ArmyList`
models so the ecosystem (Portal, API, AI) can operate on standardized data.

---

## 2. Vision

Create a parser library that reads common roster file formats and produces
Vindicta-Core `ArmyList` + `Unit` models, bridging the gap between external
roster tools and the Vindicta ecosystem.

---

## 3. User Stories

### US-01: Portal User — BattleScribe Import

> As a **Vindicta-Portal user**,
> I want to **upload my BattleScribe .rosz file**,
> So that **my army list is automatically imported with all unit stats**.

**Acceptance Criteria:**

- [ ] `.rosz` files are decompressed (ZIP) and XML is extracted
- [ ] Parser produces a Vindicta-Core `ArmyList` with all units
- [ ] Unit stats, keywords, and wargear are populated
- [ ] Parsing errors return clear error messages with line/field context

### US-02: API Developer — JSON Roster Import

> As the **Vindicta-API**,
> I want to **accept JSON roster payloads**,
> So that **programmatic roster submission is supported**.

**Acceptance Criteria:**

- [ ] JSON roster format defined and documented
- [ ] Parser produces same `ArmyList` output as XML parser
- [ ] Validation errors use consistent error model

### US-03: CLI User — Local File Parsing

> As a **WARScribe-CLI user**,
> I want to **parse a local .ros file from the command line**,
> So that **I can view my army list without opening BattleScribe**.

**Acceptance Criteria:**

- [ ] `parse_file(path)` accepts file path
- [ ] Auto-detects format from extension
- [ ] Returns `ParseResult` with army list or errors

---

## 4. Functional Requirements

### 4.1 Supported Formats

| Format                  | Extension | Parser            |
| ----------------------- | --------- | ----------------- |
| BattleScribe XML        | `.ros`    | XML (ElementTree) |
| BattleScribe Compressed | `.rosz`   | ZIP + XML         |
| JSON Roster             | `.json`   | JSON (Pydantic)   |

### 4.2 Parser API

```python
from warscribe_parser import parse_file, parse_string

# From file
result = parse_file("my_army.rosz")

# From string
result = parse_string(xml_content, format="battlescribe_xml")

# Result
if result.success:
    army_list: ArmyList = result.army_list
else:
    for error in result.errors:
        print(f"{error.field}: {error.message}")
```

### 4.3 ParseResult Model

| Field           | Type               | Description               |
| --------------- | ------------------ | ------------------------- |
| `success`       | `bool`             | Whether parsing succeeded |
| `army_list`     | `ArmyList \| None` | Parsed army list          |
| `errors`        | `list[ParseError]` | List of parsing errors    |
| `warnings`      | `list[str]`        | Non-fatal warnings        |
| `source_format` | `str`              | Detected format           |

### 4.4 BattleScribe XML Mapping

| XML Element               | Maps To                |
| ------------------------- | ---------------------- |
| `<roster>`                | `ArmyList`             |
| `<force>`                 | Faction/Detachment     |
| `<selection>` (type=unit) | `Unit`                 |
| `<profile>` (type=Unit)   | `StatsBlock`           |
| `<profile>` (type=Weapon) | `WeaponProfile`        |
| `<characteristic>`        | Individual stat fields |

---

## 5. Non-Functional Requirements

| Category           | Requirement                                   |
| ------------------ | --------------------------------------------- |
| **Performance**    | Parse 2000pt roster < 100ms                   |
| **Error Handling** | Never crash on malformed input; return errors |
| **Type Safety**    | 100% strict mypy                              |
| **Dependencies**   | Pydantic v2, lxml or stdlib xml               |

---

## 6. Out of Scope

- Audio transcription (deferred to v0.2.0)
- Video parsing (deferred to v0.3.0)
- BattleScribe catalogue (.cat) parsing
- Data file management

---

## 7. Success Criteria

| Metric          | Target                                |
| --------------- | ------------------------------------- |
| Format support  | 3 formats (ros, rosz, json)           |
| Output fidelity | Matches Vindicta-Core ArmyList schema |
| Error handling  | Graceful on malformed input           |
| Test coverage   | > 90%                                 |
