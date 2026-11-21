# Sector-sextic composition excludes a two-to-four increase

## Hypotheses

Let D=d/dx and let q be a real polynomial of degree at most six with
q(0)=1. Assume every zero z of q satisfies

\[
 \operatorname{Re}z<0,\qquad
 |\operatorname{Im}z|\le-\operatorname{Re}z/3.                 \tag{1}
\]

Let f be a monic real sextic with exactly two nonreal roots counted
with multiplicity. For any nonzero real polynomial h, write Z_c(h)
for its number of nonreal roots counted with multiplicity.

## Conclusion

One has

\[
 Z_c(q(D)f)\le2.                                             \tag{2}
\]

Also q(D) preserves real-rootedness of every real sextic, including
repeated roots and either nonzero leading coefficient. Thus no rational
q and monic rational f with nonnegative coefficients can meet the
approved sextic (2,4) witness target under (1). The coefficient-sign,
rationality and separately stipulated preservation restrictions cannot
provide an exception: (2) holds without the first two restrictions,
and preservation follows from (1).

This is a finite-degree specialization of audited C020u/C020v and an
imported real-symbol count theorem. Independent conceptual audit1488
accepts the assembly under exactly these hypotheses; it is not an
originality claim. No actual-Xi
factor correspondence, all-degree assertion or RH resolution follows.

## Proof

**Imported inputs and scope.** C020v, accepted by conceptual audit1485,
states that for

\[
 T_t=1+D_y+tD_y^2,\qquad 1/4\le t\le5/18,
\]

