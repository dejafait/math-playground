# L016 — Quotient and finite certificate for the saved common-coordinate triple

## Hypotheses

Let F=F_(97^20), let H be the order-sixteen subgroup of F_97^*,
and let C=RS[F,H,8]. Use the pinned event on 1/4<=delta<5/16 and
L010's moments. Suppose a,b satisfy L010's nonpersistent hypotheses,
and their unique four-error representatives at parameters 0,1,2 have
supports
\[
 A_0=\{1,8,12,18\},\quad A_1=\{1,8,22,27\},\quad
 A_2=\{1,33,47,50\}.
\]
All input weights range over F; there is no prime-subfield restriction.
Put U=A_0 union A_1 union A_2,
\[
 Q(X)=\prod_{x\in H\setminus U}(X-x),\quad c_x=Q(x),\quad
 v_x=(x,x^2,\ldots,x^8).
\]

## Conclusion

After multiplying both inputs by one nonzero scalar, their syndrome
pencil has the exact parameterization
\[
 s(t)=(p+t(q-p))v_1+(1-t/2)zv_8+h_0+t h_1,               \tag{1}
\]
where
\[
 \begin{split}
 h_0&=-c_{12}v_{12}-c_{18}v_{18},\\
 h_1&=c_8v_8/2+c_{12}v_{12}+c_{18}v_{18}
                    +c_{22}v_{22}/2+c_{27}v_{27}/2,
 \end{split}
\]
and the full-triple condition is
\[
 p q z(z+c_8)(-p+2q-c_1)\ne0.                            \tag{2}
\]
For each fourth four-set K, quotienting its recurrence equations by
the constant columns at 1 and 8 gives affine equations in t over F_97.
Thus its possible parameters, before the full-weight gates, are either
none, one element of F_97, or an explicitly retained universal family.
This reduction holds over every extension of F_97.

The exhaustive rational certificate described below gives
\[
 |B(a,b)|\le5                                             \tag{3}
\]
for this fixed triple, and an actual pencil with five bad parameters
attains the bound. The numerical count in (3) has explicit dependence
on the finite certificate: the analytic argument reduces all extension
inputs to 1817 small rational systems; the script exhausts those systems.
This is a fixed-triple class exclusion, not a global improvement of
L010's sixteen or a resolution of the grand challenge.

## Proof

L010 proves ker(sigma)=C, minimum codeword weight nine, and injectivity
of sigma on every coordinate set of size at most eight. Let e_0,e_1,e_2
be the three errors. Their moments satisfy
\[
 \sigma(-e_0+2e_1-e_2)=0.
\]
The word on the left is supported on U, which has nine coordinates.
A degree-less-than-eight polynomial vanishing at H minus U is a
scalar multiple of the monic degree-seven Q. Hence
-e_0+2e_1-e_2=lambda*c. At coordinate 12 only e_0 is present;
its nonzero weight forces lambda nonzero. Scaling all errors and
inputs by lambda^-1 normalizes lambda=1. This preserves both code
membership and the original event because C and its restrictions are
linear spaces.

Write e_0(1)=p, e_1(1)=q and e_0(8)=z. Reading the normalized
codeword relation coordinate by coordinate gives the weights
\[
\begin{array}{c|rrrr}
 e_0&1:p&8:z&12:-c_{12}&18:-c_{18}\\
 e_1&1:q&8:(z+c_8)/2&22:c_{22}/2&27:c_{27}/2\\
 e_2&1:-p+2q-c_1&33:-c_{33}&47:-c_{47}&50:-c_{50}.
\end{array}
\]
Each c_x on U is nonzero. Thus (2) is exactly the condition that
all twelve prescribed weights are nonzero. Conversely these formulas
give three words with the required moment relation for every p,q,z
satisfying (2). Their first two syndromes determine the affine pencil,
and direct substitution yields (1). No kernel solution is discarded:
the shortened codeword coefficient together with p,q,z describes the
entire four-dimensional homogeneous triple kernel.

For a four-set K write f_K(X)=product_(x in K)(X-x)=sum_j f_j X^j
and define
\[
 F_K(m)_i=\sum_{j=0}^4 f_j m_{i+j},\qquad 1\le i\le4.
\]
A moment vector m belongs to the span of the four columns v_x,
x in K, if and only if F_K(m)=0. Necessity follows from f_K(x)=0.
For sufficiency, solve the first four moments for the four weights by
Vandermonde inversion. The recurrence successively determines moments
five through eight, so their values agree with m. This is the same
converse moment argument used in L010; it does not assume that a
manufactured locator comes from a valid error word.

