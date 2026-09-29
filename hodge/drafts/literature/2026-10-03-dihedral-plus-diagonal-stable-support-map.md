# Dihedral support plus diagonal — literature assessment

TARGET: Review whether the cubic dihedral support C plus the diagonal defines a regular degree-three support map S -> S^{(3)} satisfying the Hilbert--Chow stable-lift criterion.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched the exact dihedral/cubic-RM Hilbert and symmetric-product construction, finite-family norm maps, Hilbert--Chow lifting and orbit collisions; followed the primary norm and ideal-of-norms statements below. No inspected theorem decides this prescribed map's stable lift.
SOURCE_EVIDENCE: Read van Geemen--Schuett, published 2025, Lemma 4.3, section 4.8, Remark 4.9 and sections 5.3--5.4, pp. 11,13--15; Rydh I, arXiv:0803.0618v1, Definition-Proposition 4.1.1 and Corollary 4.2.5, pp. 39,42--43; Rydh II, author version 2008-04-11, section 3 and Definition 3.1, p. 6, https://davidrydh.se/papers/famzerocyclesII-20080411.pdf#page=6; Ekedahl--Skjelnes, Annals 179 (2014), Definition 2.7, sections 3.1--3.3, Proposition 3.4, section 7.24 and Corollary 7.28, pp. 811,813--814,834,836--837, https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n3-p01-p.pdf#page=9; Stacks 0806; reread Yoshioka Proposition 3.4 statement, arXiv:math/9907001v2, p. 16, reusing the earlier inspected proof and polarization scope. Precise imported statements are in foundations/08-finite-family-cycle-and-norm-ideal-inputs.md.
COMPARISON: Known determinant-law, addition and symmetric-product results cover the regular-cycle framework; the full norm ideal has an inspected alternating-determinant presentation. L008 already supplies the all-fibre finite flat normalization maps, and L040 supplies the stable-lift criterion. Their application to this particular degree-three map, especially its isolated triple collisions, has not been performed or imported as a matching theorem.
GAP: Check the norm construction against the prescribed generic fibre cycle and all resolved fibres, then test invertibility of the actual image ideal J O_S at every collision; the inspected statements do not evaluate that pullback for this recipe. Transverse deformation remains a separate later gap.
REASON: Continue with one bounded specialization of the unchanged target in a later research turn, using the imported framework rather than rederiving it. Existing embedded-union and boundary-action failures do not settle this Hilbert--Chow test; a failed local image-ideal test stops the recipe. This turn derives no map, ideal, lift, action or deformation result and makes no originality claim.

## Scope, gap and downstream use

Preserve the original proposal: the generic degree-two fibre
cycle of C over a parameter point, plus that diagonal point.
Here C is L007's reduced support of C_1, with its recorded
generic multiplicity one; it is not an unspecified sum of
both pushed graph cycles. Work on the very general cubic-RM
Dickson family, with its full endomorphism field and the
general-polarization scope retained by the moduli model.

The main route gap is a representative with a possible
transverse use beyond the Dickson locus. The intermediate
target is an everywhere regular support map and its stable
lift. An alternative universal-sheaf representative could
justify a later deformation test; merely realizing the
already algebraic cubic cycle again would not enlarge the
current span. Neither existence of the proposed lift nor
its transverse deformation is assumed.

The attained span remains 21 on the Dickson family, and
three attained RM directions remain short of four required.
The earlier boundary-contained supply has at most one
transcendental direction against three required by E. The
universal target still asks for all rational Hodge classes
on every smooth projective complex variety. Deligne's
[section 1, pp. 1--2](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=2)
was reread on 2026-10-03; its rational formulation matches
the local goal. No complete informal candidate is present.

## Inspected primary statements and comparison

The new framework statements are imported by precise citation
in [the source note](../../foundations/08-finite-family-cycle-and-norm-ideal-inputs.md),
using the common Hypotheses, Conclusion, Proof, Mathlib format.
Only the named generic results are imported, not a conclusion
about this proposed support map.

