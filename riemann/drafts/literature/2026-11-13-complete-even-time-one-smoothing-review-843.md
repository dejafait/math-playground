# Complete even time-one smoothing — comparison843 completed844

TARGET: Assess whether L515's signed-measure time-one smoothing theorem applies to C759a's complete even operator with both poles and all five masked prime shifts, yielding an explicit L2-to-L-infinity bound for its semigroup.
CHECKED: 2026-11-13
DECISION: IMPORT
SEARCH_EVIDENCE: Queries "signed convolution" "Dyson" semigroup smoothing finite measure; "localized Weil" "semigroup" poles; "geometric stable" "killed" "1107.0745". The exact full-source overlap is paper67 v1, not a novel regularity target. Read its operator hypotheses and essential time-one proof case, and narrowly compare L515, C759a/k, L741(13),(16), C759i/j and stop843; irrelevant search hits were not used.
SOURCE_EVIDENCE: Read bramble_trace, Boundary traces and support variation for localized Weil operators, paper67 v1 (27 October2026), Section2 (2.1),(2.8), Section3.1 (3.1)-(3.6) and Section3.2 (3.7)-(3.8), https://rstation.ai/problems/riemann_hypothesis/papers/67; reread GR arXiv:1107.0745v1 Section2 (2.1)-(2.4) and following killed formulas, https://arxiv.org/html/1107.0745v1. Reuse the primary Engel-Nagel/FOT coverage and full stronger-norm proof recorded in L515 and drafts/literature/2026-10-30-weil-eigenfunction-boundedness-coverage.md; fresh Engel-Nagel retrieval timed out, without creating an essential coverage gap.
COMPARISON: Paper67 already states exactly full-Weil time-one smoothing, explicitly retaining the finitely truncated two-pole difference kernel and every overlapping prime-power atom. Its source operator and Fourier convention match C759a's displayed form. C759k supplies the audited local reference/domain identification; L515 supplies the audited signed-measure stronger-norm argument. Only local applicability and recording of this known bound remain, not an uncovered general smoothing theorem.
GAP: No essential source coverage is missing. A later mathematical import must check the exact finite-measure representation, both pole signs, five zero-extension masks, common form/operator domain and parity restriction, then record the source bound with its total-variation constant. This literature step establishes coverage, not that local application.
REASON: The precise full-source overlap removes the prior identification exclusion as a literature blocker. Import with the necessary applicability checks instead of reproving general semigroup theory; boundedness may later discharge C759l's bounded-forcing premise, while sign, isolation, parity and Xi transfer remain independent.
SCOPE: I=(-1,1), C759a's complete unneutralized form, C759k's G and K, real even L2 data, semigroup at time1 only. Retain all prime masks and both original poles. No trace, isolation, parity or Xi conclusion.
COVERED_TARGET: Verify and record the known time-one smoothing bound for C759a's complete even operator using paper67 v1 (3.4)-(3.8), L515 and C759k, retaining both poles and all five masked shifts.
LITERATURE_REASON: The target changes from a boundary estimate for already bounded forcing to smoothing on arbitrary L2 data; L515's existing assessment explicitly excludes full-Weil identification.

The following nomination843 is preserved as the pre-review scope;
the completed comparison844 below supersedes its pending-source language.

## Recovery comparison: three distinct continuations

1. Refining C759l's coefficient or repeating its approval has no
   specified application threshold. Audit843 accepts the existing finite
   constant. Close the approval sequence; the bound itself has not failed.
2. Direct positive-ground-state enclosure or rank-one secular isolation
   still needs controlled complementary spectrum and signed background
   information. Stops829/822 and assessment838 retain these gaps.
   C759l provides neither; another generic inverse identity is insufficient.
3. Complete-operator time-one smoothing tests independent eigenfunction
   boundedness. L515 supplies the known signed-measure method; C759k
   supplies an audited full operator and its two-pole kernel before
   parity restriction. Assess their exact compatibility without sign,
   isolation or an unrestricted residual embedding.

Select3. This nomination is neither a second mathematical attempt in843
nor approval of the specialization. The audited full operator is the
new input compared with the earlier combined enclosure stop829.

## Exact bounded test

Reuse L515's time-one theorem and factorial majorant in the stronger
operator norm. Examine the difference-kernel representation of both
poles before even restriction. Any proposed convolution measure must
be finite on the whole line and reproduce the action on I exactly;
specify its extension outside I-I rather than using a nonintegrable
global cosh kernel. Retain both signs, all five atoms and the masks.
Use C759k to check the common closed form and operator domain, not
only a formal multiplier or finite matrix.

Success would identify an explicit finite M_complete and valid
specialization of L515 for exp(-A_e) at time1 on compatible classes.
Its later eigenfunction use would include every vector in every
eigenspace. Failure means a lost pole/mask, nonfinite measure, domain
mismatch or unpaid stronger-norm passage; preserve it and stop this
fixed test without sweeping shifts or times. No result is asserted here.

First reuse the primary coverage; retrieve more only for a specific
missing hypothesis. L2-bounded perturbation alone does not imply
smoothing. Do not assume compressed commutation, small-time smoothing
or positivity of the complete semigroup. C759j's full-domain residual
obstruction and C759i's all-times order obstruction retain their scopes.
L515's theorem is the closest duplicate; approve only the necessary
full-operator applicability work if its scope is adequate.

