# History

## The Old Approach

For much of the industry's history, quantitative research followed a well-worn pattern. A small group of researchers — mathematicians, physicists, and statisticians — would develop trading strategies in MATLAB or Python. These scripting environments were well suited to rapid experimentation: easy to iterate on, rich in numerical libraries, and close to the mathematical notation of the underlying models. A researcher could move from idea to backtest in days.

The artifacts of this process were scripts: dense, clever, and often deeply personal. Variable names made sense to their authors. Logic accumulated in layers over months or years. The code worked, and it embodied hard-won insight about markets.

## Reinventing the Wheel

A second, quieter problem ran alongside the first. Because research lived in personal scripts, knowledge did not accumulate. Each researcher built their own implementation of the same basic strategies — moving averages, momentum signals, mean-reversion filters, portfolio construction routines. There was no shared library, no common vocabulary in code. Two researchers in the same team might independently implement the same idea with subtly different conventions, different handling of edge cases, different numerical choices. When results diverged, nobody could easily tell why.

This fragmentation also made it hard to build on prior work. Onboarding a new researcher meant starting from scratch rather than standing on the shoulders of what had come before. Institutional knowledge lived in people, not in code, and left with them when they moved on.

## The Handover Problem

When a strategy was deemed ready for production, it was handed to a team of software engineers tasked with reimplementing it in C++. The rationale was sound — C++ offered the performance, determinism, and operational robustness that live trading demanded. But the process was costly.

The handover was rarely clean. Researchers and engineers spoke different languages, literally and figuratively. A MATLAB matrix operation that fit on one line might require careful memory management and numerical precision choices in C++. Edge cases that the script handled implicitly had to be made explicit. Bugs introduced during reimplementation were hard to catch because the reference implementation and the production implementation diverged the moment the handover began.

The result was a slow, error-prone pipeline. Research cycles were bottlenecked by engineering capacity. The gap between idea and live strategy was measured in months. And every change to a live strategy — a parameter tweak, a new signal, a risk adjustment — risked restarting the handover process from scratch.

The problem became irreversible with the rise of modern machine learning. Libraries like PyTorch represent millions of engineering hours: automatic differentiation, GPU kernels, distributed training, a vast ecosystem of pretrained models and community tooling. Reimplementing any meaningful fraction of that in C++ is not a project — it is a decade-long research programme. Teams that insisted on the C++ production mandate simply could not use these tools, and fell behind those that did.

## A New Direction

This platform was built to close that gap. The goal is a single, unified environment where research and production are not separate stages with a handover in between, but a continuous spectrum. Researchers express ideas in high-level terms; the platform carries those ideas through to execution without a lossy translation step.

The researcher-to-developer handover implicitly borrowed the metaphor of an assembly line: one group adds their component and passes it down the line to the next. It is a tempting analogy, but a mistaken one. Assembly lines work for physical objects with stable, fully specified interfaces. Knowledge work is different — the interface between research and engineering is precisely what is hardest to specify, and it changes as understanding deepens. Applying an assembly line model to knowledge work creates the illusion of process while destroying the collaboration that actually produces results.

A better image — and one most of us have actually seen from the inside — is a modern restaurant kitchen. A professional kitchen is not an assembly line. It is a high-pressure, collaborative environment where every station is visible to every other, where the head chef and the junior cook share the same space and the same urgency, and where quality is not checked at the pass but maintained continuously by everyone. No dish leaves a serious kitchen having been touched only by one pair of hands and then handed blindly to the next. Everyone knows what the others are doing, because they have to.

A solid quant fund should look like that kitchen. Researchers and developers working in the same room, aware of each other's constraints, catching each other's mistakes in real time. Quality is not a downstream function — it is the shared responsibility of the whole team, present at every step.

The analogy carries one further implication. A chef is not expected to build the oven, construct the fridge, or wire the extraction system. A professional kitchen assumes an environment — reliable equipment, a working supply chain, the right tools at hand. The chef's job is to cook, and the kitchen's job is to make that possible. Asking a chef to fabricate their own appliances would be absurd; the result would be worse food and worse appliances.

