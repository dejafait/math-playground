# L093 — Putz algebra interface for ordered (3,5,11)

## Hypotheses

Let A,B,C be positive integers satisfying A^3+B^5=C^11 and gcd(A,B,C)=1. Put s=B^5/C^11, phi(t)=(3t^2+t+1)^5(1−5t), and E=Q[t]/(phi(t)−s).

The external input is P. H. C. Putz, *Enumeration of local and global étale algebras applied to generalized Fermat equations*, Vrije Universiteit Amsterdam doctoral thesis (2024), DOI [10.5463/thesis.832](https://doi.org/10.5463/thesis.832), version of record, **Section 5.2 p.165 and Propositions 5.18–5.20 pp.168–169** ([primary PDF](https://research.vu.nl/ws/portalfiles/portal/367784086/Thesis_CasperPutz.pdf), PDF indices 171,174–175).

Those propositions concern nontrivial integer solutions of a x^5+b y^3=c z^11 with gcd(ax,by,cz)=1, nonzero pairwise coprime integer coefficients, and, for Proposition 5.20, odd abc. They are not restricted to the nine coefficient triples of Theorem 5.1. Proposition 5.20 is a computational theorem citing Algorithm 2.74 and local_algebras.m; its conclusion is imported without an independent replay. The primary statements and relevant proof cases were inspected; the prior assessment is drafts/literature/2026-10-18-ordered-three-five-eleven-algebra-import.md.

## Conclusion

E is an étale Q-algebra of degree eleven and satisfies:

1. E tensor_Q R is isomorphic to R × C^5.
2. E is unramified at every rational prime outside {3,5,11}.
3. Writing U_d for the unramified degree-d extension of Q2 (U_1=Q2), its entire two-adic completion is isomorphic to one of
   U_10 × U_1, U_5 × U_3 × U_2 × U_1, or U_4 × U_4 × U_2 × U_1.

Each product retains all factors and their multiplicities. No irreducibility, realizability of every listed possibility, or signature exclusion is asserted.

## Proof

Apply the cited propositions with coefficients (a,b,c)=(1,1,1) and coordinates (x,y,z)=(B,A,C). The equation becomes exactly x^5+y^3=z^11. All three coordinates are nonzero integers. The source gcd is gcd(B,A,C)=1, exactly the hypothesis. Coefficients equal to one are nonzero, odd and pairwise coprime. Thus every coefficient and coordinate hypothesis in all three propositions holds. For clarity, the original equation also forces pairwise coprimality of the bases: any prime dividing two divides the third power by subtraction and hence the third base, contradicting gcd one. No stronger independent primitivity assumption is being made.

The source parameter a x^5/(c z^11) is s, so its algebra is precisely E. Positivity gives s>0 and 1−s=A^3/C^11>0. Hence s is neither branch value 0 nor 1. The polynomial has degree eleven with nonzero leading coefficient. Its discriminant is nonzero by Putz's equation (5.2), since s(s−1) is nonzero. Consequently its quotient is étale of the full degree eleven, even if reducible.

Proposition 5.18 gives the real completion in (1). For any prime p outside {3,5,11}, p does not divide abc=1; Proposition 5.19 therefore gives (2). This includes primes dividing a coordinate: the cited proof treats p not dividing xyz, p dividing x, p dividing y, and p dividing z, the last using the infinity chart. We invoke that whole proposition rather than applying an integral polynomial discriminant test at a parameter with denominator, or asserting a new verification of Theorem 2.72's normalization hypotheses.

Since 2 does not divide abc, Proposition 5.20 gives (3). Its unramified extensions have the indicated degrees; the two degree-four factors in the last product are both retained. The degree sums are 10+1=11, 5+3+2+1=11 and 4+4+2+1=11, so no selected field factor has replaced the entire algebra. This completes the cited application.

This is KNOWN_IMPORTED local progress, not a result beyond the checked source. No use is made of Theorem 5.1, its special coefficient set, or its terminal global eliminations. Unit bases are included by these hypotheses; L029 is a separate boundary exclusion and is not an input here. L002 is downstream context only. An unconditional global elimination and integer power lifting remain unproved. No abc or GRH hypothesis, field enumeration, height bound or global irreducibility is supplied.

### Independent critical application audit — 2026-10-18

Verdict: **PASS without correction**, for the necessary interface exactly as stated. This checks the application of imported theorems, not their computational implementation. The audit used the prior IMPORT assessment `drafts/literature/2026-10-18-ordered-three-five-eleven-interface-audit.md` and reopened the primary version of record at printed pp.165,168–169.

The definition of S on p.165 refers to the primitive equation (5.1), with nonzero coordinates; it is not limited to the special coefficient set C. Substitution of (1,1,1;B,A,C) meets that definition, including units. Swapping the summands changes neither an exponent on a coordinate nor a sign. The source parameter becomes B^5/C^11, and 1−s=A^3/C^11. Thus 0<s<1. Equation (5.2) is

    disc_t(phi(t)−s) = −3^50 · 5^10 · 11^11 · (s−1)^2 · s^8.

Its nonvanishing and the leading coefficient −5·3^5 justify the full degree-eleven étale quotient. No irreducible-factor selection is involved. Proposition 5.18 applies to this same quotient, giving exactly one real embedding and five conjugate pairs.

For the scope of Proposition 5.19, pairwise coprimality proved above makes the coordinate-divisor cases exhaustive and disjoint. At a prime p outside {3,5,11}, if p divides no base then s and s−1 are p-adic units. If p divides B, then v_p(s)=5v_p(B)>0; if p divides A, then v_p(s−1)=3v_p(A)>0; if p divides C, then v_p(1/s)=11v_p(C)>0. These match the zero, one and infinity branches in the proposition's proof. In particular its conclusion covers primes dividing C; polynomial discriminant integrality at such primes is not assumed. The cited theorem, including its normalizations, remains the input rather than an independently reproved ramification calculation.

For Proposition 5.20 the extra hypothesis is 2 not dividing abc, not oddness of all solution coordinates. Here abc=1, so no even-coordinate case is lost. The products retain all source factors, with two distinct factor positions of degree four in the third possibility. Each total degree is eleven. A rational two-adic factor does not imply a rational global factor. The source's Algorithm 2.74 computation remains imported without replay, and a covering list need not have every entry realized by a positive primitive integer solution.

No mismatch, new exclusion or new arithmetic information was obtained. Theorem 5.1 and its special-coefficient terminal eliminations remain outside the application. Global algebra elimination and integer lifting are still unresolved. The audit adds no mathematical input to the empty L093 DAG row.

## Mathlib

Full matching coverage of Putz's propositions and supporting declarations: **not checked**. No formal verification or absence claim is made.
