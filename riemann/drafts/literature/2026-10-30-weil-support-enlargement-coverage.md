# Compact-window Weil positivity: completed source comparison

TARGET: Assess quantitative compact-window Weil positivity and support-enlargement criteria for controlling a single newly entering prime term without assuming positivity on the enlarged window.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact-title Yoshida/Bombieri searches and compact-window/support-enlargement queries led to Zhu v2, Liu's 14 September manuscript and bramble_trace papers 60/67 v1; endpoint-trace/renewal/zero queries identify paper 67's explicitly unresolved arithmetic condition. Narrow local searches in drafts/literature and ATTEMPTS found no ready endpoint-trace assessment; the earlier rank-trace stop remains distinct. No novelty claim follows from these searches.
SOURCE_EVIDENCE: Read Bombieri (2000) Theorems 2/3/5/12 and relevant support/continuity proof passages; Zhu arXiv:2608.24827v2 Theorem 1.1 and relevant envelope, full-complement, parity and retraction passages in Sections 3–7; Liu, 14 September 2026, relevant normalization/certificate passages in Sections 2–4 and the complete Obstruction/Certification Theorems and proofs in Sections 5–6; bramble_trace paper 60 v1 Theorem 1.1 and full-complement conditions in Sections 2/6–8; paper 67 v1 Theorems 2.1/2.2/2.4 and relevant domain, renewal, collar, complementary-elimination and continuation passages in Sections 3–9. Yoshida's original chapter remains unread; supplementary numerical certificates and original renewal/boundary-regularity sources were not independently audited.
COMPARISON: Known results give full-window lower certificates, exact Schur criteria and a simple-branch signed activation asymptotic without assuming enlarged-window positivity. They do not give a uniform finite step near a first zero: paper 67 Section 9 explicitly lacks a trace bound vanishing with the ground eigenvalue, and Liu excludes a specified tail-dropping localization already at the eight threshold.
GAP: Separate the known local activation law from its independent input audits and from the missing arithmetic estimate controlling low-eigenvalue inverse response. The activation remainder is fixed-cluster, not effective or uniform as the eigenvalue/gap varies; multiple-branch matching is not supplied by Theorem 2.4.
REASON: Park automatic support propagation and tail-dropping/compact-repair implementations. A conditional audit of the actual one-atom law is now a concrete mathematical continuation; no original cancellation mechanism is yet justified. Fixed-window positivity, local extension and all-support positivity must remain distinct.
LITERATURE_REASON: At invocation the exact operator and finite-to-infinite hypotheses were essential unread coverage; this comparison closes that source-scope question and identifies a reusable conditional audit target.

## Completed comparison (2026-10-30)

The main gap is actual-Xi all-degree positivity. The intermediate target
was a full-function-space continuation criterion, including one new
prime and all complementary modes. Its plausible use is to locate the
arithmetic estimate needed for support propagation. It supplies no
all-support theorem or all-height Laguerre signs.

### Classical range and conventions

