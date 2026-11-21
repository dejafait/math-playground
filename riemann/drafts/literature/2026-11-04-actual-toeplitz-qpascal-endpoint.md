# Actual coefficient q-Pascal comparison — endpoint discriminator

TARGET: Test whether Michałowski's unchanged q-Pascal norm criterion can hold for the actual coefficients along k=1024r by determining the endpoint log-defect asymptotic and its implication for the full error norm.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step385's three-mechanism discovery searched exact source IDs, q-Pascal, coefficient Toeplitz/quadratic perturbation, Appell and related local failures. No inspected result determines the selected actual endpoint defect or proves the norm criterion along this fixed-ratio ray; no novelty claim.
SOURCE_EVIDENCE: Michałowski arXiv:2607.16795v1, (1)–(3), Lemma4.1/proof, (6), Lemma6.1/proof and Section6 full assembly; O'Sullivan arXiv:2007.13582v2, (1.2), Theorem1.4/(1.8), Section7/(7.3)–(7.14), explicit c_2 following (7.14). Detailed applicability and unimported source parts below.
COMPARISON: The exact matrix identity and norm<1 inertia criterion are known; the published positivity wedge requires k>=10^18 r^3. The proposed specialization asks only about the unchanged comparison at k=1024r. Known actual coefficient asymptotics permit a finite-value analysis with sufficiently small remainder, without new analytic continuation or assumed root signs.
GAP: Determine the actual endpoint log defect with all factorials retained, establish eventual 0<q<1, and decide whether a rigorously identified error entry already violates norm<1. No asymptotic value, sign or failure is established by this assessment.
REASON: Test a distinct actual-coefficient comparison before proposing a stronger signed minor argument. This is conventional asymptotic specialization of a known sufficient method, not an approved creative positivity mechanism. Newly ready coverage receives separate continuation approval.
SCOPE: Integer r>=2, k=1024r, actual a_j defined below; the fixed source model, normalization and full error matrix only. One endpoint asymptotic and its norm consequence; no redesigned model, higher hierarchy, assumed minors, extensive degree scan or full manuscript/certificate audit.

## Exact object and source hypotheses

Use L018/L019/L021 for actual xi, K and M_(2j); L763 fixes the
gamma normalization used in the preceding discovery. Define

    a_j = M_(2j)/(8*4^j*(2j)!) = gamma_j/(8*4^j*j!),
    f(j)=log(a_j),
    rho=a_(k+1)/a_k,
    q=a_(k-1)*a_(k+1)/a_k^2,  tau=-log(q),
    h_s=f(k+s)-f(k)-s*(f(k+1)-f(k))+tau*s*(s-1)/2.

These are the coefficient normalization and equation(6) of
[Michałowski v1](https://arxiv.org/html/2607.16795v1).
His G(z)=Theta(z/4)/8 fixes the factor8 and geometric scaling; the
factor j! separating gamma_j from ordinary coefficients is essential.
L021 supplies strictly positive a_j. All indices used below are positive.
No reality of zeros, minor signs or continuous-kernel PF premise is used.

For indices 0<=i,j<=r-1, set s=r-1-i-j and use the source matrices

    V_ij=q^(i*j),
    L_ij=[i choose j]_q (i>=j),  L_ij=0 (i<j),
    D_m=product_(h=0)^(m-1)(q^m-q^h),  D_0=1,
    F=|D|^(-1/2)*L^(-1)*(V entrywise*(exp(h_s)-1))
                           *L^(-T)*|D|^(-1/2).

Here |D| is the diagonal matrix of |D_m|. Lemma4.1 assumes 0<q<1
and gives V=L D L^T with alternating pivot signs. Lemma6.1 assumes
a real symmetric M=S J S^T with S invertible, J a signature matrix,
and symmetric perturbation E. The sufficient condition is
||S^(-1) E S^(-T)||_2<1. Its proof uses nonsingularity throughout
J+theta F, 0<=theta<=1, and Sylvester inertia. Section6 identifies
that error with the displayed F and tracks reversal and determinant
signs. These finite identities are the imported interface, not an
assertion that the criterion holds for the actual coefficients.
Check the positive diagonal normalization directly if using the full
assembly: its prose placement of rho^(-i) must be reconciled with its
displayed factorization. No unverified normalization is a premise.

The definition of F and Lemma6.1 do not require the source's cubic
wedge or weighted-algebra majorant. No GateA constant, certificate or
derivative bound is needed for the proposed endpoint test. Establish
eventual 0<q<1 from the actual coefficient asymptotic before using
|D|^(-1/2); otherwise record precisely that failed hypothesis.

## Available actual coefficient input and required difference

[O'Sullivan v2](https://arxiv.org/html/2007.13582v2), Theorem1.4,
applies to exactly gamma(n)=n!xi^(2n)(1/2)/(2n)! as n tends through
positive integers, w=W(2n/pi). It gives an explicit positive leading
term times

    1 + sum_(j=1)^(K-1)c_j(w)/n^j + O_K(log(n)^K/n^K)

for each fixed integer K, with rational c_j(w); c_1 is (1.8), c_2 is
printed after (7.14). Its Section7 proof separates the first theta
term and exponentially small remainder, then converts factorials by
Stirling. Neither an effective onset nor differentiation of the
remainder is supplied. Import the result by citation; no reproof of
the saddle theorem is needed.

The future calculation must choose a fixed expansion order adequate
for the coefficients multiplying the errors at k-1,k,k+1,k+r-1.
Control the errors at these integer arguments first, including the
large multipliers in h_(r-1). Smooth differentiation of the explicit
Lambert-W main term is permitted; differentiation of an unknown
big-O function is not. Keep gamma_j/j! and the full h definition.
No derivative of f or positive limiting constant is asserted here.

## One bounded test and decision

Determine lim_(r->infinity) h_(r-1)/r at k=1024r, or a sufficient
rigorous one-sided asymptotic bound if a full limit is unnecessary.
Extract the corresponding entry of the exact F using its triangular
factors; do not replace F by a cubic truncation or a divergent upper
majorant. Relate that entry to the required spectral norm threshold1.
This is the whole nominated mathematical attempt.

If an exact lower bound forces ||F||_2>=1 eventually, abandon the
unchanged norm criterion on this ray, retaining the actual asymptotic
and the failure evidence. This says nothing against the determinant
signs or RH. If the endpoint passes, record the still-missing full
norm estimate; a small entry alone does not prove a small norm.
Continue only with an explicit justified further estimate, not a
larger matrix scan. If inconclusive, preserve the precise residual
bound and stop this bounded test without extending the hierarchy.

Plausible use: decide whether this independently sourced coefficient
comparison can approach bounded k/r, outside its far-tail theorem.
Even success on this ray leaves other k/r, bounded k, all remaining
minors and the full unshifted Jensen/RH gap unresolved. L763/L764 are
contrasts only; this test uses neither a Gaussian multiplier nor
prescribed Hermite nodes. No theorem from another notebook is used.

The source's Remark8.2 already warns that its proved method does not
reach this region; that qualitative warning is not the requested
actual-entry estimate. A later result would be local reproduction/
specialization, not a new discovery of the tail limitation. Mathlib
coverage is not checked. No mathematical derivation or script was
performed in preparing this assessment.
