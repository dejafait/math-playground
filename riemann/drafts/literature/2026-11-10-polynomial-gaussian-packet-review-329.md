# Polynomial modulation of the Gaussian slope density — source assessment

TARGET: Assess source coverage for polynomially modulated Gaussian slope packets of degree floor(kappa*n), with original TV=1, target retention at 1+i/8 and uniform exponential suppression on [15/8,17/8].
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step330 searched the exact Laguerre slope-packet statement, polynomial-Gaussian Fourier cancellation, weighted Bernstein-Walsh, Freud Nikolskii and compact weighted Bernstein-Markov terminology; compared reviews291/312/325/327 and stops293/314/315/316/318/327. No inspected result decides the exact normalized complete-response assay; no novelty inferred. Primary references and access qualifications below.
SOURCE_EVIDENCE: Read Bloom-Levenberg-Totik-Wielonsky arXiv1502.06925v2 (4.1)-(4.4),(4.8)-(4.16), Definition4.10, Theorem4.13 with full proof and Example4.14 pp12-13,16-18,21-23; Bloom-Levenberg-Wielonsky arXiv1301.1095v1 Remark4.2/(4.1), Lp qualification and Definition4.3 p11-12; Beckermann-Helart arXiv1707.07871v1 Section1.1/(1)-(7), Theorem1.3 pp2-4. Reuse review325's analytic-saddle contracts, review312's minimax assessment, review327 and audited C997e's exact analytic kernel, C997c(1),(5), audit322 and L997(4),(7).
COMPARISON: Primary compact weighted Bernstein-Markov coverage addresses original weighted L1 versus weighted sup norms; weighted Bernstein-Walsh supplies charged complex growth. These are tools, not complete-response cancellation or target lower bounds. Constant-sharp potential-field extremizers and whole-line Hermite/Freud models cannot be substituted for this truncated slope integral. Existing unmodulated and atomic stops do not decide the new class.
GAP: Construct or obstruct a specified degree-growing multiplier with its original M_n normalization, paid complex/cutoff costs, nonzero target at 1+i/8 and uniform closed-band suppression for the COMPLETE C997c(1) response; neither response inequality follows from the inspected norm tools.
REASON: Essential norm/complex-growth tool coverage is now available from accessible primary sources, so a bounded mathematical attempt is justified. The exact integral extremal problem remains uncovered by a matching theorem, warranting EXPLORE rather than IMPORT or a claim of novelty.
LITERATURE_REASON: Multipliers of degree proportional to n can have exponential contour growth after weighted L1 normalization; the ready unmodulated Gaussian audit does not assess this added cost or uniform data cancellation.
SCOPE: Fixed kappa>0 and fixed A in C997e's sufficiently large range before n; arbitrary nonzero complex P_n of degree<=floor(kappa*n), exact truncated weighted L1 normalization and complete C997c(1) response. Tool coverage permits a bounded construction or subclass obstruction, not uniformity for A_n or kappa_n, a general all-measure claim, or an RH implication.
COVERED_TARGET: Test polynomially modulated Gaussian slope packets of degree floor(kappa*n), with original TV=1, target retention at 1+i/8 and uniform exponential suppression on [15/8,17/8].

## Exact proposed class and bounded test

Retain C997e's J=[15/8,17/8], phi and z_star=1+i/8 and the COMPLETE
C997c(1) response. Choose fixed kappa>0 and a fixed curvature A in
C997e's sufficiently large range, each before n. Let P_n be a nonzero
complex polynomial of degree at most floor(kappa*n), and define

    M_n=integral_J exp(-A*n*(c-2)^2)*|P_n(c)|dc,
    dmu_n(c)=M_n^(-1)*1_J(c)*exp(-A*n*(c-2)^2)
                           *P_n(c)*exp(i*n*(phi(c)-c))dc.

The proposed test is whether this class contains one sequence with
|H_n^+(z_star;mu_n)|>=exp(-a_n), a_n/n->0, and
sup_{gamma in J}|H_n^+(gamma;mu_n)|<=exp(-sigma*n), for some fixed
sigma>0 on an unbounded integer subsequence. The original TV is the
normalization in this definition; no auxiliary polynomial norm may
replace it. No polynomial sequence or asymptotic estimate is supplied.

The distinct mechanism is cancellation induced by degree-growing
polynomial coefficients across slopes. C997e's single quadratic phase
does not have this freedom. This is not a claim that such cancellation
can overcome the target-normalization cost. A zero at the one data
point 2 alone would not meet the closed-band requirement.

## Relevance, coverage obligations and stopping test

Main gap: L030-L032/C032a actual-Xi positivity and L966/L968 signed
forcing, with L984(H) unpaid. The local downstream use would be an
exact-range obstruction to the nominated point inequality, or a new
subclass cost showing this modulation cannot supply it. Neither would
settle the original signed assay or RH.

