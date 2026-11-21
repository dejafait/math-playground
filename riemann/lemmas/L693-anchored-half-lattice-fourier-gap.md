# Lemma 693: a fixed atom and a unit-weight perturbed half-lattice can have a Fourier gap

## Hypotheses

Use the Fourier conventions

    F_(2pi) f(t)=integral_R f(x)*exp(-2*pi*i*t*x) dx,
    F_ang f(omega)=integral_R f(x)*exp(-i*omega*x) dx,

extended to tempered distributions. A distributional Fourier gap on an
open interval means that the Fourier transform annihilates every smooth
compactly supported test function in that interval. The spatial point 0
is fixed and every spatial atom must have mass one. No reflection symmetry
or decay of the displacements is required.

## Conclusion

There exist real e_m, m in Z, with |e_m|<=1/8, such that

    mu=delta_0+sum_(m in Z) delta_(m+1/2+e_m)

is a positive tempered measure and F_ang mu vanishes on a nonempty open
interval I contained in (0,2*pi). Consecutive nonanchor atoms have gaps at
least 3/4, and each has distance at least 3/8 from the fixed atom at 0.
Every atom has mass one.

This is an existential specialization of Lev's theorem, not an originality
claim. No effective positive lower bound on the gap width, or inclusion
of a given interval, is provided. There is no conclusion about a gap
containing zero, finite
unsmoothed truncations, complex frequencies or logarithms of finite sums.
It gives no bound for the rational responses or complete charges in
L666/L657 and has no established implication for Xi. The separate
conceptual audit of 3 November 2026 (step 109) verified the application
below without changing its conclusion. This does not independently
certify Lev's contraction proof or establish a finite-transfer theorem.

## Proof

### Imported prescription theorem

