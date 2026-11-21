# Centered companion matrix source review1523

Literature-only review of assessment1522's exact target. The main gap is
L030--L032/C032a all-degree actual-Xi positivity, equivalently C028b's
unpaid H_d=o(d). C028g identifies the limiting zero functional; it does
not pay it. The intermediate object is the nominated K_d(D), with the
actual centered coefficients, arbitrary positive diagonal D, and all
algebraic multiplicities. An explicit o(d) upper cost could pay that
criterion. A uniform positive degree-linear cost floor would stop this
representation's majorant alone. Neither estimate is proved here.

## Primary statements and applicability

Gerhard Schmeisser, *Estimates for the Imaginary Parts of the Zeros of
a Polynomial*, Mathematica Balkanica16(2002),203--217,
https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf :
Section3, Lemma1, printed pp211--212, states for every complex n-by-n A
that the vector (|Im lambda_j(A)|) is weakly majorized by the singular
values of (A-A*)/(2i). Taking the full partial sum gives the total-height
bound by its Schatten trace norm. This matrix lemma has no orthogonality,
normality, simplicity, diagonalizability or real-spectrum premise.
Read the majorization definitions and Lemmas1--3, pp211--212; the proof
of Theorem1, pp213--214, applies it to characteristic roots. Lemma1 cites
Gohberg--Krein1969, Lemma6.1 p57; that book was not independently read.
The source's separate orthogonal expansion hypotheses are unnecessary
for Lemma1. Its proof is imported, not reconstructed.

Nicholas J. Higham, *What Is a Companion Matrix?*,23 March2021,
updated9 April2021,
https://nhigham.com/2021/03/23/what-is-a-companion-matrix/ :
read the opening definition, determinant identity (*) and its two
determinant arguments, including the transposed/permuted conventions.
It supplies the characteristic polynomial identity for monomial
Frobenius companions. In assessment1522's last-column convention the
roots are those of Q_d, including characteristic multiplicities; no
inverse or distinct-root hypothesis is required. Similarity preserves
the characteristic polynomial, and C028d's real translation preserves
imaginary heights. These facts verify the scope of Schmeisser's bound
for B=D A_d D^(-1). No D-dependent uniform condition number is needed.
The actual determinant and norm specialization can be written in the
future canonical calculation; no new companion identity is asserted.

John Watrous, *The Theory of Quantum Information*,2018 author-hosted
pre-publication version,
https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf :
Section1.1, printed pp32--34 (PDF pp39--41), (1.165)--(1.175),
(1.179)--(1.181), supplies Schatten norm definitions, monotonicity in p,
Frobenius entry formula, and the ideal inequality
||U X V||_p <= ||U||_infinity ||X||_p ||V||_infinity
for compatible maps between finite complex Euclidean spaces and
1<=p<=infinity. A coordinate inclusion and its adjoint have operator
norm1, so p=1 permits the proposed principal compression without a
dimension factor. The Hermitian imaginary part must be formed from
the scaled B itself; similarity is not asserted to preserve this norm.
These are imported norm properties, not a new compression theorem.

## Closest inspected scaling result

F. De Teran, F. M. Dopico and J. Perez, *New bounds for roots of
polynomials based on Fiedler companion matrices*, author manuscript
for Linear Algebra Appl.451(2014),197--230,
https://gauss.uc3m.es/fdopico/papers/laa2013-bounds-fiedler.pdf :
read Section7 Lemma7.2, Theorem7.4 and its complete proof, manuscript
pp18--19. For monic p with at least one nonzero lower coefficient,
Theorem7.4 identifies the infimum of the induced infinity norm over
diagonal similarities of each Fiedler companion with the positive
root R(p) of z^n-sum |a_k|z^k. Nonzero constant coefficient ensures
Perron-vector attainment. The zero-constant case retains the infimum
statement without that attainment conclusion. Lemma7.2 treats a
general complex matrix and the spectral radius of its entrywise
absolute value. It cites Strom1972's Theorem1/Corollaries1--2.
This is an induced row-sum norm of the whole scaled companion, not the
Schatten trace norm of its Hermitian imaginary part. Thus it does not
state the proposed optimized-cost floor. No conversion of its lower
bound into a lower bound for K_d is justified or used.

