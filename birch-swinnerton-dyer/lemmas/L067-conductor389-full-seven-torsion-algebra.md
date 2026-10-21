# L067 — The full nonzero seven-torsion algebra at conductor 389

## Hypotheses

Let E/Q be L030's exact nonsingular curve

\[
E:\quad y^2+y=x^3+x^2-2x.
\]

Use the entire geometric Galois set Z=E[7] minus {O}, not its quotient
by sign, and let R be the Q-algebra of Galois-equivariant functions
Z -> Qbar. No L026 premise, residual-surjectivity assumption, rank,
analytic order, Selmer dimension or Sha assertion is required here.

The complete finite evidence is `scripts/seven-torsion/certificate.json`.
It contains every rational coefficient, the entire 48-by-48 power
matrix and inverse, both coordinate maps in both models, rational
Bezout identities, the primitive integer field polynomial and complete
finite-field irreducibility witnesses. The independent exact replay is
`scripts/seven-torsion/verification.json`; the bounded altered-evidence
and original-byte-preservation report is
`scripts/seven-torsion/rejection-verification.json`.

Reproduction from the notebook directory uses only Python's standard
library:

```bash
python3 scripts/seven-torsion/build_certificate.py
python3 scripts/seven-torsion/verify_certificate.py
python3 scripts/seven-torsion/check_rejections.py
```

The verifier imports neither the producer nor its arithmetic routines.
This fixed production/replay and its separate critical audit pass.
The fresh audit report is `scripts/seven-torsion/audit-241/audit-report.json`.
It is a specialization of known algorithms, not a new descent theorem.

## Conclusion

Put a=-3024, b=46224, c(X)=X^3+aX+b. The rational change and inverse are

\[
X=36x+12,\quad Y=216y+108;\qquad
x=(X-12)/36,\quad y=(Y-108)/216.
\]

Define the following exact polynomials in Q[X]:

\[
\begin{aligned}
d_3&=3X^4+6aX^2+12bX-a^2,\\
A_4&=X^6+5aX^4+20bX^3-5a^2X^2-4abX-8b^2-a^3,\\
d_5&=32c^2 A_4-d_3^3,\\
d_7&=d_5d_3^3-128c^2 A_4^3,\qquad f=d_7/7.
\end{aligned}
\]

Then deg(f)=24, f is monic and squarefree, and gcd(f,c)=1. There is
an isomorphism, with the displayed full standard basis,

\[
R\simeq B:=\mathbf Q[X,Y]/(f(X),Y^2-c(X)),\qquad
\mathcal B=(1,X,\ldots,X^{23},Y,XY,\ldots,X^{23}Y).
\]

In this instance t=Y already separates all 48 points. The complete
certificate defines a monic polynomial h(T) of degree 48 and exact
polynomials X(T),Y(T),x(T),y(T) giving mutually inverse algebra maps

\[
R\simeq\mathbf Q[T]/(h(T)).
\]

In fact h is irreducible over Q: H=343h is a primitive integer
polynomial, and h has a degree-preserving irreducible reduction modulo
5. Thus the complete product-of-number-fields description consists of
**one field of degree 48**. It is the full nonzero torsion algebra,
not a degree-24 x-coordinate algebra or a single chosen point without
the remaining Galois conjugates.

This supplies the global algebra portion of L066 item 1. It supplies
no descent functions, incidence/scalar-action maps, chosen embeddings
or local factor identifications, complete units/classes, local-image
upper bounds, Selmer upper enclosure, D=D_div, successful localization
or rational Kummer membership. Divisible Sha and arbitrary-curve
complex-order/rank comparison remain unresolved. Even the other L026
premises remain separate; in particular L064's capped zero is retained.

## Proof

