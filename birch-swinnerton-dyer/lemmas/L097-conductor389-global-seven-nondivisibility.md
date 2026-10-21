# L097 — A complete reduction witness for global seven-nondivisibility

## Hypotheses

Let E/Q be the exact integral equation

\[
y^2+y=x^3+x^2-2x,
\qquad [a_1,a_2,a_3,a_4,a_6]=[0,1,1,-2,0],
\]

and let P=(0,0), Q=(1,0), R=Q-[4]P. These points satisfy the
equation. L030 supplies global minimality and discriminant 389.
The scalar is seven; the approved prime search is increasing in
11<=ell<=500, excluding 389, stopping at its first completely replayed
witness. No published Mordell–Weil basis, seven-saturation, rational
rank, Selmer dimension or Sha computation is assumed.

## Conclusion

R is not in [7]E(Q), so its class in E(Q)/7E(Q) is nonzero. The
first successful prime in the approved schedule is ell=23, where

\[
\rho_{23}(R)=(4,14),\qquad
[7]E(\mathbf F_{23})=
\{O,(18,1),(18,21),(13,11)\}.
\tag{1}
\]

This is a fixed known-method REPRODUCTION, not a new nondivisibility
theorem or a new rational-rank result. Complete independent finite
replay and the separate fixed critical audit pass. There is no
claim of full saturation, full Selmer-kernel identification, a zero-log
rational point, uniform certificate production or arbitrary-curve BSD.

## Proof

