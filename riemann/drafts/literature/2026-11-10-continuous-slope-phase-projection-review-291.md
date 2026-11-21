# Continuous-slope phase projection: source approval in step292

TARGET: Test whether the fixed continuous-slope projection separates the rational quartets of 3/4+i and 7/8+2i in the r=2 moving-band response by its exponential leakage criterion.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step292 separately reviewed the nomination, searched exact moving-band/Laguerre phase-projection terms and stronger uniform bulk and bump-transform results, and compared the narrowly named local reviews/stops below. No inspected theorem decides the specified Pi_n comparison; no novelty inference.
SOURCE_EVIDENCE: Read Vanlessen math/0504604v2 Theorem2.4(b)/(2.13), Remarks2.3/2.5, Proposition3.31/Theorem3.32/(3.100)-(3.110), Proposition5.1 and full Section5.2 pp5-7,32-34,39; Johnson1508.04376v1 Section2 pp2-3 and Section3 p5; Tlas JAT278(2022)105742 unnumbered lemma and full endpoint proof pp2-3; DLMF1.2.8 Table18.3.1,18.15.17-20,2.4.10-16,10.32.10 and10.40.2 with domains. Reuse review285's inspected Gessel diagonal/inversion tools and review288's unchanged reconstruction coverage. Precise links and limitations below.
COMPARISON: Uniform real/complex bulk expansions and analytic error representations cover tools for a bounded assay, while the bump sources cover linear real-frequency endpoint saddles. Neither states the nonlinear complex-phase projection, its complete-quartet cancellation or discrete-degree leakage. Fixed-slope L995 cannot simply be declared uniform in c; a pointwise algebraic remainder cannot be integrated as an exponentially accurate projected remainder.
GAP: Prove the parameter-dependent branch/endpoint representation and projected remainder control, then determine both complete Pi_n scales and the stated discrimination or stop criterion. No Pi_n asymptotic, lower bound, leakage obstruction, actual complement or RH implication is established by this review.
REASON: Essential primary method coverage is now accessible and inspected for the unchanged finite-input target. Approve one future bounded mathematical attempt under EXPLORE; the new work is the exact filter-specific application and cancellation comparison, not a reproof of Laguerre, inversion or saddle-point theory. No essential source-access blocker remains.
LITERATURE_REASON: Varying the upper band slope and taking an n-dependent phase projection introduces a new test family and uniform large-degree limits absent from review288; fixed-slope inverse and BV estimates alone do not cover it.
SCOPE: Exactly the displayed r=2, eta_0=3/4+i, eta_1=7/8+2i, fixed chi and z_0(c), n>=2 assay; retain all four quartet points, both critical branches, all interval endpoints and K_m's -1. A failed proof estimate is inconclusive, not a filter impossibility. No tuning of the fixed inputs or actual infinite-zero/complement claim is covered.

## Exact prospective assay

These are definitions of an unproved test, not additional conclusions
of the completed L996 audit. For eta with 1/2<Re(eta)<1 and
Im(eta)>0 let Q(eta) be the four distinct points eta, conjugate(eta),
1-eta and 1-conjugate(eta), with multiplicity one. Fix

    eta_0=3/4+i, eta_1=7/8+2*i, r=2, m=n+2, n>=2.

They are hypothetical rational inputs, not asserted zeta zeros.
Use L994's exact K_m, and define for 7/4<c<9/4

    a_n(c;eta)=-sum_(omega in Q(eta))
       [integral_m^(c*m) K_m(t)*exp((omega-1)*t)dt
                       -integral_n^(c*n) K_m(t)*exp((omega-1)*t)dt].

