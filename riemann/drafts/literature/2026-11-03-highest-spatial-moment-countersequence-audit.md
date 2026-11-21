# Nominated conceptual audit: highest-moment countersequence

TARGET: Critically audit L682's undisplaced highest-moment countersequence, checking the lattice residue identity, complete angular contour certificate, finite-n charges and original-D normalization.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 76 reused the step-74 exact-family literature comparison and step-72 residue-source scope; searched NIST logarithm series, primary university residue notes and linear-interpolation error; read the primary statements listed below and compared the complete L682 proof against their scope. No new exact-family theorem or novelty claim.
SOURCE_EVIDENCE: NIST DLMF v1.2.8 (2026-09-15), Section 1.10(iv) (1.10.8) with preceding hypotheses, and Section 4.6(i) (4.6.1),(4.6.4); University of Illinois CS450 Spring 2025 Chapter 7 Interpolation, PDF p.14 (zero-based 13), general interpolation remainder and complete linear case. Earlier step-74 Mahler/rational-norm comparison reused as context only.
COMPARISON: The inspected sources supply finite residue calculus, the two logarithm series and the one-dimensional interpolation remainder; they do not establish L682’s family-specific certificate or countersequence. L669/L670/L671 and C681c retain the narrower scopes recorded in step 74 and are not substitutes for this audit.
GAP: Mathematical audit remains open: lattice pole census and residue sign, full angular and spatial coverage, derivative and rounding/tail bounds, moving finite contour, finite-product charges, anchor separation and original-D normalization. Source coverage is sufficient for that audit, not a certification of those applications.
REASON: Separate source gate approves exactly the unchanged TARGET for a later REPRODUCTION conceptual audit under SPECIALIZE. No essential inaccessible source or unspecified asymptotic theorem is needed. No mathematical derivation, certificate replay or lemma/script edit occurs in this literature-only turn.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED required separate approval; the precise interpolation and logarithm inputs had not been source-recorded for this audit. Reuse ready exact-family comparisons rather than repeat broad searches.
SCOPE: Exactly TARGET for L682's e_m=0 sequence inside L666, with n=12q+3, k=M-1, unchanged original D and all angular u. No general-displacement lower bound, H upper bound, support or Xi conclusion is covered by this nomination.

## Preserved step-75 nomination (preapproval state)

The main gap remains actual-Xi all-degree mixed positivity. The result
under review would retire the proposed sufficient highest-coefficient
H certificate; it would not retire the full spatial polynomial route.

Essential local material is the full proof of L682, L666's exact family
and rational continuation, and
`scripts/one-sided-hankel/highest-spatial-contour-certificate.py` with
its complete JSON certificate. The two floating screens are motivation,
not proof inputs. No other notebook result is requested.

The conceptual audit should check the residue -h/(2*pi), the finite
lattice count and separate anchor, analytic continuation in the spatial
variable while u runs over the whole circle, damping on all four edges,
the radial term in the continuum exponent, exact rational rounding and
series tails, the full mesh including s=0 and both semicircles, all
derivative bounds, the A_n-to-r cost, and D>=64/21. It must verify the
strict exponent gaps and that the ratio tends to zero with one fixed
admissible sequence. An aggregate PASS without those hypotheses is
insufficient. A failure requires a documented correction or withdrawal
of the affected claim, preserving evidence; success accepts only this
target-specific stop. General H/support/realization/Xi gaps remain open.

The next source gate should reuse the ready exact-target assessment
and establish whether these standard proof tools are adequately covered
for a separate conceptual audit. Seek additional literature only for an
identified essential missing input. Full matching Mathlib coverage for
the new countersequence remains unchecked, which is not an absence claim.

## Separate source approval — step 76, 3 November 2026

The exact target is ready under SPECIALIZE. This is source coverage for
an independent audit, not an acceptance of L682's mathematical negative.
The main gap is actual-Xi all-degree mixed positivity. The intermediate
purpose is to decide whether the proposed highest-coefficient certificate
must be retired; full H, support and Xi realization remain independent.

### Primary tools and application boundaries

