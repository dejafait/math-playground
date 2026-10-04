# Compact lattice BRST gauge-fixing normalization — completed assessment

TARGET: At fixed mesh, test the normalization of standard smooth BRST-exact lattice Landau gauge fixing for SU(2) Wilson links with boundary gauge transformations fixed to the identity, before using it to extend L014.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Neuberger normalization, compact SU(2) Landau gauge fixing, boundary-pinned gauge transformations and Euler-characteristic formulations; read Testa's explicit finite-dimensional argument, Neuberger's author follow-up, Ghiotti–von Smekal–Williams and Schaden's primary statements. Boundary-specific queries supplied no separate theorem match.
SOURCE_EVIDENCE: https://arxiv.org/pdf/hep-lat/9803025v1 section 2, printed pp. 1–2, (1)–(9), and section 3, pp. 3–4, (12)–(17); https://arxiv.org/pdf/hep-lat/9801029v1 printed pp. 2–3; https://arxiv.org/pdf/hep-th/0611058v1 PDF pp. 1–3, especially p. 2, (1); https://arxiv.org/pdf/hep-lat/9805020v3 sections I–III, printed pp. 2–4, 12–16, (1), (27)–(34), (46)–(48), and section IV, pp. 16–17, (49). Rechecked Clay's linked 14-page official description, section 4, p. 6, and footnote 2, p. 12, at https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf.
COMPARISON: The closest result is Neuberger's standard compact lattice BRST normalization obstruction, explicitly presented by Testa: the gauge-fixed partition function and gauge-invariant numerators vanish. L014 instead uses a linear noncompact Gaussian prescription. The pinned cube requires a short applicability check, not a new normalization mechanism or a new no-go theorem.
GAP: Write the pinned-boundary link and interior ghost domains, verify preservation by the full nonlinear BRST transformations and justify the compact Haar/auxiliary integrals required by the cited argument. Distinguish a positive auxiliary-width definition from the exact delta-function Landau limit and a local weak-field prescription.
REASON: Complete the saved source review and approve only the bounded boundary applicability specialization. The known obstruction changes the route: no globally normalized smooth standard BRST replacement of L011's forest measure may be presumed. Cite the known argument and establish only the stated applicability difference next turn.
SCOPE: The unchanged TARGET at fixed even N >= 2, standard smooth trace-potential lattice Landau condition, full nilpotent nonabelian BRST algebra, continuous real auxiliary variables, all compact gauge copies, boundary transformations pinned and ghosts only on interior vertices. Begin with positive Gaussian auxiliary width. Equivariant, singular, restricted-copy and BRST-breaking alternatives, continuum boundary traces and ultraviolet estimates are outside ready coverage.

## Preserved target and relevance

The TARGET is exactly the saved Next action. At turn start this record
was REVIEW_REQUIRED and Neuberger was an unread lead. This literature-only
turn completes that record without evaluating a lattice normalization,
proving a pinned-boundary theorem or changing a lemma or mathematical
script. The completed [free Ward assessment](2026-10-03-auxiliary-brst-ward-identity.md)
is reused for its original Gaussian scope; it does not cover the global
compact extension.

The main intermediate gap is a legitimate nonlinear Wilson-measure Ward
formulation. A nonzero global gauge-fixing normalization would be necessary
for the proposed extension of L014. Its possible downstream use would be
a finite interacting Ward representation before tackling physical-boundary
subtraction. The overview, ID-only DAG, L003's fixed-boundary conventions
and forest reduction, L011's measure warning, L013–L014's scope and the
previous assessment were inspected. No previous local result settles this
compact normalization test.

The discriminating test remains the normalization, with the boundary and
integration hypotheses stated explicitly. If the cited obstruction applies,
stop this standard global completion and retain L014 and the exact forest
measure as separate inputs. A claimed nonzero normalization must identify
the failed hypothesis in the known theorem. Restricting copies, changing
the algebra or using singular gauge data changes the target and requires
separate screening. No search failure is evidence of originality.

The achieved free results still give no estimate on the interacting
reflected error; the required threshold remains <= c_box/2 on a specified
coupling trajectory. Physical-boundary remainder, finite matching,
ultraviolet field construction, full limiting reflection positivity,
infrared removal and finite positive mass are open. L012's strong-domain
failure and the stopped bulk-locality branch retain their original evidence.

