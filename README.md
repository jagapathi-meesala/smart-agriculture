# Smart Agriculture Agent

A production-quality independent agent for farmer decision support, analyzing soil, weather, crop suitability, and disease risks to provide actionable recommendations.

## Features
- **Deterministic Tool Logic**: Uses verifiable logic for agronomy decisions.
- **Explainable Recommendations**: Clear, actionable advice.
- **Strict Contracts**: Pydantic validated I/O for all domain tools.
- **OpenGAP v0.1.0 Ready**: Includes `agent.yaml`, `RULES.md`, `SOUL.md`, and MCP-compatible `tools/*.yaml` definitions.

## Installation

```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env with any necessary API keys (Open-Meteo is used by default and doesn't require a key, but is supported).
```

## Running the CLI

```bash
export PYTHONPATH=src
python src/smart_agri_agent/adapters/cli.py
```

## Testing

```bash
export PYTHONPATH=src
pytest tests/
```
