---
name: genpark-personal-agent-pupil-light-reflex-pupillometry-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating quantitative pupillary light reflex (PLR), autonomic constriction kinetics, and neural fatigue.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Quantitative Pupillary Light Reflex (PLR) Skill

A sovereign personal agent capability for assessing central nervous system alertness, parasympathetic cholinergic oculomotor reactivity, and autonomic sympathetic balance through deterministic pupillometry metrics.

## Core Capabilities
- **Constriction Kinetics**: Measures constriction latency, constriction amplitude, and maximum constriction velocity (MCV).
- **Autonomic Velocity Ratio**: Analyzes the balance between parasympathetic constriction and sympathetic redilation.
- **Pupillomotor Resilience Score**: 0-100 index quantifying cognitive alertness and visual-neurological fatigue.
- **Ergonomic Environmental Tuning**: Suggests display brightness adjustments, blue-light moderation, and ocular breaks.

## Fast Invocation
```python
from client import PupilLightReflexClient

client = PupilLightReflexClient()
res = client.evaluate_pupillary_dynamics(
    baseline_diameter_mm=4.3,
    minimum_diameter_mm=2.6,
    constriction_latency_ms=225.0,
    constriction_velocity_mm_s=4.9,
    redilation_velocity_mm_s=1.85
)
print("Constriction Amplitude:", res["constriction_amplitude_mm"], "mm")
print("Pupillomotor Score:", res["pupillomotor_resilience_score"])
```
