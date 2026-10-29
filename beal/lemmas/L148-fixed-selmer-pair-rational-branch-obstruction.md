# L148 — The fixed Selmer pair contains the rational branch class

## Hypotheses

Use L138's actual smooth proper odd model
Y²=(X−9075)H(X), its Jacobian J over Q, and K=Q(alpha), where

    A(alpha)=alpha⁴+64alpha³+150alpha²−32500alpha−109375=0.

Use its specified algebra Q×K, with X mapping to (9075,eta),
eta=−907500/(alpha−50), and the full odd-model square-class group
(Q×K)*/(Q×K)*², without a rational-scalar quotient. Use L139's
Kummer interface and L147's certified Selmer classes epsilon and
eta_class with masks 165 and 132102. These masks specify products in
the fixed witness list; they are not assumed to be global coordinates.
The order basis is (1,alpha,beta,gamma), with

    beta=(alpha²+14alpha+25)/50,
    gamma=(alpha³+239alpha²+4475alpha+19375)/18750.

Write D=[(9075,0)−infinity] in J(Q). No full global basis, exact Selmer
dimension, finiteness of Sha, sextic transport or covering model is assumed.

## Conclusion

In the full odd-model square-class group,

    delta(D)=epsilon != 0,
    delta(D)!=eta_class,
    delta(D)!=epsilon*eta_class.

Thus the fixed two-dimensional Selmer span contains the nonzero rational
Kummer class epsilon. The Cassels–Tate pairing restricted to this span
is identically zero; in particular <epsilon,eta_class>=0. This pair
cannot give a nonzero pairing for a sharper rank bound. This does not
assert that eta_class is outside the rational Kummer subgroup, that the
whole Selmer pairing vanishes, or that a different pair cannot work.
The bound rank J(Q)<=2+c<=4 and all point-control/Beal gaps remain.

This is a standard-method instance calculation. Independent exact replay
passes; the separate critical mathematical review of 2026-10-28 accepts
the three comparisons and the fixed-span consequence without correction.

## Proof

### Imported interface and pairing facts

Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-28-pair-branch-annihilator-test.md` and its
ready Fisher–Yan assessment, without refreshing source coverage.
Michael Stoll, *Implementing 2-descent for Jacobians of hyperelliptic
curves*, Acta Arith. 98 (2001), 245–277, Section 4, Lemmas 4.1/4.3
and Proposition 4.2, pp.249–251,
[publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83397),
DOI 10.4064/aa98-3-4, gives the injective odd-degree cohomological
representation in the norm kernel of L*/L*² and the branch evaluation.
L138 verifies the monic integral squarefree odd model with rational
infinity; L147 supplies the precise branch value and both Selmer inputs.
Equality here requires squares in both Q and K, not equality modulo scalars.

Tom Fisher and Jiali Yan, *Computing the Cassels–Tate pairing on the
2-Selmer group of a genus 2 Jacobian*, author manuscript dated
14 September 2023,
[equations (1)–(2), p.2 and equation (40), pp.18–19](https://www.dpmms.cam.ac.uk/~taf1000/papers/genus2ctp.pdf),
puts the Selmer pairing through Sha[2]. Hence the image of J(Q)/2J(Q)
is in its radical. For vanishing on the full two-dimensional span, use
also Lemma 2.4, p.10 and Lemma 3.1, p.19: the rational Weierstrass point
makes c_can zero, so the pairing is alternating. No finiteness of Sha
or full rational two-torsion is needed. The off-diagonal vanishing itself
uses only the rational radical containment.

### Exact positive comparison

The branch representative from L147 is d=(h,b), where

    h=H(9075)=73990352390625=3⁵ 5⁶ 11⁷,
    b=9075−eta=−8085−220alpha+440beta−1320gamma.

Set

    t=13341611250000000,
    s=10519/1500+(67/225)alpha+(5471/4500)beta−(947/375)gamma
     =225497/45000+(6653/187500)alpha
       −(73819/9375000)alpha²−(947/7031250)alpha³.

Using L147's exact epsilon=(q_e,b_e), direct rational arithmetic gives

    t²*q_e=h,       s²*b_e=b.                         (1)

For explicit polynomial-reduction evidence, s² modulo A has ascending
power coefficients

    (301578101/12656250, 33593417/421875000,
     −300309097/7031250000, −45107557/63281250000).

Multiplying this vector by b_e modulo A gives exactly b, in all four
coordinates. Both components in (1) are nonzero, and (1) proves that
d/epsilon=(t,s)² in Q×K. A numerical interpolation proposed s, but
only these exact identities certify equality; no numerical evidence or
root-search exhaustion is used as proof. Since v_3(h)=5 is odd, h is
not a rational square. Thus d and epsilon are nonzero classes.

### The other two comparisons

For d/eta_class a certified real embedding already suffices. There is
a real root of A in the interval

    I=[−3105933/65536, −776483/16384].

The endpoint values of A are respectively

    1222606091777206673/18446744073709551616 > 0,
    −40592557146770991/72057594037927936 < 0.

By the intermediate value theorem there is a root in I. Irreducibility
of A, already authenticated in the actual field interface, gives an
embedding K into R at this root. Termwise rational interval evaluation
of b and of the quartic component b_eta of eta_class gives respectively

    b(I) subset
      [−166956019462677687/687194767360000,
       −10684080015131015449/43980465111040000],
    b_eta(I) subset
      [404687349923679358827/43980465111040000,
       6324542858191440901/687194767360000].

The first interval is strictly negative and the second strictly positive.
Therefore b/b_eta is negative at this real embedding and cannot be a
square in K. This decides the full product-algebra comparison regardless
of its rational component (which is a square).

For d/(epsilon*eta_class), the rational component is

    4757902330643963015625000000000000000000000000.

Its 3-adic valuation is 17, so it is not a rational square. This decides
the third comparison independently of its quartic component. These are
all three nonzero combinations because the two classes are independent
by L147. No assertion about global generation is made.

### Consequence and verification

The branch divisor D is rational on the actual proper odd model, so
delta(D)=epsilon is in the rational Kummer subgroup. Radical containment
therefore gives <epsilon,v>=<v,epsilon>=0 for every Selmer class v.
Alternation gives <eta_class,eta_class>=0. By bilinearity every pairing
of two elements in span{epsilon,eta_class} is zero. Thus this pair cannot
produce the proposed rank-two pairing contribution. In particular this
is a forced-zero obstruction, not a computed nonzero pairing, an exact
rank, or evidence of point control.

Reproduction commands, run from this notebook:

```bash
python3 scripts/pair-genus-two/branch_annihilator.py
python3 scripts/pair-genus-two/verify_branch_annihilator.py
```

Full producer evidence is
`scripts/pair-genus-two/branch-annihilator-certificate.json`.
The independent replay in
`scripts/pair-genus-two/branch-annihilator-verification.json` uses the
accepted maximal-order multiplication table, a separate basis conversion,
direct multiplication s²*b_e=b, and termwise real interval bounds instead
of the producer's Horner intervals. It checks all three ratios, the full
source hashes, odd rational valuations and nonzero branch, without importing
the producer or repeating its numerical proposal stage. All 130 checks
pass. Producer/replay recorded rational coefficient sizes are 325/69 bits,
below 8192; the producer used 8 of at most 16 sign proposals and decided
3 of the required 3 comparisons. The earlier missing-SymPy import is
preserved in `scripts/pair-genus-two/branch-annihilator-initial-dependency-failure.json`;
it produced no mathematical decision. No dependency was installed or backend
probed, and no complete-factorization claim is needed: the positive case
has exact roots and both negative cases have exact obstructions.

### Separate critical mathematical audit — 2026-10-28

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-28-branch-annihilator-critical-audit.md`.
This review accepts the statement without a mathematical correction.
It imports the precise Stoll and Fisher–Yan results above and verifies
their instance hypotheses; it does not reprove general descent or pairing
theory. No claim beyond the inspected sources is made.

