# Fourfold real input roots cannot give the sector-sextic count increase

## Hypotheses

Let D=d/dx, a>0, 1/4<=t<=5/18, and
\[
 q(z)=1+az+ta^2z^2,\qquad T=q(D).
\]
Let r,b,c be real, with c>b^2/4, and set
\[
 p(x)=(x-r)^4\big((x-r)^2+b(x-r)+c\big).
\]
Count all polynomial roots with multiplicity. No rationality or
coefficient-sign restriction on p is needed for the conclusion.

## Conclusion

The symbol q has q(0)=1, positive coefficients and all its zeros in
Re z<0, |Im z|<=-Re z/3. It preserves real-rootedness of every real
sextic, including repeated roots and arbitrary nonzero leading
coefficients. Nevertheless the proposed (2,4) witness is impossible
for every input p in this statement:
\[
 Z_c(p)=2,\qquad Z_c(Tp)\le2.
\]

This excludes the fourfold-real-root input family for a **single
quadratic factor** throughout the allowed parameter interval. It does
not treat four real input roots in general position, other multiplicity
patterns, or compositions of allowed factors. The full sextic (2,4)
test remains unresolved. Independent critical audit is pending.

## Proof

**Symbol restrictions and preservation.** The two roots of q are
\[
 \frac{-1\pm i\sqrt{4t-1}}{2ta}.
\]
Their real parts are negative, and the ratio of the absolute imaginary
part to minus the real part is sqrt(4t-1)<=1/3. At t=1/4 these are
equal negative real roots. The coefficients and normalization are as
stated.

