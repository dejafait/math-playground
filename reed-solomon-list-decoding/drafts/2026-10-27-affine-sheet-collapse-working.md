# Full affine-sheet collapse — bounded attempt, 2026-10-27

Invocation target: Test universal collapse of common-center quadratic assignments on the full auxiliary affine sheet {u+vZ:u,v in F_137} in every actual-label L030 family.

Prior coverage: `literature/2026-10-27-affine-sheet-common-center-collapse.md`
(EXPLORE, supplied at invocation). This is mathematical work on that exact
target, not an assessment or an approval of a different target.

The main gap remains arbitrary-center 67/68 safety. A full-sheet collapse
would provide an arbitrary-label common-center restriction; robustness
under deletion, a cap at 1532495, compatible laws and global transfer would
still be unproved. The decisive test is a universal collapse proof, or an
exact permitted nonconstant assignment refuting collapse alone. If neither
is obtained, retain the precise remaining obstruction before stopping.

## Inputs and scope checked before the attempt

L030's construction identifies the full sheet inside every ambient family.
The signed equality and common-root methods in L031/L047/L049 are read and
reused with zero differences, every overlap and every tuple row retained.
The pinned model's unresolved July ABF source qualification is unchanged.
L051/L131/L134 are comparisons only. ATTEMPTS/031–032,106–108 stop their
specific cap, overlap and translation mechanisms, not this full-sheet test.
No cross-notebook theorem or unread external lead is an input.

## Exact system and current reasoning

Let K be E=F_65537 or F=F_(65537^28). Indices P=(u,v) lie in F_137^2.
For t in T and y in F_137, the line L_(t,y) consists of u+tv=y. The
959 labels x_(t,y) are pairwise distinct actual elements of H minus C.
Write g_P(X)=a_P+b_P X+c_P X^2. Each L_(t,y) lies in the affine plane
a+x_(t,y)b+x_(t,y)^2 c=d_(t,y) in coefficient space. Repeated g_P are
allowed. Subtracting g_(0,0) fixes the common-message gauge; the required
rank is 3(137^2-1)=56304 over E.

The attempt exploits simultaneous incidences of the complete sheet.
No affine dependence of (a_P,b_P,c_P) on (u,v), embedding of F_137 in K,
plane-net representation, rank genericity or positivity over K is assumed.
Any claimed collapse must include coefficient-span dimensions zero through
three and the possibility of repeated assignments. No mathematical result
is established by this initial checkpoint.

## Completed attempt: eliminate three complete directions

The following is the saved working reduction of the unresolved system,
not a claimed full-rank certificate or a new canonical lemma. It uses
ordinary quadratic interpolation within the approved signed-equation
method. A later argument using this reduction must check its equivalence,
not take the reduced rank threshold as an established rank value.

Choose t_1=16, t_2=64, t_3=70. For P=(u,v), write
y_i(P)=u+t_i v in F_137 and a_i(P)=x_(t_i,y_i(P)) in E. These three
actual labels are distinct even when their auxiliary y coordinates agree.
Set

\[
 \ell_{i,P}(X)=
 \prod_{j\in\{1,2,3\}\setminus\{i\}}
 \frac{X-a_j(P)}{a_i(P)-a_j(P)}.
 \tag{W1}
\]

Introduce 411 scalar variables z_(i,y), one for each line in these
three directions. Any assignment satisfying their equality constraints
has the unique expression

\[
 g_P(X)=\sum_{i=1}^3 z_{i,y_i(P)}\ell_{i,P}(X).
 \tag{W2}
\]

Indeed, its three evaluations are the three common line values. Conversely,
(W2) has evaluation z_(i,y_i(P)) at a_i(P), so every choice of the 411
variables satisfies all three directions. The parameterization is
injective: each z_(i,y) occurs as an evaluation on every index of that
line. Thus these three directions alone leave dimension 411 before
fixing a common message. In the original 56307 coefficient variables,
their 3*137*136=55896 star equations are independent. This is elimination,
not a solution of the four other directions.

For t in {102,112,118,121}, y in F_137 and v in F_137 minus {0}, put
P=(y-tv,v), P_0=(y,0), and a=x_(t,y). Their residual equation is

\[
 \sum_{i=1}^3
 \ell_{i,P}(a)z_{i,y+(t_i-t)v}
 -\sum_{i=1}^3\ell_{i,P_0}(a)z_{i,y}=0.
 \tag{W3}
\]

All auxiliary subscripts are reduced in F_137; all fractions in (W1)
and (W3) are calculated in E, or its given extension F. No auxiliary
operation is transported through the labeling. Denominators and the
displayed numerator factors are nonzero by injectivity of the actual
labels. In each row the six variable positions are distinct, since
t_i-t and v are nonzero in F_137 and i selects a separate block.

Let R be the 74528-by-411 matrix of all (W3) rows. They compare every
nonanchor index with P_0 on every remaining line, so no equality or
higher overlap is omitted. Its kernel contains the three-dimensional
space z_(i,y)=h(x_(t_i,y)) for a common quadratic h. Those vectors are
linearly independent as h varies, by evaluation at three distinct labels.
Consequently rank R is at most 408; this upper bound is not the required
lower bound.

