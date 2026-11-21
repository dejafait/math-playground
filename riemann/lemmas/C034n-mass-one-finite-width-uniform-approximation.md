# Corollary C034n: mass-one finite-width uniform approximation

## Hypotheses

Retain C033l's exact original probability laws and residual, and all
qualifications of audited C034m. In particular, Z+ is the multiset of
positive-ordinate nontrivial zeta zeros with multiplicities,
z_rho=gamma_rho-i*(beta_rho-1/2), and

    H(u)=sum_(rho in Z+) exp(-u*z_rho^2),
    ell_sigma(t)=H(t/(1+4*sigma*t))/(t*sqrt(1+4*sigma*t)),
    B_sigma(s)=integral_0^infinity (1-exp(-s*t))*ell_sigma(t)dt,
    k_sigma(s)=exp(-B_sigma(s))
             =integral_[0,infinity) exp(-s*u)dnu_sigma(u).

Here nu_sigma is the original Borel probability law with zero drift
and killing, and sigma is Gaussian half-variance. Put W=[1,2] for
widths and S=[1,2] for observations. Let mu be exactly the residual
probability law whose Levy measure is ell_1(t)dt restricted to
(0,infinity) outside [1,3/2], with zero drift and killing, and set

    muhat(s)=integral_[0,infinity) exp(-s*u)dmu(u).

Retain actual divisor/conjugation and multiplicity conventions,
excluded ordinate zero, |beta-1/2|<1/2, gamma>14, counting
N(T)=O(T*log(T+2)), verified zeros through100 and a retained real
zero in (14,15), the reciprocal-square tail, heat positivity,
separate fixed-j heat-error qualifications through2, and both
fixed-v1 preprint qualifications. This proof does not independently
verify those preprints or finite-zero data. In particular, it imports
C034m only under its stated inputs, not as an unconditional assertion
about an arbitrary kernel or an arbitrary perturbed zero divisor.

Allow finite atomic real signed measures eta on W with eta(W)=1.
There is no common total-variation bound and no positivity requirement
on eta or its output. No moment condition, full odd cancellation,
signed-height estimate, actual-Xi realization or RH is assumed.

## Conclusion

For every real epsilon>0 there exist an integer n>=1, widths
sigma_1,...,sigma_n in [1,2] and real numbers a_1,...,a_n such that

    sum_(j=1)^n a_j=1,
    sup_(s in [1,2]) |muhat(s)-sum_(j=1)^n a_j*k_(sigma_j)(s)|
        < epsilon.                                          (1)

Thus the exact residual transform is in the uniform closure on S
of the finite mass-one affine combinations of the original width
sections. For each epsilon the measure eta=sum_j a_j*delta_(sigma_j)
has finite total variation; no bound uniform in epsilon is supplied.
Widths are all in W, not in an enlarged approximation family.

This is a qualitative specialization of known real norm-closure and
signed-Riesz tools using audited C034m. It supplies no numerical
approximant, rate, number of atoms, variation cost, nonnegative output,
moment control, full odd cancellation, signed-height payment or Xi
transfer. It is local progress under the inherited qualifications,
not a result claimed beyond the sources checked or an RH candidate.
Application audit1893 below passes under these unchanged qualifications.

## Proof

### Imported tools and exact scope

