# One-factor origin margin: source assessment2230

TARGET: Test whether G_x(0)-K(0) has a uniform strictly positive rational lower bound for every x in [14,29/2], using C919m's complete sine integral and the actual theta series with both tails; at actual roots justify the resulting local-decrease implication, or record a certified failure or inconclusive bound.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Review2230 searched real-zero Fourier-kernel division, residual monotonicity/curvature, theta sine-transform and endpoint estimates; compared2225/576 and the named historical failures. No inspected exact quantitative origin-margin theorem was found. No novelty inference; source notes: drafts/literature/2026-11-21-root-conditioned-cosine-source-notes-2230.md.
SOURCE_EVIDENCE: Reuse2225/2226 Tuck2006 pp133-135,(1)-(4), https://doi.org/10.1017/S0004972700047511 and Csordas1309.0055v2 Theorem4.1/(4.2),p10, https://arxiv.org/pdf/1309.0055v2 ; reuse accepted C919f/2166 NIST DLMF3.5(ii),(3.5.6)-(3.5.8), https://dlmf.nist.gov/3.5.ii and Strang-Herman CalculusVolume2 Section6.3,Theorem6.7, https://openstax.org/books/calculus-volume-2/pages/6-3-taylor-and-maclaurin-series . Existing C919m ODE/origin identities and C919f tail/arithmetic hypotheses are the local inputs; Spigler's unread theorem is not used.
COMPARISON: The sine theorem proves G_x(0)>0, not the required comparison with K(0). The standard integration/error tools can certify a compact parameter-family integral only after every error, omitted index and spatial tail is charged. C919f's old cosine certificate is not evidence for this different signed margin. The exact remaining quantitative difference is explicit and independently testable.
GAP: Establish or fail to establish a positive infimum of G_x(0)-K(0) over the closed bracket [14,29/2]. No value or margin is known here. If successful, local-decrease consequences at actual roots require a later ODE/continuity argument. This does not establish I_x(u)>0 for all u>0, another factor removal, arbitrary iteration or all-degree mixed positivity.
REASON: A single bounded scalar obstruction test addresses the origin of the nominated decrease problem while retaining the complete signed integral; it avoids assuming global convexity. Standard tools are covered, but no exact matching theorem was identified. Separate next-turn approval is required for this newly written continuation before mathematics.
SCOPE: L018/L019/L058, accepted C919f and audited C919m. Define G_x(0) for all x in the closed bracket by C919m's integral formula; the stronger bracket-wide comparison needs no root identification. Only downstream origin matching uses Xi(x)=0, possible multiplicity, no first-zero/census premise. No parameter enlargement or global-u sweep is approved.

## Bounded test and limitations

The quantity to enclose is exactly the existing C919m expression

    x integral_0^infinity K(t) sin(x*t) dt - K(0).

This is a nominated comparison, not a derived sign. Seek a certified
rational delta>0 uniform in the whole closed x bracket, rather than
positivity at sampled parameters. A finite partition with rigorous
parameter remainders or direct interval enclosures is admissible.
Import Simpson/Taylor as cited above only after verifying the smooth
finite-integrand hypotheses and their uniform derivative bounds.
Reusing C919f's complete tail inequalities requires checking their
domains and factors for this sine integral and for K(0)'s index tail.
The initial half-lobe and all subsequent signed lobes remain included;
there is no replacement by an unsigned positivity estimate.

Record the fixed truncation/panel/parameter settings before the one
test; preserve failed enclosures. If a certificate is implemented, save
all constants, bounds, intervals and failures on disk and print only
the actual lower bound, required threshold0 and certificate paths.
Use the existing CPython/Fraction/libmpdec contracts explicitly if that
backend is reused; do not silently trust a builtin sine or directed exp.
No new mathematical script has been written during this assessment.

Continue on this mechanism only after a paid uniform positive margin
or an informative obstruction. A nonpositive value at a nonroot
refutes only the stronger bracket-wide test. Refuting strict decrease
at an actual root requires a rigorous root-qualified argument; a zero
second derivative alone would also be inconclusive. Failed error
payment is not a counterexample. Do not silently sharpen the root
bracket, assume simplicity or import a first-zero census.

A successful local shape result would only be a step toward the full
u>0 sign. The independent global cosine comparison, second removal,
iteration and actual-Xi mixed-positivity bridge remain unresolved.
This is an ordinary source-informed calculation and local proof
specialization, not a justified central creative mechanism. Mathlib's
full matching coverage is unchecked; no absence claim or cross-notebook
input. This ready assessment is a nomination pending separate approval.
