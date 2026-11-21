# Fixed U12 retained-zero subset — nomination879

TARGET: Test whether the ten published Arb 2.23.0 zero-isolating intervals below height 50 suffice for a fixed-U12 Gram lower bound exceeding C750d's epsilon_* plus all finite-input errors, using only a retained zero subset.
CHECKED: 2026-11-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review880 reused completed comparison876 and searched exact local neutral-subset/low-zero/Gram failures; inspected C750c Proof1/5, C750a integration cases, L753 hypotheses/conclusion and L018. Targeted web queries for finite Weil Gram certificates and Johansson integration supplied no inspected matching fixed-U12 margin theorem; new uninspected leads are excluded below.
SOURCE_EVIDENCE: Read Arb2.23.0 examples real_roots ten endpoints and unresolved count; arb_calc isolation contract; pinned real_roots.c callback/dispatch/flags; isolate_roots.c sign/derivative and verbose-print cases; arb_calc.h interval printer; arf decimal faithful-rounding contract. Rechecked Platt--Trudgian2004.09765v1 Theorem1/Section2, Johansson1802.07942v1 Section2 callback/direct-box cases and DLMF25.2.3/25.10.1 for real-height/Hardy-Z specialization. Exact links and limits below.
COMPARISON: Known identity, verified-height theorem, published root intervals and validated integration permit a bounded finite-subset test in the existing coordinates; no inspected source supplies its positive lower margin or conditioning. The printed endpoints need outward transport rounding, and all uncertain moments/projections must remain enclosed. This is known-method specialization, not a new positivity theorem.
GAP: No Fourier sample enclosure, retained Gram lower bound, finite-input error norm or sufficient margin has been computed. Omitted-zero sign and endpoint applicability must be written in the future certificate using the inspected height theorem and L753; C750d pays only |height|>H. Interval widths may defeat the test, but source inspection alone has not established that failure.
REASON: Literature-only review880 resolves missing source/input scope and permits exactly one fixed-data conditioning calculation. Reuse the audited tail without reproof; no lemma, numerical margin, mathematical script, new inequality or source-level novelty is produced here. New readiness receives separate supervisor approval.
SCOPE: Only the saved TARGET, C750c(15)'s ten exact complex coordinates, C750a's fixed cutoff/T=4log3, the ten printed intervals with outward endpoint-transport error, H=3000000000000 and audited C750d epsilon_*; one bounded evaluator, no root refinement, data replacement, mode/window change or precision sweep.

LITERATURE_REASON: The next target changes from auditing the unconditional
high tail to certifying a retained finite subset. Assessment875 did not
inspect exact endpoint values or establish their margin/error adequacy.
Reuse its covered identity and zero-count inputs; inspect only missing
finite-subset hypotheses and input cases before any new calculation.

The following is the preserved nomination879, superseded for source status
by completed review880 below. It was not a mathematical attempt. No result
about the retained subset is derived in879. The gate remains
REVIEW_REQUIRED; next invocation is literature-only. In particular, the
already audited tail must not be audited again as a substitute for this
missing comparison. No new lemma or mathematical script belongs to the
source-review turn.

Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity. A positive
fixed-U12 compression could help a later exact Schur/infinite-complement
analysis, but supplies neither that complement nor non-neutral signs or
global assembly. This finite certificate is a standard-method diagnostic,
not a nominated creative mechanism at the central gap.

