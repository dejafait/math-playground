# Completed comparison: strict finite-order reciprocal-density transfer

TARGET: Compare primary finite-order Pólya-frequency transform theorems with Sra v2's strict PF256 hypothesis to decide whether strict PF256 reciprocal densities force the first Laguerre sign for real even reciprocal polynomials, or nominate one fixed diagnostic.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched finite-order PF rational Laplace transforms, reciprocal-polynomial Laguerre signs, strict finite-type kernels and complex-pole convolution models; inspected Khare's primary finite-order theorems and relevant transform proof, Grochenig's all-order formulation, and Sra's strictness criterion. Queries and exact reading scope are recorded below; no matching implication or counterexample was established.
SOURCE_EVIDENCE: Khare arXiv:2008.05121v2, Theorems D/E (printed p.7), Theorem D proof (p.21); Grochenig arXiv:2007.12889v1, definition and Theorem 1 (pp.1-2, exposition of Schoenberg); Sra riem-xi v2 (29 October 2026), Theorem 1.2 and Appendix C.1/C.4, Lemmas C.1/C.6 with their complete proofs (pp.18,21). Reuse the parent Proposition 3.3/Section 3.2 reading and its qualifications; no probability or numerical certificate audit.
COMPARISON: The strict ordered-minor convention matches Sra. Khare D assumes compact support and excludes zeros of the transform, not poles of 1/P; E characterizes fixed-order nonnegative minors without an all-real reciprocal-zero conclusion. Schoenberg's characterization requires all orders. Sra C.6 supplies a sufficient global differential-determinant test, not the requested polynomial sign. L560 remains only a PF2 contrast.
GAP: The universal strict-PF256 implication is neither proved nor refuted by the inspected sources. One fixed high-rank rational diagnostic is nominated separately; positivity, strict finite-order minors and its negative polynomial sign all remain unproved. Actual-Xi transfer and the complete signed residual remain independent.
REASON: Complete the essential source comparison and move to the one fixed diagnostic under separate continuation approval. No source-access blocker is essential to that test, no universal negative follows from the search, and no new mathematics was derived this turn.
LITERATURE_REASON: The hypothesis changes from ordinary log-concavity to strictly positive ordered minors through order 256; the previous ready audit explicitly excluded these hypotheses and finite-order transform theorems are essential unread sources.
SCOPE: Completed theorem-level comparison of the precise implication below and nomination of one fixed object. This assessment does not certify that object or the universal implication. No mathematical derivation, parameter tuning, PF256 certificate audit or actual-Xi theorem application occurred.

## Exact diagnostic implication to assess

Let P be a real even polynomial with P(0)=1. Let p be an even,
strictly positive C2 probability density on R. Assume there is rho>0
such that its bilateral integral is absolutely convergent and

    integral_R exp(-zx)p(x) dx = 1/P(z)   (|Re z|<rho).

Use the following explicit strict finite-order hypothesis, now checked
against Sra v2 Theorem 1.2: for every integer
1<=m<=256 and every pair of strictly increasing real lists
x_1<...<x_m and y_1<...<y_m,

    det[p(x_i-y_j)]_(i,j=1)^m > 0.

The question is whether these assumptions alone imply

    P'(t)^2-P(t)P''(t)>=0   for every real t.

No density satisfying these stronger assumptions is asserted here.
In particular L560's density has not been tested for them. The domain
of the proposed polynomial sign is all real t, including outside the
transform strip; an in-strip theorem alone does not settle this target.
Distinguish strict from nonstrict minors and finite order from all
orders in every theorem comparison. Do not silently append actual-Xi
growth, self-decomposability, or zero information.

Start with exact theorem statements and their relevant proof cases,
not large unselected source extracts. Reuse the parent assessment
`drafts/literature/2026-10-31-complete-first-sign-mechanism-discovery.md`
for the already-read Sra passages and earlier failures. The precise
source assertion and all extra assumptions must be checked before
claiming a match. The source's certificate is not a proved premise of
this conditional diagnostic and need not be audited to compare the
implication itself. Import a covering theorem with a precise citation;
otherwise nominate at most one fixed, independently testable object
with a separate assessment. Do not declare a universal implication
false merely because no sufficient theorem was found.

Downstream use: decide whether the stronger finite-order hypothesis
can supply a sign mechanism or itself needs an obstruction test before
an actual-Xi transfer is considered. Actual-Xi realization, the complete
signed residual, higher signs and all-height RH remain independent.

Continuation/abandonment test: close the comparison only after exact
primary hypotheses give either an applicable implication, a documented
obstruction, or a specific uncovered diagnostic. An inaccessible
essential theorem is SOURCE_BLOCKED, not approval to calculate. Do not
repeat the PF2 audit or tune its parameters to fill this gap.

Mathlib: matching finite-order transform coverage has not been checked;
availability is unknown. Future mathematical targets require their own
matching assessment; this comparison alone is not their invocation gate.

## Completed source review — 31 October 2026

The main gap remains actual-Xi all-degree positivity. The intermediate
question above could validate or obstruct a finite-order sign mechanism;
it cannot supply Xi realization or higher signs. The continuation test
was a matching theorem, a source-backed obstruction, or one specified
diagnostic. The third outcome was reached, without settling the implication.

