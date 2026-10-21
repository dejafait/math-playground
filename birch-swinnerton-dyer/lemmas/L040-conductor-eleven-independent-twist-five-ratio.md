# L040 — Independent twist-five ratio for the conductor-eleven model

## Hypotheses

Let E/Q have minimal equation y^2+y=x^3-x^2-10x-20, with coefficients
[0,-1,1,-10,-20]. Let E^5 denote its global minimal positive quadratic
twist by five. For either curve, Omega is the integral of the absolute
minimal Neron differential over its entire real locus. Let f=sum a_n q^n
be E's normalized newform.

Use audited L039 only for minimality, Delta=-11^5, conductor N=11 and
modularity. Its relative functional and unknown scalar are not used.
The named optimality, torsion, denominator, analytic and period inputs
below are imported with their qualifications. No BSD, Sha finiteness,
rank, twist nonvanishing or additive-twist Manin constant is assumed.

Complete finite evidence is `scripts/conductor-eleven/twist-five/certificate.json`,
SHA256 `05f37f3d5bbc5d162e35477ed4858a9dbed947bf23ff72378338b074b9f002c0`.
The separate arithmetic replay is
`scripts/conductor-eleven/twist-five/verification.json`. Reproduction:

```bash
python3 scripts/conductor-eleven/twist-five/certify.py
python3 scripts/conductor-eleven/twist-five/verify.py
```

The verifier does not import the construction program. Both adapt the
previous exact-interval methodology to this model, but no previous ratio,
period enclosure or coefficient is imported. External source theorems
are not verified by scripts. The separate critical audit of the mathematical
assembly and complete fixed-instance evidence passes, as recorded below.

## Conclusion

The reduced denominator of q=L(E^5,1)/Omega(E^5) is at most B=10.
The complete first scheduled enclosure, at T=128 and S=2^48, gives

\[
q\in\frac{[1407374883553087,1407374883553487]}{281474976710656},
\qquad
\operatorname{width}=\frac{25}{17592186044416}<\frac1{100}=\frac1{B^2}.
\tag{1}
\]

The sole reduced rational of denominator at most ten in this interval is
5, so the independently audited certificate establishes q=5 != 0, retaining
the published optimality qualification below. This is a fixed known-method reproduction,
not progress beyond the cited algorithms. It supplies the independent
ratio input for later use of L028 with audited L039, at good ordinary
p>=5, p!=5. It does not normalize any symbols or produce a coefficient,
point witness, rank comparison, Sha elimination or arbitrary-curve result.

## Proof

