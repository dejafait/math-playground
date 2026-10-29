# L126 — Full-star-preserving thinning cannot retain the threshold on both cores

## Hypotheses

Let H be a set of size 1024, let K be a 60-subset, and choose distinct
a,b outside K. Set C=K union {a}, C'=K union {b}, and
Y=H minus (K union {a,b}). Use L030's exact construction over the
prime field F_137:

\[
T=\{16,64,70,102,112,118,121\},\qquad
\Omega=(T\times\mathbb F_{137})\sqcup D_0,\quad |D_0|=4.
\]

Write V for the polynomials of degree at most two, including zero,
and B_p={(x,p(x)):x in T}. Choose arbitrary bijections
sigma:Omega -> H minus C and sigma':Omega -> H minus C'. Require
sigma^{-1}(b)=(16,y_0) for some y_0 in F_137. Define the two full
families of 68-supports by

\[
F_L=\{C\cup\sigma(B_p):p\in V\},\qquad
F_R=\{C'\cup\sigma'(B_r):r\in V\}.
\]

Let A_L subset F_L and A_R subset F_R be arbitrary retained
subfamilies. Retain all members of F_L containing b and all members
of F_R containing a, and assume these complete common stars are equal
as families of actual supports. Require any two distinct supports in
A_L union A_R to intersect in at most 63 points; equal supports are
identified, not forbidden. No probability law or independence is assumed.

## Conclusion

The retained sizes satisfy

\[
|A_L|+|A_R|\le137^3+137^2=2590122,
\qquad \min(|A_L|,|A_R|)\le1295061.
\]

In particular they cannot both have at least 1532496 members. The
balanced upper bound is 237435 below that threshold. This is only an
obstruction for the specified two polynomial families with both complete
common stars preserved and left distinguished column 16. The bound is
not asserted sharp or attainable. It does not bound arbitrary thinnings
with incomplete stars, arbitrary local families or RS lists, and it
does not change the bracket 955–957 or decide 67/68 agreement safety.
The separate critical audit below accepts this restricted proof.

## Proof

**Assessed scope and imported input.** The pre-invocation
[SPECIALIZE assessment](../drafts/literature/2026-10-25-two-core-full-star-thinning.md)
approves exactly this deterministic correspondence and counting test.
L030 supplies the family, its size and its separate local feasibility.
L125's separately audited common-star rigidity, including its complete
840-map certificate, is used as established local mathematics. Only the
star-rigidity part and formula (8) are needed; no full-law sampling or
Hall-event probability is used. The new step is to verify the formula
on all nonstar indices as a bijection, then count its disjoint conflicts.

The assessment also records König, *Graphok és matrixok* (1931),
authorized translation *Graphs and matrices*, arXiv:2009.03780v1,
[unnumbered main theorem, PDF p. 3](https://arxiv.org/pdf/2009.03780v1).
Its maximum-matching/minimum-cover equality is not needed: the explicit
matching below gives the required count directly. Thus no general
matching theorem, symmetry bound or classification theorem is reproved.

**Why the audited rigidity applies after thinning.** Each full family
has 137^3 distinct blocks: two degree-at-most-two polynomials agreeing
at all seven distinct evaluation arguments are equal. The left star
contains exactly q^2=18769 members, with q=137, indexed by p(16)=y_0.
Evaluation at 16 is a surjective linear map V -> F_q, so each fiber has
q^2 elements. This common star is nonempty. Consequently the right
distinguished point sigma'^{-1}(a) lies in its active seven-column part,
say at (t_1,y_1); a point of D_0 belongs to no B_r.

The assumed equality of both full stars is exactly L125's equation (1)
after removing K,a,b. Its proof of column recovery and arbitrary-symbol
rigidity uses only this equality and the full polynomial stars, not the
survival of any nonstar block. It therefore applies to these ambient
families despite deletion elsewhere. The audited finite test forces
t_1=16 and identity column permutation. There are lambda in F_q^* and
u_0,v_0 in F_q such that the actual-label correspondence satisfies,
for every s in T minus {16} and every z in F_q,

\[
\sigma(s,z)=\sigma'\bigl(s,
\lambda z+(s-16)(u_0s+v_0)+y_1-\lambda y_0\bigr).       \tag{1}
\]