**Primary finite-order result.** Apoorva Khare, *Multiply positive
functions, critical exponent phenomena, and the Jain–Karlin–Schoenberg
kernel*, [arXiv:2008.05121v2](https://arxiv.org/pdf/2008.05121v2),
12 April 2021 (PDF dated 13 April), Theorem D, printed p.7, and its
proof on p.21. Its integrable function is positive on (-r/2,r/2),
vanishes outside [-r/2,r/2], and is defined on (-R,R), with
0<r<=R<=infinity, r finite. For 0<epsilon<=R-r/2 it assumes TN_q
on [0,epsilon) times (-r/2,r/2+epsilon), q>=2. The conclusion is
that its bilateral transform has no zeros in |Im s|<q*pi/r.
The proof's sampled Toeplitz matrices yield a sector exclusion for
polynomials; compact Riemann sums and Hurwitz give the stated strip.
Here the proposed density is positive on all of R, and the issue is
the reciprocal polynomial. Neither the support hypothesis nor the
conclusion matches. No truncation or pole conclusion is imported.
Theorem E on the same page was read for its fixed-order determinant
and decay characterization; it gives no missing reciprocal-zero result.

**All orders versus finite order.** Karlheinz Grochenig,
*Schoenberg's Theory of Totally Positive Functions and the Riemann
Zeta Function*, [arXiv:2007.12889v1](https://arxiv.org/pdf/2007.12889v1),
25 July 2020, definition and Theorem 1, printed pp.1-2, formulate the
all-order nonnegative-minor characterization by reciprocal
Laguerre–Polya entire functions. This is an inspected exposition,
not a newly checked proof of Schoenberg's original theorem. Original
references: Schoenberg, *On Polya frequency functions. I*, J. Analyse
Math. 1 (1951), 331-374, Theorem 1, DOI 10.1007/BF02790092; and
*On the zeros of the generating functions of multiply positive
sequences and functions*, Ann. Math. 62 (1955), 447-471,
DOI 10.2307/1970073. Their DOI routes were inaccessible; neither
original is claimed read. This is not an essential blocker for the
available primary finite-order comparison or the diagnostic below.

**A usable strictness interface.** Sra,
[*On some positivity properties of the Riemann Xi function*, v2](https://suvrit.github.io/papers/riem-xi/riem-xi-v2.pdf),
29 October 2026, Theorem 1.2 matches exactly the increasing-tuples
strictness convention above. Appendix C.4, Lemma C.6 (printed p.21)
assumes p in C^(2m-2)(R) and

    (-1)^(k(k-1)/2) det[p^(i+j)(x)]_(i,j=0)^(k-1) > 0
          for every x in R and 1<=k<=m.

It concludes strict ordered minors through m. Its entire short proof,
and Lemma C.1/proof (p.18), were read: two Wronskian transfers give
the criterion. Thus this route needs C^510 for m=256; C2 alone is
not enough to apply it. Lemma C.7 is specific to a certified Xi
convolution; its certificate is not audited or applied to a new model.
The criterion is only sufficient: failure to certify it would not
disprove strict PF256. No reproof is needed or supplied this turn.

**Additional primary comparison.** Albert–Levandosky,
[*Total Positivity and Spectral Properties of Linearized Operators*,
arXiv:2603.23876v1](https://arxiv.org/html/2603.23876v1),
Section 3, Lemmas 3.1-3.3/3.6 and Remark 3.7, distinguishes strict
from strong PF2 and asks a broader polynomial Green-kernel converse.
The explicit quartic complex-pole case there is oscillatory; it is
not an obstruction for every higher-degree convolution. These inspected
passages do not cover strict PF256. The search-returned aiXiv PF2
counterexample is an unread lead, not an imported result or priority claim.

Search queries actually used included:

- `Schoenberg Pólya frequency functions finite order Laplace transform zeros sector theorem`;
- `"Pólya frequency" "rational" "finite order"`;
- `"multiply positive" "rational" Laplace`;
- `"Pólya frequency" "rational Laplace"`;
- `"Pólya frequency" "Laguerre inequality" reciprocal`;
- `"finite order" "reciprocal polynomial" "positive"`;
- `"Polya frequency" "convolution" "complex poles"`;
- `"Pólya frequency" "perturbation" "finite order"`.

Accented and unaccented variants were also used. Search snippets are
leads only. Khare's powers/Wallis examples, discrete sequence sector
results, and Hirschman–Widder search hits are not asserted to settle
this rational, even, strictly positive density question. No matching
reciprocal-transform classification or novelty conclusion follows here.

## One fixed diagnostic nominated

The exact object and target are in
[the separate assessment](2026-10-31-high-rank-pf256-fixed-model.md).
It replaces two slow real modes by a fixed 270-fold real-pole
convolution and tests the global derivative determinants, rather than
replaying L560's scalar curvature estimate. It is not a parameter
search. All signs, smoothness/transform hypotheses and tail bounds
remain tasks for a later authorized mathematical attempt. The new
assessment receives separate approval next turn. There is no justified
creative actual-Xi sign target here: an independently controlled signed
remainder is still missing. This finite-model development is not
relabeled creative to satisfy routing preferences.

Outcome: EXPLORATION. The review resolves source scope and nominates
one test; it proves no new lemma, universal counterexample or RH result.
No lemma, mathematical script, DAG or PROOF.md change was made.