**Named inputs and applicability.** Import Sutherland, MIT 18.783,
Fall 2023,
[Lecture 5, Sections 5.5–5.6, pp. 9–14](https://math.mit.edu/classes/18.783/2023/LectureNotes5.pdf):
Lemma 5.20 (division-polynomial parity), Theorem 5.21 (multiplication
coordinates), Lemma 5.22 (degrees), Lemma 5.24 (no cancellation) and
Theorem 5.25 (degree/separability of multiplication). The formulas are
for a nonsingular short Weierstrass model, with characteristic two
and three excluded; Q satisfies these restrictions and 7 is nonzero.
The rational change above is origin-preserving and transports [7].
These are imported theorems; no general recurrence reproof is claimed.

Import Schaefer–Stoll, *How to do a p-descent on an elliptic curve*,
Trans. AMS 356 (2004), 1209–1231,
[author long version dated 13 June 2001, Section 5 step 2, printed p. 9](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf):
a rational function defined on the whole chosen finite set and
separating its points presents the equivariant function algebra by
its characteristic product. The required separation is proved here
by the full power matrix, not assumed for a y-coordinate.

For irreducibility import the finite-field power/gcd test, specifically
Lenstra, *Factorization of Polynomials*, MC Tracts 154/155 reprint,
[Section 5, Test 2 (Rabin), p. 181](https://infoscience.epfl.ch/server/api/core/bitstreams/3154505c-23e7-4fd4-be73-e8c8b9c85951/content).
For a monic degree-n polynomial over F_q the test is
T^(q^n)=T modulo it and gcd(T^(q^(n/l))-T,h)=1 for every prime l|n.
The reduction here is also independently checked squarefree. Gauss's
lemma and degree-preserving reduction then give rational irreducibility.
No converse or guarantee of finding a successful prime is used.

**Transport and all nonzero kernel points.** The verifier expands the
complete polynomial identity

\[
Y^2-X^3-aX-b
=46656\,(y^2+y-x^3-x^2+2x)
\]

under the stated substitution, and checks its inverse. L030 supplies
nonsingularity (also the identity 112^3-(-856)^2=1728*389 is replayed).
In short coordinates the cited bases are psi_1=1, psi_2=2Y,
psi_3=d_3, psi_4=4Y A_4. The odd recurrence at indices five and seven
is respectively

\[
\psi_5=\psi_4\psi_2^3-\psi_3^3,
\qquad
\psi_7=\psi_5\psi_3^3-\psi_2\psi_4^3.
\]

Replacing Y^2 by c gives exactly d_5 and d_7 above. The independent
verifier does bivariate multiplication followed by this substitution;
it checks every saved coefficient and d_7=7f with degree 24 and leading
coefficient seven. There is no unevidenced division by a coordinate
or a canceled kernel point.

The saved rational polynomials u,v,s,w satisfy, as full coefficient
identities checked by replay,

\[
u f+v f'=1,\qquad s f+w c=1.
\]

Consequently f has 24 distinct roots over Qbar, and c is nonzero at
each. Each root gives two distinct nonzero Y values. The division-
polynomial multiplication theorem, including its no-cancellation
statement, identifies precisely these 48 points with the nonzero
kernel of [7]. This also agrees with separability and deg([7])=49,
retaining O as the omitted point. The construction is Galois-equivariant
because both equations and the coordinate change are rational. By the
Chinese remainder theorem over Qbar, B becomes the full product of
48 copies of Qbar. Descent identifies B with R. Monic reduction first
in Y and then in X gives the displayed Q-basis of size 48; it is not
merely a dimension label inferred from a characteristic polynomial.

**Faithful separating element and coordinate maps.** Let M have, as
column j for 0<=j<48, the B-coordinates of Y^j, and let v_48 be the
coordinates of Y^48. The certificate supplies the full M and N with
MN=NM=I_48. The verifier reconstructs all 49 powers directly in B,
checks every matrix column and all 4608 scalar inverse identities.
Define, preserving all 48 coefficient slots,

\[
h(T)=T^{48}-\sum_{j=0}^{47}(N v_{48})_j T^j.
\]

The verifier checks h's full degree and monicity and all coordinates
of h(Y)=0. The map Q[T]/(h) -> B, T -> Y, is a homomorphism whose
matrix on the two size-48 bases is invertible. Hence it is an algebra
isomorphism. Since B is etale, this also proves Y separates all 48
geometric points.

Let e_X,e_Y be their coordinate vectors in the standard B-basis.
The saved coordinate polynomials have coefficient vectors N e_X and
N e_Y. The verifier checks both inverse maps; all 96 products of X
or Y with the standard basis agree under transport to Q[T]/(h).
Independently, direct rational polynomial reduction modulo h verifies

\[
f(X(T))=0,\quad Y(T)^2=c(X(T)),\quad Y(T)=T,
\]

and, for x(T)=(X(T)-12)/36 and y(T)=(Y(T)-108)/216,

\[
y(T)^2+y(T)=x(T)^3+x(T)^2-2x(T).
\]

Thus the presentation retains both coordinates and inverse maps,
rather than relying on a resultant or floating roots. The first
candidate k=0 in t=Y+kX succeeds, within the prescribed k<=64 cap.

**Complete field identification.** The certificate gives every
coefficient of H=343h, checks integrality, positive leading coefficient
343 and content one. Modulo five the complete ascending coefficient
vector of h is

```text
[3,0,0,0,1,0,1,0,1,0,0,0,1,0,4,0,1,0,3,0,1,0,2,0,2,
 0,0,0,1,0,0,0,1,0,1,0,3,0,4,0,2,0,1,0,0,0,3,0,1].
```

The nonzero leading coefficient is retained and 5 does not divide
343. The independently replayed search tests only primes 2,3,5,
stopping at its first success: reductions at two and three have
derivative gcd of degree 48 and are rejected. At five the derivative
gcd is one. The complete saved sequence r_i, 0<=i<=48, satisfies
r_0=T and r_i=r_(i-1)^5 modulo hbar, with r_48=T. To distinguish it
from the producer's binary modular powers, the verifier uses the
characteristic-five identity (sum c_j T^j)^5=sum c_j T^(5j), followed
by long reduction, on every coefficient at every step. The two saved
full modular Bezout identities are

\[
u_{16}\bar h+v_{16}(r_{16}-T)=1,\qquad
u_{24}\bar h+v_{24}(r_{24}-T)=1.
\]

They cover all prime divisors 2 and 3 of 48, because 48/2=24 and
48/3=16. The cited test proves hbar irreducible. Multiplication by
the nonzero constant 343 modulo five preserves that conclusion for
Hbar, so Gauss's lemma proves H, and hence h, irreducible over Q.
There is exactly one rational field factor of degree 48. The complete
factor identity is h=h, the projection is T -> T and the sole
idempotent is one; the verifier checks these full maps. There are no
distinct pairs of factors requiring additional Bezout identities.
The successful prime five is within the prescribed prime<=200 cap.

**Finite evidence and limits.** The full replay passes 4852 checks
with no failures, including both rational Bezout identities, both
matrix inverse products, all coordinate and defining-equation checks,
all generator products and all modular witnesses. The two bounded
copies change a d_7 coefficient or remove the X(T) map. The independent
verifier rejects them respectively at `psi7_odd_recurrence` and
`required_fields`; hashes prove all four original certificate/code/
draft artifacts remain unchanged during these tests.

An initial unverified producer artifact is preserved as
`scripts/seven-torsion/producer-draft-v0.json`. Trimming the zero
T^47 coefficient before appending the leading term wrongly gave degree
47. Its tests are invalid evidence and support no mathematical claim.
The corrected certificate keeps all 49 h coefficients and independently
passes the degree-48 annihilation and field checks. The rejection report
records this precise draft defect and its preserved hash. No cap was
extended and no failed mathematical route was discarded.

The finite arithmetic proves this instance only. It does not certify
universal software correctness or any of the subsequent descent data
listed in the conclusion. No progress beyond the known general
construction and irreducibility algorithms is claimed.

**Separate critical audit (2026-10-15, step 241).** The audit read the
complete proof and both independent arithmetic implementations. The
short-model substitution extends projectively to an isomorphism taking
O to O: its projective linear map is
[x:y:z] -> [36x+12z:216y+108z:z], with nonzero determinant.
Thus the imported multiplication theorem applies to the transported
group law. The two Bezout identities ensure that every affine kernel
root is simple and has two distinct Y-coordinates. The no-cancellation
theorem identifies all these points, and the separable degree 49 leaves
exactly the omitted O. No residual-image hypothesis enters this argument.

The full power matrix and both inverse identities identify the entire
48-dimensional algebra, rather than a selected orbit or a quotient.
An isomorphism over Q remains an isomorphism over Qbar, so the power
basis really does imply geometric separation by Y. The complete
coordinate transports retain Y=T, f(X(T))=0 and both curve equations;
the 96 generator-product checks verify multiplication on every basis
element. Irreducibility uses the full 48-step Frobenius chain and both
indices 16=48/3 and 24=48/2, covering every prime divisor of 48. Integrality,
content one and degree preservation justify Gauss's lemma for H=343h.

Fresh complete replay passes the same 4852 checks without changing any
original evidence. The distinct cross-check in
`scripts/seven-torsion/audit_certificate.py` uses none of either program's
arithmetic or the saved Y-power matrix/inverse. Let C be multiplication
by c(X) on A=Q[X]/f in the basis 1,X,...,X^23. It constructs C directly
by reducing the 24 polynomials X^j c(X), of degrees at most 26, and
checks that 7C has integer entries. Integer Bareiss elimination, checking
every exact division and retaining every pivot, gives

\[
\det(7t^2 I_{24}-7C)=7^{24}h(t),\qquad t=0,1,\ldots,24.
\]

Every one of the 25 differences is exactly zero. The full certificate
is `scripts/seven-torsion/audit-241/determinant-crosscheck.json`.
All odd coefficients of h are zero. Writing h(T)=g(T^2), both
det(z I-C) and g(z) have degree at most 24; their equality at the 25
distinct rational numbers 0^2,...,24^2 proves the polynomial identity.
This is a separate exact check on all coefficients of h, including
its degree padding. Its relation to the original construction is also
explicit: on B=A direct-sum AY, multiplication by Y has block matrix
[[0,C],[I,0]], whose characteristic polynomial is det(T^2 I-C).
The already verified cyclic Y-power basis has characteristic polynomial
h. This cross-check supplements, rather than replaces, faithful basis
and inverse-map evidence.

Six fresh rejection cases pass: changed psi7 coefficient, missing X(T),
changed h constant, changed Frobenius step 24, the original invalid
draft, and a complete-schema copy with only that draft's h substituted.
Their respective rejection labels are `psi7_odd_recurrence`,
`required_fields`, `h_annihilation_all_coordinates`,
`mod5_frobenius_24`, `required_fields`, and `h_monic_degree48`.
The original draft lacks `factor_denominator`, `factors`,
`primitive_integer_factors` and `product_maps`, so its own replay stops
before inspecting the degree. The first audit harness incorrectly
expected it to reach the degree check. That failed expectation and the
initial harness are preserved in
`scripts/seven-torsion/audit-241/initial-audit-report.json`
and `scripts/seven-torsion/audit-241/initial-audit-script.py`; the isolated h fixture then
tests the intended degree failure directly. This is a test-expectation
repair, not a change to any production proof or evidence. No failed
report is silently treated as passing.

Hashes before and after match for all eleven original files, including
the invalid draft, both original rejection copies and their reports.
The audit commands, from this notebook directory, are:

```bash
python3 scripts/seven-torsion/verify_certificate.py --report scripts/seven-torsion/audit-241/complete-replay.json
python3 scripts/seven-torsion/audit_certificate.py
```

The audit passes only this fixed torsion-algebra result. It activates
none of the absent functions, scalar/incidence maps, units/classes,
local conditions or residual-nonvanishing premises of the descent
application. There is no Selmer bound or BSD candidate.

## Mathlib

Full matching coverage for the seven-division-polynomial kernel theorem,
this explicit torsion algebra, coordinate transport and complete finite
field certificate was not checked. No absence claim is made. The named
primary sources above are the mathematical inputs; the saved exact
certificate and independent replay are instance evidence, not a Lean
formalization.
