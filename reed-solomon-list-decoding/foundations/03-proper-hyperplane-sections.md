# Proper hyperplane sections

These are standard geometric inputs for the component-cover review of
2026-09-25. Work over an algebraically closed field K. An affine algebraic
set is taken with its reduced structure. For an irreducible affine set W,
deg(W) means the degree of its projective closure; cdeg(V) is the sum of the
degrees of all irreducible components of V, including components of smaller
dimension. In particular, a reduced point has degree one.

## Named standard input

Use the **projective Bezout theorem, variety–hypersurface form**: if an
irreducible projective variety Z of dimension d>=1 is not contained in a
degree-e hypersurface H, the components Z_j of Z intersect H have dimension
d-1, and their positive intersection multiplicities satisfy

\[
 \sum_j m_j\deg Z_j=e\deg Z,\qquad m_j\ge1.
\]

For an affine hyperplane h=0 not containing an irreducible W of positive
dimension, apply this theorem to its homogenization and the projective
closure of W. Restriction to the affine chart discards any components at
infinity. Every remaining component is dense in its projective closure.
Consequently each nonempty component of W intersect {h=0} has dimension
dim(W)-1 and the sum of their degrees is at most deg(W). No generic choice
of h, smoothness of W, or transversality is needed; multiplicities can only
make the reduced sum smaller.

The dimension assertion also follows from the proper-subset dimension
inequality and the affine intersection dimension theorem, precisely
[Stacks Project, Lemma 33.34.2, tag 0B2N](https://stacks.math.columbia.edu/tag/0B2N).
That reference supports dimension control; it is not a citation for the
whole degree bound or the list-decoding application.

## Further degree conventions used in the graph review

The same named projective Bezout theorem applies to a proper affine
hypersurface section of degree e>=1: its components have dimension one
less, and their reduced degree sum is at most e deg(W). A nonzero constant
equation has empty zero set. A zero-dimensional irreducible affine set is
a point and is either retained or removed by an equation.

Use also the **generic linear-section characterization of projective
degree**. If Z is an irreducible projective variety of dimension t over an
algebraically closed field, and O is a nonempty open subset, a general
codimension-t linear subspace meets Z in deg(Z) distinct points, all in O.
For t=0 this says that a reduced point has degree one. For t>0, the field is
perfect, so the smooth locus is dense. The incidence dimension count lets
a general complementary linear subspace avoid Z minus O and the singular
locus, and meet the smooth locus transversely. Its intersection is therefore
reduced; its length is deg(Z), by the definition of degree via general
linear sections (equivalently t! times the leading coefficient of the Hilbert
polynomial). This is a standard degree fact; a bound for rational graph
closures still requires a separate argument controlling the pulled-back
equations.

## Mathlib

Projective Bezout, cumulative degree, the generic linear-section statement,
and the full affine statements used here: **not checked** in Mathlib.
The Stacks reference is a mathematical source, not a claim of formal-library
coverage.
