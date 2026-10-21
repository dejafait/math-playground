# L039 — Enlarged field excluded by the full rational torsion prerequisite

## Hypotheses

Fix L=Q_3(zeta_20,pi), where zeta_20 is primitive of order 20 and
pi^27=3. Normalize v_3(3)=1. Use L031's audited field data:
e(L/Q_3)=27, f(L/Q_3)=4 and v_3(L^times)=(1/27)Z. Use only the
no-primitive-third-root conclusion of L032, proved in its “Torsion and
the genuine all-unit logarithm” paragraph. Its Galois presentation,
reference subgroup and logarithm basis are not hypotheses for this test.

Use precisely **Dupuy–Hilado, arXiv:2004.13228v1 (28 April 2020)**,
**Definition 5.3.1(3)/Remark 5.3.2**, printed p. 26; **section 5.4**,
pp. 28–29; **Definition 5.5.1**, p. 30; and the individual selected
factor definitions **3.6.1/3.6.3**, pp. 11–13
([versioned HTML](https://arxiv.org/html/2004.13228v1#S5.SS3),
[versioned PDF](https://arxiv.org/pdf/2004.13228v1)). Write F for the
elliptic-curve base number field, E/F for the curve, D=F(E[ell]) for
the full eligible ell-division field, and D_w for an individual selected
completion at w above 3. The prerequisite is

    E(overline F)[30] contained in E(F).

It concerns all geometric 30-torsion, not the selected cyclic subgroup M.
The primary HTML preserves the overbar lost in PDF text extraction.
The inclusion F -> D -> D_w is the field/completion inclusion; if v is
the restriction of w, section 5.4 also includes F_v in D_w.

Import **Silverman, The Arithmetic of Elliptic Curves**, second edition,
Springer GTM 106 (2009), **Corollary III.8.1.1**, p. 96, with
**Proposition III.8.1(c,d)**, pp. 94–95: full rational m-torsion implies
containment of mu_m, for m>=2 prime to the field characteristic when
positive ([primary book PDF](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=114)).
The saved assessment `drafts/literature/2026-10-10-enlarged-field-full-torsion-test.md`
reuses inspected primary statements and the nondegeneracy/equivariance
proof cases. This known theorem and L032's local torsion conclusion are
imported without reproof; only their applicability is checked here.

## Conclusion

L cannot be isomorphic as a Q_3-field to an individual selected
division-field completion D_w in this versioned setup, for any eligible
ell. The full rational 30-torsion prerequisite alone gives the obstruction.

This stops the exact enlarged individual-factor realization route. It
does not exclude decomposed tensor components, transfer the exclusion to
native IUT definitions, invalidate any auxiliary lattice calculation,
or demonstrate an essential IUT flaw or failure of original finite B>=A.

## Proof

The base number field F has characteristic zero. Thus Silverman's
corollary applies to E/F with m=30, using the displayed full geometric
torsion prerequisite. Composite m is covered by the cited corollary;
residue characteristic 3 imposes no restriction on this characteristic-
zero application. Consequently F contains a primitive 30th root zeta.
The element rho=zeta^10 has order exactly three: rho^3=1, whereas
rho!=1 since zeta has order 30.

The map F -> D is a field inclusion. The completion map D -> D_w is
injective: a nonzero x has nonzero absolute value at w, and its image
has the same absolute value, so cannot be zero. Therefore rho maps to
an element of order three in D_w. Explicitly, its cube remains 1 and
rho-1 remains nonzero by injectivity. Selecting w, or passing through
the included F_v, cannot remove a root already in F.

If D_w were isomorphic as a Q_3-field to L, that isomorphism would
carry this element to a primitive third root in L. This contradicts
L032's no-third-root conclusion. That local conclusion uses L031's
ramification/value-group data, not the total degree 108. No new local
torsion calculation is performed here. This proves the exclusion for
each individual selected completion, independently of ell, an action,
a pilot or a radius prescription.

The elliptic-torsion-to-unit-root connection is exactly the cited Weil-
pairing corollary; absence of unit torsion alone was not used to assert
absence of elliptic torsion. Nor was a rational cyclic subgroup
substituted for full torsion. L029's old-field exclusion and L038's
auxiliary radius are comparisons and motivation, not proof inputs.
Remark 5.3.2's discussion of native prerequisites is not an equivalence
with native initial theta data. A tensor component is also not identified
with the individual D_w role tested here. These qualifications leave the
actual/native input/action, global realization, pilot transport,
essentiality and original numerical comparison unresolved.

### Separate critical audit, 2026-10-10

Verdict: the stated individual-completion exclusion passes. The audit
uses the separately approved coverage in
`drafts/literature/2026-10-10-enlarged-field-full-torsion-critical-audit.md`;
it imports the recorded primary theorem statements without claiming
fresh source access or reproving the Weil pairing. No mathematical
correction or strengthening of the conclusion is required.

The source prerequisite is the entire geometric group E(overline F)[30]
being rational over F. Silverman's Corollary III.8.1.1 applies because
F is a number field and 30 is nonzero in F. Its hypothesis is prime-to-
field-characteristic torsion, not prime-to-residue-characteristic torsion;
the prime 3 below w creates no exception. The corollary covers composite
m and supplies all mu_30, hence an element of exact order 30. Raising
that element to the tenth power gives exact order three, as checked in
the proof. Neither the chosen cyclic subgroup nor rationality of one
torsion point would suffice for this application.

Both embeddings F -> D -> D_w are unital and injective; completion at
a place is not reduction modulo its maximal ideal. Thus rho-1 remains
nonzero even at residue characteristic 3. Any proposed Q_3-field
isomorphism D_w -> L also preserves 1, multiplication and inequality
with 1, so the transferred root still has exact order three. The proof
does not require an identification of algebraic closures, a compatible
choice of torsion basis, or a particular eligible ell.

For the local contradiction, L031 fixes U unramified of degree four
and X^27-3 Eisenstein over U. Its displayed power-basis valuation gives
v_3(L^times)=(1/27)Z, with v_3(3)=1. L032's cited Eisenstein argument
for X^2+3X+3 gives v_3(zeta_3-1)=1/2 for a primitive third root.
The obstruction is exact: 1/2=k/27 would force 2k=27 for an integer k.
The total degree 108 cannot give this obstruction and is not used.
This paragraph of L032 precedes and is independent of its admitted
Galois presentation and subgroup calculations. No logarithm-span
certificate or later action theorem is needed for this audit.

The proof therefore establishes precisely the stated necessary-condition
failure for each individual D_w. The direct mathematical inputs remain
L031 and the specified paragraph of L032; L029 and L038 supply no
essential premise. Native definitions and decomposed tensor components
have not been audited here. The result confirms a local route stop,
not a flaw in IUT or a new theorem beyond the cited methods. Full
matching and supporting Mathlib coverage remains not checked.

## Mathlib

Full matching enlarged-field/source-role exclusion: **not checked**.
Supporting Weil pairing, roots of unity and injective completion maps:
**not checked**. Unknown coverage is not evidence of absence. This is
a known-result specialization (REPRODUCTION), with local route-changing
evidence and no claim of a discovery beyond the sources checked.
