# L044 — Derksen's prescribed finite bound misses the packing benchmark

## Hypotheses

Let A(n,d,w) denote the maximum size of a binary length-n,
constant-weight-w code with minimum Hamming distance at least d.
Use (n,d,w)=(965,10,9). Apply the prescribed field choice in
Derksen's Theorem 7, with h=4, without field optimization.
The downstream strict benchmark is 19800269675; it is a sufficient
cap-route test, not an RS unsafety threshold.

## Conclusion

The quoted theorem chain certifies

\[
 A(965,10,9)\ge
 \left\lceil\frac{1926341798679305029880}{872582977728}\right\rceil
 =2207631650 <19800269675.
\]

Thus this particular quoted lower bound fails the strict benchmark.
It gives no upper bound on A(965,10,9), no exclusion of larger
ordinary packings, and no conclusion about an unsafe RS list.

## Proof

**Imported input.** Harm Derksen, *Error correcting codes and
B_h-sequences*, [arXiv:math/0311385v1, 21 November 2003](https://arxiv.org/pdf/math/0311385v1),
printed pp. 2–5, Proposition 2/Corollary 4, Theorem 5, Lemma 6 and
Theorem 7. Corollary 4 gives
A(n,2h+2,w)>=binomial(n,w)/c(n,h). Theorem 7 bounds c(n,h)
by mu(q,q,h+1)/(q-1) when n-1 is a prime power; otherwise it
bounds c(n,h) by mu(q,n,h) for the least prime power q>=n.
Lemma 6 requires 0<h<q. In its close-field even case,
n<q<n+h and n+h-q even, its group-size formula is

\[
 \mu(q,n,h)=(q-1)^{q-n}(q^2-1)^{(n+h-q)/2}.
\]

This is an import of the inspected theorem chain, including its
construction theorem, not a reproof of Bose–Chowla or an assertion
that all fibers have equal sizes. The ready IMPORT assessment is
`drafts/literature/2026-10-10-derksen-finite-packing-bound.md`.

**Prescribed field.** The factorizations are
964=2^2*241, 965=5*193, and 966=2*3*7*23.
Each integer has distinct prime divisors (already 2 and 241 for 964,
5 and 193 for 965, and 2 and 3 for 966), so none is a prime power.
For primality of 967 it suffices to test primes at most
floor(sqrt(967))=31. In order 2,3,5,7,11,13,17,19,23,29,31,
the nonzero remainders are 1,1,2,1,10,5,15,17,1,10,6.
Hence 967 is prime and is the least prime power at least 965;
Theorem 7's second prescription applies. The square-root bound
follows from 31^2=961<967<1024=32^2.

**Branch and arithmetic.** We have 0<4<967, 965<967<969,
and n+h-q=2 even. Also 2h+2=10 and 0<=9<=965.
Consequently

\[
 c(965,4)\le D=966^2(967^2-1)=872582977728.
\]

No odd-branch q factor or first-prescription q-1 quotient applies.
The binomial numerator N=binomial(965,9), computed by
965*964*963*962*961*960*959*958*957/9!, is
1926341798679305029880. Exact Euclidean division gives

\[
 N=2207631649\,D+668310116408,\qquad
 0<668310116408<D.
\]

Since c(965,4)<=D and D>0, Corollary 4 gives A>=N/D.
A is an integer, so the positive remainder forces A>=2207631650.
This is smaller than the benchmark by 17592638025. It certifies
failure of this lower-bound test, not failure of packing existence.
Binary weight-nine supports have distance 18-2|B intersect B'|;
distance at least ten is exactly intersection size at most four,
so this is also an ordinary (965,9,5,1) packing lower bound.
There is no need to invoke L042: the preassigned strict comparison
already fails, and no actual-label transfer is asserted here.

**Verification and scope.** Reproduce with
`python3 scripts/finite-packing/derksen_bound.py`.
The complete certificate is
`scripts/finite-packing/derksen-bound-results.json`.
It stores every factorization, all trial remainders for 2,...,31,
the exact branch, numerator, denominator, Euclidean remainder,
ceiling and benchmark. All eleven checks pass; no failed checks
are hidden. The code reloads the full saved certificate and checks
its identity, and the complete primality evidence was inspected.
The identities above supply the mathematical verification; a preview
or approximate quotient is not used as proof. This known-result
application supplies no progress beyond the cited construction.
The graph augmentation mechanism and all other B_h constructions
remain undecided, as do RS realization and 67/68-agreement safety.

## Mathlib

Full matching theorem and supporting finite-field construction
coverage have not been checked. Unknown coverage is not absence.
The import is the precise primary citation above, with its
specialization and integer rounding justified explicitly.
