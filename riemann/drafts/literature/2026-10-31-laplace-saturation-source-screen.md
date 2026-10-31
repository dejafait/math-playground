# Direct Laplace saturation: completed source screen

TARGET: Assess primary-source coverage for a direct Laplace-integral implementation of L482's rational saturation at actual heights, retaining L477's two phases and the L481/L482/L484 obstructions, and approve or park one explicit weighted-correlation test.
CHECKED: 2026-10-31
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Completed bounded Laplace/resolvent/nonlinear Dirichlet-polynomial and stronger joint-transform searches; inspected the primary scalar formula and actual-height Fourier-Laplace theorem below. Reused the ready bounded-saturation, weighted-cubic, sign-leakage and Euler-phase comparisons and their failure records. No matching residual-weighted theorem was found; this is not evidence of novelty or falsity.
SOURCE_EVIDENCE: DLMF 5.9.1 and its parameter conditions; Arguin--Belius--Bourgade--Radziwill--Soundararajan, author version dated 14 December 2017, equations (9)--(12), (35)--(42), Propositions 5.1/5.3 and Lemma 5.2, printed pp. 8,18--21, https://math.nyu.edu/~bourgade/papers/LocalMaxZeta.pdf ; earlier author version Proposition 3.8/(26)--(33), pp. 13--14, https://www.math.mcgill.ca/radziwill/zeta_max.pdf . Retained Heap--Soundararajan and Heap--Radziwill--Soundararajan scope is reused from the prior bounded-correlation assessment.
COMPARISON: The scalar reciprocal Laplace representation is known; the inspected actual-height transform evaluates linear prime-block exponentials on a good set with restricted complex parameters. It does not supply either full residual-weighted nonlinear transform, its weighted exceptional error, or parameter-integrable asymptotic errors for the all-integer F_T. Direct integration avoids the stipulated polynomial implementation but supplies none of those missing arithmetic estimates.
GAP: For the exact C_A and proposed K_U,K_V below, no fixed A>=0, c>0, unbounded sequence, or complete integrated signed error establishes C_A>=c T(log T)^3. Uniformity near parameter zero, the full parameter range, both phases, all endpoints and any weighted approximation remain obligations. Neither defect threshold nor negative-mass saving is established.
REASON: Park direct Laplace evaluation from the inspected sources: essential theorem scope is missing, although the primary texts are accessible. The new transform comparison completes the nominated source screen; it does not approve a dependent calculation or prove the correlation false. Nominate an independent constructive Fourier-dual source screen, with REVIEW_REQUIRED, rather than repeat this blocked source chain.
LITERATURE_REASON: Direct Laplace-parameter integration is outside the assessed polynomial and Haar implementations; its essential actual-height weighted decay and uniformity inputs have not been inspected.
SCOPE: Completed source comparison only: actual L477/L481 R_T,U_T,V_T,theta,F_T on [T,2T], fixed A>=0 and Laplace parameter u>=0. No RH, Haar replacement, phase independence, weighted exceptional-set disposal, Xi norm estimate or mathematical calculation is approved. L482/L484 are restricted implementation obstructions; L571/C571a are context only.

The original nomination and in-progress note below are preserved as history;
the top fields and completed review supersede their pending-review language.

The main gap is actual-Xi signs at unbounded heights. A signed
actual-height correlation could support the negative-mass route in
the overview, with all-height signs still a separate obligation.
The intermediate source question is whether direct integral evaluation
has an applicable quantitative input where global approximation failed.
It is not enough to quote a scalar integral representation: the hard
input is a residual-weighted estimate, with uniform errors allowing
the exact required parameter integral and both signed phases.

First retrieve the exact canonical definitions and required inequality,
then compare the primary theorem hypotheses and essential proof cases.
Check the named source assessments and recorded failures before fresh
searches; do not reopen the blocked Euler-product source chain under a
new name. Preserve L481's fourth-moment lower bound, L482's degree/length
obstruction and L484's Haar-only qualification. Neither a failed search
nor an unweighted or height-averaged analogue supplies the input.

Admission test: identify one explicit actual-height weighted-correlation
test with its exact threshold, inputs, parameter range and convergence
requirements covered, or park this implementation with the specific
source mismatch. Do not derive or approve uncovered mathematics in
that review. A genuinely new central test may then be nominated as
proof_attempt/creative with a precise bounded test and escalation;
no creative mathematical attempt is ready merely from this nomination.
No cross-notebook input. Matching Mathlib coverage remains unchecked.

## Review in progress — 31 October 2026

