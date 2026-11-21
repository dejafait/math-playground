# Nominated conceptual audit of the discrete support-edge transfer

TARGET: Critically audit L721's discrete signed-bump support-edge limsup for the original L703 bump, including finite-path symbol realization, Volterra support preservation, sampled endpoint singularity and the entire exponential remainder.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 195 reused the step-193 exact-target comparison and inspected the common-phase/gamma-Rice failure records, L721 in full, and relevant L719--L720 statements/source interfaces. Targeted primary lookup checked DLMF complex-analysis statements and Tao Fubini hypotheses/proof; no repeated broad support-theorem search or novelty claim.
SOURCE_EVIDENCE: NIST DLMF 1.9(iii), (1.9.30)--(1.9.32); 1.10(ii), (iv), (vii), (viii), including (1.10.8), (1.10.12)--(1.10.14), (1.10.18), live text inspected 2026-11-03. Terence Tao, An Introduction to Measure Theory, author-hosted December 2012 preliminary PDF, Theorem 1.7.21 and proof pp.204--205, Corollary 1.7.23 p.206. Precise links and applicability boundaries below; inherited analytic-symbol source comparison reused.
COMPARISON: The sources cover Cauchy derivatives, local holomorphic inversion, identity continuation, finite residues, parameter-integral holomorphy and absolutely integrable complex Fubini. They do not certify the exact finite-path comparison, triangular support preservation or endpoint contradiction in L721. Existing broader support assessments remain inapplicable as direct imports; this is a source-ready audit of the written specialization.
GAP: Audit L721 Sections 1--5 against L719--L720, including common neighborhoods, truncation orders proportional to n, exact sampled germ identification, transverse absolute integrability, terminal support implication and the full error disk. No new theorem coverage is essential for that bounded audit; none of these local claims is accepted by this literature decision.
REASON: The formerly nominated source gate is complete. SPECIALIZE authorizes an independent conceptual audit of the existing construction using imported standard tools, without importing its signed-rate conclusion or reproving general FIO/support theorems.
SCOPE: Exactly TARGET; L721 and the original fixed bump, audited L714 (1)--(5), L719 and L720. No residue-rate, full-response, complementary Jensen or Xi claim is included.

The claimed equality is limsup log|K_(12q+3)|/(12q+3)=Re S(b),
where b is the actual right endpoint of supp(chi), not the prescribed
enclosure endpoint. The polynomial normalization n^(-1/2) must be
removed without changing zeros or the limsup. Use log(0)=-infinity.

The new input is [L721](../../lemmas/L721-discrete-signed-bump-support-edge-transfer.md).
The proof is fully written there and remains unaudited. Read its exact
hypotheses and the relevant L719--L720 inputs before assessing the
following points; this nomination grants none of them anew.

- The saddle rectangle yields positive Re S' and a nonzero derivative
  of Z=exp(-12*S), including local continuation past the actual endpoint.
  Strictly decreasing |Z| must exclude all remote aliases on the arc.
- The factorial coefficients define a convergent B(v,t). Repeated
  finite-path integration must match all a_k/n^k, with uniform factorial
  and endpoint errors through m proportional to n. Confirm that this
  compares with the entire exact Q_n, not only a saddle contribution.
- Localization and compact Fubini must give the stated fixed density
  and exponential error. The triangular equation's nonzero diagonal
  must preserve the actual support edge without an assumed inverse
  theorem, positivity of the transformed density or analyticity of chi.
- The same germ from the origin must be identified on both sides of
  the local slit. Check the biholomorphic chart, exclusion of remote
  arc pieces, transversal crossing, absolute double integrability,
  residue sign and the terminal integral implication. A branch jump
  alone is insufficient.
- The complete error series must be holomorphic on a strictly larger
  disk, including every inherited contour error. Check finite omitted
  sizes, n=12q+3 and the coefficient-growth contradiction. Only a limsup
  is claimed; a full limit and eventual nonvanishing are not premises.

Continue with a precisely covered conceptual audit and a verdict on
these claims; otherwise identify the essential missing source before
dependent mathematics. Reuse the primary comparisons already available
rather than repeating broad searches. Full matching Mathlib coverage is
not checked. A favorable audit would establish a local input for a later
residue comparison, while all full-response and actual-Xi gaps remain.