**Optimality and a denominator before numerical recovery.** Import the
exact primary [Cremona ecdata row](https://raw.githubusercontent.com/JohnCremona/ecdata/master/allcurves/allcurves.00000-09999),
`11 a 1 [0,-1,1,-10,-20] 0 5`, with
[Table One conventions](https://johncremona.github.io/ecdata/).
Only the exact model/label and torsion order five are used; the rank column
is unused. Cremona's appendix to Agashe--Ribet--Stein, *The Manin constant*,
[Theorem 5.2](https://wstein.org/papers/ars-manin/html/node13.html),
identifies label one as optimal and its Manin constant as one at N<60000,
apart from the label exception 990h. This exact model at independently
proved N=11 meets the theorem. Import its published computational
verification, including its complete-isogeny-class/two-period comparison
qualification, rather than substitute a decimal period guess or reprove
optimality. Alternatively, Cesnavicius, *The Manin constant in the
semistable case*, [arXiv:1703.02951, Theorem 2.13, printed p.9](https://arxiv.org/pdf/1703.02951),
gives zero valuation at every prime of the positive rational Manin
constant for the new optimal quotient of J_H with
Gamma_1(n) contained in H contained in Gamma_0(n), provided the square
of that prime does not divide n. Here H=Gamma_0(11), and squarefree n=11
meets that condition at every prime, again giving constant one on the base.
Neither theorem is applied to the additive twist.

Wuthrich, *Numerical modular symbols for elliptic curves*,
[arXiv:1608.06423v2 (23 March 2017), Proposition 1, pp.3--4](https://arxiv.org/pdf/1608.06423v2),
under the strong-Weil constant-one hypothesis, gives
[r]^+ in c_infinity/(2 #E(Q)_tors) Z at unitary cusps, with
lambda(r)=2 pi i integral_infinity^r f(z) dz and
[r]^+=Re(lambda(r))/Omega_+, where Omega_+ is the least positive real
period. The negative discriminant gives one real component, so
c_infinity=1 and Omega(E)=Omega_+. At all a/5, 1<=a<=4, the unitary
condition holds: M=gcd(5,11)=1 and Q=11/M=11 are coprime. Therefore

\[
[a/5]^+\in\frac1{10}\mathbf Z.                              \tag{2}
\]

Let chi be the primitive quadratic character modulo five, with
values (0,1,-1,-1,1). Cremona, *Algorithms for Modular Elliptic Curves*,
corrected second edition (1997), [Chapter 2, Section 2.11,
Propositions 2.11.1--2.11.2 and the character identity preceding
(2.11.4), pp.37--39](https://johncremona.github.io/book/fulltext/chapter2.pdf),
gives the oriented character-cycle integral sqrt5 L(E^5,1).
Here five is an odd prime away from N, chi(-1)=1 and the Gauss sum
is the positive sqrt5. Since sum chi(a)=0, replacing {0,a/5} by
{infinity,a/5} leaves the character cycle unchanged. Taking real parts,

\[
\sqrt5 L(E^5,1)=\Omega_+\sum_{a=1}^4\chi(a)[a/5]^+.
\tag{3}
\]

Pal, *Periods of quadratic twists of elliptic curves*,
[arXiv:1012.0094v2 (21 January 2011), Corollary 2.6 and Theorem 3.2,
pp.6--8](https://arxiv.org/pdf/1012.0094v2),
gives the positive minimal-twist total-period formula. Its conditions
are satisfied: E is minimal, d=5 is positive squarefree, d=1 modulo 4,
and gcd(5,Delta)=1. The minimalization factor is one, hence
Omega(E^5)=Omega(E)/sqrt5=Omega_+/sqrt5. Thus (2)--(3) imply

\[
q=\sum_{a=1}^4\chi(a)[a/5]^+\in\frac1{10}\mathbf Z.           \tag{4}
\]

This proves B=10, independently of all numerical enclosures and the
L039 functional. The bound is conservative; pairing cusps to improve it
is unnecessary. The conclusion also applies if q=0.

**Exact sign, coefficients and the infinite tail.** Cremona,
[Chapter 3, Section 3.9, pp.102--103](https://johncremona.github.io/book/fulltext/chapter3.pdf),
identifies a_p with p+1 minus the point count of the reduced minimal
equation, including the bad-prime case. For odd p, the affine count is
p+sum_x Legendre(1+4(x^3-x^2-10x-20),p). The certificate records every
character for every prime p<=128. At two it counts the four affine
pairs directly. There is one point at infinity in each projective model.
At 11 the character vector is
(1,-1,0,1,-1,0,1,1,-1,-1,-1), giving ten affine points, eleven total
and a_11=1. The replay independently exhausts y at each x, at every
listed prime, and checks the entire prime list by trial division.

At the single multiplicative prime, the Fricke eigenvalue is
epsilon_11=-a_11=-1; use Wuthrich, cited above, Section 4.1, or
Cremona [Chapter 2, Section 2.6, pp.24--25](https://johncremona.github.io/book/fulltext/chapter2.pdf).
Exactly chi(-11)=chi(4)=1=-epsilon_11, so Proposition 2.11.2 gives
the allowed branch

\[
L(E^5,1)=2\sum_{n\ge1}\frac{\chi(n)a_n}{n}\rho^n,
\qquad \rho=\exp\left(-\frac{2\pi}{5\sqrt{11}}\right).
\tag{5}
\]

The twist's root number is +1. That sign does not imply nonvanishing.
The alternative sign in the cited proposition would force zero; it is
excluded here by exact arithmetic, rather than assumed away.

Import the all-prime recurrence and Euler product from Cremona,
Chapter 2, (2.6.1)--(2.6.2), p.25, and (2.8.3), p.29. With a_1=1,
coprime multiplicativity and the counted a_p, for k>=2 use
a_(p^k)=a_p a_(p^(k-1))-p a_(p^(k-2)) at good p, and
a_(11^k)=a_11 a_(11^(k-1)) at the multiplicative prime. In particular,
a_121=1, not the value from a good-prime recurrence. Every n<=128
has its full factorization and prime-power sequence stored and replayed.
Modularity from L039 identifies these arithmetic coefficients with f.

Wuthrich, Lemma 4 and its proof, pp.6--7, supplies the all-n bound
|a_n|<=n and geometric-tail method. Therefore the omitted part at T is
at most 2 rho^(T+1)/(1-rho) in absolute value. The finite coefficient
check does not justify this infinite bound; the imported theorem does.

**All outward errors.** Put S=2^48. An integer interval [l,u] means
[l/S,u/S]. Addition/subtraction use the appropriate endpoint sums;
multiplication takes minimum/maximum of the four products; division
takes minimum/maximum of the four quotients and requires a strictly
positive denominator interval. Scale by an exact signed rational and
sort the endpoints. Round each rational lower endpoint down by floor(Sx)
and each upper endpoint up by ceil(Sx). These rules enclose every finite
rounding error, including negative summands. Square-root endpoints are
integer-square-root bounds satisfying l_root^2<=l S and
u_root^2>=u S, with one upward adjustment if necessary.

For pi use Machin's identity 16 atan(1/5)-4 atan(1/239). For completeness,
tan(4 atan(1/5))=120/119 by two tangent doublings, and subtracting
atan(1/239) gives tangent one. This angle is positive, as follows from
atan(1/5)>1/5-(1/5)^3/3 and atan(1/239)<1/239, and is less than
4/5<pi/2. Hence it equals pi/4, proving the identity. Adjacent alternating
partial sums of atan x enclose it for 0<x<1; this follows by integrating
the finite geometric-series remainder for 1/(1+x^2). With 24 terms and
the next term, the certificate saves both exact rational brackets before
outward rounding, giving pi in [884279719003555,884279719003556]/S.

The square-root rule gives sqrt11, and outward division gives
h=2 pi/(5 sqrt11) strictly in (0,1). At each h endpoint adjacent
degree-32/33 Taylor sums of exp(-h) enclose the value: the alternating
terms decrease to zero because 0<h<1. Its decreasing dependence on h
reverses the endpoints. The exact rational Taylor brackets and all
roundings give rho in [192703593019171,192703593019173]/S.
This uses no floating-point error assumption or numerical-library output.

Successive outward products enclose every rho^n, and each exact signed
weight 2 chi(n)a_n/n is applied before accumulation. All 128 powers and
partial sums are retained. One further product encloses rho^129; using
its upper endpoint and the upper endpoint rho_u<1 gives an outward
tail at least 2 rho^129/(1-rho), namely 20/S. Finite rounding makes this
conservative bound larger than the exact analytic tail. After adding and
subtracting it, the complete enclosure is

\[
L(E^5,1)\in[798836759342276,798836759342472]/S.               \tag{6}
\]

**One-real-root period with its correct component factor.** Completing
the square gives (y+1/2)^2=g(x)=x^3-x^2-10x-79/4, with minimal
differential dx/(2y+1)=dx/(2(y+1/2)). The cubic discriminant is Delta/16<0,
so there is exactly one real root r. H=4g satisfies H(4)=-47 and
H(5)=121. Exact sign-preserving bisection isolates it at
[1223376987608197,1223376987608198]/S. Every midpoint and sign is
stored and replayed, with width 1/S and no approximate sign test.

Write the conjugate roots as u+iv,u-iv with v>0. Vieta gives
u=(1-r)/2 and u^2+v^2=r^2-r-10, hence
v^2=(3r^2-2r-41)/4. Put d=r-u=(3r-1)/2 and R=sqrt(d^2+v^2).
For z=sqrt(r-(u+iv))=s+it, with s>0, one has
|z|=sqrt(R) and s=sqrt((R+d)/2): indeed |z|^2=|d-iv|=R and
s^2-t^2=d, s^2+t^2=R. The replay encloses every operation and certifies
d>0 and v^2>0; the latter interval is
[491073031263359,491073031263368]/S. All square roots take the
positive real branch. These algebraic substitutions implement the
already reviewed period formula, rather than introduce another identity
for the period or transplant the three-real-root case.

Import Cremona [Chapter 3, Section 3.7, negative-discriminant paragraph,
printed p.98](https://johncremona.github.io/book/fulltext/chapter3.pdf):
with real root e3=r and e1=u+iv, the displayed period-lattice basis has
positive real generator lambda_1=pi/AGM(|z|,s). The differential above
is exactly its completed-square differential. Since Delta<0, E(R) is
connected and the full real-locus absolute integral is this generator:
real uniformization pulls the invariant differential back to dt on the
real circle of length lambda_1. There is no extra factor two.

For the positive AGM iteration use [DLMF 19.8.1--19.8.5](https://dlmf.nist.gov/19.8.i).
At each step replace A,G by (A+G)/2,sqrt(AG). Both new exact values
lie between the previous minimum and maximum by the arithmetic-geometric
inequality; their common limit therefore lies within every finite bracket.
Outward induction encloses the exact iterates even if rounding prevents
further contraction. The initial intervals are
A in [698754208831927,698754208831929]/S and
G in [694682796946295,694682796946296]/S. After twelve steps the
minimum of the lower endpoints and maximum of the upper endpoints give
AGM in [696717015879027,696717015879041]/S, a strictly positive bracket.
All thirteen states and both operations at each step are replayed.

Divide the pi interval by this bracket to enclose Omega(E)=lambda_1,
then apply the already justified Pal comparison and the positive sqrt5
interval. This gives the total minimal twist period

\[
\Omega(E^5)\in[159767351868471,159767351868477]/S>0.          \tag{7}
\]

**Rational existence, isolation and replay.** Outward division of (6)
by (7) gives (1), including its width and positivity. For each 1<=b<=10,
every admissible numerator is in
ceil(b q_lower)<=a<=floor(b q_upper). The full exact enumeration finds
the singleton range a=5b at each denominator. Only b=1 gives a reduced
fraction, since gcd(5b,b)=b. Moreover 5S=1407374883553280 lies strictly
between both endpoints of (1). Thus 5 is present and is the only reduced
rational of denominator at most ten. By (4) the actual q belongs to this
finite set, so q=5. The width inequality is checked separately; it does
not establish rational existence on its own.

Only the first of the authorized (T,bits)=(128,48),(256,64),(512,96)
pairs was used. The verifier reads the full certificate and checks all
prime counts, factorizations and bad-prime sequences, exact Taylor errors,
every power and partial sum, the infinite-tail enclosure, every bisection
sign, every Vieta/square-root/AGM interval, the component and twist factors,
and all ten denominator ranges. Its seven grouped arithmetic checks pass
with no failures. It checks declared source parameters, not the truth of
optimality, torsion or external theorems. Those are the cited mathematical
inputs above; their specialization and the complete programs passed the
separate audit below. Calibration, coefficient calculation
and any rank/complex-order comparison remain separate work.

**Separate critical audit (2026-10-10).** Under the prior SPECIALIZE
assessment, the entire proof and both complete programs were reviewed.
The canonical certificate hash above is unchanged. Reproduce the audit by

```bash
python3 scripts/conductor-eleven/twist-five/audit.py
```

The complete record is `scripts/conductor-eleven/twist-five/critical-audit/audit.json`;
the distinct enclosure is the adjacent `independent-enclosure.json`.
All original construction/replay programs, certificate and report, and the
audit program are copied and hashed under `originals/` before execution;
`pre-replay-manifest.json` binds those bytes. The full replay runs on copies
under `replay/`, writes a fresh report, and agrees with the original report.
All seven groups pass. No original input or report is overwritten.

The source specialization survives review. The exact model/label and
torsion import, N=11 from audited L039, and Cremona's Theorem 5.2 put the
base within the published optimality/constant-one verification; its
complete-class/two-period computational qualification remains a premise.
This is not a new proof of that verification. Wuthrich Proposition 1's
unitary rational-cusp case gives the stated lattice for the four cusps,
using the least positive real period. Negative discriminant makes that
the total real period here. The oriented character sum and Pal's positive
minimal-twist factor one then give (4) before any enclosure. No rank, BSD,
additive-twist Manin constant or unknown L039 scalar enters this argument.

The Fricke case is fixed by a_11=1 and chi(-11)=1. Complete point-count and
Euler-factor replay includes the multiplicative a_121=1; the good-prime
recurrence there would be wrong. Wuthrich v2 Lemma 4's complete proof on
printed p.7 was checked directly: its all-n coefficient bound justifies
the omitted infinite sum, independently of the finite coefficient check.
The factor two and index 129 in our tail follow from (5) and T=128.
The signed endpoint rules enclose negative summands; every division has
a positive denominator. The square-root bounds enclose exact nonnegative
roots, and both elementary alternating remainders have decreasing terms
on their certified domains. No floating-point assertion is used.

Cremona Section 3.7's full negative-discriminant passage, pp.97--98, was
checked directly against the completed-square cubic and minimal differential.
The substitutions u=(1-r)/2, v^2=(3r^2-2r-41)/4, d=(3r-1)/2 and
R=sqrt(d^2+v^2) have exactly the stated signs and give
|z|=sqrt(R), Re(z)=sqrt((R+d)/2). The conjugate square-root choice has
positive real part. The resulting positive real lattice generator is the
total period on the single real component. This accounts for the factor
which would differ for a disconnected real locus. At each AGM iteration
the exact two entries lie within their outward intervals, and the common
limit lies between those exact entries; hence the minimum lower endpoint
and maximum upper endpoint enclose it even when rounding widens later
brackets. The original thirteen states and all 48 bisection signs pass.

To test correlated rounding errors, the audit also recomputes the same
T=128, b=48 instance with exact rational endpoints. It uses the fully
replayed Machin and exponential remainders, rounds rho once, and computes
each endpoint power directly as rho_lower^n and rho_upper^n. It applies
the signed rational coefficient to those endpoints and sums without
intermediate rounding; positivity of rho makes these power bounds valid.
The independent tail is exactly 2 rho_upper^129/(1-rho_upper), and is
at most the original 20/S. No later truncation/precision pair is used.

For the period, independent integer evaluation of
4k^3-4k^2 S-40k S^2-79S^3 determines every new bisection sign at k/S,
without consuming the stored sign trace. It yields the same root bracket.
The Vieta and AGM operations are recomputed with exact Fraction endpoints;
only square roots are rounded to denominator S. For a nonnegative
rational endpoint x, taking isqrt(floor(x S^2)) and adjusting the upper
endpoint upward when necessary proves the squared endpoint inequalities.
Interval addition, multiplication and positive division preserve inclusion;
thus induction proves all stored alternative period intervals valid.
Full exact endpoint powers, summands, partial sums, tail, root signs,
Vieta values, AGM states, period and ratio are saved, not just previews.

This distinct calculation gives

\[
q\in[1407374883553264,1407374883553305]/281474976710656,
\qquad\text{width}=41/281474976710656<1/100.
\]

It is contained in (1), and its endpoints strictly straddle
5S=1407374883553280. Complete enumeration again gives exactly the ten
numerator ranges [5b,5b], 1<=b<=10; only b=1 is reduced. Combined with
(4), this verifies q=5 with existence as well as uniqueness. The alternative
enclosure reuses source identities and the completely replayed coefficients;
it is a test of different finite arithmetic, not independent verification
of the external theorems or universal software correctness.

Five separate altered-evidence trials were rejected: changing a_121 to
-10, deleting the tail, doubling the total-period component factor,
replacing the AGM bracket by [1,1], and replacing the rational candidate
by 6. Each trial uses an in-memory copy and the complete replay function;
original bytes remain unchanged. These tests supplement the proof of the
checker contract; they cannot by themselves establish mathematical validity.
There are no audit failures and no mathematical correction was needed.
This validates a known-method fixed input, not a new theorem beyond the
sources checked, a general coefficient-production method, or a BSD candidate.

## Mathlib

Full matching independent elliptic twist-value certificate: not checked.
Coverage of the named optimality, unitary-cusp, character-cycle,
minimal-period, Euler-factor and AGM results: not checked. Unknown coverage
is not evidence of absence. The fixed-input interval bookkeeping is
reproduced here; no claim of a new algorithm or a uniform theorem is made.
