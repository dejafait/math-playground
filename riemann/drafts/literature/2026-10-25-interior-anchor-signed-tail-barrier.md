# Interior-anchor signed-tail barrier — source comparison

TARGET: Test whether L322's signed-tail obstruction extends under L461's retained premise to fixed 3/8<eta<1/2 and cutoffs K<=c log(2+|a|)+B with 0<=c<eta/2.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L322's full proof, L320's strip/anchor proof, L461's analytic estimates and audit, the saved construction/audit assessments and the September 24 ellipse failure. Searched exact signed-tail, logarithmic-cutoff and entire-function Taylor-section terminology; inspected the primary Cauchy estimate and a nearby finite-height Laguerre theorem, as detailed below.
SOURCE_EVIDENCE: Grava, Complex Function Theory (December 29, 2024), section 4.4, Lemma 4.16, printed p. 42 (PDF p. 46), statement and full proof; DLMF 5.11.9 and bounded-real-part uniformity; Sra, On some positivity properties of the Riemann Xi function, v1 October 20, 2026, equation (1.5) and Theorem 1.3, pp. 2–3. Reused inspected Titchmarsh Theorem 14.2 proof coverage and the pinned external premise without reopening their audits.
COMPARISON: L322 supplies the exterior-anchor signed-tail mechanism; L461 supplies separately proved conditional interior strip growth and anchor bounds. Cauchy's estimate covers coefficients without requiring the evaluation anchor to lie inside its circle. No inspected theorem states the target limit on the changed domain; a fixed-parameter specialization with all losses retained is needed, with no originality claim.
GAP: The mathematical attempt must justify independent use of L461's analytic estimates at a smaller radius and larger anchor, choose strict margins before varying height, absorb all subpower losses and control the finite sum uniformly in every allowed K. The signed-tail limit remains unproved in this review.
REASON: Essential source coverage for the exact saved test is now available. Approve one REPRODUCTION attempt using the known mechanism; this literature-only comparison neither derives the extension nor changes the old stop or the external premise's trust status.
SCOPE: Fixed 3/8<eta<1/2, fixed 0<=c<eta/2 and B>=0, nonnegative integer K, every sufficiently large absolute real height, actual Xi, and precisely L461's retained external premise. No moving anchors, endpoint c=3/16, coefficient signs or external-theorem audit.
LITERATURE_REASON: The invocation-start assessment was REVIEW_REQUIRED because the proposed anchor domain and circle ordering were outside the saved coverage. This turn fills that comparison while reusing the unchanged logarithm-source assessment.

## Purpose and proposed discriminating test

The main gap remains initial signs and global mixed positivity.
The successful L461 audit permits use of its conditional smaller
witness cutoff, but supplies no signs. Before investing in further
fixed-anchor optimization, test whether the same Taylor-tail mechanism
has the corresponding obstruction in the new anchor domain. A proved
obstruction would redirect work toward signs or a different witness
mechanism; it would not obstruct RH itself.

Use L461's H_a and T=2+|a|, and write
S_(K,a)(eta)=sum_(n=0)^K D_n(Xi;a) eta^(2n). The proposed threshold
is the uniform limit

    (H_a(eta)-S_(K,a)(eta))/H_a(eta) -> 1

as |a| tends to infinity over the stated integer cutoffs. This is a
target, not a conclusion. Continue to mathematics only after the
separate comparison establishes adequate coverage for the exact
changed domain, its strict margins, all subpower losses and uniformity
in K. Abandon this implementation if the required smaller-circle
bound is outside that coverage or its losses cannot be absorbed with
parameters fixed before height varies. Do not infer failure of a
moving-anchor or other witness method from a fixed-anchor result.

