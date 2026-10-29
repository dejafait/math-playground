# L149 — A third independent class in the saved Selmer image

## Hypotheses

Use L138's actual smooth proper genus-two curve B/Q, Jacobian J, and
monic squarefree odd model Y²=G(X)=(X−9075)H(X), with

    H=X⁴−67760X³+1581228000X²−15306287040000X+52615361700000000.

Keep its specified identification Q[X]/G=Q×K, where

    K=Q(alpha), A(alpha)=alpha⁴+64alpha³+150alpha²−32500alpha−109375=0,
    eta=−907500/(alpha−50), X ↦ (9075,eta).

Use L139's supported product norm kernel and L147's accepted complete
local images, all 39 ordered supported source columns, and the complete
31-generator coefficient kernel. In particular epsilon and eta_class
are L147's globally independent Selmer classes with masks 165 and 132102.
Masks are products in that fixed zero-based column order, not global
coordinates. Equality is in (Q×K)*/(Q×K)*², without rational scalars.
The order basis is (1,alpha,beta,gamma), with

    beta=(alpha²+14alpha+25)/50,
    gamma=(alpha³+239alpha²+4475alpha+19375)/18750.

No ambient/global basis, Selmer generation, exact class-group order,
rationality of eta_class modulo Kummer, pairing value or Sha finiteness
is assumed. L148's fixed-pair rational-radical obstruction is retained.

## Conclusion

The fourth saved kernel generator, mask 3109 (columns {0,2,5,10,11}),
represents the Selmer class nu with exact representative

    q_nu = 1/524880000000000000,
    b_nu = 90688+(99088/5)alpha−(1403152/625)alpha²
                 −(33968/625)alpha³.

It satisfies q_nu*N_K/Q(b_nu)=1 and

    nu not in span_F2{epsilon,eta_class}.

Consequently epsilon,eta_class,nu are three independent Selmer classes.
The approved test stops here, after 10 of at most 124 comparisons and
4 of 31 generator products, with no unresolved comparisons. It does not
compute the remaining image dimension, full Selmer group, rational
Kummer quotient, any pairing value or improved rank bound. In particular
rank J(Q)<=2+c<=4 and the Beal/point-control gaps remain unchanged.

This is a known-method instance calculation with independent exact replay.
The separate critical mathematical audit of 2026-10-28 accepts the stated
membership, comparisons and independence without correction, as detailed
below. No general novelty or complete Beal candidate is claimed.

## Proof

