# Original-input deletion with a counted-path residual — source comparison

TARGET: Construct polynomial-full-bit L037 data for a supplied logarithmic original-input deletion set whose every Boolean restriction satisfies L079's counted-path promise.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 307 searched noncommutative IPS/Shannon/restriction, branching backdoors/compilation and arithmetic non-skew-depth terminology; compared L072 construction and step-278 audit, L079 construction and audit interface, L037 hypotheses, ready component assessments and Attempts 019–020. No inspected full-statement match or originality inference.
SOURCE_EVIDENCE: Freshly read Darwiche–Marquis JAIR 17 (2002), Definitions 5.3–5.5 and Shannon discussion p.241, Proposition 5.1 and conditioning proof pp.242,256; reused Bryant restriction/table coverage, Raz–Shpilka Lemma 2 Step 1 and assessed L026/L035/L071 interfaces at the precise locations below.
COMPARISON: Known conditioning is Boolean; L072's formal recombination receives explicit branch values and local witnesses, but its whole theorem requires residual treewidth two. L079 supplies a different candidate branch construction, but its whole theorem retains an ER proof and its own T-derived cutoff. Component specialization is needed; no whole-theorem import covers the combination.
GAP: Justify L079's circuit-only specialization with the original T/cutoff, constants and original-alphabet branch relations; then apply only L072's formal recombination component and replace its multilinear degree ledger by a bound for the actual branch graphs.
REASON: Essential source coverage is adequate for one separate bounded proof attempt on the unchanged target. This assessment approves that attempt, not the combined theorem, a new bound or a formal identity.
SCOPE: Same L037 width-three CNF, fresh signed-AND ER, actual original T and all roots including unused ones; k=floor(log₂(T+2)) remains fixed. A supplied set of at most k original inputs is replaced by assignment scalars in every branch; recomputed syntactic supports over the remaining originals must satisfy L079's at-most-k two-large-operand gates per path, with the same cutoff k. Retain the original ER proof, axiom dictionary and sought original-alphabet formal identities.

This file proposes a mathematical target for separate source comparison
only. It does not assert
that branchwise data can be recombined or that any new class satisfies
the data bound. The exact treatment of original fixed inputs, original
Boolean/commutator placeholders and the unchanged proof must be checked;
Boolean agreement of branch values alone would not supply formal H.

The main gap remains uniform worst-case SAT decision/separation and the
nearer gap remains L037 data for arbitrary supplied ER. A positive answer
could make a restricted data receiver tolerate a small set of original
inputs whose presence obstructs the counted-path promise. This does not
assert such a set for arbitrary ER or a formula-length-only bound.

For the separate review, first compare the exact L072 input-deletion
recombination statement/proof and L079's audited receiver, then search
for matching or stronger results under standard restriction/Shannon
recombination terminology. Reuse ready primary coverage where hypotheses
remain unchanged. Check local duplicates and Attempts 019–020 without
reopening their unrestricted claims. L072 is a proposed input whose
scope still needs inspection, not a theorem already applied here.

Continue only if the assessment identifies coverage for every original-
alphabet formal relation and one polynomial in original T, including
all independently written branches, roots, degrees, dictionaries and
bit time. Otherwise record the precise missing input and park this
dependent construction or select an independently testable target.
No branch construction, bound, identity or new lemma is derived in this
proposal. Arbitrary ER data, formula-only bounds, W/V/U, every-certificate
hardness and SAT transfer remain unresolved. No cross-notebook input;
matching Mathlib coverage is not checked.

## Completed separate comparison — step 307

2026-10-18. LITERATURE_REASON: the saved target changes L072's residual
treewidth hypothesis to L079's support-sensitive counted-path hypothesis.
Reuse ready coverage for unchanged components; this is its first separate
source comparison. The proposal above is preserved as the pre-review
record. No new mathematical result, lemma or mathematical script is
produced in this literature-only step.

The main gap remains uniform worst-case SAT decision/separation; the
nearer gap is arbitrary supplied-ER L037 data. The intermediate target is
exactly TARGET. Its plausible use is restricted data construction robust
to a supplied small set of original inputs. No theorem supplies such a
set for arbitrary ER. Reuse the exact official target/version checked
in step 299, recorded in
`2026-10-17-one-small-operand-affine-abp-data.md`, and
`foundations/01-model-and-target.md`; no changed main target is proposed.

### Primary evidence and discovery limits

