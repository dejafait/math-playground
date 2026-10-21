# L022 — A surviving exponential-degree component of the assembled output

## Hypotheses

For m>=2 use exactly L019's refutation pi_m of

F_*=(x) AND (y) AND (NOT x OR NOT y),

with z_0=x, z_1=y and z_i iff (z_(i-1) AND z_(i-2)) for 2<=i<=m. Original identifiers are 1,2, and z_i has identifier i+1. Keep the input clause order shown, sort proof clauses by increasing absolute identifier (positive before negative at a tie), and keep the source premises and pivots of `scripts/er-unfolding/check_literal_substitution.py`.

Let C_m be the formal output polynomial of the deterministic `Assembly` construction in `scripts/shared-extension/check_assembly.py`, implementing L021, on that input. Work in the free noncommutative polynomial ring over F₂ on x,y and the original axiom placeholders. Write t_1,t_2,t_3 for the clause placeholders; the other placeholders index x²+x, y²+y and xy+yx. Every free input, including a placeholder, has degree one. Do not substitute the axioms, reduce Boolean powers, or commute letters.

Arithmetic trees are division-free, fan-in-two addition/multiplication formulas with field-constant and variable leaves, without powering gates or succinct word leaves. Let Fib_0=0, Fib_1=1, and Fib_(j+2)=Fib_(j+1)+Fib_j.

## Conclusion

Let rho fix x,y,t_1 and send every other placeholder to zero. Then

rho(C_m)=t_1 R_m,
R_0=1,  R_1=0,
R_i=(R_(i-1)W_(i-2)+R_(i-2))(1+W_i),
W_0=x,  W_1=y,  W_i=W_(i-1)W_(i-2).                 (1)

The projected polynomial has a unique highest-degree word, with coefficient one, and

deg rho(C_m)=Fib_(m+3)+Fib_(m+1)-4.                   (2)

Consequently deg C_m is at least (2). Every arithmetic tree computing **the identical polynomial C_m** has size at least Fib_(m+3)+Fib_(m+1)-5, using the supporting degree/size convention below. This exceeds every fixed polynomial in T_m=2+|F_*|+|pi_m|=Theta(m log(m+2)). The obstruction concerns the final formal polynomial, not just an intermediate gate or occurrence tree.

This rejects a polynomial-size same-polynomial tree conversion of the fixed L021 construction. It does not lower-bound every IPS certificate, prove that every ER translation has this degree, supply an ER lower bound, or resolve P versus NP. L019's constant-size alternative certificate is retained. The standard degree/size comparison is imported; the family-specific surviving component is established here under the prior SPECIALIZE assessment, potentially beyond the inspected full-statement match, without a certified originality claim.

## Proof

**Projection removes every correction without altering x-only coefficients.** L021's K and B witness networks use only original-variable Boolean and commutator placeholders. They are built by addition and multiplication by x-only values. They therefore vanish under rho, even though t_1 remains free. So do every substituted extension-clause witness, adjacent-swap correction, duplicate-deletion correction and pivot-commutator correction. The latter operations add witnesses; they do not replace a clause-placeholder coefficient. This uses the specified construction, rather than merely its IPS identities. The original values of z_i are exactly the monomials W_i, and their positive-literal falsity factors are 1+W_i.

The three initial roots project to t_1,0,0. In the source family, derive each positive unit z_i first by resolving the positive unit z_(i-1) against the third defining clause, then by resolving the positive unit z_(i-2) against that intermediate clause. Let U_i be the projected root for the positive unit z_i; U_0=t_1 and U_1=0.

The third defining clause has sorted list

[NOT z_(i-2), NOT z_(i-1), z_i].

For its first resolution, the left premise is the unit z_(i-1). The right negative pivot moves to the front; the added swap witness projects to zero. Its remaining factors, in order, are W_(i-2) and 1+W_i. In L021's resolution expression R V+U S+H V, the left nonpivot product U is 1, S is the projected defining-clause root 0, and H projects to zero. Hence the intermediate root projects to

U_(i-1) W_(i-2)(1+W_i).

Its sorted clause is [NOT z_(i-2), z_i]. The second resolution has the positive unit z_(i-2) on the left and this clause on the right, with the negative pivot already first. Its remaining right factor is 1+W_i; the left nonpivot product is again 1. Its projected root is therefore

U_i=U_(i-2)(1+W_i)+U_(i-1)W_(i-2)(1+W_i).             (3)

No duplicates or further reorderings change this expression. In particular W_(i-2) is on the **right** of the earlier unit root, and precedes 1+W_i. Induction, factoring on the right by distributivity without commuting any factor, gives U_i=t_1 R_i with (1).

**The final root retains this component.** The first negative unit, NOT z_2, is obtained using the two projection clauses of z_2 and the third original clause. All three of those roots project to zero. L021's resolution rule combines parent roots with x-only products and correction witnesses, so both negative inferences project to zero. For i>=3 the negative chain resolves the first projection clause of z_i against the preceding negative unit. The same reasoning makes every resulting negative-unit root zero under rho. This ancestry contains neither of the original positive-unit roots.

The final inference resolves the two units z_m and NOT z_m. Both remaining lists are empty, so their products are 1, there are no sorting/duplicate corrections, and the pivot-commutator term is zero. Its projected root is U_m+0=t_1 R_m. This proves (1) for the **final** output before axiom substitution. Distinct placeholder letters cannot cancel its t_1 words against words carrying a different placeholder.

