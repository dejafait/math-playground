# L116 — The unchanged product box passes the full anchored five/six matrix

## Hypotheses

Use L021's canonical rational primal vector a_i and exactly L098's
normalization and L112's original positive box. Namely, let

    N=floor(65537^28/2^128)+1, H=binomial(1024,68), rho=N/H,
    U=binomial(1024,64)/binomial(68,64),
    g_i=binomial(68,i)binomial(956,i),
    c_0=1, c_1=...=c_4=0,
    c_i=(N-1)a_i/((U-1)g_i), 5<=i<=68.

For k=i-5 use the unchanged integers `point[k]` and `scale_powers[k]`
in `scripts/finite-support/positive-factor-enclosure.json.gz`. The box is

    l_i=10^(scale_powers[k])*(point[k]-10^25)/10^70,
    u_i=10^(scale_powers[k])*(point[k]+10^25)/10^70,
    x_i in [l_i,u_i], 5<=i<=68.

No endpoint, scale, pair or N is varied. Use the full L112–L114 source
recipe on the universe V of 68-subsets of a 1024-point set: normalized
singleton value 1, pair value c_i at half-distance i, distinct-triple
value x_i*x_j*x_h if all three sides are at least five, and zero for a
distinct triple with a side 1,...,4. A repeated triple has its Boolean
pair value c_b, not a product. Nonempty homogeneous moments are rho
times these normalized values. In particular no additional incidence
zero from L054 is imposed. The joint L112/L113 review, L114's consumed-
input review, and L115's separate critical audit are retained inputs.

Fix A in V. For l=5,6 set S_l(A)={B in V: |A\B|=l}. Let M be the
union matrix whose indices are {A} and all {A,B} with B in
S_5(A) union S_6(A). Full source PSD, global root uniqueness,
representing measures and RS realization are not hypotheses.

## Conclusion

For every A and every x throughout the original box, the entire M is
positive definite. Its included-anchor beta reduction, after the single
positive-anchor Schur congruence, has 36 two-by-two blocks and 13
one-by-one blocks. With C_lm and D_l defined below, every old pivot has

    C_55/(c_5*D_5) >= 630869/10^6 > 0,

and every remaining pivot satisfies

    (C_66-C_56^2/C_55)/(c_6*D_6) >= 638632/10^6 > 0      (1)

when layer five occurs. For a new-only mode (1) means
C_66/(c_6*D_6). The smallest certified interval lower endpoint in (1)
occurs at (a,b)=(4,0) and is in [638632,638633)/10^6. This is a
statement about the interval certificate, not the exact minimum of
the true pivots over the box.

In particular L112's enclosed root passes this necessary matrix
simultaneously with ordinary scalar and exact-N feasibility from
L113–L114. This is a REPRODUCTION of assessed spectral, Schur and
interval methods. It parks exclusion by this fixed principal matrix
only, without a claim of originality, full SDP feasibility, a measure,
packing, RS list or change to the 955–957 bracket. The separate critical
proof review below retains this application.

## Proof

