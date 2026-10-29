# Two-peak unit-gap symbolic attempt — working record

Step539, 2026-10-28. The prior EXPLORE assessment is
`drafts/literature/2026-10-28-two-peak-unit-gap-test.md`; the current
invocation explicitly authorizes its one symbolic elimination pass.
This file preserves unfinished reasoning, not an established theorem.

Main gap: universal descent. Intermediate target: strict descent at an
assumed first coefficient drop for an actual word `1^a 0 1^c 0^d`,
with a,c,d>=1. A partial orbitwise transfer could extend the sourced
one-peak case; other shapes and finite-drop existence remain open.
Continue only with a proof, a useful exact subcase, or a material refined
mechanism. Save an unsigned expression as EXPLORATION without a census
or family expansion. L005/L109 and Attempts002/003/036 are comparisons,
not inputs; their stopping evidence is preserved.

## Initial exact setup

Use L002 for the first complete block and Rozier2019, INTEGERS19 A8,
Lemma1/equation(4)/proof pp.2–3 for the second finite affine segment.
The saved source assessment is reused; there is no new literature turn.
Write

    n=2^a u-1,  x=T^(a+1)(n)=2^c v-1,
    3^a u+1=2^(c+1)v,
    y=T^(a+1+c+d)(n)=(3^c v-1)/2^d,

where u,v are positive odd integers and y is a positive integer.
The first even run is exactly one; the observed final run need only
have length at least d. Do not impose oddness on y.

The proper-prefix guards remain in force. The guard immediately after
the first even step requires 3^a>=2^(a+1), hence a>=2. The last
proper-prefix guard and the final drop give

    2^(a+c+d) <= 3^(a+c) < 2^(a+c+d+1).

Equality with the power of two cannot occur. All intervening prefixes
must still be accounted for when the reduction is written up.

For a non-descending endpoint set h=y-n, an integer >=0. With
A=3^a, C=3^c, P=2^a, Q=2^c, D=2^d and Delta=2PQD-AC>0,
the two junction identities give

    Delta*u + 2QD*h = 2QD+C-2Q.

Both h=0 and h>0 are unresolved at this checkpoint. No formula here
asserts that the relaxation is sufficient for an actual word.

## Partial result reached in this pass

For h=y-n, the displayed identity and Delta*u>0 give

    h < 1+C/(2QD) < 1+P/A <= 13/9 < 2.

Thus the integer endpoint always satisfies y<=n+1. Non-descent has only
the cases h=0 and h=1. In the latter case Delta*u=C-2Q forces c>=2;
y=n+1 is even and T(y)=(n+1)/2<n. In particular, c=1 with an even
endpoint has strict descent already at the first coefficient drop.
This is a proved restricted transfer, not a proof of the whole target.

The exact two remaining candidates are

    h=0: Delta*u=C+2Q(D-1), Delta*v=PD+A(D-1);
    h=1: Delta*u=C-2Q,      Delta*v=PD-A.

For h=0 (respectively h=1 with c>=2), divisibility of the first numerator
by Delta also makes v an integer: A*N_h+Delta=2Q*V_h and Delta is odd.
Both numerators and Delta are odd, so u and v are odd. Their positivity
follows directly for h=0 and from Au+1=2Qv for h=1. These conditions
reconstruct the actual finite word, not just a real relaxation. Equality
makes the final even run exact; unit growth leaves exactly a further
even steps because y=2^a*u with u odd.

Neither divisor case has been excluded uniformly over the unbounded
exponents. The elementary lower bound Delta>=1 alone gives no such
exclusion. No counterexample, two-cycle exclusion or unproved power-gap
bound is assumed. Stop the one-pass attempt at this boundary; no census,
new family or second elimination has been started.

## Verification and completion

The prefix reduction, affine specialization, integer bound and both
directions of the divisor reductions are now canonical in L110,
`lemmas/L110-two-peak-unit-gap-endpoint-bound.md`. The checkpoint reports
a partial ADVANCE, not the whole strict-descent target. A separate later
critical audit remains necessary and has a REVIEW_REQUIRED nomination.
No mathematical script or finite enumeration has been run.
