# L070 — Six-label error pairs force a third error at equality

## Hypotheses

Use a gated L057 triangle over F=F_(97^20), with H the order-sixteen
subgroup of F_97^*, C=RS[F,H,8], and the pinned radius cell
1/4<=delta<5/16. Retain all its arbitrary extension-field weights and
original finite-chart parameters gamma_0,gamma_1,gamma_2. Write
s(T)=sigma(a_*)+T sigma(b_*) for its eight shifted moments and B for its
actual finite bad-parameter set. L041/L057 supply three distinct full
base errors, nonzero polynomial D and every nonzero coordinate locator.

Choose two distinct additional finite parameters eta_1,eta_2 and their
actual full-weight errors e_1,e_2 supplied by L057. Write
K_i=supp(e_i), V=K_1 union K_2, and suppose |V|=6. Thus |K_i|=4
and R=K_1 intersect K_2 has size two. Set
\[
 r_x=e_2(x)/e_1(x)\in F^*\qquad(x\in R).
\]
No equality, rationality of these ratios or existence of a third error
on V is assumed initially. Count all additional relaxed recoveries by
distinct original finite parameters, including both-zero lifts and
recoveries with vanishing fourth weights.

## Conclusion

If |B|=16, the two ratios r_x are equal to one common r in F minus
{0,1}. The original finite parameter
\[
             eta_3=\frac{eta_2-r eta_1}{1-r}                 \tag{1}
\]
is different from eta_1 and eta_2 and has an actual full-weight error
with support
\[
             K_3=(K_1\setminus K_2)\cup(K_2\setminus K_1).
                                                               \tag{2}
\]
In fact the common-nonunit-ratio condition alone already constructs
this third error, without assuming |B|=16. It can be one of the original
three base events; it is not necessarily a third *additional* event.

The three errors have exactly the explicit original-chart lift required
in L033: for the partition
\[
 Z_1=K_2\setminus K_1,\quad Z_2=K_1\setminus K_2,\quad Z_3=R
\]
of V into pairs, there are d_x in F^* such that
\[
 f_x(T)=d_x(T-eta_i)\quad(x\in Z_i),\qquad
 f_x(T)=0\quad(x\notin V),\qquad sigma(f(T))=s(T).       \tag{3}
\]
The actual errors at eta_i equal f(eta_i). This verifies the missing
third-error hypothesis, but imports no twelve bound from L033.

Consequently, if the two r_x are unequal, or at least one r_x is one,
then |B|<=15 and there are at most twelve additional relaxed recovery
parameters after the three original base events. In the remaining
common-nonunit-ratio case, any hypothetical thirteen-additional violation
belongs to the actual union-six triple branch. Its simultaneous count is
still unresolved here. No universal six-label-pair extraction, uniform
triangle bound or global improvement to 11/q–16/q follows. This partial
result passed the separate scoped critical audit recorded below; the audit
adds no count in the remaining branch.

## Proof

### Reused inputs and scope of the new argument

Use L010's shifted-moment kernel ker(sigma)=C, sparse-error uniqueness,
same-support badness, bound |B|<=16 and equality incidence: at sixteen,
all actual errors have weight four and every label occurs in exactly
four of their supports. L041's local converse and L057 justify these
nonpersistence hypotheses for every gated triangle considered here.
L057's complete moment recovery and finite gates identify the selected
pair with actual errors, not merely projected intersections.

