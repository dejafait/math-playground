# Corrected rank-two finite-rank realization — source assessment

TARGET: Test topological SU(2)-bundle realization obstructions for L049's corrected rank-two character on S x S, beginning with the symmetric survivor a=b=-10, beyond the product-line HRR tests.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded searches on 2026-10-04 covered SU(2) second-Chern realization on eight-manifolds, quaternionic line bundles, stable versus finite-rank obstruction theory, the K3 product, and possible corrections to the closest theorem; queries and inspected sources are recorded below. Prior rank/HRR coverage is reused.
SOURCE_EVIDENCE: Read Čadek--Crabb--Vanžura, Obstruction theory on 8-manifolds, author's manuscript dated 5 December 2007, corrected 8 July 2008, https://www.math.muni.cz/~cadek/papers/8_manifolds.pdf: Introduction, equation (2.1), Proposition 3.2, Sections 7--8, especially Proposition 8.2 and Corollary 8.4, manuscript pp. 1--3, 6, 10--13. Read Huybrechts, Lectures on K3 Surfaces, author's prepublication draft, Chapter 1, Definition 1.1, Section 2.4, Section 3.2 and Proposition 3.5, pp. 7, 12--13, 15--17, https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf. Read Basu--Ghosh--Sau, arXiv:2405.12835v1 (21 May 2024), Introduction/Theorem A and Proposition 4.9, pp. 1--2, 15, https://arxiv.org/pdf/2405.12835v1.
COMPARISON: Corollary 8.4 supplies an actual quaternionic-line existence criterion on closed spin eight-manifolds, hence an applicable finite-rank SU(2) criterion here; Proposition 3.2 instead concerns stable complex realization at complex rank four. L048--L049 have not evaluated the quaternionic criterion. The newer highly connected theorem assumes a 3-connected base and cannot replace it on S x S.
GAP: Apply the cited criterion to the integral second Chern class -beta_(a,b), checking Sq^2 after mod-2 reduction and the source's mod-12 characteristic number with the actual tangent Pontryagin class and full mixed tensor; begin with a=b=-10. No operation, characteristic number, extra congruence or survivor verdict is evaluated in this review.
REASON: The essential source gap is resolved. Import the general existence theorem and reproduce only its applicability and numerical specialization in a separate research turn; its finite-rank condition can discriminate surviving characters beyond ordinary index integrality, while holomorphic construction, stability and transverse transport remain separate gaps.
LITERATURE_REASON: The saved target changed from a formal character with integral product-line indices to an actual topological SU(2) bundle; the necessary primary finite-rank theorem had not been read at turn start.
SCOPE: The same fixed X=S x S, chamber and full integral mixed tensor as L048 and L049, integer corrections with a+b<=-13 and 6|(a+4)(b+4), c_1=0, rank two, ch_3=0 and the forced ch_4. Coverage includes the full admitted integer region, starting with a=b=-10. Conclusions concern topological necessity/existence, not holomorphic local freeness, polystability, uniqueness or deformation transport.
COVERED_TARGET: Determine the integer pairs in L049's surviving correction region that admit topological SU(2)-bundle realization, using Čadek--Crabb--Vanžura Corollary 8.4 and the full mixed tensor.

## Hypotheses

Preserve the saved target and the corrected data of L048--L049.
Write beta_(a,b)=(4+a)e_1+(4+b)e_2+tau_D, where tau_D is the
full integral mixed class. The prospective topological bundle has
complex rank two and trivial determinant, so its proposed c_2 is
-beta_(a,b). The symmetric pair is a concrete test input, not an
asserted bundle. No integral splitting of the Néron--Severi and
transcendental lattices is assumed.

## Conclusion

SPECIALIZE. The pending REVIEW_REQUIRED assessment is completed
without changing TARGET. The essential primary existence statement
is accessible and covers the finite-rank question under the present
manifold hypotheses. Its general proof is imported; evaluation on
the corrected family belongs to the next research turn.

This review is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. It
provides new source coverage and a concrete test, without evaluating
an obstruction or claiming a mathematical result beyond the checked
literature. The planned application is a REPRODUCTION of known tools.
No complete informal Hodge candidate arose.

