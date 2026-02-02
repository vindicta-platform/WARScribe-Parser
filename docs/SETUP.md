# Setup Guide

## Prerequisites
- Python 3.10+
- uv

## Development Setup
```bash
git clone https://github.com/vindicta-platform/WARScribe-Parser.git
cd WARScribe-Parser
uv venv
uv pip install -e ".[dev]"
```

## Running Tests
```powershell
pytest tests/ -v
```
