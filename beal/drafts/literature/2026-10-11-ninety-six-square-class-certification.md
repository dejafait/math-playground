# Prime-two-specific certification — completed source review

TARGET: Assess whether prime-two-specific class and unit certification can give an unconditional upper square-class group for the 96a1 descent without full Minkowski enumeration.
CHECKED: 2026-10-11
DECISION: IMPORT
SEARCH_EVIDENCE: Reused the FNS certificate-scope review; searched unconditional 2-class certification, prime saturation, Selmer completeness and norm relations; checked L051–L052, ATTEMPTS/018–019 and the recorded smaller-factor failure. No field-specific upper certificate was inspected; search failure does not establish absence.
SOURCE_EVIDENCE: Elsenhans–Voight October 2, 2025 Sections 4,6,7,8; Magma V2.29 Unit Groups pFundamentalUnits and Ideal Class Groups proof modes; Biasse–Fieker–Hofmann–Page author manuscript Propositions 3.7,4.6,4.8,4.28 and proofs, Corollary 4.7, Algorithm 4.9 and Theorems 4.10–4.11; Sage primary selmer_group.py introduction and pSelmerGroup input calls; prior FNS interface reused.
COMPARISON: Known methods certify units with index prime to two and check relations within known class generators; this does not certify missing ambient ideal classes. Norm-relation certification offers a different mechanism with unmatched normal-extension and subfield-data premises.
GAP: No unconditional ambient class coverage, torsion lifts, support/norm maps or complete global upper image is supplied for 96a1. Prime-specific unit coverage fills only one obligation.
REASON: Park standalone prime-two saturation as a complete-upper-image shortcut; propose a separate bounded normality test for direct norm-relation applicability, without deriving or approving its result.
LITERATURE_REASON: Changed target from a discriminant audit to prime-two-specific global completeness; its essential certification theorem and applicability are outside the saved ready assessments.
SCOPE: IMPORT covers the cited obligation comparison, not existence or impossibility of a full upper group. No field arithmetic or unconditional exclusion is approved; the normality continuation requires separate review.

## Original proposal (preserved)

The main gap remains unconditional global emptiness of L032's surviving
branches and all independent residual signatures. The intermediate target
is a checkable upper square-class certificate for the 96a1 two-descent.
Its downstream use would be the existing FNS full-disk local comparison;
neither local disjointness nor global emptiness is assumed here.

Essential inputs for review: L051's exact K96,L96 models and degrees;
L052's audited routing bound; the existing source-scope assessment's
FNS upper-image interface. L032 supplies the retained disk and full
fourth-power conditions. L050 supplies local nonemptiness only. No
L033/L045 or cross-notebook arithmetic is proposed.

Read primary theorem hypotheses and the essential completeness proof
cases before attempting an algorithm. In particular, distinguish a
subgroup saturated at 2 internally from proof that its ambient quotient
has odd order; neither a relation matrix on a partial factor base nor
the published five elements establishes the needed upper containment.
Whether class torsion lifts, the exact support set, unit square classes
and norm conditions can all be certified remains unresolved. The prior
full-certification review is reusable context, not approval of this
new target. Mathlib coverage is not checked.

Continue only if an inspected theorem yields explicit independently
verifiable completeness obligations and one bounded field-specific test
that avoids requiring enumeration to the known true Minkowski cutoff.
If the proposed method merely presumes full factor-base generation or
the unavailable class/unit certificate, record that dependence and park
this mechanism. Do not run class-group arithmetic in the review turn.
Preserve ATTEMPTS/013–019 and the blocked smaller-factor lead; their
stops are scoped evidence, not a prohibition of independent methods.

## Inspected sources and decision

