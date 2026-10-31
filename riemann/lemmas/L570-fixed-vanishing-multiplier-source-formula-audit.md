# Lemma 570: fixed vanishing-multiplier source-formula audit

## Hypotheses

Let n be a positive integer, N=n, A(z)=z-1 and B(z)=exp(z).
Write c_n=[z^n]A(z)B(z)^n. The audit concerns the vanishing/signed
extension in Flajolet--Sedgewick, *Analytic Combinatorics*, online book
running date 3 October 2008, printed pp.586--589, especially Note VIII.37
on p.589, not Theorem VIII.8 under its original nonnegative-A condition.
Primary locations are the [author-hosted book](https://ac.cs.princeton.edu/home/AC.pdf#page=603)
and [alternate author-hosted book](https://algo.inria.fr/flajolet/Publications/book.pdf#page=603).

The independent expansion input is Cormac O'Sullivan, *Revisiting the
saddle-point method of Perron*, arXiv:1702.03777v2 (30 March 2018),
[Assumptions 1.1, coefficient rule (1.7), Corollary 5.1 and proof](https://arxiv.org/html/1702.03777v2).
Its phase, amplitude, neighborhood and bounded piecewise C^1 contour
must be independent of the large parameter; phase and amplitude are
holomorphic on a domain containing the contour and neighborhood. The
phase is nonconstant, with an even-order saddle, strict real-part
maximum along the contour and opposite incoming/outgoing sectors.
The error is absolute, with amplitude dependence through a supremum
bound; amplitude nonvanishing at the saddle is not assumed.

No Xi function, hypothetical zeta zero, simplicity, separation, RH,
height-dependent uniformity or local notebook lemma is a premise.

## Conclusion

For every integer n>=1, c_n=0 exactly. For this fixed model, the
uncorrected Note VIII.37 prediction, whose proposed leading term
specializes to exp(n)/sqrt(2*pi*n^3), is false under the note's intended
signed/vanishing extension. This does not refute Theorem VIII.8 with
nonnegative A: this A fails that hypothesis.

O'Sullivan's rule gives alpha_0=alpha_2=0 in the angular coefficient
integral, consistent with the exact result. The correction already
listed on the [authors' errata page](https://ac.cs.princeton.edu/errata/),
p.589 entry credited to Elie de Panafieu, 30 August 2019, also gives zero
at that order. This is reproduction of a known source correction and a
local decision to reject the uncorrected input, not a new asymptotic
theorem or an advance toward all-height Xi signs.

## Proof

### Exact coefficient and applicability

The everywhere-convergent exponential series gives

    c_n = n^(n-1)/(n-1)! - n^n/n! = 0,       n>=1.

Both terms coincide since n!=n(n-1)!. In particular, no limiting
interchange, numerical approximation or cancellation of unknown error
terms is used.

For B=exp(z), B(0)=1, every Taylor coefficient is positive, the support
is aperiodic and the analytic radius is infinite. The spread in (83)
is lim_(x->infinity) xB'(x)/B(x)=infinity. The ratio lambda=N/n=1 is
fixed in its interior. The saddle equation zeta B'(zeta)/B(zeta)=1
therefore gives zeta=1. For every r>0,

    |B(r exp(i theta))| = exp(r cos theta)

has its unique maximum at theta=0 on [-pi,pi]. A is entire and has a
simple zero there: A(1)=0, A'(1)=1, A''(1)=0. Its constant coefficient
is negative, so the original L1 assumption on A is unavailable.
Indeed a nonzero power series with nonnegative coefficients cannot
vanish at a positive interior point of convergence. The text on p.589
explicitly extends beyond that original condition and introduces the
vanishing case; this is the extension being tested.

The uncorrected displayed expression has numerator
A'(zeta)+zeta A''(zeta), factor B(zeta)^n/zeta^(N+1), and the displayed
square-root denominator of order n^(3/2). At this model the numerator
is 1 and B(zeta)^n=exp(n). The source's saddle coordinate zeta=1 and
the curvature of log B(z)-lambda log z at zeta is

    (d^2/dz^2)(z-log z)|_(z=1)=1.

Thus both the saddle glyph zeta and curvature glyph xi specialize to
1: distinguishing these in the book extraction cannot change the
nonzero value exp(n)/sqrt(2*pi*n^3). No conclusion depends on guessing
which of those glyphs occurs in its extracted denominator. The source
prediction would require

    c_n / (exp(n)/sqrt(2*pi*n^3)) -> 1,

whereas this ratio is identically 0. Even an overall sign change would
not repair the nonzero prediction. The contradiction concerns that
uncorrected expression only, not the existence of complete saddle
expansions.

### Independent application of the known coefficient rule

Parameterize the coefficient circle by z=exp(i theta), -pi<=theta<=pi.
The exact angular integral is

    c_n = (1/(2*pi)) integral_(-pi)^pi exp(n p(theta)) q(theta) dtheta,
    p(theta)=exp(i theta)-i theta,   q(theta)=exp(i theta)-1.

The factor dz/z=i dtheta is included, so no additional multiplier or
orientation sign is missing. These p,q are entire functions of the
complex variable theta, independent of n. The contour is the real
segment [-pi,pi], with the saddle theta_0=0 in its interior and distinct
endpoints. Re p(theta)=cos theta<1=Re p(0) away from zero on this segment.
Near zero,

    p(theta)=1-theta^2/2-i theta^3/6+theta^4/24+O(theta^5)
            =1-(1/2)theta^2(1-phi(theta)),
    phi(theta)=-i theta/3+theta^2/12+O(theta^3).

Hence mu=2, p_0=1/2 with argument zero. The incoming negative real ray
and outgoing positive real ray are opposite sectors; choose the outgoing
index k=0. A fixed disk |theta|<1/4 is a neighborhood as required. On
its union with the real contour |q|<3, so K_q=3 is an admissible fixed
bound. All hypotheses of Corollary 5.1 hold without a nonzero q(0).

Applying (1.7), not rederiving the general theorem, gives

    alpha_0 = (1/2)p_0^(-1/2) q(0)=0,
    alpha_2 = (1/4)p_0^(-3/2)
              (d^2/dtheta^2)[q(theta)(1-phi(theta))^(-3/2)]_(theta=0).

The analytic branch in the second expression takes value 1 at zero.
Since

    q(theta)=i theta-theta^2/2+O(theta^3),
    (1-phi(theta))^(-3/2)=1-i theta/2+O(theta^2),

their product is i theta+(-1/2+1/2)theta^2+O(theta^3).
Thus alpha_2=0. Corollary 5.1 with M=2 supplies
c_n=exp(n)O(n^(-5/2)), which is consistent with c_n=0. It does not assert
that the next coefficient is nonzero. The computation only specializes
two coefficients of a known expansion for this one fixed model.

### Existing erratum and qualification of the source verdict

The authors' online errata p.589 entry supplies a phase-sensitive
coefficient c, with phi_m=-d^m/dtheta^m log B(zeta exp(i theta)) at zero
for m=2,3. Its proposed n^(-3/2) coefficient is

    c=-(zeta A'(zeta)+zeta^2 A''(zeta))/(2 phi_2^(3/2))
      -i phi_3 zeta A'(zeta)/(2 phi_2^(5/2)).

In this model use the analytic logarithm log B(exp(i theta))=exp(i theta).
It gives phi_2=1 and phi_3=i; hence c=-1/2-i*i/2=0, in agreement with
the exact coefficient and the independent rule. The erratum has an
absolute O(n^(-2)) remainder inside its n^(-1/2) prefactor; c=0 therefore
does not assert an erroneous relative asymptotic. Its left index is
rendered n while the prefactor retains N; here N=n, so that discrepancy
is immaterial. No general correction is derived or independently
certified here.

Access qualification: today's direct book requests returned 403 or a
size-limit response, and the shell request failed DNS. Earlier primary
book reading in the saved assessment is reused. The full selected
p.589 note, the p.586 hypotheses and extension paragraph were exposed
again as indexed primary-page passages during this audit. The complete
relevant erratum entry, including its formula, definitions, credit and
date, was likewise exposed in indexed primary-page text; a direct errata
open returned 403. No visual PDF verification is claimed. The error
verdict is independently certified by the exact identity and applicable
O'Sullivan rule, not by a search snippet, an unresolved glyph or an
assumption that the entire errata page was directly accessible. The
previously inspected June 2010 errata predates the 2019 correction;
absence from that older list was never evidence of novelty.

The fixed model rejects the short uncorrected formula as a signed
leading-term input. It does not obstruct the corrected full expansion,
prove any actual-Xi sign, bound a deflated Xi quotient or handle a
height-dependent phase. These independent application gaps remain.

## Mathlib

Full matching coverage of this source-formula audit and Corollary 5.1
is not checked. This is not evidence of absence. The proof uses the
exponential Taylor series, coefficient extraction, factorial recurrence
and the precisely cited analytic theorem; no formal verification is
claimed. No mathematical script or numerical certificate is needed for
the exact identity or the two displayed derivative calculations.