Import Nir Lev, *An example concerning Fourier analytic criteria for
translational tiling*, Rev. Mat. Iberoam. **38** (2022), no. 6, 1975--1991,
DOI [10.4171/RMI/1318](https://doi.org/10.4171/RMI/1318),
[Theorem 4.8, p.1988](https://ems.press/content/serial-article-files/39104).
With the F_(2pi) convention: for fixed 0<a<b<1/2 and epsilon>0 there
exists delta>0 such that every distribution S satisfying

    S(-t)=conjugate(S(t)),
    supp S contained in (-b,-a) union (a,b),
    sup_(k in Z) |S-hat(k)|<=delta

admits real lambda_m with |lambda_m-m|<=epsilon and

    F_(2pi)(sum_m delta_(lambda_m))=delta_0+S on (-b,b).   (1)

The coefficients are those of S regarded as a distribution on the unit
circle. For a smooth function supported in (-1/2,1/2) they are

    S-hat(k)=integral_(-1/2)^(1/2) S(t)*exp(-2*pi*i*k*t) dt.

The real-line Fourier transform at integer k agrees with this circle
coefficient because of the compact support. For the smooth prescription
below, periodic extension across +/-1/2 is smooth; the phase in (2)
need not itself be periodic. These are the Section 2 and Section 4.4
coefficient conventions of the cited arXiv version.

Reuse the invocation-start assessment
`drafts/literature/2026-11-03-anchored-half-lattice-fourier-gap.md`:
it records the primary statement and complete relevant proof-case reading,
including the sign/conjugation check against
[arXiv:2007.09930v3, Section 4.10, equations (4.24)--(4.26)](https://arxiv.org/html/2007.09930v3#S4.SS10).
In particular the counting-measure correction in (1) is +S. Import this
prescription theorem without reproving its contraction. Only the explicit
anchor-cancelling prescription and its applicability are derived here.
The older unanchored zero-prescription conclusion alone is insufficient.

### A localized prescription meeting the actual norm

Fix a=1/8, b=3/8, c=1/4 and epsilon=1/8 first, and let delta>0 be the
theorem's threshold. Choose an even real smooth cutoff eta such that

    0<=eta<=1,  eta=1 on [-1/2,1/2],  supp eta contained in [-1,1].

For an explicit standard bump construction, put u(s)=exp(-1/s) for s>0
and u(s)=0 for s<=0, theta(s)=u(s)/(u(s)+u(1-s)), and
eta(v)=theta(4*(1-v^2)/3). The denominator is everywhere positive;
these formulas have the stated smoothness, plateau and support.

Set

    h=min(1/32,delta/8)>0,
    chi(t)=eta((t-c)/h)+eta((t+c)/h),
    S(t)=-exp(pi*i*t)*chi(t).                           (2)

The two support intervals [c-h,c+h] and [-c-h,-c+h] are disjoint.
The positive one is contained in [7/32,9/32], strictly inside
(a,b)=(4/32,12/32), and the negative one is strictly inside (-b,-a).
Thus S is smooth with compact support in the required open bands.
Evenness and reality of chi give

    S(-t)=-exp(-pi*i*t)*chi(t)=conjugate(S(t)).

In particular every integer coefficient is real: conjugate its defining
integral and change variable t to -t, using this symmetry. Thus the
prescription also lies in the real coefficient space used in Lev's proof.

The disjoint cutoff supports have total length at most 4h, and 0<=chi<=1.
For every integer k,

    |S-hat(k)|<=integral |S(t)| dt
               =integral chi(t) dt<=4h<=delta/2<=delta. (3)

The pointwise amplitude is one on the plateau, but the required norm is
the supremum of integer Fourier coefficients, bounded by (3). The bands,
and hence delta, were fixed before choosing h; no uniformity of delta
under shrinking bands has been assumed.

### Translation and distributional cancellation

Apply (1), and put e_m=lambda_m-m and nu=sum_m delta_(lambda_m).
The shifts are real and bounded by 1/8. Translation of nu in the spatial
variable by +1/2 multiplies its Fourier transform by exp(-pi*i*t).
The extra fixed spatial atom delta_0 has Fourier transform 1. On (-b,b),

    F_(2pi) mu
      =1+exp(-pi*i*t)*(delta_0+S)
      =1+delta_0-chi.                                  (4)

Here multiplication of the frequency atom by the smooth phase gives
exp(-pi*i*t)*delta_0=delta_0. All equalities are distributional; there
is no pointwise evaluation of delta_0.

For completeness, use bilinear distribution/test-function pairing and
write T_(1/2)nu for the spatial translate. For a Schwartz test phi,

    <F_(2pi)(T_(1/2)nu),phi>
      =<nu, x -> integral phi(t)*exp(-2*pi*i*t*(x+1/2)) dt>
      =<F_(2pi)nu, exp(-pi*i*t)*phi(t)>.

If phi is supported in (-b,b), multiplication by this phase keeps its
support there, so the local source identity (1) applies. The transform
of the extra spatial atom pairs with phi as integral phi(t) dt, giving
the constant 1 in (4), not an additional frequency delta.

On J=(c-h/2,c+h/2), the positive cutoff is one, the negative cutoff
vanishes and 0 is absent. For every phi in C_c^infinity(J), (4) gives

    <F_(2pi) mu,phi>=integral_J (1-chi(t))*phi(t) dt=0.

Thus J is a nonempty distributional gap in (a,b). The angular transform
is the distributional pullback by omega -> omega/(2*pi): its pairing
with a test function psi equals 2*pi times the pairing of F_(2pi) mu
with t -> psi(2*pi*t). Indeed, for a Schwartz test psi, substitution
omega=2*pi*t in its Fourier integral gives

    <F_ang mu,psi>
      =<mu, x -> integral psi(omega)*exp(-i*omega*x) d omega>
      =2*pi*<F_(2pi)mu, t -> psi(2*pi*t)>.

For psi supported in 2*pi*J, the last test is supported in J. Thus the
Jacobian is 2*pi and the support dilation is by 2*pi; no pointwise
meaning of the infinite Fourier sum is used. Therefore it vanishes on

    I=(2*pi*(c-h/2),2*pi*(c+h/2)) contained in (0,2*pi),

of length 2*pi*h>0. This verifies the convention in the target.

Finally lambda_(m+1)-lambda_m>=1-2/8=3/4. Also
|m+1/2+e_m|>=|m+1/2|-1/8>=3/8, so no nonanchor atom merges with
the anchor. Every mass remains one. The displacement bound gives O(1+R)
atoms in [-R,R] and absolute convergence of the spatial sum against
every Schwartz function. The separation also bounds the mass of every
unit interval uniformly: there are at most two nonanchor atoms, and at
most one anchor, in a closed interval of length one. In particular,
writing p_2(phi)=sup_x (1+|x|)^2*|phi(x)|, partition into unit intervals
to obtain

    |<mu,phi>| <= integral |phi| d mu
               <= C*p_2(phi)*sum_(j in Z) (1+|j|)^(-2),

with an absolute C. This is a continuous Schwartz seminorm bound, not
only pointwise convergence of the defining sum. The same reasoning
applies to nu before translation. Thus mu is a positive translation-bounded
tempered measure, and the distributional operations above are justified.
No infinite Fourier sum was evaluated pointwise or truncated.

### Scope of the independent audit

Step 109 checked every local hypothesis and identity above against
Lev's exact Theorem 4.8 and its complete short proof, Section 4.10 of
arXiv:2007.09930v3. In particular that proof uses
F'=delta_Z-delta_Lambda and F_(2pi)(F')=-S, confirming the +S
in (1). The supporting contraction remains a cited theorem; its
earlier source coverage is reused. The explicit cutoff, fixed-parameter
threshold, coefficient norm, phase, angular Jacobian, unit masses and
temperedness all pass. No substantive defect or stronger conclusion was
found. The displayed test-function and seminorm details make the audit
checkable without adding a new mathematical premise.

The gap is only local vanishing in tempered distributions. This proof
does not take an unsmoothed partial sum limit at a real frequency, does
not extend the measure's transform to complex frequencies, and does
not estimate logarithms or their integrals. L666/L657 are contextual
comparisons, not inputs. A finite rational-W or complete-charge claim
would require separate estimates and a separate source assessment.

## Mathlib

Full coverage of Lev's prescription theorem and this specialization has
not been checked. Distributional translation and smooth cutoffs are
standard analytic inputs; no matching Mathlib theorem names are claimed.
Unknown coverage is not evidence of absence.
