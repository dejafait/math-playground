# Step154 — saved bounded attempt

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-10-physical-time-edge-taylor-model-152.md`.
Its separate source-approval gate is accepted for exactly the saved target.
No further literature review is needed. This is a calculation/REPRODUCTION.

Keep N=690988, x=6000000185827, a=98/625, h=27/625 and u=(t-a)/h
in [0,1]. This is an affine storage of a degree12 polynomial in t-a,
not subdivision. At each term write z_n(t)=z_n(a)exp((r_n+i q_n)u)
where r_n+i q_n=h*((log n)^2/4-alpha*log n/2).
Real exp/cos/sin multiplication has degree-j coefficient
z_n(a)(r_n+i q_n)^j/j!, with each complex operation implemented in
two real coordinates. Binomial expansion of the real product gives
this identity; it does not use a complex mean-value theorem.
The absolute series of each real coordinate is majorized by exp(v),
v=|r_n|+|q_n|. Its terms of total degree >=13 are bounded by
exp(v)*v^13/13!. A checked v<=2 and included exp(2)<8 therefore
give component remainder <=8*a_n(a)*v^13/13! after multiplying
by the unit initial phase. The latter multiplication is handled by
the two real coordinate product bounds: each coordinate of the
complex product can instead be bounded safely by twice this value.
Use that factor2, rather than claiming a complex Taylor remainder.
Every coefficient and constant interval keeps its dyadic width.

Sum all degree12 A and L coefficients and component remainder bounds
over complete support. In the final real Taylor-model products, charge
all coefficients of degree>12 and both polynomial/remainder cross terms
and the remainder product. Apply the assessed degree12 Bernstein
conversion only to the final polynomial. Subtract the full signed
remainder and the established E upper bound 203/1000000.

One pass, 600-second cost ceiling, no retry/subdivision/degree escalation.
Success needs a strict positive uniform lower endpoint. An unpaid lower
bound is inconclusive, not a negative physical value. Preserve unfinished
blocks and exact endpoints. Relevant inputs L960/L962/L963; no other
notebook. Analytic/remainder/companion/gauge, spatial/global/zero-time
and Xi mixed-positivity gaps remain independent.

## Stopped execution — no completed model

The single `scripts/physical-corner/time_taylor_154.py` run stopped
after 7.473427666 seconds at its auxiliary assertion v<=2. It saved 11
consecutive blocks through 22528 of 690988 terms. No final A/L model,
carrier product, degree12 F polynomial, Bernstein conversion or paid
sign was produced. The prospective product code remains unexecuted,
not verified by this attempt. All eight startup gates passed; the
600-second ceiling was not the cause.

The choice of 2 was an unjustified estimate, not an imported theorem.
It was wrong. The exp(v) majorant method is not disproved. Failed gates
stop the specified test, so the cap was not increased and the pass was
not resumed. This is implementation-limited EXPLORATION, not a negative
physical sign, a degree12 no-go, or an advance beyond known methods.

`scripts/physical-corner/inspect_taylor_partial_154.py` accounts for all
saved blocks and all 13 complex coefficient intervals in A and L, checks
exact total/remainder sums, independently counts primes, and checks input
hashes and saved domains. It does not replay each term's elementary values.
The stopping diagnostic evaluates only the auxiliary majorant in the
unfinished block with the established direct-log routine, without physical
phases or sums. Its first strict crossing is n=23545. Both r,q are
strictly negative, so -r-q gives a two-sided interval for the true v.
The complete dyadic lower endpoint is

    231584284731444325239459112277938573018960683155461515257037930314380914200124 / 2^256 > 2.

The positive excess lower endpoint is

    106256811934392317142260562757312420713824180387178122762298554654920252 / 2^256.

The cap is actually invalid at this n; no inference about F follows.
All 1154 partial-record/diagnostic checks pass. Full evidence:
`scripts/physical-corner/time-taylor-154.json` and
`scripts/physical-corner/time-taylor-partial-inspection-154.json`.
The complete diagnostic endpoints were inspected, not inferred from
rounded displays. The original traceback remains in
`scripts/physical-corner/time-taylor-154.log`.

Invocation-start source coverage is reused; no new literature comparison
or mathematical input was established. No lemma, DAG or PROOF change is
warranted. A distinct proposed audit isolates L963's uniform payment
input; it resumes neither failed positivity test.
