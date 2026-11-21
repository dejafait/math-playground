# Actual arithmetic contact decomposition: bounded source review904

TARGET: Assess whether square-root subordination of the absolutely convergent Möbius series for 1/zeta gives an actual reciprocal-Xi contact-forcing decomposition with derivatives through order 2m-1 and a finite-head remainder bound test.
CHECKED: 2026-11-14
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Review904 searched reciprocal Xi/Möbius/Laplace and subordination terminology, inspected DLMF and Carron's scalar toolkit, and found Polson's directly relevant SSRN7243438 lead; its full text was not retrieved. Local exact-term screens and the L625/L722, direct-Mellin and contact stops are distinguished below; no novelty inference.
SOURCE_EVIDENCE: Read DLMF27.4.5, 25.2(i), 1.14(i)/(iii), 5.11.1 and 5.11(ii), 10.32.10/10.39.2; Carron2007 Section2.2 p2333; Baudoin2013 Lecture3 scalar identity. Reused C466a/b's qualified density/contact imports. Polson7243438 remains an abstract-only lead, not an inspected theorem.
COMPARISON: Known scalar transforms and sectorial gamma estimates cover tools, not the actual signed contact threshold. A positive subordination kernel does not turn signed Möbius coefficients or C466b's sign-changing weight positive. The new directly overlapping reciprocal-sign source has unread hypotheses and proof cases, so the broad forcing proposal is not approved.
GAP: Actual differentiated inversion, quantitative cofactor-weighted error and a positive finite-head margin remain unproved; Polson's exact comparison remains unavailable. The normalization and s=1/4 cancellation must be checked before treating a truncated arithmetic head as globally dominant.
REASON: Park the dependent all-order signed-forcing proposal. Nominate an independent two-term-head normalization/relative-error diagnostic with standard contour coverage in assessment904; it does not depend on Polson's uninspected positivity claims and establishes no contact sign here.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED concerned actual zeta/gamma inversion outside the fixed-law coverage; the new directly relevant Polson lead is unread and is recorded rather than used as a theorem.
SCOPE: C466a's actual normalized density and C466b's hypothetical rank-(m-1) contact at arbitrary finite m, including beyond the cited finite-PF range; ordinary absolute convergence only, with no new zero-free region or reciprocal-series continuation.

The original nomination below is preserved; its pending-review language
does not supersede the completed decision and source record appended below.

The main gap remains L030-L032/C032a. The proposed intermediate target
would expose an arithmetic contribution to the strict contact threshold
in C466b(7), rather than infer a sign from scalar positivity. A finite
signed head with a justified error could eventually be tested against
that threshold. This is a possible downstream use, not a sign claim or
a complete route to the main target.

Start from C466a's displayed gamma/zeta factorization of h(s), and
inspect the ordinary Möbius series only where
Re(1/2+sqrt(s))>1. The source question is whether the square-root
Laplace kernels can be composed with the remaining actual factor and
inverted with all derivatives needed by C466b's frozen cofactor
functional. The cancellation associated with s=1/4 in that factorization,
normalization, contour decay, sums and derivatives must be accounted
for explicitly. No positivity of a separated arithmetic or gamma
factor is assumed. Extending the Dirichlet series outside its ordinary
absolute-convergence domain is not part of this target.

Essential local mathematical texts for a later applicability argument
are C466a and C466b. C466e is the now-audited structural contrast;
it is not an input to an actual-Xi inequality. Reuse their precise
source assessments rather than reread whole sources indiscriminately.
The next comparison must search exact statements and standard terms,
read primary hypotheses and the essential inversion/derivative proof
cases, and finish the local duplicate screen. The L625 and L722
stops retain their original force for their own observables; their
different meanings of Möbius cost and subordination do not establish
anything about this proposed representation. The previous contact
stops886/889/891/898/899 remain preserved.

Bounded continuation test: obtain adequate source coverage for a
legitimate differentiated representation and nominate a concrete
finite-head/tail comparison for C466b(7), stating the required error
relative to the signed head. If only a formal rewriting is available,
if the needed estimate assumes global PF/complete monotonicity, or if
the split cannot be justified, record that precise failure and choose
a different independently testable target. An absolute error estimate
without a head margin does not establish strict forcing. No new
decomposition, inversion, estimate, numerical experiment or lemma is
derived in this nomination.

