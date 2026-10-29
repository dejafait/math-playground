# Step530 — adjacent relative-pair application audit

Approved target: Audit whether IUT III, Theorem 1.5(iii)–(v), supplies the comparison of the retained (fQ1),(fQ2) pair for one adjacent shift, tracing the original hull determinant and localization maps.

Main gap: native q-pilot membership needed for finite B>=A. Intermediate target: apply the known background comparison to the actual relative pair, with its forgetting operation. Downstream use: one prerequisite for the Stp7/Stp8 synchronization, not membership or the inequality itself. Continue if the retained determinant and localization diagrams can be compared at the permitted formal level; otherwise isolate the exact unverified premise. Do not demand a strict original-data lift or turn an incomplete trace into an impossibility assertion.

Entry assessment: `drafts/literature/2026-10-28-relative-pair-background-comparison-audit.md` (SPECIALIZE, saved before invocation and approved by the supplied gate). This is a mathematical application audit, not a new source-discovery turn. Step528's trace, step529's assessed background comparison and September 26's correction-qualified realification coverage are reused. The primary author endpoint was reopened as IUT III, May 2020; the saved theorem and cited proof cases are used at the versions in the assessment. No cross-notebook input is used.

## Saved reasoning checkpoint — unfinished

Theorem 1.5(v) gives an isomorphism of reconstructed global Frobenioids with prime labels and compatible local divisor-monoid identifications rho. Its concluding comparison with the Frobenius-like global data is explicitly compatible with horizontal arrows up to common positive degree scaling. Clauses (iii),(iv) also compare reconstructed unit strips and mono-analytic log-shells. They must not be silently read as vertical Kummer compatibility of every original representative.

The (cQ3) collections have local objects X_v, Aut(D_v)-orbits of linear arrows a_v:X_v->D_v, a global realified object G, and chosen isomorphisms lambda_v:loc_v(G)->R_v(X_v). The attempted application will transport a collection and its arrows through the background comparison and then check whether the result has the determinant of the *retained adjacent algorithm*, rather than simply a newly declared transported determinant. In particular, lambda_v is an isomorphism that may itself be transported; the target definition does not require it to equal a predetermined preferred representative. Whether this removes a purported additional lambda obstruction must be checked using the actual contact/localization diagram.

Conditional initial Theta-data and earlier multiradial construction remain assumptions. Keep fixed q-gluing, original hull/reference determinant, conversion weights and degree line, finite negative output parameters distinct from A, refined input/output labels, tensor-power twists and all allowed log iterates. L127 can only supply reconstructed value data; L123/L126 and ATTEMPTS/003–006,037–040 are boundaries. This checkpoint asserts no transport result, counterexample, new invariant or complete candidate.

## Exact inputs and application scope

Import the following source conclusions at their assessed scope, without re-proving the reconstruction theorems:

