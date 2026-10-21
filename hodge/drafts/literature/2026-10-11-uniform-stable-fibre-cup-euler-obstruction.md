# Uniform stable-fibre determinant cup/Euler test — source comparison

TARGET: Test a uniform Euler-characteristic obstruction for L071-admitted correction pairs with neither factor charge of the form 14r^2, using both actual images and the determinant cup-square identity.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 227 searched rank-two K3-product Euler, hyperholomorphic H^1 cup, determinant cup-square, polystable positive Euler and stronger cohomological Lefschetz statements; compared L071/L090/L091 and ATTEMPTS/042/043/051/057/058. No matching uniform exclusion theorem was identified in inspected results; no novelty is inferred.
SOURCE_EVIDENCE: Freshly read Stacks live 2026-10-11, 33.33.1/5 (0BEI), 72.17.3 (0EDD) and 48.3.6 (0A9Q), including relevant proofs, and Charles's author-hosted draft Sections 3--4, Lemma 15 proof, Theorem 18 and Theorem 3 proof, pp. 10--16; reused step-223/225 BBHR, K3 RR/stable-Hom, perfect-base-change and cup/trace coverage with locators below.
COMPARISON: General sources cover finite Euler sums, proper-pushforward Euler bookkeeping, arbitrary-rank preservation, coherent duality and actual-map comparison. L090/L091 supply the audited cup identity/method but only exact-pair exclusions. Charles uses End-valued deformation products and an irreducible hyperkahler target, so it does not import this coefficient obstruction.
GAP: Separately justify both all-fibre concentrations, both actual preserved images and section-form perfection for variable dimension; test whether chi(X,F)<0 is the precise Euler-only threshold forcing common sections, then delimit the region and retain its boundary. No uniform implication or region is proved here.
REASON: Essential source scope is covered; approve one separate REPRODUCTION specialization of the saved uniform target. Reprove none of the general theorems; prove only the changed parameter-domain and finite-dimensional applications.
LITERATURE_REASON: The changed uniform domain required comparison beyond exact-pair assessments; essential unread input was finite Euler bookkeeping and proper pushforward, with a bounded stronger-result search.
SCOPE: L071's identical marked K3 factors, full negative tensor -tau_D, unchanged real h and Omega, hypothetical locally free rank-two Omega-polystable F with integral c_1=0, admitted integral (a,b), neither charge -(a+4) nor -(b+4) equal to 14r^2 for any integer r; initial higher characters unrestricted subject to rank truncation. Both actual images, arbitrary common section dimension and Euler/cup only; no inverse, L079 branch, chosen image, cross-notebook input or transport.

## Retained target and relevance

Keep L071's marked S, full negative mixed tensor, unchanged h and Omega,
and hypothetical locally free rank-two Omega-polystable F with integral
c_1=0 and ch_2=(a+4)e_1+(b+4)e_2-tau_D. Let (a,b) range over L071's
admitted integral region, and exclude from this proposed scope pairs
with either factor charge -(a+4) or -(b+4) equal to 14r^2 for an integer
r. Initial higher characters remain unrestricted subject to rank two.

The main gap remains universal primitive rational Hodge realization.
An exact uniform necessary condition could select which common-kernel
data still warrant construction work, without constructing a bundle,
cycle or transverse deformation. The proposed test varies the actual
image ranks and section dimensions rather than repeating the exhausted
numerical tests for the two already excluded pairs.

Essential local inputs for comparison are L071's full character and
exact-h factor tests, L090's audited coefficient identity and actual-map
method, and L091's audited arbitrary-rank opposite preservation and
trivial-part argument. L073/L074 remain exact forward-image comparisons,
not a theorem for the enlarged domain. No L079 branch enumeration,
independently chosen image, inverse or cross-notebook result is assumed.

Unresolved obligations are both every-fibre concentration and compatible
preservation throughout this domain, an exact Euler criterion forcing
nonzero common sections, perfection of both section forms, and the
resulting precisely delimited exclusion region. No such criterion or
region is derived in this proposal. Continue only if source comparison
covers these obligations and identifies a concrete threshold to test;
if it does not, narrow or replace the target rather than assuming that
the two fixed-pair proofs already establish it. Split factor fibres
and equality or other cases not excluded by the eventual test must be
retained as unresolved unless separately justified.

Reuse the existing inspected sources where applicable. Check exact and
stronger known statements, duplicates and ATTEMPTS/042, 043, 051, 057,
058 before approval; their numerical stops are not global bans. The
independent analytic SOURCE_BLOCKED route stays parked. Mathlib coverage
is not checked. The original target is retained. The comparison below
grants source-scope approval for a separate mathematical invocation;
it proves no uniform obstruction or correction-region conclusion.

## Completed source comparison, step 227

