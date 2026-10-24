# L094 — Independent cyclic-order rigidity for d=6,...,33

## Hypotheses

Fix an integer 6<=d<=33. Take all 25 indexed pairs of L055, changing
only H_0=40-d and H_24=32670621+d. Every J_i is unchanged.
Put r=25, B=9250245 and kappa=23/11. Let b_i be nonnegative
integers with sum b_i=B, set a_i=2+18b_i, and let pi be any
permutation of {0,...,24}. Suppose real s_0,...,s_25 satisfy
s_25=s_0, s_k>=540/11 and, for every 0<=k<25,

\[
s_{k+1}=2^{-a_{\pi(k)}}(G_{\pi(k)}s_k-Q_{\pi(k)})+\kappa,
\quad G_i=(27/16)^{J_i}(3/2)^{H_i},
\quad Q_i=(12/11)(3/2)^{H_i}+1,
\]
\[
4J_{\pi(k)}\log2\le\log s_k+\log(11/4).
\]

Each indexed outgoing pair retains its own allocation and input.
All logarithms are natural. No H guard, seed, minimum location,
integer junction, actual word, parity, residue, exact valuation or
primitive-count assumption is made.

## Conclusion

For every specified d and every allocation in the full integer
simplex, every feasible cyclic order is a rotation of 0,...,24.
More precisely, rotation to any smallest designated junction makes
pi the identity. Tails equal to 2 and repeated junction values are
included.

This is a local RESEARCH/REPRODUCTION application of audited L075
and L084 data under the prior SPECIALIZE assessment
`drafts/literature/2026-10-22-uniform-independent-cyclic-order.md`.
It supplies no new ordering mechanism or advance beyond those inputs.
The separate critical applicability audit below found no defect. No tuple feasibility,
all-order real exclusion, actual-word exclusion or universal eventual
descent is concluded. Assembly with C093a is a separate task.

## Proof

Fix d as in the hypotheses. Apply L075 independently of the full
C077a conjunction. The following matches all its conditions (1)–(7).
Only L055's indexed pair table is imported from that witness lemma;
its H/seed, minimum and primitive-count conditions are not premises.

**Table and budget, L075 (1).** These are exactly L084's d table
and budget. The unchanged J list is strictly increasing, with J_0=8.
Here H_0>=7 and all other H_i>=72, so every H_i>=3. L084's
completed step-337 all-member reconstruction gives

\[
\sum J_i=66061058,\quad\sum H_i=199390205,\qquad
K=397573379,\quad N=630138897.
\]

The opposite H changes preserve these sums. In particular N is exactly
sum_i(4J_i+H_i)+2r+18B, independently of order and allocation,
and sum_i a_i=166504460. These are the identical totals in L075 (1).

**Independent analytic tests, L075 (2).** Use exactly L084's O constants

\[
\lambda=10584/10^{14}=1323/12500000000000,\quad T=27,
\quad\ell=693147180559/10^{12},\quad
u=1098612288669/10^{12},\quad v=2.
\]

The completed L084 analytic audit proves
0<lambda<Lambda=N log2-K log3, 0<ell<log2, log3<u and
log(11/4)<2. Its O cap is

\[
U=23r/(11\lambda)+23/11
=7187500000030429/14553
<500000000000<P(27)<\exp(27),
\quad P(27)=\sum_{j=0}^{40}27^j/j!.
\]

Thus every part of L075 (2) holds with these independent constants.
No support, cutoff or H cap is used. The analytic evidence is imported
from that completed audit, not inferred from decimal approximations.

**All tail-2 offsets, L075 (3).** L084's all-member O audit certifies
all 25 negative offsets through d=35, containing the present range.
More explicitly, its row-i record uses H_floor=min(H_i,72) and
the upper enclosure
81/44-(3/11)(3/2)^H_floor. The expression decreases with H,
so this is an upper bound on the actual tail-2 offset. At row0 it
is exact, with H_floor=40-d>=7; at every other row H_floor=72.
These are precisely L075 (3)'s operands, and all are strictly negative
by the audited signs (also covered by L075's H>=5 sufficient sign
check). The changed final row24 is included. The failed tail-20
support datum is a different test and is not invoked.

**Every changed prefix and margin, L075 (4)–(5).** For k=0,...,23,
let A_k(d)=sum_(i<k)(3J_i+H_i) and
D_k(d)=sum_(i<k)(4J_i+H_i+2). These are exactly the complete
incoming prefixes in L084's O records. Its all-member audit reconstructs
every such operand and verifies

\[
A_0(d)=D_0(d)=0,\qquad
A_k(d)=A_k(1)-(d-1),\quad
D_k(d)=D_k(1)-(d-1)\quad(1\le k\le23).
\]

