# Shared ABP transition calculation

Research calculation dated 2026-10-04, within the unchanged EXPLORE target in `drafts/literature/2026-10-03-shared-homogeneous-ips-ef.md`. No additional source search is needed for the screened coefficient-matrix test.

The precise intermediate obligation is a polynomial-size CF/EF proof that a homogeneous F₂ noncommutative zero ABP evaluates to zero with its Boolean assignment variables free. Its prospective use is to replace the formula-unfolding stage in the arbitrary-degree formula-IPS simulation. Identification of the original formula with these component evaluations, assembly of both IPS identities and the original-CNF ER conversion are separate remaining obligations. A fixed polynomial in the explicit binary ABP/witness size is required; an external PIT answer or a quasipolynomial unfolding does not meet the test.

For layer matrices M(i,a), let R(i) contain a row basis of the length-i coefficient space, with R(0)=e_source. Import the standard ABP coefficient-space witness construction covered by Li–Tzameret–Wang Lemma 4.15 and Raz–Shpilka's basis calculation. Its finite constant matrices T(i,a) satisfy

    R(i-1) M(i,a) = T(i,a) R(i).

For a zero output, R(d)e_sink=0. Define shared Boolean circuits, using XOR for F₂ addition and AND for multiplication:

    p(0)=e_source; p(i)=sum_a (p(i-1) M(i,a)) x_a;
    q(0)=1;        q(i)=sum_a (q(i-1) T(i,a)) x_a.

The candidate inductive invariant is p(i)=q(i)R(i). Each step substitutes the previous invariant, distributes XOR/AND, and checks equality of the two coefficient tables. All sums have polynomially many terms and retain their shared p/q gates. Sorting terms and cancelling equal pairs should give a polynomial proof using fixed local tautologies, without enumerating words. The last invariant and the checked terminal matrix give the output zero.

The calculation must explicitly account for empty coefficient spaces, unused variables, repeated terms, extension definitions and a formula conclusion for CF-to-EF conversion. In particular, a CF proof of a circuit output alone must not be passed to the formula-conclusion conversion. Use the polynomial formula `Delta_B -> not o_B`, where Delta_B is the conjunction of the original ABP evaluation-gate definitions, to retain the output interpretation without unfolding it.

This derivation is being saved before the detailed proof and finite checks. It does not yet assert the intermediate lemma or the full simulation. Continue this mechanism only if the witness transitions and their proof costs can be made explicit; otherwise preserve the failed obligation. The semantic linear algebra is imported, while its shared propositional realization is the assessed difference under investigation.

## Mathlib

Coverage: **not checked** for the ABP witness realization or the full simulation. Relevant supporting sources and direct theorem links are preserved in the prior assessment/source note; there is no claimed full Mathlib or literature match.

## Completed calculation

The detailed proof is recorded in [L017](../lemmas/L017-shared-homogeneous-abp-zero-proofs.md). It constructs the guarded formula conclusion `Delta_B -> not o_B` in CF and then imports the formula-conclusion CF-to-EF conversion. Each transition compares two term lists of at most nW² entries, using the checked constant matrix equality to sort and cancel them; even the enclosing XOR contexts and whole per-line circuit descriptions have a fixed polynomial bound. Empty spaces and the terminal table are included. No formula-to-ABP identification or complete IPS simulation has been inferred.

The finite indexing check `python3 scripts/shared-abp/check_witnesses.py` passed 143 examples, comparing 1,991 noncommutative word coefficients and 677 Boolean assignments. It checks all layer invariants and rejects a corrupted transition; xy+yx demonstrates why Boolean zero alone does not supply a zero terminal coefficient space. These are finite checks of the construction's orientation, not an EF proof checker. The original pre-proof reasoning above is preserved.