Essential proposed inputs are L018, L320, L322 and L461, with L005
and L452's retained premise if the logarithm estimate must be reused.
L322's original stop must be preserved. In particular, any use of a
circle radius below eta must justify the separate estimate's actual
domain rather than apply L461's witness conclusion outside eta<R.
The external September 30 Theorem 1.1 at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a` remains conditional,
strict Re(s)>7/8 with the pole allowed and its manuscript/import
closure locally unaudited. Constants are existential; central zeros
must remain permitted. The prior audit only nominated this target;
the present literature review completes coverage without deriving it
or making an originality claim.
Full matching Mathlib coverage remains unchecked.

## Inspected sources and precise applicability

Tamara Grava, [Complex Function Theory](https://people.sissa.it/~grava/cft.pdf),
dated December 29, 2024, section 4.4, Lemma 4.16, printed p. 42
(PDF p. 46): an analytic function on a domain containing the closed
radius-R disk, bounded by M on its boundary, satisfies
|f^(n)(z0)| <= n! M/R^n for every nonnegative integer n. Read the
full proof from the differentiated Cauchy formula and contour length
estimate. This theorem bounds coefficients at the center; it imposes
no condition on a later point where a finite polynomial is evaluated.
L018's entire completion is the proposed analytic input. The required
height-dependent M must still be justified from the local estimates.
The finite sum and its uniform cutoff estimate are application work,
not a theorem asserted by this citation.

[DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9) was inspected with its
following uniformity sentence: the vertical gamma modulus asymptotic
holds at both signs of infinite height, uniformly for bounded real
parts. This covers the fixed-strip gamma input used in L461. Reuse
the construction assessment's inspected 5.11.1/5.11.3 sector/remainder
coverage; no new gamma estimate is needed. Bounded shifted heights
and positivity remain local applicability obligations.

Reuse [the construction assessment](2026-10-24-fixed-half-plane-witness-cutoff-coverage.md)
and [audit assessment](2026-10-24-l461-witness-cutoff-critical-audit-coverage.md)
for Titchmarsh, second edition revised by Heath-Brown (1986), Theorem
14.2, proof pp. 336–337, especially (14.2.5)–(14.2.6). Those records
inspected the logarithm normalization, Borel–Caratheodory and
three-circles cases. The printed theorem assumes RH and cannot be
imported by substituting 7/8 into its hypothesis. L461's locally
audited changed-domain argument is the proposed input. A fresh PDF
retrieval timed out; it adds no proof evidence and is not an essential
blocker because adequate passage coverage is already recorded.

The [external register](../../foundations/2026-10-quasi-riemann-input.md)
retains precisely September 30 Theorem 1.1 at the pinned commit above.
No new external-theorem audit or stronger zero-free premise is used.

## Local comparison and obligations for the separate attempt

L322's equations (4)–(6) and their proof handle a smaller circle by
using separate growth and anchor estimates, followed by Cauchy's
coefficient estimate and a finite geometric sum. Its actual domain
is eta>1/2 and r>1/2, so it does not already prove this target.
The [September 24 failure record](../../ATTEMPTS/2026-09-24-elliptical-witness-tail-test.md)
stops the exterior-anchor tail comparison and contour reshaping;
it explicitly leaves moving anchors and other comparisons separate.
Its evidence remains valid. No new ellipse estimate is proposed here.

L461's opening combined statement assumes eta<R, but the source
comparison must use the proofs of (4), (8), (10)–(12), rather than
apply its combined witness conclusion with radii reversed. The
logarithm construction uses a fixed lower real part strictly above
7/8. Whole-strip propagation is a completed-function growth argument
with a boundary at 1/2+R. The anchor argument treats its own fixed
line, strictly between 7/8 and 1, by nonvanishing, Stirling and
continuity. These are the relevant covered mechanisms. A later proof
must explicitly separate their parameters, rather than infer a
reversed-radius estimate just from the statement of L461.

Remaining mathematical obligations, not results of this review:

- Select a fixed smaller circle in the assessed interior domain,
  compatible with the target's strict cutoff margin. Justify each
  use of the independently parameterized growth and anchor estimates.
- Retain both shifted heights on the complex circle and all four
  epsilon losses in the normalized growth comparison. Establish a
  strictly decaying bound after summing all coefficients through K;
  choose radii and loss parameters before height-dependent constants.
- Verify uniformity for every integer 0<=K<=c log T+B, including c=0,
  and keep B fixed. Use the positive anchor without dividing by Xi(a)
  or any central derivative, so central zeros remain admissible.
- Prove the stated signed-tail limit itself. Do not infer a sign
  theorem, a moving-anchor obstruction, an endpoint result or RH.

These obligations use known estimates and L322's already inspected
method, but their changed-domain application has not been performed.
There is no remaining essential unread source for this bounded test.

## Search scope and nearby results

Queries on 2026-10-25 included `Riemann xi generalized Laguerre
inequalities Taylor coefficients logarithmic cutoff Taylor remainder
zero free half plane`, `entire function Taylor partial sums Cauchy
estimate smaller radius large parameter normalized tail`, `"Xi"
"signed tail" Taylor anchor`, and `"Laguerre" "witness" "cutoff"
zeta "3/16"`. Exact terminology returned no matching theorem;
this is a bounded search, not evidence of novelty. Notebook-scoped
searches located L322, the saved assessments and the ellipse failure;
unrelated response-tail records were not loaded.

Suvrit Sra, [On some positivity properties of the Riemann Xi function,
v1, October 20, 2026](https://suvrit.github.io/papers/riem-xi/riem-xi-v1.pdf),
equation (1.5) and Theorem 1.3, pp. 2–3, were read in the primary PDF.
The theorem assumes all zeros through a fixed height T lie on the
line and gives all-order Laguerre nonnegativity on |x|<=T-1/2.
That finite-height theorem does not state the proposed asymptotic
tail limit at unbounded centers. Its proof was not audited and it
is not imported into this attempt. Its notation agrees on the
coefficient definition, without supplying the missing sign coverage.

A logarithmic-order positivity manuscript, a thesis on numerical
cancellation in Taylor sections, and other returned positivity papers
were search leads only; their theorem/proof passages were not read
and no conclusions from them are used. None is an essential input
to the Cauchy/growth specialization. Full matching Mathlib coverage
and supporting API coverage remain unchecked; absence is not claimed.

Decision: SPECIALIZE for the unchanged TARGET, later classification
REPRODUCTION. The next invocation must receive separate approval
for this newly completed assessment. Continue if the strict margins
absorb the losses uniformly; otherwise record the failed threshold
and stop this implementation. No new mathematical result, lemma,
script, DAG edge or change to PROOF.md was made in this review.