In [Bombieri, *Remarks on Weil's quadratic functional in the theory of
prime numbers, I*, Rend. Mat. Acc. Lincei (9) 11 (2000), 183–233](https://www.bdim.eu/item?fmt=pdf&id=RLIN_2000_9_11_3_183_0),
Theorem 3 (pp. 197–199) gives attainment of the L2 minimum; Theorem 5
(pp. 199–200) gives continuity and decrease of the two parity minima.
Section 12, Theorem 12 (pp. 225–227), concerns a test supported on an
interval of **length** b<log 2. Its lower estimate is
log(1/b)-log^+log(1/b)-O(1), times the squared norm. Its proof removes
the prime sum because the autocorrelation has radius at most b.
This asymptotic bound alone gives positivity only for sufficiently
small b, not an effective constant at the whole endpoint. The Paperzz
transcription, document 7088948, was used for the theorem/proof
passages when BDIM timed out; retain
complex conjugation and the off-line complex ordinates despite OCR.

Yoshida, ASPM 21 (1992), 281–325, DOI
[10.2969/aspm/02110281](https://doi.org/10.2969/aspm/02110281), remains
an unread original. Liu's source identifies Lemmas 2/3 at pp. 289/290
and the finite-to-infinite computation at pp. 309–310. Those pointers
and Suzuki (2023) Sections 4.2/5.4 are reports, not inspection of
Yoshida's proof. No Yoshida-specific constant is an input below.

### Quantitative certificates and a recorded failure

[Zhu, arXiv:2608.24827v2](https://arxiv.org/html/2608.24827v2),
2 September 2026, equations (2)–(4), Theorem 1.1 and Section 4,
uses tests of radius L and autocorrelations of radius 2L. The space
is first real even; Section 6 treats the negative odd pole and complex
tests. The closed form uses the logarithmically weighted Fourier
domain, rather than assuming its value is finite for every L2 vector.
For A_L=sum_{log n<2L}2 Lambda(n)/sqrt(n), the split requires
beta=log(Tsharp/(2pi))-1/Tsharp-A_L>0. Its full-space margin is
min(lambda_head,beta-epsilon_D)-epsilon_B; positive finite spectra
alone are insufficient. Theorem 1.2/Corollary 6.3 report 8.9e-18 at
L=.8. Section 17 makes the supplementary matrices, quadrature and
residual checks part of that proof; they were not replayed here.
Section 7 retracts the L=1.19 certificate: a lower prime-comb bound
had been used where an upper bound was needed. The reported
Landau–Widom fit is not a lower-bound propagation theorem.

[Liu, *Certified Weil Positivity Beyond the Unit Window*, manuscript
14 September 2026](https://www.alphaxiv.org/abs/2609.weil-positivity-riemann-zeta-bounds.pdf),
Sections 2–6, treats complex smooth tests on (-L,L). Theorems A/B
report lower constants 2^-151 at L=1 and 2^-49162 at L=17/16.
Section 6, equations (17)–(22), requires a bounded positive reference
mI<=M<=bI, m>0, a finite isometry E, and separate cross/complement
errors with n<m before using any inverse. Its sufficient finite
inequality pays both errors; no desired target positivity is an input.
The Section 5 Obstruction Theorem, including its modulated two-bump
proof, shows the specified tail-dropping comparison has limiting
normalized value 1/16-log(2)/(2sqrt(2))<-1/8 when L>log(8)/2.
Fixed compact corrections cannot repair it. This is not a negative
Weil test: the retained positive tail may compensate it.

[bramble_trace, paper 60 v1](https://rstation.ai/problems/riemann_hypothesis/papers/60/v1),
26 October 2026, Theorem 1.1, reports strict positivity for all
0<a<=2. Sections 2 and 6–8 retain the signed pole, all active prime
powers, the whole response family and both Schur complements.
The distant covariance bound is below .145; the intermediate finite
margin is .20 minus less than 2.311e-5, giving a Schur gap >1/20.
These are source certificate conditions, not a locally certified
lower constant for the full operator. Its large numerical supplement
was not replayed. Reproducing any of these fixed endpoints is known
work, not a new mechanism or a proof of RH.

### The exact one-prime law and its limit

[bramble_trace, paper 67 v1](https://rstation.ai/problems/riemann_hypothesis/papers/67/v1),
27 October 2026, Theorem 2.4 and Section 8, gives the following
source claim. For n a prime power, a=log(n)/2, w=Lambda(n)/sqrt(n),
and a normalized simple eigenfunction u of the complete A_a with
parity p=+1 or -1, compare the branches on radius a+delta/2 with
and without just that activating atom pair. Then

    lambda_full(delta)-lambda_deleted(delta)
      = -2 w p |tau_+(u)|^2 delta/log(1/delta)
        + o(delta/log(1/delta)).

Neither eigenvalue positivity nor enlarged-window positivity is
assumed; the error is for a fixed old interval and isolated simple
eigenvalue. There is no multiple-cluster version of this finer law.
The domain is zero extension with finite logarithmic Fourier energy;
the traces are limits sqrt(log(1/t))u(+-a-+t). Sections 3.3/4 supply
the renewal normalization and strong (not norm) collar inverse limit.
Sections 5/8 eliminate the complete spectral complement; compactness
in (8.3), not a finite spectrum or just a scalar gap bound, is needed
at the smaller activation scale. These proof cases were read; their
independent verification is the nominated next audit, not a result of
this literature turn.

Section 9, (9.1)–(9.4), gives the actual collar Schur criterion when
the **old** operator is positive, retaining inverse-weighted low
traces and a high-spectrum bound. It permits a sufficiently small
step for each fixed positive old operator. It gives no uniform step
near a possible finite first zero. Its stated missing bound (9.5),
or an Osgood replacement, is not proved. Section 9 also supplies a
scalar-shifted pure-log operator whose eigenvalue crosses zero;
regularity and the support law alone cannot supply the arithmetic
bound. No new obstruction is derived here.

### Gate result and continuation test

The saved target is partially covered: an exact one-term asymptotic
and full-complement criteria exist, but an effective uniform crossing
estimate remains missing. Park automatic iteration and the specified
tail-dropping repair, preserving their source evidence. Audit the
conditional activation comparison before using it in new mathematics.
Continue only if it controls all complementary modes at little-o of
delta/log(1/delta); stop or repair the import if it needs mere O of
that scale, an unproved branch matching, or a finite-mode substitute.
This is source progress, not new mathematics beyond the sources.

Local L471 equation (6) and L511 remain contrasts only; no further
local proof was needed or read. No cross-notebook result is used.
Full matching Mathlib coverage is unchecked. Unread original renewal
and boundary sources remain independent obligations for a complete
audit of the entire source theorem.

## Initial nomination (historical; superseded by comparison above)

Main gap: actual-Xi all-degree mixed positivity. The intermediate target
is a rigorous one-window positivity continuation test, including the
new prime contribution and the full infinite-dimensional remainder.
If available, it could identify a concrete arithmetic operator estimate
for a later bounded proof attempt. Iteration to arbitrary support,
uniformity, conversion to all-height signs and RH remain unresolved.
No such criterion is derived or assumed in this nomination.

Read primary statements first:

- H. Yoshida, *On Hermitian forms attached to zeta functions*, in
  *Zeta Functions in Geometry*, Adv. Stud. Pure Math. 21 (1992),
  pp. 281–325; resolve its exact theorem numbers and test-space scope.
- E. Bombieri, [*Remarks on Weil's quadratic functional in the theory
  of prime numbers, I*](https://www.bdim.eu/item?id=RLIN_2000_9_11_3_183_0),
  11 (2000), pp. 183–233; compare the precise small-support and
  finite-reduction statements before extracting larger passages.
- [arXiv:2608.24827](https://arxiv.org/abs/2608.24827),
  *Weil positivity in compact windows: certified two-sided bounds and
  a Landau–Widom decay law*: check version, exact theorem and
  certificate hypotheses; the search-result abstract is not coverage.

Local inputs are L471 equation (6) only as the signed-identity contrast
and L511 only as the finite-allocation contrast. Neither proves Weil
coercivity or supplies a norm bound for a new prime operator. The
completed source-scope stop is in
[the rank-trace comparison](2026-10-30-weil-rank-trace-single-pair-coverage.md).
Name any further exact local claim before its narrow read. No
cross-notebook result is nominated; matching Mathlib coverage is unchecked.

Continuation/abandonment test: continue toward a proof target only if
the inspected primary results specify a genuine lower bound in a
stated function space and a controlled remainder/cost across a specified
prime-support threshold. Import a covered criterion with precise
citation; do not reprove it as new mathematics. Park the proposed
implementation if it needs all-window positivity, an uncontrolled
infinite tail or finite numerical spectra alone. A missing accessible
essential theorem is SOURCE_BLOCKED, not permission to derive one.
This nomination does not approve a creative attempt; any uncovered
mathematics needs a separate assessment/approval turn.
