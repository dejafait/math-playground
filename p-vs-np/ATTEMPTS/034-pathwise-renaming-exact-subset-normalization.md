# Attempt 034 — Pathwise cutoff for the unchanged subset normalization

The target was a uniform polynomial full-bit/time bound for L101's exact
request normalization when each backward source-reference path has at
most floor(log₂ Q) renaming lines, with original Q fixed in advance.

**WHY IT FAILS.** [L102](../lemmas/L102-pathwise-renaming-normalization-request-obstruction.md)
gives legal variable-free ground-axiom proofs with h layers and 2^h
parallel identity renamings per layer. Every path visits at most h
renaming lines, within the original cutoff, but the actual request
closure reaches the initial axiom under 2^(h²) distinct index subsets.
The specified materialization writes a separate ordinary axiom record
for each of those requests. Original Q is at most C(h+2)³2^h, making
this superpolynomial. Equal map actions and formulas are deliberately
not merged by the tested cache. The separate step-400 all-size informal critical audit in L102 finds no
substantive defect; no mathematical script or finite preview is its evidence.

Stop this unchanged implementation for the changed promise. Preserve
L101's global-count theorem and Attempts 020/032/033. Identity-rule
deletion, formula/action interning, other normalization, and alternative
proofs or witnesses are outside the tested implementation. The source
formula has an immediate proof and zero witness, so this is not an
ordinary-Frege, ABP, proof-system or SAT lower bound. A different
mechanism requires its own exact target and literature assessment.
