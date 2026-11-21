# Left-sector quartic preservers contract the nonreal-root count

## Hypotheses

Let D=d/dx and let q be a real polynomial of degree at most four with
q(0)=1. Every zero z of q satisfies
\[
 \operatorname{Re}z<0,\qquad
 |\operatorname{Im}z|\le-\operatorname{Re}z/3.
\]
Assume q(D) preserves real-rootedness of every real polynomial of degree
exactly four, including repeated roots and arbitrary nonzero leading
coefficients. For a nonzero real polynomial f, let Z_c(f) count its
nonreal roots with multiplicity.

## Conclusion

For every real quartic p,
\[
 Z_c(q(D)p)\le Z_c(p).
\]
In particular there is no witness with counts (2,4) in the class of
assessment1464: rational q with nonnegative coefficients and monic
rational p with nonnegative coefficients satisfy the hypotheses above
whenever their required universal preservation condition holds.

The key stronger statement, which does **not** require the preservation
assumption, is that the inverse of q(D) on polynomials of degree at most
four maps every strictly positive real polynomial to a strictly positive
real polynomial. Thus q(D)p cannot be a real-root-free quartic if p has
any real root. No higher-degree conclusion or actual-Xi correspondence
is asserted. Independent conceptual audit1468 (18 November 2026) retains
this local result without changing its hypotheses or conclusion.

## Proof

**Finite inverses and factorization.** Write V_4 for the real vector space
of polynomials of degree at most four. Since D^5=0 there, any polynomial
in D with constant coefficient one is invertible on V_4: the finite
geometric series in its positive-order part supplies an inverse. All
these operators and their inverses commute.

By the fundamental theorem of algebra and real conjugation, q is the
product of normalized real linear factors and real quadratic factors
for nonreal conjugate pairs. Its constant coefficient makes the product
normalization exact. A negative real root gives a factor 1+a z with
a>0. A nonreal pair -u+iv,-u-iv, where u>0 and 0<|v|<=u/3, gives
\[
 1+a z+b z^2,\qquad
 a=\frac{2u}{u^2+v^2}>0,\quad b=\frac1{u^2+v^2},\quad
 t=\frac b{a^2}=\frac{1+(v/u)^2}{4}\in(1/4,5/18].
\]
Repeated roots are retained as repeated factors. The constant q=1 is
the empty product. This factorization uses no rationality or simplicity
assumption. We will show positivity of each inverse separately and
compose them on the same space V_4.

**Real linear factors.** For a>0 and f in V_4, the inverse of 1+aD is
\[
 R_a f(x)=\int_0^\infty e^{-s}f(x-as)\,ds
        =\sum_{k=0}^4(-a)^k f^{(k)}(x).
\]
Taylor's formula is an exact finite polynomial identity here, and
the elementary integral of s^k e^{-s} is k!, so every displayed integral
is absolutely convergent and no infinite series interchange occurs.
Multiplication by 1+aD gives the identity modulo D^5. If f is nonzero
and nonnegative on the real axis, its integrand is nonnegative and is
positive on some open subinterval of s>0 for each fixed x: otherwise
the polynomial f would vanish on a half-line and be zero identically.
Thus R_a f(x)>0 for every real x. In particular R_a preserves strict
positivity.

**A conjugate-pair factor.** The inverse of 1+aD+bD^2 on V_4 is
\[
 R=1-aD+(a^2-b)D^2+(-a^3+2ab)D^3
          +(a^4-3a^2b+b^2)D^4.
\]
Direct multiplication gives one modulo D^5. If r_k is its coefficient
of D^k, put m_k=k!r_k. For a quadratic
h(y)=c_0+c_1(y-x)+c_2(y-x)^2, finite differentiation gives
\[
 R(h^2)(x)=\sum_{i,j=0}^2 c_i c_j m_{i+j}.
\]
With t=b/a^2, the moment matrix (m_{i+j}) is congruent, through the
invertible diagonal matrix diag(1,a,a^2), to
\[
 H(t)=\begin{pmatrix}
 1&-1&2(1-t)\\
 -1&2(1-t)&-6(1-2t)\\
 2(1-t)&-6(1-2t)&24(1-3t+t^2)
 \end{pmatrix}.
\]
Its leading principal minors are
\[
 1,\qquad 1-2t,\qquad
 d(t)=4-24t+48t^2-40t^3.
\]
For the entire permitted interval, 1-2t>=4/9. Set
delta=5/18-t>=0. An exact identity gives
\[
 d(5/18-\delta)=\frac{131}{729}
       +\frac{178}{27}\delta+\frac{44}{3}\delta^2+40\delta^3
       \ge\frac{131}{729}>0.
\]
Sylvester's criterion therefore makes H(t) positive definite, including
the closed sector boundary. Hence R(h^2)(x)>0 for every nonzero real
quadratic-or-lower h, at every real x. Writing h in powers of y-x does
not turn a nonzero polynomial into a zero coefficient vector.

