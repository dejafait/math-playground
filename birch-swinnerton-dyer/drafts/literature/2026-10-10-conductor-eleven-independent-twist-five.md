# Conductor-eleven independent twist-five input — source comparison completed

TARGET: Assess an independent nonzero certificate for q=L(E^5,1)/Omega(E^5) for model [0,-1,1,-10,-20], suitable for L028 calibration of audited L039.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the conductor-389 denominator/tail/positive-twist assessment; searched exact 11a1/twist-five/275b1 values and stronger denominator coverage; inspected primary exact-model and nearby exact-value tables, Wuthrich's full Proposition 1 proof, Cremona's previously uncovered negative-discriminant period case and both Fricke cases; checked L028/L031/L039 and ATTEMPTS/023--024 for duplication.
SOURCE_EVIDENCE: Cremona ecdata Table One and exact row 11 a 1 [0,-1,1,-10,-20] 0 5; Cremona Appendix to Agashe--Ribet--Stein Theorem 5.2 (N<60000, exception 990h); Wuthrich arXiv:1608.06423v2 Proposition 1 pp.3--4 and reused Lemmas 4/6; Cesnavicius arXiv:1703.02951 Theorem 2.13 p.9; Cremona corrected second edition (2.6.1)--(2.6.2) p.25, (2.8.3) p.29, Section 2.11 pp.37--39, Section 3.7 p.98 negative-discriminant case and Section 3.9 pp.102--103; Table 4 pp.313/322; Pal arXiv:1012.0094v2 Corollary 2.6 and Theorem 3.2 positive-d proof; DLMF 19.8.1--19.8.5. Direct links and qualifications below.
COMPARISON: Known results cover base-model optimality/Manin constant, torsion-based unitary-cusp denominators, independent twist-series evaluation and the correct one-real-root total-period route. The inspected exact 275B value belongs to its optimal model and does not by itself identify the required minimal-twist normalization. Prefer direct known-method recovery over an unproved isogeny-period transfer; L031's value and three-real-root implementation do not transfer.
GAP: Essential source coverage for one bounded recovery attempt is now complete; specialized denominator B, exact Fricke sign, root/period and full series enclosures, rational isolation and q!=0 remain unexecuted. No q or normalized symbols are established by this review.
REASON: New source comparison resolves the exact-model prerequisites and the essential negative-discriminant period case; the proposed concrete continuation is saved separately for next-turn approval, without deriving or running its mathematics here.
LITERATURE_REASON: Essential exact-model denominator, optimality and period coverage for independent q was expressly excluded by the ready L039 audit and has not been approved for this curve.
SCOPE: Only source comparison for this fixed model and D=5; reuse adequate general source assessments. No uniform twist-supply claim, assumed nonvanishing, BSD value, transfer of L031's numerical ratio or calibration-derived q.

The main gap remains arbitrary-curve rational-rank/complex-order equality.
An independently nonzero q could normalize L039 through L028 and supply
actual all-generator denominators; this is a local input objective, not a
route claimed to solve that main gap. Essential local inputs are audited
L039 and the conditional calibration L028; L031 is a methodological
comparison only, with its exact-model assumptions to be checked anew.

The source review should first check whether a precise existing theorem or
certified published value already supplies the required normalized ratio.
If it does, import it with exact model/total-period matching. Otherwise
assess the known enclosure-and-rational-recovery method, retaining a proved
denominator before isolation, a rigorous total-period interval, and
independence from L039's unknown scale. A displayed decimal or a conjectural
BSD quotient is insufficient. No specialized denominator, sign, ratio or
nonvanishing is derived here.

Continue only if essential coverage can be made ready for one bounded
fixed-input certificate attempt. A proved zero would abandon this twist
choice; an unresolved essential source blocks dependent calculation.
Do not reopen the parked uniform-q access route or repeat conditional
calibration as production (ATTEMPTS/023--024). Independent point and
coefficient witnesses, rational membership, divisible Sha elimination and
arbitrary complex-order comparison remain separate unresolved questions.

## Primary source comparison completed 2026-10-10

