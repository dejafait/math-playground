# Lemma 375: an exact-shift quartic common-zero family

**Hypotheses.** Let a be any real number with a>40, and define

\[
 x=a^2,\qquad b=\sqrt{x+2-\frac{30}{2x+5}},\qquad
 P_a(z)=(z^2-a^2)(z^2-b^2).
\]

For real t use the comparison-model definitions

\[
 F_a(t)=2P_a(t),\qquad
 G_a(t)=-(t^2+1/4)\operatorname{Re}
          \frac{P_a(t-2i)}{5/2+it}.
\]

These definitions retain L366 (1)'s shift and divisor only. No actual
theta representation, arithmetic input, discriminant inequality,
response Laguerre sign or zero-count asymptotic is a hypothesis.

**Conclusion.** P_a is an even monic real quartic with P_a(0)>0.
Its four zeros ±a, ±b are real, simple and outside [-40,40]. Moreover

\[
 P_a(a)=0,\qquad
 \frac{P_a(a-2i)}{5/2+ia}
       =i\frac{32a(a^2+1)}{2a^2+5}\ne0.                 \tag{1}
\]

Consequently F_a(a)=G_a(a)=0. The common-zero heights are unbounded
as a ranges over this family: for every real H there is a member with
a>max(40,H) and this common zero at a. This is a family statement,
not infinitely many common zeros of a single fixed polynomial.

The polynomial completion model

\[
 f_a(s)=P_a((s-1/2)/i)
       =((s-1/2)^2+a^2)((s-1/2)^2+b^2)
\]

is entire and satisfies f_a(1-s)=f_a(s) and
f_a(conj(s))=conj(f_a(s)). It has
f_a(1/2+it)=P_a(t) and f_a(5/2+it)=P_a(t-2i).

**Proof.** Since x>1600, 2x+5>15. Therefore

\[
 0<2-\frac{30}{2x+5}<2,\qquad x<b^2<x+2.
\]

In particular b>a>40. The factorization of P_a proves evenness,
real coefficients, degree four, monicity and P_a(0)=a²b²>0.
The four displayed roots are distinct. For explicit multiplicities,
P_a'(±a)=2(±a)(a²-b²)≠0 and
P_a'(±b)=2(±b)(b²-a²)≠0. There are no other roots because
the factorization is a product of the four corresponding linear factors.

Put Δ=x-b²=-2+30/(2x+5) and z=a-2i. Then
z²=x-4-4ia, so exact multiplication gives

\[
 P_a(a-2i)=(-4-4ia)(\Delta-4-4ia)=R+iI,
 \quad R=16-4\Delta-16x,\quad I=32a-4a\Delta.
\]

The full divided real projection, including its variable divisor, is

\[
 \operatorname{Re}\frac{R+iI}{5/2+ia}
 =\frac{(5/2)R+aI}{25/4+x}
 =\frac{40-8x-(10+4x)\Delta}{25/4+x}.          \tag{2}
\]

Its denominator is strictly positive. Substituting Δ gives zero in
its numerator: (10+4x)Δ=2(2x+5)(-2+30/(2x+5))=40-8x.
To verify the entire complex value as well, the same substitution yields

\[
 R=-\frac{32x(x+1)}{2x+5},\qquad
 I=\frac{80a(x+1)}{2x+5}.
\]

With K=32a(x+1)/(2x+5)>0 these are R=-aK and I=(5/2)K.
Thus P_a(a-2i)=iK(5/2+ia), proving (1). In particular
the shifted polynomial value itself is nonzero. The zero real projection
is not inferred from vanishing of that complex value. The definitions
now give F_a(a)=G_a(a)=0.

For any real H, choose a=max(40,H)+1. All hypotheses just verified
hold, with a>H; hence there is no uniform onset over this family beyond
which pointwise common zeros are excluded. For a fixed member, F_a has
only four zeros, so this does not refute eventual disjointness for that
member or for actual xi.

Finally ((s-1/2)/i)²=-(s-1/2)². Substitution into the two factors of
P_a gives exactly the stated formula for f_a, which has real
coefficients. Reflection changes s-1/2 to its negative, preserving its
square; real coefficients prove conjugation symmetry. Direct evaluation
of (s-1/2)/i at s=1/2+it and s=5/2+it gives respectively t and t-2i.
This proves the completion-model statements without using an assertion
about actual zeta. ∎

**Separate critical audit (2026-10-07).** All stated claims pass without
correction. Here is an independent check of both components after division.
Write d=b²−x=4(x−5)/(2x+5), so 0<d<2 for x>1600. Expanding the
monic polynomial as z⁴−(2x+d)z²+x(x+d) at z=a−2i gives
R=16+4d−16x and I=a(32+4d). Multiplication by the conjugate of
the divisor gives the two components

\[
 \frac{40-8x+(10+4x)d}{x+25/4},\qquad
 \frac{a(16x+64+6d)}{x+25/4}.
\]

The first numerator vanishes since (10+4x)d=8x−40. For the second,

\[
 (16x+64)(2x+5)+24(x-5)=8(4x+25)(x+1).
\]

It therefore equals 32a(x+1)/(2x+5)>0, proving the full identity (1)
without relying on a zero real part alone. Neither 5/2+ia nor the
shifted polynomial value vanishes. The real prefactor −(a²+1/4)
in G_a is finite and nonzero, so no prefactor singularity is involved.

The positive square root defining b exists, and b²=x+d>x=a² with
a>0 gives b>a>40. The product has precisely the roots ±a, ±b;
at ±a the remaining quadratic factor is −d, and at ±b it is d.
Multiplication by the corresponding nonzero derivative 2(±a) or
2(±b) verifies all four simple multiplicities. Its constant term
x(x+d) is positive. The change of variable z=−i(s−1/2) changes each
factor's sign, so the two signs cancel in f_a. Reflection about 1/2
preserves both squared factors; their real coefficients imply the
stated conjugation identity for every complex s. At the two claimed
vertical lines the change of variable is exactly t and t−2i. These
checks use neither a zeta functional equation nor a growth assumption.

The verified quantifiers are: for every H there exist a polynomial
P_a and a>max(40,H) satisfying the common-zero assertion. Taking
a=max(40,H)+1 is legitimate for every real H. They are not the
assertion that there exists one P with common zeros beyond every H.
Indeed each fixed member has no positive F_a zero above b, so its
eventual disjointness is automatic. The audit confirms only the
pointwise/uniform-family obstruction, with no strengthening of the
original result and no numerical or source-dependent step.

Qualifications: this is a finite polynomial obstruction to a universal
pointwise inference or a uniform geometric onset. It supplies no common
zero of actual F_0 and G, no L374 physical inequalities and no RH
counterexample. L018, L024 and L366 explain the comparison conventions;
L371/L373 are earlier arbitrary-pair contrasts. None is a mathematical
premise of this elementary construction. The separate critical audit
above verifies the stated finite-family result. The saved EXPLORE assessment found no
matching theorem in its bounded source comparison; originality is not
claimed and no Hermite–Biehler theorem is reproved or imported here.

**Mathlib.** Full matching coverage is not checked; availability is
unknown. The proof uses only finite polynomial algebra, positive real
square roots and complex division. No formal verification or absence
claim is made. [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