**From squares to nonnegative quartics.** We justify the needed finite
sum-of-squares statement directly, rather than assume positivity on
squares covers all inputs. Any nonzero real polynomial f>=0 on the
real axis, of degree at most four, has positive leading coefficient,
even degree, and every real root has even multiplicity. Factorization
over the reals expresses it as a positive constant times a square of
real linear factors times a product of at most two monic positive quadratics.
Each such quadratic is (y-u)^2+v^2 with v>0. Combining two sums of
two squares uses the exact identity
\[
 (A^2+B^2)(C^2+E^2)=(AC-BE)^2+(AE+BC)^2.
\]
Including the square of the real factors shows f=h_1^2+h_2^2 with
deg h_i<=2; at least one h_i is nonzero. Positive constants are absorbed
by their real square roots. This also covers degrees zero and two,
vanishing h_i, and repeated real roots. By linearity and the positive
definiteness just proved, Rf(x)>0 for every real x. The zero polynomial
maps to zero. Thus every allowed quadratic-factor inverse preserves
strict positivity, with the stronger nonzero nonnegative assertion.

**Composition and root counts.** The inverse of q(D) is the product of
the factor inverses on V_4. Each maps strictly positive polynomials to
strictly positive polynomials and stays within V_4. The empty product
has the same property. This proves the claimed positivity of q(D)^{-1}.

For any real quartic p with nonzero leading coefficient, divide by that
coefficient to make it monic; this changes neither count. The operator
q(D) preserves degree and leading coefficient because q(0)=1 and every
other term differentiates at least once. If q(D)p had four nonreal roots
counted with multiplicity, it would have no real root. A monic real
quartic without real roots is strictly positive everywhere, by
continuity and positivity at infinity. Applying the inverse would make
p strictly positive, excluding every real root, including a repeated
one. Consequently Z_c(p)=2 cannot yield Z_c(q(D)p)=4. A real quartic's
nonreal count is one of 0,2,4, since nonreal roots occur in conjugate
pairs with equal multiplicities. If the input count is zero, the stated
universal preservation assumption makes the output count zero. If it
is four, contraction is automatic from the degree. These three cases
prove the conclusion with all multiplicities retained.

**Scope, checks and literature qualification.** The assessment1464,
approved in1465, authorized exactly this witness/impossibility test.
The nonnegative-coefficient and rational restrictions are unnecessary
for the impossibility proof, so proving the larger real class covers
every member of the requested class. Universal preservation is a
hypothesis used only in the zero-input-count case. We do not infer it
from the sector bound or test it by sampling. The already cited Walsh
interface in C020m can certify individual preservers; its generic
counterexample lacks the present sector hypothesis and is contrast
only, not a premise here. Its source is Craven--Csordas, *Location of
zeros. Part I*, Illinois J. Math. 27(2) (1983), Theorem3.3 and
remarks(1),(3), pp.257--258. No further theorem is imported from the
damaged sector formula or blocked original sources. The finite inverse,
moment minors and elementary degree-four square representation are
proved here because preservation alone is not a count theorem and
the inspected literature did not settle this exact restricted target.
This is not a certified originality claim.

Run `python3 scripts/quartic-differential/sector-inverse-certificate-1466.py`.
Its full certificate is
`scripts/quartic-differential/sector-inverse-certificate-1466.json`.
It checks the inverse identity modulo D^5, every moment, the full
determinant polynomial and its endpoint-shift identity over the whole
parameter interval. The actual positive lower bounds are 4/9 and
131/729, against required lower bounds >0; all flags pass with no
failures. This is an algebra cross-check, not a numerical root sample
or a substitute for the factorization/composition argument above.
Actual-factor correspondence, exceptional-divisor bounds, unbounded
degrees, actual signs, initialization and overlap remain unresolved.