Essential inputs are C750c Proof1/5's ten exact coordinates, C750a's
cutoff, L753's neutral time-zero identity, L018's zero conventions and
C750d's audited coefficient-space epsilon_* at H=3000000000000.
The proposed external inputs are the already compared
[Platt--Trudgian Theorem1 and Section2](https://arxiv.org/pdf/2004.09765v1),
the [Arb2.23.0 real_roots example](https://arblib.org/examples.html#real-roots-c),
its [isolation contract](https://arblib.org/arb_calc.html#subdivision-based-root-finding)
and the [pinned example source](https://raw.githubusercontent.com/fredrik-johansson/arb/2.23.0/examples/real_roots.c).
Reuse the exact versions and qualifications in assessment875. Published
coarse intervals are not permission to infer more digits or to import
the separate refined example with unresolved subintervals.

The intended discriminating test is a rigorous comparison between a
same-coordinate retained Gram lower bound and epsilon_* plus every
finite-input error. Before authorizing it, identify whether the reported
intervals and the covered Fourier integration method support a meaningful
conditioning test. The test may fail; neither interval overlap nor an
inadequate certified lower bound disproves positivity. Preserve such a
failure and park this small-subset certificate without a root-data retry,
mode/window change or precision escalation. If the input provenance or
precision is inadequate already at source comparison, record that exact
obstruction and choose independent work next.

A critical-line positivity argument for omitted zeros must be confined
to the precisely verified height and must handle both signs,
multiplicities and the endpoint. Above H only the audited absolute bound
is available. No sign for individual high terms, RH, a positive finite
Gram margin, exact high-zero list, infinite positivity or Xi-realization
assumption is admitted. Full matching Mathlib coverage remains unchecked.
No cross-notebook input is proposed.

## Completed source/input comparison880 — 14 November2026

This completion supersedes the nomination's missing-coverage statements.
The main gap remains L030-L032/C032a actual-Xi all-degree mixed positivity.
The intermediate target is exactly TARGET above. Its possible downstream
use is a finite U12 certificate before an independent infinite-complement
argument. No finite certificate would establish that complement,
non-neutral signs, Xi mixed positivity or global assembly.

### Published input and its transport qualifications

The [Arb2.23.0 examples, real_roots.c section](https://arblib.org/examples.html#real-roots-c)
prints the following output for `real_roots 0 0.0 50.0 -verbose`:

| Root | Printed left endpoint | Printed right endpoint |
| --- | --- | --- |
| 1 | 14.111328125 | 14.16015625 |
| 2 | 20.99609375 | 21.044921875 |
| 3 | 25 | 25.048828125 |
| 4 | 30.419921875 | 30.4443359375 |
| 5 | 32.91015625 | 32.958984375 |
| 6 | 37.548828125 | 37.59765625 |
| 7 | 40.91796875 | 40.966796875 |
| 8 | 43.310546875 | 43.3349609375 |
| 9 | 47.998046875 | 48.0224609375 |
| 10 | 49.755859375 | 49.7802734375 |

The reported counts are ten isolated roots and zero unresolved
subintervals. These are cited external computational inputs, not a local
replay. Only this coarse output is admitted. Neither the separate refined
single-root run nor radius-suppressed decimal lists supply extra accuracy.
No claim that coarse intervals suffice for a positive margin follows.

Read the [isolation contract](https://arblib.org/arb_calc.html#subdivision-based-root-finding),
`arb_calc_isolate_roots`: flag1 certifies a unique simple root;
other flags are unresolved; endpoint/multiple roots cannot be isolated.
The [pinned example source](https://raw.githubusercontent.com/fredrik-johansson/arb/2.23.0/examples/real_roots.c),
lines16–49 and199–208, selects the Riemann–Siegel Z callback with
no Dirichlet character. Lines308–327 distinguish isolated and unresolved
blocks. Its refined-output branch is irrelevant to the admitted data.
The [pinned isolator](https://raw.githubusercontent.com/fredrik-johansson/arb/2.23.0/arb_calc/isolate_roots.c),
lines16–54 and86–102, requires opposite nonzero endpoint signs and an
interval derivative excluding zero; the verbose message prints the block
with15 digits. This supports root existence/simplicity; it does not
certify an off-line census or a Fourier sampling margin. The conversion
from this real callback to critical-line zeta roots is the standard
Hardy-Z identity, [DLMF25.10.1](https://dlmf.nist.gov/25.10.E1)
(Titchmarsh1986, equation4.17.2, p89); its phase factor is nonzero
and its modulus equals the zeta modulus. No RH is needed for that
identification or the simplicity of an isolated real root.

The [pinned header](https://raw.githubusercontent.com/fredrik-johansson/arb/2.23.0/arb_calc.h),
`arf_interval_fprintd`/`arf_interval_printd`, prints each endpoint using
`arf_fprintd`. The [arf input/output contract](https://arblib.org/arf.html#input-and-output)
specifies faithful decimal rounding with at most one ulp error at the
requested digits. Consequently a future certificate must transport
these printed endpoints outward with that error enclosed. Do not treat
shortened decimal strings as the exact internal endpoints merely because
they look dyadic. The future numerical artifact must expose its actual
outward input intervals and rounding allowance. A transport allowance
is distinct from the much larger isolating-interval uncertainty.

Several guessed raw-source filenames returned404 and the GitHub directory
API was inaccessible. These are resolved discovery failures: the pinned
header, isolator and public output/rounding contracts were retrieved.
They are not an unresolved essential source blocker or a reason for
installation/data retries.

### Omitted zeros, complex coefficients and cutoff

Reuse L753's audited time-zero identity, including its exact moments,
complex reflected-conjugate product and absolute convergence. Reuse
L018's zero coordinate and multiplicity conventions. The future
specialization must split that identity into the admitted retained pairs,
omitted zeros with |height|<=H, and the complete |height|>H remainder.
It must explicitly check the real-ordinate square specialization for
arbitrary complex coefficients; real basis vectors do not license a
real-coefficient-only certificate. Both signs must be counted. Use
retained simple zeros once each, with any remaining multiplicity in the
omitted part. No assumption that these ten roots are the full finite
zero census is necessary or admitted.

The relevant primary premise is Platt–Trudgian, *The Riemann hypothesis
is true up to 3 times10^12*, [2004.09765v1, Theorem1 and Section2,
printed p2](https://arxiv.org/pdf/2004.09765v1). Theorem1 reaches
3000175332800, strictly beyond the fixed H=3000000000000. Section2
compares sign-change counts with a Turing count; it does not store
precise ordinates. This covers the sign premise for omitted zeros
through H, including the cutoff, when combined with L018's conjugation
symmetry. It gives no premise above H. Height zero is not covered by
that theorem's positive-height census. The elementary real-axis input
for the future applicability proof is the alternating representation
[DLMF25.2.3](https://dlmf.nist.gov/25.2.E3), valid for Re(s)>0,
attributed to Apostol1976, equation27, p292. Its restriction to real
0<s<1 and the standard alternating-series test cover real-axis
nonvanishing; this specialization must be stated in the certificate,
not silently dropped or attributed to the positive-height census.
No original zero-exclusion theorem is needed. A nonnegative
real-ordinate square contributes no adverse error even at multiplicity
or a cutoff endpoint. The actual decomposition and its application
are research work, not a new result proved in this review.

Above H use only audited C750d(4)'s absolute coefficient-space bound.
That input needs no further audit or zero data. There is no license
to replace complex high-zero products by modulus squares. Its epsilon_*
uses the Euclidean norm of the ten original coefficients, so any finite
matrix lower bound and every error norm must use that same metric or
an explicitly paid congruence. An L2-normalized margin is not directly
comparable. C750c Proof1/5 supplies the exact basis and original-L2
projections; do not define approximate moment kernels or projections.

### Integration coverage, conditioning and the bounded test

Reuse C750a's validated whole-panel integration and elementary interval
method, and C750c Proof3/5's enclosure of exact moments and two-by-two
projection inverses. These are supporting methods; their stored
arithmetic-energy outputs supply no zero-Gram entries. A new sample
evaluation must enclose every moment, ratio, original-L2 projection,
T, pi, Fourier factor and rounding error. It may reuse certified old
input intervals only with their complete error semantics intact.

Johansson, *Numerical integration in arbitrary-precision ball arithmetic*,
[1802.07942v1, Section2, callback contract and algorithm step2](https://arxiv.org/html/1802.07942v1#S2),
allows direct whole-box integration without an analyticity assumption.
This covers real and imaginary Fourier integrands with an interval
frequency parameter; uncertainty must be carried through evaluation.
Its analytic-ellipse branch requires a separate analyticity check and
is not approved across the flat cutoff joins. It supplies an enclosure
method, not an error small enough for this certificate.

The fixed-data test is therefore specified, not already won: construct
an enclosing retained Hermitian Gram matrix from these root pairs and
the ten exact coordinates, then compare a certified lower margin with
epsilon_* and all finite errors. A direct interval positive-definiteness
test on the shifted matrix, or a midpoint matrix with a rigorously paid
Hermitian perturbation norm, is a standard finite-dimensional method.
Use the standard spectral theorem/positive-definite LDL criterion;
there is no need to reprove those named inputs. Full complex pairing,
omission and metric specialization still need to be written. No
eigenvalue, sampling rank, favorable conditioning or margin is assumed.

Coarse endpoint widths alone do not decide this conditioning comparison.
The sources neither establish an adequate margin nor prove its
impossibility. They do support one finite interval test without any
new root-data access. Before running it, fix and record one finite
integration workload and arithmetic format using the covered methods;
include their full errors. No adaptive retry to rescue a failed margin
is authorized. If intervals or input/rounding/coordinate budgets prevent
certification, preserve the informative failure and park this subset
certificate; do not infer a negative exact form or a failure of RH.
If it passes, record only a finite certificate pending independent
review; all central gaps above remain unresolved.

### Overlap, sources not used and decision

Local searches were confined to November14 neutral assessments,
attempts and histories. C750c's audited scalar-floor rejection remains
unchanged; its Proof5 exact-energy second-pivot overlap is a different
evaluator failure. C750a's coarse frequency screen is not reopened.
Comparison876 already covers the identity, complete verified height,
BPT tail inputs and database/setup failures. No full stored-list or
installation retry was made. No existing inspected local result was
found to certify the present retained margin; this is not a novelty
claim. No shared infrastructure or cross-notebook input was used.

Additional queries were `"Weil" "Gram" "finite" "zeros" positivity`,
`site:github.com/fredrik-johansson/arb "arf_interval_printd"`, and
Johansson's exact integration title/arXiv number. Results included a
scale-resolved Weil-positivity repository, a compact event-cell preprint
and an uncertainty-operator numerical study. They remain unread leads,
not theorem evidence, sign inputs or claims of matching U12 coverage.
The reused adequate assessment supplies the known-method comparison;
this review fills only its missing data/transport/omission cases.
Full matching Mathlib coverage is unchecked; supporting finite
Hermitian, Fourier and interval facts are not a full formalization.

SPECIALIZE now covers exactly the unchanged TARGET with the SCOPE
above. No new lemma or mathematical script was written, and no Gram
bound or positivity result was derived. The changed readiness receives
separate supervisor approval before the mathematical invocation. No
justified creative central mechanism is ready: this is a diagnostic
within a known finite method, with no new route across the independent
infinite-complement and global-sign obstructions.
