# Exact auxiliary Legendre field — pointed-reduction source comparison

TARGET: Determine whether L081's semistability yields stable one-pointed reduction of the unchanged E_L at every finite G-place, without extending G or its completions.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step322 compared L081 and L078 with L062, the two 2026-10-15 pointed-reduction assessments and the 2026-10-12 relative-duality assessment; scoped the exact-Legendre assessments/history318–321 and ATTEMPTS/033–034. Reused the recorded semistable/minimal-Weierstrass searches; primary PDF text searches located Conrad Theorem 5.5 and Hassett section 2. No duplicate exact-G pointed-model application was found in these paths; no novelty inferred.
SOURCE_EVIDENCE: Reinspected Conrad, Minimal models for elliptic curves (21 November 2015), section 2 p.2 and Theorem 5.5 with complete proof pp.14–15 and small-characteristic/splitness discussion pp.15–16; Hassett math/0205009v1 (1 May 2002), section 2 pp.2–3. Reuse the prior inspected Conrad minimality, Milne II.3 pp.59–61 and precise Stacks relative-duality/cohomology/ampleness statements and proof cases detailed below.
COMPARISON: These general DVR and family results have no dependence on E_0/F, G/Q normality, rational 30-torsion or everywhere splitness. L081 supplies the same-field semistability needed for their exact-G application. L062 is an audited method for a different curve, not a conclusion about E_L/G; its old local equations are not transferred.
GAP: Essential source coverage is ready; separately verify the actual minimal general-Weierstrass families, pointed generic identifications, smooth Cartier origins, geometric fibers, whole-DVR divisor identity and relative duality/ampleness for every G_v. No exact-G stable-model conclusion is derived in this literature turn.
REASON: SPECIALIZE known general results and the audited pointed-cubic method to the unchanged E_L/G; the local applicability checks remain unwritten. No new general reduction theorem or reproof is justified.
LITERATURE_REASON: The gate required coverage for the changed curve/field; the 2026-10-15 assessments explicitly covered E_0/F only. This comparison resolves that scope gap by reuse, with narrow primary confirmation rather than renewed broad discovery.
SCOPE: Exactly TARGET for L081/L078's E_L/G and origin, every finite G-place, same D,s,t,iota, embedding and H,N; no field enlargement, global minimal equation, normality verdict or sufficient native initial data.

The main gap remains finite B>=A. The intermediate target is TARGET;
its plausible downstream use is the stable pointed-reduction part of
initial-data admissibility for the exact auxiliary field prescription.
Normality and other initial-data conditions are independent, so no
sufficient-admissibility claim follows from passing this target.

Essential inputs are L081 and L078, inheriting the same auxiliary
L073/L077 choices D,s,t,iota, embedding and H,N. L062 and its source
assessments are method context; its assertion about E_0/F is not an
assertion about E_L/G. Review those existing sources narrowly before
seeking additional literature. No new mathematical derivation or
source approval for this target is made in step321.

Continue only if the inspected local-model and ampleness results cover
the unchanged pointed curve over every G_v without any field extension,
including the small-characteristic and nonsplit cases. If a case needs
an unavailable hypothesis, record that obstruction rather than enlarging
G. The test asks for stable pointed models, not regular total spaces,
splitness at every place, a single global minimal equation, or complete
initial data.

G/Q normality and the mixed radical/15-torsion kernel, retained radical
memberships/scalar occurrence, other initial data, native input/action,
marked all-image factorization, pilot transport, essentiality and the
original finite B>=A remain unresolved. ATTEMPTS/033–034 stay intact;
this target uses neither blocked classification nor cyclic Frobenius
powers. Full matching and supporting Mathlib coverage is not checked.

## Completed scope comparison — 2026-10-18, step322

The proposal above records step321's then-unapproved scope. This
completed review approves that same target for a separate application;
it does not carry out the application.

### Primary minimal-model and stability inputs