**Imported results and applicability.** The prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-fixed-product-coupled-five-six-psd.md`.
Import Polak, *Semidefinite Programming Bounds for Constant-Weight Codes*,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), §1.1 (1)–(3),
Proposition 1.1 and its complete indicator proof, printed p.2. Use its
proved constant-weight A(n,d,w) conclusion, retaining the displayed
A(n,d) qualification in foundations/12. At order three a singleton
anchor allows exactly its unions with one support; the selected complete
shells are a principal restriction. This supplies necessity for code
indicators, not representability of a passing assignment.

Import Schrijver, *New code upper bounds from the Terwilliger algebra
and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866, DOI
[10.1109/TIT.2005.851748](https://doi.org/10.1109/TIT.2005.851748),
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
(7), Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59),
III.B (64), printed pp.2,5–7. Its complete tensor decomposition and
positive diagonal rescalings retain unequal layer indices. The two
ground-set sizes are 68 and 956 and the selected layers are 0,5,6,
within the source ranges. All absent coordinates are removed by
principal restriction. Use the congruent integer beta convention
recorded in foundations/04,09; the unused complement prefactor in
(61) plays no role. This is an algebraic decomposition of the prescribed
invariant matrix, requiring neither a code nor a measure.

Import the positive-leading-block Schur congruence from Brouwer–Haemers,
*Spectra of Graphs*, [author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
Theorem 2.7.1(i), p.36, as recorded in foundations/09. The normalized
anchor is 1. The subsequent old pivots are strictly positive by L115
and the independently recovered intervals below, so no zero pivot is
inverted. Import expression inclusion for enclosing interval operations
from Rump, *Verification methods: Rigorous results using floating-point
arithmetic*, Acta Numerica 19 (2010), 287–449, DOI
[10.1017/S096249291000005X](https://doi.org/10.1017/S096249291000005X),
[corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
§5.5 (5.16)–(5.17), author p.28; foundations/14 records its inspected
scope. Exact rational endpoints avoid rounding. Repeated occurrences
may overestimate but remain enclosed. No spectral, root, Schur or
interval theorem is reproved. The finite dictionary and normalization
checks are necessary because the cited theorems do not decide these
immutable coefficients. L061's different witness is not an input.

**All entries and actual source classes.** Write

    B=(A\X) union Y, C=(A\X') union Y',
    |X|=|Y|=l, |X'|=|Y'|=m, t=|X intersection X'|,
    s=|Y intersection Y'|, h=l+m-t-s.

For (l,m)=(5,5),(5,6),(6,6), every 0<=t,s<=min(l,m) occurs:
the head and tail unions have sizes l+m-t<=12 and l+m-s<=12,
within 68 and 956. These partitions are precisely the orbits under
permutations fixing A. Thus 36+36+49=121 relations exhaust all three
matrix blocks. Their actual source coefficient and multiplicity are

    K_lm(t,s)=c_l                         if h=0,
              0                          if 1<=h<=4,
              x_l*x_m*x_h                if h>=5,
    D(l,m,t,s)=binomial(l,t)binomial(68-l,m-t)
               *binomial(l,s)binomial(956-l,m-s)>0.     (2)

The h=0 case occurs only on a Boolean diagonal l=m,t=s=l. There
is no product on that diagonal. The anchor row is exactly 1,c_5*1,c_6*1.
The prescribed recipe depends on distances for distinct entries, so
it is invariant under these coordinate permutations directly; no
averaging of arbitrary labeled moments or RS exclusions is assumed.

The independent verifier constructs actual A,B,C for every (2), saves
all eight atom sizes, and evaluates all 726 ordered presentations.
Every presentation (i,j,t',s') has h'=i+j-t'-s', t'-s'=t-s and a
positive actual D. Its two source multinomials equal g_i*D, which
equals the original g_l*D(l,m,t,s). Full atom keys minimized over all
six permutations check every cross-relation collision. The values
agree in every presentation, with no equality imposed on general
source variables merely because side distances coincide. Both endpoint
repetitions and the i=0 coincident row occur four times each across
the two diagonal blocks. Their D values are respectively 1,1,g_j.
Distinct null entries have zero pair capacity and value. The anchor's
own coincident entry is separately 1. This includes every repeated,
null, forbidden and coincident case of the selected matrix.

**One coherent unequal-layer reduction and full anchor.** Put S_l=g_l.
The imported beta coefficient is

    beta(n,l,m,a,t)=sum_u (-1)^(u-t) binomial(u,t)
       *binomial(n-2a,u-a)binomial(n-a-u,l-u)binomial(n-a-u,m-u),

where only max(a,t)<=u<=min(l,m,n-a) contributes. Modes are
0<=a,b<=6; layer five occurs exactly for a,b<=5 and layer six
occurs in all 49. Define positive factors

    D_l=binomial(68-2a,l-a)binomial(956-2b,l-b).

After dividing M by rho>0, eliminating its single anchor gives
shell blocks K_lm-c_l*c_m*J. Consequently the complete beta blocks are

    C_lm=sum_(t,s) beta(68,l,m,a,t)beta(956,l,m,b,s)K_lm(t,s)
          -1_(a=b=0)*c_l*c_m*S_l*S_m.                 (3)

The block is [[C_55,C_56],[C_56,C_66]] when layer five occurs,
and [C_66] otherwise. The full constant correction includes
c_5*c_6*S_5*S_6. It comes from the one constant block with anchor
row (1,c_5*S_5,c_6*S_6); separate shell anchor eliminations would
not supply the cross correction. All nonconstant anchor coordinates
vanish. Every source block is retained.

For clarity, a finite signed subset calculation independently checks
the common normalization, including both rectangular orientations.
For each factor n, let f_a(W) be the product over a fixed set of a
disjoint ordered point pairs of
(1_(positive member in W)-1_(negative member in W)). On l-subsets
its squared norm is 2^a*binomial(n-2a,l-a): its nonzero values choose
exactly one member per pair, plus l-a ordinary points. Evaluate at an
l-set containing all positive members and no negative members. An
m-set with nonzero value chooses z negative members and b ordinary
points in that l-set. Its signed contribution and intersection are

    (-1)^z binomial(a,z)binomial(l-a,b)binomial(n-l-a,m-a-b),
    t=a-z+b.                                         (4)

The verifier saves every term of (4) for n=68,956, both diagonal
layers and both rectangular orientations. If eta(n,l,m,a,t) is its
sum at fixed t, the exact comparisons are

    binomial(n-2a,l-a)*eta(n,l,m,a,t)=beta(n,l,m,a,t),
    binomial(n-2a,l-a)*eta(n,l,m,a,t)
       =binomial(n-2a,m-a)*eta(n,m,l,a,t).             (5)

The comparisons retain signs, not just squares. For the tensor vectors
the norm is 2^(a+b)*D_l, so their bilinear forms are the blocks (3)
times the same positive scalar 2^(a+b) across both layers. This
checks a coherent congruence, rather than choosing diagonal
normalizations independently. The imported theorem supplies the
complete decomposition; (4)–(5) are finite normalization checks only.

The mode multiplicity is

    m_ab=(binomial(68,a)-binomial(68,a-1))
          *(binomial(956,b)-binomial(956,b-1)).

Every m_ab is positive. Their sum over a,b<=5 equals S_5, and
over a,b<=6 equals S_6. The complete matrix dimension is
1+S_5+S_6. No modes with a>6 or b>6 have a surviving coordinate.

**Complete rational interval verdict.** For each (2), use the point
interval [c_l,c_l] for h=0, [0,0] for 1<=h<=4, and
[l_l*l_m*l_h,u_l*u_m*u_h] for h>=5. Form all signed sums (3)
with exact rational arithmetic. A negative coefficient uses the upper
entry endpoint in a lower bound. Subtract the exact anchor term.
Let [A],[B],[C] be the resulting C_55,C_56,C_66 intervals.
Every old lower endpoint A_->0. Square [B] by the exact range of
the square on an interval (including zero if it crosses zero), and
enclose the inverse by [1/A_+,1/A_-]. The interval

    ([C]-[B]^2*[1/A_+,1/A_-])/(c_6*D_6)              (6)

therefore encloses the true normalized Schur remainder throughout the
box. For new-only modes use [C]/(c_6*D_6). Each of the 49 lower
endpoints is at least 638632/10^6. The full least fraction is saved
at `minimum_normalized_remainder.value` in
`scripts/finite-support/fixed-product-coupled-verification.json`,
at (4,0), and exact integer comparisons give the stated bracket.
There are 49 positive, zero negative and zero unresolved blocks.
All 36 [A]/(c_5*D_5) intervals exactly recover L115's original
intervals, whose lower endpoints are at least 630869/10^6.

The positive old pivot and (6) prove positive definiteness of each
two-by-two block by the imported congruence; the new-only scalars
are positive as well. The complete source decomposition and invertible
anchor congruence prove M/rho positive definite, hence M positive
definite. The box need not consist of roots for this assertion.
At L112's one enclosed root, the same moments also satisfy L113's
upper capacities, L114's lower rows and all exact-N contractions.

**Complete evidence and limitations.** Reproduce from this notebook:

    python3 scripts/finite-support/fixed_product_coupled.py
    python3 scripts/finite-support/verify_fixed_product_coupled.py

The constructor saves `scripts/finite-support/fixed-product-coupled.json`:
345 checks, zero failures, every original endpoint and canonical pair,
121 entry intervals, all 49 blocks, anchor corrections, positive scales,
normalized pivots and sign decisions. It binds the complete relevant
root, scalar and five-shell artifacts and every stored audit input and
replay hash; all 64 strict inclusion margins and all 64 consumed lower
rows are checked. This reuses the audited root, without solving again.

The independent verifier imports no constructor routine. It saves
`scripts/finite-support/fixed-product-coupled-verification.json`:
2831 checks, zero failures. Besides every actual union and signed action
above, it reconstructs every saved interval, block, correction, pivot
and summary field from the canonical data. It checks the entire original
box with factorial binomials and separately collects the coefficients
of each common x_l*x_m*x_h expression before interval evaluation.
Those collected enclosures lie inside the saved entrywise enclosures;
they do not change or refine the box. The diagonal polynomial trace
checks cancel every distinct-product coefficient exactly and recover
S_l*c_l before anchor elimination and correction trace S_l*c_l^2.
These are polynomial identities, not equalities of overestimated
interval traces. Complete failure lists and the full least fraction
were inspected; all load-bearing arrays are consumed in full by the
independent reconstruction. Saved flags or previews do not establish
the result.

An initial binding-reader exception encountered L115's single replay
hash string where the earlier audits use maps. It occurred before
block evaluation. The reader was repaired to bind the explicit replay;
the working note preserves the exception. No coefficient or endpoint
was changed. No solve, scan, retuning, refinement or other-anchor test
was used. The separately proposed critical proof audit is completed below.
Other anchors, omitted layers, stronger distributions, global root
uniqueness, measures, actual packings, common-center RS realization and
arbitrary-center safety remain unresolved. Prior different-witness
stops, including L054 and L061's diagnostic scopes, are preserved.

**Separate critical proof audit (2026-10-24, step 437).** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-23-l116-coupled-critical-audit.md`.
This review retains the conclusion without mathematical repair. It
supersedes the earlier pending-review wording for L116 in the overview.
The argument and direct mathematical inputs are unchanged; no DAG or
overview assembly change is required. This verifies a finite application
of the cited results, without a claim beyond the sources checked.

