# L100 — Both rational-factor systems have primitive two-adic points

## Hypotheses

Interpret the full L095 systems over Z_2. Write

    Q(m,n)=3m²+mn+n²,
    H(m,n)=55n^8+165mn^7+594m²n^6+1100m³n^5
           +2145m^4n^4+2475m^5n³+2970m^6n²+1782m^7n+1215m^8.

The systems are

    I:  C=5m+u^5,       H(m,C)=a³,      A=ma, B=Q(m,C)u;
    II: C=m+5^10u^5,    H(m,5C)=5^11a³, A=ma, B=Q(m,5C)u.

Require all of m,u,a,A,B,C nonzero, min(v_2(m),v_2(u))=0 and
min(v_2(A),v_2(B),v_2(C))=0. A two-adic point has no positivity
condition or coprimality condition at other primes. In particular,
L095's integer condition gcd(C,15)=1 imposes no unit-C condition at two.

## Conclusion

Both complete systems have such points:

* I: m=u=1, C=6, B=45, A=a, where a is the root in 27+32 Z_2
  of X³−178268931.
* II: m=u=1, C=9765626, B=2384186328125033, A=a, where a is
  the root in 7+32 Z_2 of 48828125 X³−H(1,48828130).

In both, A,B are units, v_2(C)=1, and A³+B^5=C^11 holds exactly.
Standalone two-adic nonexistence therefore excludes neither system.
These are local points, not integer solutions, global rational factors,
or simultaneous witnesses at different primes. Other local branches are
not classified by this conclusion.

## Proof