Actual forcing, possible simultaneous contacts, propagation and the
final L030-L032/C032a interface remain unresolved even if this source
comparison succeeds. Full matching Mathlib coverage is unchecked.
No justified creative proof attempt is ready yet: this source review
is preparation to decide whether a new central mechanism exists, not
a creative label for ordinary transform specialization.

## Completed source comparison904 — 14 November 2026

The main gap is still actual-Xi all-degree positivity at L030-L032/C032a.
The reviewed intermediate target was an actual arithmetic decomposition
of C466b's frozen contact forcing. Its plausible use was a signed head
whose proved error is smaller than its positive margin. The continuation
test was a legitimate differentiated representation and such a
comparison, not just a transform identity. Neither is claimed here.

Representative executed web queries were `square root subordination
e^{-a sqrt s} Laplace transform heat kernel Schilling Bernstein functions
pdf`, `"reciprocal" "xi" "Möbius" "Laplace"`,
`"subordination" "reciprocal" "zeta" density`,
`Polson reciprocal xi Mobius Laplace transform gamma convolution`, and
`"Thorin, Levy and Mobius" filetype:pdf`. Follow-up exact-title,
SSRN7243438 and author-domain searches sought primary full text only.
Unrelated search hits were not used as mathematical evidence.

### Inspected standard inputs and exact limits

NIST DLMF, live edition accessed 14 November 2026:

