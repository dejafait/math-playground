# Independent twist-five value — source comparison completed

TARGET: Assess an independent exact certificate for q=L(E^5,1)/Omega(E^5) for E: y^2+y=x^3+x^2-2x using rigorous analytic enclosures and a proved rational-denominator bound, without L030's unknown scalar or BSD.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched rigorous central-value rational recovery, Manin-constant/degree bounds, numerical modular-symbol denominators and Cremona verification; checked L028, ATTEMPTS/022--023 and the calibration audit for duplicate coverage; primary statements and error proofs read below.
SOURCE_EVIDENCE: Direct primary denominator source https://arxiv.org/pdf/1608.06423v2; Wuthrich arXiv:1608.06423 Proposition 1 and Lemmas 4/6 with proofs; Cesnavicius arXiv:1703.02951 Theorems 1.2/2.13 and latter proof; Cremona corrected second edition Propositions 2.11.1--2.11.2 and Section 3.7 (3.7.1); Cremona ecdata exact conductor-389 row and optimal-label convention; DLMF 19.8.1--19.8.5; reuse Pal positive-twist period coverage in the existing audit.
COMPARISON: Known numerical modular-symbol algorithms cover rigorous rational recovery; using the semistable base curve avoids an unproved Manin-constant-one assumption for the additive twist. A later specialization must assemble its denominator, analytic tail, total-period factor and isolation certificate. No new algorithm or value is claimed.
GAP: Essential theorem coverage is available; the actual root sign, specialized denominator B, outward enclosures, unique rational and nonvanishing test remain unexecuted. Rational membership and complex/p-adic comparison remain separate gaps.
REASON: Newly inspected primary inputs cover a known production mechanism; the concrete calculation continuation receives separate next-turn approval. No mathematical derivation, lemma or script is made in this literature-only step.
SCOPE: This minimal base curve and positive twist by 5, with total real Neron periods; no BSD, finite Sha, assumed twist nonvanishing, L030 scalar or decimal rational rounding. Later L028 use requires good ordinary p>=5 with p!=5.

## Relevance and discriminating test

The main gap remains rank equality at analytic order at least two.
Independent exact q is the missing intermediate input of L028 after
L030's completed line audit. Its plausible downstream use is Neron
normalization and the all-argument denominator of L027; neither rational
membership nor complex-order comparison would follow.

After separate approval of the new production continuation, require a
proved denominator B before rational recovery and a ratio interval
containing exactly one rational of reduced denominator at most B.
Test that rational against zero. Refine an inconclusive interval within
a fixed computation budget; an exact zero abandons this fixed nonzero
twist choice. A root number of +1 alone does not prove nonvanishing.
No value or specialized denominator is asserted this turn.

## Primary inputs and hypotheses actually inspected