Adnan Darwiche and Pierre Marquis, *A Knowledge Compilation Map*, JAIR
17 (2002), 229–264, DOI 10.1613/jair.989,
[published PDF](https://www.cs.cmu.edu/afs/cs.cmu.edu/project/jair/pub/volume17/darwiche02a.pdf):
read Definitions 5.3–5.5 and the Shannon discussion, printed p.241,
Proposition 5.1 p.242, and its conditioning proof p.256, including NNF
constant substitution, preservation cases, and decision-node child
bypass. These are Boolean operations. They do not give free-associative
identities or original-axiom witnesses. Reuse the order-sensitive closure
comparison on pp.259–260 already inspected in
`2026-10-17-logarithmic-input-deletion-critical-audit.md`; no arbitrary-order
OBDD merge is licensed.

Reuse Randal E. Bryant, IEEE TC C-35(8) (1986), 677–691,
[author-restored manuscript](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf),
§1 equation (1), §2 Definitions 1–2, and §4.4, manuscript pp.3–4,15;
the exact inspected cases are recorded in the same deletion assessment
and `2026-10-17-logarithmic-large-branch-depth-data.md`. Reuse Ran Raz
and Amir Shpilka, *Deterministic Polynomial Identity Testing in Non
Commutative Models*, undated 16-page
[author manuscript](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
§2.1 and Lemma 2 Step 1, pp.4–5: paid formula leaves, parallel sums,
ordered serial products. Only this conversion component is imported;
the later homogeneous conversion's zero-free-term condition is not
silently applied. No reproof is needed for either source component.
L035, rather than the formula-input LTW Lemma 3.7, supplies the audited
arbitrary-affine-graph commutator interface.

Fresh queries: `"noncommutative" "Shannon" certificates IPS`,
`"branching" "backdoor" "circuits" compilation conditioning`,
`"arithmetic circuits" "non-skew depth" restrictions`,
`"noncommutative" "IPS" "restriction" "Boolean"`, and
`"knowledge compilation" "backdoor" "branching" circuits`.
Results included already assessed non-skew lower bounds and a lead to
backdoor-decomposable monotone circuits. Only discovery descriptions were
seen for the latter and the STACS 2020 Hankel-matrix result; neither is
an inspected input or an essential missing source. No full matching
theorem was established by this search. This is not a novelty claim.

### Local interface comparison and bounded proof scope

Read L072 through its complete construction/ledger and step-278 audit;
L079 through its complete construction/ledger and its audit's framing;
L037's exact receiving hypotheses; the ready L072-audit and L079-data
assessments; and Attempts 019–020. No duplicate combined theorem was
identified in those specific local paths. No sibling notebook was read.

L072's branch generation uses a fixed-width compiler. Its later
indicator, exact-root and ordered recombination arguments instead receive
explicit x-only branch graphs and J satisfying its equation (1).
In particular equations (5)–(7) do not stipulate a common order across
branches or a treewidth bound on those graphs. Its closing p(T) ledger
must cover all supplied branch data/time. Its stated d=max(1,n), however,
uses branch multilinearity and cannot be imported for L079's large-root
products. These are comparisons of existing statements/proofs, not a
proof that the changed branch supplier meets the interface.

L079's whole theorem cannot simply be applied to a putative restricted
ER refutation: no such refutation is supplied, and its cutoff is defined
from its input length. The later proof attempt must justify its
value-DAG/local-relation components on scalar-replaced inputs, retaining
original T and k throughout. It must explicitly map subset-variable
Boolean/commutator placeholders into the unchanged A. L079's local
relations use no original clause placeholders; exact originals, signed
constants and absent-variable zero bases still need exact reception.
Do not assume L072's sharper degree conclusion survives.

One bounded proof attempt is approved for exactly TARGET. Test whether
the existing L079 components supply every branch's required explicit
data with one original-T polynomial, and whether L072's already proved
recombination component then receives them. Pay all separate branches,
roots/signs/unused definitions, indicator pairs, L035 calls, dictionary
copies, degrees and bit time. Include empty deletion, all-input deletion,
constant branches and repeated/complementary operands. Keep scalar
replacement and syntactic supports as specified in SCOPE: no uncharged
Boolean simplification, minimal-support oracle or changed ER proof.

Continue only if those exact interfaces and a fixed polynomial in
original T can be proved. Abandon or narrow this construction if it
requires a common order on large roots, a general circuit-to-ABP
conversion, Boolean agreement in place of formal J, or a smaller
branch-length cutoff without justification. Attempts 019–020 remain
stops on those unrestricted shortcuts, not bans on this restricted test.
No bound or identity for the combined target has been derived here.
Arbitrary ER data, formula-only bounds, W/V/U, every-certificate hardness
and SAT transfer remain unresolved. Mathlib coverage is not checked.
