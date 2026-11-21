# Weak local one-sided calibration — source assessment

TARGET: Test whether the nominated paired-fiber graph admits a locally Lipschitz weakly closed one-sided calibration on a neighborhood of its strip that saturates its full mass and obstructs finite radial replacements confined to that neighborhood.
CHECKED: 2026-11-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded searches for Lipschitz/weak Stokes, local one-sided graph calibrations, degenerate holomorphic-density saturation and stronger calibration results; queries and precise local duplicate/failure comparison below. No matching existence or nonexistence theorem found; no novelty inference.
SOURCE_EVIDENCE: Kangasniemi–Prywes, J. Geom. Anal. 35, 88 (2025), Sections 3.2, 4.2–4.3, Propositions 4.2/4.5 and Appendix proof of Proposition 4.2, https://doi.org/10.1007/s12220-025-01916-6; complete Dubrovskiy arXiv:0805.4144v1 pp1–2, https://arxiv.org/pdf/0805.4144v1; reuse the precisely inspected calibration comparisons recorded below.
COMPARISON: Primary weak Stokes covers the proposed coefficient regularity and singular homotopy chains; it supplies no saturating form. The ready smooth/global, absolute-domination, scalar-foliation and nonvanishing-volume comparisons do not decide the local one-sided actual-G certificate with free fiber traces.
GAP: Construct a locally Lipschitz weakly closed, everywhere graph-plane-dominated form saturating the whole strip, or prove an exact obstruction. In particular L868's coefficient template and saturation must be justified in this changed local weak class before use; neither existence nor nonexistence is established.
REASON: Step 2026-11-07-weak-local-calibration-source-review-82 resolves the essential weak-Stokes coverage and separately approves one bounded attempt on the unchanged nominated TARGET. This is source progress only; no new mathematical result, certificate or broader stop is asserted.
LITERATURE_REASON: This turn assesses changed locally Lipschitz coefficients, distributional closedness, local domain and full graph saturation, whose essential weak-Stokes framework was missing at invocation start. Ready prior comparisons are reused; no additional literature turn is requested.
SCOPE: Exactly L847 actual G,R,C,F,omega; L879 smooth real periodic stationary u with original J!=0; the conditional clean two-simple-fiber strip and neighborhood-confined radial homotopies specified below. Includes the necessary one-fiber compatibility test, local weak coefficient reduction, saturation and the sufficient compact-chain comparison; no global existence, strong duality or unrestricted competitors.

## Exact proposed problem and remaining obligations

Use L847's actual G,R,C,F,omega and L879's smooth real periodic
stationary graph with original J!=0. Retain the conditional clean
strip S=(l,r)x(c,d), compact in a lifted chart, whose only density
zeros are the complete simple G(z1)-zero fibers alpha,beta. The
other factors G(z2) and z1-z2 are nonzero there. No realization of
this configuration or existence of a minimizer is assumed or proved.

The proposed object is a real locally Lipschitz differential two-form
alpha on some open neighborhood N of Phi_u(closure S) in (C*)^2,
with d alpha=0 in distributions. Require the upper inequality

    alpha_z(E1,E2) <= |omega_z(E1,E2)|,
    (E_j)_k = z_k(A_kj + i delta_kj),

for every z in N and every real 2-by-2 matrix A, retaining both
F=0 and J=0. There is no absolute value on the left, reverse-plane
condition or unrecorded derivative bound. Require saturation
Phi_u^*alpha = |Q| dx wedge dy on S. Locally Lipschitz is a proposed
regularity class, not an established optimal or sufficient one.
The separate review below selects the continuous representative and
the precise weak-Stokes framework. Certificate existence and the
application checks remain obligations of the mathematical attempt;
they do not follow from the earlier C1 theorem.

The intended comparator class consists of smooth real periodic
u_tilde=u+v with v compactly supported in S, endpoint J_tilde!=0,
and the full radial homotopy Phi_(u+t v)(closure S) contained in N.
No invertibility along that homotopy is imposed. The proposed
threshold is B(u_tilde)>=B(u) for every such competitor, justified
by a valid boundary comparison and pointwise domination. No such
inequality is established by this nomination. This would be a local
obstruction only; competitors leaving N would remain unresolved.

Essential local inputs are L847 and L879. L867/L868 are comparisons
whose exact global C1 conclusions cannot silently be extended;
L888 and audited L892 record stopped competitor subclasses, not
premises for the proposed certificate. Do not rely on unaudited
L888–L891 for any new sign. Prior unsigned-kernel/chord stops in
attempt65/69 remain intact. No cross-notebook theorem is requested.

