# Fixed smooth witness for the complete good-frequency screen — continuation861

TARGET: Test whether L750's fixed smooth witness with T=4log(3) rejects c_E>M/(M+1) for the complete neutral symbol, using certified sublevel-set mass and exact moments.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Separate review861 completed nomination860's effective-source comparison; reuse its exact searches, single-band concentration comparison and scoped failure checks. This is its selected witness subtarget, not another generic search or a claimed novel theorem.
SOURCE_EVIDENCE: Direct primary URLs: https://arxiv.org/html/1802.07942v1 Section2 steps2-4; https://dlmf.nist.gov/3.5.E7 and https://dlmf.nist.gov/3.5.E8; https://dlmf.nist.gov/5.7.E6; https://dlmf.nist.gov/5.5.E2; https://dlmf.nist.gov/5.11.E2 and https://dlmf.nist.gov/5.11#ii. Rechecked862 as detailed below; reuse review860 completed861 for https://arxiv.org/html/2006.00427v2 Section2.2/Theorem3/Corollary3/Section6 and Johansson Section3.2. Local inputs L744(6)-(8), L750(2)/(4), Proof Sections1/3; Plancherel and integral monotonicity. No numerical certificate imported.
COMPARISON: The witness, exact moment cancellation and validated integral methods are known. Changing T and certifying this unweighted mass ratio is local specialization; no weighted sign theorem or concentration improvement is supplied by the sources.
GAP: Establish changed-length applicability, enclose a nonzero norm and moment ratio, certify complete-symbol sublevel boxes, and compare the upper good-mass ratio to a lower threshold. No value or outcome known.
REASON: Source-only recovery862 supplies missing direct primary URLs and checks the saved scope without changing the target. SPECIALIZE remains ready for one RESEARCH/REPRODUCTION calculation; no mathematics executed in either literature turn.
SCOPE: Only the fixed witness below, I=(0,4log3), E={w>=1}, complete finite prime sum, two exact moments and a finite certified subset of E-complement. No witness/basis/window/threshold sweep, eigenvalue optimization or Q-sign claim.

## Fixed data and applicability checks

Use nomination860's unchanged w,E,M,c_E and complex admissible class.
Put T=4log3, delta=T/40. Apply L750's same formulas:

    eta(s)=exp(-1/s) for s>0, and 0 otherwise,
    theta(s)=eta(s)/(eta(s)+eta(1-s)),
    chi(x)=theta((x-delta)/delta)*theta((T-delta-x)/delta),
    phi_k(x)=chi(x)*sin(k*pi*x/T), k=1,3,
    a= integral exp(x/2)phi_3(x)dx
       / integral exp(x/2)phi_1(x)dx,
    f=phi_3-a*phi_1.

This is a proposed specialization of L750's existing recipe; its old
T=8log3 certificate is inapplicable. Prove f is smooth, supported
strictly in I, nonzero, and has both exponential moments exactly zero.
The positive denominator and symmetry relation require verification
at the new T; an approximate nullspace is not neutrality. Define a by
exact integrals, with intervals enclosing it. A real witness suffices
for an upper bound on an infimum over complex tests. Reuse L750's
scalar derivative bounds with correct scale factors, not its old
moment, norm, quadrature error or sign values.

Essential input IDs: L744 for the complete smooth form and scalar
remainder; L750 for the witness construction and derivative controls.
L741 supplies normalization context only. L752,C998z,C998 are contrasts,
not sign premises. Matching Mathlib coverage is not checked. No RH,
complement positivity, H2-prime tail, Xi realization or cross-notebook
input is assumed.

## One bounded rejection test

Interval subdivision on [-16,16] may select a finite disjoint union J
of rational boxes with certified sup_J w<1. Samples may propose boxes
but cannot certify their signs. Retain all prime powers 2<=n<81 and
exact von Mangoldt weights; retain all endpoint and special-function
errors. No claim about unselected boxes is needed for this one-sided
mass bound. This is not a frequency truncation of the form.

Enclose N=||f||_2^2 with 0<N_lower<=N<=N_upper. Plancherel retains the
whole Fourier mass exactly. Enclose from below by b>=0 the quantity

    B_J = integral_J |F_f(t)|^2 dt/(2*pi),

including inner Fourier integration, exact-a enclosures and outer
integration errors. Justify p_E(f)<=U=1-b/N_upper. Enclose complete
w(0) to obtain m0>=0 with m0<=-w(0)<=M; positive m0 is sought, not
assumed. Test

    U <= m0/(m0+1).