The same applies here. Researchers and developers on this platform should not be spending their time constructing basic infrastructure from scratch — data pipelines, execution connectors, backtesting engines, monitoring tooling. This platform exists to provide that environment. The team's energy belongs on the problems that are unique to this fund: the signals, the models, the risk framework, the edge. Everything else is the oven. It should just work.

Rather than separating researchers and developers in space and time — researchers upstream, engineers downstream, a wall between them — we believe in a checkerboard structure. Researchers and developers sit together, alternate, and collaborate continuously. A researcher working on a new signal works directly alongside the engineer responsible for the infrastructure that will run it. Knowledge flows in both directions: researchers gain an understanding of production constraints; engineers gain an understanding of the mathematical intent. The result is code that is both correct and deployable from the start, and a team that shares a common language.

In practice, the distinction between researcher and developer is often blurry — and we think that is a feature, not a problem. The modern developer on this platform sits with researchers, understands their models, and contributes to the research process. The modern researcher writes production-quality code, understands the systems their strategies run on, and takes responsibility for what they ship. We assume that most researchers on the team have strong development skills, and that most developers have the quantitative depth to engage seriously with the research. The checkerboard only works if the pieces can speak to each other.

## Containerization

One of the most practical answers to the environment problem is containerization. A container packages not just code but its entire runtime environment — the operating system libraries, the language version, the dependencies, the configuration. The result is an environment that is identical on a researcher's laptop, in the backtesting cluster, and in live production. The classic complaint — "it works on my machine" — ceases to be meaningful, because every machine runs the same machine.

For a quantitative trading platform this matters enormously. A backtest that silently produces different results in research and production, due to a library version mismatch or a difference in numerical defaults, is worse than no backtest at all — it creates false confidence. Containers make the environment a first-class, versioned, reproducible artifact, the same way code is. A strategy and the environment it runs in are deployed together, tested together, and promoted through stages together.

Containers also make the kitchen analogy concrete. The platform delivers a fully equipped, standardised kitchen to every member of the team. A researcher starting on a new idea does not spend their first day installing dependencies and debugging environment issues. They open the container and start cooking.

## Building the Kitchen

If the platform is the kitchen, then building it means deciding what equipment belongs in every kitchen, regardless of what is being cooked. Several components are non-negotiable.

**Data API.** The most critical piece of infrastructure is clean, reliable access to data. Every strategy, every backtest, every risk calculation depends on it. A well-designed data API abstracts away the complexity of sourcing, normalising, and versioning data across multiple providers and asset classes. Researchers should be able to express a data query in terms of what they need, not how to fetch it. Getting this layer right is the foundation everything else is built on.

**Common strategy tooling.** Many of the building blocks of quantitative strategies are not proprietary — they are shared across the industry and across the team. Portfolio construction, signal combination, position sizing, transaction cost modelling: these should be implemented once, tested thoroughly, and made available to everyone. A researcher building a new strategy should not be reimplementing a Markowitz optimiser or a signal blending framework from scratch. The platform provides these as first-class, shared components.

**Performance analytics.** Understanding why a strategy performed the way it did is as important as the performance itself. The platform provides a standard set of analytics — returns decomposition, drawdown analysis, factor attribution, turnover and cost accounting — that every strategy can be evaluated against. A common analytics layer also means results are comparable across strategies and across time, rather than each researcher rolling their own metrics.

**Live monitoring.** A strategy in production is not finished — it is under continuous observation. The platform provides tooling for monitoring live strategies in real time: position and exposure tracking, P&L attribution, signal behaviour, execution quality, and alerting when something drifts outside expected bounds. The goal is that problems are visible before they become costly, and that the team spends their time understanding the market, not debugging infrastructure.

One principle cuts across all of this: the kitchen must be built with researchers, not just for them. A platform designed solely by engineers, however well-intentioned, risks solving the wrong problems — optimising for technical elegance while missing the daily friction that slows research down. Researchers know what data they actually need, how they think about portfolio construction, what a useful performance report looks like, and what breaks their workflow. That knowledge has to be present in the room when the platform is being built. The checkerboard applies here too: the platform is itself a research product, and it should be developed the same way.