The entire proof and both construction/verification scripts were read.
The singleton-anchor indices are exactly the permitted order-three union
indices restricted to the two full shells. The normalized anchor is 1
because all nonempty homogeneous moments have the same positive factor
rho. Permutations fixing A act transitively on each head/tail partition;
the prescribed product recipe is invariant under that action itself.
Thus the 121 relations exhaust this matrix for every A, without an
assumption of label symmetry for arbitrary RS moments.

For the notation of (2), the complete atoms in mask order 0,...,7,
with A,B,C in bits 0,1,2, are

    (956-l-m+s, t, l-s, m-t, m-s, l-t, s, 68-l-m+t).

All entries are nonnegative at every allowed relation. The audit
reconstructs every saved atom and permutes these eight counts in all
six orders. From a permuted array q it recovers i=q_1+q_5,
j=q_1+q_3, t'=q_1, s'=q_6 and h=q_2+q_3. All 726 resulting orbits,
positive D values, t'-s'=t-s identities and multinomial products agree
exactly. Both endpoint repetitions and coincidence each occur four
times, with the stated D values and Boolean entries. All 228 presented
distinct null cases have zero entry and zero minimum pair capacity.
The positive product cases, including repeated side distances, are
handled by the original positive endpoint products. No Boolean diagonal
is evaluated by that product formula.

