# Degree-dependent central Jacobi regime — bounded algebraic test

TARGET: Determine whether L791's exact central q_0,q_1,q_2 admit positive degree-dependent parameters with free D_d and A_d>B_d+d-1, C_d>D_d+d-1 for arbitrarily large integer d, by one bounded algebraic feasibility or finite-cap argument valid for both numerator pairings.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step597's completed changed-quantifier review in 2026-11-05-degree-dependent-central-jacobi-feasibility.md, including exact-system searches, fixed-tuple/residual stops and optional unread leads. No direct central feasibility result was established by that bounded search; no originality claim.
SOURCE_EVIDENCE: Holland https://arxiv.org/html/2608.08682v1 (49),(52),(66)–(74), Lemma6.2/full proof; Martinez-Finkelshtein–Morales–Perales https://arxiv.org/pdf/2309.10970v3 Propositions2.7(iii)/2.17, Theorem3.1 and Proposition4.15(ii)/(R2), pp.11,15–16,33–34; https://dlmf.nist.gov/18.5.E7, https://dlmf.nist.gov/18.3#T1 and https://dlmf.nist.gov/18.2#vi. Primary statements and essential matching/mesh/factorization cases reviewed in step597; step474's broader root comparison reused.
COMPARISON: Conditional matching and sufficient root interpretation are known; exact central feasibility with four free positive parameters and unbounded degree remains a local algebraic specialization. L817's fixed-tuple obstruction has different quantifiers; broader continuous/discrete root regimes remain outside the proposed stop.
GAP: Establish unbounded feasibility or a necessary finite degree cap for the displayed strict regime using L791's exact data. Root-separation rates, actual signed residual bounds and mixed assembly remain independent gaps even if feasibility survives.
REASON: A single exact algebraic test can decide whether this sufficient reference regime deserves further work without repeating a fixed-model classification or solving a residual problem. Cite the general inputs; derive only the identified feasibility difference.
SCOPE: One bounded algebraic attempt, no degree sweep or parameter-family redesign. All four parameters may depend on degree; D=B_J/2 and L791's fixed solution box are not constraints. This newly written ready continuation awaits the supervisor's separate next-turn approval; no result is established in step597.

Read the completed [source comparison](2026-11-05-degree-dependent-central-jacobi-feasibility.md),
especially its exact-scope and applicability sections. Retain the actual
completion/normalization/evaluator/software contracts of L018/L021/L776/L778
and L791. The central q values, defined from gamma(j)=8*4^j*j!*a_j,
remain fixed, with the full conservative enclosures reproduced there.
Use enclosures conservatively; an interval obstruction valid for their
whole product includes the correlated actual data. Existence for
arbitrary independently chosen interval values is not actual existence.
No new coefficient evaluator or numerical data source is needed.

For k=0,1,2 use exactly

    q_k=(A_d+k)(B_d+k+1)(C_d+k)(D_d+k+1)
        /[(A_d+k+1)(B_d+k)(C_d+k+1)(D_d+k)].

Require A_d,B_d,C_d,D_d>0, A_d>B_d+d-1 and C_d>D_d+d-1.
Include the pairing obtained by exchanging the two numerator parameters;
the equations are symmetric in them. Here d is polynomial degree and
the shift stays zero. Free tuples for arbitrarily large d, rather than
one fixed tuple working for all d, are the question. The exact matching
identity is a cited conditional input, not a new existence theorem.

Seek one proof or exact rational inequality certificate deciding whether
arbitrarily large degrees are possible. A necessary bound obtained from
fewer than all three equations may suffice for an obstruction; justify
why it applies to every admissible solution and both pairings. If instead
constructing solutions, prove exact equations and strict hypotheses for
unbounded degrees; asymptotic approximate residuals do not establish
existence. Do not infer a theorem from a finite parameter search.

Bound the work to one algebraic mechanism and its necessary exact
comparisons, with no precision ladder, degree sweep, alternative root
region or extra matching indices. If a script is necessary, retain full
rational evidence on disk and print actual/required bounds and failures;
no script is required merely to create an artifact. An inconclusive
attempt records the precise remaining inequality or existence gap.

Continue this regime only if feasibility survives a necessary test or
an exact unbounded family is established. A finite cap stops only this
strict sufficient regime; it is not global hypergeometric nonexistence,
an actual-Xi nonreal root or a disproof of RH. Proposition4.15(ii)'s
weaker continuous inequalities, its discrete extensions and direct root
certificates are outside the proposed conclusion. No uniform separation
or critical-value estimate is supplied merely by per-degree simplicity.

Preserve L817's fixed-family stop, L791/L792 finite successes and the
distinct limits in C792a/b and L793. No cross-notebook input. Full matching
Mathlib coverage remains unchecked. This is conventional specialization,
not an approved new creative mechanism for the central signed gap.