Each nonempty prefix contains changed row0 and excludes row24.
Consequently the already audited margin shift gives
M_0(d)=M_0(1) and M_k(d)=M_k(1)+(d-1)(u-ell) for 1<=k<=23,
where M_k(d)=4J_(k+1)ell-27-2-A_k(d)u+D_k(d)ell is exactly
L075 (5). The audit certifies u>ell and all d1 margins, whose
minimum is attained at the empty prefix. Hence all 24 tests for
each of the 28 tables are strictly positive, with

\[
\min_{6\le d\le33,\ 0\le k\le23}M_k(d)
=60\ell-29=629441541677/50000000000>12.58.
\]

The final eligible prefixes are
A_23(d)=144318712-d and D_23(d)=162928789-d, rather than
the d0 or d5 prefixes. No prefix is omitted: k=0 is the empty
case and k=23 is the last possible first displacement. These
are imported audited identities and signs, specialized to the
specified range, not a reconstruction or tuning of the certificates.

The complete finite O operands for any such d are at
`/tables/(d-1)/O` in
`scripts/postspell-word-count/h-transfer-family-certificate.json`,
with independent counterparts at `/reconstructed_tables/(d-1)/O` in
`scripts/postspell-word-count/h-transfer-family-audit-certificate.json`;
here `(d-1)` denotes the array index. Their mathematical verification
is L084's completed all-member audit, including its analytic and
all-O passages. L084's display (4) alone, scoped to d<=4, is not
the imported coverage for these changed tables. No summary flag or
bounded certificate preview is used as verification.

**Proposed tuple, L075 (6)–(7).** The b_i, pi, a_i, lower domain,
all 25 endpoint equations, s_25=s_0 and non-strict own-input
J guards in the hypotheses coincide literally with L075 (6)–(7).
Data certificates are not substituted for these tuple assumptions.
All hypotheses of L075 now match on the same d, table and budget,
so its conclusion proves the asserted cyclic-order rigidity.

L075's existing proof retains every actual allocated tail in the full
product and compares tails only at actual lower-domain inputs. Its
rotation carries each outgoing pair and allocation with its input,
retaining the old closing edge and the new closing edge, including
tail 2 and repeated values. No minimum at indexed row0 is assumed.
No general criterion or first-displacement proof is reproved here.

