# Fixed lower Chern data — Bogomolov source assessment

TARGET: Test the Bogomolov inequality for an arbitrary-rank slope-polystable locally free bundle with c_1=0 and ch_2=2[C]+B_c in L044's fixed ample chamber, allowing arbitrary higher Chern classes.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searches on 2026-10-04 checked compact Kahler Bogomolov/Lubke inequalities, real polarizations, arbitrary-rank polystability and cubic RM product bundles; exact queries and access limits are below. Local searches found no previous evaluation for these lower data; adequate chamber and bundle-framework coverage is reused.
SOURCE_EVIDENCE: Read Perego, arXiv:1910.01867v1 (4 October 2019), Theorem 1.1, p. 4; sections 3.1--3.2, pp. 41--44; Definition 4.7, p. 59; Definition 4.20, p. 65; Corollary 6.42 and its citation paragraph, p. 118, https://arxiv.org/pdf/1910.01867v1#page=118. Read the published article's opening/Theorem 1.1, Complex Manifolds 8 (2021), pp. 1--2; later published pages were inaccessible and are not claimed read.
COMPARISON: The inspected inequality has no integral-polarization or rank-two hypothesis and uses only rank and the first two Chern classes. Its fixed-data numerical application is missing. L045's fourth-Chern exclusion concerns one K-class; the proposed test allows every higher character. Conditional hyperholomorphicity and the previous presentation tests do not decide it.
GAP: Convert the fixed ch_2 to the Chern-class convention of the cited inequality and evaluate its full intersection at p_1^*omega_c+p_2^*omega_c. No sign, discriminant value or arbitrary-rank nonexistence conclusion has been calculated in this review.
REASON: Import the known inequality without reproving its curvature or existence theory, then perform one bounded numerical specialization in a separate research turn. This tests a broader necessary condition after the fixed rank-two survivor failed; satisfying it would still leave existence and transport unresolved.
SCOPE: The same very general S, X=S x S, final A_c and ample omega_c from L044; arbitrary positive bundle rank, actual slope-polystability at the common product Kahler class, c_1=0 and ch_2=2[C]+B_c, with unrestricted higher Chern classes and K-class. The covered correction subtarget below permits only pure point-class changes while retaining the mixed action and chamber; it is numerical necessity, not bundle existence. No residue search, stability proof or transverse transport is covered.
COVERED_TARGET: Determine which rational pure point-class corrections to L044's ch_2, with c_1=0 and the mixed action fixed, satisfy the Bogomolov necessary inequality in the same ample chamber.

## Hypotheses

Use the actual ample chamber in L044 (9)--(12), rather than the
pre-chamber vector of L025. The polarization is the real class
Omega=p_1^*omega_c+p_2^*omega_c on the smooth projective fourfold
X=S x S. No rational approximation of Omega is assumed to preserve
stability. The target concerns an actual holomorphic locally free
bundle, not the virtual class excluded by L045.

The initial pending assessment is completed here without changing
its TARGET. Reuse the prior
[compatible-bundle assessment](2026-09-27-compatible-cubic-rm-stable-bundle.md)
and [fourth-Chern assessment](2026-10-03-rank-two-fourth-chern-test.md)
for their unchanged framework and scopes.

## Conclusion

SPECIALIZE: the necessary inequality has adequate source coverage
for the exact TARGET. Its application remains a separate mathematical
step. No inspected theorem evaluates the notebook's fixed lower
character or constructs a bundle with it. No new lemma, calculation
or complete Hodge candidate is produced.

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. The source
input is known mathematics; a numerical application using these
tools should be classified as REPRODUCTION. The review spends no
mathematical exploration turn and establishes no originality.

## Proof — source comparison and bounded continuation

The main gap is still a compatible representative permitting transport
into the fourth NS-fixed RM direction. The intermediate target is the
necessary stability inequality for the specified lower data, across
all positive ranks. A violation would stop that data set independently
of higher-character repairs. Passing the test would leave actual
local freeness, stability and transverse transport to be established.
The attained span remains 21 and the RM directions three against four
required; arbitrary primitive fourfold classes remain unresolved.

### Inspected primary statement and conventions

