# Family 003 zeta specialization — bounded audit nomination

TARGET: Assess source coverage for a bounded independent audit of the zeta specialization of OpenAI family 003 Theorem 1.1 at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a, identifying one load-bearing analytic claim for hypothesis and circularity checks.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the October 21 overlap assessment/register; targeted searches for continuation-criterion, common signal and inversion in the family003, fixed-half-plane and witness assessments and October 21 history found no existing audit of this proposition. Retrieved the pinned primary TeX, its Section 2 statement and complete proof, and the final theorem application; checked primary Fourier-inversion hypotheses in Mathlib and NIST DLMF. Search queries and access qualifications are recorded below.
SOURCE_EVIDENCE: OpenAI September 30 manuscript at 1581d4cbdd69a0faf34b2089614fe2a814316a6a, Theorem 1.1, Section 2 Proposition labelled lem:continuation-criterion (statement, all proof cases and following specialization), and concluding application after prop:parameter-order. Mathlib.Analysis.Fourier.Inversion, MeasureTheory.Integrable.fourier_fourierInv_eq and fourierInv_fourier_eq, including complete displayed hypotheses; DLMF 1.14(i), equations 1.14.3--4. Exact links and bounded retrieval locations follow.
COMPARISON: The selected claim is already explicitly proved in the primary manuscript; only an independent conditional audit is justified, classified REPRODUCTION if undertaken. Fourier inversion has matching standard support, but its integrability, normalization and continuity hypotheses must be checked in this signal. Neither the statement-level IMPORT nor these standard theorems independently verify the manuscript's low/high arithmetic estimates.
GAP: Audit only the conditional continuation proposition: endpoint control, Mellin holomorphy, Fourier identification, division by H, poles and the family-uniform supremum contradiction. The low/high probe estimates and H construction remain explicit assumptions; no zero-free conclusion may be used to prove them. A separate ready continuation assessment records this exact later audit.
REASON: Primary coverage now isolates one fully accessible load-bearing analytic reduction. This closes the nomination's source-scope question, not the mathematical audit or the external-premise trust qualification. Independent verification is the reason for reproducing an already stated argument; no novelty or RH progress is claimed.
LITERATURE_REASON: Essential primary proof coverage for an independent audit is absent from the existing statement-level import. Reuse that import without repeating broad discovery; retrieve only the pinned theorem and the proof cases needed to nominate one bounded claim.
SCOPE: Zeta specialization of the September 30 Theorem 1.1 only, strict Re(s)>7/8 with s=1 treated separately as the analytic pole. Preserve the external premise and all current qualifications. No conductor-uniform extension, alternate 11/12 proof, Liu improvement, whole-repository scan, Lean build or full manuscript audit is included.

## Original nomination, preserved

The following paragraphs describe the invocation-start nomination. Their
unread-source language is superseded by the completed source review below.

The exact pinned [primary TeX](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)
and [primary PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf)
are recorded in the existing register. Their present accessibility and
the correctness of any internal argument have not been checked in this
nomination. Model memory, a release announcement or comparator metadata
cannot replace the primary proof comparison. The register explicitly
distinguishes imported results from locally verified manuscripts.

The main gap remains actual-Xi all-degree positivity. This target
addresses the trust qualification of an analytic premise used by the
conditional witness branch, rather than supplying positivity itself.
The local statement to retain is L452 and its use in L461; their
proofs need not be loaded until a precise application question requires
them. No cross-notebook input is proposed. Independent initial signs,
effective overlap and actual-Xi realization remain unresolved.

Continue only if a named analytic claim can be isolated with its exact
hypotheses, proof location and essential source cases, so that a later
audit has an independently checkable threshold. If its citation already
covers it, recommend import/applicability checking rather than reproof.
If access is blocked, record the actual failed source and park dependent
work under the shared recovery rules; do not substitute another general
statement of the claimed theorem. This is a nomination requiring a
separate source review, not approval of uncovered mathematics.

A new creative attempt is not justified by the failed modulation source
screen. Its missing arithmetic bridge remains the explicit blocker;
this source-verification target must not be labeled creative to meet
a scheduling preference. Full matching Mathlib coverage is unchecked.

## Completed source review, 2026-10-30

