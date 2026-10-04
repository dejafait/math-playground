# Dahmen–Siksek's fifth-power/nineteenth-power classification

Imported on 2026-10-04 using the unchanged assessment completed on 2026-10-03. Sander R. Dahmen and Samir Siksek, *Perfect powers expressible as sums of two fifth or seventh powers*, **Acta Arithmetica 164(1) (2014), 65–100**, **Theorem 1, p. 67**, DOI [10.4064/aa164-1-5](https://doi.org/10.4064/aa164-1-5); [publisher PDF](https://www.impan.pl/shop/publication/transaction/download/product/83637), [arXiv v2 theorem statement](https://arxiv.org/html/1309.4030v2#Thmtheorem1).

## Exact imported clause and source scope

The ell=19 clause of Theorem 1 classifies coprime signed integer solutions of

\[
X^5+Y^5=Z^{19}
\]

as exactly

\[
(1,-1,0),\quad(-1,1,0),\quad(1,0,1),\quad(-1,0,-1),
\quad(0,1,1),\quad(0,-1,-1).
\]

Every triple has a zero coordinate. Hence the theorem excludes all nonzero pairwise coprime signed integer solutions, with unrestricted bases and with coordinates of absolute value one permitted. This clause is unconditional and imposes no restriction that 5 divide, or not divide, Z. Pairwise coprimality suffices for the source's coprimality hypothesis, whether expressed by the common gcd or by pairwise gcds.

The prior assessment inspected the published statement and ell=19 proof components in Section 3, pp. 69–78, and cross-checked the statement in arXiv v2, revised 26 January 2014. Journal page numbers are used here. Lemma 3.1 and Proposition 3.2, pp. 69–70, treat 5 not dividing Z through C_19: Y^2=20X^19+5. Section 3.1, pp. 70–73, completes its rational-point classification; Table 1 and the rank conclusion give rank one without GRH or an assumption on the finiteness of Sha. Proposition 3.3 and Section 3.2, pp. 73–76, cover 5 dividing Z by the modular argument, which includes exponent 19.

Section 3.3, pp. 76–78, discusses an alternative curve D_19. Its conditional rank bound in Table 2 and incomplete alternative argument are separate from the proof of the imported clause. They are not used. Theorem 3's GRH hypothesis concerns different fifth-power exponents and is not a hypothesis of Theorem 1 at ell=19.

The accessible publisher text and arXiv statement supplied the prior source evidence; earlier author-hosted HTTP 403 and shell DNS failures do not leave an essential source for this import unread. The published genus-nine, rank, and modular computations, including external MAGMA files and their underlying algorithms, are imported as part of the named theorem. They were not independently inspected or rerun in this step. Only the ell=19 clause is imported here.

## Mathlib

Coverage of the full signed classification: **not checked**. Supporting genus-nine, Chabauty, rank, modular, power, sign, and coprimality results were not checked in Mathlib. Theorem 1 at ell=19 matches the external classification; its numbered proof components support that theorem. The paper citations do not assert matching Mathlib declarations or formal verification.
