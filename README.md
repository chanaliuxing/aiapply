# apply-copilot

Minimal scaffold of the **apply-copilot** project. It contains a FastAPI backend
and placeholders for a Chrome extension, local companion and mock ATS pages.

## Prerequisites

- Python 3.11
- Node 20
- Google Chrome
- Tesseract OCR

Copy `.env.example` to `.env` and adjust as needed.

## Quickstart

```bash
make up      # start services (placeholder)
make test    # run unit tests
make e2e     # run e2e tests (skipped)
```

## Checklist for local run

```
make up
make dev-companion
make e2e
load extension dist into Chrome, open /mock-ats/greenhouse, open side panel, click Analyze→Fill→(Auto-Submit)
```

✅ READY: run make up && make e2e
