# Corollary C032l: finite signed smoothed-law mixtures cannot gain an exponential moment

## Hypotheses

Retain all source inputs and normalizations of C032k, hence those of
C032j: the actual Xi zero multiset with multiplicity, the fixed-v1
Gaussian-smoothed probability laws nu_sigma on [0,infinity), their
entire even profiles p_sigma with logarithmic real-axis growth, the
exact heat-time identity, H(t)>0 for t>0, the first-ordinate/strip and
counting inputs, and p_sigma(0)>0. These inputs are imported from the
two cited Sra preprints, with C032j's applicability qualifications;
they are not independently source-wide verified here.

Fix finite r>=2, distinct real sigma_1,...,sigma_r>0, and real
a_1,...,a_r with sum_j a_j=1. Let

    nu=sum_(j=1)^r a_j nu_sigma_j.

This is a finite signed measure of mass one. No sign is assumed for
the coefficients. The moment conclusion below assumes explicitly
that nu is a nonnegative measure; it does not establish that premise
for any proposed signed coefficients. Let b_sigma be the entire
normalized lift defined and audited in C032k.

## Conclusion

The entire function

    F(w)=sum_(j=1)^r a_j exp(-b_sigma_j(w))

is not even. If nu>=0, then for every c>0,

    integral_[0,infinity) exp(cu) dnu(u)=infinity.

In particular no allowed finite signed combination is both a
probability measure and a measure with any positive exponential
moment. This closes the finite-mixture question posed after C032j,
including all coefficient choices cancelling any finite number of
odd Taylor terms. It does not cover a zero width, an infinite sum,
coefficients depending on w, another smoothing operation, or an
identification with the unsmoothed Xi law. It proves no sign in L030
and supplies neither a proof nor a disproof of RH.

## Proof

### Classical theorem imported

