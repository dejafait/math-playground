# L032 — Exact calibrated integral symbols at conductor 389

## Hypotheses

Let E/Q be y^2+y=x^3+x^2-2x and f its normalized weight-two newform.
Use the minimal differential and the total real period
Omega(E)=integral_(E(R)) |omega_E|. A cusp symbol {alpha,beta} is
oriented from alpha to beta. Let M be the entire torsion-free relative
weight-two modular-symbol module for Gamma_0(389).

Use L030's complete audited integral presentation M=Z^390/R_sat,
its integral quotient basis of dimension 65 and its functional phi,
including the conclusion I=beta phi on all M_R for beta!=0, where
I({alpha,beta})=Re(2 pi i integral_alpha^beta f(z) dz).
Use independently audited L031's q=L(E^5,1)/Omega(E^5)=4.
For the p-adic application retain good ordinary p>=5 with p!=5.
In particular p does not divide 389 or the calibration twist 5.

The complete new finite evidence is
`scripts/calibrated-symbols/certificate.json`. Its complete independent
replay is `scripts/calibrated-symbols/verification.json`. Reproduction:

```bash
python3 scripts/calibrated-symbols/build_certificate.py
python3 scripts/calibrated-symbols/verify_certificate.py
python3 scripts/calibrated-symbols/audit.py
```

Neither program modifies the prior input evidence. The new certificate
records SHA-256 hashes of both prior certificates and their verification
and audit reports. The new checker imports no construction program.
It reuses L030/L031 as proved inputs; hash binding is not a substitute
for their mathematical proofs or primary source theorems.

## Conclusion

For chi the quadratic character modulo 5 and
G_5=sum_(a=1)^4 chi(a){infinity,a/5}, the actual certificate gives

\[
\phi(G_5)=-4,\qquad
F=\frac{4}{\phi(G_5)}\phi=-\phi=\frac{I}{\Omega(E)}.
\]

All 390 calibrated integral-generator values are saved as reduced
rational numbers. They belong to {0,1,-1,1/2,-1/2}; their least common
denominator is exactly 2. Hence

\[
F(M)\subseteq\tfrac12\mathbf Z,
\qquad v_p(F(\{\infty,r\}))\ge0\quad(r\in\mathbf Q).
\]

Thus the actual all-argument denominator constant of L028's formula is
C=0 for every retained good ordinary p>=5, p!=5. These values are the
exact normalized symbols S(r) in L027's convention. The assertion
includes arbitrary rational cusp arguments, not merely the four paths
or generators checked directly.

This produces the fixed-instance normalization and denominator inputs
for L027. No quadratic coefficient or strict nonvanishing enclosure,
other L026 premise, rank assertion or uniform production is supplied.
The separate critical audit below validates this fixed specialization.

## Proof

