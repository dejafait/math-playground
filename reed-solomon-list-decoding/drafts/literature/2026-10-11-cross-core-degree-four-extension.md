# Cross-core moment-extension assessment — source comparison completed

TARGET: Test whether L030's prescribed degree-four local moments admit one global degree-four extension on selected 68-support indicators consistent across all 61-cores.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Notebook-scoped moment/global/completion searches found the already ready 2026-10-07 global pair assessment and ATTEMPTS/022's administrative park; primary constant-weight quadruple-SDP, graph-moment and partial-matrix-completion searches/readings are recorded below.
SOURCE_EVIDENCE: Reuse foundations/08–09; freshly read Polak arXiv:1703.05171v1 Section 1.1 (1)–(3), Proposition 1.1 and proof, pp. 2–3, and Laurent PNA-R0108 Section 6.1 Lemma 13 with complete proof, pp. 13–14; foundations/10 records Grone–Johnson–Sá–Wolkowicz (1984) Proposition 2 and Theorem 7 with proof cases, pp. 118–122, https://www.math.uwaterloo.ca/~hwolkowi/henry/reports/pdcomplGJSW84.pdf.
COMPARISON: Known Boolean and constant-weight moment frameworks cover the global universe, but do not decide L030's fixed higher-moment slice; ordinary PSD completion does not enforce equal-union identities. The necessary pair slice is already assessed and untested, whereas L022–L026 use a different assignment.
GAP: Shared third/fourth-monomial agreement, global PSD feasibility and any cardinality consequence remain unproved; first perform the unchanged ready pair-slice test rather than implement the full degree-four problem.
REASON: Coverage supports the precise model and a necessary finite prerequisite, not a gluing theorem or a full fourth-moment algorithm; routing reuses a pre-invocation ready assessment without reopening an exhausted mathematical diagnostic.
SCOPE: One global Boolean degree-four assignment on all 68-subsets, M_2 PSD, pair-conflict zeros and L030's exact finite-average restrictions at every 61-core; source coverage approves formalism/comparison only, with the next bounded calculation restricted to the existing ready global pair assessment.
LITERATURE_REASON: The proposed cross-core universe and simultaneous higher-moment restrictions lie outside the prior local-degree-four assessment; the current gate explicitly requires their separate source comparison.

The main gap is arbitrary-center 68-agreement safety (and independently
67-agreement safety). This is one proposed intermediate feasibility
test, not a proposed complete proof. Its plausible downstream use is
to decide whether L030's obstruction survives enforced compatibility
between different cores; a failed extension would only exclude that
prescribed assignment, not give a useful global upper bound by itself.

Intended scope for source assessment: use binary indicators indexed by
global 68-subsets of H and a single degree-four moment assignment with
the corresponding order-two positive-semidefinite moment condition,
Boolean reductions and zeros for pairs of supports intersecting in at
least 64 positions. Require its restrictions through S=C union A to
agree with L030's prescribed local moments through degree four for
every 61-core. This specifies a proposed model to assess, not an
assertion of feasibility, impossibility or useful strength. Definitions
and any needed qualifications must be reconciled with primary sources
before a mathematical attempt is approved.

Essential proposed inputs are L027 (selected-support injection and
incidence counting) and L030 (the exact local moment prescription).
L022–L026 are comparison leads for already tested global support SDP
constraints; inspect only the relevant passages and recorded failures.
Do not assume their witnesses coincide with this prescription. L049
and L050 explain the routing away from the exhausted fixed-core cap;
their extra five-block exclusions are not imposed in this degree-four
test. No cross-notebook theorem input is proposed.

Review test: identify a primary extension theorem, existing obstruction
or ready finite criterion with matching hypotheses, and compare it
against the recorded local/global diagnostics. Import an exact match;
otherwise approve only a concretely bounded feasibility or obstruction
test supported by the inspected sources. Park the proposal if it merely
renames an exhausted diagnostic or essential coverage remains blocked.
An untested consistency condition must not be presented as new evidence.

Unresolved assumptions: whether the prescribed local moments even
agree on shared global monomials; whether a simultaneous PSD extension
exists; whether any obstruction can improve a uniform list bound.
No assumptions in this list are established here. Mathlib coverage is
not checked. This file records a continuation only and does not approve
mathematics in the current turn.

## Completed comparison and precise model

Keep the TARGET above unchanged. Write V for all 68-subsets of H.
The proposed variables are y_D for D subset V, |D|<=4, with
y_empty=1 and M_2(y) indexed by all I subset V, |I|<=2, having entry
y_(I union J). Repeated indicators use Boolean reduction. Require
M_2(y) PSD and pair zeros when distinct supports meet in at least 64
positions. For each 61-core C and every D consisting of at most four
supports containing C, prescribe y_D by L030's full finite-average
formula applied to {S minus C: S in D}. This specifies restrictions,
not conditioning on a random event and not an existence claim.
All assignments referring to the same global monomial must agree.
Checking third/fourth agreement remains research, not a result of this
review. No five-block constraints from L049/L050 are added.

The known finite-independence-system formulation and its qualifications
are reusable from [foundations/08](../../foundations/08-boolean-moment-source.md).
Its order-two relaxation is not a representing-measure theorem. The
global pair-conflict graph is finite, with vertices V and allowed
singletons, so Laurent's graph-only hypotheses match. At t=1, Lemma 13
uses M_2 and degree-four moments. Its proof explicitly includes singular
rows, zero propagation and nonnegativity through degree two. Apply
that source only to pair edges; labeled triple restrictions are supplied
by the specified local moments, not by the graph theorem. There is no
need to reprove either hierarchy.

