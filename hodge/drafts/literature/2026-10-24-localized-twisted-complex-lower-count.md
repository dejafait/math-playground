# Localized twisted-complex lower count — completed source comparison

TARGET: Assess whether localized Chern-character formulas for L147's actual twisted relative complex yield a lower split-count bound exceeding 119.
CHECKED: 2026-10-24
DECISION: IMPORT
SEARCH_EVIDENCE: Searched localized Chern character/exact-off-support, localized Riemann–Roch, excess intersection and Thom–Porteous expected-codimension terminology; inspected the primary Fulton passages and live Stacks passages below, and compared L145/L146/L147/L155/L156, ATTEMPTS/066/067/087 and the saved whole-character/whole-Euler assessments.
SOURCE_EVIDENCE: Fulton, Intersection Theory, second edition (1998), Theorem 18.1 pp. 342–343, Proposition 18.1 pp. 344–345, Corollary 18.1.2 pp. 345–346, Example 18.3.12 pp. 363–364 including all four proof reductions, Theorem 6.3 p. 102 with proof, and Theorem 14.4 pp. 254–255 with its expected-codimension clauses and flag reduction; live Stacks 42.50, Situation 42.50.1, Lemma 42.50.2 including its quasi-compact proof case, and Definition 42.50.3.
COMPARISON: Import the supported-perfect-complex equality and the regular-embedding/expected-codimension restrictions as known results. They do not supply the requested lower bound for C: C retains M off Z, the supported truncation retains the unknown W, and no independently evaluated intersection or positivity input is present.
GAP: No lower estimate, nonempty Z, global transverse degeneracy presentation or controlled excess-normal datum was found for the actual family; the inspected formulas alone do not bridge to |Z|>=120. This is a source-scope limitation, not a nonexistence theorem or an exclusion of every possible localized construction.
REASON: The bounded source comparison is complete and changes the route decision: park formula-only localized lower control rather than approve an unsupported mathematical count. Reopening requires a specific global presentation and independently controlled intersection term.
SCOPE: Same hypothetical equality F and actual L147 complex with locally free ordinary M and finite possibly empty Z; only comparison with supported-complex, excess and ordinary degeneracy formulas. No new derivation, lemma, script, Chow-class lift or positivity claim is approved.
LITERATURE_REASON: The proposed lower-count mechanism required essential previously unread supported-complex and excess/degeneracy hypotheses; the ready whole-Euler audit assessment did not cover them.

## Gap, intermediate target and discriminating test

Universal primitive rational Hodge realization remains the main gap.
For this conditional recipe, F existence and a contradictory lower split
count are independent missing steps. The target was a primary formula
with an independently evaluable term forcing z=|Z|>=120, against L156's
separately audited z<=119. Such a comparison could exclude this bundle
recipe; it would neither construct cycles nor disprove the Hodge conjecture.
The test fails for the inspected formula-only mechanism: no such term
has been identified. Empty Z remains allowed.

Retain identical marked projective K3 factors/common g,h, the fixed
chamber and full tensor, hypothetical locally free Omega-polystable
rank-two F, integral c_1(F)=0,
ch_2(F)=-14e_1-21e_2-tau_D, k=(-4,-2,1,2), k.h=0,
k^2=-14 eta and integral eta=1. Retained local inputs are L096's finite
possibly empty Z; L145/L146's actual ordinary stalks; L147's entire
ordinary complex and character; L153's same-h polystability; and
L155/L156's actual endpoint vanishings and upper bound. Their proofs
are not reaudited here. No cross-notebook input is used.

## Primary source statements actually inspected

