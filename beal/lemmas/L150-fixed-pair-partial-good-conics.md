# L150 — Rational-branch conics and partial quartic-pair evidence

## Hypotheses

Use L138's actual odd model, with roots r=9075 and the four conjugates of
eta=−907500/(alpha−50), where

    A(alpha)=alpha^4+64alpha^3+150alpha^2−32500alpha−109375=0.

Use L135's complete maximal-order prime list and basis, and L147/L149's
full Q×K representatives d=(q,b) of eta_class (mask 132102) and nu
(mask 3109). These are actual products in the fixed 39-column order,
without a rational-scalar quotient. The masks are not coefficient values.
Write d_r=q and d_eta=b and transport them by each root embedding.
For the dyadic completion use L145's certified field F=K tensor Q_2,
uniformizer pi=1+beta, maximal order and complete unit-square criterion.
Retain L147/L149's supportedness of both full representatives: valuations
of b at every finite prime outside 2,3,5,11 are even.

The conic convention is Shukla's Section 4.4 convention:

    C_ij: d_j u^2−d_i v^2+(theta_j−theta_i)w^2=0, i!=j.

The projective conic has a point iff its affine chart w=1 has a point
over the fields here: a smooth conic with a point over an infinite field
has infinitely many points by projection from that point, whereas its
intersection with w=0 is finite. No affine point is constructed here.

## Conclusion

For each of these two fixed representatives the following local conics
are soluble:

1. C_(r,eta) at all six completions of K above 3,5,11, namely L135's
   zero-based indices 27,28,29,30,31,1, in that order.
2. C_(eta_i,eta_j) for the simple Q_3 root alpha_i congruent to 2 and
   the other cubic completion (index 27); and for the simple Q_5 root
   alpha_i congruent to 1 and the other completions (indices 29,31).
3. Every real ordered root-pair specialization: twenty per class.
4. C_(r,eta) at the unique dyadic completion of K.

Moreover C_(r,eta) has a K-rational point for each class. This follows
from the complete rational-row local coverage, the outside-support
argument below and the Hasse–Minkowski theorem over number fields.
Existence is proved; explicit K-coordinates are not constructed.

This lemma alone does not prove either class good or not good. Other quartic-pair completions,
exact global root-pair field factorization, outside-support arguments
for those other conics, explicit field solutions and compatible choices
for the whole condition remain unfinished. There is no pairing value,
rank improvement or point-control conclusion. The arithmetic replays
pass; the separate conceptual review below accepts this lemma's scope.

## Proof

### Imported condition, provenance and scope

