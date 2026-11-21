# Signed block elimination — completed source comparison

TARGET: Assess whether eliminating negative-residue blocks in L777's exact signed pairing can give an actual-Xi coercivity bound beyond norm<1, with L779 as a fixed benchmark.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step440 searched Schur/coercivity, non-Hermitian compensated blocks, signed Hankel and actual-Xi overlap; inspected Gallier Sections1–2 and Berger–Giribet–Martinez Peria–Trunk Sections1–3, with the full Theorem3.3 proof. Reused ready Fredholm, accretive-sign and low-order overlap assessments; exact queries, local comparisons and unread leads below. No novelty inference.
SOURCE_EVIDENCE: Gallier, The Schur Complement and Symmetric Positive Semidefinite (and Definite) Matrices, 24 August2019, Section1 pp.1–2 and Propositions2.1–2.2/proof pp.3–4; Berger et al., arXiv:1807.08591v2, (1.1)–(1.3), Assumption3.1, Lemma3.2 and Theorem3.3/proof pp.1–5; reused Zhang 2601.18977v1 Lemma4.2/proof and L776/L777/L779 source coverage. Precise URLs and applicability below.
COMPARISON: Schur determinant factorization is covered, but symmetric positivity requires the cross-block adjoint relation; the non-Hermitian completion theorem chooses a coupling rather than bounding Xi's fixed one. L777 does not establish the needed pairing symmetry. L779's signed separation supplies neither block accretivity nor its error margin. Thus none of these results imports the actual-Xi coercivity estimate.
GAP: Pay the projection-induced asymmetry, the eliminated-block inverse/sign and a reduced-block lower bound from the actual reciprocal factor. Complex/multiple interior zeros, uniform grouping, reciprocal bounds and all mixed minors remain independent gaps. No block inequality or benchmark block value was derived here.
REASON: The primary comparison rejects an automatic compensation import and narrows the proposed mechanism to a symmetric-reference versus actual-Schur-defect test. A separate new continuation nominates that Xi-specific test; conditional Schur algebra alone is not an advance or a creative mechanism.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target changes from auditing a fixed signed determinant to a growing-order signed block estimate; its essential adjoint/coercivity hypotheses were outside the ready Fredholm assessments.
SCOPE: Completed literature-only step440. This review supplies source scope and a bounded target nomination, not a new block theorem, estimate, calculation or certificate. The new mathematical continuation has its own exact assessment and requires separate next-turn approval.

## Original nomination — retained, source-status statements superseded below

The main gap is actual-Xi all-degree mixed positivity. The proposed
intermediate target is a signed block estimate for L777's exact finite
interaction that retains compensation between opposite-sign residues.
A useful threshold would be a strictly coercive reduced block and a
separately positive eliminated-block determinant, sufficient for
determinant positivity without full operator norm<1. The ordinary block
identity alone is not the target and must be imported if covered.

Inputs are L017/L018/L021/L776/L777 and the audited L779 benchmark.
Initial scope: pairs with independently certified simple real interior
zeros, so residue signs are real signs; no global real-root assumption.
Exact grouping, complex or multiple interior zeros, actual-F reciprocal
estimates, uniformity in r and other mixed minors remain unresolved
independent assumptions. Even a conditional estimate leaves those gaps.

Compare precise block hypotheses with known Schur-complement/coercivity
theorems, ready Fredholm sources, actual-Xi low-order sign coverage and
the recorded shifted-boundary and scalar-modulus stops. First search
only the named local Fredholm proofs, assessments and failure records.
Do not repeat general Fredholm discovery or infer novelty from absence
of a match. An inverse or sign premise that merely assumes unpaid minor
positivity is a decisive obstruction, not an allowed input.

A prospective creative test, after coverage, would ask whether actual-G
structure pays a compensated block bound or whether an admissible
obstruction rules out the proposed premises. L779 is a mandatory
consistency benchmark: a criterion reinstating full norm<1 cannot
explain its signed separation. Continue only with an additional
Xi-specific estimate and a concrete finite threshold; abandon if the
remaining condition is target-equivalent, false on the benchmark or
lacks a discriminating test after comparison. A larger finite scan or
routine block identity is not a creative advance.

