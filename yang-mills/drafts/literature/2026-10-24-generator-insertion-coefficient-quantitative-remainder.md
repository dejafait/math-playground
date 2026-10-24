# Generator insertion coefficient remainder — source comparison

TARGET: Determine whether |V_N-a^(-3)K_(i,V)| <= C_i N^(5/2)log(eN)^2 holds for both actual probes, with V_N from L119 and K_(i,V) from L120.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched the 2026-10-20--24 local assessments and histories/427--435 for V_N, K_(i,V), generator insertion and displacement; read the original L120 draft/history and ATTEMPTS/030/032. Six bounded external queries listed below supplied no inspected matching rate theorem. The ready parent and L268 assessments are reused, not counted as fresh discovery.
SOURCE_EVIDENCE: Reused inspected Lawler--Limic (2010), section 1.1 pp. 9--11, Theorem 4.3.1 pp. 81--83 including the bipartite case, Corollary 4.3.3 p. 84, Proposition 4.6.2(a) p. 97 and Theorem 6.3.8 p. 131, and NIST DLMF v1.2.8 section 1.4(vi), (1.4.35)--(1.4.37). Read full L120 and L114; L119's insertion/tail/trace ranges; L267's matrix/scalar-source ranges; L248 sections 1--2 and raw/probe audit cases; L222's mode and quadrature ranges. Primary versions and precise applicability limits follow.
COMPARISON: L267 supplies full joint energy decay; L114 supplies a fixed-clearance localized projection estimate; L248 supplies quantitative raw interior forest samples and both complete heat matrices. These are usable standard inputs for quantifying L120, but no source or local theorem inspected states this exact coefficient remainder. L268's separate reduction is not the requested comparison.
GAP: Quantify L120's joint spatial/axial tails, finite-projection replacement, remote-row coefficient differences and physical quadrature against exactly (3), with uniform parameter dependence before selecting cutoffs and before the complete heat sum.
REASON: Essential scalar, calculus and canonical local coverage is accessible and sufficient for one later RESEARCH / REPRODUCTION specialization on the unchanged target; no essential unread source blocks that attempt. This approval establishes no new bound and does not audit upstream premises.
SCOPE: Relative SU(2) cube, sufficiently fine admitted even N, a=8/N, tau=1/16, lower-rooted direction-1 forest, stored coordinates, bare-first expansion, both actual probes and residual forms, original output derivative and every stencil shift, finite middle projection, min(s,t), both coefficient levels, full source/output/end rows, upper jump, constant modes and complete heat sums; all upstream qualifications remain.
LITERATURE_REASON: The saved independent insertion-to-coefficient target was REVIEW_REQUIRED at invocation start and was expressly excluded from the completed L268 audit; this separate review assesses its changed projection, tail and raw-coefficient obligations while reusing ready primary coverage.

## Relevance and exact comparison

The main gap remains interacting continuum construction, a nonzero
physical sector, the required axioms and finite positive infinite-volume
mass. This comparison could complete the generator-displacement component
rate when combined with the accepted L268 reduction. Three independent
transverse-H coefficient remainders, quantitative L011 assembly and the
construction remain unresolved. No comparison bound is derived here;
only the scope of a later mathematical attempt is approved.

The exact finite object is L119(3), with v at its original output
and Z=F_l(s)^T P F_k(t). The subtraction is exactly L120(3), whose
tensor pairs B_(r,j,m)(d) with q_(alpha,beta)(-d), and whose physical
weight is x_1+4. This is distinct from L179's K_(i,Vmix).
L120 proof sections 1--5 were read completely. Its (9) is a projection
comparison after fixed spatial/axial truncation; (11) is the ordered
kernel formula, (12)--(13) handles the actual lower prefix and min(s,t),
and (14) controls joint tensor tails by spatial Cauchy--Schwarz.
Its successive fixed-cutoff limits do not provide a finite-N rate.

The original REVIEW_REQUIRED handoff is preserved in history/435.
This review changes coverage, not L120's theorem or the main argument.
No lemma, mathematical script, DAG or PROOF change is made.

## Reused primary results and their hypotheses

