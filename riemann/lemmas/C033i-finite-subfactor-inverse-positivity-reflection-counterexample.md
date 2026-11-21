# Corollary C033i: a finite-subfactor inverse defeats positivity reflection

## Hypotheses

Retain C032j's actual-zero normalization and all its external-input
qualifications. The comparison with C032u is contextual only. Thus Z+ counts
positive-ordinate nontrivial zeta zeros with multiplicity,
z_rho=gamma_rho-i*(beta_rho-1/2), and, for t>0,

    H(u)=sum_(rho in Z+) exp(-u*z_rho^2),
    H_1(t)=H(t/(1+4*t))/sqrt(1+4*t),
    ell_1(t)=H_1(t)/t.

C032j supplies a positive Borel function ell_1 and the positive Levy
measure L(dt)=ell_1(t)dt on (0,infinity), with

    integral_(0,infinity) min(1,t) dL(t)<infinity,
    ell_1(t)>0 for every t>0,
    B_1(s)=integral_(0,infinity) (1-exp(-s*t)) dL(t),
    Laplace(nu_1)(s)=exp(-B_1(s)), s>0,

where nu_1 is a Borel probability on X=[0,infinity), and the exponent
has zero killing and zero drift. Retain the actual divisor,
conjugation, multiplicities, exclusion of ordinate zero, strip/counting,
verified zeros through height 100, first-zero/tail and heat inputs,
and both fixed-v1 preprint qualifications in C032j. Their source-wide
correctness and the finite-zero data are not independently certified
here. Sigma=1 is Gaussian half-variance, not standard deviation.

Signed measures below are arbitrary finite real signed Borel measures
on X. They are not width measures on W=[1,2]. Neither a density of
nu_1, RH, positivity of p_1, a moment condition, odd cancellation nor
unsmoothed Xi realization is assumed. No ordering of ell_1 and ell_2
is used.

Set I=[1,3/2], P(A)=L(A intersect I), and m=P(X).

## Conclusion

One has 0<m<infinity. With P^{*0}=delta_0, the series

    lambda=exp(m)*sum_(n=0)^infinity (-1)^n P^{*n}/n!       (1)

defines a finite real signed Borel measure on X, converging in total
variation, such that

    lambda(X)=1,    |lambda|(X)<=exp(2*m)<infinity,
    lambda(I)=-exp(m)*m<0.                               (2)

There is a Borel probability mu on X, with zero drift and killing
and Levy measure L-P, for which

    nu_1*lambda=mu.                                      (3)

In particular (3) is nonnegative on every Borel set, including sets
containing zero. Thus convolution by this qualified nu_1 fails to
reflect positivity even on finite real signed half-line measures of
mass one.

This is an actual-law specialization of known measure-exponential
and subordinator results, not a claim of mathematical novelty. It
stops an automatic positivity-pullback inference for arbitrary signed
remainders. It does not show that lambda is a remainder arising from
any continuum width law, settle C032q's joint cone, establish C032r's
cancellation/moment hypotheses, or prove actual-Xi signs or RH. The
specialization passes application audit1739 below under these exact
qualifications; the external preprints and zero data are not thereby
independently verified.

## Proof

### Cited tools, convention and specialization

Reuse SPECIALIZE assessment1736 and source-notes1736. For finite real
signed Borel measures on R, import the convolution exponential

    E(Q)=sum_(n=0)^infinity Q^{*n}/n!,
    ||E(Q)||_TV<=exp(||Q||_TV),
    E(Q)*E(-Q)=delta_0.

