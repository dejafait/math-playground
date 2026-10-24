# L114 — The unchanged product box passes all Boolean lower scalar rows

## Hypotheses

Use exactly L105's fixed pairs c_i and L112/L113's unchanged positive
rational box, with n=1024, w=68, d=10 and
N=floor(65537^28/2^128)+1. In particular c_0=1,
c_1=...=c_4=0 and 0<c_i<=1 for 5<=i<=68. The rational vector,
scales and box are precisely those defined in L112; none is retuned.

For every actual source orbit (i,j,t,s), put h=i+j-t-s. Define one
shared source value y as follows. For three distinct supports whose
three sides are at least five, set y=x_i*x_j*x_h for any x in that box.
For a distinct triangle with a side in {1,2,3,4}, set y=0. For a repeated
triple with sides (0,b,b), in any order, set y=c_b. Thus y=1 for the
all-equal triple. Retain all actual t-s classes, all six presentations,
both endpoint repetitions, coincident and null cases. These are source
coordinates: the homogeneous moments are (N/H)y, H=binomial(1024,68),
as in L098; y is not a raw Boolean probability.

## Conclusion

For every such orbit and every presentation with anchored sides a,b,

    1+y-c_a-c_b >= 0.

Together with L113, this assignment satisfies every ordinary source
scalar row, permutation equality and forbidden-distance zero. At L112's
enclosed root it also satisfies all 69 exact-N contractions. The lower
row verdict holds throughout the unchanged box; the contractions are
asserted only at the enclosed root.

This is a REPRODUCTION, a local specialization of the assessed source
rules and existing finite evidence. It is not a new general theorem or
a claim beyond the sources checked. Full source PSD, stronger local
distribution constraints, global positive-root uniqueness, a representing
measure, a packing and RS realization remain unresolved. The 955–957
bracket is unchanged. The separate critical review below retains this
implication and its consumed L105 evidence; there is no complete candidate
resolution.

## Proof

