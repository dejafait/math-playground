# Cyclic residual plane: saved reasoning

2026-10-14, step 224. RESEARCH / proof_attempt under the unchanged
EXPLORE assessment `drafts/literature/2026-10-14-cyclic-family-alternating-kernel.md`.

Main gap: exclude sixteen actual errors. Exact approved intermediate
target: determine whether L087's full alternating system has zero kernel
for every bijective H-labeling. Use audited L088 to restrict a possible
nonzero kernel to a rational rank-two plane S meeting every U_t.
The following are prospective deductions, saved before completion.

1. S cannot contain two moment columns: some block avoids both labels
   (at most eight blocks contain either), and six-column independence
   then prevents an intersection.
2. If S contains v_x, select consecutive blocks both avoiding x.
   Only four blocks contain x, spoiling at most eight of the sixteen
   consecutive pairs. Their intersection lines either coincide, giving
   a second moment column, or span S inside their seven-label union.
   Adjoining x gives eight independent columns, again impossible.
3. With no column in S, all sixteen intersection lines are distinct.
   In each consecutive triple the union has nine labels and the three
   lines have one relation with all three scalars nonzero. Its combined
   coordinate vector cannot be zero: that would put S in the span of
   the three shared-label columns, contradicted by a block avoiding them.
   The vector is consequently the unique nine-column Vandermonde
   circuit, nonzero at every label. All singleton coefficients are nonzero.
4. Each block appears in three consecutive triples; the singleton pairs
   in its first, middle and last roles cover all four labels. These pairs
   form a tree and determine all four coefficient ratios via the circuit
   formula d_i=1/product_(j in nine-label union minus i)(h(i)-h(j)).

Plausible downstream use: reconstruct each candidate intersection line
from h alone, then test whether their sixteen syndrome vectors have rank
two. Continue on a uniform contradiction or a useful exact residual
restriction; a positive rank sample is excluded. Original error charts,
actual-error applicability, arbitrary-family coverage and challenge
qualifications remain independent gaps. Essential inputs: L088, L087,
L010's column independence, L027's quotient interpretation. No source
refresh, cross-notebook input, labeling sweep or mathematical script.

Completed: [L089](../lemmas/L089-cyclic-residual-plane-reconstruction.md)
justifies all four deductions and reconstructs sixteen rational full
moment representatives r_s explicitly. Rank R>=2, with rank R=2
equivalent to a surviving kernel; all remaining shared-label equations
are displayed canonically. This is a local intermediate advance, not a
uniform zero-kernel proof, a new labeling computation or an actual-error
realization. No theorem beyond the checked source scope is claimed
original. Separate critical audit is the proposed continuation, pending
its own literature-scope approval.
