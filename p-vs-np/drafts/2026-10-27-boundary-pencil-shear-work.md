# Boundary-coupled block-shear attempt — step 533

## Scope and saved starting point

The pre-invocation EXPLORE assessment is
`drafts/literature/2026-10-27-boundary-coupled-unary-block-pencil.md`.
This is one mathematical attempt at its exact target, not a new source
review. Startup changes are confined to this notebook and are preserved;
no existing scripts, receipts or historical proofs are reset.

The main target remains uniform worst-case P versus NP. The local gap is
the missing uniformly linear scalar simulation bridge for the unary fourth
comparison. The intermediate target is a boundary-preserving stable shear
exchanging the rank-one coupling in the two product pencils for F_r G and
G F_r, then realizing it by right-closed scalar arrows at the original
wrapped endpoints. A successful construction could supply the F_r sector
of that comparison. General F, mixed letters, actual fixed-job reception,
whole work/wire/live bounds, certificate availability and unrestricted
complexity conclusions would remain open.

The bounded test is one explicit boundary-only block-shear template.
Continue only with all oriented boundary/transition equations and an
explicit universal bound on support plus every repeated intermediate
graph, or with a materially refined unresolved subproblem. Abandon that
template on a complete failed equation or forced superlinear charge;
neither incomplete conversion nor equality of Schur complements is an
impossibility result.

L110 sections 3–4 and 21 fix right closure and the original product recipe.
L115 sections 2–6 provide an affine-letter substitution and a single-layer
chain, whose iteration has no aggregate linear bound. L116 sections 2–3
exclude the separate all-state delay interface. Attempts 047–050 were
checked; this test preserves only boundary coupling and imports none of
their failed constructions as a premise. The source comparison's exact
Schrempf 2018 Proposition 1.13 product formula and two-sided/scalar-arrow
distinction are reused. No new literature claim or novelty claim is made.

## Initial calculation

For an operand H, write L_H(z)=I+C_H+zD_H over F_2[z], with designated
entry row e_H and exit column b_H. The imported product presentation has
diagonal blocks L_F,L_G, upper-right block b_F e_G, entry (e_F,0) and exit
(0,b_G)^T. A block permutation alone does not exchange the boundary roles.
The next calculation must specify its shear, any stabilization, and both
boundary equations before treating this presentation as a scalar arrow.
No bridge or obstruction was established at the initial checkpoint.

## Saved obstruction before final write-up

Test the scalar-shear realization with only identity-pencil stabilization:
L_B plus I_k equals P (L_A plus I_k) Q, with scalar invertible P,Q and
the correctly transformed raw entry/exit vectors. Such an equality forces
M_B plus 0_k = P (M_A plus 0_k) P^-1 after right closure. This necessary
transition condition holds regardless of support or boundary choices.

Take G on p,u,v,q with constant edges p->q,u->q,v->q and letter edges
p->u,p->v. Its accepting polynomial is 1+x+x=1; all vertices lie on
structural accepting paths and p,q are distinct extremal roots. For F_r,
let J be the shift on f_0,...,f_r, T=J(I+J)^-1 and h=T e_(f_r)^T.
In common endpoint coordinates s,F,p,u,v,q,t, direct right closure gives:

- A=Prod(F_r,G): F rows have T on F and h times (p+q+t);
  row p is u+v; all remaining rows vanish.
- B=Prod(G,F_r): F rows have T on F and h times t;
  row p is u+v; all remaining rows vanish.
- Both initial rows are s+sum_i f_i+p+q+t, and both final columns are t.

For every r>=1, T^r=J^r and T^(r+1)=0. Consequently
M_A^(r+1)=e_(f_0)^T(e_u+e_v) is nonzero, whereas M_B^(r+1)=0.
For r=1 this is a complete eight-state counterexample: M_A's only rows
are f_0->f_1+p+q+t and p->u+v, while M_B's are f_0->f_1+t and p->u+v.
The original size sum is 10r+46. Stabilization adds zero transition blocks
and cannot remove the mismatch, so no amount of scalar shear support fixes
this template. Polynomial multipliers, nontrivial added components and
singular/rectangular simulations are outside this conclusion.

The final proof must justify the closure rows including both wrappers,
the scalar two-sided-to-similarity conversion and every power identity.
This is an informative negative for one conversion mechanism, not a lower
bound on arbitrary bridges or progress beyond the assessed literature.

## Completed result and continuation scope

The saved calculation is now fully justified in
`lemmas/L117-boundary-pencil-scalar-shear-obstruction.md`, including the
complete r=1 matrices, all-r power identities, scalar boundary conversion
and original size sum. The canonical proof and exact counterexample are
the mathematical checks; no numerical script or incomplete certificate
is used. Attempt 051 preserves the failed mechanism. This completes one
RESEARCH / proof_attempt, with NEGATIVE outcome and REPRODUCTION
classification. No claim about all sparse chains or novelty is made.

For future routing, the unchanged pre-existing EXPLORE assessment
`drafts/literature/2026-10-26-unary-product-sparse-quotient.md` explicitly
covers directly constructed operand-based quotients and arbitrary scalar
F₂ maps. Its target, scope, inspected functional-quotient comparison and
final continuation conditions were read; no source was newly browsed or
assessment changed. Its qualitative inputs do not assert a sparse common
quotient. That existing target can be reused for one new singular-map
test; L117's invertibility obstruction is new information selecting the
template, not permission to infer a quotient or repeat the stopped
monomial-degree construction. The current checkpoint records the exact
matching target and bounded test. No second mathematical attempt occurs
in this step.
