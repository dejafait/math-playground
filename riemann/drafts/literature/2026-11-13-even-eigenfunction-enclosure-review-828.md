# Direct even eigenfunction enclosure — completed source comparison829

TARGET: Assess a direct weighted uniform eigenfunction-enclosure test for a simple positive lowest even eigenfunction of C759a's complete form on (-1,1), checking boundary regularity and full spectral-gap requirements without assuming semigroup or resolvent positivity.
CHECKED: 2026-11-13
DECISION: EXPLORE
SEARCH_EVIDENCE: Step829 searched exact Weil/eigenfunction/uniform-error, logarithmic boundary regularity, a posteriori eigenspace enclosure and logarithmic graph-norm terminology; compared C759a/h, assessments791/821/822, October30 boundedness/renewal/BV coverage and stops822/823/826. Primary reads and queries are recorded below; no adequate complete sign certificate or novelty claim results.
SOURCE_EVIDENCE: Reuse Suzuki2606.09096v2 and Teschl2009 as assessed791/821. Inspected Hernandez-Santamaria--Lopez Rios--Saldana2401.18033v2 Theorems1.1/1.4, definitions1.15-1.19 and Section4 proof; Liu--Vejchodsky1904.07903v4 Section2, Theorem3.1 and proof, Theorems5.1/5.2 and proofs. Arsu2015 was screened only as an embedding lead, not imported. Exact versions/links follow.
COMPARISON: Sharp boundary decay and verified Hilbert-space eigenspace errors are known separately. Neither inspected theorem supplies the actual complete operator's quantitative residual-to-weighted-uniform estimate or independently verifies a one-dimensional lowest even spectral cluster. The bounded continuation test for this implementation was not met.
GAP: Complete spectral isolation with multiplicity one, actual-Q boundedness/weak-form applicability, effective weighted error and a positive trial margin remain unpaid. No eigenfunction sign, gap, boundary weight theorem for Q or general nonembedding result is established here.
REASON: Park direct sign certification from the inspected sources; this is a source-scope stop, not an impossibility theorem. Nominate a separate, independently testable prerequisite: actual-operator interior sup-norm control from an L2 residual. Its one-family concentration test needs neither a spectral gap nor a positive eigenfunction.
LITERATURE_REASON: The target changes from the ready all-times form-order audit to full spectral isolation and weighted eigenfunction error; existing L2 resolvent and signed-nullvector regularity assessments did not cover that essential estimate.
SCOPE: Completed literature-only comparison of complete unneutralized Q at half-width1, with both poles and all five prime powers. No eigenvalue computation, new lemma, mathematical script, reproof, fixed-pair replay or source certificate import. EXPLORE does not authorize the original sign implementation; only the separately assessed prerequisite is nominated.

The original nomination and its stopping test below are preserved as
the question reviewed. Their future-tense instructions are superseded
by the completed comparison829 at the end of this file.

## Purpose and three mechanisms compared

The main gap is still L030–L032/C032a actual-Xi all-degree mixed
positivity. A simple positive lowest even eigenfunction at this one
window would supply one missing ground-state input. Odd/even ordering,
other windows, the actual-Xi realization and global positivity would
remain independent. This is a proposal for source review, not an
assertion that these inputs suffice for RH.

1. All-times positive semigroup: C759i Proof6 now independently
   validates the strict violation of its necessary form inequality.
   That implementation is closed; another pair or approval is unnecessary.
2. A positive resolvent at a prescribed parameter: stop822 lacks an
   independently controlled kernel, and C759h/stop823's full-residual
   enclosure crosses zero. Neither failure is a theorem against all
   resolvents, but no sharper mechanism justifies reopening either test.
3. Direct eigenfunction enclosure: select for review. Its proposed
   observable is a weighted uniform error relative to a positive trial,
   together with a full spectral isolation certificate. It need not
   prove cone preservation by the complete semigroup or a resolvent.
   The necessary analytic estimates have not yet been identified.

## Exact review obligations and bounded test

Keep C759a(1),(5)-(6), Proof1 as the full form and domain. C759i is
a contrast ruling out one order argument, not a sign premise for an
eigenfunction. C759h Proof1-2 provides a spectral floor and an actual
operator action on H1_0 trials, but its whole-residual bound is not
uniform control of an eigenfunction. No cross-notebook input is used.

