# Cyclotomic height criterion

## Height conventions

Use the classical Selmer dual X, generator gamma, and T = gamma - 1 from
[the cyclotomic conventions](03-cyclotomic-control.md). Let E/Q have good
ordinary reduction at an odd prime p. Write r = rank E(Q) and
V = E(Q) tensor_Z Q_p. The canonical cyclotomic p-adic height with the
ordinary unit-root choice gives a Q_p-bilinear pairing on V.

Write R_p(E) for its determinant on a basis of the free part of E(Q), with
the empty determinant equal to 1 when r = 0. Its nonvanishing is equivalent
to nondegeneracy on V. A change of basis multiplies the determinant by a
nonzero square. Normalizing the height by log_p(kappa(gamma)), where kappa
is the cyclotomic character on Gamma, multiplies R_p by
log_p(kappa(gamma))^(-r); this scalar is nonzero. Only nonvanishing is used.
See [Stein--Wuthrich, Sections 4.1 and 4.4, printed pages 1770--1771 and 1774](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=14)
for the ordinary height and normalization. No arbitrary bilinear form is
substituted for this arithmetic height.

## Named arithmetic input and checked scope

The **Schneider--Perrin-Riou characteristic-order theorem**, in the form
needed here, states that finite Sha(E/Q)[p^infinity] and R_p(E) != 0 imply
ord_T f_X = r, provided X is finitely generated and torsion over Lambda.
Those module hypotheses hold here by the named inputs already recorded.
The assertion concerns the algebraic characteristic series.

A checked statement covering elliptic curves with or without complex
multiplication is [A. Ray, *Remarks on Hilbert's tenth problem and the
Iwasawa theory of elliptic curves*, Theorem 3.4, Bull. Aust. Math. Soc.
107 (2023), 440--450, printed page 445](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/32000D6BB2B3EC97CAD0B6F932B84935/S000497272200082Xa.pdf/remarks-on-hilberts-tenth-problem-and-the-iwasawa-theory-of-elliptic-curves.pdf#page=6).
Specialize its number field K to Q. All four hypotheses (odd ordinary p,
finite p-primary Sha, nonzero regulator, and torsion finite generation)
are retained. Its non-CM restriction in Section 4 is later and does not
apply to Theorem 3.4. Its extra leading-coefficient formula is not needed.

Ray cites **Peter Schneider, *p-adic height pairings. II*, Invent. Math.
79 (1985), 329--374, Theorem 2', printed page 342**:
[publisher record](https://doi.org/10.1007/BF01388978).
The original full text could not be retrieved in this audit; the precise
attribution is checked through Ray's statement, not claimed as a direct
reading of Schneider's proof.

For the converse, [William Stein and Christian Wuthrich, *Algorithms for
the arithmetic of elliptic curves using Iwasawa theory*, Theorem 6.1,
Math. Comp. 82 (2013), 1757--1792, printed page 1776](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=20)
states that ord_T f_X = r is equivalent to finite p-primary Sha and
nondegenerate height. Their classical Selmer module is defined in Section
6, printed page 1775. Their standing non-CM assumption begins in Section
3, printed page 1761, so the converse imported from this checked source
is restricted to non-CM E. Only the good ordinary case is used; Jones's
multiplicative extension is outside this step.

Neither source is used to assert finite Sha or a nonzero regulator for an
arbitrary curve. The analytic p-adic BSD statement (Stein--Wuthrich,
Conjecture 5.1) and any comparison with complex analytic order are separate
from the characteristic-order theorem. No main conjecture is assumed here.

## Mathlib

Full coverage of the cyclotomic height, the characteristic-order theorem,
and its application to augmentation semisimplicity: **not checked**.
Supporting regulator and finite-module results: **not checked**. The
published theorem names and links above are mathematical references,
not Mathlib matches or assertions of library absence.
