# Direct rational joint-gate test — step 233

Ready assessment: `drafts/literature/2026-10-14-cyclic-family-alternating-kernel.md`.
Approved target: Determine whether L087's full alternating moment system has zero kernel for every bijective H-labeling.

Main gap: audited L088/L089 still permit rank M=27, equivalently
rank R=2. The intermediate test is whether L095's rational G=J=0
forces a pole or collision, or restricts actual transformed H seeds.
That could help exclude this family; actual-error applicability,
arbitrary families and challenge qualifications remain independent.
Continue only on a uniform exclusion or actual-H restriction; an
unresolved elimination ends this mechanism.

Coverage and duplicates: reused the supplied ready source comparison,
which distinguishes fixed H from generic-evaluation theorems. Read the
full L092–L095 proofs, L090/L091 gate statements, relevant L089 plane
conclusion, ATTEMPTS/020,029,031,032,033, and the previous joint-elimination
draft and history. L090–L095 remain unaudited. No new external theorem,
rank sample, H assignment or source search is an input. The stopped
multivariate expansion is not resumed.

## Working algebra

Use L095's rational reconstruction, with c,e,g,X as normalized seeds
and j,Y,k,d,m,n,z its forced values. Retain all finite denominators,
T(H)-membership, inverse-projectivity pole and collision tests, and
the final deductions D_0,D_4. No residual slope is inverted; in
particular rho=sigma=0 remains included.

Write L095's equations (5), without expanding in the seeds, as

    G=Uz+V,
    J=A(z-c)+B(z-j),
    U=j-k+(1-j)Y+(k-1)m,
    V=jY(m+k-1)+mk(1-j-Y),
    A=d(Y-X)(d-g)(d-j),
    B=(d-c)(X-g)X(d-Y).

A,B are nonzero at every admitted labeling: their differences compare
distinct indices, and d,X differ from zero at index seven. A short
factorization is

    V+jU=(j-k)(m-j)(Y-1)=:C.                       (1)

Indeed the Y-coefficient on the left is
j(m+k-1)-mk+j(1-j)=(j-k)(m-j), and its constant
coefficient is mk(1-j)+j(j-k)+j(k-1)m=-(j-k)(m-j).
Thus C!=0 by distinctness. This is working algebra for existing gates,
not a new uniform kernel restriction.

If U=0, (1) gives V=C!=0, so G has no finite zero. If A+B=0,
J is the constant -Ac-Bj=A(j-c)!=0. Every finite solution therefore
has U(A+B)!=0, independently of L093/L094's residual coefficients.

For U!=0 eliminate z=-V/U. The remaining equation is exactly

    A(V+cU)+B(V+jU)=0,

or

    A(c-j)U+(A+B)C=0.                              (2)

Conversely, (2) with U!=0 gives G=J=0 at z=-V/U, as equations in
this one variable, and forces A+B!=0. At that value

    z-j=-C/U !=0,
    z-c=BC/(AU) !=0,

the second equality following from (2). These particular collisions
therefore do not follow merely from (2) on its nonpole branch. This
is not existence of reconstructed labels or transformed H seeds.

Keeping (2) alone introduces a spurious branch: U=0 makes it equivalent
to A+B=0, although both original equations then have nonzero constant
terms. That branch must be excluded; no claim is made that it is
attained on L095's chart. Conversely the nonpole branch has not been
excluded on that chart.

Crucially, z is already fixed in L095 by D_2 after D_3,D_8. Equation
(2) cannot replace that condition. A reconstruction still needs
Uz+V=0 for that exact z, together with (2), the other unused gates and
the full rank test. Choosing a replacement z freely would lose one
condition. No such sufficiency claim is made.

## Decision and limits

The factor (1) resolves possible divisions, but neither (2) nor the
retained rational-z equation has been shown to force a forbidden
factor after L095 substitution. Both remain unresolved on actual
seeds. There is no uniform exclusion, actual-H restriction, compatible
labeling or new useful lemma. No symbolic expansion or mathematical
script was run; the coefficient calculation above checks the short
identity completely. Full matching Mathlib coverage was not checked.

Outcome: EXPLORATION, one mathematical exploration turn used and one
carried forward. This is not negative mathematical evidence against
zero kernel and does not reset the budget. The continuation test failed,
so stop this joint-residual/rational-gate elimination mechanism and
preserve all unfinished work. PROOF.md and DAG.md need no change.

The proposed independent continuation is conditional actual-error
realization from a cyclic rank-27 labeling. Audited L087/L088/L089 are
prospective inputs; L010 and foundations/02 need exact event/moment
comparison. L075/L076 are pattern-specific comparison leads, not
imported cyclic theorems. This target is REVIEW_REQUIRED, without
derivation or approval here. It could connect a future deficient
labeling to the frozen event, but does not exhibit one or settle
arbitrary families or challenge qualifications.
