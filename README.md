# Creative Intent → Production-Safe Visual Generation (FIBO Hackathon)

## Overview
This project demonstrates an agentic, JSON-native workflow that translates messy human creative intent into production-safe, deterministic visual generation parameters using Bria FIBO.

Instead of relying on prompt engineering, the system introduces an intelligent agent layer that:
- Asks clarifying questions
- Resolves ambiguity and production risks
- Outputs structured, repeatable JSON ready for image generation

This mirrors real-world creative and production workflows inside enterprise agencies.

---

## Problem
Creative briefs are often:
- Intentionally abstract
- Strategically rich but operationally messy
- Filled with contradictions, budget constraints, and legal sensitivities

These briefs are difficult to translate directly into AI generation without risk, inconsistency, or rework.

---

## Solution
An agent-driven workflow that separates:
1. **Human Intent** (creative direction)
2. **Production Constraints** (safety, scalability, legality)
3. **Execution Parameters** (camera, lighting, color, composition)

The output is a deterministic JSON schema designed to be directly compatible with Bria FIBO’s professional controls.

---

## How It Works
1. A messy creative brief is ingested
2. The agent asks clarifying questions
3. Human responses are captured in an intent layer
4. Production risks are detected and resolved
5. A FIBO-ready JSON object is generated
6. The JSON drives a (mocked) image generation step

---

## Key Features
- JSON-native visual control
- Agentic clarification workflow
- Production safety & constraint resolution
- Enterprise-ready, scalable design
- Drop-in compatibility with Bria FIBO

---

## Files
- `agent.py` — Creative intent agent & JSON generator
- `fibo_runner.py` — Mock FIBO generation step
- `fibo_output_*.txt` — Example generation artifacts

---

## Hackathon Category
**Best JSON-Native or Agentic Workflow**

This project showcases how structured AI workflows can replace fragile prompt engineering in professional creative production.

---

## Future Work
- Replace mock generation with live Bria FIBO API or local model
- Expand safety rules for regulatory-specific industries
- Add UI for non-technical creative teams