Canonical definitions recovered: L477 uses the fixed M=floor(sqrt(T/(2pi)))
and R_T=U+Re(exp(2i theta)V), with unweighted transfer error
O(T(log T)^(5/2)); L481 uses F_T=sum_(n<=floor(T^(1/24)))n^(-1/2-it).
The prior bounded-correlation assessment specifies the sought positive
c T(log T)^3 correlation for some fixed A>=0. This would obstruct the
selected square's little-o defect, not establish negative-mass saving.
L482's Markov/length obstruction and L484's separate Euler-phase Haar
obstruction retain their restricted scopes. No new identity or bound
has been established in this review.

New primary lead retrieved: Arguin--Belius--Bourgade--Radziwill--Soundararajan,
Maximum of the Riemann zeta function on a short interval of the critical
line, author-hosted zeta_max.pdf, Proposition 3.8/(26)--(27), printed
pp. 13--14. Its exact prime-block definitions and good/exceptional-set
proof cases still require inspection before final comparison. No
applicability to the all-integer nonlinear residual-weighted transform
is assumed. Direct exponential/resolvent searches have not yet produced
an inspected matching theorem. Review remains literature-only.

## Completed review — 31 October 2026

### Exact observable, threshold and relevance

Use the canonical definitions in L477 and L481, without changing the
cutoff or replacing actual heights by a torus. Write L=log T,
M=floor(sqrt(T/(2pi))), N=floor(T^(1/24)), and

    F_T(t)=sum_(n<=N)n^(-1/2-it), x_T(t)=|F_T(t)|^6,
    a_T=L^A, phi_(A,T)(t)=x_T(t)/(a_T+x_T(t)), A>=0 fixed,
    c_nm=log(n/m)^2/sqrt(nm),
    U_T(t)=sum_(n,m<=M)c_nm exp(it log(m/n)),
    V_T(t)=sum_(n,m<=M)c_nm exp(-it log(nm)),
    R_T(t)=U_T(t)+Re(exp(2i theta(t))V_T(t)),
    theta(t)=Im log Gamma(1/4+it/2)-t log(pi)/2.

All sums over n,m are ordered, with the zero diagonal retained. U_T
is real by symmetry. The unchanged bounded-correlation assessment
specifies the desired test

    C_A(T):=integral_T^(2T) R_T(t) phi_(A,T)(t) dt
                >= c T L^3

for some fixed A>=0, c>0 along an unbounded sequence. Neither A nor c
has been supplied by a source. Since 0<=phi<=1, such a test would
lower-bound L477's absolute residual; L477 transfers it to the square
defect with error O(T L^(5/2)). This could reject G_T=4|P_1|^2 as a
little-o approximation. It does not imply a negative-mass saving:
N(T)<=E(T) is only an upper comparison. First signs, higher signs,
and all-height RH remain independent gaps.

For precise source matching, the proposed direct-integral method would
need the full actual-height quantities, for every u>=0,

    K_U(u,T)=integral_T^(2T) U_T(t)
                         [1-exp(-u x_T(t)/a_T)] dt,
    K_V(u,T)=integral_T^(2T) exp(2i theta(t)) V_T(t)
                         [1-exp(-u x_T(t)/a_T)] dt.

It would need a lower bound at the stated scale after integration
against exp(-u)du, with the combined signed contribution and complete
errors. These are definitions and a specification of the missing
test, not transform evaluations. No inference from the large unbounded
moment integral R_T|F_T|^6 in L481 is valid without further control.
In particular, the behavior near u=0 and the rest of the parameter
integral cannot be inferred from finitely many derivatives there.

### Primary formulas and proof cases actually inspected

