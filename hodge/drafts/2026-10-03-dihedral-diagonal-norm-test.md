# Dihedral-plus-diagonal norm-ideal test — retained reasoning

Date: 2026-10-03. The prior SPECIALIZE assessment is
[the unchanged-target review](literature/2026-10-03-dihedral-plus-diagonal-stable-support-map.md).
Saved before the proof and exact checks were completed;
the working calculation below is retained as a record.
The completed result is [L042](../lemmas/L042-dihedral-plus-diagonal-has-no-stable-lift.md).
PROGRESS.md remains the sole current checkpoint.

The gap is a different representative with a possible later
transverse use. The prescribed intermediate test is regularity
of the degree-three support map on S and invertibility of the
full image ideal of norms. A stable lift would permit a later
universal-sheaf deformation test. One noninvertible stalk stops
this recipe; no modification of the parameter surface is part
of this test. The attained span and RM directions remain 21
and three against four required.

L008 supplies g_0:W -> S finite flat of degree two and regular
g_1:W -> S. Apply the cited determinant norm to (g_0)_*O_W
with the g_1-action, then add the identity point. This gives
a regular cycle morphism; its generic cycle is the prescribed
C fibre plus the diagonal. The construction retains the
nonreduced cover fibres and all resolved points at infinity.

At each of the three fixed points over infinity, use L008's
order-seven local automorphism. Finite-group averaging gives
formal coordinates u,v in which f=(alpha u,beta v), with
weights (6,2), (3,5), (6,2). The ordered support is id,f,f^{-1}.
The imported norm generators are products of alternating
three-by-three determinants, not an unspecified reduced ideal.

Let D be the ideal of those determinants in C[[u,v]].
The tuples (1,u,v), (1,u,u^2), (1,v,v^2) yield nonzero
multiples of uv,u^3,v^3. For arbitrary monomial tuples, a
mixed exponent is divisible by uv; a pure exponent needs
three distinct powers and is at least three. Thus the
proposed full answer is D=(uv,u^3,v^3), and the actual
image ideal should be

\[
K=D^2=(u^2v^2,u^4v,uv^4,u^6,v^6).
\]

At the initial checkpoint the remaining checks were the exact cyclotomic coefficients,
the passage from regular target functions to their formal
completion, and application of L040's necessity hypothesis.
The candidate ideal is nonzero and primary for the maximal
ideal of a two-dimensional regular local ring, so it cannot
be invertible. This would reject stable lifting on S, without
any transverse-deformation or nonalgebraicity conclusion.

Mathlib coverage: **not checked**. The primary norm formulas
in foundations/08 and the lifting criterion in L040 support
the argument; they do not compute this particular stalk.

## Completed test

L042 proves regularity at every resolved fibre, the exact
completed image ideal at all three isolated collisions,
and failure of stable lifting on the unchanged S. The
explicit cyclotomic determinants and five minimal square
generators passed the supporting exact script. This is
an informative NEGATIVE and a REPRODUCTION of known tools,
with no originality claim. The failure occurs before a
transverse deformation test and does not exclude a
modified parameter source. No finite-collision ideal
calculation was needed after this decisive failure.
