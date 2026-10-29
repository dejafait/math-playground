# L154 — Audited twelve-row finite-field certificate contract

## Hypotheses

Fix F=F_(97^20), H={1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96},
S={1,8,12,18,22,27,33} and J=H minus S. Use L153's complete original
pair registry and nine-dimensional kernels, and L109's quotient matrices,
shortening polynomials, shifted moments and prescribed-chart recovery.
Every variable below ranges over F; no prime-field descent is assumed.

For the necessary equality implication only, retain C152a/L086/L109's
represented t=0 class: k=8, pinned 1/4<=delta<5/16 cell, both coefficient
syndromes in U_S, sixteen original finite events, actual D and every
locator nonzero as polynomials, arbitrary original coefficients/weights
and chart. Retain all their L056/L069/L040 and L051/L055 finite-certificate
qualifications. These are conditional imported inputs, not independently
replayed here. For the selected-recovery converse, assume only a solution
to a branch of the formula specified below; polynomial nonpersistence
is then a conclusion. There is no assumption of an equality example.

## Conclusion

The explicit finite formula below has 282 unknowns and 703 generator
entries per branch, over all 79,380 registered pairs and 21 nonzero
Plucker pivots. Every actual configuration in the stated represented
t=0 class supplies a solution in at least one branch. Conversely a
solution gives twelve distinct full-weight selected recoveries, in its
encoded original finite chart, with linear supports, maximum label
degree four, all eight moments, full activity and actual polynomial
nonpersistence. It gives neither sixteen events nor t=0 nor equality.
Fixing external original coefficients requires the fourteen extra
stated equations; the resulting variant has 717 generators.

The specified nonfield degrees are at most 50; field equations have
degree 97^20. A shared arithmetic circuit for the generators has at
most 907,486 gates per branch. These are representation upper bounds,
not solver or polynomial-multiplier bounds. No positive point, branch
emptiness or uniform exclusion is established. The frozen interval
11/q–16/q and independent challenge gaps are unchanged.

## Proof

### Imported results and unchanged scope


Use L109's entire gated recovery statement, including its independent
audit, and L153's complete nine-dimensional kernels after scalar
extension. C152a supplies some disjoint actual pair, with no numeric
pair specified. L086 supplies linearity and degree at most four on
restriction; L109 supplies 12<=r<=14 actual two-overlap supports.
Their inherited hypotheses listed above are essential to this inclusion.
L104's local positive examples and L151's labeled exclusion are contrasts,
not premises for a uniform exclusion. The failed routes listed above
are not rerun. The already completed comparison in
`drafts/literature/2026-10-25-twelve-row-gated-feasibility-review.md` found no
completed matching simultaneous specification and noted the L123 duplicate.

