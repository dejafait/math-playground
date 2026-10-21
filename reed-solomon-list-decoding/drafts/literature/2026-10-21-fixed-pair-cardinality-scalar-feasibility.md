# Fixed-pair scalar/cardinality feasibility — bounded witness assessment

TARGET: Test exact-N feasibility with L098's pair marginals fixed, all original triple scalar constraints and contractions retained, and PSD constraints omitted.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 393 reused the three 2026-10-20 cardinality assessments, foundations/04,12,13 and foundations/10's polyhedral-certificate passages; compared L021–L023,L098,L105, ATTEMPTS/081–082,088 and the complete prior model/reconstruction scope. Fresh searches and their limits are recorded below; no inspected source or local duplicate decides this fixed-pair system.
SOURCE_EVIDENCE: Reuse Schrijver III.B (62)–(67), Kim–Toan v1 (31)–(35), Raghavendra–Tan v1 Section 3 pp.7–9 and Polak v1 Proposition 1.1 as precisely recorded in foundations/04,12,13; L098 supplies the audited homogeneous conversion. MIT 6.854 LP notes, Linear Equalities and Basic Feasible Solutions, and Cheung MATH5801 Section 5.4 Proposition 5.2/full proof were inspected for finite exact witness methods, with qualifications below.
COMPARISON: L098 rejects one complete control, L105 passes independent copies of contraction entries, and ATTEMPTS/082 rejects one numerical reconstruction with free pairs and PSD. None decides the shared-variable scalar-only system. Standard rational linear algebra covers a bounded restricted-support witness search; it does not make that support sufficient or prove unrestricted feasibility.
GAP: In research, construct and check one complete assignment using only the prescribed source classes with distance multiset (i,68,68) for free distinct triples, then lift to every original orbit and verify all scalar rows and contractions. A failed restricted witness leaves the full system undecided.
REASON: Essential source coverage is adequate for the single exact construction test below. This supplies a concrete method distinct from the stopped numerical solve, without a new aggregation theorem, feasibility result, source-access dependency or change of the fixed pairs.
SCOPE: The saved TARGET is unchanged; only the bounded feasible-witness construction specified in step 393 is covered. No unrestricted optimizer, infeasibility inference from the restricted support, numerical proposal, support scan, PSD constraint or changed pair prescription is approved.
LITERATURE_REASON: At invocation, the changed relaxation with fixed exact-N pairs, free triples, scalar constraints and contractions but no PSD lacked essential method coverage after L105's independent-row pass; step 393 supplies the bounded construction prescription without repeating that calculation.

## Proposed test, not an approved mathematical formulation

Use n=1024, w=68, d=10, T=65537^28/2^128 and N=floor(T)+1.
Freeze precisely the pair coordinates of L098's normalized control
z_c=alpha*z+(1-alpha)*e, with alpha, z and e as defined there.
Allow every original admissible triple-orbit coordinate to vary. Retain
the source scalar bounds, source permutation identities, impossible
orbits, forbidden distances, Boolean repetitions and all 69 L098
contractions. Omit PSD constraints. Do not freeze L098's triple values
or assume that its failed control describes all such values.

Essential inputs for the review are L098, L001, L021–L023 and the
precise normalization/source statements in foundations/04,12,13.
Use the prior source assessments for their inspected passages; no new
download is required merely to repeat existing coverage. A changed
source hypothesis or missing proof case must be identified explicitly.
No cross-notebook theorem is proposed. Full matching Mathlib coverage
has not been checked.

The main gap remains arbitrary-center 68/67 safety. This intermediate
test could determine whether the frozen pair prescription can survive
exact cardinality after changing triples; it cannot by itself prove
safety uniformly over other pair distributions. A complete feasible
assignment would stop this scalar-only exclusion diagnostic. An exact
separator would exclude these fixed pairs in this relaxation only.
Neither outcome would give an RS list or a new finite boundary.

## Coverage and stopping requirements for the next review

Check whether a known theorem or already recorded local result decides
this question before approving computation. In particular, compare
L098's audited homogeneous normalization and the failed full-variable
proposal, not merely the stale pending-audit text in PROOF.md. The
current turn read their scope and stop evidence only, and did not derive
a new aggregation, prove redundancy or run a feasibility test.

