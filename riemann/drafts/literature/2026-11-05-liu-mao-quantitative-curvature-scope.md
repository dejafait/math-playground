# Actual-coefficient quantitative curvature — completed scope review

TARGET: Review Liu–Mao 2610.04972v1 Proposition3.5 for an explicit actual-coefficient curvature estimate stronger than bare all-iterate positivity, and compare its stated scope with L772 before nominating a theta-specific minor mechanism.
CHECKED: 2026-11-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused step407 and L772/step410; narrowly searched coefficient/curvature assessments and coefficient failures, then queried the exact identifier with Proposition3.3/curvature/Toeplitz and xi Taylor-coefficient logarithmic-ratio terms. Search results supplied no inspected minor-transfer theorem; no novelty inference.
SOURCE_EVIDENCE: Verified Liu–Mao arXiv:2610.04972v1, submitted 4 October2026, in abstract/HTML/PDF; read Proposition3.5 statement and complete assembly pp.41–42, Lemma3.3 statement and its branch/four-error-term proof pp.31–37, Lemma3.4 statement and essential disk/branch/Cauchy cases pp.37–40, Lemma2.3 definitions and Lemma3.1 statement/proof; Lemma3.2 statement and final assembly only, not its full saddle proof.
COMPARISON: Proposition3.5 gives a finite-iteration positivity range and terminal ratio >e; the additional actual-coefficient premise is Lemma3.3's uniform complex curvature approximation with error <=20/n^2, n>=12000. L772 addresses neither that approximation nor its analytic interpolation. No minor-sign implication is supplied by the inspected statements.
GAP: The complex curvature estimate remains unaudited through its saddle input; its implication for exceptional minors k=r-1, all orders and bounded indices is unproved. A bounded conditional audit of Lemma3.3 can isolate the finite-difference interface without asserting the saddle estimate or RH.
REASON: The review identifies a precise quantitative premise beyond bare positivity, changing the source nomination into a testable analytic interface. This is source-scope evidence only, not an imported Xi estimate or new mathematics.
SCOPE: Completed source review for the saved TARGET only. No theorem-level endorsement, Proposition4.5 audit, new lemma, numerical scan or mathematical script. The separately nominated conditional audit requires separate approval.

## Original nomination retained (step652)

