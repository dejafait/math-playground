# Stable resolutions using several divisor classes — literature assessment

TARGET: Assess whether a stable resolution of I_C using line-bundle summands from several divisor classes can have SU(2)-invariant c_1 and c_2 for L025's common metric and ch_2 action cU on T(S), for some nonzero rational c.
CHECKED: 2026-09-27
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched mixed-polarization stable resolutions, syzygy stability, monads on projective and multiprojective varieties, and hyperholomorphic RM bundles; followed the monad stability reference to its original criterion and checked a withdrawn general-stability claim. Queries and reading scope are recorded below.
SOURCE_EVIDENCE: Mistretta, arXiv:math/0310185v2, Theorems 3.1--3.2, https://arxiv.org/pdf/math/0310185v2#page=7; Jardim--Menet--Prata--Sa Earp, arXiv:1109.2750v5, Theorem 3, https://arxiv.org/pdf/1109.2750v5#page=5; Marchesi--Macias Marques--Soares, arXiv:1801.00151v1, Theorems 3.3--3.4 and Corollary 5.3, https://arxiv.org/pdf/1801.00151v1#page=7; further statements and qualifications below.
COMPARISON: The inspected resolution theorem uses one polarization; broader stability criteria test an existing bundle, and the inspected monad constructions do not provide the required mixed resolution of I_C with stability at L025's metric and invariant full Chern classes. No full existence or nonexistence match was found.
GAP: Determine whether an actual mixed line-bundle presentation can pass both the metric-specific map/stability constraints and the full Chern-data test; formal divisor tensors do not supply its maps, exactness, stability or escape from map recovery.
REASON: The changed construction is not covered by L026 or by a cited existence theorem. Permit one bounded presentation-feasibility test in a separate research turn, starting with slope constraints on its terminal inclusion, and retain the exact target without claiming novelty.

## Hypotheses

Retain the very general cubic S, correspondence C, operator U, and a
choice of the common metric class omega supplied by L025. Put X=S x S.
The terminal object must be an actual locally free bundle slope-stable
for p_1^*omega+p_2^*omega. The diagonal SU(2) action comes from this
same metric on both factors. Presentation terms may be finite sums
of line bundles from differing divisor classes on X.

The requirements concern both full Chern classes and the ch_2 action
cU on T(S), with c rational and nonzero. An arbitrary corrected tensor,
a virtual K-class, a stable bundle for another polarization, or merely
an invariant discriminant does not fulfill the target. L025's operator
is not assumed to be realized by Chern classes.

Reuse the unchanged [rational-target audit](../../foundations/01-target-and-scope.md),
[prior bundle assessment](2026-09-27-compatible-cubic-rm-stable-bundle.md),
and [hyperholomorphic assessment](2026-09-27-hyperholomorphic-cubic-rm-representatives.md)
for their stated background scopes. This review addresses the changed
presentation terms, not the previously rejected one-polarization recipe.

## Conclusion

The exact saved target has a completed EXPLORE assessment. The bounded
search did not locate a theorem supplying or excluding all the requested
mixed resolutions. Known construction and stability tools must be cited;
their combination is not an existence theorem for this target. The
decision admits a scoped future test under the literature policy;
it does not assert that the recipe works or is original.

The gap addressed is an algebraic representative of the cubic action
that might reach V_RM outside V_D. Compatible bundle existence could
justify a later transport test. Transport into that particular NS-fixed
direction would still require proof, even after hyperholomorphicity.
The attained span remains 21-dimensional on the known family, with
three attained directions against four required. Arbitrary primitive
fourfold classes and higher-dimensional cases remain unresolved.

This step is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION, using one
exploration turn after L026. No new Chern identity, bundle, exclusion,
deformation calculation or mathematical lemma is asserted. There is no
complete candidate. The initial pending scope and the interim source
checkpoint have been incorporated into this completed comparison.

## Proof

The evidence consists of theorem statements and comparisons of hypotheses.
No specialization is proved in this section.

### Stable resolutions and evaluation kernels