Import the good-element condition, not its satisfaction, from Himanshu
Shukla, *On computation of the Cassels–Tate pairing*, University of
Bayreuth thesis (2024; repository publication 2025), DOI
[10.15495/EPub_UBT_00008348](https://doi.org/10.15495/EPub_UBT_00008348),
Section 4.4, Assumption 4.4.3 and Proposition 4.4.4, printed pp.109–111,
with Algorithm 2 pp.113–114. The inspected primary text is
[the published thesis](https://epub.uni-bayreuth.de/id/eprint/8348/1/thesis.pdf).
The prior SPECIALIZE assessment is
`drafts/literature/2026-10-29-shukla-good-element-conics.md`.
Testing this condition is known-method specialization, not a new pairing
construction. The printed algorithm's variable/guard inconsistencies are
avoided by using the displayed defining conic throughout.
For the later dyadic and local-global completion, also import the
standard named Hasse–Minkowski theorem over number fields, covered by
the same prior SPECIALIZE assessment: a nondegenerate quadratic form
over a number field is isotropic if and only if it is isotropic at every
completion. Here the ternary diagonal form has all three coefficients
nonzero, so its projective zero set is precisely a smooth conic. No
effective solution-construction theorem is being imported or asserted.

The producer independently reconstructs both products from all selected
columns. In the alpha power basis it obtains

    eta_class: q=1/26730000000000,
      b=41236+(356216/25)alpha+(397568/625)alpha^2+(4612/625)alpha^3;
    nu: q=1/524880000000000000,
      b=90688+(99088/5)alpha−(1403152/625)alpha^2−(33968/625)alpha^3.

The integral-basis replay reconstructs the same entire products and checks
q*N(b)=1 by an independent determinant. The model identification is checked
by (alpha−50)eta=−907500 and the saved quintic. Both norm-one identities
are authentication checks, not conic-solubility criteria.

### Local criterion and the complete finite tested domain

Over a field F of characteristic zero put

    a=d_i/d_j, c=(theta_i−theta_j)/d_j.

The conic is u^2−a v^2=c w^2. It is soluble iff the quaternion (a,c)
splits. If a is a square this is immediate; otherwise this is the norm
criterion for F(sqrt(a))/F. All displayed coefficients are nonzero.

At an odd-residue local field with uniformizer pi and residue F_p,
write a=pi^m u and c=pi^n v with u,v units. If chi is its quadratic
residue character, the sign-valued Hilbert symbol is

    (a,c)=chi(−1)^(mn) chi(u)^n chi(v)^m.                 (1)

For clarity, the standard norm criterion gives (1) with these signs as
follows. Remove even powers, so m,n are 0 or 1. For nonsquare unit a the
quadratic extension is unramified, its norm valuations are even, and all
units are norms. Surjectivity on units follows from the finite-field norm
and Hensel lifting the nonsingular norm form. For square unit a everything
is a norm. For m=1 the extension is ramified with uniformizer sqrt(pi*u),
whose norm is −pi*u. A unit norm has square residue, and every unit of
square residue is already a square by Hensel's lemma, hence a norm.
Dividing c by (−pi*u)^n therefore gives (1). This brief reproduction fixes
the convention essential to the certificate; it is not an original result.

At every tested prime, the residue field is F_p, including the ramified
primes. The exact integral prime lattices come from L135, not factoring a
nonmaximal polynomial order. The certificate supplies all required powers
P^k with two-way containment witnesses and determinant p^k. The replay
checks these containments by Gaussian rational coordinates and checks the
uniformizer belongs to P but not P^2. For an integral element z, its
valuation t is certified by z in P^t and z not in P^(t+1). The normalized
residue h is certified by z−h*pi^t in P^(t+1). Rational denominators are
removed using the fully computed local class of p and their unit residues.
Thus these are complete local square classes, not approximate residues.

Encode a class by m mod 2 + 2*(nonsquare unit residue bit). The rational-row
pair (class(a),class(c)) is, in prime order 27,28,29,30,31,1:

| Class | P27 | P28 | P29 | P30 | P31 | P1 |
|---|---|---|---|---|---|---|
| eta_class | (0,0) | (1,0) | (3,0) | (0,0) | (3,0) | (1,0) |
| nu | (0,3) | (2,0) | (2,0) | (0,1) | (3,0) | (0,3) |

All twelve symbols in (1) are +1. For this row, a=q/b and
c=(9075−eta)/b; the replay verifies both full coefficient identities after
multiplying by b. This proves conclusion 1 for precisely those places.

### Three additional quartic-pair completions per class

Modulo 3, alpha_i=2 is a simple root of A, and modulo 5, alpha_i=1
is simple. The full 23-step Hensel traces give roots to precision p^24,
with exact evaluation divisibility and unit derivatives at every step.
Hensel's lemma gives unique exact roots in those residue disks. Let t
be the saved rational integral approximation to alpha_i. Substitute t in
the exact b and eta polynomials, and substitute the actual alpha_j in
the indicated second completion. The approximate coefficients are

    a_t=b(t)/b(alpha_j), c_t=(eta(t)−eta(alpha_j))/b(alpha_j).

All second-root gaps t−alpha_j have valuation zero, certified in the
prime lattices. Thus these are distinct branches, not the diagonal.
The simple-root completions are Q_p; hence the specified pairs give actual
local specializations of the root-pair algebra, without requiring its
global factorization for these particular tests.

For any polynomial h with rational coefficients and integral arguments,
the difference h(t)−h(alpha_i) has p-adic valuation at least
24+min_k v_p(h_k), by factoring each difference of powers. In a second
completion of ramification e, division by b(alpha_j) therefore leaves
error valuation at least

    e*(24+min_k v_p(h_k))−v_P(b(alpha_j)).                 (2)

Use h=b for a_t and h=eta for c_t. The certificate and independent replay
verify that (2) strictly exceeds the valuation of the respective computed
coefficient in every case. The exact coefficient and its approximation
therefore have the same leading normalized residue and square class at
these odd places. This strictness check failed at precision 12 for nu;
the retained failed certificate was not accepted as evidence. Precision
24 passes all six coefficient comparisons per class.

The resulting pairs of square-class masks, in order P27 at 3 and P29,P31
at 5, are eta_class: (1,3),(3,0),(3,0), and nu: (2,0),(2,0),(3,0).
Equation (1) gives +1 in all six tests, proving conclusion 2. The first
case for eta_class uses chi_3(−1)=−1 as well as both residue bits; omitting
that sign would give an erroneous negative result.

### All real pairs

The four disjoint intervals (−48,−47),(−34,−33),(−4,−3),(20,21)
each have opposite endpoint signs of A. Since A has degree four, they
exhaust its distinct roots. Refine each by 32 exact bisections. Exact
interval evaluation proves b>0 at every root for eta_class, and b<0
at every root for nu. Both rational q are positive. The function
eta=−907500/(alpha−50) is strictly increasing on these intervals and
all four eta are strictly greater than r=9075. The saved polynomial
intervals also independently certify every ordering comparison.

For eta_class the first two conic coefficients have opposite signs for
any pair. For nu they have opposite signs on a quartic/quartic pair.
On a rational/quartic pair the two quadratic coefficients are negative
and the constant positive; reversing the pair negates this pattern after
interchanging variables. Every real conic is thus nondegenerate and
indefinite, so has a real point. The certificate checks all twenty ordered
pairs per class, proving conclusion 3. These include every real embedding
of any eventual root-pair field because all roots are real and all ordered
pairs were checked.

### Dyadic rational-root row — completion of 2026-10-29

Reuse L145's actual field, not a polynomial-order approximation:

    F=Q_2[pi], E(pi)=pi^4−64pi^3+1272pi^2−8442pi+5850=0,
    v_F(pi)=1, v_F(2)=4, O_F=Z_2[pi].

The monic Eisenstein polynomial identifies the whole degree-four
completion, so there is exactly one place above two. L145 certifies
both full basis changes and all squares of units modulo pi^9. Its
Local Square Theorem input is Pete L. Clark, *Algebraic Number Theory
II: Valuations, Local Fields and Adeles*, author-hosted 161-page notes,
[Proposition 2.20 p.72 and Theorem 2.24/full proof p.73](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
in the version inspected for L145. In this field a unit is a square
exactly when its residue modulo pi^9 is a unit-square residue. The
strict Hensel inequality v(f(s))>2v(f'(s)) supplies the root in the
complete DVR; the calculations below verify it rather than assume
that a truncated residue is itself an exact root.

Reconstruct q,b from the selected 39 columns in the pi basis. Transport
L150's a=q/b and c=(9075−eta)/b through the full alpha-to-pi map and
check a*b=q and c*b=9075−eta coefficientwise. This authenticates the
actual coefficients, with no quotient by rational scalars. Put

    k_a=floor(v_F(a)/2), k_c=floor(v_F(c)/2),
    a_0=a*pi^(−2k_a), c_0=c*pi^(−2k_c).

Both normalized coefficients are integral with valuations zero or one.
Solve U^2−a_0 V^2=c_0. The original variables are
u=pi^k_c U, v=pi^(k_c−k_a)V, w=1, since the original equation then
equals pi^(2k_c)(U^2−a_0V^2−c_0). This is an exact change of variables
over F; negative scaling exponents are allowed.

For an exact proposed V, write h=a_0 V^2+c_0. If v_F(h)=2m, normalize
to h*pi^(−2m) and take a unit s whose square has that same residue
modulo pi^9. Then U_0=pi^m s has

    v_F(U_0^2−h)>=2m+9>2(4+m)=2v_F(2U_0).

For the following actual tests m>=0, so the polynomial Z^2−h and its
approximate root are integral, and Hensel applies directly. The saved
full residuals have the exact valuations in the last two columns:

| Class | v(a) | v(c) | V | U_0 | v(h) | v(U_0^2−h) | 2v(2U_0) |
|---|---:|---:|---|---|---:|---:|---:|
| eta_class | −50 | −10 | pi^4 | 1+pi^2 | 0 | 11 | 8 |
| nu | −80 | −16 | 1 | pi^4 | 8 | 17 | 16 |

For eta_class the normalized h unit residue is 465 with digit root 5
(1+pi^2); for nu it is 1 with digit root 1. The producer checks all
256 unit-squaring rows and all eight saved residue roots, not just these
two. Hensel gives an exact U with U^2=h, proving both local conics
soluble. The displayed U_0 are approximations, not exact global or
local coordinates; the existence of U is the theorem's conclusion.

The fixed search domain was V=pi^k sum_(j=0)^8 d_j pi^j, for
k in the order 0,1,−1,2,−2 and all 512 binary digit vectors in numerical
order. It stopped at digit 16 (17 candidates) and digit 1 (2 candidates),
respectively, in the first k=0 block. Rejected candidates are only
failed values of this V, never conic-insolubility evidence. The domain
cap was 2560 per class; only 19 candidates total were needed.

### Complete rational-branch local-global existence

L138's monic H makes eta an algebraic integer. Consequently
g=9075−eta is integral, and its exact norm is

    N_K/Q(g)=H(9075)=73990352390625=3^5*5^6*11^7.

For a finite prime P of K above p outside 2,3,5,11, integrality gives
v_P(g)>=0. The norm formula v_p(N(g))=sum_(P|p) f_P v_P(g)=0,
with all f_P positive and summands nonnegative, forces v_P(g)=0.
Both q have numerator one, with complete denominator factorizations

    eta_class: 2^10*3^5*5^10*11,
    nu:        2^16*3^8*5^13.

Thus v_P(q)=0. L147/L149's full supportedness, proved using principal
ideal equalities rather than norms alone, gives v_P(b) even. It follows
that v_P(a)=−v_P(b) and v_P(c)=−v_P(b) are even. Remove square powers
of a uniformizer from both entries of the quaternion (a,c). At this
odd-residue place the remaining entries are units, so the Hilbert
symbol is +1: if the first unit is nonsquare its quadratic extension
is unramified, and every unit is a norm; if it is square splitting is
immediate. This uses precisely the standard odd local norm criterion
already reproduced above and works for every residue degree.

This proves solubility at every finite place outside the support for
these rational-row conics. L135's six prime completions at 3,5,11 were
all tested above, and the dyadic section covers the unique place at two.
The four real embeddings were all tested above. K is totally real by
the exhaustive four-root brackets; complex places in any case impose
no obstruction. All completions are therefore covered. Each conic is
nondegenerate since q,b and 9075−eta are nonzero. Hasse–Minkowski gives
a K-rational projective point, and the infinite-field argument in the
hypotheses gives an affine point with w=1.

This proves existence for the rational-first-root orbit only. A selected
K-point could be transported to its conjugates, and exchanging u,v and
negating the equation handles reversed pairs. No such explicit global
point is supplied here, and pairs of two distinct quartic roots still
require their own fields and tests. Selmer membership was used only
through its already-certified supported representatives, never as an
assumption that these stronger conics all split.

### Evidence, unfinished boundary and reproducibility

Run `python3 scripts/pair-genus-two/shukla_good_conics.py`, then
`python3 scripts/pair-genus-two/verify_shukla_good_conics.py`.
The full coefficient, lattice, root and interval evidence is in
`scripts/pair-genus-two/shukla-good-conics-certificate.json`.
The independent integral-basis replay is
`scripts/pair-genus-two/shukla-good-conics-verification.json`: 975 direct
checks plus 148629 helper checks, no failures, 18 odd tests and 40 real
ordered-pair tests. Maximum saved prime depth is 26 against cap 64;
saved rational size is 4874 bits against cap 8192; root precision is
24 against cap 24. These checks authenticate this partial domain only.

The initial index, variable-shadowing and insufficient-precision failures
remain in `scripts/pair-genus-two/shukla-good-conics-initial-*-failure.json`.
None is a negative conic certificate. No larger search or changed target
is inferred from their correction.

For the added dyadic evidence run
`python3 scripts/pair-genus-two/shukla_dyadic_conics.py`, then
`python3 scripts/pair-genus-two/verify_shukla_dyadic_conics.py`.
The complete coefficient/residual and outside-support arithmetic is in
`scripts/pair-genus-two/shukla-dyadic-conics-certificate.json`; its
independent maximal-order-basis replay is
`scripts/pair-genus-two/shukla-dyadic-conics-verification.json`.
The producer uses pi convolution and weighted valuations. The replay
uses O multiplication and repeated division by pi, rebuilds both entire
products, tests the whole residue table and all 19 candidate decisions,
checks every successful residual coefficient and the exact coordinate
transport, and independently computes the gap norm and both complete
rational denominator factorizations. It passes 1189 direct checks and
7630 helper checks, with no failures. Producer/replay rational sizes are
642/551 bits against cap 8192; unit precision is 9/9 and the tested
domain is 19 candidates out of at most 2560 per class. No hidden point
search or field backend is used.
The initial replay string-zero parsing failure is preserved in
`scripts/pair-genus-two/shukla-dyadic-conics-initial-string-zero-failure.json`;
it occurred before any conic decision and is not mathematical evidence.

The remaining quartic-pair conics have no complete all-place proof here.
There is no explicit global conic solution, whole good-element decision,
rational Kummer decision, pairing, rank improvement, marked recovery or
Beal conclusion. The newly established rational-row existence is local
progress by standard theorems, not progress beyond the cited methods.

### Separate conceptual audit — 2026-10-29

The approved audit in
`drafts/literature/2026-10-29-complete-conic-existence-audit.md` accepts
the rational-branch existence claim and the stated partial pair tests.
The complete replay was rerun: 975 direct/148629 helper checks for
the odd and real evidence, and 1189 direct/7630 helper checks for the
dyadic evidence, with no failures. Both full representatives, all saved
ideal-power containments and normalized residues, every Hensel digit,
the full dyadic square table and successful residuals were checked by
the reviewed independent programs; no preview was treated as evidence.

L135 supplies all the relevant maximal-order primes. Their local
degrees are 3+1 at three, 1+1+2 at five and 4 at eleven; all residue
degrees here are one. The tested index lists therefore omit no K-place
above these primes. The simple roots 2 modulo three and 1 modulo five
are different from the tested second-root components. The strict error
bounds preserve the full leading unit, not just valuation parity. The
odd Hilbert formula includes its minus-one factor at three.

L145's Eisenstein field is the entire dyadic completion. In the two
successful dyadic cases the Hensel inequalities are respectively 11>8
and 17>16, with integral inputs. The four disjoint real root intervals
exhaust K's embeddings; all twenty ordered real pairs per class were
checked. The outside-support step uses integrality and the supported
norm of the root gap to prove that gap is a unit at each prime, but
uses L147/L149's principal-ideal supportedness for b. It does not infer
the parity of b from its norm. The rational components are units there.
Consequently both quaternion entries have even valuation at every
remaining odd place.

The precise imported local-global reference is John Voight,
*Quaternion Algebras*, GTM 288 (2021),
[Theorem 14.6.9](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_14).
For the odd local input over arbitrary finite extensions use
[Section 12.4.8–12.4.12](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_12),
also Voight, *Identifying the matrix ring*, author version 2019-05-21,
[Proposition 5.5 and proof, p.21; Theorem 6.11, p.27](https://jvoight.github.io/articles/quatalgs-051919.pdf).
The three diagonal coefficients are nonzero: the norm-one identity
makes b and q nonzero, and H(9075) is nonzero. Thus the complete place
coverage and smoothness hypotheses justify Hasse–Minkowski over K.
Projection from its resulting point justifies the affine passage.
No new coordinates or pairing are asserted by this acceptance.

## Mathlib

Full matching coverage for this instance and Shukla's good-element test
was not checked. The scripts are rational arithmetic certificates, not
Lean proofs. Unknown matching coverage is not evidence of absence.