**Euler input and proposed threshold.** Read
[Stacks 33.33, 0BEI](https://stacks.math.columbia.edu/tag/0BEI),
Definition 33.33.1 and Lemma 33.33.5 with its full proof. A coherent
sheaf on a proper scheme over a field has a finite alternating sum of
finite cohomology dimensions. For f:Y->B between proper schemes over
that field and coherent E,
chi(Y,E)=sum_i (-1)^i chi(B,R^i f_*E). Its proof uses finite coherent
higher images and Leray; the total alternating dimension is unchanged
on each page and agrees with the limiting filtration. X, S_i and F
after projective GAGA meet the hypotheses. There is no rank bound or
Fourier-equivalence hypothesis. This supplies bookkeeping, not a
nonzero-section theorem.

Also read [72.17.3, 0EDD](https://stacks.math.columbia.edu/tag/0EDD)
and its proof, the algebraic-space counterpart. Its last filtration
sentence prints p+1=n; the scheme proof correctly prints p+q=n.
Use the scheme statement/proof here. This textual qualification is
not a new mathematical result.

Reuse Huybrechts, *Lectures on K3 Surfaces*, author-hosted
[prepublication draft](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf),
Chapter 1 (2.5)--(2.6), Proposition 2.4, pp. 11--13, and Chapter 9
Section 3.1(ii)--(iv), pp. 175--176, for RR, Serre duality, dual
stability and equal-slope stable-Hom. These allow arbitrary image
rank and stable summands, including nonzero individual first classes;
they do not guarantee sections for an arbitrary polystable bundle.

The concrete threshold to test in research is **chi(X,F)<0**,
compared through actual single-row Leray with a **strictly positive
actual-image Euler characteristic**. These are proposed tests, not
established equivalents or an exclusion. Justify the signs,
self-duality and dimension inequality, and determine what the zero
or other side permits. Retain L071's full Euler formula rather than
an exact-pair index. No new formula or region is derived here.

**Concentration and preservation in both directions.** Reuse the
inspected evidence in
[step 223](2026-10-11-flat-exception-determinant-cup-square.md) and
[step 225](2026-10-11-flat-exception-cup-square-critical-audit.md).
Bartocci--Bruzzo--Hernandez Ruiperez, *A hyperkahler Fourier transform*,
Differential Geometry and its Applications 8 (1998), 239--249,
[Sections 3.1--3.3, Definition 2, Lemmas 1--2 and Theorem 3,
pp. 243--246](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf),
requires compact hyperkahler source, compatible spheres, hermitian
quaternionic-instanton kernel and a source instanton satisfying IT
at every parameter. Neither image rank nor mixed-tensor sign is
restricted. Both sources are flat O_{S_i}; L071 supplies the
hypothetical compatible kernel connection. Prove every-fibre IT
using the excluded split charges and actual factor test before
applying it; a generic fibre or total Euler value is insufficient.

Reuse Verbitsky [math/0107182v10](https://arxiv.org/pdf/math/0107182v10),
Definition 2.1, p. 9, Proposition 3.7/Lemma 3.8, pp. 12--13,
Theorem 3.9, pp. 13--14, and Huybrechts Chapter 9 Theorem 4.9,
p. 182. Invariant full Chern classes and an actual stable connection
are required; surface contraction and Kobayashi--Hitchin cover the
same real-h polystability, allowing reducibility. No positive-sign
curvature conclusion is imported.

Reuse [Stacks 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H),
its inspected Noetherian proof case, and
[36.31.3, 0BDK](https://stacks.math.columbia.edu/tag/0BDK), full proof.
Assign the proper flat finitely presented projections, perfect O_X
and bounded base-flat F[0]. The degree-one bundle-locus criterion
permits arbitrary rank; prove concentration on every closed derived
fibre and the empty-complement passage before ordinary base change.

**Duality, sections and the same class.** Reuse step-225's Stacks
48.19(2),(9) (0AU3), 48.15.7 (0BRT), 48.12.4 (0AAB),
48.6.2 (0AA8) flat finite-presentation case and 48.7.1 (0B6J)
unit/counit proof. Freshly reread
[48.3.6, 0A9Q](https://stacks.math.columbia.edu/tag/0A9Q), statement
and projection-formula/adjunction proof: the general internal-Hom
comparison becomes an isomorphism after DQ. Retain the qualification;
use bounded coherent/perfect coefficients, smooth proper relative
dimension two, base O and omega_p[2]. There is no rank-two image
restriction in these duality statements.

Restriction of a perfect bundle form to sections needs the full
trivial isotypic part and vanishing of both cross blocks by stable-Hom.
L091 supplies the audited method for arbitrary-rank opposite H,
but its fixed O^2 count is not uniform input. Variable dimension,
including zero, is to be tested. Complex symmetric forms can have
isotropic vectors, so anisotropy is not available.

Reuse Demailly [alg-geom/9410022v3, 28 February 1995](https://arxiv.org/pdf/alg-geom/9410022v3),
Section 1.A (1.1)--(1.3), pp. 4--5, Section 4.A (4.3)--(4.4'),
pp. 27--28, for coefficient Dolbeault and Serre pairing. Reuse
step-219/225's Stacks 20.13.1/4 (01EZ/01F2), 20.28.3 (08HY),
20.31.3/7/8 (0FP3/0FP6/0H99), 15.59 (0GWN), 36.23.1 (0FLN).
The general cup/base-change proof in 0H99 is omitted; retain that
qualification. Both actual concentrated images and counit base-change
isomorphisms must precede trace comparison on the **same** global
class and determinant trivialization. Closed-fibre squares are Tor
independent by flatness of the projections, not of the point maps.
Trace constants must be nonzero; no phase or positivity is imposed.

L090's audited rank-two identity and actual-map method do not require
its correction pair or image dimensions. Simultaneous quadratic
nonvanishing in arbitrary positive finite dimension remains an
elementary linear/polynomial-algebra application to write in research.
No new version is proved here and no general theorem needs reproof.

## Search, overlap and prior failures

Queries on 2026-10-11 included `"K3" product "rank two" bundle
"Euler characteristic" hyperholomorphic`, `"hyperholomorphic"
"cup product" "H^1"`, `"rank two" bundle "determinant" "cup square"
cohomology`, `"hyperholomorphic bundles" "Euler characteristic"
cohomology`, `"K3" "polystable" "positive Euler characteristic"
bundle`, and `Verbitsky hyperholomorphic bundles cohomology H1
Lefschetz theorem`. Source-location searches found Stacks Euler
statements and Charles's paper. Search snippets and abstracts are
not theorem evidence; only inspected primary passages are used.

Charles, *Remarks on the Lefschetz standard conjecture and hyperkahler
varieties*, Comment. Math. Helv. 88 (2013), 449--468, was compared via
the [author-hosted 20-page draft](https://www.imo.universite-paris-saclay.fr/~francois.charles/Lef_cmh_3.pdf).
Read Section 3's coefficient construction, Lemma 15 with its
Atiyah/Yoneda/trace proof, pp. 10--12, Theorem 18, p. 13, and
Section 4.2's Theorem 3 proof, pp. 15--16. These concern
Ext^1(E,E), rather than H^1(F), and a nonzero deformation trace on an
irreducible projective hyperkahler variety. S x S does not meet that
irreducibility hypothesis. No stated Euler cutoff or this uniform
determinant exclusion is supplied. Initial ENS PDF retrieval failed;
the alternate author PDF succeeded. Theorem 16 refers to additional
Theorem 12 hypotheses and is not imported or assumed applicable.

Verbitsky's quaternionic-Dolbeault line-bundle vanishing paper appeared
as an abstract-only lead. Its full theorem/proof was not inspected
and is not imported for rank-two F. Other representation leads remain
unread and are not essential to this bounded test. No essential source
blocker remains; neither absence nor originality is inferred.

The requested ATTEMPTS/042/043 stop the older compatible two-projection
and residual parity/index mechanisms; ATTEMPTS/051 stops the exact
six-charge character filter. ATTEMPTS/057/058 and audited L090/L091
already exclude two exact pairs. The uniform Euler-to-section test
is the remaining difference; another exact-pair calculation would
duplicate them. Keep all stops and individual existence results.
The analytic SOURCE_BLOCKED route stays parked. No L079 branch
enumeration or cross-notebook input is used.

## Separate bounded attempt and decision test

Approve the exact TARGET as SPECIALIZE for a separate REPRODUCTION
attempt. Establish or refute the strict Euler threshold using both
actual images; if it forces positive common section dimension, test
section perfection and the same-class cup contradiction uniformly,
then state the exact region obtained from L071. Do not assume the
whole admitted domain is excluded. Equality, the other Euler side
and split-fibre charges remain unresolved unless separately justified.
A failed concentration, form or threshold bridge requires recording
that failure and narrowing or stopping this mechanism. A compatible
necessary condition supplies no kernel.

Essential input IDs are L071, L090's audited identity/actual-map
method and L091's arbitrary-rank/trivial-part method. L073/L074
cover only their original slice and are comparisons, not inputs for
the enlarged domain. F remains hypothetical with exactly SCOPE's
assumptions. Common-kernel existence, transport and universal primitive
Hodge realization remain independent gaps. Full matching and supporting
Mathlib coverage is **not checked**, which is not evidence of absence.
This turn writes no new lemma, script, PROOF argument or DAG row.
