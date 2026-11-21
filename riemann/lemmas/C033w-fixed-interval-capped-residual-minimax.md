# Corollary C033w: fixed-interval capped residual minimax

## Hypotheses

Use exactly C033l's qualified probability laws on X=[0,infinity).
The width interval is W=[1,2]. Write

    H(u)=sum_(rho in Z+) exp(-u*z_rho^2),
    ell_sigma(t)=H(t/(1+4*sigma*t))/(t*sqrt(1+4*sigma*t)),
    B_sigma(s)=integral_0^infinity (1-exp(-s*t))*ell_sigma(t) dt,
    k(s,sigma)=integral_X exp(-s*u) dnu_sigma(u)=exp(-B_sigma(s)).

Here Z+ counts positive-ordinate nontrivial zeta zeros with multiplicity,
and z_rho=gamma_rho-i*(beta_rho-1/2). Each nu_sigma is the probability
law with zero drift and killing specified in C033l. For the exact
residual, put I_0=[1,3/2], L(dt)=ell_1(t)dt and
R=L restricted to (0,infinity)\I_0. Its zero-drift, zero-killing
probability law mu has transform

    m(s)=integral_X exp(-s*u) dmu(u)
        =exp(-integral_(0,infinity) (1-exp(-s*t)) dR(t)), s>0.

The observation interval in this result is I=[1,2]; it is distinct
from the removed Levy interval I_0. Retain C033l's actual divisor,
conjugation and multiplicity conventions, excluded ordinate zero,
strict strip |beta-1/2|<1/2, gamma>14, N(T)=O(T log(T+2)), verified
zeros through100, retained real zero in (14,15), reciprocal-square-tail
qualification, heat positivity and separate fixed-j=0,1 error inputs,
both fixed-v1 preprint qualifications and Gaussian half-variance
normalization. None of those external inputs or zero data is independently
verified here. C033j's exclusion is not used in the argument below.

Set

    A_2={eta finite real signed Borel on W:
                         eta(W)=1, |eta|(W)<=2},
    Lambda={lambda finite real signed Borel on I: |lambda|(I)<=1},
    (Keta)(s)=integral_W k(s,sigma) deta(sigma),
    d_2=inf_(eta in A_2) ||m-Keta||_(C(I)).

All atoms, singular continuous parts and infinite support are allowed
in both measure classes. Observation measures have no mass constraint.
No positivity of eta or its output, undamped moments, cancellation,
RH, or actual-Xi realization is assumed. Use C032m's joint continuity
and C033l's identification B_sigma(s)=b_sigma(sqrt(s)).

## Conclusion

For lambda in Lambda define the continuous real width payoff and its
dual objective by

    f_lambda(sigma)=integral_I k(s,sigma) dlambda(s),
    D(lambda)=integral_I m(s) dlambda(s)
                    -(3*max_W f_lambda-min_W f_lambda)/2.

Then

    d_2=min_(eta in A_2) ||m-Keta||_(C(I))
       =max_(lambda in Lambda) D(lambda).                 (1)

Both extrema are attained over the indicated full classes.
Let S={s_1,...,s_n} be any finite nonempty subset of I, enumerated
without repetition, and let h>=0 satisfy
sup_(s in I) min_(t in S)|s-t|<=h. Define

    d_S=inf_(eta in A_2) max_(1<=j<=n)|m(s_j)-(Keta)(s_j)|,
    f_c(sigma)=sum_(j=1)^n c_j*k(s_j,sigma).

There are attained minima and maxima in

    d_S=min_(eta in A_2) max_j |m(s_j)-(Keta)(s_j)|
       =max_(sum_j |c_j|<=1)
          [sum_j c_j*m(s_j)-(3*max_W f_c-min_W f_c)/2],   (2)
    0<=d_2-d_S<=6*h.                                     (3)

Only the observations have been discretized in (2); the width class
remains A_2. The finite problem has an optimal atomic observation
measure sum_j c_j delta_(s_j). No finite-support optimizer is asserted
for (1), nor is any finite-support restriction imposed on a primal
optimizer. The support maximizers in C033o are not being identified
with primal minimizers here.