**A unique leading word survives for every m.** Put d_i=|W_i|. Then d_0=d_1=1 and d_i=d_(i-1)+d_(i-2), hence d_i=Fib_(i+1). From (1), R_2=1+W_2. Its unique leading word is H_2=W_2 and its degree is e_2=2.

At i=3, R_1=0, so R_3=R_2 W_1(1+W_3). Its unique leading word is H_2 W_1 W_3 and e_3=e_2+d_1+d_3=6>e_2. For i>=4 assume the assertion at all previous indices, including e_(i-1)>e_(i-2). In

R_(i-1)W_(i-2)+R_(i-2),

the first summand has degree e_(i-1)+d_(i-2)>e_(i-2). Its unique leading word is H_(i-1)W_(i-2). Thus no word from the second summand can cancel it. Multiplication by 1+W_i adds the strictly positive degree d_i at the top. The unique leading word and degree become

H_i=H_(i-1)W_(i-2)W_i,
e_i=e_(i-1)+d_(i-2)+d_i>e_(i-1).                       (4)

All factors W_j are single words of coefficient one; concatenation with a fixed word preserves distinctness. The unique longest word cannot cancel with shorter words in characteristic two. This proves the induction without relying on syntactic degree as a lower bound.

For m>=2 summing (4), with empty sums at m=2, gives

e_m=2+sum_(i=3)^m d_i+sum_(i=3)^m d_(i-2)
   =2+(d_(m+2)-5)+(d_m-2)
   =d_(m+2)+d_m-5.

The sum identities follow by telescoping d_j=d_(j+2)-d_(j+1); their endpoint values d_0=d_1=1, d_2=2, d_3=3 also cover m=2. Prefixing the independent letter t_1 raises degree by one and does not change coefficients. This proves (2). Since rho only replaces variable leaves by zero, it cannot increase polynomial degree. Equivalently every surviving word t_1 H_m already occurs in C_m. Thus deg C_m is at least (2); no exact upper bound for its other-placeholder sectors is asserted.

**Imported tree comparison and the required asymptotic threshold.** Use Li–Tzameret–Wang, [*Characterizing Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4, 11 September 2015, Definition 4.5 and the opening of the proof of Theorem 4.7, printed pp. 23 and 25](https://arxiv.org/pdf/1412.8746v4): a size-s noncommutative formula has polynomial degree at most s+1. The already inspected degree/size comparison applies with x,y and placeholders all treated as variables, over F₂, to the division-free binary trees specified here. This is a supporting theorem, not a theorem about this ER family. It gives the stated lower bound s>=deg C_m-1. Changing between standard tree node and edge counts changes at most an additive one.

For i>=2, d_i>=2d_(i-2), so d_m>=2^floor(m/2). Also d_(m+2)+d_m-4>=d_m for m>=2. L019 supplies the independent binary input bound T_m=Theta(m log(m+2)). Hence for every fixed k and constant K, eventually

Fib_(m+3)+Fib_(m+1)-5 > K T_m^k.

The achieved threshold is therefore superpolynomial in the actual supplied input length, as required by the assessment. Full binary tree descriptions also cost at least their tree size, up to fixed encoding factors. This rules out a fixed polynomial bound for trees computing the exact C_m, even when algorithms may completely reorganize its expression rather than unfold its circuit.

**Limits and finite verification.** After substituting A(x) for the placeholders, L021 gives C_m(x,A(x))=1. That substitution changes the polynomial and cannot serve as a degree test in independent variables. The original fixed CNF has L019's seven-node alternative certificate (t_3+t_1 y)+t_2, with degree two. Thus a translation choosing a different certificate may avoid this obstruction. Polynomial-degree circuit certificates, efficient tree conversion for a different output, all-certificate hardness, unrestricted decision transfer and the main goal remain unresolved.

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/shared-extension/check_output_degree.py`. It verifies the source ER family and exactly expands the projected assembly into independent noncommutative words for 2<=m<=10. Every positive and negative unit is compared with the independently generated recurrence; the unique leading word is checked. For 2<=m<=6 it also expands the full output with every placeholder kept as an independent letter and extracts its t_1 sector. No Boolean evaluation, axiom substitution or commutative specialization is used. For m=16,32,64,128 it checks a zero-aware syntactic upper bound for the projected assembly against (2), without word expansion. At m=128, T=52,518 bits and (2) is 1,473,646,213,395,791,149,646,646,119. The [saved results](../scripts/shared-extension/output-degree-results.json) distinguish those scopes. The all-m proof is the induction above, not an inference from the finite checks. This remains an informal result, not a proof-assistant verification.

## Mathlib

Coverage: **not checked** for this exact output polynomial, its projection, noncommutative degree or the formula-size lower bound. Li–Tzameret–Wang's Definition 4.5 / Theorem 4.7 proof opening, directly linked above, supplies the inspected supporting degree/size comparison. Forbes–Shpilka–Tzameret–Wigderson, [*Proof Complexity Lower Bounds from Algebraic Circuit Complexity*, Theory of Computing 17(10), 2021, Remark 1.3 and Theorems 1.2/1.4, printed pp. 5–6](https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf), permits exponential degree in a different commutative EF-to-circuit translation and supplies supporting model comparisons; it does not establish this noncommutative family result. Neither source is asserted to match the full statement. No Mathlib identifier, absence claim or certified originality is inferred.