For t not in {0,1,2}, set r=p+t(q-p), w=(1-t/2)z. The fourth-support
condition is
\[
 C_K\binom r w+F_K(h_0)+t F_K(h_1)=0,
 \qquad C_K=(F_K(v_1),F_K(v_8)).                          \tag{4}
\]
Since F_K(v_x)=f_K(x)(x,x^2,x^3,x^4), the constant matrix C_K
has rank equal to the number of elements of {1,8} absent from K.
The nonzero columns are independent because 1 and 8 are distinct.
A basis of its left kernel is defined over F_97. Applying that basis
to (4) gives affine polynomials in t. Their monic gcd is zero if all
equations vanish, constant if inconsistent, or linear with a root in
F_97. Extension of the coefficient field creates no other isolated
roots. Equivalently, the (rank(C_K)+1)-minors obtained by adjoining
the last column in (4) give the same condition. Because all the
other columns are constant, those minors are also affine in t.

The command `python3 scripts/coefficient-feasibility/shared_quotient.py`
records the complete certificate in
`scripts/coefficient-feasibility/shared-quotient-result.json`.
It enumerates each of the binom(16,4)-3=1817 other supports exactly
once, computes both the left-kernel equations and all smaller minors,
and checks equality of their monic gcds. Arithmetic uses exact integers
modulo 97, not floating-point tolerances. The classifications are:

| Fourth-support systems | Count | Consequence |
| --- | ---: | --- |
| Inconsistent | 1610 | No finite parameter |
| Isolated at 0,1,2 | 190 | No new parameter |
| Isolated with z=0 | 3 | Violates the full A0 weight at 8 |
| Admissible isolated | 13 | Listed below |
| Universal | 1 | K={12,18,22,27} |

At t=0,1,2 the stipulated errors already have weight four. Injectivity
on at most eight coordinates ensures that no different sparse error
can occur at any of those parameters. Each of the thirteen retained
supports omits 1 and 8; thus (4) uniquely fixes r and w, and hence z.
Their full fourth weights, obtained from the first four moments and
checked against all eight, are nonzero. Their complete list is:

| K | t | z | r |
| --- | ---: | ---: | ---: |
| {12,33,89,96} | 15 | 88 | 22 |
| {18,33,89,96} | 30 | 54 | 44 |
| {22,47,64,79} | 43 | 43 | 43 |
| {22,50,64,85} | 26 | 22 | 79 |
| {27,33,70,89} | 28 | 20 | 4 |
| {27,33,75,96} | 74 | 75 | 66 |
| {27,33,79,85} | 72 | 79 | 38 |
| {27,47,64,79} | 67 | 26 | 26 |
| {27,50,64,85} | 30 | 78 | 80 |
| {33,47,70,96} | 81 | 11 | 83 |
| {33,50,70,96} | 69 | 11 | 55 |
| {47,50,70,96} | 41 | 11 | 22 |
| {50,70,79,89} | 42 | 5 | 70 |

This table's exhaustiveness is the finite-certificate input to the
numerical bound, not an analytic assertion that follows merely from
dimension counting. The saved data retain all rejected systems, their
equations, and the thirteen solved Vandermonde weight vectors. The
script also checks that the homogeneous parameterization has rank
four and that the original triple constraint has rank eight.

The codeword has c_1=28 and c_8=72. Every z other than 11 occurs
in at most one retained row. For z=11 the three points (t,r) are
(81,83), (69,55), (41,22), on the line r=88+67t. Two of them
force that line, over F as well as over F_97. But its value at 2 is
28=c_1, so -p+2q-c_1=r(2)-c_1=0, violating (2). Consequently
every full-triple pencil satisfies at most one isolated row. This
argument includes nonrational p,q: two distinct rational t-values
still determine the coefficients of the same affine polynomial.

For the sole universal support, (4) gives
\[
 r=0,\qquad w=-c_8t/2,
\]
and its four error weights are
\[
 -(1-t)c_{12},\quad -(1-t)c_{18},\quad t c_{22}/2,
 \quad t c_{27}/2.                                     \tag{5}
\]
They are nonzero outside t=0,1. Substituting w=(1-t/2)z gives
\[
 t=\frac{2z}{z-c_8}
\]
when z!=c_8. The full gate z!=0,-c_8 ensures this parameter is
different from 0,1,2. The additional condition r(t)=0 can hold
at most once. When z=c_8 no finite parameter satisfies the equation.

