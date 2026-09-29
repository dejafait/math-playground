# Cubic RM after an auxiliary CM extension — literature assessment

TARGET: Test whether scalar extension V=T(S) tensor_E K with K=E(i), carrying K in Hodge type (0,0), admits a polarized weight-one half twist for any CM type, as a prerequisite to realizing U through abelian endomorphisms.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched half-twist existence, polarization, scalar extension and totally real multiplication; read the primary criterion and two related constructions below. No inspected statement answers the exact inherited scalar-extension test without an applicability calculation.
SOURCE_EVIDENCE: van Geemen, arXiv:math/0008076v1, sections 1.2--1.4, 2.5, Proposition 2.8 and sections 2.10--2.11, https://sites.unimi.it/vangeemen/0008076.pdf#page=2; van Geemen--Izadi, arXiv:math/0008170v1, section 1.5, https://sites.unimi.it/vangeemen/halfhyper.pdf#page=4; Moonen, author PDF, section 7.1, https://www.math.ru.nl/~bmoonen/Papers/TMTCC1.pdf#page=28.
COMPARISON: The general effectivity criterion allows an arbitrary-dimensional top Hodge piece, so it is the appropriate input for V. Examples with a CM action already on the original Hodge structure do not check the scalar-extension hypotheses. Polarization and Hodge inclusions are separate from algebraic comparison cycles.
GAP: Determine the K-embedding support of V^{2,0}, compare it with every CM type, and, only if the support test passes, verify the compatible-polarization input. No eigenspace calculation or existence/nonexistence conclusion for this V is made in this review.
REASON: Reuse the known criterion and polarization statement; only their application to the saved scalar extension remains. One bounded research specialization can decide whether this prerequisite survives before any search for comparison cycles.

## Hypotheses

Retain the very-general cubic-RM data: T=T(S) has rational
dimension eighteen, its full Hodge endomorphism field is
E=Q(zeta_7+zeta_7^(-1)), and dim_E T=6. The proposed field is
K=E(i), with i^2=-1. Equip the scalar extension in the target
with the Hodge structure inherited from T and a weight-zero
scalar field. No new CM action on the original T is assumed.
Weight one means an effective Hodge structure with only types
(1,0) and (0,1), as required by the proposed abelian realization.
The question is whether at least one CM type works.

The universal target is unchanged. Deligne's
[Clay statement, section 1, p. 2](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=2)
was reread on 2026-09-27: the coefficients are rational and the
variety is smooth projective over C. This prerequisite would
address only the selected cubic-RM mechanism.

## Conclusion

The exact saved target is screened as SPECIALIZE. Known inputs
are recorded by citation below; no reproof is needed. The
remaining application is expected to be REPRODUCTION, without
an originality claim. This step is LITERATURE /
NOVELTY_UNCHECKED / EXPLORATION and does not perform that
application in the same invocation.

The previously unread essential lead has been resolved. The
review establishes neither a half twist nor its impossibility
for the specified V. No algebraic class, factor of A, or
transverse RM direction is supplied.

## Proof

This section records inspected source statements and their
scope, not a proof of the saved mathematical target.

### General criterion and polarization

