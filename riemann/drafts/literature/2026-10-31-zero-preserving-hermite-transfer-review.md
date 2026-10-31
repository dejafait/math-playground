# Zero-preserving actual-Hermite transfer: completed source comparison

TARGET: Assess known zero-preserving corrections of actual-Xi Hermite truncations for enforcing L569's multiple-zero jet conditions without presupposing unknown zeros, and select one bounded signed-transfer test or park this mechanism.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched exact Xi/Hermite zero-preserving corrections, confluent interpolation with arbitrary multiplicities, and hyperbolicity-preserving operators; inspected the primary statements below and their relevant construction/proof cases. No independently specified actual-Xi correction and signed cost was found. This bounded search proves neither novelty nor impossibility.
SOURCE_EVIDENCE: Phung, Z. Anal. Anwend. 37 (2018), 251–268, DOI 10.4171/ZAA/1612, Section 2 Theorems 2.1–2.3 pp.253–254, https://ems.press/content/serial-article-files/35980 ; Borcea–Brändén, Ann. Math. 170 (2009), 465–492, Section 2.1/Theorem 2 p.470, Lemma 3 pp.477–478 and Theorem 2 proof p.480, https://annals.math.princeton.edu/wp-content/uploads/annals-v170-n1-p14-p.pdf ; Romik arXiv:1902.06330v3 Section 2.5, (2.46)–(2.51), Theorem 2.9 and full short proof, https://arxiv.org/html/1902.06330v3#S2.SS5 . Reuse Theorem 2.1 and (2.20)–(2.22) from the prior ready assessment.
COMPARISON: Confluent interpolation supports arbitrary supplied multiplicities but requires the nodes and derivative data; a hyperbolicity preserver controls the root class of already hyperbolic inputs, not equality of unknown Xi zero jets. Hermite Poisson damping is the known heat deformation. None supplies the requested actual correction with an equality-compatible signed estimate.
GAP: No construction independent of unknown zeros with controlled correction cost has passed the source test. Actual joint jets, moving-height signed bounds, cutoff changes and higher forms remain open. No general nonexistence theorem for corrections is claimed.
REASON: Park this correction mechanism after completing its bounded comparison; do not nominate an unsupported signed-transfer calculation. The changed continuation is separately source-gated and concerns a direct kernel representation, not another correction or smaller C^2 error.
LITERATURE_REASON: The startup target changed from the uncorrected absolute budget to an unknown-zero-independent correction; essential construction and multiplicity coverage were missing. Previously ready convergence and absolute-tail assessments were reused.
SCOPE: Completed literature-only comparison; no new result, correction formula, lemma, mathematical script, DAG edge or proof-overview change. EXPLORE records the completed bounded search, not approval of an unspecified correction proof.

## Gap, target and discriminating test

The main gap remains actual-Xi all-degree mixed positivity. The approved
intermediate target was an actual correction of L564's P_N, with its
normalization and N=ceil(16(T+1)^2), whose joint jets could satisfy L569
without knowing the multiple zeros in advance. Its plausible use would
be equality-compatible transfer of the first Laguerre form. All higher
forms would remain independent even after that transfer.

The admission test was a specified construction with available input
data, multiplicity coverage, and a concrete signed-error threshold.
A theorem that only interpolates at supplied zeros or preserves a root
class already assumed for the input does not pass it. No positive
correction mechanism passed; no correction was calculated or ruled out
in general. The outcome is literature EXPLORATION, not a new obstruction.

## Primary theorem comparisons

