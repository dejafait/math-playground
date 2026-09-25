# Kraus's divisibility restriction

Audited on 2026-09-25 through published numbered restatements. The original reference is Alain Kraus, *Sur l'équation a^3+b^3=c^p*, Experimental Mathematics **7** (1998), no. 1, 1–13, DOI [10.1080/10586458.1998.10504355](https://doi.org/10.1080/10586458.1998.10504355). The publisher abstract was accessible, but the original full text was not retrieved from the publisher, Project Euclid, or archive endpoints. The original theorem numbering and proof have therefore **not** been audited here.

The precise input used is the prime-p >= 17 portion of Michael A. Bennett, Imin Chen, Sander R. Dahmen, and Soroosh Yazdani, *Generalized Fermat equations: A miscellany*, International Journal of Number Theory **11** (2015), no. 1, 1–28, **Proposition 7 (Kraus)** and its following qualification, printed p. 6 ([author-hosted published PDF, page 6](https://personal.math.ubc.ca/~bennett/BeChDaYa-IJNT-2015.pdf#page=6); [DOI](https://doi.org/10.1142/S179304211530001X)). For nonzero coprime integers a,b,c satisfying a^3+b^3=c^p, with p >= 17 prime, this gives

\[
c\equiv3\pmod6,\qquad v_2(ab)=1.
\]

Here v_2 is the exponent of 2 in the absolute value. The symmetric formulation avoids assigning the even coordinate before interchanging a and b. This portion is also stated as **Theorem 1 (Kraus, 1998)** in Freitas, *On the Fermat-type equation x^3+y^3=z^p*, printed p. 296 ([publisher PDF, page 2](https://ems.press/content/serial-article-files/43415#page=2); [arXiv version, page 1](https://arxiv.org/pdf/1601.06361#page=1)). Freitas writes the parity conditions with a chosen even coordinate. Neither restatement restricts p modulo 3 for this divisibility conclusion.

The 1998 abstract retains the Taniyama–Weil hypothesis. The modern statements used here are unconditional; the named full-modularity theorem over Q, **Breuil–Conrad–Diamond–Taylor, Theorem A**, is already recorded in [the standard inputs](02-standard-results.md). This source audit does not independently reconstruct Kraus's modular argument.

Only the stated prime range is imported. The smaller-exponent extensions in Proposition 7 use further inputs, and the finite exponent exclusions mentioned in Freitas's Theorem 1 are separate assertions. Neither is imported in this step. A necessary divisibility condition does not itself exclude the whole repeated-cube family.

## Mathlib

Coverage of the full divisibility theorem: **not checked**. Supporting declarations for valuations and integer congruences: **not checked**. Proposition 7 on the specified prime range is a full external mathematical match for the input above; Freitas's Theorem 1 corroborates it. Full modularity supports its unconditional setting and is not itself a matching divisibility theorem. None of these citations is a claim of a Mathlib declaration or formal verification.
