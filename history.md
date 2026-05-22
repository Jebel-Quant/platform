# History

## The Old Approach

For much of the industry's history, quantitative research followed a well-worn pattern. A small group of researchers — mathematicians, physicists, and statisticians — would develop trading strategies in MATLAB or Python. These scripting environments were well suited to rapid experimentation: easy to iterate on, rich in numerical libraries, and close to the mathematical notation of the underlying models. A researcher could move from idea to backtest in days.

The artifacts of this process were scripts: dense, clever, and often deeply personal. Variable names made sense to their authors. Logic accumulated in layers over months or years. The code worked, and it embodied hard-won insight about markets.

## The Handover Problem

When a strategy was deemed ready for production, it was handed to a team of software engineers tasked with reimplementing it in C++. The rationale was sound — C++ offered the performance, determinism, and operational robustness that live trading demanded. But the process was costly.

The handover was rarely clean. Researchers and engineers spoke different languages, literally and figuratively. A MATLAB matrix operation that fit on one line might require careful memory management and numerical precision choices in C++. Edge cases that the script handled implicitly had to be made explicit. Bugs introduced during reimplementation were hard to catch because the reference implementation and the production implementation diverged the moment the handover began.

The result was a slow, error-prone pipeline. Research cycles were bottlenecked by engineering capacity. The gap between idea and live strategy was measured in months. And every change to a live strategy — a parameter tweak, a new signal, a risk adjustment — risked restarting the handover process from scratch.

## A New Direction

This platform was built to close that gap. The goal is a single, unified environment where research and production are not separate stages with a handover in between, but a continuous spectrum. Researchers express ideas in high-level terms; the platform carries those ideas through to execution without a lossy translation step.