### Imported membership interface and scope

Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-28-surviving-witness-span-test.md`.
Import Michael Stoll, *Implementing 2-descent for Jacobians of
hyperelliptic curves*, Acta Arith. 98 (2001), 245–277,
DOI 10.4064/aa98-3-4,
[Section 4, pp.249–253, Lemma 4.1, Proposition 4.2,
Proposition 4.6 and Corollary 4.7](https://www.impan.pl/shop/en/publication/transaction/download/product/83397).
The odd-model cohomology is represented in the full product norm kernel;
membership in the local Kummer image at every place characterizes Selmer.
At odd primes of good reduction, the unramified condition is the even
valuation condition in the product of maximal integer rings. The general
statements are imported, not reproved.

L138 verifies every model/algebra hypothesis: monic integral squarefree
degree five, rational infinity, and the actual Q×K identification. It
also verifies disc(G)=2³²3²¹5²⁷11³⁵, so every odd prime outside
S={infinity,2,3,5,11} has good reduction. L139 identifies the supported
norm kernel with the inverse-norm pairs used here. L147 supplies all
five complete local images, the authenticated supported columns and
their exact full and quotient coordinates. No scalar quotient or
surjectivity of the witness map is introduced.

### Complete domain authentication and membership

The bound source is
`scripts/pair-genus-two/odd-membership-35-certificate.json`, at
`/all_conditions/kernel`, with the original columns in
`scripts/pair-genus-two/two-adic-filter-certificate.json`, at `/witnesses`.
The new certificate binds these entire files, their accepted verification
and audits, the odd model/order inputs, and L148's branch certificates
by SHA-256. Both new implementations check the exact sources/order and
both reference products. They check all 31 saved masks are within 39
bits, independent as coefficient vectors, and zero combinations of
every concatenated quotient column. Quotient rank eight proves the
31 vectors form the full coefficient kernel. This is not global class
independence.

Each of the 39 columns has product norm one, checked again by exact
determinants. Their supportedness is L147's accepted input: the first
34 have complete principal-ideal records with even valuations outside
the seven allowed primes; the last five are the prescribed rational
elements −1,2,3,5,11, with inverse-norm rational components. Both new
scripts check every available parity entry. Valuations outside the
recorded factor base are zero by the accepted full ideal equalities;
no rational-norm support test is substituted for that fact. Products
therefore remain supported in both factors.

Mask 3109 is one of the saved kernel vectors. Multiplying its five
complete column representatives gives exactly (q_nu,b_nu) above and

    N_K/Q(b_nu)=524880000000000000.

Its packed full localization is 1965721630, using the accepted bit ranges
real 0–4, 11-adic 5–8, dyadic 9–17, 3-adic 18–23 and 5-adic 24–31.
Its quotient combination is zero at every one of these places. Thus
its restrictions belong to the five actual complete Kummer images.
Supportedness gives the local image condition at every other place
by the imported good-reduction theorem. Proposition 4.2 consequently
puts nu in Sel²(J/Q), not merely in a supported ambient group.

### Four conclusive full-group inequalities

The rational components of the ratios to the four reference classes are

| Reference | q_nu / q_reference |
|---|---|
| 1 | 1/524880000000000000 |
| epsilon | 55/12 |
| eta_class | 11/216000 |
| epsilon*eta_class | 3403125/16 |

All fractions are reduced. The first denominator satisfies

    724486024² < 524880000000000000 < 724486025².

The second and third numerators are the nonsquare integers 55 and 11.
For the fourth,

    1844² < 3403125 < 1845².

A reduced positive rational square has square numerator and denominator,
so all four ratios are nonsquares in Q. Thus none can be a square in
Q×K, regardless of the quartic component. These four obstructions alone
prove nu lies outside the reference span. The independently recomputed
full-localization differences are respectively

    1965721630, 322193568, 322382014, 1965680640,

all nonzero. They are corroborating full-coordinate obstructions, not
the zero image-quotient masks. No negative decision uses failed root
proposals, local agreement, or an incomplete factorization.

L147 proves epsilon and eta_class independent in the same group.
If a relation among these and nu had nu coefficient zero, it would
contradict that independence; if it had coefficient one, it would put
nu in the tested span. Hence all three are independent. L148 still puts
epsilon in the rational Kummer subgroup. Nothing here identifies either
of the other two modulo that subgroup or evaluates their mutual pairing.

### Earlier generators, stopping and exact replay

The first four kernel masks are 118,165,296,3109. The first three are
certified contained, so the approved first-outside stop is respected.
Mask 165 equals epsilon literally. For mask 118 divided by eta_class,
the exact rational square root is 1/1188 and the quartic square root is

    s_118=31/15−(361/375)alpha+(74/9375)alpha²+(16/9375)alpha³.

For mask 296 divided by 1, the corresponding roots are 1/522000 and

    s_296=−341/15−(1609/375)alpha+(1211/9375)alpha²+(49/9375)alpha³.

Complete products and ratios are saved in the new certificate. Exact
reduction modulo A verifies s_118²*b_eta=b_118 and s_296²=b_296, and
the rational roots verify the other components. Decimal interpolation
only proposed roots; these identities decide the positive cases. In
reference order 1,epsilon,eta_class,epsilon*eta_class, the comparison
counts for these four generators are 3,2,1,4, totaling 10. The earlier
inequalities and all roots are replayed too. There is no assertion about
the 27 untested generator products.

Reproduction from this notebook:

```bash
python3 scripts/pair-genus-two/surviving_witness_span.py
python3 scripts/pair-genus-two/verify_surviving_witness_span.py
```

Full evidence is in
`scripts/pair-genus-two/surviving-witness-span-certificate.json` and
`scripts/pair-genus-two/surviving-witness-span-verification.json`.
The producer uses power-basis polynomial reduction. The replay imports
no producer code: it uses the accepted maximal-order multiplication
table, an independent triangular inverse basis conversion and determinant
expansion. It reconstructs all tested products and references from the
39 authenticated sources, checks all 31 local-kernel combinations, every
root, all strict integer-square bounds and the four rational-only outside
obstructions. Producer/replay pass 1626/1545 checks with empty failure
lists. Their observed rational coefficient sizes are 278/77 bits against
cap 8192. The numerical proposal stage used 10 patterns total, at most
5 of cap 16 in any one comparison. No Trager shift or fallback candidate
was needed; their caps 32 and 100000 were untouched. No backend probe,
installation, expanded witness pool or renewed covering box occurred.

The initial schema failure is retained in
`scripts/pair-genus-two/surviving-witness-span-initial-schema-failure.json`;
it made zero comparisons. The adapter was corrected for the accepted
model certificate's PASS status and notebook-relative audit JSON paths.
No source input was changed. These exact checks are not formal verification
or themselves a critical proof audit. All prior stops and unfinished
L108 remain preserved. This supplies a new local instance input within
known general methods, not a mathematical advance beyond those sources.

### Separate critical mathematical audit — 2026-10-28

The prior SPECIALIZE gate is
`drafts/literature/2026-10-28-surviving-witness-third-class-audit.md`.
The review accepts exactly the stated finite result, importing the precise
Stoll statements above rather than reproving descent. Both complete
implementations and every load-bearing comparison, product and reference
record were inspected. The independent replay was rerun once: all 1545
checks pass. The independent fixed-domain supplement
`python3 scripts/pair-genus-two/audit_surviving_witness_span.py` passes
590 checks; its full evidence is
`scripts/pair-genus-two/surviving-witness-span-audit.json`.
It imports neither other implementation and performs no witness search.

**Model and support bindings.** Every mathematical JSON binding from the
producer and replay agrees with the current accepted source, including
the prior critical audits. The complete quintic and quartic, polynomial A,
transported order basis and all 64 multiplication constants agree across
L138/L147 and the order certificate. Literal power-basis multiplication
checks each of the sixteen products of basis elements against that table.
Thus the comparisons take place in the specified actual Q×K algebra.
The support is every prime above 2,3,5,11, with precisely the saved seven
indices, not a subset selected by norm alone.

Every one of the 39 entire ordered source records equals its accepted
L140 record and the records at both new odd places in L147. For the first
34, all four coefficients and all 32 valuations agree with the accepted
principal-ideal record. Each outside-S valuation is even. The supplement
also checks the literal principal multiplication matrix, its signed norm
and the entire ideal norm product. These norm checks bind the records;
they do not prove support by themselves. The complete ideal equalities
and absence of primes outside that factor base are imported from the
audited L136/L140 inputs already used by L147. The remaining five records
are exactly −1,2,3,5,11 in K, with rational coordinates their inverse
fourth powers. They are supported directly. In every case the determinant
norm gives q*N(b)=1. Products inherit even valuations outside S in both
factors; this uses the norm valuation formula for the rational component.

**Actual local images and all places.** Accepted complete image generators
in the five places (infinity,11,2,3,5) are respectively

    (30,24), (5), (352,208,404), (7,13), (102,19,68).

The supplement enumerates these five small complete spans and independently
reduces every full witness coordinate to the minimum in its image coset.
All 39 stored quotient columns agree, with exactly the disjoint bit ranges
stated above. It also checks the rational coordinate directly from q at
each place, including the three dyadic bits. The remaining field-coordinate
maps are the exact accepted L147/L145 maps, authenticated in full; the
audit does not substitute an unproved new localization convention.

All 31 saved coefficient vectors are within the 39-column domain,
independent, and zero in the concatenated quotient. The quotient columns
have rank eight, so these are the full coefficient kernel. For each vector
the independently reconstructed five full local coordinates actually
belong to the enumerated complete images, not merely to a claimed zero
mask. In particular nu has full local tuple

    (30,0,324,10,117).

This proves the required local inclusion at every supported place. L138's
monic integral squarefree quintic has polynomial discriminant supported
only at 2,3,5,11. At every other finite place the prime is odd and of good
reduction; supportedness and Stoll Proposition 4.6 give local membership.
Proposition 4.2 then puts nu in the full Selmer group. No assertion that
the 39 witnesses generate the ambient norm kernel or Selmer is used.

**All ten comparisons and stopping.** The supplement reconstructs every
reference and each of the four tested products in the literal alpha power
basis; it uses Gaussian-elimination determinants, independently of the
other implementations' determinant expansion. All four coordinates,
rational components and norms agree, including the printed nu. Mask XOR
represents class multiplication: a repeated source factor is removed by
its square in both Q and K. Thus the reference mask 132259 legitimately
represents epsilon*eta_class even though its chosen representative is
not their literal product. No rational scalar quotient is involved.

For every comparison the reduced rational fraction, both integer-square
floors and full-localization difference are recomputed. The nonzero
differences are full local square-class coordinates, so each proves a
global inequality. Each positive case has exact rational and quartic
roots; direct multiplication root²*b_reference=b_test checks all four
quartic coordinates. This verifies the three earlier containments with
counts 3,2,1. No failed numerical proposal is negative evidence.

All four outside ratios are exactly the four printed reduced fractions.
The strict consecutive-square bounds and nonsquare numerators decide
each independently in Q, hence in Q×K. They therefore prove the four
inequalities even without relying on the corroborating local differences.
The complete ordered domain has ten decisions, no unresolved comparison,
and stops at the fourth saved generator. No later generator product is
tested. L147's accepted two-class independence and nu's exclusion from
their four-element span give exactly the stated three-class independence.
Coefficient-mask independence is not substituted for class independence.

The producer/replay arithmetic sizes remain 278/77 bits; this supplement
uses at most 77/8192 bits. Its domains are 39/39 sources, 31/31 kernel
vectors, 4/4 tested products and 10/10 comparisons, including 4/4 required
outside inequalities, under the original cap 124. Two audit-adapter
failures, before any class-comparison decisions, are preserved in
`scripts/pair-genus-two/surviving-witness-span-audit-initial-schema-failure.json`
and `scripts/pair-genus-two/surviving-witness-span-audit-source-adapter-failure.json`.
They concerned a legacy digest field and the source record's retained
sign fields; neither changed a mathematical input or L149 claim.

This accepts a local instance result within known methods. It supplies
neither a rational Kummer quotient nor a nonzero pairing, exact Selmer
dimension, improved rank bound or point control. Epsilon remains a
rational radical class by L148; eta_class and nu remain undecided modulo
rational Kummer. ATTEMPTS/065–066 and unfinished L108 remain preserved.

## Mathlib

Full matching Mathlib coverage for this fixed Selmer instance and its
class comparisons has not been checked. Unknown availability is not
evidence of absence. The scripts are exact certificates, not Lean proofs.
