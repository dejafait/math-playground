# L033 — Finite quadratic coefficient enclosure at seven

## Hypotheses

Let E/Q be the minimal non-CM curve y^2+y=x^3+x^2-2x of L030.
Use the primitive untwisted ordinary series on the trivial Teichmuller
branch, the total minimal real period and kappa(gamma)=8, exactly as in
[foundations/05](../foundations/05-kato-divisibility.md).
Write L_7(E,T)=sum a_i T^i. Retain L032's audited identification
S(r)=F({infinity,r}), F=-phi on the whole relative integral module,
and its all-level denominator bound C=0.

The complete new finite evidence is
`scripts/quadratic-seven/certificate.json`; its distinct exact replay is
`scripts/quadratic-seven/verification.json`. Reproduction commands:

```bash
python3 scripts/quadratic-seven/build_certificate.py
python3 scripts/quadratic-seven/verify_certificate.py
python3 scripts/quadratic-seven/audit.py
```

The inputs are the complete relative-t2, twist-five and calibrated-symbol
certificate/replay/audit sets, bound by nine SHA-256 hashes. The preceding
canonical results justify their mathematics; hashes are only binding.
The new verifier imports no construction program. This is an ordinary
exact-arithmetic certificate; its separate critical audit below passes.
The audit also uses `scripts/quadratic-seven/audit-replays.json`, which
records the seven complete upstream/current verification runs and their
unchanged input hashes.

## Conclusion

The prime 7 is good ordinary, with #E(F_7)=13 and t=a_7(E)=-5.
At n=2, M=3 choose u=16. The exact L027 sum is

\[
b=\frac{13}{256},\qquad v_7(b)=0,
\qquad N=\min(n-1,M)=1>0.
\]

Consequently L027 gives

\[
v_7\left(a_2-\frac{13}{256}\right)\ge1,
\qquad a_2\ne0,\qquad v_7(a_2)=0.
\]

The bounded schedule stops at its first depth; n=3,4 were not attempted.
This supplies only the fixed-instance quadratic coefficient premise of
L026. Its other hypotheses, rational rank, finite F, divisible Sha,
uniform input production and comparison with complex order are not
established. Neither lower coefficient vanishing nor BSD is assumed.

## Proof