Reread Mistretta, *Stable vector bundles as generators of the Chow ring*,
[arXiv:math/0310185v2, 15 March 2007, Theorems 3.1--3.2,
p. 7, and the curve-restriction setup, pp. 7--8](https://arxiv.org/pdf/math/0310185v2#page=7).
Theorem 3.1 supplies a stable locally free terminal bundle in a resolution
of an ideal sheaf, with each presentation term a vector space tensored
with O_X(-m_i H), for one ample H. Its curve argument uses Butler's
stable evaluation-kernel theorem for a stable bundle of slope greater
than twice the curve's genus. Arbitrary mixed line-bundle terms are not
a conclusion of either statement. The prior assessment's Chow-generation
comparison is reused; it does not realize prescribed Chern data in one
bundle. On this fourfold the stated resolution has three presentation
terms, as retained in L026.

Read Ein--Lazarsfeld--Mustopa, *Stability of syzygy bundles on an algebraic
surface*, [arXiv:1211.6921v1, 29 November 2012, Theorem A and
Proposition C, pp. 1--2](https://arxiv.org/pdf/1211.6921v1#page=1).
Theorem A treats evaluation kernels for sufficiently positive line
bundles on surfaces. Proposition C extends a case to higher dimensions
under a cyclic Picard-group hypothesis. Neither is the desired theorem
on this product or an arbitrary mixed presentation of its ideal.

The search also returned Shijie Shang, *Stability of syzygy bundles on
smooth projective varieties*. Read the [arXiv:2104.10271v2 withdrawal
record, 24 April 2021](https://arxiv.org/abs/2104.10271v2).
The author reports an incorrect degree inequality on p. 4 that invalidates
the proof. Exclude the claimed general theorem as an input; the withdrawal
does not disprove that statement. The original attempted proof was not
assessed.

### What the monad results actually construct

Read Marchesi--Macias Marques--Soares, *Monads on projective varieties*,
[arXiv:1801.00151v1, 30 December 2017, Theorems 3.3--3.4,
pp. 7--9](https://arxiv.org/pdf/1801.00151v1#page=7), and
[Corollary 5.3, p. 17](https://arxiv.org/pdf/1801.00151v1#page=17).
Their monads use L^vee, O_X and L. Existence is characterized by
b>=a+c and b>=2c+n-1, or b>=a+c+n, with a base-point-free system
whose image is ACM, or linearly normal and contained in no quadric,
respectively. The stated stable-bundle corollary concerns rank two on
an ACM threefold with Pic(X)=Z. These conclusions neither prescribe
the present I_C as a resolved ideal nor provide a mixed-divisor
fourfold bundle stable at the specified irrational metric. No
applicability of the image hypotheses to the present X is asserted.

Read Maingi, *Vector Bundle construction via Monads on multiprojective
Spaces*, [arXiv:2301.04932v4, 12 September 2023, Theorems 4.1--4.3,
pp. 12--14](https://arxiv.org/pdf/2301.04932v4#page=12).
The ambient varieties are products of projective spaces. The displayed
terms use one chosen multidegree; the statements distinguish stability
of the kernel bundle from simplicity of the monad cohomology. This is
a scope comparison only: no construction or stability statement is
imported to S x S. The paper's stability reference was followed to the
original criterion below rather than assumed to provide mixed-term
existence.

### Applicable criteria still require a bundle and maps

Read Jardim--Menet--Prata--Sa Earp, *Holomorphic bundles for higher
dimensional gauge theory*, [arXiv:1109.2750v5, 21 February 2017,
Theorem 3 and proof, p. 5](https://arxiv.org/pdf/1109.2750v5#page=5).
For Pic(X)=Z^l and an ample line-bundle polarization L, stability
follows from vanishing of H^0(X, wedge^s G tensor O_X(B)) for every
0<s<rank(G) and every B with deg_L(B)<=-s mu_L(G).
The semistable criterion uses the strict inequality. This tests an
existing bundle; it neither constructs the desired resolution nor
establishes these vanishings at omega. Its ample-line-bundle formulation
is not silently replaced by the irrational metric. The same paper's
[Theorem 12, p. 10](https://arxiv.org/pdf/1109.2750v5#page=10)
requires a codimension-two local complete intersection for its
Hartshorne--Serre construction. L007's three non-lci points prevent
direct application to the existing C.

For a metric-specific necessary map test, read McCarthy,
*Stability conditions and canonical metrics*,
[arXiv:2302.04966v1, February 2023, Proposition 2.2.4(i),
printed p. 20, PDF p. 36](https://arxiv.org/pdf/2302.04966v1#page=36).
It states that Hom(E,F)=0 for slope-semistable sheaves on a compact
Kahler manifold when mu(E)>mu(F). This is an explicit restatement
attributed to Kobayashi, Proposition 5.7.11 and Corollary 5.7.12.
Only the displayed vanishing statement is used as a known supporting
criterion; no slopes of a proposed resolution have been evaluated.
The original book PDF was inaccessible, so no reading of it is claimed.

Reread Verbitsky, *Hyperholomorphic bundles*,
[arXiv:alg-geom/9307008v1, 29 July 1993, Proposition 1.2, p. 4;
Lemma 2.1, p. 7; Theorem 2.5, p. 9](https://arxiv.org/pdf/alg-geom/9307008v1#page=9).
The theorem makes a stable bundle hyperholomorphic if its first two
Chern classes are invariant; invariant two-forms have zero contraction
with the induced Kahler forms. The product is allowed, but bundle
existence and stability for its metric are hypotheses. These tools
support the proposed necessary-condition test. They do not prove
that changing presentation divisors supplies a compatible bundle.

### Existing exclusions and the precise remaining difference

Reread [L026](../../lemmas/L026-stable-resolutions-fail-common-metric-chern-test.md)
and [Attempt 017](../../ATTEMPTS/017-single-polarization-stable-resolution.md).
The rank-one divisor correction and twist-invariant obstruction stop
the specified one-polarization terms, including final twists. Varying
their exponents or retwisting cannot reopen that result. Different
divisor classes change its hypotheses; that is a reason to test them,
not a proof that their actual resolution data fill the missing tensor.

Reread [L012](../../lemmas/L012-second-syzygy-retains-cubic-obstruction.md)
and [Attempt 009](../../ATTEMPTS/009-second-syzygy-of-cubic-ideal.md).
Its two sufficiently negative presentations have vanishing
Ext^1(E,F_1) and Ext^1(K,F_0); these recover the maps and then I_C.
A different number of terms or different divisors is not verbatim
covered. Any proposed negative mixed presentation must check the
corresponding groups on its actual intermediate kernels. Stability
alone is not an escape, and nonvanishing of a possible obstruction
group alone would not exhibit a transverse lift.

Reuse the prior assessment's distinction between a numerical second
Chern bound and a prescribed full class. Its quadratic-RM, isometry,
Hilbert-scheme and conditional propagation comparisons remain
background; none is upgraded to a mixed-resolution construction.

### One bounded continuation for the unchanged target

In a separate research turn, first test presentations whose terminal
line-bundle summands are anti-ample but may come from different divisor
classes. Compare their slopes, the required stable terminal bundle,
and invariant c_1 using the read metric-specific morphism criterion.
This asks whether their terminal inclusion can exist; no answer is
asserted here. Keep any allowed final twist in the test by checking
the actual twisted maps. A conclusion for the untwisted anti-ample
case must not be extended to arbitrary summands or twists without proof.

If that necessary test survives, use only presentation data consistent
with actual maps, ranks and exactness to test the full c_1,c_2 condition,
including the mixed divisor tensor. Check overlap with L012 at the
actual presentation length. A solution in a vector space of tensors,
or an arbitrary alternating sum of line-bundle characters, must be
labelled formal and is not an actual construction.

Continue only if the test supplies an admissible concrete presentation
candidate with a bounded remaining construction check, or an informative
scoped obstruction that changes the route. Stop a recipe when its
necessary map, stability, Chern or recovery conditions rule it out;
do not turn that into nonexistence for every compatible bundle.
If the only surviving output is unconstrained formal Chern data,
reassess rather than iterate divisor choices without a mechanism.

This review uses turn 1 of the three-turn exploration window.
Two turns remain without an advance or informative negative result;
complete the continuation/stop decision by turn 3, and reassess after
two unproductive turns. No test in this paragraph was carried out here.

### Search and access record

Queries on 2026-09-27 included:

- `"stable resolution" "line bundles" "polarization" Mistretta`
- `"stable resolutions" "line bundles" "different polarizations"`
- `"syzygy bundles" "several" "line bundles" stability`
- `"stable" "monads" "K3" "product"`
- `"hyperholomorphic" "real multiplication" "Chern"`
- `stable vector bundles monads arbitrary smooth projective variety line bundles different degrees Picard number`
- `syzygy bundles stability vector bundle arbitrary dimension Ein Lazarsfeld Mustopa theorem`
- `"monads" "multiprojective spaces" stable vector bundles`
- `"Monads on projective varieties" Macias Marques Soares theorem arxiv`
- `"generalized Hoppe" "polycyclic" stability`
- `"Holomorphic bundles for higher dimensional gauge theory" arxiv`
- `"semistable" "slope" "Hom" "Kahler" vector bundles proposition`
- `"Kobayashi" "Proposition 5.7.11"`

Title/author follow-ups supplied the pinned texts above. PDF text was
read; no screenshot or complete-proof audit is claimed. An initial
request for a nonexistent v2 of arXiv:1801.00151 failed; its record
lists v1, which was read. The Shang current PDF request failed before
the withdrawal record resolved its status.

Kobayashi's [MSJ book PDF](https://www.mathsoc.jp/assets/pdf/publications/pubmsj/Vol15.pdf)
remains unread. The exact supporting vanishing was read in McCarthy's
attributed restatement, so the proposed test has no dependency on an
uninspected stronger book claim. Also inspected Anthony Mäkelä's
author-hosted *The Atiyah Class on Calabi--Yau Manifolds* (undated),
[Proposition 4.1.11(i), printed p. 50](https://anthonymkel.com/assets/The_Atiyah_Class_on_Calabi__Yau_Manifolds.pdf#page=51),
which states the same vanishing; it adds no construction theorem.

Search leads on Ulrich bundles, more recent multiprojective monads,
and quiver descriptions were not read as theorem-level sources and
are not inputs. No selected input depends on an unread lead.
This is a bounded screen, not an exhaustive novelty assessment or
proof of absence from the literature.

## Mathlib

Coverage: **not checked** for the full target or the supporting
resolution, stability and hyperholomorphic results. The named theorems
and direct links above are mathematical references; none is a full
match for the requested mixed resolution. No Mathlib declaration or
absence from checked Mathlib sources is asserted.
