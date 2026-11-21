# Fixed defect-window norm test705: work in progress

Approved target: assessment704, supplied at invocation; SPECIALIZE.
Main gap: L030-L032/C032a actual-Xi positivity and full signed S3.
Test only unchanged C744y full two-cell evidence in actual C744z
energy coordinates, against ||R||^2<3/4. No parameter tuning.

Read C744y Sections1-5, C744v response/complement and C744z Sections1-3;
reuse source coverage704/615/617/699/700. Existing source/core,
IEEE754/Decimal and unreplayed c_* qualifications remain. C744y gives
B=[[A,-T*],[-T,A]], A=D+S+256 C*C, Q B Q>=tau I,
tau=1.43, and M-F*F/tau>=delta I, delta=.027998.
Finite factor norm sum<3.162, entry error eF=eQ+3sqrt(65024*512)*1e-7,
eQ<.000000181; full high covariance<=U, ||U||=.051208.
Pending exact scalar calculation: bound ||F||, then use square
completion to get B>=m I on the whole form domain. The sufficient
scalar condition is delta-m-m||F||^2/[tau(tau-m)]>=0, 0<m<tau.
Since diag(A,A)=B+[[0,T*],[T,0]]<=B+4.71 I, such a floor would
give B>=(m/(m+4.71))diag(A,A). Restrict to exactly neutral pairs,
then use C744z actual E=A0^-1/2 to obtain ||R||<=4.71/(m+4.71).
No conclusion is claimed before checking this conversion and numbers.
Do not mistake failure of this upper bound to cross3/4 for proof of
nonempty actual windows. Stop at the insufficient comparison.

Completed705: canonical C744z Section10 contains the full proof and
qualifications. Exact extraction gives ||F||^2<10.061, a full two-cell
L2 floor .004716385, and ||R||^2<=
887364000000000000/889142023639498729<.998001. The required bound
is3/4. Even the optimal root of this scalar comparison misses it;
this is not a lower bound on actual ||R||. Stop scalarized extraction,
without a claim that every use of the directional certificate fails.
The early pending note used a triangle-bound description; the completed
proof uses orthogonality of finite/high output ranges to bound F^2.

All17 new exact checks pass, all seven inherited artifact hashes match,
and the full selected exact extraction/check arrays were inspected in
scripts/separation-seven/defect-window-norm-705.json. No upstream replay
or new source search was needed. Threshold miss is recorded separately
from the empty arithmetic-failures list. No actual window sign,
projector approximation or S3 sign is established. This is a local
standard-method specialization, not claimed new mathematics beyond
the assessed sources. New bound remains independently unaudited.

The independent continuation is a lower variational trial-pair test
against the same3/4 threshold; its finite exactly neutral interface
and source overlap are not yet assessed. Review required before
that calculation. No second mathematical attempt was made705.