**Source and reused coverage.** Import Schrijver, *New code upper bounds
from the Terwilliger algebra and semidefinite programming*, IEEE TIT
51 (2005), 2859–2866, DOI
[10.1109/TIT.2005.851748](https://doi.org/10.1109/TIT.2005.851748),
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (62)–(65), especially (65)(ii), and its justification, manuscript
p.7. Its hypotheses are a nonempty binary constant-weight code;
(n,w,n-w,d)=(1024,68,956,10) satisfies the local specialization.
The constraints are necessary conditions, with no sufficiency claim.
Use only actual orbits, without the qualified complement prefactor in
(61). Foundations/04 and the prior SPECIALIZE assessment
`drafts/literature/2026-10-23-fixed-product-boolean-lower-rows.md`
record the inspected coverage. No source theorem is reproved here.

L105 already specializes all six presentations to the scalar interval

    ell=max(0,c_i+c_j-1,c_i+c_h-1,c_j+c_h-1),
    upper=min(c_i,c_j,c_h).                            (1)

It verifies every actual interval, including forbidden and Boolean
entries, and proves the exact minimum row sum L_i=2c_i for every
i>=5. The row coefficients are positive integers

    D=binomial(i,t)binomial(68-i,j-t)
      binomial(i,s)binomial(956-i,j-s).

For forbidden entries its final lower endpoint is zero; for repetitions
it is the forced value c_b. The verified nonempty interval means these
forced values satisfy every row of (1). These statements include all
1,500,625 actual ordered entries and all six presentations. They are
reused with exactly the same pairs, not inferred from model memory or
from a preview of the certificates.

**Permitted distinct entries: pointwise consequence of a row minimum.**
Fix any actual orbit with i,j,h>=5 and three distinct supports. In its
row i, the two repeated third supports have D=1 each, value c_i each,
and thus total lower-endpoint contribution 2c_i. Every other final
lower endpoint is nonnegative and every D is positive. Consequently
L105's identity implies

    sum_(Z distinct from A,B) D*ell_final = L_i-2c_i=0. (2)

This finite sum has only nonnegative summands. Hence each summand is
zero. At the selected permitted distinct entry ell_final is precisely
ell in (1), without a forced-value override. Thus ell=0 there, which
means every pair sum among c_i,c_j,c_h is at most one. Since the
unchanged positive box gives y=x_i*x_j*x_h>0, every lower row has
slack 1-c_a-c_b+y>=y>0. This argument is pointwise; it does not assemble
independently chosen row minimizers into a shared witness. The shared
witness was already fixed in the hypotheses.

**Null and repeated cases.** A distinct triangle with a forbidden side
has y=0. L105's verified forced-zero interval gives ell<=0 in (1),
so each pair sum is at most one and each lower row has nonnegative
slack. This covers triangles with one, two or three null sides, without
division by any c_i. Do not infer this case from (2) with an overridden
lower endpoint; its input is L105's separate interval-validity check.

For sides (0,b,b), y=c_b. An anchored pair of sides 0,b has lower
slack 1+c_b-c_0-c_b=0. The remaining pair b,b has slack 1-c_b>=0.
For b=0 the all-equal value is one and every slack is zero. These
computations also cover forbidden b, when c_b=0. Both distinct endpoint
repetitions in a positive-distance row are retained; the coincident
row is a Boolean row rather than a distinct-edge equation.

These cases exhaust all actual triples. Formula (1) already includes
each of the six presentations, even when side indices repeat. Thus
the lower-row assertion holds without any additional orbit scan or
box comparison. L113 supplies all upper rows at this same box;
nonnegativity and distance zeros follow from its shared construction.
Products are symmetric, and repeated and null values are likewise
presentation independent. L112 supplies the root and contractions,
with L098's normalization restoring repetitions and the i=0 objective.
No PSD or representing-measure implication is used.

**Bounded evidence binding.** Reproduce the input-binding and minimum-
identity check from the notebook:

    python3 scripts/finite-support/fixed_product_lower_implication.py

The full certificate is
`scripts/finite-support/fixed-product-lower-implication.json`.
It records SHA-256 hashes of the L105 constructor and verification,
unchanged enclosure, upper-capacity verification, joint audit and
canonical LP data. It checks every input hash stored in the L105
constructor and joint audit and L105's verifier-to-constructor binding.
It reconstructs c_i from the exact LP data, checks equality to both the
L105 and L112 vectors and the same N, and checks 0<=c_i<=1.
For all 64 rows it checks the complete saved exact identity L_i=2c_i
and both D=1 repetitions. All 88 checks pass with no failures; actual
distinct lower sum is zero, meeting required zero. This small check
does not repeat L105's full orbit verification or the L112/L113 audit;
those are mathematical inputs with their existing qualifications.
It binds their unchanged evidence and checks the identities consumed
by (2). The source proof and the case split above, rather than the
hashes or saved outcome flags, justify the new lower-row conclusion.

**Separate critical review (2026-10-23, step 429).** The prior SPECIALIZE
assessment is
`drafts/literature/2026-10-23-l114-lower-implication-critical-audit.md`.
The review retains the conclusion without changing any mathematical
input or repairing an inference. It closes the pending review of this
implication, including precisely L105's consumed interval/minimum claims.
It supersedes historical pending-review wording for L114 in the overview;
it does not complete L105's separate review of its unrelated upper-capacity
optimum and attainment argument. No new theorem beyond the assessed
specialization is claimed.

The source normalization was checked against foundations/04 and L098's
homogeneous conversion. The scalar lower row is conditional on the anchor
normalization: it is 1+y-c_a-c_b, not a row with unnormalized singleton
N/H substituted for 1. Multiplication by N/H>0 gives the homogeneous
row. The prescribed source assignment is shared across all six
presentations before any lower-row deduction. Its symmetric products
may coincide across additional t-s classes by choice, without treating
those coincidences as source-required identifications.

The complete independent L105 verifier was read and replayed, with no
constructor or search. Its eight atoms are nonnegative, sum to 1024,
and each of the three words has size 68. For each permutation of the
bits x,y,z, atoms[x]+atoms[x|z] counts X\Y, atoms[x]+atoms[x|y]
counts X\Z, and atoms[y]+atoms[x|y] counts Y\Z. The intersections
are atoms[x] and atoms[y|z]. Thus the reconstructed six pairs of
anchored sides really supply every required lower and upper inequality,
preserving t-s even with repeated distances. Their maximum lower
endpoint starts at zero. Crucially, the verifier checks the raw
lower<=0<=upper inequality for every forbidden entry *before* replacing
both endpoints by zero. It likewise checks the raw Boolean interval
before replacing its endpoints by c_b. Permitted distinct endpoints
are never overridden. The overlap of forbidden and repeated cases is
valid: its forced c_b is already zero. The all-equal case is Boolean
and has value one.

For every original entry the verifier independently computes the two
source multinomials and divides their product by g_i. Factorial
cancellation gives exactly D, and the checked positive integer D agrees
with the saved four-region factors. Complete t,s ranges, every h
record, every shell count g_j and every row total H are reconstructed.
The only repeated third supports in each i>0 row are Z=A,B, with D=1
each. At i=0 they coincide, D=g_j and the row is the objective identity;
no two-repetition subtraction is applied there.

Reproduce the bounded audit from the notebook:

    python3 scripts/finite-support/critical_audit_l114.py

The new full replay certificate is
`scripts/finite-support/l105-l114-critical-reverification.json`.
All 30,071,176 exact comparisons pass, covering 1,500,625 ordered entries,
9,003,750 presentations, 205 repeated entries and 10,232 entries with
a forbidden side (including 12 repeated entries). Every mathematical
field equals its original saved counterpart. The original verifier's
historical start timestamp is refreshed only in memory, so its runtime
check measures the present replay, not a new combined constructor/replay
run. The old certificate and every mathematical input are unchanged;
only elapsed time and peak memory are excluded from the equality check.
No original resource measurement is reasserted on that basis. The saved
check count is 30,071,176; the verifier prints 30,071,177 because it
performs one final output-size check after writing the certificate. That
last check also passes and does not add a mathematical interval check.

The 88-check binding/minimum verifier is also replayed to
`scripts/finite-support/l114-critical-binding-reverification.json`,
which agrees in full with its saved original. A further 146 checks bind
all inputs and replays, verify strict positivity of all permitted c_i,
and check every reconstructed lower sum and repetition pair. For each
of the 64 permitted rows the integer residual is exactly

    reconstructed_lower_numerator - 2*pair_numerator = 0,

with a positive common denominator. The required residual is zero.
The full audit, including every residual, input/output hashes, clock
adaptation and empty failure list, is
`scripts/finite-support/l114-critical-audit.json`. Full relevant arrays
are consumed by the reconstruction and comparison; previews and flags
alone are not the verification.

Finally, equation (2) is a finite nonnegative-sum argument. Each permitted
entry has a positive D and its original lower endpoint is its final one,
so that endpoint is zero. No row interpolation or independent-row
attainment is used to infer shared feasibility. Null entries instead use
the separately verified raw intervals. Repeated entries have lower
slacks 0 and 1-c_b, including null b and coincidence. These cases exhaust
the original orbits. L112/L113's retained joint review supplies the
unchanged positive box and all upper rows, and its root supplies the
contractions after restoring repetitions. Thus the lower assertion is
box-wide, while exact-N feasibility is asserted at the root only.
Full PSD, stronger local distributions, global uniqueness, measures,
packing and RS realization remain independent gaps. The mathematical
argument and direct inputs are unchanged, so no DAG or overview assembly
change is needed. ATTEMPTS/082,093 retain their original scopes.

## Mathlib

Full matching fixed-box scalar/cardinality application: not checked.
Supporting finite nonnegative sums and rational inequalities: not
checked. Unknown coverage is not evidence of absence. No uninspected
Mathlib theorem is used.
