# Moving-band Jensen root count: nomination1364

TARGET: Establish or refute the existence of c>0 such that, for all sufficiently large d, the actual Jensen polynomial J_d has at least c*d^(1/4) distinct negative roots whose q parameters lie in (q_e(d)+d^(-1/2),q_e(d)+2*d^(-1/2)), using C019h, the local Gaussian term and exact phase barriers, and verify separation from Ono v1's counted bulk intervals.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1365 reused assessments1361/1362 and audited C019h, searched the exact-identifier edge/root, unshifted-Jensen phase/saddle and Ono d^(1/4) terms listed below, and checked C019g and stops1345/1355/559 narrowly. No inspected theorem states the requested band-localized count; search absence is not novelty evidence.
SOURCE_EVIDENCE: Ken Ono, An Asymptotic Jensen–Pólya Criterion for GRH, arXiv:2610.38870v1, 28 October2026, https://arxiv.org/html/2610.38870v1 : (2.8)-(2.10), Lemma7/(3.3)-(3.11), Lemma9/(3.13)-(3.16), Corollary10/(3.17)-(3.20), Lemma11/(3.21)-(3.24), Lemmas12-14 including the uniform oscillatory Gaussian proof, Proposition15/(5.2)-(5.5) and its local/complement split, Corollary16's conjugation proof, (5.6), Lemma17/(6.1)-(6.2), complete Section6 count and Remark18 inspected or reused as detailed below.
COMPARISON: The local part of Proposition15 is available on q_e<q<=c_0*T with n_q>=1, and its proof cites a Gaussian estimate uniform as Re(D_q/|D_q|) tends to zero. Corollary16 and Lemma17 are printed on I_d; the former's conjugation identity and the latter's branch/bound ingredients are separately identified below. C019h replaces one complement estimate only. No source directly imports the proposed localized count.
GAP: On the changed band one must verify a common local-Gaussian onset, assemble a full signed error, check continuous bounded phase correction, prove a lower phase-span bound, perform ordered integer hitting and strict interval counting, and verify exact reciprocal-map separation from the old bulk intervals. No such specialization is proved in this review.
REASON: Essential source coverage is complete for this bounded established-method application. Cite the named local Gaussian, saddle derivative, logarithms and sign-count mechanism; derive only their changed-band specialization and combination with C019h next turn. No general Gaussian/IVT reproof, generic Airy import or further essential source is needed for that attempt.
SCOPE: K=Q, integer d tending to infinity, exact d-dependent q_e, Lambda, T, B=T^2, A_d and X=-T^2/(d*q); precisely the open band in TARGET, with its closed endpoints allowed as sign samples. No changed band, effective onset, simplicity, uniqueness, improved overall deficit order, every-degree hyperbolicity or global positivity. This completed comparison approves an attempt, not its conclusion.
LITERATURE_REASON: The target changes from one complementary integral to an actual growing root count. Review1365 completes the previously missing theorem-level scope comparison, reusing assessment1361's source extraction and assessment1362 rather than reopening their estimates.

## Relevance and bounded test

The main gap is L030-L032/C032a actual-Xi all-degree positivity; on this
route every-degree Jensen hyperbolicity remains unproved. The proposed
intermediate target is a growing family of real roots in an omitted band.
Such a family could reduce the omitted near-edge count in a lower-bound
argument. The larger far-end loss is independent, and success here would
not by itself improve the overall source deficit order or imply RH.

Use C019h for its now-audited complement estimate and C019c for exact
conventions. L018/L021 identify the actual family and coefficient
normalization; their use must be spelled out in the eventual application.
C019g supplies fixed-window comparison context, not a growing-window
input. Reuse the precise source statements recorded in
`2026-11-17-jensen-edge-bulk-overlap-nomination-1361.md` and
`2026-11-17-jensen-moving-saddle-complement-1362.md` before further browsing.
Check for an already covered count or obstruction in those assessments
and their cited local results. Preserve stops1345/1355/559; none is a
proof that this different signed application is impossible.