Read Bert van Geemen, *Half twists of Hodge structures of
CM-type*, [arXiv:math/0008076v1, 10 August 2000, pp. 2, 4--6](https://sites.unimi.it/vangeemen/0008076.pdf#page=2),
and the corresponding sections of the
[published version, J. Math. Soc. Japan 53 (2001), 813--833](https://www.jstage.jst.go.jp/article/jmath1948/53/4/53_4_813/_pdf).
Journal locations are sections 1.2--1.4, pp. 814--815;
2.5, p. 817; Proposition 2.8, pp. 818--819; and
2.10--2.11, pp. 819--820. Here W is an effective rational
Hodge structure of weight k>=1 with a Hodge-compatible
K-action. Use the following general statements:

- In section 1.2, the CM terminology requires a Hodge-compatible
  K-action, without requiring a commutative Mumford--Tate group.
- For a CM type Sigma, let W_+ denote its embedding summands and
  W_- the conjugate summands. Sections 1.4 and 2.5 define
  (W_{1/2})^{p,q}=W_+^{p+1,q} direct sum W_-^{p,q+1};
  effectivity on all of W holds exactly when W_-^{k,0}=0.
- Sections 2.10--2.11 require a polarization Psi satisfying
  Psi(ax,y)=Psi(x,bar(a)y). An existing half twist is then
  polarizable; the source supplies a construction.
- Proposition 2.8 gives Hodge inclusions
  W_{1/2}(-1) into W tensor_Q K_{-1/2} and
  W into W_{1/2} tensor_Q K_{-1/2}, conditional on existence.

These citations supply supporting results, not a worked example
of the notebook's V. Applying them requires the actual scalar
extension, rather than copying the top Hodge piece of T.

### Independent formulation and geometric scope

Followed the paper's reference to van Geemen--Izadi,
*Half twists and the cohomology of hypersurfaces*,
[arXiv:math/0008170v1, 22 August 2000, sections 1.3--1.6, pp. 3--4](https://sites.unimi.it/vangeemen/halfhyper.pdf#page=3).
Section 1.5 states the same criterion in terms of the
eigenvalues on the top Hodge piece, with explicit plus/minus
notation. This checks the conjugation convention in the
first source's extracted text.

Also read [section 2.1, pp. 4--5, and Theorem 5.2, pp. 12--13](https://sites.unimi.it/vangeemen/halfhyper.pdf#page=12).
The theorem constructs a Kuga--Satake correspondence for
the cyclic-cover cases (d,k)=(3,4) and (4,2) in that notation.
Those are geometric CM actions on the specified cohomology;
the theorem does not assert the scalar-extension construction
in the present target. This is a comparison of hypotheses,
not an exclusion of other algebraic correspondences.

### A related abelian-endomorphism construction

Read Moonen, *On the Tate and Mumford--Tate conjectures in
codimension one for varieties with h^{2,0}=1*,
[section 7.1 and equation (7.1.1), p. 28](https://www.math.ru.nl/~bmoonen/Papers/TMTCC1.pdf#page=28).
Version: the 45-page author PDF accessed on 2026-09-27;
pagination here is PDF pagination. This section assumes that
the original variation's Hodge endomorphism field is CM.
With its primitive CM type, unique top-piece embedding and
polarization hypotheses, it
constructs an abelian scheme and identifies the original
weight-zero variation with an E-linear Hom of weight-one
variations. It does not state that adjoining i as a
weight-zero scalar to a totally real variation meets those
hypotheses. No part of its Tate or Mumford--Tate conclusion
is imported as algebraicity of the missing cubic cycle.

### Search record and access limits

Queries on 2026-09-27 included:

- `van Geemen "Half twists of Hodge structures of CM-type" half twist existence polarization`
- `"half twist" "real multiplication" scalar extension CM type`
- `"half twist" "scalar extension" Hodge`
- `"half twists" "totally real" tensor`
- `"half twist" "polarization" "van Geemen"`

The arXiv record identified the first source; its author copy
and published text supplied the statements. Some J-STAGE
screenshots timed out; the accessible text and the companion
paper's plus/minus notation resolve the needed criterion.
The UCSD endpoint for the published van Geemen--Izadi paper
failed; its explicitly identified author-hosted v1 was read
instead. Published numbering is not attributed to that v1.

Lang and DMOS, cited behind van Geemen's polarization result,
were not independently read. No separate statement from them
is used; the inspected section 2.11 is the cited input.
Search results for ball quotients and later surveys were not
used as theorem-level evidence. No essential unread source
blocks the bounded application, and no novelty follows from
the absence of an exact worked scalar-extension example.

### Relevance, overlap, and the discriminating test

The gap remains algebraic realization of the cubic action
beyond the Dickson locus. A successful auxiliary weight-one
construction could make an abelian-endomorphism transfer worth
investigating. Algebraic inclusion and retraction
correspondences involving S would still have to be supplied;
the Hodge inclusions above do not supply those cycles.

L032--L034 test the existing Clifford representation and
specified transfers. They do not settle this auxiliary
Hodge structure. The completed nonabelian-source assessment
likewise supplied no half-twist test. There is no duplicate
calculation to repeat and no reason to reprove the general
half-twist criterion.

The remaining bounded application must retain the whole V
with K in type (0,0). Determine its top-piece support over
all embeddings of K, including the conjugate pairs above
each real embedding of E. Compare that support simultaneously
with the CM-type condition. Do not discard a summand,
change the Hodge structure of K, or substitute a formal
weight shift for the effective structure being asked for.
No support multiplicities have been computed in this review.

Continue this mechanism only if some CM type passes and
the polarization input is justified. Stop this exact recipe
if the criterion excludes every CM type. Either outcome
must retain the scope of the fixed scalar extension; it
would not classify all auxiliary Hodge structures.

The achieved span remains 21 on the known family and only
three RM directions are attained against four required.
Algebraic beta_U and the separate kappa, arbitrary primitive
fourfold classes and higher-dimensional cases remain missing.
This source review is the second consecutive exploration
turn after L034. The next bounded application must finish
its continuation/stop assessment within the same allowance;
the mechanism change has not reset the count.

## Mathlib

Coverage: **not checked** for half twists, the CM-type support
criterion, or the exact scalar-extension statement. No full
Mathlib match or absence claim is made. The primary citations
above are supporting mathematical inputs, not library matches.