**Prescribed-node confluent interpolation.** Van Manh Phung,
*Continuity and Convergence Properties of Integral Means of Bojanov–Xu
Interpolation*, [publisher PDF, Section 2](https://ems.press/content/serial-article-files/35980#page=3),
Theorems 2.1–2.3, pp.253–254. Theorem 2.1 takes distinct real nodes
 t_i, positive integers mu_i, d=sum mu_i, and a function with derivatives
through mu_i-1 at each node. It gives a unique polynomial of degree at
most d-1 matching those derivatives. Theorem 2.2 explicitly constructs
it from the derivative data and the nodal polynomial
w(t)=product_i(t-t_i)^(mu_i). Theorem 2.3 assumes g in C^(d-1)(I)
and gives continuity when nodes coalesce, including the Taylor limit.
These full statements and the displayed construction were read.
Multiplicity is allowed; neither unknown nodes nor their derivative
data are produced. Xi's analyticity satisfies smoothness at any
*specified* real nodes, but does not provide its unknown zero list.
The result therefore supplies no usable correction here. Continuity
alone is no moving-height quantitative bound. No specialization or
reproof is made. The cited upstream reference is Bojanov–Hakopian–
Sahakian, *Spline Functions and Multivariate Interpolations*, Kluwer
1993, Theorems 1.1/1.4; its proof was not independently inspected.

**Node-independent root-class preservers.** Julius Borcea and Petter
Brändén, [published version, Theorem 2](https://annals.math.princeton.edu/wp-content/uploads/annals-v170-n1-p14-p.pdf#page=8).
For a real linear T on polynomials of degree at most n, preservation
of hyperbolicity is characterized by a range of dimension at most two
spanned as specified by interlacing hyperbolic P,Q, or real stability
of T[(z+w)^n] or T[(z-w)^n]. Read the nonstrict definitions, all three
branches, Lemma 3's low-rank versus preserving/reversing alternatives,
and the short reduction to Theorem 4. Nonzero hyperbolic inputs allow
multiple roots; output zero is permitted. The criterion supplies no
previously unproved hyperbolicity of P_N or Xi, no equality of input
and output zero locations, and no Xi-remainder derivative cost. Its
finite polynomial scope cannot silently be extended to Xi. The source
is a theorem-level comparison, not an imported sign theorem or an
independent audit of its upstream stability results. The older
three-author Master4 manuscript has different numbering; it is not
the version cited here.

**Hermite damping.** Romik v3, [Section 2.5, Theorem 2.9](https://arxiv.org/html/1902.06330v3#S2.SS5),
(2.46)–(2.51), defines the Poisson flow by coefficient weights r^n and
proves X_r^H(t)=Xi_((r^2-1)/4)(rt), 0<r<=1. Read the generating-function
calculation through its final kernel integral, together with the
positive-time hyperbolicity discussion. This is a deformation and
rescaling, not a source assertion of unchanged Xi zeros or L569 jets.
The exact heat-flow identification was already recorded in the ready
moving-degree/first-sign reviews. It is duplicate coverage, not a new
mechanism or a fresh negative result. No source interchange is newly
proved or applied. Romik's Theorem 2.1 and its compact remainder are
reused; L564 retains its explicit absolute-tail qualification.

## Search/access and local failure record

Queries actually used included `"Riemann xi" "Hermite" "zero preserving"`,
`"zero preserving" "approximation" entire functions multiple zeros`,
`Hermite interpolation analytic function multiple zeros prescribed nodes remainder theorem`,
`Borcea Branden Polya Schur master theorems circular domains theorem 1 real stability preserving operators arxiv`,
`"Riemann xi" "Hermite" "correction" zeros`,
`"zero-preserving" "entire" approximation multiplicities`,
`"multiplicative approximation" "entire functions" zeros`, and
`"Hermite interpolation" "distinct" "r_i" pdf theorem`.
The exact-Xi searches located expansion/flow material and unrelated
or unreviewed RH claims, not a correction theorem meeting the test.
No claim of exhaustive search or originality follows.

DLMF Section 3.3(vi) was inspected: it points to Hermite-interpolation
references but does not itself state the arbitrary-multiplicity theorem.
Dahlquist–Bjorck, *Numerical Methods in Scientific Computing I*,
Theorem 4.3.1 was a search lead only: the institutional PDF timed out
and the publisher chapter exposed only its opening/access page.
Neither the search excerpt nor that landing page counts as inspected
proof. The ScienceDirect quadrature source returned 403; Sidi's
rational-interpolation author PDF returned 502. These optional leads
are parked; the accessible Phung statements/construction suffice for
the prescribed-node applicability comparison. No dependent research
is waiting on them. Hu's UCLA interpolation notes were read as
supplementary exposition only, not the primary theorem evidence.

Local reads: L569 in full; L564's coefficient normalization and complete
tail proof; L568's hypotheses, sign/decomposition and scope; the two
prior compensation assessments and named multiple-zero stop; the
moving-degree and CD source notes; the completed first-sign discovery.
Scoped term searches checked zero preservation, confluent interpolation,
operator/Hermite–Biehler comparisons and recorded failures. The October 6
multiplicity-count assessment already distinguishes polynomial and
entire-function Hermite–Biehler hypotheses; the October 31 translate
review retains assumed LP in its necessity argument. Those are
comparisons, not available positivity premises. No sibling notebook or
cross-notebook theorem was read. Existing changes were preserved.

## Route decision and continuation boundary

Park unknown-zero-preserving actual-Hermite correction development.
Reopen only with a concrete input-independent correction and an
independently checkable signed cost; a node list assumed to be the Xi
zeros, existing heat damping, smaller absolute errors or another B_N
probe grid does not supply that input. L568/L569's stops keep their exact
scopes. Full signed cancellation and other actual constructions remain
mathematically possible.

The next nomination is a distinct source question about direct
positive-semidefinite representations of the two-variable de Branges
kernel for (Xi,Xi'). The proposed assessment is
`2026-10-31-theta-de-branges-kernel-construction-review.md` and is
REVIEW_REQUIRED. It must distinguish an explicit construction from
assuming Hermite–Biehler membership, and retain possible multiple real
zeros. The old equivalence/translate reviews do not cover a construction.
No kernel formula, positivity or finite-section calculation is derived
here. No justified creative proof target is available yet: an explicit
positive representation independent of the desired sign is missing.
Essential source coverage takes precedence over the scheduling preference.
Full matching Mathlib coverage was not checked; availability is unknown.
