# L118 — The unchanged product box passes the included-anchor three-shell matrix

## Hypotheses

Use L021's canonical positive rational primal vector a_i and L098's
normalization, with exactly the original box of L112. Write

    N=floor(65537^28/2^128)+1, H=binomial(1024,68), rho=N/H,
    U=binomial(1024,64)/binomial(68,64),
    g_i=binomial(68,i)binomial(956,i),
    c_0=1, c_1=...=c_4=0,
    c_i=(N-1)a_i/((U-1)g_i), 5<=i<=68.

For k=i-5, retain the exact integers q_k=`point[k]` and
p_k=`scale_powers[k]` in
`scripts/finite-support/positive-factor-enclosure.json.gz`. Set

    l_i=10^p_k*(q_k-10^25)/10^70,
    u_i=10^p_k*(q_k+10^25)/10^70,
    x_i in [l_i,u_i], 5<=i<=68.

Every original point, scale and endpoint is unchanged. On the universe V
of 68-subsets of a 1024-point set use L112–L114's same normalized moments:
singleton 1, pair c_i at half-distance i, and distinct-triple value
y=x_i*x_j*x_h when all three sides are at least five. A distinct triple
with a side 1,...,4 has y=0. A repeated triple with sides (0,b,b)
has y=c_b, including y=1 if all three supports coincide. Nonempty
homogeneous moments equal rho times these normalized values.

Fix A in V and let S_l(A)={B in V: |A\B|=l}. Let M be the union
moment matrix indexed by {A} and all {A,B} with B in the union of
S_5(A), S_6(A), S_7(A). No code, full source PSD, measure, global
positive-root uniqueness or RS realization is assumed. The root/upper,
consumed-lower and included/excluded two-shell audits retain their
original scopes; L117 is a parallel slice, not an included-entry input.

## Conclusion

For every A and every x throughout this unchanged box, M is positive
definite. After dividing by rho and eliminating the one positive anchor,
the complete source reduction has 36 three-by-three, 13 two-by-two and
15 one-by-one blocks. All 149 normalized elimination-pivot intervals
have strictly positive lower endpoints. In layer order 5,6,7 their
respective uniform bounds are

    layer five:  >=630869/10^6,
    layer six:   >=638632/10^6,
    layer seven: >=638510/10^6.                         (1)

Each layer's smallest certified lower endpoint occurs at (a,b)=(4,0)
and is strictly below its displayed bound plus 10^-6. These bounds
describe the interval certificate, not attained minima of eigenvalues
or pivot functions. Independently, all 306 nonempty principal minors
of the complete reduced blocks have strictly positive interval lower
endpoints.

At L112's enclosed root this retains the enlarged necessary matrix
together with L113–L114's ordinary scalar and exact-N feasibility. It
parks exclusion by this fixed slice only. This is a REPRODUCTION of
assessed spectral, Schur and interval tools, with no claim beyond the
sources checked. Full source PSD, other matrices, stronger distributions,
global uniqueness, measures, packings, RS realization and arbitrary-center
67/68-agreement safety remain unresolved. The 955–957 bracket is unchanged.
The separate critical proof audit below retains this application; there
is no complete candidate resolution.

## Proof

**Imported theorems and specialization.** The prior SPECIALIZE assessment
is `drafts/literature/2026-10-24-fixed-product-included-five-six-seven-psd.md`.
Import Polak, *Semidefinite Programming Bounds for Constant-Weight Codes*,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), §1.1 (1)–(3),
Proposition 1.1 and full indicator proof, printed p.2. At order three
the singleton-conditioned indices are exactly {A} and {A,B}; selecting
three full shells is a principal restriction. Use the proved constant-weight
A(n,d,w) qualification, as recorded in foundations/12. Here n=1024,
w=68,d=10. This gives necessity for indicators, not sufficiency of a
passing assignment for a representing measure.

Import Schrijver, *New code upper bounds from the Terwilliger algebra
and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866, DOI
[10.1109/TIT.2005.851748](https://doi.org/10.1109/TIT.2005.851748),
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
(7), Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59),
III.B (64), manuscript pp.2,5–7. Its complete tensor decomposition,
unequal layers, extension/reset argument and positive rescalings apply
to arbitrary invariant coefficients. The two ground-set sizes are 68
and 956; all selected layers 0,5,6,7 are within range. Principal layer
restriction is allowed. Use the congruent integer-beta convention in
foundations/04,09, without Schrijver (61)'s unused complement prefactor.
The algebraic theorem requires neither a code nor a measure.

