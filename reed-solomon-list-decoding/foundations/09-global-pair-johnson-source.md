# Global pair moments and Johnson spectral inputs — source record

## Hypotheses

The constant-weight universe consists of all w-subsets of an n-set,
with n>=2w. Its distance-i relation matrix A_i has entry one when
two supports intersect in w-i points; A_0=I. Moment coordinates
x(D) are indexed by support families D of size at most two.
All matrices and moment coordinates here are real.

## Conclusion

The cited constant-weight moment program uses x(empty)=1, pair zeros
at distances below the minimum, and PSD matrices indexed by unions.
At order two its unconditioned matrix has the constant and singleton
indices; the other matrices retain scalar nonnegativity. The source
identifies the optimized order-two bound with the Johnson Delsarte
bound. Neither this identification nor its optimal value decides an
additional prescribed-coordinate slice.

The Johnson eigenmatrix entries, with eigenspace index j and relation
index i, are the known Eberlein values

\[
 p_j(i)=\sum_{h=0}^{i}(-1)^h\binom jh
           \binom{w-j}{i-h}\binom{n-w-j}{i-h}.
\]

The valency is p_0(i)=binomial(w,i)binomial(n-w,i).
The relation matrices share orthogonal eigenspaces; the constant
eigenspace projector is J/|V|. The standard Schur-complement congruence
reduces a real symmetric block matrix with a positive definite leading
block to that block and its Schur complement, retaining zero eigenvalues.
These are source inputs, not a certificate for the notebook's fixed slice.

## Proof

Import Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight
Codes*, IEEE Trans. Inform. Theory 65 (2019), 28–38,
DOI 10.1109/TIT.2018.2854800. Inspected
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), 15 March 2017:
Section 1.1, equations (1)–(2), Proposition 1.1's complete indicator proof,
printed p. 2; Section 1.2's averaging argument, p. 3; Section 1.3, p. 4.
The displayed proposition ends in A(n,d), while its proof uses A(n,d,w);
retain that qualification already recorded in foundations/08.

