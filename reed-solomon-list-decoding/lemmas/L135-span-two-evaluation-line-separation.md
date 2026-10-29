# L135 — Complete direction classes in the span-two coefficient plane

## Hypotheses

Use the pinned L030 instance: q=137,
T={16,64,70,102,112,118,121} in F_137, E=F_65537,
F=F_(65537^28), H=<19139> of order 1024, and k=64. Let C be any
61-subset of H and let sigma be any bijection from
(T times F_137) disjoint union four dummy points to H minus C.
Write x_(t,y)=sigma(t,y). In particular, all 959 x_(t,y) are distinct.
There is no asserted embedding of F_137 into E or F.

Let K be E or F. For every P=(u,v) in F_137^2 let g_P in K[X]
have degree at most two, allowing zero and repeated polynomials. Assume
g_P(x_(t,y)) is constant as P ranges over the auxiliary line

\[
 A_{t,y}=\{(u,v):u+tv=y\}.
\]

Let g_0=g_(0,0) and suppose
V=span_K{g_P-g_0:P in F_137^2} has dimension exactly two.
Put W=g_0+V, viewed as an affine coefficient plane. For every (t,y),
let d_(t,y) be the common value on A_(t,y), and define its restricted
evaluation level set

\[
 \ell_{t,y}=\{g\in W:g(x_{t,y})=d_{t,y}\}.
\]

## Conclusion

At most one of these level sets is not a genuine affine line. If one
is exceptional, it is all of W; omit its entire direction class, leaving
six complete classes. All the genuine lines are pairwise distinct in
this case. If there is no exceptional set, all 959 lines are pairwise
distinct, leaving all seven complete classes.

Consequently any three of the retained complete classes have injective
maps y -> ell_(t,y)^* into the projective dual of the projective completion
of W, and their images are pairwise disjoint. The three dual points
selected by any auxiliary P are distinct and collinear, since their
primal lines contain g_P. Repeated g_P and additional incidences have
not been excluded. No group-labeled classification is invoked.

This is an all-label bridge for the coefficient-span-two case, not a
proof that the case cannot occur. Coefficient span three, full-sheet
collapse, partial-sheet retention, the cap 1532495 and RS-list transfer
remain unresolved. The separate critical audit on 2026-10-27 accepts this
bridge with its stated hypotheses and qualifications; it proves no collapse.

## Proof

**Scope and sources.** The pre-invocation EXPLORE assessment is
[the span-two bridge assessment](../drafts/literature/2026-10-27-span-two-light-multinet-bridge.md).
L030 supplies the ambient sheet. The local signed/common-root methods in
L031/L047/L049 motivate the hypotheses; none of their fixed-label rank
conclusions is used here. The standard polynomial root bound over a
field is the only polynomial theorem needed below.