For preservation, import Walsh's convolution theorem from Thomas Craven
and George Csordas, *Location of zeros. Part I: Real polynomials and
entire functions*, Illinois J. Math. **27**(2) (1983), 244--278,
Theorem3.3 and remarks(1),(3), printed pp.257--258,
[primary scan](https://scispace.com/pdf/location-of-zeros-part-i-real-polynomials-and-entire-z3v2jd50yw.pdf).
Its degree-six, closed-half-plane, repeated-root interface was inspected
in assessment1468/review1469 and is reused unchanged. For degree-six
f and g=sum b_j x^j the convolution is
W(f,g)=sum_(k=0)^6 (6-k)!b_(6-k) f^(k). If f and g are real rooted,
the two closed-half-plane applications put every zero of W on the real
axis; no simplicity assumption is imposed. Here
\[
 g(x)=Tx^6=x^4(x^2+6ax+30ta^2).
\]
The quadratic discriminant is a^2(36-120t)>=(8/3)a^2>0. Thus g is
real rooted, and its coefficients give W(f,g)/6!=Tf, since
5!(6a)/6!=a and 4!(30ta^2)/6!=ta^2. Its leading coefficient and
the leading coefficient of Tf are nonzero. This proves the stated
universal preservation, including all multiplicities and either sign
of the leading coefficient. It is only an applicability argument for
the cited theorem, not a reproof or a count consequence of preservation.

**Reduction and exact output.** Put x=r+ay. Dividing p(r+ay) by a^6
gives y^4(y^2+B y+C), with B=b/a and C=c/a^2>B^2/4. Under this
change of variable aD_x=D_y and ta^2D_x^2=tD_y^2. Positive scaling,
translation and multiplication by a nonzero constant preserve every
root multiplicity. It is therefore enough to work with a=1,r=0;
rename B,C as b,c.

The quadratic x^2+bx+c is strictly positive on the real axis, so p
has exactly four real roots, all at zero, and two nonreal roots. Direct
differentiation gives
\[
 Tp=x^2H(x),
\]
where the monic quartic is
\[
 H(x)=x^4+(b+6)x^3+(c+5b+30t)x^2
                  +(4c+20tb)x+12tc.                 \tag{1}
\]
We prove H has at least two real roots, counting multiplicity.

**Two evaluation points.** Set
\[
 C_t(x)=x^2+4x+12t,\quad s=\sqrt{4-12t},\quad
 \alpha_-=-2-s,\quad \alpha_+=-2+s.
\]
Here 2/3<=s^2<=1, so these are two distinct real roots of C_t.
Divide (1) by C_t. The exact remainder is A_t(x)+b B_t(x), where
\[
 A_t(x)=(32-96t)x+96t-216t^2,\qquad
 B_t(x)=(8t-4)x-12t.                                \tag{2}
\]
For completeness the quotient is
x^2+(b+2)x+c+b+18t-8. In particular the c-dependence disappears
at both alpha points. Put
\[
 a_0=-64+288t-216t^2,\quad a_1=32-96t,\quad
 b_0=8-28t,\quad b_1=8t-4.
\]
Then A_t(alpha_+)=a_0+a_1s, A_t(alpha_-)=a_0-a_1s, and likewise
B_+=B_t(alpha_+)=b_0+b_1s and B_-=B_t(alpha_-)=b_0-b_1s.

Throughout the closed interval, b_0>=2/9>0 and b_1<0. Therefore
B_->0. Also
\[
 (-b_1)^2s^2-b_0^2
   =(4-8t)^2(4-12t)-(8-28t)^2
   =48t^2(5-16t)\ge\frac53>0.                       \tag{3}
\]
Since -b_1,s,b_0 are positive, (3) gives (-b_1)s>b_0 and hence B_+<0.
Thus B_- and -B_+ are strictly positive weights. Equations (2) yield
the exact weighted identity
\[
 \begin{split}
 B_-H(\alpha_+)-B_+H(\alpha_-)
 &=2s(b_0a_1-b_1a_0)\\
 &=192s t^2(18t-5)\le0.                             \tag{4}
 \end{split}
\]
The b terms cancel; no input restriction on b or c was used in (4).

If t<5/18 the last expression is strictly negative, so at least one
of the two H values is negative. A monic quartic tends to positive
infinity at both ends of the real axis. The intermediate value theorem
then gives one root to each side of a point where H is negative.
These are two distinct real roots.

If t=5/18, (4) is zero. Either one H value is negative, giving the
same conclusion, or both are nonnegative. In the latter case their
strictly positively weighted sum can be zero only if both are zero.
Then alpha_- and alpha_+ are already two distinct real roots of H.
This handles the closed sector boundary without replacing <= by <.
The lower endpoint t=1/4 belongs to the strict-negative case.

Consequently x^2H has at least four real roots counted with
multiplicity. Multiplicities in the product add even if factors share
a root. It has degree six, so Z_c(Tp)<=2, while Z_c(p)=2 as proved
above. This is the claimed exclusion. Multiplying p by any nonzero
real leading coefficient would leave the argument's root counts
unchanged, though the nominated input is monic.

**Verification, purpose and limits.** Run
`python3 scripts/quartic-differential/sector-sextic-fourfold-certificate-1471.py`.
The full certificate is
`scripts/quartic-differential/sector-sextic-fourfold-certificate-1471.json`.
It checks (1), the complete division identity (2), the polynomial
identities (3)--(4), the endpoint substitutions and the degree-six
Walsh coefficients exactly. The interval bounds, positive-weight
argument and root-count conclusion are proved above; they are not
inferred from numerical sampling. The discriminant bound is 8/3
after division by a^2, the squared-weight gap is at least 5/3, and the
weighted-sign threshold is <=0 with equality allowed at t=5/18.

The prior EXPLORE assessment1468, approved in review1469, authorizes
the fixed sextic test. This is a restricted impossibility result within
that test, obtained while examining output collisions. C020n's quartic
inverse proof and C020o's sextic inverse obstruction are comparisons,
not premises here. The finite identity (4) is proved because Walsh
only supplies preservation and the inspected sources do not give this
partial-count conclusion. The recorded search does not certify
originality. In particular no composition argument can be inferred:
after one factor the polynomial need not retain a fourfold real root.
General four-real-root inputs and products are still unpaid, as are
actual-Xi factor applicability, exceptional-divisor bounds, unbounded
degrees, signs, initialization and overlap. There is no RH candidate.

## Mathlib

Full matching coverage of this restricted count result, its weighted
identity and the Walsh specialization has not been checked. The
certificate uses rational polynomial algebra and is not a Lean proof.
Unknown coverage is not evidence of absence.
