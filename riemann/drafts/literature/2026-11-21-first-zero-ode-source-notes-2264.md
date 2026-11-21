# Direct first-zero ODE source review2264

21 November2026. LITERATURE only; source comparison completed.
The exact target is the TARGET in nomination2263. No new differential
identity, curvature theorem, kernel calculation or script is asserted.

The main gap is L030-L032/C032a actual-Xi all-degree algebraic mixed
positivity. The intermediate target is a one-dimensional comparison
for the proposed first-zero sine resolvent. Its plausible use is a
shape input for repeated zero removal; actual-Xi applicability,
iteration and all-degree transfer remain independent gaps.

Continue only with a matching primary theorem or one precise extra
condition having a bounded independently testable sign threshold.
Otherwise reject the proposed direct import. Preserve C919s's fixed
quartic point test and C919t's audited joint-density obstruction.
Neither decides generic marginal preservation. Their full matching
Mathlib coverage remains unchecked. No cross-notebook input is used.

## Saved source scope before further reading

Local reads: C919s's full proof and qualifications; C919t's hypotheses,
conclusion and its distinction between density and marginal curvature;
notes2257/2260 and history2263. A targeted search of21November source
assessments and first-zero/sine ATTEMPTS found no ready direct forced
ODE comparison in those ranges. This is not a novelty claim.

Initial actual searches:

- `log concavity inhomogeneous Helmholtz equation log concave right hand side Neumann comparison`
- `Kennington power concavity elliptic equation log concave forcing positive zeroth order`
- `log concavity sine resolvent first zero Fourier transform differential equation`
- `Korevaar 1983 convexity properties solutions elliptic PDE concavity maximum principle pdf theorem b decreasing`

Three source candidates were considered, as detailed below. DLMF/Tuck
solution and positivity coverage is reused from2257 without browsing.

## Candidate1: Kennington1985, limited access, no import

A.U. Kennington, *Power Concavity and Boundary Value Problems*,
Indiana Univ.Math.J.34(1985),687-704, DOI10.1512/iumj.1985.34.34036.
Primary scans: https://math.jhu.edu/~js/Math745/kennington.pdf and
https://math.jhu.edu/~js/Math646/kennington.pdf .
Indexed primary excerpts exposed Theorems3.1/3.2, Remark3.1.1,
pp691-693, and part of Theorem4.1's proof p696. The general principle
asks for strict decrease in the solution variable and harmonic
concavity; its conclusion only excludes an interior positive maximum
of the convexity function. The boundary theorem adds a strict
directional boundary-slope condition. The forcing theorem concerns
bounded convex Dirichlet problems, n>=2, with power-concave forcing.

These are leads, not fully inspected theorem/proof imports: web PDF
extraction returned no readable lines, screenshot calls supplied no
inspectable images, direct curl failed DNS, and the publisher/DOI
endpoints failed. Indexed excerpts do not discharge primary-proof
coverage. No claim depends on their uninspected proof cases. In
particular neither a one-dimensional extension nor a half-line
boundary passage is imported. Access is parked; it is not essential
to the distinct, fully readable candidate3 hypothesis test below.

## Candidate2: Keady1985, inspected mismatch

G. Keady, *The power concavity of solutions of some semilinear
elliptic boundary-value problems*, Bull.Austral.Math.Soc.31(1985),
181-184, Theorem1 pp181-182 and proof discussion pp182-184:
https://doi.org/10.1017/S0004972700004676 . Publisher PDF:
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/07C9AA7CEA8EFD032A8E8462E656C100/S0004972700004676a.pdf/div-class-title-the-power-concavity-of-solutions-of-some-semilinear-elliptic-boundary-value-problems-div.pdf .

The theorem treats positive C2 interior, continuous up-to-boundary
solutions of -Delta u=u^gamma, 0<=gamma<=1, zero Dirichlet data,
on a smooth bounded convex planar domain, with boundary curvature
uniformly bounded away from zero. It concludes alpha-concavity for
0<=alpha<=(1-gamma)/2. The proof uses a curvature quantity, its
boundary positivity, a nonnegative zeroth-order coefficient and a
separate check on a degeneracy set. These hypotheses and the boundary
discussion were inspected in publisher text; several displayed
coefficient formulas are illegible in extraction and are not imported.
The paper refers intricate coefficient calculations to report[3],
which was not read. Its homogeneous reaction, planar Dirichlet data
and positive-superharmonic setting do not match the forced oscillatory
Neumann/decay problem. No coefficient substitution or theorem
extension was attempted. This rejects the direct citation only.

## Candidate3: readable general principle and a bounded next test

M. Gallo, R. Moraschi and M. Squassina, *Quantitative and exact
concavity principles for parabolic and elliptic equations*,
Proc.Roy.Soc.Edinburgh A, First View,1-54, published online
23September2026, DOI10.1017/prm.2026.10177. Inspected publisher
HTML version21November2026:
https://www.cambridge.org/core/journals/proceedings-of-the-royal-society-of-edinburgh-section-a-mathematics/article/quantitative-and-exact-concavity-principles-for-parabolic-and-elliptic-equations/A4D4DE35A8D20F122BBB36D4D2ECFA43 .
This is a primary research article. Use the published numbering;
the search-exposed preprint has different numbering and is not used.

