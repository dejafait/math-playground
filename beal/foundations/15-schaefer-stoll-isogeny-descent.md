# Schaefer–Stoll: general isogeny-descent source scope

## Hypotheses

K is a number field, p an odd prime, and theta:E -> E' a K-defined isogeny of elliptic curves whose kernel has exponent p. For the cyclic-isogeny construction in Section 9, its degree is p. Write theta' for the dual isogeny. A finite set S of places contains the places above p and every finite place v where either curve's Tamagawa number is divisible by p.

## Conclusion

The theta-Selmer group consists exactly of the classes in H^1(K,E[theta];S) whose restrictions at every place in S lie in the local connecting-map images. Here the semicolon S means classes unramified outside S. This is a Selmer description, not an assertion that every such class comes from a global point.

For a Galois-invariant spanning subset X of E'[theta'] minus the origin, let D be its finite étale algebra. Section 5 uses functions f_P with divisor p(P)-p(O), compatibly chosen under Galois action. Evaluation on good degree-zero divisors realizes the connecting map in D^*/D^{*p}. The method requires injectivity globally and locally and identification of the cohomological image. Section 9 supplies the cyclic-isogeny case; if the relevant étale algebra splits, one may use a factor. These statements do not assert splitting for a particular curve or field.

The finite arithmetic data are S-units modulo pth powers (a subgroup of index prime to p suffices) and S-class-group p-torsion, via the exact sequence in Section 5. Their theoretical finiteness does not certify any computed class group, unit group, Selmer dimension, rank or rational-point list.

## Proof

Citation only: Edward F. Schaefer and Michael Stoll, *How to do a p-descent on an elliptic curve*, Transactions of the American Mathematical Society **356** (2004), no. 3, 1209–1231, [DOI](https://doi.org/10.1090/S0002-9947-03-03366-X). The inspected primary text is the [author-hosted long manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf), dated **June 13, 2001**, 34 PDF pages. All following locators refer to this manuscript, not assumed identical numbering in the published article.

Proposition 4.6, printed p. 7, gives the finite-place Selmer description. Its proof invokes Lemmas 4.1 and 4.5; the odd-degree infinite-place case and Lemmas 4.2–4.5's unramified-image argument on printed pp. 6–7 were inspected. Section 5, printed pp. 8–10, gives the good-divisor evaluation, its two injectivity/image requirements, the unit/class exact sequence, formula (5.1), and the separate treatment of places above p. Its identification of function evaluation with the connecting map cites Schaefer [25], Theorem 2.3; that reference was not independently reread, and this source's stated identification is imported, not reverified. Section 9, printed pp. 21–24, gives the cyclic-isogeny étale-algebra construction; its initial construction and Lemma 9.1 with the proof on pp. 22–23 were inspected. No full-p descent, CM bound, numerical example, or claim about an actual Beal solution is imported.

Important qualifications: a quotient of rational points injects into the Selmer group; equality requires the relevant Shafarevich–Tate obstruction to vanish. Neither that vanishing nor finiteness of the whole Shafarevich–Tate group is an assumption for the connecting map or its necessary Selmer condition. Section 9's formula (9.2) is explicitly stated there for K=Q and is not transferred to a degree-12 field. A single isogeny Selmer group does not determine the full p-Selmer group or rank. Computing class/unit data under GRH would make that computation conditional, although the cited general theorems have no GRH premise.

## Mathlib

Full matching theorem and supporting isogeny, Galois-cohomology, divisor-evaluation and S-unit declarations: **not checked**. Unknown coverage is not evidence of absence.
