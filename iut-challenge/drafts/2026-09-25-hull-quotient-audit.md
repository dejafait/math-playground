# Hull quotient audit — 2026-09-25

One bounded quotient audit, completed as exploration turn 3 of 3. The initial target and unfinished reasoning were saved before the detailed source test. No candidate resolution was obtained, and no budget reset is claimed.

## Gap, intermediate target, and test

The unresolved claim is input-degree membership in the output range in IUT III, Corollary 3.12(xi-f): with the source record's A and B, prove finite B and A ≤ B, or demonstrate an essential invalid inference under the full hypotheses.

This step tests the quotient mechanism in Remark 3.9.5(v)–(vi), (ix). The intermediate target is to identify the quotient's actual equivalence relation and determine precisely what an identity after that quotient says about the represented input degree. Its downstream use would be to isolate either a valid route to A ≤ B or a specific compatibility obligation that can be tested in the original construction. The initial Θ-data and the full image family remain additional unresolved obligations.

The discriminating test has two parts within this single audit: first identify whether the quotient preserves order or merely identifies points; then check whether the cited closed loop carries the input into the distinguished output class with a controlled numerical lift. A quotient identity with a proved lift would support continuation; a source-specific contradiction would be an informative negative result; an abstract countermodel without a faithful realization would not demonstrate an IUT flaw. If the test remains only a generic diagnostic, conclude this bounded exploration and stop this route at turn 3/3.

## Redundancy and alternatives

L001 already treats the valuation defect of an abstract power map. L002 already treats coherent path cancellation and common determinant normalization. Neither establishes a represented hull comparison. Repeating either calculation is excluded. Constructing the full indeterminacy orbit was compared with the quotient audit in the previous step; the latter has the narrower source anchor and is the only mechanism tested here.

## Source qualification

The official announcement and current prize page were rechecked with the same [scope](../foundations/01-challenge-scope.md). The author-hosted IUT III still has 199 pages and is headed May 2020. The relevant quotient passages and their qualifications are now pinned in the [source record](../foundations/02-comparison-claim-and-sources.md). The checked passages include Remark 3.9.5(v)–(vi), (vii)(Ob5)–(Ob9), (ix), and Corollary 3.12(xi-c)–(xi-g). Reading these passages does not verify their prerequisite constructions.

## Completed mathematical test

[L003](../lemmas/L003-hull-collapse-and-degree-membership.md) supplies the full proof. For a fixed subgroup S of an additive group G, collapse S to one point using π_S. For subgroups H,K, the equality π_S[H] = π_S[K] holds exactly when H = K or both H,K lie in S. In particular, the collapsed point detects containment; the operation does not erase that information. This validates the elementary subgroup version of the stated hull equivalence, including its qualification for distinct hulls. It does not classify all the original archimedean hulls or formal categorical objects.

For full p-adic lattices with a single fixed Haar measure, put B = ν(S). The real log-volume ν does not descend to the image quotient, since S and pS have the same image and different volumes. However, its composition with the collapse of (−∞,B] does descend. The resulting map is well-defined without an assumption about an external input A. Thus a general claim that quotienting automatically destroys every useful degree comparison would be false.

The actual missing input is more specific: a comparison must identify the class of this particular A with the distinguished class of the output bound. At the degree level that equality is exactly A ≤ B. An identity loop fixes every class, including uncollapsed classes with A > B, so unmarked loop closure alone does not suffice. The identity-loop example in L003 tests only this weakened implication, not the formal comparison asserted in the source.

The test also distinguishes a sufficient geometric condition from the necessary numerical target. In dimension two a lattice can have smaller volume than S while extending outside S. Requiring literal containment of the original input region would therefore impose more than A ≤ B in that model. No such unnecessary requirement is used to declare a flaw.

Finally, collapsing before taking an intersection can give a nonempty set when the original intersection is empty. L003 records this exact calculation. Since formal objects and ordinary intersections are different inputs, the calculation alone is not an objection to a formal construction. A later extraction of numerical data would have to specify the appropriate realization; this step has not proved that such extraction fails for IUT.

## Effect on the main gap and decision

The achieved result is a valid elementary compatibility between subgroup collapse and a **collapsed** degree, together with the precise membership condition needed to use it. There is no computed bound for the original B, no proof of its finiteness under all original hypotheses, and no proof or violation of A ≤ B. The known requirement remains finite B ≥ A; mere categorical comparability of objects supplies no numerical estimate here.

The quotient-only objection therefore stops. Its proposed source-specific failure was not obtained: the elementary collapse is consistent with the desired kind of upper bound, while the actual categorical transport is outside what L003 establishes. Removing that extra structure and announcing a contradiction would change the hypotheses. The [stopped attempt](../ATTEMPTS/003-quotient-only-membership-objection.md) preserves this limitation.

This is EXPLORATION, not an IUT-specific ADVANCE or NEGATIVE. The current bounded sequence is assessed and stopped at 3/3 without a reset. This is a stop of the tested route and sequence, not a mathematical ban on other mechanisms. The remaining potential direction concerns transport of the actual structure poly-morphism on the distinguished pilot object, because the quotient's elementary set theory is no longer the unresolved local test. The sole current route decision and concrete action are in PROGRESS.md; no further research step is begun here.

## Checks and limits

The mathematical checks were the subgroup difference argument, the finite-index Haar-volume identity, well-definedness of the collapsed-degree map, and the exact dimension-two and intersection examples in L003. No numerical experiment was needed. L003 uses neither L001 nor L002: their role here is to exclude repeated routes, not to prove the new statement. Its DAG row therefore has no lemma inputs. The new source references retain the distinction between a formal quotient and a set quotient.

Mathlib coverage for the full statement and supporting results is **not checked**. No machine verification, full IUT instance, or verified flaw is claimed. Structural validation is recorded in the dated history after execution.
