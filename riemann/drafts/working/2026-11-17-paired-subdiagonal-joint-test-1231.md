# Paired subdiagonal joint test1231

17 November 2026. One RESEARCH / proof_attempt / development step under
the unchanged ready EXPLORE assessment1228 (review1229). The supplied
startup snapshot satisfies the startup reads. No fresh source approval,
cross-notebook input, or independent audit of C030s is undertaken.

Main gap: L030-L032/C032a actual-Xi positivity in every degree. The
approved intermediate target is the full absolute subdiagonal comparison
in assessment1228. Its plausible use is finite-basis evolution together
with C030q's diagonal estimate, conditional on still-unpaid reference
evolution, degree/time, Xi supply, complement, theta signing and realization.
Continue on a dimension- and contrast-independent constant at scale x*M;
an admissible M>0 sequence with unbounded normalized difference refutes
the target. A diagnostic or a loose upper bound cannot refute it.

Coverage reused: the supplied assessment1228; C030r's determinant and beta
interface; C030o's precise degree-two Haar contraction; C030q's physical
first-response bound; and the new partial proof C030s. Scoped duplicate
search in the paired working/assessment files and reads of
stops1117/1181/1193/1200/1107 supply no completed full comparison and no
counterexample in this family. These scoped stops remain preserved.

## Initial reasoning checkpoint

For F_k=Z_(k,b)/Z_(k,0), C030r gives the exact ratio
beta_b/beta_0=sqrt(F_(i+1)*F_(i-1))/F_i. C030s pays large active
multiplicities but its separate maximal-beta and compression-variance
bounds lose dimension at size-two classes. The next bounded calculation
retains the rank dependence of these ratios, seeking a joint estimate
or a rigorous degeneration that tests this apparent loss. No second
derivative is inferred from C030q's first-derivative estimate. No complex
variance, reference-beta lower bound, independent blocks or shared rank
normalizer is assumed. At this checkpoint there is no new result.

## Completed bounded calculation

The attempted joint proof did not yield an inequality. The completed
task is RESEARCH / calculation / REPRODUCTION, with outcome EXPLORATION.
The finite-determinant diagnostic below probes the sparse-class loss;
it is not an advance beyond the cited determinant mathematics or a
rigorous negative result. No lemma, source assessment, DAG row or
PROOF.md argument was changed. C030s remains unaudited.

Take m=1, x=1, b=1/4, a=1+max(delta,0) and
r=1+max(-delta,0). Thus a-r=delta, both rates are positive,
M=1/16, and x*A=1/4 is exactly the allowed closed boundary. There is
one active size-two class when delta!=0. The diagnostic uses
n=8,16,32,64; delta=0 and both signs of n/4,n,4n,n^2; and the distinct
ranks in {1,2,n/4,n/2-1}, always with d=n/2 and 1<=i<d.
This is 135 parameter/rank points, not an asymptotic sequence proof.
The n=2m boundary and several distinct active real-rate classes are not
sampled. The universal target still includes both.

### Exact formula implemented, and numerical qualifications

The canonical mathematical input is C030r(2),(7), with its cited Sra
author-v3 C.6/(C.10), pp23-25, and actual derivative-Hankel interface.
No new orbital-density or special-function theorem is used. The
following partial fractions implement this known finite convolution.
They are calculation details, not a newly asserted comparison theorem.

Write N=n-2 and f_b(x)=R_b*exp(-r*x)*h_b(x). Directly taking the
Laplace transform of each exponential convolution gives

    H_b(s)=1/[s^N*((s+delta)^2+b^2)].

This identity can equally be checked by convolving the elementary
inverse transforms; absolute convergence holds to the right of all
poles. For delta!=0 and b=0, or for b!=0, let A_k be the Taylor
coefficients at s=0 of 1/((s+delta)^2+b^2). Multiplication by its
denominator gives

    (delta^2+b^2) A_k
       =1_{k=0}-2*delta*A_(k-1)-A_(k-2),

where negative-index coefficients are zero. The polynomial part of
h_b is sum_(j=1)^N A_(N-j)*x^(j-1)/(j-1)!. When b!=0 and delta!=0,
the pole p=-delta+i*b has residue 1/(2*i*b*p^N); its conjugate pole
has the conjugate residue. Thus the v-th derivative of the remaining
part at x=1 is

    2*Re[exp(p)*p^(v-N)/(2*i*b)].

For b=0, delta!=0, the pole p=-delta is double, with coefficients
U=p^(-N) and V=-N*p^(-N-1). Its inverse transform is
(U*x+V)*exp(p*x), whose v-th derivative at x=1 is

    exp(p)*[p^v*(U+V)+v*p^(v-1)*U],

