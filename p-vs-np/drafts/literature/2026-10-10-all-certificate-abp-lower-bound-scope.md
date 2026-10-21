# All-certificate affine-ABP lower bounds — completed source-scope review

TARGET: Assess whether FSTW's IPS lower-bound theorems cover every original-axiom affine-F₂ ABP certificate of an explicit width-three UNSAT family in L048's format.
CHECKED: 2026-10-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Two targeted external queries located the journal lower bounds and finite-field follow-ups; read the primary journal statements and essential proof cases and reused the existing finite-field assessment. Exact queries and qualifications below; no search establishes novelty or nonexistence.
SOURCE_EVIDENCE: FSTW, Theory of Computing 17(10), 2021, Definitions 1.1/1.8, pp.3,6–7; Lemmas 5.1/5.2, pp.42–44; Proposition 5.13 and Corollaries 5.14/5.15, pp.51–52; Corollary 6.23, p.65; Lemma 7.1 and Corollaries 7.2/7.3 with complete proofs, pp.66–68; Discussion items 2/3, p.68. The relevant statements and proof cases were read in the 88-page journal PDF, not inferred from search snippets.
COMPARISON: The checked lower bounds quantify over every certificate in specified commutative roABP or multilinear-formula classes, rather than a selected output; none matches L048's arbitrary free-F₂ affine graphs and original width-three clause/Boolean/commutator axioms. Corollary 7.3 admits nonlinear placeholders but retains the field, model and axiom mismatches.
GAP: A transfer would still need a suitable F₂ UNSAT clause family, a certificate-class-preserving reduction, both formal original-axiom identities and a polynomial full-formula-length ledger; no such transfer is supplied by the checked theorems.
REASON: New theorem/proof-level evidence parks direct FSTW import for this target. The recorded algebraic ABP/roABP correspondence motivates only a separate substitution-compatibility test, not a lower-bound transfer or a new theorem here.

## Completed step 144

The main gap remains unrestricted SAT decision/separation. The intermediate target was a theorem covering **every** C for some explicit UNSAT family in L048's exact format, with lower bounds exceeding every polynomial in complete formula length N. This could address certificate hardness; L049 still leaves arbitrary ER-to-ABP representation and decision transfer independent. Continue direct import only upon a matching field/model/axiom theorem or an inspected preserving reduction. Otherwise park it. The present comparison fails that test without proving an impossibility theorem.

### Primary evidence

Michael A. Forbes, Amir Shpilka, Iddo Tzameret and Avi Wigderson, [*Proof Complexity Lower Bounds from Algebraic Circuit Complexity*, Theory of Computing 17(10), 2021, 1–88, DOI 10.4086/toc.2021.v017a010](https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf). Printed and one-based PDF pages agree. Use the internal **Corollary** numbering below; introductory Theorems 1.16/1.20 summarize these results.

* Corollary 5.15, p.52: char(K)>binom(2n,2), β∉{0,…,binom(2n,2)}; axioms Σ_{i<j}z_ij x_i x_j−β, x²−x, z²−z. Every roABP-IPSLIN certificate, in any variable order, needs exp(Ω(n)) size. It also bounds multilinear-formula IPS. Read its complete proof and the preceding matching-restriction and coefficient-dimension cases.
* Corollary 7.3, pp.67–68: char(K)>n; f=∏_{i<j}(x_i+x_j−1), g=Σ_i x_i−n, and x²−x. Every roABP-IPS certificate, in any order, needs exp(Ω(n)) size, without placeholder linearity. Read the complete proof: unique Boolean solution of g, Lemma 7.1's nonzero-multiple extraction, coefficient interpolation, and read-twice normalization; Corollary 6.23 supplies the final lower bound.
* Definitions 1.1/1.8, pp.3,6–7, impose commutative identities and read-once oblivious layers. Section 7 and Discussion items 2/3, pp.66,68, distinguish restricted classes, globally supported axioms and the unresolved extension-variable/CNF transfer. No hypothesis-preserving CNF reduction is stated there.

These are source statements and proof-scope findings, not local derivations or imported lemmas. No reproof is justified or attempted. The general Lemma 7.1 statement was checked over an arbitrary field; its algebraic extraction alone does not supply the restricted receiving representation or a hard UNSAT instance over F₂. Corollary 7.2 concerns depth-three powering IPS in characteristic zero and supplies no closer receiving class.

### Exact receiving comparison

