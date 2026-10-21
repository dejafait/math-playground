# Diagonal-augmented matrix IPS interface — completed source comparison

TARGET: Assess diagonal-augmented upper-triangular matrix evaluation as a replacement IPS interface for L048, checking satisfiability preservation and common-order roABP representation.
CHECKED: 2026-10-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 149 searched matrix/noncommutative IPS, diagonal augmentation, triangular Boolean matrices and ABP/roABP separations; inspected primary passages listed below and reused step-145 coverage; no full matching interface theorem was established.
SOURCE_EVIDENCE: Reused Forbes–Shpilka arXiv:1209.2408v2 Construction 4.1 and Lemmas 4.2–4.5; inspected FSTW ToC 17(10) (2021) Lemmas 3.6–3.7/Fact 3.8 pp.19–20, Proposition 6.21 and Corollary 6.22 with complete proofs pp.65–66; Li–Tzameret–Wang arXiv:1412.8746v4 Definition 1.2/footnote 7 p.6; additional qualified comparisons below.
COMPARISON: The positional theorem uses strictly upper-triangular shifts and layer relabelling, not repeated diagonal variables; the known all-field any-order roABP obstruction supplies a sharper representation test, not a counterexample on valid L048 certificates or an IPS transfer.
GAP: Satisfiability equivalence, a consistent full-placeholder substitution proving both matrix identities, and polynomial complete-size common-order roABP entries are still unproved for this proposal; realizing the known obstruction inside valid certificate entries is a separate local obligation.
REASON: Essential source-scope comparison is complete without a source blocker; narrow the next mathematical target to diagonal-entry representation, since the inspected all-field obstruction gives a discriminating test rather than another scalar audit.
LITERATURE_REASON: Changed receiving system from the exhausted fixed scalar interface to diagonal-augmented matrices; existing primary coverage does not assess diagonal variables, substituted axiom entries or common-order roABP entry complexity.

## Original proposal at invocation start (preserved)

Use L048's full Hypotheses, including occurring originals, all A positions, explicit affine graphs, formal identities and complete dictionaries. L050 and Attempt 023 supply only the reason to change receiving systems. No cross-notebook input is proposed. Preserve Attempts 018/020/021/022/023 and the parked FSTW import.

Compare the following concrete candidate, without asserting its properties. For positive D bounded polynomially in the supplied graph length, let Z_i,D be Construction 4.1's (D+1)-dimensional positional shift matrix and propose X_i=x_i I+Z_i,D, with new commuting scalar diagonal variables x_i. For each axiom position a, let T_a=t_a I+U_a, where U_a has an independent commuting variable in every strictly upper-triangular entry. All variables, matrix entries and dictionaries are explicit and distinct except for the repeated diagonal variable. Candidate receiving equations are every entry of A_a(X)=0, retaining Boolean and commutator positions as well as clauses. Candidate certificate data are the entries of C(X,T). Placeholder zero means all t_a and all entries of U_a are zero; axiom substitution would have to identify a consistent substitution for this same full placeholder package. Do not silently omit diagonal entries, constant entries, zero entries or the identity matrix output.

The desired comparison asks whether published results cover (a) equivalence between satisfiability of these entry equations over an algebraic closure of F₂ and satisfiability of the original Boolean CNF, (b) both formal IPS identities with output I, and (c) one polynomial bound in 2+|F|+|C|+|A|+D on complete explicit common-order roABPs for all certificate entries together. Here common order means one order of all independent scalar original and placeholder variables, shared by all entries; the order may depend on the supplied package. Distinguish an unrestricted arithmetic ABP bound from a read-once oblivious bound. Neither is assumed to follow from matrix substitution. Identify whether a cited theorem instead requires different matrices, a restricted certificate domain, a larger field, or a different receiving class.

Reuse exact primary passages already inspected for the unaugmented map. Search the changed statement, standard matrix-IPS and roABP terminology, stronger results and obstructions; inspect primary hypotheses and relevant proof cases before larger extracts. The present proposal is not evidence that any of (a)–(c) holds or fails. No matrix calculation, new lemma or mathematical script is authorized until separate coverage is ready. If known results already decide the proposed interface, record precise citations and qualifications rather than planning a reproof.

Plausible downstream use: a satisfiability-preserving matrix receiver with controlled entry representations could provide a different comparison interface after the scalar stop. Continue toward a bounded mathematical test only if the comparison leaves a concrete independently testable obligation with adequate sources. Abandon or narrow this candidate if a known mismatch defeats satisfiability preservation or the required entry class; do not repeat the scalar audit. Even a positive interface would leave F₂ every-certificate hardness for this receiving system, hardness preservation, general ER-to-ABP representation and unrestricted SAT transfer unresolved. Mathlib coverage is not checked. This proposal is REVIEW_REQUIRED, not a newly approved continuation or a claim of novelty.