This is L125's equation (7) with both symbol normalizations undone.
All these labels lie in Y. The distinguished-column values of sigma
and sigma' away from b and a remain arbitrary; (1) does not constrain
them and the argument below does not require such a constraint.

**A bijection on the nonstar indices.** Put

\[
V_L^*=\{p\in V:p(16)\ne y_0\},\qquad
V_R^*=\{r\in V:r(16)\ne y_1\}.
\]

For every p in V define exactly the polynomial in L125's formula (8):

\[
\Phi(p)(X)=\lambda p(X)+(X-16)(u_0X+v_0)+y_1-\lambda y_0.\tag{2}
\]

It lies in V because each term has degree at most two. If
Phi(p)=Phi(p'), subtraction and lambda!=0 give p=p', proving
injectivity. For any r in V the explicit inverse is

\[
p(X)=\lambda^{-1}
\bigl(r(X)-(X-16)(u_0X+v_0)-y_1+\lambda y_0\bigr),       \tag{3}
\]

which also lies in V and substitutes into (2) to give r. Thus Phi is
surjective on V. At the distinguished argument,

\[
\Phi(p)(16)-y_1=\lambda(p(16)-y_0).
\]

It follows in both directions that p belongs to V_L^* if and only if
Phi(p) belongs to V_R^*. Formula (3) therefore also proves surjectivity
of the restriction, not just an injection into the right nonstar set.
Each nonstar set has exactly

\[
N=q^3-q^2=2552584
\]

elements. No polynomial is normalized up to scalars or omitted.

**Every paired support is distinct and forbidden.** For p in V_L^*
let S_p=C union sigma(B_p) and R_p=C' union sigma'(B_{Phi(p)}).
For every one of the six arguments s!=16, (1) and (2) identify the
actual labels sigma(s,p(s)) and sigma'(s,Phi(p)(s)). They are six
distinct points of Y, by bijectivity of sigma and the distinct columns.
Both supports also contain K. Hence |S_p intersect R_p|>=60+6=66.

S_p contains a but not b, since sigma^{-1}(b)=(16,y_0) and
p(16)!=y_0. Conversely R_p contains b but not a, by the distinguished
value identity. Thus S_p and R_p are distinct actual supports, and
their intersection is forbidden by the assumed upper bound 63. Any
additional intersection of their seventh residual points only strengthens
this conclusion. There is no exception for equal supports in this pairing.

**Disjoint-edge counting.** Tag supports by their side when counting
|A_L|+|A_R|. Injectivity of the polynomial-to-support maps, and the
bijection Phi:V_L^* -> V_R^*, show that the N forbidden pairs above
are vertex-disjoint and cover every nonstar vertex on each side.
At most one member of each pair can survive, so the total retained
nonstar count on the two sides is at most N. This elementary sum of
N inequalities is sufficient; no matching optimality theorem is used.

Every star member survives on each side, contributing 2q^2 to the
sum of the two family sizes. Although each common support is the
same actual support on both sides, it occurs once in each family
size and must be counted twice in that sum. No nonstar support can
be common to both sides, because of the a/b distinction just proved.
Consequently

\[
|A_L|+|A_R|\le 2q^2+N=q^3+q^2=2590122.
\]

At least one size is at most half this even integer, namely 1295061.
But twice the proposed threshold is 3064992, exceeding the sum bound
by 474870. This rules out both sizes reaching 1532496. Additional
conflict edges could strengthen this upper bound; their absence is
neither assumed nor proved. No realization or sharpness follows.

**Arithmetic check and limits.** The complete exact-integer certificate
is `scripts/finite-support/full-star-thinning-count.json`; it records
q, family and star sizes, matching size, actual and required bounds,
both shortfalls and all arithmetic checks. All checks pass. This
arithmetic is a check of the displayed integer comparisons, not a
substitute for the symbolic bijection and intersection proof. The
independent gaps listed in the conclusion remain open.

**Separate critical audit, 2026-10-25.** The pre-existing
[SPECIALIZE audit assessment](../drafts/literature/2026-10-25-l126-critical-audit-coverage.md)
approves this verification. No new external theorem is needed. The
audit accepts L126 under exactly its stated hypotheses, without
strengthening its conclusion or asserting sharpness.

The applicability check starts with the ambient full stars, not with
a probability law. Equality of these stars, after removing K,a,b,
is exactly L125 (1). Their used labels are the other six full columns:
every such label occurs by interpolation, whereas every other label
is unused. Within these used labels noncooccurrence identifies columns.
This recovers the arbitrary column and symbol bijections even after
all nonstar members have been deleted. The normalized six-column
family contains every affine evaluation vector. Consequently L125's
three-coordinate functional equation applies for every pair of field
values. Subtracting constants gives additivity on the entire prime
field, hence nonzero scalar symbol slopes; two coordinates give the
invertible affine coefficient map. None of these steps invokes full-law
sampling, survival of a nonstar block, or a cross-support inequality.

The induced projective map sends the right six-set to the left six-set,
with nonzero denominator on the right. These are precisely the 840
cases of the accepted L125 test. Its identity survivor forces the same
distinguished column and scalar linear part. Undoing normalization
multiplies by s-16 and restores y_1 on the right, giving exactly (1),
including the sign of the constant y_1-lambda*y_0. The unconstrained
distinguished-column labels and dummy points never enter that equation.

The polynomial maps (2) and (3) compose to the identity in both orders
on the full three-dimensional polynomial space. Both have degree at
most two, and evaluation at 16 gives the displayed nonzero-scalar
identity. Thus their restrictions are inverse bijections on the two
nonstar fibers' complements, covering every nonstar vertex, including
constant and zero polynomials whenever those are nonstar. There is no
quotient by scalars. Distinct indices give distinct actual supports:
removing the core and undoing its bijection recovers all seven values,
and the polynomial difference root bound gives injectivity.

For every paired nonstar index the six identified labels are distinct
and outside K,a,b. The left member contains a and excludes b, while
the right contains b and excludes a. They therefore cannot be equal,
so the hypothesis really forbids their intersection of at least 66.
Tagging vertices by side makes the pairs disjoint. Summing one
retention inequality per pair gives the nonstar bound. Each retained
star contributes q^2 to its own family's size; their equality in the
union does not remove either contribution from the sum of sizes.
This verifies the factor two and the balanced bound without assuming
that the matching lists every conflict or that the bound is attainable.

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_l126.py`.
The complete certificate is `scripts/finite-support/l126-critical-audit.json`.
The audit recomputes and compares all 14 fields, including the complete
nine-check dictionary, empty failure list and qualification, of the
original arithmetic certificate. It verifies both original rigidity
input hashes against the accepted L125 audit, compares all 840 entire
records to that audit, and independently checks their exact ordered-case
coverage, determinants, anchor images, all six images including poles,
and acceptance decisions. Three distinct anchor images uniquely determine
each invertible projective map, so the seven times 120 exhaustive cases
leave no missing map. The sole accepted map is again the identity for
removed point 16. All checks pass. Complete arithmetic, input-linkage,
accepted-map and failure fields were inspected; record checks inspect
the complete data programmatically, not a preview.

The verified retained-size sum is at most 2590122 against required
3064992, and the balanced bound is 1295061 against required 1532496.
Their shortfalls are respectively 474870 and 237435. The numerical
certificate does not replace the preceding universal symbolic proof.
This is acceptance of a previously unaudited local input, classified
REPRODUCTION, not a claim of new mathematics beyond the sources checked.
All scope exclusions in the conclusion remain. The argument and direct
inputs are unchanged; this audit supersedes the overview's pending-audit
qualification without altering the mathematical assembly.

## Mathlib

Full matching theorem for this specific full-star thinning obstruction:
**not checked**. Supporting polynomial root bounds, evaluation fibers,
finite bijections and finite sums: **not checked**. L125's audited
rigidity and exhaustive finite test are local inputs, not claims of
Mathlib coverage. Unknown availability is not evidence of absence.
The assessed search did not establish prior coverage of this particular
specialization; POTENTIALLY_NEW records that limited comparison, not
certified originality or progress beyond every known result.
