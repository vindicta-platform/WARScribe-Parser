# WARScribe-Parser Constraints

> Critical rules agents MUST follow when modifying this repository.

## ⛔ Hard Constraints

1. **Output to WARScribe-Core** - All output must be valid WARScribe notation
2. **Async Processing** - All I/O bound operations async
3. **Fail Gracefully** - Partial extraction better than failure
4. **No PII Retention** - Audio/video deleted after processing

## 📥 Input Rules

### Supported Formats
```python
SUPPORTED = {
    "roster": [".ros", ".rosz", ".xml"],
    "image": [".jpg", ".jpeg", ".png", ".webp"],
    "audio": [".mp3", ".wav", ".m4a", ".ogg"],
    "video": [".mp4", ".mov", ".webm"],
}
```

### Size Limits
- Image: 10MB max
- Audio: 30 minutes max
- Video: 10 minutes max
- Roster: 5MB max

## 🔍 Extraction Rules

### Confidence Thresholds
- OCR: 0.8 minimum confidence
- STT: 0.7 minimum confidence
- NLP extraction: 0.75 minimum

### Fallback Behavior
1. Try primary extractor
2. On failure, try fallback
3. On complete failure, return partial with warnings

## 🔒 Security Rules

- Sanitize all input filenames
- Temporary files in isolated directory
- No execution of extracted content

## 🧪 Testing Requirements

Before merging:
- [ ] `pytest` passes
- [ ] Test fixtures for each input type
- [ ] Confidence threshold tests
- [ ] Memory usage profiled for large inputs
