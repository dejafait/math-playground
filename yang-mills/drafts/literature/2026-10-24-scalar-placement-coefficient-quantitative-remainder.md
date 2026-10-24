# Scalar-placement coefficient remainder — source comparison

TARGET: Determine whether |Delta_sc-a^(-3)K_(i,sc)| <= C_i N^(5/2)log(eN)^2 holds for both actual probes, with Delta_sc and K_(i,sc) exactly as in L121.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read full L121 and L113, L114's statement and projection proof, L267's full-matrix scalar specialization, L248's raw-link/prefix/probe ranges and L222's calculus/modal/quadrature ranges; searched the scoped 2026-10-10/17/20--24 assessments and histories/430--439 for scalar-placement duplicates. Five fresh external queries are recorded below; no inspected matching remainder theorem was located.
SOURCE_EVIDENCE: Reuse Lawler--Limic (2010), section 1.1 pp. 9--11, Theorem 4.3.1 pp. 81--83 including the bipartite proof case, and Proposition 4.2.3 p. 79 through the recorded L267 production/audit coverage; freshly read NIST DLMF v1.2.8 section 1.4(vi), (1.4.35)--(1.4.37), including its closed-interval smoothness hypothesis. Reuse the primary exclusions documented in the generator coefficient and complete-coefficient assessments.
COMPARISON: L121 already places its finite-projection error within the requested budget, but proves only qualitative joint-tail removal and fixed-offset derivative matching. L267 supplies usable shifted energy-kernel decay and L222/L248 quantitative smooth-mode support; no source or L269 statement supplies this complete scalar-placement rate.
GAP: Quantify L121(11)'s complete closed scalar difference against exactly L121(3), including joint spatial/axial tails, finite component restrictions, transverse derivatives of the actual raw paths, separate levels, min(s,t), quadrature and the complete heat sum.
REASON: Essential source ingredients are accessible and assessed; the remaining work is a different quantitative specialization of known Green/Fourier/calculus methods. Approve one subsequent bounded proof attempt on TARGET, without asserting the rate or originality.
SCOPE: Relative SU(2) cube, sufficiently fine even N, a=8/N, tau=1/16, lower-rooted forest, stored coordinates, bare-first order, probes i=3,6, both Q forms, both original coefficient levels, original finite P, all shifted path/component stencils, min(s,t), upper jump, all rows, constant modes and complete heat sums; all imported audit qualifications remain.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED coverage concerned a changed scalar-placement rate, outside the ready generator-insertion target; the full L121 derivative/commutator obligations had not yet been compared with the reusable sources.

## Relevance and threshold

The main gap is still an interacting continuum construction with a
nonzero physical sector, the required axioms and finite positive mass.
The official Jaffe--Witten 14-page Clay statement, section 4 p. 6 and
footnote 2 p. 12, was rechecked in the 2026-10-24 generator-coefficient
source review; that version and route scope are reused unchanged.

This one intermediate target could fill the scalar-placement part of
the quantitative transverse-H remainder and later L011 assembly.
The exterior-circulation and energy-placement rates, full quantitative
assembly and all construction requirements remain independent gaps.
A successful comparison is local standard-method progress, not a new
Yang--Mills construction or a claim beyond the checked literature.

## Primary inputs, hypotheses and exclusions

