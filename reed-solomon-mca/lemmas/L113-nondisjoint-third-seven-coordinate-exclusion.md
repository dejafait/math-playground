# L113 — One nondisjoint third support is excluded for the fixed pair

## Hypotheses

Use F=F_(97^20), the order-sixteen subgroup H of F_97^*, dimension
eight, L010's shifted moments and the pinned same-support event on
1/4<=delta<5/16. Assume the actual Hankel determinant D and all coordinate
locators are nonzero polynomials, both coefficient syndromes belong to
U_S for S={1,8,12,18,22,27,33}, and there are sixteen original finite
bad parameters with t=0 in L104's notation. Weights and the prescribed
original finite chart are arbitrary over F. Retain audited L109's and
L086's inherited finite-certificate qualifications, including the
L010/L103/L104 smaller-support and nonpersistence inputs.

Suppose three actual two-overlap supports are

    A1={1,8,47,50}, A2={12,18,64,70}, A3={1,22,75,79}.

For A=I union K use I subset S, K subset J=H minus S, |I|=|K|=2,
and exactly L109's six-by-21 exterior block N_A with increasing S-pair
column order. No universal occurrence of these labeled supports is assumed.

## Conclusion

The hypotheses are contradictory. This particular nondisjoint third
support cannot occur with A1,A2 in the stated t=0 equality class.

All 756 possible fourth supports are covered. Exactly 254 are pairwise
linear with the three fixed supports. Of these, 118 have stack rank 21;
112 have rank 20 and 24 have rank 18. Every complete deficient kernel
in the pairwise-linear class is contained in

    E_1 wedge F_97^S,

where E_1 is the coordinate vector at label 1. Every nonzero point of
each such kernel is decomposable over every extension. Its plane contains
E_1, so the first row either has rank-zero projection, or its unique
recovery has lambda=0 and zero overlap weight at label 8. Both cases
fail L109's necessary gates. In particular the 24 projective planes of
kernel points are excluded as entire loci, without rational-point sampling.

This is a restricted result with explicit finite-computation dependence.
The same-step independent replay below passes; the separate step-309
critical proof/program audit below found no defect. Arbitrary third supports, pairs,
seven-sets, universal representation, other t profiles and challenge
qualifications remain unresolved. The global interval stays 11/q–16/q.

## Proof

### Imported results, exact scope and comparison

Apply audited L109's necessary support filter and full projective gates,
and audited L086's pairwise linearity at sixteen original finite bad
parameters. Their field, H, dimension, pinned event, actual polynomial
nonpersistence and original-chart hypotheses are exactly those retained
above. L109 supplies independent lift coefficients and r=12+n_0 in
12–14 distinct actual two-overlap rows. Only its necessary direction is
used; its r>=6 converse is not applied to a four-row subfamily.