The definitions and norm bound are in Vydas Cekanavicius and
Palaniappan Vellaisamy, *On closeness of two discrete weighted sums*,
Modern Stochastics: Theory and Applications 5(2) (2018), 207-224,
[Section 1 immediately after (1), and the inverse use (23)-(24)
in the proof of Theorem 2.1](https://www.vmsta.org/journal/VMSTA/article/114/read),
DOI 10.15559/18-VMSTA103. Their finite-signed-measure exponential
framework applies to measures on R, without a lattice or density
hypothesis; the paper's later discrete approximation bounds are not
being applied here. Only this known exponential/inverse framework is
imported, not reproved.

Mathias Trabs, *Information bounds for inverse problems with application
to deconvolution and Levy models*, Ann. Inst. H. Poincare Probab.
Statist. 51(4) (2015), 1620-1650,
[Section 4.2, (4.8), p.1636 and the reflected inverse display
p.1637](https://www.numdam.org/article/AIHPB_2015__51_4_1620_0.pdf),
is a compatible finite-activity source. Its reflected kernel display
is not directly substituted as an inverse on X. We use the unreflected
measure-exponential convention above: negating P in E(-P) changes
coefficients, not jump locations. Equivalently, reflection of both
factors in a reflected inverse identity restores this convention,
since reflection commutes with convolution. No score-operator
injectivity or density hypothesis from that paper is used.

For the positive residual law import Jean Bertoin, *Subordinators,
Levy processes with no negative jumps, and branching processes*,
Maphysto 2000 course,
[Theorem 1.2(ii), proof pp.7-8 and finite-activity case
p.9](https://www.maphysto.dk/oldpages/events/LevyBranch2000/notes/bertoin.pdf).
A positive measure on (0,infinity) with finite integral of min(1,t)
gives a subordinator law at time one; zero drift and killing give
Laplace exponent integral (1-exp(-s*t)) against that measure.

For positive half-line convolution transforms and uniqueness use
Ante Mimica, *Laplace transform*, Dresden course, 27 April-1 May 2015,
[Proposition 1.4(iv), pp.6-7 and Proposition 1.8,
pp.9-10](https://web.math.pmf.unizg.hr/~amimica/lt.pdf),
as already inspected in assessment1559. Only uniqueness of finite
positive Borel measures on [0,infinity) is used, not the source's
inversion formula at zero.

The remaining work checks this law's restricted measure, its inverse's
support and negative set, normalization, and the positive residual
identification. The cited general theorems do not supply those checks
for this qualified nu_1.

### Finite positive subfactor and its signed inverse

The Borel measure P is positive and carried by I. Since min(1,t)=1
on I, Levy integrability gives

    m=integral_I ell_1(t)dt
       <=integral_(0,infinity) min(1,t) dL(t)<infinity.

It is strictly positive. Indeed the measurable sets
I_k={t in I: ell_1(t)>=1/k}, k>=1, cover I by pointwise strict
positivity. Some I_k has positive Lebesgue measure, because I has
positive Lebesgue measure and a countable union of null sets is null.
Then m>=Lebesgue(I_k)/k>0. This needs neither a numerical lower bound
nor continuity of ell_1.

Extend P to R by zero. Each P^{*n} is a positive measure of mass m^n;
for n>=1 it is carried by [n,3*n/2], since every jump belongs to I.
Consequently

    sum_(n=0)^infinity ||exp(m)*(-1)^n P^{*n}/n!||_TV
        =exp(m)*sum_(n=0)^infinity m^n/n!=exp(2*m).

Thus the imported exponential gives the finite signed measure (1).
Every term is carried by X; convergence in total variation retains
zero restriction to R\X, so lambda is a measure on X. Its norm
satisfies (2). Evaluation on X is a bounded linear functional in
total variation, hence

    lambda(X)=exp(m)*sum_(n=0)^infinity (-m)^n/n!=1.

Likewise evaluation on I can be made term by term. The n=0 term
is zero on I since 0 is not in I. For every n>=2 its supporting
interval has lower endpoint n>=2>3/2, so that term is also zero on I.
The n=1 term alone gives

    lambda(I)=-exp(m)*P(I)=-exp(m)*m<0.

There is no cancellation hidden at either endpoint, and no assumption
of disjoint supports among the higher convolution powers is needed.
The norm estimate is an upper bound, not an asserted equality.

Define the probability

    pi=exp(-m)*E(P).

Its series has positive terms of total mass exp(-m)*exp(m)=1,
all carried by X. The imported inverse identity gives

    pi*lambda=E(P)*E(-P)=delta_0.                         (4)

Both factors in (4) are finite signed measures, and all convolution
products are defined in total variation. In particular this is an
identity of measures, not merely a formal transform calculation.

### Positive residual and all-Borel convolution identity

Let R=L-P, understood concretely as the restriction of L to
(0,infinity)\I. This avoids subtracting possibly infinite total
Levy masses. R is positive, has no atom at zero, and

    integral min(1,t) dR(t)<=integral min(1,t) dL(t)<infinity.

Bertoin's cited result therefore supplies a Borel probability mu on
X with zero drift and killing and transform

    Laplace(mu)(s)=exp(-B_R(s)),
    B_R(s)=integral (1-exp(-s*t)) dR(t), s>0.

The integral is finite: for s>0 and t>0,
1-exp(-s*t)<=max(1,s)*min(1,t). Write also
B_P(s)=integral (1-exp(-s*t)) dP(t). Since L=P+R as positive
measures, integration of this nonnegative integrable function gives

    B_1(s)=B_P(s)+B_R(s).                                (5)

The positive series for pi and the convolution transform formula give

    Laplace(pi)(s)=exp(-m)*sum_(n=0)^infinity
                       (integral exp(-s*t) dP(t))^n/n!
                  =exp(-B_P(s)).

All sums here have nonnegative terms; P is finite and the exponential
test is bounded. Thus pi*mu and nu_1 are finite positive measures
on X with equal Laplace transforms by (5). Positive-measure
uniqueness, including the point zero, identifies

    nu_1=pi*mu.                                         (6)

Finally, finite-signed convolution is associative and commutative on
R, and hence on these half-line-supported measures. In the present
application, the absolute integral of an indicator against the product
of their variation measures is at most
||pi||_TV*||mu||_TV*||lambda||_TV<=exp(2*m)<infinity.
Fubini and the addition map therefore justify these operations on
every Borel set. Combining (4) and (6) yields

    nu_1*lambda=(pi*mu)*lambda
               =mu*(pi*lambda)=mu*delta_0=mu.

For every Borel A in X this equals mu(A)>=0, and for A=X it equals
one. No signed-measure Laplace uniqueness, density, unbounded moment
test, limiting width or omitted zero atom occurs. Equations (2)-(3)
meet all parts of the stated positivity-reflection counterexample.

The measure lambda lives on output space X, with no established
representation as the signed remainder of a width mixture. Therefore
this counterexample alone supplies neither the positivity nor the
cancellation needed for the continuum width problem. The main
all-degree positivity gap is unchanged. ∎

### Application audit1739, 19 November 2026

Verdict: the stated conditional counterexample passes the complete
application audit under unchanged SPECIALIZE assessment1737, separately
approved1738. Source-notes1736 and assessment1559 supply the already
inspected source statements and essential proof cases. This is local
verification of a known-tool specialization, not a new general theorem
or a source-wide verification of either fixed-v1 preprint. No correction
to the mathematical argument, hypotheses or conclusion was necessary.

1. **Exact input and restricted mass.** C032j supplies the strictly
   positive Borel density, Levy integrability, probability transform and
   absence of killing and drift used here. It also supplies every
   inherited divisor, multiplicity, conjugation, finite-height, first-zero,
   heat and fixed-v1 qualification. The sigma=1 specialization matches
   its Gaussian half-variance convention. On I=[1,3/2], min(1,t)=1,
   so restriction gives finite mass. The sets {ell_1>=1/k} cover I;
   countable subadditivity of Lebesgue measure ensures that at least
   one has positive measure. Hence m>0 without continuity, finite total
   Levy mass or a quantitative zero estimate. The direct local input
   remains C032j alone. C032u/q/r/v describe comparisons or unpaid
   downstream problems; none supplies a premise of this construction.

2. **Signed measure, normalization and negative witness.** The positive
   convolution power P^{*n} has mass m^n and carrier [n,3n/2] for n>=1;
   P^{*0}=delta_0. The sum of term norms in (1) is exp(2m), proving
   absolute total-variation convergence. It only bounds the norm of
   the sum from above. Both evaluation on X and evaluation on I are
   bounded functionals of norm at most one, so the displayed termwise
   evaluations are justified. Evaluation on X gives exp(m)exp(-m)=1.
   On I the zero-jump term vanishes, and n>=2 has lower support bound
   2>3/2. The remaining term is exactly -exp(m)m<0. Endpoints do not
   introduce another term. Overlap of higher-power supports is irrelevant.
   All powers and their total-variation limit are carried by X.

3. **Inverse convention.** The positive series pi=exp(-m)E(P) has mass
   one. The cited finite-signed-measure exponential identity applies
   to P extended by zero to R and gives pi*lambda=delta_0. The scalar
   factors exp(-m) and exp(m) cancel. The minus sign in E(-P) acts on
   coefficients, with every jump remaining nonnegative. Trabs's reflected
   kernel and density-dependent score injectivity are not substituted.
   No claim about invertibility of the full, possibly infinite-activity
   law nu_1 is needed.

4. **Residual law and positive uniqueness.** R is the restriction of L
   to the complement of I in (0,infinity), not a subtraction of infinite
   masses. It is positive, has finite integral of min(1,t), and has no
   zero atom as a Levy measure. With zero killing and drift it satisfies
   Bertoin's converse hypotheses and gives a probability mu on X. The
   displayed integrand bound makes B_P and B_R finite at every s>0.
   Positive integral additivity for L=P+R proves (5). Tonelli for pi's
   positive series yields exp(-B_P). The measures pi*mu and nu_1 are
   positive finite measures with identical Laplace transforms on s>0;
   Mimica's uniqueness theorem therefore gives (6), including zero.
   No signed transform uniqueness or moment assumption is being used.

5. **Every Borel set and retained scope.** For a Borel indicator, the
   triple integral against the product variation measures is bounded
   by 1*1*exp(2m). Signed Fubini, associativity and commutativity are thus
   legitimate and give nu_1*lambda=mu as measures, not merely for
   transform tests. In particular no zero atom is discarded. This
   validates failure of positivity reflection on the stated mass-one
   signed half-line class. It does not put lambda in a width-remainder
   range or mu in C032q's width-mixture range. Full J_eta cancellation,
   moment/tail implications and actual-Xi transfer remain unpaid.

All discriminating checks in assessment1737 pass. The unrestricted
pullback inference stays stopped. A representation-specific claim
requires its own source comparison and mathematical test; this audit
provides neither such a claim nor a reason to repeat the same inverse
construction. Full matching Mathlib coverage remains unknown.

## Mathlib

Full matching coverage of this qualified actual-law specialization
has not been checked and remains unknown. Supporting finite-signed
convolution, measure-exponential and subordinator APIs have not been
assessed here. No Mathlib theorem replaces either fixed-v1 preprint
input or the cited probability and measure-exponential results.