Full matching Mathlib coverage is unchecked. No cross-notebook input
is used. Positive trial margin, full isolation, parity and actual-Xi
mixed positivity remain open. A justified creative main-gap target is
still blocked by the absence of a concrete signed arithmetic/Xi transfer;
this known-method regularity check is not labeled creative for scheduling.

## Completed source comparison844

### Exact inspected overlap

[bramble_trace, *Boundary traces and support variation for localized
Weil operators*, paper67 v1, 27 October2026](https://rstation.ai/problems/riemann_hypothesis/papers/67),
Section3.1, (3.4)-(3.6), fixes a support-radius upper bound A and uses

\[
 \mu_A=\nu_r+\sum_{\log n\le2A}\frac{\Lambda(n)}{\sqrt n}
 (\delta_{\log n}+\delta_{-\log n})
 -2\cosh(t/2)\mathbf1_{|t|\le2A}\,dt,
\]
\[
 c=\log(2\pi),\qquad
 M_A=\gamma+\frac\pi2+2\log2
       +2\sum_{\log n\le2A}\frac{\Lambda(n)}{\sqrt n}+8\sinh A.
\]

The source's \(\nu_r\) is the even density extension of
\(e^{-t/2}/(1-e^{-2t})-e^{-t}/(2t)\), for t>0.
Its (3.5) identifies the compressed full Weil operator with the
killed reference minus c and this measure; (3.6) bounds its variation
by M_A. The cutoff retains the pole on all interval differences.
Section3.2, (3.7)-(3.8), states

\[
 \|e^{-A_a}\|_{2\to\infty}\le e^{c+M_A}/\sqrt2,\qquad
 \|u\|_\infty\le e^{\lambda+c+M_A}\|u\|_2/\sqrt2.
\]

The hypotheses are fixed 0<a<=A, the zero-extension logarithmic
closed form (2.1), its Friedrichs realization, and a finite real even
signed measure. There is no positivity or simplicity requirement.
The essential proof case uses killed-kernel domination, variation
measures, whole-line convolution and the factorial Dyson bound.
These are existing source statements; no local specialization is
proved in this literature turn. Later source sections are outside
this review and are not imported.

### Applicability obligations for the known-result import

C759a(1),(5)-(6), Proof1 and C759k Proof1,5 already supply the local
complete form, its smooth-core closure and the killed-reference
normalization. Compare those statements with the source at a=A=1.
The source uses the same Fourier convention and scalar log(2pi).
Do not confuse its one-sided r with L741's one-sided r: L741(13)
has the displayed factor2, while C759k uses rho(x)=r(|x|)/2.
The later import must state its chosen measure explicitly, rather
than silently identifying symbols across the two conventions.

Use the source's finite pole extension before even restriction.
A global uncut cosh density is outside L515's hypotheses. Check
that compression agrees with C759k's two-pole kernel and then with
its even P, including the opposite sign of the measure contribution
and the positive sign of P in A_e. Retain all n=2,3,4,5,7 atom
pairs and their zero-extension masks, rather than replacing them
by unmasked or periodic shifts. C759k(5)-(6) and Proof5 give the
common form/operator-domain and parity statements to use in checking
this application. No new realization theorem is required.

L515 already contains the full arbitrary-finite-measure proof and
its separate audit. Its Conclusion(1)-(3), Dyson(7)-(9), and
stronger-norm(10) cover the required convergence topology. Cite them;
do not infer L2-to-L-infinity convergence from bare L2 bounded
perturbation, assume compressed commutation, or require a C0
semigroup on L-infinity. The source's M_A is a total-variation
majorant; C759k's operator-norm budget24 cannot simply replace it
in L515. The explicit symbolic source constant suffices; a numerical
optimization is not part of the approved target.

The prior assessment's primary Engel-Nagel coverage (2000,
III.1.3 p158; III.1.9-1.10 pp162-163) and FOT coverage (second
revised edition, Theorems4.4.2-4.4.3 pp173-175) remain applicable
and are reused, not presented as freshly retrieved. The present
Engel-Nagel URL timed out. That is not a persistent essential source
blocker because the same theorem and application were already read
and audited in L515. The fresh GR Section2 inspection confirms
the half-speed normalization and killing after whole-line
subordination. No different process realization is being imported.

### Failure screen, decision and continuation

C759i Conclusion(3) obstructs all-times preservation of the positive
cone; it does not obstruct an unsigned norm bound at time1.
C759j Conclusion(1)-(2) obstructs unrestricted residual L2-to-supremum
control for arbitrary domain vectors; the proposed import concerns
the exponential semigroup and then genuine eigenvectors. Neither
stop is reopened or weakened. Stop843 closes the completed boundary
approval sequence; this independent regularity prerequisite does not
repeat its constant audit.

Decision IMPORT covers only the exact follow-on COVERED_TARGET above,
as KNOWN_IMPORTED. A later entry must verify the full measure and
domain identification and record the explicit source bound; it may
give only the necessary applicability argument. No new general
smoothing theorem or reproof is justified. Success requires a finite
variation measure, every pole/mask, equality of the closed realizations
and an applicable stronger-norm conclusion. A failure of one of those
checks stops this test and preserves the boundedness premise.

This is a useful source-overlap finding, not a new mathematical
regularity result. No lemmas, scripts, DAG or PROOF were changed.
Full matching Mathlib coverage remains unchecked; supporting named
theorems are recorded in L515 and C759k, with no claim of formal
verification. The source gap is closed for the stated import only.
Positive trial margin, lowest-even isolation/sign/simplicity, parity
comparison and actual-Xi all-degree mixed positivity remain unresolved.
