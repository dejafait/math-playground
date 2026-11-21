# Source assessment: the highest prescribed spatial moment with unit residues

TARGET: Test whether L666's full independently displaced family with unit original residues satisfies max_(|u|=1)|c_(M-1)(u)|>=C*n*exp(-n/32)*sqrt(D) for absolute C>0 and all sufficiently large q, using the direct angular rational response of the highest prescribed spatial moment.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 74 completed bounded searches for weighted/pure power sums, rational prescribed-pole norm bounds and positive-residue Blaschke sums; compared the exact L666 family against the primary statements below and the scoped L649/L666/L669/L670/L671 failure records. No theorem or countersequence matching the fixed highest-moment angular/diagonal inequality was identified; no novelty conclusion follows.
SOURCE_EVIDENCE: New reading: Baranov--Zarouf arXiv:1310.1182v1 (4 October 2013), definitions p.1, Theorem 2.4 p.5, Section 4.4 Step 1 pp.12--13 including (4.13)--(4.18); Brunault--Zudilin ISBN 9781108794459, Propositions 1.4--1.5 pp.6--7 all complex-analytic root cases and Lemma 1.6/proof p.8. Reuse Danchenko--Semin v1 Theorem 2 and its complete proof reading, Biro's p.344 theorem, Friedland--Yomdin Theorems 1.1--1.2 and Moitra v4 Theorems 2.2--2.3 from the ready assessments specified below. No new theorem enters the RH argument.
COMPARISON: Spatial endpoint-coefficient transfer is covered by the cited polynomial results. Rational norm comparisons and exact observation control norms of the combined response, not its size relative to the original separate-term diagonal D. Pure-power and exponential-sample bounds have different index and amplitude hypotheses. L669's fixed-angle stop and L670/L671's clearing costs do not decide the direct highest-moment angular maximum; C681c uses different auxiliary weights.
GAP: Prove or refute the exact uniform scale C*n*exp(-n/32)*sqrt(D), retaining the complex radial multiplier (a/R)^(M-1), independent n-dependent displacements and the original D. No signed coercivity, uniform onset, noncancellation estimate or admissible countersequence is supplied by this source review. H/support/realization/Xi signs remain independent.
REASON: Essential theorem comparison is complete for one bounded attempt under EXPLORE; the exact family estimate remains uncovered by the inspected results. The new mechanism is angular compensation for a fixed highest original moment, rather than another pure-sum recovery, scalar c_0 deformation or clearing certificate. This is source coverage for later mathematics, not approval of the inequality or a mathematical advance.
LITERATURE_REASON: The invocation-start target was REVIEW_REQUIRED; the changed fixed-highest-moment scope needed comparison with rational norm estimates and the endpoint spatial transfer. Ready quadrature, power-sum and sampling assessments were reused rather than refreshed.
SCOPE: Exactly TARGET for L666's n=12q+3, M=n/3, x=-5/4, R=11/8, full W_a including j=0 and denominator angle 1/u, all independent |e_m|<=1/8, normalized original D, and the same displacement vector for every u. No fixed-angle substitution, arbitrary auxiliary weights, denominator-clearing shortcut or unproved signed-energy coercivity is covered.

## Preserved step-73 nomination

The following records the nomination before step 74's source review.
Its statements that coverage was missing describe that earlier state.

This is a new target nomination after one completed conceptual audit,
not a second mathematical attempt or same-turn source approval.
The active main gap is actual-Xi all-degree mixed positivity. The
potential downstream use is the spatial root formula: a sufficiently
large highest coefficient could support the required logarithmic H
bound while keeping the full spatial polynomial. Its applicability,
including the possibility that the highest prescribed coefficient
vanishes at some angles, must be reviewed rather than assumed.
H-to-support and actual-Xi realization/sign steps remain independent.

The precise original quantities are already defined in L666:

    c_(M-1)(u)=R^(-1)*sum_(a in Z) W_a(u)*(a/R)^(M-1),
    D=mean_u sum_(a in Z)|W_a(u)|^2/(R^2-|a|^2).

No residue in these definitions is changed. The displayed multiplier
is the existing spatial moment, not a newly assigned quadrature weight.
The needed scale is C*n*exp(-n/32)*sqrt(D), with a single absolute
positive C and uniform onset for all allowed displacement vectors.
Nonzero rationality alone, a finite sample or a bound with a worse
exponential rate would not establish this inequality.

The source review should reuse the exact rational quadrature and root
formula readings, then compare primary results on angular maxima of
weighted power sums/rational responses against these hypotheses and
recorded stops. No broad refresh of unchanged quadrature theory is
needed. Full matching Mathlib coverage is unchecked. L669's fixed-angle
loss is an additional preserved obstruction to replacing the angular
maximum by u=-1. L670/L671 are method limitations, not upper bounds
for the true H or this highest coefficient.