with the last summand absent at v=0. These principal parts give the
whole rational function: their subtraction has no finite pole and
vanishes at infinity. At delta=0 the directly convergent entire series
is h_b(x)=sum_(k>=0)(-b^2)^k*x^(n+2k-1)/(n+2k-1)!;
only derivatives v<=n-2 are needed, so all displayed factorials are
nonnegative. The b=0 case reduces to the first term.

Removing R_b and exp(-r*x) leaves beta unchanged. Indeed the Leibniz
rule transforms the derivative Hankel matrix by triangular binomial
matrices on both sides with diagonal 1, and multiplies each entry by
R_b*exp(-r*x); its size-k determinant gains exactly
R_b^k*exp(-r*k*x). Those factors cancel in the beta ratio. Multiplying
h_b by the positive constant (n-1)! likewise cancels. The script forms
these scaled moments and eliminates their Hankel matrix without row
swaps. If p_j is its j-th pivot (indices start at 0), the leading
determinant ratios give beta_i^2=-p_i/p_(i-1). The sign is precisely
C030r's alternating signed norms. Every computed pivot was checked
against that sign; a failure would have been recorded, not bypassed.

The first invocation failed because system Python has no mpmath. The
script was changed to use standard-library Decimal; no dependency was
installed. This setup failure is retained in the JSON. Complex powers
use explicit pairs of Decimal numbers; exp and sqrt use Decimal;
sin(1/4) and cos(1/4) use convergent Taylor sums. Two complete runs used
precision 420+floor(|delta|/2)+4*n and then 520+floor(|delta|/2)+4*n
decimal digits, paying for cancellation in slow-pair cases. The extra
rank i=2 explicitly tests small real-reference beta. Repeated precision
and stopping when a rounded series sum is unchanged are diagnostics,
not rigorous interval or truncation certificates.

### Evidence and remaining gap

Reproduce from this notebook with
`python3 scripts/paired-subdiagonal/sparse_pair_1231.py`.
Full results: `scripts/paired-subdiagonal/sparse-pair-1231.json`.
Its `kind` explicitly says FINITE_PRECISION_DIAGNOSTIC_NOT_PROOF.
All 135 points completed without a signed-pivot or precision-check
failure. The two runs agree in their stored 90-significant-digit
normalized differences. For delta=0 the known real-reference value
sqrt(i*(n-i)) agrees to relative error below 1.34e-90 in the stored
numbers, compared with a diagnostic tolerance of 1e-60.

The largest sampled |beta_b-beta_0|/(x*M) is approximately
0.165312269987263, at n=64,i=1,delta=-4096. The respective maxima for
n=8,16,32,64 are approximately 0.151942,0.158584,0.162902,0.165312.
At n=64,delta=-4096, i=2 gives beta_0 approximately 1.98535e-816
and normalized difference 1.60393e-817; i=31 gives beta_0 approximately
30.95055 and normalized difference 9.04573e-10. These are sampled
values, not certified inequalities, lower bounds, limits or evidence
that all n are bounded. They illustrate why a beta_0 lower bound is
unavailable and why its separate ambient-size bound may be too coarse.
Full per-dimension maxima and the two last cases were inspected using
the shared JSON inspector, not inferred from a truncated preview.

The exact missing joint estimate can be stated without inventing a
second-derivative consequence of C030q. In C030s's notation put

    H_k=sum_E [M_E/(g_E^2-1)]
           *E_(k,0,x)[tr(C_E^2)-tr(C_E)^2/g_E].

C030s's already written Haar contraction and cosine step give
0<=1-F_k<=x^2*H_k. To finish by that method one would need to control
x*beta_(i,0)*max_(k=i-1,i,i+1) H_k by an absolute multiple of M;
the available separate estimates only give the multiplicity loss.
No such joint inequality or violating family has been proved here.
Nor does the diagnostic bound any exact H_k. Adjacent-rank cancellation
could still allow the full target even if this sufficient estimate
fails. This is an unpaid proof direction inside the unchanged target,
not a separately approved lemma or a theorem imported from a source.

Retain the ready full target for an analytical attempt at joint control;
do not repeat this finite grid as a purported verification. It remains
eligible after this one EXPLORATION, following the partial ADVANCE1230.
No source-covered new central actual-Xi mechanism was prepared, so a
creative nomination would currently lack its essential source and
signed-input specification. The next route stays development. All
transfer stops and independent main-gap obligations remain unchanged.
