# Fixed matched model across degrees — completed source review

TARGET: Assess whether L791's unchanged exact parameters A,B,C,D give p_d exactly d simple positive roots for every degree d>=1, using primary hypergeometric or multiplier-sequence results and distinguishing this model-existence question from universal residual preservation.
CHECKED: 2026-11-05
DECISION: IMPORT
SEARCH_EVIDENCE: Step594 searched hypergeometric real-zero classifications, Pochhammer-ratio multipliers and Jensen criteria; read Sokal Theorems3/5 and full Theorem5 proof, the infinite Pólya–Schur characterization, and Holland's finite-model hypotheses. Exact DOI/arXiv searches in local assessments, attempts and history found no earlier L791 classification assessment; Ki–Kim–Lee heat-flow hits were unrelated.
SOURCE_EVIDENCE: Sokal JMAA515(2022),126432, pp.2–3, Theorems3/5 and proof includes p=q and imports Ki–Kim JMAA243(2000),249–260, Theorem3. Katkova–Shapiro–Vishnyakova arXiv:1010.6052v1 p.2 Theorem3 gives the infinite Pólya–Schur bridge. Original Ki–Kim PDF inaccessible; its classification is a cited external theorem, not an independently audited proof.
COMPARISON: The known p=q classification supplies a necessary integer-matching test for the fixed coefficient model via Pólya–Schur. This addresses model existence, not the residual operator. Holland's sufficient Jacobi regime and L791's five-root brackets do not answer the all-degree question.
GAP: Only the local applicability argument remains: check coefficient/scaling conventions, the exact positive box, both parameter matchings and multiplicity logic. No fixed-model obstruction, failure degree, simplicity theorem or redesign is proved in this literature turn.
REASON: Essential source coverage is sufficient for one known-theorem application. Cite the classification instead of deriving hypergeometric asymptotics, reproving necessity or running a degree sweep.
SCOPE: The unchanged exact L791 solution, fixed D and p_d below; only a necessary obstruction to all-degree simple positive roots is covered. A positive simplicity theorem, effective first failure degree, parameter retuning and actual/model residual transfer are outside this import.

Use the exact positive L791 solution A,B,C and its exact D=B_J/2,
with all original box and L778 analytic/data/software qualifications.
These parameters are fixed once, using the same central n=0 data;
they are not recomputed as d changes. Define the target family by

    p_d(y)=sum_(j=0)^d (-1)^j binom(d,j)
           (A)_j(C)_j D^j/[A^j C^j(B)_j(D)_j] y^j.

This merely restates the proposed extension of the existing formula;
no root or multiplier property is claimed. The exact parameters, not
rounded centers, must satisfy any imported theorem's inequalities.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
decide whether this fixed matched reference family even supplies the
positive-rooted models a growing-degree transfer would need. A positive
answer would still leave separation, actual residual estimates and mixed
assembly unpaid. A negative answer would park this fixed choice while
allowing degree-dependent parameters and other references.

## Primary theorem and proof scope

