# L031 — Remaining positive (3,4,7) placements

## Hypotheses

Let A,B,C be positive integers with gcd(A,B,C)=1. Unit bases are allowed. The external input is Bjorn Poonen, Edward F. Schaefer and Michael Stoll, *Twists of X(7) and primitive solutions to x^2+y^3=z^7*, **Duke Mathematical Journal 137 (2007), no. 1, 103–158, Theorem 1.1**, [DOI](https://doi.org/10.1215/S0012-7094-07-13714-1). The [July 16, 2006 author PDF](https://math.mit.edu/~poonen/papers/pss.pdf#page=1), p. 1, classifies all integer triples satisfying X^2+Y^3=Z^7 and gcd(X,Y,Z)=1. It allows signed and zero coordinates and has no conjectural hypothesis.

## Conclusion

Neither A^7+B^4=C^3 nor A^3+B^7=C^4 holds. Interchanging the summands gives the same exclusions. No exponent-divisor extension is established here.

## Proof

For A^7+B^4=C^3, put (X,Y,Z)=(B^2,-C,-A). Then

X^2+Y^3=B^4-C^3=-A^7=(-A)^7=Z^7.

These are integers with X>0,Y<0,Z<0 and X a positive square. For every prime ell, ell divides all three of X,Y,Z if and only if it divides B,C,A: squaring and negation preserve prime support. Thus gcd(X,Y,Z)=1. No sign change of a fourth power is used.

For A^3+B^7=C^4, put (X,Y,Z)=(C^2,-A,B). Then

X^2+Y^3=C^4-A^3=B^7=Z^7.

Here X>0,Y<0,Z>0 and X is a positive square. The identical prime-support argument proves gcd(X,Y,Z)=1. If pairwise coprimality is desired, a prime dividing any two coordinates divides the third by the source equation; primitivity then excludes it. Pairwise coprimality is not assumed for arbitrary triples.

Theorem 1.1 supplies precisely the following complete list. Each first-coordinate sign is expanded separately; rows 5 and 6 are the simultaneous whole-triple signs of (0,1,1). The table gives one sufficient rejection in each application. Required conditions are denoted 743: X>0,Y<0,Z<0 and X square; 374: X>0,Y<0,Z>0 and X square.

| Row | (X,Y,Z) | 743 rejection | 374 rejection |
| --- | --- | --- | --- |
| 1 | (1,-1,0) | Z=0 | Z=0 |
| 2 | (-1,-1,0) | X<0 | X<0 |
| 3 | (1,0,1) | Y=0 | Y=0 |
| 4 | (-1,0,1) | X<0 | X<0 |
| 5 | (0,1,1) | X=0 | X=0 |
| 6 | (0,-1,-1) | X=0 | X=0 |
| 7 | (3,-2,1) | Z>0 | 1^2=1 < X < 4=2^2 |
| 8 | (-3,-2,1) | X<0 | X<0 |
| 9 | (71,-17,2) | Z>0 | 8^2=64 < X < 81=9^2 |
| 10 | (-71,-17,2) | X<0 | X<0 |
| 11 | (2213459,1414,65) | Y>0 | Y>0 |
| 12 | (-2213459,1414,65) | X<0 | X<0 |
| 13 | (15312283,9262,113) | Y>0 | Y>0 |
| 14 | (-15312283,9262,113) | X<0 | X<0 |
| 15 | (21063928,-76271,17) | Z>0 | 4589^2=21058921 < X < 21068100=4590^2 |
| 16 | (-21063928,-76271,17) | X<0 | X<0 |

For 743 no row meets all required signs. For 374 exactly rows 7,9,15 meet the signs, and each first coordinate is strictly between consecutive squares. If X=k^2 for a positive integer k, n^2<X<(n+1)^2 would imply n<k<n+1, impossible. Hence neither application has a surviving source triple: actual survivors are zero separately, matching the required zero. This contradicts either hypothesized equation. Unit bases are included throughout. Summand interchange follows from commutativity of addition, without moving an even power across the equation.

The full arithmetic certificate is [scripts/three-four-seven-specialization/remaining-placements.json](../scripts/three-four-seven-specialization/remaining-placements.json), reproducible by `python3 scripts/three-four-seven-specialization/check_remaining_placements.py`. All 16 relevant evidence rows were inspected: every equation difference is zero, every gcd is one, both sign filters agree with the table and the three load-bearing square bounds are strict. This verifies local transcription and arithmetic only; classification completeness remains the imported theorem.

### Source qualifications and limits

The classification is cited rather than reproved. The undetermined full C5(Q) set is not a premise. Section 7.6 and Lemma 7.8, author pp. 21–22, restrict the C5 subset relevant to primitive integral solutions by reductions at both 2 and 3. Section 13, pp. 41–45, excludes that intersection; Section 13.7 establishes subgroup index prime to 14 and completes Theorem 1.1. Section 12.3, pp. 36–41, treats the remaining twists. Published descent, modularity, newform and Magma/PARI computations remain cited inputs, not independently rerun. No BSD, GRH or full-C5 conjecture is used. The auxiliary Section 12.3.2 text-extraction inconsistency recorded in [the scope assessment](../drafts/literature/2026-10-07-three-four-seven-classification-scope.md) does not affect the unambiguous theorem list used here.

The [remaining-placement coverage](../drafts/literature/2026-10-07-three-four-seven-remaining-placements.md) and approved specialization assessment delimit this local difference: signed substitutions, prime-support verification and the exact sign/square filters. The result uses no other local lemma, conditional exceptional algebra or cross-notebook input. It adds two fixed-placement applications of known mathematics, without claiming a new classification or a Beal resolution. Independent critical review of this application was completed on 2026-10-07, as recorded below.

### Independent application audit — 2026-10-07

The two substitutions and their prime-support equivalences above were checked independently. The inverse maps on any sign-compatible positive-square source row would be (A,B,C)=(-Z,sqrt(X),-Y) for 743 and (-Y,Z,sqrt(X)) for 374. They recover the original identities and preserve prime support; no inverse is needed because the filters have no survivors. Positivity of A,B,C excludes zero source coordinates even for unit bases. In the expanded source list, rows 2,4,8,10,12,14,16 have X<0; rows 5,6 have X=0; rows 1,3 have a zero coordinate; rows 11,13 have Y>0. The remaining rows 7,9,15 all have Z>0, excluding 743. For 374 their first coordinates obey respectively 1<3<4, 64<71<81, and 21058921<21063928<21068100. These endpoints are 1^2,2^2; 8^2,9^2; and 4589^2,4590^2, so none is a positive integer square.

An independent literal 16-row transcription from the retained Theorem 1.1 list was compared with every field of the original certificate. All equation differences are zero and gcds are one; sign-compatible row sets are empty for 743 and {7,9,15} for 374. Both actual survivor counts are zero, matching the required zero. All full relevant rows of the [audit certificate](../scripts/three-four-seven-specialization/remaining-application-audit.json) were inspected; reproduce it with `python3 scripts/three-four-seven-specialization/audit_remaining_placements.py`. No discrepancy or withdrawn conclusion was found. This verifies the local applications of the cited theorem, including the simultaneous signs in rows 5,6; it does not independently certify the source's descent or computational completeness. The source qualifications above remain essential, and no exponent-divisor extension or uniform Beal conclusion follows.

## Mathlib

Full matching classification and supporting declarations: **not checked**. No claim of absence or formal verification is made.
