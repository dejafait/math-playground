# Actual fixed-pair Fredholm calculation — step431

Target is the exact Next action approved by the pre-existing SPECIALIZE
assessment `literature/2026-11-04-actual-fredholm-fixed-pair-norm-test.md`.
This is a calculation, not a new identity or literature review. The main
gap is actual-Xi all-degree mixed positivity. The intermediate target is
the original operator at (r,R)=(2,1024), with independently paid contour
count and L777 data. A bound below one could pay L776 for this one pair;
wrong count stops the application, lower norm bound at least one stops
its sufficient test, and a crossing interval is inconclusive.

Read complete L018/L021/L776/L777; reused the supplied source comparison
and searched the named step427–429 working notes and shifted-boundary
stop for duplicates/failures. No existing actual norm certificate was
found in those records. Existing notebook changes are preserved. No
cross-notebook input. Mathlib matching coverage remains unchecked.

Implementation checkpoint: system Python has no python-flint or mpmath.
Check a temporary isolated installation before any numerical claim.
Every eventual enclosure must use ball arithmetic; ordinary floating
point cannot pay zero count, multiplicity or the norm threshold.

Installation failed: pip could not resolve pypi.org. Available Python
3.12–3.15 and Xcode Python do not provide flint, mpmath or sympy; no
local flint/arb installation or cached matching wheel was found. This
is an execution dependency failure, not missing theorem coverage.

Bounded fallback within the approved entire-series evaluator scope:
use L017/L018 with x=exp(2u), obtaining
G(w)=[1+(w-1)J(w)]/16, where
J(w)=integral_0^infinity exp(u/2) psi(exp(2u)) cosh(sqrt(w)u/2) du.
Use directed Decimal intervals (finite decimal endpoints), elementary
Taylor/Cauchy errors and the argument principle; no new numerical
library or special-function theorem is needed. Save each quadrature
cell bound and every contour segment. Cap the implementation at one
coefficient build and fixed contour/DFT resolutions, preserving failures.

Completed: one 128-cell degree24 coefficient build, two 512-segment
contour certificates (no subdivision needed), a strict real root bracket,
and a 1024-point interval Fourier calculation with N=192. The resulting
original norm is in (0.84228998371291,0.84228998371298), below one.
Full reasoning and evidence locations are in canonical L778; do not
replace its analytic proof by this working recap. Exact rational saved-
data checks passed for every contour record and finite Gram/norm input.
Analytic implementation remains unaudited. The completed step is a
known-method calculation with a new local enclosure, not a new general
theorem or RH candidate. New independent-audit scope is REVIEW_REQUIRED
for separate approval next turn; no second mathematical attempt here.
