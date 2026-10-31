# Global translation variation: bounded attempt in progress

Approved target: bound the global L1 translation quotients of L520's
fixed-model zero extension, using L513 renewal and L520 localization.
The saved EXPLORE assessment is
`literature/2026-10-30-weil-global-translation-variation-test.md`.

Main gap: L516's signed eigenvalue-relative cancellation and actual-Xi
all-degree positivity. A global BV estimate could enable individual
prime Stieltjes correlations; it would give neither their signs nor
the eigenvalue-relative saving. All model, trace and realization
qualifications in L513/L515/L516/L520 remain.

Preliminary direction (not yet proved): split f into two endpoint
collars and an interior piece. Factor L513's half-line potential as
u(x)=integral_0^x v(x-z) B(z) dz, where
B(z)=integral_0^infinity v(t)g(z+t)dt. Test whether the small factor
V(delta) in an endpoint collar multiplies a global quotient norm of
the complete bounded interior forcing. Treat exterior forcing using
its positive separation from that collar, without differentiating
the trace error. For the interior, investigate a smaller L1 norm of
a high-frequency version of L520's integrable resolvent kernel,
retaining the cutoff commutator exactly. None of these proposed
estimates is currently established.

Pass: a global finite h-independent bound with strict absorption.
Stop: retain the exact boundary/translate term if it cannot be
controlled. No inference from a logarithmic modulus or multiplier
decay alone is permitted. Prior harmonic-gradient/kernel-BV stops
remain; no cross-notebook input or mathematical script is planned.

## Candidate closure, saved before full write-up

Let B1=|c|+||mu_A||_TV and choose delta<ell/4. The endpoint
factorization appears to give, for each of two collar pieces,

    Q_h(collar f) <= V(delta)V(ell) B1 Q_h(f)+C_delta.

The steps are to extend the interior forcing by zero, bound its
quotient by B1 Q_h(f)+2||c f+mu_A*f||_infinity, and convolve with
v restricted to (0,ell). Its cutoff at (0,delta) adds only bounded
jumps. The exterior contribution is an integral of the functions
1_(0,delta)(z) v(y-z), y>ell; each has variation at most
2v(ell-delta). This uses no derivative or variation of u. Convolution
by v restricted to (0,delta) supplies the small V(delta).

For the fixed interior cutoff chi, the exact commutator obeys the
relative quotient estimate

    Q_h(C_chi f) <= A_chi Q_h(f)+B_chi ||f||_1,
    A_chi=integral min(||chi'||_infinity |r|,2||chi||_infinity)n(r)dr,
    B_chi=integral min(||chi''||_infinity |r|,2||chi'||_infinity)n(r)dr.

Both constants are finite. With eta_N(xi)=eta(xi/N), e_N its
Schwartz inverse transform, set K_N=p-e_N*p. Since p is in L1 and
integral e_N=1, approximate-identity convergence gives ||K_N||_1->0;
this is an L1 argument, not a multiplier-decay inference. L520's
localized inversion then suggests

    Q_h(chi f) <= ||K_N||_1 (|c+1|+||mu_A||_TV+A_chi)Q_h(f)
                   +C_(delta,N).

Choose delta first and N second, so the sum of the three coefficients
is <=1/2. All Q_h(f) are finite before absorption because f is L1.
The remaining work is to check the factorization, cutoff constants,
global localization and all h-independent remainder bounds in a
canonical proof. This is a conditional intermediate result, not a
candidate RH solution; no correlation specialization is attempted.

## Completed disposition

The closure is written in
[L521](../lemmas/L521-fixed-model-global-translation-variation.md),
with explicit finite error constants. The two endpoint coefficients
sum to at most 1/4 after choosing delta; the interior coefficient is
at most 1/4 after then choosing N. Thus the actual achieved coefficient
is at most 1/2, strictly below the required threshold 1. The argument
works with the unknown finite Q_h on both sides before absorption,
and retains every signed term. No mathematical script was required.

This is a local conditional ADVANCE awaiting a separate conceptual
audit, not a complete RH candidate or verified originality. The
preliminary reasoning above is preserved; the canonical proof controls
the statement. No Stieltjes specialization or sign estimate was made.
