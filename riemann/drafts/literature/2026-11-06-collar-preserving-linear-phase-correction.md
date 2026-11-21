# Collar-preserving linear phase correction — completed source comparison

TARGET: Determine whether there exist an L849(18) cutoff torus u and a smooth real exchange-equivariant v vanishing on a smaller diagonal collar such that D(Im q)_u[v]=-Im q_u on T^2.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact-Xi/linearized-contour, relative phase, support-preserving divergence, real degenerate-volume and holomorphic-Moser searches completed; reused the full-phase/collar comparisons and searched named local source/history/failure paths. No adequate matching theorem located; queries and scope below, with no novelty inference.
SOURCE_EVIDENCE: Read Guillemin–Sternberg (2010 manuscript) Section13.13 (13.7)–(13.9) and Section13.14–13.14.1 pp449–455; Teixeira 1608.06213v7 Sections2.2–4, Theorems2/3 with proofs pp6–10 and Theorem1 p2; Teixeira 1705.01416v1 Theorem1/Remark1/Lemmas1–2 with proofs pp2–4; Soldatenkov–Verbitsky 2109.00935v2 Definition2.1/Lemma2.4/Theorem2.5 with proofs pp3,5–6; Volk–Khesin (2026) Definition1.1/Theorem1.2/Corollary1.4 and Section3 proof, including relative support construction. Full citations below.
COMPARISON: Pullback differentiation is available without nonvanishing. Teixeira's linear theorem solves ordinary divergence with collar support and zero integral, not the uncomputed graph operator. Real same-sign transport, real Morse-Bott equivalence and nondegenerate holomorphic isotopy do not decide this complex full-form equation with constrained variations. Existing product/averaged-extension stops remain narrower.
GAP: Determine the range of the actual linearized full pullback under real radial, collar-vanishing, periodic exchange-equivariant variations, including every zero and degeneracy, with a permitted choice of L849 cutoff. No inspected theorem supplies that reduction, solvability or obstruction; this is the bounded mathematical task, not an unread essential theorem.
REASON: Essential source comparison is complete for one unchanged-target bounded attempt under EXPLORE. Import standard differentiation or divergence results only after checking the exact application hypotheses; do not reprove them or substitute an unconstrained Moser flow. Newly ready coverage awaits separate next-turn approval; no mathematics is invoked in this literature turn.
LITERATURE_REASON: The invocation-start target added relative support and linear-range constraints beyond the retained full-phase assessment; the supplied REVIEW_REQUIRED nomination required this separate comparison before any calculation.
SCOPE: Actual G,R,C and full oriented r=2,k=1 form of L847; exactly L848 h,b and L849(18)'s even cutoff family with 0<a<b_0<epsilon_0; real smooth periodic exchange-equivariant variations vanishing on an open smaller diagonal collar; all density zeros and possible complex-Jacobian degeneracies retained. Covers deriving the full linear operator and a bounded existence/range test for TARGET, without assuming ellipticity, invertibility, nonvanishing or any effective collar width. No nonlinear correction or global nonnegativity theorem is included.

## Completed comparison, 6 November 2026

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. TARGET is one intermediate feasibility test for a later
global phase correction preserving the accepted positive collar. Even
success would leave nonlinear convergence, global sign, other
orders/shifts and positivity transfer unresolved. This review completes
source coverage; it establishes no new lemma, operator identity, range
condition or sign statement.

### Local scope and duplicate/failure checks

Used the supplied complete overview/DAG before loading the needed proofs.
Read L847's hypotheses, conclusions and graph/pullback/homotopy argument
(1)–(5); L848's hypotheses and (3)–(7); L849's hypotheses/conclusion and
the complete collar/cutoff construction around (18). These reads identify
the object and permitted family, rather than re-audit the accepted proofs.
The residual is the imaginary part of the scalar density in the original
dt wedge ds orientation, with the full Jacobian from L847(3). The target
does not use a logarithmic phase defined only away from zeros.

Reused `2026-11-06-actual-g-radial-graph-full-phase.md` and
`2026-11-06-exact-collar-construction-audit.md`. Targeted searches for
relative deformation, linearization, divergence, Moser, collar and L849
in the named 6 November assessments/histories/failures, and for the new
source names in those source notes and `foundations/notation-and-inputs.md`,
located no prior solution of this relative linear problem. Read
`ATTEMPTS/2026-11-06-actual-g-product-radial-graph-stop.md` and
`ATTEMPTS/2026-11-06-exchange-diagonal-averaged-extension-stop.md`.
Independent product curves and that particular averaged extension remain
excluded at their recorded scope. They do not decide the nominated
coupled first variation. Chaperon's scalar theorem covers the accepted
local branch, not a global relative range problem. No historical stop is
promoted to a global ban.

