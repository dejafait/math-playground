# Cubic RM Kuga--Satake small-factor test

Completed working record, 2026-09-27. The exact saved target was to decide
whether the full A=KS(T), at the specified very general rank-eighteen
cubic-RM point, has a nonzero abelian subquotient of dimension at
most six. The prior assessment is
[SPECIALIZE](literature/2026-09-27-cubic-rm-kuga-satake-small-factors.md).
Existing notebook changes are preserved.

The local gap is algebraic beta_U beyond the Dickson family, with
algebraic kappa a separate missing input. A small subquotient would
be a prerequisite for the reviewed low-dimensional Weil-cycle
supplies through abelian homomorphisms. Their absence would stop
only this recipe. The threshold is twelve for rational H^1, not
six; no sharp rational factor classification is needed to exclude it.

Reused the ready assessment and reread Schlickewei, Theorem 3.3.1,
and van Geemen, section 5.4 and Lemma 5.5, at their saved primary
PDFs. Their statements and hypotheses agree with the assessment.
No new target was screened and no source-discovery pass was needed.

Preliminary calculation: after complexification the three
six-dimensional orthogonal factors each have two half-spin modules
of dimension four. The full even Clifford H^1 contains the eight
external tensor products, each of dimension 4^3=64. Using
Schlickewei's V=W^(direct sum 4) and the regular left action on
each split even Clifford algebra gives multiplicity 4*4^3=256
for each type; 8*64*256=2^17 checks the full dimension.

The completed proof checks the actual Hodge-group action on all
of H^1, invariance of rational subquotients after complexification,
and contravariance and Poincare complete reducibility for quotients
of abelian subvarieties. A nonzero such subquotient has rational
dimension at least 64 and abelian dimension at least 32>6.
Complex half-spin blocks are not claimed to descend individually;
the lower bound is sufficient without being asserted sharp.

The separate divisor-algebra obstruction and earlier support/bundle
failures are not inputs to this calculation. This is an application
of the reviewed representation theory, classified as REPRODUCTION.
No algebraic cycle or transverse extension is constructed.

The canonical full proof is
[L032](../lemmas/L032-cubic-kuga-satake-has-no-small-abelian-subquotients.md).
The completed target supplies an informative negative result and
stops the low-dimensional homomorphism recipe. This conclusion also
holds for powers of A and for homomorphisms in either direction.
Higher-dimensional Pryms and arbitrary algebraic correspondences
remain outside the test.

An exact integer arithmetic check enumerated all eight sign triples,
confirmed dimension 64 and multiplicity 256 for each, and checked
the sum 131072=2^17 and the threshold 64>12. This checks bookkeeping;
the representation and subquotient arguments are the written proof.
No mathematical script was added or modified.
