# L068 — Five isolated scalars with two antipodal singleton pairs

## Hypotheses

Use audited L057's triangle local converse over F=F_(97^20), with
H={1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96}, the order-sixteen
subgroup of F_97^*. The code is RS[F,H,8]; shifted moments are
sigma_j(e)=sum_(x in H)e(x)x^j for j=1,...,8. All displayed integers
are elements of F_97 embedded in F. The pinned cell is
1/4<=delta<5/16; identification with the unread ABF26 definition is
not assumed.

Set ordered P=(a,b,c)=(64,75,33), Y={1,96}, Z={18,79}, W={8,50}.
These nine labels are distinct. Y and Z are antipodal; W is not.
The three base supports are A_0={a,b} union Y, A_1={a,c} union Z,
A_2={b,c} union W. Choose gamma=(0,1,2), lambda=1 and
(p,q,r)=(71,5,17). Thus g=1, rho=2, alpha=(-1,2,-1), and all
original parameter and base-weight gates in L057 hold.

## Conclusion

This triangle has **at least five distinct additional isolated
disjoint-P recovery scalars**, namely {22,30,34,50,63}. They all
survive the original finite gates and have full fourth weights.
Consequently the proposed uniform upper bound three for triangles
with two antipodal pairs and arbitrary W is false. The relaxed count
also includes these witnesses, since it permits zero fourth weights.

This is negative evidence against that intermediate bound only. It
does not refute the triangle twelve-additional-recovery bound or the
challenge, nor establish an enlarged-family maximum. The global
interval stays 11/q–16/q. A separate critical audit on 2026-10-11
found no defect in this explicit counterexample; no complete challenge
candidate is claimed.

## Proof

### Inputs and exact original pencil