Reuse the unchanged SPECIALIZE assessment1888 and source-notes1889,
including the primary statement and complete proof coverage recorded
in notes1532/1748. From Theo Buhler and Dietmar A. Salamon,
*Functional Analysis*, version11 May2016,
[primary text](https://math.jhu.edu/~js/Math637/eth.functionalanalysis.pdf),
import Theorem2.3.22 and Corollary2.3.24, printed pp70-71: for a real
normed space E and linear subspace V, a point x lies in the norm
closure of V if and only if every bounded real linear functional
vanishing on V vanishes on x. V need not be closed or finite
dimensional. The closure bars omitted by the recorded PDF extraction
are essential; the criterion is norm closure, not algebraic membership.

Use the standard signed Riesz representation theorem as recorded in
the same text, Example1.3.7, printed p28: the continuous real dual
of C(M;R) for second-countable compact Hausdorff M is the space of
finite real signed regular Borel measures on M, with total-variation
norm. Supplementary primary coverage is Terence Tao, *245B, Notes12:
Continuous functions on locally compact Hausdorff spaces*, 2 March2009,
[Theorem24, Lemma29, Exercise31 and Remark33](https://terrytao.wordpress.com/2009/03/02/245b-notes-12-continuous-functions-on-locally-compact-hausdorff-spaces/).
Notes1532/1889 record its positive theorem and signed-decomposition
proof coverage; Exercise31 states the signed conclusion. The displayed
nonnegativity assertion for arbitrary signed I in Lemma29 is not used.

These general tools are imported rather than reproved. The work here
is their application to the exact original sections, the affine mass
constraint and the entire observation-measure dual. No density theorem
for a PSD kernel, algebra-closure theorem, discretization theorem or
compactness assertion for uncapped signed measures is used.

### Continuous real functions and the exact affine class

Let E=C(S;R) with norm ||f||_infinity=sup_(s in S)|f(s)|. For a fixed
sigma in W, k_sigma is real and continuous on S: if s_r tends to s
in S, exp(-s_r*u) tends pointwise to exp(-s*u) and is bounded by1
on [0,infinity). Dominated convergence for the probability nu_sigma
therefore gives k_sigma(s_r) tending to k_sigma(s). The same argument
for mu proves muhat in E. It retains all atoms, including u=0, and
requires no moment. In particular all these functions are bounded
by1. Their exact identification with the displayed heat-law sections
is part of the retained C033l/C034m inputs.

Fix the admissible reference width sigma_*=1, and define

    V=span_R {k_sigma-k_1 : sigma in W},
    A={sum_(j=1)^n a_j*k_(sigma_j) : n>=1, sigma_j in W,
                                      a_j real, sum_j a_j=1}.

The span in V is algebraic: every element is a finite sum; the empty
sum is0. We have the exact equality

    A=k_1+V.                                               (2)

Indeed, for a member of A, subtracting k_1 gives
sum_j a_j*(k_(sigma_j)-k_1), using sum_j a_j=1. Conversely, for
v=sum_(j=1)^m b_j*(k_(tau_j)-k_1) in V,

    k_1+v=(1-sum_(j=1)^m b_j)*k_1
              +sum_(j=1)^m b_j*k_(tau_j).                  (3)

These are finitely many real coefficients of sum exactly1 at widths
in W. If m=0, (3) is the single section k_1 with coefficient1.
Coincident widths and zero coefficients cause no problem; merging
coincident atoms preserves their total mass. Thus (2) is an algebraic
identity, not an assertion about an approximate mass or a limiting
signed measure.

### The full continuous real dual

Let Lambda:E->R be any continuous real linear functional vanishing
on V. The interval S is compact metric, hence second-countable and
Hausdorff. Signed Riesz therefore represents Lambda by a finite real
signed regular Borel measure h on S:

    Lambda(f)=integral_S f(s)dh(s),
    |h|(S)=||Lambda||<infinity.

This covers every continuous functional, including representatives
with endpoint atoms or singular continuous parts. Conversely every
finite real signed Borel measure on compact metric S is regular and
defines a continuous functional. There is no restriction to a finite
grid, a positive measure, a density or a common bound on ||Lambda||.

For each sigma in W, annihilation of the generator k_sigma-k_1 gives

    integral_S k_sigma(s)dh(s)=integral_S k_1(s)dh(s)=:c.    (4)

The number c is real and finite, since |k_1|<=1 and |h|(S) is finite.
Equation (4), with this arbitrary real c, is precisely the equation
in C034m: the same original k_sigma, the same closed intervals W
and S, and an arbitrary finite real signed Borel observation measure.
Audited C034m forces h=0 and c=0. Hence Lambda=0. The arbitrary-
constant conclusion is essential: the affine translation would not
justify assuming c=0 before applying C034m. No part of that lemma's
analytic continuation or large-width proof is reproved or strengthened
here, and no large width is inserted in A.

### Norm closure and finite mass-one recovery

Apply the cited norm-closure criterion to the real normed space E,
its linear subspace V, and x=muhat-k_1 in E. Every continuous real
functional vanishing on V is zero by (4) and C034m, so each such
functional vanishes on x. Therefore x lies in the norm closure of V.
For any epsilon>0 the definition of norm closure gives a v in V
with

    ||(muhat-k_1)-v||_infinity<epsilon.                   (5)

Write this particular v as a finite sum with coefficients b_j and
widths tau_j as in (3), and define

    eta=(1-sum_(j=1)^m b_j)*delta_1
                    +sum_(j=1)^m b_j*delta_(tau_j).

This is a finite atomic real signed Borel measure supported on W,
and eta(W)=1 exactly. Its total variation is finite, with the bound

    |eta|(W)<=|1-sum_(j=1)^m b_j|+sum_(j=1)^m |b_j|.

If m=0 this gives eta=delta_1. By finite linearity its transform
combination is k_1+v. Equation (5) is therefore exactly (1), with
n=m+1 and the coefficients displayed above. The number of atoms
and the finite variation bound may depend on epsilon. No infinite
series or signed-measure limit is needed to recover eta. This proves
the claimed approximation under the retained hypotheses.

Uniform approximation is asserted only on the fixed observation
interval S. It asserts neither equality of the laws on all Borel sets
nor convergence in total variation on the output half-line. It also
does not place these approximants inside any prescribed variation
cap. The recorded exact-range exclusion and fixed-cap obstructions
are thus not negated or assumed as mathematical inputs here. The
stopped evaluator, grid and inverse-rate mechanisms remain stopped.

### Application audit1893: real dual and exact finite mass

20 November2026. The separate application audit uses the unchanged
SPECIALIZE assessment1891, approved1892 before invocation. It checks
only this application of the cited tools and audited C034m, without
reproving C034m or independently certifying its external inputs.

1. **Function space.** For each original probability nu_sigma and
   for the exact residual probability mu, the integrands exp(-s*u)
   are real, bounded by1 for s in S, and converge pointwise whenever
   s converges in S. Dominated convergence against each fixed finite
   probability proves continuity at both endpoints as well as in the
   interior. Thus k_sigma and muhat are in real C(S), with norm at
   most1. No moment, density, zero-atom exclusion or uniformity in
   sigma is needed for this particular step.

2. **Affine identity.** For every finite coefficient list of sum1,
   subtracting k_1 yields a finite sum of k_sigma-k_1. Conversely a
   finite sum v=sum b_j(k_tau_j-k_1) gives reference coefficient
   1-sum b_j and remaining coefficients b_j. These are real and sum
   exactly1, all at widths in W. The empty sum gives k_1 and delta_1;
   merging coincident widths preserves mass. This verifies both
   inclusions in (2), without taking any measure limit.

3. **Entire norm dual.** Compact metric S satisfies the cited signed
   Riesz hypotheses. Every continuous real functional annihilating V
   therefore has a finite signed Borel representative h; endpoint
   atoms and singular parts are included. Annihilation of each
   generator gives integral k_sigma dh=c for every sigma in W,
   where c=integral k_1 dh is a finite real number. This is exactly
   C034m's constant equation, including its full signed-measure class
   and arbitrary c. Its qualified conclusion h=c=0 makes the whole
   annihilator zero. The argument never sets c=0 in advance and never
   assumes that a positive-functional theorem covers signed functionals.

4. **Norm and finite recovery.** The cited real norm-closure criterion
   applies to the algebraic subspace V whether or not V is closed.
   Since its annihilator is zero, it applies in particular to
   x=muhat-k_1. Membership in the norm closure supplies an actual
   v in V at strict distance less than every prescribed epsilon>0.
   Algebraic span membership supplies a finite representation of v;
   item2 then gives n=m+1>=1 and eta(W)=1 exactly. The displayed sum
   of absolute coefficients is finite and bounds |eta|(W), even with
   repeated atoms. There is no bound uniform in epsilon.

5. **Scope and inputs.** The norm in (5) is precisely the supremum
   over all s in [1,2], not a sampled or pointwise norm. All approximant
   widths remain in [1,2]; C034m's use of analytic continuation does
   not enlarge the approximation class. The result is conditional on
   the same exact laws and all retained actual-divisor, heat-error,
   finite-zero and fixed-v1 inputs. Its direct mathematical inputs
   are still C033l and C034m, already recorded in the DAG. No graph
   change is needed. The known closure/Riesz tools are imported by
   the precise citations above, not reproved or claimed as new.

The application passes without mathematical repair. This establishes
acceptance of the previously unaudited local input, not a new result
beyond the checked tools. C033j's exact-range exclusion and C034l's
cap-two interval bound have different conclusions and remain intact.
No nonnegative output, uniform input variation, rate, full odd
cancellation, moment payment, signed-height control or Xi realization
has been established. Supporting and matching Mathlib coverage remains
unknown as stated below.

## Mathlib

Full matching coverage for this qualified original-width affine
specialization has not been checked and is unknown. Supporting
Hahn--Banach norm-closure, signed-Riesz, continuous-function and
finite-atomic-measure APIs were not assessed in this step. No formal
verification of this argument, C034m's external inputs or the finite
zero data is claimed.
