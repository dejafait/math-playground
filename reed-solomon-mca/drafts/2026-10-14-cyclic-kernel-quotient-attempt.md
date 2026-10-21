# Cyclic alternating kernel: bounded quotient attempt

2026-10-14, step 221. Completed under the pre-existing EXPLORE
assessment `drafts/literature/2026-10-14-cyclic-family-alternating-kernel.md`.
The target remains the entire common exterior kernel for L087, uniformly
over bijective H-labelings. No labeling computation is proposed.

Main gap: exclude sixteen actual errors. Intermediate target: force the
cyclic family's common kernel to zero, or obtain an exact restriction
with a residual test. A family-specific obstruction would still need
actual-error applicability and would not cover arbitrary families.

The coordinate-kernel start of L027/L029 does not transfer: three linear
four-blocks have union at least nine. Instead use the image S of an
alternating tensor and Q=V/S, retaining every zero projected column.
The elementary alternating-elimination argument in L073 is a method
comparison, not an imported plane-family conclusion. Its implication
dim(S intersect U)>=rank(p)/2 will be checked explicitly here.

Reasoning checkpoint saved before the full proof; all items below were
subsequently justified in canonical L088:

- Rank eight fails using the twelve distinct neighbors of one vertex.
- Rank six gives one-dimensional block images in Q. At least ten
  columns project nontrivially. Their collinearity graph is connected:
  every vertex has only three nonneighbors. This contradicts dim Q=2.
- Rank four: every block has a disjoint partner, forcing each block
  image in Q to have dimension two; disjoint block images are
  complementary. Any two vertices admit disjoint containing blocks.
  For the ordered pair (0,d), d=1,...,8, candidate block-shift pairs
  are (10,1),(10,1),(10,3),(12,4),(12,4),(15,6),(0,7),(0,8).
  Translation and reversing the vertex pair cover all pairs. Thus two
  nonzero projected columns cannot be proportional. At most four
  columns are zero. Among the sixteen translates of the block triangle
  (B_0,B_1,B_2), whose intersection labels are {1,2,6}, some triangle
  has all three intersection projections nonzero. Its three distinct
  two-dimensional block images must lie in one three-dimensional
  subspace. Its nine-label union then contradicts independence of any
  eight original columns after quotient by S of dimension four.
- If this excludes rank four, every nonzero kernel tensor has rank two.
  Use disjoint B_0,B_7 to place the whole kernel in U_0 wedge U_7.
  Two independent rank-two cross tensors whose sum also has rank two
  must share one factor. If that factor lies in U_0, the disjoint pair
  B_7,B_14 avoids it except when it is proportional to v_4; then use
  B_1,B_8 instead. A common-factor three-space would have to meet both
  complementary block spaces in dimension at least two, impossible.
  The U_7 case follows by an abstract index translation, not by changing
  or assuming symmetry of the field labeling.

Completed result: [L088](../lemmas/L088-cyclic-alternating-kernel-restriction.md)
proves K has dimension zero or one and every nonzero element is
decomposable. Its full proof retains all zero projections and the
exceptional common-factor case. The rank-27 versus rank-28 issue remains;
no nonzero kernel has been exhibited and no uniform zero-kernel claim
has been proved. This is a local mathematical advance beyond the
conclusions of the sources checked, not certified originality or a
family exclusion. The result awaits separate critical audit. No
mathematical script or rank sampling was used. Prior failure records
ATTEMPTS/020,029,031 remain intact.
