# Siksek–Stoll's primitive (3,4,5) classification

## Hypotheses

Let x,y,z be rational integers, of either sign or zero, with gcd(x,y,z)=1 and x^3+y^4+z^5=0. The source calls a solution nontrivial when xyz is nonzero. Neither nontriviality nor a lower bound on the absolute values of the coordinates is imposed in its classification theorem.

## Conclusion

The complete list is

\[
(0,\pm1,-1),\quad(-1,0,1),\quad(1,0,-1),\quad(-1,\pm1,0).
\]

In particular, the cited theorem has no nonzero primitive signed solutions. This is the source's conclusion, not a new local proof or an assertion about arbitrary signatures.

## Proof

Imported source: S. Siksek and M. Stoll, *Partial descent on hyperelliptic curves and the generalized Fermat equation x^3+y^4+z^5=0*, **Bulletin of the London Mathematical Society 44** (2012), 151–166, **Theorem 1.1**. [Publication DOI](https://doi.org/10.1112/blms/bdr086). The inspected [author-hosted revised manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/345-revised.pdf) is dated **July 4, 2011**, with the theorem on manuscript p. 2 and its application proof in Sections 4–6, pp. 10–15. The publisher records the same revision date and publication on October 19, 2011. The separately inspected [arXiv:1103.1979v1](https://arxiv.org/abs/1103.1979v1) is the March 10, 2011 submission; it must not be labeled as a July arXiv revision. Both inspected theorem statements agree; the author-hosted revised manuscript is the chosen proof source.

The following records inspected source coverage, without independently reproducing its computations.

- Section 4, Theorem 4.1 (pp. 11–12), explicitly restates Edwards's completeness theorem for coprime signed integers a,b,c with a^2+b^3+c^5=0. Every such triple is represented as a=f_i(u,v), b=g_i(u,v), c=h_i(u,v) for coprime integers u,v and some 1<=i<=49. The integral binary forms have degrees 30,20,12 respectively; Table 1 and the following formulas specify them. The additional forms with negative f_i are retained. The cited original is J. Edwards, *A complete solution to X^2+Y^3+Z^5=0*, **J. reine angew. Math. 571** (2004), 213–236, especially pp. 235–236, last paragraph of p. 236. Edwards's original full text was not obtained; this is an inspected restatement in the primary paper proving the present classification.
- Section 5, Lemma 5.1 (p. 12), states the explicit square-condition reduction y^2=f_i(u,v), x=g_i(u,v), z=h_i(u,v) for coprime u,v and i in {2,3,5,6,15,16,17,23,24,27,28,29,31,32,36,37,38,40,41,43,44,47,49}. The curves have genus 14 in weighted projective space with weights (1,1,15); this is not restricted to an affine chart. Sixteen indices have no 2-adic points, two have no 3-adic points, and eight fail the source's square-and-primitivity test modulo 2^8. Further similar prime-power tests failed to eliminate the remaining indices. This is a source-certified constrained test, outside ATTEMPTS/001's unrestricted congruence mechanism.
- Section 6.1 (p. 13) treats all thirteen irreducible degree-30 forms using factorization of type [6,24] over specified quintic fields. The computed fake Selmer sets with local conditions at primes below 100, infinity, and primes dividing the leading coefficient are empty. The source uses emptiness of these necessary conditions to prove absence of rational points; it does not claim that this selected finite set equals all local conditions.
- Section 6.2 (pp. 13–14) treats indices 2,36, of type [10,20]. It gives index 2 in detail and states the other is practically identical. The quotient Y^2=X^5+20736 has Jacobian group Z/5Z by the cited MAGMA descent; its rational points, including infinity, give only zero-coordinate triples. The displayed larger triples are discarded as nonprimitive.
- Section 6.3 (pp. 14–15) treats indices 3,17,47, of type [6,12,12]. It gives index 3 in detail and records the curves' isomorphism. The quotient elliptic curve Y^2=X^3+25 has group {O,(0,5),(0,-5)}; the resulting triples have a zero coordinate.
- Section 6.4 (p. 15) treats indices 5,6,31,32,49, of type [1,1,4,4,4,8,8], each with two Selmer elements. It displays index 5 and its first element, the genus-one quotient 45u^4-v^4=5y_3^2, and Jacobian Y^2=X^3+4500X with group {O,(0,0)}. The resulting larger triple is nonprimitive. The other Selmer element and indices are asserted to be treated similarly; their complete individual computational outputs are not printed or independently inspected here. The import rests on the published Theorem 1.1, not a claimed independent verification of those omitted computations.

Theorem 1.1 is stated without GRH or another conditional hypothesis. The inspected application sections have no conditional branch; they use MAGMA for local solubility, Selmer calculations, and Mordell–Weil information. No independent rerun, certification of the full implementation, or reproof of Edwards is claimed. These computational qualifications accompany every later citation.

Application to the local positive placements, their base-one cases, and L002's exponent-divisor extensions is deliberately left to the approved subsequent research step. This source review does not change the assembled argument or DAG.

## Mathlib

Coverage of the full classification and supporting parametrization/descent results: **not checked**. No matching theorem, supporting declaration, or absence claim is asserted.
