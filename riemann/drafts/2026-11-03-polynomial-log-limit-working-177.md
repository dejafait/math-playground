# Approved polynomial logarithmic-limit attempt — step 177

The invocation-start SPECIALIZE assessment is
`literature/2026-11-03-signed-bump-polynomial-zero-limit.md`; its exact
target is unchanged. The main gap is actual-Xi mixed positivity, with
the complementary spatial Jensen defect unpaid. This attempt concerns
only L714's normalized polynomial logarithm. Its plausible use is the
exponential scale of the inner inverse kernel; resolvent and signed
bump cancellation remain independent.

L714's coefficients and root argument have been read, together with
the three specified signed/absolute/blend failure records. Existing
uncommitted notebook work is preserved. No source discovery is needed:
the assessed JKM profile theorem is the intended import. Its precise
normalizations will be checked while applying it, without reproving
general zero convergence.

Working calculation (not yet a result): reflection and normalization
give coefficients binom(N,j) times product over 1<=k<=N of
(1-j*k/(U*n^2)). The candidate profile is binary entropy plus
the integral of log(1-t*s/U) over 0<=s<=1. Degree N versus n,
the coefficient hypothesis, uniqueness of the identified limit and
the bounded complex-log kernel at escaping roots all require proof.

Continuation test: obtain one analytic limit locally uniformly on
|zeta|<1 from the exact profile and the cited theorem. Stop this
application if a required hypothesis fails; real-only convergence,
numerical roots and unproved subsequence uniqueness do not suffice.
No boundary, signed-rate, nonvanishing of p_n/R_n or realization claim
is authorized. Preserve log(0)=-infinity in the separate signed test.

The primary theorem's Definition 1.2 and Theorem 2.2(a),(b),(e)
were checked directly at the assessed version, pp.3,5--6. This is
application of the ready source coverage, not another literature
search. It permits degree n-1 with the missing mass 1/n at infinity;
the profile interval is (0,1), so that mass disappears in the limit.

Proof plan now justified algebraically: obtain the reflected-root
measure from the profile theorem, push it by y -> -1/y into [0,1],
and integrate the uniformly convergent series log(1-zeta*a).
This gives uniform convergence on each closed subdisk. Identification
uses x=t/(1-t)*exp(integral_0^1 s/(U-t*s) ds) and integrates its
unique inverse through F(-x)'=t/x. The constant is fixed by F(0)=0.
The full proof and final qualifications are now canonical in
[L715](../lemmas/L715-inverse-kernel-polynomial-logarithmic-limit.md).
The target succeeded as a known-theorem specialization, classified
REPRODUCTION. This working note is not a substitute for that proof.
