# Free-variable exact-cardinality feasibility — source assessment

TARGET: Test exact-N feasibility with free pairs and triples, all 69 contractions, all ordinary scalar and pair rows, and both full zero-index PSD blocks.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: On 2026-10-20 searched fixed-cardinality constant-weight SDP, Schrijver triple marginal sums, rational coding certificates and the exact A(1024,10,68) string; compared primary Polak quadruple and Tseng–Lai–Yu split-algebra formulations, Brouwer's table scope, L021,L023,L098 and ATTEMPTS/033,034,067,068,080,081. No inspected result decides this finite free-variable system; no novelty inference follows.
SOURCE_EVIDENCE: Reused foundations/04,12,13 and freshly inspected Schrijver III.B (60)–(67), https://homepages.cwi.nl/~lex/files/codes.pdf ; Kim–Toan arXiv:1212.3467v1 (31)–(35), pp.8–9, https://arxiv.org/pdf/1212.3467v1 ; Raghavendra–Tan arXiv:1110.1064v1 Section 3 pp.7–9, https://arxiv.org/pdf/1110.1064v1 ; Polak arXiv:1703.05171v1 Proposition 1.1/full proof and Sections 1.1–1.3 pp.2–4, https://arxiv.org/pdf/1703.05171v1 . Reuse weak-duality coverage in foundations/04 and affine-LMI/elimination coverage in foundations/10, https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf and https://web.stanford.edu/~boyd/papers/pdf/semidef_prog.pdf .
COMPARISON: The cited methods cover necessity, source normalization and exact-certificate sufficiency; L098 supplies the normalized contractions and exact-N support reduction. L098's one-control rejection, L097's system without contractions and L051/L052's fixed pair prescriptions do not decide this system. Stronger known programs require additional moments/blocks; their inspected statements provide no matching finite verdict.
GAP: Construct the full original-orbit model and obtain either one complete rational feasible witness or one exact contradiction over all its free variables. Neither feasibility, strict feasibility, rational attainment, a separator's existence nor practical tractability is established by this review.
REASON: Essential coverage is adequate for the single bounded attempt specified below, using existing normalization/contraction proofs rather than deriving a new hierarchy. The changed uniform question is independently testable; old frozen controls and stopped fixed-column solves remain parked.
SCOPE: Exactly the saved TARGET, with all source orbits and no extra pair/triple prescriptions; one bounded matrix-free proposal and one rational reconstruction/verification, subject to the caps below. No enlarged block family or repeated solve is covered.
LITERATURE_REASON: The startup REVIEW_REQUIRED gate concerns a changed uniform free-variable target; earlier ready assessments covered a frozen-control diagnostic or a system omitting cardinality, not this feasibility question.

## Proposed scope and downstream use

Use n=1024,w=68,v=956,d=10 and N=floor(65537^28/2^128)+1.
Allow all pairs and all actual triple-orbit variables to vary, fixing
only normalization, forbidden distances, Boolean repetitions and the
source equalities preserving t-s. Retain the exact-N objective and all
L098 contractions, every ordinary source scalar and L021 pair row, and
both full (0,0) source matrices from foundations/04. L098's control is
neither a starting feasible point nor a parameter family to be retuned.
No L053–L096 fixed-column subsystem or L097 optimization is reopened.

An exact infeasibility certificate for this necessary relaxation could
certify 68-agreement safety via the exact-N support reduction. A complete
rational feasible point would instead stop this particular combination
as a sufficient support certificate. Neither result is asserted here.
The 67-agreement question, RS realization, other PSD blocks and the
qualified ABF comparison remain independent unresolved questions.

The completed review below identifies a bounded certificate construction and
verification procedure, with explicit size/work limits. The full orbit
domain is large. Aggregating distinct t-s variables requires justification;
arbitrary distance-only identification could invalidate an upper bound.
Infeasibility of an unjustifiably restricted model is not an acceptance
result. No mathematical script, new theorem or solve for this target was
created in step 362.

## Recovery comparison and test

Three distinct possibilities were considered for continuation:

1. The proposed free-variable exact-cardinality system addresses the
   missing uniform inference after L098's single-control rejection.
   Its outcome can be tested by a full rational witness or exact dual.
