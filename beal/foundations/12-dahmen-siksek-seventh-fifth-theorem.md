# Dahmen–Siksek's seventh-power/fifth-power classification

Imported on 2026-10-04 using the unchanged prior assessment. Sander R. Dahmen and Samir Siksek, *Perfect powers expressible as sums of two fifth or seventh powers*, **Acta Arithmetica 164(1) (2014), 65–100**, **Theorem 2, p. 67**, DOI [10.4064/aa164-1-5](https://doi.org/10.4064/aa164-1-5); [publisher PDF](https://www.impan.pl/shop/publication/transaction/download/product/83637), [arXiv v2 theorem statement](https://arxiv.org/html/1309.4030v2#Thmtheorem2).

## Exact imported statement and source scope

Theorem 2 classifies coprime signed integer solutions of

\[
X^7+Y^7=Z^5
\]

as exactly

\[
(1,-1,0),\quad(-1,1,0),\quad(1,0,1),\quad(-1,0,-1),
\quad(0,1,1),\quad(0,-1,-1).
\]

Every triple has a zero coordinate. Hence there are no nonzero pairwise coprime signed integer solutions, with unrestricted bases and with coordinates of absolute value one permitted. Pairwise coprimality suffices for the source's coprimality hypothesis, whether expressed using the common gcd or pairwise gcds. The theorem is unconditional and covers both 7 dividing Z and 7 not dividing Z.

The prior assessment read the published statement and selected supporting passages in Section 4, pp. 78–91, and cross-checked the statement in arXiv v2, revised 26 January 2014. Journal page numbers are used here. The read scope includes Proposition 4.1 and its modular conclusion, the branch-to-curve reductions in Section 4.3, Lemma 4.12, Remark 4.14, Lemma 4.15, and Proposition 4.16 with its proof and closing assembly. This is a citation-based import, not an independent verification of all intermediate proofs or external algorithms.

For 7 not dividing Z, the source uses the restricted set C_{5,3}(K)' and Lemma 4.15; it does not require or assert a complete classification of C_{5,3}(K). For 7 dividing Z, it uses D_{5,2}(K) and Lemma 4.12, where K=Q(zeta_7+zeta_7^{-1}). Proposition 4.16, pp. 90–91, completes both branches. The rank tables used for these cases are unconditional. The GRH qualification in Theorem 3 concerns different exponents and is not a premise of Theorem 2.

The accessible publisher text and arXiv statement supplied the prior source evidence. Earlier failures to access an author-hosted PDF or download through the shell do not leave this named theorem unread. The published modular, rank, and rational-point computations are imported as part of the theorem. The external MAGMA files Modular77l.m and Chabauty77l.m and their underlying algorithms were not independently inspected or rerun. No other signature from the paper is imported here.

## Mathlib

Coverage of the full signed classification: **not checked**. Supporting modular, rank, rational-point, sign, power, and coprimality declarations were not checked. Theorem 2 matches the external classification; the named Section 4 components support that theorem. The direct primary-source links are mathematical citations, not matching Mathlib declarations or claims of formal verification.