Import Gergely Zábrádi, *Notes for the course p-adic methods in
arithmetic*, 29 June 2022, Theorem 2.4, printed p.4
([author PDF](https://zabradi.web.elte.hu/Jegyzetek/p-adic-meth-arith.pdf)).
For an integral polynomial and an integral approximate zero modulo p^n,
if a chosen derivative has valuation k with 0<=2k<n, this theorem
gives an exact integral zero congruent to the seed modulo p^(n−k),
fixing the other coordinates. Its hypotheses and proof were inspected
in the prior assessment and are recorded in
`foundations/17-local-power-hensel-inputs.md`. The theorem applies at
p=2. No reproof or theorem of square-root surjectivity is needed.

Fix m=u=1 first, so that C and B are fixed by the defining equations.
For I this gives C=N=6, Q(1,6)=45 and H(1,6)=178268931.
For II it gives C=1+5^10=9765626, N=5C=48828130,
Q(1,N)=2384186328125033 and scale 5^11=48828125. Let

    F_I(X)=X³−178268931,
    F_II(X)=48828125 X³−H(1,48828130).

Both are integral polynomials. Here are finite exact valuation
certificates, retaining every coefficient of H:

| System | seed a0 | N mod 64 | H(1,N) mod 64 | scale*a0³ mod 64 | F(a0) mod 64 | F'(a0) |
| --- | --- | --- | --- | --- | --- | --- |
| I | 27 | 6 | 3 | 35 | 32 | 2187 |
| II | 7 | 34 | 59 | 27 | 32 | 7177734375 |

For I, direct substitution gives the exact error −178249248.
For II, N=34 modulo 64 has powers N²=4, N³=8, N^4=16,
N^5=32 and N^6=N^7=N^8=0 modulo 64. Thus H(1,N) reduces to

    2145*16+2475*8+2970*4+1782*34+1215 = 59 (mod 64);

the term 1100*32 is zero modulo 64, as are all higher N-degrees.
Also 5^11=29 modulo 64 and 7³=23 modulo 64, giving 27 for
the scaled cube. The two displayed derivatives are respectively
3*27² and 3*5^11*7². They are odd. Hence both errors have valuation
exactly five and both derivatives have valuation k=0.

Apply the cited theorem with p=2, n=5: both errors vanish modulo 32
and the strict inequality is 2k=0<5. It gives exact roots a in the
claimed residue classes modulo 32. Each root is odd and nonzero.
Uniqueness within either stated disk follows directly: if x,y are
odd roots of the same polynomial, then

    0 = scale*(x−y)*(x²+xy+y²).

The scale is odd, and the last factor is odd. Both are nonzero in
Q_2, so x=y. This is only uniqueness for these fixed m,u, not a
classification of the full systems.

All other coordinates have already been fixed as nonzero integers.
The values B=45 and B=2384186328125033 are odd. Both choices of C
are 2 modulo 4. Thus m,u,a,A,B are units and v_2(C)=1. This proves
all required nonzero conditions, auxiliary primitivity and reconstructed
primitivity. In particular it retains an even right-hand base rather
than incorrectly restricting C to the units.

The full simultaneous reconstruction uses L095's polynomial identity

    N^11−Q(m,N)^5(N−5m)=m³H(m,N).                 (4)

An identity over Z remains valid over Z_2; its use does not apply
L095's positive-integer converse to local points. In I, N=C,
N−5m=u^5=1 and H=a³. Thus (4) gives C^11−B^5=(ma)³=A³.
In II, N=5C, N−5m=5^11u^5 and H=5^11a³. Consequently (4) is

    5^11(C^11−B^5)=m³5^11a³.

Cancellation of the nonzero two-adic unit 5^11 gives the same original
equation. The lifted cube coordinate leaves the single common C and
all defining relations unchanged throughout each construction.

The prior assessment is
`drafts/literature/2026-10-19-rational-factor-two-adic-solvability.md`
(EXPLORE), saved before this calculation. This is a reproduction of
the assessed elementary lifting method on these explicit systems, not
a claim of progress beyond the checked source methods or of originality.
Putz's necessary algebra covering list is comparison context only;
it is not used to deduce existence.

Supporting finite verification is reproducible with
`python3 scripts/rational-factor/check_two_lifts.py`. The full certificate
is `scripts/rational-factor/two-lifts-certificate.json`. The complete
modulo-32 search checks all 768 pairs with at least one odd member
in each system, retaining zero coordinate residues; each has one odd
cube-coordinate residue and a primitive reconstructed triple modulo 32.
All 18 checks pass, including exact seed errors, derivatives, both
scales, the numerical complementary identity and reconstructed residuals.
The full load-bearing seed records were inspected. These finite checks
support the explicit theorem application above; residue survival alone
is not exact existence, and no claim that every residue branch lifts
is required here. The separate independent critical application audit
is recorded below. Integer lifting, global compatibility, other algebra
types and residual signatures remain unresolved.

### Independent critical audit — 2026-10-19

Verdict: **PASS without correction**, for the exact local existence
claims and ancillary finite-domain claims stated above. The prior
EXPLORE assessment is
`drafts/literature/2026-10-19-rational-factor-two-adic-audit.md`;
its TARGET exactly matches this audit. Reuse Zábrádi's Theorem 2.4,
29 June 2022, printed p.4, with its hypotheses as stated above and in
`foundations/17-local-power-hensel-inputs.md`. No new external input,
reproof of Hensel's theorem, or original mathematical discovery is
claimed. L095's audited integral identity is the sole lemma input;
neither its positive-integer converse nor Putz's classification is
used to produce these local points.

The coefficient audit expands Q^5 independently by the multinomial
theorem. For r+s+t=5, the term selecting r copies of 3m², s copies
of mn and t copies of n² has coefficient
5! 3^r/(r!s!t!) and m-degree 2r+s. Multiplication by n−5m places
this coefficient in degree 2r+s and its negative fivefold in degree
2r+s+1, with complementary n-degrees totaling eleven. Subtracting
from n^11 gives zero in m-degrees zero, one and two and, in degrees
three through eleven, exactly

    55, 165, 594, 1100, 2145, 2475, 2970, 1782, 1215.

Thus all coefficients of H and the entire identity (4) agree, rather
than only its selected values. This is verification of the existing
identity, not a new identity needed as a separate result.

The full seed arithmetic was independently reconstructed. In I,
C=N=6, Q=45, H=178268931, a0=27, the exact error is
−178249248 and the derivative is 2187. In II, C=9765626,
N=48828130, Q=2384186328125033, scale=48828125 and a0=7.
The complete values are

    H = 1777147412308222434037022227424644756945882013371940868310546875,
    F(a0) = -1777147412308222434037022227424644756945882013371940851562500000,
    F'(a0) = 7177734375.

The independent mod-64 tuples (N,H,scale*a0³,F(a0)) are
(6,3,35,32) and (34,59,27,32), respectively. In the second tuple,
the powers of 34 modulo 64 in degrees two through eight are
4,8,16,32,0,0,0. In particular the degree-five contribution
1100*32 vanishes, and the displayed reduction of H retains every
nonzero contribution. Both exact errors are nonzero and equal to
32 modulo 64; both derivatives are odd. Hence the actual valuations
are v2(F(a0))=5 and k=v2(F'(a0))=0, meeting precisely n=5 and
the strict required inequality 2k=0<5. These are integral polynomials
with the other coordinates fixed. The imported theorem therefore
produces exact roots in the stated disks, rather than only residues.

Each disk consists of odd numbers, so each root is nonzero. If two
roots lie there, their difference times the odd unit
scale*(x²+xy+y²) is zero. The integral domain Z_2 then makes their
difference zero. This checks uniqueness without reading it into the
cited existence statement. Both fixed B values are nonzero odd
integers and both C values are 2 modulo 4; m=u=1 and A=a are
units. Thus every required coordinate is nonzero, the auxiliary pair
is primitive, and the reconstructed triple is primitive despite its
even C. No assertion about positivity or primitivity at other primes
enters this local conclusion.

For the same fixed tuple in I, N=C and N−5m=1=u^5. Identity (4)
therefore gives C^11−B^5=m³H=(ma)³. For the same fixed tuple in
II, N=5C and N−5m=5(C−m)=5^11u^5. The left side of (4) is
then exactly 5^11(C^11−B^5), while its right side is
m³5^11a³. Cancelling the nonzero two-adic unit 5^11 gives
C^11−B^5=(ma)³. Lifting a changes none of m,u,C,N,B.
This verifies the simultaneous equations, not independent equations
whose shared coordinates might disagree. The exact seed residuals
C^11−B^5−(ma0)³ are respectively 178249248 and
36395979004072395449078215217656724622251663633857348640;
they equal −m³F(a0)/scale, as required by the two reconstructions.

The ancillary finite claim also survives full replay. For each system
the complete domain is the 768 ordered pairs modulo 32 with at least
one odd coordinate, including zero coordinate residues. Cubing
permutes the sixteen odd residues and is its own inverse there
(x^9=x for odd x modulo 32); even cubes are even. Independently
evaluating H/scale for every pair gives an odd residue, so this
permutation provides exactly one odd cube root and excludes even
ones. Each corresponding reconstructed triple has an odd coordinate
and satisfies the original equation modulo 32. Both entire ordered
768-triple arrays, all fields of both seed records, all original
assertion records, counts and empty failure lists were compared with
the original certificate. Nothing is inferred from an array preview.
This finite-domain statement does not assert that every residue point
has nonzero coordinates or lifts as a complete local point; exact
existence above uses only the two fixed nonzero tuples.

Reproduce the independent verification with
`python3 scripts/rational-factor/audit_two_lifts.py`. All 34 audit
checks pass and all 18 original assertions are replayed, with no
failures. The full certificate, including complete arrays, exact
records, actual and required bounds and the original certificate hash,
is `scripts/rational-factor/two-lifts-audit-certificate.json`.
The arithmetic checks support the Hensel application, uniqueness and
reconstruction proofs just checked; they do not replace those proofs.
This secures the recorded stop on standalone two-adic exclusion,
without a new solution, local classification, global compatibility
statement or integer exclusion. The argument and DAG are unchanged.

## Mathlib

Full matching coverage of these systems and the supporting Hensel
declarations: **not checked**. No formal verification or absence claim
is made.