## Purpose and discriminating decision

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. This intermediate target tests whether paired contacts
can resist a whole neighborhood of finite replacements through a
boundary certificate, instead of choosing another shrinking bridge.
It could retire a finite-depinning mechanism at a stated scope or
identify a precise obstruction to its dual certificate. Failure to
find such a certificate would not establish a descent direction.

Continue only if the source review supplies the necessary weak
comparison framework and leaves a concrete certificate construction
or an exact nonexistence test. Import any matching theorem with its
precise hypotheses; do not reprove it as new mathematics. If a known
rigidity or regularity obstruction already excludes this class,
record that source-based stop and choose a different target. A formal
period, a nonsaturating form or an unjustified smoothing does not
meet the test. Graph/minimizer existence, replacements outside N,
other contact types, L868's sharp global bound, higher signs and Xi
transfer remain independent gaps. Mathlib coverage is unchecked.

The preceding problem specification was nominated in step81 without
mathematics. The separate source review below now approves the unchanged
target for one bounded mathematical attempt. It does not approve an
answer to the certificate question.

## Separate source review — 7 November 2026, step82

### Primary weak comparison framework

Ilmari Kangasniemi and Eden Prywes, *On the Moduli of Lipschitz
Homology Classes*, **Journal of Geometric Analysis 35**, article 88
(published 6 February 2025),
[Sections 3.2, 4.2–4.3, Proposition 4.5 and Appendix proof of
Proposition 4.2](https://link.springer.com/article/10.1007/s12220-025-01916-6).
Read the weak-derivative definition, all six properties of Proposition
4.2, the manifold construction and Proposition 4.5, and the complete
Appendix proof of Proposition 4.2, especially its mollification case.

Proposition 4.5 assumes M is a topologically closed Lipschitz
n-submanifold of an oriented Lipschitz Riemannian n-manifold, U is open
in M, a singular Lipschitz k-chain sigma lies in U, and a (k-1)-form
a belongs to W^{d,infinity}_loc(U). It gives
integral_(boundary sigma) a = integral_sigma da. Use n=4, k=3,
M=the ambient X and U=N; M is closed in itself. Locally Lipschitz
coefficients with distributional da=0 meet that Sobolev hypothesis.
The homotopy is a singular chain, requiring no embedding or nonzero J.
Proposition 4.2(1),(4) and its mollification proof provide the interface
with ordinary integrals of the continuous representative; retain that
representative when stating pointwise domination and saturation.
Corollary 7.1 and its following examples instead allow exceptional
chains at finite p, so are insufficient for a prescribed comparison.

This imports an integration theorem, not the desired certificate.
The future application must explicitly identify the oriented boundary
of the compact parameter box, its side faces and all graph integrals.
No assertion that an ambient a.e. derivative identity restricts
pointwise to the three-dimensional homotopy is needed or approved.
Likewise, smoothing used to justify integration does not entitle one
to smooth a candidate while preserving domination or saturation.

Stanislav Dubrovskiy, *Stokes Theorem for Lipschitz forms on a smooth
manifold*, [arXiv:0805.4144v1, 27 May 2008, pp1–2](https://arxiv.org/pdf/0805.4144v1).
Read the entire two-page note. It treats compactly supported Lipschitz
(n-1)-forms on a smooth n-manifold, starts with terms f dg1 wedge ...
wedge dg_(n-1), and passes from Euclidean/half-space charts by partition
of unity. This supports weak-Stokes terminology but is not used to
assert a chain rule for restriction of ambient a.e. derivatives to a
lower-dimensional singular homotopy. Proposition 4.5 above is the
selected source, so no such extra premise is imported from this note.

### Reused calibration coverage and exact differences

Reuse the inspected statements and proof cases in
`2026-11-06-oriented-one-sided-dual-period-test.md` and
`2026-11-07-paired-fiber-finite-replacement-test.md`:

- Lawrence–Yamauchi, *Convex optimization and contour deformations*,
  [arXiv:2311.13002v2, Section III (18)–(20), IV A/C and its contour
  qualification](https://arxiv.org/pdf/2311.13002v2#page=5).
  Its absolute-domination sufficient comparison and generalized-chain
  relaxation give neither a local Lipschitz saturating representative
  nor a necessity/existence theorem for this oriented graph class.
  The cosine two-zero example remains a different density/dimension.
- Harvey–Lawson, *Calibrated geometries*, Acta Math. **148** (1982),
  47–157, [II.3 (3.1), II.4 Definition 4.1 and Theorem 4.2/proof,
  pp56–59](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6313-11511_2006_Article_BF02392726.pdf#page=13).
  Reuse the previous full theorem/proof inspection. Its smooth closed
  Riemannian-comass calibration is given, and the current to be minimized
  is already calibrated. Our degenerate density and restricted ordered
  planes have no supplied identification with that Riemannian problem.
  No local certificate existence follows from this comparison theorem.
- Helein, *Isoperimetric Inequalities and Calibrations*,
  [arXiv:1805.10217v1, Section 1.2 Theorem 1 pp4–5,
  proof Steps 1–5 pp5–9](https://arxiv.org/pdf/1805.10217v1#page=4).
  Reuse the checked scalar one-dimensional-base theorem: its extremal
  foliation, nonnegative velocity Hessian and Legendre-map conditions
  are additional data, absent from this vector graph at a zero divisor.
- Lotay–Pacini, *From Lagrangian to totally real geometry*,
  Communications in Analysis and Geometry **28** (2020),
  [Section 9.1 Lemmas 9.2–9.4, pp666–668](https://archive.intlpress.com/site/pub/files/_fulltext/journals/cag/2020/0028/0003/CAG-2020-0028-0003-a005.pdf#page=60),
  as assessed in `2026-11-06-actual-g-radial-graph-full-phase.md`.
  Their nonzero ambient volume form does not cover the included G-zero
  fibers; their characterization supplies no fixed-boundary graph.

The Harvey–Lawson mirror timed out during a fresh open; the prior
ready theorem assessment above is retained and suffices for that
unchanged comparison. Search excerpts on its coflat variants are
uninspected leads, not imported theorems or obstructions. No essential
source is blocked. Whitney Chapter IX and Federer 4.1.19 are references
identified by Kangasniemi–Prywes, not independently inspected here.
Ball–Currie–Olver's derivative-only null-Lagrangian classification is
also already compared in the one-sided assessment; it supplies no
ambient-variable certificate extension. Mathlib coverage is unchecked.

### Local duplicates, failures and bounded search

Read L867 and L868 through their coefficient and closure arguments;
read L847's graph/homotopy interface, L879's hypotheses and conclusions,
and L888's exact pinned-trace hypotheses and unpaid interface statement.
Read the named attempt65/69 stop records and the step81 route decision.
The supplied overview and DAG suffice for the remaining local scopes;
no sibling notebook, global checkpoint search or cross-notebook input
was used.

L867 uses global absolute domination and cannot exclude the proposed
one-sided class. L868's C1 coefficient equations are a template, not a
ready theorem at Lipschitz regularity on N. L888 requires pinned first
traces, unlike this problem. L887 and audited L892 stop stated bump
and thin-bridge subclasses only. Attempt65's negative kernel sectors
and attempt69's unpaid signed compensation do not decide a local dual
certificate. No stopped construction is rerun or broadened here.

The bounded external search used these queries and close refinements:

- `Stokes theorem Lipschitz differential forms weak exterior derivative flat forms calibration`
- `Stokes theorem Lipschitz forms Goldshtein Dubrovskiy`
- `On the Moduli of Lipschitz Homology Classes pdf Stokes flat forms`
- `calibrations degenerate parametric integrands graph null Lagrangian one sided calibration existence`
- `calibration parametric integrands existence foliation graph`
- `Harvey Lawson calibrated geometries closed forms mass minimizing theorem pdf`
- `locally Lipschitz calibration closed form`
- `calibration degenerate holomorphic contour zeros saturation`
- `locally Lipschitz calibration closed differential form holomorphic`
- `weak calibration graph null Lagrangian`
- `calibration holomorphic zeros contour`

Primary weak-Stokes sources above were inspected. Results about
nonlocal calibrations, uniformly elliptic parametric hypersurface
integrands, Lorentzian calibrations and special-holonomy geometries
were search leads only; none is cited as a theorem here. This search
found no adequate match to the exact local actual-G certificate. It
does not establish originality or imply that a certificate exists.

### Approved bounded test; no mathematical answer this turn

One next mathematical attempt may use L868's pointwise coefficient
calculation as a template, justify the local weak closure system, and
test compatibility of full graph saturation through a simple fiber.
Any one-fiber obstruction must apply to every certificate in the
nominated class to exclude the paired certificate. Conversely a
one-fiber construction alone does not calibrate the whole strip.
If compatibility survives, a proposed certificate must be specified
on an open neighborhood of the whole graph strip, satisfy every
matrix inequality including F=0 and J=0, and justify saturation and
the full boundary comparison. No new coefficient condition,
compatibility result, smoothing construction or mass inequality has
been derived in this source-only step.

Continue on a verified full-strip construction or an informative exact
obstruction; if neither is obtained after the bounded attempt, save
the unresolved compatibility condition and reassess. Do not substitute
an unchanged omega period, presume dual attainment, assume a minimizer,
or revive the same shrinking bridge. Existence of the nominated actual
graph, competitors leaving N, other contacts, the global sharp bound,
higher signs and Xi transfer remain independent gaps. The TARGET is
unchanged, and this separate literature gate approves its first attempt.
