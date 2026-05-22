# A Technology Vision for Quantitative Trading

*Thomas Schmelzer — May 2026*

*These are my personal views on how a quantitative trading platform should be built. I have spent two decades working across systematic hedge funds, high-frequency trading, family offices and sovereign wealth funds. The practices I describe in the early sections were perfectly reasonable at the time. Technology has moved on, and I think the way we build and run these platforms should move on too.*

---

## Executive Summary

For most of its history, quantitative trading has been organised around a handover. Researchers developed strategies in MATLAB or Python; engineers reimplemented everything in C++. Knowledge fragmented across personal scripts. New hires rebuilt the same basic tools from scratch. When modern machine learning arrived, the C++ mandate became impossible to sustain. No team can reimplement PyTorch.

This platform is built on a different premise. Research and production share the same environment. The container a researcher uses to develop a strategy is the same one that runs live. Moving between environments is a matter of changing configuration files, not rewriting code. A clean interface to the prime broker means the strategy works the same way whether it is talking to a simulator or a live venue.

The team is not divided into researchers and developers. It works more like a professional kitchen: collaborative, with quality as a shared responsibility at every step. Common tools for data access, portfolio construction, performance analytics and live monitoring are built once and shared. Rhiza keeps project scaffolding consistent across all strategy repositories so infrastructure drift never becomes a distraction. The platform exists so the team can focus on the one thing that cannot be bought off the shelf: the edge.

---

## The Old Approach

For most of the industry's history, quantitative research followed a familiar pattern. A small group of researchers, typically mathematicians, physicists and statisticians, would develop trading strategies in MATLAB or Python. These environments suited the work well: easy to iterate on, rich in numerical libraries and close to the mathematical notation of the models. A researcher could move from an idea to a backtest in a matter of days.

The outputs were scripts: dense, clever and personal. Variable names made sense to their authors. Logic accumulated in layers over months or years. The code worked, and it carried real insight about markets.

## Reinventing the Wheel

Because research lived in personal scripts, knowledge did not accumulate. Each researcher wrote their own version of the same basic components: moving averages, momentum signals, mean-reversion filters, portfolio construction routines. There was no shared library, no common vocabulary in code. Two researchers on the same team might implement the same idea with different conventions, different edge case handling, different numerical choices. When results diverged, it was hard to know why.

This also made it difficult to build on what had come before. Onboarding a new researcher often meant starting from scratch. Institutional knowledge lived in people rather than in code, and walked out the door when those people moved on.

## The Handover Problem

When a strategy was ready for production, it was passed to a team of software engineers to reimplement in C++. The rationale made sense: C++ offered the performance, determinism and operational robustness that live trading required. But the process was expensive.

The handover was rarely clean. A MATLAB matrix operation that fit on one line might require careful memory management and numerical precision decisions in C++. Edge cases the script handled implicitly had to be made explicit. Bugs crept in during reimplementation and were hard to catch because the reference and production implementations diverged the moment the handover began.

The result was a slow pipeline. Research cycles were constrained by engineering capacity. Months could pass between an idea and a live strategy. Every change to a live strategy risked restarting the process.

Modern machine learning made this untenable. Libraries like PyTorch represent millions of engineering hours: automatic differentiation, GPU kernels, distributed training, a vast ecosystem of pretrained models. Reimplementing any meaningful fraction of that in C++ is not a project; it is a decade-long programme. Teams that held to the C++ mandate found themselves unable to use these tools, and fell behind those that did.

## A New Direction

This platform is built around a single environment for both research and production. Researchers express ideas in high-level terms and the platform carries them through to execution without a translation step.

The old handover model borrowed, implicitly, from the assembly line: one group does its work and passes the output down the line. It is an appealing image, but it does not fit knowledge work. Assembly lines function because the interfaces between stations are fixed and fully specified in advance. In research and engineering, the interface is exactly what is hardest to define, and it changes as understanding develops. Treating it like a fixed handoff creates the appearance of process while undermining the collaboration that actually gets things done.

A more useful image is the professional kitchen. Most of us have spent time in one, or at least observed one closely. A kitchen is not sequential. Every station is visible to every other. The head chef and the junior cook share the same space and the same pressure. Quality is not inspected at the end; it is everyone's responsibility throughout. No serious dish leaves a kitchen having passed through one pair of hands with no awareness of what came before or after.