- [27.4.5](https://dlmf.nist.gov/27.4#E5) states
  sum mu(n)n^(-w)=1/zeta(w) for Re(w)>1. This is the ordinary
  absolute-convergence domain; no continuation of that series is imported.
  The source covers the arithmetic transform, not a differentiated
  inverse transform with the completion factor.
- [25.2(i)](https://dlmf.nist.gov/25.2#i) states that zeta has a simple
  pole at w=1 with residue one. Together with C466a's existing
  factorization, this identifies a required cancellation to inspect at
  s=1/4. No finite-head cancellation or inverse asymptotic is derived here.
- [1.14(i), inversion](https://dlmf.nist.gov/1.14#i) assumes absolute
  integrability and local bounded variation. Equation
  [1.14.20](https://dlmf.nist.gov/1.14#E20) uses continuity of f,
  piecewise continuity of f', and a line to the right of its exponential
  growth bound. Equations [1.14.27](https://dlmf.nist.gov/1.14#E27) and
  [1.14.29](https://dlmf.nist.gov/1.14#E29) retain initial values and
  impose regularity/growth conditions. A formal factorization verifies
  none of these hypotheses for a separated gamma inverse. The safe
  prospective alternative is Fourier inversion of the known tilted
  density, with absolutely integrable polynomial frequency weights
  proved before differentiating. C466a already uses that method at
  fixed order; its estimates are not automatically an effective
  Möbius-head error estimate.
- [5.11.1](https://dlmf.nist.gov/5.11#E1) is sectorial log-Gamma
  asymptotics for |arg z|<=pi-delta. The first paragraph of
  [5.11(ii)](https://dlmf.nist.gov/5.11#ii) bounds the complex
  log-Gamma remainder by the first neglected term times
  sec(arg(z)/2)^(2n). These are usable tools for the composed argument
  sqrt(s)/2+1/4. A bound for Gamma itself must not be inverted without
  a lower-modulus estimate. No explicit completed-factor bound, line
  integral, or constant for the proposed truncation is supplied here.

Gilles Carron, *Riesz transforms on connected sums*, Ann. Inst. Fourier
57(7) (2007), 2329-2343,
[Section 2.2, p2333](https://www.numdam.org/article/AIF_2007__57_7_2329_0.pdf#page=6),
displays the Poisson/heat subordination kernel
a exp(-a^2/(4t))/(2 sqrt(pi) t^(3/2)), a>0. Read the displayed identity
and its use in Lemma 2.3's proof. That lemma's geometric Sobolev
hypotheses and heat-kernel bounds are not inputs here. Fabrice Baudoin's
[Lecture 3, exercises, 24 June 2013](https://fabricebaudoin.blog/2013/06/24/lecture-3-semigroup-generated-by-a-symmetric-diffusion-operator/)
states the scalar identity for a>0 and real spectral parameter.
It is an exercise statement, not a proof of our proposed inversion.

The scalar integral's standard special-function references were also
inspected: [DLMF10.32.10](https://dlmf.nist.gov/10.32#E10), with
|arg z|<pi/4, and
[10.39.2](https://dlmf.nist.gov/10.39#E2), the elementary value of
K_(1/2). Their hypotheses cover the positive real scalar case; complex
extension and composition with the actual factor still need an
applicability argument. The a=0 term is a point mass at zero, not the
displayed density with a naively set to zero. Positive scalar kernels
alone say nothing about signs after multiplying by mu(n).

### Essential unread lead and bounded access record

The search found Nicholas G. Polson, *Thorin, Levy and Mobius: Sign
Structure in the Reciprocals of xi and zeta*,
[SSRN7243438](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7243438),
DOI 10.2139/ssrn.7243438. The indexed primary landing page reports
35 pages, written 6 August and posted 8 August 2026. Only its abstract
was available. It advertises a signed arithmetic/archimedean comparison
and a square-variable representation. No theorem number, hypotheses,
contact estimate, version-specific proof or asserted equivalence from
this lead is imported. The abstract cannot establish either coverage
or a new obstruction to the present target.

Direct SSRN access returned403; the delivery URL and DOI route failed.
Exact-title, DOI/PDF and author-domain searches did not retrieve a
primary full text. These are access results, not evidence the paper
or relevant theorem does not exist. No authentication or API key was
used. Sra's v1 Hub also timed out; reuse C466a/b's existing inspected
source chain, rather than replacing it with newer-version snippets.
The attempted Schilling--Song--Vondracek PDF links were inaccessible;
the accessible Carron/scalar and DLMF inputs above suffice for the
independent diagnostic, so those book failures create no new dependency.

### Duplicate/failure comparison and decision

Read C466a/b in full. Reused their density assumptions, fixed-order
Fourier argument, flat endpoint and exact signed threshold (7).
The separate arithmetic pieces are not known densities. C466e is only
a structural contrast, as already audited in903.

The local screen searched reciprocal, Möbius/Mobius, subordination,
inverse-Laplace and Bromwich terminology in the relevant November
assessments and failure records. Assessment884/886 and898 preserve
the scalar, cumulative and contact stops. Assessment651
(`2026-11-05-direct-mellin-schoenberg-scope.md`) and its recorded
direct-Mellin stop concern the reciprocal of a different Mellin factor
and an unpaid PF deconvolution premise. They do not authorize this
gamma inverse. The L625 raw-amplifier assessment concerns height
differentiation of a fourth-moment observable. The L722 stop concerns
signed spatial-residue rates at a fixed profile; its word
"subordination" is not Laplace square-root subordination. Neither
settles the proposed arithmetic representation. No exact matching
local head/remainder result was located; this is not an originality
claim or a global history scan.

Decision: SOURCE_BLOCKED for the broad contact-forcing comparison.
The standard toolkit is documented, but full theorem-level comparison
with the directly relevant lead and an actual signed margin are missing.
Do not repeat source retrieval or formal inversion indefinitely.
Park that dependent proposal. Assessment904 nominates a different,
independently testable two-term-head cancellation/relative-error
diagnostic using only the existing normalization and standard contour
tools. Its result may delimit global domination while leaving a compact
joint-cancellation approach open. No such diagnostic was performed here.

No new lemma, decomposition, estimate, script or numerical experiment
was produced. Full matching Mathlib coverage is unchecked; C466b's
supporting convolution coverage does not verify this arithmetic split.
Actual contact forcing, simultaneous contacts, propagation and the
L030-L032/C032a interface remain open. This is bounded source review,
not progress beyond the inspected mathematics or an RH candidate.