The threshold c*d^(1/4) is a proposed test, not a result of this turn.
Source comparison should first identify the exact hypotheses for the
local part of Proposition15, the conjugation argument, the branch choices
in (6.2), and Section6's use of continuity without phase monotonicity.
Distinguish source statements on I_d from analytic identities that may
hold on a larger range. Keep the positive normalization and degree-
dependent edge throughout. Do not infer signed barriers from modulus
control alone, or identify lower-bound losses with actual nonreal zeros.

After separate approval, continue only if the full signed error at the
proposed barriers is strictly smaller than its leading margin, the phase
span supplies the stated growing count, and the resulting open intervals
are disjoint from the source's counted intervals. A failure of one
majorant is not a refutation of the root-count statement. Preserve the
failing term or hypothesis and require a materially different test before
repeating an unsuccessful implementation. The next turn is literature-only
until this changed target has a ready decision; no new lemma is authorized
by this nomination.

Creative discovery remains due. This is a potential specialization of an
established phase-barrier mechanism, not a creative global mechanism.
The independent far-end/global closure obstruction lacks a justified new
test, so no creative label is assigned merely to satisfy scheduling.
Full matching Mathlib coverage and source formal artifacts remain unchecked.

## Completed scope review1365 — 17 November 2026

This section supersedes the nomination's pending-coverage instructions.
It approves only the exact TARGET above for a later mathematical attempt.
No new estimate, phase extension or root count is established here.

### Source evidence and the permitted specialization

