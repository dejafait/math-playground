# Quartic differential preservation does not imply nonreal-count contraction

## Hypotheses

Work over the real polynomials, with D=d/dx and Z_c(f) the number
of nonreal zeros of a nonzero polynomial f, counted with multiplicity.
Set
\[
 q(z)=1-z^2+\tfrac32 z^4,\qquad T=q(D),\qquad
 p(x)=x^4+15x^2-1.
\]
Here q has rational coefficients, q(0)=1 and degree four, and p is
a monic rational quartic. Real-rooted quartics in the conclusion
have degree exactly four; repeated roots and arbitrary nonzero real
leading coefficients are allowed.

## Conclusion

For every real-rooted real quartic f, Tf is a real-rooted quartic.
Nevertheless,
\[
 Z_c(p)=2,\qquad Tp=x^4+3x^2+5,\qquad Z_c(Tp)=4.
\]
Thus universal real-rootedness preservation in this fixed degree does
not imply contraction of the multiplicity-aware nonreal-root count
on arbitrary real quartics.

This is a finite-degree obstruction only. It does not claim preservation
in all degrees, nonnegative coefficients of q, a prescribed sector for
the zeros of q, realization by the actual Xi/Jensen family, or any
improvement of the actual unshifted Jensen exceptional-root deficit.

## Proof

