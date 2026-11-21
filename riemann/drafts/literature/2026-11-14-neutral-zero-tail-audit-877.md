# C750d tail audit — source readiness repaired in878

TARGET: Audit C750d's exact-coordinate projection constants, full-strip product bound and complete BPT zero-tail specialization establishing epsilon_*<2e-16, without assuming a finite Gram margin.
CHECKED: 2026-11-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse completed comparison876 in 2026-11-14-neutral-zero-gram-remainder-875.md and unchanged exact-tail scope in 2026-11-14-neutral-zero-tail-coefficient-bound-876.md; in878 directly reopen both primary theorem URLs below and locate Lemma4. This recovery adds traceable source access, not a new mechanism or novelty search.
SOURCE_EVIDENCE: Reopened https://maths-people.anu.edu.au/brent/pd/rpb276-MC-preprint.pdf published p2923 Lemma1/footnote1 and endpoint convention, and https://arxiv.org/html/2403.17803v1#S2.SS2 Lemma4/full proof attribution. These match the prior assessments. C750d uses L753, L750(11) cutoff bounds and C750c Proof1/5 exact coordinates; their local proofs remain for the conceptual audit.
COMPARISON: A conceptual audit checks the now-written fixed-basis specialization and endpoint/convergence argument, not a new zero-count theorem or positivity criterion. General formulas and methods are known; only validity of these explicit local constants is at issue.
GAP: C750d has a full informal proof and an exact scalar certificate but no independent conceptual audit. Neither a finite Gram margin nor positivity, a stored-zero dataset, infinite-complement control, non-neutral signs or the main mixed-positivity gap is supplied.
REASON: Recovery878 repairs the missing direct-source-URL field and completes source readiness for the unchanged saved audit target. No audit or mathematical advance is claimed; the next turn should perform the conceptual audit using this SPECIALIZE assessment.
SCOPE: Exactly C750d as written in877, T=4log3, H=3000000000000, the ten original C750c(15) coordinates, N=2 and BPT Lemma1 with phi(t)=t^-4; no root calculation, precision sweep, finite Gram sign or broader coordinate family.

The audit should inspect the exact moment lower bounds, three-mode
cutoff-loss Gram comparison and projection contraction in the original
L2 metric, including complex coefficients. Check the global cutoff
derivative bounds, the ten-coordinate norm conversion and the use of
L753(10) on both reflected strips without replacing the holomorphic
product by an off-axis modulus square. Inspect all BPT hypotheses,
the limiting sum, strict/half-weight endpoint handling, multiplicity
and both height signs. The exact scalar certificate proves arithmetic
comparisons only; it does not audit the analytic argument.

Acceptance requires the stated bound for every c in C^10 with no
extra sign, root-data or reality hypothesis. A failed estimate must be
recorded precisely and corrected only within assessed scope. An accepted
bound remains a local standard-method specialization. Usefulness still
requires a separately certified Gram margin exceeding epsilon_* plus
all finite errors. Full matching Mathlib coverage is unchecked.

No newly uncovered mathematics is approved or derived by this review.
The source methods and hypotheses are identical to the assessment saved
before877. Source readiness is complete; independent scrutiny remains.

## Direct source verification878

LITERATURE_REASON: Supervisor recovery requires direct primary-source URLs
in the ready assessment; the audit target and hypotheses have not changed.

Read the [BPT published offprint](https://maths-people.anu.edu.au/brent/pd/rpb276-MC-preprint.pdf),
Math. Comp. 90 (2021), 2923–2935, DOI
[10.1090/mcom/3652](https://doi.org/10.1090/mcom/3652), printed p2923:
the introductory conventions, Lemma1 and footnote1. The lemma is credited
there to Lehman. Its finite-interval hypotheses are 2*pi*e<=T1<=T2 and a
nonnegative monotone decreasing weight. The stated error uses A=.28;
zero sums count multiplicities and half endpoint weights. Its scalar
estimate is unconditional. The audit must check the t^-4 envelope,
strict cutoff and infinite limit; the citation alone does not validate
C750d's coefficient constants or its complex-product majorization.
The sharper Theorem1 on p2924 is not required.

Read [Carneiro–Milinovich v1, Section2.2 Lemma4](https://arxiv.org/html/2403.17803v1#S2.SS2),
26 March2024, including its complete proof attribution to Iwaniec–Kowalski
Theorem5.12. This explicit-formula lemma is expressly unconditional,
despite the paper's RH-conditional main results. It requires analyticity
through |Im s|<=1/2+epsilon and decay O((1+|s|)^(-1-delta)) there, with
epsilon,delta>0. It evaluates the test at (rho-1/2)/i rather than replacing
zeros by real ordinates. L753 is the existing local specialization;
the audit must verify its use for the holomorphic product on both
reflected strips. No new proof of that specialization is supplied here.

The ready scope remains exactly that in SCOPE above. No stored-zero
retrieval, new sign theorem or precision sweep is authorized by this
assessment. Prior C750c scalar-floor/data failures remain relevant;
none obstructs this source-ready audit. Full matching Mathlib coverage
remains unchecked. No cross-notebook input or new source blocker occurs.
