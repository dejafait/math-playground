# L912 conceptual audit — step168 working record

Exact approved target: critically audit L912's positive full-cut certificate,
including full-kernel Cauchy remainder, derivative theta tails, weighted
moments, exact accumulator scaling and normalization, without changing the
grid or degree. Reuse the unchanged SPECIALIZE assessment
`literature/2026-11-09-full-cut-quadratic-certificate-audit.md`.

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity. This audit
can establish only an independently reviewed necessary cut sign for L905's
four-demand block; infinite allocation, residual identity, other lobes and
heights, and mixed signs remain open. Success requires the complete analytic
chain and all numerical arrays/cells, with positive final lower endpoint.
A concrete failure requires repair or qualification, not mesh/degree growth.

Read L912 in full; inspected L905's cut/reflection/spatial tail and step139
audit, L312's full derivative tails, L908's k=4W normalization, and L910's
analytic-even series and closed-strip envelope including its prior audit.
The historical whole-box mesh stop is preserved and is method-specific.
Step165/167 primary-source coverage is reused; no source gap was identified.

Analytic checks so far: radius 1/4 lies strictly inside the analytic strip;
c=7pi/8>9/4 makes the reflected global envelope decrease for r>=0.
The Leibniz third-directional remainder is 4*64*121*h^3. Full evenness,
not reflected-head differentiability, supplies the seam and k'(0)=0.
P2, its 147v^4 bound, decreasing n>=5 envelope and geometric ratio give
the printed second-derivative error. The signed moments and six Taylor
coefficients have been checked algebraically. These observations are not
yet acceptance of the numerical certificate.

Planned single replay: recompute every full center jet by order-two formal
series arithmetic (not the printed derivative polynomials); recompute all
moments by centered monomial/series integration with tighter auxiliary
arithmetic; prove containment in every original fixed interval; generate
the bivariate coefficient matrix from (tau+eta/2)^r(tau-eta/2)^s/(r!s!)
and reconstruct every original lobe/term accumulator with exact integers.
The moment series is an independent evaluation of the same moments, not
a change to the degree-two amplitude or grid. Check all complete errors,
source hashes, denominator, rational comparisons and audited positive A0.
Save full evidence under `scripts/theta-marginal/`; preserve step166 files.

First replay: all 5248 center triples and all t moments passed containment.
The new audit implementation used pi*(2j+1)/256 for the q center phase;
the first q-moment check failed. The required phase is pi*(2j+1)/512,
because 16q0=16*(2j+1)h. This was an audit-code error, not evidence against
step166. Preserve both the initial audit script and failure certificate as
`audit_full_cut_initial_phase_error_168.py` and
`full-cut-audit-initial-phase-error-168.json` in `scripts/theta-marginal/`.
Correct this coefficient only and rerun the same audit. Grid and amplitude
degree are unchanged.

Completed replay: all 34647 checks pass; every center and moment interval
is contained, and all 4,718,592 cells give exactly the original thirty
accumulator pairs. The complete raw interval remains strictly inside
(15/10^6,27/10^6); no original certificate repair was required. Full audit
proof and qualifications are canonical in L912; evidence is
`scripts/theta-marginal/full-cut-audit-168.json`. The complete result, error
bounds and generated coefficient matrix were inspected. The normalizer
hash also matches step139's audited M=128 source. No pending computation
remains for this fixed target; the separate signed-tail source nomination
is REVIEW_REQUIRED and was not attempted here.
