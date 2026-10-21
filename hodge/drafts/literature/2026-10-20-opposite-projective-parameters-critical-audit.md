# Opposite projective parameters — independent audit scope

TARGET: Critically audit L137's opposite determinant pullbacks, fixed projective choices and normalization-degree formula.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Separate approval review completed: read full L137, its three saved source assessments, history/425 and ATTEMPTS/070,073,078; reuse the determinant/reduced-ring discovery evidence. Targeted query for finite morphism intersection degree, Hilbert polynomial and support dimension located Stacks 33.45; inspect its relevant statements and proof cases without a new opposite-family calculation.
SOURCE_EVIDENCE: Reused Huybrechts–Lehn (1997), 8.1.5/8.1.9–8.1.12, pp. 180–185, and Section 8.3/8.3.1(ii), pp. 195–197, https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf ; reused Hoa arXiv:math/0608118v1, pp. 4–5 and Theorems 0.2/4.1, https://arxiv.org/pdf/math/0608118v1 . Newly read Stacks 30.17.2 (0B5V), 37.44.1 (02LS), and 33.45.1–2, 33.45.3, 33.45.7, 33.45.10–11 (0BEL), statements and relevant proofs, https://stacks.math.columbia.edu/tag/0B5V , https://stacks.math.columbia.edu/tag/02LS , https://stacks.math.columbia.edu/tag/0BEL , accessed 2026-10-20.
COMPARISON: Reused whole-semistable descent, fixed-determinant positivity and K-theoretic GRR cover the general determinant framework; the inspected Stacks inputs cover finite pullback, proper/quasi-finite finiteness and degree/Hilbert leading terms without normality or CM. Family-specific specialization and correctness remain for the audit; no effective exponent or defect estimate is imported.
GAP: Source coverage is ready for the exact saved audit. Independently check the full opposite specialization, F-independent choice order, original-image compactification bridge and leading-coefficient comparison; this literature review reaches no independent critical verdict on L137.
REASON: The separately required approval review is complete and retains SPECIALIZE for this unchanged target. Invoke one research proof audit next; do not repeat literature work absent a concrete newly missing input.
LITERATURE_REASON: The supervisor explicitly requires a separate literature-only approval of the newly written audit scope; reuse ready determinant coverage and check precise supporting statements for the image/leading-coefficient bridge, without repeating its mathematical derivation.
SCOPE: Exactly L137 under L071/L118/L120's hypothetical rank-two locally free Omega-polystable F, integral c_1=0, ch_2=-14e_1-21e_2-tau_D, opposite base B=S_1 and fibre Y=S_2, L118's own common H, original reduced image and finite birational K3 normalization. No new lemma, numerical threshold or defect inequality is preapproved by this audit scope.

Reuse `2026-10-20-opposite-projective-polarization-specialization.md`,
`2026-10-20-opposite-image-projective-degree-defect.md` and
`2026-10-15-equality-determinant-line-positivity.md`. The last two
contain the actual inspected-source evidence; the present assessment
does not turn unread source leads into inspected theorems. General
results should be cited rather than reproved. L107 is only a comparison,
not the opposite pullback input.

The main gap is universal primitive Hodge realization. The intermediate
audit target tests whether the new parameter input is sound. Its plausible
downstream use is a separately scoped application of Hoa's bounds to the
original image, followed by a quantitative usefulness test. F existence,
collision sizes/counts, that comparison and transport remain unresolved.

Continue if all retained hypotheses justify the actual integral lines,
projective choices and degree comparison. Repair a real error if found;
otherwise preserve the conditional statement without inflating the verdict
into new mathematics. A failed degree/embedding bridge must be documented
and the dependent defect mechanism parked until repaired. In particular:

- Check the opposite fibre's numerical class, both Euler coefficients,
  relative Todd factor, full transpose convention and rank-two character
  identities. Do not substitute the forward computation.
- Check whole-semistable descent and fixed-determinant projectivity before
  selecting ell,k,N. Distinguish fixed moduli dependence from an unknown
  image Hilbert polynomial and from an explicit numerical bound.
- Retain the actual reduced image in the stable open when viewing it in
  the projective moduli space. Neither nu nor f is assumed embedded.
- Verify the finite degree-one Hilbert-leading-term argument, without
  cohomology vanishing or discarding Q's lower coefficients. The actual
  full q(DH,DH), rather than a positive-plane eigenvalue replacement,
  controls the square for an arbitrary permitted integral H.
- Preserve ATTEMPTS/070,073,078 and parked order-five evidence. Check no
  normalization-defect bound or contradiction has been silently claimed.

Mathlib full matching coverage remains not checked; no absence is asserted.
No cross-notebook input is used. No new source research is needed unless
the audit identifies a concrete essential missing hypothesis or unread
proof case, in which event record LITERATURE_REASON and keep that work
literature-only.

## Separate source-approval review, 2026-10-20

The preceding audit checklist remains the research target, not a completed
correctness verdict. Read the complete L137 to identify its source
obligations; no determinant calculation or degree formula was rederived.
The 2026-10-15 assessment supplies the inspected book proof cases,
including stabilizer descent and the fixed-determinant ample combination.
The two 2026-10-20 assessments supply the opposite scope and Hoa's
reduced-ring comparison. Neither the book nor Hoa was newly inspected
externally in this approval review.

The additional primary check is [Stacks 33.45](https://stacks.math.columbia.edu/tag/0BEL),
accessed 2026-10-20. Lemma 33.45.1 bounds the degree of the Euler
polynomial by support dimension; its proof handles embedded associated
points and uses lower-dimensional cokernels. Lemma 33.45.2 identifies
top terms by generic lengths. Lemma 33.45.7 proves the proper-morphism
intersection projection formula using generic finiteness and lower-degree
higher-image terms. Definition 33.45.10 identifies the leading coefficient
as degree divided by dimension factorial; Lemma 33.45.11 states finite
dominant degree multiplicativity for proper varieties. None assumes a
normal or Cohen--Macaulay target. These statements supply the general
inputs for the audit's leading-term check; their family application is
not carried out here.

Also inspected [Stacks 02LS](https://stacks.math.columbia.edu/tag/02LS):
proper with finite fibres, or proper and locally quasi-finite, is equivalent
to finite. Its proof uses étale-local finite neighbourhoods and descent.
[Stacks 0B5V](https://stacks.math.columbia.edu/tag/0B5V) assumes a finite
surjective map between schemes proper over a Noetherian ring; ampleness
pulls back, with the forward proof using affineness. This supplies no
numerical very-ample threshold.

Source availability therefore passes the saved continuation test. The
next audit must still check every applicability bridge and integral
identity itself. Essential inputs are L071, L118, L120 and full L137;
L107 remains comparison only. No duplicate proof or new exclusion was
found or claimed. ATTEMPTS/070,073,078 and the parked order-five route
remain preserved. This is source-coverage approval, not approval of
L137's correctness or progress beyond the imported general theorems.
No new lemma, mathematical script, PROOF.md or DAG.md change was made.