These are standard set-inclusion, Plancherel and monotone-integral
comparisons recorded in completed861, not numerical inequalities
established here. The required threshold remains M/(M+1). Do not
substitute an upper bound for M in the rejection direction. Verify M
finite using L744(8) and the finite sum; no global minimizer or full
E decomposition needs computing.

Composite Simpson requires real C4 integrands, even subinterval count
and the full fourth-derivative bound; interval-box integration is also
allowed. Johansson's Gaussian branch requires analyticity on the whole
complex ellipse. Flat cutoff joins are not analytic there: use valid
real boxes or smooth-rule remainders. All norm, coefficient, Fourier,
digamma and rounding errors enter the certificate. Save full bounds
and failures on disk; a grid or preview is not evidence. No infinite
frequency tail is discarded: spatial Plancherel supplies total mass
and only positive bad mass is retained.

A certified comparison rejects the strict c_E screen, not Q positivity
or RH. If this f supplies insufficient certified bad mass, bounds
overlap, neutrality fails or integration remains unresolved, stop the
single test as inconclusive with its evidence. Do not infer the screen
holds or silently tune another witness. Improved weighted observation
would require separate coverage.

Plausible use: screen a coarse signed-payment mechanism before investing
in global observation. Non-neutral poles, arbitrary windows, assembly
and actual-Xi all-degree mixed positivity remain independent gaps.

After separate approval: calculation/standard/high, REPRODUCTION.
This is reliable scalar integration for one existing construction,
not a creative mechanism.

## Source-link recovery862 — 13 November 2026

LITERATURE_REASON: Supervisor recovery reported missing direct source URLs
in this ready continuation. Repair that defect with primary passages;
reuse the completed861 theorem comparison rather than repeat discovery.
The exact TARGET, witness, rejection direction and scope are unchanged.
This is a process repair (STALLED), not a new mathematical advance.

Primary sources opened directly this turn:

- Johansson, *Numerical integration in arbitrary-precision ball arithmetic*,
  [arXiv:1802.07942v1](https://arxiv.org/html/1802.07942v1),
  22 February 2018, Section 2, callback contract and steps 2–4;
  Section 2.1 tolerance qualifications. Direct boxes require valid
  integrand enclosures. The Gaussian branch requires analyticity and a
  magnitude bound throughout its ellipse. Requested tolerance alone
  does not certify accuracy; inspect the returned radius. This supports
  the existing method choice, with no enclosure for this witness imported.
- NIST DLMF v1.2.8, release 15 September 2026,
  [3.5(ii), equations 7–8](https://dlmf.nist.gov/3.5#ii):
  composite Simpson requires C4 regularity and even n; error bound is
  (b-a)h^4 sup|g^(4)|/180. No new derivative bound is established here.
- Same DLMF release, [5.7.6](https://dlmf.nist.gov/5.7.E6):
  partial fractions exclude nonpositive integer poles;
  [5.5.2](https://dlmf.nist.gov/5.5.E2) supplies recurrence.
  [5.11(ii)](https://dlmf.nist.gov/5.11#ii) supplies the
  complex remainder qualification for [5.11.2](https://dlmf.nist.gov/5.11.E2),
  with the secant factor retained. Reuse L744's right-half-plane
  specialization; a truncated asymptotic series alone is insufficient.

Reused, rather than newly re-read: Karnik–Romberg–Davenport,
[arXiv:2006.00427v2](https://arxiv.org/html/2006.00427v2),
28 September 2020, Section 2.2, Theorem 3, Corollary 3 and Section 6,
as inspected in completed861. Its single-band comparison remains
insufficient for the two-moment multi-component level set. It is a
scope comparison, not an essential numerical input to this witness.
Johansson Section 3.2 remains reused for manual tails; the nominated
one-sided test uses spatial Plancherel instead of discarding a Fourier tail.

Local checks used only review860's definitions, scope comparisons and
recorded failures, L744's complete smooth form, and L750's exact recipe
and reflection argument. The old T=8log3 numerical certificate remains
inapplicable. Changed-length neutrality, norm, Fourier integrals and
all rounding/remainder bounds remain calculation obligations, not
results of this approval. Full matching Mathlib coverage is not checked.
No lemma, mathematical script, PROOF or DAG change is required.
