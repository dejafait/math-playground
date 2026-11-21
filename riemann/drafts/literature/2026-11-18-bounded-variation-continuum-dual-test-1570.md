# Bounded-variation continuum dual test1570

TARGET: Seek a certified q in C032q's cone using w in {1/4,1/2,1,2,i/4,i/2,i,2i} and Laplace parameters {1/16,1/4,1,4}, with ||1+q||_infinity<1/2 on [1,2], to test the total-variation-at-most-2 class.
CHECKED: 2026-11-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded discovery1570 compared three mechanisms, searched continuum signed-measure/TV dual certificates and rigorous discretization, and checked C032l/stop1302, stops1534/1536/1538/1546/1564/1566 and notes1532/1551/1552/1562/1565/1567. Queries and actual inspected coverage are recorded in drafts/literature/2026-11-18-continuum-discovery-source-notes-1570.md; no exact-family certificate or matching bound was found, which establishes no novelty.
SOURCE_EVIDENCE: C032q already proves the signed norm pairing, full cancellation constraints and positive bounded-test interface; C032m supplies uniform entire lifts and Gaussian envelopes. Tang-Bhaskar-Recht, Sparse Recovery Over Continuous Dictionaries—Just Discretize, author manuscript SectionsII/III equations(2),(5),(10), A1/A2 and complete Theorems1/2 proofs pp1-3 https://people.eecs.berkeley.edu/~brecht/papers/2013_JustDiscretize_v4.pdf cover fixed finite-dimensional signed-TV models, not the actual data or effective errors. Reuse C032m's Haslinger2.39 and C032q's Riesz/separation coverage without reproof. No optimizer-convergence theorem or unaudited C032n identity is imported.
COMPARISON: This is a uniform necessary-constraint certificate for continuum width measures with prescribed variation budget2, not a finite-width cancellation attempt or a full feasibility criterion. C032q already explains why a fixed residual cannot decide arbitrary variation. Generic convergence, sparse minimizer uniqueness and the scalar one-jump bound do not produce the proposed q.
GAP: Find rational coefficients and complete uniform enclosures meeting residual<1/2, or record a certified finite-dictionary obstruction or the specific unattained error bound. No certificate, density, output sign, continuum witness or unrestricted infeasibility is currently established.
REASON: An actual bounded-error test is independently checkable and can quantify one necessary variation cost for continuum cancellation/positive output; it avoids another criterion audit. This is ordinary calculation/development, with no justified creative all-order mechanism. Separate next-turn approval precedes the attempt.
SCOPE: W=[1,2], X=[0,infinity), eta real finite signed Borel with mass1 and |eta|(W)<=2, including arbitrary atoms and singular parts, C032q's full J_eta=0 and nu_eta>=0, and all C032j/m/q actual-divisor/multiplicity/zero-ordinate/strip/counting/finite-zero/heat/fixed-v1 qualifications. The width measure is never restricted to a numerical grid.

## Exact proposed certificate

Use C032m/q's existing kappa_w(sigma)=exp(-E_sigma(w))*sinh(O_sigma(w))
and b_sigma. The dictionary consists only of Re(kappa_w), Im(kappa_w)
at the eight displayed w, and

    L_sigma(s)=exp(-b_sigma(sqrt(s))),
    s in {1/16,1/4,1,4}, sqrt(s)>0.

Seek q equal to a finite real rational linear combination of those real
odd-kernel functions, plus a nonnegative rational linear combination
of the four L functions. Identically zero dictionary functions may be
omitted; no division by an unverified nonzero value is allowed. The
L terms are precisely T f_s for the bounded nonnegative continuous
tests f_s(u)=exp(-s*u). Thus the proposed form is already within C032q's
cone, without positivity of eta, a Lebesgue density or an unbounded test.
The finite w-list is only a necessary part of full J_eta=0.

The requested numerical threshold is the strict uniform bound
||1+q||_infinity<1/2. Its proposed interpretation uses exactly C032q's
existing finite-variation error bound and nonnegative cone pairing;
check the signs and strictness explicitly in the mathematical attempt.
No new norm inequality or local exclusion theorem is proved here.
Budget2 is a fixed first quantitative test, not an assumption about all
feasible eta. An exclusion would leave variation greater than2 open.

## One bounded attempt and its error obligations

Use one initial solve on sigma=1+j/128, j=0,...,128, and at most one
refinement solve on sigma=1+j/256. These are candidate-generation
grids only. Rationalize a candidate before final validation. Preserve
the signs of all four nonnegative coefficients. Account for coefficient
size multiplying every kernel error; large coefficients are not evidence
of accuracy. Do not claim a grid optimum is a continuum lower bound.

Validate the entire closed interval, endpoints included, by explicit
Gaussian/primitive enclosures based on C032m, with at most4096 width
subintervals. The existing divisor/counting and finite-zero assumptions
must remain visible. Any finite-zero coordinates used require actual
certified input intervals; verification through100 alone does not supply
coordinates. Coarse retained inputs may be insufficient: report that
mathematical error barrier instead of silently inserting numerical zeros.
There is no need to use C032n's unaudited PDE. Direct Gaussian envelopes
or an explicitly justified width modulus may supply the enclosures; a
qualitative continuity assertion or existential counting constant does
not certify the requested residual.

Save full coefficients, interval bounds, tail and rounding allowances,
and every failed inequality in a local certificate. Print only the
actual/required residual, dominant error, failures and artifact paths.
Inspect complete load-bearing values with the shared JSON inspector.

Continue only if the strict uniform bound is certified. Alternatively,
a rigorous lower bound >=1/2 for this fixed dictionary is an informative
stop for this dictionary, not for the full cone. If neither bound is
certified within the stated solve/validation scope, record the remaining
error and stop as inconclusive. No automatic new w-values, more widths,
higher local odd jets or increased variation budget follows from failure.
A successful certificate still needs a later independent audit.

## Downstream use and unresolved inputs

This could measure a necessary total-variation cost of a continuum
positive-output annihilator, a step beyond merely restating C032q's
alternative. To exclude all finite variation by this type of argument
would require certified residuals tending to zero; no decay mechanism
is supplied. To establish feasibility instead requires an actual finite
signed eta with full cancellation and positive output. Unsmoothed Xi
realization, H_d=o(d), S_F=0 and actual all-degree positivity remain open.

Essential established interfaces are C032j/m/q, with C032t/u/v and
C032l/stop1302 as comparisons and stops, not additional assumptions.
Calculation1564's counting/tail estimates may be reused only within
their stated ranges; extending an endpoint bound to all widths is part
of the proposed mathematical work. Sources already cover the general
norm/kernel tools. The unpaid tasks are actual enclosures and data,
not another literature search for generic separation. Full matching
Mathlib coverage remains unchecked and unknown. No lemma, program or
actual certificate was written during this literature-only review.