[Conrad, *Minimal models for elliptic curves*, 21 November 2015](https://math.stanford.edu/~conrad/BSDseminar/refs/minimalmodel.pdf),
section 2 p.2, gives integral general Weierstrass models over an
arbitrary DVR, with a specified generic isomorphism taking infinity
to the origin. Theorem 5.5, pp.14–15, identifies the smooth locus
of a minimal model with the Neron identity open subgroup and relates
good/multiplicative reduction to smooth/geometrically nodal special
fibers. Read its full proof: the minimality comparison and the
one-versus-two geometric points on the smooth compactification are
both included. The discussion pp.15–16 treats characteristics 2,3,
imperfect residue fields and splitness separately. Its nodal conclusion
does not require a split torus. Reuse the previously inspected
minimal-equation existence discussion in section 2 p.6 and
[Milne, *Elliptic Curves*, second edition (2021), II.3 pp.59–61](https://www.jmilne.org/math/Books/EC2.pdf).
Milne was not freshly retrieved in this turn.

The hypotheses here require a local DVR and the same pointed elliptic
generic curve, not a particular number-field presentation or normality
over Q. L078 supplies a number field and nonsingular E_L with its
origin; L081 supplies semistability at all its finite places. No
additional torsion criterion is needed for the proposed pointed-model
step. The application must choose minimal general equations locally;
the literal Legendre equation need not already be integral or minimal
at every place. In particular retain general a1,a3 rather than use
a short-equation test that excludes small characteristics. This is a
comparison of input hypotheses, not a construction of those models here.

[Hassett, *Moduli spaces of weighted pointed stable curves*,
arXiv:math/0205009v1, 1 May 2002](https://arxiv.org/pdf/math/0205009v1),
section 2 pp.2–3, was read through the full family and stability
definitions. They require a noetherian base, proper flat family of
connected nodal geometric fibers of fixed arithmetic genus, smooth
markings with the stated weight condition, and relative log-canonical
ampleness. All weights one give ordinary pointed stability; this
definition imposes no residue-characteristic restriction. It supplies
the test, not an exact-G verdict. General stable reduction after a
ramified extension would not meet this target.

### Reused relative hypotheses and required application checks

The two `2026-10-15-everywhere-stable-pointed-reduction*.md`
assessments and the section “Relative-duality hypotheses and inspected
proof cases” of `2026-10-12-native-all-place-critical-audit.md` in this
directory give adequate primary coverage; no new Stacks retrieval is
needed. The latter records statements and relevant complete proof cases
for the following inputs, with their live-version qualification:

- [0A9W, Lemma 48.15.1](https://stacks.math.columbia.edu/tag/0A9W):
  projective-bundle duality over a quasi-compact quasi-separated base,
  for a locally free module of the indicated rank.
- [0A9X, Lemma 48.9.7](https://stacks.math.columbia.edu/tag/0A9X),
  [0AA4, Lemma 48.14.2](https://stacks.math.columbia.edu/tag/0AA4),
  and [0ATX, Lemma 48.16.3](https://stacks.math.columbia.edu/tag/0ATX):
  the pseudo-coherent closed-immersion right adjoint, the effective
  Cartier formula and composition over a noetherian base. Neither
  a smooth Cartier divisor nor a regular total space is required.
- [0E6N, Lemma 109.19.1/Definition 109.19.2](https://stacks.math.columbia.edu/tag/0E6N)
  and [0E6R, Lemma 109.19.3](https://stacks.math.columbia.edu/tag/0E6R):
  the relative curve dualizing sheaf for the stated proper flat
  finite-presentation families with one-dimensional Cohen–Macaulay
  fibers, and invertibility/base change for Gorenstein fibers.
- [01XT, Lemma 30.8.1](https://stacks.math.columbia.edu/tag/01XT),
  [01VG, Lemma 29.38.2](https://stacks.math.columbia.edu/tag/01VG)
  and [01PT, Lemma 28.27.2](https://stacks.math.columbia.edu/tag/01PT):
  projective-space cohomology and ampleness versus a positive tensor
  power over the base ring.

Changing from E_0/F to E_L/G changes the local applicability checks,
not these source hypotheses. The separate application must verify
properness, finite presentation and flatness of each actual local
cubic; connected geometric genus-one fibers and nodality in the
nonsplit case; the smooth Cartier origin; the whole-DVR hyperplane
divisor identity; and the global relative-duality shifts and
ampleness inference. A fiber degree alone does not verify the divisor
identity. No new divisor computation or sheaf calculation occurs here.

### Decision, failures and limits

SPECIALIZE approves exactly TARGET for a separate REPRODUCTION step,
importing the general results without reproof. The extra work is the
particular all-G_v applicability argument. L062's audited proof is a
method reference only; no old E_0-model, splitness, level-30 torsion,
or above-3 model is a premise for E_L/G. Full matching and supporting
Mathlib coverage remains unchecked, without an absence claim.

The scoped exact-field records contain semistability and completion
results, but no completed pointed-model application for this G.
ATTEMPTS/033–034 concern classification retrieval and a stopped
cyclic-Frobenius separator; this target uses neither. The recorded
L050/ATTEMPTS/028 descent-model obstruction concerns a different
quantifier and is not reopened. A regular I_n polygon, a splitting
extension or a single global minimal equation is unnecessary for
the proposed local pointed-family test.

Continue if every unchanged G_v supports the complete cited family
and marked-ampleness checks, including p=2,3 and geometric nonsplit
nodes. If an essential hypothesis fails or needs a field extension,
record the failed case and narrow or abandon this same-field target;
do not enlarge G to make it pass. A successful next application would
remove only the stable pointed-reduction prerequisite. G/Q normality,
the mixed radical/15-torsion kernel, other initial data, native
input/action, marked all-image factorization, pilot transport,
essentiality and finite B>=A remain independent unresolved gaps.

No lemma, mathematical script, PROOF.md or DAG.md is changed in this
source review. The original and auxiliary witnesses remain distinct,
with the same auxiliary D,s,t,iota, embedding and H,N throughout.
