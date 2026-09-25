# Attempt 009 — Forgetting a sufficiently negative ideal presentation

Date: 2026-09-25. Outcome: stopped for the transverse NS-fixed RM direction.

The tested vector bundle is the second syzygy of I_C in two presentations by sufficiently negative powers of an NS-fixed ample line bundle. Its c_2 differs from [C] by divisor products and acts as U. The new idea was to forget the presentation maps, potentially allowing the bundle to lift without its obstructed support. The full proof is [L012](../lemmas/L012-second-syzygy-retains-cubic-obstruction.md).

**WHY IT FAILS.** Serre duality turns the two map-lifting obstruction groups into third cohomology groups killed by the positive-twist hypotheses and H^3(X,O_X)=0. Every bundle lift therefore restores both presentation inclusions and produces a flat coherent lift of I_C. The determinant, H^1(X,O_X)=0, and Hartogs extension across codimension two reconstruct its inclusion into O_XA with flat quotient. Conversely an embedded lift restores the chosen presentations. The bundle's Atiyah obstruction kernel is exactly the three-dimensional family tangent, versus four RM dimensions required. This stops the specified sufficiently negative syzygies; it does not obstruct all bundles, other sheaf representatives, or the Hodge class.
