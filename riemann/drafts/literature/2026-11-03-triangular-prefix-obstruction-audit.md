# Causal prefix obstruction: source-covered audit nomination

TARGET: Audit paper 47/v1 Proposition 4 and its transfer (39) for L729's prescribed triangular Möbius family, retaining N-dependent complex anchors, arbitrary fixed-zero multiplicity and causal support.
CHECKED: 2026-11-03
DECISION: IMPORT
SEARCH_EVIDENCE: The completed prefix-obstruction comparison searched exact Selberg/Mobius prefix and Pintz-filter terminology, checked the local recorded lead and failures, and found an exact statement in paper 47/v1 Proposition 4. No novelty claim; ready coverage newly saved for separate supervisor approval.
SOURCE_EVIDENCE: bramble_trace, A logarithmic-prefix Nyman–Beurling criterion and transferred zero bounds, rStation paper 47/v1, 24 October 2026, Section 1/(1)--(3), Section 7 Proposition 4/(37)--(48) and final divisor identity; Pintz arXiv:2608.24878v2 Theorem 6.1/(6.16)--(6.23) inspected as methodological background, not a directly applicable theorem.
COMPARISON: The source's H, rho_k and f_N exactly match L729's family (rho_1=0); Proposition 4 includes all complex drifts, each fixed nontrivial zero with beta>=1/2 and its actual multiplicity. No new specialization is needed beyond identifying the family and cell endpoint.
GAP: Local verification of manuscript support, contour estimates, uniform bounded-anchor error, nonzero residue and finite-prefix transfer remains; a full norm bound, any actual off-line zero and mixed positivity remain unresolved.
REASON: A bounded conceptual audit can accept or reject a concrete drift-uniform necessary condition without assuming RH or the unpaid residual. It verifies cited mathematics, not a creative mechanism or new growth theorem.
SCOPE: Audit and, only if valid, canonically import Proposition 4 and (39). Exclude Corollary 5's upper-growth proof, optimal-prefix Theorems 1--2, numerical scripts, new kernels, growing-zero uniformity and every norm-decay claim.

The exact primary source is
[paper 47/v1](https://rstation.ai/problems/riemann_hypothesis/papers/47/v1).
The extracted hypotheses, all essential proof cases and source comparison
are in [the completed assessment](2026-11-03-triangular-prefix-obstruction-coverage.md).
Its source's acceptance report is not a mathematical premise.
Pintz's [v2 Theorem 6.1](https://arxiv.org/html/2608.24878v2) concerns
M(x), eta<1/10 and a Gaussian filter with a paid tail. It does not imply
this causal, arbitrary-multiplicity, drift-uniform statement by citation
alone. The source supplies the changed proof, whose validation is the
purpose of the audit. Do not seek novelty or rederive a different theorem.

For integer N>=2, H=L²((1,infinity),dx/x²), ell=log N, and the actual
Mobius coefficients of L729, the claimed conclusion is as follows.
For every fixed nontrivial zero rho=beta+i gamma of zeta, beta>=1/2,

    inf_(a in C) sum_(j<=N)|a j-psi(j)|²/[j(j+1)]
      >=c_rho N^(2 beta-1),   N>=N_rho,

with c_rho>0. Consequently the squared norm of 1-g_N on [1,N+1)
is at least c_rho N^(2 beta-1)/(log N)², and hence so is the norm on
the larger source prefix [1,ceil(N log N)+1). No zero is assumed simple,
no uniformity in height is claimed, and this is not a full-norm upper bound.
The source's head residual identity uses

    alpha_N=sum_(k<=N)mu(k)(1-log k/ell)/k,
    ell(1-g_N(j))=(ell alpha_N)j-psi(j),  1<=j<=N.

Essential local input: L729 fixes H, rho and g_N and gives elementary
divisor identities; the actual mu and Lambda must be retained. No result
of L730 or L731, RH, simplicity, derivative moments, subpower growth,
neutral saturation or full-update contraction may be assumed.

Bounded audit: check the source's G(s) in (41), including removal of the
order-m zero and pole at z=1; prove its inverse Mellin integral bounded
and zero for H<=0 by the stated lines and horizontal bounds. Check
absolute Fubini on Re s=3 for bounded complex anchors, then the move to
Re s=-1/8 in (45), the excluded z=0 and s=-1 poles, and absence of poles
at other zeros. Verify the residue in (46) is independent of a and nonzero
for every m, with a uniform-in-a remainder. Check the large-|a| branch,
weighted Cauchy--Schwarz in (47)--(48), and exact finite-divisor transfer
including k=1, k=N and the interval [1,N+1). No implementation is needed.

Continuation test: if every case passes, write a cited, qualified canonical
proof with Mathlib status and exact direct inputs. If any essential
claim fails, record that precise failure and stop this import; do not
invent a replacement filter or change the target during the audit.
This gives a reusable necessary-condition test, not progress beyond the
sources or an independently proved arithmetic upper estimate. A later
creative norm mechanism still requires genuinely new input and coverage.

Mathlib: full matching theorem not checked; availability unknown.
