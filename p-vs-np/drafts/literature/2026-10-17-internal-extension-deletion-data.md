# Internal extension-vertex deletion — proposed source scope

TARGET: Assess whether a supplied set of at most floor(log₂(T+2)) internal extension vertices whose deletion leaves the full signed value graph of treewidth at most two suffices for polynomial-full-bit L037 data.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 279 searched internal-gate conditioning/cutsets, circuit backdoors, noncommutative IPS/treewidth and ABP conditioning; inspected compilation separator cases, CSP backdoor semantics and circuit-aware gate branching. No inspected full L037-data theorem matches; no novelty inference.
SOURCE_EVIDENCE: Jha–Suciu ICDT 2012 Lemma 2.12 complete section 4 proof (PDF p.9); Amarilli–Bourhis–Senellart arXiv:1604.02761v1 Lemma 6.6 complete Appendix A proof (PDF pp.28–29); Ganian–Ramanujan–Szeider arXiv:1610.03298 section 2.1, Definitions 4–5 and Lemma 1 complete proof sketch (PDF pp.4–6); Derkinderen–Lagniez IJCAI 2025 sections 2–3.1, Example 3 and Proposition 1 complete proof (pp.4455–4457). Reuse ready L026/L035/L036/L037/L071/L072 component coverage.
COMPARISON: Sources cover Boolean compilation, retained CSP constraints and gate branching with auxiliary variables or projection. They do not eliminate guessed internal values into original-variable affine graphs with both formal witness identities. L072 covers only independent original inputs; its original-variable indicators cannot be imported unchanged.
GAP: Test explicit compatible-branch reconstruction retaining every deleted definition, exact roots and both L037 formal identities with aggregate full-bit/time bound polynomial in T and 2^k; compatibility and witness-size control are unproved.
REASON: Essential Boolean and local witness components are covered; the remaining difference is a bounded mathematical construction/obstruction test, not a missing essential source. Approve that test after the supervisor's separate readiness approval; no sufficiency theorem is established here.
SCOPE: Proposed target only, retaining L037's signed-AND ER conventions, unchanged F/π/A, all signed and unused roots, exact original/signed roots, faithful representatives, independent explicit graph copies and polynomial aggregate encoding/time in T and 2^k.

The original proposal below was REVIEW_REQUIRED at invocation start. The
completed step-279 review following it supersedes that readiness state.
The completed step-278 audit of L072 is unaffected. This literature-only
review supplies no new lemma, conditioning proof or counterexample.

The exact deletion set would consist of at most floor(log₂(T+2)) positive
extension-AND vertices of the full L071 signed value graph. Original inputs
and NOT vertices are not themselves deleted. Every definition and original
root association remains an obligation in the unchanged proof. Do not
assume the internal values are independent Boolean inputs or that L072's
original-variable indicators still prove the required formal identities.

Essential local inputs for the comparison are L072 and its completed
step-278 audit, L071's exact full graph promise, and L026/L035/L037 receiving
interfaces. Reuse their primary assessments where their hypotheses still
apply. Compare with Attempts 019–021 before pursuing any proposed universal
OBDD or prescribed-output conversion. No cross-notebook result is proposed.
Full matching Mathlib coverage for the proposed change is not checked.

The downstream purpose would be a restricted representation input covering
small internal separators as well as the already handled original-input
case. It would still leave arbitrary ER data, formula-only bounds, W/V/U
and SAT decision/separation unresolved. The literature turn must determine
whether an import, precisely delimited specialization or independently
testable construction/obstruction is justified. If the sources and interface
comparison do not support such a target, narrow or replace it rather than
relabel the completed original-input proof or assume a generic Boolean-zero
witness bound.

## Completed source comparison — step 279

The exact TARGET is unchanged. The main gap is unrestricted SAT decision
or separation; this target concerns only a restricted sufficient input to
L037. Reuse the same-day primary target verification recorded in the ready
treewidth assessment and foundations/01-model-and-target.md. No main-goal
candidate, new mathematical result or certified originality is claimed.

Queries actually issued:

