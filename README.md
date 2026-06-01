# Platform — Jebel Quant Research

This repository contains the platform for systematic quantitative trading developed by
[Jebel Quant Research](https://github.com/Jebel-Quant). It provides the shared
infrastructure — data access, portfolio construction, execution, risk management and
repo tooling — that lets a trading team focus on signals and models rather than
rebuilding common components from scratch.

## Vision

The thinking behind the platform is set out in full in the vision document:

**[A Technology Vision for Quantitative Trading (PDF)](https://raw.githubusercontent.com/Jebel-Quant/platform/gh-pages/vision.pdf)**

The document covers the problems with the traditional research-to-production handover,
the case for a shared environment, the kitchen analogy for team structure, and the
role of containerisation, backtesting discipline, risk management and AI in a modern
quant operation.

## Key components

- **Data API** — clean, versioned access to market data across asset classes
- **Portfolio construction** — convex optimisation tools built with Stephen Boyd's group at Stanford
- **Execution layer** — strategy-as-a-service with a standardised API; broker communication handled by the platform
- **Risk management** — pre-trade checks, live monitoring, drawdown limits and kill switch
- **[Rhiza](https://github.com/Jebel-Quant/rhiza)** — keeps all strategy repositories aligned with a common template

## Related repositories

| Repo | Purpose |
|---|---|
| [rhiza](https://github.com/Jebel-Quant/rhiza) | Scaffolding sync engine |
| [rhiza-cli](https://github.com/Jebel-Quant/rhiza-cli) | CLI for Rhiza |
| [linalg](https://github.com/Jebel-Quant/linalg) | Linear algebra utilities |
| [basanos](https://github.com/Jebel-Quant/basanos) | Portfolio construction |
| [jquantstats](https://github.com/Jebel-Quant/jquantstats) | Performance analytics |
