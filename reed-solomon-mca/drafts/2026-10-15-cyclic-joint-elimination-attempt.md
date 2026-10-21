# Joint residual elimination — step 232

Ready assessment: `drafts/literature/2026-10-14-cyclic-family-alternating-kernel.md`.
Exact approved target: Determine whether L087's full alternating moment
system has zero kernel for every bijective H-labeling.

Main gap: the possible rank-27 kernel in audited L088/L089. The
intermediate test is whether L093's Delta and L094's Psi force a pole
or collision in the rho_1!=0 branch, uniformly in the normalized seed
variables; the rho=0 and sigma=0 branches must remain unresolved unless
separately excluded. A uniform contradiction could remove this family,
but actual-error applicability, arbitrary families and the challenge
qualifications remain independent gaps.

Before calculation: retain c,d,e,g as indeterminates over F_97, and
use exactly L092–L094's rational reconstruction, Q,E,P. Compute their
linear remainders and test the factors of the joint seed equations.
No generic nonidentity will be called an actual-H restriction. Continue
only on a uniform exclusion or an actual-H restriction; otherwise stop
this residual-elimination route and select an independently testable
continuation. No H-label sweep, rank sampling or new source review.

Inputs read: full L092–L094, the needed L090/L091 gate derivations,
the previous S_0 diagnostic implementation and ATTEMPTS/020,029,031,032.
The prior source assessment is unchanged and reused. L090–L094 remain
unaudited; their formulas are provisional inputs to this attempt.

All seed denominators, q_2, ell, O(X), W(X), inverse-projectivity
poles, transformed H-membership and all sixteen distinct labels remain
required. Working over a rational-function field does not exclude
specializations on a coefficient-zero locus. In particular a generic
gcd equal to one would not prove that simultaneous specializations
are impossible.

Completed: [L095](../lemmas/L095-cyclic-rational-seven-seed-reconstruction.md)
gives a different seven-seed reconstruction with at most one completion.
The key exact cancellation is t=j/[c(j-e)], independent of d after
D_1,D_10. With X a seed, S_8 determines Y, D_15 determines k, and
D_10 determines d. The two potential denominator-zero branches are
incompatible with distinct labels. This is a uniform restriction for
actual H-labelings, not an arbitrary-seed nonidentity; it changes the
seed set and does not strengthen L092 for its original seed choice.
The canonical proof retains every residual-zero branch and gives the
two remaining rational gate equations G,J explicitly.

The initially attempted direct multivariate expansion did not finish.
`scripts/cyclic-shared-gates/joint_generic_elimination.py` saved only
the quadratic and its coefficients before rational-function cancellation
was interrupted during V. Its full partial output is
`scripts/cyclic-shared-gates/joint-generic-elimination.json`, explicitly
marked INCOMPLETE. It certifies no joint factors, residual bound, pole
implication or kernel exclusion. A first printing error was repaired;
the later interrupt guard was not rerun. None of this computation is an
input to L095, whose identities and exceptional cases are proved there.

The requested joint incompatibility remains open. The useful output
of this one attempt is a rational chart covering every admitted
reconstruction, including rho=sigma=0. Continue with one direct
factor/pole test of L095's G=J=0 on this chart, retaining transformed
H-membership and all other gates. Stop this algebraic elimination if
it supplies only generic nonidentities or another unfinished expansion.
The analytic result is local progress, not certified novelty or a rank
bound. No H-label assignments, rank tests or new source searches were
performed. Zero mathematical EXPLORATION turns used or carried forward.