Use L057's audited local construction and same-support failure statement.
Its recurrence input is Przemek Chojecki, *Shortening Bounds for
Reed–Solomon MCA*, live author TeX v9.2, July 17, 2026, DR2
(`drc:lem-locator-recurrence`) and DR6–DRC
(`drc:thm-exact-compiler`), statements and proofs at source lines
2785–2935, [author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
The source is mutable and is not certified identical to ePrint 2026/1463.
The already assessed specialization has distinct nonzero labels,
R=8, t=4 and multiplier x. This step imports L057; it does not
reprove general recurrence, interpolation or shortening. The new work
is an explicit counterexample in the separately approved enlarged
family. L067's restricted maximum and L066's conditional anchor
requirement are not mathematical premises of this counterexample.

For U=P union Y union Z union W,

\[
 Q(X)=(X-12)(X-22)(X-27)(X-47)(X-70)(X-85)(X-89),
 \qquad c_x=Q(x).
\]

Direct evaluation gives:

| x | 1 | 8 | 18 | 33 | 50 | 64 | 75 | 79 | 96 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| c_x | 45 | 70 | 8 | 5 | 74 | 55 | 71 | 18 | 40 |

L057 (2) gives the following actual base errors, zero off the listed
supports. Entries are in the displayed support order:

| i | support order | actual weights | sigma(e_i), moments 1 through 8 |
|---|---|---|---|
| 0 | (1,96,64,75) | (52,57,72,33) | (94,11,53,70,93,44,31,20) |
| 1 | (18,79,64,33) | (4,9,15,91) | (90,45,20,83,71,25,55,93) |
| 2 | (8,50,75,33) | (27,23,90,80) | (86,79,84,96,49,6,79,69) |

For example, e_0(a)=-c_a p=-55*71=72 modulo 97;
e_1(a)=c_a(1-p)/2=15. All twelve base weights are nonzero.
The displayed moment vectors satisfy s_2=2s_1-s_0 entrywise.
Thus the original syndrome pencil is s(T)=s_0+T(s_1-s_0), with
s_1-s_0=(93,34,64,13,75,78,24,73). L057's local converse supplies
this actual pencil, independent coefficient syndromes and its
nonpersistent tau-zero locators. It applies because all nine labels
are distinct and p,q,r avoid 0,1.

### Five full recovered errors and isolated classification

For each row below, define e_K to have the actual weights listed on K
and zero elsewhere. Set E=2+mu and T=2/E, as in L057 (12)–(14).

| K, in weight order | mu | E | T | actual weights e_K |
|---|---:|---:|---:|---|
| (22,27,47,85) | 30 | 32 | 91 | (34,55,84,93) |
| (22,27,47,89) | 50 | 52 | 56 | (20,81,69,71) |
| (22,27,85,89) | 22 | 24 | 89 | (72,26,96,29) |
| (22,47,85,89) | 34 | 36 | 27 | (86,15,92,55) |
| (27,47,85,89) | 63 | 65 | 6 | (35,6,75,20) |

Every K is disjoint from P and different from each base support.
Every weight is nonzero. The five scalars are distinct, nonzero and
different from -1; all E are nonzero; the five T are distinct and
avoid 0,1,2. Thus no excluded base parameter or original infinity
is counted. The original chart and lambda have been specified rather
than inferred to be rational for arbitrary triangles.

Here is the complete eight-moment equality for these five errors.
Both sides in each row are evaluated by the finite sum defining sigma:

| T | sigma(e_K)=s_0+T(s_1-s_0) |
|---:|---|
| 91 | (21,1,57,89,31,61,81,67) |
| 56 | (64,72,48,22,25,47,17,34) |
| 89 | (29,30,26,63,75,2,33,18) |
| 27 | (83,56,35,33,81,16,0,51) |
| 6 | (70,21,49,51,58,27,78,70) |

For instance at T=91, the first actual moment is
34*22+55*27+84*47+93*85=21 modulo 97, and the pencil's first
moment is 94+91*93=21. The table records all eight, with no omitted
high-moment conditions. Since these are prime-field equalities, they
remain equalities in F; they are not numerical approximations.

To confirm that these are isolated, not both-zero lifts, use L057 (5)
with J=P. Write f_K(X)=product_(k in K)(X-k) and
G_P(X)=(X-64)(X-75)(X-33). The projected scalars are
y_K=sum_(y in Y)c_y y f_K(y)G_P(y) and
z_K=sum_(z in Z)c_z z f_K(z)G_P(z). Direct finite evaluation gives:

| mu | y_K | z_K |
|---:|---:|---:|
| 30 | 21 | 48 |
| 50 | 13 | 68 |
| 22 | 90 | 40 |
| 34 | 56 | 61 |
| 63 | 39 | 32 |

Every entry is nonzero and z_K=mu*y_K in each row. L057 therefore
classifies them as isolated. Their already verified original moments
establish the restored coefficients, rather than treating projected
compatibility alone as recovery. For reference the numerator weights
omega=E*e_K are (21,14,69,66), (70,41,96,6), (79,42,73,17),
(89,55,14,40), (44,2,25,39), respectively. All eight numerator
residuals and all eight original-pencil residuals vanish.

L057's same-support argument applies to each K: agreement and input
failure occur on the same complement H minus K of size twelve. In
particular these are actual recoveries for the pinned model, not merely
supports solving a quotient equation. Five distinct finite scalars
with these properties contradict the proposed upper bound three.

### Calculation evidence and limits

The candidate was found by
`scripts/triangle-recovery/two_antipodal_anchor_sweep.cpp`, adapted
from L067's audited arbitrary-pair evaluation path. It normalizes
Y={1,96}, chooses seven Z pairs and all 66 possible unordered W
pairs outside Y union Z, then all 720 ordered shared triples and
715 disjoint-P supports per assignment. It permits zero fourth
weights and deduplicates scalars at fixed weights. The intended full
scope has 462 pair choices, 332640 assignments and 237837600 rows.
It stopped at its first assignment with at least four scalars, which
had five: 99052 assignments and 70822180 rows had been processed.
This is incomplete enlarged-family coverage and proves no upper bound.

The partial packed evidence is
`scripts/triangle-recovery/two-antipodal-anchor-rows.bin`, 354110900
bytes, SHA256
`e74f4d7a7de658803d1c203dc9a1a406f121eff0fdb6dd82df49730fcdd1a931`.
The summary is `scripts/triangle-recovery/two-antipodal-anchor-sweep.json`.
The producer did not verify original moments; its zero moment-test count
is not a mathematical verification. The packed prefix has not been
equation-replayed and is not needed as proof of the displayed witness.

The independent checker
`scripts/triangle-recovery/check_two_antipodal_witness.py` takes the
displayed labels and weights as fixed input, reconstructs Q, base
errors and moments, then uses seven-column shifted Vandermonde
inversion for every one of the 715 supports disjoint from this P.
It does not import the C++ interpolation or row-classification formulas.
Its arithmetic utility is shared with the earlier independent table
verifier; this is limited implementation independence, not a completed
critical audit. It retains both-zero diagnostics and applies no
nonzero-fourth-weight filter before collecting eligible isolated rows.
For every positive row it separately computes L057's projected scalars,
all eight numerator moments and all eight original moments, plus E,T
and every finite gate. Actual/required failures are 0/0. It finds the
five displayed scalars, and all five fourth errors are full weight.

Full fixed-assignment tests and witness data are saved in
`scripts/triangle-recovery/two-antipodal-witness-verification.json`.
All complete load-bearing witness rows, base errors, base moment vectors,
Q evaluations and the empty failure array were inspected. No claim about
both-zero count or a full bad-set maximum is needed or made.

Reproduce from the notebook directory:

```sh
clang++ -std=c++17 -O3 -Wall -Wextra -pedantic scripts/triangle-recovery/two_antipodal_anchor_sweep.cpp -o /tmp/mca-two-antipodal-anchor-sweep
/tmp/mca-two-antipodal-anchor-sweep produce scripts/triangle-recovery/two-antipodal-anchor-rows.bin scripts/triangle-recovery/two-antipodal-anchor-sweep.json
python3 scripts/triangle-recovery/check_two_antipodal_witness.py
```

The ready literature comparison found no matching imported enlarged
count. This negative local result is not certified original mathematics.
Preserve ATTEMPTS/025 and L067's true three-antipodal bound. This
counterexample abandons the proposed two-antipodal bound three, while
the triangle twelve bound and the main challenge gaps remain unresolved.

### Separate critical audit (2026-10-11, step 158)

The approved audit reused the existing source comparison and checked the
complete displayed witness, L057's exact local-converse and same-support
scope, the inherited L010 kernel and uniqueness, and L041's local converse.
It found no wrong equality, missing finite gate or missing dependency.
The sole direct input remains L057. No L066 count, L067 maximum, pending
L060–L064 result, or ABF26 identification is used.

The base construction has alpha=(-1,2,-1), hence the signs and division
by two in the displayed errors are correct. Q has precisely the seven
complement roots, every c_x is nonzero, all normalized weights avoid 0,1,
and all actual base weights are nonzero. The eight moment equalities
s_2=2s_1-s_0 hold. Thus L057's local converse applies without an equality
or completion premise. Its independent coefficient syndromes and tau=0
nonpersistence are inherited in exactly that scope.

For the seven-column verifier, let M have columns v_x for x in K then P,
and solve its first seven rows for Y and Z. This square matrix has
determinant (product x) times the Vandermonde determinant on seven distinct
nonzero labels, so it is invertible over F_97 and F. Its eighth-row
residual is the functional with polynomial
X product_(x in K union P)(X-x): the leading coefficient is one and it
vanishes on all seven columns. Consequently its residuals are exactly
L057's y_K,z_K, with moment indices 1 through 8, not 0 through 7.
Both residuals are nonzero in each retained row, giving mu=z_K/y_K.

Write d_x for the P coefficients of the solved Z-mu Y. To place N_K in
the K span its three added coefficients must be -d_a,-d_b,-d_c. Solving
gives p=(1+d_a/c_a)/(1+mu), q=d_b/(mu*c_b), r=-d_c/c_c, precisely the
verifier's signs. The divisions are nonzero after the isolated and
mu!=-1 gates. The K coefficients then give omega; the actual weights
are omega/E since g=lambda=1. All five E=2+mu are nonzero, all T=2/E
are distinct and outside {0,1,2}, and every recovered weight is nonzero.
Complete numerator and original moment tables and both projections were
inspected for all five rows, including every zero residual.

The shared arithmetic utility uses Gauss–Jordan row operations modulo 97
with nonzero pivots and exact modular dot products. Its bounded replay
completed all 715 supports and reproduced the entire saved JSON byte for
byte: SHA256 d89495d812ee232f78cbcf72d984380187418c682673375e8cfb014527ae142c.
Both-zero diagnostics remain in that certificate; they are not incorrectly
counted as isolated. No total bad-count conclusion is drawn from this test.

An additional direct audit script imports neither the producer nor the
shared arithmetic utility. It starts with the displayed errors and uses
literal finite sums and Lagrange interpolation. Take actual input words
a_*=e_0 and b_*=e_1-e_0, giving exactly the displayed syndrome pencil.
For each K, it verifies that a_*+T b_*-e_K is the evaluation of a polynomial
of degree at most seven by interpolating its first eight H values and
checking all sixteen. This gives agreement on the same S=H minus K.
For failure, interpolate b_* on the first eight labels of S in increasing
order. The residuals at the remaining four labels are, in witness-table
order,

| mu | last four labels of S | b_* minus interpolant |
|---:|---|---|
| 30 | (75,79,89,96) | (0,0,34,0) |
| 50 | (75,79,85,96) | (0,0,47,0) |
| 22 | (70,75,79,96) | (69,69,4,91) |
| 34 | (70,75,79,96) | (87,87,43,81) |
| 63 | (70,75,79,96) | (63,63,88,62) |

The degree-at-most-seven interpolant on eight distinct nodes is unique
over F as well as F_97; the supporting interpolation input is J. I. Hall,
*Notes on Coding Theory*, [GRS chapter, p. 65](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
as covered in the reused assessment. Each nonzero residual therefore
proves b_*|_S is not in C|_S, even allowing extension-field polynomial
coefficients. This directly confirms the same-support conclusion already
proved by L057, without substituting closeness for input failure.

Reproduce only this bounded audit with
`python3 scripts/triangle-recovery/audit_two_antipodal_witness.py`.
Full independent witness and interpolation evidence is in
`scripts/triangle-recovery/two-antipodal-critical-audit.json`; actual/required
witnesses are 5/5, fixed-assignment support tests 715/715, failures 0/0.
All five complete audit rows and the empty failure array were inspected.
The count five exceeds the proposed bound three, whose falsification
threshold was four. This validates existing negative evidence, not a new
upper bound or a claim of originality.

The producer stop was separately checked in its control flow and summary:
it stops after finishing the first assignment reaching at least four,
with 70,822,180 of 237,837,600 support rows, and reports zero original
moment tests in produce mode. Its packed prefix remains unreplayed and
supplies no maximum. The explicit five witnesses need no prefix equations.

## Mathlib

The full matching five-scalar counterexample is **not checked** in
Mathlib. Supporting finite-field arithmetic, shifted Vandermonde
independence, interpolation, moment kernel and same-support facts are
also **not checked** in Mathlib for this step. L057 is the audited
informal input. No absence claim, Lean verification, uniform enlarged
upper bound or challenge solution is asserted.
