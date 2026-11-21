# Cell moments do not lower the prime-only L2 Rayleigh supremum

4 November 2026, step 284. The approved finite-window diagnostic gives
equality of the exactly cellwise-neutral and unrestricted smooth upper
Rayleigh suprema. The full proof and source imports are canonical in
[L743](../lemmas/L743-neutral-prime-delay-rayleigh-supremum.md);
its separate proof audit passed on 4 November 2026, step 285, within
the same fixed-K, unweighted scope.

WHY IT FAILS: For each fixed finite window, simultaneous high modulation
can preserve every arithmetic delay in operator norm. Both moments on
each cell tend to zero, and a fixed smooth two-moment right inverse
corrects them exactly at vanishing unweighted L2 cost. Thus neutrality
alone cannot provide a strictly smaller upper Rayleigh supremum for this
complete prime-delay sum. This is an unconditional arithmetic obstruction,
not a negative Weil vector or a disproof of RH. It does not control the
logarithmic Fourier energy of those modulated tests. A joint estimate
using that energy is a different, still unresolved target; the earlier
conditional summability and signed-tail stops remain unchanged.
