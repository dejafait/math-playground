# L093 — Uniform literal survivor roots fail their own-input H guard

## Hypotheses

Fix an integer 6<=d<=33. Take L055's 25 indexed pairs in literal
order, changing only H_0=40-d and H_24=32670621+d. Put B=9250245,
kappa=23/11 and fix t in {0,1}. Set a_i=2 for 0<=i<=22,
a_23=2+18t and a_24=2+18(B-t). Consider real s_0,...,s_25
satisfying s_25=s_0 and every endpoint

\[
s_{i+1}=2^{-a_i}\left((27/16)^{J_i}(3/2)^{H_i}s_i
                 -(12/11)(3/2)^{H_i}-1\right)+\kappa.
\tag{1}
\]

No J guard, H guard, lower-domain condition, minimum, seed,
integer-junction, parity, residue, exact-valuation, primitive-count or
actual-word premise is assumed. All logarithms are natural.

## Conclusion

For every specified d,t there is exactly one real endpoint tuple.
It is positive rational, every n_i=s_i-kappa is greater than 47, and

\[
\log s_{18}+693015\log(27/16)-3295208\log2
<F_{18}(d)
:=-\frac{457745289}{50000000000}-(d-1)(u-\ell)
\le-\frac{203648044633}{100000000000}<0,
\tag{2}
\]

where ell=693147180559/10^12 and u=1098612288669/10^12.
Thus neither specified root satisfies its own outgoing row18 strict
H guard. This is a fixed-root result only: it gives no reduction of
other allocations or cyclic orders to these roots and no actual-word
application or universal eventual-descent conclusion.

This is local RESEARCH/REPRODUCTION under the prior SPECIALIZE
assessment `drafts/literature/2026-10-21-uniform-literal-survivor-h-test.md`.
It specializes existing affine formulas and audited data by justifying
the restricted cap/margin implication without the failed full O/S/C
conjunction. It claims no new general theorem beyond the sources
checked. The independent critical audit below found no defect. Attempt 032 and both
original d=0 rational witnesses remain unchanged.

## Proof

### Independent endpoint premises

The table has r=25, p=23, q=24, strictly increasing J_i>=8 and
H_i>=7. Both allocations are exactly the last-pair family of L077
(1)–(2). L084 (2) and its completed all-member audit give

\[
K=397573379,\quad N=630138897,\quad
0<\lambda_-:=10584/10^{14}<\Lambda=N\log2-K\log3
<\lambda_+:=10585/10^{14}<1.
\tag{3}
\]

Opposite changes in the two H entries preserve these totals. At t=0
the final tails are (2,166504412); at t=1 they are (20,166504394).
Each complete tail list sums to 166504460, so both changing tails,
including the closing one, occur in N and the full cyclic product.

Write

\[
c_i(t)=3^{3J_i+H_i}/2^{4J_i+H_i+a_i(t)},\quad
C_i(t)=\prod_{j<i}c_j(t),\quad C_0=1,
\]
\[
\eta_i=\kappa-(16/27)^{J_i}(12/11+(2/3)^{H_i}).
\]

Every eta_i lies strictly between 0 and kappa, as in L077.
L084's independent C/H audit verifies eta_24>=eta_0>2 throughout
the requested range. Its eta_0 bound holds even at H_0=3, and its
monotonic comparison uses J_24>=J_0,H_24>=H_0. The same audited
data give 2(1-lambda_+)/lambda_+=39999999995766/2117>47.
Thus L077 (3) holds with e=2, independently of every O/S test,
J guard and boundary rejection test.

Use only L077's endpoint proof, (7)–(10). With n_i=s_i-kappa,
it gives the unique real cyclic tuple and the identities

\[
D=\exp(\Lambda)-1>\Lambda>\lambda_-,\qquad
S(t)=\sum_{j=0}^{24}\eta_j/C_j(t),\qquad n_0=S(t)/D,
\]
\[
n_i=C_i(t)\left(S(t)/D+\sum_{j<i}\eta_j/C_j(t)\right).
\tag{4}
\]