The primary is [Ono v1](https://arxiv.org/html/2610.38870v1), identified
by the HTML as 28 October 2026. Assessment1361 already extracted the
cutoff and counting proof; assessment1362 covered the local analytic
inputs. This review checked the following load-bearing statements and
proof cases against the primary, rather than treating the old bulk
corollary as a theorem on the new band.

* Lemma7 applies on q_e<q<=T. Equations (3.6)-(3.7) give uniform
  r comparable to q^(-1/2) and q-q_e comparable to alpha^2 near the
  degree-dependent edge. Its implicit-function proof, particularly
  (3.11), makes that comparison uniform in 1/Lambda. Lemma9 gives
  Re D_q>0 and |D_q| comparable to sin(alpha). These are the source
  inputs for a future lower bound on n_q, not a lower bound proved here.
* Corollary10 supplies the unchanged ell_q and the normalized p_q
  with bounded C3 norm, p_q(0)=p_q'(0)=0, p_q''(0)=-D_q/|D_q|,
  Re p_q<=0 and |p_q'(y)|>=|y|/2. Lemma13 supplies f_q(0)=1
  and its uniform C1 bound for q_e<q<=c_0*T.
* Lemma14 assumes those C3/C1 bounds, |A|=1, Re A>0 and real n>=1.
  Its principal-root Gaussian formula has absolute error O(n^(-3/5))
  and relative error O(n^(-1/10)) when f(0)=1, uniformly in A.
  The proof uses cancellation for both finite tails and the infinite
  Gaussian tails; it does not require Re A bounded away from zero.
  Thus no different stationary-phase theorem is essential at this gate.
* Proposition15's local-integral proof uses precisely these statements
  and produces the nonzero Z_d of (5.3). Its local and complementary
  contributions are evaluated separately. Reusing the local part while
  replacing its complementary bound by C019h is the identified
  specialization. The printed full-circle Corollary16 on I_d cannot
  simply be cited on the new band. Also (5.5) assumes an upper endpoint
  Q sufficiently large: do not substitute the bounded band's upper
  endpoint into that statement. Check n_q from (5.2) and the pointwise
  saddle estimates instead. This is a hypothesis obligation, not a
  source obstruction to that different application.

Corollary16's proof identifies the upper integral as the exact conjugate
of the lower integral, using real-entire F, real q and the single-valued
Cauchy integrand with conjugate factorization branches. This identity
does not use its preceding I_d error estimate. The future application
must retain the same circle, angular orientation, positive P_d=d!/d^d
and principal square root as C019h, then put both errors on the common
2|Z_d| scale. A modulus estimate on the complement alone is not a sign
formula. The full cosine-normalized error must be strictly below 1/2
at the selected barriers.

Lemma17 is stated on I_d. Its proof uses the following independent
ingredients: continuous saddle parameters; Re D_q>0 and principal
Arg D_q; the Euler-product logarithm in Re s>1, bounded at the saddle
by N log(zeta(4)) once (4.9) gives Re s>=4; and Lemma12's single
holomorphic log(g_K), with bound O(1/(Tr)) for |arg w|<=pi/2,
|w|>=W_0. Formula (6.2) retains every term, including -mu_K*alpha
and -Arg(D_q)/2. For K=Q, (4.1) gives mu_K=7/4. None of these
ingredients invokes the old tau cutoff. This identifies the hypotheses
to check on the changed band; the extended bounded continuous phase
statement itself remains mathematical work for the next turn.

### What the count still has to prove

Lemma11/(3.22) gives the exact derivative S'(q)=r^2 sin(2 alpha)>0
on the saddle branch. Its (3.23) is only an upper bound near q_e.
Subtracting two such upper bounds cannot establish the positive phase
span sought here. Use (3.22) together with the uniform pointwise
geometry to seek a lower bound across this particular band, retaining
Lambda and q_e(d). This review does not carry out that integration or
assert that the proposed d^(1/4) threshold has been achieved.

Section6 supplies the established sign-count mechanism: for a continuous
phase with positive endpoint span Delta, its ordered consecutive integer
levels can be hit without monotonicity, and alternating signs yield at
least Delta/pi-2 distinct roots in intervening open intervals. The next
attempt must give a growing quantitative span after the bounded phase
correction and the integer losses. Endpoint samples are permitted, but
every claimed root must lie strictly inside the open TARGET band.
No simplicity or uniqueness follows from this argument.

For comparison, the source's actual counted q intervals are in
I_d=[q_e+tau,Q], tau=M*sqrt(log(d)/d), Q=c_0*T, with M fixed
as in (5.6); Remark18 and (2.10) give their exact reciprocal images.
The future proof must explicitly compare the proposed band's upper
endpoint with q_e+tau and check injectivity of the same reciprocal map.
Do not use the coarse containing interval in Remark18 as an exact
counted interval, or interpret the lower-bound loss as known nonreal
roots. Theorem1's much larger global count does not locate this extra
family; the independent larger far-end loss remains unpaid.

### Search, duplicates, limits and decision

Queries were `"2610.38870" "edge" "roots"`,
`"unshifted Jensen" "phase" "saddle"`, and
`"Jensen" "Ono" "d^{1/4}"`. Results included aggregators, shifted
Jensen work and unrelated papers; no additional matching primary
theorem was identified. No theorem was imported from snippets,
aggregators, forums or claimed resolutions. Reuse assessment1361's
earlier exact-identifier/nonstationary searches and shifted-Hermite/CFU
scope comparisons. These bounded searches do not establish originality.

Narrow local checks covered C019g's normalization/identity passage,
C019h's exact hypotheses/conclusion/qualification, assessments1361/1362,
and stops1345/1355/559. C019g supplies a fixed-window count only;
C019h supplies the audited complement only. The older stops concern
different automatic imports, endpoint signs or scaling, and remain
preserved. No duplicate completed moving-band count was found in
these relevant local records. No cross-notebook theorem is used.

Decision SPECIALIZE is ready for the exact TARGET: import the named
results and prove only the listed applicability, signed assembly,
quantitative phase and counting differences. Continue on uniform sign
margin, sufficient lower phase span and exact separation; preserve any
failed term or hypothesis and distinguish a failed bound from a false
root-count statement. No effective onset or global closure is included.
This is established-method development, not a protected creative
mechanism. No independently justified creative far-end/global test is
available from this source comparison.

The primary's appendix advertises a separate Lean repository; that is
an unread artifact lead, not inspected evidence of the specialization
or of matching Mathlib coverage. No source-wide validity, formal replay
or full matching Mathlib theorem was checked. Later canonical proofs
must retain those qualifications and cite the named v1 results exactly.

Completed outcome EXPLORATION records the new scope assessment without
a mathematical advance, informative counterexample or originality
claim. Completed kind LITERATURE, classification REPRODUCTION, actual
task literature_comparison. No lemmas, mathematical scripts, PROOF or
DAG were changed. Research on this newly ready target remains for a
subsequent invocation and its separate supervisor approval.
