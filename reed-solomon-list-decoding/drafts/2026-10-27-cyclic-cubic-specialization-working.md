# Cyclic cubic specialization — working checkpoint

Approved target: Determine whether the union of any three complete dual direction components supplied by L135 lies on a plane cubic, with every group-labeling and degeneracy hypothesis justified.

The pre-invocation SPECIALIZE assessment is
`literature/2026-10-27-l135-cyclic-cubic-containment.md`. The main gap is
arbitrary-center 67/68 safety. Cubic containment could constrain span-two
coefficient geometry; collapse, span three, retention and RS transfer
remain independent. This is a source-backed specialization, not a new
classification or a restart of ATTEMPTS/109.

For distinct retained directions a,b,c, work only in the auxiliary field
F_137 to put lambda=(b-c)/(b-a), mu=(c-a)/(b-a). Both are nonzero.
The intersection of u+av=y_a and u+bv=y_b has
u+cv=lambda*y_a+mu*y_b. Consequently choose y_a=r/lambda,
y_b=s/mu and y_c=r+s. Multiplication by the two inverse scalars is
bijective; L135 supplies injectivity, disjointness and the prescribed
collinear triples. The group is additive F_137, cyclic of order 137.
These are index permutations, not coordinate-field homomorphisms.

Remaining write-up checks: choose dual coordinates over K explicitly;
prove distinctness and collinearity survive K -> algebraic closure;
retain the wholly collinear case via a K-line cubed; cite
Korchmaros–Nagy arXiv:1710.00172v1 Proposition 4.5 in other cases with
characteristic 65537>137. Descend its nonzero cubic using the
411-by-10 degree-three evaluation matrix over K: ranks agree over a
field extension, hence a nonzero kernel over the closure gives one over K.
No factor descent, common cubic across triples or irreducibility is needed.

Continue only if these obligations all hold for arbitrary labels and the
actual L135 exceptional-direction rule. Otherwise save the exact failed
hypothesis; generic labels and an ordinary-net assumption do not pass.

Existing notebook changes are preserved. No mathematical script is
needed for the symbolic labeling and linear-algebra descent.

Completed in step 531: all listed obligations are written in
`../lemmas/L136-triple-direction-cubic-containment.md`. The canonical
proof imports the geometric result and proves the local applicability
and rank-descent steps. Independent audit remains pending; this working
checkpoint is preserved as pre-completion reasoning, not another proof.
