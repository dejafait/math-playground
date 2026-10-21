# L058 — fixed conductor-36 CM quadratic coefficient at seven

## Hypotheses

Use the globally minimal elliptic curve E: y^2=x^3+1, differential
dx/(2y), conductor 36 and normalized rational weight-two newform of
L057. Retain L057's audited CM-inclusive ordinary analytic convergence,
optimal degree-one differential scale one and total minimal real period.
Use its primitive untwisted trivial Teichmuller branch, generator
kappa(gamma)=8 and coefficient a_2=[T^2]L_7(E,T).

Use audited L056's exact normalized functional F on the full relative
integral module modulo torsion, with all 72 original generators and the
13-dimensional quotient in `scripts/conductor36-table/presentation.json`.
Its reduced common denominator is 12. Put S(r)=F({infinity,r}); no new
calibration or scale is imposed. Source and fixed-instance qualifications
of these inputs remain in force. No lower vanishing, rational rank or
Sha hypothesis is imposed.

The new finite evidence is `scripts/conductor36-quadratic-seven/certificate.json`.
The independent complete replay is
`scripts/conductor36-quadratic-seven/verification.json`, together with its
fresh complete upstream table and structure reports. These are finite
known-method certificates, not a universal software correctness theorem.

## Conclusion

In precisely this primitive normalization,

    v_7(a_2 + 715533/8540717056) >= 2,
    a_2 != 0,    v_7(a_2) = 1.

The scheduled n=2 attempt is inconclusive; n=3 is the first strict
success and n=4 is not executed. Complete independent production replay
passes. The separate fixed critical audit below also passes.

This is reproduction of known analytic and finite modular-symbol methods,
not a BSD candidate or a new rank theorem. It supplies no lower-coefficient
vanishing, rational direction, finite/full Sha result or comparison with
complex order. The non-CM arithmetic implication L004 is unavailable.

## Proof

