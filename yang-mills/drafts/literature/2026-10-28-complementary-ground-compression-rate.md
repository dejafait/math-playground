# Quantitative complementary ground compression — completed source comparison

TARGET: Determine whether L297's ground compression satisfies ||P_N W_N^(0) P_N||=O(N^-1 log(eN)^2) on the full relative cube.
CHECKED: 2026-10-28
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed the bounded queries and local duplicate/failure comparison below; reused the ready Gaussian, matrix-calculus, scalar-Green and rectangle-reflection readings. Read Brydges--Mitter 1112.0671v3 Theorem 2.1 and its proof assembly, and Lawler--Limic Proposition 4.6.2(a) with its transient-case proof. No inspected matching full relative-cube compression theorem was found; this is not a novelty finding.
SOURCE_EVIDENCE: L297(6)--(7),(15)--(18), L282(6)--(18), L283(5)--(11),(17), L288(2)--(5), L289(11)--(12), and L003 section 2 fix the operator and available errors. Primary quantitative comparison: Brydges--Mitter arXiv:1112.0671v3 (20 December 2011), Theorem 2.1 (2.23), pp. 6--9; supporting scalar input: Lawler--Limic author text, Proposition 4.6.2(a), p. 97, with previously assessed Theorem 4.3.1/Corollary 4.3.3. Exact versions, hypotheses and limitations are recorded below.
COMPARISON: Existing ordered limits and fixed-m boundary constants give no stated target rate. Quantitative finite-range convergence concerns scalar full-lattice fluctuation kernels, not the complete Wilson/density ground compression. Scalar Green bounds and exact relative tensor modes support a direct boundary-kernel test; no general theorem supplies its signed all-face estimate.
GAP: Prove or obstruct the requested rate for the full four-dimensional ground-space bilinear form, retaining density, quartic and cubic kernels, transverse projection and all boundary strata. Effective boundary-depth errors and complete internal sums remain research obligations; none is assumed from the scalar sources.
REASON: Coverage is adequate for one bounded direct test from the exact finite-domain kernels and established scalar tools; no inaccessible theorem is essential to starting it. The changed assessment is ready for separate continuation approval, not a proof of the rate. No lemma, mathematical script or new estimate is produced in this literature turn.
LITERATURE_REASON: The changed quantitative target goes beyond the strong qualitative limits covered for L297; the necessary uniform rate and full relative-boundary estimates have not been assessed.
SCOPE: L297's zero-source one-color operator W_N^(0) and rank-four P_N; exact SU(2) relative cube, even N>=2, a=8/N, counting measure, all-face pins/fixed gauges, all variable normal links, ambient own-slice Wilson jets and full density. Retain L003 L280 L282 L283 L287 L288 L289 L296 L297 and their upstream hypotheses; L291 and one-face replacements are not inputs.
COVERED_TARGET: Determine whether L297's ground compression satisfies ||P_N W_N^(0) P_N||=O(N^-1 log(eN)^2) on the full relative cube.

## Proposed threshold and downstream use

The main gap remains the interacting continuum construction and positive
infinite-volume mass. The proposed intermediate target is only the
quantitative ground compression displayed in TARGET. L297(23)--(24)
identifies it as control of the coefficient of the largest low-pole term;
this is a plausible next use of the accepted qualitative cancellation.
The proposed rate would suppress that contribution at r_N. This is the
reason for seeking the rate, not a claim that it is available.

Other one-line residues, source derivatives and high-spectrum bounds
would still need stronger estimates for a bounded complete tail. No
uniform higher remainder, interacting lower bound, nonzero continuum
sector, field axioms or positive mass would follow from this target alone.

The separate review should reuse the finite Gaussian, analytic derivative
and trace-ideal readings already recorded in the two complementary
assessments. Its changed task is quantitative relative-boundary coverage,
including whether available whole-box approximation errors can reach the
stated rate. L288 is a specific local quantitative approximation lead;
its needed proof ranges and any external rate theorem remain to be
compared for this target. Do not replace the box by a single face or
silently convert an ordered approximation limit into an effective bound.

