# L115 — The unchanged product box passes the full anchored distance-five shell

## Hypotheses

Use L021's canonical rational primal vector a_i, L098's normalized pairs
on the universe V of all 68-subsets of a 1024-point set, and exactly
L112's original positive rational box. Thus

    N=floor(65537^28/2^128)+1, H=binomial(1024,68), rho=N/H>0,
    U=binomial(1024,64)/binomial(68,64),
    g_i=binomial(68,i)binomial(956,i),
    c_0=1, c_1=...=c_4=0,
    c_i=(N-1)a_i/((U-1)g_i) for 5<=i<=68.

For k=i-5, let p_k and q_k be respectively `scale_powers[k]` and
`point[k]` in `scripts/finite-support/positive-factor-enclosure.json.gz`.
The unchanged box is the product of intervals

    [l_i,u_i]=[10^(p_k)(q_k-10^25)/10^70,
               10^(p_k)(q_k+10^25)/10^70], 5<=i<=68.

For any real x in this box use the shared source recipe fixed by
L112–L114: a distinct triple with all three half-distances i,j,h>=5
has normalized value y=x_i*x_j*x_h; a distinct triple with a forbidden
side 1,...,4 has value zero; repetitions with sides (0,b,b) have value
c_b. Singleton value is 1. Homogeneous nonempty moments are rho times
these values. No additional incidence zero is imposed. No full source
PSD, representing measure, global positive-root uniqueness or RS
realization is assumed.

Fix A in V and let S_A={B in V: |A\B|=5}. Consider the union matrix
indexed by {A} and all {A,B}, B in S_A, with each entry the homogeneous
moment of the union of its two indices.

## Conclusion

For every A and every x in the unchanged box, this entire matrix is
positive definite. After division by rho and the positive-anchor Schur
congruence, all 36 shell spectral coordinates sigma_ab satisfy

    sigma_ab/c_5 >= 630869/1000000 > 0,  0<=a,b<=5.       (1)

The minimum of the certified interval lower endpoints occurs at (4,0)
and lies in [630869,630870)/10^6. This is a bound on the interval
certificate, not an assertion about the location of the actual minimum
eigenvalue as x varies. The shell dimension is

    S=binomial(68,5)binomial(956,5)=68643272053310642688.

In particular L112's enclosed root passes this necessary principal
matrix test simultaneously with its scalar and exact-N conditions.
This is a REPRODUCTION of assessed Johnson/tensor/Schur/interval methods,
a local finite pass without an originality claim. It gives no other
source PSD matrix, full SDP feasibility, measure, packing, RS list or
improvement of the 955–957 bracket. The separate critical proof audit
below retains this application; it distinguishes the original arithmetic
verification from the later manuscript and source-normalization review.

## Proof

