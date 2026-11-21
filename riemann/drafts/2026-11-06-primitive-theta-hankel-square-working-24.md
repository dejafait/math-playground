# Primitive-theta Hankel-square coefficient test — working step24

The supplied SPECIALIZE assessment approves exactly the unshifted
H_K on Lebesgue L2(0,infinity), A=H_K^*H_K, c=S_1/Tr(A).
No operator alteration or higher-coefficient extension is authorized.
Main gap: L030-L032/C032a. Local input proofs L016/L019/L021/L024/L025
were read; the completed step22 duplicate/failure comparison is reused.

Proposed bounded calculation: prove the second residual positive using
a fixed unit trial function for H_K, an upper bound on Tr(A), and
S_2/S_1^2 <= 2/3 from L021/L025. For f=1_[0,b]/sqrt(b), write
J=<f,H_K f>=b^(-1) integral_0^(2b) w_b(u)K(u)du, where
w_b(u)=min(u,2b-u). Then Tr(A^2)>=||H_K f||^4>=J^4.
The first inequality still needs its precise operator justification in
the final proof. A lower bound J^4/Tr(A)^2>2/3 would reject the ansatz.
The trial function is a bound on the fixed operator, not a fitted weight
or change to the determinant. Parameters and actual bounds are pending.

For rigorous interval integration, put q(v)=(8v^2-12v)exp(-v).
For v>=pi>3, q'(v)=-4(2v-1)(v-3)exp(-v)<0. Thus on [a,b],
each positive summand is between exp(a/2)q(pi*n^2*exp(2b)) and
exp(b/2)q(pi*n^2*exp(2a)). Need rigorous pi/exp arithmetic, explicit
omitted-n bound, all-half-line Tr(A) tail and M_0,M_2 bounds if used
to enclose the unnormalized residual. No numerical result yet.

Stop at a certified nonzero residual. If this coarse separator fails,
do not infer compatibility; save the inconclusive evidence. Even a
proven finite match would leave higher traces and Xi identification open.

The saved explicitly NONRIGOROUS diagnostic shows the universal 2/3
bound is too coarse for the proposed constant trial. Do not claim that
separator. Instead enclose M_0,M_2,M_4 directly to bound S_2 via L025;
the estimated normalized S_2 is much smaller. This is the same fixed
coefficient test, without any operator modification. Fix b=3/10 and
use positive cell bounds with mesh 1/2000 on [0,2]. Numerical estimates
are feasibility evidence only; rigorous enclosures are still pending.

Completed: L876 and scripts/primitive-hankel/coefficient-test-24.json
provide the full rigorous proof/certificate. The residual is strictly
between 0.00021317 and 0.00050451, so this fixed determinant fails at z^4.
The preliminary diagnostic was preserved under
scripts/primitive-hankel/diagnostic-24.json. This working note retains
the actual reasoning chronology; its earlier pending statements are
superseded by the canonical lemma, not additional open obligations.