If comparison justifies that mathematical attempt, nominate
proof_attempt/creative, deep_research/max. Its escalation obstruction
is missing signed compensation at growing order despite the audited
norm>1 benchmark; the bounded test must identify the exact coercivity
threshold or a counterexample under the proposed hypotheses. At present
essential source coverage and the Xi-specific estimate are missing,
so the immediate routing is literature_comparison, standard/high.
This nomination is REVIEW_REQUIRED, not a ready mathematical continuation.

## Completed comparison — step440, 2026-11-04

The main gap, intermediate purpose and independent gaps in the original
nomination remain unchanged. The negative finding is about source
applicability: neither ordinary positive Schur theory nor the inspected
indefinite completion theorem proves the actual signed compensation.
It is not a counterexample to Xi positivity or a global stop of the route.
No new lemma or mathematical script was written, and no proposed
matrix or benchmark block was evaluated.

### Primary statements and essential proof cases

Jean Gallier, *The Schur Complement and Symmetric Positive Semidefinite
(and Definite) Matrices*, 24 August2019,
[author PDF](https://www.cis.upenn.edu/~jean/schur-comp.pdf),
Section1 pp.1–2 and Section2 pp.3–4. Read both elimination factorizations
and Propositions2.1–2.2 with their congruence proof. The general block
factorization requires an invertible eliminated block. The positivity
equivalence additionally requires a real symmetric matrix and a positive
eliminated block. The displayed transformation is a congruence; the
nearby prose's word “similar” must not be used as a similarity claim.
The singular case is not imported; a pseudoinverse is no free replacement.

Thomas Berger, Juan Giribet, Francisco Martinez Peria and Carsten Trunk,
*On a class of non-Hermitian matrices with positive definite Schur
complements*, [arXiv:1807.08591v2](https://arxiv.org/pdf/1807.08591v2),
3 October2018. Read (1.1)–(1.3), Assumption3.1, Lemma3.2 and the full
Theorem3.3 proof, pp.1–5. For Hermitian A,D the structured matrix is
[A,-AK; K* A,D], with complement D+K*AK. Write p_+ for A's positive
eigenvalue count, q for D's nonpositive count and p_0=dim ker D.
Theorem3.3(i) asserts existence of K with ||K||<kappa and positive
complement exactly when q<=p_+ and kappa^2 lambda_i+mu_i>0 for
1<=i<=q-p_0, in the source's ordered spectra. Part(ii) uses q-p_0<=p_+,
weak inequalities and ||K||<=kappa for a semidefinite complement.
The necessity proof uses subspace counts and Weyl; sufficiency constructs
K by aligning eigenspaces. This is an existence/completion result,
not a bound for a prescribed coupling. Moreover the determinant formula
still retains det(A); complement positivity alone cannot pay its sign
when A is indefinite. Section4's spectrum formulas concern the constructed
K and are not imported for Xi. This is the relevant stronger-looking
non-Hermitian result, with its restrictive structure retained.

Reuse the ready real accretive determinant implication in
`2026-11-04-signed-qpascal-symmetric-part-review.md`: Teng Zhang,
*Johnson's determinantal identity for contiguous minors of Toeplitz
matrices, with an accretive extension*,
[2601.18977v1, Lemma4.2/proof](https://arxiv.org/html/2601.18977v1#S4).
A real finite matrix with strictly positive symmetric part has positive
determinant. The earlier comparison read its full skew-symmetric
factorization and semidefinite-limit proof. Its hypotheses are unchanged;
no repeated discovery or reproof is needed. It supplies a sign interface,
not the strict lower bounds. The older q-Pascal coordinate obstruction
concerns another matrix; it does not prohibit this Schur normalization.

Reuse the ready finite-rank Sylvester identity and arbitrary trace-class
Bornemann perturbation comparison in
`2026-11-04-signed-rank-two-fredholm-diagnostic.md`, and the audited
L776/L777 normalization. These already cover reducing the signed
determinant without replacing it by singular values. No new general
Fredholm search or positive-selfadjoint perturbation import is needed.

### Applicability, duplicates and failures

L777 writes A=UCY*, with U=Q_r H(b)V and Y=Q_r conj(V). In the proposed
certified real/simple case, C is the diagonal matrix of complete real
residues and S=Y*U is the exact signed pairing. The record establishes
neither S=S^T nor a positive diagonal symmetrizer. Reality of coefficients
and symmetry of each Hankel factor are insufficient *as cited premises*:
the pairing includes a one-sided projection and different column maps.
No claim that actual symmetry is false was proved here. A future attempt
must check the exact relation rather than insert an adjoint by analogy.

The reciprocal-factor dependence is essential: b=p/F and c=F/p;
complete residues involve F at the interior zeros, whereas S involves
positive Laurent coefficients of p/F. Splitting residue signs alone
does not provide a cited estimate for the resulting block products.
Theorem3.3's freely constructed K cannot replace these fixed data.

L779 is an independently audited positive determinant with original
norm>1, under its documented arithmetic contracts. Its complete proof
and exact pairing were consulted; its certificate was not replayed or
sampled again. No block positivity follows from that determinant sign.
Ready literature already records low-order positivity and the mismatch
between fixed-order/far-tail results and k=r-1 at growing r. That overlap
assessment was reused, without asserting a new low-order theorem.

The targeted local comparisons also included the shifted Fredholm
boundary-sign ATTEMPTS record, L775's hypotheses/conclusion and sector
qualification, the direct actual-theta compensation source-limit record
and assessment, and the signed q-Pascal odd-coordinate stop. They retain,
respectively, an unpaid boundary determinant, an overwhelming full
absolute complement, no actual signed cofactor bound, and a failed
specific accretive normalization. The proposed actual Schur defect is a
different observable; none of those records proves its sign or bans it.
No matching paid block estimate was found in these named local records;
that is not a novelty claim. No other notebook was consulted.

### Search and access limits

Queries included `Schur complement coercivity non Hermitian block matrix
numerical range positive definite block elimination theorem`, `Riemann
xi Toeplitz determinants signed Hankel Schur complement positivity
reciprocal zeros`, `"signed" "Hankel" "Schur complement" "Riemann"`,
`"Riemann xi" "Fredholm" "coercivity"`, `"Riemann xi" "negative
residues" Hankel`, and `"Riemann xi" "Schur complement" coercivity
Toeplitz`. Primary theorem hypotheses were retrieved before the longer
Theorem3.3 proof. Search snippets and secondary reports were not imports.

Boyd–Vandenberghe AppendixC.4 timed out; Gallier and Berger supply the
needed elimination proof, so this is not an essential source blocker.
Direct shell downloading also failed DNS; browser-readable primary text
supplied the statements and proof cases. An accidentally opened unrelated
arXiv identifier was excluded. Search leads on dissipative Hamiltonian
systems (2111.05616), pseudo numerical ranges, Xi operator-realization
claims and newer kernel-positivity manuscripts were not read at theorem
level or imported. No claim about their correctness or novelty is made.
They are not needed for the bounded test of the already specified pairing.
Mathlib coverage for the full new estimate is not checked; no absence
claim and no new Mathlib-based hypothesis is asserted.

### Decision and nominated test

Do not approve “negative residues give a positive correction” as a
theorem. Nominate one explicit absolute-residue-balanced Schur test,
specified in `2026-11-04-balanced-schur-defect-test.md`, for separate
approval. Its target is an actual-Xi lower bound that pays the difference
between the true nonsymmetric pairing and its symmetric reference,
including the eliminated inverse. A conditional Schur identity alone
does not count as completing that target.

Continue only upon a positive eliminated-block coercivity margin and a
strict reference-minus-defect margin, derived from actual F/p data and
compatible with L779. A certified adverse block direction or unpaid
inverse/sign stops this specified normalization, not RH. No radius or
precision sweep is nominated. The bounded analytic attempt is creative
only because of the proposed Xi-specific payment; importing Schur algebra
or checking a two-by-two scalar is routine work within that attempt.