Import the positive-leading-block Schur congruence from Brouwer–Haemers,
*Spectra of Graphs*, [author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
Theorem 2.7.1(i), p.36. Import enclosing-expression arithmetic from Rump,
*Verification methods: Rigorous results using floating-point arithmetic*,
Acta Numerica 19 (2010), 287–449, DOI
[10.1017/S096249291000005X](https://doi.org/10.1017/S096249291000005X),
[corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
§5.5 (5.16)–(5.17), author p.28. Foundations/09,14 retain the inspected
hypotheses and essential cases. Exact rational endpoints avoid rounding
error, while repeated occurrences can enlarge interval bounds. All
inverted pivots below have positive lower endpoints. L112 already
supplies its root; no new root or global uniqueness theorem is used.
No imported theorem is reproved. Finite verification is necessary because
these theorems do not decide the frozen coefficients' signs.

**Complete source dictionary.** Write

    B=(A\X) union Y, C=(A\X') union Y',
    |X|=|Y|=l, |X'|=|Y'|=m,
    t=|X intersection X'|, s=|Y intersection Y'|,
    h=l+m-t-s.

For the six unordered layer pairs 55,56,57,66,67,77 every
0<=t,s<=min(l,m) occurs. Their head and tail unions have size at
most 14, within both ground-set sizes. In bit order A,B,C the eight
atoms (masks 0,...,7) are

    (956-l-m+s,t,l-s,m-t,m-s,l-t,s,68-l-m+t).

They are nonnegative and exhaust 1024 points; bijections of equal atoms
give precisely the stabilizer orbits. Thus the full relation count is
36+36+36+49+49+64=270, with the transposed rectangles supplied by
symmetry. With B fixed, the actual multiplicity and entry are

    D(l,m,t,s)=binomial(l,t)binomial(68-l,m-t)
               *binomial(l,s)binomial(956-l,m-s)>0,
    K_lm(t,s)=c_l       if h=0,
              0        if 1<=h<=4,
              x_l*x_m*x_h if h>=5.                    (2)

Here h=0 occurs only at a Boolean diagonal l=m,t=s=l. No product
replaces that pair value. Distances through 14 are retained; no old
minimizing column or free seven/seven entry is imported. The normalized
anchor row is 1,c_5*1,c_6*1,c_7*1. All seven layer cases (0,0),
(0,l),(l,0), l=5,6,7, have Boolean value c_max(l,m), their own opposite
pair and multiplicity g_m for l=0, otherwise 1.

The independent verifier constructs actual A,B,C for every relation
and all 1620 orders. In each order (R,S,T) it reconstructs
i=|R\S|, j=|R\T|, t'=|(R\S) intersection (R\T)|,
s'=|(S\R) intersection (T\R)| and h'=|S\T|, checking

    h'=i+j-t'-s', t'-s'=t-s,
    D'=binomial(i,t')binomial(68-i,j-t')
        *binomial(i,s')binomial(956-i,j-s').

The head/tail multinomial product equals g_i*D'=g_l*D(l,m,t,s).
Each presentation saves its own source tuple, D', opposite pair c_h'
and y interval. The six y values agree, including presentations outside
the retained layers; complete eight-atom keys check every collision.
The coincident i=0 case and the two endpoint repetitions each occur
six times, with D'=g_j,1,1 respectively. Distinct forbidden entries
have zero capacity and value. The separate anchor coincident entry is 1.
The recipe itself is invariant under permutations fixing A, since
it uses distances and Boolean repetitions. This uses no averaging of
actual subgroup-label restrictions or of an arbitrary feasible point.

**One coherent complete source reduction.** For each 0<=a,b<=7 let
T_ab={l in {5,6,7}: l>=max(a,b)} and put

    d_l(a,b)=binomial(68-2a,l-a)binomial(956-2b,l-b)>0,
    beta(n,l,m,a,t)=sum_(u=max(a,t))^min(l,m,n-a)
      (-1)^(u-t)binomial(u,t)binomial(n-2a,u-a)
      *binomial(n-a-u,l-u)binomial(n-a-u,m-u).

Ordinary out-of-range binomials vanish. Eliminate the positive scalar
anchor 1 once from the entire normalized matrix M/rho. The full
shell coefficient is K_lm-c_l*c_m*J, so its congruent source blocks are

    C_lm=sum_(t,s) beta(68,l,m,a,t)beta(956,l,m,b,s)K_lm(t,s)
          -1_(a=b=0)c_l*c_m*g_l*g_m, l,m in T_ab.     (3)

All six constant corrections are retained. In particular the cross
terms with layer seven are c_5*c_7*g_5*g_7 and c_6*c_7*g_6*g_7.
Separate shell eliminations would omit them. No nonconstant mode
has an anchor coordinate. Every L116 block and both its pivot
intervals are recovered exactly at the identical normalization.

The independent signed subset-action check extends L116's finite
normalization to all nine ordered layer pairs. On r-subsets of an
n-set use the product of a disjoint signed point-pair differences;
its squared norm is 2^a*binomial(n-2a,r-a). Evaluating the action
from m-subsets at an l-subset containing all positive partners and
no negative ones gives intersection-t coefficient

    eta(n,l,m,a,t)=sum_(z,b: a-z+b=t)
       (-1)^z binomial(a,z)binomial(l-a,b)
       *binomial(n-l-a,m-a-b),                         (4)

where 0<=z<=a and 0<=b<=l-a. Nonzero terms choose exactly one member
of each pair and m-a ordinary points; the two ordinary regions have
sizes l-a and n-l-a. Thus (4) counts complete actual subsets with
their signs. Every term, for n=68,956, all ordered l,m and all a,
is saved. Exact comparisons check

    binomial(n-2a,l-a)*eta(n,l,m,a,t)=beta(n,l,m,a,t),
    binomial(n-2a,l-a)*eta(n,l,m,a,t)
       =binomial(n-2a,m-a)*eta(n,m,l,a,t).             (5)

Consequently tensor-vector bilinear forms are 2^(a+b) times (3),
with the same positive factor in every layer. This checks both signs
of each rectangle in one coherent congruence. Completeness comes from
the imported source theorem, not from this finite action test alone.

The positive multiplicity is

    m_ab=(binomial(68,a)-binomial(68,a-1))
          *(binomial(956,b)-binomial(956,b-1)).

For each l its sum over a,b<=l is g_l, so
sum_(a,b) m_ab*|T_ab|=g_5+g_6+g_7. The original matrix has dimension
1+g_5+g_6+g_7, including the eliminated anchor. All 64 modes survive:
36 have three layers, 13 have two, 15 have one. There is no surviving
coordinate for a>7 or b>7. No omitted or new-only mode is suppressed.

**Whole-box interval certificate.** Enclose each (2) by its exact
point interval on Boolean/null entries and by
[l_l*l_m*l_h,u_l*u_m*u_h] on permitted distinct entries. Form (3)
with signed rational interval sums, subtracting the exact constant
correction. For any enclosure [v_-,v_+], multiplying by a negative
coefficient swaps its endpoints. Products take all four endpoint
products; squares include zero if the interval contains zero.

At each elimination step let P enclose its diagonal pivot. Only if
P_->0, use P^(-1)=[1/P_+,1/P_-] and enclose the remaining entries by

    [C_ij] <- [C_ij]-[C_ki]*[C_kj]*P^(-1),          (6)

using the square operation for i=j. Every update uses the same
pre-step matrix. Expression inclusion covers correlations between
repeated variables and overestimation. Induction through the positive
Schur congruences shows that positive pivot lower endpoints certify
each entire block for every point of the box. Normalize the pivot
of layer l by the positive exact c_l*d_l(a,b); this does not change
its sign. No zero pivot is inverted. The 149 resulting intervals
give (1); the verifier checks their exact rational lower bounds and
brackets. The full minimum for the new layer is saved at
`per_layer_minimum_pivot/7/value` in the verification certificate.

As a separate finite check, the verifier expands every nonempty
principal determinant directly over permutations using full block
intervals, divides by the product of the corresponding c_l*d_l,
and checks its lower endpoint positive. There are
36*7+13*3+15=306 such minors. This supplies a second whole-block
certificate, rather than a sample of minors. Independently collecting
common product coefficients gives intervals contained in the entrywise
enclosures, without changing the original box. Diagonal polynomial
trace checks cancel every distinct-product coefficient and recover
g_l*c_l before anchor subtraction and correction trace g_l*c_l^2.
These are identities of coefficient polynomials, not of overestimated
interval traces.

Thus all source blocks are positive definite throughout the box.
Their complete source decomposition and invertible full-anchor
congruence prove M/rho, and hence M, positive definite. In particular
the enclosed root passes. Contractions hold at that root only;
the PSD and ordinary scalar conclusions hold throughout the box.

**Evidence, failures and limits.** Reproduce from this notebook:

    python3 scripts/finite-support/fixed_product_three_shell.py
    python3 scripts/finite-support/verify_fixed_product_three_shell.py

The constructor saves `scripts/finite-support/fixed-product-three-shell.json`:
596 checks, zero failures, all endpoints, canonical pairs, 270 entries,
64 complete blocks, corrections and every interval elimination stage.
It retains the root/upper, consumed-lower and both two-shell audits,
binding their complete saved inputs, code and replay evidence. The
full 64 root margins and every consumed lower row are checked, without
rerunning a nonlinear solve. No hashed old mathematical input was edited.

The verifier imports no constructor routine. Its complete certificate,
`scripts/finite-support/fixed-product-three-shell-verification.json`,
reports 6300 checks and zero failures, with full actual-union data,
1620 presentations, all signed action terms, 149 pivots, 306 positive
minors and the complete source dimension checks. It reconstructs every
saved entry, block, correction and stage from factorial binomials and
the original box, rather than accepting a saved success flag. All
arrays are consumed in full. The complete failure lists and the
load-bearing exact minimum fractions were inspected with the scoped
JSON inspector; previews are not a proof. The supplementary frozen-input
JSON is a lossless extraction of the original point/scales/box/N/H,
fully compared against the compressed authoritative original.

Two initial JSON-inspector reads failed because that helper accepts
plain JSON, not gzip. This preceded matrix calculation; the lossless
extraction resolved access and changed no mathematical value. A final
verifier rerun added exact layer-minimum brackets and total positive
pivot/minor assertions, with no coefficient, normalization or box change.
The working record preserves these details. No mathematical failure,
negative block or interval straddle occurred. No solve, scan, retuning,
refinement, other-anchor enlargement or global-PSD test was performed.

This stops only this necessary principal matrix as an exclusion
diagnostic for the frozen assignment. Earlier distinct-witness and
smaller-slice stops remain valid. Larger matrices, global consistency,
measures, actual packings and a common-center RS list do not follow.
The separately approved critical proof review is completed below.

**Separate critical proof audit (2026-10-24, step 445).** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-24-l118-included-three-shell-critical-audit.md`.
This review retains the conclusion without mathematical repair. It
supersedes pending-review wording for L118 in the overview and
ATTEMPTS/096. The argument and direct mathematical inputs are unchanged;
no overview assembly or DAG change is needed. This is local verification
of an application of known tools, not a new general theorem or a result
beyond the assessed sources.

The entire manuscript, constructor and independent verifier were reviewed
against the retained source statements and essential cases. The fixed
recipe is invariant under permutations fixing A because both distances
and Boolean repetition are invariant. Every head/tail partition is an
actual orbit, and permutations within A and its complement give
transitivity on that partition. This proves exhaustion for each A; it
makes no symmetry claim for arbitrary labeled RS restrictions. The
positive homogeneous factor rho multiplies the whole matrix. The
reviewed root/upper and consumed-lower results supply precisely the
stated root and scalar conclusions. The PSD assertion is box-wide;
contractions are asserted only at the enclosed root. L117's retained
excluded-anchor result supplies no included-entry or PSD sign premise.

The full original verifier was replayed, without its constructor, to
`scripts/finite-support/l118-critical-reverification.json`. All 6300
checks pass, and the entire replay equals the original verification
certificate, including all 270 relations, 1620 presentations, signed
actions, blocks, corrections, stages, pivots and minors. All original
input bindings and prior audit/replay bindings agree. This reconstruction
consumes the complete evidence rather than accepting counts or flags.
The additional audit independently computes exact N, H, rho, canonical
pairs and all 64 original point/scale/endpoint triples. It compares the
whole frozen extraction with the compressed authoritative input and
retains every original root margin and consumed lower-row identity
through the full verifier and already reviewed input scopes.

For each of the 270 relations the additional audit reconstructs the
eight atoms in (2)'s notation, and then permutes those counts directly
in all six orders, independently of the verifier's actual-set method.
From the permuted counts q it recovers i=q_1+q_5, j=q_1+q_3,
t'=q_1, s'=q_6, h'=q_2+q_3. The exact multinomial product is
68!*956!/product_(mask=0)^7 q_mask!. All presentations agree with
that count, g_i*D'=g_l*D, t'-s'=t-s, their own opposite pair c_h',
and the shared union entry. Each repetition type occurs six times;
all 408 distinct null presentations are retained (136 with forbidden
opposite side and 272 with forbidden anchored side). These cases
have zero union entry and zero minimum pair capacity. Permitted products
retain third distances through 14 and repeated side distances. The
seven anchor cases include the all-equal value one before elimination.

All 118 signed-action records are checked term by term, including zeros,
for both ground sets and all nine ordered layer pairs. A nonzero signed
function chooses exactly one element from each designated pair, followed
by m-a ordinary points. Its norm has 2^a choices of pair members and
binomial(n-2a,l-a) ordinary choices. Thus the factor 2^a is common
across layers, and tensoring gives the common factor 2^(a+b).
All 242 rectangular weighted-action comparisons agree. The source's
complete decomposition supplies the mode spaces and their coherent
matching; these signed checks verify its finite normalization, not its
completeness in isolation. Every multiplicity and d_l is positive, and

    1 + sum_(a,b) m_ab*|T_ab| = 1+g_5+g_6+g_7.

This retains 36 three-dimensional, 13 two-dimensional and 15
one-dimensional blocks, with no omitted new-only mode.

For the constant mode write u=(c_5*g_5,c_6*g_6,c_7*g_7)^T and let C
be the full three-by-three block after the anchor subtraction. Before
elimination the block and congruence are

    K = [[1,u^T],[u,C+u*u^T]],
    T = [[1,-u^T],[0,I_3]],
    T^T*K*T = diag(1,C), det(T)=1.

Block multiplication gives the displayed identity for arbitrary C.
The audit also checks every entry at all 64 independent endpoint
choices of the six symmetric entries. This is an identity check, not
an inference of whole-box PSD from corner signs. It retains all six
anchor corrections, particularly both cross terms with layer seven;
all nonconstant corrections vanish.

The replay and additional audit reconstruct every interval elimination
stage from its entire pre-update matrix. For a positive pivot interval
P and a remaining off-diagonal interval V, let
q_+=max(V_-^2,V_+^2), and let q_-=0 if V contains zero, otherwise
q_-=min(V_-^2,V_+^2). A remaining diagonal interval A updates to

    [A_- - q_+/P_-, A_+ - q_-/P_+].

Off-diagonal updates use all endpoint products of both cross intervals
and [1/P_+,1/P_-]. Every division checks 0<P_-<=P_+ first. For each
remaining layer i the audit additionally verifies the denominator-cleared
comparison

    A_-*P_- - q_+ >= b_i*c_i*d_i*P_- > 0,

where b_5=630869/10^6, b_6=638632/10^6, b_7=638510/10^6.
These include both elimination stages of every three-layer block;
no zero pivot or midpoint sign is used. Every old L116 block and
normalized pivot agrees exactly. The 149 complete pivot intervals
satisfy (1), and each layer has unique minimum lower endpoint at (4,0),
strictly below b_i+10^-6. The full fractions are saved under
`per_layer_minimum_pivot` in the audit certificate and were inspected
in full. They bound certificate endpoints, not actual spectral minima.

As an additional determinant check, for each three-by-three block
[[A,D,E],[D,B,F],[E,F,C]] use

    det = A*B*C + 2*D*E*F - A*F^2 - B*E^2 - C*D^2.

For each two-by-two principal block use A*B-D^2; singletons are their
diagonals. Enclosing products and zero-aware squares give strictly
positive lower endpoints for every one of the 306 principal minors.
Each closed-form interval lies inside its corresponding saved
permutation-expansion interval, whose normalized endpoints also agree.
This independently checks the full minor list and ordering. The replay's
trace checks are coefficient-polynomial identities, not identities
between interval overestimates. Interval inclusion, positive pivots and
the imported invertible congruences establish whole-box positive
definiteness with dependency overestimation allowed.

Reproduce the bounded audit, preserving both originals:

    python3 scripts/finite-support/critical_audit_l118.py

The complete additional certificate is
`scripts/finite-support/l118-critical-audit.json`: 6370 checks,
zero failures, all original endpoints, every pivot comparison and all
306 closed-form minor intervals, with original/replay bindings. Every
consumed original remains unchanged. An initial successful audit was
rerun after removing an unused temporary factorial computation; all
compared values and outcomes stayed identical. No mathematical failure,
solve, scan, retuning, box refinement or extra matrix test occurred.
The earlier two gzip-inspector access failures and extraction repair
remain preserved in the construction record.

This retains only the unchanged included-anchor three-shell application
and its stop as an exclusion diagnostic. Full source PSD, stronger
distributions, global positive-root uniqueness, measures, actual
packings, RS realization and the 955–957 boundary remain unresolved.

## Mathlib

Full matching mixed-layer Terwilliger theorem and this finite three-shell
application: not checked. Supporting signed subset-action, Schur,
rational-interval and finite-matrix PSD coverage: not checked. Unknown
availability is not evidence of absence; no uninspected Mathlib result
is imported.