2. Stronger actual-label support restrictions address RS realization,
   but PROOF.md records deletion obstructions for the prescribed shift
   patterns in L042/L048/L050. A new quantitative pattern family needs
   separate source discovery and a new discriminating target.
3. A 67-agreement center construction would address unsafety directly,
   but the existing L019 witness reaches only 66 agreements. No new
   concrete center with a verified count is available in this audit.

Step 362 selected (1) for this separate literature comparison. This changes the logical
question from rejecting a fixed point to testing all assignments in a
specified necessary system. Preserve ATTEMPTS/081 and earlier stops.
No source-access retry, control retuning or further audit of the same
result is proposed.

The separate review now supplies coverage and a bounded test, without
a finite feasibility verdict. A later mathematical attempt succeeds only with
the complete witness or exact infeasibility certificate described above.
A numerical solver status, time limit or missing certificate gives no
infeasibility result. If no justified bounded formulation is available,
park this proposed system and select a different independently testable
mechanism rather than cycling through source retrieval.

Essential continuation inputs: L001,L021,L023,L098 and foundations/04,12,13.
L097 and ATTEMPTS/033,034,080,081 are comparisons, not premises asserting
feasibility or infeasibility of the new system. No cross-notebook input.
Full matching Mathlib coverage is not checked.

## Source-review checkpoint — step 363

2026-10-20: primary Schrijver III.B (60)–(67), Kim–Toan v1
(31)–(35), Raghavendra–Tan v1 Section 3 and Polak v1 Sections
1.1–1.3 are accessible. Reused the canonical source records and read
L098's complete contraction/support-reduction argument. No uniform
finite-instance verdict has been imported. The fuller assessment below
distinguishes a bounded certificate search from an algorithm guaranteed
to decide feasibility. No lemma, mathematical script or solve was made.

## Inspected sources and limits

The main gap is uniform arbitrary-center 68-agreement safety. The
intermediate target is the stated necessary exact-N relaxation. Its
possible downstream use is L098's already proved exact-N reduction from
any list exceeding T=65537^28/2^128. Selecting N candidates and then
68 agreement columns is valid for whole tuples by L001; no global
measure for relaxed moments or RS realization is inferred.

Reuse the primary-source assessment in
`2026-10-20-fixed-cardinality-triple-marginals.md` for the general
conditioned-cardinality framework. Freshly read Raghavendra–Tan v1's
Section 3 local-distribution consistency, inner products, cardinality
display and global-distribution warning, printed pp.8–9. The source
variables here index all 68-subsets and its cardinality fraction is
N/binomial(1024,68). This is only a necessary slice of that hierarchy.
L098 already handles zero pair probabilities and both repeated terms;
there is no reason to reprove that conversion.

Schrijver (2005), DOI 10.1109/TIT.2005.851748, III.B, printed p.7,
(60),(62)–(67), and Kim–Toan v1, (31)–(35), pp.8–9, were read for
actual-orbit normalization, the two affine families, all scalar rows,
repetitions and the t-s-preserving equality. Use foundations/04's
qualified formulas directly; Schrijver (61)'s complement prefactor
is still unused. Retaining only label (0,0) in each PSD family weakens
the source program. It supplies no inference about omitted blocks.
Pair rows are precisely L021's 68 basic Delsarte inequalities, whose
known-method optimum exceeds threshold; no new pair bound is claimed.

Polak (2019), DOI 10.1109/TIT.2018.2854800, inspected v1,
Section 1.1 (1)–(3), Proposition 1.1 and full indicator proof, p.2,
Section 1.2 p.3 and Section 1.3 p.4: quadruple programs A4/B4 are
available, with constraint-preserving averaging. Retain the printed
A(n,d) versus proved constant-weight qualification. Its comparison
with A3/Schrijver and Kim–Toan does not settle a cardinality-constrained
two-block slice at n=1024. Tables 2–3 concern small lengths; the p.4
report that a largest B4 computation took about three weeks directly
precludes treating polynomial size as a practical runtime guarantee.
No quadruple program or block diagonalization is imported for execution.

