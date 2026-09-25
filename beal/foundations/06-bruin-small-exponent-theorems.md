# Bruin's fourth- and fifth-power theorems

Audited on 2026-09-25. Nils Bruin, *On Powers as Sums of Two Cubes*, in Wieb Bosma (ed.), *Algorithmic Number Theory*, ANTS-IV, Lecture Notes in Computer Science **1838**, Springer, 2000, pp. 169–184, DOI [10.1007/10722028_9](https://doi.org/10.1007/10722028_9).

## Exact statements and source scope

**Theorems 1 and 2, printed p. 170**, assert, respectively for n=4 and n=5, that integers X,Y,Z satisfying X^3+Y^3=Z^n and XYZ nonzero have gcd(X,Y,Z)>1. Thus there are no primitive nonzero integer solutions at either exponent. The equations and gcd convention are introduced on printed p. 169; trivial solutions there mean XYZ=0. Signed coordinates are allowed, and neither theorem requires the absolute values of nonzero coordinates to exceed one.

Both numbered statements and the definitions were read in the [publisher's two-page preview, pp. 169–170](https://page-one.springer.com/pdf/preview/10.1007/10722028_9#page=2). No modularity or abc hypothesis appears in either statement. The discussion of these hypotheses elsewhere in the introduction is not a condition on Theorems 1 or 2. The abstract describes reductions also at 7,11,13 but claims completion only at 4,5; no exclusion at the other exponents is imported from it.

The [author's publication list](https://www.cecm.sfu.ca/~nbruin/publications.shtml) identifies the same paper and links a [PostScript manuscript](https://www.cecm.sfu.ca/~nbruin/eq33p.ps.gz) and computation files. The browser could not parse the compressed PostScript. The full proof and associated computations were not independently rerun in this step: these published theorems are precise cited inputs, not newly proved or formally verified results. The two-page publisher preview supplies the exact statements used here.

## Mathlib

Coverage of the full signed nonexistence statements: **not checked**. Supporting power, sign, and gcd declarations were not checked. The numbered theorems above match the external mathematical inputs; neither the publisher links nor the author's computation files are Mathlib matches.