- Read van Geemen--Schuett, *On families of K3 surfaces with
  real multiplication*, **published version**, Forum of
  Mathematics, Sigma 13 (2025), e2: Lemma 4.3, section 4.8
  and Remark 4.9,
  [pp. 11--13](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26D90B781A518CB95969B4473C8852C8/S2050509424001464a.pdf/on-families-of-k3-surfaces-with-real-multiplication.pdf#page=11),
  and sections 5.3--5.4,
  [pp. 14--15](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26D90B781A518CB95969B4473C8852C8/S2050509424001464a.pdf/on-families-of-k3-surfaces-with-real-multiplication.pdf#page=15).
  These cover the dihedral cycle and the very-general family.
  The inspected sections do not assert the proposed Hilbert-cube
  lift. Remark 4.9 cautions against assuming this correspondence
  model for arbitrary RM surfaces. Retain L006's normalization
  and L007's support identification; no cycle action is recalculated.
- Read Rydh, *Families of zero cycles and divided powers: I.
  Representability*, arXiv:0803.0618v1, dated 4 March 2008:
  Definition-Proposition 4.1.1 and proof,
  [p. 39](https://arxiv.org/pdf/0803.0618v1#page=39),
  and Corollary 4.2.5 and proof,
  [pp. 42--43](https://arxiv.org/pdf/0803.0618v1#page=42).
  Read part II, **author PDF dated 11 April 2008**, section 3
  through Definition 3.1,
  [p. 6](https://davidrydh.se/papers/famzerocyclesII-20080411.pdf#page=6),
  with Theorem 2.3's polynomial-law identification, p. 5.
  This supplies norm and addition tools without requiring a
  flat reduced image support. Applying them here still requires
  comparison with the prescribed generic cycle.
- Read Ekedahl--Skjelnes, *Recovering the good component of
  the Hilbert scheme*, **published version**, Annals of
  Mathematics 179 (2014), 805--841: Definition 2.7,
  [p. 811](https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n3-p01-p.pdf#page=7);
  sections 3.1--3.3 and Proposition 3.4 with proof,
  [pp. 813--814](https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n3-p01-p.pdf#page=9);
  section 7.24, Theorem 7.25 and Corollary 7.28 with proofs,
  [pp. 834--837](https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n3-p01-p.pdf#page=30).
  The source note retains mixed norm generators and the full
  centre. The target-specific ideal is not computed here.
- Read [Stacks Lemma 31.33.5, Tag 0806](https://stacks.math.columbia.edu/tag/0806),
  statement and proof on 2026-10-03. Its Cartier hypothesis
  is a condition to check. Reuse L040's necessity qualification
  for an integral parameter surface generically outside the
  centre; the cited sufficient property alone is not a blanket
  lifting theorem for every symmetric-product map.
- Reread Yoshioka, *Irreducibility of moduli spaces of vector
  bundles on K3 surfaces*, arXiv:math/9907001v2, 7 February 2000,
  [Proposition 3.4 statement, p. 16](https://arxiv.org/pdf/math/9907001v2#page=16).
  Reuse [the existing import](../../foundations/06-exceptional-hilbert-cube-model.md)
  and the earlier inspected proof and general-polarization assessment.
  This supplies the global moduli model, not a map from S.
  L040's all-fibre support comparison remains a local result.

## Bounded specialization and stopping test

The remaining application is concrete, not an unrestricted
search for a new source. Use L008's finite flat double cover
and regular second projection to check the norm-cycle
description at every resolved fibre. Then retain the actual
image ideal K=J O_S from L040. The required threshold is
invertibility everywhere, including codimension two; knowing
only the reduced inverse collision set or generic regularity
does not reach it.

The all-fibre check must retain the cover-branch collisions,
the two finite diagonal-intersection fibres in L009, and the
three isolated common graph points over infinity. At the
latter, L008 and L009 give the local description using id,
f and f^{-1} for an order-seven local automorphism. This is
a recorded local model for a future norm-ideal test, not a
computed pullback or a failure certificate in this turn.
Proposition 3.4 provides a primary formula for that test;
no determinant is evaluated now.

Continue only if the prescribed cycle gives a regular map
and the scheme-theoretic criterion holds everywhere. An
unavoidable indeterminacy or one noninvertible image-ideal
stalk rejects this recipe. A positive result would still
leave the representative's transverse deformation and all
other universal Hodge cases unresolved. Do not repair a
failure by silently replacing the parameter S by a blowup:
that changes the saved target.

L009's stopped embedded union and L013's sheaf extensions
are relevant comparisons, not an obstruction for every
family with their leading cycle. L038's scalar fixed-point
recipe remains stopped; L041 excludes only entirely
collision-contained support. These failures do not justify
skipping the present test or assuming its success.

## Search and access record

Queries actually used included:

- `"van Geemen" "Schütt" "Dickson" correspondence K3 symmetric product`
- `"van Geemen" "Schütt" "dihedral" "Hilbert"`
- `"dihedral" "correspondence" "symmetric product" K3`
- `dihedral correspondence K3 Hilbert scheme points rational map symmetric product lift`
- `"Hilbert-Chow" "lift" "rational map" surface norm ideal`
- `"K3" "degree three" "correspondence" "Hilbert"`
- `"Rydh" "families of zero-cycles" finite locally free norm symmetric product`
- `"Hilbert scheme" "orbit map" "fixed point" surface`

Broad hits on Hilbert-scheme fibrations, birational maps and
arbitrary orbit maps did not supply an inspected match for
this degree-three recipe. They are discovery leads only.
Rydh's author [publication index](https://davidrydh.se/papers)
identified the exact I/II versions followed above. His
*Families of cycles* draft and Baranovsky's *Norm functors
and effective zero cycles* were search leads, not inspected
theorems used here. No essential source is inaccessible:
the norm, addition, centre and moduli inputs were read or
reused from adequate assessments. Failure to find a full
match is not evidence of novelty.

## Outcome and Mathlib

The gate is complete as SPECIALIZE for the **unchanged**
saved target. This literature turn is EXPLORATION, with one
consecutive exploration turn since L041; it neither proves
a new mathematical input for the proposed map nor supplies
an informative mathematical negative. Known framework
statements are imported; the future application is scoped
reproduction of those tools, without an originality claim.
No map, lift, action, new algebraic class or transverse
surface is asserted. The separate research test has not
been started in this turn.

Mathlib coverage is **not checked** for the full proposed
map or its stable lift, or for the supporting norm and
Hilbert--Chow results. Direct primary theorem names and
links above match framework parts only. No Mathlib absence,
full target match or certified novelty is asserted.
