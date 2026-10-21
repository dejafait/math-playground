# Conditional q=29 exceptional-field parameter audit

This is exactly the mathematical audit authorized by the ready SPECIALIZE assessment in [the parameter-bridge assessment](literature/2026-10-04-mixed-seventh-parameter-bridge.md). The main gap is uniform zero positive primitive solutions for the residual Beal signatures. The intermediate target connects an explicit exceptional descent algebra to L016's four parameters; it does not establish that every solution has that algebra, the representation hypotheses, irreducible-packet coverage or the other global branches.

The threshold sought is: for every nonzero primitive signed integer solution X^5+Y^3=Z^7 with A_eta=Q[T]/(Phi(T)-eta) isomorphic to the stated exceptional field, prove 29 does not divide XYZ and eta reduces to {10,14,24,28}. Check all ordinary residues and all nonzero unit residues in each coordinate-divisibility branch. A missed root cluster or a branch matching the exceptional factor type stops reliance on the claimed bridge. Four survivors are not zero integer solutions.

## Reasoning saved before enumeration

Let p=29, Phi(T)=15T^7-35T^6+21T^5 and eta=X^5/Z^7. Primitivity and the equation imply pairwise coprimality, so at most one coordinate is divisible by p. The derivative is 105 T^4(T-1)^2. The ordinary reduction is separable for eta not 0 or 1. Reconstruct the exceptional polynomial's factor type independently.

If a=v_p(X)>0, write eta=p^(5a)u with u a unit. The two roots away from zero lift from 15T^2-35T+21. For the five roots near zero, use the integral polynomial p^(-5a)(Phi(p^a S)-eta), whose reduction is 21S^5-u. Each nonzero simple residue root lifts in an unramified extension; together with the two unit roots this accounts for degree seven. This avoids applying monic factor-Hensel to a degree-dropping reduction.

If b=v_p(Y)>0, eta-1=p^(3b)u. The identity Phi(1+V)-1=V^3(35+105V+126V^2+70V^3+15V^4) gives three roots via p^(-3b)(Phi(1+p^b S)-eta), reducing to 35S^3-u, and four other roots via the quartic. If c=v_p(Z)>0, write eta=p^(-7c)u; all seven roots are supplied by p^(7c)(Phi(p^(-c)S)-eta), reducing to 15S^7-u. The normalizations preserve every positive valuation and signed unit.

For each separable reduction, Frobenius orbit lengths of its roots give the unramified Q_p-algebra degrees. Hensel uniqueness makes the lifted roots equivariant for Frobenius; multiplying or translating by Q_p scalars does not change those orbit lengths. A Q-algebra isomorphism base changes to Q_p, whose product-factor degrees are invariant. Check the source's printed branch types as arithmetic claims, and retain a correction if one differs without assuming that the final restriction fails.

Classification intended: REPRODUCTION of the screened conditional claim, using cited general inputs; no novelty inference from search failures. Mathlib coverage is not checked. The stopped unconstrained congruence route does not bar this test with its explicit global field hypothesis, and no repeated-cube route is reopened.

## Completed audit

The full conditional implication is reproduced in L018, with all original saved reasoning retained above. The exceptional polynomial has squarefree factor type [1,3,3]. All 27 ordinary parameters, all 84 branch-unit residues and all three fixed polynomials were checked by Frobenius gcds. The four matching ordinary parameters and exceptional polynomial also have explicit linear/two-cubic product certificates. Every printed table agrees; t0 is respectively 14,10,25,15. The exact standard-library reproducer and output are scripts/mixed-seventh-certificate/check_parameters.py and parameter-results.json in that directory.

The local proof handles every positive valuation with integral scaled polynomials. Simple-root lifting over finite unramified extensions produces two plus five roots when 29 divides X, four plus three when it divides Y, and seven when it divides Z. Root counts exhaust the degree and preserve orbit lengths. All branch types differ from [1,3,3], so the algebra-isomorphism hypothesis excludes coordinate divisibility at 29 and forces the four ordinary parameters. No unread local-model theorem or global Branch (II) assumption is used.

Completed classification: RESEARCH / ADVANCE / REPRODUCTION. This is a newly established notebook input, not mathematics beyond the checked source claim or a signature exclusion. The exceptional-algebra hypothesis remains explicit, as do the original representation, irreducible-packet and global-descent gaps. The next direction is theorem-level assessment of the original representation hypotheses of L017, a changed target beyond its prior conditional character coverage; the persistent descent and archive blockers remain parked. Mathlib coverage stays not checked.
