# Hermite banded Gram: source-review working record

Literature-only step; the saved target is unchanged. No coefficient
matching, feasibility calculation, new lemma or mathematical script has
been performed. Existing unfinished work is preserved.

Inspected so far:

- Local actual-Hermite mixed-term assessment, L564/L565 hypotheses and
  L565 conclusion, its ready finite-audit assessment, diagonal-CD stop,
  and last finite-audit history. The old stop concerns its specified cone.
- Laurent, *Sums of squares, moment matrices and optimization over
  polynomials*, author PDF dated February 5, 2008, Lemmas 3.5 and 3.8,
  pp. 23–25, including root-factorization and Gram-factorization proofs.
  https://homepages.cwi.nl/~monique/files/moment-ima.pdf
  The CWI repository's 13237C.pdf resolves to this same dated version;
  do not label its theorem numbering as an inspected November 2009 text.
- Gatermann–Parrilo, arXiv:math/0211450v1 (28 November 2002),
  Lemma 2.1 and its proof, pp. 4–5; Definition 3.1/Theorem 3.3 and
  full averaging proof, pp. 7–9, subsequently inspected.
  https://arxiv.org/pdf/math/0211450v1
- Vandenberghe–Andersen, *Chordal Graphs and Semidefinite Optimization*,
  DOI 10.1561/2400000006, copyright 2015, journal volume dated 2014,
  Theorem 9.2 and proof, pp. 340–341; Theorem 10.1 and proof,
  pp. 356–357; section 9.1, pp. 337–338, including zero-pivot case.
  https://www.seas.ucla.edu/~vandenbe/publications/chordalsdp.pdf

Load-bearing scope distinction: Theorem 9.2 concerns a zero-filled
sparse matrix being PSD and uses a sum of embedded PSD clique matrices.
Theorem 10.1 characterizes existence of a PSD completion of partial
entries. They must not be interchanged. No restricted Hermite
feasibility result is supplied by either theorem. Necessary principal
block tests remain only necessary for the proposed certificate.

Completed: the canonical assessment
`literature/2026-10-31-hermite-banded-gram-diagnostic.md` records exact
queries, theorem hypotheses/proof cases, version qualifications and
EXPLORE coverage for the unchanged next action. This working record
preserves the intermediate source state only; the assessment governs
continuation. No mathematical attempt or feasibility claim this turn.
