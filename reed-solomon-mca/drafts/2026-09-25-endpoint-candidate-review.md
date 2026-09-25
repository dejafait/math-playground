# Endpoint candidate review — 2026-09-25

This is one critical review of the existing conditional endpoint candidate.
The required shared/local files and whole overview/DAG were read; existing
changes, identifiers, and historical branches are preserved.

Gap: the frozen affine-support event has not been identified with the current
ABF26 challenge, including its radius endpoints and permitted code parameters.
Intermediate target: either certify that identification for the smooth
length-16 witness or find a concrete mismatch that retires the candidate as
a challenge-level objection. Downstream use: select the correct mathematical
threshold problem before attempting an error bound. Sharp upper/lower bounds
remain unresolved even if the definitions match.

Discriminating test: check the challenge's quantifier order, sampler, agreement
inequality, number of inputs, radius range, and field/domain/dimension
restrictions against L001/C001a; independently review the witness and the exact
comparison with 2^-128. Continue the challenge-level candidate only if its
essential source bridge is justified. A source mismatch rejects that bridge;
failure to recover text leaves it unverified, not disproved or certified.

Redundancy check: L001 already proves the radius-cell fact and C001a already
constructs the witness. No duplicate lemma is sought. The unsuccessful direct
PDF retrieval and automatic grid-to-real-maximum transfer remain recorded.
This review will instead seek primary indexed definition text and inspect the
candidate's mathematical and quantifier assumptions. The current consecutive
exploration count is zero; the completed assessment will classify this step
by its actual evidence.

Saved before source review. No new result is asserted here.

## Review finding and bounded mathematical test

The official page still states the real-maximum target and includes the clause
assuming the field is sufficiently large for such a radius to exist. The
ePrint metadata still reports the July 6 revision. Indexed-definition searches
and the additional Stanford publication-page lead did not recover its text;
the direct PDF was not retried. The pinned `IsMCA` and `mcaError` declarations
were read again and agree with the frozen event. No algebraic error was found
in L001 or C001a.

The field-size clause is a separate candidate weakness, even if the support
event is identified correctly. C001a establishes one finite field size, with
only a nonempty safe set. It does not refute a statement about all sufficiently
large fields at fixed length. A concrete discriminating test is available:
for a length-n constant code, every bad support contains a pair of coordinates
on which the direction differs. Each such pair permits at most one challenge.
Thus the candidate upper bound is binomial(n, 2)/q at every radius. For n=16,
q >= 120 * 2^128 would make all radii safe. This would show that the source's
field-size clause can materially exclude the witness, rather than merely
leaving a hypothetical parameter loophole.

Unfinished proof to check: if a+gamma*b is constant on S but a or b is not,
then b cannot be constant on S (otherwise a is too). Choose i,j in S with
b_i != b_j and solve gamma=(a_j-a_i)/(b_i-b_j). Conversely each such collision
is a bad two-coordinate support when delta >= 1-2/n. A union over unordered
pairs proves the bound. No restriction on the pair a,b or on the support
chosen after gamma is introduced. The error must still be maximized over a,b.

This is a field-quantifier test within the candidate review, not a separate
attempt to solve the sharp-threshold problem.

## Completed assessment

The support-pair proof is complete in
[L002](../lemmas/L002-constant-code-field-size-saturation.md). It works after
the support is chosen, uniformly in both words, and gives the exact union of
pair-collision challenges at terminal radii. It does not assert that every
pair contributes a different challenge or that its upper bound is sharp.
At length 16 it gives all-radius safety for q >= 120 * 2^128, with a smooth
example at q = 5^60. Exact integer checks passed during the review.

The endpoint witness's model-only proof survives, but the challenge-level
candidate remains incomplete under the source's field-size qualification.
The new mathematical evidence makes this an informative NEGATIVE, with no
claim to have settled the primary definition, the intended endpoint meaning,
or a sharp threshold. The failed unqualified inference is recorded in
[the attempt note](../ATTEMPTS/002-single-field-endpoint-disproof.md); the
current bottleneck and continuation action are kept only in PROGRESS.md.
