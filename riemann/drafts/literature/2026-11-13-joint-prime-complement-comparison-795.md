# Joint prime-delay complement bound — completed source comparison

TARGET: Assess whether the joint prime-delay upper Rayleigh coefficient on C759a's fixed odd complement can be bounded by 3/2, retaining correlations among all five delays and checking known finite-codimension obstructions before approving one test.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step796 searched finite-interval truncated translations, joint numerical ranges and finite-codimension/phase-return obstructions; checked C759a, L741/L744, the named earlier stops and L743. No inspected theorem supplies the requested real-odd fixed-complement coefficient; no novelty inference.
SOURCE_EVIDENCE: Clark Geometry of Numbers, current159-page author PDF, Theorem13.3/Corollary13.4 p72; Fillmore-Stampfli-Williams Acta Sci.Math.33(1972), Theorem5.1 and Corollary pp188-189, with proof; L743 Sections1-4 and its separate audit give the local finite-delay modulation mechanism on a different space.
COMPARISON: Joint correlations can matter, but L743 warns against expecting finite constraints alone to improve an unweighted arithmetic supremum. Its complex cell-neutral theorem does not cover real odd W. Essential numerical-range theory requires a weakly-null sequence in the relevant parity space and does not supply its Rayleigh value or the3/2 comparison.
GAP: Neither the3/2 upper bound nor its negation is established. The remaining bounded specialization is a real odd carrier, exact projection off120 sine modes, complete five-delay Rayleigh limit and rigorous constant-envelope threshold comparison; this is nominated separately, not performed here.
REASON: Essential coverage supports one obstruction test before attempting an upper certificate. Retain C759a's stop and L743's narrower equality; do not repeat absolute costs, scan cutoffs, or claim the bound is already false.
LITERATURE_REASON: The saved REVIEW_REQUIRED target introduced real odd finite-codimension and joint-delay hypotheses outside assessments791/792; L743 and primary essential numerical-range theory are new relevant coverage.
SCOPE: Completed literature-only review; fixed interval(-1,1), fixed120-mode split, all five actual prime-power delays, unweighted L2 arithmetic form only. No new lemma, mathematical script, full-energy sign or parity-gap conclusion.

## Completed comparison — 13 November 2026, step796

The main gap remains actual-Xi all-degree mixed positivity in
L030-L032/C032a. The intermediate question is the nominated3/2 upper
arithmetic coefficient on C759a's W. Such a bound could improve its
odd lower estimate, but would leave coupling, the finite Schur sign,
parity ordering, even simplicity/sign, Xi realization with multiplicities
and global assembly unresolved. The review sought applicable coverage
and an independently checkable bound or obstruction. Coverage supports
one obstruction attempt; the inequality is unresolved. This is
EXPLORATION, not a proved3/2 obstruction or an RH sign advance.

### Primary sources actually inspected