Use Raghavan Narasimhan, *Un analogue holomorphe du théorème de
Lindemann*, Annales de l'Institut Fourier **21** (1971), no.3,
271-278, Theorem 1, printed p.271,
[doi:10.5802/aif.391](https://aif.centre-mersenne.org/articles/10.5802/aif.391/),
[original PDF](https://www.numdam.org/item/10.5802/aif.391.pdf).
Its statement is: if f_1,...,f_p are holomorphic on C^n and every
difference f_i-f_j for i!=j is nonconstant, then exp(f_1),...,exp(f_p)
are linearly independent over C[z_1,...,z_n]. No growth or finite-order
assumption is made. We use only n=1 and constant coefficients.
The primary statement, its prerequisites on p.272 and its complete
one-variable proof on pp.273-277 were inspected in review1301.
That ready assessment is reused; there is no local reproof of this
classical theorem and no claim of a new dependence theorem.

### Applicability to the complete reflected family

For each 1<=j<=r set

    f_(j,+)(w)=-b_sigma_j(w),
    f_(j,-)(w)=-b_sigma_j(-w).

C032k's global lift and separation, including its audit1302, show
that these 2r functions are entire, vanish at zero, and are pairwise
distinct. In particular, the same-width opposite reflections are
distinct: b_sigma'(0)=2*pi*p_sigma(0)>0, whereas the derivative of
b_sigma(-w) at zero is negative. Different widths with the same
orientation are separated by C032k's heat-time argument; opposite
orientations are separated by their derivative signs.

If a difference of two f functions were constant, evaluating at zero
would make that constant zero. This would contradict pairwise
distinctness. Thus every such difference is nonconstant, exactly the
theorem's hypothesis, not merely a distinctness assumption about
arbitrary entire functions. Narasimhan's theorem now gives linear
independence of all 2r exponentials over the constants.

If F were even, the full relation would be

    sum_(j=1)^r [a_j exp(f_(j,+)(w))
                 -a_j exp(f_(j,-)(w))]=0

for all w in C. Independence forces a_j=0 and -a_j=0 for every j.
This contradicts sum_j a_j=1. Zero coefficients are harmless: one
may retain them in the relation or omit their two functions. At
least one coefficient remains, and even a single retained width
has two distinct reflected functions. Therefore F is not even.

### Positive-measure consequence

If nu>=0 it is a probability measure by its mass. For every s>0,
finite additivity of bounded Laplace integrals gives

    integral exp(-su) dnu(u)=F(sqrt(s)).

C032k's audited positive-moment implication says that a finite
integral of exp(cu) against this nonnegative nu for any c>0 would
force F to be even on C. Its proof uses holomorphy near s=0 and the
identity theorem; it never interchanges divergent signed moments.
This contradicts the preceding paragraph. Since the integrand is
nonnegative, each such moment exists as an extended integral; being
nonfinite it is +infinity. The reverse implication in C032k's moment
equivalence was also audited, but is not required for this exclusion.

The source inputs from C032j and C032k remain in force throughout.
In particular this specialization does not replace the preprint heat
positivity input with an unconditional claim verified from scratch,
nor identify nu with any unsmoothed reciprocal transform. The result
is a known-theorem specialization resolving a local surrogate test,
not certified originality or a main-gap sign advance. No numerical
test or finite Taylor truncation is used as proof.

### Independent critical audit1340, 17 November 2026

The written specialization passes under precisely its stated inputs.
This audit uses C032k's audited global lift and separation as inputs;
it does not repeat audit1302 or verify the two Sra manuscripts as a
whole. Narasimhan's primary statement and complete one-variable proof
coverage are reused from review1301 and its separate approval1339.
There is no reproof of the imported independence theorem.

Here are all pair types in its application. Put
c_j=b_sigma_j'(0)=2*pi*p_sigma_j(0)>0. Then

    f_(j,+)'(0)=-c_j,     f_(j,-)'(0)=+c_j.

Consequently f_(j,+) and f_(k,-) are different for every j,k,
including j=k, since their derivative difference is -c_j-c_k<0.
For j!=k, the two plus exponents are different by C032k's
distinct-width separation. The two minus exponents are also different:
an identity between them, composed with w->-w, would identify the
two plus exponents. This exhausts every pair among the 2r functions.
All are globally entire and zero at zero. A constant difference must
therefore be zero, contradicting the established distinction. The
nonconstant-difference hypothesis is verified for the full family;
no finite-order hypothesis is being silently added or omitted.

If F is even, the exact constant-coefficient relation is the displayed
sum with coefficients a_j and -a_j. Narasimhan Theorem1, n=1,
annihilates every coefficient. This contradicts sum_j a_j=1 even
when some coefficients vanish. Finiteness and positive, distinct
widths are used here; no limiting relation is asserted.

For the measure step, total variation satisfies

    |nu|([0,infinity)) <= sum_j |a_j| < infinity,
    nu([0,infinity)) = sum_j a_j = 1.

For real s>0, exp(-su) is bounded by one on this support. Linearity
of its integral against the finite signed sum, followed by each
individual law's Laplace identity and C032k's b_sigma(w)=B_sigma(w^2)
for w>0, gives exactly integral exp(-su) dnu=F(sqrt(s)). This step
is valid before assuming nu>=0 and involves no unbounded integral.

Now assume nu>=0 and, for contradiction, integral exp(cu) dnu<infinity
for some c>0. Since the support is [0,infinity), this is an absolute
exponential moment of a probability measure. The precise analytic
input is Boyer, *The speed of convergence in the renewal theorem*,
[19 June 2015 manuscript](https://maths.jbboyer.fr/documents/articles/renewal.pdf),
Definition2.1 and Lemma2.2 with proof, printed p6, as applied in
C032k. It supplies a holomorphic f(s) on a disk |s|<rho, rho>0,
agreeing with the positive-real Laplace transform there. No renewal
or drift assumption is used.

Both F(w) and f(w^2) are holomorphic on |w|<sqrt(rho). For every
real w in (0,sqrt(rho)) they agree by the bounded Laplace identity.
This set has an accumulation point inside the disk, so the identity
theorem gives equality throughout the disk. Hence F(w)-F(-w)=0
there. That difference is entire, so it vanishes on C, contradicting
the checked independence argument. For each c>0 the exponential
moment of the nonnegative nu is an extended nonnegative integral;
its nonfiniteness therefore means +infinity. No converse moment
implication, cancellation of divergent moments, or positivity of
the individual coefficients is required.

No defect or mathematical correction was found. The audit certifies
only the qualified local obstruction already stated, not new
mathematics beyond the cited theorem. In particular H(t)>0,
p_sigma(0)>0, the heat identity, profile regularity and zero inputs
keep their inherited source qualifications. It supplies no actual-Xi
sign, no positive signed mixture and no global ban on smoothing.

## Mathlib

Full matching coverage is unchecked and unknown. No Mathlib theorem
is imported. General entire-function or probability support is not
asserted to include Narasimhan's dependence theorem, C032k's lift and
moment criterion, or this complete finite-mixture specialization.
