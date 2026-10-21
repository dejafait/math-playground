# L106 — The prescribed two-distance-68 support cannot meet exact cardinality

## Hypotheses

Use n=1024,w=68,v=956,d=10, and precisely L098's fixed pairs:

    g_i=binomial(68,i)binomial(956,i),
    U=binomial(1024,64)/binomial(68,64), M=(U+1)/2,
    N=floor(65537^28/2^128)+1, alpha=(N-1)/(M-1),
    c_0=1, c_1=...=c_4=0,
    c_i=alpha*a_i/(2*g_i) for 5<=i<=68.

Here a_i is L021's exact rational primal vector, the factor 2 is
L022's normalization, and original triple coordinates have L023's
source convention. In particular sum_i g_i*c_i=N. Freeze these pairs,
not the triple values in L098's failed control. Retain all actual
(i,j,t,s), the source equalities preserving u=t-s, every source scalar
row, distance zeros, Boolean repetitions, and all 69 L098 contractions.
Omit every PSD constraint.

For this construction only, prescribe zero on every permitted distinct
triple whose sorted half-distance multiset is not (r,68,68), 5<=r<=68.
Leave each retained source class free. This is a restriction on a
proposed witness, not a necessary property of arbitrary feasible moments.

## Conclusion

There are exactly 64 retained source classes and 190 retained original
ordered entries. The 69 contractions on this support have rank 64 and
one signed rational solution. Write x_r for its class (r,68,68;u=r).
It is

    x_r=(N-2)*c_r/binomial(956-r,68)                 (5<=r<68),
    x_68=(N-2)*(3*c_68-2*(N-1)/g_68)/binomial(888,68).

The last coordinate is strictly negative. More precisely,

    rho=g_68*c_68/(N-1)=a_68/(U-1),
    7919/10^6 <= rho < 7920/10^6 < 2/3.

Thus no assignment on this prescribed support satisfies both the
contractions and scalar nonnegativity. The unique signed candidate
passes every contraction and every scalar upper/lower row, but fails
nonnegativity at exactly the original orbit (68,68,68,0).

This parks this restricted-support construction only. Unrestricted
shared-triple scalar/cardinality feasibility at the same pairs remains
open. Nothing here supplies a separator for that full system, other
pairs, PSD feasibility, a packing, an RS list, or a change to the
955–957 bracket. This is a local negative result using assessed known
methods, classified REPRODUCTION, without a novelty claim. The separate
critical proof review below retains this restricted obstruction.

## Proof

**Imported statements and applicability.** Schrijver, *New code upper
bounds from the Terwilliger algebra and semidefinite programming*,
IEEE TIT 51 (2005), 2859–2866, DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (62)–(67), p.7, supplies actual-orbit normalization, scalar rows,
source equalities and distance zeros. Kim–Toan,
[arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1), (31)–(35),
pp.8–9, cross-checks them. Their code hypotheses are nonempty binary
constant weight and 0<10<136<=1024. Only actual orbits are used;
Schrijver (61)'s qualified complement prefactor is unused. No PSD or
block-decomposition result is needed.

L098's separately audited homogeneous specialization of Raghavendra–Tan,
[arXiv:1110.1064v1](https://arxiv.org/pdf/1110.1064v1), Section 3,
Definitions 3.1,3.3 p.7 and the cardinality display pp.8–9, with Polak,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), Proposition
1.1 and its indicator proof p.2, Section 1.2 p.3, supplies

    sum_(j,t,s) D(i,j,t,s)*y_ij^(t,s)=N*c_i,
    D=binomial(i,t)binomial(68-i,j-t)
       binomial(i,s)binomial(956-i,j-s).

The normalization divides by the positive singleton moment, never by
a pair moment. Both repeated third words contribute c_i for i>0;
row zero is the objective, and rows 1,...,4 vanish. The primary-source
qualifications in foundations/04,12,13 remain: Polak's indicator proof
has the constant-weight conclusion, and local marginals need not
have a global representing distribution. L098 gives necessity for
exact-N support codes from arbitrary-center lists, not a converse.
The elementary finite rational elimination method is covered by the
prior SPECIALIZE assessment; it supplies no theorem that this proposed
support is sufficient. We do not reprove those imported results.

**Exhaustion of the construction support.** An actual orbit obeys

    max(0,i+j-68)<=t<=min(i,j),
    max(0,i+j-956)<=s<=min(i,j), h=i+j-t-s.

