# Neutral cutoff attempt606 — saved reasoning

Approved target: the exact target of assessment604, reused unchanged.
Main gap: L030-L032/C032a actual-Xi positivity. This step only attempts
an explicit infinite-complement norm remainder for C744z(4).

Inputs read: C744z Sections1-3 and its actual U bound; C744v Sections3-4
and audit534; C744w Section2/(8); C999k Sections1-2. Assessment604's
source comparison and stops537/598/600/603 have been checked. No new
source coverage or external mathematics is needed for this specialization.

Candidate derivation, still being checked:
- Let b=max(0,max_{0<=n<512}[-h(n*pi/ell)]), a completely specified finite
  special-function constant. All remaining diagonal entries are positive
  by C744v(5). Put d_N=log(N/(2ell))-2ell^2/(9N^2).
- Positivity of S and a0(Eu,Eu)=||u||^2 give the raw tail bound
  ||Q_N Eu||^2 <= (1+b/c_*)/(d_N+b) ||u||^2.
- Correct the two moments exactly in modes0,1 using C999k's parity
  ratios. Their tail ratios are at most a/n^2 with
  a=1+ell^2/(4pi^2); orthogonality gives correction factor
  eta_N=sqrt(1+a^2/[3(N-1)^3]). Hilbert best approximation then gives
  ||(I-P_N)E||<=delta_N=min(c_*^-1/2,
  eta_N sqrt((1+b/c_*)/(d_N+b))). No commutation is assumed.
- With M=c_*^-1/2, k=4.71, u=29.813203120 and ||R||<=1,
  the proposed full block bound is epsilon_N=2 M delta_N (u+2k).
  Account explicitly for R*R, RR*, V14 and R^2, their two-sided
  projection losses, and the mixed endpoint/complement blocks.

Continuation test: all these bounds must hold on the full neutral form
domain for arbitrary complex endpoints and tend to zero without S3
positivity. Preserve c_*/core/analytic/arithmetic qualifications. A later
normalized finite margin and finite entry enclosure remain absent.

Even success will give very poor constants: the displayed epsilon_N is
larger than6e6 for every512<=N<=exp(10^6), using c_*<1e-16, d_N<10^6,
and b>=0. This is a limitation of this bound, not a lower bound on the
actual truncation error. No numerical experiment or sign claim is made.

Completed606: the canonical proof is now
[C999r](../lemmas/C999r-explicit-neutral-cutoff-norm-bound.md). Its
conditional norm bound closes this target, with ineffective constants;
the draft above is a preserved working record, not independent evidence.
The size comparison is proved there by a convex combination of1/d_N
and1/c_*, avoiding any need to evaluate b. Separate audit remains pending.