**Imported preservation input.** Use Walsh's convolution theorem as
stated in Thomas Craven and George Csordas, *Location of zeros. Part I:
Real polynomials and entire functions*, Illinois J. Math. **27**(2)
(1983), 244--278, Theorem 3.3 (p.257), and remarks (1) and (3)
(p.258), [author-hosted primary scan](https://math.hawaii.edu/~tom/mathfiles/locationI.pdf),
[matching scan](https://scispace.com/pdf/location-of-zeros-part-i-real-polynomials-and-entire-z3v2jd50yw.pdf).
The statement and remarks on both pages were retrieved in this step;
the author-hosted parsed page initially loaded but subsequent range
requests timed out, and the matching scan supplied the full relevant
range. This imports the named theorem, rather than reproving it.

In the notation needed here, if f and g are degree-n polynomials,
g(x)=sum_(j=0)^n b_j x^j, and all zeros of f lie in a circular region C,
then the zeros of
\[
 W(f,g)(x)=\sum_{k=0}^n (n-k)!\,b_{n-k} f^{(k)}(x)
\]
lie in the union of the translates C+beta as beta runs through the
zeros of g. Circular regions include closed half-planes. In particular,
when f and g are real rooted, apply the theorem first with C the closed
upper half-plane and then with C the closed lower half-plane: translating
either by a real beta leaves it unchanged, so every zero of W(f,g) is
real. The theorem and this specialization impose no simple-root
hypothesis. If f and g have leading coefficients a_n,b_n, the leading
coefficient of W is n! a_n b_n, so it is nonzero and has degree n.
This is precisely remark (3); no nonreal-count assertion is imported.
Theorem 3.4's nonnegative-factorial-coefficient hypothesis is not used.

**Exact correspondence.** Take n=4 and
\[
 g(x)=Tx^4=x^4-12x^2+36=(x^2-6)^2.
\]
All four zeros of g are real: +sqrt(6) and -sqrt(6), each twice.
With b_4=1,b_2=-12,b_0=36 and b_3=b_1=0, the displayed convolution
gives, for every real quartic f,
\[
 \frac{W(f,g)}{4!}
 =f+\frac{2!(-12)}{4!}f''+\frac{0!36}{4!}f^{(4)}
 =f-f''+\tfrac32 f^{(4)}=Tf.
\]
Consequently Walsh applies to every real-rooted f of degree four,
including repeated roots of f and the double roots of g. Since T's
constant term is one and differentiation lowers degree, Tf has the
same leading coefficient as f. This proves universal preservation
without relying on a finite test set of hyperbolic inputs.

**Input and output counts.** Writing y=x^2, the two roots of
y^2+15y-1 are
\[
 y_+=\frac{-15+\sqrt{229}}2>0,\qquad
 y_-=\frac{-15-\sqrt{229}}2<0,
\]
because 229>225. They are distinct and nonzero. Hence p has the
two distinct real roots +/-sqrt(y_+) and the two distinct nonreal
roots +/-i sqrt(-y_-). Thus Z_c(p)=2 with multiplicity.
Now p''=12x^2+30 and p^(4)=24, whence
\[
 Tp=p-p''+\tfrac32p^{(4)}=x^4+3x^2+5.
\]
For every real x this is at least 5, so it has no real zeros. Its
degree is four, so the fundamental theorem of algebra gives four
nonreal zeros counted with multiplicity. In fact the output is
squarefree: its derivative is 2x(2x^2+3); at x=0 the output is 5,
and at x^2=-3/2 its value is 11/4, both nonzero. This last check is
not needed to infer the multiplicity-aware count, but excludes any
hidden repeated-root convention in the witness.

**Exact arithmetic cross-check.** Run
`python3 scripts/quartic-differential/certificate-1463.py`.
The full rational certificate is
`scripts/quartic-differential/certificate-1463.json`.
It verifies the operator/convolution identity on the entire monomial
basis of degree at most four, the Appell factorization, the output
identity and the complete Sturm sequences. The input variations at
(-infinity,+infinity) are (3,1), and the output variations are (2,2);
the last Sturm remainders are nonzero constants, confirming two and
zero real roots with squarefree input and output. The full relevant
Sturm sequences and all check flags were inspected. No failures were
reported. The script does not certify Walsh's theorem or replace the
universal preservation argument above.

**Scope and overlap.** The prior assessment1461, approved separately
in1462, authorized exactly this finite rational quartic test. Walsh's
preservation theorem is known mathematics; the local contribution is
the explicit witness and checked specialization. The inspected
coefficient-diagonal CZDS counterexample and finite-free inverse-factor
tests concern different maps. The source search did not establish
originality of this witness, and no claim of originality is made.
This does not reopen the blocked1961 source or the exhausted direct
moment/variation routes. Actual divisor control, signs, initialization,
overlap, unbounded-degree counts and the RH gap remain unresolved.

### Independent audit1464 — 18 November 2026

This audit reuses the unchanged EXPLORE assessment1461 and verifies the
supplied answer, without a degree sweep or a stronger root-count claim.

**Source interface.** The author-hosted request timed out. The matching
primary scan above was retrieved, and Theorem3.3 and remarks(1),(3) on
printed pp.257--258 were inspected. The displayed convolution has
exactly the weights (n-j)! b_(n-j) f^(j), with ordinary coefficients
b_j of g. The circular regions explicitly include closed half-planes;
remark(3) states the real-rooted specialization. Neither the theorem
nor that remark requires distinct roots. The parsed coefficient formula
and these hypotheses are readable; page-image calls returned no
inspectable image, so no visual verification is claimed. This is a
check of the cited interface, not an independent proof of Walsh/Grace.
The nonnegative-coefficient assumption in the separate Theorem3.4 is
irrelevant to this application of Theorem3.3.

**Applicability and normalization.** For degree-four f with nonzero
leading coefficient a, the k=0 term of W is 24 f; every other term has
smaller degree. Thus W has degree four even for repeated-root f, and
W/24 has leading coefficient a. The coefficients b_4=1,b_2=-12,b_0=36
of g=(x^2-6)^2 give respectively f,-f'',(3/2)f^(4) after division by
24. The two half-plane applications concern the same polynomial W.
All g-roots are real, so both translates remain the same respective
closed half-plane. Their intersection is the real axis. This checks
universal preservation for the stated class, with no limiting argument
or assumption of simple roots.

**Independent count checks and replay.** The input's y=x^2 quadratic
has discriminant 229>225, product -1 and two nonzero distinct real
roots of opposite signs. Each positive y contributes two simple real
x-roots and each negative y two simple nonreal x-roots; hence Z_c(p)=2.
Differentiation gives p''=12x^2+30 and p^(4)=24, so Tp=x^4+3x^2+5.
It is positive for every real x and remains degree four; hence its
multiplicity-counted nonreal count is exactly four, regardless of
squarefreeness. The optional squarefree calculation also checks:
Tp=11/4 when x^2=-3/2, and Tp(0)=5.

The certificate1463 script was read and replayed. All five basis
identities and every check flag pass; actual counts (2,4) equal the
required (2,4), with an empty failure list. The complete input, output
and Appell Sturm sequences, their infinity signs, variations and last
remainders were inspected using the shared JSON inspector. Their real
counts are respectively 2,0,2; the input/output gcd degrees are zero,
while the Appell gcd degree is two, consistently with its double roots.
The two algebraic count arguments above supply a separate check rather
than treating a script's boolean report as the proof.

**Decision.** Retain the proof and the generic preservation-to-count
stop without correction. This verifies the existing local obstruction;
it establishes no stronger mathematics, originality, sector-symbol
counterexample, actual-Jensen root loss, or RH conclusion. The original
symbol has a negative quadratic coefficient, and C020m supplies no
sector restriction on its zeros. Those absent hypotheses cannot be
silently added when applying its negative conclusion. Mathlib coverage
remains unchecked as recorded above.

## Mathlib

Matching coverage of this full result, Walsh convolution and this
finite-degree counterexample has not been checked. No absence claim
is made. The exact arithmetic certificate is a Python cross-check,
not a Lean formalization.
