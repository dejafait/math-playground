# Compressed direction presentation — source comparison

TARGET: Construct and independently verify a compressed scalar-invariant direction-algebra presentation of the conductor-389 seven-incidence maps, with full rational transports to L069's ordered-pair domain.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact p-descent/direction-algebra, scalar-invariant/finite-etale and incidence-compression searches located Schaefer--Stoll's general-p A_+ construction and finite invariant-algebra sources; scoped comparison with L067--L069, the previous incidence assessment, history 247 and ATTEMPTS/021/032--035 found no completed local compressed certificate; no novelty or comprehensive absence claim follows.
SOURCE_EVIDENCE: Schaefer--Stoll, author long version 2001-06-13, Lemma 7.2 and proof pp. 13--14 plus the following general-p paragraph, Lemma 7.5 p. 16 and Proposition 7.10 with its defining paragraph p. 19; Stacks 03QR and 03BE equation 39.23.0.1, Lemmas 39.23.5(3)/39.23.6 and Proposition 39.23.9, and 0BD2; primary hypotheses and essential proof cases read; prior incidence/cohomology and group-law assessments reused.
COMPARISON: The source already supplies the projective-direction algebra A_+ and the general incidence pullback/norm; invariant equalizers support a smaller rational presentation. It supplies neither this model's compressed coefficients/full transports nor an effective cost bound. Only the applicability argument and complete fixed-instance arithmetic remain to be reproduced; the p=3 slope formula is inapplicable.
GAP: The direction basis/kernel, full point-direction component, affine-line relation/equalizer, both inclusions, all inverse coordinates on invariant images, rank-seven basis and universal norm representation are unconstructed; no arithmetic certificate or Selmer bound is imported.
REASON: New essential coverage is Lemma 7.2's general-p scalar-orbit construction; it permits an invariant-first bounded attempt distinct from the stopped full 2016-column translation action, without extending that presentation's caps or claiming a new general theorem.
SCOPE: L067's exact conductor-389 curve at seven; audited L067/L068 and independently replayed L069; invariant-first direction/incidence/line construction, full rational transports on invariant images, determinant norm, independent replay and bounded failure tests; no residual-image, global-unit/class, local-arithmetic or Selmer conclusion.
COVERED_TARGET: Construct and independently verify a compressed scalar-invariant direction-algebra presentation of the conductor-389 seven-incidence maps, with full rational transports to L069's ordered-pair domain.

## Imported inputs and exact source scope

