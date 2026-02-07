# WARScribe-Parser

Parser and validator for the WARScribe data format.

## Overview

WARScribe-Parser is the core parsing library for WARScribe notation, providing schema validation, data extraction, and format conversion.

## Features

- **Schema Validation**: Validate against WARScribe specification
- **Data Extraction**: Parse army lists, unit profiles, game state
- **Format Support**: JSON, YAML, custom notation
- **Error Reporting**: Detailed parsing error messages

## Installation

Install from source using uv:

```bash
uv pip install git+https://github.com/vindicta-platform/WARScribe-Parser.git
```

Or clone and install locally:

```bash
git clone https://github.com/vindicta-platform/WARScribe-Parser.git
cd WARScribe-Parser
uv pip install -e .
```

## Quick Start

```python
from warscribe_parser import Parser, ValidationError

parser = Parser()

try:
    army = parser.parse_file("mylist.warscribe")
    print(f"Army: {army.name}")
    print(f"Points: {army.total_points}")
except ValidationError as e:
    print(f"Invalid list: {e}")
```

## Related Repositories

| Repository | Relationship |
|------------|-------------|
| [WARScribe-CLI](https://github.com/vindicta-platform/WARScribe-CLI) | CLI consumer |
| [Battle-Transcript-Toolkit](https://github.com/vindicta-platform/Battle-Transcript-Toolkit) | Transcript parsing |

## Platform Documentation

> **📌 Important:** All cross-cutting decisions, feature proposals, and platform-wide architecture documentation live in [**Platform-Docs**](https://github.com/vindicta-platform/Platform-Docs).
>
> Any decision affecting multiple repos **must** be recorded there before implementation.

- 📋 [Feature Proposals](https://github.com/vindicta-platform/Platform-Docs/tree/main/docs/proposals)
- 🏗️ [Architecture Decisions](https://github.com/vindicta-platform/Platform-Docs/tree/main/docs)
- 📖 [Contributing Guide](https://github.com/vindicta-platform/Platform-Docs/blob/main/CONTRIBUTING.md)

## License

MIT License - See [LICENSE](./LICENSE) for details.
