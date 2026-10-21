# Retained Legendre odd-torsion attempt — step 273

The approved target is the conditional full-15-torsion test, using
`drafts/literature/2026-10-17-retained-legendre-odd-torsion-compatibility.md`
(SPECIALIZE, saved before this invocation). The main gap is still finite
B>=A. This intermediate test could discharge one model-compatibility
prerequisite before a later exact-generation comparison. It leaves the
independent initial-data, source-marked all-image and essentiality gaps.

## Working reasoning saved before final assembly

L045 supplies full 30-torsion on the unchanged E_0 over F; hence its
full 15-torsion is rational there. L048 gives v_3(j)=-30. In the same
embedding, j=1728 has valuation 3 and j=0 cannot have this finite
valuation. The conditional T=F_tpd subset F is a number field, so both
E_0/T and the specified nonsingular geometric pointed descent E_L/T
are over a common characteristic-zero field with nonexceptional j.

The inspected classification supplies a quadratic twist character on
G_T. Choose a geometric pointed isomorphism phi:E_0 -> E_L. Its cocycle
phi^(-1) sigma(phi) is that character as an automorphism of E_0.
Transport a basis of E_0[15] by phi. On G_F the known twist formula
is simply rho_L,15=chi Id, because rho_0,15=Id. Since -Id!=Id
on (Z/15Z)^2, the full kernel is exactly G_F intersect ker(chi).
Thus full rational 15-torsion on E_L is equivalent to trivial chi|G_F,
or to its quadratic parameter being a square in F. The actual parameter
is not supplied by the conditional native setup; no verdict follows.

Continuation test: only an identified trivial restriction permits a
later minimal-generation comparison for that model. An identified
nontrivial restriction stops that model over this unchanged F. An
unidentified restriction stays conditional. No field enlargement or
curve reselection is licensed. The stronger general division-field
clause excluded by step272 is not used.

Duplicate/failure check: foundations/05 step272 and its detailed
source comparison identify this as an unperformed application;
L045,L048 and ATTEMPTS/028 do not test this character. The broad
selected-model reduction stop is a different predicate. Preserve
ATTEMPTS/027,031,032 and all unfinished work.

## Completed attempt

The conditional specialization is written in canonical L070, including
the common-field/short-equation checks, nonexceptional j, transported
basis, full restricted kernel and all unresolved assumptions. The test
is established but its actual character remains unidentified. This is
local progress by known methods, with no claim beyond the sources
checked. No numerical experiment or mathematical script was needed.
Separate critical review is the next target; exact generation is not
authorized by this conditional outcome.