For completeness the certificate independently tests the coefficient
of t in (4) for every four-set, including the original three, to
classify a possible sparse point at projective infinity. Its only
full-triple possibility is the same universal K with z=c_8 and
q-p=0, with weights c_12,c_18,c_22/2,c_27/2. It replaces, rather
than adds to, its finite universal parameter. Thus there are at most
three stipulated, one isolated and one universal sparse points even
on the projective syndrome line.

There is no hidden lower-weight parameter. Any error of weight at
most three can be enlarged to a four-set K for purposes of (4).
At 0,1,2 uniqueness excludes such an error. At a new finite parameter,
every surviving isolated system has four nonzero weights, and the
universal system has the four nonzero weights (5). All other systems
are excluded either by their equations or the full-triple gate.
The infinity check likewise has four nonzero weights. Since sigma
is injective on K, none can also be a smaller representative. Thus
the list controls all weight-at-most-four parameters over F, not
only those found in a prime-field sample. L010 identifies the finite
decodable set with the original bad set under the hypotheses, proving
(3), with the stated finite-certificate dependence.

To attain five take (p,q,z)=(5,85,11). Its triple weights are
(5,11,53,16), (85,90,21,53), (40,64,63,28). The universal parameter
is 6, because 2*11/(11-72)=6 and r(6)=5+80*6=0. The isolated row
at 81 is also satisfied, because r(81)=83. Its weights on
{33,47,70,96} are (4,64,17,42), as independently solved in the
certificate. These give the five sparse parameters {0,1,2,6,81}.
All errors have weight four and their support intersection is empty.
The determinant is nonzero at 0. By L010's pointwise locator formula,
an identically zero coordinate locator would force that coordinate
to belong to every one of these weight-four supports. Their empty
intersection excludes it. L010's original-support argument proves all five
are bad, and (3) proves there are no others over the full field.

The auxiliary actual-pencil audit recomputes the determinant and
locator from the input words, verifies failure/agreement on all 2517
admissible supports in two affine charts, and independently checks
the eight-moment recurrence. The original direction has no sparse
point at infinity, checked by all fourth-support recurrences. A
chart whose infinity has no coordinate root gives degree-four
coordinate locators and a degree-64 resultant. All 48 residuals of
the covered fourth-root comparison and the full L010 equality test
are retained; the fourth-power identity fails. Squarefree radical
incidence and modular Frobenius give exactly five bad roots over
F_(97^20), all already in F_97, with common locator gcd one excluding
lower weights. These are independent checks of the fixed-class
conclusion, not an extension-input enumeration or a global bound.

## Mathlib

The full shared-coordinate quotient and fixed-triple count: **not checked**
in Mathlib. Supporting shortening, Vandermonde, kernel and recurrence
coverage: **not checked**. The proof specializes the already established
local moment and minimum-distance arguments; no matching theorem or Lean
verification is claimed.

Supporting resultant product and specialization coverage is **present**
in the previously inspected
[Resultant.Basic at commit 300d0e535721bc098547106fc297d8ba2a63f6bb](https://github.com/leanprover-community/mathlib4/blob/300d0e535721bc098547106fc297d8ba2a63f6bb/Mathlib/RingTheory/Polynomial/Resultant/Basic.lean),
including
[`Polynomial.resultant_prod_left`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Resultant/Basic.html#Polynomial.resultant_prod_left)
and
[`Polynomial.resultant_map_map`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Resultant/Basic.html#Polynomial.resultant_map_map).
The full fixed-triple statement is **absent from that source checked**;
coverage elsewhere is **not checked**. These are supporting audit tools,
not a full matching result.

The audit imports the resultant formula from Milne, *Fields and Galois
Theory*, v5.10, Proposition 4.35(b),
[printed p. 58](https://www.jmilne.org/math/CourseNotes/FT.pdf#page=58),
and its exact-field root description on printed p. 53. Squarefree
multiplicity recognition is supported by Volkovich, *On Some Computations
on Sparse Polynomials*, Lemmas 23–24,
[p. 48:8](https://drops.dagstuhl.de/storage/00lipics/lipics-vol081-approx-random2017/LIPIcs.APPROX-RANDOM.2017.48/LIPIcs.APPROX-RANDOM.2017.48.pdf#page=8).
Those statements were read in the saved SPECIALIZE assessment and are
reused. This step reproduces the covered moment/recurrence framework
and its exact finite implementation; it claims no certified originality
or progress beyond the checked literature.
