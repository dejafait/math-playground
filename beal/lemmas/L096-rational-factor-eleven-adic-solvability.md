# L096 — Both rational-factor power systems have primitive eleven-adic points

## Hypotheses

Use the integral forms Q,H and the two systems of L095, now interpreted
over Z_11. Require m to be a unit, m,u,a and reconstructed A,B,C to be
nonzero, and min(v_11(A),v_11(B),v_11(C))=0. This is a local test;
integer positivity and coprimality conditions at other primes are not
conditions on a Z_11 point.

## Conclusion

Each system has a point with every listed coordinate a unit:

* I: m=u=1, C=6, a is the unique root congruent to 3 modulo eleven of
  X^3−178268931. Then A=a and B=45.
* II: m=u=1, C=9765626, a is the unique root congruent to 1 modulo
  eleven of 5^11 X^3−H(1,48828130). Then A=a and
  B=2384186328125033.

Both satisfy A^3+B^5=C^11 exactly in Z_11. Neither system can be
excluded by eleven-adic nonexistence alone. No integer solution, global
rational factor, or simultaneous satisfaction at other places follows.

## Proof

The imported lifting theorem is Gergely Zábrádi, *Notes for the course
p-adic methods in arithmetic*, 29 June 2022, Theorem 2.4, printed p.4
([author PDF](https://zabradi.web.elte.hu/Jegyzetek/p-adic-meth-arith.pdf)).
For an integral polynomial, an approximate root modulo p^n and a partial
derivative of valuation k with 0<=2k<n give an exact root congruent
modulo p^(n−k). Its hypotheses and proof were inspected in the prior
assessment; foundations/17-local-power-hensel-inputs.md records the
input. We use n=1,k=0 and fix every variable except a. Uniqueness in
the stated residue disk also follows directly: if x,y are roots there,
their difference times scale*(x²+xy+y²) is zero, and the latter factor
is a unit since its residue is scale*3*a0², which is nonzero.

All coefficients of H except 1215 are divisible by eleven, whereas
1215 is congruent to 5. Hence H(1,n) is congruent to 5 for every n.
For I set m=u=1 and C=5m+u^5=6. Direct evaluation gives
H(1,6)=178268931. At a0=3 the polynomial F(X)=X³−H(1,6)
vanishes modulo eleven because 3³ is congruent to 5; its derivative
F'(3)=27 is a unit. The cited theorem produces an exact unit a
congruent to 3. Q(1,6)=45 is congruent to 1, so the residues of
(A,B,C) are (3,1,6), all nonzero. The variables m,u are also units.

For II set m=u=1 and C=m+5^10 u^5=9765626, and n=5C=48828130.
Fermat's little theorem in F_11 gives 5^10 congruent to 1, so C is
congruent to 2 and n is congruent to 10. Put
F(X)=5^11 X³−H(1,n). Since 5^11 is congruent to 5, F(1) is zero
modulo eleven, while F'(1)=3*5^11 is congruent to 4 and is a unit.
Hensel therefore gives an exact unit a congruent to 1. Here
Q(1,n)=2384186328125033 is congruent to 3. Thus the reconstructed
(A,B,C) have residues (1,3,2); all listed coordinates are again units.

For completeness the reconstruction uses L095's polynomial identity
n^11−Q(m,n)^5(n−5m)=m³H(m,n), valid also in Z_11. In I, n=C
and n−5m=u^5, so it gives C^11−B^5=A³. In II, n=5C and
n−5m=5^11u^5; substituting H=5^11a³ and cancelling the nonzero
unit 5^11 gives the same equation. Thus each is one common tuple,
not independently chosen roots of separate coordinate conditions.
Units are nonzero and give valuation minimum zero, proving the exact
local requirements. Existence suffices; no classification of nonunit
valuation cases is needed or claimed.

The script `python3 scripts/rational-factor/check_eleven_lifts.py`
checks all sixteen finite assertions, including both full integer
complementary identities, the exact errors and derivatives, and every
coordinate residue. Its complete certificate is
`scripts/rational-factor/eleven-lifts-certificate.json`; both errors
have valuation one against the required strict lower bound zero, and
there are no failures. Both complete records were inspected. The
existence proof is Hensel's theorem with the explicit hypotheses above,
not a finite-precision inference.

This reproduces an elementary specialization of the assessed Hensel
method, without claiming progress beyond the checked method sources.
The prior EXPLORE assessment is
`drafts/literature/2026-10-18-rational-factor-eleven-adic-solvability.md`.
The result retires only this standalone local exclusion route. In
particular C=6 in I is not coprime to three; it is a valid eleven-adic
unit but is not an integer witness satisfying all of L095's global
conditions. Neither lifted a is asserted to be an integer. Global
elimination, integer lifting and other algebra factors remain open.
The independent critical application audit is recorded below.

### Independent critical audit — 2026-10-18

Verdict: **PASS without correction**, restricted to the two local points
and their stated uniqueness and reconstruction. The prior assessment is
`drafts/literature/2026-10-18-rational-factor-eleven-adic-audit.md`.
L095 is the sole direct lemma input. Zábrádi's Theorem 2.4, cited above,
is imported unchanged; no new existence theorem or reproof is used.

Independent integer polynomial multiplication expands
(N²+N+3)^5(N−5). Subtracting it from N^11 gives, in ascending N degree,

    [1215,1782,2970,2475,2145,1100,594,165,55,0,0,0].

These are precisely the coefficients of H(1,N), with every term of
degree above eight zero. Independent Horner evaluation at N=6 and
N=48828130 reproduces both full H values, both Q values and every
field of both original certificate records. No finite-precision root
approximation is used to infer exact existence.

| System | a0 | scale | F'(a0) | (F(a0)/11) mod 11 | v11(F(a0)) | v11(F'(a0)) |
| --- | --- | --- | --- | --- | --- | --- |
| I | 3 | 1 | 27 | 3 | 1 | 0 |
| II | 1 | 48828125 | 146484375 | 2 | 1 | 0 |

Here F(X)=scale X³−H(1,N). The exact errors are divisible by eleven,
and their displayed nonzero quotients modulo eleven establish valuation
exactly one. Both polynomials have integral coefficients and a0 is
integral. Thus the cited theorem applies with n=1 and k=0, satisfying
0<=2k<n, and supplies an exact root a in the stated residue disk.
In particular a remains a unit and cannot vanish.

For any two roots x,y in that same disk, subtraction gives

    (x−y) scale (x²+xy+y²)=0.

The second factor has residue 3 scale a0², equal to 5 in I and 4 in
II. It is therefore invertible in Z_11, so x=y. This proves uniqueness
in each claimed disk; no uniqueness clause beyond the imported
existence conclusion was assumed.

The reconstruction retains m=u=1, A=a, B=Q(1,N) and the fixed C.
In I, N=C=6 and N−5=1. L095's identity gives
C^11−B^5=H(1,N)=a³. In II, N=5C and
N−5=48828125=5^11. The same identity gives

    5^11(C^11−B^5)=H(1,N)=5^11 a³.

The scale 5^11 is an eleven-adic unit, so cancellation is valid.
Equivalently the audit checks the constant and cubic coefficients of
5^11(C^11−B^5−X³)=−F(X) in II, and the corresponding scale-one
identity in I. Thus the same lifted a gives the full original equation;
the complementary equation has not been checked at an unrelated point.

The ordered residues (m,u,a,A,B,C,N) are (1,1,3,3,1,6,6) in I and
(1,1,1,1,3,2,10) in II. Hence every required coordinate is nonzero
and a unit, and all three reconstructed base valuations equal zero.
Both points meet the stated local primitivity requirement. Positivity,
coprimality at other primes, global rational-factor existence and integer
values of a are neither hypotheses nor conclusions of this local audit.
The C=6 failure of the global three-condition remains explicit.

Reproduce the independent arithmetic with
`python3 scripts/rational-factor/audit_eleven_lifts.py`. It does not
import or execute the original script: polynomial multiplication and
Horner evaluation replace its hard-coded H coefficient evaluation.
All sixteen original assertions and sixteen audit checks pass, including
equality of the entire original certificate, its counts and empty failure
list. Full evidence and the original certificate hash are saved in
`scripts/rational-factor/eleven-lifts-audit-certificate.json`; both
complete audit records were inspected. The theorem application and
uniqueness argument above remain essential beyond these finite checks.

This verifies the existing specialization and confirms ATTEMPTS/043's
standalone eleven-adic stop. It supplies no new mathematical input,
integer exclusion, global compatibility, or claim beyond the checked
known method. The argument and its mathematical dependencies are
unchanged.

## Mathlib

Full matching coverage of these two local systems and supporting
Hensel declarations: **not checked**. No formal verification or absence
claim is made.