**Imported results and their scope.** The prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-fixed-product-distance-five-shell-psd.md`.
Import Polak, *Semidefinite Programming Bounds for Constant-Weight Codes*,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), §1.1 (1)–(3),
Proposition 1.1 and its indicator proof, p.2. At order three a singleton
anchor permits all the two-element indices used here; restriction to
the shell is a principal restriction. Use the proved constant-weight
A(n,d,w) conclusion, retaining the source's displayed A(n,d)
qualification in foundations/12. This makes the test necessary for
code indicators, without making a passing trial representable.

Import the simultaneous Johnson relation eigenvalues and complete
multiplicities from Brouwer–Cioaba–Ihringer–McGinnis,
[arXiv:1709.09011v2](https://arxiv.org/pdf/1709.09011v2), §§1.2,3,3.4,
pp.3,10,12. Both factors below satisfy n>=2d with d=5. Import the
complete tensor spectrum, common idempotents and positive-leading-block
Schur congruence from Brouwer–Haemers, *Spectra of Graphs*,
[author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
§§1.4.7,11.2, pp.19,162–163, Theorem 2.7.1(i), p.36. Identity
relations use identity matrices; the Schur congruence inverts only 1.
The inspected coverage is retained in foundations/09. For the independent
normalization check import Schrijver, IEEE TIT 51 (2005), 2859–2866,
DOI [10.1109/TIT.2005.851748](https://doi.org/10.1109/TIT.2005.851748),
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Theorem 1 (51), III.A (52)–(59), III.B (64), pp.6–7; foundations/04
retains the actual-orbit and unused complement-prefactor qualifications.

Import rational interval-expression inclusion from Rump, *Verification
methods: Rigorous results using floating-point arithmetic*, Acta Numerica
19 (2010), 287–449, DOI
[10.1017/S096249291000005X](https://doi.org/10.1017/S096249291000005X),
[corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
§5.5 (5.16)–(5.17), author p.28; foundations/14 retains the inspected
cases including repeated variables. L112 already supplies the root by
its separate strict inclusion theorem. No spectral theorem, root theorem
or interval theorem is reproved here. The new work is their necessary
finite specialization to a different assignment from L054–L056.

**Complete geometric dictionary and entries.** Reuse L054's shell
dictionary: write B=(A\X) union Y and C=(A\X') union Y', with X,X'
five-subsets of A and Y,Y' five-subsets of its 956-point complement.
Let r=5-|X intersection X'| and q=5-|Y intersection Y'|. Every
(r,q) in {0,...,5}^2 occurs, and the four-region stabilizer is transitive
on each such relation. The source coordinates are

    i=j=5, t=5-r, s=5-q, h=r+q,
    D=binomial(5,r)binomial(63,r)binomial(5,q)binomial(951,q).

These are all actual t-s classes in this shell, without identifying
general source variables by distance multisets. Here the equality of
product entries across some classes is part of the specified recipe.
The normalized entry K_rq is exactly

    K_00=c_5,
    K_rq=0 if 1<=r+q<=4,
    K_rq=x_5^2*x_(r+q) if r+q>=5.                      (2)

The first case is the Boolean equality B=C, not a cube. In particular
(r,q)=(2,3) retains its positive product, with none of L054's old
incidence override. The anchor entry is 1 and every anchor/shell entry
is c_5. Thus, with R_r^(n) the relation-r matrix on five-subsets,

    M/rho = [[1, c_5*1^T], [c_5*1, C]],
    C=sum_(r,q) K_rq R_r^(68) tensor R_q^(956).          (3)

This establishes invariance directly for this assignment and every A;
no arbitrary labeled feasible point is averaged or relabeled.

The independent checker constructs actual sets for all 36 relations,
their full eight-atom partitions, and all six ordered presentations.
It recovers each actual (i,j,t,s), its positive D and preserved t-s,
and checks that all six full counts g_i*D equal g_5 times the D above.
For the diagonal, the six presentations include both distinct endpoint
repetitions in an i=5 row (D=1) and the coincident i=0 row (D=g_5).
Every forbidden case uses value zero and capacity zero. Thus null,
repeated and coincident cases are included before spectral reduction.
No complete-source claim outside this shell is inferred from these
representatives; L112–L114 supply that separate coverage.

**Complete spectrum and positive anchor.** With binomials zero outside
their ordinary range, the imported factor values and dimensions are

    E_a^(n)(r)=sum_(v=0)^r (-1)^v binomial(a,v)
                         binomial(5-a,r-v)binomial(n-5-a,r-v),
    m_a^(n)=binomial(n,a)-binomial(n,a-1).

For a=0,...,5 the multiplicities are

    n=68:  1,67,2210,47838,764269,9609743;
    n=956: 1,955,455534,144707330,34440116295,6550452053781.

They are positive and sum to the two layer sizes. All product modes
have multiplicity m_a^(68)*m_b^(956), totaling S. Define

    e_ab=sum_(r,q) K_rq E_a^(68)(r)E_b^(956)(q),
    sigma_ab=e_ab-1_((a,b)=(0,0))*S*c_5^2.             (4)

Indeed, (3)'s positive-anchor congruence gives 1 and C-c_5^2 J;
J/S is the constant projector. The correction affects only (0,0),
including when a lower block might be singular. In the unnormalized
constant vector, the two-by-two block is [[1,S*c_5],[S*c_5,S*e_00]],
whose remaining quadratic coefficient is S*(e_00-S*c_5^2). This
independently verifies the same anchor correction and its normalization.

**Unchanged-box intervals and all signs.** Positivity of all endpoints
gives the exact entry enclosures

    [K_rq]=[c_5,c_5] if r=q=0;
             [0,0] if 1<=r+q<=4;
             [l_5^2*l_(r+q),u_5^2*u_(r+q)] otherwise.

For each integer weight w=E_a^(68)(r)E_b^(956)(q), its contribution
to the lower endpoint of e_ab is w times the entry's lower endpoint
if w>=0 and its upper endpoint otherwise; the upper endpoint uses
the reverse choice. Sum these exact fractions, subtract (4)'s exact
correction, and divide by positive c_5. These operations enclose the
whole box, including repeated variables. No midpoint evaluation or
choice of independent occurrences is used as equality. All 36 resulting
lower endpoints are strictly positive. Their least one is the exact
fraction at `minimum_normalized_lower.value` in
`scripts/finite-support/fixed-product-five-shell-verification.json`.
Exact integer comparisons put that fraction in [630869,630870)/10^6,
at mode (4,0), proving (1).

All exact fractions, including every entry interval, both endpoints of
every mode and the complete minimum fraction, are saved in the two
certificates below. No numerical surrogate is used for a sign. The
positive multiplicities exhaust the shell, so (4)'s complete positive
spectrum and the invertible positive-anchor congruence prove positive
definiteness of (3), hence of M since rho>0.

**Independent complete verification.** Reproduce from this notebook:

    python3 scripts/finite-support/fixed_product_five_shell.py
    python3 scripts/finite-support/verify_fixed_product_five_shell.py

The constructor saves `scripts/finite-support/fixed-product-five-shell.json`.
Its 35 input/normalization/trace checks pass. It binds the original
enclosure, canonical LP and retained L112/L113 and L114 audits, checks
all their stored input hashes, all 64 strict root inclusion margins,
the full original positive box and canonical pair equality. This uses
the existing audited root; it does not rerun or refine a nonlinear solve.

The independent script imports no constructor routine. Its full output is
`scripts/finite-support/fixed-product-five-shell-verification.json`:
759 checks pass with zero failures. It reconstructs all 64 endpoints
and pairs using factorial binomials, the exact N and objective. The
actual-union checks above cover 36 relations and 216 presentations.
Its separately normalized beta expression is

    Etilde_k^(n)(r)=1/binomial(n-2k,5-k) *
      sum_(u=max(k,5-r))^5 (-1)^(u-(5-r)) binomial(u,5-r)
             binomial(n-2k,u-k)binomial(n-k-u,5-u)^2.

Both denominators are positive for all k<=5. All 72 values agree
exactly with the constructor's Johnson eigenmatrix. Both identity
relations, all valencies and all 72 trace-orthogonality identities
are checked. The checker reconstructs every entry and mode endpoint
and multiplicity, including the full constant-mode subtraction.

As an additional interval check it collects, for each h=5,...,10,
the integer coefficient of x_5^2*x_h, then encloses the signed linear
sum in x_h and multiplies its interval by the positive interval for
x_5^2. This independently collected enclosure lies inside the saved
entrywise interval in every mode. All six weighted coefficient-trace
identities vanish exactly; the constant diagonal trace is S*c_5,
and the total anchor correction is S*c_5^2. These are polynomial
identities, not an equality of overestimated interval traces.
The complete failure list, minimum fraction and constant-mode endpoints
were inspected; all load-bearing arrays are consumed in full by the
independent reconstruction, rather than verified from previews or flags.

L054/L055's different exclusions and L056's different shell witness
are unchanged. This pass retains only the prescribed included-anchor
distance-five matrix. Other layers, excluded-anchor PSD, stronger local
distributions, full source PSD, global uniqueness, measures and RS
realization remain open. The original calculation proposed the separate
critical audit completed below.

**Separate critical proof audit (2026-10-23, step 433).** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-23-l115-five-shell-critical-audit.md`.
The audit retains the conclusion without a mathematical repair. This
section supersedes earlier pending-review wording for L115 in the
overview. The argument and direct mathematical inputs are unchanged;
no DAG or overview assembly change is needed. This is a verification
of the finite application of known results, not a new spectral theorem.