**Actual proper curve and equality group.** L138's accepted inverse
proper-model isomorphism sends (T,W)=(-2,0) to (9075,0) and (2,0) to
the unique rational odd infinity. Its squarefree quintic makes both
Weierstrass points smooth. Thus D is an actual rational degree-zero
divisor class on this J. Stoll's branch formula is (H(r),r−eta), with
the positive H(r) sign. Its norm is H(r)², as required. The injective
odd-degree representation uses the full Q×K square-class group. Both
components must be squares for equality; no rational scalar is removed.
The odd valuation of H(r) verifies nonzero image modulo 2J(Q), rather
than assuming this for every rational two-torsion class.

**Complete instance evidence.** Both arithmetic implementations were
read completely, and the independent maximal-order replay was rerun:
130 checks pass. Its full input hashes still match L147's accepted
membership certificate and audit. The additional independent literal
power-basis check
`scripts/pair-genus-two/audit_branch_annihilator.py` passes all 55 checks;
its full evidence is `scripts/pair-genus-two/branch-annihilator-audit.json`.
It imports neither implementation. It binds all source inputs, verifies
the actual eta formula, H(r) and its factorization, both printed forms
of s, every printed coefficient of s², and both identities (1), directly
against L147's exact representatives. It also recomputes every printed
interval endpoint, A endpoint value and the odd product valuation, and
checks all four coordinates of all three saved quartic ratios.

The interval I is strictly negative. Each monomial is monotone there,
so summing its endpoint extrema gives the stated valid termwise
enclosures. The strict endpoint sign change gives a real root. L138's
accepted field identification and irreducibility make evaluation at
this root a field embedding of the same K. The numerator is negative
and denominator positive throughout I; hence their ratio is negative
at that embedding and cannot be a square. Uniqueness of the root in I
is unnecessary. The product comparison uses the odd valuation 17 in
the rational component alone. These are conclusive nonsquare witnesses,
not unsuccessful searches. Only the exact displayed square roots
are used from the numerical proposal stage. No complete factorization
or root-search exhaustion is assumed.

**Precise pairing consequence.** L147 already supplies actual all-place
Selmer membership and independence of masks 165 and 132102. The equality
delta(D)=epsilon places epsilon in the rational Kummer image, which
maps to zero in Sha[2]. The cited pairing therefore vanishes in either
argument against epsilon, without any finiteness assumption on Sha.
For the self-pairing of eta_class, the rational Weierstrass point gives
zero canonical cocycle in Fisher–Yan Lemma 2.4; Lemma 3.1 then gives
alternation. Thus every one of the four generator pairings is zero,
and bilinearity proves the stated full-span vanishing. A full Selmer
basis and full rational two-torsion are unnecessary. Rationality or
nonrationality of eta_class modulo 2J(Q) is not decided.

This accepts ATTEMPTS/066's obstruction to this particular pair, while
preserving ATTEMPTS/065's separate finite construction failure. It gives
no improved rank bound, full pairing matrix, marked/integer recovery,
rational-point classification or resolution of other signatures.

## Mathlib

Full matching Mathlib coverage for this specific odd-model equality,
Selmer pairing and arithmetic certificate has not been checked. Unknown
coverage is not evidence of absence. These exact scripts are arithmetic
certificates, not Lean proofs.