## Completed source comparison — step 149

This invocation performed one literature comparison, classified NOVELTY_UNCHECKED with outcome EXPLORATION. It established source coverage for a concrete further test, not properties (a)–(c), a new lemma, or an obstruction on certificates. The original proposal above is preserved as historical scope; its REVIEW_REQUIRED label describes its state at invocation start. The completed decision is the single-line EXPLORE field.

### Primary statements and essential cases actually inspected

Reuse step 145's Forbes–Shpilka construction/proofs exactly as recorded in `drafts/literature/2026-10-10-position-encoding-ips-substitution.md`, including its version/date conventions. Their matrix indices strictly advance on every nonconstant symbol; Lemma 4.5 assigns symbols by homogeneous layer. Repeated diagonal scalar variables and full triangular placeholder matrices are changed hypotheses, not a specialization already proved there. No hitting set is imported.

The new load-bearing source is Forbes–Shpilka–Tzameret–Wigderson, [*Proof Complexity Lower Bounds from Algebraic Circuit Complexity*, Theory of Computing 17(10), 2021](https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf). Read Lemmas 3.6–3.7 and Fact 3.8, printed pp.19–20: univariate matrix-product normal form, coefficient-dimension characterization, and constant-specialization closure in the induced order. Read Proposition 6.21 and Corollary 6.22, printed pp.65–66, including both complete proofs. For any field and constants α_ij, every nonzero multiple of ∏_(i<j)(x_i+x_j+α_ij) requires roABP width at least 2^floor(n/2) in every order. The proof embeds a matching across an arbitrary balanced partition and works over a fraction field; Proposition 6.21 uses extremal diagonals and the sparsity result Corollary 6.13. Its statement and relevant translation proof were inspected on p.60. No characteristic lower bound or Boolean-function interpretation is imposed. The journal's headings are **Proposition** 6.21 and **Corollary** 6.22, although its proof cross-references say “Theorem 6.21.” Do not substitute older manuscript numbering. No source theorem is reproved or imported into the argument this turn.