Polak's source uses the constant-weight universe n=1024,w=68 and binary
minimum distance 10, with moment-family sizes unrelated to RS k=64
or interleaving m. Its M_(4,empty) is the same union-indexed matrix.
Full A_4 also has nonempty conditioning matrices and nonnegative
triple/quadruple moments; those are not silently added here. Its
indicator proof establishes a code bound, not extension of prescribed
local moments. Preserve the printed Proposition 1.1 typo recorded in
foundations/08–09: the proof concludes A(n,d,w), not the displayed A(n,d).
No numerical table or fourth-order symmetry implementation is imported.

[foundations/10](../../foundations/10-psd-completion-source.md) records the
primary completion comparison. It cannot be used to glue the local
matrices: all specified clique matrices and chordality would need to
be checked, and even an ordinary completion does not enforce the
equal-union identities on its remaining entries. No chordality,
nonchordality, compatibility failure or global impossibility is asserted.
These distinctions explain why citations alone do not solve the target.

## Duplicate and stopped-route comparison

The exact [global pair assessment](2026-10-07-global-pair-marginal-extension.md)
already covers rho, local N_i, overlap-61/62/63 entries, forbidden pair
zeros, all global Johnson eigenspaces and the augmented constant row.
Its singleton and pair compatibility specification was checked there;
do not call that check new evidence. Degree-four PSD retains the
constant/singleton principal matrix, while pair nonnegativity is part
of Laurent's cited low-degree conclusion. Thus that unchanged pair
test is an appropriate prerequisite, not an arbitrary stronger test.
Its source normalization and averaging qualifications remain reusable
from [foundations/09](../../foundations/09-global-pair-johnson-source.md).
Only the pair-only diagnostic has licensed full position averaging;
no symmetry reduction of the complete higher-moment model is inferred.

ATTEMPTS/022 explicitly says that no mathematical pair test was completed.
History/067–069 confirms that its park followed process recovery rather
than an exact obstruction. The new discriminating purpose is to test
a necessary principal slice before investing in the proposed simultaneous
degree-four extension. Preserve that historical park, without treating
it as a permanent mathematical ban. The earlier assessment and exact
target were saved and separately approved before this invocation.

L021's unrestricted optimum does not decide a prescribed subvector.
The read hypotheses/conclusions of L022–L026 instead prescribe L022's
p_i and its product-form triple extension. Their PSD/scalar/weak packing
passes do not assert L030's prescribed local restrictions. Their parked
individual-block diagnostics remain parked. No duplicate completed
fixed-slice certificate was found in the scoped paths inspected.
ATTEMPTS/021,031,032 retain the independent local-cap obstructions;
none supplies a shared global assignment or an RS list. L027's selected
support restriction and L030's full distribution/pair computation were
read; their finite audits were reused, not rerun or newly certified.

## Search and inspected-source evidence

External queries on 11 October 2026 were:

- `constant weight codes quadruple semidefinite programming bound Gijswijt Mittelmann Schrijver moment subsets size four`
- `Laurent comparison Sherali Adams Lovasz Schrijver Lasserre hierarchies moment matrix stable set 2003`
- `Grone Johnson Sa Wolkowicz 1984 positive definite completions partial Hermitian matrices theorem 7 pdf`
- `prescribed local moments global consistency constant weight codes moment extension`
- `"local" "moment" "global" "Boolean" "positive semidefinite" completion`
- `"constant weight" "prescribed" "moment" extension`
- `"2571353" "moment" packing`

The primary passages freshly inspected were Polak's
[v1](https://arxiv.org/pdf/1703.05171v1), Section 1.1 and the full
indicator/principal-submatrix proof, printed p. 2, plus the averaging
argument, p. 3; Laurent's
[31 July 2001 report](https://ir.cwi.nl/pub/4319/04319D.pdf), Lemma 13 and
its complete three-direction proof, pp. 13–14; and the completion source
and qualifications in foundations/10. Older GPT and Johnson spectral
assessments were reused in their covered scopes, not claimed freshly
retrieved. Grone's browser text is accessible; shell DNS failure and
unavailable screenshot image data do not block the ready pair sources.

Gijswijt–Mittelmann–Schrijver arXiv:1005.4959, sparse moment articles,
and a search hit for *Simulating Correlated Binary Outcomes* remain
unread leads. No result from them is used; searches with the exact
number mostly returned irrelevant material. No failure to find a match
establishes novelty. No inspected theorem decides this fixed extension.
Full matching Mathlib coverage remains not checked.

## Bounded continuation and decision rule

Use exactly the existing ready pair assessment's TARGET as the next
action, with essential inputs L027, L030, L021 and foundations/08–09.
It is the constant/singleton prerequisite to this reviewed target.
The source application requires every Johnson eigenspace, the
constant Schur-complement coordinate, all fixed entries and nonnegative
free entries, allowing singular matrices. Save a complete exact rational
primal certificate or an exact infeasibility certificate; a numerical
solver status is not a result. No mathematical calculation ran here.

Pair infeasibility stops this prescribed degree-four extension, not
all extensions or lists. Pair feasibility stops only the pair diagnostic
and leaves shared higher-monomial agreement and M_2 PSD unproved;
select a separately assessed bounded higher-order test then. Neither
outcome is a safety certificate, an unsafe-list witness or a boundary
improvement. The main gap and bracket 955–957 remain unchanged.