A quant fund should work the same way. Researchers and developers in the same room, aware of each other's constraints, catching problems early. Quality is not a downstream function.

The kitchen analogy has a further implication. A chef is not expected to build the oven or construct the fridge. A professional kitchen assumes a working environment: reliable equipment, the right tools available. Asking a chef to fabricate their own appliances would produce worse food and worse appliances. The same applies here. Researchers and developers should not be building basic infrastructure from scratch: data pipelines, execution connectors, backtesting engines, monitoring tooling. That is what the platform provides. The team's energy belongs on the signals, the models, the risk framework. Everything else is the oven, and it should just work.

We organise the team in what we call a checkerboard structure rather than separating researchers and developers upstream and downstream. They sit together, alternate and collaborate continuously. A researcher working on a new signal works alongside the engineer responsible for the infrastructure that will run it. Knowledge moves in both directions. The result is code that is correct and deployable from the start.

In practice the boundary between researcher and developer is often blurry, and we think that is a good thing. The modern developer on this platform understands the models and contributes to the research process. The modern researcher writes production-quality code and takes responsibility for what they ship. We assume most researchers have strong development skills, and most developers have enough quantitative depth to engage seriously with the research.

## Containerization

Containerization is one of the most important practical tools for closing the gap between research and production. A container packages not just code but the entire runtime environment: the operating system libraries, the language version, the dependencies, the configuration. The environment is then identical on a researcher's laptop, in the backtesting cluster and in live production. The familiar complaint, "it works on my machine," loses its meaning because every machine runs the same machine.

For a quantitative trading platform this matters a great deal. A backtest that silently produces different results in research and production, because of a library version mismatch or a difference in numerical defaults, is worse than no backtest at all. It creates false confidence. Containers make the environment a versioned, reproducible artifact in the same way code is. A strategy and the environment it runs in are deployed together, tested together and promoted through stages together.

In practical terms, containers deliver a standardised, fully equipped kitchen to every member of the team. A researcher starting work on a new idea does not spend their first day installing dependencies and debugging environment issues. They open the container and start.

## Building the Kitchen

Building the platform means deciding what belongs in every kitchen regardless of what is being cooked. Several components are non-negotiable.

**Data API.** Access to clean, reliable data is the foundation. Every strategy, every backtest, every risk calculation depends on it. A well-designed data API handles the complexity of sourcing, normalising and versioning data across providers and asset classes so researchers can ask for what they need without worrying about how to fetch it. Getting this layer right is what everything else is built on.

**Common strategy tooling.** Many of the building blocks of quantitative strategies are not proprietary. Portfolio construction, signal combination, position sizing, transaction cost modelling are shared across the industry and across the team. They should be implemented once, tested thoroughly and available to everyone. A researcher building a new strategy should not be reimplementing a portfolio optimiser or a signal blending framework from scratch.

**Performance analytics.** Understanding why a strategy performed the way it did matters as much as the performance itself. A standard set of analytics, covering returns decomposition, drawdown analysis, factor attribution and cost accounting, means every strategy can be evaluated consistently. Results are comparable across strategies and over time rather than each researcher maintaining their own metrics.

**Live monitoring.** A strategy in production requires continuous observation: position and exposure tracking, P&L attribution, signal behaviour, execution quality and alerting when something moves outside expected bounds. Problems should be visible before they become costly.

One principle applies across all of this. The kitchen must be built with researchers, not just for them. A platform designed only by engineers, however capable, risks solving the wrong problems. Researchers know what data they actually need, how they think about portfolio construction, what a useful performance report looks like and what slows their work down. That knowledge needs to be in the room when the platform is being built.

## Building the Strategies

With the kitchen in place, strategies can be built in earnest. Each strategy lives in its own repository, but left unmanaged a collection of strategy repos quickly becomes a zoo. CI workflows diverge. Python versions drift. Linting configs split. A security fix lands in one repo and is missed by the rest. The same fragmentation that plagued the old world of personal scripts reappears at the infrastructure level.