L048's hypotheses and formula ledger were read through the two component applications. They require free associative F₂ identities, actual occurring identifiers, ordered original clause positions, Boolean axioms and pair-once commutator axioms, a complete explicit dictionary, and arbitrary acyclic affine graphs. Mixed labels, repeated symbols on paths, arbitrary endpoints and nonlinear placeholder paths remain allowed. These requirements are not changed to make a theorem fit.

The all-certificate quantifier is present in the primary lower bounds, but only inside their stated subclasses. “Any variable order” allows any read-once order; it does not remove the read-once and oblivious restrictions. Affine labels in L048 do not impose either restriction. Likewise, neither the source's multilinear-formula result nor its unrestricted-placeholder roABP result covers every L048 graph. L046's already established replacement removes one placeholder-path restriction for supplied graphs; no roABP conclusion is stated in that interface, and it is not used here to derive one.

The characteristic assumptions fail for the unbounded F₂ family required by TARGET. Passing to a larger field of characteristic two does not satisfy a lower bound on characteristic. Changing characteristic changes the certificate identities and is outside the target. The source's global algebraic axioms are not L048's actual clause-falsity polynomials, even where a displayed polynomial has degree three. Total polynomial degree is not clause width or bounded variable support.

Commutator placeholders are independent symbols before substitution in L048. A comparison in the commutative quotient would need its own representation and substitution justification; it cannot retain a free-ring lower bound by naming the graph models alike. In particular, the polynomial-complexity correspondence mentioned in §1.2.2 is not an IPS simulation statement. Its original reference [27], Forbes–Shpilka, FOCS 2013, pp.243–252, [arXiv:1209.2408](https://arxiv.org/abs/1209.2408), is an **unread proof lead** for the distinct continuation below, not an essential missing source for the present negative scope verdict.

No F_n in the required CNF format or certificate-preserving reduction has been supplied. Consequently there is no formula length N_n or valid transfer comparing exp(Ω(n)) with all polynomials in N_n. L048's existing a(N+2)³ original-axiom ledger does not pay for an unproved new-family construction or establish hardness after adding gate clauses. Actual raw names, coefficients and placeholder dictionaries would all have to be charged in such a future reduction. The source bounds are not reported as achieved bounds for L048.

### Search, reuse and prior failures

Queries actually issued: `"Proof Complexity Lower Bounds from Algebraic Circuit Complexity" ABP IPS lower bounds characteristic` and `noncommutative IPS ABP lower bounds Frege all certificates finite field`. Primary journal text supplied the evidence above. Screenshot calls returned no inspectable images, including one timeout; they are not evidence. There is no essential source blocker for this review.

The previously inspected finite-field comparison in `drafts/literature/2026-10-08-boolean-zero-affine-abp-ideal-witness.md`, especially its finite-field paragraph, is reused: Elbaz–Govindasamy–Lu–Tzameret, ECCC TR25-080, Definition 9, Theorems 1/3, Corollary 43 and Proposition 48/Theorem 49. Its commutative roABP-IPSLIN′ and restricted multilinear scope does not remove the arbitrary-free-graph mismatch. The new search hits on positive-characteristic IPS and sums of roABPs remain unread leads; they are not matched theorems or claims of absence. No additional retrieval of that already adequate assessment was warranted.

L049's completed one-way comparison and its primary coverage are reused, without another audit. Attempts 020/021 were read: canonical L033/L034 obstruct prescribed outputs, not every certificate. No identical-output converter is reopened. A narrowly checked historical L032 audit is already complete and is not proposed for repetition. All unfinished work and Attempt 018 are preserved; no cross-notebook input is used.

### Decision and continuation

Outcome **NEGATIVE / LITERATURE / NOVELTY_UNCHECKED**: inspected theorem and proof scope changes the route by parking direct FSTW import. This is local source-scope evidence, not a new mathematical discovery, a proof of no possible transfer, or a P-versus-NP candidate. No lemmas or mathematical scripts were changed. PROOF.md and DAG.md are unchanged because the mathematical argument and its direct inputs did not change. Mathematical exploration usage remains one since step 141; this literature result does not spend or reset that budget.

The next independently testable interface is whether the position encoding cited in §1.2.2 preserves the actual two IPS substitutions, rather than merely polynomial identity and ABP complexity. Its exact proposed target and essential unread primary proof are saved in `drafts/literature/2026-10-10-position-encoding-ips-substitution.md` as REVIEW_REQUIRED. No preservation or counterexample is derived or approved here. Even preservation would leave the field, explicit original-CNF family, hardness and decision-transfer gaps open.

Mathlib coverage for the full source theorems and this certificate-scope comparison is **not checked**; unknown availability is not absence.
