# SysBridge

SysBridge is a local-first, policy-governed OS control layer designed
to safely translate structured intents into real system actions.

## Motivation
Why giving LLMs direct OS access is dangerous.
Why confirmation, sandboxing, and explainability matter.

## Architecture Overview
Intent → Action → Policy → Executor → Result

## Core Concepts
- Actions
- Policy Guards
- Execution
- Dry Run & Confirmation
- Journaling & Logging

## Safety Model
- Filesystem sandbox
- Risk levels
- Human-in-the-loop confirmation

## Current Capabilities
- Filesystem listing (scoped)
- File / folder opening
- Application launching
- System information (time, battery)

## Non-Goals
- Autonomous agents
- Arbitrary shell execution
- Networked side effects
