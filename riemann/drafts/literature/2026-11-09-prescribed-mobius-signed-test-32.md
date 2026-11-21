# Prescribed Mobius two-shift signed test: bounded specialization

TARGET: Test whether the prescribed normalized quadratic-taper Mobius two-shift form has an error-dominating signed eigenvalue decision at N=floor(T^(1/5)), using BBLR's complete six-term formula with exact Hardy phase and Xi curvature, without changing the taper, length or shifts.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed prescribed-profile comparison in 2026-11-09-prescribed-mobius-two-shift-scope-31.md, completed step32; no additional searches or mathematical attempt are claimed in this nomination.
SOURCE_EVIDENCE: BBLR https://arxiv.org/pdf/1609.02539v1#page=2, Theorems1.1--1.2 and holomorphy remark printed pp2--4 (directly reopened 2026-11-09, recovery step33); primary mollifier comparisons and precise URLs in the completed assessment. L622 Sections1--4 and its November1 application audit supply the established exact-phase/jet method, not this length's remainder or sign.
COMPARISON: The unnormalized q_N fits the source coefficient convention; the exact b_N factor can remain outside. No checked explicit mollifier theorem supplies the requested signed two-by-two answer. Import the arithmetic theorem and specialize only this profile; do not reprove its moment/divisor theorem.
GAP: Establish the complete Hermitian main form and every absolute application cost, then separate a negative unit direction or a uniform positive eigenvalue from those costs. Normalization asymptotics, main scale, margin and effective onset are not assumed.
REASON: One bounded prescribed-coefficient test is source-supported and distinct from the parked arbitrary-pair nomination and fixed-bump realization stop. This is established-route specialization, not a creative central mechanism or approved mathematical result.
SCOPE: Actual L637 Z,W,w with fixed w>=0 in C_c^infinity((0,1)), integral one, T<=X<=2T, L=log T, N=floor(T^(1/5)), only observer shifts +/-1/L, complex scalar pair of squared norm one, exact q_N and b_N below. No profile optimization, extra shifts, changed length, pointwise sign premise or RH candidate.

Step32 nominated this continuation without performing its application.
Recovery step33 separately checked its primary source and repaired the
missing direct URL. The target and SPECIALIZE scope are unchanged;
no mathematical application or sign is established by either review.

The exact prescribed definitions are

    q_N(n)=mu(n)(log(N/n)/log N)^2, 1<=n<=N,
    b_N^2=sum_(n<=N)|q_N(n)|^2/n,
    M_N(t)=b_N^(-1)sum_(n<=N)q_N(n)n^(-1/2-it),
    U_a(t)=M_N(t)[a_-Z(t-1/L)+a_+Z(t+1/L)],
    |a_-|^2+|a_+|^2=1,
    I_a(T,X)=integral w((t-X)/T) W(t)|U_a(t)|^2 dt.

Main gap: L030--L032/C032a actual-Xi all-degree mixed positivity.
Downstream use: an error-dominating negative average would supply
actual first-sign evidence for separate scrutiny; a positive margin
would stop this precise family. Neither supplies unsigned microscopic
realization, all-height signs, higher signs or an RH resolution.

Essential mathematical inputs are L637's definitions and analytic
normalization and L622 Sections1--4's exact phase, holomorphic shifts
and zero-safe curvature method. L934 specifies the dictionary and
retained realization stop; its projection inequality is a contrast,
not a sign input. Reuse the November1 source comparisons, including
L622's audit, and step32's exact BBLR scope. No other notebook input.

One coherent attempt is approved in scope: specialize the full source
expression to q_N, keep b_N^(-2) exactly in every term and error,
extract only the first two factors' fixed Laguerre jets, evaluate the
other two factors at the two observer shifts, and test the resulting
two-by-two Hermitian main form against a proved total absolute error.
Do not differentiate M_N or the scalar pair. Keep both mixed
orientations, every gcd multiplicity and all six terms together at
collisions. No logarithmic normalization asymptotic or reference
T(log T)^6 signal may be assumed.

Subdivide the original smooth window into finitely many admissible
BBLR windows at comparable source heights. Prove uniform weight
bounds including the exact analytic Hardy phase, use a fixed source
length exponent between 1/5 and 1/4 while retaining the actual N,
and justify the fixed complex Cauchy extraction. Restore all source
coefficient factors. Pay the actual Xi-curvature cost even at zeros.
These local obligations have source coverage but are not established
for this changed application by this assessment.

The decisive test is rigorous separation: a negative value for one
unit scalar pair or a uniform positive smallest eigenvalue, with the
ratio of complete error to the signed margin tending to zero uniformly
in X (or a fully effective bound stronger than the error). A computed
main-term sign without the complete comparison is only exploratory.
The source's existential constants do not yield a finite-height
certificate. If no separation can be justified in this bounded
attempt, save the failed inequality and unfinished reasoning, then
park this profile without changing its parameters. An informative
obstruction is useful; no lemma or sign outcome is required.

Independent unresolved gaps remain: evaluation and conditioning of
the signed main form, complete asymptotic error, effective onset,
individual heights, realization and all higher orders. Full matching
Mathlib coverage is unchecked. No known arithmetic theorem is to be
reproved. Recommended completed classification for the specialization
is REPRODUCTION unless the work actually changes its source-covered
scope, which would require a new review before proceeding.

## Separate source-gate review — 9 November 2026, step33

Opened the [versioned primary PDF](https://arxiv.org/pdf/1609.02539v1#page=2)
and read printed pp2--4: Theorem1.1 hypotheses, full six-term formula,
prime-power orientations, collision remark and Theorem1.2. The source
requires complex shifts O(1/log T), coefficients bounded by n^epsilon,
and smooth support [1,2] with fixed derivatives O_j(T^epsilon). Its
error is O_epsilon(T^(1/2+2vartheta+epsilon)+T^(3/4+vartheta+epsilon)).
The collision remark extends the total error holomorphically by maximum
modulus. Theorem1.2 retains six terms and the same error; neither
theorem asserts the proposed signed margin.

Reuse step32's completed coefficient and competing-mollifier comparison
in 2026-11-09-prescribed-mobius-two-shift-scope-31.md, including its
recorded failures and November1 application audit. No changed hypothesis,
new search for a sign theorem, or reproof is claimed. In particular,
window subdivision, Hardy-phase weight bounds, Cauchy extraction and
Xi-curvature payment remain application obligations, not consequences
already verified for this profile. The existing exact normalization and
no-retuning requirements remain binding. Full matching Mathlib coverage
is unchecked.

This repair supplies the previously missing direct source URL and
separate review, not new mathematical evidence. Outcome STALLED;
completed kind LITERATURE, classification NOVELTY_UNCHECKED. The same
source-supported specialization is the concrete next test. No lemma,
mathematical script, DAG edge or argument overview changed.
