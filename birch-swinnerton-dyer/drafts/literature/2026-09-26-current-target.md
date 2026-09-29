# Rank-zero Kato class: anticyclotomic lift assessment

TARGET: Test whether the rank-zero Kato class of E^K admits a global lift along 1 - epsilon d, using its explicit reciprocity law to identify the relaxed minus line and distinguishing its usual cyclotomic deformation.
CHECKED: 2026-09-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Kato class anticyclotomic deformation, individual Beilinson--Kato lifts, relaxed heights/cup products, universal zeta morphisms, and the saved CM lead; exact queries and inspected sources are recorded below.
SOURCE_EVIDENCE: Burungale--Skinner--Tian--Wan, https://arxiv.org/pdf/2409.01350v2, Sections 1.1.3, 3.2, Theorems 3.13--3.14 and 5.26; Castella, https://arxiv.org/pdf/2204.09608v3, Theorems A--B; https://web.math.ucsb.edu/~castella/GKC-IMC.pdf, Theorem A; Nakamura, https://arxiv.org/pdf/2006.13647v2, Theorem 1.1; prior Castella--Hsieh and duality audits reused as specified below.
COMPARISON: The reciprocity input and cyclotomic family are covered. The checked two-variable specialization concerns a weighted combination, and the CM and universal-deformation theorems have different hypotheses; none is a match for the individual inverse-anticyclotomic first-order lift.
GAP: Determine the actual arithmetic obstruction -d cup z^- in L011 after checking the rank-zero twist representative and its normalization; its vanishing or nonvanishing is not supplied by the inspected theorems.
REASON: Import the known reciprocity input and restrict further work to the specified representative/local-condition comparison and arithmetic obstruction. Do not reprove Kato's theorem, infer an individual lift from a weighted combination, or replace the saved target by a cyclotomic calculation.

## Scope, relevance, and discriminating test

This is a completed source review of the exact saved target, with no new
mathematical derivation. Retain all of L009--L011's hypotheses and their
Q_p coefficient restriction: good ordinary p > 3, split imaginary
quadratic K, nonzero generalised Kato class kappa, and the auxiliary
central-value and residual conditions. In particular L(E^K,1) is nonzero.
The direction d is the tangent of the normalized CM diagonal family;
the dual deformation is 1 - epsilon d over Q_p[epsilon]/(epsilon^2).
The auxiliary theta forms having CM does not make E a CM elliptic curve.

The main missing claim on this branch remains q(kappa) = 0. The achieved
bound r <= 2 is short of the required r >= 2. L011 has already isolated
a one-dimensional relaxed minus space and the mixed strict/relaxed
obstruction. Its proposed rank-zero Kato representative would turn that
obstruction into an arithmetic class to study, instead of another
formal-duality model.

A successful test must supply a global relaxed first-order lift with
the specified nonzero reduction, or determine its obstruction. A
cyclotomic family, ordinary height vanishing, or only a scalar
reciprocity value does not pass this test. A first-order answer would
still leave the necessity/sufficiency of strict lifting for Kummer
membership, kappa nonvanishing from m(E) = 2, auxiliary existence in
the unrestricted target, and higher ranks unresolved.

## Search record

Searches on 2026-09-26 included:

- Kato zeta element anticyclotomic deformation rank zero elliptic curve quadratic twist
- "2204.09608" "Kato"
- "Kato" "anticyclotomic" "lift" elliptic
- "Kato" "exp" "L(E, 1)" reciprocity law rank zero
- "Kato" "anticyclotomic" "Bockstein"
- "Zeta morphisms for rank two universal deformations" arxiv
- "Beilinson-Kato" "anticyclotomic" "deformation"
- "Kato" "relaxed" "height" "anticyclotomic"
- "Kato" "anticyclotomic" "cup"

The useful new comparisons were the two-variable zeta element and
universal deformation results below. Search snippets were used for
discovery, not as theorem evidence. No claim of novelty follows from
the lack of an exact match.

## Inspected theorem statements

### Reciprocity and the closest two-variable construction

