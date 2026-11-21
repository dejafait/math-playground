# Prescribed Hermite family fails the original coefficient cap

11 November2026, step389. WHY IT FAILS: upper-node derivative matching
forces exponentially large original monomial coefficient norm despite
the successful uncapped residual. Full proof and the n>=4096 onset
are in [C997x](../lemmas/C997x-prescribed-hermite-jets-exceed-coefficient-cap.md).
The original exp(sqrt(n)) cap is eventually violated.

This stops these coefficients only; it neither refutes C997w nor
bounds the capped infimum over other coefficients. Step390's independent
audit accepts this scoped stop. Reopening requires changed input avoiding these exact
jets while proving a complete residual bound and paying the cap;
rescaling without a residual proof is not a continuation.
