# L133 — The pair branch quartic has no quadratic tower over Q

## Hypotheses

Use L110's exact branch factor Q4(T)=7+52T−6T²−64T³−25T⁴ and its
irreducibility over Q from L132's degree-preserving irreducible reduction
modulo 19. Let K=Q(theta), Q4(theta)=0. All field maps are over Q;
a splitting-field subfield is not presumed to lie in K.

## Conclusion

There is an explicit field isomorphism

    K ≅ Q[alpha]/(alpha⁴+64alpha³+150alpha²−32500alpha−109375),
    alpha=25theta,       theta=alpha/25.

K has no quadratic subfield, hence no tower of two quadratic extensions
of Q and no primitive generator with an even quartic minimal polynomial.
This closes the quadratic-tower shortcut only. The displayed primitive
integral polynomial has height 109375 versus Q4's height 64, so this
scaling provides no coefficient improvement. Other non-even defining
quartics might be smaller. There is no maximal-order, field-discriminant,
class/unit, Selmer, rank, point or Beal-exclusion conclusion.

## Proof

### Field identification

The monic irreducible polynomial of theta is

    f(X)=X⁴+(64/25)X³+(6/25)X²−(52/25)X−7/25.

Multiplication by −1/25 preserves irreducibility, so L132 applies.
For g(X)=X⁴+64X³+150X²−32500X−109375, coefficient comparison gives

    g(25X)=25⁴f(X),       f(X/25)=g(X)/25⁴.

Thus alpha -> 25theta and theta -> alpha/25 define inverse homomorphisms
of the quotient algebras: both compositions fix the generator. Hence
g is irreducible too. The full alpha-to-theta power-basis matrix is
diag(1,25,625,15625), determinant 25⁶=244140625 != 0. Its inverse is
diag(1,1/25,1/625,1/15625), and both products are I4. This identifies
the field without asserting that Z[alpha] is its maximal order.

### Imported resolvent theory and the exact cubic

Import Keith Conrad, *Galois Groups of Cubics and Quartics (Not in
Characteristic 2)*, author-hosted 18-page version accessed 2026-10-25,
[Definition 3.1 and equation (3.7), p.6; Theorem 3.6, pp.7–8](https://kconrad.math.uconn.edu/blurbs/galoistheory/cubicquartic.pdf).
For an irreducible monic quartic X⁴+aX³+bX²+cX+d in characteristic
different from two, the resolvent is

    R(Z)=Z³−bZ²+(ac−4d)Z−(a²d+c²−4bd).

An irreducible resolvent makes the quartic splitting group A4 or S4
in its four-root action. Here the base is Q, so the characteristic
and separability hypotheses hold. Substitution of the coefficients of f
gives exactly

    R(Z)=Z³−(6/25)Z²−(2628/625)Z−43128/15625,
    H(Y)=25³R(Y/25)=Y³−6Y²−2628Y−43128.

The invertible scaling preserves reducibility over Q. H is irreducible
by either of two complete certificates. The rational-root theorem says
any rational root of this monic integral cubic is an integer dividing
43128. Complete divisor generation tests every n from 1 through 207,
since 207²<=43128<208², retaining both n and 43128/n when divisible.
There are 24 positive divisors, and all 48 signed evaluations are nonzero.
Full generation remainders and evaluations are saved and replayed below.
A cubic is reducible over a field exactly when it has a root.

Independently, reduction modulo 7 gives Hbar(Y)=Y³+Y²+4Y+6, whose
values at 0,1,2,3,4,5,6 are 6,5,5,5,4,1,2 in F7. Thus Hbar is
irreducible. The monic integral polynomial has degree-preserving
reduction, so Gauss's lemma and irreducibility by reduction prove H
irreducible over Q. These seven evaluations alone suffice independently
of the integer-root list. Therefore R is irreducible and the imported
quartic criterion applies.

### The quartic field, rather than its normal closure

Import Conrad, *Galois Groups of Cubics and Quartics in All
Characteristics*, author-hosted 21-page version accessed 2026-10-25,
[Theorem 4.1 and proof, p.18; subgroup obstruction, p.19](https://kconrad.math.uconn.edu/blurbs/galoistheory/cubicquarticallchar.pdf).
The cited subgroup argument rules out quadratic subfields of the
degree-four root field in both cases: A4 has no index-two subgroup;
the only index-two subgroup of S4 is A4, which does not contain the
S3 point stabilizer. By Galois correspondence an intermediate quadratic
field would require exactly such a subgroup containing the root
stabilizer. K is this root field, so has no quadratic subfield.
The same source's Theorem 4.1 characterizes quartic fields with such
a subfield by an even-quartic primitive generator. Its contrapositive
gives the stated absence of an even defining polynomial. General
group/subfield theory is imported, not reproved as a new result.

There are no rational resolvent-root branches, so no exceptional
pair-sum/product, zero-discriminant or V4 construction was omitted.
A quadratic field solely in the normal closure would not contradict
this conclusion.

### Reproduction, certificates and bounds

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-25-pair-quartic-field-tower.md`.
This is an exact-instance reproduction, with no originality claim
beyond the inspected sources.

Producer: `python3 scripts/pair-genus-two/quartic_field.py`.
It creates a fresh ledger only when none exists. The successful current
run used `--resume-ledger` after a recorded instrumentation repair,
preserving the initial failed preparation's charges. Full exact
coefficients, divisor-generation remainders, all signed root trials,
field maps, matrices and compositions are saved in
`scripts/pair-genus-two/quartic-field-certificate.json`.

Replay: `python3 scripts/pair-genus-two/verify_quartic_field.py`.
It imports only accounting, reconstructs the entire divisor scan and
evaluates every candidate by Horner's rule rather than the producer's
power sum. It also checks all seven residues modulo 7, both field
relations in the quotient rings, both generator compositions, complete
four-dimensional bases and matrix products, and the determinant by
elimination. All 164 checks pass, with no failures, in
`scripts/pair-genus-two/quartic-field-verification.json`.
These arithmetic checks are not a separate critical proof audit.

The cumulative `scripts/pair-genus-two/quartic-field-ledger.json` records
actual/required caps: 0/3 resolvent-root branches, 0/6 relative-factor
candidates, 517/250000 root/divisor trials, 5458/500000 instrumented
exact scalar operations, polynomial degree 4/8 and integer numerator/
denominator bits 47/4096. No cap was hit. The 517 trials include both
207-entry divisor scans, both 48-entry root tests and seven modular
tests. Scalar charges count the integer/rational arithmetic and
comparison API, including normalization and rejected candidates;
internal Fraction gcd/bit operations, loop indices, allocation, sorting
internals and serialization are not elementary operations counted here.
The initial observer TypeError, retained initial ledger and accounting
repair are documented in `drafts/2026-10-25-pair-quartic-field-attempt.md`.
No mathematical correction was needed.

The only alternative absolute model tested is the certified scaling g.
Its primitive integral height 109375 fails the threshold <64. No relative
quadratic-equation height test applies, since a quadratic subfield is
impossible. Direct quartic arithmetic and non-tower polynomial reduction
remain possible. Class/unit completeness, quotient ranks and points,
marked lifts, degree-nine recovery, both L095 systems and other residual
exponent signatures remain unresolved.

## Mathlib

Full matching coverage and supporting resolvent, Galois-correspondence,
finite-field and number-field-map results have not been checked in
Mathlib. No absence claim or Lean verification is made.