All four endpoints and the -1 in K_m remain. Define the explicit
normalizing factor using the following functions, without asserting
a singularity or an asymptotic formula for the c-dependent response:

    w_c=(2-c+i*sqrt(c*(4-c)))/2,
    f_c(w)=w*exp(c*w/(1-w)),
    z_0(c)=exp(-c*(eta_0-1))*f_c(w_c),
    chi(c)=Z^(-1)*exp(-1/(1-16*(c-2)^2)) for |c-2|<1/4,
    chi(c)=0 otherwise, Z=integral_(7/4)^(9/4)
                                  exp(-1/(1-16*(c-2)^2))dc,
    Pi_n(eta)=integral_(7/4)^(9/4) chi(c)*z_0(c)^n*a_n(c;eta)dc.

At c=2 this normalization is motivated by L995's already checked
selected singular point. Its proposed use for varying c remains
unverified and must be included in the source comparison.

The desired discrimination is a nonzero algebraic leading scale
for Pi_n(eta_0), with Pi_n(eta_1)=o(Pi_n(eta_0)). A decisive stop
for this PARTICULAR filter would be a rigorous incompatible
selected scale, or selected root growth at most1 together with
limsup_n |Pi_n(eta_1)|^(1/n)>1. Root growth equal to1 by itself
does not settle the relative little-o test. This is not a request
to tune chi or replace the two quartets after seeing the outcome.
Preserve a failure as evidence about the fixed assay.

## Relevance, coverage and routing

Main gap: actual-Xi positivity L030-L032/C032a and signed forcing
L966/L968. The intermediate question is whether an extra continuous
band parameter can distinguish a selected spectral contribution
before an actual complementary-holomorphy assertion is made. Even
a positive finite assay leaves actual prime endpoint control,
infinitely many zeros, a regulator-uniform remainder, both actual
outputs, L993 recovery and L984(H) unpaid. It is necessary evidence
for pursuing this filter, not evidence of an RH solution. A negative
assay would stop this filter without forbidding other localization.

The nominated source review was required to inspect primary theorem hypotheses for uniform
Laguerre/diagonal asymptotics as c varies, both conjugate critical
branches and all other endpoint terms, followed by Fourier-Laplace
asymptotics with this explicit smooth bump. Check stronger results
and existing obstructions before approving any calculation. Reuse
L994/L995's ready coverage only for their unchanged substatements;
do not assume they prove uniformity in c. Full matching Mathlib
coverage is unchecked and unknown. No cross-notebook input.

If coverage becomes ready, nominate one proof_attempt/creative:
the new mechanism is phase-selective averaging in the band parameter.
Its precise escalation is the possibility that different real growth
rates defeat phase discrimination even for these two quartets; the
bounded test is the displayed Pi_n comparison. A successful bound
could justify a later actual spectral localization test; a rigorous
leakage obstruction would rule out this proposed mechanism early.
Do not invoke that mathematical attempt during source approval.

### Historical nomination boundary — step291

The step291 task remained only the L996 conceptual audit. Apart from
the test definitions, no representation or asymptotic for Pi_n, limit,
lemma, mathematical script, source approval or claimed novelty was
produced for this nomination. Stops214/244/
279/284/285 and unfinished inverse271 remain intact.

## Separate source approval — step292, 10 November 2026

This completes the literature-only action required by the supplied
REVIEW_REQUIRED nomination. All displayed assay definitions and the
exact TARGET are preserved. No coefficient, critical-value identity,
asymptotic for Pi_n, mathematical script or new lemma was derived.
The existing Gessel coverage is reused; no general inversion theorem
is reproved. EXPLORE approves an attempt, not its desired conclusion
or originality. These same sources need no repeated approval if the
target and assumptions remain unchanged.

### Primary contracts and application boundaries