Lawler--Limic, *Random Walk: A Modern Introduction* (Cambridge, 2010),
[author-hosted 289-page text](https://www.math.uchicago.edu/~lawler/srwbook.pdf):
reuse the inspected statements and proof cases recorded in
`2026-10-23-transverse-h-quantitative-remainder.md` and
`2026-10-17-e-static-trace-continuum-rate.md`. Section 1.1 and
Theorem 4.3.1 cover symmetric finite-range irreducible walks, d>=3,
including nearest-neighbor bipartite walks. The continuum Green
leading term has a uniform O(|x|^(-d)) scalar remainder. Corollary
4.3.3 covers first and repeated-coordinate second differences;
arbitrary mixed differences are not attributed to that corollary.
Proposition 4.6.2(a) gives the transient killed-Green exit identity.
Theorem 6.3.8 controls bounded-step differences of harmonic functions
in a buffered ball by its radius and the function's supremum.

Four-dimensional nearest-neighbor walk meets the hypotheses, and
L267's already audited matrix specialization retains H=G_walk/8
for L_4=8(I-P_walk). Its full shifted Frobenius estimate, rather than
a differentiated scalar remainder, is the proposed energy input.
Three-dimensional scalar vertex uses, if needed, must retain the
different normalization Delta_0=6(I-P_walk). L114's relative-domain
identities and L120's q definition supply the local projection
geometry. No source theorem identifies every relative link component
with scalar killed Green or gives the full variable-coefficient trace.
Import the named scalar theorems if used; do not reprove them or
differentiate their asymptotic error. Their prior primary inspections
are reused here; no fresh book retrieval is claimed.

NIST, [DLMF 1.4(vi)](https://dlmf.nist.gov/1.4#vi), version 1.2.8,
released 2026-09-15, (1.4.35)--(1.4.37): reuse the inspected integral
and Lagrange Taylor remainders from the L268 production/audit coverage.
The C^(n+1) closed-interval hypothesis holds for the prescribed smooth
displacement and trigonometric relative modes. L222's quantitative
mode and rectangle-quadrature results and L248's unaveraged-link
specialization already apply this calculus with explicit bounds.
They do not make a rough projection or forest kernel smooth. Further
reproof of Taylor's theorem is unnecessary; applying the existing
estimates in this different trace is the required specialization.

Reuse Adams--Lee, [0709.0781v3](https://arxiv.org/pdf/0709.0781v3),
section II pp. 5--7 and Appendix A pp. 19--23, (A1), (A11)--(A18),
as assessed in `2026-10-17-complete-coefficient-quantitative-remainder.md`.
Its four-dimensional translation-invariant Brillouin integrals,
smooth scaled data, infrared finiteness and negative lattice degree
have not been matched to this pinned trace with variable coefficients
and full heat sum. Its rate is not an import for the current target.
The same assessment records proof-region and parameter restrictions.

The parent assessment's Del Debbio--Patella--Rago
[1306.1173v1](https://arxiv.org/pdf/1306.1173v1), section 6,
(6.1)--(6.16), and Luescher--Weisz
[1101.0963v2](https://arxiv.org/pdf/1101.0963v2), sections 7.2--7.4/8.2,
remain exclusions: renormalized flowed Ward identities do not assign
an isolated bare forest component its rate. Their inspected primary
coverage is reused without fresh proof reading. Gurevich
[1504.02673v2](https://arxiv.org/pdf/1504.02673v2), Conditions 2.1--2.3
and Theorem 3.1, is only the previously assessed whole-lattice,
constant-coefficient parabolic lead; it is not imported and its
remaining proof remains unread. No essential source is inaccessible.

The official Jaffe--Witten 14-page
[Clay PDF](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)
was reopened on 2026-10-24: section 4, printed p. 6 retains the
continuum axiomatic target and finite positive mass; footnote 2,
p. 12 retains the compactness qualification. The target version and
the existing construction-gap interpretation are unchanged.

## Local applicability and unproved rate obligations

| Existing input inspected | Permitted use and limitation |
| --- | --- |
| L119(2)--(6), (13)--(16) | Exact insertion, full trace/heat count and uniform kernel truncation. Its qualitative Theta(J0,R) is not already a quantitative schedule. |
| L267(1), scalar proof sections 1--3 | Full-matrix energy decay at all signed offsets, finite shifts and small arguments. Its different compression conclusion is not this coefficient comparison. |
| Full L114, especially (2), (4)--(5) and proof sections 2--4 | Projection Hilbert--Schmidt comparison on rows of fixed physical clearance, with every boundary input retained. A growing truncation must preserve that clearance with constants uniform in N. |
| L120(8)--(14) | Exact finite/bulk projection order, q geometry, two original levels, lower prefix and a^4 normalization. Its fixed-offset argument must be quantitatively replaced, not invoked at varying cutoffs. |
| L248 proof sections 1--2, (3)--(11), raw/probe audit cases | Uniform raw interior link values and polynomial mode errors, both complete heat matrices, constant axial prefix and original traversal signs. These supporting estimates match L120(2),(12); the reverse-trace conclusion does not transfer. |
| L222(2)--(5) | Quantitative smooth-mode dispersion/derivatives, smooth coefficient consistency and compact rectangle quadrature. Its diagnostic conclusion is a different result. |

L248's raw values match V_mu+V_nu and V_nu-V_mu on the actual
four traversal slots; L120's phi labels use those same signed b,q
combinations. Both probe matrices have the same L080 normalization.
This permits their supporting estimates, including the Gaussian
polynomial error envelope and omitted mesh labels, to be reused after
locality is justified. The independent value bound must accompany
the error bound for high modes. Neither endpoint-averaged diagnostic
values nor the reverse-trace density replace L120's raw exterior.

L248 covers compact interior samples and fixed stencil enlargements.
L119's untruncated B has noncompact input. Thus remote input rows
must first be estimated or separated; their forest prefixes cannot
be silently extended across the upper pin. Likewise L114 restricts
projection output rows only, after cyclicity supplies the correct
adjacent compact rows. Its proof includes every projection input.

The bounded test is to quantify L120's existing joint truncation and
coefficient comparison, retaining uniform dependence on each cutoff.
One may test a spatial/axial near/far separation using L267 and
L120's joint B,q pairing, then L114 on the adjacent interior rows,
and L248/L222 for the remaining raw/heat matching and quadrature.
This is a proposed mechanism, not a new tail, moment or rate estimate.
Every finite-stencil shift, coefficient at t-j and x-d, min(s,t),
missing lower half-line and end strip must remain until bounded.
The derivative stays at L119's original output. There is no outside
a^(-1) in V_N and no other/other outside factor 3 in K_(i,V).

## Search, duplicates and failures

Fresh bounded queries on 2026-10-24 were:

- `"lattice" "Green function" "trace" "variable coefficients" asymptotic remainder`
- `"lattice" "Helmholtz projection" "boundary" Green function estimates`
- `"gradient flow" "translation Ward identities" lattice 1306.1173`
- `"lattice" "trace asymptotics" "projection" "Green"`
- `"lattice Green" "first moment" "projection"`
- `"Dirichlet" "lattice" "variable coefficients" "trace" asymptotics remainder`

They returned the already assessed flowed-Ward paper and continuum
spectral/PDE or projector leads. No new matching primary theorem was
inspected; search excerpts and third-party pages are not theorem
inputs. No novelty or global absence is inferred from these searches.

The original L120 draft and history/146 prove only the qualitative
limit. The scoped 2026-10-20--24 searches distinguish K_(i,Vmix),
L267's compression rate and L268's first-order reduction from this
coefficient rate. No duplicate quantitative comparison was found in
those records. All unfinished work is preserved.

L109 and ATTEMPTS/032 rule out separate first absolute moments of
the projected alternating factor; they do not prohibit a joint
quadratic or closed-trace estimate. ATTEMPTS/030 stops substituting
varying parameters into a fixed-mass qualitative theorem. These
obstructions remain evidence, not a global ban on a new uniform
finite estimate. No rough-column smoothness, compact moved output,
deleted low mode or small projection operator norm is approved.

## Continuation decision

Approve one subsequent proof_attempt / REPRODUCTION turn under
SPECIALIZE for exactly TARGET. Essential inputs are L119 L120 L267,
with L028 L080 L088 L111 L113 L114 L222 L248 for the stated
conventions and quantitative support. L268 is the downstream assembly
input only; it is not a premise proving this independent rate.
Every upstream analytic and audit qualification remains unresolved.
No cross-notebook result is used.

Continue if the complete finite comparison with exactly L120(3)
has all projection, tail, coefficient, quadrature and heat allowances
within C_i N^(5/2)log(eN)^2. Isolate or reassess any above-budget
term, lost-clearance estimate, uncontrolled remote row or nonsummable
mode envelope. Such an upper-bound failure is not signed growth.
Newly essential uncovered mathematics requires review before its
dependent derivation. Two unproductive attempts require reassessment.

This completed step is LITERATURE / NOVELTY_UNCHECKED, outcome
EXPLORATION: new exact-target coverage is ready, but no rate theorem
is imported or proved. Mathematical exploration usage remains zero.
The unchanged exact target needs no additional coverage-only turn.
Full matching and supporting Mathlib coverage are **not checked**;
unknown availability is not absence.
