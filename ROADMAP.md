# WARScribe-Parser Roadmap

> **Vision**: Multimodal input layer for video, audio, and roster ingestion  
> **Status**: Active Development  
> **Last Updated**: 2026-02-03

---

## v1.0 Target: April 2026

### Mission Statement
Deliver a production-ready parser that accepts multiple input formats (roster files, audio, video, TTS logs) and normalizes them into structured WARScribe-Core compatible intermediate representations.

---

## Milestone Timeline

```
┌─────────────────────────────────────────────────────────────────┐
│  Feb 2026          Mar 2026          Apr 2026                   │
│  ─────────────────────────────────────────────────────────────  │
│  [v0.1.0]          [v0.2.0]          [v0.3.0]      [v1.0.0]     │
│  Roster Files      Audio Support     Video/TTS     Production   │
│                                                                  │
│  Week 2-3          Week 4-5          Week 6-7      Week 8       │
└─────────────────────────────────────────────────────────────────┘
```

---

## v0.1.0 — Roster File Parsing (Target: Feb 17, 2026)

### Deliverables
- [ ] BattleScribe XML parser
- [ ] WARScribe JSON parser
- [ ] ROS format parser
- [ ] Format auto-detection
- [ ] Validation error messages
- [ ] Unit extraction and normalization

### Key Measurable Results
| Metric | Target | Measurement |
|--------|--------|-------------|
| **Format Support** | 3 roster formats | Parser tests |
| **Parse Accuracy** | 100% valid files parse | Test suite |
| **Error Quality** | Actionable error messages | Manual review |

### Exit Criteria
- [ ] Parse BattleScribe exports successfully
- [ ] Parse WARScribe JSON format
- [ ] Clear error messages for malformed input

---

## v0.2.0 — Audio Transcription (Target: Mar 3, 2026)

### Deliverables
- [ ] Whisper API integration
- [ ] Local Whisper model support (small)
- [ ] Audio file processing (MP3, WAV, M4A)
- [ ] Timestamped transcript segments
- [ ] Speaker diarization (optional)
- [ ] Agent-Auditor-SDK integration

### Key Measurable Results
| Metric | Target | Measurement |
|--------|--------|-------------|
| **Transcription Accuracy** | 90%+ on clear audio | WER measurement |
| **Processing Speed** | <20 min per hour of audio | Benchmark |
| **40K Vocabulary** | Recognize unit names | Custom test set |

### Exit Criteria
- [ ] Transcribe 1-hour game audio
- [ ] Timestamped segments available
- [ ] Quota-aware processing via Agent-Auditor

---

## v0.3.0 — Video & TTS Support (Target: Mar 17, 2026)

### Deliverables
- [ ] Video to audio extraction (FFmpeg)
- [ ] YouTube/Twitch URL support
- [ ] Tabletop Simulator log parser
- [ ] Discord log parser
- [ ] Stream capture (basic)

### Key Measurable Results
| Metric | Target | Measurement |
|--------|--------|-------------|
| **Video Formats** | MP4, WebM, MOV | Format tests |
| **TTS Log Parsing** | 95%+ action extraction | Test logs |
| **URL Support** | YouTube, Twitch | Integration test |

### Exit Criteria
- [ ] Process YouTube video URL
- [ ] Parse TTS game logs
- [ ] Extract audio from video files

---

## v1.0.0 — Production Release (Target: Apr 21, 2026)

### Deliverables
- [ ] Performance optimization
- [ ] Batch processing support
- [ ] PyPI publication
- [ ] CLI tool for local use
- [ ] Comprehensive documentation

### Key Measurable Results
| Metric | Target | Measurement |
|--------|--------|-------------|
| **Test Coverage** | >85% | pytest-cov |
| **Processing Reliability** | 99%+ success on valid input | Error rates |
| **PyPI Downloads** | 50+/month | PyPI stats |
| **Documentation** | All inputs documented | Doc review |

### Exit Criteria
- [ ] No critical bugs for 2 weeks
- [ ] CLI usable for local transcription
- [ ] Published to PyPI

---

## Supported Input Formats

| Input Type | Format | Parser | Status |
|------------|--------|--------|--------|
| **Roster** | BattleScribe XML | XMLParser | v0.1 |
| **Roster** | WARScribe JSON | JSONParser | v0.1 |
| **Roster** | ROS format | ROSParser | v0.1 |
| **Audio** | MP3, WAV, M4A | WhisperTranscriber | v0.2 |
| **Video** | MP4, WebM | FFmpeg + Whisper | v0.3 |
| **Text** | Discord logs | TextNormalizer | v0.3 |
| **Game Logs** | TTS logs | TTSLogParser | v0.3 |
| **Stream** | YouTube, Twitch | StreamCapture | v0.3 |

---

## Dependencies

| Dependency | Status | Notes |
|------------|--------|-------|
| WARScribe-Core | 🔄 Parallel | Output format |
| Agent-Auditor-SDK | 🔄 Parallel | Whisper quota |
| Whisper | ✅ Available | Speech-to-text |
| FFmpeg | ✅ Available | Audio extraction |
| lxml | ✅ Available | XML parsing |

---

## Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Whisper accuracy varies | Medium | Medium | Human review queue |
| 40K jargon misheard | High | Medium | Custom vocabulary |
| Long videos expensive | Medium | Medium | Agent-Auditor quota |
| TTS log format changes | Low | Medium | Version detection |

---

## Success Criteria for v1

1. **Coverage**: Support roster, audio, video, and TTS inputs
2. **Accuracy**: 90%+ transcription accuracy on clear audio
3. **Performance**: Process 1-hour video in <30 minutes
4. **Integration**: Outputs consumed by Battle-Transcript-Toolkit

---

*Maintained by: Vindicta Platform Team*
