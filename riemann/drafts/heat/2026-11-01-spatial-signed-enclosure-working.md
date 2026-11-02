# Approved capped signed spatial calculation

Completed bounded attempt: INCONCLUSIVE. The unchanged SPECIALIZE assessment is
`drafts/literature/2026-11-01-spatial-signed-entry-enclosure-scope.md`.
Only its exact COVERED_TARGET is attempted. Existing work is preserved.

Main gap: actual-Xi signs at all heights. Intermediate target: one full
closed positive-time interval with every canonical cutoff entry. Its
downstream use is qualified finite collision exclusion, with neither
all-height nor zero-time transfer. The strict test is the complete
two-charge cost below r0 on every covered piece. All stated hard caps
apply; partial coverage is INCONCLUSIVE and parks this estimator.

Implementation plan: use eta as the real local coordinate (strictly
increasing by L495), and demodulate by exp(i*eta*h0), with h0 fixed
between the block log frequencies. Keep the primitive and centered
log-weighted polynomial together through degree 16. Enclose sigma over
the whole original cutoff cell as an interval parameter; hence no
unproved approximation of its x dependence enters the coefficients.
Taylor's order-17 remainder is bounded throughout each eta subcell.
The carrier has unit modulus; conservative R0,J0,ell0 inequalities
explicitly charge restoring it and the Euler factors. This does not
assert cancellation in the Euler product or in the final conjugate term.

Reuse C499c's audited log enclosures, exact parameters, input hashes,
and C499d's independently uniform charge interfaces, not their endpoint
increment. Source proofs remain unaudited. No new literature is needed.
The available Python environment has no flint, mpmath or gmpy2. Use
exact integer endpoints on a 2^-256 grid, count scalar interval operations,
and store full finite coefficients, remainders, range bounds and failures.
No binary floating-point mathematical data are accepted.

## Retained specialization and unfinished obligations

For each fixed cutoff q, enclose x on the outward closed superset of
its canonical cell. L495 gives eta'>0, and L496 gives sigma'>0.
Compute interval enclosures for sigma and eta from C499c's exact
real-axis formulas. Choose a fixed real h0 between the block's log
frequencies, and write delta_j=log(j)-h0. For an independent parameter
s in the sigma interval define

    P(y,s)=sum_(n<j<=q) exp(t*log(j)^2/4-s*log(j))
                          *exp(-i*y*delta_j),
    V(y,s)=sum_(n<j<=q) delta_j*exp(t*log(j)^2/4-s*log(j))
                          *exp(-i*y*delta_j).

At y=eta(x), s=sigma(x), the original sums are
DeltaS=exp(-i*eta*h0)*P and
DeltaL=exp(-i*eta*h0)*(h0*P+V). This substitution restores the
carrier exactly, without differentiating a varying sigma as though it
were constant. The interval parameter s ranges independently: its
overenclosure contains every actual pair (eta(x),sigma(x)).

For eta centre e and half-width r, use u=(y-e)/r in [-1,1].
Degree-16 coefficient enclosures are the signed sums of

    w_j(s)*exp(-i*e*delta_j)*(-i*r*delta_j)^k/k!.

Multiplication by delta_j gives V's coefficients. Each real/imaginary
Taylor remainder is bounded by
sum_j w_j,upper*|r*delta_j|^17/17!, with one further |delta_j|
for V. These partial-y derivative bounds hold throughout the eta
piece for every s in its interval; they are not asserted to be total
derivatives of P(eta(x),sigma(x)). The cited real-component Taylor
formula and finite-expression containment cover this parameterization.
Shared signed sums are formed before real/imaginary Horner range
enclosures and modulus bounds are taken. C499c's exact DeltaG formula
and C499d's Euler envelopes then give the sufficient bound

    B <= R0*((1+2*(h0+J0)/ell0)*|P|+2*|V|/ell0).

Here h0>0; the inequality explicitly discards the carrier phase only
after reconstruction, and does not assume favorable Euler phases or
replace actual ell by an unrelated phase. The independently uniform
U_s and U_r are replayed from C499d's formulas with the full support,
both saddle terms and full epsilon_1. No signed sum reduces those charges.

The producer first used unnormalized eta differences. Tiny high-order
coefficient intervals rounded on an absolute grid were amplified by
large radius powers. It was interrupted to normalize the coordinate;
all 137049390 operations and 39663 evaluated/started enclosures from
that run remain charged. The interrupted manifest's IN_PROGRESS and
“all canonical cells covered” default banner were misleading; they
are preserved in `scripts/heat/spatial-signed/pre-normalization.json`
and explicitly corrected by the final manifest. No full-coverage claim
follows from that banner. An initial zero-operation provenance-key error
was repaired and preserved separately as `startup-key-error.json`.

The normalized continuation stopped at exactly 268435456 operations,
with 50975 evaluated/started Taylor enclosures plus two empty-cell tests (50977 total cases), no 512-bit replay, no depth
over 16, and no producer implementation failures. Both interrupted
and final partial cells, all attempts and all elementary enclosures
are retained. Complete root records exist for q=691005,...,691086,
with 18208 final covering leaves; q=691087 is unfinished. The initial
q=n cell has an exact zero increment. Coverage at q=N and the rest of
the prescribed interval was not obtained. The maximum completed-cell
recorded cost upper bound is .00041324640051515739150849692, against
reserve lower .00042249381587054327798642829. This is producer evidence
only, not an independently audited partial exclusion theorem.

The separate ledger checker consumed every recorded complete/partial
leaf, all root hashes, interval ordering, dimensions, final scalar
thresholds and counters: 923 checks, zero failures. It performs no new
enclosure evaluations or scalar interval arithmetic and does not
reconstruct elementary bounds, coefficients or their Taylor remainder
arithmetic. It therefore does not certify the mathematical producer.
Two started but uncompleted evaluations account for the interrupted and
capped leaves. Complete evidence: `scripts/heat/spatial-signed/certificate.json`
and `scripts/heat/spatial-signed/ledger-check.json`.

Decision: park this capped estimator. Its full prescribed comparison is
unresolved; cap exhaustion is not an envelope lower bound, collision,
RH counterexample or proof of a general cancellation obstruction.
Outcome EXPLORATION, REPRODUCTION: a known-method finite test with no
completed new mathematical input. No lemma, PROOF or DAG change is needed.
Any later use of the partial scalar successes requires a separate
coefficient/remainder audit. The next nomination concerns a different
central mechanism and has REVIEW_REQUIRED, with no source approval here.