[Schaefer--Stoll, *How to do a p-descent on an elliptic curve*](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
Trans. AMS 356 (2004), 1209--1231, DOI
10.1090/S0002-9947-03-03366-X; theorem/page references here use the
34-page author long version dated 13 June 2001.

Lemma 7.2 assumes an etale algebra from a Galois set with GL(2,F_p)-action
whose point stabilizers meet the scalar center trivially. It gives its
scalar-orbit subalgebra and cyclic degree-(p-1) covering. The proof uses
free scalar fibers; its cohomological part uses character decomposition.
The following paragraph applies this to nonzero E[p], identifying A_+
with projective directions and permitting degree p+1. Its x-coordinate
example is explicitly p=3. Lemma 7.5 identifies affine lines missing zero
with the ordinary linear dual's nonzero elements. Proposition 7.10 defines
the incidence algebra and computes pullback followed by norm through a
p-dimensional multiplication representation. These are known inputs,
not new compressed formulas or a cohomology computation here.

Specialization: Q is a number field, seven is odd, and L067/L068 supply
all nonzero E[7] and its geometric scalar action. The source explicitly
checks the needed stabilizer condition for that set. It does not require
the actual residual Galois image to equal GL(2,F_7). Its direction-degree
requirement is eight and covering degree six. Reuse L068's forward
pullback convention. Do not identify A_+ with the source's affine-line
algebra B_inc or erase its dual/cyclotomic distinction. No L026 premise
is needed for these finite-algebra maps.

[Stacks 03QR, Lemma 58.2.2](https://stacks.math.columbia.edu/tag/03QR)
applies over a field with a separable closure; finite etale algebras are
handled contravariantly via their spectra. Its orbit/stabilizer proof
retains all finite separable factors. Rational geometric identifications,
not sampled roots or a selected field factor, remain obligatory.

[Stacks 03BE](https://stacks.math.columbia.edu/tag/03BE), equation
39.23.0.1, defines invariant functions as an equalizer. Lemma 39.23.5(3)
uses flat base change; its proof identifies the equalizer with a linear
kernel. Lemma 39.23.6 identifies geometric quotient points. Proposition
39.23.9 requires affine schemes, finite locally free source/target maps,
and an equivalence relation; it represents the quotient and its proof
uses flat descent. A compressed correspondence must meet those hypotheses;
a candidate kernel dimension alone does not establish them. This is the
same quotient theorem as in the prior assessment, now compared with an
invariant-first representation rather than a full action matrix.

[Stacks 0BD2, Lemma 31.18.6](https://stacks.math.columbia.edu/tag/0BD2)
requires a finite locally free morphism of fixed positive degree. It
constructs the norm by a multiplication determinant, independent of basis
and compatible with arbitrary base change. The prior incidence assessment
already covers the full-fiber interpretation and source group law; reuse
it without reproof. No general quotient, incidence-sequence or norm
theorem needs a new lemma.

## Permitted construction and unproved implementation obligations

The next attempt may first compute the entire scalar-fixed subalgebra of
L067's A by exact linear algebra using L068, with a complete rational
basis, multiplication and kernel-rank certificate. This is an application
of the imported scalar-orbit theorem; no guessed separating generator is
assumed. A power-basis presentation, if used, must have a full inverse.

The proposed compressed ambient description uses nonzero points together
with projective directions. Its specification retains exactly those
pairs (P,d) with P outside d. The research step must construct this
component rationally, including any idempotent and its complementary
component, and prove its identification with the scalar-orbit quotient
of L069's pairs (P,Q). It must not discard a denominator-zero component
without accounting for it. Required sizes are eight for directions,
384 for the whole point-direction ambient algebra and 336 for the desired
component; these are source-based construction thresholds, not measured
instance ranks. This specification is not a newly proved presentation.

The affine-line algebra must then be built from the complete finite
relation specifying equal affine cosets, with its geometric identification
proved and all rational equalizer identities checked. On representatives,
the prior assessment uses Q -> bQ and P -> P+aQ. A compressed implementation
must justify the relation after removing the choice of Q; it may use
pullbacks to L069 to compare functions. Do not assume that representative
translation induces an automorphism of the intermediate algebra. No such
descent has been proved or approved as a formula in this literature turn.
The required result is the full B_inc of dimension 48 and a degree-seven
incidence map, not an arbitrarily chosen 48-dimensional subspace.

“Full rational transports to L069” means exact inclusions of the smaller
algebras into S, and inverse coordinates on their entire specified invariant
images. Verify both composites there and certify completeness of those
images. It does not mean a two-sided algebra isomorphism between all of
S (dimension 2016) and an algebra of dimension 336 or 48. A linear coordinate
retraction on the ambient space, if provided, must not be called an algebra
homomorphism there without proof. Full basis identities and kernel ranks,
including both L067 coordinate transports, are required; sampled fibers
or one-way substitution do not suffice.

To finish the saved target require both incidence pullbacks, a full
B_inc-basis of D of size seven, multiplication by every element of A's
48-element basis, and complete rational inverse transports. Independent
replay must justify the determinant norm universally from that faithful
representation and the complete geometric fibers (or a separately
justified characteristic-polynomial computation). Norm values on finitely
many input units, or norms of basis vectors alone, are insufficient. Only
on units does this induce the required seventh-power-class map. This
approval covers the known construction and its applicability proof;
any replacement theorem or mechanism outside it needs separate review.

## Bounded test, duplicates and preserved failures

The changed mechanism is invariant-first: obtain the small direction
algebra before the incidence and line computations. Do not regenerate the
stopped 2016-by-2016 translation matrix, increase its limits, or complete
its unverified column stream. L069's domain and secant inverse remain
usable inputs; its separate critical audit is still pending. No old
translation/action column is treated as verified arithmetic.

Before new arithmetic, checkpoint the representation, conventions,
predeclared stages, hypotheses and unresolved geometric obligations.
Retain a 180-second limit per declared arithmetic stage and a 128-MiB
certificate limit for the new presentation. Enforce the timer around the
actual loop and use an independent watchdog; do not split failed stages
retrospectively to evade the bound. Preserve elapsed times, complete vs
required ranks/columns, byte counts, failures and original hashes.
These are local stopping criteria, not mathematical complexity theorems.
The first discriminating test is a complete degree-eight direction basis
and inverse/kernel certificate within the cap, followed by a whole-domain
compressed relation and transport cost test before norm construction.

Continue only while full-domain geometric identification, complete ranks,
all denominators/transports and independent replay can be certified under
the unchanged limits. Missing components, lack of an inverse on the full
invariant image, or a capped arithmetic stage stop this presentation;
preserve partial evidence and record the exact failed obligation. A
partial direction result can be useful but is not completion of this target.
Required full completion thresholds remain dim D=336, dim B_inc=48,
rank over B_inc seven and universal norm replay. Include bounded altered
scalar, omitted component, wrong relation/inclusion and wrong norm-convention
rejections with original bytes preserved. No calculation was run here.

The scoped duplicate/failure comparison used the prior incidence
assessment, L069's full proof, L068's scalar conventions and history 247,
plus ATTEMPTS/021/032--035. They retain respectively the independent finite
quotient obstruction, capped zero Kurihara residue, absent ordinary
local evaluation, repeated-interface stop and uncompressed action cost
stop. The latter recorded 329/2016 columns, 372.06086778640747 seconds
against 180, and 32920675 bytes; the missing timer coverage is preserved.
This assessment does not reopen any of those schedules.

Searches included `Schaefer Stoll p descent A+ invariant algebra lines
7.5 7.10`, `elliptic p descent algebra projective lines invariant
subalgebra scalar multiplication incidence`, `finite etale algebra
invariant algorithm group`, `Magma invariant subalgebra etale algebra
fixed algebra automorphism`, and exact p-descent/direction/incidence
variants restricted to author/arXiv sources. The general-p paragraph and
Lemma 7.2 are inspected coverage, not a search-snippet inference. The
prior Magma seven-isogeny/rational-torsion mismatch remains unchanged;
no new package was executed or taken as a certificate. Magma V2.29 field-
automorphism/etale documentation search results were leads only, not
read theorem evidence. Knus--Merkurjev--Rost--Tignol, *The Book of
Involutions*, available author draft, Section 18.B p. 287, definition and
Proposition 18.14 proof, was narrowly inspected for fixed algebras as
orbit-constant functions; no extra input is needed from that draft.
Creutz's thesis and explicit n-descent papers remain unread leads for
this target. Failure to locate a fixed certificate does not establish
novelty. Detailed extraction is checkpointed in
`drafts/2026-10-16-conductor389-seven-compressed-source-review.md`.

## Relevance and completion limits

The main gap remains rank E(Q)=m(E) for arbitrary analytic order at least
two. This intermediate target could supply L066's necessary incidence
constraint once independent complete global power classes and all other
descent data exist. The official Clay scope and rank/refined-formula
separation are unchanged. No cross-notebook input is used.

Essential local inputs are audited L067/L068 and independently replayed
L069 with its separate audit pending. Global functions, complete
units/classes, embeddings/local identifications, local bounds and Selmer
containment remain missing. L026 residual premises, successful
localization, rational membership, divisible Sha and arbitrary-curve
complex-order/rank comparison remain unresolved. No claim here closes
any of these independent gaps.

Mathlib full matching coverage for this compressed fixed certificate:
not checked; supporting algebra alone would not supply the instance.
This literature step supplies known-source coverage and approves only a
bounded REPRODUCTION under SPECIALIZE. It proves no new lemma and writes
no mathematical script. No new compressed coefficient, quotient, norm,
Selmer bound or mathematical discovery is claimed. Mathematical exploration
usage is unchanged. The updated ready assessment is available for the
supervisor's separate next-turn approval; no mathematical work is invoked
in this turn.