Burungale--Skinner--Tian--Wan, *Zeta elements for elliptic curves and
applications*, arXiv:2409.01350v2, 2024-09-11:
[Section 1.1.3](https://arxiv.org/pdf/2409.01350v2#page=5),
[Sections 3.2.1--3.2.3](https://arxiv.org/pdf/2409.01350v2#page=26),
[Theorems 3.13--3.14](https://arxiv.org/pdf/2409.01350v2#page=29),
and [Section 5.5, Theorem 5.26](https://arxiv.org/pdf/2409.01350v2#page=54)
were read (printed pages 5--6, 26--27, 29, 54--56).

Kato's reciprocity statement here is
loc_p(z_F) in H^1_f(Q_p,V_p F) if and only if L(F,1) = 0.
The Kato family is cyclotomic. Theorem 3.14 identifies its Coleman
image with the p-adic L-function of Theorem 3.13.

For the two-variable construction retain Theorem 1.14's p not dividing
2N, split p, coprime discriminant, and E(K)[p] = 0 hypotheses when
invoking that formulation. Its ordinary local conditions are
relaxed/ordinary. In source-compatible normalizations, Section 3.2.3
and Theorem 5.26 identify its cyclotomic specialization with

\[
c\,\frac{L_p(E^K)\mathbf z_E+L_p(E)\mathbf z_{E^K}}{2},
\qquad c\ne0.
\]

Our applicability comparison: this is not a stated lift of the
individual twist class. Its coefficient involves L_p(E), whose
augmentation is zero in the current setting by Theorem 3.13.
No division or extraction of an individual first-order lift is
justified here.

### The formerly unread CM lead

Castella, *Generalised Kato classes on CM elliptic curves of rank 2*,
[arXiv:2204.09608v3](https://arxiv.org/abs/2204.09608v3), submitted
2026-02-13; PDF dated 2026-02-17, final version to appear in
American Journal of Mathematics according to the arXiv record.
Read [Theorems A and B and their setup, printed pages 3--5](https://arxiv.org/pdf/2204.09608v3#page=3).

Here E itself has CM by K, p >= 5 splits, and the auxiliary Hecke
characters satisfy (1.5) and Theorem A's distinctness/sign conditions.
Theorem B gives Selmer dimension two from a nonzero modified
generalised Kato class, with a localization criterion for the converse.
It does not identify an individual rank-zero quadratic-twist class
with a lift in our deformation. Theorem A's Hecke-character main
conjecture therefore cannot be imported merely because the auxiliary
forms in the notebook have CM. This resolves the saved unread lead;
it does not establish failure of the proposed lift.

### Non-CM strengthening

Castella, *Nonvanishing of generalised Kato classes and Iwasawa main
conjectures*, author PDF dated 2024-06-20:
[Theorem A and remarks, printed pages 2--3](https://web.math.ucsb.edu/~castella/GKC-IMC.pdf#page=2).
The theorem assumes ordinary p > 3, absolutely irreducible E[p],
a prime q exactly dividing N with residual ramification if
q = +/-1 modulo p, and either p > 5 or the stated SL_2(F_p) image
condition. Under its auxiliary choices it strengthens the
nonvanishing/localization equivalence and identifies the strict
Selmer line. The displayed P,Q are a Selmer basis, not constructed
rational points. No individual Kato lift or Kummer criterion is stated.
Its proof was not re-audited.

### Universal deformations are a different source scope

Nakamura, *Zeta morphisms for rank two universal deformations*:
read [arXiv:2006.13647v2, Theorem 1.1 and setup, printed pages 3--5](https://arxiv.org/pdf/2006.13647v2#page=3),
dated 2020-07-02. The later publication is
[Inventiones 234 (2023), 171--290](https://doi.org/10.1007/s00222-023-01203-7);
the theorem numbering used here is the inspected preprint's.

The theorem constructs zeta morphisms for rank-two representations
of G_Q with specified oddness, irreducibility, p >= 5 and local
residual restrictions. Specialization recovers Euler-factor-modified
Kato morphisms. It is not a theorem for arbitrary G_K deformations.
Applying it to our chosen anticyclotomic deformation would require
a comparison not supplied by that statement. Neither its title nor
its universal property supplies the missing lift. No such comparison
is derived in this review.

### Reused notebook sources and scope check

Reused the published Castella--Hsieh audit in
[the nonvanishing foundation](../../foundations/07-castella-hsieh-nonvanishing.md),
the actual family's local conditions in
[the deformation foundation](../../foundations/09-cm-diagonal-deformation.md),
and the strict/relaxed conventions in
[the duality foundation](../../foundations/10-selmer-bockstein-duality.md).
Re-read [Castella--Hsieh, Theorem A and Section 5.7](https://doi.org/10.1017/fms.2021.85),
published 2022, printed pages 5 and 28--29: the rational-point
application adds finite p-primary Sha. It cannot settle q(kappa) = 0
without that extra hypothesis.

Rechecked the [Clay page](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/)
and [Wiles, printed page 2](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf#page=2).
The target remains the rank/order assertion for every E/Q, with the
refined formula separate.

## Access and evidence limits

The original [Kato, Asterisque 295 (2004), Theorem 12.5](https://www.numdam.org/item/AST_2004__295__117_0/)
was followed, but its 18 MB PDF exceeded web retrieval limits and
the shell download failed DNS resolution. It is not represented as
read. The needed reciprocity statement was instead checked in the
accessible primary paper above, including its numbered theorem and
interpolation statement. This resolves the statement-level input
for this assessment; no independent review of Kato's full proof is
claimed. Nakamura's publisher full-text retrieval also failed, so
the inspected preprint and its version are identified explicitly.

The saved CM lead is now read at theorem level. Other search results
were not used as mathematical inputs. This bounded assessment does
not certify that no additional theorem exists.

## Decision and continuation boundary

SPECIALIZE applies because the representative's reciprocity input
is known, while the requested arithmetic deformation is not covered
by the statements checked. On a subsequent research turn, cite that
input and check only the twist restriction, relaxed local conditions,
nonzero normalization against L011's line, and the actual inverse
anticyclotomic obstruction. No reproof of the Euler system or of
the already recorded strict/relaxed duality is warranted.

Continue this mechanism only with an arithmetic relation controlling
the mixed obstruction or an actual lift with the required reduction.
If the proposed argument only returns the known weighted
specialization or the ordinary/scalar data already excluded by
L009--L011, stop that argument. Failure of a full-family import does
not rule out a first-order lift; no nonliftability theorem is claimed.
The normalization check alone must not be reported as closing the
arithmetic gap.

This step is EXPLORATION: the literature comparison is now complete
for the bounded target, but the requested lift remains undecided.
Exploration turns used are 1 of 3. The results described above are
known source results, not new discoveries; the uncomputed obstruction
has no originality claim. The exact saved action is retained for
the next invocation, and no research is performed in this turn.

## Mathlib

Full coverage of the individual Kato-class anticyclotomic lift:
**not checked**. Supporting coverage for Kato reciprocity, two-variable
zeta elements, Selmer complexes, and Bockstein maps: **not checked**.
The named sources above support only the stated inputs and comparisons;
none is asserted to match the full target in Mathlib.