In particular C_25=exp(-Lambda)<1 is retained in D, and the tuple
is rational and positive. L077's independent domain argument also
gives every n_i>47: unchanged tail-2 rows before row23 have c_i>2,
so their incoming prefixes are at least one and n_i>=n_0>
eta_0/D>47 for i<=23. For the varying final input L077 (10)
instead gives n_24>eta_24/D>47. Closure repeats n_0. No growth of
either varying row or location of a minimum is assumed. All log
arguments in (2) are therefore positive.

### Restricted H cap with complete incoming data

The full theorem L083 cannot be invoked: L084 and Attempt 032
record the failed S row0 test for these tables. We justify only its
earlier fixed-root proof cases (6)–(9), using (4) and independently
matched H data. The values t=0,1 are hypotheses here, so no C077a
reduction is needed to put t in [0,m] with m=1.

Use L084's independent H package, not C's t=2 package:

\[
w_d=10^8(2/3)^{d-1},\quad L_0=1,\quad
L_i=w_d2^{i-1}\ (1\le i\le24),\qquad L_*=\min_i L_i=1.
\tag{5}
\]

L084 (5) and its completed all-member C/H audit establish every
incoming bound C_i(1)>=L_i for 0<=i<=24. Specifically row0 has
c_0=3^63/2^73*(2/3)^(d-1)>w_d. Rows1–23 have unchanged pairs
J>=15,H>=72 and actual tails at most 20; the audited weaker
tail-38 comparison gives c_i>=3^117/2^170>2. Multiplication gives
all the stated incoming bounds, including input24. For i<=23,
C_i(t)=C_i(1); for i=24, C_24(t)=C_24(0)2^(-18t)>=C_24(1).
Thus the bounds apply at both specified roots. No lower bound is
imposed on C_25; row24's compensating tail remains in (4).

The actual L_*=1 follows since w_d>=w_33>1. Retain the complete
finite reciprocal sum and define

\[
Q_d=\kappa\sum_{i=0}^{24}1/L_i
=\kappa\left(1+\frac2{w_d}(1-2^{-24})\right),\qquad
R_H(d)=Q_d/\lambda_-+Q_d+\kappa.
\tag{6}
\]

L084's all-member audit certifies R_H(d)<20000000000<exp(24)
for every requested d. Its display (7), limited to d<=4, is not
used to extend that scope. As an exact finite applicability check,
w_d decreases and Q_d increases with d, and

\[
w_{33}=\frac{429496729600000000}{1853020188851841}>1,\qquad
R_H(33)=\frac{208953172694278031610263934769714811527}
{10486541660339652526080000000}<20000000000.
\tag{7}
\]

The positive degree-40 exponential lower sum at 24, already audited
in L084, certifies the latter exponential threshold. The H cap uses
actual L_*=1 throughout, rather than C's different L_24 denominator.

Now (4)–(6) imply 0<S(t)<Q_d because every eta_j<kappa.
Every proper partial sum in (4), including the empty one, is
nonnegative and strictly below Q_d. At each incoming index,

\[
0<\frac{s_i}{C_i(t)}
=\frac{S(t)}D+\sum_{j<i}\frac{\eta_j}{C_j(t)}
                    +\frac{\kappa}{C_i(t)}
<Q_d/\lambda_-+Q_d+\kappa/L_*<\exp(24).
\tag{8}
\]

Thus log s_i<24+log C_i(t). All divisions have positive
denominators; strictness already follows from S<Q_d and D>lambda_-.
This establishes the needed restricted implication without any
J/H guard, successful O/S conjunction, minimum or seed premise.

### Own-input row18 and exponent directions

Put A_i=sum_(j<i)(3J_j+H_j) and
D_i^0=sum_(j<i)(4J_j+H_j+2). The actual incoming denominator
exponent is D_i(t)=D_i^0 for i<=23, and
D_24(t)=D_24^0+18t>=D_24^0. Thus the incoming lower bounds use
t=1, while the larger H upper expression uses t=0. Both directions
are required, even though row18's prefix itself is independent of t.

L084's audited analytic bounds have 0<ell<log2 and log3<u.
Since both coefficients below are positive, (8) gives

\[
\log s_i+J_i\log(27/16)-H_i\log2
<24+(A_i+3J_i)u-(D_i^0+4J_i+H_i)\ell.
\tag{9}
\]