The source union-matrix indices satisfy the order-three singleton-anchor
rule. The bijection B=(A\X) union Y exhausts the product of the two
five-set layers. For an ordered pair of shell indices, the head and tail
partitions are determined by r,q, and permutations within A and its
complement act transitively on each partition. Thus representative
entries cover the entire matrix for this prescribed assignment, not
merely selected entries of it. In mask order 0,...,7, with membership
in A,B,C represented by bits 0,1,2, the full atoms are

    (951-q, 5-r, q, r, q, r, 5-q, 63-r).

All 36 saved partitions agree with this formula. All 216 ordered
presentations are checked against the source multinomials: their product
equals g_i*D exactly. The six presentations at r=q=0 include two with
i=0, two with j=0 and two with h=0. They retain the coincident row and
both endpoint repetitions. The Boolean diagonal is c_5; every distinct
forbidden entry is zero; every permitted entry is the positive product,
including (r,q)=(2,3). No old incidence override is imported from L054.

The entire independent verifier was read and replayed to the new file
`scripts/finite-support/l115-critical-reverification.json`. All 759
checks pass, and the whole JSON object equals the original verification
certificate. It reconstructs every field of all 36 modes in the
constructor certificate, all entries, the 64 original endpoints/scales,
canonical pairs, exact N and normalization. It also reconstructs every
factor value by the independently normalized beta formula. The complete
signed interval sums use the upper endpoint for negative weights in a
lower bound. Dependence between repeated factors only enlarges these
enclosures; it is not assumed absent. The second collected expression
checks enclosure without replacing or refining the original box.

