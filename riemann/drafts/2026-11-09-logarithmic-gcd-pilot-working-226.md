# Critical logarithmic gcd pilot — step226

Approved target: the unchanged COVERED_TARGET in
drafts/literature/2026-11-09-logarithmic-gcd-critical-coercivity-review.md.
Essential input: audited L737 (5)–(7), (11), and the source-covered
Hermitian Rayleigh theorem. No theta, moment or Xi sign is assumed.

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
Intermediate target: one finite diagnostic of F_(2 log N)/Q at
N=2^j, 1<=j<=9. Sharper arithmetic norm control might inform
multiplier lengths; conditioning, moment errors, realization and
signed transfer remain independent gaps.

Plan saved before calculation: diagonalize the real symmetric form in
y_d=sqrt(phi(d))B_d only to choose trials. Round B coordinates to
integers and use finite Möbius inversion to obtain integer b, with
c_n=sqrt(n)b_n. Evaluate the exact original gcd form and the complete
divisor form independently. Certify logarithms by a finite rational
atanh series with a rigorous positive tail bound; certify Q exactly.
Store every vector and coefficient in scripts/logarithmic-gcd/.

Continuation test: identify an explicit scalable pattern or a specific
analytic bound worth separate source review. Finite positive or
negative trials do not bound the whole spectrum or settle an absolute
C. Without such a mechanism, park the numerical route after this grid.
Do not enlarge the grid to renew exploration. No general inequality is
proved or approved by this pilot.

Existing unfinished work is preserved. No lemma, DAG or PROOF change
is planned for a purely diagnostic outcome.

## Completed bounded attempt

Reused the supplied EXPLORE assessment unchanged. Narrow local searches
found no duplicate resolution or pilot of this exact form. Read L737
including its separate audit in full. Its short-dictionary exclusion
does not decide this threshold; no fresh literature was needed.

The full certificate is scripts/logarithmic-gcd/critical-pilot-226.json;
the companion Python script generates it and replays all exact values.
In y_d=sqrt(phi(d))B_d coordinates the floating symmetric numerator
has diagonal 2 log N+2 kappa(d), and off-diagonal entry
-Lambda(r)sqrt(phi(d)/phi(dr)) at (d,dr) for every prime power r>1.
The denominator is sum y_d^2. This is exactly the real specialization
of L737 (6)–(7), retaining every kappa and cross term. The source-covered
Rayleigh theorem permits selecting a floating least-eigenvector as a
trial, without certifying the spectrum.

For each N, rescale the resulting B to maximum absolute value 1,
multiply by 10^9 and round to integers. Save every entry. Finite
Möbius inversion gives integer b and the admissible real vector
c_n=sqrt(n)b_n. Rational b rather than rational c is expressly
permitted by the assessment. Exact arithmetic verifies every B_d,
Q=sum phi(d)B_d^2=sum gcd(m,n)b_m b_n>0, and every coefficient of
log p in F in two independent arrangements: original gcd pairs and
divisor/prime-power sums. The diagonal logarithmic correction in the
original formula vanishes; the 2 log N Q term includes every pair.
In the divisor expression phi(d)/(p-1) is integral when p|d, so the
kappa contribution is also evaluated with integers, without rounding.

For the logarithm certificate write p=2^k a, 1<=a<2, and put
t=(a-1)/(a+1) in [0,1/3]. The convergent identity is
log a=2 sum_(i>=0) t^(2i+1)/(2i+1). Floor each of 100 summands
at scale S=10^80. If L is twice the sum of these integers, then
S log a lies in

    [L, L+200+ceil(2S t^201/[201(1-t^2)])].

Flooring loses less than 200 in total. The omitted positive tail is
bounded by replacing all denominators by 201 and summing its geometric
series. At a=1 the same enclosure is valid. The series at t=1/3
bounds log 2; add k copies of that interval. All operations use
integers. Each exact signed prime-log coefficient selects its proper
interval endpoint. Divide by exact positive Q and S and round outward
to 12 decimal places. Neither floating logs nor eigenvector accuracy
is a premise of the certificate. The complete operations, all vectors,
coefficients, Q values and intervals are saved by the script.

| N | Certified trial F_(2 log N)/Q interval |
| --- | --- |
| 2 | [1.099183398211, 1.099183398212] |
| 4 | [2.015927008219, 2.015927008220] |
| 8 | [2.797007500595, 2.797007500596] |
| 16 | [3.593931046526, 3.593931046527] |
| 32 | [4.294662144040, 4.294662144041] |
| 64 | [5.033788774221, 5.033788774222] |
| 128 | [5.746817297254, 5.746817297255] |
| 256 | [6.460849063012, 6.460849063013] |
| 512 | [7.165157864642, 7.165157864643] |

Every saved vector and exact value was reloaded and recomputed by
--verify, including both full-form arrangements; all nine replays
passed. The floating eigenvector residual at N=512 is approximately
1.41e-14, diagnostic only. Its 512 B entries have the same sign;
this does not assert a scalable extremizer or a global sign theorem.

Reproduction from the notebook:

    OPENBLAS_NUM_THREADS=1 python3 scripts/logarithmic-gcd/critical-pilot-226.py
    OPENBLAS_NUM_THREADS=1 python3 scripts/logarithmic-gcd/critical-pilot-226.py --verify

Outcome: RESEARCH / EXPLORATION / POTENTIALLY_NEW. This is a local
diagnostic under the prior EXPLORE assessment, without a certified
originality claim or new arithmetic inequality. Each trial gives an
upper bound on its finite infimum; positivity of the trials gives no
lower bound on any full spectrum. The required
inf_(N,c!=0) F_(2 log N)/Q>-infinity remains undecided. No matching
Mathlib coverage of the finite certificate was checked. Canonical
identities, source citations and qualifications remain in L737 and
the unchanged prior assessment.

## Decision and uncovered continuation

Park the numerical mechanism after this approved grid: no scalable
negative pattern or analytic bound has been justified, so no grid
extension is warranted. A different proposed analytic lead is the
prime-power row sum in L737 (9). The new source question asks whether
sum_(2<=r<=x) Lambda(r)/phi(r)<=log x+C0 holds with an absolute C0
for every real x>=2, and whether standard coverage permits use in
the exact weighted Schur mechanism. Neither this estimate nor its
sufficiency for the critical form is proved or approved here. The
new REVIEW_REQUIRED assessment nominates a separate source review;
no further arithmetic derivation is undertaken. Conditioning, charged
moment errors, microscopic realization, signed transfer and actual-Xi
mixed positivity remain independent gaps. PROOF.md and DAG.md unchanged.