Elsenhans–Voight, [*Computing class groups and unit groups in Magma*](https://jvoight.github.io/articles/clgpunitgp-magma-02Oct25.pdf),
October 2, 2025, Section 4, equations (4.1)–(4.4), separates factor-base
generation from relations. Section 6, pp.12–13, assumes roots of unity
and independent units of full rank; residue-group linear algebra detects
missing prime roots. Section 7, pp.13–14, uses unit and cyclic-factor
principal generators for saturation but treats missing ideal-class
generators separately. Section 8 retains a generation check. A saturated
partial factor base therefore supplies no inspected ambient odd-index
certificate.

The [Magma V2.29 Unit Groups handbook](https://magma.maths.usyd.edu.au/magma/handbook/text/417),
`pFundamentalUnits(O,p)`, requires a maximal order and prime p, returning
a finite-index unit subgroup whose index is prime to p. Field input uses
its maximal order. Taking p=2 meets the prime hypothesis; no L96 computation
was made. `IndependentUnits` alone lacks that unconditional guarantee;
the default `UnitGroup` proof is separate from class certification.
The [Ideal Class Groups handbook](https://magma.maths.usyd.edu.au/magma/handbook/text/416),
`ClassGroup`, makes `Subgroup` a possible proper subgroup; `Full` inherits
the global bound setting and can remain GRH-conditional.

Cremona's [primary Sage selmer_group.py](https://github.com/sagemath/sage/blob/develop/src/sage/rings/number_field/selmer_group.py),
develop branch inspected October 11, 2026, defines K(S,p) by valuations
outside S and gives its exact sequence with S-units modulo powers and
S-class p-torsion. `pSelmerGroup` calls class-number, class-group and unit
computations with the proof flag; its generators include torsion-ideal
principal generators and S-supported ideals with p-divisible class.
This code supplies no independent prime-only certification of those inputs.

Biasse–Fieker–Hofmann–Page,
[*Norm relations and computational problems in number fields*](https://www.normalesup.org/~page/Recherche/Documents/articles/brauer.pdf),
39-page author manuscript linked to [arXiv:2002.12332](https://arxiv.org/abs/2002.12332)
and [JLMS DOI 10.1112/jlms.12563](https://doi.org/10.1112/jlms.12563),
gives a distinct mechanism. Proposition 3.7 assumes a normal extension
and a norm relation, with class maps composing to multiplication by its
denominator. Propositions 4.6,4.8 and Theorem 4.10 give saturation
correctness; Theorem 4.11's effective bound assumes GRH. Proposition 4.28,
Section 4.6, PDF pp.32–33, requires correct subfield class groups and
roots of unity, bounded unit indices prime to p, S-unit indices prime
to p, and its strict numerical inequality. Its proof treats the
coprime-to-p part separately, bounds a rational discrepancy's denominator
and forces that discrepancy to equal one. This is an unconditional
certificate with obligations, not automatic ambient coverage from
p-saturation. The complete relevant proof cases were inspected.

Exact searches: `number field unconditional 2 class group certification
p saturation relation group odd index`; `Selmer group number field
unconditional class group certification modulo squares saturation`;
`Norm relations and computational problems in number fields pdf Biasse
Fieker Hofmann Page`; `number field 2 class group certification
unconditional Selmer`. Snippets and unrelated average results were not
theorem evidence. Field-specific normality and larger normal-closure
leads remain unassessed.

The full-upper-group threshold is unmet: unit certification leaves the
ambient-generation and class-torsion obligations unresolved. This is
NEGATIVE routing evidence from known sources, not a new impossibility
theorem or progress beyond the sources checked. Standalone saturation
is parked. A separate finite normality test using L051's degree and
audited L052's local data can check the direct-over-Q norm framework's
first premise without a factor base; its answer is not derived here.
Failure would park only that framework, not relative-base, normal-closure
or generalized methods. Success would still leave norm relations,
subfield certificates, unit indices, torsion lifts, support/norm maps and
full-disk disjointness unresolved. Reuse the prior FNS assessment for the
downstream interface. Mathlib coverage is not checked. No new lemma,
mathematical script, DAG edge or proof assembly was written.
