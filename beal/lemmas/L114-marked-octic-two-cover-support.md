# L114 — Sufficient support for the marked octic two-cover map

## Hypotheses

Work over Q with L113's audited smooth proper genus-three model C of

    Y²=G(t)=3025t⁸−31460t⁶+76230t⁴−39204t²+2673.

Retain its actual minus-three marking and original scalar s. Let
A=Q[t]/(G), theta the image of t; use the entire etale algebra, with
no irreducibility, maximal-order basis or class-group assumption. Use
Bruin–Stoll's even-degree fake map with target

    H_Q={delta in A*/(A*² Q*): N(delta) in 3025 Q*²}.

## Conclusion

The exact polynomial discriminant is

    disc(G)=2^72 * 3^27 * 5^8 * 11^21.

A sufficient finite base-prime support is S_fin={2,3,5,11}; retain the
real place separately. At every finite prime outside S_fin the entire
point image has an unramified representative in the scalar quotient.
By the cited global supported-representative theorem the rational point
image, and the fake two-Selmer set, lie in H_Q(S), represented by square
classes unramified outside S in all simple factors, followed by the
even-degree scalar quotient. This is containment, not enumeration.

The two distinct rational infinity points I_minus and I_plus have
q=0, Z=−55 and +55 in L113's chart, respectively, and

    mu(I_minus)=mu(I_plus)=[3025]=[1].

Both have original scalar s=1 and remain boundary points, not primitive
integer solutions or disjoint factors in a regular fiber.

## Proof

### Imported support theorem and its specialization