Lawler--Limic, *Random Walk: A Modern Introduction* (Cambridge, 2010),
[author-hosted 289-page text](https://www.math.uchicago.edu/~lawler/srwbook.pdf):
reuse primary inspections recorded in
`2026-10-23-transverse-h-quantitative-remainder.md` and
`2026-10-24-generator-insertion-coefficient-quantitative-remainder.md`,
and the audit comparison in
`2026-10-24-generator-insertion-coefficient-rate-critical-audit.md`.
Section 1.1 and Theorem 4.3.1 cover symmetric finite-range irreducible
walks in dimension at least three, with the bipartite case explicitly
retained. Theorem 4.3.1 gives the continuum Green leading term and
uniform O(|X|^(-d)) remainder. Proposition 4.2.3 supplies the transient
Fourier Green representation with its periodicity qualification.
Four-dimensional nearest-neighbor walk has covariance I/4 and
L_4=8(I-P_walk), hence L267 uses H=G_walk/8. These named scalar
results are citation imports, not proposed reproofs.

L267's full shifted Frobenius bound (1) is the local matrix input;
its proof handles mixed differences by bounding the scalar remainder
at each shifted argument, not differentiating that remainder. Its
compression conclusion is a different result. No primary scalar
statement identifies the whole pinned variable-coefficient trace or
provides the new scalar-placement rate. The projection kernel here
is L114's three-dimensional gradient projection, not the circulated
four-dimensional covariance. L121's joint pairing keeps that distinction.
No extra pointwise projection-kernel theorem is required by the proposed
ell2-pairing test; if a later approach needs one, assess it first.

NIST [DLMF 1.4(vi)](https://dlmf.nist.gov/1.4#vi), version 1.2.8,
released 2026-09-15, (1.4.35)--(1.4.37), was freshly inspected.
Taylor's polynomial, Lagrange and integral remainders require
f in C^(n+1)[a,b]. Their intended use is on the fixed smooth
displacement and trigonometric modal/prefix coefficient expressions
on interior closed segments. The source does not make a clamped
coefficient smooth across a face or a forest lift smooth through its
upper pin. Taylor's theorem itself needs no reproof. Its specialization
to differentiated raw path coefficients with uniform polynomial mode
bounds is part of the later research obligation, not completed here.

Reuse the inspected Adams--Lee [0709.0781v3](https://arxiv.org/pdf/0709.0781v3),
section II pp. 5--7 and Appendix A pp. 19--23, (A1), (A11)--(A18),
comparison in `2026-10-17-complete-coefficient-quantitative-remainder.md`.
Its translation-invariant four-dimensional Brillouin integrals require
smooth scaled data, the stated denominator growth/zero conditions,
infrared finiteness and negative lattice degree. Those hypotheses have
not been matched to this pinned variable-coefficient full-heat trace.
The source's integral remainder is not an import for TARGET.

Reuse Del Debbio--Patella--Rago
[1306.1173v1](https://arxiv.org/pdf/1306.1173v1), section 6,
(6.1)--(6.16), and Luescher--Weisz
[1101.0963v2](https://arxiv.org/pdf/1101.0963v2), sections 7.2--7.4/8.2,
as assessed in the parent and generator-coefficient source comparisons.
Renormalized flowed Ward finiteness does not give the rate of this
isolated bare forest block. Their prior primary inspections are reused;
no fresh proof retrieval is claimed. Gurevich 1504.02673v2 remains an
unused whole-lattice constant-coefficient parabolic lead; its previously
unread proof portions remain unread and nonessential. No essential
source is blocked. No cross-notebook theorem is used.

## Local proof obligations and permitted specialization

Full L121 fixes the original difference and coefficient, including
its exact finite selectors H_N and scalar difference L in (10)--(11).
Its two path-placement errors and scalar projection commutator are
combined before expansion. The later attempt must retain that identity.

| Inspected input | Available conclusion and remaining obligation |
| --- | --- |
| L113(3)--(6), proof sections 1--4 | Clamped global Lipschitz/value bounds and the actual finite scalar commutator bound; not a small projection operator norm or a quantitative coefficient limit. |
| L121 proof section 2, L114(2)--(5) and its proof | The finite-to-bulk projection replacement already has O(N^(5/2)(log N)^(3/4)) allowance. The selector is on projection-adjacent output rows and retains every input; this comparison is not to be silently repeated or transferred to a different order. |
| L121(10)--(15), L267(1) and its mixed-shift proof | Exact complete scalar difference, joint energy/projection majorant and summable first joint moment. Quantitative tail and clipped Taylor-remainder moduli, uniformly over every axial offset and finite shift, still need proof. |
| L121(16)--(17), L248(3)--(8) and raw/prefix audit paragraph, L222(2)--(4) | Exact unaveraged lower prefix, modal C^m bounds and uniform value/mode errors. L248's stated raw value estimate alone is not a bound for L/a: quantify the needed transverse derivative comparison and higher derivative envelope using the same explicit smooth expressions. |
| L121(18), L222(5), L248(10)--(11) | Original a^4 quadrature normalization, compact smooth quadrature and both complete heat-matrix errors. Quantify the axial level mismatch and min weight before summing all offsets; include omitted labels, constant modes, triplet average and both shear polarizations. |

The proposed bounded mechanism is to quantify the existing joint
closed-trace expansion, using L267 for its energy factor and L121's
unweighted ell2 projection factor, then interior smooth-coefficient
Taylor bounds and full heat-weighted quadrature. Remote rows must be
bounded in the original trace before replacing their clamped samples.
Any N-dependent truncation must retain fixed physical clearance for
all local expansion segments; fixed-cutoff convergence alone is not
an admissible quantitative estimate. No new tail, derivative, moment,
projection or rate inequality is derived in this source comparison.
L269's accepted rate concerns a different insertion and is only a
methodological contrast, not proof of this target.

## Searches, duplicates and failures

Fresh bounded external queries were:

- `lattice Green function projection commutator variable coefficient trace asymptotic remainder scalar placement`
- `lattice Helmholtz projection discrete Green function commutator Lipschitz trace asymptotics`
- `lattice Yang Mills gradient flow translation Ward identities 1306.1173`
- `"lattice" "projection" "scalar" "trace" "commutator" Green remainder`
- `"lattice Green function" "commutator" Lipschitz`

The Ward query returned the already assessed primary paper. Other
results were unrelated wave/crystal/projector or continuum/asymptotic
leads; their search excerpts are not theorem evidence. No newly
matching primary rate theorem was inspected, and no novelty or global
absence follows from this bounded search. Reusable inspected sources
above provide the essential coverage without reopening unread leads.

Scoped local assessment/history searches found the parent qualitative
gap and the invocation-start handoff, not a duplicate scalar-placement
rate. Read ATTEMPTS/030 and ATTEMPTS/032: varying a parameter inside
a fixed-parameter qualitative theorem and separate first absolute
moments of projected alternating factors remain stopped shortcuts.
L109's recorded obstruction does not prohibit this joint pairing.
L113 also explains why the component-dependent shortcut from L096 is
inapplicable. These stops are preserved, not treated as global bans.
No existing unfinished work is discarded.

## Continuation and limits of approval

Approve one subsequent proof_attempt / REPRODUCTION step on exactly
TARGET under SPECIALIZE, subject to the supervisor's separate next-turn
approval of this newly completed assessment. Essential inputs are
L121 L113; supporting L114 L120 L267 L248 L222 retain their existing
analytic and audit qualifications. There is no new theorem-level
assumption, altered probe or boundary prescription in this approval.
Newly essential uncovered mathematics requires review before derivation.

Continue only if the complete finite comparison against precisely
L121(3) fits C_i N^(5/2)log(eN)^2, with every original row, shift,
orientation, level, heat label and normalization restored. If a tail,
derivative, boundary, clearance or heat allowance remains uncontrolled
or above budget, isolate that failure and reassess instead of calling
it signed growth. Two unproductive attempts require a materially
reassessed mechanism. The scalar comparison does not import energy-
placement or exterior-circulation rates and carries no outside factor 3.

Completed outcome: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED.
Coverage is now ready for a separate mathematical attempt; no requested
rate has been proved or imported and no mathematical exploration turn
is spent. Full matching and supporting Mathlib coverage are **not checked**;
unknown availability is not absence. Lemmas, mathematical scripts,
PROOF.md and DAG.md are unchanged during this turn.