The upstream formal-affine input, already specialized in L075, is
Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239, section 2, equations (2)–(4),
Lemma 2, pp. 228–229
([primary paper](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf)).
Only formal real affine algebra is imported; no integer itinerary
realization is needed. The audited positive-real analytic inputs are
NIST DLMF [4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.2.19](https://dlmf.nist.gov/4.2.E19) and
[4.6.4](https://dlmf.nist.gov/4.6.E4). Their inspected domains and
rational remainders are reused through L075/L084, without a new source
retrieval or a current-release claim.

L089 covers only d5 and supplies no changed-range premise here.
Attempt 032's stop for the failed full conjunction remains valid;
this independent O implication neither invokes nor repairs it.
Both original d0 rational witnesses remain valid. No assembly with
C093a or actual-word application is performed, and entry, arbitrary
tables, other cycles, divergence and universal descent remain open.

### Independent critical applicability audit — 2026-10-22, step 406

Under the prior SPECIALIZE assessment
`drafts/literature/2026-10-22-uniform-independent-order-critical-audit.md`,
the verdict is no defect in this application of L075 (1)–(7), for exactly
the stated 28 tables and full integer allocation simplex. This establishes
local reliability of an existing reproduction, not a new ordering theorem,
an additional exclusion, or progress beyond the inspected sources. The
primary affine and analytic coverage cited above is reused. No optimizer
theorem, parity converse or failed full C077a conjunction is imported.

**Table and independent analytic premises.** Read L055's complete pair
table and L075's entire statement, proof and completed audit, together
with L084's completed all-member reconstruction and analytic/O audit.
The unchanged J list is strictly increasing from 8; the changed H_0
ranges from 34 down to 7, and every other H_i is at least 72. Thus all
integer domains in L075 (1) hold. Both opposite H changes are retained,
so sum J=66061058 and sum H=199390205. Direct summation gives exactly
K=397573379 and N=630138897, with sum a=50+18B=166504460.
These totals concern every allocation and order, not an original witness.

The O constants match L075 (2) exactly. L084's audited positive-real
logarithm endpoints imply ell<log2, log3<u, log(11/4)<2 and
lambda<Lambda. The lower Lambda endpoint uses the lower log2 endpoint
and upper log3 endpoint with the positive coefficients N,K; the upper
endpoint uses the opposite choices. Their complete rational operands
were matched, retaining cancellation errors. The full cap equals
7187500000030429/14553<500000000000. The independently summed degree-40
positive exponential polynomial at 27 equals
1112436109266660239093546627471481746956608769015849/
2106019961293006716393905717248000000000 and exceeds 500000000000.
Its positive omitted terms imply P(27)<exp(27). Thus the O minimum cap
has the required direction. The log-series validity and outward remainder
proofs are imported from the completed L084 audit, not independently
reproved here; no S/C/H cap substitutes for this O cap.

**Complete finite applicability evidence.** The bounded checker
`python3 scripts/postspell-word-count/audit_uniform_independent_order.py`
independently transcribes the canonical 25 pairs, changes only the two
specified H entries, and reconstructs every relevant rational O operand.
Its complete evidence is
`scripts/postspell-word-count/uniform-independent-order-audit-certificate.json`.
For every d=6,...,33, it compares the entire rows/counts/Lambda/O objects
against both original certificates, with exact dictionary equality rather
than selected entries or stored PASS flags. It records all operands,
relations, failures and hashes of the input certificates. All 4661 checks
pass with zero failures, covering 700 offsets and 672 margins. These
are verification counts, not counts of distinct mathematical results.
The complete selected d6 margins, d33 boundary operands, Lambda interval
and exponential sum were also inspected without truncation; the all-member
check reads every relevant value, not a preview.

For every offset, H_floor=min(H_i,72)<=H_i and the base 3/2>1 make
81/44-(3/11)(3/2)^H_floor an upper bound on the actual offset, with
the correct direction after subtraction. At row0 this is exact; its
largest value over the specified range is -3969/1408 at d=33. At all
other rows H_floor=72, including the changed row24, and the upper bound
is negative. Thus all 700 comparisons certify L075 (3). In particular
the positive tail-20 offset responsible for Attempt 032 is never used.

For L075 (4)–(5), the empty incoming prefix is exactly zero. Every
nonempty eligible prefix includes row0 and omits row24, giving the
stated -(d-1) shifts relative to d1 in both exponents. Substitution
therefore adds +(d-1)(u-ell) to its margin; u-ell>0. All 24 operands
per table were freshly summed and their shifts checked. At k=23 they
are exactly A=144318712-d and D=162928789-d, including d33 values
144318679 and 162928756. Their margins are positive, as are every
earlier margin. The minimum in every table is the empty-prefix value
60ell-29=629441541677/50000000000>12.58. Since J is increasing and
ell>0, L075's weakest row k+1 comparison covers every displaced row
j>k. The last displacement k=23 can carry row24; a permutation cannot
first differ at position 24. No changed prefix or endpoint is omitted.

**Tuple hypotheses, rotation and conclusion.** Every real-tuple premise
of L075 (6)–(7) is explicit in L094: b_i are nonnegative integers of
sum B, a_i=2+18b_i, pi is a permutation, all inputs have s>=540/11,
all 25 exact endpoints close, and each non-strict J guard uses that
same outgoing indexed row's own input. The lower domain gives
n=s-23/11>=47, so the positive-coordinate product and actual-input
tail comparison in audited L075 apply. All actual allocated tails remain
in the product, including any tail 2 at either closing cut.

More explicitly, for any minimum occurrence q in chronological order,
the rotated input x_k=s_((q+k) mod 25) carries outgoing row
pi((q+k) mod 25) and its same b and a. The old closing edge is at
new position 24-q; the new closing edge is old edge (q-1) mod 25.
For q=0 these cuts coincide and retain the original closing equation;
q=24 is also covered. Own-input guards keep the same two sides under
this reindexing. Coincident junction values remain separate occurrences,
so ties and repeated values cause no loss of an equation. L075's strict
first-displacement contradiction then applies to this minimum rotation
and forces its permutation to be identity. No minimum at indexed row0
was assumed before the theorem. Undoing the rotation gives exactly
L094's conclusion, without a feasibility claim.

No H guard, seed, integer junction, primitive-count or realization premise
is needed. L089 remains only the d5 comparison, not a changed-range
input. Attempt 032 and both d0 witnesses retain their original scopes.
The argument, hypotheses and direct inputs L055,L075,L084 are unchanged;
DAG and PROOF are not edited for audit status alone. This canonical
audit supersedes their pending-audit wording for L094. Assembly with
C093a, actual-word transfer and universal eventual descent remain separate
unresolved work. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage for this simultaneous cyclic-order application
is unchecked. Supporting finite-product and positive-real logarithm
facts do not constitute a matching theorem. Unknown coverage is not
evidence of absence, and no formal verification is claimed.
