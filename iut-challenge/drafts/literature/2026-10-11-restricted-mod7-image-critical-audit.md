# Restricted mod-7 image — critical-audit source coverage

TARGET: Critically audit L047's restricted mod-7 image containment for the same L046 curve over L045's F.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared canonical L047, L045/L046 hypotheses and conclusions, ready restriction assessment, histories 150–152 and ATTEMPTS/022,025,026,027; the separate audit remains pending and no distinct audit was found in these scoped records. Reused prior primary inspection without fresh external searches.
SOURCE_EVIDENCE: Reused inspected Milne Fields and Galois Theory v5.10 (September 2022), Theorem 3.17(b),(d) and Propositions 3.19,3.21, printed pp.39–42, and Conrad Simplicity of PSLn(F), author-hosted 9-page version retrieved 2026-10-11, Theorem 3.3 and complete proof p.4, as recorded in 2026-10-11-mod7-image-after-torsion-adjunction.md; full-coordinate kernel coverage is retained through audited L045.
COMPARISON: The same finite-Galois restriction and elementary-generation inputs cover every general theorem needed for this separate audit; only their written specialization and elementary finite-quotient checks require critical verification.
GAP: The critical audit itself remains undone: check actual image equality, normality/index divisibility, both elementary families and retained same-curve conclusions; no stronger image or IUT conclusion is covered.
REASON: This comparison supplies separate audit-scope approval using adequate unchanged primary coverage; no essential unread case, changed hypothesis or new source lead justifies repeated browsing.
SCOPE: Exactly TARGET for the unchanged L047 argument, the same L046 E_0 and L045 F inside the fixed Q-bar; no full GL_2 image over F, disjointness or sufficient initial-data hypothesis.

## Relevance and reuse

The main gap remains original finite B>=A in IUT III Corollary 3.12,
step (xi-f). The intermediate target is the exact critical audit above.
A successful audit would make the restricted large-image prerequisite
reusable alongside full rational 30-torsion and embedded H,N completions
in a later, separately assessed initial-data test. It cannot itself
validate original initial data or numerical comparison.

Read the ready assessment
`drafts/literature/2026-10-11-mod7-image-after-torsion-adjunction.md`,
canonical L047 in full, and L045/L046's hypotheses, conclusions and
imported-input passages. The ready assessment records primary theorem
statements and essential proof cases actually inspected previously;
this turn reuses that evidence rather than claiming fresh retrieval.
The audit of L045 and L046 is recorded canonically and in the relevant
histories. No new theorem, order calculation or correctness verdict is
established in this literature-only comparison.

## Exact source-to-obligation comparison

- Milne, [Fields and Galois Theory v5.10](https://www.jmilne.org/math/CourseNotes/FT.pdf),
  Theorem 3.17(b),(d), printed pp.39–40, covers index/degree and
  normality/quotient correspondence for a finite Galois extension.
  Proposition 3.19, pp.40–41, covers restriction from a Galois
  compositum to the intersection subgroup. Its recorded proof checks
  injectivity and surjectivity using the image's fixed field.
  Proposition 3.21, pp.41–42, covers intersections and composita of
  Galois extensions, with normality and separability proof cases read.
  L047 uses finite coordinate fields in one Q-bar and L045 supplies
  Galoisness of F/Q. These are within the inspected scope. The later
  audit must establish K's coordinate-kernel identification and the
  actual G_F image, rather than accept a subgroup inclusion as equality.
  Standard extension of embeddings into an algebraic closure supplies
  the absolute-to-finite restriction surjectivity; no disjointness
  theorem or new infinite-Galois result is needed.
- L045's audited full-coordinate representation input, precisely cited
  there to Sutherland MIT 18.786 Lecture 20 (2024-05-01), section 20.1
  pp.1–2, and Yvon arXiv:2407.14370v1, Introduction pp.1–2, applies
  to the same characteristic-zero elliptic curve and both coordinates
  of all geometric torsion. L046 supplies the global image over Q.
  The audit must check that L045 is applied to that reselected curve,
  not a second independent approximation. Its retained completions
  are imported conclusions, not new local computations.
- Conrad, [Simplicity of PSLn(F)](https://kconrad.math.uconn.edu/blurbs/grouptheory/PSLnsimple.pdf),
  Theorem 3.3, p.4 of the inspected 9-page version, covers generation
  of SL_2 over any field by upper/lower elementary unipotents. Its
  complete proof handles both off-diagonal cases and diagonal matrices
  and displays the subgroup-exchanging conjugation. F_7 needs no
  exceptional-field hypothesis. This author source already covers
  generation; reproof of its factorization, simplicity or perfectness
  is unnecessary. The audit must separately verify the written orders
  of both elementary families, including t=0, and their images in the
  normal finite quotient using Lagrange's theorem. These elementary
  checks specialize the known mechanism and do not require a new
  subgroup classification.

This comparison approves SPECIALIZE, with a later REPRODUCTION audit,
not a fresh theorem import resolving the challenge. It neither derives
the containment nor repeats the completed construction. No novelty
claim follows from the scoped duplicate check. Full matching Mathlib
coverage and supporting theorem names remain unchecked, not absent.

## Continuation and abandonment test

Essential inputs are canonical L047 with audited L045 and L046 for
the same E_0 and embedded Q-bar, retaining L044/L042 and Omega,H,N
through those inputs. Audit full-coordinate K, D=FK, restriction onto
Gal(K/(K intersect F)), Galoisness of the intersection, normality and
index divisibility. Verify the exact elementary orders and generation
in the fixed basis and that no reselection occurs. Pass only if every
obligation holds; a failed obligation requires naming its precise
missing hypothesis or error before accepting L047. Do not infer
linear disjointness or full GL_2 image over F from prime-to-7 degree.

Geometric-parameter/full initial data, effective coefficients,
native/input/action, marked pilot transport, essentiality and original
finite B>=A remain unresolved. ATTEMPTS/022,025,026 exclude different
exact fields/roles; ATTEMPTS/027 excludes the exact Tate curve rather
than the changed-curve finite-torsion construction. Their evidence is
preserved and no stopped route is reopened. No cross-notebook input,
lemma/script write, DAG edit or argument change is involved.