Alan D. Sokal, *When does a hypergeometric function pFq belong to the
Laguerre–Pólya class LP+?*, JMAA515(2022),126432,
[published primary text](https://discovery.ucl.ac.uk/10150527/1/Sokal_1-s2.0-S0022247X22004462-main.pdf),
pp.2–3, Theorems3/5 and complete Theorem5 proof; also
[arXiv:2204.01045v1](https://arxiv.org/pdf/2204.01045v1), printed pp.3–4.
For p=q>=1, real numerator parameters outside {0,-1,...} and positive
denominator parameters, these are equivalent: finitely many zeros;
only real zeros; LP+ membership; and reindexing so a_i=b_i+m_i with
nonnegative integers m_i. Zero differences are allowed. Theorem5 includes
p=q, leaving no extra denominator parameters. Its necessity proof imports
Ki–Kim; the multiple-Laguerre discussion is a sufficient direction, not
an independent necessity proof. That discussion's extra pairwise
noninteger-difference assumption is not a classification hypothesis.
The general p<q statement quantifies over extra denominators; it is not
a classification for each arbitrary fixed choice of those extras.

The imported theorem is Haseo Ki and Young-One Kim, *On the Zeros of
Some Generalized Hypergeometric Functions*, JMAA243(2000),249–260,
Theorem3, [DOI10.1006/jmaa.1999.6662](https://doi.org/10.1006/jmaa.1999.6662).
The publisher abstract was accessible through search; original HTML/PDF
requests returned403 and shell retrieval failed DNS. Its original proof
was not read. We accept the precisely identified external classification
stated and used in Sokal's primary theorem and inspected proof; we do
not claim an independent audit of Ki–Kim. No reproof is proposed.

Olga Katkova, Boris Shapiro and Anna Vishnyakova, *Multiplier sequences
and logarithmic mesh*, [arXiv:1010.6052v1](https://arxiv.org/pdf/1010.6052v1),
28 October2010, printed p.2, Theorem3, reaccessed after ready step484
coverage identified this source: for a real sequence alpha_j, the infinite
multiplier property, the entire same-sign real-polynomial compact-limit
property, the type-I product representation up to reflection, and
same-sign hyperbolicity of every binomial symbol are equivalent.
The theorem allows multiplicities. It is not the finite invertible
Theorem4 and does not extend one finite multiplier to an infinite one.
The standard Pólya–Schur theorem is imported, not reproved or audited.

For conventions read Craven–Csordas,
[*Composition theorems, multiplier sequences and complex zero decreasing
sequences*](https://math.hawaii.edu/~tom/mathfiles/czdssurvey.pdf),
printed pp.11–12, Theorem3.3, Definition3.4 and compact-limit passage:
the exponential generating function uses alpha_j/j! and the shift-zero
Jensen symbol uses binom(d,j)alpha_j. This supporting survey does not
replace the precisely cited infinite theorem.

## Comparison and bounded continuation

Inspected Holland [arXiv:2608.08682v1](https://arxiv.org/html/2608.08682v1),
Lemma6.1/equation(57), equations(66)–(71), and Lemma7.3's factorization
and Jacobi hypotheses. Its sufficient regime includes B,D>=K_r d and
C-D>=4d. Failure of sufficient hypotheses is not failure of roots.
No eventual-shift theorem is imported at n=0; L791's direct finite
brackets remain valid independently of this comparison.

The next application must identify the exponential generating function
of the fixed positive ratio sequence with p=q=2, checking D/(AC),
the reflection y -> -y and the exponential factorial. Use the entire
exact L791 radius10^(-15) box and D enclosure to test both matchings of
(A,C) with (B,D); rounded centers are not premises. Failure of the weaker
all-degree real-root premise suffices to reject all-degree simple
positive roots. No sufficiency-to-simplicity inference is licensed.
No such application or integer-exclusion arithmetic was performed here.

Continue if the necessary condition applies and both matchings can be
decided from the exact enclosures. If a matching survives or a hypothesis
fails, stop with that precise limitation. A rejected fixed model would
park only this unchanged choice, leaving degree-dependent models open;
an existential obstruction need not identify a first failure degree.
Separation, actual signed residual control and mixed assembly remain
independent gaps. C792a/b and L793 are contrasts, not assumed root inputs.
No cross-notebook result is used; full matching Mathlib coverage unchecked.

Queries included `hypergeometric 2F2 only real zeros positive parameters
multiplier sequence Ki Kim`, `generalized hypergeometric multiplier
sequences numerator denominator integer differences real zeros`, the
exact Ki–Kim title/DOI, and `Jensen theorem multiplier sequences Jensen
polynomials Laguerre Polya Craven Csordas theorem pdf`. DLMF16.9 was a
lead only. Failed searches/accesses are not an absence theorem.

The precise application is nominated separately in
`2026-11-05-fixed-model-classification-application.md`. No lemmas,
mathematical scripts, DAG or PROOF changed. No justified central signed
mechanism is ready; this is ordinary known-theorem application.