- Mochizuki, [IUT III, May 2020](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf), Theorem 1.5(iii)–(v), pp.48–51, including its proof by the cited definitions/results on p.51. Fix initial Theta-data as in IUT I, Definition 3.1, and the lattice in III, Definition 1.4. Clauses (iii),(iv) compare reconstructed unit strips and mono-analytic log-shells in their specified classes of poly-isomorphisms; (v) compares reconstructed global realified Frobenioids, prime labels and rho maps. The final compatibility with the Frobenius-like global realizations in (v) is stated for horizontal arrows and their common positive-scaling orbits. It is not a separate assertion of strict vertical Kummer compatibility.
- III, Proposition 1.3(i)–(iv), pp.41–43, and Remarks 1.3.1–1.3.2, pp.43–44: the vertical D-theater comparison and its log-link construction, with synchronized local choices and translation symmetry. A comparison from log(F) to the next F is not silently identified with a ring-compatible comparison from the original F. Proposition 1.2(iv), pp.30–31, retains this distinction.
- III, Definition 3.8(iii) and Remark 3.8.2, pp.114–115: the full vertical log-links and the extension of Theorem 1.5 to the active LGP lattice. This does not replace the fixed horizontal q-gluing.
- Mochizuki, [IUT II, December 2020](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20II.pdf), Corollaries 4.5(ii), pp.131–132; 4.6(i)–(ii), pp.137–138, proof and Remark 4.6.1, pp.139–140; 4.10(i),(iv)–(v), pp.158–161, and proof on p.161. These specify the global/local reconstruction used above. In particular, rho identifies the v-component of a global divisor monoid with a local real value monoid. Corollary 4.6(ii) constructs its global comparison together with the compatible local monoid comparisons; its archimedean qualification cannot be removed by choosing arbitrary independent local scales.
- III, Remark 3.9.5(vii)(Ob3)–(Ob6), pp.131–135, (Ob8), pp.137–138, and (ix)(cQ3)/(cQ4), pp.141–142: the weighted/reference determinant, local marking orbits, collection diagrams and permitted formal identifications. Mochizuki, [Essential Logical Structure, March 2024](https://www.kurims.kyoto-u.ac.jp/~motizuki/Essential%20Logical%20Structure%20of%20Inter-universal%20Teichmuller%20Theory.pdf), §3.9, pp.140–144, and §3.10(Stp5)–(Stp8), pp.150–154, provide the descent and refined-label use being audited. Neither the p.143 closed-loop assertion nor Stp8's synchronization is used as an input establishing the comparison under examination.
- Reuse the correction-qualified contact/realification constructions of [Frobenioids II, June 2008](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20II.pdf), Example 5.6(iii)–(iv), pp.63–65, and Remark 5.3.3, p.57, as assessed in `drafts/literature/2026-09-26-current-target.md`. They provide distinct global and local contact functors, with a coproduct completion on the global side; they do not identify a divisor-monoid map with every chosen localization isomorphism. The live endpoint again identified the 72-page June 2008 text and returned the p.65 contact-functor passage; a further line-positioned request timed out. No new theorem is imported from that failed request, and it does not invalidate the previously read coverage or constitute a persistent source blocker.

The scoped duplicate/failure review used the step528 and step529 notes and ATTEMPTS/003–006,037–040. It found no completed application of the background comparison to this retained pair. L127's conclusion remains confined to equal-global-parameter reconstructed data; no part of its ordinary numerical reconstruction supplies a marked local-category comparison here. L006 is a contrast: its fixed arithmetic fiber and finite-zigzag invariant are not the formal quotient now under examination.

## Attempted transport of a collection and its arrows

This is a calculation in the application trace, with the currently unverified comparison data displayed as hypotheses. It is not a new claimed IUT transport lemma or a definition of the source's formal quotient.

At the two adjacent labels write C_g,C'_g for the global realified categories, C_v,C'_v for the local categories, and A_v,A'_v for their contact/realified target categories. Write

    L_v:C_g -> A_v,       R_v:C_v -> A_v,
    L'_v:C'_g -> A'_v,    R'_v:C'_v -> A'_v.

Here A_v may include the required coproduct completion. The notation makes no assertion that a general localization has a single component. The same notation can be used after the stipulated pullbacks to the composite input/output labels. A marked collection is (G,{X_v,[a_v],lambda_v}), where a_v:X_v->D_v is linear, its orbit is under Aut(D_v), and lambda_v:L_v(G)~>R_v(X_v). Its unmarked collection forgets only [a_v].

To attempt the transport, suppose the background comparison has been realized on this diagram by functors F_g,F_v,Q_v of the respective global, local and contact categories and invertible natural comparisons

    alpha_v: L'_v F_g => Q_v L_v,
    beta_v: Q_v R_v => R'_v F_v.

Suppose F_v preserves linear arrows and there is an admitted identification d_v:F_v(D_v)~>D'_v with the retained target. These are witness data for this proposed construction, not necessary strict-lift conditions on every possible formal comparison. They may live on a permitted presentation or pullback of the formal diagram; no lift of the original Hodge data is required.

The candidate image of a collection is forced by these types:

    G' = F_g(G),  X'_v = F_v(X_v),
    [a'_v] = [d_v F_v(a_v)],
    lambda'_v = beta_v(X_v) Q_v(lambda_v) alpha_v(G).

Products denote composition with the rightmost map first. Every factor in lambda'_v is an isomorphism, and the composite has exactly the required type L'_v(G')->R'_v(X'_v). If a_v is replaced by u_v a_v for u_v in Aut(D_v), then its image changes by postcomposition with d_v F_v(u_v) d_v^(-1), an automorphism of D'_v. Thus the formula respects the marking orbit. Replacing d_v by another isomorphism from the same F_v(D_v) to D'_v also only postcomposes the marking by a target automorphism. This does not authorize changing D'_v itself.

For an admitted arrow (h_g,{h_v}) between collections, marking compatibility is [a_(2),v h_v]=[a_(1),v], and localization compatibility is

    R_v(h_v) lambda_(1),v = lambda_(2),v L_v(h_g).

The image arrows are F_g(h_g),F_v(h_v). The first equation survives by functoriality and the same conjugation of target automorphisms. For the second, naturality of beta_v and alpha_v gives, with X_i,G_i denoting the source and target objects,

    R'_v(F_v(h_v)) lambda'_(1),v
      = beta_v(X_2) Q_v(R_v(h_v)) Q_v(lambda_(1),v) alpha_v(G_1)
      = beta_v(X_2) Q_v(lambda_(2),v) Q_v(L_v(h_g)) alpha_v(G_1)
      = beta_v(X_2) Q_v(lambda_(2),v) alpha_v(G_2) L'_v(F_g(h_g))
      = lambda'_(2),v L'_v(F_g(h_g)).

Identities and compositions follow from those of F_g,F_v,Q_v. Applying the same formulas after removing the markings gives the candidate functor on (fQ2). Consequently the comparison commutes with forgetting markings at this presented level. There is no new global arrow G->D, no demand for arrows between arbitrary collections and no use of a scalar defect condition.

This calculation supplies only a functor under the displayed hypotheses. If the application requires an equivalence of presented pairs, inverse comparison data and the corresponding coherence must also be supplied; none is inferred just from this one-way formula. The calculation does not itself establish an equivalence of the formal quotient diagrams.

This computation separates two issues which an incomplete audit could conflate. The chosen lambda_v is part of the object being carried, so one need not prove equality with an independently preselected lambda'_v. What one still needs is the appropriate comparison of the contact diagrams, including alpha_v and beta_v, or its permitted formal counterpart. An equality of rho maps alone is not the displayed naturality equation: rho has a divisor-monoid domain, whereas this equation has objects and arrows as its arguments. Conversely, the type difference alone is not proof that such a natural comparison cannot be induced by the reconstructed data.

## Applying the computation to the original determinant

There are two legitimate branches to distinguish. If the source identifies both labels with pullbacks of the same original determinant parameter, the target in the calculation must be that pullback, and d_v is interpreted within that identification. If it transports the parameter, the resulting target must be identified with the determinant attached to the retained adjacent algorithm. In either case the determinant is that of the original bounded hull in (Ob5), with the packet weights, inverse reference determinant and common exponent of (Ob3); it is not selected afresh for each approximant.

Merely setting D'_v:=F_v(D_v) makes the displayed formula a transport to a newly specified relative category. It does not identify that category with the one the adjacent algorithm already supplies. Likewise, equality of normalized global parameters from L127 supplies no comparison of the local marking diagrams. This is a proof-use limitation, not an assertion that the determinants are unequal.

At the other extreme, imposing a globally compatible family of strict determinant arrows as a *necessary* condition would repeat the stopped ordinary-model objection. The source permits local marking orbits, twists and formal pullbacks. Moreover, (Ob3-2), p.132, explicitly permits a sufficiently divisible exponent so the localizations of the determinant line bundles are trivial. Thus a bare claim that no local determinant identification can exist is not a sound diagnostic. Local triviality, however, does not check the source-admissibility of all choices relative to the particular contact comparison, reference normalization and fixed q-gluing.

Theorem 1.5(v) provides a substantive F_g candidate at the reconstructed global level. Clauses (iii),(iv) provide the assessed local unit/log-shell comparisons. Corollary 4.6(ii) ensures compatible global/local monoid reconstructions, rather than unrelated choices of rho. The application trace still has not produced the comparison on the full contact diagram of the retained (cQ3) collections from these data. In particular, the presently inspected arguments do not give this trace a verified alpha_v/beta_v on that diagram or a verified identification of its hull parameter after the prescribed pullbacks. This is a statement about the unfinished application, not an exhaustive claim about what can be deduced from the theory.

Even if the displayed presented-level functor were fully supplied, its compatibility with the permitted tensor-power-twist and log-iterate diagrams would still need verification before invoking the formal quotient and subsequent synchronization. This single-pair audit has not supplied coherent iterates or compared the fixed q-relation through the whole algorithm. It neither replaces the formal quotient by an orbit set nor requires Kummer/log squares to commute strictly in original representatives.

## Outcome and bounded continuation

EXPLORATION / RESEARCH / REPRODUCTION / proof_audit. The completed work is the typed transport calculation and orbit/arrow/forgetting checks above, followed by the unsuccessful application to the actual retained adjacent pair. It clarifies why individual lambda representatives are not an additional fixed-choice obstruction, but establishes neither the missing background-to-contact comparison nor the determinant identification. No source-compatible obstruction, invariant, new canonical lemma or result beyond the assessed methods is claimed. The main gap and all independent initial-data, directed (*), pilot/action/factorization, authentication, synchronization, essentiality and finite-B>=A gaps remain.

This is the second mathematical EXPLORATION on the formal-descent route, counting step528 and retaining the step529 source advance without resetting this count. Reassess rather than invoke the background theorem a third time as though the missing application were automatic. The next independently checkable source question concerns the actual global/local contact interface at one nonarchimedean place. IUT II, Corollary 4.5(ii), p.132, explicitly constructs its reconstructed global Frobenioid via IUT I, Example 3.5(i),(iii); III's retained prime-strip context also refers to IUT I, Definition 5.2(iv). These particular construction cases have not been covered for the contact-naturality question by the saved assessment. Their inspection requires a separate literature turn; no unassessed extension is proved here.

The new assessment `drafts/literature/2026-10-28-reconstructed-contact-interface.md` therefore records REVIEW_REQUIRED, with the exact source question and no approved calculation. A positive answer at one place would remove one concrete premise from the transport trace, while leaving the determinant/formal-equivariance and other-place questions open. A negative scope answer must identify the missing named datum rather than infer impossibility. If the contact interface cannot be specified from those constructions, park the dependent transport work instead of repeating the broad coricity audit.

A creative invariant test remains unjustified: the permitted action on the actual contact/marked diagram is not yet identified, so a claimed invariant could test a stronger or different quotient. This is a blocker to selecting such a test, not a ban on a later materially different mechanism. Preserve the recorded stops. No PROOF assembly or DAG change is warranted by an unfinished application.

## Mathlib

Full matching transport for these Frobenioid relative diagrams: **not checked**. Supporting category-theoretic naturality and comma-category constructions: **not checked**. No absence, formal verification or new general theorem is claimed. The displayed calculation is retained as unfinished application reasoning, not promoted to a canonical lemma with unverified IUT hypotheses.
