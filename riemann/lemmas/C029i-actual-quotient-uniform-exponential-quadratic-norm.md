# Corollary C029i: actual quotient uniform exponential quadratic norm

## Hypotheses

Use exactly C028b/C028d/C028f's actual family and normalizations:

    F(u)=sum_(j>=0) b_j u^j/j!,  b_0=1,  b_j>0,
    U_d(u)=sum_(j=0)^d ((d)_j/d^j) b_j u^j/j!,
    P_d(x)=sum_(j=0)^d binom(d,j)b_j x^(d-j),
    Q_d(y)=P_d(y-b_1),
    f_d(y)=log|Q_d(y)|-d log|y|,  t_d(y)=f_d(y)/d.

Here F is the actual entire function of order 1/2, d ranges over every
integer d>=3, and (d)_0=1. P_d and Q_d are monic of degree d. Write
z_j for the roots of P_d and alpha_j=z_j+b_1 for those of Q_d, always
with algebraic multiplicity. The logarithms are defined off the finite
set containing zero and the real roots of Q_d; assign arbitrary finite
values to t_d on that null set. All integrals are Lebesgue integrals.

C028f supplies a fixed K>=1 and B=K*3^(3/4)/log 2 such that, for
every d>=3 and r>=1,

    log F(r)<=K r^(3/4),
    #{u:U_d(u)=0, |u|<=r}<=B r^(3/4),
    sum_(U_d(u)=0, |u|>r) 1/|u|<=4B r^(-1/4).

These are previously proved actual-family inputs, not additional
assumptions about its zeros. No RH, simplicity, real-rootedness,
compact nonreal-divisor exclusion or vanishing height limit is assumed.

## Conclusion

There exists a finite constant C, depending only on the actual F, such
that for every integer d>=3,

    integral_R t_d(y)^2 exp(|t_d(y)|/4) dy <= C.             (1)

The estimate retains every real or multiple-root singularity, a possible
root of Q_d at zero, and both infinite tails. It is uniform in d, not
merely a finite-degree integrability assertion. No effective numerical
value of C is claimed. This is a reproduction/specialization of standard
finite-factor, convexity and growth methods. The separate conceptual
audit1982 below accepts this bound under the stated input contracts.

## Proof

### Source scope and reason for the specialization

