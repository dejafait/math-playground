# Lemma 800: the finite Mellin Gaussian completion allowance

## Hypotheses

Use L798's domain, saddle and branches:

    D={s: |s|>=6000, Re(s)>=-|s|/(8 log|s|)},
    F(z)=z(pi exp(2z)-9/4), x=x(s)=u+ih, F(x)=s,
    Q=pi exp(2u), d=3/(16u), A=2F'(x)/x, B=|A|,
    theta=Arg A, a=exp(-i theta/2),
    G(s)=a integral_{-d}^{d} exp(-Bv^2/2) dv,
    C(s)=sqrt(2pi/A), T_G(s)=|G(s)-C(s)|/|C(s)|.

Arg and the complex square root are principal. L798, using L797,
supplies on all D

    u>3, Q>1000, B>(15/4)Q, Re A>0,
    |a|=1, C=a sqrt(2pi/B), |C|=sqrt(2pi/B)>0.          (1)

The target is exactly the normalized finite Gaussian test approved in
`drafts/literature/2026-11-05-mellin-gaussian-completion-test.md`.
The allowance is taken from bramble_trace, *A continuum certificate for
the decreasing Levy factor associated with Riemann xi*,
[paper23 v1](https://rstation.ai/problems/riemann_hypothesis/papers/23),
18 October 2026, Section 3, Lemma 2, (10)–(14). No tail estimate from
that paper or its unread supplementary derivations is assumed.

## Conclusion

For every s in D, with t=d sqrt(B/2)>0,

    T_G(s)=erfc(t)
      < (16/3)sqrt(8/(15pi)) (u/sqrt(Q))
                                  exp(-(15/8)Qd^2)
      < (47u/(20sqrt(Q))) exp(-(33/20)Qd^2).           (2)

Thus the specified omitted Gaussian cost is strictly below the source's
2.35/1.65 allowance. This is an effective specialization of known real
Gaussian-tail bounds, not a mathematical novelty claim. Step519 supplies
the proof; step521's independent audit below verifies it without a
mathematical correction or extra hypothesis.

The result concerns exactly the finite G of L798. It supplies no global
theta-contour tail or continued endpoint identity, Mellin relative-error
assembly, quotient/inversion bound, evaluator/certificate, Levy-density
sign or sufficient actual-Xi mixed-positivity theorem.

## Proof

### Exact real Gaussian completion with the existing branch

Import [NIST DLMF 7.7.6](https://dlmf.nist.gov/7.7.E6): for real y
and Re(alpha)>0,

    integral_y^infinity exp(-(alpha v^2+2 beta v+gamma)) dv
      = (1/2)sqrt(pi/alpha) exp((beta^2-alpha gamma)/alpha)
        erfc(sqrt(alpha)y+beta/sqrt(alpha)).            (3)

Only its real specialization alpha=B/2>0, beta=gamma=0 is used.
All these integrals converge absolutely. At y=0, erfc(0)=1 and
evenness give

    integral_R exp(-Bv^2/2) dv = sqrt(2pi/B).

At y=d, (3) gives

    2 integral_d^infinity exp(-Bv^2/2) dv
       = sqrt(2pi/B) erfc(d sqrt(B/2)).                (4)

In particular the finite integral is strictly between zero and its
complete value: d>0 and the real integrand is positive. Using the
exact complex identity in (1), not just its absolute value, we have

    C-G = a [sqrt(2pi/B)-integral_{-d}^{d} exp(-Bv^2/2) dv]
        = a 2 integral_d^infinity exp(-Bv^2/2) dv.

Taking absolute values and dividing by |C| proves the equality in (2)
by (4). There is no contour rotation or replacement of B by Re A.
Only integrals in the real parameter v are completed.

### Imported Mills bound and uniform constant comparison

[NIST DLMF 7.8.1–7.8.2](https://dlmf.nist.gov/7.8.E2) defines

    M(t)=exp(t^2) integral_t^infinity exp(-w^2) dw

and states, for real t>=0,

    M(t) <= 1/(t+sqrt(t^2+4/pi)).                     (5)

The present argument t=d sqrt(B/2) is strictly positive. Since
sqrt(t^2+4/pi)>t, (5) and the defining real erfc integral imply

    erfc(t)=(2/sqrt(pi))exp(-t^2) M(t)
           < exp(-t^2)/(sqrt(pi)t)
           = sqrt(2/pi)/(d sqrt(B)) exp(-Bd^2/2).     (6)

Both factors on the right decrease with B>0. Thus (1), d=3/(16u)
and Q>0 yield

    T_G < (16/3)sqrt(8/(15pi)) (u/sqrt(Q))
                                      exp(-(15/8)Qd^2). (7)

The prefactor is strictly less than 47/20. Indeed pi>3 gives

    [(16/3)sqrt(8/(15pi))]^2 < 2048/405 < 2209/400,

where the last exact comparison is

    2048*400=819200 < 894645=2209*405.

All prefactors are positive, so taking square roots is legitimate.
Finally

    15/8-33/20=9/40>0,  Qd^2>0,

and hence exp(-(15/8)Qd^2)<exp(-(33/20)Qd^2).
Together with (7) these prove the required allowance.

This proof uses only inequalities valid at every s in D. L798's (1)
already holds on both closed boundaries of D, for h=0, for either sign
of h and for unbounded u. No maximum at u=3, compactness assumption,
asymptotic onset or sampling argument is used here. The normalization
is valid throughout because Re A>0 fixes the principal square root.
Conjugate parameters therefore have the same real tail expression;
the argument also applies directly without invoking conjugation.

The cited formulas were inspected in the prior step518 assessment
`drafts/literature/2026-11-05-mellin-gaussian-completion-scope.md`.
Their exact hypotheses are reproduced above. The explicit specialization
is needed because those formulas do not state the moving-parameter
2.35/1.65 comparison. No reproof of the imported tail theorem, new
source search or numerical script is needed.

### Independent critical audit, 5 November 2026 — step521

Reused the unchanged SPECIALIZE assessment
`drafts/literature/2026-11-05-mellin-gaussian-completion-audit.md`,
its inspected NIST statements and step518's scoped overlap/failure
comparison. Claim (2) passes. This verifies a source reproduction,
not a result beyond the sources checked or the full Mellin estimate.

**Inputs and branch.** L798 (5) gives
B>4Q-3/2>(15/4)Q because Q>1000>6. Separately Re A>0 puts
theta in (-pi/2,pi/2). Writing A=B exp(i theta) gives the principal
value C=sqrt(2pi/B)exp(-i theta/2) exactly. Thus G and C share
the unit factor a; replacing B by Re A is unnecessary. L798 is the
sole direct notebook input, with L797 supplying geometry through it.
L799 is not used.

**Completion.** For each s in D, u>3 gives d>0 and B>0.
The real positive Gaussian is absolutely integrable. DLMF 7.7.6
applies with alpha=B/2, beta=gamma=0 at y=0 and y=d. Evenness
gives C-G=2a integral_d^infinity exp(-Bv^2/2)dv. This tail is
strictly positive, so taking absolute values and dividing by
|C|=sqrt(2pi/B)>0 gives exactly erfc(t), t=d sqrt(B/2)>0.
There is no complex contour rotation or lost factor two.

**Inequality and threshold.** DLMF 7.8.1–7.8.2 applies at this
positive real t, without a sector or asymptotic restriction.
Since sqrt(t^2+4/pi)>t, its upper bound gives
erfc(t)<sqrt(2/pi)exp(-Bd^2/2)/(d sqrt(B)). With d>0 fixed,
both positive factors B^(-1/2) and exp(-Bd^2/2) decrease in B.
Substituting B>(15/4)Q and d=3/(16u) therefore gives (7) in
the correct direction. The squared prefactor is
2048/(135pi)<2048/405<2209/400, where the last comparison is
819200<894645. All quantities are positive. Independently,
15/8-33/20=9/40>0 and Qd^2>0. The two strict comparisons
give exactly the claimed 47/20 and 33/20 allowance.

**Domain and limits.** L798's strict hypotheses hold on both closed
boundaries of D and their intersections. The argument uses only
u>3 and real positive B,Q,d, so applies directly for h=0 and
either sign of h. Each s has finite parameters; no upper bound on
u, compactness, limiting operation or numerical sample is used.
The existing sole DAG input L798 is complete. No mathematical
script or new literature search was needed. Global theta tails,
continued endpoint, Mellin assembly, quotient/inversion, certificates
and sufficient Xi signs remain open. Retire this passed finite test.

## Mathlib

Full matching coverage is not checked; no absence claim is made.
Supporting Gaussian-integral, complementary-error-function and
real-inequality coverage has not been checked. The proof relies on
the precise NIST formulas above and L798, not on formal verification
or an assumption about Mathlib availability.