The gauge g_(0,0)=0 is exactly z_(1,0)=z_(2,0)=z_(3,0)=0, by quadratic
interpolation at those three labels. Delete those three columns from R
to obtain R_0, with 74528 rows and 408 columns. Every kernel vector of R
can be put in this gauge by subtracting a unique common h. Thus universal
collapse is equivalent to rank_E R_0=408 for every permitted C,sigma.
The full gauged signed system has rank

\[
 55896+\operatorname{rank}_E R_0;
 \qquad\hbox{required: }55896+408=56304.
 \tag{W4}
\]

This identity follows by first eliminating the three-direction equations
and then imposing precisely their residual equations. The coefficients
are in E. The same minors test ranks over F, so this reduction never
assumes that a given F-valued assignment descends to E. A nonzero kernel
vector over F exists if and only if one exists over E, but none has been
constructed here. Repeated assignments are allowed throughout.

## Where direct rigidity stopped

The easy one-dimensional possibility does not explain a nonconstant
kernel. In working form, subtract g_(0,0) and suppose all remaining
g_P lie in K h for one nonzero quadratic h. Write g_P=c_P h. Outside
the at most two line labels that are roots of h, each line forces all
its c_P to agree. At least five of the seven directions have no such
exceptional line. Two of these complete directions connect any P to Q
through the intersection of their respective lines. Hence c_P=c_Q;
the zero gauge forces all g_P=0. This observation is not a substitute
for treating coefficient-span dimensions two and three.

For dimension two, evaluations restrict the coefficient image to affine
lines, except possibly at a common root of the two spanning polynomials.
That alone does not provide an injective plane-net embedding: different
indices may have equal polynomial images, and selected incidences do not
forbid additional incidences. Dimension three leaves planes, not lines.
No proof of affine dependence on (u,v), of a faithful translation action,
or of the required plane-net hypotheses was obtained. Those would be
additional mathematical claims, not permissible assumptions.

The same obstruction has an exact dual description. If d_(t,y) is the
common evaluation on a line, associate the projective point

\[
 A_{t,y}=[1:x_{t,y}:x_{t,y}^2:d_{t,y}]
 \quad\hbox{on }Q:\ Z_0Z_2=Z_1^2\subset\mathbb P^3(E\text{ or }F).
 \tag{W5}
\]

For g_P(X)=a_P+b_P X+c_P X^2, its seven prescribed points lie in
the plane Z_3=a_P Z_0+b_P Z_1+c_P Z_2. Each such plane avoids the
cone vertex [0:0:0:1]. The 959 design points are distinct, with distinct
x coordinates, but the indexed planes may repeat and may contain other
design points. This is a point-plane configuration on a quadratic cone,
not the projective-plane net required by the inspected literature.
No assertion about its rigidity is established here.

## Source use and stopped shortcuts

The signed method is Alrabiah, Guruswami and Li,
*Randomly punctured Reed–Solomon codes achieve list-decoding capacity over
linear-sized fields*, [arXiv:2304.09445v3](https://arxiv.org/pdf/2304.09445v3),
Definition 2.5 and Lemma 2.7 with proof, printed pp. 7–8. Common-root
division is the factor-theorem step of Shangguan–Tamo,
*Combinatorial list-decoding of Reed–Solomon codes beyond the Johnson
radius*, [arXiv:1911.01502v1](https://arxiv.org/pdf/1911.01502v1),
Lemma 4.3's common-root proof case, printed pp. 11–12. Their local
specializations and tuple qualifications are already canonical in
L031/L047/L049; they are not reproved as new source theorems here.

For an original common center, row-wise differences of degree-63 messages
are divisible by the degree-61 core polynomial. Their degree-at-most-two
quotients satisfy the displayed line equations. This is only a necessary
reduction until collapse is proved. There is no scalar projection of
given tuples, field enlargement of the original instance, or assertion
that a full retained sheet exists.

Korchmaros–Nagy–Pace, *k-nets embedded in a projective plane over a field*,
[arXiv:1306.5779v1](https://arxiv.org/pdf/1306.5779v1), Section 2,
Proposition 3.1, Proposition 4.1 and Theorems 4.2–4.4/5.2, were assessed
before invocation. They cannot simply be applied to (W5). This turn did
not browse again or use an unread theorem. Full and supporting Mathlib
coverage for the proposed rigidity remains not checked.

## Outcome and precise continuation obstruction

EXPLORATION: the exact residual system is saved, but its universal rank
lower bound remains unproved. Achieved universal full-rank certificate:
none. Required reduced rank: 408; required original gauged rank: 56304.
No permitted nonconstant assignment, numerical rank sample, mathematical
script, new lemma, cap or improvement of the 955–957 bracket was produced.

The unresolved claim is the all-label 408-column rank bound in (W3)–(W4),
including repetitions and coefficient spans two and three. A generic or
single-label rank cannot resolve it. The direct attempt is parked pending
a materially new input. The proposed source comparison concerns (W5),
including whether known cone/circle-net rigidity addresses these weak
incidences. Its assessment is REVIEW_REQUIRED; no new mathematics on
that lead has been approved or attempted. Retention at 1532496,
compatible laws, global RS transfer and the pinned source qualification
remain independent gaps.
