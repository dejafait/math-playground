# Compact-width analytic specialization: working1529

18 November 2026. In progress under the unchanged prior SPECIALIZE
assessment1528. Target only: joint continuity and locally uniform entire
lifts for widths in [1,2], then finite-total-variation width integration.
Main gap is actual-Xi all-degree positivity; this auxiliary construction
could make a later signed odd-transform test well posed.

Local inputs read: C032j, complete C032k including audit1302, C032l and
audit1340 as finite-family contrasts; source ledger1528 and review1301.
The previous finite stop remains. No probability-kernel or continuum
independence claim is covered. No source-wide preprint verification.

Candidate bound, still to check: the Gaussian modulus on a fixed complex
disk is bounded uniformly in sigma by a summable Gaussian in ordinates.
On the real axis retain the common absolute Gaussian envelope Q(x)
rather than infer uniform logarithmic constants from individual bounds.
For x >= X = 2M+1, control the removable integrand by
4[Q(x)+A_M]/(3x^2). Prove Q(x)/x^2 integrable by splitting each translated
Gaussian at x=gamma/2 and summing a Gaussian tail plus gamma^(-2), using
N(T)=O(T log(T+2)). The compact part will use the even entire lift h_sigma
and a common Cauchy bound for h_sigma'. Both removable points and (0,0)
must be included. Derive bounded primitives and apply Haslinger2.39 to
the signed integrals via d eta = theta d|eta|, |theta|<=1.

Continue only if every stated majorant is finite and independent of width,
including widths 1 and 2. Otherwise preserve the failed bound. No
calculation outside this approved analytic target is authorized here.

## Completed bound check

Set c_Y=exp((Y+1/2)^2/4)/sqrt(4*pi) and
A_M=c_M sum_rho exp(-(gamma_rho-M)_+^2/8). Uniform Gaussian
modulus gives |p_sigma(z)|<=A_M on |z|<=M. The common real envelope
is Q(x)=(c_0/2) sum_rho [exp(-(x-gamma)^2/8)+exp(-(x+gamma)^2/8)].
For X>=1, termwise integration with nonnegative summands gives
integral_X^infinity Q(x)/x^2 dx <=
c_0[S_G/X+2*sqrt(8*pi)*S_2], where S_G=sum exp(-gamma^2/32)
and S_2=sum gamma^(-2) are finite by the retained counting input.
The two portions x<gamma/2 and x>=gamma/2 establish this bound.

For X=2M+1, the compact divided difference is bounded by
A_sqrt(X^2+1), using h_sigma(u)=p_sigma(sqrt(u)) and Cauchy's
radius-one estimate on h_sigma'. Hence the proposed D_M is integrable
and uniform, including all removable points. This passes the analytic
test; the full proof, constants and signed-measure application are being
saved in C032m. No cancellation or measure-kernel conclusion follows.

Finalization: the full proof is now canonical in
`lemmas/C032m-compact-width-uniform-entire-lifts.md`. This working file
preserves the initial plan and bound check, not a second proof. The
independent conceptual audit is nominated, not completed.
