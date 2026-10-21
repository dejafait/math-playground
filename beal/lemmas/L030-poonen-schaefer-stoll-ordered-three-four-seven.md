# L030 — Ordered (3,4,7) exclusion from Poonen–Schaefer–Stoll

## Hypotheses

Let A,B,C be positive integers with gcd(A,B,C)=1. Bases equal to one are allowed.

The external input is Bjorn Poonen, Edward F. Schaefer and Michael Stoll, *Twists of X(7) and primitive solutions to x^2+y^3=z^7*, **Duke Mathematical Journal 137 (2007), no. 1, 103–158, Theorem 1.1**, [DOI](https://doi.org/10.1215/S0012-7094-07-13714-1). The inspected [author PDF](https://math.mit.edu/~poonen/papers/pss.pdf#page=1), dated July 16, 2006, states the complete classification on p. 1. Its hypotheses are signed integers X,Y,Z, the equation X^2+Y^3=Z^7 and gcd(X,Y,Z)=1; it imposes no nonzero, positivity or conjectural condition.

## Conclusion

The equation A^3+B^4=C^7 cannot hold. This conclusion concerns only this ordered signature; no other placement or exponent-divisor extension is claimed here.

## Proof

Suppose the equation holds and set X=B^2, Y=A, Z=C. Then X^2+Y^3=B^4+A^3=C^7=Z^7 and X,Y,Z are strictly positive integers. A prime divides B^2 if and only if it divides B. Thus any prime dividing X,Y,Z would divide B,A,C, contradicting gcd(A,B,C)=1. This proves gcd(X,Y,Z)=1. Conversely their common prime divisors are exactly those of A,B,C, although this converse is not needed. If a source convention requires pairwise coprimality, a prime dividing any two of X,Y,Z divides the third by X^2+Y^3=Z^7, contradicting their gcd one. No pairwise equivalence for arbitrary triples is assumed.

Theorem 1.1 gives exactly the following 16 signed triples. The table retains every sign individually and records why each fails the necessary conditions X,Y,Z>0 and X a positive integer square.

| Row | (X,Y,Z) | Rejection |
| --- | --- | --- |
| 1 | (1,-1,0) | Y<0 and Z=0 |
| 2 | (-1,-1,0) | X<0, Y<0 and Z=0 |
| 3 | (1,0,1) | Y=0 |
| 4 | (-1,0,1) | X<0 and Y=0 |
| 5 | (0,1,1) | X=0 |
| 6 | (0,-1,-1) | X=0, Y<0 and Z<0 |
| 7 | (3,-2,1) | Y<0 |
| 8 | (-3,-2,1) | X<0 and Y<0 |
| 9 | (71,-17,2) | Y<0 |
| 10 | (-71,-17,2) | X<0 and Y<0 |
| 11 | (2213459,1414,65) | 1487^2=2211169 < X < 2214144=1488^2 |
| 12 | (-2213459,1414,65) | X<0 |
| 13 | (15312283,9262,113) | 3913^2=15311569 < X < 15319396=3914^2 |
| 14 | (-15312283,9262,113) | X<0 |
| 15 | (21063928,-76271,17) | Y<0 |
| 16 | (-21063928,-76271,17) | X<0 and Y<0 |

Rows 5 and 6 are the source's simultaneous signs ±(0,1,1). All other sign pairs affect X alone. Exactly two source triples have all three coordinates positive. In each, the displayed strict consecutive-square inequalities prove that X is not an integer square: a nonnegative integer square cannot lie strictly between n^2 and (n+1)^2. Hence neither can have X=B^2. The actual survivor count is zero, meeting the required zero threshold. This contradiction proves the conclusion, including unit-base cases, without invoking their separate exclusion.

The finite arithmetic certificate is [scripts/three-four-seven-specialization/finite-filter.json](../scripts/three-four-seven-specialization/finite-filter.json). It records every triple, its equation difference and gcd, positivity, and the complete relevant square bounds; all equation differences are zero and all gcds are one. These checks corroborate the transcription and elementary filter. They do not independently prove the source classification's completeness; that is the cited theorem input.

### Source qualifications

The classification is imported, not reproved. The source's full C5(Q) remains undetermined, but its integral-solution subset is completely excluded: Section 7.6 and Lemma 7.8 (author PDF pp. 21–22) require reductions to (1:0:0) or (1:1:1) modulo 2 and to (0:1:0) modulo 3; Section 13 (pp. 41–45) excludes their intersection, with Section 13.7 establishing that the known subgroup has index prime to 14 and explicitly completing Theorem 1.1. The height-10^7 search for full C5(Q) is not the completeness argument used here. The remaining twists are treated in Section 12.3 (pp. 36–41). Descent bounds, modularity, newform calculations and the Magma/PARI computations acknowledged on p. 45 remain cited inputs, without an independent rerun. No BSD, GRH, full-C5 rational-point conjecture, exceptional algebra or cross-notebook hypothesis is imposed.

The prior assessment records an auxiliary Section 12.3.2 text-extraction inconsistency; this application uses the unambiguous Theorem 1.1 list, not that auxiliary displayed set. Source/version and inspected proof-case details are retained in [the scope assessment](../drafts/literature/2026-10-07-three-four-seven-classification-scope.md). The only local rederivation is the required prime-support and positivity/square specialization, which the signed (2,3,7) statement does not itself express. This is progress in the local assembly of known results, not a new classification or a solution of Beal.

### Critical application audit — 2026-10-07

The separate application audit passed without a correction. The primary author PDF's Theorem 1.1 was compared with all 16 rows above, expanding each first-coordinate sign separately and the whole-triple sign on (0,1,1). The substitution identity and prime-support argument were checked directly: for every prime ell, ell divides B^2,A,C simultaneously if and only if it divides B,A,C simultaneously. Thus primitive positive target solutions satisfy exactly the imported theorem's integer and gcd hypotheses, with no appeal to L002 or L029.

Every rejection in the table is necessary under X=B^2>0, Y=A>0, Z=C>0. Rows 1–10, 12, and 14–16 have a zero or negative required coordinate; rows 11 and 13 are the only positive triples. Independently recomputed integer squares give 2211169 < 2213459 < 2214144 and 15311569 < 15312283 < 15319396, with endpoints respectively 1487^2,1488^2 and 3913^2,3914^2. These are strict consecutive-square bounds, so both fail X=B^2. The full [audit certificate](../scripts/three-four-seven-specialization/application-audit.json) independently expands the primary list and checks every prior certificate field, the exact equation and gcd, and these square bounds. All 16 rows agree, there are no failures, and actual survivors equal the required zero. Its complete rows were inspected; no rounded arithmetic or summary-only verification is used.

Lemma 7.8 and Section 8 (author pp. 21–22) were rechecked together with Section 13.7 (p. 45): only the integral-relevant C5 subset is required, and the source proves that subset empty after checking the subgroup index is prime to 14. The unknown full C5(Q) set is not a premise. This is a critical review of the elementary application, not an independent verification of the published descent, sieve or software computations. It confirms the existing ordered exclusion and introduces no new signature, divisor extension or global resolution.

## Mathlib

Coverage of the full classification and ordered specialization: **not checked**. Supporting prime-divisibility, gcd and square-order declarations: **not checked**. Unknown availability is not a claim of absence; the cited theorem is the external mathematical input, and the finite applicability proof is written above.