**Imported analytic input and exact finite domain.** Apply L057 under
its unchanged audited hypotheses. Its authority for CM-inclusive
convergence and coefficient bounds is Balakrishnan--Muller--Stein,
*A p-adic analogue of the conjecture of Birch and Swinnerton-Dyer for
modular abelian varieties*, Math. Comp. 85 (2016), 983--1016,
[DOI 10.1090/mcom/3029, Section 2.2, equations (2.6)--(2.9),
Proposition 2.9 and proof, pp.991--993](https://wstein.org/papers/mcom3029.pdf#page=9).
The all-level denominator and root substitution specialization are the
proved L057 result; they are not reproved or extended here. L056's
independently isolated analytic table supplies the actual normalized
values, not merely relation-compatible guesses.

For the complete relative presentation and path identification retain
L056's source imports: Stein, *Modular Forms, a Computational Approach*,
GSM 79 (2007), [equation (3.2.1), Propositions 3.10--3.11,
Theorem 3.13, pp.40,42--44](https://wstein.org/books/modform/stein-modform.pdf),
and Cremona, *Algorithms for Modular Elliptic Curves*, corrected second
edition (1997), [Propositions 2.2.1--2.2.2,
pp.15--16](https://johncremona.github.io/book/fulltext/chapter2.pdf).
These apply at composite level 36 and include relative boundary directions.
The approved prior assessment is
`drafts/literature/2026-10-13-conductor36-cm-quadratic-seven-production.md`,
SPECIALIZE. Citations alone do not compute the finite residues, paths or
sum for this model; that fixed execution is the purpose of this certificate.

**Independent ordinary arithmetic and root precision.** Exhaust all
49 pairs (x,y) modulo seven in y^2=x^3+1. The counts at x=0,...,6 are
[2,2,2,1,2,1,1]. There are eleven affine points and the point at infinity,
so t=8-12=-4. The discriminant -432 is nonzero modulo seven and t is a
unit. The ordinary root polynomial is h(X)=X^2+4X+7. At both reached
precision levels the producer obtains the rational integer unit u=304:

    u mod 7 = 3 = -4 mod 7,
    h(u) = 93639 = 39*7^4,
    h'(u) = 612 = 3 mod 7.

Thus v_7(h(u))=4 and the derivative is a unit. This meets M=3 at n=2
and M=4 at n=3. The replay independently enumerates all integers modulo
7^M in residue class 3 satisfying h(u)=0 modulo 7^M and finds exactly
this one. L057's Hensel application therefore identifies the ordinary
unit root within precision M; no approximate floating root is used.

**Complete residues and oriented paths.** At each reached depth n,
construct every w_(n,d), d=1,...,6, in [1,7^n-1], with residue d modulo
seven and w^6=1 modulo 7^n. The n=2 values in d order are
[1,30,31,18,19,48]; the n=3 values are [1,324,325,18,19,342]. Replay
independently enumerates candidates in each residue class and verifies
uniqueness, every exact sixth-power residual and every derivative
6w^5 modulo seven. The residual zero at w=1 is retained with infinite
valuation. Every other residual has valuation at least n and every
derivative is a unit.

For every d and 0<=j<7^(n-1), form the least positive residue
r=w_(n,d)*8^j modulo 7^n. The entire list equals every unit modulo
7^n exactly once; replay checks this equality, without discarding any
j=0,1 or zero-valued symbol. Evaluate both

    A=S(r/7^n),   B=S(r/7^(n-1)).

Each saved path runs from infinity to the exact reduced rational
argument. Continued-fraction convergents give adjacent endpoints,
with a determinant-one segment matrix h sending 0 to the start and
infinity to the end. Production locates its coset by the complete unit
orbit of the bottom row modulo 36. Replay independently partitions all
864 primitive pairs into 72 unit orbits and checks every stored lift.
For each segment it tries all 72 lifts g_i and finds exactly one with
h*g_i^(-1) in Gamma_0(36); it verifies the determinant, exact matrix
product, lower-left divisibility, ordered endpoints and telescoping.
This includes noninvertible bottom-left entries, rather than applying
a prime-level modular inverse formula.

Let raw be the resulting 72-coordinate integral generator sum and let
c be its integral image in the full 13-dimensional quotient. Every
path is checked by both raw evaluation on all L056 table values and
c evaluation on all thirteen quotient functional values. They agree
exactly. Source relations and all saturated columns vanish on the
normalized table, all 72 generators reconstruct in the quotient, the
common denominator is 12 and all sixteen zero generator values remain.
Thus these are the actual S-values in L057's orientation. Since seven
does not divide twelve, the all-level denominator loss is C=0.

**Every binomial term and both finite attempts.** Include all six
classes and every j, with the integer weight j(j-1)/2, also at j=0,1.
At each reached n compute the exact sum in L057 equation (2):

    b = sum_(d,j) binom(j,2)*(u^(-n)*A - u^(-(n+1))*B).

The producer stores every residue, both path references, both rational
symbols, binomial weight and exact term. The checker derives r by
repeated multiplication, independently reconstructs every path value,
checks each term, and accumulates both weighted symbol sums at integer
scale twelve. Write SA=sum binom(j,2)*A and SB=sum binom(j,2)*B.
The complete replay gives:

| n | M | u | actual/required terms | SA | SB | b | v_7(b) | N=min(n-1,M) |
|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 304 | 42/42 | 0 | -35 | 35/28094464 | 1 | 1 |
| 3 | 4 | 304 | 294/294 | -2331 | 6909 | -715533/8540717056 | 1 | 2 |

In addition to term-by-term rational summation, the replay uses

    b=(u*(12*SA)-(12*SB))/(12*u^(n+1)).

The integer accumulated pairs (12*SA,12*SB) are (0,-420) and
(-27972,82908). At n=3, the numerator before reduction is
304*(-27972)-82908=-8586396=-12*715533; hence b=-715533/304^4.
Now 715533=7*102219 with 102219 not divisible by seven, and 304 is a
unit. Both finite b-values therefore have valuation exactly one.
The n=2 comparison 1>1 fails and remains saved as inconclusive.
At n=3 the strict comparison 2>1 holds, so the bounded schedule stops
there. No n=4 or extrapolation beyond the approved schedule is performed.

**Limiting inference and normalization.** L057 at n=3, M=4, C=0 gives
v_7(a_2-b)>=min(2,4)=2. Since v_7(b)=1, the strong triangle inequality
forces a_2 nonzero and v_7(a_2)=1. This is a limiting analytic conclusion,
not simply nonvanishing of a finite sum. It does not assume either
lower coefficient vanishes. All six classes are summed without an
average, generator 8 is unchanged, and the primitive interpolation
multiplier (1-alpha^(-1))^2 is retained. No bad-prime Euler factor,
period factor, scale or non-CM arithmetic hypothesis is transferred.

**Complete replay, preservation and limitations.** Reproduce from the
active notebook:

    python3 scripts/conductor36-quadratic-seven/build_certificate.py
    python3 scripts/conductor36-quadratic-seven/verify_certificate.py

The checker imports no coefficient producer. Its complete report verifies
630/630 distinct paths, 3375/3375 segments and 336/336 terms across the
two attempts, every root/residue test, both integer sums, first strict
stopping and absence of unused paths. All eleven final checks pass with
zero failures. It invokes unchanged complete upstream verifiers, writing
fresh reports `scripts/conductor36-quadratic-seven/coefficient-upstream-structure.json`
and `scripts/conductor36-quadratic-seven/coefficient-upstream-table.json`.
The first replays all 864 orbit assignments, 144 source relations,
59 saturated columns, 144 structural/reflection paths and 626 segments;
all actual/required counts match. The second replays all 476280 Fourier
terms including zeros, all 1316 signed occurrences, 288 quotient endpoints,
72 integer isolations and all complete table/period/geometry/tail evidence.
The code checks the complete relevant inputs, not a preview or historical
audit flag. The full original inputs and all 98 table term files are
bound by SHA-256 before production and unchanged after replay. Hashes
supplement this arithmetic replay, rather than replace it.

An initial binding attempt named a nonexistent optional upstream verifier
filename and stopped before arithmetic. Its failure is preserved at
`scripts/conductor36-quadratic-seven/initial-binding-failure.json`.
The filename was corrected to the actual `verify_compressed_plan.py`
before final production/replay; there is no remaining validation failure.
The earlier preliminary finite certificate is preserved separately at
`scripts/conductor36-quadratic-seven/initial-finite-certificate.json`.
Original notebook certificates, reports and failed schedules are retained.
No changed source hypotheses or new analytic theorem is needed.

This closes this fixed finite coefficient-production gap under the
imported audited inputs. The separate critical audit below verifies the new executable
assembly under these unchanged hypotheses. Uniform useful coefficients, rational Kummer
directions, Sha and arbitrary complex-order/rank equality remain open.

**Separate fixed critical audit, 2026-10-14, BSD-200.** The prior
SPECIALIZE assessment
`drafts/literature/2026-10-13-conductor36-cm-quadratic-seven-critical-audit.md`
approves exactly this audit. The analytic theorem and its applicability are
reused through audited L057, with the precise primary citation above. This
is not a new source import, strengthened bound or removal of L004's
non-CM restriction. Audited L056 supplies the actual full-relative table;
its normalization, all-level denominator and upstream source qualifications
remain essential.

The complete producer and separate verifier were reviewed before execution.
The script `scripts/conductor36-quadratic-seven/audit.py` preserves the
original programs and coefficient evidence, and records all 649 original
files in `scripts/conductor36-quadratic-seven/critical-audit/pre-replay-manifest.json`.
This includes every bound upstream input, all table term files and the
original reports and failure artifacts in the table and nonunitary-cusp
folders. Optimized assertions and bytecode writes are disabled. The unchanged
programs run with ROOT redirected beneath `critical-audit/`; upstream input
paths are unchanged, and all transitive report writes are isolated. An
independent rebuild gives the identical certificate bytes. This byte
comparison supplements, rather than replaces, complete arithmetic replay.

The fresh complete replay in `critical-audit/replay/verification.json`
checks all 630 original paths, 3375 segments and 42+294 terms. Its entire
report agrees with the original after changing only output paths. Both
fresh upstream reports agree in full with their originals: structural
replay checks all 864 orbit assignments, 72 cosets, 144 relations, 59
saturated columns, 144 structural/reflection paths and 626 segments,
including both transform inverses. Table replay checks all 476280 finite
Fourier terms (423360 zero-coefficient terms retained), 149760 cosine
steps, sixteen attenuation brackets, 1316 signed occurrences, 288 period
quotient endpoints, 72 integer isolations and all relation/reconstruction
identities. The table's actual width remains at most 2^-60, strictly below
2^-38; the full upstream tails and positive total-period replay pass.
Historical upstream plan fields saying that a table was not yet produced
retain their original scope; the fresh full-table replay is complete.

For each of the 630 exact positive nonintegral arguments r=a/b, the audit
constructs a different chain using the ceiling Euclidean algorithm:
k=ceil(a/b), remainder=k*b-a, and (a,b) is replaced by (b,remainder).
Every remainder satisfies 0<=remainder<b, so this terminates. Exact
backwards evaluation of the negative continued fraction gives r. Starting
with (p_0,q_0)=(0,-1) and (p_1,q_1)=(1,0), the updates are
(p_2,q_2)=k*(p_1,q_1)-(p_0,q_0). Every new denominator is positive and
every p_2*q_1-p_1*q_2 is -1. Thus

    h = [-p_2, p_1; -q_2, q_1]

has determinant one and maps 0 to the preceding endpoint and infinity
to the next endpoint. Ordered endpoint checks give adjacency and exact
telescoping from infinity to r. Because every reduced denominator is
divisible by seven, r is nonintegral: its ceiling first endpoint differs
from the saved floor first endpoint. The audit checks this for every path.
These are applications of the already cited arbitrary-level Manin path
presentation, not an inference of path equivalence from scalar agreement.

For each of the 7515 alternate segments, all 72 supplied integral lifts
g_i are tested. Exactly one h*g_i^(-1) has lower-left entry divisible by
36; its determinant and full product with g_i are checked. This uses no
prime-level inverse, and includes noninvertible bottom-left residues.
Summing these segments gives a new integral raw vector. For its difference
delta from the original raw vector, the saved normal-form head and K
matrices give the integer witness c=head*delta with K*c=delta. Independently,
all thirteen quotient coordinates of delta are zero. The full saturation
contract already replayed upstream therefore identifies the two paths in
the integral relative quotient modulo torsion. Every raw vector differs
from the original, while every quotient and both functional evaluations
agree. `critical-audit/alternative-paths.json` retains every original and
alternate segment, raw vector, quotient, Euclidean remainder and saturated
relation witness. No boundary direction is discarded.

The audit independently enumerates all six roots at each reached depth
and the ordinary root modulo 7^M, and reconstructs every argument pair.
It evaluates only the alternate paths and accumulates integers at scale
twelve, using sum(range(j)) for the binomial weight. All j=0,1, all zero
values and all j>2 contributions are retained. Every reconstructed term
is compared with the production term. The six class-wise integer pairs
are recorded in `critical-audit/integer-sums.json`; their total pairs are
again (0,-420) and (-27972,82908). Integer numerator accumulation and
independent rational term summation give the two b-values in the table
above. This verifies both root powers and both argument denominators,
not only a final scalar or a historical verification flag.

For the limiting application, h(304)=93639=39*7^4, h'(304)=612 is a unit,
and C=0 follows from denominator twelve on the entire integral module.
Both finite sums have valuation one. L057's all-level closed-lattice tail
and root-substitution estimate therefore give N=1 at n=2 and N=2 at n=3.
Equality at depth two stays inconclusive. Only the strict depth-three
inequality 2>1 yields the stated valuation of a_2. The source measure's
primitive multiplier, all six classes without averaging, generator eight,
infinity-to-r orientation and total-period convention remain unchanged.
No lower coefficient was set to zero and no depth-four calculation occurs.

Four altered copies separately change gamma, one full-quotient coordinate,
one root residual, and one nonzero j>2 weighted term at depth three. Each
run completes fresh upstream replay and then fails at exactly its intended
assertion. Each replaces a seeded successful report (with a unique stale
sentinel) by a fresh failure report with empty results; traceback checks
identify the intended failed expression. All altered inputs, full reports,
command logs and their digests remain in `critical-audit/rejections/`.
These bounded rejection tests supplement the complete positive replay and
do not establish universal verifier correctness.

The final `scripts/conductor36-quadratic-seven/critical-audit/audit.json`
records 17 passing checks, no audit failures, all four intended rejections,
and no changed original files. The missing-filename failure and preliminary
certificate are preserved. Reproduce this isolated audit from the active
notebook with

    python3 scripts/conductor36-quadratic-seven/audit.py

This closes the pending critical verification of this fixed known-method
coefficient certificate. It is local progress in assurance, not progress
beyond the checked source theorems, a CM arithmetic implication, or a BSD
candidate. The direct mathematical inputs remain L056 and L057; no DAG
edge is added. All rational-direction, Sha and complex-order gaps remain.

## Mathlib

Full matching coverage of this CM analytic coefficient certificate, its
full relative-symbol computation and its finite-to-limiting assembly has
not been checked. Supporting exact arithmetic is distinct from the full
statement. Unknown coverage is not absence; no formal verification or
novelty is asserted.
