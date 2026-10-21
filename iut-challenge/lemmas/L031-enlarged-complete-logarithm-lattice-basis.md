# L031 — Exact enlarged unit-logarithm lattice basis

## Hypotheses

Fix an algebraic closure of Q_3, a primitive twentieth root zeta_20,
and pi with pi^27=3. Set U=Q_3(zeta_20), L=U(pi),
theta=zeta_20^4, O=O_L, J=log(O^times), and H=pi^14 O.
Normalize v_3(3)=1. Log is the ordinary continuous unit logarithm,
killing unit torsion and given on principal units by its convergent series.
No O_U-module structure on J is assumed.

L030 supplies the audited field model: U is unramified of degree four,
L/U is Eisenstein of degree 27, and O=O_U[pi]. Its scalar-transport
failure is preserved. L016's filtration/certificate method is reused,
but neither its old representatives nor its numerical separator is an
input to this computation.

Import **Pete L. Clark, Algebraic Number Theory II: Valuations, Local
Fields and Adeles**, undated author-hosted 161-page version inspected
2026-10-08, **Proposition 2.5/Corollary 2.6**, pp. 63–64,
**Proposition 2.9/Corollary 2.10**, p. 65, and **Proposition 2.30**,
pp. 76–77 ([primary notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf)).
These supply the integral unramified/Eisenstein models and order-preserving
prime-to-3 torsion lifting. Import the principal-unit quotients from
**Hess–Pauli–Pohst, Computing the Multiplicative Group of Residue Class
Rings**, undated author-hosted 18-page manuscript, **section 3,
Theorems 3.1/3.3 and case-I proof**, pp. 3–5, and the inverse deep
log/exp theorem from **Proposition 5.1(i,iii–iv)**, pp. 9–10
([primary manuscript](https://page.math.tu-berlin.de/~kant/publications/papers/hepapo.pdf)).
These general inputs are cited, not reproved. The specialization has
absolute ramification e=27, residue degree f=4, and deep depth 14>27/2;
Theorem 3.3's case-I alternative holds since 2 does not divide 27.
The manuscript's number-field formulation applies by completing
Q(pi,zeta_20) at the place fixed by the chosen algebraic closure.
Only its unit-filtration and deep analytic inputs are required here.

For logarithm additivity import **Keith Conrad, Infinite Series in
p-Adic Fields**, undated author-hosted 42-page version inspected in the
2026-10-08 source comparison, **Theorem 8.5**, pp. 27–28; for continuity
and convergent-series valuation bounds use **Corollary 3.14**, p. 14,
and **Theorem 2.1**, pp. 1–2
([primary notes](https://kconrad.math.uconn.edu/blurbs/gradnumthy/infseriespadic.pdf)).
Theorem 8.5 applies to principal units in the complete field L, where
both |x-1| and |y-1| are strictly less than one. The extension to all
units is justified below. Compactness of O follows from **Clark,
Theorem 2.15**, p. 69, since L is a finite extension of Q_3.
The suspect extracted formula in HPP Proposition 5.1(ii) is not used.

## Conclusion

The 108 elements b_(r,a), 0<=r<=26 and 0<=a<=3, in the table below
form an exact **Z_3-basis of the complete J**. In the common coordinate
order theta^a pi^r, index 4r+a, their matrix is B_int/9, where
`/integer_basis_matrix` of `scripts/cyclotomic-log/enlarged-basis.json`
stores every integer entry of B_int, with rows and columns in that order.
The table lists columns, rather than asserting that its four columns
are scalar multiples over O_U.

The determinant has v_3 equal to 4 relative to this integral basis of O.
The minimum field valuation on J minus {0} is -2, attained by b_(9,0).
This determinant is a covolume datum, not an index assertion for nested
O and J. No action, orbit radius, packet admissibility, original input,
pilot transport or essential IUT flaw is established. The result is a
known-method **REPRODUCTION**, validated by the separate critical audit below.

## Proof

### Exact unramified coefficient model

Theta has order five and satisfies Phi_5(X)=X^4+X^3+X^2+X+1.
Its reduction has order five by the cited torsion theorem. Frobenius
has orbit length ord_5(3)=4, since 3,9,27,81 reduce to 3,4,2,1
modulo five. Hence Phi_5 is irreducible over F_3. It is separable:
X^5-1 has derivative 5X^4, relatively prime to X^5-1 in characteristic
three, so its Phi_5 factor is square-free.

For an additional exact polynomial certificate, reduction modulo Phi_5
gives X^81=X and X^9=2+2X+2X^2+2X^3 over F_3.
The Euclidean remainders for gcd(Phi_5,X^9-X) are
1+2X^2, 1, 0; those for gcd(Phi_5,Phi_5') are X+2X^2, 1, 0.
The full divisions are stored under `/field_checks` and checked exactly.

The cited unramified integral-model theorem therefore gives
O_(Q_3(theta))=Z_3[theta], with basis 1,theta,theta^2,theta^3.
It is a subfield of U with degree four, so equals U. Thus

    O = direct-sum_(r=0)^26 direct-sum_(a=0)^3 Z_3 theta^a pi^r.

For c=sum_a c_a theta^a in U, v_3(c)=min_a v_3(c_a): after dividing
by the least rational coefficient valuation, residue-basis independence
prevents cancellation. For y=sum_r c_r pi^r, the fractional parts r/27
are distinct, so v_3(y)=min_r(v_3(c_r)+r/27). Consequently

    H = direct-sum_(r,a) 3^(d_r) Z_3 theta^a pi^r,
    d_r=1 for r<14 and d_r=0 for r>=14.

This proves the coordinate model and the full deep-ideal basis used below.
It imposes no O_U-stability on J.

### Complete unit generation and both image containments

Write U_j=1+pi^j O. The cited principal-unit quotient theorem identifies
U_j/U_(j+1) with the additive residue field F_81, whose F_3-basis
is the reduction of 1,theta,theta^2,theta^3. For each j=1,...,13 the
classes of 1+theta^a pi^j, a=0,...,3, are therefore a basis of that
quotient. Removing the four classes at each successive layer gives
every u in U_1 as

    u = product_(j=1)^13 product_(a=0)^3
        (1+theta^a pi^j)^(epsilon_(j,a)) * u_14,
    epsilon_(j,a) in {0,1,2}, u_14 in U_14.

This is a finite layer-removal argument: products modulo pi^(j+1)
add the leading coefficients because 2j>=j+1. It uses all four
residue directions and all thirteen shallow depths.

The residue-unit group has order 80. Henselian prime-to-3 torsion lifting
gives a representative in mu_80 for every residue unit. Such torsion
has logarithm zero. The lift gives the unique decomposition
O^times=mu_80 times U_1: reduction is an isomorphism on mu_80, so its
intersection with U_1 is trivial. The residue-unit part is locally
constant. Extending the principal-unit logarithm by zero on mu_80 is
therefore continuous; Conrad's Theorem 8.5 makes it an additive
homomorphism on this commutative product. Thus all units, including
the residue-unit part, are covered by the displayed reduction.
The cited deep inverse theorem applies strictly at 14/27>1/2,
giving log(U_14)=H. The unit group is a closed subset of the compact
O (the maximal ideal is open), so J is compact, hence closed in L.
Being an additive subgroup, J is closed under integer multiplication.
For lambda in Z_3 and x in J, choose integers n_i converging to lambda;
then n_i x converges to lambda x in L, which lies in J by closedness.
This proves Z_3-stability without asserting O_U-stability. Therefore

    J = H + sum_(j=1)^13 sum_(a=0)^3 Z_3 log(1+theta^a pi^j).

The forward inclusion follows from complete unit reduction; the reverse
inclusion follows because every shallow logarithm and every element of H
is a genuine unit logarithm and J is Z_3-stable. These are separate
containments, not an assumption of residue-field linearity.

### Complete infinite tails and rational representatives

For every j,a set

    S_(j,a) = sum_(k=1)^242 (-1)^(k+1) theta^(ak) pi^(jk)/k.

Each theta^(ak) is a unit. For 3^h<=k<3^(h+1), h>=5, the
integer pi-valuation of each omitted term is

    jk-27 v_3(k) >= 3^h-27h.

At h=5 this is 108>=14. Its increment is 2*3^h-27>0,
and it tends to infinity. Thus the entire omitted infinite series,
for each of the 52 logarithms, converges in the closed ideal H.
This bound handles shallow inputs directly and does not use HPP
Remark 5.2 outside its deep-input hypothesis.

Here is an explicit formula for every finite rational coordinate.
For t modulo five let eta_(t,b)=1 if t=b<4, zero for the other b<4,
and eta_(4,b)=-1 for all b=0,...,3. Then theta^t=sum_b eta_(t,b)theta^b.
For 0<=r<=26, 0<=b<=3,

    s_(j,a,r,b) = sum_(1<=k<=242, jk congruent r mod 27)
        (-1)^(k+1) 3^((jk-r)/27) eta_(ak mod 5,b)/k.

The coefficient vector of S_(j,a) is precisely s_(j,a,r,b).
Every such rational coefficient has v_3>=-2. To see this without a
precision assumption, the minimum of 3^h-27h for h>=0 is -54,
at h=3; the values for h=0,1,2,3,4 are 1,-24,-45,-54,-27,
and the increments are positive from h=3 onward. Thus every series
term has pi-valuation at least -54. Equivalently, in the above coordinate
formula each nonzero term has rational valuation at least -2, since
(jk-r)/27-v_3(k) is an integer greater than -3. Sums preserve this bound.

Reduce 9s_(j,a,r,b), which is 3-integral, modulo 3^(d_r+2), using
the inverse of its denominator prime to three. Let n_(j,a,r,b) be
the canonical residue in {0,...,3^(d_r+2)-1}, and define

    q_(j,a) = sum_(r,b) (n_(j,a,r,b)/9) theta^b pi^r.

The exact rule gives v_3(s_(j,a,r,b)-n_(j,a,r,b)/9)>=d_r.
Together with the tail bound this proves
log(1+theta^a pi^j)-q_(j,a) in H. In particular every q_(j,a)
belongs to J, by subtraction of an element of H from a genuine log.
Conversely every shallow log belongs to H+sum Z_3 q_(j,a).
We have therefore proved the exact complete-image equality

    J = H + sum_(j=1)^13 sum_(a=0)^3 Z_3 q_(j,a).

All 52 finite vectors and all 5,616 rational congruences are stored in
the certificate, under `/finite_sums`, `/representatives` and
`/congruence_valuations`. None is inferred from a precision label.

### Exact basis and both integral span certificates

Let G be the 108-by-160 rational matrix whose first 52 columns are
q_(j,a), ordered by increasing j and then a, followed by all 108 columns
3^(d_r)theta^a pi^r of H, ordered by r and then a. Put M=9G.
Every entry of M is an integer by the explicit residue rule above.

The calculation uses integer column operations from the standard
Hermite normal-form method, keeping their full transformation V and
inverse V_inv. A two-column operation replaces columns i,j by
u col_i+v col_j, w col_i+z col_j, with uz-vw=1; sign changes and
integer column additions also have determinant a unit. These preserve
the integer column span in both directions, and hence its Z_3-span.
The precise sequence of 1,699 operations is stored, but the proof
also checks the resulting complete identities directly.

Let W be the last 108 columns of V and C the last 108 rows of V_inv.
The complete stored matrices satisfy, entry by entry,

    M V = [ 0_(108 by 52)  B_int ],    V V_inv = I_160,
    M W = B_int,                     B_int C = M.

All entries of W and C are integers. B_int is upper triangular with
positive diagonal; hence it has rank 108. In detail its diagonal
valuations are: eight entries of valuation 0, sixteen of valuation 1,
forty-eight of valuation 2, and thirty-six of valuation 3.
Their sum is 220, so v_3(det(B_int/9))=220-216=4.

Dividing M W=B_int by nine shows that every basis column belongs to
the Z_3-span of the complete genuine-image generators. Dividing
B_int C=M by nine gives the reverse inclusion for **every** generator.
Together with the proved complete-image equality this identifies
J=(B_int/9)Z_3^108. Nonzero determinant gives uniqueness of basis
coordinates, so these columns are a basis, not just generators.

For reproducibility run:

    python3 scripts/cyclotomic-log/compute_enlarged_basis.py
    python3 scripts/cyclotomic-log/compute_enlarged_basis.py --verify

The second command reads the saved full certificate, recomputes all
52 finite sums from their defining series, all representatives, all
5,616 congruences and all 160 generator columns, then multiplies the
full stored matrices to verify both span identities, the transformation
and its inverse, every rank condition and complete agreement of the
displayed basis table with the matrix certificate. Its evidence is stored in
`scripts/cyclotomic-log/enlarged-basis-verification.json`. Both runs have
zero failures. Their finite checks do not substitute for the complete
unit-generation and infinite-tail proofs above.

### Explicit basis table and valuation qualification

The following is the full basis. A product such as `theta pi^3`
means multiplication in L. The indexed column b_(r,a) has last nonzero
coordinate theta^a pi^r, consistent with the triangular certificate.

| r | b_(r,0) | b_(r,1) | b_(r,2) | b_(r,3) |
| --- | --- | --- | --- | --- |
| 0 | 3 | 3 theta | 3 theta^2 | 3 theta^3 |
| 1 | 3 pi | 3 theta pi | 3 theta^2 pi | 3 theta^3 pi |
| 2 | 3 pi^2 | 3 theta pi^2 | 3 theta^2 pi^2 | 3 theta^3 pi^2 |
| 3 | 3 pi^3 | 3 theta pi^3 | 3 theta^2 pi^3 | 3 theta^3 pi^3 |
| 4 | 3 pi^4 | 3 theta pi^4 | 3 theta^2 pi^4 | 3 theta^3 pi^4 |
| 5 | 3 pi^5 | 3 theta pi^5 | 3 theta^2 pi^5 | 3 theta^3 pi^5 |
| 6 | 3 pi^6 | 3 theta pi^6 | 3 theta^2 pi^6 | 3 theta^3 pi^6 |
| 7 | 3 pi^7 | 3 theta pi^7 | 3 theta^2 pi^7 | 3 theta^3 pi^7 |
| 8 | 3 pi^8 | 3 theta pi^8 | 3 theta^2 pi^8 | 3 theta^3 pi^8 |
| 9 | 4/9 + 1 pi + 1/3 pi^3 + 1/9 pi^9 | 8/3 + 8/3 theta + 8/3 theta^2 + 25/9 theta^3 + 2 pi + 2 theta pi + 2 theta^2 pi + 2 theta^3 pi + 1/3 theta^2 pi^3 + 1/9 theta pi^9 | 1/9 theta + 1/3 theta^3 + 1 theta^3 pi + 8/3 pi^3 + 8/3 theta pi^3 + 8/3 theta^2 pi^3 + 8/3 theta^3 pi^3 + 1/9 theta^2 pi^9 | 26/9 + 26/9 theta + 2/9 theta^2 + 26/9 theta^3 + 1 theta^2 pi + 1/3 theta pi^3 + 1/9 theta^3 pi^9 |
| 10 | 1 pi^3 + 1 pi^10 | 1 theta^3 pi^3 + 1 theta pi^10 | 1 theta pi^3 + 1 theta^2 pi^10 | 2 pi^3 + 2 theta pi^3 + 2 theta^2 pi^3 + 2 theta^3 pi^3 + 1 theta^3 pi^10 |
| 11 | 1 pi^6 + 1 pi^11 | 1 theta^3 pi^6 + 1 theta pi^11 | 1 theta pi^6 + 1 theta^2 pi^11 | 2 pi^6 + 2 theta pi^6 + 2 theta^2 pi^6 + 2 theta^3 pi^6 + 1 theta^3 pi^11 |
| 12 | 5/3 + 2 pi^3 + 1 pi^4 + 1/3 pi^12 | 1/3 + 1/3 theta + 7/3 theta^2 + 1/3 theta^3 + 2 theta pi^3 + 1 theta^2 pi^4 + 1/3 theta pi^12 | 1 + 1 theta + 1 theta^2 + 2/3 theta^3 + 2 theta^2 pi^3 + 2 pi^4 + 2 theta pi^4 + 2 theta^2 pi^4 + 2 theta^3 pi^4 + 1/3 theta^2 pi^12 | 2 theta + 8/3 theta^2 + 2 theta^3 pi^3 + 1 theta pi^4 + 1/3 theta^3 pi^12 |
| 13 | 1 + 1 pi^13 | 1 theta^2 + 1 theta pi^13 | 2 + 2 theta + 2 theta^2 + 2 theta^3 + 1 theta^2 pi^13 | 1 theta + 1 theta^3 pi^13 |
| 14 | 1 pi^14 | 1 theta pi^14 | 1 theta^2 pi^14 | 1 theta^3 pi^14 |
| 15 | 2 + 1 pi^5 + 2 pi^6 + 1/3 pi^15 | 1 + 1 theta + 1 theta^2 + 1 theta^3 + 1 theta^2 pi^5 + 2 theta pi^6 + 1/3 theta pi^15 | 2 theta^3 + 2 pi^5 + 2 theta pi^5 + 2 theta^2 pi^5 + 2 theta^3 pi^5 + 2 theta^2 pi^6 + 1/3 theta^2 pi^15 | 2 theta^2 + 1 theta pi^5 + 2 theta^3 pi^6 + 1/3 theta^3 pi^15 |
| 16 | 1 pi^16 | 1 theta pi^16 | 1 theta^2 pi^16 | 1 theta^3 pi^16 |
| 17 | 1 pi^17 | 1 theta pi^17 | 1 theta^2 pi^17 | 1 theta^3 pi^17 |
| 18 | 1/3 + 1 pi^2 + 1/3 pi^6 + 1/9 pi^18 | 1/3 theta^3 + 2 pi^2 + 2 theta pi^2 + 2 theta^2 pi^2 + 2 theta^3 pi^2 + 1/3 theta^2 pi^6 + 1/9 theta pi^18 | 1/3 theta + 1 theta^3 pi^2 + 8/3 pi^6 + 8/3 theta pi^6 + 8/3 theta^2 pi^6 + 8/3 theta^3 pi^6 + 1/9 theta^2 pi^18 | 8/3 + 8/3 theta + 8/3 theta^2 + 8/3 theta^3 + 1 theta^2 pi^2 + 1/3 theta pi^6 + 1/9 theta^3 pi^18 |
| 19 | 1 pi^19 | 1 theta pi^19 | 1 theta^2 pi^19 | 1 theta^3 pi^19 |
| 20 | 1 pi^20 | 1 theta pi^20 | 1 theta^2 pi^20 | 1 theta^3 pi^20 |
| 21 | 2 + 1 pi^7 + 1/3 pi^21 | 1 + 1 theta + 1 theta^2 + 1 theta^3 + 1 theta^2 pi^7 + 1/3 theta pi^21 | 2 theta^3 + 2 pi^7 + 2 theta pi^7 + 2 theta^2 pi^7 + 2 theta^3 pi^7 + 1/3 theta^2 pi^21 | 2 theta^2 + 1 theta pi^7 + 1/3 theta^3 pi^21 |
| 22 | 1 pi^22 | 1 theta pi^22 | 1 theta^2 pi^22 | 1 theta^3 pi^22 |
| 23 | 1 pi^23 | 1 theta pi^23 | 1 theta^2 pi^23 | 1 theta^3 pi^23 |
| 24 | 1 pi^8 + 1/3 pi^24 | 1 theta^2 pi^8 + 1/3 theta pi^24 | 2 pi^8 + 2 theta pi^8 + 2 theta^2 pi^8 + 2 theta^3 pi^8 + 1/3 theta^2 pi^24 | 1 theta pi^8 + 1/3 theta^3 pi^24 |
| 25 | 1 pi^25 | 1 theta pi^25 | 1 theta^2 pi^25 | 1 theta^3 pi^25 |
| 26 | 1 pi^26 | 1 theta pi^26 | 1 theta^2 pi^26 | 1 theta^3 pi^26 |

Every coordinate term in this full table has field valuation at least -2.
The coefficient 4/9 of b_(9,0) has valuation -2, while its other terms
have strictly larger valuation. Thus b_(9,0) has valuation -2, and
the ultrametric inequality proves the lower bound -2 for every nonzero
Z_3-linear combination. This establishes the stated minimum on J.
It gives no radius for an action group on a shell or on an actual input.

The prior SPECIALIZE assessment approves this exact calculation as a
specialization of known unit/lattice methods. It supplies no new general
logarithm theorem, and no claim of progress beyond the sources checked.
L030's stopped scalar transport, the unchanged packet's realization
stop, native/actual inputs, action compatibility, pilot transport,
global realization, essentiality and the original finite B>=A gap
remain unresolved or preserved as appropriate.

### Separate critical audit, 2026-10-08

The audit validates this local result under precisely the stated field
and ordinary-logarithm hypotheses. It imports the already inspected
Conrad additivity/continuity and Clark compactness results above,
replacing an implicit standard-logarithm input with precise citations.
No extracted HPP multiplicative formula is used for additivity.

The analytic review checks all cases: theta's order and degree identify
U and its integral basis; the valuation formula gives every coordinate
of H; all residue units and all four directions at every shallow depth
are removed before applying log(U_14)=H. The strict inequality is
14/27>1/2, not an endpoint assertion. For every omitted k>=243 there
is an h>=5 with 3^h<=k<3^(h+1), and v_3(k)<=h. Hence the bound
jk-27v_3(k)>=3^h-27h applies to every j>=1 and every theta^a.
Its initial value 108 exceeds 14, its increments are positive, and
it tends to infinity; convergence in the closed ideal controls the
entire remainder. For every finite coefficient, the term bound -54
in pi-valuation gives an integer rational-coordinate valuation >-3,
hence at least -2, as used in the exact residue rule. These arguments
cover all 52 series; checking finitely many omitted terms is unnecessary.

Run the independent saved-certificate audit:

    python3 scripts/cyclotomic-log/audit_enlarged_basis.py

It imports no builder code. Repeated multiplication by theta using
Phi_5 and by pi using pi^27=3 recomputes all 52 finite series, all
5,616 coordinate congruences and all 160 generator columns. Independent
dot products check M W=B_int, B_int C=M, the full transformation,
and both products of its inverse. Complete shape/integrality checks
exclude an implicit rational-span substitution. The canonical table is
parsed independently into all 108 columns and compared entry by entry.
The original saved-evidence verifier was also rerun after its scope
was inspected. Both checks have zero failures; full independent evidence
is in `scripts/cyclotomic-log/enlarged-basis-independent-audit.json`.

The positive upper-triangular diagonal gives rank 108; its valuation
sum is 220 and division of each of 108 columns by 9 subtracts 216,
giving determinant valuation 4. Every basis term has valuation at least
-2. For b_(9,0), the four term valuations are -2, 1/27, -8/9 and
-5/3, so the unique least term attains -2 without cancellation.
Integral linear combinations cannot have a smaller valuation. This
proves the claimed minimum on J and the covolume interpretation;
neither is promoted to an action radius or a nested-lattice index.

This is verification of a known-method local reproduction, not a new
general result or a candidate IUT flaw. No new lemma input is used:
L030 supplies the field model; L016 remains method comparison only.

## Mathlib

Full matching rank-108 logarithm-basis result: **not checked**.
Supporting unramified/Eisenstein models, torsion lifting, unit filtration,
log/exp, valuation and lattice normal-form coverage: **not checked**.
Unknown formal availability is not evidence of absence. The precise
primary inputs above and the exact finite certificate support this
informal result; neither software output nor Mathlib availability is
an original-IUT correctness certificate.