**Imported theorems and specialization.** Use J. H. Silverman,
*The Arithmetic of Elliptic Curves*, second edition, GTM 106,
Springer (2009), DOI 10.1007/978-0-387-09494-6:
[III Algorithm 2.3, printed pp.53–54](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=71)
for the complete group law, and
[VII Proposition 2.1, printed pp.188–190](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=204)
for the reduction homomorphism. Retain the corrections to pp.188–191
in the [author's errata, 13 October 2022, PDF p.21](https://www.math.brown.edu/johsilve/AEC/AECErrata.pdf).
The exact scope and inspected proof cases are recorded in the prior
SPECIALIZE assessment
`drafts/literature/2026-10-20-Q-minus-four-P-global-reduction-witness.md`.
Neither general theorem is reproved here.

For K=Q_ell, L030's integral minimal model has good reduction at every
tested prime because ell does not divide 389. Consequently the domain
of reduction is the whole E(Q_ell), and
rho_ell([7]S)=[7]rho_ell(S), including for S with nonintegral affine
coordinates. Rational points embed in this local group. If R=[7]S
for rational S, its reduction must therefore belong to the full finite
image [7]E(F_ell). No assertion of surjectivity from E(Q) onto the
finite group is needed.

**Complete finite certificates.** The full input and exact replay are

`scripts/global-reduction-377/certificate.json` and
`scripts/global-reduction-377/verification.json`.

Reproduce from this notebook directory:

```bash
python3 scripts/global-reduction-377/build_certificate.py
python3 scripts/global-reduction-377/verify_certificate.py
```

The certificate SHA-256 at this step is
`1a2fc0d80693278515ea44e10c9f4758b054463e476d9913ad8aff8b97be4858`.
The verifier imports or executes no producer. It checks all integers
from 11 through the stopping prime, including every trial-divisor
remainder for primality. At each retained prime it independently tests
every pair (x,y) in F_ell^2, compares the full affine solution list and
adds O. It checks nonsingularity at every affine solution using
(2y+1,-3x^2-2x+2); at O=[0:1:0], the homogeneous partial derivative
with respect to Z is one. The discriminant residue is also checked.
At 23, the trial divisors 2,3,4 leave remainders 1,2,3, and
389 mod 23=21, so all required reduction hypotheses hold.

For finite inputs A=(x,y), B=(u,v), negate by
-(x,y)=(x,-y-1). Identity and inverse cases are treated before division.
For a chord put d=u-x, m=(v-y)/d, n=(yu-vx)/d; for a nonvertical
tangent put d=2y+1, m=(3x^2+2x-2)/d, n=(-x^3-2x-y)/d.
Then A+B=(z,w) with

\[
z=m^2-1-x-u,\qquad w=-mz-n-1.
\tag{2}
\]

Every saved active denominator is nonzero and has a saved inverse
verified by multiplication. Every slope, intercept, branch and output
is checked, including the full coefficient identity

\[
(mT+n)^2+(mT+n)-(T^3+T^2-2T)
=-(T-x)(T-u)(T-z).
\tag{3}
\]

Tangency also checks the derivative identity. Vertical tangents belong
to the inverse branch. The verifier independently translates by
X=x+1/3, Y=y+1/2 to

\[
Y^2=X^3-\frac73X+\frac{107}{108},
\]

whose denominators are invertible at every tested prime. It replays
each operation using the short-model law and checks all translated
curve equations and outputs. This translation fixes O and transports
the original group law, rather than selecting a different group.

For every finite group element A, including O, the saved chain is
2A=A+A, 3A=2A+A, 6A=3A+3A, 7A=6A+A. All four rows and every
image are retained, with duplicates. A second chain successively adds
A from O seven times; every intermediate is recorded in the replay
report and its 2,3,6,7 endpoints agree with the saved chain. Thus the
certificate covers the entire domain, not a subgroup or a sample.

The full bounded schedule gives:

| ell | #E(F_ell) | rho_ell(R) | size of full [7] image | outside image? |
|---|---:|---|---:|---|
| 11 | 16 | (1,0) | 16 | no |
| 13 | 17 | (6,2) | 17 | no |
| 17 | 24 | (1,16) | 24 | no |
| 19 | 15 | (17,18) | 15 | no |
| 23 | 28 | (4,14) | 4 | yes |

These five full enumerations test all 1469 affine pairs. All 415 saved
operations and 720 independent sequential operations pass. The saved
branch counts are 48 left-identity, 1 right-identity, 179 tangent,
156 chord and 31 inverse. No arithmetic failure occurred. Earlier
nonwitness primes are preserved; no prime greater than 23 is tested.

**The entire witness group and image.** For ell=23 the complete table
is as follows; coordinates are residues in 0,...,22.

| A in E(F_23) | [7]A |
|---|---|
| O | O |
| (0,0) | (18,1) |
| (0,22) | (18,21) |
| (1,0) | (18,1) |
| (1,22) | (18,21) |
| (3,5) | (13,11) |
| (3,17) | (13,11) |
| (4,8) | (18,21) |
| (4,14) | (18,1) |
| (5,1) | (18,1) |
| (5,21) | (18,21) |
| (6,7) | (13,11) |
| (6,15) | (13,11) |
| (7,7) | (18,21) |
| (7,15) | (18,1) |
| (9,7) | (18,21) |
| (9,15) | (18,1) |
| (13,11) | (13,11) |
| (16,6) | O |
| (16,16) | O |
| (18,1) | (18,21) |
| (18,21) | (18,1) |
| (19,2) | O |
| (19,20) | O |
| (21,0) | (13,11) |
| (21,22) | (13,11) |
| (22,1) | O |
| (22,21) | O |

The exhaustive affine-plane check verifies that this list has neither
omissions nor duplicates. All 28 multiplication chains, including
those meeting O or an inverse branch, are checked as described above.
The table proves the complete image in (1), retaining every preimage.

**Target identity and contradiction.** In F_23 the three target rows
of (2) are

| inputs | d | inverse of d | m | n | output |
|---|---:|---:|---:|---:|---|
| P,P | 1 | 1 | 21 | 0 | (3,5) |
| 2P,2P | 11 | 21 | 7 | 7 | (19,20) |
| Q,-4P | 18 | 9 | 18 | 5 | (4,14) |

Here -4P=(19,2). Independent sequential additions give
O, (0,0), (3,5), (9,7), (19,20) for the multiples 0,...,4 of P.
Negation is checked against the original equation and its sum with
4P is O. Since P and Q are integral and reduce to the displayed
points, the imported homomorphism gives

\[
\rho_{23}(Q-[4]P)=\rho_{23}(Q)-[4]\rho_{23}(P)=(4,14).
\]

This explicitly uses homomorphism compatibility; no separately reduced
rational coordinate for R is required. The target point is absent
from all four elements of the image (1). If R=[7]S for rational S,
the reduction homomorphism would put it in that image, a contradiction.
This proves R not in [7]E(Q).

**Separate fixed critical audit (step 380).** The full evidence is in
`scripts/global-reduction-audit-380/audit.json`, `fresh-replay.json`
and `intersection-certificate.json`. The audit command is

```bash
python3 -B scripts/global-reduction-audit-380/audit.py
```

The harness intentionally refuses to overwrite an existing `originals`
directory; reproducing it requires a fresh audit-output directory (a copy
of the harness in another directory immediately under `scripts/`).
It never executes or imports the producer. Its inventory and byte copies
bind the original producer, verifier, certificate and verification report
before execution; all four original files and their copies match afterward.
The certificate hash remains the one above. Fresh complete five-prime
replay equals the entire original report, including every sequential
chain, and checks all 1469 affine pairs, 415 saved operations and 720
sequential operations. No range extension occurs.

The distinct modulo-23 check enumerates the group by
`(2y+1)^2=4x^3+4x^2-8x+1`, recovering the same 28 elements. It constructs
all 784 ordered additions by a separate line-intersection computation.
For finite noninverse inputs `(x,y),(u,v)`, the secant coefficients are
`(A,B,C)=(y-v,u-x,xv-uy)`; at a repeated input they are the tangent
coefficients `A=-3x^2-2x+2`, `B=2y+1`, `C=-Ax-By`. Identity and
vertical cases are handled first, so B is nonzero. The polynomial

\[
G(T)=(-AT-C)^2+B(-AT-C)-B^2(T^3+T^2-2T)
\]

is exactly B² times the curve equation restricted to the line. Its
saved coefficient vector is
`(C²-BC,2AC-AB+2B²,A²-B²,-B²)`. Exact synthetic division first by
`T-x` and then `T-u` has zero remainders, including the tangent case
with its repeated root. The residual polynomial has nonzero linear
coefficient, so enumeration finds exactly one remaining root. The line
then gives exactly one y-coordinate. Negating this third intersection
gives the sum by the imported group law. Every polynomial, both
quotients and every exceptional case are persisted and checked;
the table has 55 identity, 27 vertical, 26 tangent and 676 secant rows.
This uses neither the producer's slope routine nor the verifier's
short-model routine.

For every group element the distinct chain `2A,4A,6A,7A` agrees with
the full original multiplication list, including all duplicate images.
Four successive subtractions of P, starting at Q, give

\[
(1,0),(22,1),(4,8),(13,11),(4,14).
\]

Thus the independent target calculation and full image agree with (1).
All 28 inputs and all 784 additions are covered, with zero failures.
The harness also recomputes the original invariants, Delta=389 and
the full rational short-model polynomial translation.

For the essential domain check, take K=Q_ell with its complete discrete
valuation and perfect finite residue field, for each of the five
retained primes. L030's exact integral equation is minimal; its
discriminant is a unit at each such ell. Every projective reduction
therefore lies on the smooth special fiber. In the notation of the
imported VII Proposition 2.1, E_0(K)=E(K). Reduction uses primitive
projective coordinates: scale a nonzero triple so its minimum valuation
is zero, then reduce. This applies also to a rational hypothetical
division point with nonintegral affine coordinates; no affine-integrality
assumption on that point enters the contradiction. The book's theorem,
with the cited author errata, supplies the homomorphism on this entire
domain. Its surjectivity is not needed. Translation denominators 2 and
3 are units at the retained primes, and the polynomial check verifies
the stated translation fixing O. These checks validate the exact
specialization rather than reprove the general reduction theorem.

The fixed critical audit passes. It adds no dependency beyond L030
and the already cited standard theorems. It validates this known-method
certificate, without extending its mathematical conclusion.

**Qualifications and comparison.** Cremona's published full basis
already covers the stronger group input, as explained in the prior
assessment; this calculation is useful as a separately reproducible
finite witness avoiding that unreplayed saturation premise. It does
not claim progress beyond the sources checked. L096 separately gives
the audited local relation at seven; it is not used in this global
proof. In particular the present result does not assert full
Selmer-kernel identification or the existence of a rational point of
zero local logarithm. Arbitrary-curve rank/order equality, uniform
rational directions, and the refined BSD formula remain unresolved.

## Mathlib

Full matching theorem and supporting exact Weierstrass group-law,
reduction-homomorphism and finite-enumeration coverage: not checked.
No absence claim is made. The named general theorems are imported
precisely above; only the approved fixed finite arithmetic is reproduced.