Essential inputs are C997c(1),(5), audit322, L997(4),(7) and audited
C997e(4),(15)-(16), with reviews291/325/327. Compare C997b's audited
prescribed-Chebyshev cost and stops293/316/327; preserve trials314/315/318
and the parked C997d certificate. These are comparison evidence, not
premises excluding the proposed polynomials. No cross-notebook input.

Search the exact weighted polynomial problem, standard weighted
approximation terminology, stronger available results and known
normalization obstructions. Retrieve primary hypotheses and the
load-bearing proof cases before accepting a tool. In particular assess
degree/weight coupling, complex growth relative to M_n, and uniform
control of the exact finite response with both branches, both beta
terms, both interval contributions, K's -1 and both cutoff endpoints.
Do not turn an arbitrary entire-function extremizer into a realized
slope polynomial or infer uniform suppression from finitely many nodes.

A useful source assessment either identifies an applicable theorem and
the exact remaining specialization, documents an informative mismatch,
or isolates a precise missing contract. A later mathematical attempt
must produce both required response inequalities with paid costs, or
a genuine incompatible lower bound for a specified design. Failed
upper estimates alone are inconclusive. No previously stopped certificate
is reopened merely by changing its name.

Selected/both-sign transfer, C997a(8), the original assay, reconstruction,
signed recovery, infinite-zero complements, regulator uniformity, L993
and L984(H) remain unresolved. Full matching Mathlib coverage is unknown.
The preceding nomination was REVIEW_REQUIRED at step329. The separate
literature-only comparison in step330 below supersedes that gate; it
does not assert either packet inequality.

## Separate source comparison — step330, 10 November 2026

### Primary contracts and applicability