NIST DLMF v1.2.8, released 15 September 2026,
[Section 1.10(iv), (1.10.8)](https://dlmf.nist.gov/1.10#E8),
requires analyticity inside a simple closed contour and continuity up to
its boundary apart from finitely many interior singularities. It gives
the integral divided by 2*pi*i as the sum of interior residues, with the
usual positive orientation. Read the preceding hypotheses and formula;
the cited Copson pp.117–120 proof was not independently inspected.
For L682 Section 2, the later audit must check holomorphy of F_n on the
closed rectangle, all kernel poles and their residues, absence of boundary
poles, orientation and the separate anchor. The finite contour varies with
n; this calls for individual finite applications, not a theorem about an
infinite lattice sum. No Poisson-summation or saddle theorem is imported.

NIST [Section 4.6(i), (4.6.1) and (4.6.4)](https://dlmf.nist.gov/4.6)
gives the principal logarithm series for log(1+z), and the odd-power
series for log z in powers of (z-1)/(z+1). Read both formulas and their
stated domains; only strict interior arguments and positive real scaled
arguments are needed here. L682 Sections 3 and 4 must still justify its
uniform argument clearance, integration of the series, derivatives and
explicit truncation and rounding bounds. General series identities do not
certify the implementation. No boundary convergence case is required.

University of Illinois, CS450 Spring 2025,
[Chapter 7: Interpolation](https://relate.cs.illinois.edu/course/cs450-s25/file-version/9b3a009d3abd3160be3746d4f083e6fe166b6f54/pdfs/cs450_s25_chap07l_300dpi.pdf),
PDF p.14, slide “Error for Global Polynomial Interpolant”: read the
C^n hypothesis, n-node remainder, and its complete n=2 specialization.
For a real C^2 function on the interpolation interval, the linear error
is at most M*h^2/8, M=max|f''|. This covers the one-dimensional tool
invoked in L682 Section 3. Its successive application, convex endpoint
weights, both semicircles, derivative bounds and split at s=0 remain
mathematical audit obligations. The PDF text clearly exposes the formula
and hypotheses; screenshot retrieval timed out and supplies no evidence.
No unread proof is represented as inspected.

The general named results are imported by citation; there is no reason
to reprove them. L682's clearance bounds, exact finite sums, interpolation
charges and asymptotic comparison are the identified specialization to
be audited. No new conclusion is derived here. Full matching Mathlib
coverage remains unchecked; the supporting Mahler names in L682 do not
formalize this contour argument.

### Reuse, failures and bounded decision

Reused the full step-74 displaced-highest-spatial-moment assessment and
step-72 positive-blend audit source scope. Read L682 in full, L666's
family/admissibility and rational-continuation sections, step-75 history,
the targeted highest-moment working-record matches and its ATTEMPTS
record; the script header/log/series routines were read only to identify
source needs. No certificate was run or accepted. Step 74 already
compares exact rational observation, rational norm estimates and power
sums with original D. Refreshing those unaffected comparisons would not
help this audit. Their preserved manuscript qualifications stay intact.
The historical fixed-angle, clearing and auxiliary-blend stops do not
establish a full-circle original-unit-residue stop.

Search queries: “site.nist.gov DLMF logarithm power series 4.6.1”,
“site.math.mit.edu residue theorem simple closed contour complex analysis
notes”, and “site.math.umd.edu linear interpolation error second derivative
h squared 8”. Search leads beyond the inspected sources are not inputs;
no failed search establishes novelty. The prior exact-family discovery
search is reused, not replaced by these standard-tool queries.

Continuation inputs are L682, L666's definitions and rational formula,
and the complete highest-spatial-contour-certificate.py and JSON. The
next turn must inspect the full load-bearing evidence, rather than an
aggregate PASS or a preview. Continue retaining the target-specific stop
only if all contour hypotheses and finite errors verify the uniform
bound and normalized-ratio limit for the same e_m=0 sequence. Otherwise
correct or withdraw the affected claim while preserving evidence. No
broader H or RH stop follows. This approval changes source readiness,
not mathematical truth; creative discovery is deferred for this one
necessary conceptual audit, with no renewed calculation budget.
