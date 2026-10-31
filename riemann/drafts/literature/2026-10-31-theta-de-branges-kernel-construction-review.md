# Direct theta/de Branges kernel construction: completed comparison

TARGET: Assess theta-based positive-semidefinite representations of the de Branges kernel for the pair (Xi,Xi'), retaining multiple real zeros, and nominate one explicit finite-section test independent of RH or park this mechanism.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Compared three construction candidates: the direct derivative-pair/Weil realization, shifted Fredholm canonical systems, and the older translation-positive space. Searched exact construction terminology, followed primary references, and reused the correction/translate/multiplicity assessments and named local stops. No actual-pair construction passed the independent-positive-data test; this bounded search is not exhaustive.
SOURCE_EVIDENCE: Suzuki, Canadian Journal of Mathematics, online 3 November 2025, DOI 10.4153/S0008414X25101739, (1.3), Theorem 1.1, Sections 2.3/3.2, Proposition 4.1, Section 5 including Lemmas 5.1/5.3 and Theorem 5.5; Suzuki arXiv:1204.1827v2, Theorems 2.2–2.3 pp.7–9, Lemmas 4.1–4.4/proofs pp.11–13, Section 5 pp.23–24; Conrey–Li arXiv:math/9812166v1, Section 2/Theorem 1/proof and Section 3.1 pp.1–7, also readable arXiv HTML. Exact links and reading limits below.
COMPARISON: The direct-pair realization assumes RH; the explicit shifted construction proves a different parameter range and does not supply its zero-shift limit; the older extra translation sign is distinct from ordinary kernel positivity. No independently positive theta weight, actual-pair operator bound or controlled signed remainder was supplied by the inspected constructions.
GAP: Actual-pair positivity, an independent constructive representation and its all-parameter bounds remain missing. Multiplicity is retained in the direct-pair source, but neither its conditional space nor positivity of a finite section removes the RH premise. No impossibility theorem or matching new mathematical result is asserted.
REASON: Park direct kernel construction after this source comparison. Reopen with specified actual data and an independent positive bound, not another inverse-existence/equivalence citation. Select a separate critical replay of unaudited L569 under its unchanged, previously ready exact audit assessment.
LITERATURE_REASON: The startup REVIEW_REQUIRED target changed from zero-preserving corrections to a two-variable kernel construction; essential primary construction hypotheses and multiplicity cases had not been inspected. This turn supplies that comparison once.
SCOPE: Completed literature-only comparison of three candidates. No new result, proof specialization, lemma, mathematical script, DAG edge or argument-overview change; no theorem is installed as an unconditional local sign input.

## Gap and admission test

The main gap is actual-Xi all-degree positivity. The intermediate target
was independently positive construction data for the actual two-variable
kernel. Such data could provide a structured sign mechanism; its precise
implications for all higher mixed forms would still require justification.
A finite positive principal section by itself proves neither full kernel
positivity nor RH.

The startup test required specified actual input data plus an independent
positive weight/operator bound or signed remainder. None of the three
candidates below passes that test for the actual pair. Therefore no
finite-section calculation is nominated. This is a completed source
comparison with outcome EXPLORATION, not proof that no such representation
can exist or progress beyond the checked sources.

## Primary construction comparisons

**1. Direct pair and Weil realization.** Masatoshi Suzuki,
[On the Hilbert space derived from the Weil distribution](https://doi.org/10.4153/S0008414X25101739),
publisher HTML, version published online 3 November 2025.
Equation (1.3) uses E_xi(z)=xi(1/2-iz)+xi'(1/2-iz), with the prime
an s derivative. Theorem 1.1 assumes RH and identifies the model,
de Branges and completed Weil spaces with their stated norm constants;
it is explicitly not an isomorphism of reproducing-kernel spaces.
Read its statement, Section 2.3, the Section 3.2 cancellation at
zeros of arbitrary multiplicity, Proposition 4.1, and Section 5's
RH assumption, Lemmas 5.1/5.3 and Theorem 5.5/proof. The argument
uses an inner function and a real-zero sampling measure, rather
than proving these from theta positivity. Section 3.2 explicitly writes
A/(A+iA') near a zero with m_gamma retained; no simplicity premise
is needed for that cancellation. The inspected representation therefore
retains multiplicity but does not provide the independent positive data
required here. No upstream proof audit or unconditional import is made.

**2. Explicit shifted canonical systems.** Masatoshi Suzuki,
[A canonical system of differential equations arising from the Riemann zeta-function](https://arxiv.org/pdf/1204.1827v2).
The arXiv wrapper says v2, 23 September 2016; the PDF footer says
13 September 2018. References here identify this exact URL and numbering.
Theorem 2.3 requires omega>1 and constructs a diagonal Hamiltonian
from m(a)=det(1+H_omega,a)/det(1-H_omega,a), with the stated entire
solution and matching at a=1. It concerns the shifted pair (1.1).
Read Theorem 2.2's three alternatives, Theorem 2.3, and Lemmas
4.1–4.4 with full proofs: innerness licenses the contour shift/isometry;
zero-count noncompactness and compactness yield norm<1 for omega>1/2.
Section 5 separates continuity, Hilbert–Schmidt and small-shift
difficulties. These arguments do not furnish an unconditional norm
bound throughout 0<omega<1/2, a zero-shift limit for the derivative
pair, or its positive theta representation. Computing a shifted
finite section would not close those missing steps.

**3. Older translation positivity.** J. B. Conrey and Xian-Jin Li,
[A note on some positivity conditions related to zeta and L-functions](https://arxiv.org/html/math/9812166v1),
3 December 1998 preprint, Section 2/Theorem 1 and Section 3.1.
The source convention is E#(z)=conj(E(conj(z))) and

    K_E(w,z)=[E(z)conj(E(w))-E#(z)conj(E#(w))]
             /[2 pi i (conj(w)-z)].

Its reproducing-space interpretation starts with the upper-half-plane
Hermite–Biehler inequality. Theorem 1 additionally requires no real
zeros, E#(z)=epsilon E(z-i), |epsilon|=1, vertical strict monotonicity,
and Re<F,F(.+i)> >=0 for every F in the translation domain. Read
the entire proof, including K(w,w+i)=0 and repeated zero-factor
division. Section 3.1 takes E(z)=xi(1-iz), not the actual derivative
pair; its xi lacks L018's factor 1/2. It reports Mathematica negative
signs, not interval certificates. They are source-reported objections
to the extra translation condition, not locally verified counterexamples
or failures of ordinary kernel positivity. Thus this condition is
neither a positive construction for the target nor a substitute
for its multiplicity qualifications.

These are applicability comparisons. No known theorem is reproved or
specialized into a new lemma. No desired positivity is assumed as an
available mathematical premise.

## Local reuse, access and search limits

Read L018–L020's exact entirety, symmetry, positive theta kernel and
cosine representation, including their proofs. Their positive scalar
weight is not a theorem about the two-variable kernel. No local
normalization bridge or new kernel identity was derived here.
Read the October 6 multiplicity-count assessment and October 31
translate and zero-preserving correction assessments; the correction
and translate construction stops were read in full. Narrow term
searches checked de Branges, canonical systems, Hermite–Biehler,
Suzuki, Burnol and Conrey in local literature/attempts. The earlier
Weil-support note mentioned Suzuki only as an unread report; that
does not count as prior coverage of this construction target.
No sibling notebook or cross-notebook input was read.

Queries actually submitted:
- Lagarias Hilbert spaces entire functions Dirichlet L functions xi derivative de Branges 2006
- Suzuki canonical systems Riemann xi function theta kernel Fredholm determinant positivity
- Conrey Li note positivity conditions Riemann zeta de Branges kernel
- Lagarias "Hilbert spaces" "Dirichlet" filetype:pdf
- Suzuki "canonical system" "1204.1827"
- "Lagarias" "Hilbert spaces of entire functions" "Theorem" xi
- "E(z)" "xi" "Lagarias" "derivative" de Branges
- "Hilbert spaces of entire functions and Dirichlet" arxiv Lagarias 2005

Lagarias's [author-hosted 2006 chapter](https://websites.umich.edu/~lagarias/doc/debranges-houches.pdf)
had corrupted extraction; web screenshot calls supplied no usable image,
and shell retrieval failed DNS. No theorem proof from that file is
claimed read. The readable [18 June 2012 author slides](https://websites.umich.edu/~lagarias/TALK-SLIDES/benasque-riemann2012jun.pdf),
slides 11, 29–30 and 33, were supplementary only: they distinguish
multiplicity from no-real-zero normalization and describe the singular
endpoint construction problem. Their starred unpublished claims are
not used. The accessible publisher Suzuki source suffices for the
conditional-realization comparison; the inaccessible chapter is parked,
not a reason to retry access next turn. Conrey–Li's arXiv HTML resolved
the PDF extraction's lost nonstrict-inequality signs. Its ar5iv mirror
failed. No numerical certification was attempted.

Burnol's gamma/Sonine constructions, the upstream proof of Lagarias's
Theorem 1, and newer unrelated search hits remain uninspected leads,
not asserted positive representations of the actual pair. The bounded
comparison is not an exhaustive classification. Full matching or
supporting Mathlib coverage was not checked.

## Route and continuation

Park this direct construction mechanism. Reopen only with explicitly
available actual-pair data and a positive weight, operator bound or
signed remainder established independently of unknown zeros, RH, LP
or Hermite–Biehler membership. Retain common real factors and singular
endpoint issues; a normalized no-real-zero theorem cannot be applied
silently. Existing correction, translate, parity and absolute-budget
stops keep their exact scopes.

No justified creative actual-Xi target emerged: the missing independent
positive construction is a mathematical blocker, not an API/access
blocker. Select instead the separate critical replay of L569's
unaudited generic obstruction, using unchanged ready coverage
in `2026-10-31-hermite-compensation-multiple-zero-audit.md`.
The exact saved TARGET there remains the Next action. The prior
authoring step classified the local predicate; the next task is
independent proof verification, not a claim of a fresh classification
or reopening the stopped small-error sufficiency mechanism.

L569 is the canonical statement to check; it has no direct lemma inputs.
L564/L568 supply context only and are not needed to prove the generic
two-jet assertion. Verify both directions, all equality boundaries,
m=2 versus m>=3, and epsilon-small real analytic violations for each
fixed admissible F on a compact neighborhood. Repair any failure;
otherwise retain only the generic absolute-budget stop. Actual Hermite
realization, hypothetical versus existing multiple Xi zeros, signed
cancellation, all-height margins and higher signs remain unresolved.
L469's independent audit already exists and is not nominated again.