This is a local specialization of known minimax, compactness and
Laplace regularity, not progress beyond the inspected general results.
It supplies no evaluated d_2 or d_S, no claim d_2>0, no numerical
certificate or feasible approximation, and no arbitrary-variation
estimate. Signed height, full cancellation and actual-Xi positivity
remain unresolved. C033v is unused. Application audit1795 below passes
under the unchanged qualifications; this is not a candidate resolution
of RH.

## Proof

### Imported tools and the unchanged source gate

Reuse SPECIALIZE assessment1792 and source-notes1792/1748. Import:

- M. Sion, *On general minimax theorems*, Pacific J. Math.8(1)
  (1958),171-176, [Theorem3.4, printed p174](https://msp.org/pjm/1958/8-1/pjm-v8-n1-p14-p.pdf),
  with definitions2.4-2.7: for two compact convex strategies and a
  real separately upper/lower semicontinuous, quasi-concave/convex
  payoff in the maximizing/minimizing variables, sup-inf equals
  inf-sup. The inspected complete proof and Remark3.6 are recorded
  in source-notes1792. We use this two-compact-set version.
- T. Buhler and D. A. Salamon, *Functional Analysis*, version11 May2016,
  [Example1.3.7 p28 and Theorem3.2.4 p100](https://math.jhu.edu/~js/Math637/eth.functionalanalysis.pdf):
  real signed regular measures identify isometrically with the dual
  of C of a second-countable compact Hausdorff space, and closed dual
  balls are weak-star compact. The source coverage is recorded1748.
- A. Mimica, *Laplace transform*, Dresden course,27 April-1 May2015,
  [Remark1.2(i) and Proposition1.4(i), printed pp5-7](https://web.math.pmf.unizg.hr/~amimica/lt.pdf):
  positive-argument smoothness and derivative formula for positive
  measures with finite positive-real Laplace transforms. Its precise
  probability specialization is C033n's Proof (6)-(7).

Use the standard named Fubini theorem for absolutely integrable
functions on products of finite positive measure spaces, applied to
Jordan parts, and the mean value and extreme value theorems. C033o's
audited support formula for every continuous real width payoff is
imported unchanged. None of these general theorems or that support
calculation is reproved. The work here checks their interval-specific
hypotheses, attainment and uniform finite-observation comparison.

### Both full signed strategy spaces and the continuous kernel

Give measures on W and I the weak-star topologies from C(W;R) and
C(I;R), respectively. These are the restrictions of Hausdorff locally
convex topological vector-space topologies. Finite Borel measures on
compact metric intervals are regular, including both Jordan parts of
a signed measure. Thus the cited signed Riesz identification covers
all measures allowed here, with dual norm exactly total variation.

C033l's compactness argument applies unchanged to A_2: its mass-one
condition is closed because evaluation at the constant function 1 is
weak-star continuous, inside the compact radius-2 dual ball. It is
nonempty (delta_1 is feasible) and convex. The observation class Lambda
is exactly the radius-1 closed dual ball of C(I;R), so is compact and
convex by the same cited theorems and is nonempty (it contains zero).
There is no restriction to positive or atomic inputs.

C032m and the identification in the hypotheses show that
k(s,sigma)=exp(-b_sigma(sqrt(s))) is jointly continuous on I times W.
The positive square root is continuous on all of I. Probability
integration gives 0<k<=1 and 0<m<=1. The function m is continuous
on I by dominated convergence, dominated by 1 under the probability
mu. Uniform continuity of k on the compact product and the bounded
variation inequalities show Keta in C(I;R) and f_lambda in C(W;R).

We need continuity into these uniform norms, not just convergence
at individual coordinates. Suppose a net eta_alpha in A_2 converges
weak-star to eta in A_2. Given epsilon>0, choose finitely many points
t_i in I so that every s in I has an i with

    sup_(sigma in W)|k(s,sigma)-k(t_i,sigma)|<epsilon/8.

This is possible by joint uniform continuity and compactness of I.
Weak-star convergence at those finitely many continuous width
functions makes every |integral_W k(t_i,sigma) d(eta_alpha-eta)|
less than epsilon/2 eventually. Since |eta_alpha-eta|(W)<=4,
the triangle inequality gives, uniformly for all s,

    |(Keta_alpha)(s)-(Keta)(s)|<epsilon/2+4*epsilon/8=epsilon.

Thus K:A_2 -> C(I;R) is continuous in the asserted topologies.
For a weak-star convergent net lambda_alpha -> lambda in Lambda,
choose finitely many widths sigma_i so that each sigma has an i with
sup_(s in I)|k(s,sigma)-k(s,sigma_i)|<epsilon/4. Weak-star convergence
at these finitely many continuous observation functions and
|lambda_alpha-lambda|(I)<=2 give
||f_(lambda_alpha)-f_lambda||_infinity<epsilon/2+2*epsilon/4=epsilon
eventually. Hence lambda -> f_lambda is also continuous into C(W;R).
These net arguments prove continuity without a sequential-compactness
assumption and retain both interval endpoints.

### Real payoff, signed Fubini and attained minimax

Define the real affine payoff

    P(lambda,eta)=integral_I [m(s)-(Keta)(s)] dlambda(s).

All integrals are finite. In particular,

    integral_(I times W) |k(s,sigma)| d(|lambda| times |eta|)
       <= |lambda|(I)*|eta|(W)<=2.

Fubini applied to the four products of finite positive Jordan parts
therefore gives

    P(lambda,eta)=integral_I m dlambda-integral_W f_lambda deta. (4)

For fixed eta the first definition is weak-star continuous in lambda;
for fixed lambda, (4) is weak-star continuous in eta. In fact the
payoff is jointly continuous on Lambda times A_2. For convergent nets
(lambda_alpha,eta_alpha) -> (lambda,eta), write the difference as

    integral_I (m-Keta) d(lambda_alpha-lambda)
       +integral_I (Keta-Keta_alpha) dlambda_alpha.

The first term tends to zero by weak-star convergence and continuity
of the fixed test; the second is at most ||Keta-Keta_alpha||_infinity
in absolute value and tends to zero by the preceding paragraph.

For fixed eta, write r=m-Keta. Then

    max_(lambda in Lambda) P(lambda,eta)=||r||_infinity.   (5)

Indeed the variation inequality gives the upper bound. If r is
nonzero, choose s_0 attaining |r(s_0)| and take
lambda=sign(r(s_0))*delta_(s_0), of variation one. If r is zero,
lambda=0 suffices. These are measures on the closed I, so an endpoint
extremizer is permitted.

For fixed lambda, C033o applies to the continuous real f_lambda.
Taking the infimum of (4) over eta in A_2 gives

    inf_(eta in A_2) P(lambda,eta)
       =integral_I m dlambda-sup_(eta in A_2) integral_W f_lambda deta
       =D(lambda).                                      (6)

The support is subtracted, not added. C033o includes negative and
constant payoffs: if f_lambda=c, its support is c and the subtracted
expression (3c-c)/2 is exactly c. No saturation of variation is assumed.

Apply Sion Theorem3.4 with lambda the maximizing variable and eta the
minimizing variable. Both sets are nonempty compact convex subsets
of the specified real topological vector spaces. The real payoff is
continuous separately (indeed jointly) and affine in each variable,
so is quasi-concave in lambda and quasi-convex in eta with the required
semicontinuity. Using (5)-(6), its equality is precisely

    inf_(eta in A_2) ||m-Keta||_infinity
       =sup_(lambda in Lambda) D(lambda).

For attainment, eta -> ||m-Keta||_infinity is continuous on compact
A_2 by the norm continuity of K. Also lambda -> integral m dlambda
is weak-star continuous, and max and min are 1-Lipschitz functionals
on C(W;R). The norm continuity of lambda -> f_lambda proves D continuous
on compact Lambda. The extreme value theorem gives both attainments
in (1). Since D(0)=0 and a norm is nonnegative, the proof covers a
zero optimum without claiming it is excluded.

### Finite observation dual with continuum widths

For S as in the conclusion let C_S={c in R^n: sum_j |c_j|<=1}.
This is a nonempty compact convex set. Associate to c the signed
observation measure lambda_c=sum_j c_j delta_(s_j). The distinctness
of the points implies |lambda_c|(I)=sum_j |c_j|, including zero
coefficients. The map c -> lambda_c is weak-star continuous because
integration of any continuous observation function is a finite linear
combination of its values.

Restrict P to C_S times A_2. It remains real, affine in both arguments
and separately continuous. For every eta,

    max_(c in C_S) sum_j c_j*r(s_j)=max_j |r(s_j)|.

The upper bound is the l1 inequality; equality is given by a signed
coordinate vector at a maximum, or by zero if every value is zero.
For fixed c, the width support is C033o's value for f_c. Sion therefore
gives the equality in (2). Its primal objective is a finite maximum
of continuous coordinate absolute values on compact A_2. Its dual
objective is continuous on C_S, since c -> f_c is continuous in
uniform norm and max/min are continuous there. Both extrema are
attained. This establishes a finite atomic optimal observation for
this finite problem only, with no assertion about a width grid or
the supports of the primal minimizers.

### Uniform full-class modulus and the required mesh allowance

Use only the universal probability-law part of C033n's Proof (6)-(7),
not its existential separator data. Its cited Mimica theorem applies
to mu and every nu_sigma because their Laplace transforms are finite
at every positive argument. With reference argument 1, (7) states
|(Lrho)'(r)|<=2 for r>=1/2 for each such probability rho, independently
of sigma. The mean value theorem along any segment in [1,2] yields

    |m(s)-m(t)|<=2|s-t|,
    sup_(sigma in W)|k(s,sigma)-k(t,sigma)|<=2|s-t|.

Consequently every eta in the full A_2 satisfies

    |(m-Keta)(s)-(m-Keta)(t)|
       <=2|s-t|+|eta|(W)*2|s-t|<=6|s-t|.                (7)

No derivative is taken through a signed width mixture. Possible law
atoms at u=0 are included and contribute zero to the derivative;
no undamped moment at zero is required. The constant is uniform in
eta, its support, both width endpoints and both observation endpoints.

For every s in I a nearest t in the nonempty finite S exists and has
|s-t|<=h. Applying (7) and taking the supremum over s proves for each
eta in A_2

    max_(t in S)|(m-Keta)(t)| <= ||m-Keta||_infinity
       <= max_(t in S)|(m-Keta)(t)|+6h.                  (8)

The first inequality gives d_S<=d_2 after infimization. Evaluate the
second at an attained minimizer for d_S to get d_2<=d_S+6h. This is
(3), including all boundary, constant and zero-residual cases. There
is no division by h and no assumption of a positive optimum. This
completes the approved specialization.

The result provides an exact variational interface, not evaluated
width extrema or a certified positive margin. It does not reopen
coarse-box stop1571, evaluator stops1576/1781/1782, or parked C033v
propagation. It supplies no new realization, height or RH assertion.

### Application audit1795 — 19 November 2026

Verdict: (1)-(3) pass the exact application audit covered by SPECIALIZE
assessment1793, separately source-approved1794. No mathematical repair
or additional hypothesis is required. This checks the specialization
of the cited known tools, not a new minimax theorem, an evaluated
certificate or independent verification of the inherited inputs.

1. **Full signed classes and topology.** On each compact metric
   interval every finite positive Borel measure is regular; applying
   this to both Jordan parts includes every allowed signed measure.
   The cited signed Riesz theorem identifies its norm with total
   variation. The weak-star topology is Hausdorff and locally convex,
   and Banach--Alaoglu applies to both closed balls. Evaluation at the
   continuous constant 1 makes the mass-one constraint closed.
   Thus A_2 is compact, convex and nonempty, and Lambda is compact,
   convex and nonempty. The proof includes nonsaturated, atomic,
   singular and infinitely supported measures. Lambda has no mass
   constraint. No positivity restriction has been introduced.

2. **Both uniform-norm continuity assertions.** C032m supplies joint
   continuity of b_sigma(w), and C033l supplies its identification at
   the positive square root. Hence k is continuous on the entire
   compact product I times W. For a weak-star convergent net in A_2,
   the finite observation net in the proof controls the difference
   at all its centers eventually, since there are finitely many.
   The remaining error is bounded by 4*(epsilon/8), using the
   difference variation bound 4. The center error is <epsilon/2,
   so the final uniform error is <epsilon. The same argument in the
   other variable uses difference variation at most 2 and width
   kernel error <epsilon/4. It too gives uniform error <epsilon.
   These are continuity statements for nets on the capped spaces,
   not merely pointwise or sequential assertions. Continuity of m
   follows by domination by 1 under mu. Both closed endpoints are
   included in every compactness and continuity assertion.

3. **Signed integrability and minimax orientation.** The probability
   kernels satisfy |k|<=1. Therefore its integral against the product
   of variation measures is at most 1*2=2, so each of the four Jordan
   products meets absolute Fubini. The payoff is real affine in both
   variables. For fixed eta its continuous test is m-Keta; for fixed
   lambda, signed Fubini gives the continuous width test f_lambda.
   This verifies the required separate continuity. The additional
   joint-continuity argument is valid because the varying lambda
   has variation at most 1 and K is uniform-norm continuous.
   Sion Theorem3.4 applies with lambda maximizing and eta minimizing:
   affinity gives the required quasi-concavity/quasi-convexity.
   Maximizing in lambda yields the residual norm, with a signed
   Dirac mass at any absolute maximum; zero residual permits zero.
   Minimizing in eta subtracts its *supremal* width support. C033o
   gives precisely (3 max f_lambda-min f_lambda)/2, including negative
   and constant f_lambda. Thus the sign and order in (1) are correct.

4. **Both continuum extrema.** The primal norm is continuous on A_2
   by the proved continuity of K. The dual objective is continuous
   on Lambda: its first term is a weak-star continuous evaluation,
   its kernel image is uniform-norm continuous, and max and min
   change by at most the uniform change of that image. The extreme
   value theorem therefore supplies both stated extrema. A zero
   optimum is allowed, since D(0)=0. Neither compactness nor Sion
   establishes a positive value, an effective optimizer or finite
   support for a continuum optimizer.

5. **Finite observation problem.** Distinct nodes make the variation
   of sum c_j delta_(s_j) equal to sum |c_j|. The finite l1 ball is
   compact and convex, its map to Lambda is continuous, and it has
   no coefficient-sum constraint. Its support on a residual vector
   is its largest absolute coordinate, including the all-zero case.
   Restricting only the maximizing strategy therefore gives exactly
   (2), using the same C033o width support and the same continuum
   A_2. Both objectives are continuous on their respective compact
   domains, so both extrema are attained. This asserts atomic
   observation attainment only for the finite problem and makes no
   atomic restriction on a minimizing width measure.

6. **Uniform modulus and direction of the error.** C033n Proof (6)-(7)
   is a universal probability-law estimate: with reference argument
   1, its derivative bound is 2 for every r>=1/2. Its proof uses
   u exp(-r u)<=1/r<=2 and total mass one, independently of any
   separator data. Thus it applies to mu and every nu_sigma on all
   segments in I. The individual transform differences are at most
   2|s-t|, uniformly in sigma. Integrating their width difference
   against variation at most 2 and paying the residual-side 2 gives
   exactly 6|s-t|. This differentiates no signed mixture and needs
   no moment at zero; atoms at zero contribute zero to the derivative.
   A nearest node exists in any nonempty finite S. Consequently (8)
   holds for each eta. Its lower inequality yields d_S<=d_2; its upper
   inequality at a minimizing eta for d_S yields d_2<=d_S+6h.
   No infimum/supremum exchange beyond the separately justified
   minimax is hidden here. The proof needs neither division by h
   nor h>0; it proves the conditional statement for every specified
   covering radius, including all endpoint and constant cases.

7. **Dependencies and limits.** The existing direct inputs C032m,
   C033l, C033n and C033o suffice. C033n is used only for its universal
   probability regularity, not its assumed separator; C033l is used
   for its laws, kernel identification and compactness interface,
   not its exclusion-based separation conclusion. Neither C033j's
   exclusion nor C033v is an extra premise. All actual-divisor,
   conjugation/multiplicity, excluded-zero-ordinate, strict-strip,
   gamma>14, counting, through100/retained-real-zero, reciprocal-square
   tail, heat positivity/separate fixed-j errors, half-variance and
   fixed-v1 qualifications stated above remain unchanged. They are
   not independently audited here. No d_2 or d_S value, positive
   margin, unrestricted-variation rate, signed-height payment,
   cancellation or Xi realization follows. The stopped evaluators
   and parked propagation work remain preserved.

This completes the bounded audit. The formulas are valid under their
stated inputs; the main actual-Xi all-degree positivity gap is open.

## Mathlib

Full matching coverage of this qualified minimax and mesh result is
unchecked and unknown. Supporting signed-measure/Riesz, weak-star
compactness, minimax, Laplace differentiation and norm APIs have not
been inspected in this step. The proof is informal and conditional
on the inherited external inputs; no formal verification is claimed.