This keeps each outgoing pair attached to its own input. At row18
that pair is unchanged: J_18=693015,H_18=3295208. L084 (9) and
its audited prefix sums give
A_18=6078923-(d-1), D_18^0=6862840-(d-1). Consequently the
right side of (9) is exactly

\[
24+(8157968-(d-1))u-(12930108-(d-1))\ell
=-457745289/50000000000-(d-1)(u-\ell)=F_{18}(d).
\]

Because u>ell, its maximum for d=6,...,33 is F_18(6)=
-203648044633/100000000000<0. This proves (2) at both specified
roots for every requested table. One strict failure of the required
positive H margin suffices; no verdict on the other guards is needed.

### Sources, finite checks and limits

Import formal affine composition and its nonzero-denominator fixed-point
identity from Halbeisen–Hungerbuehler, *Optimal bounds for the length
of rational Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
already specialized in L077. Integer rows specify a finite nonempty
formal word; (3) supplies the nonzero denominator. No coding reproof
or parity-realization converse is used. The positive-real analytic
inputs are the previously assessed [DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19). Import L084's audited
outward bounds, finite reciprocal/factor coverage, exponential threshold
and amplified errors. This attempt does not independently re-audit
those analytic inputs.

The finite applicability certificate is
`scripts/postspell-word-count/uniform-literal-survivor-h-applicability-certificate.json`.
It records every L_i, the complete reciprocal sum, Q_d,R_H(d), both
row18 coefficients and F_18(d), with operands, exact differences and
verdicts for 84 successful rational comparisons over all 28 tables.
It checks the arithmetic (5)–(7) and (9), not the imported analytic
or incoming-factor proofs. The full relevant extreme comparisons were
inspected; no certificate preview is used to establish the imported
coverage. L088's audited d5 proof is comparison only, not a theorem
for this range; L091/L092 are downstream motivation only.

No allocation assembly, cyclic-order reduction or actual-word transfer
is performed. The failed full sufficient conjunction in Attempt 032
remains a valid stop, and neither d=0 witness falls within this scope.
Universal eventual descent remains unresolved. The separate critical
audit below checks this restricted applicability and its imported evidence.

### Independent critical audit — 2026-10-21, step 394

The pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-21-uniform-literal-survivor-h-critical-audit.md`
licenses this RESEARCH/REPRODUCTION audit. No defect was found in the
stated 56-root scope. This validates an existing local input; it supplies
no additional exclusion or mathematical discovery beyond the checked
sources. The full L083 theorem remains unavailable in this range.

**Endpoint hypotheses and closure.** A separate transcription of all
25 pairs agrees with L055's canonical table. For each d=6,...,33 only
H_0,H_24 change; every H>=7 and the J values are strictly increasing.
Both complete tail lists independently give K=397573379,N=630138897
and total tail 166504460. Subtracting kappa from (1) yields exactly
n_(i+1)=c_i(n_i+eta_i), with both subtracted offsets inside tail division.
Thus L077 (7)–(10), including the closing edge, applies under (3) alone.
It does not require its boundary rejection tests or any O/S tests.

For all rows, positive integer J,H imply 0<eta_i<kappa. The audit
checks eta_0>2 separately at each changed H_0, and also the weaker
eta(8,3)>2. Monotonicity in J,H and the checked final-row comparisons
give eta_24>=eta_0. Positive Lambda makes C_25<1 and the affine
fixed point unique among all real tuples; the nonzero denominator
and rational coefficients give rationality. L077's strict domain
bound 2(1-lambda_+)/lambda_+>47 applies. Unchanged tail-2 prefixes
give n_i>=n_0>47 for i<=23, whereas the positive-coefficient formula
for n_24 gives n_24>eta_24/D>47 separately. Closure repeats n_0.
No growth of a varying row or minimum location enters this reasoning.

**Every incoming factor and the complete cap.** For each d the exact
row0 multiplier 3^(64-d)/2^(74-d) exceeds w_d. Every actual row1–23
factor in each of the two full allocations is checked by a rational
interval for log(c_i/2), with its entire exponent retained; every
lower endpoint is positive. The common weaker comparison
3^117/2^170>2 is also checked, with J>=15,H>=72 and tail<=38
verified separately for these rows. In particular row23's actual
tail20 at t=1 is retained. Multiplication proves C_i(1)>=L_i for
all incoming indices0–24, with L_0=1 and actual L_*=1. C_25 is
excluded from these lower bounds and retained in the root denominator.

All 25 reciprocal terms are reconstructed for every d, and their sum
agrees with (6). All 28 caps are strictly below 20000000000. Their
largest value is the exact R_H(33) in (7); the minimum w is the
stated w_33>1. This independently establishes the changed-range cap
coverage rather than extrapolating L084's d<=4 display (7) or using
C's different L_24 cap. For either fixed parameter, (4) and
0<eta_i<kappa give S<Q_d and every proper partial sum <Q_d.
With D>lambda_- and C_i>=L_i, this proves (8) strictly at every
incoming input, without J/H guards, seed or minimum premises.

**Opposite parameter directions and own-input sign.** Both complete
denominator-prefix lists are reconstructed. For i<=23 the incoming
exponents are independent of t; input24 has exactly 18t additional
halvings. Hence m=1 supplies incoming lower bounds, while t=0
supplies the larger H upper expression. The final outgoing tail
compensates in both complete exponents N. Row18 keeps its own pair
(693015,3295208) and the exact prefixes
A_18=6078923-(d-1),D_18^0=6862840-(d-1). Both coefficients in
(9) are positive. All 28 resulting bounds agree with (2), whose
maximum is exactly -203648044633/100000000000 at d=6. The true
H margin is strictly smaller, so it cannot meet the strict positive
guard for either endpoint root. Other guards need no verdict.

**Independent arithmetic and analytic evidence.** Run
`python3 scripts/postspell-word-count/audit_uniform_survivor_h.py`.
It imports or executes no construction or earlier audit module. It
reconstructs every mathematical field of L093's applicability
certificate, including all 84 comparisons with operands, differences
and verdicts; only its free-text kind label is omitted from comparison.
All 1672 leaf comparisons and 12781 proof checks pass, with zero
failures. These include bookkeeping and repeated factor checks, not
that many distinct mathematical claims. Full evidence is in
`scripts/postspell-word-count/uniform-literal-survivor-h-audit-certificate.json`;
the original applicability certificate remains unchanged.

The analytic reconstruction applies the cited positive-real series
scheme independently: for z=1/3,1/2 it generates all 100 terms
2z^(2k+1)/(2k+1), k=0,...,99, and the upper remainder
2z^201/[201(1-z^2)]. These arguments meet the assessed domains.
Positive omitted terms make the lower endpoints strict. Writing the
intervals as (l2,h2),(l3,h3), it checks ell<l2 and h3<u, and
lambda_-<N*l2-K*h3<N*h2-K*l3<lambda_+ with amplified errors
N(h2-l2),K(h3-l3) retained. Thus the near-cancellation in Lambda
is handled before positivity or division is used.

The degree-40 positive exponential sum is independently regenerated as
202750314819830504045671593478515759301/7661655986496068058455078125,
strictly between 20000000000 and exp(24). For each row18 coefficient
pair P,R, the outward excess of P*u-R*ell over P*log3-R*log2 lies
strictly between P*(u-h3)+R*(l2-ell) and P*(u-l3)+R*(h2-ell).
Both exact error endpoints, their positive order and every actual-factor
interval are stored and checked for every d and both tails. Complete
selected Lambda/error intervals, the exponential sum and the empty
failure list were inspected; previews are not the arithmetic proof.
The general series and affine results remain precise cited imports,
not re-proved analytic or coding theorems.

The direct mathematical inputs remain L055,L077,L083,L084. L088 is
method comparison only; L091/L092 are prospective downstream inputs,
not premises here. Attempt 032's full-support failure and both d=0
witnesses remain valid. No allocation assembly, cyclic-order reduction
or actual-word transfer follows from this audit alone. The argument
and DAG are unchanged, so PROOF.md and DAG.md are not edited for
audit status; this canonical audit supersedes their pending-audit
wording for L093. Universal eventual descent remains unresolved.

## Mathlib

Full matching coverage for this changed-range fixed-root implication
has not been checked. Supporting affine, finite-sum and log/exp facts
do not constitute a matching theorem. Unknown coverage is not absence;
no Lean verification is claimed.