Korchmaros and Nagy, *Group-labeled light dual multinets in the projective
plane (with Appendix)*, [arXiv:1710.00172v1](https://arxiv.org/pdf/1710.00172v1),
30 September 2017, Introduction and Definition 2.1, pp. 1–4, require
injective component maps (with disjoint components in the introduction).
The inspected source does not supply these properties for the present
evaluation lines. The proof below addresses precisely that missing
degeneracy and separation step. It does not reprove or apply their
Proposition 4.5 or any net classification. In particular, no auxiliary
isotopy, faithful action or ordinary-net hypothesis is presumed.

**Restricted normals and the exceptional case.** Choose a basis h_1,h_2
of V and write

\[
 g_P=g_0+z_{P,1}h_1+z_{P,2}h_2.
\]

The z_P affinely span K^2: z_(0,0)=0 and their linear span is K^2.
In these coordinates ell_(t,y) is

\[
 h_1(x_{t,y})z_1+h_2(x_{t,y})z_2
       =d_{t,y}-g_0(x_{t,y}).                 \tag{1}
\]

If its normal is zero, the right side is zero too, since at least one
g_P belongs to the level set. Thus it is the whole plane. Suppose such
a label x_0 exists. Every element of V is divisible by X-x_0. The
two-dimensional space of degree-at-most-two multiples of X-x_0 equals V,
so we may use the basis X-x_0, X(X-x_0). At any x!=x_0 the projective
normal is [1:x], and these normals are distinct for distinct x. All such
evaluations are nonzero; hence there is just one exceptional index,
and no two other lines coincide. Omitting its one direction leaves six
complete classes. This proves all claims in the exceptional case.

For the rest of the proof assume no evaluation normal is zero; all
seven classes are available. For any projective normal [r:s], the
polynomial s h_1-r h_2 is nonzero by linear independence and has degree
at most two. Every label whose evaluation normal is [r:s] is a root
of that polynomial. The labels are distinct, so each projective normal,
and consequently each affine line, has at most two indexed occurrences.
This conclusion does not assume that different messages are distinct.

**No coincidence within a direction class.** Suppose two indices
(a,y_1),(a,y_2), with y_1!=y_2, define the same affine line ell.
Every indexed line of any other direction is different from ell,
because ell already has its maximum two occurrences.

Parametrize the two auxiliary lines by
P_i(w)=(y_i-aw,w), w in F_137. For r in T minus {a}, projecting P_1(w)
along its auxiliary r-line to A_(a,y_2) gives P_2(w+delta_r), where

\[
 \delta_r=(y_1-y_2)/(r-a)\quad\text{in }\mathbb F_{137}.
\]

Both polynomial images belong to ell and to the same other affine
evaluation line. Two distinct affine lines with a common point have
just one common point, so

\[
 g_{P_1(w)}=g_{P_2(w+\delta_r)}.              \tag{2}
\]

For distinct r,s in T minus {a}, (2) implies invariance of
w -> g_(P_1(w)) under translation by delta_r-delta_s. This translation
is nonzero: y_1-y_2, r-a, s-a and r-s are nonzero. Every nonzero
translation on the additive group of the prime field F_137 is a single
137-cycle. Thus all values on A_(a,y_1) equal one polynomial R.

For any auxiliary point Q, choose three distinct directions other than
a. Its line in each chosen direction meets A_(a,y_1), at a point with
value R. At the three distinct actual labels of those lines, g_Q-R
vanishes. Its degree is at most two, so g_Q=R. This makes V zero,
contradicting its dimension. Coincidences within a class are impossible.

**The finite projection identity for different directions.** For each
unordered pair a,b in T, order it as a<b using the displayed integer
representatives. List T minus {a,b} increasingly as r_0,...,r_4, and put

\[
 \kappa_r=\frac{r-a}{r-b},\qquad
 \gamma_j=\kappa_{r_j}/\kappa_{r_0}\quad(1\le j\le4)
                  \quad\text{in }\mathbb F_{137}^{\times}.             \tag{3}
\]

The following complete table gives gamma and a nonnegative exponent
vector e such that product_(j=1)^4 gamma_j^(e_j)=2 modulo 137.
It is an explicit certificate for all 21 pairs, with no omitted labels
or sampling.

| (a,b) | (gamma_1,gamma_2,gamma_3,gamma_4) | (e_1,e_2,e_3,e_4) |
| --- | --- | --- |
| (16,64) | (102,122,100,134) | (0,1,0,2) |
| (16,70) | (20,78,19,35) | (2,0,2,0) |
| (16,102) | (118,102,87,47) | (0,2,2,0) |
| (16,112) | (60,36,120,34) | (0,1,2,1) |
| (16,118) | (119,51,18,12) | (3,0,0,2) |
| (16,121) | (103,91,104,126) | (5,0,2,0) |
| (64,70) | (118,60,119,103) | (3,1,0,1) |
| (64,102) | (20,36,51,91) | (3,3,0,1) |
| (64,112) | (78,102,18,104) | (1,0,0,2) |
| (64,118) | (19,87,120,126) | (0,1,0,1) |
| (64,121) | (35,47,34,12) | (2,0,1,0) |
| (70,102) | (102,28,20,90) | (0,1,1,3) |
| (70,112) | (122,110,136,5) | (0,1,0,1) |
| (70,118) | (100,118,2,93) | (0,0,1,0) |
| (70,121) | (134,48,133,45) | (1,0,0,1) |
| (102,112) | (20,45,89,99) | (4,1,1,1) |
| (102,118) | (95,90,49,33) | (1,2,0,1) |
| (102,121) | (4,36,39,105) | (1,0,1,2) |
| (112,118) | (39,2,21,46) | (0,1,0,0) |
| (112,121) | (55,83,120,92) | (1,0,2,1) |
| (118,121) | (26,110,84,135) | (0,0,2,2) |

In F_137, 2^68=1, 2^34=136=-1 and 2^4=16!=1. Every proper divisor of
68 divides 34 or 4, so 2 has order exactly 68. It follows from the table
that the subgroup generated by the ratios (3) contains a subgroup of
order 68 and has at most two orbits on F_137^times under multiplication.
The point 0 is a separate orbit and will be retained below.

Reproduce the certificate with
`python3 scripts/finite-support/span_two_direction_orbits.py`.
The full output is `scripts/finite-support/span-two-direction-orbits.json`.
The program computes (3), constructs the generated subgroups by closure,
checks all products and inverses, lists their cosets, and supplies every
table identity above. All 21 required cases pass: minimum subgroup size
68 (required 68), maximum orbit count 2 (required 2). The complete
`required_witnesses` field was inspected, including all generators and
exponents; the complete size table was inspected as well. The printed
table is the load-bearing finite certificate, so no uninspected sampled
rank or large numerical summary is a premise of the proof.

**No coincidence across direction classes.** Suppose A_(a,y_a) and
A_(b,y_b), a!=b, have the same geometric line ell. Translate auxiliary
coordinates so their intersection O is (0,0). This changes their
intercepts, not directions or the injectivity of actual labels. Explicitly,
if the old O is (u_O,v_O), reindex g by P_old=P_new+O and reindex the
labels by x'_(t,y)=x_(t,y+u_O+t v_O). No field operation is transported
through sigma. In the
translated coordinates the two lines can be parametrized as

\[
 P_a(w)=(-aw,w),\qquad P_b(z)=(-bz,z).
\]

Write A(w)=g_(P_a(w)) and B(z)=g_(P_b(z)); these are polynomial-valued
functions, not polynomials in the auxiliary variable. Every other
indexed evaluation line is different from ell, by the two-occurrence
bound. Projection from P_a(w) along a direction r outside {a,b} reaches
P_b(kappa_r w). The two coefficient images lie on ell and on that other
geometric line, hence

\[
 A(w)=B(\kappa_r w).                         \tag{4}
\]

Using r and r_0 in (4) gives A(w)=A((kappa_r/kappa_(r_0))w).
Thus A is invariant under the generated multiplicative subgroup.
By the finite identity it takes at most two polynomial values R_1,R_2
on w!=0. (They may coincide.) Equation (4) shows that B on z!=0 takes
values in the same set. All these coefficient points belong to ell.
The value A(0)=B(0)=g_O need not equal either R_i.

Now let Q be any auxiliary point off the two auxiliary lines. For each
t in T consider its auxiliary t-line M_t. If t!=a, mark M_t's
intersection with A_(a,0); for t=a, mark its intersection with A_(b,0).
These intersections always exist. A marked point is O only when M_t
passes through O. Since Q!=O, at most one of the seven distinct lines
through Q does so. Therefore at least six of the marked points have
nonzero coordinates on the two auxiliary lines. Their polynomial
values belong to {R_1,R_2}. At least three of them have the same
polynomial value R_i. At the three distinct actual labels attached to
those M_t, g_Q-R_i vanishes. The quadratic root bound gives g_Q=R_i.

It follows that the images of all Q off the two lines belong to ell;
the images on the two lines already belong to ell by their definition.
All g_P would lie on a single affine line in W, contradicting that their
affine span is W of dimension two. This excludes cross-class collisions.

**Dualization and qualifications.** The exceptional case left six
complete classes, and the other case leaves seven. Distinct affine
lines have distinct projective closures and hence distinct dual points.
For any chosen three directions and auxiliary P, the three lines meet
at the finite coefficient point g_P; projective duality makes their
three distinct dual points collinear. Parallel lines within a class are
allowed. Parallel distinct lines across classes cannot occur because
their auxiliary lines intersect and supply a common coefficient point.
No further exclusion of extra incidences or repeated g_P is used.

The stronger arithmetic probe allowing an arbitrary omitted direction
is false: omitting 102 for {a,b}={64,70} gives subgroup size 34, and
omitting 16 for {70,118} gives size 17. These two failures, their full
subgroups and cosets remain in the certificate's `arbitrary_omission_probe`
and `cases` fields. They are not permissible omissions in the nonexceptional
proof. When an exceptional root really occurs, the separate [1:x] normal
argument handles it without this orbit test. Neither arithmetic failure
is a compatible quadratic assignment or an RS counterexample.

All field operations in (2)–(4) are auxiliary F_137 operations; geometric
lines and polynomial roots are over K. No equality mixes these fields.
No use is made of the unaudited working rank identities (W1)–(W5), any
field embedding, generic labels, sampled rank, or a distinct-message
assumption. The actual subgroup H is only used to supply the pinned
distinct labels. A later use of a group-labeled classification would
still have to verify its isotopy and every additional hypothesis.

**Separate critical audit, 2026-10-27.** The audit accepts the proof above
under the pre-invocation
[audit coverage](../drafts/literature/2026-10-27-l135-critical-audit-coverage.md).
It imports no classification and strengthens no hypothesis. L030 is used
only for its ambient labeling construction; its probabilistic moments and
the determinant table are not inputs to this proof. L031/L047/L049 remain
context, not inputs. The following checks make explicit the points where
degeneracy, a changed affine origin or the two different fields could
otherwise invalidate the argument.

The affine hull of the z_P is their linear span because it contains zero.
Thus it really is K^2, not just a set whose linear span is K^2 after an
unjustified translation. A zero normal has a nonempty level set, so its
right side is zero. The factor theorem embeds V into
(X-x_0)K[X]_{<=1}, which has dimension two; equality follows. At every
other actual label the normal is a nonzero multiple of (1,x). This deals
with the entire exceptional case independently of every orbit bound.
In the nonexceptional case s h_1-r h_2 is nonzero for every [r:s], even
when r or s vanishes, and has at most two distinct roots. Hence any
assumed coincident line exhausts its two indexed occurrences.

For the within-class collision, set A(w)=g_(P_1(w)), B(w)=g_(P_2(w)).
Equation (2) gives A(w)=B(w+delta_r) and
A(w+delta_r-delta_s)=B(w+delta_r), so the asserted translation invariance
has the correct sign. The nonzero translation generates the entire
additive group of F_137. The subsequent three roots are at distinct
actual labels because the three auxiliary directions are distinct;
they need not be distinct coefficient images. The root bound makes
every g_Q equal to R, contradicting dim V=2.

For the cross-class collision, translation by O changes the reference
polynomial to g_O but preserves V: each g_P-g_O is in V, and
g_P-g_0=(g_P-g_O)-(g_0-g_O) belongs to the span of the new differences.
Thus W=g_O+V is the same affine plane. The reindexing of y is a
permutation separately for each t, preserving all 959 distinct labels.
The r-line equation is (r-b)z=(r-a)w, verifying (4) and its ratios.
Invariance under each nonzero generator implies invariance under its
inverse by substitution, hence under its full generated subgroup.
The functions A,B take values in K[X]; no polynomial dependence on w
or z over F_137 is asserted. Their nonzero-parameter value sets agree
using r_0. The origin's value remains unrestricted.

For Q off the two auxiliary lines, its seven distinct lines M_t can
include the line QO at most once. Each marked point is O exactly when
its M_t contains O. The rule marking the b-line for t=a and the a-line
otherwise always gives an intersection. Therefore at least six marks
are nonzero-parameter points. Even if two marked points coincide, they
belong to distinct M_t indices and give distinct actual labels. With
at most two polynomial values, three such indices share a value R_i.
The degree-two root bound applies over K to g_Q-R_i at those labels.
All coefficient images then lie in ell, contradicting their affine
span. Dualization uses distinct projective line closures through the
finite point g_P and requires no exclusion of repeated messages.

Independent exact reproduction is
`python3 scripts/finite-support/critical_audit_l135.py`; its full output
is `scripts/finite-support/l135-critical-audit.json`. It solves each
modular quotient exhaustively and constructs every subgroup and coset
using discrete logarithms and gcds in a fully enumerated cyclic group,
independently of the producer's breadth-first closure. It checks all
21 printed pairs, all four ratios and exponents in every row, every
product equal to 2, and the exact order 68 of 2. It also compares every
field of all 126 saved cases, every size-table entry and both summaries.
All pass: required minimum subgroup size 68 (at least 68 needed),
maximum orbit count two (at most two needed). The complete required
checks and both failed probes' subgroups/cosets were inspected. The
failures remain size 34/four orbits for (64,70)/102 and size 17/eight
orbits for (70,118)/16, and are not used as permissible omissions.

The first audit-program run failed to parse the symbolic table header
and produced no certificate. The repaired numeric-row parser passed;
no mathematical input or threshold changed. The
[audit record](../drafts/audits/2026-10-27-l135-critical-audit.md) preserves
that implementation failure. This audit verifies a local input already
proposed here, not a new classification or progress beyond the checked
literature. Mathlib coverage is unchanged.

## Mathlib

Full matching coverage and supporting theorem names have not been
checked. The proof uses polynomial root bounds, elementary affine-plane
incidence, the additive cyclicity of F_137 and the complete modular
certificate above. No claim of absence from Mathlib or of global
originality follows from the reused bounded source search.