### Independent conceptual audit1468 — 18 November 2026

This audit uses the unchanged EXPLORE assessment1466, separately approved
in recovery1467. It verifies the proposed finite result; it neither
strengthens that result nor establishes originality beyond the reviewed
sources. The following checks retain the proof without correction.

1. **Normalization and finite inverses.** A normalized conjugate factor
   has roots -u+iv and -u-iv exactly when its coefficients are the stated
   a and b. Thus a>0 and t=(1+(v/u)^2)/4, with the full closed outer
   endpoint 5/18. At v=0 the roots are real and belong to the linear
   factor case; no limiting argument is needed. Inverting each factor
   modulo D^5 is legitimate on the same V_4. Multiplication of these
   inverses remains an inverse even when the formal product has terms
   of degree greater than four, because those terms annihilate V_4.
   Repeated factors are separate copies of the same invertible map.

2. **Independent matrix check.** Finite Taylor expansion of h(y)^2 about
   y=x gives m_k=k!r_k with the signs and factorials displayed above.
   Eliminating the first row and column of H by a congruence gives the
   Schur complement
   \[
   \begin{pmatrix}
    1-2t&-4+10t\\
    -4+10t&20-64t+20t^2
   \end{pmatrix}.
   \]
   Its determinant is (1-2t)(20-64t+20t^2)-(-4+10t)^2
   =4-24t+48t^2-40t^3, independently checking the certificate's
   permutation expansion. Substitution t=5/18-delta gives the four
   stated positive coefficients. Hence the claimed bounds 4/9 and
   131/729 are genuine whole-interval lower bounds, both strictly
   above the required zero threshold, not bounds inferred from a grid.

3. **Positivity domain.** Every nonzero globally nonnegative polynomial
   in V_4 has even real-root multiplicities and positive leading
   coefficient. In its real factorization, distributing the square
   factors across the two-square identity leaves each summand of
   degree at most two before squaring. This includes positive
   constants, double real roots and fourth powers. At every x, a
   nonzero summand has a nonzero coefficient vector in powers of y-x;
   the positive definite matrix therefore gives strictly positive
   evaluation. For a real linear inverse, the half-line integral is
   finite and strictly positive for a nonzero nonnegative polynomial.
   These arguments prove exactly the positivity needed at each stage
   of the composition. The empty product q=1 preserves strict
   positivity; it is not claimed to send a polynomial with real zeros
   to a strictly positive one.

4. **Multiplicity and preservation.** Dividing p and its image by the
   same nonzero leading coefficient preserves every root and its
   multiplicity. A real monic quartic with four nonreal roots is
   strictly positive, even when its nonreal roots are repeated.
   Inverse positivity excludes such an image from an input with a
   real root, including a double real root. This proves the two-to-four
   exclusion. The zero-input-count case uses universal preservation
   exactly as assumed; the four-input-count case uses degree four.
   Neither positivity alone nor sector membership is substituted for
   the preservation hypothesis. Dropping rationality and coefficient
   nonnegativity only enlarges the class proved, so it covers the
   originally nominated class.

All complete certificate1466 fields were inspected, including every
inverse coefficient, moment, matrix entry, determinant coefficient,
endpoint-shift coefficient and failure field. Its script was replayed;
there were no failures and the certificate was reproduced byte-for-byte
(SHA256 `39a8b0b89793321c3e379fa4f58c019492393609997db2887b9cbda96f93f06c`).
The replay checks finite algebra; items 1, 3 and 4 supply the separate
logical audit. No Walsh theorem is used in this proof: it occurs only
in the comparison with C020m, so C020n still has no local lemma inputs.
No higher-degree, actual-factor, exceptional-divisor or actual-Xi sign
claim follows. The main RH gap is unchanged.

## Mathlib

Matching coverage of the full sector-restricted contraction result,
the inverse-positivity formulation and its moment-matrix specialization
has not been checked. Sylvester's criterion, the fundamental theorem of
algebra and finite polynomial identities are standard mathematical
inputs; no assertion about their exact Mathlib names or absence is made.
The rational certificate is not a Lean formalization.