David Bindel, Shivkumar Chandrasekaran, Jim Demmel, David Garmire and
Ming Gu, *A Fast and Stable Nonsymmetric Eigensolver for Certain
Structured Matrices*,31 May2005 author manuscript,
https://www.cs.cornell.edu/~bindel/papers/2005-compan.pdf :
read Section7, manuscript pp9--10, its displayed general diagonal
scaling and the distinction between general and geometric scaling.
Its whole-matrix norm-balancing discussion supplies no theorem for
the present imaginary-part trace-norm infimum. This manuscript has
unfinished references/sections, so its balancing claims are not a
load-bearing import. Strom1972's separate spectral/logarithmic-norm
theorems remain unread leads; no claim about their precise conclusions
is based on the search results or an unsuccessful unverified URL.
The essential matrix interface is accessible independently above.

## Search, overlap and failure comparison

Queries included `Ky Fan eigenvalues imaginary part majorization
Hermitian imaginary part matrix trace norm theorem`; `diagonal scaling
companion matrix imaginary part eigenvalue bounds cycle product lower
bound`; `Schmeisser Estimates for the Imaginary matrix`; `diagonal
similarity companion bound numerical radius`; `companion diagonal
imaginary parts norm`; `diagonal similarity skew companion norm`;
`Minimization of norms and logarithmic norms by diagonal similarities`.
Followed the primary references and the author-hosted Fiedler manuscript.
Search-only leads, including forum answers, do not supply mathematics.
The bounded search did not locate a theorem evaluating this exact K_d
infimum or paying its actual centered degree asymptotics. This is not
a novelty claim or evidence that no matching theorem exists.

Local reads: C028a's matrix interface/cubic mismatch, C028b's convention
and criterion, C028c's hypotheses and retained-cost interface, and
C028d's centered coefficient formula and centering proof. Reused
source-notes1493/1496/1500 and audit1497 for their recorded scopes;
the exact-projection similarity and degree-increment comparisons were
searched narrowly. C028a stops one fixed Gaussian reference; C028c
stops its stipulated positive Jacobi reference family. Neither is an
optimization over the nominated monomial companion's positive diagonal
similarities. The fixed-terminal calculation therefore has an untested
scope. These older stops remain intact. No different Xi series,
primitive prescription or whole-matrix modulus bound is substituted.

## Decision and bounded continuation

SPECIALIZE: source coverage suffices for one finite actual-coefficient
test. Import the named matrix and norm facts; derive only the centered
terminal entries and their optimization, with every factorial and
scale retained. Start with the last three principal coordinates and
arbitrary positive ratios, allowing them to vary with d without bounds.
The available inputs are C028d's exact coefficient formula and second
coefficient, and C028a's actual central cubic combination and strict
signs. No centered cubic identity or optimized block estimate is
derived here. A three-coordinate test is a narrowing of the nominated
at-most-four-coordinate test, not a new mechanism invented to meet a
quota. The standalone continuation assessment1523 requires separate
approval on a later turn before its mathematical invocation.

Continue toward a stop only with a proved uniform constant c>0 and an
onset valid for every positive D. If the block instead admits cost/d
approaching zero, preserve the exact escaping ratios and abandon this
block as an obstruction; that alone supplies no upper bound for the
full K_d. An inconclusive finite optimization is recorded as such, with
no parameter sweep or root-reality conclusion. The remaining upper
payment S_F=0, RH and all-degree positivity stay unresolved. Full
matching Mathlib coverage is unchecked, not absent. No mathematical
script, lemma, PROOF or DAG was modified in this literature turn.

## Recovery1524: direct URLs in the ready assessment

LITERATURE_REASON: The supervisor reported that the ready assessment
lacked a direct source URL; the citations were previously delegated to
these notes. Reopened Schmeisser's PDF Section3 definitions/Lemma1
pp211-212, Watrous's author-hosted PDF (1.165)-(1.175),(1.179)-(1.181)
pp32-34, and Higham's opening companion definition/identity(*).
The accessible statements confirm the recorded hypotheses. Copied their
direct URLs into assessment1523's SOURCE_EVIDENCE and separately approved
its unchanged target. No fresh search, coefficient derivation, optimized
cost bound, lemma or mathematical script was needed. Outcome STALLED:
valid process repair, no new mathematical or source-scope evidence.