Read Theorem4.1's entire statement and proof, equations4.1-4.8,
Remarks4.2-4.3; Theorem4.4's statement4.9-4.11 (not its entire
proof); and Section5's boundary discussion, Theorem5.1's statement
and its initial boundary-exclusion proof case. No full boundary
theorem or harmonic-concavity application is imported.

For precision, the local hypothesis in Theorem4.1 is as follows.
The equation is

    -sum a_ij(D_x v,t) D_ij v = B(x,v,Dv,t).

The matrix is symmetric positive definite, B is locally bounded
and differentiable in its solution and time-derivative variables,
and v is C2 in space and C1 in time. Put p=(p_tilde,p^(n+1)).
At an attained negative interior minimum of the time-weighted
concavity function, all three spatial gradients agree. The required
inequalities are

    B_(p^(n+1)) <= 0,
    B_s + mu B_(p^(n+1)) <= -sigma < 0,
    mu>=0, sigma>0.                                      (S)

The second inequality need only hold at the middle spatial point,
on the solution-value and time-derivative intervals specified in
the statement. Its conclusion bounds that minimum by the source's
concavity defect divided by sigma, with the stated time factor.
It does not itself establish a global minimum or boundary control.
The proof's decisive cases were inspected: coincident gradients,
the Hessian inequality, the mean-value step in B, the time derivative
sign at a minimum, and the use of(S) in4.8. Remark4.3 explains the
time-weight repair when B includes -v_t. It is not a repair for an
equation independent of the time-derivative variable by citation
alone. Theorem4.4 instead retains strict solution-variable decrease.

Section5 obtains boundary control with bounded smooth strongly convex
domains, n>=2, positive solutions vanishing on the boundary, a strict
inward normal derivative, and log-concave initial data. Theorem5.1
also assumes a uniform upper bound on the derivative of its
log-transformed reaction. Its proof excludes initial-time and spatial
boundary minimizing sequences before using the interior theorem.
Our Neumann origin condition and decay at infinity do not establish
these hypotheses. A first cosine zero is not a cited principal
Dirichlet eigenvalue condition. The oscillatory term +x^2 G and
the forcing x^2 K must both be retained in any later substitution.

Thus there is no direct import from this candidate either. Unlike
candidate1, its complete relevant local condition and proof are
available: (S) supplies a precise, inexpensive exclusion test before
any attempted half-line comparison. This is a useful source-level
narrowing, not a new marginal theorem or proof that(S) fails here.

## Continuation nomination, no calculation performed

The exact future target is:

Test the strict solution-variable monotonicity hypothesis of Gallo-Moraschi-Squassina Theorem4.1 for the stationary logarithmic first-zero resolvent equation, retaining both forcing and oscillatory terms and the theorem's restricted solution-value intervals.

This is one hypothesis test, not a generic preservation proof.
Conditionally suppose K has nomination2263's full generic hypotheses,
x is its least positive cosine zero (multiplicity allowed), and G is
a positive C2 solution of the stated half-line equation with Neumann
origin data and decay. The sine formula, even extension and quotient
interpretation remain separate unpaid generic interfaces. Their truth
must not be inferred from the conditional algebra test. C919s supplies
one fixed example under its software contracts, not a general theorem.

The next calculation is to derive the equation for v=log G, normalize
its leading coefficient to the sign in Theorem4.1, and test(S) in the
stationary representation with no inserted -v_t term. No expression
for the specialized B or its derivative is derived in this source
turn. The sign convention must be checked, not changed by replacing
the desired concavity with convexity. A restriction to the exact
middle-point solution intervals is allowed; a uniform condition on
all real solution values is stronger than the source requires.

Decisive threshold: a negative upper bound -sigma<0 on the applicable
B_s. If that is structurally impossible even on every nonempty
restricted interval, abandon this direct stationary principle. A
successful bound only justifies later investigation of source
concavity and boundary behavior, not preservation itself. No
parabolic embedding, parameter scan, new point test, retuned model,
paired-density premise or boundary exhaustion is part of this test.

This conditional matching calculation uses ordinary chain/product
rules and the inspected source condition; no missing theorem prevents
it. No standard result needs reproof. Newly written EXPLORE coverage
for it is separately subject to the next-turn gate approval. Actual-Xi
applicability, positivity/quotient interfaces, iteration and all-degree
transfer remain open even if this necessary condition passes. Full
matching Mathlib coverage remains unchecked, not asserted absent.

## Search and outcome qualifications

Further actual queries were targeted to Kennington's title,
Theorems3.1/3.3/4.1 and proof p692, and to Korevaar1983's convexity
principle. These yielded the indexed extracts and the accessible
Gallo-Moraschi-Squassina primary article above. Secondary surveys,
search-exposed Brascamp-Lieb discussions, Greco-Kawohl1999 and
Korevaar originals remain unread leads; no fourth candidate was
reviewed. No claim of novelty follows from unsuccessful searches.

Outcome NEGATIVE at source-comparison level: direct imports from the
readable candidates miss their equation/boundary contracts; generic
ODE curvature preservation remains unproved. The specific remaining
monotonicity question is now covered for a bounded calculation,
instead of another broad source search. The optional Kennington
access problem does not block it. No new lemma, proof, mathematical
script, DAG edge, PROOF paragraph or supervisor state was changed.
