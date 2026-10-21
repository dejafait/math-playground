# Logarithmic large-operand branching depth — proposed coverage

TARGET: Construct polynomial-full-bit L037 data when every ancestry path has at most k AND gates with two operands of syntactic original support greater than k, where k=floor(log₂(T+2)).
CHECKED: 2026-10-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 303 searched exact small-support/operand promises, branching-depth unfolding, multiplicative depth and noncommutative non-skew depth; compared L076–L078 and Attempts 019–020. No inspected full-statement match; this is not a novelty claim.
SOURCE_EVIDENCE: Reused step-299 Bryant §1 equation (1)/§2 Definitions 1–2 and local formal components; reread Raz–Shpilka author manuscript §2.1/Lemma 2 Step 1, PDF pp.4–5 (all leaf/sum/ordered-product cases), and inspected Limaye–Malod–Srinivasan (2016), §1.2 pp.3–4, especially the definition preceding Theorem 1.2.
COMPARISON: Paid formula-to-graph conversion and small-root formal witnesses are covered components; L078 proves only the zero-two-large-gate case. Published non-skew depth counts a different gate condition in a richer arithmetic syntax and supplies no full match for this signed-AND data target.
GAP: Prove or refute polynomial all-root copying under the exact counted-path promise, then justify unchanged small-root H reception and a complete degree/bit/time ledger. No changed presentation bound or data theorem is established by this review.
REASON: Essential component coverage is available; the changed bounded-branching presentation remains an explicit bounded proof test under EXPLORE. Import the graph conversion and reuse audited witness components rather than reprove them.
SCOPE: L037's width-three original CNF, fresh signed-AND ER and actual binary T, all definitions including unused ones, exact original/scalar/sign roots, syntactic reachable-original supports, complete original-axiom dictionaries and pre-substitution degrees; k=floor(log₂(T+2)).

This is an unapproved continuation proposal, not a result of step 302.
An ancestry path follows actual operands from any source node toward
bases, retaining sign vertices. A counted AND has BOTH operand supports
larger than k; the proposed promise permits at most k such vertices on
every path, including paths from unused definitions. Operands and their
left/right positions remain the supplied ones. Support is syntactic,
before simplification. No bound on exact unreduced degree or global
diagram width is assumed.

The main gap remains unrestricted SAT decision/separation, with arbitrary
ER data as the nearer route gap. A successful intermediate construction
could supply L037 on a broader checkable structural class than L078.
It would not make that promise hold for arbitrary ER, give formula-only
bounds, establish W/V/U or every-certificate hardness, or transfer to SAT.

Essential candidate inputs are audited L078, L026's local formal
identities, L071's audited post-compilation graphs, L077's audited
support/diagram components and L037's receiver. L076 is a comparison
only unless its exact degree premise is independently justified.
Reusing these components does not approve a new presentation bound.
No cross-notebook input is proposed; Mathlib coverage is not checked.

The separate review should compare the exact statement and standard
bounded branching, formula unfolding and multiplicative-depth results,
with their noncommutative and signed-AND restrictions explicit. Reuse
the existing paid-formula and small-cone source assessments where their
hypotheses still apply. Check local duplicates and Attempts 019–020;
neither unrestricted diagram width nor general degree-only same-output
conversion is a permitted shortcut. Record any full theorem match and
import it rather than reprove it. Unread discovery leads remain leads.

The test sought after approval is one fixed polynomial in actual T for
all separately written values and formal H witnesses, their degrees,
complete dictionaries and deterministic bit time. Continue only if
coverage supports an explicit presentation and formal-reception test
under this exact promise. Abandon or narrow if it needs unbounded
copying, Boolean-to-formal identification outside its valid subspace or
an extra unsupported unrestricted conversion. No recurrence, new bound
or proof for this changed target is derived or approved in this file.

## Separate completed source comparison — step 303

2026-10-18. LITERATURE_REASON: the counted two-large-operand gates change
L078's single-chain hypothesis; step-299 coverage is reused for unchanged
components, while branching/non-skew-depth terminology needs comparison.
The proposal above is preserved as its historical unapproved scope. This
section records EXPLORE coverage for the exact TARGET, not its proof.
No new lemma, recurrence, bound or mathematical script was produced.

The main gap is still uniform worst-case SAT decision/separation. The
nearer gap is general supplied-ER L037 data. The intermediate target is
exactly TARGET: a construction on the stated logarithmic counted-path
class. Success could extend L078's sufficient class and feed L037; it
would not establish that arbitrary ER has this structure. Formula-only
bounds, W/V/U, every-certificate hardness and SAT transfer stay open.
The official target was checked in step 299 against Cook's currently
linked Clay description, §1 pp.1–2; reuse that precise target record in
`2026-10-17-one-small-operand-affine-abp-data.md` without another retrieval.