After coverage approval this is a proposed proof_attempt/creative
nomination: the obstruction is uniform signed cancellation of the
highest original spatial moment under independent displacements. Its
radial factor changes both magnitude and phase, so a new mechanism
must control it together with D; the audited blend argument does not.
The bounded test is to establish the displayed scale for the complete
rational response, establish a useful uniform intermediate estimate
with its exact remaining loss, or give a rigorous admissible sequence
whose ratio to that scale tends to zero. An informative negative stops
this highest-moment certificate, not H or RH. Repeating a finite fit,
changing the route name, or merely proving nonvanishing is insufficient.
No mathematical exploration budget is reset by this nomination.

## Completed comparison — step 74, 2 November 2026

### Exact scope and useful consequence

The target and SCOPE above are unchanged. The main RH gap is actual-Xi
all-degree mixed positivity. The intermediate target concerns only the
finite original unit-residue family. It could supply L658's sufficient
H threshold; it would leave the support and actual-Xi bridges open.
No family inequality is proved or numerically tested in this turn.

**Spatial transfer, already known.** F. Brunault and W. Zudilin,
*Many Variations of Mahler Measures*, ISBN 9781108794459,
[publisher excerpt](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf):
Proposition 1.4 p.6 covers all three root-modulus cases, using an
indentation at boundary roots. Proposition 1.5 p.7 retains the actual
leading factor and multiplicities. Lemma 1.6/proof p.8 gives the
degree-index coefficient bound, with binomial factor one at the leading
index. For a slice with c_(M-1) nonzero the degree is M-1; a vanished
coefficient supplies no nonzero leading value. Constants and lower
degrees use the same theorem. No angle attaining the target scale is
guaranteed. These results are imported without reproof.

The downstream comparison is with L658's existing sufficient threshold
H >= (log D)/2-n/32+log n, allowing an absolute additive constant.
L658 (2) retains its 2log n arc-measure cost and 32*pi^2/9 loss.
That is a conditional use of an established local statement, not a proof
of this target or the H-to-support implication. No infinite limiting
interchange or continuity rate in growing degree is being imported.

### Direct rational norms versus the original diagonal

