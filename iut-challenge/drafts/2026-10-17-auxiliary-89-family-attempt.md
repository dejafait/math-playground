# Auxiliary p=89 family attempt — step 286

Approved target: test the p=89 translated cubic within L046/L048's
fixed-c, fixed-M family, using the prior SPECIALIZE assessment
`literature/2026-10-17-auxiliary-89-frobenius-family-test.md`.

Main gap: original finite B>=A. Intermediate target: an actual joint
scalar for a new auxiliary curve while retaining the named local and
global prerequisites. Possible later use: L072's sufficient radical
test for that new curve. Continue only if reduction, same-element
fixing and the positive full-rank count all pass; otherwise stop this
specified condition. Native T/model, exact generation, independent
initial data, marked factorization and essentiality remain open.

Work saved before final assembly: impose d=c^2/3 and e=c^3/27+1
modulo 89, using inverses only modulo 89. CRT with the original
3^M classes gives free progressions of step 89*3^M. Translation
over F_89 gives y^2=z^3+1, discriminant -432=13 mod 89.
Since 3*59=177=1 mod 88, cubing is bijective on F_89, including
zero. For each y exactly one z solves z^3=y^2-1, so there are
89 affine points and one point at infinity. Thus a_89=0.
The imported Frobenius identity gives pi^2=[-89]. On full E[120]
this is scalar 31, giving -Id on E[8] and Id on E[15].

Completed assembly: the full proof, source citations, fixing-field
argument, refined affine lattice/count and same-witness retention are
canonical in L073. All three tests pass for a new auxiliary witness.
No assertion about the retained E_0 is made. Independent critical
audit remains pending; the new audit assessment is REVIEW_REQUIRED.
