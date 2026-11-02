# Suzuki kernels: large-parameter compact-interval diagnostic

TARGET: Determine whether Suzuki's complete kernels satisfy sup_{0<=t<=T} ||K_theta[t]||_{L2->L2}->0 as theta->infinity for every fixed T>0, with a theta-uniform bound.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The completed post-C499e screen followed the exact power-regularized limit to Suzuki 1907.07302v2; exact-title/large-theta/kernel-limit searches found no matching compact-norm statement. Scoped canonical-system/theta assessments and failure records contain no completed version of this parameter diagnostic. This is bounded coverage, not an originality claim.
SOURCE_EVIDENCE: Suzuki, Integral operators arising from the Riemann zeta function, arXiv:1907.07302v2 (6 March 2020), (1.1), (1.10)-(1.13), Theorem 1.2 and complete (K-v) proof (3.14)-(3.15), printed pp.2-3/7-8; DLMF 5.9.13 with Re(z)>0 and principal logarithm, and 5.11.2 with its closed-sector restriction; L001/L005/L018. Links and scope below.
COMPARISON: Sources cover the complete causal kernel, its multiplier and fixed-parameter local operator setup, plus supporting digamma estimates. They do not supply the requested large-theta uniform bound by citation. Only this parameter specialization and its operator-norm transfer are proposed; do not reproduce the known kernel construction or assume the printed implicit constants are uniform in theta.
GAP: Establish or refute a bound uniform in theta tending to zero on each fixed t interval, retaining the entire zeta multiplier, rational and gamma factors, inversion/Fourier weights and the support restriction. No limiting norm or rate has been proved here.
REASON: This independently testable actual-kernel diagnostic checks whether smoothing can mask the fixed-parameter global obstruction. It replaces an unsupported direct-sign nomination with a concrete estimate; the newly written assessment needs separate next-turn approval before research.
SCOPE: Real theta>=2 tending to infinity; each fixed finite T>0; operator on L2((minus infinity,t),dx) with the exact kernel defined below. Ordinary contour/Fourier estimation, no zero-free-region improvement, no reciprocal-series continuation, no RH or innerness assumption, no lemma about growing T or global determinant nonvanishing.

## Object and precise proposed threshold

Use L018's xi, with its factor 1/2. For theta>1 use the known
K_theta specified by [Suzuki v2, (1.10)](https://arxiv.org/pdf/1907.07302v2):

    exp(-2 theta xi'(s)/xi(s)) = integral_R K_theta(x) exp(i z x) dx,
    s=1/2-i z, Im(z)>1/2.

The prime on xi is its complex s derivative, not a Xi derivative.
Equation (1.1) defines

    (K_theta[t]f)(x)=1_(x<t) integral_(-infinity)^t
                                   K_theta(x+y)f(y) dy.

Here t is the operator interval parameter, not a zero height or heat
time. For each fixed T>0, the sought threshold is a proved function
b_T(theta) tending to zero with

    sup_(0<=t<=T) ||K_theta[t]||_(L2->L2) <= b_T(theta)

for all sufficiently large real theta, or precise evidence refuting
that limit. The full arithmetic kernel is required; testing only its
archimedean component or a finite matrix does not settle this target.
No bound, constant, coefficient or sign is asserted in this nomination.

## Source scope and required difference

Suzuki's Theorem 1.2 and its Section 3 proof establish a continuous
causal kernel and local determinant nonvanishing for theta>1. Read
the entire (K-v) argument, including weighted transforms and its
reference to the small-interval method. Its estimate (3.14) is not
used here as a bound uniform in theta. Rebuild the required parameter
dependence directly from the defining multiplier instead. This is
why an explicit applicability calculation is needed despite the known
representation; it is not a new construction of that representation.

[DLMF 5.9.13](https://dlmf.nist.gov/5.9.E13) is an integral identity
for psi on Re(z)>0 with the principal logarithm. It can support
estimates uniform on a chosen vertical line. Alternatively
[DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2) gives the digamma expansion
in |arg z|<=pi-delta. Neither states the proposed operator limit.
Any error used must be controlled before exponentiation by theta;
fixed-theta big-O notation is insufficient.

L001 gives nonvanishing only on Re(s)>1. L005 gives the locally
uniform Euler logarithm there; differentiating that series requires
its derivative majorant or an ordinary holomorphic argument. L018
fixes the completion and its rational/gamma factors. These are the
essential local input IDs; C032a and C465a provide relevance context,
not mathematical premises of this estimate. No external half-plane
manuscript or cross-notebook result is an input.

Verify Fourier/inversion convergence and all weights on the selected
line before transferring estimates to the compressed L2 norm. Retain
the whole parameter dependence; do not shift through an unknown zero,
assume a global L2 isometry, or replace support estimates by a
finite-dimensional spectral preview. Standard Fourier inversion,
Plancherel and dominated convergence may be cited by their named
theorems with their hypotheses checked. No numerical script is needed
unless a genuinely load-bearing finite estimate arises.

## Relevance, decision and remaining gaps

The main target is actual-Xi mixed signs below logarithmic tail
cutoffs at unbounded heights. A proved compact-interval collapse
would diagnose a quantifier failure in attempts to infer fixed-theta
global positivity by increasing smoothing on tested windows. It would
neither prove that such a global statement is false nor improve a Xi
sign. If collapse fails, identify the precise lower-bound witness or
uncontrolled term; failure of one upper estimate is not refutation.

Continue only if the complete norm bound tends to zero, or an
informative obstruction decides this exact limit. Otherwise park the
diagnostic after the bounded attempt, preserving unfinished reasoning;
do not expand to arbitrary scaling laws or another broad discovery
screen in the same turn. Full mixed signs, fixed-parameter all-window
control, realization and terminal-kernel decay remain independent gaps.

This is a REPRODUCTION/SPECIALIZE calculation with known analytic
tools, not a protected creative attempt. No independently positive
signed transfer for actual Xi has been identified. Routing is
calculation, standard/high. The supervisor must separately approve
this new continuation; no mathematical work is approved retroactively.

## Mathlib

Full kernel/limit coverage has not been checked. L001/L005 retain
supporting Euler-product/nonvanishing APIs, including
`riemannZeta_ne_zero_of_one_lt_re` and
`riemannZeta_eulerProduct_exp_log`; these do not formalize the kernel
or parameter limit. No absence or formal-verification claim is made.