1. **Uniform Laguerre input.** M. Vanlessen, *Strong asymptotics of
   Laguerre-type orthogonal polynomials and applications in random
   matrix theory*, [math/0504604v2, 29 August 2005](https://arxiv.org/pdf/math/0504604v2),
   Theorem2.4(b)/(2.13), printed pp5-6, treats orthonormal polynomials
   for x^alpha exp(-Q(x)), alpha>-1, Q a real polynomial with
   positive leading coefficient. It is uniform on B_delta for
   allowed fixed delta. Remark2.5 pp6-7 specifies upper boundary
   values and conjugation. Proposition5.1/(5.5)-(5.6), p39, retains
   both exponential branches. Proposition3.31/Theorem3.32 pp32-34
   give an analytic error matrix off the reduced contour, uniformly
   I+O(1/d), with an asymptotic expansion. These include the full
   Section5.2 bulk proof, not just its theorem statement.

   Applicability: Q(x)=x, alpha=2, degree d=m-1=n+1; Remark2.3
   gives the monomial scaling, here 4d. Real t/d stays in a compact
   subset of (0,4) for large n. Complex contour inclusion and
   shifted endpoint amplitudes still require proof. The theorem
   gives no exponentially accurate projected relative error.

2. **Normalization and real-domain check.** [DLMF Table18.3.1](https://dlmf.nist.gov/18.3#T1)
   gives norm squared Gamma(d+alpha+1)/d! and leading coefficient
   (-1)^d/d! for L_d^(alpha), alpha>-1. It fixes the conversion
   to positive-leading orthonormal polynomials; do not suppress
   that sign. [DLMF18.15.17-20](https://dlmf.nist.gov/18.15#iv),
   version1.2.8, released15 September2026, gives fixed-alpha,
   fixed-truncation Bessel expansions at argument nu*x,
   nu=4d+2alpha+2, with envelope errors uniform on 0<=x<=1-delta.
   Alpha=2 covers the real bulk range. Formula18.15.14 instead
   holds on fixed-argument compact intervals and cannot cover
   t of order d. No complex-error continuation follows merely
   from the real O symbol; use the stronger input above.

3. **Exact bump model.** S. G. Johnson,
   [*Saddle-point integration of C-infinity bump functions*,
   1508.04376v1](https://arxiv.org/pdf/1508.04376v1),
   Section2 pp2-3 retains the complex Gaussian prefactor and
   both endpoints for exp(-1/(1-x^2)) at real large frequency.
   Its envelope has scale k^(-3/4) exp(-sqrt(k)); the transform
   oscillates and gives no positive lower bound. Section3 p5
   treats generalized bumps, and the opening mentions analytic
   multipliers. This is not a theorem or uniform error estimate
   for our n-dependent nonlinear complex phase. The change
   x=4(c-2) identifies chi's bump up to fixed normalization and
   interval change; it supplies no formula for either Pi_n.

4. **Published stronger comparison.** T. Tlas,
   [*Bump functions with monotone Fourier transforms satisfying decay
   bounds*, J. Approx. Theory278(2022),105742](https://scholarworks.aub.edu.lb/server/api/core/bitstreams/54c4c8f0-46bc-49f6-a174-05f4c16c255c/content),
   unnumbered lemma and full proof pp2-3, treats
   exp(-B/(1-x)^A-B/(1+x)^A) on |x|<1, A,B>0, Fourier convention
   exp(-2*pi*i*xi*x). A=1,B=1/2 is the present bump. The proof
   retains both endpoints and rescales the endpoint saddle;
   footnote2 notes the parameter-dependent contour and amplitude.
   Its cosine shorthand gives no lower bound near its zeros;
   do not discard the complex Gaussian phase or infer a relative
   asymptotic at cancellations. The main theorem constructs a
   different function with monotone transform, so does not permit
   replacing fixed chi. Neither statement settles nonlinear phase,
   complex frequency or this discrete n sequence.

5. **Analytic saddle tools.** [DLMF2.4(iii)-(iv)](https://dlmf.nist.gov/2.4#iii),
   equations2.4.10-16, requires analytic phase/amplitude on an
   admissible path, local expansions with Re(lambda)>0, mu>0,
   p_0!=0, absolute uniform endpoint convergence and strict
   real-part separation away from the relevant endpoint/saddle.
   The large parameter lies in a sector of width<pi. At a simple
   interior saddle p'=0,p''!=0, the coefficient uses
   q/(2p'')^(1/2), with branch fixed by the path. Import these
   standard tools, checking their hypotheses. The bump's essential
   endpoint singularities do not satisfy the unrescaled
   algebraic-endpoint assumptions. Rescaling, n-dependent amplitude
   control and excluded-contour bounds remain mathematical work.

   [DLMF10.32.10](https://dlmf.nist.gov/10.32.E10) is an optional
   endpoint model: K_nu(z)=(z/2)^nu/2 times the integral of
   exp(-t-z^2/(4t))*t^(-nu-1) on (0,infinity), |arg z|<pi/4.
   [DLMF10.40.2](https://dlmf.nist.gov/10.40.E2) gives its
   fixed-order large-z expansion sqrt(pi/(2z))*exp(-z) times an
   inverse-power series, |arg z|<=3*pi/2-delta. The integral's
   smaller sector cannot be enlarged just by citing the expansion.
   No Pi_n substitution or contour rotation is established here.

### Discovery, duplicates and access

Queries included `Laguerre polynomials Plancherel Rotach uniform
asymptotics oscillatory interval 0 4 n c`, `Fourier transform bump
function exp -1/(1-x^2) asymptotic Johnson saddle point`,
`Vanlessen strong asymptotics Laguerre type orthogonal polynomials
theorem 2.4 bulk`, `Laguerre phase projection asymptotic`,
`Laguerre bump Laplace asymptotic`, `Laguerre moving band asymptotic
quartet`, `Laguerre compactly supported complex phase asymptotics`,
and the exact Tlas title. No inspected result decides this fixed
two-quartet comparison. Search failure establishes no originality.

Local comparison used L994's exact kernel/coefficient definitions,
L995's inverse formula and full fixed-c=2 response, review285's
ready Gessel/residue coverage, and the supplied L996 audit.
Searches for continuous slopes, phase selection, Fourier-Laplace
and the source names found no matching assessment beyond review291.
The initial local search returned excessive unrelated output;
subsequent reads were narrowed to the named relevant records.
No sibling notebook was read; unfinished work was preserved.

Review214's ordinate-replacement/full-Li warning, review244's
proper-power scope, review279's small-disk interface boundary,
stop284's repeated-approval closure and stop285's unpaid actual
complement remain. This hypothetical finite-input test assumes
none of their missing actual sign or complement claims. Ready
source tools do not automatically reopen those routes.

Dunster-Gil-Segura1705.01190v1 was inspected only in its opening
and Section2 basic error discussion; its full applicability is an
unused lead, not theorem evidence. A search-returned Li-block blog
could not be fetched (502); its snippet is not theorem evidence
and it is not essential to this finite projection. Shell download
failed DNS; web primary text remained accessible. PDF screenshots
returned placeholders and a TeX endpoint was unsupported; neither
counts as inspection. The primary text of the cited hypotheses
and proof cases was inspected. There is no essential source blocker.
Full matching Mathlib coverage is unchecked and unknown.

### Approved bounded continuation

Next is one proof_attempt/creative on the unchanged TARGET. Import
known tools without reproof. Prove a complete representation and
projected error control before using leading terms; retain both
Laguerre branches, all quartet points, all interval endpoints and
the exact subtraction. A c-uniform inverse selection or analytic
remainder assertion must be proved, not borrowed from fixed-c L995.
Finitely many integrations by parts do not provide an exponential
leakage certificate; a summand does not represent the full quartet.

Continue on a proved nonzero algebraic selected scale with
Pi_n(eta_1)=o(Pi_n(eta_0)); stop on the precise incompatible-scale
alternatives above. Equal root growth one, failed bounds or a
numerical preview are inconclusive. Save incomplete reasoning and
its missing estimates. Success would only justify a later actual
localization question; actual prime/complement/regulator control,
infinitely many zeros, both signed outputs, L993 and L984(H)
remain unresolved. No Pi_n asymptotic or leakage result was proved
in this literature-only step.