Any aggregation over t,s must sum admissible original entries with the
correct multiplicities, including repeated words and zero pair
coordinates. Equating distinct original entries just because their
three pair distances agree needs justification; it cannot silently
restrict the feasible set and then support an infeasibility claim.
This is a review obligation, not a promised reduction.

Approve one bounded mathematical attempt only if the review identifies
an exact finite witness or original-coordinate separation test with
explicit work limits. Preserve ATTEMPTS/033–034,067–068,080–082:
no old numerical solve, rounding sequence, support enlargement or
parameter scan is authorized by this pending assessment. If the
proposed smaller question is already decided, merely a renamed old
test, or lacks a justified bounded method, record that finding and
select an independent target rather than renewing the exhausted
translated-pole budget. No new mathematics is derived or approved in
this assessment.

## Step 391: completed scope review and narrower continuation

The full saved target remains undecided and is not approved for a new
joint solve. Reused the three 2026-10-20 cardinality assessments,
foundations/04,12,13 and L098's complete necessity/normalization proof.
Read L021–L023's hypotheses and conclusions and step 362's audit record;
the frozen control is already audited, despite the stale overview wording.
Compared ATTEMPTS/081–082 and the complete model/failed reconstruction
description in the free-cardinality working record. The latter has
1,500,625 original coordinates and 269,774 free coordinates before
cardinality. Removing PSD and freezing pairs changes its mathematical
question, but supplies neither a small exact projection nor a justified
new joint algorithm. No claim of impossibility or computational lower
bound follows. Do not restart the stopped numerical prescription.

Fresh searches on 2026-10-21 used `constant weight code triple
distribution linear programming marginal constraints fixed cardinality
Schrijver` and `"A(1024,10,68)"`. Results gave the already assessed
Schrijver/Polak/Trinker leads and no inspected matching finite verdict.
Trinker and doubly constant-weight strengthening leads remain unread;
no blocked access was retried and none is essential for the elementary
scalar-only test below. Search results are discovery evidence only,
not theorem evidence or an originality claim.

Recovery compared three genuinely different mechanisms: (1) a joint
fixed-pair scalar LP, requiring a new exact solution/separator method;
(2) independent contraction-row capacity tests, dropping cross-row
coupling and using only original scalar intervals and exact arithmetic;
(3) new labeled forbidden-pattern bounds, which need a pattern mechanism
beyond L042/L048/L050's recorded deletion obstructions. Select (2) as
one bounded preliminary test of the saved question. This changes the
next action; it does not assert joint feasibility or renew the exhausted
translated-pole budget. The ready narrower assessment is
`2026-10-21-fixed-pair-contraction-row-capacity.md`; it requires separate
next-turn approval. The full target's REVIEW_REQUIRED status is retained:
approval of a necessary row test does not approve a joint solve.

No new mathematical result, interval derivation, aggregation theorem,
lemma or mathematical script was produced in this literature turn.

## Step 393: source comparison and one exact construction prescription

This supplement supersedes the pending gate and lack-of-method finding
above, preserving their historical evidence. It approves a future
known-method specialization, not a mathematical result derived in this
literature turn. The supervisor separately approves the newly ready
continuation before research. Full matching Mathlib coverage is not
checked; unknown coverage is not absence.

### Sources actually covered

