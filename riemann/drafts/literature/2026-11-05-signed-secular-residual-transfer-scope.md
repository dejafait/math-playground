# Signed secular residual transfer — completed bounded source comparison

TARGET: Assess whether signed secular-equation perturbation bounds yield a degree-explicit sufficient test for p+E to retain simple positive roots when p is simple-positive-rooted and E has zero coefficients through degree four, using signed residues rather than an absolute coefficient envelope.
CHECKED: 2026-11-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Step593 searched mixed-sign secular residues, diagonal rank-one perturbations and finite real-root bounds; inspected primary cases below and reused the finite-pencil, root-disk and rational-inertia assessments. No matching signed finite guarantee was identified in this bounded search; no absence or novelty claim.
SOURCE_EVIDENCE: Ipsen--Nadler author manuscript, Section2.4 Theorem2.6/proof pp5--6 and Section4 Theorem4.1/full proof pp10--12; Ran--Wojtylak arXiv:2007.01188v1, equations(3)--(6), Proposition2/full proof pp3--5, Theorem13/proof p10, Section6/Theorem24 pp17--19; correction arXiv:2203.07811v1 introduction p1. Exact links and qualifications below.
COMPARISON: The inspected Hermitian finite bounds need plus/minus yy*; the non-Hermitian bound is norm-based and allows complex eigenvalues. Secular multiplicity and robust-collision results require unpaid critical-value information. These do not furnish the requested signed improvement over L793 or the fixed-pencil scope of L792.
GAP: No usable finite mixed-sign bound with full-degree and positive-root control was imported. Actual signed residual control and growing-degree model existence remain independent gaps; zero residues and leading-coefficient cancellation cannot be omitted.
REASON: Park automatic transfer from these sources rather than turn a norm estimate or collision identity into a signed theorem. An independently testable next source target concerns existence of the fixed L791 model across degrees, not another perturbation budget.
SCOPE: Completed literature-only screen of real degree-d p,d>=5 with simple positive roots, real deg(E)<=d and E_0=...=E_4=0. No new inequality, specialization, lemma, mathematical script or numerical test; no technical research continuation is approved by this source-screen outcome alone.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED lacks primary coverage of finite mixed-sign secular transfer; the existing assessments cover different hypotheses and were reused without reopening their conclusions.

## Original nomination, retained as context

The main gap remains actual-Xi all-degree mixed positivity. The proposed
intermediate target is a finite, quantitative signed transfer criterion
for a specified real-rooted model. Its plausible downstream use is to
turn actual theta residual cancellation into a root-retention bound,
if a later independently justified signed estimate and growing-degree
models become available. None of those inputs is supplied by this
nomination. It is not a new mathematical result or ready research scope.

The next source review should check signed secular equations and
indefinite rank-one perturbation bounds, keeping finite versus
infinitesimal claims separate. Retrieve primary hypotheses and the
essential cases for mixed residue signs, a varying leading coefficient,
and exclusion of zero or negative output roots. A source criterion must
use independently accessible model/residual data and guarantee the full
degree at the requested perturbation size. A count bound for nonreal
roots, a formal characteristic-polynomial identity, or an output
real-root premise does not meet this target.

Compare the exact target with
`2026-11-05-root-eliminating-reciprocal-bezoutian-review.md` and
`ATTEMPTS/2026-11-05-root-elimination-automatic-sign-source-stop.md`:
those transformations retain unpaid inertia or residue orientation.
Here model roots are retained and the question is a quantitative finite
perturbation range, not automatic signing of an actual reciprocal block.
Also reuse the finite-pencil and componentwise root-disk coverage;
merely restating their critical-value or absolute-norm criterion gives
no different mechanism. The selected local search found those overlaps,
not evidence of novelty or complete literature coverage.

Continue only if an inspected theorem provides a sufficient signed
bound whose improvement can be tested without assuming p+E's roots or
actual Xi positivity. Otherwise record the precise source limitation
and stop this lead. Do not derive a bound or test the matched prefix
during that source turn. If the resulting claim needs new mathematics,
nominate its exact later test separately; if a known theorem covers it,
import it with only necessary applicability work.

Essential context is C792a/C792b's fixed prefix, L791/L792's conditional
model and residual normalization, and L793's finite absolute-tolerance
scope. Their exact-data and analytic/evaluator/software contracts stay
unchanged. No growing-degree model or signed residue estimate is
assumed. No cross-notebook input is proposed; full Mathlib matching
coverage is unchecked. Missing independently supported signed control
still blocks a justified creative proof attempt. This source nomination
must not be labeled creative merely to meet the scheduling preference.

## Completed comparison — step593, 5 November 2026

The main gap is still actual-Xi all-degree mixed positivity. The finite
intermediate target could have converted independently proved signed
residual cancellation into positive-root retention for a specified model.
The inspected sources do not supply that missing cancellation or a usable
signed finite test of the requested kind. This is a source-scope negative,
not a counterexample to such tests or to the actual family. No bound was
derived, no model tested and no theorem reproved.

### Primary hypotheses and essential cases inspected

