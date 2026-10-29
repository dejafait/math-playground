# L130 — The marked elliptic quotient has no rational three-isogeny

## Hypotheses

Use L112's actual nonsingular short model over Q,

    E': y²=x³+a x+b, a=−2874960, b=1739350800.

No minimality, rank upper bound, rational kernel point, complete Selmer
group or primitive integer solution is assumed.

## Conclusion

E' admits no isogeny of degree three defined over Q. Its three-division
polynomial has no rational root. This excludes the proposed rational
three-isogeny descent shortcut, not general three-descent. It supplies
no rank upper bound, marked-point classification or Beal exclusion.
L112's Q-isomorphism transfers the result to its original elliptic
quotient with the specified origin.

## Proof

### Imported criterion and specialization

Import J.E. Cremona, *Algorithms for Modular Elliptic Curves*, second
edition, CUP 1997, corrected online edition, Chapter III Section 3.8,
printed p.99, [author's Chapter III](https://johncremona.github.io/book/fulltext/chapter3.pdf).
For a nonsingular short model over Q, a rational three-isogeny exists
exactly when psi3(X)=3X⁴+6aX²+12bX−a² has a rational root. This is
the rational subgroup criterion; its two nonzero kernel points need
not themselves be rational. We import this criterion without reproof.
L112 supplies its hypotheses; independently the discriminant is
−16(4a³+27b²)=213864120124199424000, nonzero. No twist replacement,
model change or j-invariant comparison occurs. Exact substitution gives

    psi3(X)=3X⁴−17249760X²+20872209600X−8265395001600.

By the named rational root theorem, a reduced root m/n has n>0,
n dividing 3, and m dividing the nonzero constant −a². Thus m is
nonzero and n is 1 or 3; both numerator signs must be retained.

### Complete finite certificate

Exact factorization, checked by two different trial traversals, is

    |a|=2⁴·3³·5·11³, a²=2⁸·3⁶·5²·11⁶.

The products are verified exactly. Primality is checked by trial division
through each factor's square root: empty ranges for 2,3; divisor 2 for
5; divisors 2,3 for 11; none divides. Every positive divisor is uniquely

    d=2^i 3^j 5^k 11^l,
    0<=i<=8, 0<=j<=6, 0<=k<=2, 0<=l<=6.

There are 9·7·3·7=1323 such divisors. Enumerate m=±d and n=1,3,
discarding only gcd(m,n)>1. Of 5292 raw candidates, exactly 2268
are discarded (n=3 and j>=1), leaving 3024: 2646 with n=1 and
378 with n=3. Evaluate each as an integer using

    H(m,n)=n⁴ psi3(m/n)=3m⁴+6am²n²+12bmn³−a²n⁴.

The complete evaluation has no zero residual. Its minimum absolute
residual is 401657211648>0. Hence all possible rational roots fail.

Run, from this notebook:

    python3 scripts/pair-genus-two/three_isogeny_eligibility.py

Full signed numerators, denominators and exact residuals are in
`scripts/pair-genus-two/three-isogeny-eligibility-certificate.json`, field
`all_reduced_candidates_and_residuals`. Certificate SHA-256:
`2e10573b933d85f115ec98738fbd36f6a817a6d55bdb2e9e385a11253edff179`.

The producer builds divisors multiplicatively, traverses magnitude/sign/
denominator and evaluates expanded H. The replay independently factors
|a| by odd-divisor traversal, traverses denominator/exponent tuple/sign
in a different order, rejects exactly n=3 with m divisible by 3, and
evaluates H by the different expression

    (((3m)m+6an²)m+12bn³)m−a²n⁴.

Every replay key is unique; its complete key set equals the producer's,
and every corresponding residual agrees exactly. Both zero sets are
empty. This complete comparison is executed by the script, not inferred
from a preview of the residual list. The full summary and two-run
ledger were inspected. Neither run had mathematical check failures;
no sieves, backend probes or truncated enumerations occurred.

Before the factor loops, both traversals were bounded together by 3434
trial divisions; after factorization, explicit primality tests were
bounded by 6 further divisions. Before either candidate loop, both
passes and postprocessing were bounded together by 40·1323=52920
work units. The traversal costs 2·(5292+3024)=16632; six additional
record passes are conservatively charged 6·3024=18144 units for table
construction, set construction/comparison, zero filtering, and minimum
filtering/reduction. Total charge per execution is therefore 34776.
The first ledger omitted those postprocessing passes. The original
certificate is preserved in
`scripts/pair-genus-two/three-isogeny-eligibility-initial-accounting-omission.json`.
The ledger was corrected by 18144 units before rerunning the corrected
script. Both complete executions are included: actual cumulative work
is 84 factor trials and 69552 candidate work units, against unchanged
caps 10000 and 200000. Even the corrected first-run preflight bound
fits the cap; no cap violation occurred. The persistent ledger is
`scripts/pair-genus-two/three-isogeny-eligibility-ledger.json`; reruns
accumulate rather than reset its counters.

The imported criterion proves the conclusion. The prior assessment is
`drafts/literature/2026-10-25-marked-elliptic-three-isogeny-eligibility.md`
(SPECIALIZE). This is an exact-instance reproduction of known methods,
not a new general theorem or a novelty claim. It closes only this
shortcut. Global arithmetic for other descents, upper ranks, marked
lifts, integer recovery and other signatures remain unresolved.

## Mathlib

Full matching criterion and instance coverage were not checked in
Mathlib. The rational root theorem is a standard imported input; no
matching Lean theorem, absence from Mathlib or formal verification is
claimed. This is an informal exact computational certificate.