**Supported-complex formula.** [Fulton, second edition scan](https://djvu.online/file/Pl4avuZzLcI6I),
Section 18.1 pp. 340–345, constructs the localized character for a
bounded vector-bundle complex exact outside the closed support.
Theorem 18.1 gives its bivariant operations; Proposition 18.1 gives
pushforward to the alternating ordinary character and additivity.
Example 18.3.12 pp. 363–364 identifies its Todd-weighted action with
the alternating supported homology classes. Its proof uses proper
pushforward, exact-complex additivity, elementary complexes and
birational reduction. Corollary 18.1.2 pp. 345–346 handles changing a
regular ambient embedding, with the inverse normal Todd factor.

**Excess and degeneracy formulas.** In the same primary text,
Theorem 6.3 p. 102 requires a cartesian regular-embedding square and
its excess normal quotient; its proof uses the quotient-bundle exact
sequence, Whitney and projection formulas. Theorem 14.4 pp. 254–255
constructs a rank-degeneracy class for E -> F. Positivity of that class
on its full support requires expected codimension (e-k)(f-k);
identification with the fundamental cycle also assumes a
Cohen–Macaulay base. Read the theorem's flag/Grassmann reduction.
These statements provide no unconditional numerical lower bound.

The scan is a third-party host of the primary book. OCR damages some
symbols; no disputed coefficient was recovered from ambiguous OCR.
The exactness requirement and pushforward identity are independently
legible in [Stacks 42.50, tag 0FB0](https://stacks.math.columbia.edu/tag/0FB0).
Situation 42.50.1 assumes a perfect object, a closed support and one
of the stated finiteness alternatives; the projective base meets the
quasi-compact alternative. Lemma 42.50.2 and Definition 42.50.3 give
localized character only when the restriction outside the support is
zero, and its pushforward equals the ordinary character. The proof's
quasi-compact case verifies that Chern operations exist on the proper
graph modification. The separate localized-c_p alternative requires
a degree-zero bundle of rank less than p; it is not a license to
localize an arbitrary nonzero middle bundle in degree two.

An optional lead is Fulton–Lazarsfeld, *Positive polynomials for ample
vector bundles*, [author-hosted PDF](https://www.math.stonybrook.edu/robert.lazarsfeld/Reprints/Fulton.Laz.PPAVB.pdf),
Section 3b, Proposition 3.5, printed p. 49. Search extraction displayed
its ampleness hypothesis on Hom(E,F) and its cone-class proof, but the
PDF text extraction/visual retrieval did not provide a usable complete
page in this session. It is not counted as an independently inspected
positivity theorem and is not used. A shell download failed at DNS;
this optional access failure does not block the completed comparison.

## Comparison with the actual retained complex

L147 concerns C=Rp_{2*}(F tensor p_1^*L^{-1}), with ordinary sheaves
H^0(C)=0, H^1(C)=M locally free of rank 24, and
H^2(C)=W=sum of one residue field at each point of Z. In particular,
C is not exact on B minus Z. The main localized-character hypothesis
therefore fails for C itself. A zero virtual rank alone would not
replace this derived exactness requirement either.

The standard supported truncation is the top cohomology W in its
retained derived degree. Applying a supported formula to it retains
the same unknown point lengths already identified by L145/L147.
No global direct-sum splitting of C is needed to make this observation,
and none is asserted. Cancelling M as a virtual class is not an
independently specified supported complex with a new count. L147
already records [C]=-[M]+[W] and its full cohomological character;
the pushforward equality gives no separate value for the unknown
middle character or for z. In particular, no cohomological character
is silently promoted to an independently known Chow class.

L146's minimal local presentation has ranks (1,26,1) and splits
locally into the middle free term and an exact-off-the-point Koszul
piece. It determines a local length, not a global transverse map
between specified bundles. Treating an individual boundary in that
presentation as an arbitrary bundle homomorphism does not verify
Theorem 14.4's expected-codimension condition. Its positive-cycle
conclusion cannot simply be assigned to the isolated support.
Nor has a cartesian regular-embedding square and its normal quotient
been specified to which Theorem 6.3 supplies a new global number.
A future such construction could change the comparison; it is
currently an additional mathematical input, not a consequence of
finiteness, stalk ranks or the word “excess”.

L153's polystability and L155/L156's vanishing control the ordinary
middle bundle at h. They establish neither ampleness of a proposed
Hom bundle nor the missing intersection data. L156's z<=119 and
h^1(M)=119-z survive unchanged. No formula inspected here forces
even one split parameter, let alone 120.

## Overlap, decision and limits

Reuse the inspected general coherent GRR coverage in
[the whole-character assessment](2026-10-22-twisted-middle-global-character.md)
and the source approval in
[the whole-Euler audit assessment](2026-10-24-whole-euler-split-bound-critical-audit.md).
The new contribution of this source turn is the precise comparison
with supported-complex exactness and excess/degeneracy hypotheses.
ATTEMPTS/066's old metric shortcut, ATTEMPTS/067's duality-only stop,
ATTEMPTS/087's numerical compatibility and the October 12 twisted-IT
failure are not reasserted as new evidence or global bans.

Outcome: NEGATIVE, LITERATURE, KNOWN_IMPORTED. Park only the proposed
formula-only lower-count route. No new mathematical lower bound,
novelty, F exclusion, cycle or universal solution is claimed. A future
reopening must name an actual global presentation or intersection
whose independent value/sign gives a numerical lower-count test.
Full matching Mathlib coverage is not checked; unknown availability
is not evidence of absence. No standard theorem is reproved, and no
lemma or mathematical script is changed.