An audit of this newly derived endpoint transfer takes priority over
inventing a creative target to satisfy scheduling. No independently
source-ready mechanism for the complementary Jensen or Xi-realization
gaps was established in step 194. The sole current action and routing
are recorded in PROGRESS.md.

## Completed source gate — step 195, 3 November 2026

The nomination above is preserved as historical scope, not a second pending
source task. This section discharges that task; the mathematical audit is
still pending. No lemma or mathematical script was changed in this turn.
LITERATURE_REASON: Newly nominated audit requires explicit coverage of the
finite-path and transverse-contour tools, especially complex Fubini at the
crossing, beyond the prior general analytic-support comparison.

### Primary statements actually inspected

- [DLMF 1.9(iii)](https://dlmf.nist.gov/1.9.iii),
  (1.9.30)--(1.9.31): analytic interior, continuous closed-contour data,
  interior evaluation point and positive orientation are required for
  Cauchy's value/derivative formulas. (1.9.32) distinguishes inside/outside
  winding for a simple positive contour. These cover the named tools,
  subject to the audit's neighborhood and contour checks.
- [DLMF 1.10](https://dlmf.nist.gov/1.10), inspected sections ii, iv,
  vii and viii: identity continuation needs a connected common domain;
  (1.10.12)--(1.10.14) provide a local analytic inverse at a point with
  nonzero derivative, not global injectivity. The residue theorem
  (1.10.8) allows finitely many interior singularities, none on the
  contour. The finite parameter-integral theorem (1.10.18) requires
  joint continuity and holomorphy in its complex variable. These
  statements do not cover a crossing contour by themselves.
- T. Tao, *An Introduction to Measure Theory*, AMS GSM 126 (2011),
  [author-hosted preliminary PDF, December 2012 file](https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-126-tao5-measure-book.pdf),
  Theorem 1.7.21 and its proof, printed pp.204--205, and Corollary
  1.7.23, p.206 (PDF pages 220--222, one-based), read in full.
  For complete sigma-finite measure spaces, measurable complex integrands
  with finite product integral of their modulus have equal iterated
  integrals, with sections defined almost everywhere. The corollary
  permits proving this by an iterated modulus bound. The proof reduces
  real/imaginary and positive/negative parts to Tonelli. Apply the
  standard theorem after real parametrization of the contour; checking
  the actual crossing domination remains the audit's job.
  The preliminary PDF prints the same iteration twice in Theorem
  1.7.21(iii); its clauses (i)--(ii), proof and following Euclidean
  formulation explicitly supply the intended swapped-order assertion.
  No inference depends on the duplicated display.

The DLMF pages are live sources inspected on CHECKED; no fixed release
number is asserted. They state the standard named theorems; their book
references were not separately opened. Tao's original Tonelli construction
is imported, not reproduced here. No Plemelj, Borel-summability or analytic
FIO inverse is an additional essential source for the written finite
construction. General wavefront and sampled real-Laplace sources retain
the exact limitations already recorded in step 193; they were not reread.
Full matching Mathlib coverage remains unchecked.

### Audit obligations and decision test

L721 is the only located written proof of this particular transfer in the
specific local records inspected. L719--L720 supply phase and all-order
kernel inputs; they do not supply the signed-rate conclusion. The
common-phase and gamma/Rice stops were read directly and retain their
qualifications: neither rules out this exact discrete construction,
neither establishes a rate, and L717/L718 remain excluded inputs.

The audit must independently check the actual assertions (5)--(22),
including fixed domains for B, every integration-by-parts endpoint and
uniform truncation range, the whole Q_n comparison, and preservation of
the actual support edge under (17). At (19)--(20), test both the common
germ identification on the connected slit neighborhood and absolute
integrability after parametrization. Ignoring a crossing parameter is
legitimate only after the latter hypothesis is verified; neither the
residue theorem nor compactness alone grants it. Finally check all
exponential weights, finite omitted samples, n=12q+3 and normalization,
with log(0)=-infinity. These are audit questions, not findings this turn.

Accept only a fully justified limsup for the unchanged original bump;
otherwise preserve the exact failed inference or missing input. Do not
replace it by a full limit, positivity, eventual nonvanishing, an endpoint
law or a different bump. This audit could validate an input for a later
actual-residue comparison; complementary spatial Jensen defect, other
responses, amplitude/full charge, H/support and Xi realization stay open.
The essential audit takes priority over preparing a creative mechanism;
no independently source-ready central mechanism was established here.
