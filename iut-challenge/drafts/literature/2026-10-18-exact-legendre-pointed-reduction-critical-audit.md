# Exact-G stable pointed reduction — critical-audit coverage

TARGET: Critically audit L082's stable one-pointed reduction over unchanged G, including every finite completion, small residue characteristics, nonsplit nodes and whole-DVR pointed ampleness.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step324 read full L082 and compared the exact-G application assessment, L062 audit assessment/completed audit record and L051 relative-duality assessment; scoped L078/L081 input statements and L081 audit, history323 and ATTEMPTS/033–034. Reused recorded general-Weierstrass and Stacks searches; no fresh external search or source retrieval.
SOURCE_EVIDENCE: Reuse inspected Conrad (21 November 2015), section 2 pp.2,6 and Theorem 5.5/proof pp.14–16; Milne EC second edition (2021), II.3 pp.59–61; Hassett math/0205009v1 section 2 pp.2–3; precise Stacks statements/proof cases in the 2026-10-12 assessment, enumerated below. No fresh retrieval or L082 audit verdict is claimed.
COMPARISON: The general DVR, geometric-fiber and relative-family theorem hypotheses are unchanged by E_0/F becoming E_L/G. L078 supplies the number field/pointed curve and L081 the audited all-place semistability; no G/Q normality, splitness or old E_0/F model is required. Actual L082 calculations remain independent audit obligations.
GAP: Essential source coverage is ready for exactly TARGET; the independent check of L082's local equations, flatness, fibers, Cartier marking, whole-DVR divisor, duality shifts and marked relative ampleness remains undone.
REASON: SPECIALIZE already inspected general theorems to critically audit this particular all-G_v application, without reproving them or transferring a different curve's models. This approves coverage only.
SCOPE: Exactly TARGET with full L082, L078 and L081, unchanged D,s,t,iota,G, embedding,H,N; L062 is method context only. No new field, curve, action, normality test or initial-data assertion.

The main gap remains original finite B>=A. This intermediate audit
would test the correctness of the pointed-reduction prerequisite,
which can be useful independently of normality and other initial
data. Its inputs are the complete canonical L082 proof, L081's
audited semistability and L078's number-field/pointed-curve and
completion facts. L062 is method context only, not an input theorem
about E_L/G.

The completed comparison below compares the actual hypotheses of the cited
minimal-model, relative duality, cohomology and ampleness results
with the proposed audit obligations. Existing adequate assessments
are `2026-10-18-exact-legendre-stable-pointed-reduction.md`,
`2026-10-15-everywhere-stable-pointed-reduction-critical-audit.md`
and the relative-duality section of
`2026-10-12-native-all-place-critical-audit.md` in this directory.
No essential unread theorem was identified by the completed comparison. Full matching
and supporting Mathlib coverage is unchecked.

The discriminating audit is whether every actual minimal general
Weierstrass family has the required flat geometric fibers, smooth
Cartier origin, whole-DVR div(C)=3S, duality shifts and marked
relative ampleness, with the pointed generic isomorphism over the
unchanged completion. Continue on a complete check; repair or narrow
on a failed hypothesis, and do not extend the field to pass the test.
No such independent audit occurs in this literature turn.

G/Q normality and mixed radical/15-torsion information, other initial
data, retained radical memberships/scalar occurrence, native
input/action, marked all-image factorization, pilot transport,
essentiality and original finite B>=A remain open. The original and
auxiliary witnesses stay distinct and ATTEMPTS/033–034 remain intact.

## Completed scope comparison — 2026-10-18, step324

LITERATURE_REASON: The saved L082 audit was REVIEW_REQUIRED; its changed exact-G scope required comparison with existing adequate assessments. No changed source hypothesis or essential unread theorem emerged, so no redundant retrieval was undertaken.

The preceding proposal is retained as scope history, not as an audit
verdict. This review read L082 to identify its cited inputs and proof
obligations, without adjudicating those computations. No duplicate
completed L082 audit occurs in the scoped construction record or the
canonical proof. L062's completed audit supplies a method comparison,
not a theorem about this curve.

### Source hypotheses matched to audit obligations