[Wuthrich, *Numerical modular symbols for elliptic curves*,
arXiv:1608.06423](https://arxiv.org/pdf/1608.06423), 25-page version
(also Math. Comp. 87 (2018), 2393--2423):
Proposition 1, PDF pp. 3--4, with its complete torsion-reduction proof,
gives, assuming strong Weil Manin constant one, the unitary-cusp lattice
`[r]^+ in c_infinity(E)/(2 #E(Q)_tors) Z`.
Its period is the least positive real period. Use the optimal base case.
Section 2.2's optimality qualifications were read. Lemma 4, p. 7, uses
`|a_n|<=n` and bounds the tail by
`exp(-2*pi*T*y)/(exp(2*pi*y)-1)`.
Lemma 6, p. 8, bounds finite-sum error when
`2^(-b)<epsilon0/(2*T*(T+epsilon0))`.
Read both proofs and Section 4.1--4.2's unitary path splitting,
equations (6)--(9); the semistable sign is epsilon_Q=-a_Q.
Transcendental evaluation errors still require certification.
No conjectural complexity estimate or assumed cancellation is needed.

[Cesnavicius, *The Manin constant in the semistable case*,
arXiv:1703.02951](https://arxiv.org/pdf/1703.02951), 28-page version:
Theorem 1.2 = Theorem 2.13, PDF pp. 2 and 9, applies to a new elliptic
optimal quotient of J_H, Gamma_1(n) contained in H contained in
Gamma_0(n), and a prime l with l^2 not dividing n. The Manin constant
has l-adic valuation zero. Read Theorem 2.13's proof via Lemma 2.12
and Theorem 2.11, retaining integrality and optimality; import without
reproof. L030's squarefree conductor 389 covers every prime on the base,
once its optimal identification is imported below. This theorem does
not give constant one for the additive twist at 5.

[Cremona ecdata documentation](https://johncremona.github.io/ecdata/),
Table One, specifies minimal coefficients, torsion order and the verified
optimal-label convention below 370000 apart from 990h.
The conductor-389 region of [the primary allcurves table](https://raw.githubusercontent.com/JohnCremona/ecdata/master/allcurves/allcurves.00000-09999)
has the sole row `389 a 1 [0,1,1,-2,0] 2 1`.
The model matches exactly; only its optimal identification and torsion
entry are relevant, not its rank column.
[Cremona's appendix to Agashe--Ribet--Stein](https://wstein.org/papers/ars-manin/html/node13.html),
Proposition 5.1 and Theorem 5.2, were also read: the latter covers
optimal quotients at N<60000 and identifies label one except 990h.
The former's full proof retains a complete isogeny class and two-period
comparison. A single approximate period or an unexplained label would
not replace those hypotheses. We import the published small-conductor
verification rather than reprove optimality.

[Cremona, *Algorithms for Modular Elliptic Curves*, corrected second
edition (1997), Chapter 2](https://johncremona.github.io/book/fulltext/chapter2.pdf),
pp. 37--39, Propositions 2.11.1--2.11.2: read both Fricke-sign cases
and formula (2.11.3). For odd ell not dividing N, chi(-N)=epsilon_N
forces the twist value to be zero; in the other case it is
`2 sum chi(n) a_n/n exp(-2*pi*n/(ell*sqrt(N)))`.
The following Gauss-sum identity relates it to the oriented character
sum of cusp paths, with positive square root for ell=1 mod 4.
A later calculation must certify epsilon_N, not select the nonzero
branch. Point-count coefficients and this analytic sum do not use
L030's functional. No approximate Fricke-sign test or twist-search
existence theorem is imported.

[Cremona Chapter 3](https://johncremona.github.io/book/fulltext/chapter3.pdf),
Section 3.7, pp. 97--98, equation (3.7.1): read the completed-square
cubic and the positive-discriminant real-root case. For ordered roots
e3>e2>e1, with positive square roots, the real period generator is
`pi/AGM(sqrt(e3-e1),sqrt(e3-e2))`.
L030's positive discriminant supplies this case. The later implementation
must isolate roots and retain the minimal differential. This period
formula does not certify floating-point output by itself.

[NIST DLMF Section 19.8(i)](https://dlmf.nist.gov/19.8.i),
equations 19.8.1--19.8.5: read the positive arithmetic/geometric iteration,
common limit, quadratic convergence and integral representation.
These support a finite enclosure using positive interval inputs.
The finite bracketing argument and outward errors are the later
specialization's work, not established here.

Reuse the already inspected Pal Corollary 2.6 and Theorem 3.2
(arXiv:1012.0094v2) in
[the calibration-audit assessment](2026-10-07-prime-twist-certificate-critical-audit.md)
for the positive minimal twist and total-period comparison, and
Stein--Wuthrich Section 3 for
`Omega_total=c_infinity Omega_plus`.
The prime 5 satisfies the source's positive, squarefree, 1-mod-4
condition and is prime to L030's discriminant 389.
No new twist minimalization assumption or Manin constant for the twist
is required. The later denominator application must account for the
character sum and this component factor explicitly.

## Comparison, limits, failures and unread scope

The calculation is a specialization of a known algorithm. Its required
difference is an explicit fixed-input certificate: import optimality,
derive the denominator lattice from the unitary-cusp bound and established
twist identity, enclose the analytic series and Neron period independently,
then perform exact rational isolation. No theorem beyond these sources
is proposed. There is no matching-value computation this turn.
Full Mathlib coverage was not checked; unknown coverage is not absence.

The inspected Cesnavicius--Neururer--Saha Theorem 1.2,
[*The Manin constant and the modular degree*](https://ems.press/content/serial-article-files/42577),
gives a degree-dependent bound, including the cube-free case; it does not
supply the twist's degree certificate. That less economical alternative
is parked. [Sage's numerical-symbol documentation](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/mod_sym_num.html)
retains a strong Weil Manin-constant assumption outside verified tables.
Its exact-symbol alternative still requires independent scale certification.
A routine call or displayed decimal is not a complete certificate.
No implementation internals were audited; they are not substituted for
outward error evidence.

ATTEMPTS/022--023 stop repeating conditional enclosure/calibration
audits without inputs. Producing an independent value is a materially
different test; the historical stops remain intact.
The Nottingham preview and one author URL were inaccessible, and LMFDB
class access intermittently showed a CAPTCHA. Accessible author/arXiv
PDFs and the primary Cremona row supplied the essential coverage.
No persistent source blocker remains, and no failed search implies novelty.

Queries: `elliptic curve rigorous L value rational denominator bound
Manin constant central value computation`; `Manin constant divides
modular degree`; `Christian Wuthrich numerical modular symbols denominator
bounds algorithm paper`; `Cremona Manin constant verification conductor
500000 rigorous theorem`.
No sibling notebook input was used.

The [current Clay page](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/)
still links [Wiles's official description](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf).
Read printed p. 2's rank/order assertion and separate refined Remark 1.
Neither the exact target nor PROOF.md's argument changes.

Essential continuation inputs are L030's audited arithmetic and line
(with certificate.json, verification.json and audit.json), L028's
conditional calibration and total-period convention, and the sources
above. q, normalized scale, C, b, other L026 premises, F, divisible Sha,
rational membership and complex-order comparison remain unresolved.
A newly saved concrete production assessment receives separate approval
next turn; this completed source comparison is not a mathematical attempt.
