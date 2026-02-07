# SysBridge — Design Rationale

This document explains the architectural decisions behind SysBridge. The goal is not to describe *what the code does*, but *why it is structured this way*.

SysBridge is intentionally conservative. It is designed to be a safe, inspectable bridge between high-level intent (e.g., from an LLM) and low-level OS side effects.

---

## Core Design Principle

**No component is allowed to both decide *and* execute.**

Decision-making, safety checks, and side effects are strictly separated. This keeps the system auditable, testable, and extensible without increasing risk.

---

## 1. Declarative Actions (Data Before Execution)

Actions in SysBridge are *declarative objects*, not executable commands.

An Action:

* Describes **what** is intended
* Contains **parameters** only
* Has **no side effects** by itself

Example intent (conceptually):

> "List the contents of this directory"

This intent becomes an Action object that can be:

* Inspected
* Validated
* Rejected
* Logged
* Explained to a human

Only after passing all checks does it reach execution.

**Why this matters**:

* Prevents accidental execution during parsing or validation
* Allows dry-runs and previews
* Makes actions serializable and explainable
* Keeps LLM output harmless by default

---

## 2. Single Execution Choke Point

All real system side effects happen in exactly one place: the **ActionExecutor**.

The executor:

* Receives validated actions
* Enforces confirmation rules
* Performs the real OS interaction
* Returns a structured result

No Action is allowed to touch the OS directly.

**Why this matters**:

* Easy to audit what can affect the system
* One place to add logging, tracing, or rate limiting
* Prevents privilege creep across the codebase

---

## 3. PolicyGuard as a First-Class Layer

Policy enforcement is handled by a dedicated **PolicyGuard**, not by individual actions.

Responsibilities:

* Path sandboxing
* Risk-level enforcement
* Deny/allow decisions
* Parameter validation

Policies are **explicit and centralized**.

**Why this matters**:

* Changing safety rules does not require rewriting actions
* Makes the safety model visible and reviewable
* Enables future policy backends (time-based, role-based, etc.)

---

## 4. Human-in-the-Loop Confirmation

Some actions are inherently risky (e.g., launching apps, modifying files).

SysBridge models this explicitly:

* Each action declares a `risk_level`
* Medium or high risk actions require confirmation
* Confirmation happens *before* execution

This is not a UI feature — it is part of the execution contract.

**Why this matters**:

* Preserves human authority
* Prevents silent escalation of autonomy
* Makes the system usable in real environments

---

## 5. Filesystem Sandboxing via Allowed Roots

Filesystem access is restricted to predefined root directories.

Design choice:

* Use **path-based sandboxing** instead of pattern matching or heuristics

Rules:

* All paths are resolved absolutely
* All access must remain inside allowed roots
* Escapes (e.g., `..`) are rejected

**Why this matters**:

* Deterministic safety guarantees
* Simple mental model
* Resistant to prompt injection or malformed paths

---

## 6. Explicit Action Results

Every execution returns a structured `ActionResult`.

An ActionResult includes:

* Status (executed / denied / failed)
* Result payload (if any)
* Preview or explanation

Results are objects, not strings.

**Why this matters**:

* Enables downstream reasoning
* Supports UI, logging, and testing
* Makes failures informative instead of silent

---

## 7. Non-Goals (Intentional Omissions)

SysBridge deliberately does **not** support:

* Arbitrary shell execution
* Autonomous decision loops
* Network-side effects
* Self-modifying behavior

These are excluded to keep the system:

* Predictable
* Reviewable
* Safe to run locally

---

## Summary

SysBridge is designed as a *trust boundary*.

It assumes:

* Inputs may be untrusted
* Actions may be dangerous
* Humans remain in control

By enforcing strict separation between intent, policy, and execution, SysBridge provides a solid foundation for building higher-level AI systems without sacrificing safety or clarity.