### Primary sources inspected

**General pullback differentiation.** Victor Guillemin and Shlomo
Sternberg, *Semi-classical analysis*, manuscript dated 13 January 2010,
[Section13.13, (13.7)–(13.9), pp449–452; Section13.14–13.14.1,
pp453–455](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf#page=449).
Read the statement and proof for smooth parameter-dependent maps
between differentiable manifolds and smooth parameter-dependent forms,
including the vector field **along** the map and its contracted pullback.
This formula needs neither a nonzero form nor a diffeomorphic map.
It is a standard input for the later differentiation, imported without
reproof; its actual graph specialization is deliberately not performed
here. The following Moser argument separately needs a solvable vector-field
equation and sufficient flow existence. Its volume-form example uses
nowhere-vanishing real top forms on a compact connected oriented manifold
with equal integrals. It does not supply the constrained variation in
TARGET. Smoothness is furnished by L849 for each admissible cutoff;
no global logarithm, division by a density or flow theorem is needed
merely to use the differentiation identity.

**Support-preserving linear divergence.** Pedro Teixeira,
*Dacorogna–Moser theorem on the Jacobian determinant equation with
control of support*, DCDS **37** (2017), 4071–4089, DOI
10.3934/dcds.2017173; inspected
[arXiv:1608.06213v7, 5 August 2018, Section4 Theorem3/Remark3
and proof, pp8–10](https://arxiv.org/pdf/1608.06213v7#page=8).
For n>=2, a bounded connected smooth open Omega in R^n, its collar U,
integer r>=0, 0<alpha<1 and real h in C^(r,alpha) on the closure,
integral h=0 and h=0 on U give a vector field w in C^(r+1,alpha)
with div w=h and w=0 on U. The linear solution operator is independent
of the regularity indices, hence preserves smooth data; its bound depends
on r,alpha,U,Omega. Read also Section2.2's boundary convention and
Theorem2/proof used in its divergence-free extension. The signed linear
datum h need not be positive. Theorem1's nonlinear determinant datum
does require positivity. These are known tools, not results to reprove.
No reduction from TARGET to this unrestricted ordinary divergence equation
has been established. Graph coefficients, topology, support, symmetry
and zero-locus compatibility remain application obligations.

**Relative transport between real densities.** Pedro Teixeira,
*Addendum to: “Dacorogna–Moser theorem on the Jacobian determinant
equation with control of support”*,
[arXiv:1705.01416v1, 2 May 2017, Theorem1/Remark1, Lemmas1–2
and proofs, pp2–4](https://arxiv.org/pdf/1705.01416v1#page=2).
For a bounded connected open Omega, integer r>=0 and 0<alpha<1,
real C^(r,alpha) densities f,g on the closure with fg>0, equal integrals
and supp(f-g) contained in Omega admit a C^(r+1,alpha) pullback
diffeomorphism supported in Omega. Lemma1 fixes a neighborhood of a
prescribed collar where the data agree. The proof first solves on a
smaller domain and extends by identity; Lemma2 checks agreement by
composition. Remark1 allows rougher data outside the active subdomain,
but retains same-sign nondegeneracy on it. Thus the fixed collision zero
alone is not a universal objection to an argument supported elsewhere.
However the required pair of real same-sign densities and a reduction to
the permitted real radial variations have not been supplied. This source
does not identify the range of our complex-density linearization.

**Holomorphic Moser comparison.** Andrey Soldatenkov and Misha Verbitsky,
*The Moser isotopy for holomorphic symplectic and C-symplectic structures*,
[arXiv:2109.00935v2, header 2 October 2021, internal version1.1
dated 5 October; Definition2.1 p3, Lemma2.4/Theorem2.5 and proofs
pp5–6](https://arxiv.org/pdf/2109.00935v2#page=3).
A C-symplectic form on a real 4n-manifold is closed, has (n+1)st
power zero and has nonzero Omega^n wedge conjugate(Omega)^n everywhere.
Lemma2.4 requires type-(1,0) primitives of the parameter derivatives;
its proof inverts contraction with a nondegenerate holomorphic symplectic
form. Theorem2.5 obtains vector fields under constant de Rham class
and H^1(X_t,O_X_t)=0; compactness supplies the full flow. Read its
noncompact qualification too. This neither covers the full ambient
vanishing form in L847 nor imposes our support/graph/symmetry conditions.
It gives no permission to delete the divisor. Only the preprint version
was inspected: the 2025 AIF PDF endpoint returned403, so no version
identity or published-text verification is claimed. The preprint supplies
the needed hypothesis comparison; there is no essential access blocker.

**Zeros do not by themselves prohibit Moser arguments.** Luke Volk and
Boris Khesin, *Morse-Bott Volume Forms*, Arnold Mathematical Journal
**12**(1) (2026), DOI10.56994/ARMJ.012.001.005,
[Definition1.1, Theorem1.2, Corollary1.4 and Section3's complete
Theorem1.2 proof](https://armj.math.stonybrook.edu/Articles/250611-Khesin/index.html).
On a compact connected oriented n-manifold with an oriented common zero
submanifold Gamma, their Morse-Bott forms are smooth **real nonnegative**
top forms whose ratios to a reference volume have nondegenerate critical
minima along Gamma. Equality in H^n(M,Gamma) gives diffeomorphism
equivalence fixing Gamma. In codimension one, Corollary1.4 requires
equal volumes on each complementary component. The proof first matches
forms near Gamma, then uses a primitive vanishing on a smaller tubular
neighborhood for the complementary correction. The global reality,
nonnegativity and prescribed whole zero set required here are not known
for our cutoff graph; the theorem also does not restrict deformations
to our radial graphs. It is not an import for TARGET. Its relative
construction is useful comparison evidence, not a proof of a new
range condition. The transverse-zero Cardona–Miranda paper cited there
is an unread historical lead; no conclusion from it is used.

### Search record and bounded coverage decision

Queries included the following exact phrases and standard terminology:

- `"holomorphic volume form" "linearization" "totally real"`;
- `"relative" "Moser" "volume forms" "vanishing"`;
- `Dacorogna Moser theorem control support Teixeira 2017 divergence compact support`;
- `"Dacorogna-Moser" "control of support" Teixeira arxiv`;
- `"special totally real" deformation linearisation`;
- `"holomorphic volume" "Moser" zeros deformation`;
- `"linearized" "perfect contour"`;
- `"special totally real" "deformations" Pacini persistence`;
- `"holomorphic volume form" "linearisation" deformation submanifolds`;
- `"Moser" "volume forms with zeros"`;
- `"Moser isotopy for holomorphic symplectic" arxiv`;
- `"perfect contours" "linear" "zeros"`;
- `"phase" "radial graph" "Moser"`;
- `"Riemann Xi" "linearized" contour`;
- `"relative" "phase" "holomorphic volume form" deformation`;
- `"volume forms" "zeros" "Moser" theorem singular`.

Search hits returning the previously assessed Lawrence–Yamauchi and
Lotay–Pacini sources are covered by the retained full-phase assessment;
they were not re-imported as new existence results. Thesis, aggregator,
unrelated purported-RH and unrelated symplectic-packing hits supplied no
theorem evidence. The inspected primary statements and essential proof
cases above, rather than snippets, support the method comparison.
No adequate match for the exact actual-G, fixed-cutoff-family linear
range target was located in this bounded search. That is not a novelty
claim or a claim that no such theorem exists.

The decision is EXPLORE, not IMPORT: standard differentiation and
relative divergence are available, while the essential difference is
precisely the actual constrained range problem. A later attempt may
derive the full operator and test it directly, or check a reduction to
a cited tool. It may not assume that zero total integral suffices, that
the contraction map is invertible, or that a formal flow preserves the
graph. No new theorem asserting these properties was derived here.
No further essential source coverage is missing for that bounded test.
Full matching Mathlib coverage remains unchecked; none of these source
comparisons is represented as a Mathlib formalization. No cross-notebook
input, numerical certificate or mathematical script was used.

### Continuation and stopping test

After separate next-turn approval of this newly ready assessment,
undertake exactly TARGET. Preserve its existential choice of an
L849(18) cutoff and its support requirement. Success needs an actual
admissible smooth real v, with periodicity, exchange equivariance,
vanishing on an open smaller collar, and the equation checked on the
entire torus. An obstruction must specify whether it covers one chosen
cutoff, a subclass or all permitted cutoffs. Failure for one cutoff
does not refute the existential target. Merely deriving an operator or
checking an integral is not a solution. If neither solution nor an
informative scoped obstruction is obtained, save the unresolved range
condition and reassess the mechanism before repetition.

Essential inputs are L847's exact full form/graph/homotopy, L848's
prescribed h,b/sector/K and accepted L849's branch/cutoff, retaining
L018/L775 actual G,R,C and L778(2)–(5)/step433 analytic/software
qualifications. No new nonvanishing or effective width is assumed.
Nonlinear convergence, global reality and nonnegativity, other
orders/shifts, mixed-positivity transfer and RH remain independent gaps.

The proposed research routing is proof_attempt/creative,
deep_research/max: the obstruction is whether this actual residual
belongs to the support-restricted real graph range through its retained
zeros and degeneracies. A solution or scoped obstruction is the bounded
decisive evidence. This is a new complementary-phase mechanism after the
local collar audit, not another local audit or the stopped averaged
extension. This literature turn makes no mathematical attempt and
changes no lemma, mathematical script, DAG edge or PROOF argument.

## Original nomination — preserved as the pre-comparison record

The sections below record the initial REVIEW_REQUIRED nomination.
Their missing-coverage descriptions are historical; the completed
comparison above supplies the source readiness and its precise limits.

## Proposed bounded target and its relevance

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. The completed L849 audit accepts a local exact positive
collar. The proposed next mechanism tries to correct the phase of a
global graph while preserving that local construction. A successful
first linear correction would supply one concrete feasibility input
for a later nonlinear global-reality attempt. Nonlinear convergence,
regularity estimates, global nonnegativity, other orders/shifts and
transfer to all-degree positivity would still be separate gaps.

The operator in TARGET is defined, not evaluated here, by

\[
 D(\operatorname{Im}q)_u[v]
 :=\left.\frac{d}{d\tau}\right|_{\tau=0}
          \operatorname{Im}q_{u+\tau v},\qquad \tau\in\mathbb R,
\]

using L847's full pullback, not a logarithmic phase after
deleting its zeros. The existence quantifier permits a choice among
L849's legitimate cutoff widths. A positive result must specify that
choice and v, prove smoothness, periodicity and v_2(t,s)=v_1(s,t), and
verify the displayed equation everywhere. The perturbation must vanish
identically on an open diagonal collar contained in L849's positive
one. An explicit nonzero range obstruction would be informative, but
must state whether it applies to one chosen cutoff, a subclass, or
every admissible cutoff. Failure of an estimate or one cutoff alone
does not refute the existential target or other coupled graphs.

This nomination derives no operator formula, range condition or
solvability claim. A first correction does not itself give exact reality
of q_(u+v), nonnegativity, or a convergent correction sequence. The
independent nonlinear and sign gaps must remain explicit.

## Required source comparison and continuation

Reuse `2026-11-06-actual-g-radial-graph-full-phase.md` and
`2026-11-06-exact-collar-construction-audit.md`. Check exact terminology,
stronger results and local duplicates for relative volume/phase
deformation, support-preserving transport and linearized graph
equations. Retrieve primary theorem hypotheses and essential proof
cases before using any general Moser-type argument. In particular,
check whether its nonvanishing, boundary/support, cohomology, graph
or regularity assumptions hold here; none is supplied by the nomination.
Do not repeat a global normalizing-flow existence claim already marked
conditional in the full-phase assessment.

Essential local inputs are L847's full form and graph class, L848's
exact prescribed data and qualified sector input, and accepted L849's
implicit branch and cutoff. L018/L775 fix actual G,R,C, and
L778(2)–(5)/step433 numerical/software qualifications remain inherited.
No cross-notebook input. Full matching Mathlib coverage is unchecked.

If adequate coverage is obtained, the intended later research purpose
is proof_attempt/creative, deep_research/max: the precise obstruction
is whether the retained zero divisor and real graph/support constraints
permit this residual to lie in the linearized phase range. This matters
because the local collar alone leaves all complementary phase error
uncontrolled. The bounded decisive test is an actual admissible solution
of the linear equation or a proved scoped range obstruction, with no
nonlinear or positivity inference. This is a routing proposal for a
later research turn; the immediate next task is literature_comparison.