The primary lead is Yanxin Liu and Jianxi Mao,
[*Infinite log-concavity of the Taylor coefficients of the Riemann
xi-function*, arXiv:2610.04972v1](https://arxiv.org/html/2610.04972v1),
as recorded in step407. Verify source identity and exact version before
using any statement; a rendering mismatch or inaccessible premise is
not evidence that the estimate holds. Preserve the original theorem
number if HTML and PDF differ. This file is a nomination, not a finding
that an adequate quantitative estimate exists.

The main gap is actual-Xi all-degree mixed positivity. A genuinely
stronger quantitative curvature premise could help discriminate an
actual-theta mechanism that L772 does not address. Other determinant
orders, sign margins and realization obligations would still remain.
Do not infer a sign from the existence of a bound. Account for the
coefficient normalization recorded in step407 before any comparison.

Continue only if the inspected source yields an explicit additional
quantity or bound with a concrete independent check and plausible
downstream use. If it supplies only positivity, an assumed real-zero
premise or an inaccessible quantitative obligation, record that scope
and park the transfer. Do not automatically expand this into an audit
of Proposition4.5 or the entire theorem. If a usable new mechanism
emerges, prepare its exact bounded target for separate approval;
do not derive and approve it during the review.

Retain L772's generic stop, L773's finite-grid exclusion, step407's
condensation/multiplier restrictions and the existing actual-Xi sign
gaps. Neither L766 nor the preprint's claimed theorem is an imported
premise. Full matching Mathlib coverage is unknown. No new mathematics
or mathematical script was produced in preparing this continuation.


## Completed source review — 5 November 2026, step653

The main gap remains actual-Xi all-degree mixed positivity. This turn
reviewed the saved Proposition3.5 target only; it did not prove a
coefficient estimate or approve an uninspected transfer. The useful
intermediate object is a quantitative analytic curvature estimate.
Its plausible use is to control variation of neighboring actual
coefficients before attempting a determinant comparison. Whether it
provides adequate precision at growing order remains open.

### Exact primary statements and conventions

Yanxin Liu and Jianxi Mao, *Infinite log-concavity of the Taylor
coefficients of the Riemann xi-function*,
[arXiv:2610.04972v1](https://arxiv.org/pdf/2610.04972v1),
4 October2026, 60 pages. HTML and PDF agree on the relevant theorem
numbers; page numbers here are printed PDF pages.
Equation(1.1) uses lambda_n=xi^(2n)(1/2)/(2n)!, not gamma_n=n!lambda_n.
Retain step407's normalization a_n=lambda_n/(8*4^n). No new
normalization or sign-transfer derivation is made in this review.

Proposition3.5, pp.41–42: for each integer n>=12000 and
M=ceil(log_2 n), A_(m,n)=(L^m lambda)_n>0 for 0<=m<=M.
The denominator of r_(M,n)=A_(M,n)^2/(A_(M,n-1)A_(M,n+1))
is positive, and r_(M,n)>e>(3+sqrt(5))/2. The complete printed
assembly uses Lemmas2.2/2.3/3.3/3.4 and gives g_M(n)>=9/8>1.
This is not a statement for every iteration or for n<12000.
Theorem1.1's all-index conclusion also invokes Proposition4.5;
that finite certificate remains unread and unaudited here.

Equations(2.10), (3.52) and Lemma3.3, pp.31–37, specify:

- H(z)=2^(1-2z) integral_0^infinity u^(2z)e^(u/4)omega(e^u) du,
  Lambda(z)=H(z)/Gamma(2z+1), Re z>-1/2;
  omega(t)=sum_(j>=1)(2pi^2 j^4 t^2-3pi j^2 t)e^(-pi j^2 t).
- Delta^2 f(z)=f(z-1)-2f(z)+f(z+1),
  g_0(z)=-Delta^2 Log Lambda(z),
  w=W_0(2z/pi), Q(z)=2w/[z(1+w)].
- For real n>=12000, D_0={|z-n|<=n/2}, g_0 is holomorphic
  on a neighborhood of D_0 and real on [n/2,3n/2]; at every
  integer k in D_0 it equals log(lambda_k^2/(lambda_(k-1)lambda_(k+1))).
- On the entire closed disk, |g_0-Q|<=20/n^2,
  Re(n g_0)>5/8, |n g_0|<9/2; at the center n g_0(n)>5/4.

Lemma3.4, pp.37–41, is a conditional analytic recurrence statement
for real n>=6000, with M=ceil(log_2 n),
D_m={|z-n|<2^(-m/3-1)n}. Its initial assumptions are holomorphy,
reality, Re(n g_0)>=5/8 and |n g_0|<=9/2 on D_0, and
n g_0(n)>=5/4. The recurrence uses h(z)=Log(1-e^(-z)).
It states holomorphy, positive real part, reality on each real
section, and |2^(-m)g_m-g_0|<=S_m<1500/n^2 on D_m, 0<=m<=M.
Here S_0=0 and S_m=sum_(ell=0)^(m-1)3*2^(-ell)/delta_ell^2,
delta_ell=2^(-ell/3-1)(1-2^(-1/3))n. The inspected proof cases
include delta_m>20, a right-half-plane logarithm for the normalized
1-e^(-g_m), and Cauchy's second-derivative estimate on disks of
radius delta_m-1. No independent validation of that induction is
claimed. The initial curvature estimate is the useful new source
lead; the terminal closure ratio is not itself a minor criterion.

### Essential source proof cases and remaining obligations

Lemma3.3 uses the open disk |z-n|<2n/3. Its logarithms agree
with real logarithms on the positive real interval, including
shifted arguments; it does not assume a zero-free disk for F.
The underlying source claim, Lemma3.2, is instead about H(z)
in |arg z|<=pi/4, |z|>=4000. With w=W_0(2z/pi), a=Re w,
T=|z|/a and
H_*(z)=4pi^2 exp(7w/4) sqrt(2w/(1+w))
 exp(2z(Log(w/2)-1/w)), it states |H/H_*-1|<=30/T and
|Log(H/H_*)|<=32/T<0.051. Its final assembly and the statement
were read; its long H_1 saddle and H_2 tail proofs were not audited.
Lemma3.1's sector bound a>=6 and T>630 was also inspected.
These facts must remain explicit assumptions of a conditional audit.

The four cases in Lemma3.3's printed proof are (3.62)–(3.68):
write Log H=p+h_0+epsilon with
p=2z(Log(w/2)-1/w),
h_0=log(4pi^2)+7w/4+(1/2)Log(2w/(1+w)),
epsilon=Log(H/H_*). The source bounds
|Delta^2 p-p''|<1/n^2, |Delta^2 h_0|<8/n^2,
|Delta^2 epsilon|<5/n^2, and
|Delta^2 Log Gamma(2z+1)-2/z|<4/n^2.
The printed sum is <18/n^2<20/n^2. Its remainder case uses
Cauchy on radius n/7 around every |z_0-n|<=n/2+1, not
pointwise control on the real axis. The Gamma case uses its exact
functional equation and convergent logarithmic series, with branches
fixed first. These are source statements recorded for checking;
this literature turn does not rederive or certify them.

### Comparison and bounded continuation

L772/step410 remains a valid larger-class obstruction. Its positive
entire sequence and global strong ratio condition are not a
realization of the actual Lambda or a verification of the above
complex-disk approximation. Conversely, Proposition3.5 does not
state total positivity, an exceptional-minor sign, or a comparison
at all degrees. Its n>=12000 range cannot simply be substituted
for k=r-1 in every order. Small orders and the remaining independent
sign/realization gaps survive.

The overlap check also inspected the statements and scope of L790
and its source assessment: those reproduce an all-degree derivative
bound for log of the actual moment quotient at k>=10^9. The new
lead concerns finite differences on a much larger complex disk,
a different explicit range, and a Lambert-W main term. This does
not establish an improvement on the existing wedge or a new result
beyond either source. No matching completed local audit was found
in the narrow paths searched; this is not exhaustive novelty evidence.

Continue only with the bounded conditional Lemma3.3 audit nominated
in the separate assessment. Accept it as an interface only if every
branch, disk inclusion and all four uniform error bounds follow
from the stated sector inputs, without a hidden RH premise. Otherwise
record the exact failed inequality and park that interface. Even a
successful conditional audit leaves the saddle input and any
minor-sign implication unproved. No creative target is justified
yet by this source-scope step: an independently certified actual-theta
premise and a quantified determinant error budget are still missing.
Full matching Mathlib coverage has not been checked. No lemmas,
mathematical scripts, DAG or PROOF argument were changed.