## Proof — source comparison and applicability

### Exact finite-rank input

Use Čadek--Crabb--Vanžura,
[Corollary 8.4, manuscript p. 13](https://www.math.muni.cz/~cadek/papers/8_manifolds.pdf#page=13).
For a connected closed smooth eight-manifold M, a complex line
lambda with l=c_1(lambda) reducing to w_2(M), and u in H^4(M,Z),
the criterion for an H_lambda-line with c_2=u is

\[
\operatorname{Sq}^2\rho_2(u)=\rho_2(lu),\qquad
\frac14\left\langle p_1(TM)u+2u^2-l^2u,[M]\right\rangle
\equiv0\pmod{12}.
\]

The numerical expression is integral when the cohomology condition
holds. The conclusion concerns a quaternionic line, of complex
rank two. Section 7 identifies its skew form and determinant.
[Proposition 8.2 and the top-cell comparison, p. 12](https://www.math.muni.cz/~cadek/papers/8_manifolds.pdf#page=12)
use a factor of two from quaternionic to complex K-theory; the
untwisted spin index of a quaternionic bundle is even.
[Proposition 3.2, p. 6](https://www.math.muni.cz/~cadek/papers/8_manifolds.pdf#page=6)
gives complex-rank-four realization using a mod-6 condition.
That stable-range conclusion alone is insufficient for rank two.
Corollary 8.4's proof splits a quaternionic summand using the zero
Euler class, supplying the finite-rank conclusion.

The manuscript is dated 5 December 2007 and explicitly corrected
8 July 2008 on its first page; its pagination is used throughout.
The [arXiv record](https://arxiv.org/abs/0710.0734) lists only the
3 October 2007 v1 and the journal reference *Manuscripta Mathematica*
127 (2008), 167--186. Do not label the corrected author's copy
arXiv v2 or substitute the older v1's theorem numbering. A speculative
v2 URL returned 404; it is not a source blocker because the corrected
primary text was read. Followed the internal proof through Sections
7--8, Lemma 7.1 and Proposition 8.2; the older cited KO-Euler papers
are unread supporting leads, unnecessary for importing this theorem.

### Applicability and supporting surface inputs

Huybrechts's [Chapter 1, Definition 1.1, p. 7](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=7)
gives the trivial canonical bundle. Read
[Section 2.4, pp. 12--13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=12)
for the second Chern number 24, and
[Section 3.2 and Proposition 3.5, pp. 15--17](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=15)
for torsion-free H^2, vanishing odd integral cohomology, the even
K3 lattice, and w_2=c_1 modulo two. These are supporting facts,
not a realization theorem for the present character. The web copy
identifies itself as a prepublication draft; the locators refer to
that copy, also used by the existing foundations.

The complex manifold underlying this smooth projective product is
connected, closed and smooth of real dimension eight. Trivial
canonical bundles and the standard Whitney formula meet the spin
hypothesis; the trivial lambda is therefore allowed. The ordinary
quaternion algebra and Sp(1)=SU(2) identify the sought structure.
On a compact space a Hermitian metric reduces a trivial-determinant
complex rank-two bundle to SU(2). Thus no holomorphic hypothesis,
stability, 3-connectivity or new source manifold is needed for this
topological test. This is a hypothesis comparison, not an evaluation
of the criterion for beta_(a,b).

For the separate application, keep the mod-2 operation on the
actual integral Künneth class, and use the tangent Pontryagin class
of X rather than the putative bundle's class. Standard naturality,
the Cartan formula and Sq^2(z)=z^2 in degree two may be used with
the cited K3 lattice facts. The full mixed square already computed
in L048 is available. Neither that operation nor the characteristic
number is evaluated here. The source treats closed spin manifolds;
it does not authorize discarding obstructions on arbitrary
eight-complexes or classifying/uniquely identifying all bundles.

### Closest alternative and reused coverage

Read Basu--Ghosh--Sau,
[arXiv:2405.12835v1, Introduction/Theorem A, pp. 1--2](https://arxiv.org/pdf/2405.12835v1#page=1),
and [Proposition 4.9, p. 15](https://arxiv.org/pdf/2405.12835v1#page=15).
The setting is a 3-connected eight-dimensional Poincaré duality
complex; Proposition 4.9 tests primitive fourth-cohomology classes
using the top-cell attaching map and a mod-24 congruence. Its general
existence conclusion concerns some bundle, not prescribed arbitrary
Chern data. Here H^2(X,Z) is nonzero, so that setting fails. No
primitive-class or highly connected theorem is imported onto X.

Reuse the
[prior corrected-data assessment](2026-10-04-corrected-point-rank-two-integrality.md)
for Fulton/Stacks rank truncation, characters, Todd classes and HRR.
The previously inspected Maciocia Fourier--Mukai results have extra
kernel hypotheses. Further browsing of those adequate sources is
unnecessary. Their supporting role and the product-line filter's
exhaustion are unchanged.

### Gap, discrimination and continuation limits

The main local gap is an actual compatible representative that could
reach the fourth NS-fixed RM direction. The intermediate target is
topological rank-two realization of the corrected full second
character. This can reject impossible data before trying holomorphic
construction, rather than repeat the exhausted product-line indices.
No complete passage from a topological bundle to that direction is
asserted: holomorphic local freeness, polystability, invariant classes
and transverse transport would still need proof.

The separate research test should evaluate both cited conditions,
beginning with the saved symmetric survivor. A failed condition stops
that input. Coverage also permits determining the full admitted
integer region without another review: retain the same fixed tensor,
vary a,b, and compare with the required zero mod-12 residue and
vanishing cohomology operation. An empty region stops these corrected
rank-two data. A nonempty region settles only topological existence
for its members and shifts the bottleneck to holomorphic construction
and compatibility; repeatedly testing equivalent topological or
ordinary index conditions would not add evidence.

Local redundancy checks found no existing evaluation of this
quaternionic-line criterion. L045 fixes a different K-class, L046
excludes unchanged lower data, and L048--L049 give only the corrected
arithmetic tests. Preserve those stops and the undoubled/presentation
exclusions with their original scopes. Parked original-source access
leads remain parked; no essential unread source blocks this target.

The known cycle span remains 21 and the attained RM directions three
against four required. General primitive fourfold classes and the
universal rational Hodge target are still unresolved. Mathematical
exploration usage stays zero: this literature turn spends no
calculation turn and supplies no new lemma or script.

### Search record and scope limits

Queries on CHECKED included:

- `SU(2) bundles 8 dimensional manifolds second Chern class realization Cadek Crabb Vanzura`
- `rank 2 complex vector bundles eight dimensional spin manifolds second Chern class quaternionic`
- `"Obstruction theory on 8-manifolds" Cadek Crabb Vanzura 2008`
- `"SU(2)" "8-manifolds" "c2" bundle`
- `"SU(2)" "K3" "product" "bundle" obstruction`
- `"Corollary 8.4" "Cadek" quaternionic`
- `"SU(2)-bundles over highly connected 8-manifolds" arxiv`
- `"Obstruction theory on 8-manifolds" correction quaternionic line`

Search returns about arbitrary eight-complexes, instanton gluing,
Spin(7), gauge-group homotopy, and a 2021 quaternionic-projective-plane
paper were leads only. The NSF-hosted PDF for the last lead failed to
open; it is not essential after reading the direct closed-manifold
criterion. Nonprimary snippets supplied discovery, not theorem
evidence. The checked general theorem covers the realization
framework; the search did not identify an evaluation of this fixed
corrected RM character. That observation certifies no novelty.

## Mathlib

Coverage: **not checked** for the full realization target, the
quaternionic-line criterion, or its supporting characteristic
operations. No declaration name or absence from checked Mathlib
sources is asserted. Corollary 8.4 matches the general finite-rank
existence question; Huybrechts and the earlier character/index sources
are supporting inputs. None evaluates the specific saved survivor
here. Library lookup is optional and unnecessary for this assessment.
