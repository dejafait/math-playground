# Fixed-cardinality marginals — primary source input

## Hypotheses

Use a finite Boolean variable universe of size H, a prescribed integer
number N of ones, and consistent local distributions through order r.
The source uses alphabet [q], cardinality fractions c_i, and arbitrary
finite CSP variables. Here q=2 and c_1=N/H. These variables will index
68-subsets, not the 1024 evaluation positions. No linear-code hypothesis
is involved. The source moment order is unrelated to RS dimension or m.

## Conclusion

Import the source's cardinality condition: for each local assignment
alpha on S, |S|<=r-1, the uniform average over variable indices j of

    Pr_(mu_(S union {j}))(X_j=i | X_S=alpha)

is c_i. The same section requires consistency of the local distributions
and agreement of their moments with the SDP vector inner products.
It explicitly warns that these distributions need not have a global
representing distribution.

This is an imported condition of the known relaxation, not a theorem
that arbitrary consistent marginals already satisfy cardinality. The
conditional display requires care at probability-zero assignments.
Conversion to homogeneous Boolean equations, all repeated-index terms,
and the Schrijver orbit coefficients is deferred to the mathematical
specialization; none is established by this source record.

## Proof

Prasad Raghavendra and Ning Tan, *Approximating CSPs with Global
Cardinality Constraints Using SDP Hierarchies*,
[arXiv:1110.1064v1](https://arxiv.org/pdf/1110.1064v1), 5 October 2011,
Section 3, Definition 3.1 and Definition 3.3, printed p. 7; the paragraph
headed “Lasserre SDP Hierarchy for Globally Constrained CSPs” and its
unnumbered conditional-cardinality display, printed p. 8; continuation
on p. 9. Read the local-distribution and inner-product requirements and
the nonexistence-of-global-distribution qualification. These supply
the general framework; no approximation or rounding theorem is used.
In particular, no asymptotic algorithmic guarantee supplies a finite
bound on A(1024,10,68).

The underlying constant-weight indicator necessity and permissible
unlabeled averaging are already imported in
[foundations/12](12-global-degree-three-moment-source.md), from Polak
v1 Section 1.1, (1)–(3), Proposition 1.1 and its full indicator proof,
p. 2, and Section 1.2, p. 3. Those passages were reinspected. Preserve
its printed A(n,d) versus proved A(n,d,w) qualification. The normalized
ordered-triple convention remains exactly
[foundations/04](04-constant-weight-triple-sdp-source.md), with all
impossible-orbit and complement-prefactor qualifications intact.

Independent thinning is separately recorded in
[foundations/11](11-independent-thinning-source.md). Last–Penrose,
21 August 2017 author version, Definitions 5.3 and 5.7, (5.6), and
Proposition 5.4 with its complete product-integral proof, pp. 40–43,
were reinspected. This input concerns an existing random subset and
independent marks; it does not provide deterministic size N or a
representing measure for a relaxed moment assignment. No fixed-size
sampling-without-replacement formula is imported here.

## Mathlib

Full matching cardinality-conditioned finite marginal/SDP theorem and
the proposed Schrijver specialization: not checked. Supporting finite
probability, convexity and Boolean-moment coverage: not checked.
Unknown availability is not evidence of absence.