## Search and access record

The bounded search used these queries and source-directed follow-ups:

- Neuberger 1987 Nonperturbative BRS invariance vanishing lattice gauge fixing partition function pdf
- lattice BRST Neuberger fixed boundary gauge transformations identity Euler characteristic
- Neuberger problem SU(2) Landau gauge partition function Euler characteristic lattice one site fixed
- Schaden Equivariant gauge fixing SU(2) lattice gauge theory hep-lat 1998 Euler characteristic
- "Neuberger" "boundary conditions" "gauge fixing"
- "Neuberger" "fixed" "boundary" BRST
- "Nonperturbative BRS invariance" filetype:pdf Neuberger
- "Neuberger" "SU(2)" "boundary" "BRST" lattice
- "lattice BRST" "fixed boundary"

Neuberger's 1987 publisher record identifies *Nonperturbative BRS invariance
and the Gribov problem*, *Physics Letters B* 183 (1987), 337–340,
[DOI 10.1016/0370-2693(87)90974-9](https://doi.org/10.1016/0370-2693(87)90974-9).
Its abstract was available; its full text was not read. The publisher open
failed and CERN's record returned a bot challenge. Those access failures
are preserved, with no repeated retrieval loop. The exact argument is
read in Testa's primary paper and corroborated by the author's accessible
1998 follow-up, so the original scan is not an essential blocker for this
bounded test. No conclusion depends on an unread equation in that scan.

Browser PDF text supplied the passages below. Screenshot requests yielded
no additional formula evidence and are not relied on. Schaden v2 was
initially read; the corresponding statements were then checked against
v3, the 21 October 1998 final arXiv revision used below. Search snippets,
ResearchGate results, dissertations and secondary summaries are leads,
not inputs. No essential source remains unread within the approved scope.

## Inspected primary statements

**M. Testa, *Lattice Gauge Fixing, Gribov Copies and BRST Symmetry*,
[hep-lat/9803025v1](https://arxiv.org/pdf/hep-lat/9803025v1),
30 March 1998; *Physics Letters B* 429 (1998), 349–353.**
Section 2, printed pp. 1–2, (1)–(9), is the closest usable citation. It
starts from finite-dimensional gauge-invariant Haar integration, adds
continuous real multipliers with positive Gaussian width and the standard
nilpotent BRST ghost pair, and introduces a parameter in the BRST-exact
gauge-fixing factor. Equations (6)–(9) state parameter independence and
zero normalization and gauge-invariant numerators. Section 3,
pp. 3–4, (12)–(17), illustrates copy cancellation and the need for globally
defined periodic data in an abelian example. This supplies the known
argument; the notebook's exact boundary restriction is not explicitly
named there. No derivation of that restriction is made in this review.

**H. Neuberger, *Comment on lattice BRST invariance*,
[hep-lat/9801029v1](https://arxiv.org/pdf/hep-lat/9801029v1),
21 January 1998, RU-98-02.** Printed pp. 2–3 distinguish perturbative
expectations from the global compact problem. The explicit example on
p. 3 is U(1), not this SU(2) cube. Its discussion warns that a preferred
trivial configuration or an apparently favorable gauge potential does not
remove the signed-copy problem. This is supporting scope evidence, not
a separate pinned-boundary theorem.

**M. Ghiotti, L. von Smekal and A. G. Williams,
*Extended Double Lattice BRST, Curci-Ferrari Mass and the Neuberger Problem*,
[hep-th/0611058v1](https://arxiv.org/pdf/hep-th/0611058v1),
6 November 2006.** Read PDF pp. 1–3. Page 2, (1), and its following
discussion extend the obstruction to the ghost/antighost-symmetric
Curci–Ferrari formulation and identify the normalization with the Euler
characteristic of the product of site gauge groups. That characteristic
vanishes for the stated SU(N) groups. A nonzero Curci–Ferrari mass changes
nilpotence, so its regulated model cannot be substituted for L014's
nilpotent construction. This is supporting topology and hypothesis coverage.

**M. Schaden, *Equivariant Gauge Fixing of SU(2) Lattice Gauge Theory*,
[hep-lat/9805020v3](https://arxiv.org/pdf/hep-lat/9805020v3),
21 October 1998; *Physical Review D* 59, 014508.**
Section I, printed pp. 2–4, (1), specifies the product of site groups and
separates tree gauge from covariant BRST gauge. Section II, pp. 12–13,
(27)–(34), restricts ghosts to charged components; the symmetry squares
to a residual U(1) transformation. Sections III–IV, pp. 15–17,
(46)–(49), state the orbit-independent normalization and the nonzero
Euler characteristic for the SU(2)/U(1) coset product. These inspected
statements describe a changed equivariant mechanism. They do not give
standard Landau gauge with all three ghost colours, this cube's boundary
formulation or an ultraviolet estimate. The full alternative construction
and its later continuum discussion are not imported.

**Official target check.** On 2026-10-04 the
[Clay problem page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/)
still links to Jaffe–Witten's 14-page
[*Quantum Yang–Mills Theory*](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf).
Section 4, printed p. 6, retains nontrivial continuum Yang–Mills for every
compact simple group, the specified axioms and finite positive mass.
Footnote 2, p. 12, retains the exclusion of bare weak compactness as a
resolution. The version and target agree with the existing source audit;
no route change weakens them.

## Exact applicability work approved

**Decision: SPECIALIZE.** The general obstruction is imported as literature
coverage. The unchanged TARGET is ready for a mathematical theorem
application classified REPRODUCTION. Do not reprove the deformation
argument, Euler-characteristic identity or L003's forest reduction. The
remaining work is a short check of the actual domains and convergence.

The boundary convention in L003 pins transformations at boundary vertices
and leaves independent SU(2) variables at interior vertices. The follow-up
must check that this restriction preserves the full nonlinear BRST algebra
and fixed boundary links, retains a nonempty ghost space for the admitted
meshes, and leaves compact invariant integration domains. A geometric
space-time boundary must not be mistaken for a boundary of a site-group
manifold. This is a source-applicability checklist, not a proved local
normalization verdict.

Use the standard globally smooth link-trace Landau potential and state
its interior gauge condition. Retain the nonlinear ghost transformation;
L014's free sc = 0 is not the nonabelian algebra. First define the auxiliary
integrals with positive Gaussian width, as in the closest citation and
L014's original auxiliary prescription. Check differentiation and BRST
integration coefficientwise on that finite functional. Only the necessary
applicability argument is authorized, without recomputing copies or
performing a nonlinear perturbative expansion.

Strict zero-width Landau gauge is a distributional limit. The standard
positive-width family already has the cited normalization obstruction;
calling its limit Landau gauge is not a justified normalization procedure.
If the follow-up instead uses an exact delta-function representation, it
must state how it treats degenerate copies and why that definition follows
from an inspected theorem. No nonzero direct singular prescription is
preapproved. A local logarithm chart, a copy restriction, an absolute FP
determinant or a BRST-breaking regulator cannot silently alter this test.

Continue the proposed global completion only if the applicability check
finds a concrete failed hypothesis and a separately justified nonzero
prescription. If it passes, record the known obstruction by citation and
stop this completion; the exact forest-measure and local free work remain
available. Equivariant gauge fixing is a distinct screened source lead,
not an approved boundary construction. There is no request to retry the
inaccessible 1987 scan or repeat this review before the bounded application.

This completed step is NEGATIVE / LITERATURE / NOVELTY_UNCHECKED: newly
inspected known obstruction changes the proposed extension's route, while
the local pinned-boundary verdict is deferred. No result beyond the
checked literature is claimed. Zero inconclusive mathematical attempts
remain on the auxiliary-field route; this review spends no calculation
turn. The preceding stopped bulk-locality route retains 3 of 3.
STATUS remains IN_PROGRESS, with no complete candidate resolution.

## Mathlib

Full pinned-boundary compact gauge-fixing normalization coverage:
**not checked**. Supporting compact Haar integration, Euler-characteristic,
Berezin and nonlinear BRST library coverage: **not checked**. The named
sources above provide the normalization obstruction and supporting
statements; no Mathlib theorem or library absence is asserted.
