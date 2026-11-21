# Zero-moment coefficient attempt — step 208

Invocation-start gate: EXPLORE, exact COVERED_TARGET in
`literature/2026-11-03-complete-response-zero-moment-edge.md`.
The main gap remains actual-Xi mixed positivity. Test only the unchanged
L666/L703 coefficient at u_* for rate at least r(b)/2; prospective use
is spatial Jensen, with angular/global charge and realization unpaid.

Read exact definitions and relevant proofs in L666, L703, L708, L714,
L719, L720 and L723; L721 support argument still to inspect in full.
Existing highest-moment and angular-origin stops have different scopes.
Preserve all prior files and accepted audits.

Working obligations, not established conclusions:

- L714 gives g_n=c_0 p_n-h p_n' on v>0. Use L720 on nested fixed
  complex domains to differentiate its normalized factorial remainder.
  Check leading multiplier c_0-A S'(v)=alpha-u s_v and its separation
  from zero before applying the L721 fixed-density construction.
- The original finite coefficient should be compared to a symmetrically
  paired half-integer comb, with g_n(0+)/2 at the origin and both original
  tails. Separate one-sided absolute sums are forbidden.
- L723 gives |W_n(y)|<=C exp(-n/500)/|y| for |y|>=2/5 and a positive
  frequency tilt bound for g_n. Pair W_n(y)+W_n(-y) at large y; use its
  odd leading rational term, retaining a polynomial cutoff and full
  error. Shift differences may use the real logarithmic derivative
  bound and sum |e_m|<infinity. Check the origin coefficient separately.

The proposed closure now has explicit estimates (pending canonical
write-up and later independent audit):

- For Q_n=n^(-1/2)exp(-nS)p_n, the changed symbol is
  (alpha-u*s_v)Q_n-(A/n)Q_n'. Nested-domain Cauchy estimates give
  coefficients a_tilde_0=(alpha-u*s_v)a_0 and
  a_tilde_k=(alpha-u*s_v)a_k-A*a'_(k-1), with the full factorial
  remainder. Re(alpha-u*s_v)>2/25 on I; ellipticity survives.
- Let beta_n=d*product_(j>=1) r_(j/n). The real tail estimate implies
  |beta_n|<=C exp(-n/500) by the y->infinity limit, and
  g_n(0+)=beta_n/h. The half-integer comb contributes pi*g_n(0+)
  plus the positive 2*pi aliases; negative aliases vanish.
- For y>=16n^2, factor W_n(y)=beta_n/(-iy)*E_n(y). The sum of
  absolute numerator/denominator parameters is <=4n^2, so
  |E_n(y)-1|<=16n^2/y. Therefore the paired tail is bounded by
  32|beta_n|n^2/y^2. Below that cutoff use L723's 1/y bound,
  costing only C*n*log(n+2)*exp(-n/500). Shift differences cost
  C*E*exp(-n/500) from |W_n'/W_n|<=2n/d on the real line.
- These bounds suggest R*G_n(u_*,0)=1-integral chi*g_n+epsilon_n,
  |epsilon_n|<=C exp(-n/1000). The L721 fixed-density construction
  with the changed elliptic coefficients would then give rate r(b),
  stronger than the required r(b)/2. Every summation limit still
  needs its precise convention in the canonical proof.

Continue only after the complete correction cannot cancel the bump on
the same allowed subsequence. A fixed-order expansion, scalar
nonidentity or unpaid exponential loss does not pass. No result yet.

Completion: the estimates above were closed and written in canonical
L725, `lemmas/L725-complete-zero-moment-support-edge.md`. The result is
the complete zero-moment limsup r(b), pending independent critical
audit. This draft retains the preliminary obligations as the working
record; the final proof and qualifications are in L725.