The imported complete unequal-layer decomposition supplies the mode
spaces, their simultaneous layer matching and multiplicities. The audit
consumes all 50 saved signed-action records, including every zero term,
for both factors and all four layer orientations. The signed count in
(4) chooses exactly one point per designated pair; its remaining points
come from the n-l-a ordinary points outside the evaluation l-set and
all designated pairs. The norm count chooses either pair member and
then l-a points among n-2a ordinary points. Consequently (5) uses the
same factor 2^a in both layers, and the product action uses the common
2^(a+b). All 72 signed rectangular comparisons agree, so no independent
sign or scale choice is made on the two sides. The 49 mode
multiplicities and positive D_l factors are checked in full, and

    1 + sum_(a,b) m_ab * number_of_surviving_layers(a,b)
      = 1 + g_5 + g_6.

This retains 36 two-dimensional blocks and 13 new-only scalars. The
source theorem, rather than a representative-vector calculation alone,
establishes exhaustion of the whole matrix.

For the constant block let u=c_5*S_5, v=c_6*S_6 and let A,B,C denote
its three entries after anchor elimination. Before elimination it is

    K = [[1,u,v], [u,A+u^2,B+u*v], [v,B+u*v,C+v^2]].

The unit upper triangular matrix

    T = [[1,-u,-v], [0,1,0], [0,0,1]]