### Discovery and primary evidence

Queries submitted included `arithmetic circuits bounded branching depth
skew circuits branching programs weakly skew multiplicative depth
noncommutative`, `arithmetic circuit formal degree branching program size
multiplicative depth unfolding skew circuit`, `"non-skew depth"
noncommutative circuits size theorem`, `"circuits" "logarithmic" "small
support" operands formula`, `"circuit" "formula" "branching depth"
arithmetic`, `"AND" "support" "logarithmic" "formula" circuit`, and
`"noncommutative" "circuit" "unfolding" "depth" formula`.
These yielded related depth and skew results, but no inspected theorem
stating this complete data package. Search silence does not prove novelty.

**Imported component.** Raz and Shpilka, *Deterministic Polynomial Identity
Testing in Non Commutative Models*, undated 16-page
[author manuscript](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
§2.1 and Lemma 2 Step 1, PDF pp.4–5. Read the model, full lemma hypotheses
and all Step 1 cases: leaf edges, parallel sums and ordered serial
products. This gives a linear-size constant/variable-edge graph from an
already paid formula. It works over F₂ and retains mixed degrees and
constants. The full lemma's zero-free-term assumption belongs to its
later homogeneous-output conversion; Step 1 precedes its use. No new
proof of this component is needed. It does not bound DAG unfolding.

**Terminology comparison.** Limaye, Malod and Srinivasan, *Lower Bounds
for Non-Commutative Skew Circuits*, Theory of Computing 12(12), 2016,
[published PDF](https://theoryofcomputing.org/articles/v012a012/v012a012.pdf),
§1.2 pp.3–4. The definition preceding Theorem 1.2 counts non-skew
multiplication gates on input-output paths; skew means a scalar/variable
operand. Our cutoff uses syntactic Boolean support and permits entire
small-support cones. Their arithmetic syntax also permits general sums.
Thus the definitions do not identify the two promises. Read Theorem 1.2
as a lower-bound comparison, not an upper-bound construction or an
obstruction for this target; its proof is not imported. The same section's
mixed-side/cancellation warning prevents a skew-to-ABP shortcut. No
homogeneity or degree conclusion is transferred to our representatives.

Bryant (1986), §1 equation (1), §2 Definitions 1–2, author-restored PDF
pp.3–4, remains reused Boolean table/diagram coverage from step 299.
Its Boolean semantics alone does not identify arbitrary free polynomials.
The formal comparison instead uses the already proved local L026 and
L071 interfaces, with their ordered-multilinear hypotheses retained.

Uninspected leads include Grinchuk's *On circuits of functional elements
of finite depth of branching* and Ganardi–Jeż–Lohrey's *Balancing
Straight-Line Programs*. Only discovery records/snippets were seen;
neither supplies evidence for this target or an essential input. Their
titles do not identify our support-sensitive path promise. No dependent
claim is deferred to an inaccessible source.

### Local reuse, duplicates and bounded next test

Read L078's paid-tree and local-reception proof, L076's exact T+D
hypotheses/conclusion, L037's full receiving hypotheses, L077's support
scope, and L071's explicit value/K/W graph and formal-identification
passages. Also checked the prior step-299 assessment and work note,
L078 work note, the targeted recent assessment matches, and Attempts
019–020. No existing local result is asserted to cover the changed
branching bound. L076's polynomial in T+D cannot be called a polynomial
in T here; L077 requires every whole root small. L078's audited
single-chain count cannot simply be quoted for branching roots.

Attempt 019 stops universal common-order diagrams; no diagram for a
large root is proposed. Attempt 020 stops a general same-polynomial
arithmetic-circuit conversion, with unrestricted sums; it neither proves
nor refutes this restricted target. Both stops remain preserved. No
cross-notebook theorem was read. Mathlib coverage is **not checked** for
the full target or a matching support-sensitive unfolding theorem.

One bounded proof attempt is now covered: retain L078's small-cone
cutoffs, examine the large-node occurrence structure under the stated
path promise, and try to pay its complete formula presentation before
using the imported graph conversion. Separately check applicability of
L026/L071 to each small-output definition using the exact chosen
signed representatives. Do not assume a bound for large-root diagrams,
exact unreduced degree or arbitrary mixed-side skew circuits. The target
remains unchanged; no recurrence or polynomial bound is approved here.

Continue only with one fixed polynomial in actual T paying all separate
roots, both signs, unused definitions, ordered/repeated operands,
formal H identities, pre-substitution degrees, complete repeated
original-axiom dictionaries and deterministic bit time. Abandon or narrow
this construction if copying cannot be controlled under the exact
promise, the small-root interface mismatches, or it needs Boolean-to-free
identification outside the ordered multilinear subspace. A failure of this
attempt would concern this construction, not unrestricted ER or SAT.
EXPLORE authorizes the test, not its success or certified originality.