[Rhiza](https://github.com/Jebel-Quant/rhiza-education) addresses this directly. Rather than generating project scaffolding once and walking away, Rhiza keeps every strategy repository aligned with the platform's canonical standards. When the central template changes, a new CI workflow, an updated linting config, a change to the containerisation setup, Rhiza opens a pull request in each downstream repo with a clear diff of what changed. Owners review, adapt where needed and merge. Nothing is forced and nothing is missed.

This is the infrastructure equivalent of shared strategy tooling. Researchers should not reimplement portfolio construction from scratch, and developers should not be manually maintaining CI pipelines in every repo. Rhiza keeps the scaffolding consistent so the team's attention stays on what is inside it.

## Live Trading

When a strategy goes live, the cost of any discrepancy between research and production becomes real and immediate. A backtest that behaves differently from the live system, because of an environment mismatch or a parameter misconfigured during deployment, can produce losses that no amount of prior testing would have flagged. Closing this gap is a core design requirement, not a convenience.

Proximity is the answer. The container a researcher uses to develop and backtest a strategy is the same container that runs in production. There is no reimplementation, no port, no translation step where something can silently go wrong.

What changes between environments is the configuration, not the code. The container is a fixed, versioned artifact. Configuration files tell it where to find data, which parameters to use, what risk limits to respect and which execution venue to connect to. Moving a strategy from backtesting to paper trading to live means changing the configuration it runs against. The container has no knowledge of which environment it is in. It reads its configuration and runs.

This separation of code from configuration is what makes promotion between environments safe and auditable. Every configuration file is versioned. Every deployment is a known container image combined with a known configuration state. If something goes wrong in production, the team can reconstruct exactly what was running and with what parameters. Rolling back is a configuration change, not an emergency deployment.

**Prime broker connectivity.** A live strategy communicates with the outside world: placing orders, receiving fills, querying positions, reconciling cash and margin with a prime broker. This boundary is among the most consequential in the system. Errors here are not silent; they are immediate and financial.

The platform puts a clean interface in front of prime broker communication. The strategy expresses intent, buy this instrument in this quantity with this urgency, and the execution layer handles the translation into whatever protocol the broker expects, whether FIX or a proprietary API. The strategy does not need to know which broker it is talking to. Switching brokers or adding a new venue is a configuration change.

In backtesting and paper trading the same execution interface is present, backed by a simulated fill engine rather than a live connection. The strategy code is identical across all environments. The broker, like everything else, is a configuration detail.

## Jebel Quant Research

Jebel Quant Research develops the tools and infrastructure that the platform described here is built on. The work spans several areas.

**Project infrastructure.** Rhiza is the first publicly available tool from Jebel Quant Research. It solves the repo zoo problem for Python-heavy organisations by keeping project scaffolding continuously aligned across many repositories through a pull request based sync mechanism. It is already in use beyond Jebel Quant, including at Stanford's CVXGRP and Janus Henderson. Relevant repos: [rhiza](https://github.com/Jebel-Quant/rhiza), [rhiza-cli](https://github.com/Jebel-Quant/rhiza-cli), [rhiza-tools](https://github.com/Jebel-Quant/rhiza-tools), [rhiza-hooks](https://github.com/Jebel-Quant/rhiza-hooks), [rhiza-education](https://github.com/Jebel-Quant/rhiza-education).

**Data access.** A clean, versioned API into market data is foundational to everything else. Jebel Quant Research has developed tooling for sourcing, normalising and serving data across asset classes, with a consistent interface that works identically in research and production.

**Portfolio construction.** Drawing on work developed in collaboration with Stephen Boyd's group at Stanford and informed by co-authored research with Ron Kahn, Jebel Quant Research has built portfolio construction tools grounded in convex optimisation. These cover mean-variance optimisation, transaction cost aware rebalancing and risk-constrained allocation. Relevant repos: [linalg](https://github.com/Jebel-Quant/linalg), [basanos](https://github.com/Jebel-Quant/basanos).

**Signal combination and performance analytics.** Tools for combining signals from multiple sources, evaluating strategy performance consistently and attributing returns across factors and time periods. The goal is a shared analytical vocabulary across the team rather than each researcher maintaining their own metrics. Relevant repos: [jquantstats](https://github.com/Jebel-Quant/jquantstats).

**Live trading infrastructure.** The container-based deployment model, configuration management framework and prime broker connectivity layer described in this document are products of Jebel Quant Research. They are designed to be reusable across strategies and, where appropriate, across organisations.