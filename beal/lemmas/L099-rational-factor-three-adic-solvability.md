# L099 — Both rational-factor systems have primitive three-adic points

## Hypotheses

Interpret L095's systems over Z_3, with

    Q(m,n)=3m²+mn+n²,
    H(m,n)=55n^8+165mn^7+594m²n^6+1100m³n^5
           +2145m^4n^4+2475m^5n³+2970m^6n²+1782m^7n+1215m^8.

Require m,u,a,A,B,C nonzero, min(v_3(m),v_3(u))=0, C a unit,
and min(v_3(A),v_3(B),v_3(C))=0. Positivity and coprimality at
other primes are not conditions on a Z_3 point. The systems are

    I:  C=5m+u^5,        H(m,C)=a³,       A=ma, B=Q(m,C)u;
    II: C=m+5^10 u^5,   H(m,5C)=5^11a³,  A=ma, B=Q(m,5C)u.

## Conclusion

Both systems have such a point. Explicit exact descriptions are:

* I: m=3, a=1, u is a root in 25+27 Z_3 of
  F_I(U)=H(3,15+U^5)−1. Define C=15+u^5, A=3 and B=Q(3,C)u.
* II: m=3, a=2, u is a root in 7+27 Z_3 of
  F_II(U)=H(3,15+5^11 U^5)−8*5^11. Define
  C=3+5^10u^5, A=6 and B=Q(3,5C)u.

In both points u,B,C are units, v_3(A)=1, and
A³+B^5=C^11 holds exactly. Standalone three-adic nonexistence cannot
exclude either system. No integer solution or global rational factor
is asserted, and neither full local valuation classification nor
simultaneous compatibility at different primes is claimed.

## Proof

