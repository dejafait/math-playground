# Sharp quartet response — working checkpoint, step248

The pre-existing SPECIALIZE assessment review246, approved in step247,
authorizes exactly the fixed synthetic quartet calculation. No actual
zero, prime estimate or full zero-sum exchange is assumed.

Main gap: actual-Xi positivity and signed arithmetic cancellation.
Target: positive exponential upper excursions of W_n for tau=10^13.
Use: test whether one spectral mode can be automatically paid by the
moving-block kernel. Continue only with a smaller remainder and an
integer positive subsequence; zero rate/cancellation stops this test.

Unfinished calculation, not yet a result: L985's finite identity and
source bulk formula suggest K_n=e^(u/2)*A_n(u)*cos(Phi_n(u))
-1/(n-1)+O(e^(u/2)*n^(-5/2)), uniformly on [n,2n]. Here
A_n=sqrt(2/(pi*(4n+2)))/((n-1)*D(u/(4n+2))) and D(t)=
4*t^(5/4)*(1-t)^(1/4). For q with real part3/4, retain the
upper and lower endpoint terms with denominators
1/4+i*(tau+-Phi_n'). Bound the differentiated explicit amplitude
only; integrate the unknown additive remainder in absolute value.
The real-part1/4 pair is exponentially smaller but must be retained.

At2n, the prospective phase is
Phi_n(2n)=n*(1+pi/2)-pi+O(1/n), derivative1/2+O(1/n),
and A_n(2n)=n^(-3/2)/(2*sqrt(pi))+O(n^(-5/2)). Hence the
candidate leading factor is Re(c_+*exp(i*n*alpha_+)+
c_-*exp(i*n*alpha_-)), with alpha_+=2*tau+1+pi/2,
alpha_-=2*tau-1-pi/2, c_+=1/(1/4+i*(tau+1/2)),
c_-=1/(1/4+i*(tau-1/2)). All zero/paired frequency tests may
follow from irrationality of pi, without full-torus independence.
Still owed: verify prefactor, error integral, both endpoints, -1
term, all frequency coincidences, and the positive-subsequence bound.

Inputs: L985 finite connection and bulk formulas (to be justified from
their cited DLMF contracts); L981/L982 normalization and L986 are
context only. Preserve all existing arithmetic route stops. This
checkpoint makes no new-source claim and is not a complete solution.

Completed later in this same step: the proposed endpoint formula and
sign test are proved in [L987](../lemmas/L987-fixed-quartet-sharp-block-positive-excursions.md).
The complete finite integration error, retained endpoints and quartet,
and positive integer subsequence give exact limsup rate1/2. The
working notes above preserve the unfinished reasoning at its save
point; the canonical lemma supersedes their provisional status.
No actual-prime transfer was obtained. A separate critical audit of
the same target is the continuation, using the unchanged ready source
assessment; no new target or additional source approval is nominated.
