# Common scaling quotient — working record

Approved target: Test whether the common rational-root ratio parametrizes the rational scaling quotient of each complete L095 system, and whether primitive integral lifting yields a nontrivial class-free restriction.

This attempt uses full audited L095 and reuses SPECIALIZE coverage in
`drafts/literature/2026-10-19-rational-factor-scaling-quotient.md`.
No L097/L098 theorem or class data is used.

Checkpoint before completing the proof: write d=1 or 5 and n=dC.
Then n-5m=d^11 u^5 and H(m,n)=d^11 a^3. The common scale has
weights (m,n,u,a)=(15,15,3,40). On n,u,a nonzero set t=m/n,
h(t)=H(t,1), F=d^77 h(t)/(1-5t)^8 and w=a/u^13.
The equations suggest u=w^3/F, a=w^40/F^13,
n=d^11 w^15/((1-5t)F^5), m=tn. These formulas still require full
forward/reverse, rational-orbit and omitted-locus checks.

For an admissible integer tuple L095 gives gcd(m,n)=1. Thus t=M/N
in positive reduced form forces m=M,n=N, rather than permitting
arbitrary denominator clearing. The prospective lifting criterion is
exactly the original fifth- and cube-power tests with C=N/d; it must
not be presented as an exclusion or a stronger condition. Need check
both d values, all gcd constraints, rational fifth-root scaling and
unique primitive representative before deciding the route.

Outcome at this checkpoint: unfinished proof; no new result assumed.

Completed outcome: NEGATIVE for the direct quotient shortcut. The full
forward/reverse formulas, invariant-field calculation, boundary treatment
and exact primitive lifting equivalence are in
[canonical L101](../lemmas/L101-rational-scaling-quotient-and-primitive-lifting.md).
The quotient is rational, and primitive lifting restores exactly L095.
No integer exclusion, new positive-genus model or originality claim results.
The unfinished checkpoint above is preserved as the working history; its
checks are completed in L101. Independent critical audit remains pending.