I.C.F. Ipsen and B. Nadler, *Refined perturbation bounds for eigenvalues of
Hermitian and non-Hermitian matrices*,
[author manuscript](https://www.weizmann.ac.il/math/Nadler/sites/math.Nadler/files/publications/refined_perturbation_bounds_for_eigenvalues_of_hermitian_and_non-hermitian_matrices.pdf),
undated PDF accessed 5 November 2026: Section2.4, Theorem2.6 and complete
proof, printed pp5--6, bounds interior eigenvalues of A+/-yy* for Hermitian
A. Its proof compresses to principal submatrices and uses Hermitian
interlacing. This hypothesis does not cover arbitrary mixed-sign updates.
Section4, Theorem4.1 and complete proof, pp10--12, permits general E but
requires Hermitian A, an eigenvalue mu of A+E, its closest lambda_i(A),
and Gap_i>3||E||_2. It concludes
|lambda_i(A)-mu|<=sqrt(5)||E v_i||_2 for unit v_i. The proof uses
Bauer--Fike, Weyl and a resolvent estimate after unitary block reduction.
It explicitly permits complex mu. Thus it is a finite norm estimate,
not by itself a signed reality/positivity and full-count certificate.
No specialization of its matrices or constants to our polynomial was made.

A.C.M. Ran and M. Wojtylak, *Global properties of eigenvalues of parametric
rank one perturbations for unstructured and structured matrices*,
[arXiv:2007.01188v1](https://arxiv.org/pdf/2007.01188v1), 2 July 2020:
equations(3)--(6), Proposition2 and full proof, printed pp3--5, use
B(tau)=A+tau uv* and Q=v*(lambda I-A)^(-1)u. Away from sigma(A),
multiplicity k is characterized by Q=1/tau and vanishing derivatives
through k-1, with kth derivative nonzero. Pole cancellation/frozen
values require separate treatment. Theorem13 and full proof, p10,
show persistence of a real collision satisfying Q'=0,Q''!=0,Q>0 under
small real perturbations; Section6/Theorem24, pp17--19, extends the
collision discussion to specified indefinite structures. Neither
excludes collisions throughout a given finite parameter interval.
Its derivative tests retain the unpaid critical-value information.
Theorem24's printed J-symmetric/J-Hamiltonian terminology is not used
for an import here. The
[2022 correction](https://arxiv.org/pdf/2203.07811v1), introduction p1,
concerns Theorem17's large-parameter asymptotics; those are not used.
This is comparison of inspected statements, not a new application.

### Exact differences from the requested result

The target allows E(rho_i)=0. An off-spectrum secular multiplicity
statement cannot silently count these shared model/output roots.
It also allows a varying leading coefficient, including complete
cancellation unless separately excluded. The inspected fixed-matrix
characteristic-polynomial formulas are monic; a claimed polynomial
application would need explicit normalization and a degree check.
No such normalization, finite path bound or root-count theorem was
proved during this source turn.

The prescribed zero coefficients through degree four are additional
constraints, not hypotheses of the cited perturbation bounds. None
of the inspected passages explains a quantitative signed benefit from
that prefix. Likewise a local collision formula does not certify that
all d roots at the requested parameter are simple and positive. A
successful signed test must separately account for both properties,
full degree, and any zero residues, using model/residual data.

Reuse the complete finite-pencil assessment
`2026-11-05-central-signed-index-five-residual.md` and L791/L792's
normalization/hypotheses: their d=5 reciprocal constant pencil already
has quantitative collision margins. Reuse
`2026-11-05-mesh-losing-root-disk-tolerance.md`, L793's method/hypotheses
and `ATTEMPTS/2026-11-05-relative-root-disk-transfer-unpaid.md`:
another generic absolute budget would not supply actual-family inputs.
Reuse the reciprocal-Bezoutian comparison and its automatic-sign stop
for the distinction between a signed signature identity and an estimate.
These adequate assessments were not refreshed by further browsing.
C792a/b's universal and same-mesh stops retain their original limits.

### Search record, access qualifications and decision

Queries included `secular equation mixed signs residues real roots rank
one perturbation sufficient condition`, `diagonal rank one perturbation
real eigenvalues mixed signs small perturbation bounds secular equation`,
`secular equation real-rooted residues`, and title searches for the
primary papers above. More literal signed-residue searches produced
irrelevant results, not evidence of theorem absence. Search snippets,
MathOverflow and abstracts were not accepted as theorem coverage.

Gernandt--Trunk's *Eigenvalues of parametric rank one perturbations of
matrix pencils*, 2022 preprint, remains an unread lead: the DNB PDF
returned429 and the institutional PDF redirected to a browser challenge.
The 1996 diagonal-perturbation secular-equation publisher page returned403.
No essential result is attributed to these inaccessible passages. The
accessible papers suffice for the source-scope comparison just made;
these failures are not a reason to continue access retries or claim a
general obstruction. The correction's full asymptotic proof, unrestricted
spectral-placement papers and secular numerical algorithms remain unread
and are not inputs.

The continuation test fails for the inspected candidate imports: no
signed finite improvement independent of an output-root premise was
identified. Park automatic secular transfer; reopen only with a precise
new finite theorem or an independently supported signed estimate, not
another collision-identity or norm-bound audit. Full matching Mathlib
coverage is unchecked. No new lemma, DAG input or main argument results.

The separately nominated next source question is whether L791's **fixed**
exact parameter choice supplies a positive-rooted model in every degree.
That tests model existence before perturbation and is independent of
universal residual preservation. It neither assumes such an extension
nor proposes parameter tuning, a sweep or a new tolerance. Its scope
requires separate review; no protected creative attempt is justified
by the present source screen.