For a retained class, permute its words to present the distances as
(i,j,h)=(r,68,68). Admissibility forces t=r, and h=68 then forces s=0.
Consequently u=r, and every retained class has this presentation.
Conversely (r,68,r,0) is actual for every 5<=r<=68. The complete source
presentation with permuted distances (a,b,c) has

    t'=(a+b-c+u)/2, s'=(a+b-c-u)/2.

These are precisely the cited equalities with u preserved, not a
new equality based on distances alone. Thus there is exactly one
retained class for each r. For r<68 it has the three ordered original
presentations

    (r,68,r,0), (68,r,r,0), (68,68,68,68-r).

For r=68 these coincide at (68,68,68,0). Hence there are
3*63+1=190 retained original entries. Nonretained source classes
remain distinct even though the prescription assigns all of them zero.

**Unique solution and its sign.** For 5<=i<68, only the first retained
presentation contributes a free value to contraction row i. Its
coefficient is B_i=binomial(956-i,68)>0. Including the two repetitions
therefore gives

    B_i*x_i=(N-2)*c_i.

In row 68 the two presentations for each i<68 each have coefficient
H_i=binomial(68,i)binomial(888,i). The final presentation has
coefficient B_68=binomial(888,68)>0. Thus the remaining equation is

    2*sum_(i=5)^67 H_i*x_i+B_68*x_68=(N-2)*c_68.

Rows 0,...,4 impose no further restriction. These 64 equations are
triangular with positive diagonal B_5,...,B_68, proving rank 64,
consistency and uniqueness of the signed solution. In particular
there are no nonpivot choices to vary.

Counting disjoint choices of sizes i and 68 in a 956-set, or cancelling
factorials, gives

    g_i*B_i=g_68*H_i.

Substitute the first 63 solution coordinates and use
sum_(i=5)^67 g_i*c_i=N-1-g_68*c_68. The row-68 equation becomes exactly
the displayed formula for x_68. Since N>2 and B_68>0, its sign is the
sign of 3*rho-2. Also alpha=2*(N-1)/(U-1), so rho=a_68/(U-1).
The complete rational reconstruction below gives the exact ratio

    rho = 999827353056294107002031770259284685411165837067392868070193840389936016500775876936698401230511
          /126241790782674344390415873704003538302112683925274740089310694724316617167200847228172347907068912.

Integer cross-multiplication gives the bounds in the conclusion.
Consequently x_68<0. This is already a rigorous obstruction to this
support, independent of the remaining scalar verdicts. It does not
extend to a support with additional free entries.

**Complete original-coordinate evidence.** The sole approved run was

    python3 scripts/finite-support/fixed-pair-shared-scalar-construct.py
    python3 scripts/finite-support/fixed-pair-shared-scalar-verify.py

The files `scripts/finite-support/fixed-pair-shared-scalar-results.json`
and `scripts/finite-support/fixed-pair-shared-scalar-verification.json`
retain input hashes, exact pairs and N, the entire class lift, all
coefficient factors, the 69-by-64 matrix, every rational row operation,
all echelon entries, the complete signed candidate, every contraction
residual, and all scalar slacks by lossless factoring. The codebook
stores zero, all 69 Boolean pair values, and all 64 free values with a
single positive common denominator q. For every original entry its
three scalar slack numerators are explicitly

    value[code], pair[i]-value[code],
    q+value[code]-pair[i]-pair[j].

The lift retains each original t,s separately; the saved pattern counts
and signs are not an assertion that different source variables agree.
The original pairs are recovered from L021's exact vector and checked
against the selected complete values of L098's frozen certificate.
All of that certificate's endpoint hashes are checked by streaming,
without loading its 307 MiB contents as a new model.

The verifier imports no constructor routine. It reconstructs every
original orbit from the eight membership atoms

    (956-i-j+s, t, i-s, j-t, j-s, i-t, s, 68-i-j+t),

indexed by the three membership bits. Permuting those bits rebuilds
all six actual presentations, including their invariant t-s, Boolean
cases and forbidden cases. Independent factorial multinomials divided
by g_i recover every D. All 1,500,625 original entries, 4,501,875 scalar
rows, 205 repeated entries and 10,232 forbidden entries are checked.
The complete source-class count is 271,950; only the specified 64
classes are free in this construction. Every small-system coefficient
and all 69 residuals are reconstructed from the full original lift;
all residuals vanish. Every saved elimination operation is replayed,
including the first-available pivot choice. The unique candidate also
agrees with all 64 closed formulas above.

Exactly one nonnegativity row fails, at (68,68,68,0); no scalar upper
or lower row fails. Both constructor and verifier preserve this
negative result instead of treating successful equation solving as
feasibility. The entire relevant negative rational and all 69 zero
residuals were inspected. The ratio rho is compared with 2/3 exactly.