1. Pete L. Clark, *Geometry of Numbers with Applications to Number
Theory*, [author PDF](https://plclark.github.io/PeteLClark/Expositions/geometryofnumbers.pdf),
159-page version retrieved13 November2026, Theorem13.3 and
Corollary13.4, printed p72. For a finite real list theta_j and integer
M>1, the corollary gives integers0<m<M with
max_j||m theta_j||<=M^(-1/d). No independence or algebraicity is
required. Read the linear-forms proof setup and N=1 specialization;
the source leaves remaining proof details to the reader. Import the
named theorem without reproving it. L743 Section2 already handles
both bounded- and unbounded-denominator cases to obtain arbitrarily
large simultaneous returns. That finite-list argument, unlike its
cell-neutral conclusion, does not require L=K log(3)/2.

2. P. A. Fillmore, J. G. Stampfli and J. P. Williams, *On the essential
numerical range, the essential spectrum, and a problem of Halmos*,
Acta Sci. Math. (Szeged)33(1972),179-192,
[primary journal scan](https://acta.bibl.u-szeged.hu/14354/1/math_033_fasc_003_004_179-192.pdf),
Theorem5.1 and Corollary, pp188-189. For a bounded operator on a
complex separable infinite-dimensional Hilbert space, essential
numerical-range membership is equivalent to a weakly-null unit
sequence whose Rayleigh values approach the scalar. Read the complete
proof, including its finite-rank compression and Hilbert-Schmidt
subsequence construction, and the compact-perturbation definition
on pp187-188. This supports the comparison; it does not identify a
scalar for A. Real odd tests must first be supplied. A direct finite
projection estimate can replace use of the abstract theorem in the
proposed proof. No new essential numerical-range theorem is needed.

The standard named Riemann-Lebesgue lemma, imported in L743, applies
to fixed L1 oscillatory pairings. Its hypotheses and the change from
complex modulation to a real sine carrier remain application obligations.
No quantitative return frequency or prime-log independence is needed.

### Local overlap and failures

Read C759a Sections1-4, L741's normalization statements, L744's
hypotheses/(6), and L743's full proof and separate audit. L743 was
identified through the neutral-prime-only-rayleigh-saving stop of
4 November. It preserves an unweighted arithmetic supremum under
complex modulation and exact cellwise exponential correction at fixed
K. Its conclusion concerns neither real odd parity nor sine constraints.
Its conjugation, recurrence and bounded-form continuity tools are
reusable; the parity-preserving construction is an unproved difference.

Assessments791/792 cover full-form/Schur theory, not this coefficient.
Assessment583's completed comparison treats three separated neutral
cells; its large-ball Wiener-Hopf and prolate sources do not sign a
fixed-cosine complement. That failure does not prohibit a fixed-window
recurrence obstruction. The short-bump projection stop concerns a
different Hardy dictionary; the generic joint-energy stop leaves
joint archimedean control unpaid. None supplies a3/2 counterexample
for W. A targeted local lemma search for finite-codimension, essential
numerical-range and odd-modulation statements found no exact match.
This bounded search is not a novelty or absence proof.

### Search record and route decision

Queries submitted: `truncated translation operators finite interval
essential spectrum finite codimension simultaneous recurrence`;
`finite section sum truncated translation operators irrational shifts
numerical range`; `essential numerical range weakly null unit vectors
finite codimensional subspaces Fillmore Stampfli Williams pdf`;
`Kronecker simultaneous approximation theorem continuous parameter real
numbers recurrent phases logarithms pdf`; `"prime" "translation"
"finite codimension" Rayleigh`; `"truncated translation" "odd" spectrum`;
and the exact Fillmore-Stampfli-Williams title/year. Hits on Hardy
model-space shifts, numerical finite sections, effective Kronecker
for algebraic inputs and a prime-translation academia manuscript
were not used as theorem inputs. There is no essential access blocker.

Nominate one constant-envelope real odd carrier/projection obstruction
test before computing an upper certificate. Assessment796 specifies
its exact scope for separate approval next turn. Neither its limit
nor its scalar threshold comparison was performed here. Failure must
stop that family without inferring the upper bound or switching
envelopes. Even success would leave full Q unsigned: L744 warns that
modulation does not preserve logarithmic Fourier energy. No canonical
argument or DAG edge changes. Matching Mathlib coverage for this
parity/projection statement is not checked; no absence claim.

## Original nomination (preserved; review status superseded above)

The proposed operator is
A=sum_(n=2,3,4,5,7) (Lambda(n)/sqrt(n))
(T_(log n)+T_(log n)^*), with zero-extended shifts on(-1,1).
Let W be the full odd L2 complement of sin(pi*j*x),1<=j<=120,
as in C759a. The question is whether
sup_(w in W, ||w||_2=1) <Aw,w> <=3/2
is available or independently testable. This is a proposed inequality,
not a proved claim. In particular compression by finite codimension
does not automatically lower an operator norm or its upper Rayleigh
coefficient. The source review must check possible high-frequency
recurrence/finite-codimension obstructions, including applicable local
modulation and joint-delay failures, before allowing a computation.

The threshold is nominated for possible use with C759a's existing
T100 archimedean and pole enclosures. The new mechanism would have to
retain the correlations among actual translations in one quadratic
form instead of adding their separate absolute bounds. The old method
stop remains valid. The new target is not covered by the previous
SPECIALIZE scope, which explicitly excluded refined mechanisms.

Essential inputs to review: C759a, L741, L744. Named local inputs may
be extended only after identifying a specifically relevant result.
No new source theorem or mathematical implication is imported here.
If source/duplicate comparison supplies an obstruction or only repeats
the old triangle bound, reject this target without a cutoff sweep; a
historical stop alone is not a global ban. If a genuine signed bound
or discrimination test is feasible, write its exact assessment for
separate approval. No archive recovery or external numerical certificate
is necessary merely to formulate this question.

Unresolved independently: complete odd lower floor, coupling and Schur
sign, actual parity ordering, even simplicity/sign, an arithmetic
ground-state-to-Xi realization with multiplicities, and shifted/global
mixed positivity. These missing bridges prevent representing this
fixed-window refinement as a creative central RH mechanism. Full
matching Mathlib coverage is not checked; no cross-notebook input.
