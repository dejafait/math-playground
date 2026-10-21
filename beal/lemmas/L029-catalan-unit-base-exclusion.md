# L029 — Catalan exclusion of the unit-base boundary

## Hypotheses

Let A,B,C,x,y,z be positive integers with x,y,z>2 and A^x+B^y=C^z. No primitivity hypothesis is imposed.

The external input is the full **Catalan–Mihăilescu theorem**: for integers U,V,m,n all greater than one, U^m−V^n=1 implies (U,m,V,n)=(3,2,2,3). Cite Preda Mihăilescu, *Primary cyclotomic units and a proof of Catalan's conjecture*, **J. reine angew. Math. 572** (2004), 167–195, **Theorem 5, p. 188**, [DOI](https://doi.org/10.1515/crll.2004.048). The complete positive-integer statement is also given in Yuri F. Bilu, *Catalan's conjecture [after Mihăilescu]*, **Astérisque 294** (2004), exposé 909, 1–26, **Conjecture 1.1 and the immediately following assertion that it is proved, printed p. 1**; the square cases and odd-prime formulation are distinguished on pp. 1–2 of the [original PDF](https://www.numdam.org/item/SB_2002-2003__45__1_0.pdf).

Source qualifications: the publisher retrieval of Mihăilescu's paper was unavailable; its published-paper transcription has imperfect OCR. The inspected original Bilu PDF corroborates the full classification, including the square cases. Exact source access and comparison are recorded in drafts/literature/2026-10-07-base-one-catalan-coverage.md and drafts/literature/2026-10-07-base-one-catalan-import.md. The full named theorem is imported; neither its cyclotomic proof nor the historical square-case proofs are independently reproduced. The odd-prime formulation alone is not the input used here.

## Conclusion

Every such solution has A,B,C>1. Equivalently, there is no positive Beal solution with at least one base equal to one, for arbitrary original integer exponents greater than two, even without requiring gcd(A,B,C)=1.

## Proof

First, C cannot equal one: A^x and B^y are positive integers, so A^x+B^y>=2, whereas 1^z=1. Thus C>=2 in every proposed solution.

If A=B=1, the equation gives C^z=2. But C>=2 and z>=3 imply C^z>=2^3=8, a contradiction. This deals with the overlap of the two unit-summand cases; any overlap involving C=1 was already excluded.

Suppose A=1 and B>1. Rearranging the original equation, without changing exponents, gives C^z−B^y=1. Apply the full cited theorem with (U,m,V,n)=(C,z,B,y). Both bases exceed one, both exponents exceed one, and every coordinate is a positive integer. Its conclusion is (C,z,B,y)=(3,2,2,3), which contradicts z>2.

For completeness, the exception cannot have another power representation that evades the original exponent bound. The equality C^z=9 forces every prime divisor of C to be 3, so C=3^k for an integer k>=1. Then kz=2, whose only positive integer solution with z>1 is k=1,z=2. Similarly B^y=8 forces B=2^h with h>=1 and hy=3; with y>1 this gives h=1,y=3. Thus the larger power cannot be represented with exponent greater than two. The exponent x of the unit base is arbitrary and has no effect on this contradiction.

Finally, suppose B=1 and A>1. The original equation gives C^z−A^x=1. The same theorem applies with (U,m,V,n)=(C,z,A,x), yielding (C,z,A,x)=(3,2,2,3), again contrary to z>2. The representation argument for 9 applies unchanged, and the representation of 8 now gives A=2,x=3. The unit exponent y remains arbitrary.

These cases exhaust every position and overlap of a unit base. The attained threshold is zero positive solutions on this boundary. Primitivity, pairwise coprimality, exponent-divisor reduction and signed-power conversions were not used. In particular, L002 is contextual rather than a mathematical input. This is a specialization of a known theorem, not progress beyond the cited classification. The infinitely many residual signatures with all bases greater than one, and the exceptional-algebra and packet-exhaustion gaps in the mixed-seventh route, remain unresolved.

### Critical application audit — 2026-10-07

The separate audit reuses drafts/literature/2026-10-07-unit-base-application-audit.md and the source-access qualifications above; it does not audit the cyclotomic proof. The case partition is exhaustive: first C=1; then C>1 with A=B=1, A=1<B, or B=1<A. These include every nonempty set of unit positions. Both source bases exceed one before the theorem is applied. In either single-unit case the larger consecutive power is C^z, so the exponent forced to two is the original right-hand exponent, not the exponent of a unit base.

Even before imposing exponent bounds, all positive integer base/exponent pairs representing 9 are (9,1) and (3,2): unique factorization gives base=3^k and k times the exponent equal to 2. All such pairs representing 8 are (8,1) and (2,3), since base=2^h and h times the exponent equals 3. A base of one represents neither value. Thus no representation of the larger exception survives z>2. The cited tuple classification already implies this; the enumeration is an applicability check, not a new exclusion.

No failed clause, missing local mathematical input or required correction was found. The conclusion, proof scope and empty local-input DAG row are unchanged. The zero-solution threshold is met only on the unit-base boundary; all-bases-greater-than-one cases remain independent.

## Mathlib

Full matching coverage of Catalan–Mihăilescu and this unit-base consequence: **not checked**. Supporting prime-factorization and power declarations: **not checked**. No absence claim or formal-verification claim is made.
