# Penultimate Jacobi test1504: working checkpoint

Gate: unchanged EXPLORE assessment1503, explicitly approved by this
invocation. One research attempt; no additional source review needed.
Main gap and test are those in assessment1503. C028a/C028b, L018/L021,
L025/L027 and source-notes1503 were read; the changed-series and finite
moment stops remain contrasts. No claim of novelty follows from reuse.

Let v=S_2>0, t=S_3>0, delta=m+b_1 and A=s-v. Write H_n for the monic
Hermite polynomial in x-m with variance s. Directly from the stipulated
recurrence, pending full coefficient verification:

    q_(d-1)=H_(d-1)-u H_(d-2),
    q_d=H_d-(u+w)H_(d-1)
        +[uw+(1-r)s(d-1)]H_(d-2)-u s(d-2)H_(d-3).

The actual polynomial has Hermite expansion
P_d=sum binom(d,k) g_k H_(d-k), where g_k/k! is the coefficient of z^k
in F(z) exp(mz+sz^2/2). The local logarithm from L025 yields

    g_1=delta, g_2=delta^2+A,
    g_3=delta^3+3delta A+2t,
    g_4=delta^4+6delta^2 A+8delta t+3A^2-6S_4,
    g_5=delta^5+10delta^3 A+20delta^2 t+15delta A^2
        -30delta S_4+20A t+24S_5.

The matching constraints should therefore reduce to

    u+w=-d delta,
    uw+(1-r)s(d-1)=binom(d,2)g_2,
    -u s(d-2)=binom(d,3)g_3.

If matched, a_(d-4)=binom(d,4)g_4 and a_(d-5)=binom(d,5)g_5.
The exact denominator has the factor r; no uniform lower bound on s
or r is assumed. Pending: verify these identities, derive all-scaling
positive-parameter restrictions, and decide the retained-cost test.
Nothing in this working checkpoint establishes a pass or obstruction.

## Completed attempt, superseding the pending calculations above

The identities above are proved in canonical C028c. Positivity gives
delta^2<=8v/3, s<=5v/3, rs<=dv/2 and g_3=O(1/d) uniformly over
all feasible choices, including vanishing s,r. Under g_3=g_4=g_5=0,
elimination produces a degree-six polynomial and a cubic with a common
root. Their scaled Sylvester determinant lies strictly between
-21.518952570 and -21.518952569, so no such common zero exists.
Compactness then supplies B_d>=c*d^4 eventually, with c>0 independent
of the feasible parameter choice. This is a bound-only family stop.

Actual finite coefficients come directly from L778's already audited
entire evaluator, not L827's representing measure or compensated law.
Read L778's evaluator, complete analytic tails and step433 audit;
add E_G/1600^j before converting its first six coefficients to F.
This is an implementation of assessment1503's stipulated actual top-five
coefficient calculation, with unchanged target/hypotheses and explicit
inherited arithmetic contracts; it does not reopen the L827 sequence.
No new source theorem or stronger coefficient assumption is introduced.

Full arithmetic evidence: scripts/jacobi-reference/penultimate-cost-1504.json.
The same certificate proves (9v/10)^3-S_3^2>1.6659e-14, allowing an
explicit positive matching family (u=0, s=v/10). Thus the negative
result is a residual-cost obstruction, not merely unproved feasibility.
Full proof, citations, qualifications and reproduction command: C028c.
Independent conceptual/arithmetic audit remains pending; no RH claim.
