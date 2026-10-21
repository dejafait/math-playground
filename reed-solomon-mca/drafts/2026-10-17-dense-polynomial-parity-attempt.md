# Step 269 — bounded dense-polynomial parity attempt

Completed: the candidate mechanism below is now fully written in
[L100](../lemmas/L100-cyclic-low-degree-polynomial-parity-exclusion.md).
It excludes every nonconstant R in the approved range; separate critical
audit remains pending. This initial checkpoint is retained as saved
work-in-progress reasoning, not a second canonical proof.

Work in progress under the unchanged pre-invocation EXPLORE assessment
`drafts/literature/2026-10-17-cyclic-dense-polynomial-parity-test.md`.
The main gap is sixteen-count exclusion; this test concerns only the
hypothetical cyclic plane, not uniform triangle twelve or arbitrary families.

Candidate mechanism, not yet a reviewed result: for R of exact degree d,
1<=d<=4, subgroup power sums identify the product pairing with
16 times the coefficient of X^15 in Rfg. Its radical on polynomials of
degree at most seven should be the polynomials of degree at most 7-d,
with a nondegenerate d-dimensional top-coefficient quotient. Total
isotropy of the six-dimensional W forces the entire radical into W
for d=3,4, contradicting a full block intersection by Vandermonde.
For d=1,2 it instead forces P to contain a nonzero vector whose first
six moment coordinates vanish. Choose this vector as the direction
of a new plane chart. Each block line is finite, since a four-column
combination cannot have its first four moments zero. The locator
determinant then has degree at most two, whereas each coordinate
belongs to four distinct finite block events and is omitted at another.
Verify this determinant identity and every dimension implication before
promoting the argument to a canonical lemma.

Stop test: prove exclusion of every nonconstant degree-at-most-four R,
or retain the exact failed implication. Even exclusion supplies no
cyclic-plane impossibility and no extra product-dual direction. No
label census or gate-elimination restart is proposed.
