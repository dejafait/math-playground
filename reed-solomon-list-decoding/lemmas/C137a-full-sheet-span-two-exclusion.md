# C137a — Exclusion of coefficient span two on the full pinned sheet

## Hypotheses

Use q=137 and T={16,64,70,102,112,118,121} in the auxiliary field
F_137. Let E=F_65537, F=F_(65537^28), H=<19139> of order 1024,
and k=64. Let C be any 61-subset of H and sigma any bijection from
(T times F_137) disjoint union four dummy points onto H minus C.
Write x_(t,y)=sigma(t,y); these 959 actual labels are distinct.
Let K be E or F. No embedding of F_137 into K is assumed.

For each P=(u,v) in F_137^2, let g_P in K[X] have degree at most two,
allowing zero and repeated polynomials. For every (t,y), assume there
is a value d_(t,y) in K such that

\[
 g_P(x_{t,y})=d_{t,y}\qquad
 \text{for every }P\in A_{t,y}:=\{(u,v):u+tv=y\}.
\]

Set g_0=g_(0,0) and V=span_K{g_P-g_0:P in F_137^2}.
These are constancies on the entire auxiliary sheet, not only on a
retained subset of its points.

## Conclusion

The coefficient-difference span cannot have dimension exactly two:
dim_K V != 2.

This is a local consequence of L135 and L137 and the standard
projective-duality input below. The separate critical audit on
2026-10-29 accepts this implication under its unchanged hypotheses
and inherited source qualifications. It does not exclude dimension three, prove
full-sheet constancy in every case, bound a partially retained family,
or supply a transfer from arbitrary RS lists to these hypotheses.
The finite bracket 955–957 and arbitrary-center 67/68 safety are unchanged.

## Proof