Assessment1978, separately approved before this attempt, covers this
exact norm and the finite-factor/convex-averaging method. Import C028b's
reciprocal scaling, C028d's centered factorization and C028f's common
coefficient majorant, closed count and strict tail with the hypotheses
above. Their analytic source is the standard Jensen formula, Min Ru,
*Nevanlinna Theory*, undated author-hosted notes,
[Theorem A1.1.1 and Corollary A1.1.3, printed pp.1-2](https://www.math.uh.edu/~minru/log.pdf),
and the actual entire-function identification in Cormac O'Sullivan,
*Zeros of Jensen polynomials and asymptotics for the Riemann xi function*,
arXiv:2007.13582v2, 9 December 2020,
[Introduction (1.2), Section 3.1, Theorem 3.1](https://arxiv.org/html/2007.13582v2#S3.SS1).
The relevant applicability arguments are already in C028b/C028f;
neither general theorem is reproved here.

We also use the standard finite Jensen inequality for a convex real
function and equal positive weights. A precise classical reference is
Cover and Thomas, *Elements of Information Theory*, first edition (1991),
[Section 2.6, Theorems 2.6.1-2.6.2, printed pp.24-26](https://sites.stat.columbia.edu/liam/teaching/neurostat-spr11/papers/EM/Cover%26Thomas-Ch2.pdf),
whose Jensen scope is recorded in source-notes1978 and the reused
source-notes1962. Only a finite sum of finite real values is used below,
so no probabilistic exponential-integrability premise is required.

The new local verification is necessary because the strict reciprocal
tail alone does not bound the roots near its origin, and a finite-root
formula alone gives no uniform angular or full-line bound. Fradelizi's
median-relative probability theorem, reviewed in assessment1978, is
not applied to unweighted Lebesgue measure. No general concentration
theorem or assertion of novelty is needed.

### A common origin disk and the complete absolute root sum

Since F is continuous at zero and F(0)=1, choose a fixed 0<r_0<1 with
F(r_0)-1<=1/2. For every d>=3 and |u|<=r_0, positivity of the b_j
and 0<=(d)_j/d^j<=1 give

    |U_d(u)-1|
      <=sum_(j=1)^d ((d)_j/d^j)b_j |u|^j/j!
      <=F(r_0)-1<=1/2.

Thus |U_d(u)|>=1/2 on this whole closed disk for every degree, including
the smallest degrees. Every root of U_d has modulus strictly greater
than r_0. C028f's closed count at r=1 and strict tail at r=1 now give

    sum_(U_d(u)=0) 1/|u|
      =sum_(r_0<|u|<=1) 1/|u|+sum_(|u|>1) 1/|u|
      <=B/r_0+4B.                                         (2)

Each sum includes all multiplicities; roots on the unit circle belong
to the first sum. There is no degree-dependent origin cutoff or omitted
finite group of low-degree polynomials.

For u!=0 the exact polynomial identity is

    U_d(u)=(u/d)^d P_d(d/u).

Both polynomials have nonzero constant and leading coefficients. As in
C028b, inversion therefore pairs their full degree-d root multisets,
with z_j=d/u_j and multiplicities preserved. C028d's real translation
gives alpha_j=d/u_j+b_1. Consequently (2) implies

    (1/d)sum_(j=1)^d |alpha_j|
      <=sum_(j=1)^d 1/|u_j|+b_1
      <=D:=B/r_0+4B+b_1<infinity.                          (3)

This is an absolute first moment. It uses no algebraic-square identity
or inference about the imaginary parts of compact roots.

### One logarithmic factor, uniformly in its angle

Put Psi(s)=s^2 exp(s/4) for s>=0 and Phi(t)=Psi(|t|) for real t.
For a complex alpha define, almost everywhere on R,

    g_alpha(y)=log|y-alpha|-log|y|.

We prove an absolute constant C_0 with

    integral_R Phi(g_alpha(y))dy<=C_0 |alpha|.              (4)

If alpha=0, g_alpha=0 away from zero, so the assertion holds with both
sides zero. Otherwise let r=|alpha|>0, beta=alpha/r and y=rx. Then
|beta|=1, dy=r dx, and the two log r terms cancel exactly:

    g_alpha(rx)=h_beta(x):=log|x-beta|-log|x|.

It is enough to bound the integral of Phi(h_beta) independently of all
unit complex beta. Psi is nondecreasing on [0,infinity), since
Psi'(s)=exp(s/4)(2s+s^2/4)>=0. Split the real line into three regions.

For 0<|x|<=1/2, the triangle inequalities give

    |x|<=1-|x|<=|x-beta|<=1+|x|<=3/2.

Hence 0<=h_beta(x)<=log(3/(2|x|)), and its contribution is at most

    C_origin=2 integral_0^(1/2)
                   [log(3/(2x))]^2 (3/(2x))^(1/4) dx.     (5)

For 1/2<|x|<2, write a=Re beta, so |a|<=1. The upper bound
|x-beta|/|x|<=6 gives h_beta<=log 6. If h_beta<0, then, away from
the single point x=a,

    -h_beta=log(|x|/|x-beta|)<=log(2/|x-a|),

because |x-beta|>=|x-a|. These two cases imply the single nonnegative
envelope

    |h_beta(x)|<=log(6/min(1,|x-a|)).

Indeed, when |x-a|>=1 its negative part is at most log 2, while when
|x-a|<1 it is at most log(2/|x-a|). The envelope also dominates the
positive part in both cases. The point x=a can be ignored as a null
set; an infinite envelope there is allowed. Translation v=x-a maps
this region into [-3,3], so monotonicity of Psi bounds its contribution
by the beta-independent constant

    C_middle=integral_(-3)^3
           [log(6/min(1,|v|))]^2 (6/min(1,|v|))^(1/4) dv. (6)

Both (5) and (6) are finite. Near their only possible singular endpoint
zero, each integrand is bounded by a constant times
x^(-1/4)(1+|log x|^2). Substitution x=exp(-s) reduces its integral
on (0,1] to integral_0^infinity exp(-3s/4)(1+s^2)ds, which is finite
by two integrations by parts. The remaining compact subintervals have
bounded integrands. This proves angular uniformity even for beta=1
or -1, and for nonreal beta arbitrarily close to either endpoint.

Finally, for |x|>=2 set v=1/|x|<=1/2. The triangle inequalities give

    log(1-v)<=h_beta(x)=log|1-beta/x|<=log(1+v).

The elementary real bounds log(1+v)<=v and
-log(1-v)=integral_0^v (1-s)^(-1)ds<=2v imply
|h_beta(x)|<=2/|x|<=1. Therefore

    Phi(h_beta(x))<=4 exp(1/4)/x^2,
    integral_(|x|>=2) Phi(h_beta(x))dx<=4 exp(1/4).        (7)

Define C_0=C_origin+C_middle+4 exp(1/4). It is finite, absolute and
independent of beta. Equations (5)-(7), followed by the scaling dy=r dx,
prove (4). No global complex logarithm, removed neighborhood of a root,
or asymptotic angular separation was used.

### Convex averaging and the actual quotient

Psi is convex as well as nondecreasing, since

    Psi''(s)=exp(s/4)(2+s+s^2/16)>0  (s>=0).

Together with Psi'(0)=0, or by composition with the convex absolute
value, this proves that Phi is convex on all of R. C028d's monic
factorization gives, at every real y outside the finite exceptional set,

    t_d(y)=(1/d)sum_(j=1)^d g_(alpha_j)(y).

The finite Jensen inequality now gives pointwise almost everywhere

    Phi(t_d(y))<=(1/d)sum_(j=1)^d Phi(g_(alpha_j)(y)).

Every summand on the right is nonnegative, measurable and integrable
by (4). Integrating the inequality and then using (3) proves

    integral_R Phi(t_d(y))dy
      <=(C_0/d)sum_(j=1)^d |alpha_j|
      <=C_0 D.

This establishes (1) with C=C_0(B/r_0+4B+b_1). Only finite sums and
ordinary changes of variables were interchanged with integration;
no d-limit or infinite zero sum appears.

Every repeated root is retained as repeated equal terms in the same
average. Roots alpha_j=0 contribute identically zero factors, exactly
accounting for common numerator/reference zeros. Multiple real roots
and colliding nonreal roots do not require disjoint neighborhoods:
the pointwise convex bound and the uniform single-factor integral
already include them. Arbitrary finite choices on the exceptional
null set change no integral. Thus the estimate covers all the cases
required by the approved target, including infinity.

### Relevance and limitations

The achieved threshold is precisely one finite bound independent of
every d>=3. It could support a later small-exponent remainder comparison;
the exact comparison, its window factors and any limit order are outside
this proof. C028d still gives integral_R t_d=pi H_d/d, and no upper
estimate tending to zero for that signed integral has been obtained.
C028b's RH-equivalent H_d=o(d), the vanishing of S_F, and actual-Xi
all-degree mixed positivity remain open. C029e's numerator-only cost
and C029f's fixed-q obstruction are contrasts, not inputs. The complete
height-limit theorem C028g is not needed for this bound.

### Separate conceptual audit1982 (20 November 2026)

The whole proof has been replayed under the unchanged SPECIALIZE
assessment1980, separately approved1981. The conclusion passes without
a corrected constant, a stronger hypothesis or an additional theorem.
This verifies the local specialization; it is not a new theorem beyond
the methods cited above or a re-audit of the entire earlier Xi chain.

1. **Common origin and complete moment.** Continuity of the fixed F at
   zero supplies a single positive r_0<1. Positive coefficients and
   0<=(d)_j/d^j<=1 give |U_d-1|<=1/2 on the closed disk for every
   allowed d. Thus all roots satisfy |u|>r_0, strictly. The closed
   count n_d(1)<=B and strict tail sum_(|u|>1)1/|u|<=4B partition
   the full multiset, including every root on |u|=1, so (2) follows.
   There is no hidden origin contribution or eventual-degree exception.
   C028f's constants come from the order of the fixed F and the common
   majorant |U_d(u)|<=F(|u|), not from separate polynomial growth
   constants. Its Jensen contours avoid the finitely many root radii;
   the resulting closed count retains their full multiplicities.

2. **Normalization and inversion.** Expanding (u/d)^d P_d(d/u)
   gives binom(d,j)b_j(u/d)^j, exactly the coefficient defining U_d.
   P_d has constant b_d>0 and leading coefficient 1; U_d has constant
   1 and leading coefficient b_d/d^d>0. Inversion therefore loses
   neither zero nor infinity roots, and its nonzero derivative preserves
   multiplicity. After translation alpha_j=d/u_j+b_1, the triangle
   inequality gives (1/d)sum |alpha_j|<=sum 1/|u_j|+b_1.
   The last term is b_1, not d*b_1. This is the absolute moment
   required by (4); the algebraic sum of squares in C028d is unused.

3. **Uniform single-factor integral.** For alpha!=0 the scaling
   y=|alpha|x cancels the two log|alpha| terms and supplies exactly
   one factor |alpha| in the integral. For |x|<=1/2 the lower ratio
   is at least 1, including the boundary, so (5) bounds the absolute
   logarithm. In the middle region the upper ratio is at most 6.
   The negative logarithm is bounded by log(2/|x-Re beta|) when it
   occurs. Splitting |x-Re beta| at 1 gives precisely (6)'s envelope;
   its translated domain is a subset of [-3,3]. At the single point
   x=Re beta the envelope can be infinite even when the factor is
   finite, which is harmless for Lebesgue integration. Near zero
   the envelopes have the integrable form |v|^(-1/4) times a
   quadratic logarithm: after |v|=exp(-s), the decaying factor is
   exp(-3s/4). This checks beta=1,-1 as well as approach from either
   nonreal half-plane. On |x|>=2, |h_beta|<=2/|x| and
   integral_(|x|>=2)x^(-2)dx=1, verifying exactly 4 exp(1/4)
   in (7), including both infinite tails. The omitted region endpoints
   form a finite null set. Alpha=0 is separately identically zero a.e.

4. **Convex averaging, collisions and integration.** Direct
   differentiation gives Psi'(s)=exp(s/4)(2s+s^2/4)>=0 and
   Psi''(s)=exp(s/4)(2+s+s^2/16)>0 on [0,infinity).
   Composition of this nondecreasing convex function with |t| is
   convex on R, including at zero (both one-sided first derivatives
   there vanish). Thus the cited finite Jensen inequality applies
   with exactly d weights 1/d. The monic factorization makes
   t_d=(1/d)sum g_(alpha_j) at every real point outside the finite
   exceptional set; no leading constant is missing. Repeated roots
   remain repeated summands. A root alpha_j=0 cancels its own
   reference factor and contributes zero a.e. Neither these cases nor
   collisions require separated root neighborhoods. Each Phi(g_alpha)
   is measurable and integrable by (4). Finite linearity and the
   a.e. inequality therefore give the full integral bound before
   applying (3). No limit in d, infinite zero sum, or integration
   of individually non-L1 signed factors has been used.

The required threshold is one finite C independent of every d>=3;
the checked value is C=C_0(B/r_0+4B+b_1), with C_0 exactly as in
(5)-(7). This is existential and no effective numerical C is certified.
The direct inputs remain C028b, C028d and C028f; C028g is unneeded.
The audit supplies no small-exponent window comparison, signed-log
upper payment, compact nonreal-mass exclusion, S_F=0 or RH. In
particular an L2-type majorant on R is not a vanishing signed L1
bound on growing windows. C029f's fixed-q loss remains intact.

## Mathlib

Not checked. Full matching theorem availability, and availability of
the uniform angular specialization, are unknown. Standard convexity,
finite Jensen, polynomial factorization and integration are supporting
mathematics, not a claim that this whole result is formalized. No absence
or formal verification is asserted.