Search exact a posteriori eigenfunction-enclosure, spectral-projection
and logarithmic boundary-regularity terminology, then inspect primary
theorem statements and the relevant proof cases. Determine which norm,
weight, endpoint conditions and complete spectral separation are needed.
If a weighted sup-norm method is applicable, the proposed later test
must compare its certified relative error strictly against the trial's
positive weighted margin throughout the open interval. Both the weight
and that margin must be justified, not chosen from numerical samples.
This names the desired threshold; no such inequality is derived here.

Account for endpoint behavior and translated prime terms. An interior
continuity theorem, a finite-dimensional eigenvalue separation, an L2
eigenvector error, or a theorem assuming a positive ground state is
insufficient. Proving simplicity requires isolation with multiplicity
one in the full even operator, not only in a trial matrix. The reviewed
condition must expose how all complementary modes are controlled.

Continue only if primary results give a noncircular, quantitatively
evaluable error mechanism and specify the remaining arithmetic inputs
for one fixed trial/isolation test. If the hypotheses already require
the desired sign, give only interior regularity, or supply no effective
complete error, record that scope obstruction and park this proposal.
Do not substitute eventual positivity or restart the parameter-16 test.

## Existing source scope and failure evidence to reuse

[Suzuki2606.09096v2](https://arxiv.org/html/2606.09096v2), the exact
realization passages listed above, is already assessed in791. Its
small-window positivity does not cover half-width1. The Teschl input
in C759h is [Mathematical Methods in Quantum Mechanics, 2009 version,
Theorem2.18 and Lemma2.7](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf);
only its inspected L2 spectral-distance estimate is reused, not any
unread uniform eigenfunction estimate. Read no large source passage
until its precise theorem and assumptions are relevant to the test.

The local October30 assessment
`2026-10-30-weil-nullvector-bounded-variation-coverage.md` already records
that Kulczycki–Ryznar arXiv:1307.7158v1 Theorem1.1 requires nonnegative
harmonic data and Jarohs–Kassmann–Weth arXiv:2311.15337v2 Theorem1.5
provides interior continuity under its stated assumptions, not global
BV control of the signed solution. Those comparisons concern L516's
different fixed nullvector problem and are used only as import cautions;
no L516 theorem is imported or rederived here. A quantitative weighted
eigenfunction enclosure is not established by either recorded conclusion.

No justified creative central mechanism is yet available: the required
error estimate and an arithmetic bridge to actual-Xi positivity are
missing. This source review must establish a concrete discriminating
test before choosing any proof-attempt route; it is not relabeled
creative to fill a scheduling quota. Mathlib coverage is unchecked.


## Completed comparison829 — 13 November2026

### Boundary theorem: useful upper control, unpaid sign/error input

Hernandez-Santamaria, Lopez Rios and Saldana, *Optimal boundary
regularity and a Hopf-type lemma for Dirichlet problems involving the
logarithmic Laplacian*, DCDS45(2025),1-36,
[arXiv:2401.18033v2](https://arxiv.org/html/2401.18033v2),
Theorem1.1 assumes a bounded exterior-uniform-sphere domain, bounded
forcing, and a bounded zero-exterior weak solution in H(Omega).
It gives continuity and |u(x)|<=C sqrt(ell(dist(x,boundary))), with
ell(r)=1/|log(min(r,0.1))|. Its symbol is2log|xi|.
The complete Section4 proof uses Kelvin barriers, a small-domain
maximum principle and both u and -u; its transformed forcing depends
on u. It does not state a computable residual-to-error constant for Q.
Theorem1.4's Hopf lower bound assumes a nontrivial nonnegative
continuous supersolution in V(Omega), vanishing at the boundary point,
and an interior sphere. These sign hypotheses cannot prove the desired
sign. Definitions(1.15)-(1.19) fix the weak pairing.

The interval geometry fits, but the full operator, its bounded
solution/forcing hypotheses and an effective error bound still need
justification. The October30 boundedness/renewal assessments already
inspect this theorem; their source coverage is reused. L515's audited
bound concerns its specified signed-convolution model, with actual-Weil
identification still conditional; no unnoticed identification or uniform
bound for a general eigenfunction error is imported here. A boundary
upper estimate is not a positive weighted trial margin. No new boundary
lemma or specialization was derived829.

### Eigenspace errors: the full spectral gap is an input

Xuefeng Liu and Tomas Vejchodsky, *Fully computable a posteriori error
bounds for eigenfunctions*, Numerische Mathematik152(2022),183-221,
[arXiv:1904.07903v4,16July2022](https://arxiv.org/html/1904.07903v4).
Section2 uses Hilbert inner products a,b and compact gamma:V->W.
Theorem3.1 assumes correctly dimensioned clusters and
lambda_n<rho<=lambda_(N+1); its proof sums over the complete spectrum.
Theorem5.1, with its full proof, bounds Hilbert-space projector error
by residual/sigma when the entire complementary spectrum avoids the
approximate cluster enlarged by sigma>0. Theorem5.2 and proof retain
this exclusion for the weak formulation and use its dual norm.
Neither theorem supplies a weighted sup norm. The Introduction explicitly
assumes independently obtained two-sided eigenvalue bounds.

Thus a finite Ritz separation does not verify these hypotheses. To
identify the lowest even space as one dimensional, its full second
eigenvalue must be separated, counting multiplicity; any conversion to
pointwise error remains a different obligation. Applying the abstract
framework would require checking a positive shifted form, compact
embedding and the exact norms; no application is performed here.
C759h's scalar floor establishes an inverse at-16, not such a cluster
isolation. This source comparison is local progress in selecting a test,
not progress beyond the cited results or toward an RH sign bound.

### Search, duplicates and read limits

Queries included: `logarithmic Laplacian boundary regularity eigenfunctions
logarithmic Holder boundary weight`; `a posteriori eigenfunction error
bounds uniform norm spectral gap logarithmic Laplacian`; `logarithmic
Laplacian optimal boundary regularity log Holder Hopf lemma 2024`;
`"Weil quadratic form" "eigenfunction" "uniform" error`;
`"logarithmic Laplacian" "a posteriori"`; `"logarithmic Laplacian"
"eigenfunction" "sup" "error"`; `"logarithmic" "graph norm"
"L infinity"`; and generalized Fourier-weight embedding queries.
No failed search establishes novelty or nonexistence.

Arsu, *On Hormander--Kato spaces*, J.Operator Theory73(2015),159-185,
[primary PDF](https://www.theta.ro/jot/archive/2015-073-001/2015-073-001-008.pdf),
was screened through its Introduction/Definition1.1 and bounded search
hits for embeddings. No applicable necessity theorem or full proof was
inspected; none is imported. Hormander's book Theorem2.2.7 was only
identified through secondary references and remains unread. Lin--Stamm's
elliptic DG estimates, geometric-stable Green estimates and logarithmic
FEM papers are leads, not assessed input for the complete Q certificate.
The incorrect guessed1904.07903v6 URL failed; the version record and v4
HTML/PDF were accessible, so there is no persistent source-access blocker.

Narrow local searches also found residual-compression assessment729;
its positive quadrature/moment error concerns C998u's kernel construction,
not an operator-domain embedding or eigenfunction enclosure. It is not a
duplicate. L515's time-one bound, C759h's resolvent error and C759i's order stop retain
their scopes. We do not repeat the disjoint-pair test, the256-dimensional
solve, a parameter sweep, or a proof of an already inspected theorem.

### Decision and one discriminating continuation

The nomination required an effective complete weighted error mechanism
and spectral isolation before attempting a sign certificate. Those
requirements were not supplied; park that implementation, preserving
its independent gaps in ATTEMPTS/2026-11-13-even-eigenfunction-enclosure-source-stop-829.md.
This is informative source-scope evidence, not a counterexample to a
positive simple lowest even eigenfunction and not a global route ban.

A different, necessary norm question can be tested independently: can
an L2 residual control even an interior uniform norm on this operator's
full domain? The new assessment
`2026-11-13-even-residual-interior-norm-test-829.md` defines one central
concentration family and a divergence threshold. Its approval is for a
future bounded test only; no divergence, embedding failure, coefficient
bound or mathematical lemma has been proved in this literature turn.
If that test supplies an obstruction, stronger residual norms or a
specific spectral/error subspace would still be possible, with their own
coverage. Full spectral isolation and boundary-relative control remain
independent. No main-gap creative mechanism is justified yet: no signed
arithmetic transfer to actual-Xi mixed positivity has been supplied.
Mathlib coverage is unchecked. No cross-notebook input was used.