**Imported algorithm and applicability.** Apply L027 as proved, rather
than reprove its convergence/error theorem. Its named inputs are
Stein--Wuthrich, *Algorithms for the arithmetic of elliptic curves using
Iwasawa theory*, Math. Comp. 82 (2013), 1757--1792,
[Section 3, pp. 1762--1766, Propositions 3.1/3.5 and Corollary 3.3](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=6),
and Conrad, *Hensel's Lemma*,
[Theorem 4.1, printed p. 6](https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf#page=6).
This step is their assessed finite specialization, not a new production
theorem or a reproof of those inputs. The source normalization and
primitive interpolation multiplier are retained unchanged.

L030 gives Delta=N=389 and non-CM minimality. Since 389=4 modulo 7,
reduction at 7 is good. The full point count, independently replayed
by exhausting all 49 affine pairs, is as follows:

| x | y satisfying the equation modulo 7 |
|---|---|
| 0 | 0,6 |
| 1 | 0,6 |
| 2 | none |
| 3 | 1,5 |
| 4 | 1,5 |
| 5 | 0,6 |
| 6 | 1,5 |

These give 12 affine points, and the projective Weierstrass model has
its unique point at infinity [0:1:0]. Thus t=7+1-13=-5, a 7-adic unit.
L032 applies because p>=5, p!=5 and p is now certified good ordinary.
Its normalization on the entire integral relative module supplies all
exact symbol values and C=0 at every level, not only this sample.

**Root and residue evidence.** At n=2, the six least-positive residues
modulo 49, their residual valuations and simple-root derivatives are:

| d | w | v_7(w^6-1) | 6w^5 modulo 7 |
|---|---|---|---|
| 1 | 1 | infinity | 6 |
| 2 | 30 | 2 | 3 |
| 3 | 31 | 2 | 2 |
| 4 | 18 | 3 | 5 |
| 5 | 19 | 3 | 4 |
| 6 | 48 | 2 | 1 |

Every w is in [1,48], congruent to d modulo 7 and satisfies w^6=1
modulo 49. The replay enumerates all integers in that range in each
residue class and finds exactly the listed solution. The residual is
zero for w=1; this is an exact root, not a failed valuation computation.
All derivatives are units. These are precisely L027's Teichmuller data.

For f(X)=X^2+5X+7, u=16 is a unit with u=-5 modulo 7, and
f(16)=343=7^3, while f'(16)=37=2 modulo 7 is a unit.
Thus L027's M=3 premise holds for the correct unit root alpha.
The replay also enumerates the residue class modulo 343 and verifies
that 16 is its unique root residue. Hensel's theorem supplies
v_7(alpha-16)=3; no approximate root is substituted into a cusp argument.

**Every exact symbol evaluation.** For d=1,...,6 and j=0,...,6 put
r=w_d 8^j modulo 49 in [1,48]. The certificate contains all 42 ordered
pairs (d,j). The replay independently obtains each r by repeated
multiplication and checks that the resulting multiset is exactly all
units modulo 49, with no omitted or repeated residue. Its two rational
arguments are exactly r/49 and r/7, not nearby root approximations or
altered coset representatives.

All 84 oriented paths from infinity to these arguments are recorded.
Their 326 segments have integer lifts h=(A,B;C,D) of determinant one.
For each segment the replay checks start=B/D and end=A/C in canonical
projective coordinates, starting at infinity, with consecutive endpoints
equal and final endpoint the exact reduced argument. It evaluates the
saved continued fraction backwards to confirm that endpoint independently
of the builder's recurrence.

For each h, the replay exhausts all 390 L030 lifts g_i and finds exactly
one with gamma=h g_i^(-1) in Gamma_0(389). It checks det(gamma)=1,
389 divides its lower-left entry, and gamma g_i=h exactly. Therefore
the oriented segment equals g_i{0,infinity} in the relative quotient.
Telescoping identifies the entire path with its integral generator sum.
No segment is reversed or divided by two.

For every path the replay reconstructs all 390 raw coordinates, sums
their complete 65 quotient coordinates using L030's integral coordinate
matrix, and compares every entry with the certificate. It evaluates F
both by the quotient functional and by all calibrated generator values.
These agree with the saved rational value. It also checks all 390 values
against minus phi and checks all 780 source and 325 saturated relations.
The full presentation and normalization are the audited L030/L032 inputs;
the new path checks do not infer completeness from a finite sample.

**Complete sum and strict bound.** The saved terms retain every j,
including j>2. Their weights are exactly j(j-1)/2. Put
A_(d,j)=S(r/49), B_(d,j)=S(r/7). Complete exact summation gives

\[
\sum_{d=1}^6\sum_{j=0}^6\binom j2 A_{d,j}=13,
\qquad
\sum_{d=1}^6\sum_{j=0}^6\binom j2 B_{d,j}=0.
\]

Every summand and symbol value is retained in the certificate, not just
these totals. For a distinct accumulation the replay doubles the full
L032 functional to integral generator values. It obtains the integer
totals sum_A2=26 and sum_B2=0 from the reconstructed paths, and computes
b=(16 sum_A2-sum_B2)/(2*16^3). It also recomputes each individual rational
term and their sum. Both computations agree with the reduced fraction
13/256, without trusting saved aggregates.

The eight grouped replay checks all pass, with actual/required term
count 42/42 and no replay failures. The exact residual, all paths,
root data and all summands were checked; a preview alone is not evidence
for their equalities. Since 7 divides neither 13 nor 256, v_7(b)=0.
L027 with n=2, C=0 and M=3 gives N=1 and the claimed enclosure.
The strict inequality N>v_7(b) gives v_7(a_2)=0 and nonvanishing.
No assertion about a_0 or a_1 was used.

This is local progress by reproducing an assessed known algorithm. It
does not go beyond the sources checked, give a uniform nonvanishing
algorithm or settle any independent arithmetic premise of L026.
The separate critical review below finds no failed equality or missing
instance hypothesis; there is no BSD candidate.

**Separate critical audit, 2026-10-08.** The approved audit read the
complete L027/L028/L030/L031/L032 proofs, both quadratic-seven programs,
and the primitive conventions in foundations/05. It reused the ready
primary-source assessments; no new theorem or theorem reproof was needed.
The minimal non-CM model, good ordinary p=7, independent twist scale,
full relative lattice and all-level C=0 meet precisely L027's hypotheses.
This is an audit of a known-algorithm specialization, not new mathematics
beyond the assessed sources.

All seven complete replay/audit runs pass: L030 verification and audit,
L031 verification and audit, L032 verification and audit, and the new
L033 replay. Their complete output and before/after hashes are retained
in `scripts/quadratic-seven/audit-replays.json`. All nine input artifacts
are unchanged. In particular the full L030 paths, lattice and rank
witnesses, L031 arithmetic, tail and total-period enclosure, and L032
calibration evidence pass their existing complete checks. This reuses
the canonical source applications above; hashes and successful programs
alone do not prove imported arithmetic theorems.

The supplemental program `scripts/quadratic-seven/audit.py` imports no
notebook program. Its complete evidence is
`scripts/quadratic-seven/audit.json`. It counts the 57 projective points
of P^2(F_7), represented without duplication by [x:y:1], [x:1:0] and
[1:0:0], and checks the homogeneous equation at every one. Exactly 13
lie on E, including only [0:1:0] at infinity. All six root residues,
exact residuals, derivatives and uniqueness checks reproduce the table
above, including v_7(0)=infinity. Exhaustion modulo 343 in the residue
class 2 gives the unique root residue 16, residual 343 and derivative
37. Hensel's cited simple-root theorem identifies alpha and its distance;
exhaustion by itself asserts only a finite congruence.

For every original segment the audit reconstructs its determinant-one
lift from the canonical starting cusp b/d and ending cusp a/c. With
s=ad-bc in {1,-1}, the matrix (sa,b;sc,d) has determinant one and the
required oriented endpoints. For each of the 390 supplied coset lifts
(e,f;g,k), the projective cross-product test Ck-Dg=0 modulo 389
identifies the bottom-row class of (A,B;C,D). Exactly one class matches.
The explicit matrix h g_i^(-1), its determinant, lower-left divisibility
and product with g_i are all checked against the saved segment. All
326 original segments, 84 endpoint chains, 390-entry raw vectors and
65-entry quotient vectors are reconstructed completely.

A different decomposition is then built for each rational endpoint r.
Set x=r and repeatedly take a=ceil(x), replacing x by 1/(a-x) unless
x=a. The new reduced denominator is smaller, so this finite construction
terminates. For the resulting negative continued-fraction digits use
(p_-2,q_-2)=(0,-1), (p_-1,q_-1)=(1,0) and
(p_i,q_i)=a_i(p_(i-1),q_(i-1))-(p_(i-2),q_(i-2)). The program checks
the actual final endpoint and every adjacent determinant exactly; no
unproved assertion about convergence is used. These give 84 different
oriented chains with 534 segments. The same explicit coset-membership
checks identify each segment. For every alternate chain its entire
65-entry quotient vector agrees with the original, with all differences
zero. Thus agreement holds in the full relative module, not just after
evaluation. All segment matrices, raw vectors, quotient vectors and
differences are saved in the audit artifact.

The audit also recomputes every one of the 390 calibrated values from
the 65-entry functional -phi, and all 780 source and 325 saturated
relation residuals. Every value is half-integral and y_7=-1/2. Together
with the certified complete integral presentation this confirms the
all-rational-argument C=0 at p=7. The scale still comes independently
from L031's q=4 and L032's oriented d=-4; neither the new path sample
nor its coefficient values are used to infer it. Both periods are total
minimal real periods, and the twist 5 is prime to 7 and Delta=389.

For a complementary summation, index by the 42 units r modulo 49 and
exhaustively identify their unique pair (d,j). Starting with the constant
polynomial one, multiply by (1+T) exactly j times; use all its coefficients
instead of a binomial-library call. Evaluate both symbol families using
the alternate paths and accumulate the complete polynomials. The result is

\[
\begin{aligned}
\sum_{d,j} A_{d,j}(1+T)^j&=13T^2+26T^3+24T^4+11T^5+2T^6,\\
\sum_{d,j} B_{d,j}(1+T)^j&=0.
\end{aligned}
\]

All 42 saved individual terms agree with this computation, including
j=3,4,5,6. The T^2 coefficient of 16^(-2) times the first polynomial
minus 16^(-3) times the second is exactly 13/256. The arguments remain
r/49 and r/7, with the least positive integer r and gamma=8, as required
by L027 (1)--(2). No twist, Euler-factor removal or rescaling is present.
Finite vanishing of the constant and linear coefficients above is not
used to infer vanishing of the limiting series' lower coefficients.

Finally L027's proof bounds the limiting tail by n-1-C=1 using the
all-level denominator and coefficientwise convergence, and the root
substitution by M-C=3. These are different errors; the strict test uses
the minimum 1, not the root precision alone. Since 7 divides neither
13 nor 256, the error is of strictly larger valuation than b. Thus the
limiting a_2 is nonzero with valuation zero. All six supplemental grouped
checks pass, actual/required terms are 42/42 and there are no failures.
The audit supplies only this fixed coefficient input; it assumes no
other L026 premise, rational-point independence, lower coefficient
vanishing, finite or divisible Sha conclusion, or complex-order equality.
The production schedule remains stopped at n=2.

## Mathlib

Full matching p=7 finite coefficient implementation: not checked.
Supporting cusp paths, rational arithmetic, valuation and Hensel
coverage: not checked. Unknown coverage is not evidence of absence.
The ordinary construction and error estimate are imported by the precise
citations above and L027; Python replay is not formal verification.