**Compact weighted norm and growth tools.** T. Bloom, N. Levenberg,
V. Totik and F. Wielonsky, [*Modified logarithmic potential theory and
applications*, arXiv:1502.06925v2](https://arxiv.org/pdf/1502.06925v2),
version stamp 29 October 2015 (retrieved PDF also displays 22 August
2021), printed pp12-13,16-18,21-23. Read (4.1)-(4.4),(4.8)-(4.16),
Definition4.10, Theorem4.13's complete proof and Example4.14.
For F_k={p_k(g(z))q_k(f(z)):p_k,q_k in P_k}, f,g holomorphic near
the polynomial hull, (4.8) requires K,f(K),g(K) subset D_A subset U.
Theorem4.13 assumes compact strongly regular K and positive Borel mu
with mu(D(z,r))>=r^T uniformly for z in K, 0<r<=r_0. For continuous
real Q, (4.15) compares ||h_k exp(-kQ)||_K with its L1(mu) norm
up to C_epsilon exp(epsilon*k). The proof localizes near a weighted
maximum, uses regular compact neighborhoods and Cauchy estimates, then
integrates on radius exp(-3epsilon*k) using mass density. Example4.14
includes interval Lebesgue measure. Equation(4.14) bounds complex growth
by exp(k W*_(K,Q)); it does not bound oscillatory integrals from below.

For the proposed application K=J, use interval Lebesgue measure,
f=g=identity and q_k=1; an enclosing disk supplies D_A (this source
symbol is unrelated to packet curvature A). Interval regularity and
the endpoint mass-density hypothesis are covered. The candidate weight
is real continuous on J; its complex extension in a contour estimate
is a different object. A weighted norm estimate must retain the original
M_n, and the source's exponential growth charge must remain in every
contour/error estimate. No value of W*, contour margin or packet rate
has been evaluated here.

**Degree/weight coupling.** T. Bloom, N. Levenberg and F. Wielonsky,
[*Vector Energy and Large Deviation*, arXiv:1301.1095v1](https://arxiv.org/pdf/1301.1095v1),
version stamp 7 January 2013 (retrieved PDF also displays 15 June 2018),
Remark4.2/(4.1) and the following Lp qualification, printed pp11-12.
For compact K, a weighted Bernstein-Markov property persists for
admissible Q_k converging uniformly to the fixed admissible Q.
The proof explicitly sandwiches exp(-kQ_k) between exp(-kQ)exp(+/-k*epsilon).
The paragraph following (4.1) states the finite-p equivalence, including
p=1; Definition4.3 defines the strong property for every continuous Q.

Here the required bookkeeping is k=floor(kappa*n), with effective
field Q_n(c)=(A*n/k)(c-2)^2 and limit (A/kappa)(c-2)^2, ignoring only
the finitely many k=0 indices. Thus a later application must handle
degree at most k, not assume deg(P_n)=k, and use the varying-field
clause rather than silently fix n/k. This is an applicability check,
not a polynomial construction, full-line replacement or response bound.

**A stronger-looking extremal theorem with different hypotheses.**
B. Beckermann and T. Helart, [*On the sharpness of the weighted
Bernstein-Walsh inequality, with applications to the superlinear
convergence of conjugate gradients*, arXiv:1707.07871v1](https://arxiv.org/pdf/1707.07871v1),
25 July 2017, Section1.1/(1)-(7), Theorem1.3, printed pp2-4.
The constant-sharp theorem assumes Sigma=[alpha,b], Q=U^rho/k with
rho a positive compactly supported measure on (-infinity,alpha].
Its constructed degree-k polynomials give lower bounds for real
point evaluations outside the equilibrium support relative to a
weighted supremum norm. No such representation of our quadratic
field is supplied. This theorem is not imported for the packet.
No proof of its sharpness claim is needed because its hypotheses
already prevent the proposed direct use.

The point here is also the observable: evaluations of a slope polynomial
are not evaluations of H_n^+ as a function of the ordinate. Even a
matching polynomial extremizer requires a realized integral response
with its normalization and unwanted terms paid.

### Exact response, duplicates and prior failures

Reuse review325's inspected Hitrik-Sjostrand Theorems2.3.1/2.3.3,
Lemma2.3.2 and proof (arXiv:1508.00649v1, Section2.3 pp37-40).
Its exponential remainder is multiplied by a complex-domain amplitude
norm. The new polynomial may make that norm exponentially large;
the remainder exponent cannot be read without that charge. Reuse
review327's complete Vanlessen assessment and the audited C997e exact
analytic amplitudes rather than a real-axis bulk O term. No reproof
or new asymptotic is performed in this literature turn.

Review312's already inspected Sete-Liesen Propositions3.2/3.3 control
the continuum polynomial minimax problem, but do not realize those
polynomials through this exact slope operator. Review325's unread
Epperson wave-packet lead remains unused and nonessential. No additional
source is required merely to try a specified polynomial design.

Stop293 concerns fixed projection weights. Stop316/audit317 proves
a normalization cost for prescribed atomic Chebyshev measures.
Audited C997e/stop327 treats P_n=1. None covers arbitrary continuous
polynomial multipliers. Conversely trials314/315/318 only expose
unpaid dual/interpolation/strip certificates, not impossibility of
the measure class. Those routes remain parked on their stated evidence.

A future attempt must retain both analytic Laguerre branches, both
beta terms, upper and lower intervals, K's -1 and both c-cutoff
endpoints in C997c(1). The proof of the existing Gaussian result
only treats its displayed ordinates; a new uniform assertion across
E=J needs its own uniform argument. Applying pointwise estimates at
finitely many data nodes, a full-line Hermite formula, or a complex
polynomial evaluation theorem cannot supply that assertion.

### Discovery and access record

Queries included `weighted Bernstein Walsh inequality polynomials Lp
norm exponential weight Gaussian Saff Totik theorem`, `weighted
polynomial inequalities Gaussian weight complex plane L1 Freud
polynomials`, `polynomial Gaussian modulation Fourier transform
Hermite weighted L1 extremal band suppression`, `Bloom Levenberg
strong Bernstein Markov measures continuous weights Lp interval
Lebesgue theorem pdf`, and exact `Laguerre slope Gaussian polynomial
packet cancellation` terms. No adequate exact-response theorem was
identified; a failed search is not novelty evidence. Unrelated web
results and nonprimary mirrors were not used as mathematical inputs.

Lubinsky-Saff, *Uniform and Mean Approximation by Certain Weighted
Polynomials, with Applications*, Constr. Approx.4(1988),21-64,
author-hosted [texts/82.pdf](https://www.math.vanderbilt.edu/saffeb/texts/82.pdf),
was discovered but not read: web opens failed with 502/timeouts, and
shell curl failed DNS. Search-indexed excerpts are not imported.
Pritsker's 1998 varying-weight compact approximation paper was an
unread lead after failed primary retrieval. The accessible primary
compact tools above remove dependence on these blocked sources;
no repeated access turn is proposed. The 2015 Bloom-Levenberg-Piazzon-
Wielonsky survey pp75-76,81 identified the primary Theorem4.13 and
confirmed the norm terminology; it is not a substitute for that proof.
Full matching Mathlib coverage is not checked; none is assumed.

### Decision and bounded continuation

EXPLORE for the exact COVERED_TARGET. This completes source comparison
for a single mathematical attempt; it does not complete the assay or
produce a lemma. Import the cited norm/growth tools only with their
hypotheses and give necessary specializations in a future canonical
proof. Construct one admissible design with BOTH response thresholds,
or prove an incompatible normalized lower bound for a specified design.
If only failed upper estimates or isolated data zeros result, label the
attempt inconclusive and reassess that design; do not declare the whole
class impossible. Preserve unfinished reasoning and all historical stops.
The newly ready continuation receives separate approval next turn.
