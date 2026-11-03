# Quantitative Pupillary Light Reflex (PLR) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive calculation of Pupillary Light Reflex (PLR) dynamics, autonomic tone, and central nervous system alertness.

```mermaid
flowchart TD
    PupilCam["Infrared Pupillometry / Optical Sensor"] --> Dynamics["Pupil Diameter Tracking Over Time"]
    Dynamics --> Extraction["Kinetic Metric Extraction (Latency, MCV, %CA, RDV)"]
    Extraction --> ScoreEngine["Autonomic Pupillary Resilience Engine"]
    ScoreEngine --> Agent["OpenClaw / Hermes Personal Agent Actions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Pupillometric Standard Metrics**: Implements validated equations for constriction velocity, amplitude percentage, and redilation rate.
- **Autonomic Tone Assessment**: Quantifies balance between cholinergic parasympathetic and adrenergic sympathetic branches.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import PupilLightReflexClient

client = PupilLightReflexClient()
result = client.evaluate_pupillary_dynamics(
    baseline_diameter_mm=4.3,
    minimum_diameter_mm=2.6,
    constriction_latency_ms=225.0,
    constriction_velocity_mm_s=4.9,
    redilation_velocity_mm_s=1.85
)
print("Constriction Amplitude:", result["constriction_amplitude_mm"], "mm")
print("Classification:", result["classification"])
```

## License
Apache-2.0
