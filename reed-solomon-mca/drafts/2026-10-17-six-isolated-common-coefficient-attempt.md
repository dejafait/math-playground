# Six isolated rows: common-coefficient elimination attempt

STEP_ID: 2026-10-17-mca-267-six-isolated-common-coefficients

The prior EXPLORE assessment is
`literature/2026-10-17-six-isolated-restored-system-test.md`.
Its exact six-row target and scope are retained. The main gap is the
uniform triangle twelve bound. An incompatibility of the actual common
label coefficients could restrict high-count isolated fibers; a fully
gated six-row witness could refute this local exclusion. Neither six-row
extraction nor equality is assumed.

## Working checkpoint

The attempted mechanism is joint elimination in the coefficient space of
the six actual support quartics, using L057 (5), (6), (10), L059 (4), and
L064's exact pair compatibility. L010/L041 enter through that recovery
framework. L068/L080 are comparisons, not mathematical premises.
ATTEMPTS/036 already stops automatic cross-difference minors and their
insufficient root count; none is proposed as a new condition here.

For a quartic f with roots K disjoint from P, let eta(f), zeta(f) be
the two scalar projections in L057 (5). For x in P set

    D_x(f) = x c_x f(x),
    Y_x(f) = -sum_(y in Y) c_y y f(y) ell_x(y),
    Z_x(f) = -sum_(z in Z) c_z z f(z) ell_x(z).

These are linear functionals on the five-dimensional quartic coefficient
space, with the SAME nine-label coefficients for all six rows. In
particular u_x=Y_x/D_x, v_x=Z_x/D_x. Isolation and eligible scalars give
eta*zeta*(eta+zeta)!=0; disjointness from P gives every D_x!=0.
The candidate scalar is mu=zeta/eta.

The three restored weight fractions have quadratic numerators and
denominators

    A_a = eta D_a - eta Z_a + zeta Y_a,
    B_a = (eta+zeta) D_a,
    A_b = zeta Y_b - eta Z_b,   B_b = zeta D_b,
    A_c = eta Z_c - zeta Y_c,   B_c = eta D_c.

Thus p=A_a/B_a, q=A_b/B_b, r=A_c/B_c. The next check is whether
dependencies of six quartics in a five-dimensional space add a usable
incompatibility, rather than simply rewriting these fractions or L064.
All ranks must be retained. Full recovered weights and original E gates
remain independent tests. No new result or witness is claimed at this
working checkpoint.

## Completed elimination and reverse check

For row i evaluate the six quadratic forms above at its actual monic
quartic f_i. None of B_ai, B_bi, B_ci vanishes: the only factors used
are eta_i, zeta_i, eta_i+zeta_i, and D_xi, whose nonvanishing follows
from the target hypotheses. For x=a,b,c the six equations are

    A_xi = w_x B_xi,  1<=i<=6,

where (w_a,w_b,w_c)=(p,q,r). Eliminate w_x using row 1. The result is

    A_xi B_x1 - A_x1 B_xi = 0,  2<=i<=6.                 (1)

Conversely (1) recovers precisely w_x=A_x1/B_x1 and all six original
equations. Pair comparisons not involving row 1 follow by subtraction
after division by the proved nonzero B entries. Thus there are fifteen
displayed equations, not fifteen independent restrictions established
here. This is exactly L064's compatibility locus after substituting
the actual common-label formulas, with mu_i=zeta_i/eta_i. It is not a
new sufficient condition, stricter test, or incompatibility theorem.

This computation does use the common nine-label origin: eta,zeta,D_x,
Y_x,Z_x are fixed linear functionals of f, rather than unrelated row
coefficients. But that origin alone did not prove a nonzero left side
of (1) for every admitted six-support configuration. No generic rank
claim or division by a coefficient of a putative resultant is made.
Vanishing numerators, vanishing minors and deficient joint ranks remain
admitted. The only pivots inverted are the B entries proved nonzero.

The reverse check also retains the gates. Require the recovered common
p,q,r to avoid 0,1, the six mu to be distinct and avoid 0,-1, and each
of the twenty-four omega coefficients in L057 (13) to be nonzero.
For a prescribed chart retain every E_i!=0. When these hold, L057's
complete converse supplies all eight moments for every row; checking
(1) alone does not supply fullness or the chart gates. Conversely every
six-row witness in the target satisfies all these conditions. No
witness was constructed, and no moment verification of a witness is
claimed. Both-zero projected rows are outside this isolated-row target,
not excluded from the main triangle problem.

## Six-quartic dependence test, including deficient ranks

The following records an attempted consequence of the COMPLETE systems,
not a new bound or an independently established canonical input.
Write f_i also for its column of five coefficients, C=[f_1 ... f_6],
and M=diag(mu_1,...,mu_6). Distinct monic support quartics are not
proportional, so 2<=rank(C)<=5; the argument does not assume rank five.

Using the actual common weights, set

    N_0 = Z+c_a(1-p)v_a+c_c r v_c,
    N_1 = Y+c_a p v_a+c_b q v_b.