1. [Conrad, *Minimal models for elliptic curves*, 21 November 2015](https://math.stanford.edu/~conrad/BSDseminar/refs/minimalmodel.pdf),
   section 2 pp.2,6 and Theorem 5.5 with proof/discussion pp.14–16,
   covers pointed integral minimal general Weierstrass equations over
   a DVR and the good/multiplicative smooth/geometrically nodal bridge.
   The exact-G application assessment records inspection of the full
   proof and small-characteristic/splitness discussion. Reuse also
   [Milne, *Elliptic Curves*, second edition (2021), II.3 pp.59–61](https://www.jmilne.org/math/Books/EC2.pdf).
   The source scope includes the complete DVRs of a number field;
   normality over Q and a split torus are not hypotheses. The audit
   must check the actual pointed generic identification, retaining
   general a1,a3, rather than assuming the global Legendre equation
   minimal. No new minimal-model theorem is needed.
2. [Hassett, math/0205009v1, section 2 pp.2–3](https://arxiv.org/pdf/math/0205009v1)
   defines stable weighted pointed families over a noetherian base.
   Weight one requires proper flatness, connected nodal geometric
   fibers of fixed genus, a smooth marking and relative log-dualizing
   ampleness. This definition has no excluded residue characteristic.
   The audit must verify these properties; semistability alone is not
   a verification of the written model. Geometric nodality does not
   require changing the actual DVR to split its branches.
3. The previously inspected [Stacks 0A9W](https://stacks.math.columbia.edu/tag/0A9W)
   assumes a quasi-compact quasi-separated base and a locally free
   projective-bundle module. [0A9X](https://stacks.math.columbia.edu/tag/0A9X)
   assumes a pseudo-coherent closed immersion, quasi-compact
   quasi-separated ambient scheme and a bounded-below quasi-coherent
   complex. [0AA4](https://stacks.math.columbia.edu/tag/0AA4)
   supplies the effective-Cartier normal-bundle twist and shift;
   [0ATX](https://stacks.math.columbia.edu/tag/0ATX) supplies composition
   over a noetherian base, with its proper right-adjoint proof case
   already inspected. None requires regular total space or a smooth
   Cartier hypersurface. Check the actual immersion, finiteness,
   complex boundedness, global twists and shifts in L082; the source
   formulas are imported by citation, not reproved.
4. [Stacks 0E6N](https://stacks.math.columbia.edu/tag/0E6N),
   Lemma 109.19.1/Definition 109.19.2, treats proper flat
   finite-presentation curve families with equidimensional
   one-dimensional Cohen–Macaulay fibers and identifies the sheaf
   in cohomological degree -1. [0E6R](https://stacks.math.columbia.edu/tag/0E6R)
   gives invertibility and base change for Gorenstein fibers.
   The recorded reduction proof and Gorenstein proof were inspected
   in the 2026-10-12 assessment. L082 must verify these actual family
   hypotheses and distinguish the relative complex from ambient Ext.
5. [Stacks 01XT](https://stacks.math.columbia.edu/tag/01XT),
   Lemma 30.8.1, covers projective-space cohomology over an arbitrary
   ring; its complete Cech proof was inspected previously. It supports
   the fiber connectedness/arithmetic-genus check, not normalization
   genus. [01VG](https://stacks.math.columbia.edu/tag/01VG),
   Lemma 29.38.2, and [01PT](https://stacks.math.columbia.edu/tag/01PT),
   Lemma 28.27.2, cover positive tensor powers and relative ampleness.
   Their proof coverage is already recorded. The smooth Cartier
   section and whole-DVR divisor identity remain audit obligations;
   equal supports or fiber degrees alone do not meet them.

These are reused primary theorem statements and relevant proof cases,
not fresh retrievals. Stacks retains the recorded live-version
qualification, without a pinned revision claim. The exact-G application
assessment and L051 duality assessment give the source versions and
full supporting scope; no new external lead is left essential here.
Full matching and supporting Mathlib coverage remains unchecked.

### Decision and discriminating test

SPECIALIZE approves exactly TARGET for a separate REPRODUCTION
proof audit. The strongest relevant known conclusion is the general
minimal-model/pointed-family method; an existence citation does not
check L082's actual equations, section or whole-DVR sheaf argument.
Thus those local verification steps are justified, while a reproof of
the general theorems is not. This is no claim beyond checked sources.

Continue if the independent audit verifies every stated obligation at
every unchanged G_v, including 2,3 and nonsplit nodes. If any essential
hypothesis fails, record and repair or narrow that assertion within
scope; do not extend G to obtain a pass. An uncovered replacement
claim needs separate source review before dependent mathematics.

ATTEMPTS/033–034 concern unnecessary classification retrieval and the
failed cyclic-Frobenius normality separator, respectively; neither is
used by this target. The different descent-model quantifier in
ATTEMPTS/028 and the regular-polygon issue remain distinct. This
source comparison neither reopens them nor resolves normality or any
transport/essentiality gap. No lemma, script, PROOF or DAG is changed.
