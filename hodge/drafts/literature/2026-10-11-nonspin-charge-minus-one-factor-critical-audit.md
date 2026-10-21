# Individual nonspin factor — critical-audit source coverage

TARGET: Critically audit L088 exact-h locally free rank-two determinant-k charge-minus-one existence, including the primitive freeness exceptions and real-stratum transfer.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the construction assessment; inspected L088, L052's exact perpendicular-lattice passage, histories 210–212 and ATTEMPTS/056; searched the precise Yoshioka freeness proposition and Greb–Toma chamber theorem and retrieved their primary statements and relevant proof cases.
SOURCE_EVIDENCE: Yoshioka math/9907001v2 (7 February 2000), Theorem 0.1 and Section 0.2 p. 2, Proposition 0.5 p. 4, Remark 2.2 and Lemma 3.1 p. 11, Section 3.1.3/Proposition 3.2 p. 15, Proposition 3.4 and Sections 3.2–3.3 p. 16; Greb–Toma Algebraic Geometry 4 (2017), Theorem 6.6 with complete proof p. 74 and Section 6.3.3 pp. 74–75; O'Grady Algebraic Geometry 9 (2022), Definitions 3.1–3.3 and Proposition 3.4 p. 8, Proposition 3.10 with proof pp. 9–10.
COMPARISON: Named theorems cover the existence/freeness and stability-stratum inputs; the audit must independently check L088's arithmetic, generality, simultaneous slope stability and unchanged-real-metric specialization. This approves audit coverage, not L088's correctness or any tensor existence.
GAP: Verify every specialization bridge, especially the normalized freeness exception, the rational ray in the actual relative stratum and strict rather than semistable endpoint stability.
REASON: Essential audit-specific comparison is now complete; proceed to one mathematical critical audit using the cited inputs without re-proving general existence or chamber theorems.
SCOPE: L088 with L052's marked projective K3 S, fixed real ample h and primitive k with k^2=-14 and NS(S) intersect h-perp=Zk; ordinary rank-two determinant O_S(k), c_2=-eta; no tensor, image, kernel or transport existence.

LITERATURE_REASON: The saved next action is the separate critical audit of the newly specialized L088; its freeness-exception and real-stratum source comparison was explicitly incomplete at invocation start.

## Relevance and bounded test

The main gap remains algebraic realization of every primitive rational
Hodge class, already on arbitrary fourfolds. The local common-kernel
route still lacks F with the full negative tensor. The intermediate
target is independent verification of L088's individual factor, which
could support a later normalized tensor test with the L080 factor.
Individual existence alone cannot establish that tensor's stability
or acyclicity, identify the actual L079 image, or provide transport.

Continue if the imported hypotheses and all changed-charge bridges
survive an independent audit. Repair or qualify a failed claim and
retain only what is proved; do not reuse L080's spherical automatic
point-defect removal. No new mathematical result is derived here.

## Primary existence and freeness coverage

[Yoshioka, *Irreducibility of moduli spaces of vector bundles on K3
surfaces*, math/9907001v2](https://arxiv.org/pdf/math/9907001v2),
7 February 2000: Theorem 0.1 assumes primitive positive rank,
algebraic first class and general ample H; square at least -2 gives
nonemptiness. Section 0.2 states condition (♮) for equality slopes.
Proposition 0.5 keeps these hypotheses and classifies moduli with
no locally free points. Section 3.3(2) expands its shortened final
form into rank one, v=(rank v_0)v_0-eta, or
v=ell v_0-(ell+1)eta with rank v_0=1 and spherical v_0.
Section 3.1.3's Proposition 3.2 realizes the second exception by
point quotients of repeated spherical bundles. Proposition 3.4's
proof explicitly normalizes the rank-one spherical vector by a
line-bundle twist before writing ell-eta. Thus that displayed short
form must not be interpreted as forbidding twists. Section 3.2
handles the equality boundary; Section 3.3 distinguishes the slope
locus from the locally free locus.

The audit must check L088's exclusions against this full list and
justify one simultaneously free and strictly slope-stable point.
It must not infer simultaneous existence from unrelated nonempty
loci. These are audit questions, not conclusions of this review.

## Numerical walls and exact real endpoint

[O'Grady, *Modular sheaves on hyperkähler varieties*, Algebraic
Geometry 9 (2022), 1–38](https://content.algebraicgeometry.nl/2022-1/2022-1-001.pdf):
Definitions 3.1–3.3 give locally finite closed numerical walls and
the sheaf wall parameter. Proposition 3.10 bounds a destabilizing
class, retaining its zero-class alternative; its proof uses the
Chern identity, Hodge index and Bogomolov. Proposition 3.4's stated
stability comparison uses ample divisor classes. The audit must
check L088's discriminant-ten parameter and saturation argument;
this source alone is not an irrational-endpoint theorem.

[Greb–Toma, *Compact moduli spaces for slope-semistable sheaves*,
Algebraic Geometry 4 (2017), 40–78](https://content.algebraicgeometry.nl/2017-1/2017-1-003.pdf):
Theorem 6.6 fixes full topological invariants and a compact subset
of P(X), then supplies finitely many rational linear walls with
uniform stability and semistability comparison. Its complete proof
reduces to a compact convex ample neighborhood and the finite
hyperplanes from Lemma 6.4. Section 6.3.3 expressly treats connected
strata of smaller dimension. Its rational-point argument and
positive-scaling invariance are relevant; Proposition 6.7 itself is
stated for dimension greater than two and is not needed as a surface
existence input. On the surface the power map is the identity, as
already used in L088. The audit must keep artificial walls through
h as equalities, preserve all other signs, and verify generality
for Yoshioka separately. An arbitrary nearby rational H would not
be a justified substitute. The theorem covers both strict stability
and semistability; no weakening of the desired endpoint is intended.

## Search, duplication, access and limits

Queries: `"Yoshioka" "Proposition 0.5" "locally free" K3`;
`"Greb" "Toma" "Theorem 6.6" chambers stability`.
The construction assessment's prior discovery is reused. A primary
Bayer–Macri wall-crossing paper appeared as a supporting citation
lead but was not inspected or used; unrelated quiver-GIT theorem
numbering and secondary survey hits supply no evidence here.
No novelty inference follows from these searches.

Targeted local inspection found L088 is the new individual-factor
application. L052 supplies its fixed lattice input. Histories 210–212
and ATTEMPTS/056 keep the half-adjoint filter exhausted, while
L080's different spherical defect argument is expressly excluded
from L088. No duplicate audit conclusion is imported.

Web primary PDF text was accessible; the Greb–Toma statement,
complete short proof and lower-stratum paragraph were read. A local
curl download failed DNS resolution; web access supplied the needed
text, so this is not an essential source blocker. A screenshot call
returned a reference only; no visual verification is claimed.
Full matching and supporting Mathlib coverage: not checked.

Only the assessment, checkpoint and concise history are updated.
No lemma, mathematical script, DAG or argument overview is changed.
The next invocation is the mathematical audit under this exact
ready target, subject to supervisor approval of the changed assessment.