The combined 18,007,500 presentation visits remain below 20,000,000;
8,255 elimination updates remain below 5,000,000. The run and complete
verification take about 32.1 seconds against 900, with measured live
memory below 112 MiB against 1 GiB, rational codebook components of at
most 1071 bits against 262144, and certificates below 12 MiB against
256 MiB. No cap, implementation failure, parameter scan, numerical
proposal, PSD calculation or support enlargement occurred. Over 31
million verifier checks pass; the mathematical scalar failure is
recorded separately from reconstruction failures.

The prior assessment is
`drafts/literature/2026-10-21-fixed-pair-cardinality-scalar-feasibility.md`,
step 393. L105's independent-row interval pass and L098's distinct
frozen-control rejection retain their original scope. Neither is
contradicted by this joint restricted-support failure.

**Separate critical proof audit (2026-10-21, step 396).** The preexisting
SPECIALIZE assessment
`drafts/literature/2026-10-21-l106-critical-audit.md` covers exactly this
audit. Reinspection of foundations/04,12,13 and L098's homogeneous
conversion retains the source hypotheses, positive singleton divisor,
null-pair cases, both repetitions, and the distinction between necessary
support-code conditions and RS realization. No source theorem is
reproved and no new hierarchy or support assumption is introduced.

The support argument is exhaustive: any allowed class can be anchored
with (i,j,h)=(r,68,68); the actual inside range forces t=r, and h forces
s=0. Thus u is forced, rather than discarded. The three presentations
listed above are distinct for r<68 and coincide only for r=68. The
audit checks that these and only these 190 original entries are free.
Rows 5 through 67 each contain just their own positive coefficient;
row 68 has the two earlier presentations and a positive last coefficient.
Rows 0 through 4 contribute no additional free equation: row zero is
the objective N, and each null pair forces all its entries to zero.
Consequently the full system has rank 64, not merely a rank-64 subsystem
with unchecked consistency. The binomial identity and all 64 closed
formulas were checked exactly against the original system. The exact
rho above is retained; its strict comparison with 2/3 proves the sign
without relying on a decimal approximation or a solver flag.

Run the independent audit with

    python3 scripts/finite-support/fixed_pair_shared_scalar_critical_audit.py

Its complete evidence is
`scripts/finite-support/fixed-pair-shared-scalar-critical-audit.json`.
It imports neither original script. It reconstructs the fixed pairs
from L021's vector and also checks all 64 equations defining that
imported uniquely specified vector. All original input hashes and the
complete L098 endpoint hashes match; selected L098 values are decoded
in full and compared exactly. The two original certificates are
unchanged. The audit uses its own clock because the original verifier's
historical constructor timestamp cannot serve as a new-run deadline.

Every original orbit is regenerated from admissibility, with all three
weight-68 sets recovered from eight membership atoms. Six permutations
are formed using Boolean membership predicates, independently of the
constructor's distance-permutation formulas; the saved original lookup
is compared at every presentation. The audit checks all 271950 source
classes, 205 repeated entries and 10232 forbidden entries, retaining
different t-s values. Every original coefficient factor, lift code and
scalar slack is reconstructed, not merely its reported sign. The full
lift and scalar codebook are saved afresh. The original 69-by-64 matrix,
all fixed terms and right sides agree with both full-orbit accumulation
and the triangular manuscript formulas. Every saved pivot, rational
operation and echelon entry is replayed, with no new candidate solve.

All 1500625 original orbits, 4501875 scalar rows and 69 contraction
residuals agree. The complete negative rational at (68,68,68,0), exact
rho, and all 69 zero residuals were also inspected without previews.
Precisely one nonnegativity row fails; all scalar upper and lower rows
pass. Over 30 million independent reconstruction checks pass with no
implementation failure. The new run uses 9003750 presentation visits
against 20000000, 8255 elimination updates against 5000000, 13.07 seconds
against 900, 143065088 peak live bytes against 1073741824, at most 1071
bits per checked rational/codebook component against 262144, and
11173367 certificate bytes against 268435456. The output-size check is
additional to the checks recorded before writing the certificate.

This audit validates the existing restricted negative result; it does
not establish new mathematical discovery, a full-system separator,
another pair assignment, PSD infeasibility, a representing measure or
RS safety. L105's independent-row pass is a contrast, not an input to
the proof. The argument and direct mathematical inputs are unchanged.

## Mathlib

Full matching finite restricted-support obstruction, Schrijver
specialization and certificate machinery: not checked. The primary
source imports above, exact pair data, elementary binomial identities
and rational substitution supply this local proof. Unknown Mathlib
coverage is not evidence of absence.