The finite-field certificate input is S. Gao, A. Platzer and E. M. Clarke,
*Quantifier Elimination over Finite Fields Using Gröbner Bases*, CAI 2011,
LNCS 6742, pp. 140–157, DOI 10.1007/978-3-642-21493-6_9,
[author PDF](https://symbolaris.com/pub/QEfin.pdf), Theorem 2.2 p. 143
and its radical-ideal proof pp. 143,156. Every variable is constrained
to F_Q by X^Q-X, Q=97^20. Theorem 4.1 and Lemmas 4.1–4.2 cover
finite-formula conversion, including nonzero atoms. Here explicit
inverse witnesses and Boolean bit lookups give a conjunction directly;
no auxiliary source disjunction variable is presumed Boolean. The
source's Theorem 5.2 p. 150 provides no practical complexity guarantee.
This is a REPRODUCTION specialization of that machinery and L109,
not a new algebraic theorem or a claim of originality.

L109 retains the exact coding imports: J. I. Hall, *Notes on Coding
Theory*, [Theorem 5.1.1, pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf);
I. Marquez-Corbella–R. Pellikaan, accepted manuscript 2016-02-29,
[section 5, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2, Lemma 5.3 and following GRS shortening formula.
Sixteen distinct labels, unit multipliers, dimension eight and exactly
seven shortening deletions meet the recorded hypotheses. No distance,
shortening, exterior-power or finite-field certificate theorem is
reproved here. L109's explicit all-rank reconstruction is used as given.

### Exact finite formula

All coefficients of the uniform-existence formula lie in F_97; every
unknown lies in F=F_Q. In the externally fixed-coefficient variant, the
additional constants u*,v* may instead lie anywhere in F_Q.
Use the exact ordered H, S, J, support universe and coordinate ordering
of L153. Write A_a=I_a union K_a for 0<=a<756. Fix one of its
79,380 unordered disjoint registered pairs (a_1,a_2), a_1<a_2.
Let B_1,...,B_9 be its saved complete kernel basis in exterior
coordinates. This is a family indexed by every pair, not one common
kernel or an identification under permutations. The specification needs
no new read or replay of all 79,380 records: it uses their established
L153 contract. A future instance checker must bind its particular record
to the original two blocks and verify its complete basis as described
in the certificate contract below.

#### Plane and arbitrary original chart

Choose a chart a<b in the seven S-coordinates. There are 21 choices.
Use nine unknowns theta_i and define p=sum_i theta_i B_i, extended
antisymmetrically with p_xx=0. Impose

    p_ab=1,
    p_ij p_kl - p_ik p_jl + p_il p_jk=0  (i<j<k<l in S).

There are 35 quadratic Plucker equations. Define U_x=p_xb, V_x=p_ax.
L109's reconstruction gives U wedge V=p, with U_a=1, U_b=0,
V_a=0, V_b=1. In particular these vectors are independent. No kernel
rank is deleted and no rational descent is imposed.

Use four further unknowns m11,m12,m21,m22 and one inverse witness d:

    u=m11 U+m12 V,   v=m21 U+m22 V,
    d (m11 m22-m12 m21)-1=0.

The ordered pair (u,v) is the encoded original affine basis; the finite
pencil is u+T v. It is not replaced by (U,V). All invertible changes
over F, including charts whose omitted direction is not F_97-rational,
are retained. Each actual original basis has unique such coefficients
in U,V. There is no normalization gamma_1=0 or gamma_2=1.

If externally supplied original coefficients u*,v* are to be held fixed,
add the fourteen equations u_x=u*_x, v_x=v*_x. Alternatively specify
their known invertible matrix m directly. The counts below are for the
uniform existence formula with m variable. Its emptiness excludes all
original charts; a point certifies its encoded chart only, and may not
be reported as a point for some other externally prescribed chart.
The externally fixed-coefficient variant has 717 rather than 703
equations, with the same 282 unknowns and no higher nonfield degree.

#### Twelve distinct selected supports, retaining the pair

Slots s=1,2 have the fixed pair supports. For each s=3,...,12 use ten
unknowns b_s0,...,b_s9 with b_si(b_si-1)=0. For 0<=a<756 let

    delta_sa = product_(i=0..9) [b_si if bit_i(a)=1, else 1-b_si].

Here bit_i(a) denotes an ordinary integer binary digit of the registry
index, never its residue modulo 97. Require sum_(a=0..755) delta_sa=1.
On Boolean assignments exactly one of the 1,024 ten-bit words matches;
this equation keeps precisely the 756 legal indices. It is not a
cardinality equality for 756 independent Boolean selectors. Invalid
codes 756–1023 give zero on the left, not a congruent large count.

For any table T_a define its slot value by sum_a delta_sa T_a;
for slots 1,2 take the literal table value. Use the following 51
table entries per slot, always with the original H labels:

* D_sx=1_(x in A_s), x in H (16 entries);
* G_sx=g_(K_s)(x), x in S (seven entries);
* Q_s: L109's original four-by-seven covector matrix (28 entries),
  with z=min(S minus I_s) and increasing remaining x-coordinate order.

For every s<t among the twelve slots put

    c_st=sum_(x in H) D_sx D_tx,       c_st(c_st-1)=0.

For every x in H put n_x=sum_(s=1..12) D_sx and require

    n_x(n_x-1)(n_x-2)(n_x-3)(n_x-4)=0.

Each selected support is a four-set. Thus c_st is the image of an
integer in 0..4 (the looser bound 0..16 also suffices), and n_x is
the image of an integer in 0..12. These ranges are strictly below
97. The equations therefore mean exactly c_st<=1 and n_x<=4 as
integer conditions. Equal supports would give c_st=4 and fail;
distinctness is included. The fixed pair's c_12=0 equation is retained
as a redundant zero generator in the counts. No sorting or symmetry
identification of the remaining slots is used.

#### Finite recovery, projection and weight gates

For each slot use unknowns gamma_s, lambda_s, its inverse l_s,
seven weight-inverse witnesses w_sx (x in S), and four witnesses
eta_sr (r=1,...,4). That is fourteen unknowns per slot. Put

    E_sx = u_x + gamma_s v_x - lambda_s G_sx   (x in S).

Require the following sixteen equations per slot:

    (1-D_sx) E_sx=0                         (seven equations),
    lambda_s l_s-1=0                        (one),
    D_sx (E_sx w_sx-1)=0                    (seven),
    sum_(r=1..4) eta_sr (Q_s v)_r -1=0       (one).

At legal support selections, the first seven impose precisely the
five shortening equalities on S minus I_s. The weight equations
impose precisely the two nonzero I_s-weights, leaving the other five
witnesses free. The two K_s-weights are -lambda_s g_(K_s)(k),
nonzero since lambda_s!=0 and each table value there is nonzero.
Neither zero lambda nor either canceled overlap weight is divided
out silently: each fails an explicit inverse equation.

The first equations imply Q_s(u+gamma_s v)=0. Since u,v are
independent, this implies rank(Q_s on span(u,v))<=1 and all six
L109 exterior-block equations N_s p=0; the nonzero determinant of
m only rescales u wedge v relative to p. These exterior equations
are consequences, not six additional generators in our count.
The last equation is equivalent to Q_s v!=0: choose an inverse
on any nonzero coordinate, with the other eta values zero. Together
with Q_s u=-gamma_s Q_s v it forces rank exactly one.

This covers all four possible nonzero projection pivot coordinates,
including overlaps, without choosing a preferred pivot or dropping a
deficient branch. There are 4^12 possible independent choices if one
were to expand these witnesses as pivot disjunctions; the formula
does not expand them. Rank zero is deliberately rejected under L109's
actual nonpersistence hypothesis, not alleged impossible for arbitrary
relaxed planes. A rank-one row whose sole recovery is the original
infinite direction has Q_s v=0 and Q_s u!=0, and fails the finite
shortening equations. Thus finite-direction gating is enforced in the
encoded original basis. No convenient new omitted point is chosen.

Finally append X^Q-X=0 for all 282 unknowns, including the bits
(redundantly). These are F_Q equations, not X^97-X equations.
No row variables, theta coordinates or chart coefficients are
restricted to the prime field.

### Necessity and exactly what a point recovers

Take any actual configuration in the retained represented t=0 equality
class. C152a selects a disjoint actual pair; it is one of L153's
registered pairs. Of the r actual two-overlap supports, 12<=r<=14,
choose ten others. This retains the pair even when r=12. L086's
linearity and degree bounds pass to this subfamily. The arbitrary
ordering of those ten slots is allowed by the selectors.

Let u0,v0 be the actual lift coefficients, independent by L109.
Their nonzero wedge p0 belongs to the complete pair kernel. Choose
p0_ab!=0 and set p=p0/p0_ab. L153's basis over F expresses p in
the theta coordinates, including every extension-field point.
L109 reconstructs U,V; the actual u0,v0 give an invertible m, so
take u=u0,v=v0, not a substituted affine chart. The actual gamma_s
and lambda_s pass the shortening and full-weight tests. L109
nonpersistence gives projected rank one; because its actual finite
vector is u0+gamma_s v0, Q_s v0 cannot vanish (otherwise Q_s u0
would also vanish). Hence the eta witnesses exist. All inverse
witnesses and all field equations hold. This proves inclusion of
every original equality configuration in the retained represented t=0
class at this fixed H/S in at least one branch.

Conversely, a point of any branch decodes twelve legal distinct
supports of degree at most four, with pairwise intersections at most
one, and a common independent u,v over F. For every slot the gates
are exactly L109's rank-one, nonzero lambda, two nonzero overlap
weights and prescribed finite-chart gates with h_s=u+gamma_s v;
its original coefficient alpha_s is one. L109 gives the full error

    e_s(i)=E_si (i in I_s),
    e_s(k)=-lambda_s g_(K_s)(k) (k in K_s),
    e_s(x)=0 otherwise.

All eight moments agree. The directions, and therefore the finite
gamma_s, are distinct: equality of a parameter would give two full
weight-four errors with the same syndrome; sparse moment uniqueness
would make their distinct supports equal. This uses L109's established
recovery/uniqueness, not a new generic incidence theorem.

There are twelve rows and degree at most four, so every coordinate
is omitted somewhere. L109's converse supplies actual polynomial
nonpersistence, full activity of S and twelve original finite bad
events for the pencil obtained by extending u,v by zero off S.
For externally fixed words a*,b* with the same coefficient syndromes,
the same moment polynomials and conclusions apply. No assertion that
the original words themselves are supported on S is needed.

This converse does NOT supply sixteen events, their remaining degree
balances, t=0, or equality. A selected-row point is not a t=0 example.
Absence of points in every branch would exclude represented t=0
equality at this fixed H/S, conditional on the inherited inputs.
Such absence has not been tested. Neither implication resolves
arbitrary representation, other supports/fields, radii, the July
ABF26 definition, or identification with the grand challenge.

### Independently checkable certificate contract

Each future branch artifact must identify the pair indices, pivot a,b,
support ordering, Q, H/S and the exact formulas above. Bind the input
pair to L153's original record; verify the two original six-row blocks
from the g-values, a nonzero original twelve-by-twelve minor, all nine
saved null vectors against all original rows, and an identity matrix
on their free coordinates. This gives completeness, not just a null
subspace. Retain the exact labels; equal ranks do not transfer loci.
These are future input checks, not new census executions in this step.

A positive certificate specifies an exact common field presentation,
all 282 values, the decoded indices and all residuals, with no
floating point tolerance. One possible presentation is
F_97[Z]/(m) with monic irreducible m of degree twenty, each element
stored as twenty residues. Irreducibility must actually be certified,
not assumed from the degree or from a software constructor's name.
A brute-force fallback verifier can divide m by every monic polynomial
of degrees one through ten and require every remainder nonzero; any
reducible degree-twenty polynomial has such a factor. This is a finite
verification contract, not a suggestion to run that expensive fallback.
The standard uniqueness of a finite field of a given order identifies
this presentation with F; the embedding of F_97 is the prime subfield
embedding. No extra descent hypothesis is introduced. A checker then
evaluates every generator exactly and independently reconstructs the
twelve full errors and all eight syndrome residuals. The latter
residuals are redundant but make positive-certificate scope explicit.
No such positive artifact or field modulus is supplied this turn.

An emptiness certificate for a branch is a finite list of polynomials
H_i in the same polynomial ring satisfying the exact identity

    1 = sum_i H_i f_i,

where the f_i are all its specified generators, including field
equations. Gao–Platzer–Clarke Theorem 2.2 supplies the finite-field
unit-ideal criterion; no Gröbner basis search or theorem reproof is
needed to state it. A checker expands or otherwise exactly verifies
the complete polynomial identity. Truncated coefficients, a time-out,
a nonzero remainder on a partial basis, or unverified numeric search
are not certificates. A circuit representation of generators is allowed,
but a circuit-evaluation preview is not a proof of a polynomial identity;
the verifier must certify the whole identity in the polynomial ring.
There is no claimed bound on degrees or size of the multipliers H_i.

Uniform emptiness requires a certificate for every pair/chart branch,
or a complete checkable aggregate identity with its selector coverage
proved. Checking a prefix is insufficient. Identities after removing
field equations would instead exclude solutions over every extension,
a stronger assertion. A proper ideal without the field equations
does not certify a point over F_Q. Even with field equations, an
unverified claim of properness is not a positive certificate.

### Size derivation and bounded checks

This counts a shared arithmetic-circuit representation of generators,
not their expanded monomial lists or the unknown-size H_i certificate.
All lookup expressions are substituted polynomials, not new unknowns.

| Unknowns per branch | Number |
| --- | ---: |
| Complete-kernel coefficients | 9 |
| Original-chart matrix and determinant inverse | 5 |
| Ten support slots times ten Boolean bits | 100 |
| Twelve slots times fourteen recovery witnesses | 168 |
| Total | 282 |

| Equations per branch before field equations | Number |
| --- | ---: |
| Boolean bits; legal support codes | 100 + 10 |
| Normalized pivot; Plucker; chart invertibility | 1 + 35 + 1 |
| All slot pairs; sixteen label degrees | 66 + 16 |
| Twelve slots times sixteen recovery gates | 192 |
| Total | 421 |

Add 282 field equations: **703** generator entries per branch,
including redundant entries. There are 79,380*21=**1,666,980**
pair/chart branches, not 21 distinct planes or symmetry classes.
Naively materializing every branch gives 470,088,360 variable
occurrences and 1,171,886,940 generator entries. Sharing templates
is possible; these are not lower bounds on any alternative encoding.
The ten unordered-free slots admit 756^10 =
60,984,287,617,695,474,350,923,186,176 ordered assignments before
incidence and row gates, not that many feasible families.

The bit indicators have degree ten. The D/G/Q lookup entries
have degree at most ten, p/U/V degree one, and u/v degree two.
Shortening gates have degree at most 21; overlap-weight gates 22;
projection gates 13. Incidence gates have degree at most 40;
label-degree gates at most 50. All other nonfield generators have
degree at most ten or three, apart from these listed bounds.
Thus nonfield degree is at most 50. Field generators have degree

    Q=5,437,943,429,267,472,574,499,737,549,036,572,950,401.

Sparse/circuit storage of X^Q-X does not make that degree small.

Here is an explicit arithmetic-gate upper bound, counting scalar
multiplications, additions and subtractions, and sharing each indicated
expression inside a branch. Form all ten bit complements per free
slot (100 gates), then all 756 product indicators per free slot with
nine products (68,040). Form 51 lookup entries per slot by 756 scalar
products and 755 additions each (770,610), allowing zero coefficients
to cost a gate. Sum legal indicators and subtract one (7,560).
Compute the 21 kernel coordinates with nine scalar products and
eight sums (357), allow fourteen sign gates for U,V, and form both
chart vectors (42). Boolean gates cost 200; pivot one; Plucker 175;
determinant inverse five. Each pair incidence gate costs at most
16 products + 15 sums + subtraction + product = 33 (2,178 total).
Each degree gate costs 11 sums + four subtractions + four products
= 19 (304). Per coordinate form E and (1-D)E with six gates
(504); reuse E for D(Ew-1), three gates (252). Lambda inverse
gates cost 24; twelve rank-one witness gates cost 12*(52+8)=720.
This totals 851,086 gates before field equations.

The order Q has 132 binary digits and 69 set bits. Binary powering
uses 131 squarings and 68 other products per variable, followed by
one subtraction, hence 282*200=56,400 further gates. The total
explicit upper bound is **907,486 arithmetic gates per branch**.
It is not an operation bound for solving or for verifying arbitrary
multiplier certificates. No straight-line flattening is performed;
if a future implementation adds gate variables, its variable and field
equation counts must be recalculated rather than using 282/703.

Reproduction command:

    python3 scripts/seven-coordinate/twelve_row_specification_size.py

Full arithmetic and elementary encoding evidence is in
`scripts/seven-coordinate/twelve-row-specification-size.json`.
The program enumerates all 1,024 ten-bit words, checking every
indicator and recording the selected code (or empty illegal code),
and checks incidence/degree residues for every integer 0..16.
All 1,024 code checks and 17 integer-gate checks passed; zero
failures. It records the complete count derivation and qualifications.
It neither loads pair kernels nor computes compatible configurations.
The all-code identity and exact-integer arguments above, not a sample
or preview, establish the elementary selector/gate semantics.

### Separate critical audit — step 478, 2026-10-25

Verdict: PASS for the specified conditional inclusion, selected-recovery
converse and size bounds. This canonical record preserves the mathematics
of step 476's specification following a separate invocation-start approved
RESEARCH / REPRODUCTION audit, under
`drafts/literature/2026-10-25-twelve-row-specification-critical-audit-review.md`.
No new obstruction, originality or progress beyond the checked sources
is claimed. One coefficient-field qualification in the draft is corrected
below; no missing branch or count defect was found. The historical draft is preserved. L153's complete-census
certificate remains an imported finite-computation input; this audit
checks its contract, not all of its stored pair matrices anew.

**Selection and all branches.** The 756 supports are exactly the two-plus-two
sets in the original registry. A legal ten-bit word selects precisely its
integer index, so every lookup uses one common row's D, G and Q entries.
A Boolean equation over F has only the roots zero and one. In each lookup
product, a mismatching digit makes the product zero, and matching all ten
makes it one. Illegal words have no matching registry index and fail
validity. Thus no characteristic-97 cardinality alias occurs. Pair
intersections are integers from zero to four; label degrees are integers
from zero to twelve. Their images in F are distinct, so the indicated
root polynomials enforce exactly the claimed integer restrictions.
Repeated supports fail at intersection four. No assumption of regularity,
nonisolated labels or distinct bits between slots is inserted.

C152a supplies some unordered pair in the complete registry. There are
at least twelve actual rows, so two fixed pair slots plus ten distinct
others are always available. No labeled pair or slot sorting is forced.
The 21 choices cover every nonzero wedge. For a normalized pivot,
the 35 increasing-index relations imply the same relations for any
ordering by antisymmetry; cases with repeated indices are automatic.
Consequently the reconstruction covers all p with p_ab=1. The full
invertible matrix m retains every original ordered basis. The determinant
is not constrained to one: u wedge v=det(m)p. This also explains why
normalizing p loses neither scalar nor original chart. No pair/kernel
symmetry or prime-field rationalization is used.

**Finite recovery and excluded strata.** Each row's five off-I equalities
are h=lambda*g on S minus I. They imply Qh=0 because g(z) is nonzero.
The eta equation is soluble exactly when Qv has a nonzero coordinate;
choosing its inverse gives witnesses for every such coordinate, including
multiple simultaneous nonzeros. With h=u+gamma*v this gives precisely
rank one and a finite intersection line. An actual finite row must have
Qv nonzero: otherwise Qh=0 forces Qu=0, contradicting L109's actual
rank-zero exclusion. Conversely the explicit eta equation rules out
rank zero. If the unique intersection is the original infinite direction,
Qv=0 and Qu is nonzero, so no finite gamma passes. Changing m is allowed
only in the uniform chart-existence formula; external words require the
extra fourteen coefficient equations. Those equations constrain only
their unique S-supported syndrome lifts, and do not assert that the
external words themselves have support in S.

Both I-error weights and lambda have inverse witnesses; the two K-weights
then are nonzero because g does not vanish on K. For a solution, extending
h by zero off S yields h-e=lambda*g at every label of H: check I, S minus I,
K and J minus K separately. L109's imported shortening/moment identity
therefore restores all eight moments. If two finite parameters coincide,
their full errors have equal syndromes and their difference is supported
on at most eight labels. L109's sparse uniqueness makes the errors equal,
contradicting distinct supports. For proportional h vectors the same
argument after nonzero scaling gives distinct projective directions.
Every coordinate is omitted by some row since twelve exceeds four;
L109's converse applies with r=12 to prove actual polynomial nonpersistence
and full activity. It does not supply missing events or t=0. This is
exactly the stated converse, not challenge equivalence.

**Independent recount and its evidence.** The support count is
binom(7,2)binom(9,2)=756. Choosing four labels in each part, an unordered
partition of the S labels into pairs, and an assignment of two J labels
to the first S pair gives binom(7,4)binom(9,4)*3*6=79,380 pair branches.
This independently checks the count, while set completeness and kernel
ranks remain L153's imported certificate. Multiplying by binom(7,2)
gives 1,666,980 pair/pivot branches. There is no division by 10! for slots.

The audit program constructs the full formal arithmetic-circuit template
from the displayed formulas, with one degree-tracking node per operation
and one unknown per input. It imports no producer routines or count map.
It counts all constant multiplications, including zero entries, and
fourteen charged signed-frame aliases; degrees propagate by maximum at
addition and sum at multiplication. Cancellation can only reduce those
bounds. Table constants are not actual pair data in this count-only
construction. All 421 nonfield generators, all 282 field generators,
every operation group, all binary-power steps, every saved selector
record and all seventeen saved integer-count records were compared.
The complete relevant arrays are read and compared, not sampled.

Manual degree reconstruction agrees: degree(p)=1, degree(u),degree(v)<=2;
delta,D,G,Q have degree at most ten; E has degree at most eleven.
Hence shortening has degree at most 21, overlap-weight gates 22,
projection gates 13, incidence gates 40 and label-degree gates 50.
The remaining nonfield equations have degrees at most ten or three.
The field-power circuit has exactly 131 squarings and 68 further
products per unknown, followed by subtraction. These bounds hold at
all 21 pivots; zero frame coordinates only lower actual degrees.
No polynomial-identity certificate is inferred from this degree circuit.

Reproduce the bounded checks from the notebook with:

    python3 scripts/seven-coordinate/twelve_row_specification_size.py
    python3 scripts/seven-coordinate/audit_twelve_row_specification_size.py

Full independent evidence is
`scripts/seven-coordinate/twelve-row-specification-critical-audit.json`.
All 26 comparisons pass with zero failures. In particular the independently
constructed circuit gives 851,086 nonfield gates plus 56,400 field gates,
282 inputs and 703 generator entries; the fixed-coefficient variant has
717 entries. The certificate records each generator's degree bound, all
operation subtotals, complete actual/required selector/count records and
input hashes. Both paths share Python exact integer arithmetic. Neither
is formal verification, a fresh pair census or a feasibility computation.

**Coefficient-field qualification and certificate semantics.** The draft
said that all coefficients below lie in F_97, but its optional external
u*,v* may be arbitrary elements of F_Q. That blanket sentence is too
broad for the externally fixed variant. The uniform-existence coefficients
are in F_97; the fourteen additional equations can have F_Q coefficients.
The statement above now distinguishes these cases. This correction changes
no solutions, generators, degrees or counts: both variants are polynomial
systems over F_Q, as already required by the certificate contract. It needs
no source beyond the already approved arbitrary-prime-power theorem.

Gao–Platzer–Clarke Theorem 2.2 applies to
F_Q and all variables' field polynomials, including inverse and selector
witnesses. Coefficients in the prime subfield are permitted. A unit-ideal
identity is therefore a sufficient and necessary finite-field emptiness
certificate; its verification still needs the full polynomial identity.
The field equations must not be replaced by X^97-X. A positive artifact
requires a certified degree-twenty irreducible modulus and all residuals,
not merely a proper ideal or a numeric solver output. The fallback
irreducibility check is finite because any reducible degree-twenty monic
polynomial has a monic factor of degree at most ten, including repeated
factors. This validates the stated contract, without creating a field
modulus or claiming practical verification cost. The sources do not
bound the unknown certificate multipliers for this instance.

## Mathlib

Full matching twelve-row formula/certificate theorem: **not checked**.
Supporting finite-field, polynomial-ideal, exterior-power, matrix and
coding coverage is not checked anew; L109/L153 retain their qualifications.
Unknown availability is not absence. No Lean verification is claimed.
