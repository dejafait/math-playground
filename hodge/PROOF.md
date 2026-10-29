# Hodge conjecture: argument overview

Status and the sole next action are in [PROGRESS.md](PROGRESS.md); canonical dependencies and lemma navigation are in [DAG.md](DAG.md). Full proofs and qualifications remain in the lemma files. This argument is incomplete.

## Assembly and unresolved gap

The [exact target](foundations/01-target-and-scope.md) is surjectivity of the rational cycle-class map for every smooth projective complex variety and every codimension. Lefschetz (1,1), Hard Lefschetz and functoriality cover the recorded extremal codimensions; L001 isolates the primitive (2,2) gap on fourfolds, without reducing the general conjecture to that case.

No argument here constructs algebraic cycles for every primitive class, even on arbitrary fourfolds. L002/L003 show why universal divisor-product generation, or adjoining just the diagonal, is insufficient on the K3 self-product family. Special algebraic classes do not establish the required uniform realization of Hodge endomorphisms.

## Partial results

The current branch tests hypothetical bundle/kernel data on identical marked K3 factors with fixed connection and Chern character. Audited L159 excludes two extremal z=0 branches using the actual opposite-coefficient harmonic map and strict normalized trace signs. Audited L160 retains the ordinary top sheaf W and uses dual truncation and degree-one detection away from its finite support to obtain m_-1*m_1=0. Audited L161 gives m_-2*m_2=0 with W retained, throughout 0<=z<=119. These conditional restrictions neither improve the upper bound on z nor give an independent lower comparison.

L162 tests same-sign first/second-power coexistence. Its degree-two mixed cup pairs negatively with the cup of the harmonic opposites, giving a norm balance that cancels the positive trace product. Thus this sign test does not prove m_1*m_2=0. The harmonic-representative correction and cancellation are recorded with a separate critical audit pending; no compatible kernel is constructed.

L163 compares the untwisted End_0(F) trace forms with L117's actual maps through L116, retaining the finite point term and unknown multiplicity. For nonzero section space K=J^{-1}Phi_1 is positive self-adjoint; zero space is vacuous. Its strictness hypotheses remain canonical. It awaits critical audit and gives no exclusion.

L164 identifies the actual finite-point adjoint bracket with the symmetric split-fibre pairing, retaining derived base change. Nondegeneracy on its 52-dimensional derived middle space gives a conditional t>26 nonvanishing test. The actual section pairings and t are unknown; the vanishing route is parked. Critical audit is pending; no exclusion follows.

Audited L170 identifies the radical on L164's 50-dimensional ordinary image with the actual two-dimensional KS plane: the incoming differential gives the correct annihilator, and actual base-tangent integrability gives its inclusion. The restricted rank is exactly 48. Its isotropic-section inequality is dimension at most 24 plus the intersection dimension with that plane, recovering 26 without further intersection control. It evaluates no section quadric and gives no new exclusion.

Audited L171 compares the family Atiyah/KS morphism with the actual truncation inclusion. Its degree-one sheaf map extends L108's specific tangent inclusion, and local projectivity identifies its derived lift with j composed with i[-1]. The first-order extension interpretation then gives e_z i(z)=kappa_z, retaining all derived middle directions at split points. Actual section brackets and F existence remain unresolved.

L172 combines the audited L171 identity with the fixed normal splitting: every global section evaluates in N(z), whose image under the injective e_z meets the actual KS plane trivially. L170 then gives t<=24 under total section isotropy, sharpening the conditional nonvanishing test to t>24 when the split set is nonempty. This specialization awaits separate critical audit. It computes no actual section bracket and gives no unconditional bound on t, exclusion of F or split cardinality.

Audited L165 tests scalar isotropy with the complementary global obstruction component retained. L116's actual trace-adjoint retraction identifies the orthogonal complement of the nondegenerate included H^1(B,M); its tangent summand ensures dimension at least 20. Every point-quotient vector consequently has a fourfold Serre-isotropic lift. The audit preserves the actual adjoint and shift comparison and parks only scalar-isotropy-only exclusion; it determines no actual bracket or compatible deformation map.

L167's 21-square witness at s=800,t=48 is formal. Audited L173 places the complementary bracket in H^1(B,N), with square capacity 704-s+2t. Audited L177 uses both actual transposes and the fixed correspondence to remove fourteen nondegenerate normal directions with zero point projection, reducing the original point-quartic capacity to 690-s+2t. It does not evaluate the section quadrics or their minimum square length.

Audited L174–L176 give residual Gram rank 15, point-map rank at most one and normal rank>=14 (>=15 for empty Z), hence t<=46 and the prior s<=782. L177's zero quartic alone did not exclude s=782: it need not mean a zero bracket.

Audited L178 matches the prescribed point vector and residue/trace conventions, giving coefficient gamma*s/d. The k-line Gram factor d^2-16+14s has its sole zero in (39/56,6/7); fifteen normal directions survive for integer s>=1, giving s<=781. It excludes no F and supplies no fifteenth point-free direction.

Audited L179 gives only a formal s=781,t=46 witness. Audited L180 excludes that endpoint using actual trace cups: Gram rank 1081>816. Audited L181 extends this to every retained t and empty Z: t(t+1)/2<=724+2t and parity give even t<=38. No s bound or F realization follows.

L182 transports the signed trace-free cubic through actual j_3/J. Perfect Serre detection identifies it with L180's full four-word traces, so it adds no bound. Its critical audit is pending; universal-cubic exclusion is parked.

Audited L168 identifies the actual quotient adjoint with gamma^{-1}[-2], proving orthogonality across distinct reduced split points. Finite-support evaluation expresses the quotient form as a weighted sum of squares of L164's actual section quadrics, with a local Koszul formula retaining the canonical trace functional and common scalar. It computes no section quadrics, numerical residue weights or minimum square length and gives no exclusion.

L169 compares that oriented Ext generator with the cited regular-section residue and L111's actual KS pairing. The local coefficient of sigma_B cancels, giving the common weight delta_B*kappa/(2lambda), where delta_B records one global base-trace convention. This conditional specialization awaits separate critical audit. It removes independent point coefficients in the fixed bracket coordinates, but computes no actual section quadrics, square length or exclusion.

The existence of the equality-kernel F, exclusion of the remaining stable decompositions, transport and global primitive Hodge realization remain unproved. All specific markings, twists, integral classes and audit qualifications live in the canonical statements; do not replace their actual cup maps with arbitrary matrices.

## Known traps checked

- Hodge decompositions, finite models and Riemann–Roch do not construct cycles or sheaves. A zero diagonal quartic does not determine the polarized bracket Gram rank.
- Preserve actual twists, ordinary versus derived top terms, parallel reduction, edge degrees and all independent Euler/trace signs. A z=0 exclusion cannot silently be reused for positive z.
- Restricted K3 calculations do not settle arbitrary fourfolds, higher dimensions or all codimensions. No complete candidate is asserted.

## Historical overview

The [pre-compaction overview](history/2026-10-24-proof-overview-before-compaction.txt) is preserved verbatim for historical context. It is not a replacement for current canonical proofs or the checkpoint. Read only relevant passages when tracing a prior argument.
