# Determinant cup-square exclusion — critical-audit source coverage

TARGET: Critically audit L090's determinant cup-square exclusion of both L079 branches, including the two actual restriction-to-Serre comparisons.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step-219's exact coefficient-cup/Plucker search and inspected source comparison; scoped L090/L079 and histories 219/220, ATTEMPTS/055/056/057; focused Stacks trace/base-change queries located 48.7.1 and 48.12.4. No new broad novelty search or matching full exclusion theorem is claimed.
SOURCE_EVIDENCE: Reused Demailly alg-geom/9410022v3 Sections 1.A (1.1)--(1.3), pp. 4--5, and 4.A (4.3)--(4.4'), pp. 27--28, and step-219's product/Kunneth/duality coverage; freshly read Stacks 20.13.1/4 (01EZ/01F2), 20.28.3 (08HY), 20.31.8 (0H99), 48.3.6 (0A9Q), 48.4 setup and 48.4.1 (0E4G), 48.5.0.1 construction (0AA5), 48.6.2 (0AA8), 48.7.1 (0B6J), 48.12.4 (0AAB), live 2026-10-11, including the essential proof cases described below.
COMPARISON: Known composition, counit-defined coefficient base change, cup compatibility and trace base change cover the new audit bridges at the smooth proper K3 projections. These theorems do not state L090's rank-two identity or prescribed common-kernel exclusion; its actual maps, coefficient product, scalars and simultaneous-nonvanishing argument still require independent mathematical review.
GAP: No essential source blocker remains for this exact audit; correctness of L090 equations (2)--(8), especially both evaluations of the same global class and both actual trace comparisons, remains unverified in this literature step.
REASON: Approve one separate critical audit using reused ready machinery plus the newly inspected trace/counit sources; no new exclusion, enlarged charge range or reproof of the general theorems is authorized by this comparison.
LITERATURE_REASON: The newly written critical-audit target needs separate scope approval; its precise edge/evaluation and relative-to-fibre trace bridges warrant the narrow primary-source additions beyond step-219's general duality coverage.
SCOPE: Exactly L090 under L079's rank-two locally free Omega-polystable F, integral c_1=0, full ch_2=-9e_1-10e_2-tau_D on the identical marked K3 product; both actual base-changing odd images and perfect symmetric trivial-part forms, t=1 or 2. No inverse transform, projector lift, independently chosen image identification or cross-notebook theorem is an input.

## Reused coverage and relevance

The ready [step-219 assessment](2026-10-11-common-kernel-determinant-cup-square.md)
remains unchanged. Its exact search, Demailly coefficient-resolution and
Serre-pairing evidence, graded signs, cup composition, scalar Kunneth
and smooth proper duality are reused. The changed-sign rank-two-duality
assessment supplies its inspected 48.3.6 proof and the qualification
on quasicoherent internal Hom. No repeat retrieval of Demailly's
previously blocked author-hosted books is needed; the archived v3
already resolves the essential coefficient-model coverage.

The main gap remains algebraic realization of arbitrary primitive
Hodge classes. The intermediate target is independent verification
of the exact common-kernel exclusion. A sound exclusion would justify
retiring that recipe despite the independent image blocks; a failed
bridge would require correcting or narrowing the existing argument.
Neither finding realizes a Hodge class or supplies transverse transport.

Read L090's full proof and L079's exact hypotheses, actual image and
pairing construction, Leray passage, trivial-part argument and existing
critical audit. Histories 219/220 distinguish source approval from the
completed attempt. ATTEMPTS/055/056 retain the exhausted projector
and half-adjoint filters; ATTEMPTS/057 records the new scoped stop,
which is still pending mathematical audit. No duplicate global-cup
exclusion was identified in these scoped records. This is not a
novelty claim, and no earlier stop is used as a global prohibition.

## Added primary statements and essential proof cases

**Composition and the actual maps.** Freshly read
[Stacks 20.13.1, 01EZ](https://stacks.math.columbia.edu/tag/01EZ),
including its injective-to-acyclic composition proof, and
[20.13.4, 01F2](https://stacks.math.columbia.edu/tag/01F2).
For a morphism of ringed spaces the former identifies derived global
sections with those of the derived pushforward, also on inverse
images of open subsets; the latter gives Leray for bounded-below
coefficient complexes. F in degree zero is within that scope. These
are composition/edge machinery, not an assertion of multiplicative
Leray or an automatic fibre base-change isomorphism.

Freshly read [20.28.3, 08HY](https://stacks.math.columbia.edu/tag/08HY).
It constructs the canonical derived base-change map for a commutative
ringed-space square as the adjoint of the pulled-back counit.
This supplies an explicit source construction for auditing L090's
claim that evaluation of its actual edge section is fibre restriction.
The equality on the particular degree-one class is still an audit
obligation; no proof of that specialization is performed here.

Rechecked [20.31.8, 0H99](https://stacks.math.columbia.edu/tag/0H99):
relative cup commutes with those base-change maps for derived
coefficients in a commutative square. Its proof is omitted in the
source, as already recorded. It does not itself assert the maps
are isomorphisms. L079's every-fibre concentration and locally free
images are the separate local inputs to be retained. Smooth fibre
inclusions pull back locally free F without an extra coefficient
Tor term. The same determinant wedge must be used throughout.

**Trace and dualizing base change.** Focused queries were
`site.stacks.math.columbia.edu "trace map" "base change" "48.7"`,
`site.stacks.math.columbia.edu "base change" "counit" "proper" "48.6"`
and `site.stacks.math.columbia.edu "Lemma 48.6.2" "proper"`.
Search results located statements; the primary pages and essential
proofs were then read, rather than importing snippets.

Read the quasi-compact/quasi-separated cartesian-square setup and
48.4.1 in [48.4, 0E4G](https://stacks.math.columbia.edu/tag/0E4G),
and the unit/adjoint/counit construction of 48.5.0.1 in
[48.5, 0AA5](https://stacks.math.columbia.edu/tag/0AA5).
Tor independence permits inversion of the adjoint transformation
used in that construction. Only the introductory construction is
needed from 48.5; no use of its later stacking lemmas is proposed.

Read [48.7.1, 0B6J](https://stacks.math.columbia.edu/tag/0B6J),
its full statement and unit/counit proof. In the preceding cartesian
setup, under Tor independence, relative trace and the fibre trace
commute through the pushforward and right-adjoint base-change maps.
The proof identifies the actual transformations using adjoint mates
and the unit/counit identities. This is the precise trace-compatibility
source missing from the earlier explicit audit-scope evidence.

Read [48.12.4, 0AAB](https://stacks.math.columbia.edu/tag/0AAB):
for a proper flat morphism of finite presentation and a base change
of quasi-compact quasi-separated schemes, the right-adjoint
base-change map is an isomorphism on all D_QCoh coefficients.
Its proof reduces to affine bases and 48.6.2. Accordingly read
[48.6.2, 0AA8](https://stacks.math.columbia.edu/tag/0AA8),
retaining its affine-base, properness and Tor-independence hypotheses.
Inspected the flat-finite-presentation case: a perfect generator and
perfection of its pushforward yield the Hom comparison; the final
commuting diagram verifies that the comparison is the stated map,
not just an abstract isomorphism. The other alternatives are not
needed here.

For either actual K3 projection, the morphism is smooth projective,
hence proper flat of finite presentation. Source and base are
quasi-compact quasi-separated Noetherian schemes. The closed-point
fibre square is cartesian and Tor independent because the projection
is flat; the point map need not be flat. The duality coefficient is
O on the base. Thus these statements cover the required source scope
in both directions. Reused 48.15.7/48.19 identifies the smooth
relative dualizing coefficient with the canonical line shifted by two.
The later audit must check that the determinant/canonical choices
in L079 and L090 give the claimed fibre scalar comparisons; any
normalization difference must be a nonzero scalar, not an assumed
phase, positivity or equality of independently chosen forms.

Re-read [48.3.6, 0A9Q](https://stacks.math.columbia.edu/tag/0A9Q)
and its adjunction/projection-formula proof. Its general map becomes
an isomorphism after DQ; that qualification is not removed here.
Use the saved bounded coherent proper-duality formulation for F and
O at these Noetherian smooth proper projections. No unqualified
internal-Hom assertion on arbitrary ringed spaces is imported.

## Separate audit boundary and discriminating test

This literature step establishes coverage, not the rank-two identity,
the two scalar comparisons or the exclusion. A later audit must
independently inspect the coefficient Dolbeault product in L090 (2),
its passage to coherent cup, the same V in both edge maps (5), both
actual restriction/trace comparisons (6)--(7), the perfect forms
on all trivial summands and the nonzero scalar Kunneth product.
It must permit isotropic lines for t=2 and check simultaneous
nonvanishing on the same vector, rather than choose two vectors.
The elementary local algebra and these actual-object comparisons
are the identified specialization beyond the cited machinery; no
reproof of Dolbeault, Kunneth, base change or duality is warranted.

Essential local inputs are L090 and L079. L071 is needed only if
inherited full-tensor/identical-metric hypotheses require checking.
No block-existence result, inverse, projector lift, cross-notebook
result or actual image identification is assumed. F remains
hypothetical with precisely the hypotheses in SCOPE; the scalar and
trace bridges remain unresolved review obligations. Mathlib full
matching and supporting coverage is not checked; unknown is not absent.

Preserve L090's exact exclusion only if all these bridges and both
branch contradictions survive independent review. A failed claim
requires an explicit correction or narrowed conclusion preserving
the original work. Broader charge ranges, common-kernel construction,
transport and a complete Hodge argument are outside the approved
audit. STATUS remains IN_PROGRESS. This ready continuation receives
the supervisor's separate next-turn approval before research.
