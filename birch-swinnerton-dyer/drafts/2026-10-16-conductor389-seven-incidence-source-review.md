# Incidence source review — inspected evidence

2026-10-16, literature-only step 246; no mathematical construction has been run.

The exact saved target is construction/independent verification of the
Schaefer--Stoll Section 7 incidence pullback and fiber norm for L067.
The long author version dated 2001-06-13 has now been inspected at
Lemma 7.5, Lemmas 7.6--7.7 and Proposition 7.8, Corollary 7.9,
Proposition 7.10 (printed pp. 16--19), and Section 10.1 (pp. 24--25).
Primary URL: https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf .

Source definitions: A is the function algebra on nonzero torsion; B is
the function algebra on nonzero elements of Hom(E[p], Z/pZ), identified
with affine lines missing zero by the level-set value one. D corresponds
to incident pairs (P,line). The projections induce A -> D and B -> D.
Proposition 7.10 uses the determinant norm from D to B after pullback
from A, with a p-by-p multiplication matrix over B. These are imported
definitions/results, not a newly derived incidence lemma.

Do not replace B by A or by the scalar-fixed direction algebra A+.
Section 10.1 explicitly restricts its chord-slope formula to p=3;
that formula is not source coverage for p=7. The general Section 7
construction does apply to odd p over a number field without a full
GL(2) residual-image premise. Its cohomology conclusions still require
the two kernels and all unramified/local conditions, independently of
map production.

L067/L068 and scoped searches found no existing local incidence
certificate. ATTEMPTS/021/032/033/034 preserve independent finite
quotient, zero scalar, absent ordinary evaluation and interface stops.
They are not a ban on this distinct finite target.

The pending comparison is now complete in the canonical assessment
`drafts/literature/2026-10-16-conductor389-seven-incidence-maps.md`.
It imports Stacks 03QR (Galois sets), 39.23.5(3)/39.23.6/39.23.9 in
03BE (invariant equalizers, geometric orbits, finite-free quotients),
and 0BD2 (basis-independent determinant norm and base change).
Their statements and the relevant proof cases were read directly.
Sutherland Lecture 2 Section 2.2 supplies addition, including inverse,
doubling and O cases; L068 scalar coverage is reused unchanged.

The ordered-independent-pair quotient is an approved implementation
specification for the source incidence sets. Its actual rational
presentation, all quotient identifications, freeness and denominator
witnesses must be established in the future research attempt. No
instance computation or new quotient theorem is proved here.
Source-specialized required sizes are B_inc=48, D=336 and D/B_inc=7;
the ordered-basis ambient problem fits within A tensor A of size 2304.
These are requirements, not experimentally obtained dimensions.
Practical coefficient/rank-computation cost remains untested.

Magma V2.29 (2026-08-03) official handbook text/1568 and text/1570
were inspected at auxiliary etale functions, full three/five descent,
and p-isogeny descent. The seven-isogeny routines require a rational
point of order seven. The fake second-isogeny set does not give this
full incidence map. The general etale/unit routines are supporting
tools, not a preexisting fixed full-domain certificate. No software
execution or comprehensive absence claim follows from this comparison.

The assessment's decision is SPECIALIZE for the unchanged target,
limited to known-method reproduction with full independent replay.
No polynomial, map, norm matrix, rank witness or mathematical script
was produced. The proof overview and DAG are unchanged.
