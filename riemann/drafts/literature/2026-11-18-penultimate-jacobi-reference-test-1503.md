# Penultimate Jacobi reference: bounded test nomination1503

TARGET: Test whether the penultimate-site Jacobi reference in assessment1503 admits positive degree-dependent parameters matching the first three subleading coefficients of unchanged P_d=R_d/gamma_0, and whether its combined fourth/fifth Schmeisser residual cost can be o(d^2).
CHECKED: 2026-11-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Source review1503 searched optimized orthogonality measures, prescribed coefficients, Jacobi recurrences and moment feasibility; checked the fixed Gaussian and changed-series stops and the closed L827 finite sequence. No matching actual-polynomial optimized-cost result was located; see drafts/literature/2026-11-18-nongaussian-reference-source-notes-1503.md for queries and limits.
SOURCE_EVIDENCE: Schmeisser2002 (1.1)/(1.5) pp203-204, Corollary1/(2.3)-(2.5) pp206-207, https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf ; Simon2011 Proposition1.3.6/Theorem1.3.7 pp16-17 and complete proof, https://assets.press.princeton.edu/chapters/s9377.pdf ; Curto-Fialkow1991 Theorems3.1/3.9 pp612/619-620, https://hjm.math.uzh.ch/v017n4/0603CURTO.pdf . Reuse C028a's height theorem/proof coverage.
COMPARISON: Favard supplies positive reference existence under real/positive bounded recurrence data; Schmeisser supplies the coefficient-height bound and norm ratios. Neither supplies this constrained cancellation or residual cost. Changing only the last diagonal is explicitly redundant in the source; the penultimate-site and beta changes are the proposed different mechanism.
GAP: Positive matching and the retained-cost asymptotics remain completely unproved; passing them leaves all lower residuals, the full I_d=o(d) estimate and RH unresolved.
REASON: The fixed matched Hermite bound diverges in C028a while C028b makes an independent sublinear payment central. A finite recurrence perturbation changes both coefficient matching and orthogonal norms without changing actual R_d; its first two surviving costs provide an independently falsifiable early test, before attempting the entire sum.
SCOPE: Only the explicitly defined positive recurrence family, three leading cancellations and combined two retained costs below; no larger measure search, numerical degree sweep, all-degree positivity claim or modification of the actual input function.

## Candidate family, defined without claiming feasibility

For each integer d>=5 let m,u,w be real and s,r strictly positive;
all five may depend on d. Define q_(-1)=0, q_0=1 and

    q_n(x)=(x-alpha_n)q_(n-1)(x)-beta_(n-1)q_(n-2)(x).

Here beta_0=1 is immaterial. Specify

    alpha_n=m             (1<=n<=d-2),
    alpha_(d-1)=m+u,      alpha_d=m+w,
    beta_j=s*j            (1<=j<=d-2),
    beta_(d-1)=r*s*(d-1).

For an infinite reference choose alpha_n=0 for n>d and beta_j=1
for j>=d. Each fixed-d sequence is real, strictly positive in beta,
and bounded in index. Simon's bounded Favard theorem is the intended
import, using a_j=sqrt(beta_j), b_j=alpha_j, to justify a positive
infinite-support reference probability measure with all moments.
Its bound may depend on d. Do not replace this by a d-point atomic
measure with vanishing higher orthogonal norms. Record the hypotheses
and their applicability when actually using the theorem.

Use precisely C028a's actual b_j and monic P_d. Expand uniquely

    P_d=sum_(nu=0)^d a_nu q_nu,    a_d=1,
    h_nu=integral q_nu^2 dmu_d.

Only source-known recurrence/norm interfaces are imported; no
coefficient formula, parameter solution or optimized bound is
asserted here. In particular source absorption of a real a_(d-1)
must be distinguished from useful cancellation of lower terms.

## One bounded test and its downstream use

Derive the finite coefficient equations

    a_(d-1)=a_(d-2)=a_(d-3)=0

for this family and check s,r>0. If feasible, analyze only

    B_d=(h_(d-4)|a_(d-4)|^2+h_(d-5)|a_(d-5)|^2)/h_(d-1).

The necessary threshold for the hoped-for full Schmeisser budget is
B_d=o(d^2). For d=5 the second term is the constant residual; there
is no negative index. The finite computation needs only the actual
top five subleading coefficients, not a new infinite moment law.
Use L021/C028a conventions; import existing coefficient/logarithm
identities if needed, with their hypotheses, rather than treating
formal zero power sums as positive moments under an RH premise.

Decisive failure: prove infeasibility for all sufficiently large d,
or B_d>=c*d^2 with c>0 for all feasible choices eventually. Decisive
pass of this necessary test: exhibit a positive matching parameter
sequence and rigorously prove B_d/d^2->0. A finite-degree numerical
pass, an unconstrained stationary point or a compact-parameter
search does neither. A negative assertion must include all feasible
degree-dependent scalings and positive parameters approaching zero.

A pass would justify separately assessing the remaining full residual
sum; it would not estimate that sum. A failure stops this family only.
If neither alternative is established in the bounded attempt, save
the unsolved equations/parameter regimes and report EXPLORATION;
do not extend an uninformative parameter sweep. The novel ingredient
being tested is redistribution through an earlier Jacobi site and a
positive off-diagonal parameter, not another last-diagonal gauge.

## Inputs, approval and qualifications

L018/L021 fix actual Xi and its coefficients; C028a fixes the exact
R_d and the matched-Gaussian failure; C028b fixes the height criterion.
No input asserts a nonreal actual zero, RH, positive matching, a
uniform measure bound, or control of omitted residuals. L763/L764,
L827 and the inverse/grid stops are contrasts, not theorem inputs.
Mathlib coverage is not checked; availability is unknown.

This is a new ready nomination produced by a literature-only turn.
It requires a separate approval next turn before mathematical work.
Recommended eventual routing: proof_attempt/creative, deep_research/max.
The central obstruction is whether positive reference-norm freedom
can pay the cubic mismatch without recreating a linear height cost;
the bounded test above supplies the precise pass/stop evidence.