Additional comparison: P.-C. Tseng, C.-Y. Lai and W.-H. Yu,
*Semidefinite programming bounds for binary codes from a split
Terwilliger algebra*, [arXiv:2203.06568v1](https://arxiv.org/pdf/2203.06568v1),
13 March 2022. Read pp.1–2, Section III's partition/orbit setup p.4,
Proposition 6 statement and outer-product setup pp.5–6 and (12)–(13)
p.7. These concern an unrestricted binary code and additional partition
variables/PSD blocks. They are neither the constant-weight exact-N
system nor a finite n=1024 certificate. No specialization, full proof
audit or theorem import from this lead is claimed. It does not justify
identifying our different t-s coordinates.

The [Brouwer table page](https://aeb.win.tue.nl/codes/Andw.html), source
list and parameter headings, was inspected; it has no 1024 entry.
It is not a theorem establishing absence of better bounds. Searches
also found Trinker, *The triple distribution of codes and ordered codes*,
Discrete Math.311 (2011), 2283–2294. Its PMC page returned a browser
challenge; the theorem text remains unread and is not imported. It is
a nonessential lead given the inspected primary normalization and
cardinality sources, not a reason to repeat access attempts. The search
was bounded, not an exhaustive originality certification.

Queries included `constant weight codes semidefinite programming fixed
cardinality triple distribution marginal constraints`, `A(1024,10,68)`
(with quotation marks), `Schrijver constant weight code triple
distribution fixed code size constraints sum`, `constant-weight exact
cardinality Schrijver`, and `constant weight codes rational semidefinite
certificate`. Search abstracts alone were not used as theorem evidence.

## Exact model contract for the later attempt

Use exactly n=1024,w=68,v=956,d=10 and N=floor(T)+1. Keep all
admissible ordered (i,j,t,s), i,j=0,...,68, with the full ranges from
foundations/04. Normalize p0=1; retain all forbidden-distance zeros,
Boolean repetitions and precisely the source equality classes. Pairs
and every other source triple class remain free. Quotienting only
these exact equalities is permitted if the complete ordered-orbit map
and its lift are saved and independently checked. Distance-only
identification, setting unexamined orbits to zero and fixed old pairs
are not model reductions authorized here.

Retain L098 (1) for all i=0,...,68, with its original D coefficients;
i=0 already fixes the objective N, while i=1,...,4 are zero controls.
Retain every actual-orbit scalar row of foundations/04, all 68 L021
pair rows and pair signs, and exactly the two full 69-by-69 (0,0)
matrices of L023, now evaluated at the free variables. L023 supplies
their coefficient convention, not a feasible point on this slice.
L097's other 166 matrices are not extra constraints of this target.

Necessity and weak-duality coverage are imported, not reproved.
Foundations/04's Boyd–Vandenberghe §5.9.1, pp.264–266, and
foundations/10's Vandenberghe–Boyd (1996), DOI 10.1137/1038003,
§§1.1,3.1, pp.49–51,63–65, cover finite affine PSD certificates and
the failure of unrestricted strong-duality inferences. Their previous
detailed readings are reused; no fresh book/PDF fetch is claimed.
Exact elimination coverage in foundations/10 is also reusable. No
general SDP convergence, exact rational feasibility or dual-attainment
theorem is imported. Mathlib matching coverage remains not checked.

## One bounded construction and certificate test

This specifies future work, not a calculation made in this turn.
Local read-only capability checking found NumPy, but no SciPy, CVXPY,
Clarabel, SCS, HiGHS Python package or SymPy in the checked `python3`.
No package installation, authentication or external solve is required.

1. Save a lossless source model before numerical work. Stream the
   actual-orbit maps, scalar/pair recipes, factored integer D/beta
   coefficients and all equality rows. Independently reconstruct
   counts and coefficients from actual regions/source formulas.
   L023/L098's recorded 1500625 ordered orbits and 4501875 scalar
   rows are checks to reproduce, not evidence supplied by a preview.
   Record actual free-variable/equality ranks without predicting them.
2. Use one full-variable NumPy matrix-free product-cone residual
   descent proposal, at most 200 complete sweeps and 600 seconds of
   numerical iteration, whichever occurs first. Fix its update rule,
   step sizes, initialization and invertible power-of-two variable,
   scalar and positive block scalings in the saved model before
   iteration. All required rows participate in every sweep; no
   dense matrix with a dimension equal to the full variable count is
   permitted. The initialization is only a numerical point, not the
   L098 control or a new pair prescription. No convergence claim is
   needed: this stage only proposes a candidate. Numerical failure,
   nonfinite scaling or a missed cap stops this prescription.
3. Make one rational reconstruction. Round scaled nonpivot coordinates
   once to the nearest multiple of 2^(-40), ties to even. Determine
   pivot coordinates by exact elimination of the saved equalities,
   retaining all redundant rows and checking every residual. Source
   equalities/zeros/repetitions must already have their exact lift.
   Inconsistency or any failed sign/PSD row rejects this reconstructed
   assignment only. Do not fix the pairs, scan parameters, repeat
   rounding or rerun a solve. If a dual iterate is available, one
   direct rational reconstruction may instead be checked against the
   full coefficient identity below; no separate weight search.
4. A feasible certificate saves the complete rational lifted p,y,
   every contraction and scalar/pair slack (losslessly factored data
   is allowed), both full rational matrices and invertible rational
   congruences to nonnegative diagonal matrices. At a zero pivot the
   full residual row must vanish. An independent verifier regenerates
   all actual orbits, every source equality including t-s, all 69
   contractions, all scalar/pair rows and every matrix/factor entry.
   A preview or numerical eigenvalue is never a verification.
5. An infeasibility certificate is the cited weak-duality identity
   -1=sum lambda_r*g_r+sum trace(Z_b*A_b)+sum nu_j*e_j, with rational
   lambda>=0, rational PSD Z and signed equality weights. Check the
   constant and every free coefficient, including every lifted orbit,
   and transport all scalings back. Count both off-diagonal trace
   contributions. A restricted-ansatz separator is inadmissible.

Hard construction/verification caps: at most 1501000 coordinates before
source quotienting, 4600000 scalar/pair rows, 69 contraction rows and
two 69-by-69 matrices; at most 20000000 source-orbit coefficient visits
outside numerical sweeps, 2 GiB of declared live arrays, 512 MiB of
certificate output, 262144 bits per exact numerator/denominator and
1800 seconds for the full attempt. Save checkpoints and stop at a cap;
do not silently omit constraints, enlarge caps or count an interrupted
verification as complete. The next turn must state actual versus allowed
counts and the first failed bound. These are work limits, not estimates
that the target is tractable. If exact elimination itself exceeds them,
park the implementation without a mathematical infeasibility claim.

Put future scripts/artifacts under `scripts/finite-support/` with the
prefix `free-cardinality-zero-block-`; save full evidence and print only
counts, required bounds, failures and paths. Use the shared JSON inspector
for bounded navigation, and inspect full load-bearing evidence.

## Decision and continuation/abandonment test

Coverage is SPECIALIZE for this single attempt, with future classification
REPRODUCTION. A complete rational feasible witness stops precisely this
two-block/cardinality combination as a sufficient safety certificate.
A complete original-coordinate contradiction, together with L098's
support reduction, could establish 68-agreement safety; it must first be
recorded as an UNVERIFIED CANDIDATE and separately critically reviewed.
Neither outcome settles 67 agreements, omitted PSD blocks, a representing
measure, RS realization or the qualified ABF/ArkLib comparison.

A failed proposed point, absent exact separator or exceeded work limit
leaves the free-variable system undecided. Preserve its evidence and
park this numerical prescription; no iteration/rounding retry or return
to the old controls is covered. ATTEMPTS/067,068 are warnings about
failed numerical reconstruction, not a global prohibition: this target
has different free pairs, all source triples, exact-cardinality equations
and no ancestral fixed columns. ATTEMPTS/033,034,080,081 retain their
original scope. No duplicate uniform verdict was located locally.

This literature step produces no finite witness, separator, new lemma,
mathematical script or boundary improvement. The newly ready assessment
receives the supervisor's separate approval on the next turn before
research. Essential inputs remain L001,L021,L023,L098 and
foundations/04,12,13; foundations/10 supplies only reusable general
certificate/elimination coverage. No cross-notebook input is used.
