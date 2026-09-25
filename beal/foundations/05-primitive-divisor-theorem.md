# Primitive divisors: the imported theorem and its range

Audited on 2026-09-25. Yu. Bilu, G. Hanrot, and P. M. Voutier, *Existence of primitive divisors of Lucas and Lehmer numbers*, with an appendix by M. Mignotte, Journal für die reine und angewandte Mathematik **539** (2001), 75–122, [DOI](https://doi.org/10.1515/crll.2001.080). The [author's publication list](https://perso.ens-lyon.fr/guillaume.hanrot/) confirms the bibliographic identification. Statements were read in the [author-uploaded manuscript](https://www.researchgate.net/profile/Paul_Voutier/publication/2397582_Existence_of_Primitive_Divisors_of_Lucas_and_Lehmer_Numbers/links/559999c308ae99aa62cc6983/Existence-of-Primitive-Divisors-of-Lucas-and-Lehmer-Numbers.pdf); the DOI endpoint and author-page download failed, and HAL returned an access-denied page.

A Lucas pair consists of algebraic integers alpha,beta with nonzero coprime integer sum and product, and alpha/beta not a root of unity. Put U_n=(alpha^n-beta^n)/(alpha-beta). A primitive divisor is a prime dividing U_n but not (alpha-beta)^2 U_1 ... U_(n-1). These definitions are on manuscript pp. 1–2.

**Theorem 1.4**, manuscript p. 4, guarantees primitive divisors for every index n>30. **Theorem C and Table 1**, manuscript p. 3, classify the smaller defective Lucas pairs; there are none at n=17,19,23,29. Together these give existence for every prime index at least 17. The small-index conclusion is a separate table input, not an extension of Theorem 1.4's inequality. No statement for all indices at most 30 is imported.

These cited statements impose no valuation-one or valuation-not-divisible-by-index condition on the prime they supply. L008 checks their applicability and tests that distinction in the relevant coefficient family.

## Mathlib

Coverage of the full primitive-divisor theorem: **not checked**. Supporting declarations for Lucas sequences and multiplicative orders: **not checked**. The named citations above are not claims of matching library declarations.