The selected claim is the Section 2 proposition **Continuation from a common
signal**, TeX label `lem:continuation-criterion`, in the pinned
[primary TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
Theorem 1.1 is `thm:main`. The proposition's complete statement and proof,
not just its introductory description, were read. In the web tool's rendered
line numbering they occupy 339--477; the final application was read at
15557--15585. These are retrieval coordinates, not asserted physical TeX
line numbers or PDF pages. The stable labels identify the passages.

### Exact hypotheses and claimed conclusion to audit later

These are source statements, not a new local lemma or a verification.
The field is F=Q(sqrt(-3)). Let beta_* be the supremum of {1/2} together
with real parts of zeros in 1/2<=Re(rho)<=1 of all primitive finite-order
Hecke L-functions over F. Poles are omitted. Fix sigma_0 in (1/2,1),
assume Delta_0=beta_*-sigma_0>0, and put C(s)=s+c for fixed real c.
The numbers omega and sigma obey 0<omega<Delta_0 and sigma>0 and must
be chosen independently of the primitive target eta.

For each such eta the assumptions supply a finite prime-ideal set S, a
holomorphic H_eta on Re(s)>sigma_0 with
sup |H_eta(s)-1|<=1/2, and J_eta(Z) for every sufficiently large real Z.
Define, for all Z>0,

    L_F^S(s,eta)=L_F(s,eta) product_{p in S}(1-eta(p) Np^(-s)),
    f_eta(Z)=(1/(2 pi i)) integral_{Re(s)=2}
             Z^(s+c) exp((s-5/6)^2) H_eta(s)/L_F^S(s,eta) ds.

The two assumed bounds are

    |J_eta(Z)| <<_eta Z^(C(sigma_0)+omega),
    |J_eta(Z)-f_eta(Z)| <<_eta Z^(C(beta_*)-sigma).

Constants, thresholds, S and H_eta may depend on eta. The claimed conclusion
is a contradiction with beta_*>sigma_0, conditional on these assumptions
for every primitive target. The manuscript's definition assigns local value
zero at ramified primes. Original zero extensions and finite deleted Euler
factors must be retained. Principal functions are meromorphic; a pole is
not a zero.

### Proof cases and precise comparison

The source introduces epsilon_*=min(Delta_0-omega,sigma). Its proof uses:
the two large-Z bounds; contour shifts only to fixed lines Re(s)=B>2
to control Z approaching zero; a locally uniformly convergent Mellin
transform on Re(s)>beta_*-epsilon_*; Fourier inversion on Re(s)=2;
the identity theorem; division by nonvanishing H_eta; and a zero selected
from the supremum defining beta_*. Each of these proof passages was read.
Their correctness is the later audit target, not a finding of this review.

The exact Fourier input has primary coverage in
[Mathlib's inversion documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/Inversion.html#MeasureTheory.Integrable.fourier_fourierInv_eq).
`MeasureTheory.Integrable.fourier_fourierInv_eq` assumes integrability of f
and its inverse Fourier transform and continuity of f at the evaluation
point; it concludes Fourier(inverseFourier(f))=f there. The companion
`fourierInv_fourier_eq` states the other orientation. The displayed
hypotheses include finite-dimensional real inner-product domain and complete
complex normed codomain; R and C fit these type hypotheses. The documentation
links to the [pinned supporting source](https://github.com/leanprover-community/mathlib4/blob/d0207795ac79006da92d98544e1ce915ae386160/Mathlib/Analysis/Fourier/Inversion.lean).
The manuscript instead writes exp(i t u) with coefficient 1/(2 pi), so
the audit must explicitly check the change of frequency convention and
both L1 hypotheses, not substitute a formal double integral.

[NIST DLMF 1.14(i)](https://dlmf.nist.gov/1.14#i), equations 1.14.3--4,
was also read: its stated alternatives impose local bounded variation or
continuous derivative, in addition to absolute integrability. Do not silently
use the bounded-variation version from bare continuity. The exact L1/L1
Mathlib statement is adequate primary theorem coverage for the intended audit.
The manuscript cites no specialized external theorem inside this proposition;
the remaining standard inputs are the named Cauchy integral theorem, identity
theorem and classical Hecke meromorphic continuation/Euler product theorem.
No unproved zero-free bound left of Re(s)=1 is an approved standard input.
Full matching Mathlib coverage of the continuation proposition and its
Hecke-family assembly is not checked; the inversion theorem is supporting
coverage only. No formal build was run.

For the downstream use, the manuscript substitutes sigma_0=7/8 and
C(s)=s-11/16, with omega=Delta/2 and sigma=m/2 in its concluding argument.
That passage invokes `prop:parameter-order` and
`eq:shared-principal-nonvanishing`, then
`prop:hecke-dirichlet-transfer`. Those constructions, their positive
family-uniform margins, the first-stage 11/12 theorem and the transfer
proof are outside the selected audit. Their mention identifies the use;
it does not verify their hypotheses. In particular even a successful
conditional audit does not verify Theorem 1.1 or its local uses L452/L461.

### Search, access and decision limits

External queries included “Fourier inversion theorem f and Fourier transform
integrable Folland 8.26 theorem” and primary-author Tao Fourier-inversion
queries. Tao's 245C Notes 2 formula (11) was inspected and concerns Schwartz
functions at that point; it is not the selected L1/L1 justification.
A Folland search extract was not promoted to primary-read evidence after its
PDF URL returned 404. Search snippets and secondary discussions were not
used as theorem evidence.

The GitHub HTML TeX view exposed metadata only, but raw TeX through the web
tool supplied the full selected proof. Shell curl failed with DNS resolution;
the PDF routes failed with restricted-URL/unsupported-content-type responses.
These are delivery limitations, not a persistent essential source blocker:
the exact pinned TeX is accessible. No downloaded TeX or PDF is claimed.

Continue to one conditional critical audit if its scope remains exactly the
proposition above. Success means every stated analytic operation and the
family-uniform contradiction check out under the explicit assumptions;
failure means a precise missing hypothesis or invalid operation is recorded.
Do not extend that result to the arithmetic estimates. If a necessary source
outside this coverage becomes essential, stop dependent derivation and record
the missing case. This completed nomination is literature EXPLORATION,
not a new bound, a mathematical advance, or an audit verdict.


### Source-hypothesis correction, 2026-10-30

The direct-source recovery in
[the conditional audit assessment](2026-10-30-family003-common-signal-critical-audit.md)
supersedes the sentence above attributing inverse-transform integrability to
`fourier_fourierInv_eq`. Its explicit hypothesis is forward-transform
integrability. No independent applicability verdict accompanies this source
correction. The nomination's conditional target and all exclusions persist.
