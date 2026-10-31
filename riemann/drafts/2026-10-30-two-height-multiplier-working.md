# Two-height multiplier test: working checkpoint

The supplied EXPLORE assessment
`literature/2026-10-30-l504-two-height-positive-multiplier-test.md`
authorizes this single mathematical attempt. L504 was read in full;
its independent audit and the parent positive-class source comparison
were checked. Their source coverage and failure distinctions are reused.
No additional external theorem, L503 conclusion or cross-notebook input
is needed. Pre-existing notebook changes are preserved.

Main gap: actual-Xi all-degree positivity and initial signs at unbounded
heights. Intermediate target: the exact approved family
F=E_a+alpha P_b+beta P_{2b}, alpha,beta>=0, with coefficient choices
allowed to vary arbitrarily with a. An O_R(a) full-space M norm would
bound E_a on H_a and then Q_a by L504. A uniform lower obstruction
would stop only this family, not either positive-class inequality.

Test: verify the extended kernel, endpoint integrability and positivity
application, then control the complete residual uniformly in both
coefficients using genuine smooth-Fourier tests. Continue only with the
specified upper threshold or a quantified uniform obstruction; otherwise
preserve the partial calculation and stop. No arbitrary-measure search
or positive-class counterexample is authorized.

Initial observation (unproved at this checkpoint): on cos(sz) with
sa in 2pi Z the complete transform suggests
P_h=I_b(s)-2 cosh(sh)J_h(s), where J_h integrates the kernel tail
over [2a,infinity). Thus F involves both a common I_b term and two
different exponentially amplified tails. Fixing coefficients before
letting a grow would not suffice; the next calculation must rule out
coefficient choices depending on a. Smooth-test errors must also be
controlled uniformly in those coefficients. No result claimed yet.

## Completed attempt

The initial resonant-tail approach above was superseded within this
attempt by a common-sign phase: cos(sa)=0, sin(sa)=-1. The complete
argument is canonical in L505; no tail asymptotic is needed. Both
positive kernels decrease in their horizontal displacement, so their
clipped sine integrals have a common positive lower bound. Smoothing
preserves negative E_a, P_b and P_{2b} separately, uniformly before
any coefficients are chosen. The family therefore has norm at least
c_R L^(R/4)/a^2 for all alpha,beta>=0 at every large real T.

Outcome NEGATIVE, with no positive-class counterexample or actual-Xi
conclusion. L505 is not independently audited. No mathematical script
was necessary: all bounds, constants and the common symbolic onset are
in its full proof. The original approved assessment was left unchanged.