These are full four-support moment vectors on A_1 and A_0 respectively,
by the base gates. Let H_j be the 4-by-5 recurrence matrix with
(row l,column t) entry (N_j)_(l+t), l=1,...,4, t=0,...,4.
L057's full recurrence equations say

    H_0 C = H_1 C M.                                    (2)

For clarity, ker(H_1) is exactly the line spanned by the monic base
locator f_A0, and ker(H_0) is the line spanned by f_A1. Indeed the
first four columns of H_j factor as a four-label Vandermonde matrix,
a diagonal matrix of the four nonzero weights times their nonzero
labels, and the transpose Vandermonde matrix. They are invertible.
The base locator annihilates its own four moment terms, so it spans
the remaining one-dimensional kernel. This is the existing full-weight
recurrence specialization, not an assumption about the six-row rank.

For EVERY d in ker(C), (2) gives the necessary memberships

    C M d       in span(f_A0),
    C M^(-1) d  in span(f_A1).                           (3)

For the second membership apply (2) to M^(-1)d; all mu_i are nonzero.
Thus (3) has eliminated p,q,r from this particular consequence: C,M
and the base locators are determined solely by the common labels.
Membership can be tested without divisions by requiring all two-row
minors of [f_A0,CMd], respectively [f_A1,CM^(-1)d], to vanish.
It must hold for a full basis of ker(C), not an arbitrarily chosen
nonzero vector only.

If rank(C)=5, ker(C) is a line. For nonzero d on that line, CMd is
nonzero: otherwise Md also lies on that line, so d is an eigenvector
of the diagonal matrix with pairwise distinct entries. Such a vector
has exactly one nonzero coordinate, contrary to Cd=0 because each
f_i is nonzero. The same reasoning applies to M^(-1). Hence in this
branch (3) asks for the two exact nonzero locator directions.

If rank(C)<5, that argument does not apply. Both images in (3) may
vanish for some d, and one must retain all kernel vectors and every
zero image. A chosen five-column minor can vanish. No such minor is
inverted and no branch is dropped. The full coefficient equations
(1), the gates and the support-intersection conditions remain necessary
in these branches as well.

This was the discriminating coefficient-dependence test attempted in
addition to the weight fractions. No incompatibility between (3) and
the fixed-H quartics was established in any exhaustive rank partition.
In particular six vectors in a five-dimensional space merely guarantee
a kernel vector; they do not force either image in (3) to have a
forbidden direction. The displayed implications are linear combinations
of (2), so they cannot by themselves strengthen the exact recovery
criterion. A hypothetical nonzero residual would need a proof using
the actual label and support constraints; none was obtained. Neither a
rank-five assumption nor the words "six simultaneous systems" supply
that missing proof. These unfinished consequences are preserved for
reference, not promoted to a lemma or a ready renewed target.

## Evidence, stopping decision and source qualifications

The canonical inputs are L057, L059 and L064. The recurrence source is
imported through L057: P. Chojecki, *Shortening Bounds for Reed–Solomon
MCA*, author TeX v9.2, July 17, 2026, DR2 and DR6–DRC, lines 2785–2935,
[author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
Its assessed specialization uses R=8, t=4, multiplier x, eta_j=s_(j+1),
distinct nonzero labels and nonzero full-error weights where required.
The prior assessment supplies the inspected primary proof cases; no new
source retrieval or general recurrence reproof is needed. The mutable
source is not certified unchanged today or identified with another paper.
No matching Mathlib theorem was checked; no absence or formal proof is
asserted.

Outcome: EXPLORATION / RESEARCH / POTENTIALLY_NEW, actual task type
proof_attempt. This classification concerns the assessed target; no
originality, new mathematical input, uniform exclusion or verified
six-row witness is claimed. The required threshold was a genuine
fixed-label-coefficient obstruction or a full witness. The achieved
output is a reversible rewriting of the exact weight comparisons and
unresolved necessary rank-branch conditions. It does not meet that
threshold. No mathematical script or finite label sweep was run.

Stop this simultaneous-elimination attempt under its preapproved test.
ATTEMPTS/036's earlier root-count stop and L080's completed fixed-label
exclusion remain intact. Reopening would require a specific coefficient
nonvanishing argument with every deficient-rank case, not more copies
of (1), an unproved resultant, or increasing the row count. One
mathematical EXPLORATION attempt has been used since the carried zero;
this does not reset any budget. The main bound, six-row coexistence,
few/no-both-zero fibers, extraction/assembly and challenge-definition
qualifications remain unresolved. The interval stays 11/q–16/q.

For routing only, a different bounded candidate is recorded in
`literature/2026-10-17-cyclic-dense-polynomial-parity-test.md` as
REVIEW_REQUIRED. It concerns dense polynomially weighted product
parities and the exact bilinear equations of L097, not block-supported
parities or six-row weight elimination. No such new mathematics is
derived, approved or attempted here.
