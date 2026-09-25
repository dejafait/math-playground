# Small-support field-size test — 2026-09-25

The required shared/local instructions, complete overview, and DAG were read,
and the existing changes were inspected and preserved. The
[official prize page](https://proximityprize.org/) and
[ePrint metadata](https://eprint.iacr.org/2026/680) were reread: the former retains its unspecified sufficiently
large field clause, and the latter still lists the July 6 revision. The unread
paper-to-model correspondence is not assumed. This is one interpolation and
counting step in the separately frozen affine-line model.

Gap: the field-size scope beyond the dimension-one case is not quantified.
Intermediate target: for RS dimension k < n, reduce every bad support to a
bad (k+1)-coordinate support and prove the uniform all-radius bound
E_C(delta) <= min(1, binomial(n,k+1)/q).
Downstream use: delimit eventual safety at fixed length/dimension and distinguish
it from the sharp-radius problem at the given field size. The source bridge,
the intended endpoint convention, and sharp errors before the small supports
become admissible remain later gaps.

Discriminating test: interpolate the direction on any k coordinates of a bad
support. If a disagreement outside those coordinates always exists and gives
a (k+1)-support bad for the same challenge, count its unique possible challenge.
A failure of either same-support implication abandons this reduction. Compare
the sufficient threshold q >= 2^128 * binomial(n,k+1) with the actual 2^-128
budget; a large-field estimate alone is not a resolution at arbitrary q.

Redundancy and failures: L002 proves only the constant-code version; L001 and
C001a address endpoint nonattainment. The stopped single-field disproof is not
reopened. No repeated PDF retrieval or grid-to-real-maximum identification is
needed for this test. The consecutive exploration count starts at zero.

## Saved unfinished reasoning

On a bad support S, b|_S cannot be in the punctured code, since then subtracting
gamma*b from the matching combination makes a|_S a code restriction too.
Every support of size at most k is fully interpolable. Choose k coordinates
B in S and their degree-less-than-k interpolant p for b. Some j in S outside B
satisfies b_j != p(x_j). Then T = B union {j} has size k+1, b|_T is not in
the code restriction, and the original combination still is.

For such a T, the leading coefficient functional of the degree-at-most-k
interpolant is
  h_T(z) = sum_{i in T} z_i / product_{j in T, j != i}(x_i-x_j).
The punctured RS code is its kernel. Thus a bad T forces h_T(b) != 0 and
gamma = -h_T(a)/h_T(b). Each of the N = binomial(n,k+1) supports supplies at
most one challenge, without requiring T itself to meet a smaller radius's
support threshold. For delta >= 1-(k+1)/n, all these certificates are admissible.

A sharpness check belongs to the same counting test: choose b_i = x_i^k, so
h_T(b)=1 for every T. Distinct supports have distinct h_T because every
coefficient on their support is nonzero. Avoid the binomial(N,2) hyperplanes
h_T(a)=h_U(a). The elementary union bound should give such an a whenever
q > binomial(N,2), making all N challenges distinct at terminal radii.
This needs a complete interpolation proof and quantifier review before any
sharpness claim is recorded. No completed result is asserted in these notes.

## Completed assessment

The full argument is now in
[L003](../lemmas/L003-rs-small-support-field-threshold.md). The certificate
reduction succeeds, with a necessary qualification: shrinking a support need
not preserve its radius admissibility. Containment of events still gives the
upper bound; equality of the event with the union of certificate roots holds
only when supports of size k+1 are admissible. The hyperplane argument proves
sharpness there when q > binomial(N,2), uniformly for any distinct evaluation
points. This extra field-size condition is not assumed in the upper bound.

The actual 2^-128 budget gives a sufficient all-radius threshold
q >= N*2^128. A smooth length-16 example over F_(5^64) meets it at all four
rates. At n=256, k=128, this threshold exceeds 2^379, so the result does not
supply a useful universal answer at an arbitrary given field size. The source
bridge and sharp errors at earlier radii remain open.

The auxiliary script exhaustively checked 16,369 input-pair classes modulo
codeword translations across six small parameter sets, with direct polynomial
code enumeration independent of the certificate formula. Every support and
challenge was checked, including empty supports and zero directions. An
explicit F_101 example has ten distinct certified roots; the integer threshold
comparisons also passed. These checks support the written proof but do not
replace it. Outcome: ADVANCE for a relevant model-only mathematical input,
with consecutive exploration turns reset to zero. No complete challenge
candidate or sharp-radius solution is claimed; the current continuation is
recorded only in PROGRESS.md.