The standard inputs are imported through L109 and L104 from J. I. Hall,
*Notes on Coding Theory*, [Theorem 5.1.1, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
[accepted manuscript, 2016-02-29, section 5, Definitions 5.1–5.2, Lemma 5.3 and the following shortening formula, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf).
The sixteen distinct labels, unit evaluation multipliers, field and
dimension are unchanged. Shortening exactly J minus K, seven coordinates,
leaves dimension one with nonzero retained multipliers, giving L109's
g_K and recovery formulas. No general coding theorem is reproved.

The ready EXPLORE assessment at turn start was
`drafts/literature/2026-10-18-fixed-pair-remaining-third-gates-review.md`;
its COVERED_TARGET is exactly this diagnostic. This is REPRODUCTION of
the assessed finite gate mechanism, without a claim of originality or
progress beyond the checked literature. L111/L112's disjoint-third
certificates do not cover this A3. ATTEMPTS/041's failure of uniform
rank-only extrapolation is preserved: the new calculation finds genuine
rank drops and excludes them by full gates.

### Complete finite support and kernel certificate

Enumerate binom(S,2) times binom(J,2), with increasing pair order:
21*36=756 distinct fourth supports. This is the entire two-overlap class,
before incidence filtering. A fourth support is eligible precisely when
its intersections with each fixed support have size at most one.
This also excludes repeated rows. The all-case rank histogram is

    {17:3, 18:214, 19:47, 20:293, 21:199}.

The pairwise-linear sublist has histogram

    {18:24, 20:112, 21:118}.

For each case build the four-block stack N. Direct products for g_K and
an independent derivative construction of its values give identical blocks:
at x in S union K,

    g_K(x)=16*x^15 / product_(y in (S union K) minus {x})(x-y).

This follows by differentiating X^16-1=g_K(X)*product_(y in S union K)(X-y)
at its simple root x. All denominators and the numerator are nonzero,
because the labels are distinct and nonzero and 97 does not divide 16.

Incremental row elimination and independent column elimination agree on
every rank. At each of the 199 full-rank cases, a saved 21-by-21 minor
has nonzero residue modulo 97, checked also by exact integer fraction-free
elimination. These minors remain nonzero over every extension.
At all 557 deficient cases, including those rejected by incidence,
a complete normalized kernel basis is saved. A third quotient construction
using w_x/g_K(x)-w_z/g_K(z) and Gauss–Jordan elimination computes it;
the pivot columns agree with the independent rank computation, the free
coordinate submatrix is the identity, and every residual against the
original stack vanishes. These 1,041 basis vectors therefore span the
entire kernels, including after scalar extension.

For all 136 eligible deficient cases, every entry of every basis vector
in a coordinate pair not containing label 1 is zero. This checked linear
identity for the complete basis proves the claimed containment in
E_1 wedge F_97^S, and then in E_1 wedge K^S over every field extension K.
It is not inferred from checking finitely many projective points.

For an explicit rank-18 example choose A4={1,12,85,89}. In increasing
S-pair column order the complete basis is

    (0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (11,0,0,53,27,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0).

The certificate preserves this basis, its complete residuals and every
other case; this example is illustrative rather than the coverage proof.

### Entire extension-field gate loci

Take an eligible deficient stack and any nonzero p in its kernel over an
extension K of F_97. The basis identity gives p=E_1 wedge w for some w;
nonzero p means w is not proportional to E_1. Thus p is decomposable and
its plane is L=span(E_1,w). Since label 1 lies in I1={1,8}, L109's Q_1
annihilates E_1. Hence rank(Q_1 restricted to L) is either zero or one.
Rank zero is an explicitly prohibited branch by L109's actual
nonpersistence argument. At rank one, its kernel in L is exactly
K*E_1. The unique recovery direction is therefore h=c*E_1, c nonzero.
The pivot z=min(S minus I1)=12 is different from 1, so

    lambda=h_12/g_K1(12)=0,   h_8-lambda*g_K1(8)=0.

This fails both the nonzero-lambda and one overlap-weight gate. These
failures are invariant under every nonzero rescaling and every choice
of original chart. A finite direction cannot repair them; an infinite
direction is already inadmissible. This excludes every nonzero point
of every eligible deficient kernel over every extension, including F.

The saved full-gate calculation also explicitly retains all 35 Plucker
quadrics. At each of the 112 one-dimensional kernels its sole projective
point passes Plucker, has rank-one projection at each of the four rows,
and fails lambda at the first row. All four recovered row errors,
overlap weights and original-chart linear conditions are saved; all
448 row tests have vanishing eight-moment residuals, including failed
full-weight errors.

Each rank-18 kernel is three-dimensional. All 35 quadratic polynomials
vanish identically in its three kernel coordinates, so its decomposable
projective locus is the entire P^2 over any extension. The calculation
uses the complete 21-chart cover p_ab!=0. Fifteen charts per kernel
are identically empty, and six remain. In each remaining chart put

    U_x=p_xb, V_x=p_ax.

L109's Plucker reconstruction gives U wedge V=p_ab*p. Since p_ab!=0,
U,V are independent and span L. For row j let qU=Q_j U, qV=Q_j V.
All their two-by-two minors vanish. Rank zero has no nonzero pivot;
rank one is covered by the four possibilities
(qU_n,qV_n)!=(0,0), each retaining both alternatives. Set

    alpha=-qV_n, beta=qU_n, H=alpha*U+beta*V.

Then H is nonzero, Q_j H=0 and it spans the recovery direction. The
three full-weight numerators are

    H_z,  g_K(z)*H_i-g_K(i)*H_z for i in I_j.

Each must be nonzero; their omitted denominators g_K(z) are nonzero
constants. For every nonempty chart and every first-row projection
pivot, H_12 and the overlap numerator at label 8 are identically zero
quadratic polynomials. If both projection-pivot forms vanish the branch
is empty instead. All coefficient vectors, identity certificates and
rank-zero alternatives are retained. No ideal solver, source access,
finite-point assumption or resource cap leaves an unresolved locus.

For each row and branch the saved prescribed-chart inequality is
D*alpha-C*beta!=0: if u_original=A*U+B*V and v_original=C*U+D*V,
AD-BC!=0, the original first coefficient of H is
(D*alpha-C*beta)/(AD-BC). The actual error is divided by that coefficient.
The calculation never chooses a replacement original chart. Intrinsic
lambda-zero failures already exclude all its possibilities.

### Equality transfer, verification and limitations

If the three actual supports existed, L109 would supply at least twelve
distinct actual two-overlap rows, so choose any fourth different from
them. L086 makes it pairwise linear with the fixed three. It is therefore
one of the 254 eligible cases. Rank 21 contradicts L109's required
nonzero wedge. In every deficient case the full-gate obstruction just
proved contradicts that same actual wedge. This proves the conclusion.

Reproduce the complete certificate with
`python3 scripts/seven-coordinate/nondisjoint_third_diagnostic.py`.
Full evidence is in `scripts/seven-coordinate/nondisjoint-third-diagnostic.json`.
The program prints actual/required coverage, rank and gate counts,
unresolved indices, failures and the certificate path.

Run `python3 scripts/seven-coordinate/verify_nondisjoint_third_diagnostic.py`
for the same-step independent replay; its full output is
`scripts/seven-coordinate/nondisjoint-third-diagnostic-replay.json`.
It imports no producer module, independently reconstructs H, all g_K
polynomials and derivative values, and uses greatest-pivot ratio
covectors plus forward elimination/back substitution to recover every
rank and complete kernel. All 199 exact integer minor determinants,
557 deficient bases and 1,041 vectors agree. The coordinate-factor identity
is checked for every vector of every one of the 136 eligible kernels.

The replay checks all 504 projective charts of the 24 larger kernels,
including 360 empty charts and 144 nonempty charts; all 2,304 symbolic
row/pivot branches and 16,128 saved polynomial identities agree. It
recovers every relevant homogeneous quadratic from its exact determining
values at e_i and e_i+e_j: diagonal coefficient f(e_i), mixed coefficient
f(e_i+e_j)-f(e_i)-f(e_j). Degree at most two is known from the saved
formulas, so this determines coefficients over any extension; it is
polynomial identity verification, not numerical sampling of a locus.
There are 13,824 determining branch evaluations. For each isolated point,
a direct five-by-three system in (alpha,beta,lambda) reconstructs every
recovery independently of the producer's quotient pivot, checking all
448 row gates and 3,584 original shifted-moment residuals. No failure,
intrinsic survivor or unresolved case was found.

The two paths share Python and prime-field arithmetic. This remains
finite-computation evidence; the separate critical audit is recorded below.
No universal seed extraction, all-third census, local four-row converse,
t=0 construction or sixteen-event pencil follows. No global count or
challenge-definition gap is closed.

### Separate critical audit, 2026-10-18

Step 2026-10-18-mca-309-nondisjoint-third-critical-audit used the prior
EXPLORE assessment
`drafts/literature/2026-10-18-nondisjoint-third-critical-audit-review.md`
and its exact COVERED_TARGET. The complete proof, both programs and all
actually called helper routines were inspected. Audited L086 and L109
were read in full; their inherited finite-certificate qualifications
are reused, not freshly audited or erased. The supplied assessment's
primary Hall and GRS-shortening extractions suffice for the unchanged
field, distinct labels, unit multipliers and seven deletions. No new
source theorem, mathematical dependency or repair was needed. This is
a REPRODUCTION audit, not a claim of novelty beyond checked sources.

**Complete coverage and bases.** All 756 fourth supports are distinct
members of the exact product of the two pair sets. Intersections are
recomputed against all three fixed supports, giving exactly 254 eligible
cases. The all-case and eligible rank histograms above reproduce. The
independent replay computes greatest-pivot ratio quotients, while the
producer uses least-pivot direct covectors. Each quotient system has
kernel consisting of the two free overlap coordinates and the one g
vector, so changing pivot or nonzero row scaling preserves its row space
and exterior-square kernel. Forward elimination with back substitution,
Gauss–Jordan reduction and column elimination agree on every pivot set.
All 199 full-rank minors have the stated nonzero integer residue. Every
one of the 557 deficient cases has exactly 21-rank basis vectors; their
free-coordinate matrix is the identity and all original-stack residuals
vanish. This proves independence and completeness, not merely membership.
The 1,041 vectors include every incidence-rejected case as well.

Rank over any extension equals rank over F_97: a nonzero rank minor
remains nonzero and every larger minor remains zero. The same basis
therefore spans the extended kernel. All 136 eligible complete bases
have zero entries on every pair not containing label 1. Consequently
every extended tensor is E_1 wedge w. For a nonzero tensor E_1,w are
independent, and their plane contains E_1. No claim of descent of w or
of the original chart is used. This linear identity is the decisive
extension-field certificate; neither rational-point enumeration nor a
solver's missing component could affect it.

**Every gate branch.** Q_1 E_1=0 because 1 belongs to I1. If its plane
has zero projection, audited L109 constructs coefficient representatives
on A1 and contradicts the actual nonpersistent locators. Otherwise its
intersection with ker(Q_1) is exactly the line through E_1. Both the
12-coordinate and the 8-coordinate of that recovery vanish. Since
z1=12 and g_1(12) is nonzero, lambda and the label-8 overlap weight
vanish. This contradiction is homogeneous and applies to any prescribed
original chart, including one whose excluded point is nonprime. The
finite-direction gate cannot turn a zero intrinsic weight into a full
error. This handles all extension-field points, including rank-zero
specializations that are absent at a chosen rational point.

The separate replay checks all 504 charts of the 24 larger kernels,
360 identically empty and 144 nonempty; all four quotient pivots per
row retain both alternatives. At a nonzero p_ab, U wedge V=p_ab*p
makes U,V independent. At a rank-one projection, a nonzero pair
(qU_n,qV_n) gives nonzero H=-qV_n U+qU_n V in its kernel. If all pairs
vanish, the restriction has rank zero and is rejected as above. Thus no
point at projective infinity or exceptional zero pivot is lost. The
original-coordinate change has inverse first coefficient
(D*alpha-C*beta)/(AD-BC), with AD-BC nonzero; the saved finite gate has
the correct signs. No replacement rational chart is selected.

**Polynomial identities and full moments.** Each bivector coordinate,
U,V, quotient image, alpha and beta is homogeneous linear in the three
kernel coordinates. H, the projection minors, recovered-weight
numerators, quotient residuals and moment residuals are homogeneous
quadratic. All g values and inverse denominators are fixed nonzero
field constants. Hence the replay's values at e_i and e_i+e_j recover
every coefficient exactly as stated above, even at probes outside a
particular open chart. This checks polynomial identities, not absence
of solutions by point sampling. The replay checks 16,128 saved identity
certificates and 13,824 determining branch evaluations.

As an additional check, run
`python3 scripts/seven-coordinate/audit_nondisjoint_third.py`
after the two reproduction commands above. This audit supplement imports
neither producer nor replay routines. It forms the complete coefficient
vectors by ordered convolution and verifies the saved array dimensions,
all 4,760 Plucker coefficient vectors for the 136 eligible kernels,
all 24,984 saved basis residuals, all 3,024 chart reconstruction identities,
and all 2,304 row/pivot branches. For every such branch define
lambda=H_z/g(z) and e by (5) of L109. Coefficientwise, H-e=lambda*g
on all sixteen labels, including zeros outside S union K. All eight
shifted moments then vanish coefficientwise. All 110,592 scalar moment
coefficients are checked explicitly, and the first row's lambda and
label-8 weight numerators are zero polynomials in every branch. This
also verifies the all-moment bridge on the larger loci, not just their
isolated rational representatives. Full residual vectors and all larger
case/chart identifiers are saved in
`scripts/seven-coordinate/nondisjoint-third-critical-audit.json`.
The original replay separately verifies the 448 isolated-point row gates
and all 3,584 moment residuals using its direct five-by-three system.

The producer and independent replay were rerun in this separate turn.
Both certificates reproduced byte for byte against the pre-audit hashes
in `drafts/2026-10-18-nondisjoint-third-audit-before.json`; the supplement
records the same hashes. No failure, survivor or unresolved case was
found. These programs share Python and prime-field integer arithmetic;
this audit is not formal proof-assistant verification.

**Equality transfer and scope.** Actual sixteen-count equality is used
before L109's independent lift and at least twelve distinct two-overlap
rows. Thus there exists an actual fourth support different from the
three specified ones. L086 applies to those actual errors before the
pairwise-linear filter. The same nonzero lift wedge must satisfy the
four-row stack, contradicting either full rank or the intrinsic gate
failure. No use of L109's converse with four rows occurs. The only
direct mathematical inputs remain L086 and L109; L111/L112 and
ATTEMPTS/041 are comparison and failure evidence, not premises.

The audit validates precisely this conditional exclusion and changes no
argument or global bound. It supersedes the pending-L113-audit wording
in the unchanged PROOF.md overview. Arbitrary t=0 support profiles,
universal representation and challenge qualifications remain unresolved;
STATUS stays IN_PROGRESS and there is no complete challenge candidate.

## Mathlib

Full matching coverage for this labeled finite gate census is not checked.
The ready assessment reuses the standard coding sources and L109's exact
Plucker reconstruction. No claim of Mathlib absence, formal verification
or mathematical novelty is made.
