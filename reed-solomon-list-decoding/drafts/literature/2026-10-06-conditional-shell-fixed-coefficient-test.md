# Conditional (67,68)-shell diagnostic — source-ready proposal

TARGET: Test AVZ Proposition 17 on shells (67,68) of L022's unchanged pair witness using the fixed head-weight partition and integer shortening upper coefficients.
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact-target discovery and original-source retrieval recorded in drafts/literature/2026-10-06-conditional-bounded-shell-review.md; scoped prior scalar, mixed-block, cap-10 and incompatible-shell stops contain no conditional fixed-pair test.
SOURCE_EVIDENCE: Direct primary manuscript https://publications.lib.chalmers.se/records/fulltext/local_14986.pdf, June 24, 2000; AVZ Proposition 17 and complete proof, Lemma 18, printed pp. 9–11; Theorems 22,26–27,32,36, pp. 12–14,16–17, and one-block Theorems 8–9, pp. 6–7. Corroborating restatement https://arxiv.org/pdf/1212.3467v1, Kim–Toan Theorem 21, pp. 16–17. Canonical source detail is foundations/06-conditional-shell-source.md.
COMPARISON: Conditional punctured-shell bounds differ from ordinary individual caps and L025's four-block small-residual rows; published head-weight splitting and shortening suffice for fixed certified upper coefficients, but possibly smaller exact packing maxima and stronger source bounds are not evaluated.
GAP: Certify the prescribed integer coefficients, choose the actual ratio branch and evaluate its necessary rows exactly; no coefficient strength, exclusion or feasibility assertion is presently available.
REASON: One fixed pair with source-covered orientation and proof cases gives an independently testable diagnostic without changing the witness, extending the old cap or selecting another individual PSD block.
SCOPE: Only the exact TARGET, n=1024,w=68,v=956,d=10,i=67,j=68, and the coefficient prescription below; no optimization, retuning, additional shell pairs or exact-maxima claim.

The main gap remains arbitrary-center safety at 68 agreements and
955<=t_star(m)<=957. Essential local inputs are L021, L022, L023's full
scalar supplement, L025, C001a and foundations/04–06. Preserve L024's
independent stop and ATTEMPTS/017. Source review established coverage;
this newly written continuation needs separate approval next turn.

Use B_(2a)=binom(68,a)binom(956,a)p_a=a_a^*/2 for a=67,68,
exactly as L022 specifies, with no assumption of actual packing or
full-SDP feasibility. Set δ=5 and Δ=63. Verify the index hypotheses
and i+j<=n-δ rather than transferring Theorem 17's failed prerequisite.

Prescribe R_d on one or two (weight,length) blocks for d=8 or 10.
Complement each block to u=min(b,length-b), remove zero-weight blocks,
and let S be the remaining total weight. Put R_d=1 if S<d/2,
including the empty tuple. At S=d/2 use min floor(length/u) over
positive blocks. Above this base case use the minimum, over every
positive block, of floor((length/u) R_d(child)), where the child
shortens that block to (u-1,length-1) and normalizes again. Invalid
weights are rejected, not treated as nonempty codes. These are the
published reflection, disjointness and integer shortening rules from
Theorems 8–9,32,36. Justify the induction and boundary cases explicitly
before using an implementation; do not copy L025's cutoff 5 into d=8.

Set P_a=R_10((a,68),(a,956)) for a=67,68. For the two conditional
T' inputs (63,68,4,888,8) and (63,67,5,889,10), prescribe

\[
U'_d(w_1,n_1,w_2,n_2)
=\sum_{a=0}^{63}R_d((a,n_1),(w_1+w_2-a,n_2)).
\]

Use this only for those two displayed inputs, verifying that every
head weight 0,...,63 is admissible. Repeated Theorem 26 with its
parameter e=0 and terminal Theorem 22 supplies the fixed partition
bound; explain that import and its application, without re-proving
Proposition 17. Set P_67,68=min(P_67,U'_8(63,68,4,888)) and
P_68,67=min(P_68,U'_10(63,67,5,889)). This clipping is prescribed
before calculation and keeps both conditional bounds below their
individual caps. All bounds concern maxima, not the relaxed assignment.

Verify positivity of P_67,P_68 and decide the source branch by the
integer sign of P_67,68 P_68+P_68,67 P_67-P_67 P_68. Test both
source rows (62)–(63) if positive, and row (64) otherwise. Retain
the polynomial form, including equality and any zero conditional
coefficient. Check individual-cap slacks separately so an exclusion
is attributed correctly. Record whether both clipped coefficients
equal their individual caps, the source's explicit redundancy case.
Do not claim a general redundancy theorem from a pass on one point.

Save complete pair input values, every head-weight summand, all
reachable recursion states and shortening branches, exact coefficient
identities, branch sign and row slacks in a disk certificate. Independently
reconstruct the two pair values and normalization and verify every
recursive identity, base case, coefficient bound and tested rational
row. Print the actual coefficients, applicable rows, actual/required
slacks, objective/threshold comparison, failures and certificate paths.
No sampled verification or approximate signs suffice.

Continue on a certified violation: it excludes this prescribed pair
witness and every triple extension sharing it, and identifies a
necessary row for a later optimization attempt. It does not prove a
threshold upper bound for all assignments. If all rows pass, or the
fixed prescription reduces to individual caps and those pass, park
this diagnostic; do not retune coefficients or shell pairs in the same
attempt. A computational interruption preserves the certificate and
unfinished induction rather than claiming a pass. Exact T' values,
full-SDP feasibility, actual list realization, 67-agreement safety,
sharpness, exponent m and ABF equivalence remain open. This is a
REPRODUCTION of assessed known tools, without a novelty assertion.
