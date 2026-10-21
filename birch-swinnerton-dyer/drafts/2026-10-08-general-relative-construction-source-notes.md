# Arbitrary-level construction — completed primary source comparison

Saved and completed literature-only checkpoint. Target: assess construction coverage for
L037's complete torsion-free relative presentation and certified geometric
reflection/good-prime operators at arbitrary exact conductor N. No new
lemma, calculation or mathematical program is authorized in this step.

Inspected Stein online v0.1 weight-two equation (3) (integral relative
homology), Propositions 3.10--3.11, Theorem 3.13 and the good-prime endpoint
formula. These have arbitrary positive-level hypotheses. Read both path
reduction proofs, including infinity and signed convergents. Read Cremona
corrected second edition Chapter 2 Propositions 2.2.1--2.2.2 and their
composite-level coset/lift discussion. Its rational absolute Theorem 2.1.4
alone would not certify the required lattice. Existing L030 and its fixed
assessment are comparisons, not general construction premises.

Access qualifications: MathNet's English Manin PDF link and direct full-text
endpoint returned internal errors; the bibliographic record was retrieved.
Direct shell retrieval failed with DNS restriction. Stein's precise
published theorem can be imported without claiming to have read Manin's
omitted injectivity proof. The Kannan--Bachem author-hosted mirror returned
404 and the publisher PDF request redirected to the abstract.

The rectangular/arbitrary-rank normal-form statement and termination
proof have now been read. Full citations and domain qualifications follow;
the prior pending passage is preserved by this dated completion statement.

## Inspected source statements

[William Stein, *Modular Forms, a Computational Approach*, GSM 79,
AMS, 2007](https://wstein.org/books/modform/stein-modform.pdf),
equation (3.2.1), printed p. 40, identifies the torsion-free symbol module
with integral relative cusp homology. Propositions 3.10--3.11, pp. 42--43,
cover cosets and integral path generation for positive N. Both reduction
proofs were read, including the zero-denominator case and formal initial
convergents. Theorem 3.13, p. 44, gives all two/three-term relations followed
by quotienting torsion. Its proof verifies the relations and surjectivity;
injectivity is cited to Manin Section 1.7, not proved in the book. Section
3.4.1, pp. 47--48, gives the good-prime endpoint formula without restricting
N to be prime. This is complete relative, not just boundary-kernel coverage.
Theorem 3.7 concerns the latter and alone is insufficient. Import the stated
theorems; no new topological reproof or elliptic-point exclusion is needed.
Do not claim the raw integral relation quotient is already torsion-free.

[Stein online v0.1, General Modular Symbols](https://wstein.org/books/modform/modform/modular_symbols.html),
equations (11)--(12) and Remark 1.43, were read under the hypothesis that
diag(-1,1) normalizes the group. They define star with a minus sign; at
weight two geometric endpoint reflection is its negative, as already
checked in L029. Its full-relative adjointness coverage is reused unchanged.
This gives the convention to implement, not a new sign derivation here.
The alternative Merel construction is unnecessary for direct endpoint
reduction, and its determinant-two example does not approve all primes.

[John Cremona, *Algorithms for Modular Elliptic Curves*, corrected second
edition, 1997, Chapter 2](https://johncremona.github.io/book/fulltext/chapter2.pdf),
Propositions 2.2.1--2.2.2, pp. 15--16, identify projective primitive residue
pairs with cosets, using coprime integer lifts and Bezout top rows. Read the
equivalence proof and lift discussion, including composite N. Section 2.2,
p. 17, explicitly requires extra projective representatives beyond the
prime-power list. Theorem 2.1.4 is a rational absolute-homology theorem;
its elimination discussion is not an integral-lattice certificate. The
future specialization must certify a complete coset list and lifts using
these criteria, without copying L030's prime-level list.

[Francis Sergeraert, *About the Kannan--Bachem algorithm*,
arXiv:2411.02422v1, 4 November 2024](https://arxiv.org/html/2411.02422v1),
Sections 2, 3.1, 4, 6--7 and Theorem 1 with its entire proof were read.
Section 4 specifies rectangular/arbitrary-rank pivot and zero-tail cases.
Section 7 proves finite diagonalization by alternating the two Hermite
reductions; Section 2 supplies divisibility normalization and unimodular
operations. Tracking these operations supplies transformation witnesses.
Section 6 records coefficient explosion in a naive rank-deficient extension;
it does not refute finite normal forms. Import this general finite algorithm
and the named Smith normal form theorem; make no polynomial bound or
practical runtime claim for the notebook implementation. Benchmarks are
not mathematical termination evidence. The inaccessible original
Kannan--Bachem paper is not used as the general-domain premise.

[SageMath 10.8 Reference Manual, Dense matrices over the integer ring,
smith_form](https://doc.sagemath.org/html/en/reference/matrices/sage/matrix/matrix_integer_dense.html#sage.matrix.matrix_integer_dense.Matrix_integer_dense.smith_form)
specifies S=U A V with transformation output, and includes singular,
nonsquare and empty cases. This is an implementation option, not a
replacement for the mathematical theorem or an independent replay.
Its invariant-only shortcut is inadequate when coordinate witnesses are
required. The neighboring saturation option may restrict to one prime;
full quotient certification must remove all torsion, not only p-torsion.

## Applicability and evidence contract for later mathematics

The source domains match positive N, weight two and trivial character,
allowing elliptic points and composite levels. L029's M is already defined
modulo all torsion. The later proof must spell out how finite integer
normal-form witnesses certify that specific quotient and retain every
integral-generator coordinate; this review does not supply that derivation.
All paths, including infinity and negative rational endpoints, must retain
the orientation from alpha to beta. Direct reduction of reflected paths
and the ell+1 good-prime paths must cover every generator and check descent
through the complete relations and saturated quotient. A kernel-vector
eigenvalue check alone is insufficient. Finite exact rank computations and
independent arithmetic eigenvalues remain part of L037's application.

Coverage is SPECIALIZE, not a novelty finding. Sources already supply the
mathematical presentation and finite algorithms; only their certified
assembly remains to be written in a research turn. No general construction
theorem, matrix, new proof or certificate was produced here. If that
assembly fails to keep the full lattice or operator descent, stop its
application and record the exact failure. No repeated audit can replace
the independent normalization and arithmetic data.

Queries: `Manin modular symbols integral relative homology torsion elliptic
points theorem 1972 1.7`; `Stein modular forms weight two Theorem 3.13 torsion
Manin symbols integral continued fractions`; `Manin Parabolic points pdf`;
`Manin 1.7 torsion modular symbols`; `modular symbols Smith normal form
integral algorithm`; `Smith normal form Algorithm 2.4.14 Cohen`; `Kannan
Bachem 1979 polynomial algorithms Smith Hermite normal forms integer matrix
pdf`; `site:doc.sagemath.org smith_form transformation integral rectangular
matrix`. Cohen search snippets, prize pages, forum discussions and
nonprimary mirrors are not theorem inputs. No novelty is inferred from
search results or access failures. Manin's original Section 1.7 remains
unread; Stein's precise theorem is the cited standard input instead.

Main BSD gap remains rational rank equals complex order for arbitrary
analytic order at least two. Construction coverage could support producing
L029/L037's full relative line without q; q, normalization/coefficient
certificates, rational membership, divisible Sha and complex-order
comparison remain independent. Preserve ATTEMPTS/022--024. Approve only
complete integral quotient and finishing finite operator coverage; otherwise
qualify or narrow the target. Mathlib matching coverage is not checked.