**Assessed scope and imported geometry.** The pre-invocation SPECIALIZE
[assessment](../drafts/literature/2026-10-28-span-two-collinearity-consequence.md)
covers exactly this consequence, including repeated messages, the
exceptional evaluation direction and a primal point at infinity.
Use A. I. Kostrikin and Yu. I. Manin, *Linear Algebra and Geometry*,
translated by M. E. Alferieff, Gordon and Breach, 1997 paperback edition,
Chapter 3, Theorem 6.5 and Sections 6.8–6.12, printed pp. 226–228,
and Sections 7.1–7.2, p. 229
([primary PDF](https://www.math.mcgill.ca/darmon/courses/19-20/algebra2/manin.pdf)).
The imported facts are incidence-reversing finite-dimensional projective
duality over an arbitrary field, uniqueness of the projective line
through two distinct points and of the intersection of two distinct
projective-plane lines, and the affine chart with its line at infinity.
Proposition 6.11 and Section 6.12 identify the infinity points of affine
lines. There is no characteristic-zero or algebraic-closure requirement
for these facts. The coordinates below identify their application to
the actual evaluation lines; no classification or duality theorem is
reproved here.

**Evaluation lines and the rational pencil point.** Suppose for
contradiction that dim_K V=2. Choose a K-basis h_1,h_2 of V and put
W=g_0+V. Write uniquely

\[
 g_P=g_0+z_{P,1}h_1+z_{P,2}h_2,\qquad z_{P,i}\in K.
\]

Identify the projective completion of W with P^2(K), taking g_P to
Z_P=[z_(P,1):z_(P,2):1]. Thus every Z_P is finite, and Z_0=[0:0:1].
The infinity line is Z_3=0.

For each label, let ell_(t,y) be the level set in W of evaluation at
x_(t,y) with value d_(t,y). Apply L135 with the assumed dimension two.
If no level set is exceptional, retain I=T. Otherwise omit the entire
direction containing its unique exceptional level set; then |I|=6.
In both cases all ell_(t,y) with t in I and y in F_137 are genuine
affine lines, pairwise distinct across all these indices. In particular
there are at least two retained directions, and each is complete.

The closure of each retained line has equation

\[
 h_1(x_{t,y})Z_1+h_2(x_{t,y})Z_2+
       (g_0(x_{t,y})-d_{t,y})Z_3=0.                 \tag{1}
\]

Its first two coefficients are not both zero, since the line is genuine.
The corresponding dual point is

\[
 p_{t,y}=[h_1(x_{t,y}):h_2(x_{t,y}):g_0(x_{t,y})-d_{t,y}].
\]

All hypotheses of L137 are the same ones now in force, including the
prescribed omission rule. Its conclusion gives one line in the dual
projective plane, defined over K, containing all p_(t,y). Write that
line as q_1 U_1+q_2 U_2+q_3 U_3=0, with (q_1,q_2,q_3) in K^3
nonzero. By the imported duality its primal pencil point is
Q=[q_1:q_2:q_3] in P^2(K). Substituting each p_(t,y) in this equation
and comparing (1) explicitly verifies that Q belongs to the projective
closure of every retained evaluation line. This also checks rationality
over the specified K, without descending a point from an extension.

Fix distinct a,b in I. For every P=(u,v), put y_a=u+av and y_b=u+bv
in F_137. Both corresponding evaluation lines are retained because
the two direction classes are complete. The full-sheet constancies
give

\[
 g_P\in\ell_{a,y_a}\cap\ell_{b,y_b}.              \tag{2}
\]

Their indices have different directions, so L135 makes them distinct.
Their projective closures remain distinct: their intersections with
the affine chart recover the original affine lines. Both closures
contain Q as well as the finite point Z_P from (2).

**Infinite-point branch.** If q_3=0, Q is at infinity and differs from
Z_P, whose third coordinate is one. The two distinct projective lines
would then contain two distinct points Q and Z_P. Uniqueness of the
line through those points contradicts their distinctness. It is enough
to use P=(0,0) for this branch. In particular, no assumption that the
pencil point is finite has been made.

**Finite-point branch.** If q_3!=0, Q represents the coefficient point

\[
 R=g_0+(q_1/q_3)h_1+(q_2/q_3)h_2\in W.
\]

For every P, the two distinct closures above have the unique
intersection Q. Since Z_P is also in their intersection, Z_P=Q,
so g_P=R. This applies to P=(0,0) too, giving R=g_0. Consequently
every difference g_P-g_0 is zero and V={0}, in contradiction to
dim_K V=2. The two cases exhaust all projective points Q, and prove
the conclusion.

**Qualifications.** The argument uses just two of the six or seven
complete retained directions after L135 and L137 have been applied.
It does not replace their full-sheet hypotheses by two-direction
hypotheses. The exceptional direction is not reconstructed, and the
failed arbitrary-omission tests in L135 are not used. Auxiliary
arithmetic only chooses y_a,y_b; all geometric arithmetic is over K.
No injectivity of P -> g_P is assumed: the finite branch proves equality
of the messages as a consequence, and contradicts the assumed span.
The existing L137 theorem imports, including its qualification that the
source's cuspidal calculation was not independently reproduced, are
unchanged. No use is made of the blocked design-matrix transfer or of
the unfinished span-three/two-fiber constructions. This is a recorded
local specialization, not a claim of progress beyond the checked
geometric literature or a candidate solution of the main problem.

**Separate critical audit, 2026-10-29.** The unchanged pre-invocation
SPECIALIZE
[audit assessment](../drafts/literature/2026-10-28-c137a-critical-audit-coverage.md)
covers exactly this implication. The audit accepts it; no additional
hypothesis, changed conclusion or new geometric theorem is needed.
L135 and L137 have precisely the same C, sigma, actual labels, fields,
quadratic family, reference polynomial and full-sheet constancies as
here. The assumption dim_K V=2 is made only inside the contradiction
argument, so their conditional conclusions are legitimately applicable.
No nonvacuity or construction of such an assignment is used.

The coordinates are over K throughout. Each retained normal is nonzero,
so (1) defines a genuine projective line whose affine part is exactly
the specified level set. Its dual representative agrees with L137,
including the sign g_0(x)-d. The nonzero K-form for the common dual
line gives Q over K directly; substituting the representative gives
the same equation (1), with no extension-field descent or polarity
assumption. Distinct affine lines have distinct closures because the
affine parts of equal closures would agree.

In the exceptional case the entire prescribed class is omitted and
six complete classes remain. In the nonexceptional case all seven are
kept; the two failed arbitrary-omission probes from L135 are irrelevant.
Fixing a,b in I is permitted only after those full hypotheses have
been used. For every P, both indices (a,u+av),(b,u+bv) are retained;
the full-sheet equations supply (2), and L135 gives distinctness
even if the two intercepts happen to agree. For P=0 the indices are
(a,0),(b,0), their values equal g_0 at their labels, and their closures
both contain Z_0=[0:0:1]. Thus an infinite Q and Z_0 would be two
distinct common points of distinct lines. This rejects the entire
infinite branch without presuming a finite pencil.

For a finite Q, each pair in (2) consists of distinct projective lines
with Q and Z_P in their intersection. Unique intersection implies
Z_P=Q for every P, not merely for distinct message values. The
normalized representatives have third coordinate one, so equality
of projective points gives equality of their two coefficient coordinates.
At P=0 those coordinates vanish, and hence every g_P equals g_0.
It follows that V is the zero subspace, which contradicts dimension
two over either permitted field. Repetitions are allowed throughout.

This audit verifies the local application of the cited arbitrary-field
duality and incidence facts and the audited L135/L137 interfaces. It
does not independently reprove L137's imported classification or its
source's omitted cuspidal computation. Its direct local inputs remain
L135 and L137, with L030's setup inherited. No extra DAG edge, numerical
certificate, translation action on messages or retention assumption is
used. The concise
[audit record](../drafts/audits/2026-10-29-c137a-critical-audit.md)
records the bounded decision and remaining limitations.

## Mathlib

Full matching coverage for this pinned full-sheet exclusion has not
been checked. Supporting formal statements for arbitrary-field
projective duality, affine completion and unique projective incidence
have not been looked up in Mathlib during this step; no absence claim
or exact declaration name is asserted. The proof is informal and uses
the precise textbook citation above and the audited local inputs.