We import Gergely Zábrádi, *Notes for the course p-adic methods in
arithmetic*, 29 June 2022, Theorem 2.4, printed p.4
([author PDF](https://zabradi.web.elte.hu/Jegyzetek/p-adic-meth-arith.pdf)).
For an integral polynomial, an approximate root modulo p^n and a
partial derivative of valuation k with 0<=2k<n give an exact root
congruent to that approximate root modulo p^(n−k). The precise source
hypotheses and lifting proof were inspected in the prior assessment;
foundations/17-local-power-hensel-inputs.md records them. Apply this
one-variable theorem to F_I or F_II, with p=3, n=3, k=0. We vary u
while holding m and a fixed. Thus the relation defining C is retained
identically, rather than checked at a separately chosen tuple. No cube
root surjectivity or unit cube derivative at three is assumed.

Here are complete small-modulus computations of the required errors.
Substituting m=3 in the displayed H gives

    H(3,N) = 55N^8+9N^7+54N^5 (mod 243).

Indeed its nine coefficients, in descending N-degree, reduce to
[55,9,0,54,0,0,0,0,0]. At the proposed integral seeds:

| System | u0 | N(u0) mod 243 | scale*a³ mod 243 | H(3,N(u0)) mod 243 | F(u0) mod 243 |
| --- | --- | --- | --- | --- | --- |
| I | 25 | 199 | 1 | 163 | 162 |
| II | 7 | 122 | 70 | 151 | 81 |

Here N_I(U)=15+U^5 and N_II(U)=15+5^11U^5; the scales are 1
and 5^11, respectively. The table follows by substituting 199 and 122
in the reduced polynomial above. Thus v_3(F_I(25))=4 and
v_3(F_II(7))=4, not merely a lower bound inferred from a preview.
Both errors in particular vanish modulo 27.

Modulo three, H(3,N)=N^8. Since both polynomials have integral
coefficients, differentiation commutes with reduction. We have
N_I(U)=U^5 and N_II(U)=2U^5 modulo three. With the chosen a values,
both subtracted constants reduce to one. Consequently

    F_I(U)=F_II(U)=U^40−1 (mod 3),
    F_I'(U)=F_II'(U)=U^39 (mod 3).

Both seeds are 1 modulo three, so both derivatives are units. Equivalently,
the exact derivatives are 5U^4 H_n(3,N_I(U)) and
5^12 U^4 H_n(3,N_II(U)); no derivative scale has been omitted.
The strict inequality 2k=0<n=3 holds. The cited theorem therefore
supplies exact integral roots u with u=25 modulo 27 in I and
u=7 modulo 27 in II. Each u is 1 modulo three and is nonzero.

The fixed choices m=3, a=1 or 2 are nonzero, and A=ma is 3 or 6,
so v_3(A)=1. In I, C=15+u^5 is 1 modulo three and N=C is 1.
In II, C=3+5^10u^5 is 1 modulo three and N=5C is 2.
In both, Q(3,N)=N² modulo three is 1. Thus B=Q(3,N)u is 1
modulo three, as is C. In particular all required coordinates are
nonzero, the pair (m,u) is primitive at three, and the reconstructed
bases are primitive at three. Divisibility of A by three is permitted.

It remains to verify the complete equation at the same exact tuple.
L095's identity is a polynomial identity, hence holds in Z_3:

    N^11−Q(m,N)^5(N−5m)=m³H(m,N).

In I, N=C and N−5m=u^5, and the root equation gives H=a³.
The identity becomes C^11−B^5=(ma)³=A³.
In II, N=5C, N−5m=5^11u^5 and H=5^11a³. It becomes

    5^11(C^11−B^5)=m³5^11a³.

Cancelling the nonzero three-adic unit 5^11 yields the same equation.
This uses one common u and C throughout each system.

The reproducible finite search is
`python3 scripts/rational-factor/check_three_lifts.py`; its full
certificate is `scripts/rational-factor/three-lifts-certificate.json`.
For each system it enumerates all 729 pairs (m,u) modulo 27, retains
486 with C a unit and (m,u) primitive modulo three, and finds 162
surviving pairs and 810 triples (m,u,a). Zero a residues are retained:
a nonzero exact coordinate may reduce to zero. Both selected seeds
occur in this complete list. These counts do not assert a finite
obstruction or classify exact points. No search beyond modulo 27 was
needed; reduction of the exact seed error modulo 243 certifies its
valuation and is not a further search.

All 34 arithmetic checks pass. The full errors, derivatives, coordinate
residues and selected seeds were inspected. An alternate evaluation
through (N^11−Q^5(N−5m))/m³ checks the complete H values and the
error residues without reusing the H coefficient sum. Hensel's theorem
and the reconstruction proof above, rather than residue survival,
supply the exact existence conclusion. This arithmetic cross-check is
distinct from the subsequent independent critical audit recorded below.

L095 supplies the forms and reconstruction identity. This is a local
reproduction of the assessed Hensel method, not a claim of progress
beyond the checked known method sources or an originality certification.
The unchanged prior EXPLORE assessment is
`drafts/literature/2026-10-19-rational-factor-three-adic-realization.md`.
L096 is only a comparison at eleven, not a mathematical input here.
Both integer systems, integer lifting, other algebra factors and other
Beal signatures remain unresolved. Exact local points retire only the
standalone three-adic nonexistence mechanism.

### Independent critical audit — 2026-10-19

Verdict: **PASS without correction**, for both exact primitive Z_3
points and their common-tuple reconstructions. This is independent
verification of the stated specialization, not a stronger existence
theorem, an integer solution or an originality certification. The prior
EXPLORE assessment is
`drafts/literature/2026-10-19-rational-factor-three-adic-audit.md`;
its TARGET exactly matches the saved audit action. No additional
mathematical input or changed DAG edge is needed.

Independently derive H from identity (4) of audited L095 as follows.
The term indexed by i+j+k=5 in Q(m,N)^5 is

    5!/(i!j!k!) * 3^i * m^(2i+j) * N^(j+2k).

Multiply this full expansion by N−5m and subtract from N^11.
Every term of m-degree below three cancels, and the nine remaining
terms, after division by m³, have exactly the nine coefficients of H
displayed above. This coefficient check is an identity of polynomials,
not division by a potentially vanishing local coordinate. It verifies
all degrees, including the m^8 term and both scaled substitutions.

Write sigma=1 in I and sigma=5^11 in II. With m=3 and fixed a=1
or 2, expand the integral polynomial

    F(U) = sum_(i=0)^8 H_i * 3^i * (15+sigma U^5)^(8−i)
           − sigma a³.

Formal differentiation of the full expansion independently gives the
derivative, including the factors 5 and 5^12 in the two cases. An
additional check differentiates the complementary identity itself:

    27 H_N(3,N) = 11N^10
                  −5 Q(3,N)^4(3+2N)(N−15)−Q(3,N)^5.

Evaluating the expanded F and F' at 25 or 7 agrees with every digit
of the original errors and derivatives. Their residues are respectively
F(25)=162 and F(7)=81 modulo 243, and both derivatives are 1
modulo three. The full reduced polynomials are U^40−1 and U^39
for F and F', respectively, in both systems. Thus each error has
valuation exactly four and each derivative has valuation zero.

Zábrádi's cited Theorem 2.4 applies over the complete ring Z_3:
the coefficients and seeds are integral, F vanishes modulo 3^3,
and 0=2k<3 with k=0. It gives an exact root in the specified
seed class modulo 27 while leaving m and a fixed. The defining
polynomial for C consequently stays true at that same root. These
roots are units; C and B have residue one. The constants m=3 and
a=1,2 are nonzero, and A=3,6 has valuation one. Hence every required
coordinate is nonzero and both the auxiliary pair and the reconstructed
bases are primitive at three. No positive-integer converse is applied
over Z_3. Direct evaluation of the polynomial identity gives the
unscaled equation in I and gives 5^11 times it in II; cancellation is
legitimate since 5^11 is a unit. This checks the full systems rather
than two independently lifted equations.

The independent replay is
`python3 scripts/rational-factor/audit_three_lifts.py`. It uses the
multinomial expansion above and a direct exhaustive product of all
27³ triples, instead of the original cube-value lookup. It reproduces
486 admissible pairs, 162 surviving pairs and every entry of both
810-triple lists, including zero cube residues. It compares all 27
fields of each stored record, both complete certificates, all 34
original assertions and the empty failure lists. Its **83 audit checks
pass**, with full expanded polynomials, derivatives, exact records and
source hashes saved in
`scripts/rational-factor/three-lifts-audit-certificate.json`.
The complete load-bearing audit fields and original exact errors and
derivatives were inspected; previews and stored pass flags were not
used as substitutes for this replay. The Hensel application and
reconstruction argument, rather than the finite list, prove existence.

The audit secures the stop on standalone three-adic nonexistence in
ATTEMPTS/046. Integer lifting, global compatibility, other factors and
other signatures remain unresolved. Mathlib coverage is unchanged.

## Mathlib

Full matching coverage of these two systems and supporting Hensel
declarations: **not checked**. No formal verification or absence claim
is made.
