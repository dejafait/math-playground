# Prescribed zero-padding rank-two update — stop2054

21 November 2026. The single approved N=6-to-7, principal-index
{0,1,2} test rejects rank(D_6)<=2. See the full proof and exact
qualifications in [C029x](../lemmas/C029x-consecutive-newton-hermite-rank-two-obstruction.md)
and `scripts/pollaczek/consecutive-hermite-rank-2054.json`. All 28
checks pass; the minor's determinant is strictly negative. The new
implementation still needs its independent audit.

WHY IT FAILS: The actual full Jensen weights change the Newton-sum
forms enough that their prescribed monomial zero-padded difference
already has a nonzero 3-by-3 principal minor. Rank at most two would
force every such minor to vanish. This stops only this rank bound
at this pair, not an eventual-only identity or another independently
specified mechanism. It is distinct from C029q's affine-quotient
Bezoutian embedding and leaves its evidence and stops2042/2044/2047
intact. Even a different low-rank identity would still require signed
control, initialization and uniformity before C029m could apply.
No further minor/degree/precision test is authorized by this attempt.

21 November 2026, audit2056: the fixed stop is now independently audited
in C029x. All 108 checks pass; complete original endpoints, matrices,
padding and both rational witnesses agree. A separate formal
logarithmic-derivative reconstruction also encloses every moment.
See `scripts/pollaczek/consecutive-hermite-audit-2056.json`. This
validates the finite stop only; its original scope is unchanged.