- `Boolean circuits treewidth backdoor internal gates conditioning OBDD cutset`
- `cycle cutset conditioning deterministic nodes Bayesian networks assignments consistency Pearl 1986`
- `noncommutative IPS branching Boolean conditioning internal gates extension variables`
- `"noncommutative" "IPS" "treewidth"`
- `"algebraic branching program" "internal" "conditioning" circuit`
- `"ideal proof system" "backdoor"`
- `circuit internal gate cutset conditioning knowledge compilation consistency gates`

Search hits alone supply no mathematical premise. Bayesian cutset and
relational-circuit hits remain unread leads; none is required for the
bounded test below. The directly relevant circuit-aware paper was read.

**Separator gates are functions, not independent inputs.** Abhay Jha and
Dan Suciu, *On the Tractability of Query Compilation and Bounded
Treewidth*, ICDT 2012, DOI 10.1145/2274576.2274603,
[author PDF](https://homes.cs.washington.edu/~suciu/file38_paper.pdf),
Lemma 2.12, complete section 4 proof, PDF p.9. The separator includes
expression gates, replaced temporarily by symbols. The proof bounds
residual Boolean functions through the descendant relation among these
gates, including the no-descendant base case and recursive case. It does
not assert that the symbols may take independent values consistent with
the original circuit. Corollary 2.14's fixed-width compilation scope is
already assessed locally. These are representation bounds, without
original-axiom free-ring witnesses.

**Algorithmic compiler scope.** Antoine Amarilli, Pierre Bourhis and
Pierre Senellart, *Tractable Lineages on Treelike Instances: Limits and
Extensions*, arXiv:1604.02761v1, 10 April 2016,
[long-version PDF](https://pierre.senellart.com/publications/amarilli2016tractable_long.pdf),
Lemma 6.6 and complete Appendix A proof, PDF pp.28–29. Read the order,
level-wise merging, restricted-copy equivalence test, disagreement gadget
and combined-bag decomposition. For fixed treewidth the compilation time
is polynomial; its exponent depends on the width. The restrictions in
this proof substitute input gates. The manuscript's initial constant-width
shorthand is corrected by its later polynomial pair count, as already
recorded in the ready assessment. It supplies neither an internal-deletion
theorem nor original-axiom witnesses. A width parameter growing with the
input cannot simply be treated as fixed in this theorem.

**Backdoors retain constraints.** Robert Ganian, M. S. Ramanujan and Stefan
Szeider, *Combining Treewidth and Backdoors for CSP*,
[arXiv:1610.03298 PDF](https://arxiv.org/pdf/1610.03298), inspected the
22-page version returned on 2026-10-17, section 2.1, Definitions 4–5 and
Lemma 1, PDF pp.4–6. Restriction deletes incompatible relation tuples and
assigned coordinates, preserving the residual constraints. A strong
backdoor requires every assignment to yield the tractable class. Lemma 1
receives such a backdoor and uses torso bags; its complete proof sketch
handles forget/join nodes and solves residual components at leaf/introduce
nodes. This is a CSP decision/counting theorem, not circuit-value ABP
compilation. No identification of the circuit deletion graph with its
incidence/torso graph, and no L037 consequence, is imported.

**Direct internal-gate branching comparison.** Vincent Derkinderen and
Jean-Marie Lagniez, *Circuit-Aware d-DNNF Compilation*, IJCAI 2025,
pp.4454–4462, [proceedings PDF](https://www.ijcai.org/proceedings/2025/0496.pdf).
Read section 2, section 3.1, Example 3 and Proposition 1's full proof,
pp.4455–4457. Gate branching uses the Tseitin encoding; the discussion
distinguishes projection to original variables from retaining auxiliary
variables. Proposition 1 permits elimination of a gate only when its
output is neither used nor fixed, with its model comparison interpreted
on the remaining encoding variables; an unconstrained erased variable
must not be counted as an extra model coordinate. The proof treats OR
and states the analogous AND case. Its hypotheses do not permit deleting
arbitrary supplied internal gates while forgetting their constraints.
The paper's d-DNNF/query interface supplies no full formal L037-data match.
No claimed general polynomial bound or new correction of the paper is
used here.

## Reused local inputs and failures

Read the exact L026/L037 receiving hypotheses, L035/L036 conclusions,
L071's full-graph and compiler interface, L072's conditioning and complete
indicator/recombination calculation, and history/278's audit record.
Reuse the ready component assessments:

- `2026-10-16-treewidth-two-extension-data.md` and
  `2026-10-17-logarithmic-input-deletion-data.md` in this directory;
- `2026-10-05-obdd-reduced-data.md`;
- `2026-10-07-alternative-abp-commutator-witnesses.md` and
  `2026-10-07-affine-abp-boolean-witnesses.md`;
- `2026-10-07-alternative-affine-abp-certificate-assembly.md`.

The component imports retain their primary scopes: de Colnet–Ordyniak–
Szeider, AI 351 (2026), Proposition 2 for same-order completion;
Raz–Shpilka, author manuscript Lemma 2 Step 1 p.5 for disjoint graph
composition; Li–Tzameret–Wang arXiv:1412.8746v4 Lemma 3.7 p.18 for
formula-input commutator witnesses. Audited L035/L036, rather than an
enlargement of that formula theorem, supply the local arbitrary-ABP
corrections. Their proofs need no new reproof in this literature turn.

L072's indicators use original variables with original Boolean/commutator
axioms. Its interpolated exact input roots use formal identities that
cannot be cited for unspecified internal-value indicators. L026 requires
common-order, all-assignment-correct operand/output diagrams; replacing a
deleted gate by a guessed bit does not by itself discharge that promise
at the deleted definition. L035/L036 correct commutation and Booleanity
of already explicit x-only graphs; neither supplies a generic witness for
every Boolean-zero polynomial. These are applicability differences still
to be tested, not new impossibility results.

Read Attempts 019–021 completely. The HWB stop concerns unrestricted
supplied-proof OBDD width; degree control and prescribed-pair conversion
stops concern identical formal outputs. They do not resolve this changed
structural promise or forbid alternative witnesses. The scoped local
search in the treewidth/deletion notes and history/278 found only the
unassessed internal extension proposal, not a completed duplicate. No
sibling notebook or cross-notebook theorem was read. Existing unfinished
work and all stop evidence remain intact.

## One bounded specialization test

After separate supervisor approval, retain exactly TARGET and test a
compatible-branch construction, or give a precise obstruction to it.
Possible mechanisms to compare within this one attempt are topological
reconstruction of the deleted gates and explicit compatibility guards for
their guessed values. These are proposals, not proved recurrences. No
choice or success of either is assumed by this assessment.

The required threshold is one fixed polynomial in T and M=2^k for the
entire supplied data and deterministic bit time, including every explicit
graph, dictionary, original axiom, root and copied correction. At
k≤floor(log₂(T+2)) this is the desired polynomial-in-T threshold; no
construction achieving it is asserted. Every root must remain faithful
on all original assignments, originals/constants exact, and signs exact
complements. All deleted AND definitions, signed/repeated operands and
unused roots remain obligations for unchanged F/π/A. Supply both formal
identities H_i(x,0)=0 and H_i(x,A)=r_i+r_a r_b using only original Boolean
and commutator placeholders, together with paid pre-substitution degrees.
Branch compilation orders may differ.

Continue only if compatible branch selection and all local defects have
an explicit formal derivation with that fixed-polynomial aggregate bound.
Abandon or narrow the mechanism if it needs independent internal values,
free extension axioms, uncontrolled substitution/path unfolding, a common
order not proved, or a generic Boolean-zero witness premise. A concrete
obstruction should identify the failed interface; failure of a particular
formula is not a disproof of the structural sufficiency target.

The plausible downstream use is restricted input data for L037's already
audited assembly. Arbitrary ER data, formula-only bounds, W/V/U and SAT
transfer remain independent gaps. Mathlib full matching coverage remains
not checked, not absent. No mathematical script or lemma was written;
PROOF.md and DAG.md need no change because no argument changed.

Completed outcome: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED. The new
source comparison supports SPECIALIZE readiness, not the claimed theorem
or certified originality. Mathematical exploration usage remains zero.