Read Arvid Perego, *Kobayashi-Hitchin correspondence for twisted
vector bundles*, [arXiv:1910.01867v1, 4 October 2019](https://arxiv.org/pdf/1910.01867v1).
Theorem 1.1 (p. 4) treats a compact Kahler manifold with a Kahler
metric; Corollary 6.42 (p. 118) states, for a slope-semistable
twisted holomorphic bundle of rank r,

\[
\int_X\bigl((r-1)c_1(E)^2-2r c_2(E)\bigr)
             \wedge\sigma_g^{n-2}\leq0.
\]

Definition 4.7 (p. 59) uses the degree integral against
sigma_g^(n-1) divided by rank. Definition 4.20 (p. 65) includes
semistability in polystability and requires stable summands of equal
slope. Sections 3.1--3.2 (pp. 41--44) specify Chern--Weil classes
and sigma_g as the metric's real (1,1)-form. Taking the trivial
cocycle and zero B-field gives ordinary Chern classes. That auxiliary
B-field is unrelated to the notebook's correction B_c.

These hypotheses require no rationality of the metric's Kahler
class. The citation therefore covers Omega directly. Translating
the given second character, setting n=4, and contracting the full
class are deferred to research. No curvature reproof is needed.

The [published version](https://unige.iris.cineca.it/bitstream/11567/1038747/1/10.1515_coma-2020-0107.pdf),
*Complex Manifolds* 8 (2021), 1--95, DOI
[10.1515/coma-2020-0107](https://doi.org/10.1515/coma-2020-0107),
was readable at its opening but returned 403 for later-page requests.
The precise inequality citation above intentionally uses the fully
inspected preprint numbering and page, not an inferred published page.

### Closest known scope and redundancy

The source supplies a stronger stability hypothesis range than the
requested polystable case. It does not prescribe a Chern class or
evaluate this cubic correspondence. The remaining work is cup-product
bookkeeping for the specific beta=2[C]+B_c, with its pure components
and mixed operator recorded in L044 (12) and L045 (7). Do not replace
the full beta by its mixed RM action or by its divisor contribution.
No such contraction appears in the local Bogomolov/Lubke search.

L045 excludes only the exact V' by rank truncation. L028's parity
argument and L030's divisible presentation stop impose different
recipe hypotheses. Preserve all those failures; they do not answer
the saved arbitrary-rank stability test. The earlier Verbitsky and
stable-resolution comparisons are sufficient and are not reopened.

The explicit COVERED_TARGET uses the same inequality with only the
two pure point coefficients allowed to change. It covers numerical
constraints on rational data, not integrality or realizability as a
bundle. It permits reuse if a later turn chooses that bounded test.

### Search record and unread leads

Searches on 2026-10-04 included:

- `Kobayashi Differential geometry complex vector bundles Bogomolov inequality Einstein Hermitian Kahler Theorem 4.7 pdf`
- `Bando Siu Stable sheaves Einstein Hermitian metrics 1994 Corollary 3 Bogomolov inequality pdf`
- `Uhlenbeck Yau 1986 existence Hermitian Yang Mills stable bundles compact Kahler theorem pdf`
- `Kobayashi "Differential geometry" pdf site:mathsoc.jp`
- `Kobayashi "Differential geometry" pdf site:math.berkeley.edu`
- `"Stable sheaves and Einstein-Hermitian metrics" "Corollary"`
- `"Bando" "Siu" "Stable sheaves" pdf`
- `"On the existence" "hermitian" "Uhlenbeck" "Yau" filetype:pdf 1986`
- `"Differential Geometry of Complex Vector Bundles" "pdf" "Kobayashi"`
- `"Bando" "Siu" "pdf" "Bogomolov"`
- `"Stable sheaves and Einstein-Hermitian metrics" filetype:pdf -site:researchgate.net -site:citeseerx.ist.psu.edu`
- `"Differential Geometry of Complex Vector Bundles" "djvu"`
- `Perego "Kobayashi" "twisted vector bundles" arxiv`
- `Lübke "Chernklassen" "Hermite"`
- `"Kobayashi" "Differential Geometry of Complex Vector Bundles" site:djvu.online`
- `"K3" "real multiplication" "Bogomolov"`
- `"K3" "product" "polystable" "Bogomolov"`
- `"cubic" "real multiplication" "stable bundle"`

The exact-family searches returned the already assessed conditional
Schlickewei route and unrelated uses of the name Bogomolov; they
supplied no direct fixed-data theorem. This is bounded discovery,
not evidence of novelty. Only the primary statements named above
and the saved adequate assessments support the decision.

Perego's citation paragraph points to Kobayashi, *Differential Geometry
of Complex Vector Bundles* (1987), Chapter IV, Theorems 4.7 and 5.7,
and Lubke--Teleman, *The Kobayashi--Hitchin Correspondence* (1995),
Theorem 2.2.3 and Corollary 2.2.4. The
[MSJ volume link](https://www.mathsoc.jp/assets/pdf/publications/pubmsj/Vol15.pdf)
timed out; the local download failed DNS. The
[Bando--Siu author page](https://people.math.harvard.edu/~siu/bando_joint_paper/index.html)
offers scanned images which were not readable through the tools used.
These originals and the Uhlenbeck--Yau/Lubke original-paper leads
are unread and supply no theorem evidence here. Their access is
parked: the inspected exact inequality in the primary Perego paper
supplies the necessary source scope without them. An equality or
projective-flatness argument is not covered by this assessment.

### Continuation test

Compare the cited inequality with its required zero threshold by an
exact contraction in the saved chamber, retaining both pure point
coefficients and the full mixed class. Violation closes this lower-data
recipe. Satisfaction supplies only a necessary condition; it does not
revive the excluded V', prove stability, or justify unbounded signed
sampling. No discriminant value or sign is asserted here.

## Mathlib

Coverage: **not checked** for the Bogomolov inequality or its fixed-data
application. No matching declaration or absence from checked Mathlib
sources is asserted. Perego's named corollary supplies the inequality;
it is supporting input rather than a match for the evaluated TARGET.
