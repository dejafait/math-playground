# Shared formula-IPS binary-bound audit

Research audit dated 2026-10-04. The target is the exact previously approved binary-bound action in `drafts/literature/2026-10-03-shared-homogeneous-ips-ef.md`; no source scope is changed and no additional literature work is needed. Existing formula-IPS assembly, scripts and inactive routes are preserved.

The main gap remains a polynomial SAT algorithm or an unconditional separation. The intermediate test is whether L018 really constructs an original-CNF EF/ER refutation with one fixed polynomial bound in the complete supplied data. Its downstream use is to screen this certificate fragment out of prospective ER-hard families. An unproved circuit identification, residual evaluation hypothesis, exponential expansion or invalid final conversion would block that screen. L016 does not settle arbitrary degree; L017 alone retains its evaluation definitions. The existing stopping evidence for decision-to-proof transfers still applies.

## Reasoning saved before the audit is complete

The finite closure algebra has the correct orientation: `K E_0=K+I`, `G_b=E_b K`, and `h_D X K=0` follows from support below the diagonal, without requiring `h_D=0`. Combining `r=e_0 K+r X K` with this checked constant identity yields the triangular graph recurrence. These observations need a proof-cost audit rather than another numerical PIT test.

The vulnerable encoding point is L017's prescribed flat recurrence, an XOR of individual `p_u AND x_b` terms. L018's written matrix recurrence can instead be implemented as an XOR over b of `(XOR_u h_u) AND x_b`. A choice of XOR parenthesization cannot make those circuits identical. At layer one there may also be `1 AND x_b` gates. Definition substitution correctly proves the flat evaluator zero; identifying that evaluator with the factored matrix circuits requires explicit constant reduction and distributivity, not just structural congruence. The audit will specify both encodings, prove their equality layer by layer, and charge the full rooted substitution circuits. A finite syntax check will reject substitution of factored values into flat gate definitions and confirm the repaired substitution has no non-assignment inputs.

This saved reasoning was provisional. The completed audit below fixes this particular identification gap; it does not produce a complete P-versus-NP candidate.

## Completed audit and decision

The correction is in [L018](../lemmas/L018-shared-formula-ips-polynomial-er-simulation.md), equation (15) and its definition-discharge paragraphs. Define the flat evaluator exactly as prescribed by L017. Use its actual rooted gate circuits in the substitution, so each elementary definition is reflexive. Its output is the flat a_k(t). A separate layer induction, using constant reduction, AND congruence, distributivity and XOR reassociation, proves a_k(t) equivalent to the factored h_k(t). This fixes an omitted proof step in the written encoding argument. Structural congruence remains appropriate only for copies with identical connective structure. The theorem's hypotheses and claimed conclusion do not change.

The repair costs polynomially many local steps: at most nN flat terms in each of DN coordinates, with all preceding-layer circuits treated as shared references. If M is the sum of the evaluation-gate counts, with the input variables and constants charged for each component, then M=O((T+2)^5). Charging every gate's complete rooted substitution DAG separately costs at most O(M²) nodes and O(M²(T+log₂(M+T+2)+1)) binary bits. This composes with the already stated polynomial circuit substitution and proof conversion costs. It never expands a rooted circuit into a tree.

The other assembly checks found no new gap within the screened hypotheses:

- Constant closure is finite because E_0 is strictly triangular. The checked coefficient equalities are expanded into local circuit proofs; the computation of K is not a supplied symbolic identity axiom.
- Support below the diagonal kills the next transition from h_D, rather than the possibly nonzero h_D itself. Summing only the D recurrences is therefore valid. The resulting triangular graph equations uniquely identify the rows by coordinate induction.
- Tree occurrences are disjoint. Only each subtree's source has incoming edges from outside it, justifying the leaf/addition/multiplication identification with its evaluation without a monomial expansion.
- L017's output-zero premise is formal noncommutative zero. The independent Boolean-zero commutator is not admitted by that premise. All original evaluation names are substituted; the proof's extension variables have already been eliminated by EF-to-CF conversion.
- The zero proofs are combined while the assignment stays free. Clause falsity polynomials are derived zero under the original conjunction; Boolean and commutator polynomials use local tautologies. Only the final negated-CNF formula is passed to CF-to-EF conversion. The ER conversion introduces fresh definitions and retains the original clauses as original premises.
- Degree zero, an empty alphabet and an original empty clause have the separate ground or immediate-contradiction treatments stated in L018. All matrix entries, copied axiom occurrences, sparse names and proof references are explicitly polynomially bounded. No certificate search is claimed.

`PYTHONDONTWRITEBYTECODE=1 python3 scripts/shared-abp/check_definition_discharge.py` passed six cases and 19 assignment checks. It detects the nonreflexive substitution already for the scalar-one first layer, and makes all definitions reflexive with the repaired flat substitution. Five nonempty cases reject a changed AND definition. The dense layered case has 2,537 original gate definitions; charging all their rooted DAGs separately counts 223,033 node occurrences. A fully unfolded root would have 178,267,485,250,079 nodes. These numbers illustrate the representation distinction; the uniform bound is the informal estimate above. Neither this syntax check nor its finite output comparisons verify a CF/EF/ER proof string.

This step is ADVANCE / RESEARCH / REPRODUCTION for a local mathematical proof repair, not a new theorem or an originality claim. The informal forward upper-bound screen survives the audit with its missing encoding derivation supplied. The main SAT gap does not narrow to a resolved separation. In particular, the implication from short formula-IPS certificates to short ER proofs does **not** imply that formula-IPS certificate lower bounds would rule out all ER proofs. Whether a suitably bounded reverse translation is known is a distinct, unreviewed target; it will be assessed before any dependent calculation. Further repetitions of this audit would not count as advances.

## Mathlib

Coverage: **not checked** for this audit or the full simulation. The unchanged assessment preserves the named sources, versions and direct links for supporting representations, witnesses and proof operations; it records no matching full-statement theorem or originality certification.