**Known inputs and instance applicability.** L028 is the imported
prime-twist calibration and finite-lattice denominator argument, with
the hypotheses and conventions proved there. Its primary inputs are
Cremona, *Algorithms for Modular Elliptic Curves*, corrected second
edition, [Section 2.11, pp. 38--39, identity preceding (2.11.4)](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=32),
Pal, [arXiv:1012.0094v2, Corollary 2.6 and Theorem 3.2](https://arxiv.org/pdf/1012.0094v2),
and Stein--Wuthrich, *Algorithms for the arithmetic of elliptic curves
using Iwasawa theory*, Math. Comp. 82 (2013),
[Section 3, p. 1762](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=6).
No theorem reproof or new normalization assertion is needed here.

By L030 the base model is globally minimal, non-CM and has N=Delta=389.
The twist prime 5 is positive, is 1 modulo 4 and is coprime to Delta
and the retained p. L030 supplies the full relative integration line
and complete integral lattice, not only an absolute eigenspace.
L031 supplies independent nonzero q=4 without using phi. Thus all
L028 hypotheses hold. Its positive-twist total-period identity gives
I(G_5)/Omega(E)=4, and its conclusion F=(4/phi(G_5))phi applies once
the actual evaluation below is performed. No twist Manin constant or
untwisted central nonvanishing is inserted.

**Complete oriented path witnesses.** Import Stein, online v0.1,
[weight-two Proposition 3.10, Proposition 3.11 and Theorem 3.13](https://wstein.org/books/modform/modform/weight_two.html).
The projective bottom rows identify right cosets; integral path
generation and the complete two/three-term Manin presentation modulo
torsion apply at this positive level and weight two. L030 already
certifies that presentation and its saturation. We only reproduce the
four finite path reductions needed for calibration.

Use L030's zero-based generators g_i, i=0,...,389. For i<389 their
SL_2(Z) lifts are (0,-1;1,i), mapping {0,infinity} to {-1/i,0};
the final lift is the identity. The complete new path certificate gives
the following continued fractions and ordered segment cosets:

| a | Continued fraction of a/5 | Segment cosets | phi({infinity,a/5}) |
|---|---|---|---|
| 1 | [0,5] | 0,78 | -1 |
| 2 | [0,2,2] | 0,195,233 | 1 |
| 3 | [0,1,1,2] | 0,1,194,156 | 1 |
| 4 | [0,1,4] | 0,1,311 | -1 |

The evidence contains all 12 segment lifts h=(a,b;c,d), their start
and end cusps and gamma=h g_i^(-1), not just the coset list. The
independent checker proves for each segment det(h)=1,
start=b/d, end=a/c in canonical projective coordinates, det(gamma)=1,
gamma's lower-left entry divisible by 389, and gamma g_i=h exactly.
Thus gamma belongs to Gamma_0(389), and that oriented segment equals
g_i{0,infinity} in the relative module. It checks every consecutive
endpoint, starting at infinity and ending at a/5. Telescoping gives
each path as the integral sum of the listed generators with coefficient
+1; no segment reversal or half-projection is used. The continued
fractions are also evaluated exactly, independently of the builder's
recurrence. The general path-generation theorem is imported, not
inferred from testing four paths.

Since chi(1)=chi(4)=1 and chi(2)=chi(3)=-1, cancellation of the
common first segments gives the actual representative

\[
G_5=g_{78}-g_{195}-g_{233}-g_{194}-g_{156}+g_{311}.
\]

The complete 390-entry raw representative and 65-entry quotient vector
are saved under `G5`. The checker recomputes both from all four paths
and independently multiplies the raw vector by L030's full integral
coordinate matrix. Evaluation by the stored quotient-basis phi and
by all 390 original generator values agrees exactly. The four
evaluations in the table give
d=(-1)-(1)-(1)+(-1)=-4. Thus d is nonzero, and L028 gives F=-phi
on the entire relative module. The certificate also checks F(G_5)=4
through both coordinate expressions. This last equality is a consistency
check; q=4 comes independently from L031.

**Relations and exact denominator evidence.** For every original
integral generator, the certificate stores y_i=-phi(g_i) as a reduced
rational number and also the scaled 65-entry basis functional. The
checker recomputes all 390 dot products, with exact vector lengths,
and checks equality with the saved values. It reconstructs every
two/three-term row from the projective coset action, checks agreement
with the 780 L030 rows and verifies their y-residuals are zero. It
also verifies every one of the 325 saturated relation rows annihilates
y. Hence these values descend to the entire certified integral quotient.

The complete value list consists of 0, +/-1 and +/-1/2. The checker
computes the least common multiple of all reduced denominators,
obtaining 2, verifies its full factorization 2^1, and checks 2y_i is
integral for every i. The denominator witness is y_7=-1/2, so the
common denominator is exactly 2 rather than merely at most 2.
All reduced values are retained in the certificate; the witness alone
would not prove an upper bound for the other 389 generators.

For any x in M choose an integral representative sum z_i g_i;
the imported complete presentation ensures every element admits one.
Then F(x)=sum z_i y_i belongs to (1/2)Z. For the retained odd p,
2 is a unit in Z_p, so every y_i belongs to Z_p, and the finite
nonarchimedean sum gives v_p(F(x))>=0. L028's nonnegative maximum
therefore equals C=0. Its identification S(r)=F({infinity,r}) and
integral path generation apply to every rational r. There is no
dependence on the cusp denominator, path length or cyclotomic level.

**Replay and limits.** All eight grouped checks in the independent
replay pass, with four paths, 12 segments, 390 generator values,
780 Manin rows, 325 saturated rows, d=-4, scale=-1 and common
denominator 2; there are no remaining replay failures. The first
checker invocation incorrectly treated L030's integer dual matrix
entries as rational strings and stopped before the path checks.
Its report is retained as
`scripts/calibrated-symbols/verification-initial-type-failure.json`.
The correction requires integer rows of length 65 for that input;
it changes no mathematical data or computed scale. The final complete
replay succeeds after this input-type correction.

This is a fixed known-source specialization, not new mathematics
beyond the assessed sources and not a BSD candidate. Even C=0 does
not produce L027's finite coefficient b or prove its strict threshold
min(n-1,M)>v_p(b). All independent arithmetic, finite-Selmer,
divisible-Sha, rational-membership and complex-order gaps are retained.

**Separate critical audit, 2026-10-07.** The approved audit read both
complete new programs and the canonical L028/L030/L031 proofs, retaining
their previously inspected source coverage. It reran the complete L030
and L031 verification and audit programs: 27 and nine grouped checks
for L030, seven full checks and all 256 direct-power/sum comparisons
for L031 pass. Their six input artifacts retain exactly the hashes in
the L032 certificate. This replays the input finite evidence; it does
not claim to reprove the imported source theorems. The complete L032
replay again passes all eight checks, with no failure.

Supplemental evidence is `scripts/calibrated-symbols/audit.json`, made
by `scripts/calibrated-symbols/audit.py`, which imports neither new
production nor replay program. For every one of the twelve original
segments it tests h g_i^(-1) against **all** 390 supplied lifts. Exactly
one is in Gamma_0(389), and its recorded matrix agrees. Determinant
one, both oriented endpoints and gamma g_i=h are verified exactly.
This independently identifies the coset without the two original
programs' modular-inverse lookup. Successive endpoint equality and
telescoping therefore justify the entire path, not just its evaluation.

The complementary audit also uses these explicit alternate paths:

| Endpoint | Ordered cusp chain from infinity | Cosets |
|---|---|---|
| 1/5 | infinity, 0, 1/5 | 0,78 |
| 2/5 | infinity, 0, 1/3, 2/5 | 0,130,234 |
| 3/5 | infinity, 1, 2/3, 3/5 | 0,259,155 |
| 4/5 | infinity, 1, 4/5 | 0,311 |

For consecutive reduced cusps b/d,A/C, the integer A d-b C is +/-1.
Multiplying the end column by that sign gives an SL_2(Z) matrix with
columns (signed A,signed C) and (b,d); hence its path is oriented
from b/d to A/C. The audit verifies all ten matrices and cosets by
the exhaustive membership test. Summing their complete 65-entry
quotient coordinates gives the original path coordinates, with all
65 differences zero for each path. Thus the alternate paths agree in
M, not only after applying phi. The report retains every lift, coset,
Gamma_0 matrix, raw vector, quotient vector and difference. The first
path is reused here; the other three decompositions differ.

For the source-relation comparison the audit uses Stein's
tau=(1,-1;1,0), rather than the builders' U=tau^2. Projective bottom
rows of tau and tau^2 are (c+d,-c) and (d,-c-d). Exhaustive projective
cross-product tests identify their cosets. Since U^2=-tau and signs
are projectively immaterial, this reconstructs the same three-term
relations; all 780 source rows are checked against the base evidence.
The audit computes all 390 integers 2y_i, verifies their source and
325 saturated relation residuals are zero, and compares every value
with minus the original basis-functional dot product. Their exact
distribution is 162 zeroes, 30 each of +1 and -1, and 84 each of +1/2
and -1/2. Together with y_7=-1/2, this independently proves the exact
common denominator two. It does not infer an upper bound from a
single witness. All eight supplemental grouped checks pass.

The normalization review uses L028's oriented Gauss-sum identity and
Pal's positive-twist period formula with 5 coprime to Delta=389 and
5=1 modulo 4. Both use total minimal real periods. The common
{infinity,0} segment cancels in the character sum, so neither a sign
nor a factor of two is introduced. L031's independent q=4 and the
audited d=-4 determine F=-phi on the entire relative module through
L030's real line. F(G_5)=4 alone would not validate that scale.

Finally, integral generation of the whole relative module puts every
{infinity,r} in the integral span of the 390 checked generators.
Their half-integral values consequently give F(M) contained in
(1/2)Z. For each retained good ordinary p>=5, p!=5, the integer 2
is a p-adic unit; the nonnegative maximum in L028 is exactly C=0.
This uses no assertion that all primes are ordinary and no restriction
to sampled cusps, absolute cycles or a rational basis. The initial
type-failure report remains preserved and is not counted as a pass.
No source-hypothesis mismatch or failed instance equality was found.
This validates the known-input specialization for subsequent use of
L027; b and its strict nonvanishing test remain uncomputed, as do
the independent BSD premises already listed.

## Mathlib

Full matching conductor-389 calibrated relative-symbol certificate:
not checked. Supporting coverage of Manin presentation, cusp-path
generation, twist-period calibration, rational linear algebra and
p-adic valuations: not checked. Unknown coverage is not evidence
of absence. Named results are imported by the precise citations above;
the new work is their finite-instance implementation and exact replay.