**Scalar formula.** [DLMF 5.9.1](https://dlmf.nist.gov/5.9.E1)
assumes mu>0, Re(nu)>0, Re(z)>0 and principal fractional powers.
Its mu=nu=1 case is the standard reciprocal Laplace integral. With
z=1+x/a>0 (a>0,x>=0), it supplies the scalar ingredient for the
proposed saturation representation. No reproof is needed. This says
nothing about arithmetic signed correlations or asymptotic errors.
[DLMF 1.14.17--19](https://dlmf.nist.gov/1.14.iii) gives the transform
and exponential-growth convergence conventions; no varying-T estimate
is contained in those definitions. A fixed-T Fubini justification and
an interchange of a uniform asymptotic with the parameter integral are
different requirements. The latter is the substantive missing input;
this review proves neither a new interchange nor a new integral identity.

**Actual-height transform.** Arguin--Belius--Bourgade--Radziwill--
Soundararajan, *Maximum of the Riemann zeta function on a short interval
of the critical line*, [author version dated 14 December 2017](https://math.nyu.edu/~bourgade/papers/LocalMaxZeta.pdf),
(9)--(12), (35)--(42), Propositions 5.1/5.3 and Lemma 5.2,
printed pp. 8,18--21. For fixed integer K>3, its blocks are

    J_j=(exp(L^(j/K)),exp(L^((j+1)/K))],
    sigma_0=1/2+L^(-1+3/(2K)),
    P_j(t)=Re sum_(p in J_j)p^(-sigma_0-it), 1<=j<=K-3,
    s_j^2=(1/2)sum_(p in J_j)p^(-2sigma_0),
    B={t in [T,2T]: |P_j(t)|<=L^(1/(4K)) for all j}.

Proposition 5.3/(37), with E=T^(-1) integral_T^(2T), states for
complex |xi_j|<=L^(1/(16K))

    E[exp(sum_j xi_j P_j(t)) 1_B]
       =exp((1/2)sum_j xi_j^2 s_j^2)
                          +O(exp(-L^(1/(4K)))).

Read the Gaussian-moment comparison, exceptional-set moment bound,
Taylor cutoff 10L^(1/(3K)), and Cauchy--Schwarz removal of the cutoff
for those moments; also inspected its two-point proof case. These are
restricted prime-block transforms, with an explicit good set and
parameter bound. They are not residual-weighted nonlinear transforms.
No extension is imported or reproved here. The earlier undated
[McGill author PDF](https://www.math.mcgill.ca/radziwill/zeta_max.pdf),
Proposition 3.8/(26)--(33), pp. 13--14, was inspected first; the dated
revision's numbering and additive error above govern this comparison.
The publication is CPAM 72 (2019), 500--535,
[DOI 10.1002/cpa.21791](https://doi.org/10.1002/cpa.21791);
no identification of the two author PDFs with the version of record
or independent full manuscript audit is asserted.

The mismatch is substantive: F_T contains all integers through a fixed
power of T, rather than these subpower prime blocks; x_T is nonlinear;
K_U and K_V include the full quadratic residual and the actual chirp.
The theorem's unweighted exceptional measure does not estimate the
required residual-weighted error. Its restricted complex parameters
and Gaussian main term do not evaluate the u integral above. Even an
unweighted transform for F_T alone would leave these signed correlations
unresolved. These are comparisons of exact hypotheses, not a proof
that no future extension exists.

### Reuse, failures and search record

Reused the ready assessments of bounded short-resonator correlation,
actual-weight cubic feasibility, sign-adapted chirped leakage and the
Euler-product phase dual. Their primary finite-polynomial and
absolute-moment coverage remains qualified exactly as recorded; no
extra search was done merely to reapprove those tools. The cubic
five-range dual is parked for absent bounded-range |R_T|-weighted
mass, not because every saturation fails. L481's fourth-moment bound,
L482's global-envelope degree/length contradiction and L484's different
real Euler-phase Haar obstruction do not establish a bound for C_A.
The sign-boundary and Euler-product source-chain stops are preserved.
No essential source-access failure occurred in this review.

Queries included `"Dirichlet polynomials" "Laplace transform"
distribution`, `"Dirichlet polynomials" "characteristic function"
joint distribution finite`, `zeta resonator bounded weight saturation
Laplace`, `"Dirichlet polynomials" "nonlinear" mean values bounded`,
`"Dirichlet polynomial" "resolvent" correlation`, and exact
Fourier-Laplace/theorem-title follow-ups. Unrelated Dirichlet-process,
majorization and differential-operator results were screened out.
Search snippets and random-model statements were not coverage.
The bounded search found no matching primary theorem; no exhaustive
search, originality claim or mathematical nonexistence result follows.

### Decision and continuation

SOURCE_BLOCKED means missing essential scope, not inaccessible text.
Park evaluation of C_A through the direct Laplace implementation.
Reopen only with a precise actual-height joint transform, or a different
method removing that obligation, including signed and parameter-integrable
errors at the required scale. Another scalar Laplace identity or another
absolute moment does not pass. No lemma, mathematical script, source
specialization estimate or RH candidate was produced. Mathlib matching
for the complete target is unchecked; absence is not asserted.

The separate next nomination asks about constructive finite-interval
Fourier duals for ratio/chirped separation, without saturation, a
resolvent, a prime-product phase, sgn(U_T), or an automatic Haar transfer.
This is REVIEW_REQUIRED, not an approved mathematical mechanism. It
must first distinguish itself from the recorded separated-linear-
frequency and sign-leakage mismatches. An independent lower bound for
integral|U_T| would still be needed after any separation inequality.
No justified creative proof attempt is ready from the present sources.
