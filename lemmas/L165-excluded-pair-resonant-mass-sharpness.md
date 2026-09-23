# Lemma 165: excluded-pair resonant mass sharpness

**Hypotheses.** Let N≥1 be real, I be the positive integers in [N,2N],
and fix 0<c≤K. Suppose c N^(−1/2)≤A_n≤K N^(−1/2) on I.
Use the finite sums S,D2,D3,W of L162; in particular W sums ordered
sextuples (a,b,r,s,m,n) with arm=bsn and a≠b, r≠s, m≠n.

**Conclusion.** Uniformly over these amplitudes, as N tends to infinity,

0≤D3−W≤C_K(1+log N),                                    (1)
W ≍_(c,K) (log N)^4,                                    (2)
0≤1−W/D3≤C_(c,K)(log N)^(−3).                           (3)

For the Gaussian amplitudes A_n(t)=T^(3/4)b_n(t) of L155 in the
window [N,2N], N=sqrt(T/(2π)), these conclusions hold uniformly for
T≤t≤2T. In particular W(t)≍(log T)^4. The exclusions remove a
vanishing relative fraction of the positive triple diagonal mass.

**Proof.**

Let E2 count ordered quadruples (u,v,x,y) in I with uv=xy.
Put g=gcd(u,x), u=gr, x=gs. Then gcd(r,s)=1, and rv=sy
forces v=hs, y=hr for a unique positive integer h. Conversely
these formulas always give equal products. For j=max(r,s), the
upper bounds on all four factors imply g,h≤2N/j and j≤2N.
There are at most 2j ordered positive pairs (r,s) with maximum j,
even before imposing coprimality. Dropping the lower window bounds
only enlarges the count. Hence, with J=floor(2N),

E2≤Σ_(j=1)^J 2j floor(2N/j)^2
   ≤8N² Σ_(j=1)^J 1/j≤8N²(1+log(2N)).                  (4)

Each term in D2 has four amplitude factors, so
D2≤K^4 N^(−2)E2≤8K^4(1+log(2N)). There are at most N+1≤2N
integers in I, giving S≤2K². The nonnegative excluded mass is,
by the exact inclusion–exclusion identity of L162,

0≤D3−W=3 S D2−2 S³≤3 S D2
                      ≤48K^6(1+log(2N)).               (5)

This proves (1), without needing a lower bound on the collision mass.
L164 supplies D3≥c1(log N)^4 for all sufficiently large N, with
c1>0 depending only on c, and D3≤C1(log N)^4 with C1 depending
only on K. Subtracting (5), its O(log N) loss is eventually at most
half of c1(log N)^4. Thus W≥(c1/2)(log N)^4, while W≤D3 gives
the matching upper bound. Division of (5) by the lower bound for D3
proves (3). All thresholds and constants are uniform in the amplitudes.

For the Gaussian specialization, L155 defines

b_n(t)=c₀ n^(−2)exp(−log(n/N_t)²),
c₀=exp(π²/16), N_t=sqrt(t/(2π)).

Put u=t/T∈[1,2] and x=n/N∈[1,2]. Direct substitution gives

sqrt(N) A_n(t)
 =c₀(2π)^(3/4)x^(−2)exp(−(log x−(log u)/2)²).           (6)

Here |log x−(log u)/2|≤log 2. Consequently the right side lies
between c₀(2π)^(3/4)exp(−(log 2)²)/4 and c₀(2π)^(3/4).
These constants are positive and independent of T,t,n. Apply (1)–(3)
and use log N=(log T−log(2π))/2 to obtain the uniform assertions. ∎

## Scope, verification

This is an unweighted arithmetic mass estimate. It does not establish
that W is large on the event M<Q<2M, or determine the sign or size of
E_T[χ''(Q/M)W]. The sign-changing cutoff and nonresonant terms remain
uncontrolled. Neither the fixed-cutoff tail target nor RH follows.

Verification is analytic: unique gcd parametrization, the finite harmonic
bound, four- and six-amplitude normalizations, the inclusion–exclusion
sign, and the compact uniform bounds in (6). The existing exact regression
`python3 scripts/heat/check_triple_diagonal.py` checks the identity used
in (5). No finite computation certifies asymptotic growth.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
