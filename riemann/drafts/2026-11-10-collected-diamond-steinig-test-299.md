# Collected coefficient test — completed bounded attempt

Target: the exact review297 C_n at nu=n; prior SPECIALIZE coverage is
ready. Inputs: Ramaré2009 (12)-(18), L998 definitions and its unmerged
obstruction; review296's source comparison. No arithmetic input is used.

For an admissible full exponent vector ell of length r, the first
family has sign (-1)^(r-1), while every ordered split in the second
family has sign (-1)^(r-2). Thus the complete coefficient to test is

    b_n(ell)=(-1)^(r-1) w(ell) [2n (r-1)!/ell!
       - n^2 sum_{k<=ell, sum j k_j=n}
          (|k|-1)! (r-|k|-1)!/(k! (ell-k)!)].

The split weighted sum forces both lengths positive. For r<=n,
all these splits satisfy the total-length restriction. Ordered k and
ell-k are both retained, even if equal. This formula follows directly
from the two defining sums, not from independence of arithmetic factors.

The discriminating balanced-vector test is settled in canonical L999:
the complete coefficient is (-1)^m*3*binom(2m,m)/12^m, of magnitude
at most 3^(1-m). Its ratio to the signed first-family coefficient is
-1/binom(3m-1,m). This parks the natural L998 balanced witness,
without deciding the full C_n limsup. The initial proposed test sought
an exponentially large residue; it found exponential cancellation.

Exact full collection for n=1..12 and direct balanced split sums for
m=1..30 are in scripts/diamond_steinig/collected_mass_299_certificate.json.
The full mass is 1, 4/3, 27/20 at n=1,2,3 and is below 1 for n=6..12.
These finite values are diagnostic only. The general balanced proof
is in L999, not inferred from samples.

Unfinished full-target reasoning: the formal logarithm of
1+sum_j Y_j*t^j/j! converts the untruncated expression into
p_n^2-p_(2n) for reciprocal polynomial roots. L999 justifies only the
cubic extraction needed for its coefficient. A possible different
mechanism is a uniform bound on products of two reciprocal roots,
followed by a bound recovering the sum of absolute coefficients.
No such bound or full-variable/truncation argument is established
here. A fixed-radius Mahler-measure/coefficient-norm theorem is an
unread lead, outside the current finite-arithmetic assessment scope.
Its hypotheses, constants, degree-uniformity, cutoff handling and
coefficient recovery require separate literature review before use.
Do not treat this lead as a proved theorem or an approved continuation.

Downstream: positive rate parks automatic subexponential overhead for
this representation; zero rate permits only a separately reviewed
arithmetic interface. L984(H), actual factor norms, correlations,
Laguerre transfer, prime powers, endpoints, compensation, complements
and regulator/infinite-zero control remain open. Mathlib unchecked.