An additional direct subset count checks the factor normalization.
Fix k disjoint ordered pairs and a five-set T containing their positive
members, no negative members, and 5-k ordinary points. For a five-set W,
use the signed function product over pairs of
(1_(positive in W)-1_(negative in W)). Nonzero contributions select
exactly one member of each pair. With z negative choices and b ordinary
points of T selected, the intersection size is k-z+b, the relation is
r=5-k+z-b, and the signed number of such W is

    (-1)^z binomial(k,z) binomial(5-k,b)
             binomial(n-5-k,5-k-b).

The remaining 5-k-b points come from the n-5-k points outside T and
all designated pairs. Summing these counts for each r recovers all
six entries of each of the twelve factor rows at n=68,956 and
k=0,...,5. All signed terms are saved. This is a finite normalization
cross-check, not a substitute proof of the imported complete eigenspace
decomposition or its multiplicities. Those positive multiplicities
exhaust exactly S=68643272053310642688 shell indices.

The positive leading scalar is 1 after division by rho=N/H>0. On the
constant vector of squared norm S, the exact congruence with
T=[[1,-S*c_5],[0,1]] transforms
[[1,S*c_5],[S*c_5,S*e_00]] to
diag(1,S*(e_00-S*c_5^2)); both interval endpoints check identically.
All nonconstant modes have zero correction. Thus no normalization by
S, square root or c_5 is missing, and no possibly singular shell block
is inverted. Every normalized lower endpoint is checked against the
explicit manuscript bound, not merely its own computed decimal floor.
The least is the full exact fraction saved at
`minimum_normalized_lower` in the audit certificate, at (4,0), and
lies in [630869,630870)/10^6. All 36 lower bounds are strictly positive.

The retained L112/L113 and L114 audits are reused in their established
scopes. Every stored input/code/replay hash is checked. All 64 retained
lower-minimum rows match the canonical pairs and have zero distinct
residual; every original strict inclusion margin is retained. Their
complete relevant proof cases were inspected, without repeating the
already completed root or global scalar audits. The shell assertion is
box-wide; simultaneous exact-N feasibility is asserted only at the
enclosed root. The two statements are not interchanged.

Reproduce the audit without changing any original artifact:

    python3 scripts/finite-support/critical_audit_l115.py

The full additional certificate is
`scripts/finite-support/l115-critical-audit.json`: 478 additional checks,
zero failures, complete signed subset counts, every normalized lower
endpoint and exact minimum, all input hashes and the replay hash.
The whole two original shell certificates are consumed by the replay
and equality comparison. Full selected fractions and failure lists
were inspected; previews and saved success flags are not the proof.
No solve, scan, retuning, box refinement or other-shell test was used.
The audit verifies precisely this necessary principal matrix. Full
source PSD, stronger distributions, global root uniqueness, measures,
packing, RS realization and arbitrary-center safety remain unresolved.

## Mathlib

Full matching Johnson/product/Schur/interval application: not checked.
Supporting finite-set counts, spectral decompositions and rational
interval inequalities: not checked. Unknown coverage is not absence;
no uninspected Mathlib theorem is used.