Continue to a later mathematical attempt only after adequate source
coverage identifies a concrete quantitative estimate to test. In that
attempt, success requires a complete uniform bound at the stated rate;
failure of one crude norm estimate is not a lower bound or a disproof.
An actual slower signed boundary contribution or an uncontrollable
remainder requires refinement or abandonment of that rate, with evidence
preserved. ATTEMPTS/047--050 remain distinct stops, not global bans.
The initial registration supplied no rate calculation or source approval;
the completed comparison below supplies only readiness for a later test.
Full matching and supporting Mathlib coverage for the new rate is not
checked; absence is not asserted.

## Completed comparison (step 535, 2026-10-28)

### Exact object, existing coverage and duplicate check

Use L297(7)'s operator, at zero sources, on its fixed transverse space:
W_N=D_N+E_N/4-A_N/4. Here E_N is the complete two-covariance cubic
contraction and A_N the contracted quartic; these are not merely their
internal-curl or bulk parts. L297(15)--(18) proves its limiting ground
compression is zero, using the exact identity in L289(16). The present
target strengthens that conclusion, without identifying W_N with a
renormalized effective action.

The needed proof ranges were read before comparing external rates.
L282(10)--(14) gives complete-density approximation errors in s_m,t_m;
its (17)--(18) takes N first at fixed m. L283(6)--(11) gives a uniform
nearby-covariance/quartic error and again fixed-m boundary control.
L288(3) gives the genuine uniform internal-curl operator error K/(m+1).
But L289(11)'s row-range and boundary constants still depend on m, and
its (12) is an ordered strong limit. No simultaneous choice m=m(N)
with the requested error has been established in these results.
L297(17) explicitly retains the external-curl difference; a later proof
must include that recorded error rather than silently drop the group.
This is comparison of written estimates, not a newly optimized bound.

Searched the recent boundary/complementary literature assessments and
history/531--534 for ground-compression/rate matches, then inspected the
older transverse-H compression assessment and actual-normal-face source
comparison. Their targets are respectively L116's different trace
comparison and one normal-normal face patch. Neither is a duplicate
of this rank-four full-box estimate. No sibling notebook was read.
ATTEMPTS/047--049 stop rearrangement, absolute-norm and generic orbit
identity mechanisms; ATTEMPTS/050 stops the all-tail expression. None
proves or refutes this quantitative mixed-line compression. The accepted
one-face results in the overview do not cover edges, corners or all
components and are not replacement inputs here.

### Primary quantitative lead and its limits

