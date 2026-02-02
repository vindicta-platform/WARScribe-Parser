# WARScribe Parser

**High-level parsing for WARScribe notation.**

Parse transcripts, extract actions, and analyze match data.

## Installation

```bash
uv pip install git+https://github.com/vindicta-platform/WARScribe-Parser.git
```

## Usage

```python
from warscribe_parser import parse_transcript

transcript = parse_transcript("match.transcript")
for action in transcript.actions:
    print(action)
```

MIT License