**Exact base model.** The primary
[ecdata row](https://raw.githubusercontent.com/JohnCremona/ecdata/master/allcurves/allcurves.00000-09999)
is `11 a 1 [0,-1,1,-10,-20] 0 5`. The
[Table One documentation](https://johncremona.github.io/ecdata/), inspected
at its 2020-11-27 version, identifies minimal coefficients and torsion order.
Import only that model/torsion identification; the rank column is unused.
[Cremona's appendix to Agashe--Ribet--Stein, Theorem 5.2](https://wstein.org/papers/ars-manin/html/node13.html)
proves the optimal-label and Manin-constant-one assertions for N<60000,
apart from the stated label exception 990h. Its complete period/isogeny
verification qualification is retained from the earlier assessment. The
exact coefficient match and N=11 from audited L039 put this base model
within that theorem. No additive-twist Manin-constant assertion is needed.

**Denominator coverage.** Re-read
[Wuthrich, arXiv:1608.06423v2 (23 March 2017), Proposition 1, pp.3--4](https://arxiv.org/pdf/1608.06423v2)
and its full proof, including the nonrectangular lattice and rational
unitary-cusp cases. With strong-Weil constant one, the unitary-cusp bound
is `[r]^+ in c_infinity(E)/(2 #E(Q)_tors) Z`, normalized by the least
positive real period. At denominator five, its definition has M=gcd(5,11)
and Q=11/M; the required coprimality is satisfied. The source does not
certify a numerical value. The later denominator assembly must combine
this bound with the character cycle and total period; no B is derived here.
[Cesnavicius, arXiv:1703.02951, Theorem 2.13, printed p.9](https://arxiv.org/pdf/1703.02951)
was spot-checked with its proof: it retains a new elliptic optimal quotient,
Gamma_1(n) contained in H contained in Gamma_0(n), and p^2 not dividing n.
The squarefree base level 11 meets the last condition at every prime.
This is alternative coverage of the base constant, not a new reproof.

**Changed real-period case.** Read the complete negative-discriminant
paragraph in [Cremona, corrected second edition (1997), Chapter 3,
Section 3.7, printed pp.97--98](https://johncremona.github.io/book/fulltext/chapter3.pdf).
For one real root e3 and conjugate roots e1,e2, put
`z=sqrt(e3-e1)=s+it`, with s>0. The displayed positive real period is
`lambda_1=pi/AGM(|z|,s)`. The preceding discussion identifies a basis
of the full period lattice. L039's negative discriminant places this
instance in this case. Root isolation, square-root branch certification,
AGM brackets and conversion to the total minimal period remain later
implementation work. Reuse
[DLMF 19.8.1--19.8.5](https://dlmf.nist.gov/19.8.i) for positive AGM
iteration and its limit. L031's ordered three-real-root certificate is
inapplicable as written; copying its component factor would be unjustified.

**Twist and analytic coverage.** Re-read both cases and the full oriented
character-cycle calculation in [Cremona, Chapter 2, Section 2.11,
Propositions 2.11.1--2.11.2, printed pp.37--39](https://johncremona.github.io/book/fulltext/chapter2.pdf).
An odd prime away from N is required; the comparison with the Fricke
eigenvalue decides forced zero versus the exponential series. Do not infer
nonvanishing from the allowed sign. Reuse Wuthrich Lemma 4 and its proof
for the full analytic tail, and Lemma 6 only if its finite-precision
hypotheses are used; exact outward arithmetic still needs proof.
The new instance includes bad-prime coefficients already at small n;
the good-prime recurrence from L031 cannot be used at 11.
Read the all-prime recurrence and Fricke sign in the same book's
Section 2.6, equations (2.6.1)--(2.6.2), p.25, and the full Euler product
(2.8.3), p.29. Chapter 3 Section 3.9, pp.102--103, supplies minimal-model
point counts at bad primes and the quadratic-twist/newform identification.
These cover the new coefficient case without reproof or omitted local
factors; the actual coefficients/sign still require exact calculation.
Re-read [Pal, arXiv:1012.0094v2 (21 January 2011), Corollary 2.6,
printed p.6, and Theorem 3.2, pp.7--8](https://arxiv.org/pdf/1012.0094v2),
including the odd-prime/2-adic corollary proof and positive-d proof (3.1)--(3.2).
Minimal E, squarefree d>0, d=1 mod 4 and coprimality to Delta are the
relevant conditions, satisfied by d=5 and L039's Delta=-11^5.
The formula integrates the absolute minimal differential over the entire
real locus. It imposes no positive-discriminant condition on the base.
Apply the cited theorem later with that convention, without an isogeny
period guess or an assumed twist constant.

**Published values compared.** Read
[Cremona Table 4 introduction, p.313, and row 275B, p.322](https://johncremona.github.io/book/fulltext/table4.pdf).
The rank-zero rational-factor column is explicitly exact; it is distinct
from the decimal L/period columns and the BSD-predicted Sha column.
The exact factor there is 1 for the strong Weil curve. The inspected
ecdata model of 275b1 is `[0,1,1,-8,19]`, while the same class also lists
`[0,1,1,-258,-2981]` and `[0,1,1,-195508,-33338481]`.
The table alone gives neither a proved identification of the required
minimal twist nor its period transport from the optimal representative.
No exact q for the present target is imported from that class. The older
linked `allbsd/bsd.1-1000` uses older class letters and also covers optimal
representatives; it supplies no missing period transport. Decimal
recognition and the Sha column are excluded. Direct base-period recovery
avoids this additional model/isogeny comparison. This conclusion is
limited to the inspected sources, not a claim that no published exact
matching value exists.

## Decision, reuse and limits

The ready mechanism is a known-algorithm specialization. New local source
coverage consists of the exact base prerequisites and the previously
unread one-real-root period case. No mathematical certificate, independent
nonzero q or progress beyond the cited results was produced. No reproof of
the imported theorems is proposed. Full matching Mathlib coverage was not
checked; this is not evidence of absence.

Queries included `Cremona 11a1 275b quadratic twist 5 L value optimal curve`,
`11a1 twist 5 L`, `275b1 L`, and `Wuthrich numerical modular symbols
elliptic curves proposition 1 denominator torsion`. Search snippets were
used only as leads. LMFDB returned a CAPTCHA; three guessed table paths
failed. The authoritative linked Table 4 and primary PDFs were accessible,
so no essential source blocker remains and those failed paths are parked.
No sibling notebook was read. The official target and PROOF.md assembly
are unchanged; the earlier Clay/Wiles scope assessment remains applicable.

The [concrete recovery scope](2026-10-10-conductor-eleven-twist-five-certificate.md)
is newly saved ready coverage, subject to separate next-turn approval.
Its continuation must use L039's audited arithmetic, L028's established
conventions and the primary sources above. L031 supplies methodology only.
The test is a proved denominator followed by a complete outward ratio
interval with one explicitly enumerated admissible rational; allow zero.
The unknown functional scalar is excluded from the calculation. All the
rank, coefficient, Sha and uniform-production gaps identified above remain.
