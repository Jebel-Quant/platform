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

The analogy breaks down in a second way too. Anyone who has worked in a modern car factory knows that no serious manufacturer separates quality into a final inspection stage at the end of the line. Quality is an integrated function, present at every step — built into the process, not bolted on afterwards. The software equivalent is no different: correctness, performance, and operational robustness cannot be retrofitted by a downstream team. They have to be present from the start, which means researchers and engineers must work together from the start.

Rather than separating researchers and developers in space and time — researchers upstream, engineers downstream, a wall between them — we believe in a checkerboard structure. Researchers and developers sit together, alternate, and collaborate continuously. A researcher working on a new signal works directly alongside the engineer responsible for the infrastructure that will run it. Knowledge flows in both directions: researchers gain an understanding of production constraints; engineers gain an understanding of the mathematical intent. The result is code that is both correct and deployable from the start, and a team that shares a common language.

In practice, the distinction between researcher and developer is often blurry — and we think that is a feature, not a problem. The modern developer on this platform sits with researchers, understands their models, and contributes to the research process. The modern researcher writes production-quality code, understands the systems their strategies run on, and takes responsibility for what they ship. We assume that most researchers on the team have strong development skills, and that most developers have the quantitative depth to engage seriously with the research. The checkerboard only works if the pieces can speak to each other.