**New rational-norm comparison.** A. Baranov and R. Zarouf,
*A model space approach to some classical inequalities for rational
functions*, [arXiv:1310.1182v1](https://arxiv.org/pdf/1310.1182v1),
4 October 2013, definitions p.1, Theorem 2.4 p.5. For rational f of
degree at most N with no poles in r<=|z|<=1/r, 0<r<1, and
1<=p<s<=infinity, (2.6) states

    ||f||_s <= ((1+r)/(1-r))^(1/p-1/s)
               *[N_1^(1/p-1/s)+(N_2+1)^(1/p-1/s)] ||f||_p,

where N_1,N_2 count inside/outside poles; circle measure is normalized.
Read Section 4.4 Step 1, pp.12--13, (4.13)--(4.18), covering
p=2,s=infinity and both pole sides by representation and kernel
estimates. Earlier representation lemmas were not independently audited;
other cases and extremal examples are not inputs. L666's pole census
is compatible; the spatial multipliers are angular constants. This
compares norms of combined f, without a lower comparison to D. No
reproof or new application bound is claimed.

**Reuse exact angular observation.** The ready assessment
`drafts/literature/2026-11-02-displaced-signed-angular-sampling.md`,
"Exact rational observation", records V. I. Danchenko and L. A. Semin,
*Sharp quadrature formulas and Nikol'skii type inequalities for rational
functions*, [arXiv:1503.06476v1](https://arxiv.org/pdf/1503.06476v1),
22 March 2015, Theorem 2 PDF pp.1--2 and complete proof pp.6--7.
The statement was rechecked here; the saved proof reading is reused.
It requires a finite distinct interior set containing zero, its
circle-reflected completion, ordinary orders <=s and combined
zero/infinity order <=2s-1. At radius and s equal to one its normalized
weights are 1/(2mu). L666 supplies the rational formula and pole census.
Theorem 1's underlying proof retains its unaudited qualification.
It observes the full complex response; it does not erase cross terms
or compare that response to D. Any application to the highest moment
must retain every original multiplier. No such coercivity is imported.

### Power sums and separated samples

Reuse `drafts/literature/2026-11-02-positive-mass-angular-propagation.md`,
"Primary statements and proof scope", for A. Biro,
*An improved estimate in a power sum problem of Turan*, Indag. Math.
11(3) (2000), 343--358,
[unnumbered Theorem p.344](https://users.renyi.hu/~biroand/pdfs/Turan1.pdf).
For N complex nodes with z_1=1 it gives an absolute q_*>1/2 such that
max_(1<=j<=N)|sum_k z_k^j|>q_*; repetitions are allowed. The ready
assessment records the inspected proof portions and qualifications.
This chooses a power from a block with unit amplitudes. The present
target fixes the spatial power M-1 and varies u inside complex W_a(u).
Original residues one do not turn these amplitudes into one. The radial
multiplier cannot be removed. L649's stopped inverse recovery remains
relevant evidence against that shortcut, rather than a counterexample
to this target.

The same ready assessment covers O. Friedland and Y. Yomdin,
[*An observation on the Turan-Nazarov inequality*, v3](https://arxiv.org/pdf/1107.0039v3),
Theorems 1.1--1.2 and complete latter proof, PDF pp.1--5. Those
estimates concern fixed complex exponential sums on a real interval,
with a positive-measure or positive-metric-span observation set. They
propagate an existing norm; they do not compare this rational sum to D.
No exponential representation with an adequate error is assumed.

Reuse the finite-sample comparison in
`drafts/literature/2026-11-02-displaced-signed-angular-sampling.md`:
A. Moitra, [arXiv:1408.1681v4](https://arxiv.org/pdf/1408.1681v4),
Theorems 2.2--2.3 and proof pp.5--7, gives Vandermonde bounds for
separated unit-circle nodes and sufficiently many exponential samples
with fixed complex amplitudes. Those hypotheses cannot be replaced by
vertical pole spacing alone. A transfer of the full rational response,
including its error and diagonal normalization, remains unproved.
The Negreanu--Zuazua indexing qualification stays parked; it is not an
input or an essential missing source for the direct rational test.

### Bounded search, local overlap and nonessential leads

Searches on 2 November 2026 included:

- `"rational functions" "reverse" "Nikol'skii" prescribed poles sum`
- `"power sums" "complex coefficients" Turan lower bound maximum`
- `"rational functions" "positive residues" Blaschke lower bound sum`
- `Turan power sum theorem arbitrary coefficients maximum consecutive powers lower bound pdf`
- `rational functions prescribed poles lower bound norm sum kernels cancellation Nikol skii Danchenko`
- `"Blaschke" "power sums" inequality positive residues`
- `Baranov Zarouf rational functions prescribed poles Nikolskii inequality arxiv`

These located the primary rational-norm paper above and generalized
power-sum comparisons, not an exact-family result. Search snippets,
aggregators and recent pure-power constant proposals were not used as
theorems. No claim of exhaustive coverage or originality follows.

A. J. van der Poorten, *Generalisations of Turan's main theorems on
lower bounds for sums of powers*, Bull. Austral. Math. Soc. 2 (1970),
15--37, [publisher PDF](https://doi.org/10.1017/S0004972700041575):
screened the introduction and Theorem 2 discussion pp.15--19. Its
quantitative displayed formulas were not reliably available in text
extraction; the screenshot interface supplied no readable image, and
direct download failed DNS resolution. No quantitative theorem or proof
from it is imported. This optional generalized-power-sum lead is parked;
the ready Biro/propagation comparisons suffice to distinguish those
models from the unchanged direct rational target. It is not an essential
source blocker or a reason to repeat access attempts next turn.

The local reads were confined to L666 definitions/source/pole/bridge
sections, L664's cited inputs, L669's audited conclusions and source
scope, L670/L671 hypotheses, conclusions and relevant source/transfer
sections, and L658's statement. The nomination's scoped duplicate
search was supplemented by highest/leading spatial searches in local
assessments, ATTEMPTS and the 2 November histories. No duplicate direct
highest-moment angular theorem was identified. This is a bounded local
comparison, not an audit of all those results.

Preserve these distinctions:

- L669 excludes a uniform logarithmic loss at u=-1; it does not settle
  this full-circle linear-rate inequality.
- L670 bounds exposed coefficients of a particular complete clearing;
  its endpoint-support assertion also retains its generic-vector caveat.
  L671 stops a degree-index certificate for the bottom spatial face.
  Neither upper-bounds this rational angular maximum.
- L666's c_0 sampling/deformation continuation remains parked after two
  inconclusive attempts. The current target uses the highest prescribed
  original spatial multiplier. Repeating its c_0 energy derivative,
  positivity of observation weights or finite fits is not a new test.
- C681c stops the unchanged convex blend of two auxiliary positive
  constructions, without deciding arbitrary weights or original H.

### Gate, continuation and limitations

EXPLORE covers one bounded mathematical attempt at exactly TARGET,
after the supervisor's separate approval of this updated assessment.
The discriminating test is the stated uniform bound (or a useful
rigorous intermediate bound with its exact remaining loss), or an
admissible sequence whose ratio to the required scale tends to zero.
An informative negative retires this highest-moment certificate only.
Nonvanishing, isolated angles, sampled maxima, finite fits and a bound
with an unpaid worse exponential rate do not pass.

Essential continuation inputs are L666's full W,c_k,D definitions and
its rational pole census, with L658 for the conditional downstream
threshold and the cited spatial endpoint formula. L669/L670/L671 and
the recorded L649/L666 stops are comparisons. Signed noncancellation,
radial-factor cost, n-uniform constants/onset and degree-drop handling
remain obligations; no ready scalar energy bound is assumed. H/support
and actual-Xi realization/signs remain independent unresolved steps.

Mathlib: reuse the inspected coverage in
`drafts/literature/2026-11-02-localized-logarithmic-joint-moment.md`:
[MahlerMeasure documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html)
includes `Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`
and `Polynomial.norm_coeff_le_choose_mul_mahlerMeasure` as supporting
results. Totalized real logarithms do not remove the analytic nonzero
condition. Full matching coverage for the present rational highest-
moment/diagonal target and the rational-norm theorem is unchecked.
No Mathlib absence claim, new lemma or mathematical script is made.