Li–Tzameret–Wang, [*Characterizing Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4](https://arxiv.org/pdf/1412.8746v4), Definition 1.2 and footnote 7, printed p.6, were read with the surrounding qualifications. The definition retains formal free-algebra identities and Boolean/commutator axioms; it measures formula size. The footnote concerns existence of 0–1 solutions in algebras, not this parametrized matrix receiver or entry roABP bounds. It cannot be cited as the missing interface theorem.

Grigore Călugăreanu, [*Central stable range one for elements and rings*, São Paulo Journal of Mathematical Sciences 19:26 (2025)](https://math.ubbcluj.ro/~calu/centralSr.pdf), §3.3, p.8, states that the constant-diagonal triangular ring over a division ring is local with zero-diagonal radical; Proposition 3.5 and its short proof concern central stable range one. That is supporting ring background, not a proof of the proposed satisfiability equivalence. In particular the coefficient **polynomial** ring before scalar assignment is not asserted to be a division ring. No idempotent specialization or solution correspondence was derived here.

Two additional search leads were checked sufficiently to delimit relevance. Andrews et al., [*On Closure Properties of Read-Once Oblivious Algebraic Branching Programs*, ITCS 2026, paper 9](https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/html/LIPIcs.ITCS.2026.9/LIPIcs.ITCS.2026.9.html), §2.1/§2.3 and Theorem 12, gives an evaluation-dimension criterion with an infinite-field converse; its advertised symmetric-composition separation has characteristic-zero hypotheses. Those statements were inspected, not their separation proofs, and are not essential inputs. Use the all-field coefficient criterion above for an F₂ test instead.

Hakoniemi–Limaye–Tzameret, [*Functional Lower Bounds in Algebraic Proofs: Symmetry, Lifting, and Barriers*, ECCC TR24-079, retrieved 64-page report](https://eccc.weizmann.ac.il/report/2024/079/download), p.6 “Noncommutative approach” and §2.4.1 pp.19–20, were inspected. The matrix discussion concerns ranks associated with noncommutative proofs, not an evaluated triangular-matrix IPS system. Its ABP/roABP correspondence cites Forbes–Shpilka rather than adding the missing substitution theorem. Other lower-bound proofs in this report, the finer-ROABP-subclass paper and the thesis search hit remain unread leads; none is claimed to settle this receiver or needed for the selected test.

### Comparison and remaining obligations

For (a), the scalar solutions of **all** entry equations over the algebraic closure of F₂ must be compared with original Boolean assignments. Entry assignments and actual matrices, the diagonal variables and positional shift variables, and the commutator equations must all be retained. The ring background does not by itself provide that comparison. No direction of equivalence is recorded as proved.

For (b), a proposed evaluation must respect ordered products, map the free-ring unit to I, and provide one consistent substitution of every independent t_a and every U_a entry to the corresponding complete A_a(X) package. Repeated diagonal entries must use the same scalar image. Placeholder-zero must remove that whole package. Formal identities, not Boolean evaluations or separate homogeneous scalar encodings, are required. This basic applicability argument is not supplied by the source's PIT theorem and is left for mathematical work.

For (c), an unrestricted arithmetic ABP representation does not establish a read-once oblivious representation. The imported positional proof cannot charge repeated diagonal reads as separate independent variables while calling them the same x_i or t_a. Common order permits choosing a permutation, but only one read per independent scalar variable. The new all-order, all-field source obstruction is consequently a relevant test ingredient. It does **not** show that an actual valid L048 certificate entry realizes that obstruction. Building such a certificate, checking both free-ring identities and the complete input ledger, identifying its diagonal entry, and proving a width-preserving specialization/coefficient extraction remain unperformed.

No complete matching interface theorem was established by this bounded search. This does not establish novelty or absence of one. No essential source access remains blocked for the selected representation test. Satisfiability and identity work is parked while that independently testable obligation is examined; failure of the requested universal entry bound would suffice to stop the full proposed interface, without settling either other property.

### Search record and duplication checks

The twelve actual queries were:
- `"noncommutative" "IPS" "matrix" upper triangular`
- `"read once oblivious" "diagonal" noncommutative matrix`
- `"x_i" "upper triangular" Boolean polynomial matrix idempotent`
- `"ROABP" "exponential" "ABP" any order lower bound determinant`
- `"IPS" "matrix substitution" noncommutative`
- `"upper triangular" idempotent "constant diagonal" field`
- `"ROABP" "ABP" "exponential" "any variable order"`
- `"noncommutative IPS" "matrices"`
- `"IPS" "upper triangular"`
- `"idempotents" "local ring" "upper triangular" "constant diagonal"`
- `"diagonal" "matrix" "non-commutative IPS" Forbes Shpilka`
- `"diagonal augmentation" "roABP"`

Only primary passages or the explicit reused assessment support the comparison; snippets and secondary copies are discovery leads. L048's actual Hypotheses, L050's scope, Attempt 023, history/145 and the step-144 all-certificate assessment/Attempt 022 were read. Narrow searches of the step-145 work and Attempts 020/021/022/023 found no recorded diagonal-entry realization. Attempts 020/021 stop different prescribed-output converters; Attempt 022's IPS lower-bound field mismatch must not be transferred to the separate all-field polynomial theorem. Attempt 023 remains an exact scalar stop. Attempt 018 and unfinished work are preserved. No cross-notebook input is used.

### Decision, threshold and continuation

The main gap is still unrestricted SAT decision/separation. The chosen intermediate test is whether valid L048 certificates themselves defeat a universal polynomial complete-size roABP bound for the proposed diagonal-augmented entries. Seek an explicit full family with a superpolynomial lower bound compared with Q=2+|F|+|C|+|A|+D, using the known theorem rather than reproving it. A positive construction of small general ABPs alone does not meet that threshold. Continue this representation target only upon a valid-certificate realization or a demonstrated obstruction to the proposed realization; do not promote failure of one padding device to a receiver-wide lower bound.

A negative representation result could screen out this full receiver before pursuing its hardness transfer. A successful polynomial entry construction would justify returning to satisfiability and formal identities, with separate coverage as needed. Both outcomes leave every-certificate hardness, certificate selection, general ER-to-ABP representation and unrestricted SAT transfer unresolved. Mathlib coverage of the exact interface and the new polynomial theorem is not checked; no absence is asserted.

The next narrowed target is saved in `drafts/literature/2026-10-11-diagonal-entry-roabp-obstruction.md`. Its new SPECIALIZE assessment proposes a subsequent mathematical application; it receives separate approval next turn. No new mathematics is derived or validated in this literature invocation. Mathematical exploration usage remains 0 since step 146. PROOF.md, DAG.md, lemmas/ and scripts/ are unchanged by this step.