Import Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. 78 (2009), 2347–2370,
[DOI 10.1090/S0025-5718-09-02255-8](https://doi.org/10.1090/S0025-5718-09-02255-8).
The inspected version is [arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2),
21 October 2008: Section 2 p.3 (target and exceptional evaluations),
Definitions 4.1–4.2 and Lemma 4.3 p.6, containment proof pp.6–7,
and Section 6 pp.11–13 (supported global representatives). Page numbers
refer to that manuscript. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-21-marked-octic-two-cover-support.md`.
The general theorems are imported, not reproved here.

The first part of Lemma 4.3 assumes a nonarchimedean characteristic-zero
local field with finite odd residue field, an integral squarefree
polynomial, unit leading coefficient and discriminant valuation at most
one. It concludes unramified point images in the entire algebra's scalar
quotient, including nonintegral point coordinates. Section 6 takes S
containing infinity, dyadic primes, coefficient denominators, nonunit
leading coefficients and discriminant valuations greater than one; it
gives mu(C(Q)) subset Sel_fake^(2)(C/Q) subset H_Q(S). We do not use
the second part of Lemma 4.3, its residue-size bound or any assertion
that the chosen local tests suffice to compute the fake Selmer set.

L113 proves that G is squarefree of degree eight and identifies C with
the actual marked curve on smooth proper charts. All coefficients are
integers, and the leading coefficient is 3025=5²*11². The discriminant
calculation below shows that for p outside {2,3,5,11}, p is odd,
G is integral, its leading coefficient is a p-adic unit and
v_p(disc(G))=0<=1. Every hypothesis of the containment part applies.
This refers to every field factor of A tensor Q_p, not a selected root
field. Section 6 then supplies the stated global containment. The support
means all maximal-ring places over these rational primes in every simple
factor. No identification of the polynomial order with a maximal ring
is made. In particular no supported-class group is replaced by S-units:
class-group two-torsion may contribute.

### Complete exact arithmetic certificate

Let P(X)=3025X⁴−31460X³+76230X²−39204X+2673, so G(t)=P(t²).
The Sylvester determinants give

    Res(G,G')=314894711716680648285949773305306815086970702629049466880000000000,
    Res(P,P')=678364670460641419041177600000.

For degree n and leading coefficient a, the polynomial discriminant is
(−1)^(n(n−1)/2) Res(f,f')/a. Both signs here are positive. Exact division
by 3025 gives

    disc(G)=104097425360886164722628024233159277714701058720346931200000000,
    disc(P)=224252783623352535220224000
           =2^32 * 3^11 * 5^3 * 11^9.

Successive exact divisions of disc(G) by 2,3,5,11 have exponents
72,27,8,21 and remainder one. These four integers are prime (trial
division through their square roots suffices), so this certifies the
complete displayed factorization, including its positive sign.
As an arithmetic cross-check the two computed discriminants satisfy

    disc(G)=2^8 * 3025 * 2673 * disc(P)^2.

The conclusion uses the direct octic determinant, independently of this
cross-check identity; no new general composition formula is needed.

Reproduce with `python3 scripts/pair-genus-two/marked_octic_support.py`.
The complete evidence is
`scripts/pair-genus-two/marked-octic-support-certificate.json`.
It stores both complete Sylvester matrices (sizes 15 and 7), every pivot,
row swap and divisor, both resultants/discriminants and complete prime
division outputs. For each matrix the first deg(f') rows are shifted
descending coefficient rows of f, and the remaining deg(f) rows are
shifted rows of f'. The exact determinant computation replaces trailing
entries at step k by

    a_ij <- (a_kk*a_ij−a_ik*a_kj)/previous_pivot,

after the recorded nonzero-pivot row swap; the first previous pivot is
one. All divisions have zero remainder. The determinant is the final
entry multiplied by the accumulated row-swap sign. This fraction-free
elimination is ordinary determinant elimination with the pivots cleared;
the saved full matrices and recurrence suffice to replay every integer
operation without a numerical approximation or black-box field backend.
All 11 checks pass, with no failures, factorization remainder 1/1 and
infinity rows 2/2. Complete relevant certificate values were inspected.
These checks certify polynomial arithmetic, not class/unit completeness.

### Both infinity rows and the original boundary

L113's infinity chart is

    Z²=3025−31460q²+76230q⁴−39204q⁶+2673q⁸,
    q=1/t, Z=Y/t⁴.

At q=0 it has exactly Z=±55. The derivative in Z is ±110, nonzero,
so each point is smooth and q is a local parameter. L113's regular
transport gives the following separate rows:

| Point | Z | (T,h,R) | (u,v,z,s) | fake representative | fake image |
| --- | --- | --- | --- | --- | --- |
| I_minus | −55 | (2,0,−165) | (0,0,0,1) | 3025 | [1] |
| I_plus | 55 | (2,0,165) | (0,0,0,1) | 3025 | [1] |

Section 2's square-leading-coefficient convention assigns [f_n] to each
infinity point. Here f_n=3025=55² is already a square in A*, hence both
images equal the identity. They lie in H_Q since their norm class is
square and f_n is square. This equality of fake images does not identify
the two points. We never substitute q=0 into the noninvertible affine
expression q(1−q theta). L113 supplies the original marked transport and
normalized boundary interpretation; no other point is classified here.
The rational boundary forces a nonempty fake Selmer set.

### Use and limitations

This completes only the approved instance support prerequisite, by
specialization of the cited known method. It supplies no progress beyond
that general method. A future finite cover collection still needs
maximal-ring unit/class data for every simple factor, complete required
local tests and point control on surviving covers. Degree-nine root
recovery, compatible remaining factors, both L095 integer systems and
the minus-eleven alternative remain unresolved. Preserve ATTEMPTS/050–051,
unfinished L108 and L113's two initial check failures. The independent
critical audit below confirms this specialization without changing the claim.

### Independent critical audit, 2026-10-22

The approved audit passes. This establishes reliability of the instance
input by reproduction; it supplies neither a new support theorem nor
rational-point completeness. The exact polynomial, support and two
infinity images require no correction. The direct mathematical input
remains L113; the argument assembly and DAG are unchanged.

The independent script is
`scripts/pair-genus-two/audit_marked_octic_support.py`; run it with
`python3 scripts/pair-genus-two/audit_marked_octic_support.py`.
It imports no producer code and reconstructs G directly as eleven times
the nine coefficients of (1) in L113. It constructs both Sylvester
matrices by multiplying the ascending polynomials by the required
monomials and reversing their complete coefficient vectors. All 225
octic and 49 quartic matrix entries agree with the saved matrices.

Ordinary Gaussian elimination over exact rational numbers gives each
determinant as the product of its pivots times the row-swap sign:
row addition leaves the determinant unchanged, row swapping changes
its sign, and the final triangular matrix has determinant the product
of its diagonal entries. This algorithm is independent of the producer's
fraction-free updates. The octic uses four swaps, at steps 7,9,11,13
(zero-based); the quartic uses none. Both determinants agree with the
full integers displayed above. The discriminant signs are positive
because 8*7/2=28 and 4*3/2=6 are even. Exact division by 3025 gives
both displayed discriminants, without identifying either with a field
discriminant.

As a separate full replay, every producer pivot, chosen row and previous
divisor agrees. At each step the fraction-free pivot equals the product
of the rational Gaussian pivots so far, before the accumulated swap
sign. All 1,106 trailing-entry divisions in the two fraction-free
computations are exact; the signed final entries agree with the
independent determinants. Thus the audit does not merely compare
producer check flags or rely on the quartic composition identity.
Successively dividing the octic discriminant by 2,3,5,11 yields exactly
72,27,8,21 divisions and remainder one. The quartic yields 32,11,3,9
and remainder one. Trial division through the integer square root
certifies all four primes; multiplying the powers recovers each whole
positive discriminant. The composition identity is also checked, only
as redundant arithmetic evidence.

For the theorem application, use precisely the containment part of
Bruin–Stoll Lemma 4.3, Definitions 4.1–4.2, and Section 6 cited above.
The primary statements and the integral/nonintegral proof cases were
rechecked against this application. For every rational prime outside
S_fin, the coefficients lie in Z_p, 3025 is a unit, p is odd and the
polynomial discriminant has valuation zero. Characteristic zero and
squarefreeness give the entire degree-eight etale algebra; the source
does not require it to be a field. Its definition tests every local
field factor. The integral-coordinate case, exceptional evaluations
and the nonintegral-coordinate case are included in the cited point
map and containment theorem. In particular the nonintegral case uses
the common scalar x before testing square classes, so no denominator
prime of a point is silently added to S. Section 6 supplies the global
supported representatives in the even-degree scalar quotient. No
choice of independent local scalars is asserted to give a global
representative without that cited input. The norm condition is
well-defined because a scalar has norm its eighth power. All maximal
places over S_fin in every simple factor are retained, as is the real
place. The stronger residue-size assertion, minimal support, polynomial
order maximality, S-unit exhaustion and complete local-image tests are
not premises of this containment.

For the infinity evaluation, substitute q=0 separately in the regular
formulas (6) of L113. At each sign Z0=±55, the coefficient 2Z0 is
nonzero, so q is a genuine uniformizer. One obtains T=2, h=W=0 and
R=3Z0. The original functions have F=11, K=1, L=5, u=0, M=2 and
rho=1/12, with all displayed denominators nonzero. Therefore v=z=0
and s=H0(0,0)=phi(0)=1. The normalized residues, computed from the
same regular formulas, are

    h/q = -12, W/q = -12Z0, v/q = -1,
    z/q² = 1, v/W = 1/(12Z0).

The two v/W residues are -1/660 and +1/660 respectively. They retain
the two distinct marked boundary lifts. Section 2 p.3 assigns each
infinity point the class of 3025=55²; LocalImage's infinity treatment
pp.10–11 confirms that no affine reciprocal evaluation at zero replaces
this rule. The representative is invertible in every factor. Its norm
divided by the required leading coefficient is
3025^8/3025=55^14=(55^7)^2, so it lies in the stipulated norm fiber.
Both images are identity although their R coordinates, smooth points
and normalized marked lifts differ. Known rational boundary points
force nonemptiness of the fake Selmer set; they do not classify it.

Full evidence, including both matrices, rational elimination traces,
all producer trace comparisons, complete prime-division chains and
both independently reconstructed transport rows, is saved in
`scripts/pair-genus-two/marked-octic-support-audit-certificate.json`.
All 80 checks pass; actual/required discriminant exponents are
(72,27,8,21)/(72,27,8,21), final factorization remainders 1/1 for
each polynomial, and distinct smooth infinity rows 2/2. The complete
producer evidence was consumed and compared, not inferred from a
bounded preview. The proof above justifies the source application;
arithmetic flags alone do not verify a theorem's hypotheses.

The first auditor run passed 78 of 80 checks: only the two norm-fiber
comparisons failed, because Python integer division introduced a
floating-point value into comparison with the exact integer 55^14.
Replacing that division with an exact rational constructor gives the
identity displayed above. The initial evidence is preserved in
`scripts/pair-genus-two/marked-octic-support-audit-initial-check-failure.json`.
This repairs an auditor check, not L114's mathematics. L113's earlier
initial check failures remain untouched. Unit/class arithmetic, complete
local tests, surviving-cover points and all downstream integer gaps
remain unresolved.

## Mathlib

Full coverage of Bruin–Stoll's supported fake two-cover map, its scalar
quotient and exceptional infinity conventions was not checked. No absence
claim or formalization claim is made. The result uses the precise primary
citation above and exact integer arithmetic, not a Mathlib theorem import.
