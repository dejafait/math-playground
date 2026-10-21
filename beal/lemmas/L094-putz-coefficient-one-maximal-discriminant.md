# L094 — Coefficient-one maximal-algebra discriminant restrictions

## Hypotheses

Let A,B,C be positive integers with A^3+B^5=C^11 and gcd(A,B,C)=1. As in L093, put s=B^5/C^11, phi(t)=(3t^2+t+1)^5(1−5t), and E=Q[t]/(phi(t)−s). Let O_E be the integral closure of Z in the entire étale algebra E, and let delta=disc(O_E/Z), defined by the trace pairing on an integral basis. For each rational prime p, v_p is normalized by v_p(p)=1; its value on the nonzero integer delta is unaffected by sign.

The external input is P. H. C. Putz, *Enumeration of local and global étale algebras applied to generalized Fermat equations*, Vrije Universiteit Amsterdam doctoral thesis (2024), version of record, DOI [10.5463/thesis.832](https://doi.org/10.5463/thesis.832), **Proposition 5.7 p.165 and Table 5.8 p.166**, with the entire-algebra discriminant convention in **Section 1.5.2/Proposition 1.16 p.22** ([primary PDF](https://research.vu.nl/ws/portalfiles/portal/367784086/Thesis_CasperPutz.pdf), PDF indices 171–172 and 28). The prior IMPORT assessment is `drafts/literature/2026-10-18-ordered-three-five-eleven-discriminant-import.md`.

## Conclusion

The discriminant of the entire maximal algebra satisfies

| Prime p | Necessary possibilities for v_p(delta) |
|---|---|
| 3 | 6, 8, 10 |
| 5 | 8, 10 |
| 11 | 9, 11 |

These are covering restrictions, not an assertion that every choice or combination occurs. They concern all global factors together, without an irreducibility hypothesis. They do not exclude any positive primitive solution by themselves.

## Proof

Apply Proposition 5.7 with source coefficients (a,b,c)=(1,1,1) and source coordinates (x,y,z)=(B,A,C). Its equation a x^5+b y^3=c z^11 is exactly the given equation. All coordinates are nonzero integers, and its primitive condition gcd(ax,by,cz)=1 is precisely gcd(B,A,C)=1. The coefficients are nonzero pairwise coprime integers. Thus this is a nontrivial primitive solution in the source's scope, without invoking Theorem 5.1's special coefficient set.

The source parameter a x^5/(c z^11) equals s. Its displayed algebra is therefore E, the same entire algebra certified étale of degree eleven by L093. In particular 0<s<1, so neither branch value 0 nor 1 occurs. No factor is selected and no rational field factor is inferred from a local factor.

For each p in {3,5,11}, v_p(abc)=v_p(1)=0. Hence the coefficient-unit row of Table 5.8 applies at each of these primes and gives exactly the three sets displayed above. Its condition is on abc, not xyz. Therefore no assumption that p avoids A, B, or C is needed. In particular, cases where a coordinate has positive valuation, including the denominator coordinate C in the infinity branch, remain within this cited application. There is no bound on coordinate valuations imposed here.

The discriminant used by the proposition is that of the integral closure in the full algebra, as defined on p.22. If E is a product of number fields, its maximal ring is the product of their integer rings and the trace pairing is block diagonal; delta is the product of their discriminants, by the cited entire-algebra convention. The table therefore bounds the sum of their p-adic discriminant valuations. It is not a bound on the discriminant of the polynomial phi(t)−s or its power order, and no polynomial-index equality is assumed.

Proposition 5.7's proof cites Algorithm 2.74 and the accompanying Magma script `ramification.m`. We import that computational theorem by precise citation, without code inspection, execution, or an independent verification of its enumeration. No conditional hypothesis is stated for this proposition. Its extra transformations for the nonunit-coefficient Table 5.11 are not used. Remark 5.13 p.167 warns about the size of the coefficient-one degree-eleven Hunter workload; the present application neither performs that enumeration nor imports the terminal exclusions for other coefficients.

This completes the hypothesis-checked import. It is KNOWN_IMPORTED local progress, with no result beyond the checked source and no new computational reproof. Global algebra elimination, global irreducibility, and integer power lifting remain unresolved. No abc, GRH, effective height bound, or complete list of number fields is assumed.

### Independent critical application audit — 2026-10-18

Verdict: **PASS without correction**, as an application of the cited computational theorem. The prior IMPORT assessment is `drafts/literature/2026-10-18-ordered-three-five-eleven-discriminant-audit.md`. The audit reopened the primary version of record at printed pp.22,163,165–167, including the complete statement, table and proof of Proposition 5.7. It does not verify the implementation behind that theorem.

The actual source equation (5.1) becomes B^5+A^3=C^11 under (a,b,c;x,y,z)=(1,1,1;B,A,C); its gcd is gcd(B,A,C)=1. All coefficient and coordinate nonvanishing requirements hold, including unit bases. Section 5.2 defines the solution set for general nonzero coefficients. Proposition 5.7 explicitly assumes pairwise coprime coefficients, without the special coefficient-set restriction of Theorem 5.1. Its parameter is exactly s, and L093 supplies the full degree-eleven étale algebra at 0<s<1.

Here is an exhaustive coordinate check, independent of any unit-coordinate reading of the table. If a prime divides two of A,B,C, the equation forces it to divide the third, contradicting primitivity. Thus for each p in {3,5,11} exactly one of the following patterns applies. Write k for the positive valuation in a divisible-coordinate row.

| Coordinate pattern | v_p(s) | v_p(1−s) |
|---|---|---|
| p divides no coordinate | 0 | 0 |
| p divides B | 5k | 0 |
| p divides A | 0 | 3k |
| p divides C | −11k | −11k |

These values follow directly from s=B^5/C^11 and 1−s=A^3/C^11. In every row the coefficient product is still abc=1. Consequently the applicable source condition remains v_p(abc)=0; no finite bound on k, unit denominator, or change to a nonunit-coefficient table is justified or needed. The last row specifically retains the infinity branch. This is a check of theorem applicability, not a new ramification proof.

Direct comparison with Table 5.8 confirms all entries: {6,8,10} at 3, {8,10} at 5, and {9,11} at 11. Section 1.5.2 and Proposition 1.16 identify its discriminant with that of the full integral closure. For E=product_i K_i, the supported integral bases of the O_{K_i} give a block-diagonal trace matrix, hence delta=product_i disc(O_{K_i}/Z). Taking v_p gives a sum over every component, including repeated isomorphism types. There are no cross-resultant factors here: those belong to polynomial discriminants. No irreducibility or power-order maximality is used.

The proof's Algorithm 2.74/ramification.m input remains imported without replay. Its extra transformations concern Table 5.11, not the coefficient-unit table. The audit found no additional conditional premise. The values remain necessary covering sets, with no simultaneous realization claim. Remark 5.13's coefficient-one Hunter workload warning remains intact.

No defect, new exclusion or stronger bound was obtained. The audit secures the existing restriction for potential global-candidate filtering; global elimination and integer lifting remain open. Its only direct local lemma input is still L093, so the DAG and mathematical overview do not change.

## Mathlib

Full matching coverage of Proposition 5.7/Table 5.8 and supporting declarations: **not checked**. No formal verification or absence claim is made.
