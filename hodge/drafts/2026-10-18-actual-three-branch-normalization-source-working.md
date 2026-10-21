# Actual three-branch normalization length — source-review record

2026-10-18. Literature-only step 372; no local length formula is proved.
The target remains the supplied actual-image question, including nonlinear
normal jets. Existing notebook changes and unfinished mathematical work
are preserved. No lemma, mathematical script, DAG or proof overview is edited.

## Sources inspected so far

- Wen-Wei Li, *Yanqi Lake Lectures on Algebra, Part 3*, version
  2026-07-05, Lemma 5.2.3, printed p. 53 (PDF p. 58),
  <https://www.wwli.asia/downloads/YAlg3.pdf#page=58>.
  The complete statement and proof were read: a filtered-module map has
  surjective underlying map if its source is complete, its target is
  Hausdorff and exhaustive, and its associated graded map is surjective.
  The proof makes successive corrections of increasing filtration order,
  takes their convergent sum in the source, and uses separatedness in
  the target. This supplies a known lifting tool, not its applicability
  to our branch restriction map.
- Stacks Project, Lemma 10.97.1 (00MA), statement and complete proof:
  <https://stacks.math.columbia.edu/tag/00MA>. Noetherian completion
  preserves exact sequences of finite modules and agrees with tensoring
  by the completed ring. The proof uses Artin--Rees to compare induced
  and adic filtrations before taking inverse limits.
- Stacks Project, Lemma 10.97.8 (07N9), statement and complete proof:
  <https://stacks.math.columbia.edu/tag/07N9>. Completion of a finite
  algebra over a local base is the product of its local completions
  above the closed point; the proof decomposes the Artinian quotients
  and takes their inverse limit.
- Stacks Project, Lemma 10.97.3 (00MC), statement and complete proof:
  <https://stacks.math.columbia.edu/tag/00MC>. Completion of a
  Noetherian local ring is faithfully flat. This is supporting descent
  coverage, not an assertion that normalization commutes with completion.
- Stacks Project, Section 12.19 (0120), Definition 12.19.3 and Lemmas
  12.19.12--13, statements and proofs:
  <https://stacks.math.columbia.edu/tag/0120>. Induced/quotient
  filtrations are essential; arbitrary filtered maps cannot be treated
  as strict. The finite-filtration statements alone are not infinite
  complete-filtration lifting theorems.

The Serre *Local Algebra* II.A Proposition 6 lead appeared in search,
but its PDF could not be opened; a shell fetch failed DNS resolution.
It is not an inspected input. Li's author-hosted statement and full
proof supply the needed accessible substitute, so this is not an
essential source blocker. The previously parked all-orders source was
not retried.

## Local comparison checked

Read the required portions of L118/L120/L121 and L122's entire
restriction-image argument, including the all-degree interpolation,
finite normalization and length computation. Reuse the completed
Leahy--Vitulli/Greuel--Pfister comparison in
`drafts/literature/2026-10-17-opposite-image-normalization-quotient.md`.
ATTEMPTS/070--072 retain their respective minimal-gluing, order-zero
and full-range first-derivative stops. No duplicate nonlinear transfer
assessment was found in the narrowly searched recent local source notes.

The completed comparison and exact covered continuation are recorded in
`drafts/literature/2026-10-18-actual-three-branch-normalization-length.md`.
It also records Stacks 0C0S's regular complete coefficient-field
statement and proof. The review distinguishes branch order from the
image's intrinsic maximal-ideal filtration and leaves the full nonlinear
specialization to a separate research turn. No simultaneous linearization
or actual length four is established here.