The standard distance input is J. I. Hall, *Notes on Coding Theory*,
GRS chapter, Theorem 5.1.1 and its proof, printed pp. 63–64 of the
[author-hosted chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
undated copy inspected in the reused October 11 pair assessment.
Here the sixteen labels are distinct, evaluation multipliers are one,
and 0<8<=16, so every nonzero codeword has weight at least nine over F.
This theorem is imported, not reproved. The new specialization is the
incidence deficit for a pair's actual affine lift before its other
cancellation parameters have been identified. The prior triple
classification assumes three errors; it does not supply this extraction.

### Actual pair lift and the nonzero-codeword alternative

Define, on all coordinates,
\[
 f(T)=\frac{eta_2-T}{eta_2-eta_1}e_1
       +\frac{T-eta_1}{eta_2-eta_1}e_2.                 \tag{4}
\]
Its denominator is nonzero. It is supported in V for every T, equals
e_i at eta_i, and has sigma(f(T))=s(T) as a polynomial identity by
affine interpolation of the actual syndromes. No coordinate outside V
is used, and no value of f at another parameter is presumed an error.

At any finite bad parameter T, let e_T be the unique error of weight
at most four. If e_T differs from f(T), then f(T)-e_T is a nonzero
codeword. Its support is contained in V union supp(e_T). In particular,
at sixteen-count equality, putting m_T=|V intersect supp(e_T)| gives
\[
 9\le wt(f(T)-e_T)\le |V\cup supp(e_T)|=10-m_T,
 \qquad m_T\le1.                                     \tag{5}
\]
This uses the fixed set V, not the possibly smaller support of f(T).
Zeros in the lift and cancellations against the error only shrink the
support of the difference. Thus (5) includes constant shared coordinates,
distinct shared-coordinate roots, and errors using a zero coordinate of
the lift. The exception f(T)=e_T must be retained explicitly.

Suppose now |B|=16 and that no error outside eta_1,eta_2 equals f(T).
Equation (5) bounds each of those fourteen errors' incidences with V by
one. The two selected errors contribute four each, so
\[
 \sum_{T\in B}|V\cap supp(e_T)|\le 4+4+14=22.         \tag{6}
\]
L010's equality balance requires exactly 6*4=24 on the left. Therefore
there is a third finite bad parameter eta_3, distinct from eta_1,eta_2,
with e_(eta_3)=f(eta_3). This conclusion uses actual equality errors;
neither a projective point at infinity nor an unlifted candidate can
fill the deficit.

### All cancellations at the extracted parameter

For x in K_1 minus K_2, (4) reads
e_1(x)(eta_2-T)/(eta_2-eta_1), with its only zero at eta_2.
For x in K_2 minus K_1 it reads
e_2(x)(T-eta_1)/(eta_2-eta_1), with its only zero at eta_1.
At the third parameter these four coordinates are all nonzero.
Equality has already made e_(eta_3) a weight-four error, so both
coordinates in R must vanish there. For each x in R, the nonzero
affine polynomial in (4) is
\[
 f_x(T)=\frac{e_1(x)}{eta_2-eta_1}
             [eta_2-r_x eta_1+(r_x-1)T].              \tag{7}
\]
If r_x=1 this is the nonzero constant e_1(x), which cannot vanish.
Otherwise its unique finite root is (eta_2-r_x eta_1)/(1-r_x).
Alternatively, evaluating (7) at eta_3 gives directly
\[
              r_x=\frac{eta_3-eta_2}{eta_3-eta_1}.    \tag{8}
\]
Both denominators in these arguments are nonzero. Thus the two r_x
are equal; their common value is nonzero by full weights and is not
one since eta_1!=eta_2. This proves the necessity of (1) and (2).

Conversely, suppose the two ratios equal r!=0,1 without an equality
assumption. Define eta_3 by (1). Subtracting eta_1 and eta_2 gives,
respectively, (eta_2-eta_1)/(1-r) and
r(eta_2-eta_1)/(1-r), both nonzero. Equation (7) makes both R
coordinates zero there, while the four exclusive coordinates are
nonzero. Therefore f(eta_3) has exactly support (2) and all eight
moments s(eta_3). L010 gives its uniqueness and actual same-support
badness. The original chart was never changed; eta_3 lies in F and
is finite. This proves the converse and does not assert that it differs
from the original gamma_i.

On each Z_i the coordinate polynomial has a root eta_i and is nonzero
at the other two selected parameters. It consequently has a nonzero
slope d_x and equals d_x(T-eta_i). This proves (3), including the
nonzero-slope and all full-weight gates. The syndrome nondegeneracy and
original finite chart are inherited unchanged. No rational descent is
asserted or needed. Naming L033 here identifies a proved applicability
condition; none of its subsequent incidence-count claims is an input
to this argument.

### Original triangle count and qualifications

If either ratio condition in the conclusion fails, sixteen is
impossible by (6)–(8), and L010's integer upper bound gives |B|<=15.
Every additional relaxed recovery in L057 is an actual finite bad
parameter different from its three distinct base events. Counting by
parameters, there are consequently at most |B|-3<=12. Possible
repeated support witnesses for a lower-weight error count only once.

Conversely, thirteen distinct additional relaxed recoveries and the
three base events would give |B|>=16, hence equality by L010. Only
then are all recovered errors declared full and coordinate balance
used. This retains zero-weight and both-zero recoveries throughout the
initial contradiction. Their projected classification is irrelevant to
(4)–(8) once their actual moments and finite parameters are recovered.
Thus the restriction covers every case of the approved pair scope,
but does not exclude the common-nonunit-ratio branch. In particular the
mere presence of the extracted third error supplies no further count
contradiction. No finite computation, candidate L040 bound, or original
triangle support symmetry is used.

### Separate critical audit, 2026-10-11

Step 166 independently checked the full argument under the saved EXPLORE
audit scope. No mathematical defect was found. This is a REPRODUCTION
audit of the existing partial result, not a new bound or a claim of
originality. The following checks use the actual extension field and
original finite parameters throughout.

The input check uses L041's local converse, not its initial equality
hypothesis. In the L057 triangle the three supports have empty common
intersection. Their full weights give D(gamma_i)!=0; each label is absent
from at least one support and hence has a nonzero locator evaluation.
Thus L010 applies before any high-count assumption. Its kernel identity
and distance-nine uniqueness apply to every recovered error. The reused
Hall theorem has all its hypotheses: a field, sixteen distinct evaluation
points, unit nonzero multipliers, and dimension eight. No theorem on a
generic evaluation domain or on prime-field weights is being substituted.

For the pair lift (4), the difference from an actual error has zero
syndrome. Distance nine applies only if that difference is nonzero.
At equality the other error has exactly four nonzero coordinates, so
the fixed-union bound is 6+4-m_T, even if either shared lift coordinate
has vanished, or an error coefficient cancels a surviving lift value.
Using supp(f(T)) instead would require extra case distinctions; using V
in (5) is valid in every case. The hypothetical absence of a third
equal-vector error gives exactly fourteen such nonzero differences.
Consequently the maximum is 22, whereas six coordinates used four times
require 24. The two selected errors contribute eight incidences even
though they share two labels: these are error-coordinate incidences.
This verifies that the exceptional equal-vector case is forced rather
than silently treated as a nonzero codeword.

Away from eta_1 and eta_2 the four exclusive coordinates of (4) never
vanish. Each common coordinate is either a nonzero constant (r_x=1)
or a nonconstant affine polynomial with one finite root. If the two
nonconstant roots differ, at most one common coordinate can vanish at
any parameter; if either coordinate is constant, both cannot vanish.
Thus precisely the common-root case permits the extracted weight-four
error. Formula (8) proves that common roots force equal ratios, without
any omitted zero denominator. Conversely r!=0,1 gives the two nonzero
differences displayed after (8), so (1) is finite and different from
both selected parameters. At that value the common pair vanishes and
all four exclusive entries survive. Affine interpolation supplies all
eight moments, not only four of them. L010's nonpersistent same-support
argument then makes this an actual bad parameter on the complement of
its four-support. These checks validate sufficiency without equality.

For the downstream L033 hypothesis comparison, the omission classes
are exactly the three disjoint two-sets Z_i stated in the conclusion.
Every coordinate has a finite root at its assigned eta_i and a nonzero
value at each of the other two parameters, hence a nonzero slope.
The lift is supported on V and has the unchanged moment pencil.
Its coefficient vectors u,v are independent as well: any linear relation
between them would give the same relation between sigma(u),sigma(v),
contradicting the independent coefficient syndromes supplied by L041.
Restriction to V loses no coordinates. This verifies also the rank-two
premise behind L033's projective notation, without a rational-chart
assumption or an invocation of L032 to manufacture a third error.

Finally L057's change of variables has t=rho/E, with rho!=0,1 and
mu!=0,-1, E!=0. Its admitted finite parameters therefore avoid exactly
the three original base events. Its restored equations and all-eight-
moment converse apply in both the isolated and both-zero projected
cases, including vanishing fourth weights. The present argument counts
the image set of these recoveries, so multiple support witnesses do not
increase the count. Subtracting the three original base parameters from
|B|<=15 gives twelve even if the extracted eta_3 is itself a base event.
In a hypothetical thirteen-additional case, fullness and coordinate
balance are used only after L010 gives sixteen total parameters.

No mathematical script or finite enumeration is needed for this audit.
The proof uses L010, L041 and L057; comparison with L033 adds no proof
input. It proves neither universal pair existence nor the remaining
clustered count and imports no L040 bound. Independent main-challenge
and other-pattern gaps remain. Mathlib coverage remains not checked.

## Mathlib

Full pair-to-third equality extraction and its count specialization:
**not checked**. Supporting affine interpolation, code distance,
shifted-moment kernels, sparse uniqueness and double-counting coverage:
**not checked** in Mathlib for this step. L010, L041/L057 and the precise
standard citation above are informal inputs; no Lean verification or
certified originality is claimed. The ready EXPLORE comparison did not
find a matching theorem; that is not evidence of novelty.
