# Equality normalization degree — source-review working notes

Literature-only step 257, 2026-10-13. No degree proof is being made.
Target: the saved L098 normalization/generic-degree question, retaining Z.

The old L065 assessment supplies normalization and stable Mukai-form
coverage. Its global unramifiedness/finite-etale Euler argument is outside
the current hypotheses. L098 supplies unramifiedness only on U; all Z
maps to m_0. Audited L095 evaluates the actual raw form on this family.

Primary statements inspected so far:

- Stacks 0GS9: connected, dominating unramified source over an integral
  geometrically unibranch target is etale. Use only after removing the
  finite exceptional target set; no whole-target application is approved.
- Stacks 0BMB, 0H2W: purity/extension have regular-target hypotheses.
  They can screen covers of the smooth K3 punctured at finitely many
  points, not remove ramification over a possibly singular normalization.
- Stacks 03SF: connected finite etale covers admit a connected Galois
  refinement; automorphism group size equals degree for a Galois cover.
- Stacks 0EY6: unique finite depth-at-least-two extension of an etale
  cover across a depth-at-least-two complement. Its proof identifies
  the reflexive algebra with the pushforward from the open set.
- Huybrechts, author-hosted 449-page K3 draft, chapter 15 section 1.2,
  Corollary 1.8 and following table, printed p. 310: nonidentity finite
  symplectic automorphisms have orders 2 through 8, with Picard lower
  bounds 9,13,15,17,17,19,19. The invariant-cohomology/Lefschetz
  proof passage was inspected. Chapter 7 Corollary 1.4, pp. 127--128,
  gives simple connectedness. These are known results, not local advances.
- Xiao, Ann. Inst. Fourier 46 (1996), 73--88, section 1, p. 74:
  finite symplectic quotients have rational double points and are
  unramified off them. This is obstruction screening, not a counterexample
  family F or a claim that every quotient matches L098's one image value.

Local retained rank-four scope is in foundations/05-cubic-rm-family.md
and L025's hypotheses, passed through L044/L071 to L098. It excludes
arbitrary specializations with larger Picard rank from any future
rank-based application.

Completed source comparison: see
[the canonical assessment](literature/2026-10-13-equality-normalization-generic-degree.md).
The additional algebraic simple-connectedness source is Huybrechts
Remark 1.2.3, p. 11; cover extension uses Stacks 0H2W/0EY7 and 0EY6.
The coarse family formula is reused on U only. SPECIALIZE approves
an application next turn, with every actual covering and form bridge
still to be proved. No source blocker, new lemma or degree verdict.
