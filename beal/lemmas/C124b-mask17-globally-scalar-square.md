# C124b — Mask 17 is globally scalar-square

## Hypotheses

Use L115's entire field K=Q[theta]=Q[t]/(F), where

    F(t)=275t⁸−2860t⁶+6930t⁴−3564t²+243

is irreducible of degree eight. Use L124's fixed generators
g0=−3−theta and g4=3−theta and its mask convention. Thus mask 17 is
delta=g0*g4=theta²−9. The quotient is K*/(K*² Q*), with a single
embedded rational scalar group. No supported-group completeness, class
group, unit basis, rational-point hypothesis or global independence of
the generators is assumed.

## Conclusion

The fixed element is globally trivial in this quotient. Precisely, put

    h=(275theta⁷−3085theta⁵+8865theta³−6183theta)/1728.

Then h is nonzero and

    theta²−9 = −11 h².                                      (1)

In particular the localization collision of g0 and g4 comes from a
genuine global scalar-square relation. Equation (1) does not assert that
delta itself is a square in K, determine all supported classes, realize
a fake image by a rational point, or exclude either L095 integer system.

## Proof

### Coverage and method

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-24-mask17-global-scalar-square.md`.
This is a REPRODUCTION of an exact fixed-element computation using known
factorization and quotient methods, with no novelty claim.

The method source is Barry M. Trager, *Algebraic Factoring and Rational
Function Integration*, Proceedings of SYMSAC '76 (1976), pp.219–226,
[DOI](https://doi.org/10.1145/800205.806338),
[primary scan](https://www.cecm.sfu.ca/~mmonagan/teaching/TopicsinCA11/TragerFactor.pdf),
Section 2 pp.219–221, Theorems 2.1–2.3, Lemma 2.4, Corollary 2.5 and
the algorithms sqfr_norm/alg_factor. L115 supplies a monic irreducible
defining polynomial F/275 over the characteristic-zero effective field Q.
The source provides a complete general method; the present positive
certificate needs only exact polynomial identities. We do not claim to
have executed its full shift/norm algorithm or to have proved factor
irreducibility. Neither is necessary to verify a displayed root.

For the quotient convention use Nils Bruin and Michael Stoll,
*Two-cover descent on hyperelliptic curves*, Math. Comp. **78** (2009),
2347–2370, [DOI](https://doi.org/10.1090/S0025-5718-09-02255-8),
inspected [arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2),
21 October 2008, Section 2 p.3 and Section 6 pp.11–13, especially
ad 12. The field is the unchanged even-degree algebra from L124; the
scalar −11 is a single element of Q*, not independent local scalars.
The identity below also proves triviality directly from the definition
of the quotient, without importing any point-existence conclusion.

### Exact positive certificate

Define integer polynomials

    P(t)=275t⁷−3085t⁵+8865t³−6183t,
    R(t)=3025t⁶−36410t⁴+120825t²−110592.

The following is an identity in Z[t]:

    11P(t)² + 1728²(t²−9) = F(t)R(t).                       (2)

For a full coefficient check, both sides of (2), in ascending order
and retaining all fifteen coefficients, are

    [−26873856, 0, 423510363, 0, −1205870490, 0,
     1284110685, 0, −639074700, 0, 158322725, 0,
     −18664250, 0, 831875].

Substitute theta into (2). Since F(theta)=0 and 1728 is a nonzero
rational number, division by 1728² gives (1) with h=P(theta)/1728.
The element delta is nonzero: otherwise the nonzero polynomial t²−9
of degree two would annihilate theta, contradicting L115's irreducible
degree-eight minimal polynomial. Equation (1) then implies h is nonzero.
Thus both factors required in delta=(−11)h² lie in their stated
multiplicative groups. This proves the exact positive decision for an
arbitrary-scalar existence question. A complete negative-case scalar
enumeration or any assumption about S-class two-torsion is unnecessary.

For reproducibility, the discovery used u=theta² and v=1−9/u.
Substitution gives Q(v)=v⁴+128v³+1920v²+4352v+1024=0.
The polynomial

    H(Y)=Y⁴+44Y³+264Y²−1936Y−3872

satisfies H(Y)H(−Y)=11⁴Q(−Y²/11). Reducing H modulo
Y²=−11v gives an invertible linear equation in Y in the entire field.
Its solved root yields h above. The producer saves that inverse and
checks Y²=−11v. This explains how the candidate was obtained; (2) is
the self-contained load-bearing certificate. The bounded factor search
has no negative interpretation and does not certify completeness of
any other square tests.

### Evidence, downstream use and limitations

Run from the notebook:

    python3 scripts/pair-genus-two/mask17_global_scalar_square.py
    python3 scripts/pair-genus-two/replay_mask17_global_scalar_square.py

The full producer evidence is
`scripts/pair-genus-two/mask17-global-scalar-square-certificate.json`.
It retains the field, factor identity, v, linear equation, inverse,
root, h and exact F-multiple, with six passing exact checks and no
failures. The independent integer-only arithmetic replay imports no
producer code and writes
`scripts/pair-genus-two/mask17-global-scalar-square-replay.json`.
It compares all fifteen coefficients of (2) and the producer's actual
h, scalar and field polynomial: eighteen comparisons pass, with no
failures. This arithmetic replay is not a separate critical audit.

The achieved threshold is an exact global relation, stronger than the
previous local membership information for this fixed mask. It may be
used to remove this redundant generator relation from later supported
arithmetic. No full supported group is supplied. Independent gaps remain:
units/S-class two-torsion, other supported classes, surviving-cover
points, degree-nine root recovery, compatible remaining factors, both
L095 integer systems and minus-eleven. Identity and the known rational
infinity points survive. This is local notebook progress using known
methods, not progress beyond the inspected general factorization theory
or a Beal resolution. The separate critical audit below confirms this
fixed relation without a correction.

### Independent critical mathematical audit, 2026-10-24

The invocation-start approval is
`drafts/literature/2026-10-24-mask17-global-scalar-square-critical-audit.md`.
This is a REPRODUCTION proof audit under SPECIALIZE, reusing the precise
Trager and Bruin–Stoll source coverage above. No new theorem, square
search or supported-group enumeration is claimed.

Run the independent arithmetic auditor from the notebook:

    python3 scripts/pair-genus-two/audit_mask17_global_scalar_square.py

It imports neither earlier implementation and preserves both input
certificates. The complete evidence is
`scripts/pair-genus-two/mask17-global-scalar-square-audit-certificate.json`.
Its 57 comparisons pass with no failures; both input SHA-256 hashes,
all actual/required values and all monomial reductions are retained.
The full comparison records were inspected, not merely their pass count.

1. **Entire algebra and actual mask.** L115's audited proof establishes
   irreducibility of the displayed F of degree eight. Since 11 and 275
   are rational units, (G)=(F)=(F/275) in Q[t]. Thus L124 and this
   certificate use the same entire field and generator, rather than a
   chosen component or a changed root. L124's mask convention selects
   bits 0 and 4 for 17; direct multiplication of its actual generators
   (-3-t)(3-t) gives t²−9, with ascending coefficients [-9,0,1].
   No local collision is used to infer the global relation.
2. **Complete integer identity.** Independent multiplication of the
   explicitly displayed P, F and R gives all fifteen coefficients in
   (2), including all odd zero coefficients. Both sides agree with
   every entry of the printed vector. As a separate arithmetic check,
   exact Horner evaluation gives equality at each integer 0 through 14.
   Both sides have degree at most fourteen, so these fifteen distinct
   zeros also certify that their difference is identically zero over Q.
   These are exact integer evaluations, not approximate samples.
3. **Field reduction and stored evidence.** A separate reduction forms
   t^k modulo F for 0<=k<=14 by repeated shifting and the relation
   t⁸=-(243−3564t²+6930t⁴−2860t⁶)/275. Reducing
   -11(P/1728)²-(t²−9) gives all eight zero basis coefficients.
   Its unreduced polynomial is exactly F times -R/1728². The full
   producer F, h, scalar, delta, unreduced identity, F-multiple and
   remainder match these independent values. Every coefficient and
   parameter of the replay, its h vectors and its producer hash also
   match. This checks the complete load-bearing evidence; it does not
   independently reproduce the optional discovery factor search or
   assert completeness of its possible scalar choices.
4. **Denominators and nonzero conditions.** The rational denominator
   1728 is nonzero in this characteristic-zero field, so substituting
   F(theta)=0 into (2) permits division by its square. The polynomial
   t²−9 is nonzero of degree two, below the minimal degree eight;
   consequently delta is nonzero. Independently P is nonzero of degree
   seven, so h is also nonzero. Every nonzero element is invertible
   because this entire algebra is a field. No maximal-order, unit or
   S-class calculation is required for these assertions.
5. **One common scalar.** Equation (1) explicitly writes delta as
   the product of the single embedded rational number -11 and the
   square of an element of K*. It therefore lies in K*² Q*, precisely
   the denominator subgroup in Bruin–Stoll's even-degree quotient.
   This proves its class is identity using the quotient definition;
   it does not use independently adjustable component scalars. It
   does not assert delta is in K*². Point-image or norm-condition
   theorems are not needed to certify this fixed quotient equality.
6. **Dependency and scope check.** The direct mathematical inputs remain
   L115 and L124. C124a's local squareness is context, not a premise;
   neither L116 nor a negative-case scalar enumeration enters the proof.
   The audited relation is available for removing this redundancy in
   later supported arithmetic. Full units/S-class two-torsion, other
   classes, points on surviving covers, degree-nine root recovery,
   compatible remaining factors, both L095 systems and minus-eleven
   remain unresolved. Known infinity points still survive. The audit
   changes neither the argument nor its conclusions, and supplies no
   complete Beal candidate or progress beyond the cited general methods.

## Mathlib

Full matching Mathlib coverage of this fixed identity and its quotient
interpretation was not checked. The proof reduces to rational polynomial
arithmetic in a field quotient; no specific supporting formal theorem
names were checked. Unknown coverage is not evidence of absence.