For the explicitly nonnegative formulation import Andries E. Brouwer
and Sven C. Polak, *Uniqueness of codes using semidefinite programming*,
[arXiv:1709.02195v1](https://arxiv.org/pdf/1709.02195v1),
7 September 2017, Section 2, equation (1) and the ensuing Johnson A_2
comparison and orbit-averaging discussion, printed p. 2. No uniqueness
theorem, complementary-slackness conclusion or numerical output is used.

Import Andries E. Brouwer, Sebastian M. Cioabă, Ferdinand Ihringer and
Matt McGinnis, *The smallest eigenvalues of Hamming graphs, Johnson graphs
and other distance-regular graphs with classical parameters*, J. Combin.
Theory Ser. B 133 (2018), 88–121, DOI 10.1016/j.jctb.2018.04.005.
Inspected [arXiv:1709.09011v2](https://arxiv.org/pdf/1709.09011v2):
header 20 April 2018, title-page date 23 April 2018; Section 1.2,
printed p. 3, and Section 3's opening three eigenvalue formulas, p. 10.
The first formula is precisely the displayed p_j(i), with their d=w,
their relation j=i and their eigenspace i=j. No theorem identifying a
smallest eigenvalue is needed: all eigenspaces must be retained.

For the common spectral decomposition and constant projector import
A.E. Brouwer and W.H. Haemers, *Spectra of Graphs*, Springer, 2012,
ISBN 978-1-4614-1938-9; inspected
[author-hosted preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
retrieved 7 October 2026, Section 11.2, printed pp. 162–163,
including the expansions in minimal idempotents and Theorem 11.2.1's
proof. For the Schur complement use its Theorem 2.7.1(i), p. 36,
including the complete invertible triangular congruence identity.
Numbering and page references here are to that preprint. The
[author's errata page](https://homepages.cwi.nl/~aeb/math/ipm/)
was inspected; published-page corrections are not silently substituted
for preprint numbering. Taking the leading block to be [1] requires
no inverse of the lower block, even when that block is singular.

Delsarte's original thesis was not retrieved: its UCLouvain repository
marks the file restricted. The explicit eigenvalue input above is cited
to the inspected Brouwer–Cioabă–Ihringer–McGinnis passage, which refers
to Delsarte p. 48 and Karloff Theorem 2.1; those references remain unread.
No reproof of the scheme, hierarchy or eigenvalue theorem is proposed.

## Product spectral coverage added 2026-10-12

For finite undirected relation graphs, import Brouwer–Haemers, the same
author preprint, Section 1.4.7, printed p. 19: tensor products of factor
eigenvectors have the product eigenvalue, and the complete product
spectrum consists of those products. The entire passage, including the
coordinate definition of the tensor eigenvector, was inspected. Identity
relations are handled by their identity matrices, not by assuming a
loopless graph theorem applies to a diagonal relation. Section 11.2,
printed pp. 162–163, supplies simultaneous factor eigenspaces, their
complete idempotent decomposition, and the rank-one constant projector.
These are known linear-algebra inputs for linear combinations of tensor
relation matrices; no particular trial's spectrum is asserted here.

Primary cross-check: Schrijver's
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Theorem 1 (51) and Section III.A (52)–(59), printed pp. 6–7.
Freshly read (53)–(54)'s tensor change of basis, the full formula (56),
the weight-layer restriction (57)–(58), and the complete extension/reset
argument proving that this is the block diagonalization. Section III.B
identifies Y with (X\\Y,Y\\X), then states the PSD test (64).
For a fixed weight layer the source retains every admissible factor
index, not just the trivial representation. This algebraic input does
not require a code, a moment representing measure or averaging of a
labeled feasible point. The coding-average application is separate.
The qualifications on the complement prefactor and impossible scalar
orbits in foundations/04 remain in force.

Brouwer–Cioabă–Ihringer–McGinnis v2, Section 1.2, printed p. 3,
and Section 3, printed p. 10, cover all relations and eigenspace indices
of J(n,d) with n>=2d. Section 3.4, printed p. 12, states their
multiplicities binomial(n,j)-binomial(n,j-1). The opening formulas and
this multiplicity passage were inspected; no smallest-eigenvalue or
asymptotic theorem is substituted for the full spectrum. The hypotheses
cover the factors J(68,5) and J(956,5). Their use for L053's particular
shell and its anchor is a finite specialization still to be verified;
no PSD sign, shell eigenvalue or boundary improvement is established
by this source addition. The Schur theorem above inverts only the
positive leading scalar, so singular shell blocks need no new theorem.

## Mixed-layer algebra coverage added 2026-10-14

Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE Trans. Inform. Theory 51
(2005), 2859–2866, DOI 10.1109/TIT.2005.851748,
[eight-page author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf).
Read equation (7), printed p. 2; Proposition 5 (44)–(47), pp. 5–6;
Theorem 1 (51) and III.A (52)–(59), pp. 6–7; III.B (64), p. 7.
The tensor identity and the complete extension/reset argument were
inspected. The orthogonal blocks allow unequal layer indices i,j.
For two ground-set sizes w,v, equal cardinality in the two factors gives
block indices i,j in W_k intersect V_l, where W_k={k,...,w-k} and
V_l={l,...,v-l}. Equation (58) includes positive binomial rescalings;
(64)'s congruent beta form supports exact rational PSD checks. Singular
blocks are included. No code or representing measure is needed for
this algebraic input. The beta convention and source qualifications
remain canonical in foundations/04; no complement prefactor is used.

For the proposed application w=68,v=956, both source ground-set sizes
are positive and the layers 0,5,6 lie within both ranges. These layers
are selected by principal restriction in the source's layer coordinates,
equivalently by padding other layers with zero. This is the applicable
source operation, not a verified reduction of the notebook's prescribed
coefficients. Research must check the complete invariant coefficient
dictionary, all surviving source blocks, normalization and equality of
every represented unordered triple. It must also justify that averaging
preserves this exact unlabeled slice. No rectangular coefficient,
cross-mode sign, simultaneous extension or RS conclusion is established
by this coverage addition. Screenshot requests returned references only;
the readable formula text and existing foundations/04 convention were
used, without claiming visual inspection or a new local PDF.

## Mathlib

Full matching Johnson spectral theorem, constant-weight pair-moment
program and fixed-slice result: not checked. Supporting spectral,
Schur-complement and finite-set coverage: not checked. Unknown
availability is not evidence of absence.
Full matching mixed-layer Terwilliger block theorem and supporting
rectangular/invariant PSD reduction: not checked.