D. C. Brydges and P. K. Mitter, *On the Convergence to the Continuum
of Finite Range Lattice Covariances*,
[arXiv:1112.0671v3, 20 December 2011](https://arxiv.org/pdf/1112.0671v3),
section 2 and Theorem 2.1, (2.23), PDF pp. 6--7. For d>=3, fixed
dyadic L sufficiently large as specified there for dimension and decay
order, epsilon_n=L^-n, mass parameter a>=0, n>=l>=d and each integer
k>=0, it bounds the scalar fluctuation-kernel difference in the
stated lattice Sobolev norm by c_(k,L)L^(-n/2)exp(-c sqrt(a)).
The source's a is a mass parameter, not our mesh spacing. Section 3's
proof assembly, (3.1)--(3.4), PDF pp. 8--9, combines continuum and
lattice Fourier errors and uses d>=3 for low-frequency integrability.
The detailed proofs of both auxiliary Fourier lemmas were not imported.
The result concerns the BGM full-lattice scalar decomposition, not
L288's geometric-polynomial parameter or a relative-boundary Wilson
operator. Its rate therefore cannot be substituted for the target.
It is a screened supporting lead, not an essential missing source or
an imported compression estimate.

Reuse Bauerschmidt,
[arXiv:1206.2212v3](https://arxiv.org/pdf/1206.2212v3), Theorem 1.2,
Remarks 1.7--1.8 and section 2.1, as assessed in
`2026-10-28-complementary-covariance-infrared-test.md`. Its positive
finite-range decomposition needs the stated propagation and, for kernel
estimates, heat-kernel hypotheses. Those conditions must be checked on
the actual underlying scalar/Hodge operators before any application;
the nonlocal transverse projection is not itself a nearest-neighbor
scalar operator. This theorem does not bound the Wilson contractions.
The unchanged Gaussian and matrix-calculus coverage in that assessment
and its critical-audit companion is reused without another source tour.

### Scalar boundary tools and the proposed specialization

G. F. Lawler and V. Limic, *Random Walk: A Modern Introduction*
(Cambridge, 2010),
[author-hosted 289-page text](https://www.math.uchicago.edu/~lawler/srwbook.pdf),
Theorem 4.3.1 and Corollary 4.3.3, printed pp. 81--84, are already
assessed in `2026-10-23-transverse-h-compression-quantitative-rate.md`.
For the specified symmetric finite-range irreducible walks in d>=3,
they give scalar Green asymptotics and coordinate-difference decay.
Newly read Proposition 4.6.2(a), printed p. 97, and its transient proof:
the killed Green function equals the full Green function minus its
exit-distribution contribution. The proof splits total visits at exit
and uses the Markov property. This is a scalar Dirichlet tool; neither
it nor the repeated-coordinate difference bound supplies the mixed
staggered vector estimates or Wilson products. Check generator and
counting-measure normalization before applying it.

Reuse the inspected Brandt (1966) rectangle/reflection comparison in
`2026-10-27-actual-normal-source-face-transfer.md`: *Estimates for
Difference Quotients of Solutions of Poisson Type Difference Equations*,
Math. Comp. 20, 473--499,
[author copy](https://www.wisdom.weizmann.ac.il/~achi/LOP3.pdf),
Theorems 5.1/5.2, 7.1/7.2 and section 8. Its zero-Dirichlet or centered
ghost-point Neumann conditions and corner qualifications must not be
silently transferred to our mixed midpoint/vertex grids. No matching
vector or Wilson theorem is imported from it.

The preferred bounded test is direct quantitative localization of the
ground **bilinear** forms using L003 section 2's exact tensor heat
kernels and their correct sine/cosine grids. Keep the complete transverse
Green expression and full signed D_N,E_N,A_N contractions. A proposed
proof must control kernel tails, boundary-depth dependence and all
internal pairs uniformly, including faces meeting at edges/corners and
both normal endpoints. If scalar difference estimates are used, justify
every mixed difference and boundary specialization. No estimate of
those errors is asserted here. This stronger finite-domain statement
justifies development beyond the existing qualitative proofs; standard
Green or Gaussian theorems should be cited rather than reproved.

Three mechanisms were compared: the existing single-parameter geometric
approximation, a multiscale finite-range decomposition, and the exact
tensor heat-kernel localization just specified. The first has unresolved
effective boundary constants; the second does not automatically commute
with projection or contraction. Start with the third, using the first
as a preserved fallback comparison, without changing the registered
target or claiming the other mechanisms impossible.

### Search record, decision and continuation test

Queries on 2026-10-28 included:

- `Brydges Guadagni Mitter finite range decomposition Gaussian processes lattice Green function derivative estimates theorem 1.1 pdf`
- `lattice Green function rectangular domain Dirichlet boundary estimates discrete continuum convergence rate heat kernel`
- `Brydges Mitter convergence continuum finite range lattice covariances 1112.0671 theorem rate`
- `Lawler Limic random walk modern introduction pdf theorem 4.3.1 Green function difference estimates`
- `"lattice gauge" "ground" "compression" boundary perturbation`
- `"Yang Mills" "Dirichlet" "one loop" boundary lattice mass term finite volume`
- `"relative boundary" "Wilson" "covariance" lattice`
- `"lattice Green function" "derivatives" "boundary" rectangle four dimensional`

Search-result leads about continuum half-spaces, scalar smooth-domain
heat kernels or numerical gauge-fermion boundary improvement were not
treated as whole-cube rate theorems. In particular the 2026 *Worldline
images for Yang--Mills theory within boundaries* result remains a
screening lead, not inspected proof coverage or an essential dependency.
Failed exact-term searches establish no novelty. Reuse the current
Clay statement/version check recorded in the complementary-covariance
assessment; this step does not select a different main route.

EXPLORE permits one later proof attempt at exactly TARGET after the
separate approval of this newly completed assessment. Success means a
complete uniform bound on the full ground compression at the requested
rate, with constants and every remainder controlled. A weaker explicit
modulus is a partial result only. A demonstrated slower signed boundary
term would change the rate decision; failure of a crude estimate alone
does not refute it. If the first quantitative localization cannot control
the complete internal sum or boundary strata, save that precise residual
and refine or park this mechanism rather than invoke qualitative limits
again. Other source residues, higher remainders and the interacting
continuum/mass construction remain independent gaps. This source review
uses zero mathematical exploration turns and proves no new estimate.