has determinant one and satisfies
T^T*K*T = diag(1,[[A,B],[B,C]]). The full rational identity is
checked at all eight endpoint choices for A,B,C; the displayed algebra
holds for arbitrary entries. These checks do not infer positivity of
a nonlinear interval expression from corners. They verify the common
anchor correction, including u*v. All 48 nonconstant modes have zero
anchor correction, as required by the imported constant-mode splitting.

For a two-dimensional mode write its saved intervals as
[A_-,A_+], [B_-,B_+], [C_-,C_+]. All A_->0. Set
q_+=max(B_-^2,B_+^2), and q_-=0 when the B interval contains zero,
otherwise q_-=min(B_-^2,B_+^2). The exact lower and upper bounds are

    (C_- - q_+/A_-)/(c_6*D_6),
    (C_+ - q_-/A_+)/(c_6*D_6).

They enclose the true Schur remainder: the denominator is positive,
the square is nonnegative, and repeated occurrences can only widen
the expression enclosure. Every endpoint equals the saved certificate.
For every two-dimensional mode the audit additionally checks the
division-free inequality

    C_-*A_- - q_+ >= (638632/10^6)*c_6*D_6*A_- > 0.

Each of the 13 new-only modes meets the same normalized bound directly.
All 36 old intervals agree with the audited L115 values; their minimum
is in [630869,630870)/10^6. The final-pivot lower endpoints have unique
minimum at (4,0), whose complete rational value is in
[638632,638633)/10^6. These bounds concern enclosing interval endpoints,
not an attained minimum of the actual pivot function. The positive
pivots and invertible congruences establish the claimed whole-box
positive definiteness.

Reproduce this bounded review, preserving both original certificates:

    python3 scripts/finite-support/critical_audit_l116.py

The full verifier is replayed to
`scripts/finite-support/l116-critical-reverification.json`. Its complete
JSON object equals `fixed-product-coupled-verification.json`; all 2831
checks pass. That replay reconstructs every original canonical pair,
exact N, all 64 endpoints/scales, 121 entries, 49 full blocks and all
signed interval operations from the original data. It also consumes
all retained root margins and lower-minimum rows and recovers every
L115 pivot. Equality of the complete verification objects retains all
saved dictionary, signed-action, trace and extremal evidence; hashes
alone are not used as mathematical verification.

The new `scripts/finite-support/l116-critical-audit.json` records 1780
additional checks, zero failures, every normalized old/final lower
endpoint, the full exact minimum, dimension and input/code/replay
bindings. All original inputs are unchanged. The repaired L115 replay
binding is explicitly checked as a string naming its single saved
replay; the earlier audits retain their filename-to-hash maps. The
original pre-evaluation schema exception remains preserved in
`drafts/2026-10-23-fixed-product-coupled-working.md`. The complete minimum
fraction and empty failure list were inspected, and the reconstruction
consumes all relevant arrays rather than sampled previews.

The canonical L112/L113, L114 and L115 reviews are reused in their
proved scopes, including the consumed L105 minima/interval validity.
The assertion here is box-wide PSD; exact-N feasibility is asserted
only at L112's enclosed root. No root solve, scan, retuning, box
refinement or other-anchor test was performed. ATTEMPTS/094's exclusion
stop is retained. Full source PSD, other layers/anchors, stronger
distributions, global positive-root uniqueness, measures, packing,
RS realization and arbitrary-center safety remain unresolved.

## Mathlib

Full matching unequal-layer beta/union-matrix/Schur/interval application:
not checked. Supporting finite-set counts, rational interval inequalities
and mixed-layer spectral results: not checked. Unknown availability is
not evidence of absence; no uninspected Mathlib theorem is used.