the image T_t(RQ) has at least four real roots, counted with
multiplicity, whenever R is a monic real-rooted quartic and
Q=y^2+B y+C with C>B^2/4. Neither the coefficients nor the roots
of R must be rational, and no coefficient-sign hypothesis appears.
C020u's preservation interface gives real-rootedness of T_t h for
every real-rooted sextic h, with arbitrary multiplicities and nonzero
leading coefficient. Its external theorem is Thomas Craven and George
Csordas, *Location of zeros. Part I: Real polynomials and entire
functions*, Illinois J. Math. **27**(2) (1983), 244--278, Theorem3.3
and remarks (1),(3), printed pp.257--258,
[primary scan](https://scispace.com/pdf/location-of-zeros-part-i-real-polynomials-and-entire-z3v2jd50yw.pdf).
The Walsh normalization and applicability are already justified in
C020u: T_t y^6=y^4(y^2+6y+30t), with discriminant
36-120t>=8/3. No preservation theorem is reproved here.

For real linear factors import the classical real-symbol
complex-zero-decreasing inequality: if p is a nonzero real polynomial
having only real zeros, then

\[
 Z_c(p(D)h)\le Z_c(h)                                       \tag{3}
\]

for real polynomials h whenever the image is nonzero. The precise
source reused from assessment1468/review1469 and its underlying
assessment1464/review1465 is Craven--Csordas's 2004 survey,
[author manuscript](https://www.dcce.ibilce.unesp.br/~dimitrov/ProfRusev/czdssurvey.pdf),
p.2, equation (1.2), with its multiplicity convention. The named
Hermite--Poulain theorem and first-order factor argument are also
inspected in Allan Pinkus, *Some Remarks on Zero-Increasing
Transformations*, [author manuscript](https://pinkus.net.technion.ac.il/files/2021/02/stl.pdf),
pp.3--4, with the multiplicity convention on p.1. Here only
p(z)=1+a z, a>0, is used: its sole zero -1/a is real, and p(0)=1
ensures that the degree-six image is nonzero. The cited all-real-symbol
inequality is not being applied to a nonreal quadratic symbol. The
quadratic two-count bound instead comes from C020v.

**Normalized symbol factors.** Real factorization, with repetitions
retained, and q(0)=1 give an exact product of factors with constant
coefficient one. A real zero -u, u>0, contributes

\[
 1+a z,\qquad a=1/u>0.                                    \tag{4}
\]

A nonreal conjugate pair -u+iv,-u-iv, where u>0 and
0<|v|<=u/3, contributes

\[
 \frac{(z+u)^2+v^2}{u^2+v^2}=1+a z+b z^2,\quad
 a=\frac{2u}{u^2+v^2}>0,\quad b=\frac1{u^2+v^2},\quad
 t=\frac b{a^2}=\frac{1+(v/u)^2}{4}\in(1/4,5/18].           \tag{5}
\]

There is no remaining scalar factor since both sides have value one
at zero and the same zeros with the same multiplicities. If q=1,
the product is empty. No individual factor is assumed rational.
This normalization also appears in C020n's quartic comparison, but
its quartic inverse-positivity/count argument is not used here.

**One quadratic factor on the zero/two-count class.** Let
L=1+aD_x+bD_x^2 be a factor from (5), and let h be any monic real
sextic with Z_c(h) in {0,2}. Set

\[
 g(y)=a^{-6}h(ay).
\]

The positive real dilation and nonzero scalar preserve the count and
make g monic. Direct differentiation, using b=t a^2, gives

\[
 T_t g(y)=a^{-6}(Lh)(ay).                                  \tag{6}
\]

If Z_c(h)=0, then g is real-rooted, and C020u's preservation input
implies Z_c(Lh)=0 by (6). If Z_c(h)=2, real conjugation and
multiplicity counting factor g as RQ: its four real roots give the
monic real-rooted quartic R, while the remaining conjugate pair
gives Q=y^2+B y+C with C>B^2/4. Repeated real roots are allowed.
The two nonreal roots are a single conjugate pair of multiplicity
one each, since their total count is two. C020v now yields
Z_c(T_t g)<=2, hence Z_c(Lh)<=2 by (6). The output is still monic
of degree six, because every positive derivative term has lower
degree. Its real coefficients imply an even nonreal count, so it
again belongs to the zero/two-count class. The upper sector boundary
in (5) is included by C020v; real pairs at v=0 are treated by (4),
not omitted as a limiting case.

**Composition.** Start with h_0=f and apply the factors (4)--(5)
in any fixed order. A real linear factor keeps Z_c<=2 by (3),
and a quadratic factor keeps Z_c<=2 by the preceding paragraph.
Every factor has constant coefficient one, so every intermediate
polynomial is a monic real sextic. Inductively its nonreal count is
always either zero or two, which is exactly the domain needed for
the next factor. No intermediate rationality or nonnegative
coefficient assumption is made. Repeated symbol roots simply repeat
the corresponding operation. Multiplicity is retained in each
imported count/preservation statement and in C020v, so collisions
of intermediate real roots do not create a missing case.

Polynomial functional calculus for D identifies this finite operator
product with q(D): multiplying two polynomials in D multiplies their
symbols, and all the factors commute. This proves (2), including the
empty product. If instead h_0 is any real-rooted sextic, each linear
factor preserves count zero by (3), and each quadratic preserves it
by C020u and (6). Dividing out the initial nonzero leading coefficient
reduces to the monic case; linearity restores either sign afterwards.
This proves the additional universal preservation assertion.

**Qualifications.** The proof resolves the exact saved (2,4) target
by impossibility, rather than by a failed witness search. It does
not decide other partial counts, other input degrees or a wider
sector. Earlier inverse-positivity and expanded-discriminant failures
retain their scoped conclusions; C020p's unrelated count proof and
C020o/q are unused. Actual-factor correspondence, paid exceptional
loss, unbounded-degree positivity, signs, initialization and overlap
remain independent gaps. No numerical computation or mathematical
script is needed for this factorwise specialization.

**Independent conceptual audit — 18 November 2026, step1488.**
The audit accepts (2) and the additional real-rooted preservation
assertion. It checks this finite composition, reusing C020u/audit1482
and C020v/audit1485 without claiming a fresh audit of their internal
proofs. The external inputs retain the exact citations and scopes
above: the real-symbol count law is used only on linear factors,
Walsh preservation only on real-rooted inputs. Preservation is never
substituted for a partial-count inequality.

For normalization, q(0)=1 excludes a zero at zero. A negative real
zero -u contributes (z+u)/u, and a conjugate pair contributes exactly
the quotient in (5). These factors have precisely the original roots
and multiplicities; their product and q differ by a scalar which
evaluation at zero fixes to one. Positivity of u gives a>0, while
0<|v|/u<=1/3 gives 1/4<t<=5/18. The upper endpoint is covered by
both local inputs. The lower endpoint is allowed by those inputs;
actual nonreal factors have t>1/4, and repeated real zeros are
handled by linear factors. There is no omitted sector-boundary or
repeated-symbol case, and no rationality of these factors is needed.

The dilation is checked directly, not inferred from a change of
notation: for g(y)=a^(-6)h(ay),
g'(y)=a^(-5)h'(ay) and g''(y)=a^(-4)h''(ay). Thus

\[
 g+g'+tg''=a^{-6}\big(h+ah'+ta^2h''\big)(ay)
             =a^{-6}(Lh)(ay).
\]

The real nonzero dilation and scalar preserve the multiplicity of
each root and whether it is real. The scaled input is monic of
degree six. For count zero the preservation interface has exactly
the required domain. For count two, conjugation forces one nonreal
pair, each root simple, and leaves four real roots counted with
multiplicity. Their product is the monic real-rooted quartic R;
the pair gives Q=y^2+By+C with C-B^2/4>0. Hence C020v applies
even when several of the four real roots coincide. It guarantees
four real output roots counted with multiplicity, sufficient for
count at most two, without asserting simplicity of those roots.

Each factor has constant coefficient one, so its order-zero term
retains the degree and leading coefficient of its input, and its
other terms have smaller degree. In particular no intermediate image
vanishes or drops degree. All coefficients remain real; conjugation
therefore makes its nonreal count even. The bound at most two means
the next image is again in exactly the zero/two-count input class.
For a linear factor (3) supplies the bound for both cases; for a
quadratic the two preceding branches supply it. This proves the
finite induction in any fixed factor order. Collisions cause no
exception because every count and each invoked input already counts
multiplicities. No rationality or coefficient-sign condition on an
intermediate image is required. The polynomial identity for q(D)
is exact and finite, since D^j D^k=D^(j+k). The empty product
q=1 returns the original sextic and satisfies both conclusions.

For the preservation conclusion, divide a real-rooted sextic with
leading coefficient c!=0 by c. The same induction stays entirely
in the zero-count branch. Linearity then restores c, of either sign,
without changing any roots. Thus the separate universal preservation
restriction in the original rational nonnegative-coefficient (2,4)
test is also verified, rather than assumed for the conclusion.

No discrepancy, new mathematical dependency, numerical replay or
mathematical script was needed. The degree bound on q is respected;
this audit asserts no other input degree or count class. Inverse
stop1470 and coefficient stop1473 do not contradict this assembly,
and neither is reopened. Actual-Xi factor correspondence, a paid
exceptional-root loss and unbounded-degree signs remain unresolved.

## Mathlib

Full matching coverage of this finite sector-symbol count theorem has
not been checked. Supporting mathematics consists of real polynomial
factorization into linear/quadratic factors, the chain rule and
composition of polynomials in a linear operator. No matching Lean
theorem or formal verification is asserted; unchecked coverage is
not evidence of absence. The analytical count/preservation inputs
are the cited results and the audited local C020u/C020v assertions.
