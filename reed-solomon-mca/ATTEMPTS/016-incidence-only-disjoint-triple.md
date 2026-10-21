# Incidence-only disjoint-triple reduction fails

Date: 2026-10-05.

WHY IT FAILS: [L023](../lemmas/L023-balanced-support-matching-counterexample.md)
gives the exact sixteen-edge, sixteen-vertex, four-uniform, degree-four
requirements with matching number two, by specializing the known cyclic
difference-cover construction. Balanced incidence therefore cannot force
three disjoint supports. This stops that reduction alone: the example is
not known to satisfy affine-moment compatibility, and L022 does not cover
arbitrary disjoint triples even if a triple is obtained by another mechanism.
Additional RS constraints may exclude this abstract family; that is a
separate, presently uncovered target. The global 11/q–16/q interval stays
unchanged.