Reuse the inspected primary theorem statements and proof cases in
foundations/04,12,13, with their hypotheses unchanged. Schrijver,
[*New code upper bounds from the Terwilliger algebra and semidefinite
programming*](https://homepages.cwi.nl/~lex/files/codes.pdf), IEEE TIT
51 (2005), 2859–2866, DOI 10.1109/TIT.2005.851748, III.B (62)–(67),
p.7, supplies the normalized actual-orbit scalar constraints and
permutation equalities. Kim–Toan,
[arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1), (31)–(35),
pp.8–9, cross-checks them. Nonempty binary constant-weight codes with
0<10<136<=1024 meet these hypotheses. Impossible multinomial indices
are absent; forbidden-distance actual orbits are present and zero.
Schrijver (61)'s complement prefactor is unused. No PSD theorem or
new block decomposition is needed.

Raghavendra–Tan,
[arXiv:1110.1064v1](https://arxiv.org/pdf/1110.1064v1), Section 3,
Definitions 3.1,3.3 p.7, conditional-cardinality display p.8 and
qualification p.9, supplies cardinality-conditioned local marginals,
without a global representing-distribution conclusion. Polak,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), Proposition
1.1 and its indicator proof p.2, Section 1.2 p.3, supplies ordinary
constant-weight indicator necessity and constraint-preserving averaging.
Retain its printed A(n,d) versus proved constant-weight qualification.
L098's separate audit already checks homogeneous conversion, both
repeated third words and null pairs. Use it, rather than reproving the
hierarchy or dividing by a zero pair. Ordinary support consistency is
being tested; no actual-label RS averaging is added.

The existing foundations/10 polyhedral coverage cites MIT 6.854,
[Linear Programming notes, 2020 collection](https://courses.csail.mit.edu/6.854/20/Notes/n11-lp.html),
sections Linear Equalities and Basic Feasible Solutions. Freshly read
the elimination/Cramer's-rule certificate discussion and complete
movement-to-a-basic-solution argument. It supports exact rational
linear-system witnesses and their verification. It does not supply
a finite verdict for this notebook. The mixed-year compilation and
the previously qualified unrelated geometry statements remain unused.

Also read K. Cheung, MATH5801, [Section 5.4, Auxiliary problem,
Proposition 5.2 and its full proof](https://people.math.carleton.ca/~kcheung/math/notes/MATH5801/05/5_4_two_phase.html),
and Section 5.1's revised-simplex steps and degeneracy discussion.
The auxiliary problem assumes a full-row-rank finite real matrix and
nonnegative right side. Its zero optimum is equivalent to feasibility;
an intermediate positive value is not an infeasibility certificate.
The Section 5.4 outline prints A-transpose despite its stated dimensions;
only the dimensionally consistent Proposition 5.2 is used. These known
methods offer no runtime guarantee for this instance. No simplex run
is selected: exact linear elimination with one fixed free-coordinate
choice is a smaller construction test. Its complete original-coordinate
substitution, not an algorithmic success flag, will be the evidence.

### Discovery, duplicates and failures

Fresh queries on 2026-10-21 were `bounded variable revised simplex upper
bounds phase I lecture notes linear programming`, `"constant weight"
"triple" "fixed cardinality" linear programming marginals`,
`"Schrijver" "triple" "cardinality" "linear programming" constant weight`,
and `"fixed" "pair distribution" "triple distribution" codes linear
programming`. The coding queries yielded no inspected matching finite
verdict; several results were unrelated. Reuse the prior exact
A(1024,10,68), Schrijver, Polak and split-algebra comparisons rather
than downloading them again. This is bounded discovery, not proof of
novelty. Trinker and the prior doubly constant-weight strengthening
leads remain unread and are not essential for constructing an ordinary
scalar witness.

Additional method queries used `site.princeton.edu Vanderbei linear
programming upper bounds bounded variables pdf` and `site.ms.uky.edu lee
"Bounded Variables" simplex`. Lee's Fall 2000 and Fall 2003 PDF URLs
returned 404. The Fall 2005 PDF initially exposed its title/contents,
but retrieval of Section 12.8 failed; that chapter was not read and
its bounded-variable algorithm is not imported. A guessed Cheung
upper-bound page was inaccessible. Wiley chapter and Vanderbei bounds
passages are unread leads. None blocks the selected linear-system
construction, whose essential coverage is already readable. No further
access retry is needed.

Compared L098's complete proof/audit, L105's scalar-interval and
independent-row proof, and L021–L023's hypotheses/conclusions. Targeted
search of the three cardinality assessments, prior working record and
ATTEMPTS/081–082,088 found no recorded test of exactly the construction
support below. L098's control is audited, despite stale PROOF wording.
Its triple values are not reused. ATTEMPTS/082 used 269774 free
coordinates before cardinality, a matrix-free numerical update, two
PSD blocks and one failed rounded reconstruction. The construction
below has fixed pairs, no PSD and no numerical reconstruction. This
comparison licenses neither a restart nor a uniform exclusion claim.
L105's independent-row pass is not a shared-variable witness and is
not repeated.

### One bounded future mathematical attempt

Keep the exact TARGET and all of its constraints. For construction
only, prescribe zero at every permitted distinct-triple source class
except classes whose sorted half-distance multiset is (i,68,68),
5<=i<=68. Leave each retained source class free independently,
including every admissible t-s value. This is a proposed support for
one witness, not a theorem that the support suffices, an aggregation,
or an additional necessary constraint on feasible assignments.

1. Checkpoint the input contract before construction. Recover L098's
   exact N and pair coordinates from L021–L023/L098's canonical data,
   check hashes, normalization, forbidden pairs and objective N.
   Preserve previous artifacts. No old numerical proposal is an input.
2. Enumerate every original admissible (i,j,t,s) and all source
   presentations. Quotient only by the cited source equalities with
   invariant t-s; record the complete original-coordinate lift. Keep
   forbidden triples zero and Boolean repetitions at their fixed pair
   values, before applying the distinct-triple prescription. Derive
   and justify the construction's model in research. Do not presume a
   retained-class count, triangular rank or redundant contraction.
3. Substitute this support into all 69 L098 contraction equations,
   summing the integer D of each original entry into its source-class
   coefficient. This sums coefficients of variables already equal
   by the source; it does not equate distance-only variables. Retain
   all original scalar rows for final substitution, including positive
   lower bounds if any. A zero outside the proposed support that fails
   a lower bound rejects the construction; it is not a row to omit.
4. Perform one exact rational Gaussian elimination in lexicographic
   class order, with the first available nonzero pivot row. If the
   system is consistent but underdetermined, set its nonpivot
   coordinates to zero once and back-substitute. No parameter search,
   simplex, optimization, rounding or alternate free-coordinate choice
   is covered. Save all operations and the complete candidate. An
   inconsistent restricted system or a failed sign/scalar row stops
   this prescription and leaves unrestricted feasibility undecided.
5. Independently regenerate every original orbit from its eight
   membership regions, the source-class lift, all presentations and
   all D coefficients. Substitute the complete rational assignment
   into every ordinary source scalar row, forbidden/repeated value,
   source equality and all 69 contractions. Include zero pair cases
   and both repetitions. Check every original equation after any
   elimination; no rank, interval, copied flag or preview suffices.
   A full passing witness decides feasibility of the saved scalar-only
   system, even though construction used a restricted support.

Use future artifact prefix `scripts/finite-support/fixed-pair-shared-scalar-`.
Store the exact support prescription, full lossless lift, rational
candidate, every contraction residual, all scalar slacks (lossless
factoring is allowed), and independent verification with hashes. Print
only counts, actual/required bounds, failures and paths. Record the
first failed bound or mathematical check without hiding other controls
that have not yet been verified.

Hard limits: 1501000 original entries per construction or verification
pass, 1024 free retained source classes, 69 contraction equations,
4600000 original scalar rows, 20000000 coefficient/presentation visits
over both passes, 5000000 rational elimination updates, 1 GiB declared
live memory, 256 MiB certificate output, 262144 bits per rational
component and 900 seconds for the full attempt. Count coefficient work
on a presentation visit where possible. No dense matrix may have an
axis equal to the full original-orbit count; the small retained-class
linear system is permitted. Check caps before allocation, and stop and
preserve an incomplete certificate when a cap is reached. The limits
are not a claim of tractability.

### Relevance and decision test

The main gap remains arbitrary-center 68/67 safety in the 955–957
bracket. The intermediate target is shared-triple scalar/cardinality
feasibility at L098's pairs. A full witness would stop scalar-only
exclusion of those pairs and identify PSD or other pair prescriptions
as a remaining issue. A genuine original-coordinate separator could
reject these pairs only, but no separator search is covered here.

Continue only through the one prescribed exact construction and its
complete verification. If it passes, stop this scalar-only exclusion
diagnostic. If it fails or exceeds a cap, park this construction without
a support enlargement, free-coordinate scan or rerun; the full target
stays open. L105's much weaker pass, the frozen-control rejection and
all historical stops remain intact. No code, measure, RS realization,
full SDP feasibility, uniform bound over other pairs or boundary change
follows from either construction outcome. Independent 67-agreement
safety, L104's bulk estimate/audit, L105's critical review and the
qualified ABF comparison remain unresolved.

Essential mathematical inputs are L001,L021–L023,L098,L105 and
foundations/04,12,13; foundations/10 supplies only the cited general
linear-algebra/certificate coverage. There is no cross-notebook input.
Use classification REPRODUCTION for the future attempt. This completed
literature step derives no new lemma, projection, rank, feasible value
or counterexample, and modifies no lemmas or mathematical scripts.
