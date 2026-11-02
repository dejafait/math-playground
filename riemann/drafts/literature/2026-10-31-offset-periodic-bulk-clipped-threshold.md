# Constant-offset periodic bulk: source comparison

TARGET: Test whether a constant-offset periodic bulk attains clipped mean at least 1/288 with a strictly interior L586 covariance remainder compatible with L587.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed a bounded search for the exact clipped periodic variational problem, Laguerre/derivative inequalities and prescribed spectral-atom bounds; reused the saved wave/packet and cone comparisons. No inspected theorem decides this family's joint strict-remainder and 1/288 test; queries and read/unread distinctions are recorded below. No novelty inference follows.
SOURCE_EVIDENCE: Reuse approved L586/L587 Fourier, finite-cone and finite-mixture coverage, and the three-wave assessment's inspected Csordas--Escassut sign theorem. Read di Dio--Schmuedgen arXiv:1809.00584v1 Section 3 setup/Definitions 5 and 9, Lemma 22, and Section 10 Definition 74/Proposition 75 with proof and compactness qualification, pp.5--6,11,28--29; this source was already assessed for L579's different target.
COMPARISON: Known results supply the actual function-space cone and atom-bound tools, not the nonlinear clipped threshold or a joint remainder certificate. L576/L577/L579 stop different fixed families; L581/L584 stop an exact law and a discarded-energy budget. None decides the constant-offset family. Matrix positivity and separate maximal-atom bounds do not certify the required joint interior remainder.
GAP: Compute the exact offset-path covariance and clipped mean; certify either a strictly interior remainder with mean at least 1/288 or a rigorous family obstruction. No parameter choice, uniform threshold bound or L587 extension is established here; actual-Xi transfer remains independent.
REASON: Essential source coverage now permits the unchanged bounded mathematical test using imported cone tools and explicit elementary integration. Investigate only the recorded nonlinear comparison and strict residual feasibility; no new lemma, calculation, script or reproof was performed in this literature turn.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target changes moment-feasibility auditing to a quantitative clipping test. This separate source comparison completes that gate; further unchanged-scope literature is unnecessary.
SCOPE: L473's exact six ordinary lag-one jets, Q(v)=(x_0 z_0-y_0^2)_+, and K; fixed smooth periodic h(s)=a+b cos(omega s), 0<b<a and 0<omega<=1/2; L586's actual V and C_I; L585's fixed rare carrier and L587's eventual-ray probability/support requirements.

## Exact proposed test, not a proved construction

Seek fixed parameters a,b,omega in the stated domain for which both

    K-C(h) belongs to int_V C_I,
    (1/P) integral_0^P (h(s)h''(s)-h'(s)^2)_+ ds >= 1/288,
    P=2pi/omega,

hold, where C(h), C_I and V are exactly as in L586. The amplitude
parameters include the possible conic weight of this one whole path.
These are requirements to test, not conclusions of this nomination.
Do not substitute ambient PSD positivity for the residual-cone
condition, or any positive constant for the specified threshold.

The plausible downstream use is a sign-sensitive bulk inside a variant
of L587's bounded periodic law while retaining all 147 tolerances.
A strict residual margin is requested so a later construction can
address the fixed rare covariance; that extension, its probability
normalization, common onset and lower bound must still be justified.
Actual-Xi transfer remains independent, even if this abstract path
test and the subsequent assembly succeed. No RH candidate is proposed.

The constant offset and fixed frequency change the stationary path
family materially. L576 assumes equal amplitudes and independent
uniform frequencies/phases. L577 assumes three equal-amplitude waves.
L579 assumes a first/second-harmonic packet with a uniform frequency
and a single-wave remainder. This nomination keeps all their negative
evidence and does not claim they ruled out arbitrary stationary paths.
L581 concerns an exact corrected law, and L584 an absolute discarded-
energy budget, neither of which is imposed here.

## Nomination's required comparison (completed below)

Reuse the already inspected cone/interior/compression sources rather
than browsing them again unchanged. Search for the exact clipped
periodic variational problem, stronger derivative-moment inequalities,
and finite spectral-moment bounds controlling atoms at zero and at
a fixed frequency. Read primary theorem hypotheses and relevant proof
cases before declaring any usable upper bound or existence theorem.
The current local duplicate check does not establish novelty.

Continue to a separate mathematical attempt only if the comparison
provides an applicable import or a bounded uncovered calculation with
these exact hypotheses. That attempt should certify both an interior
residual and the numerical threshold, or retain a rigorous obstruction
for this family. A positive clipped value without the 1/288 threshold,
a numerical fit, or an unproved cone remainder is not success. If a
uniform bound rules out the threshold, abandon this path family rather
than repeat a parameter adjustment under another name.

Essential inputs are L473 (1)--(2),(6)--(9), L585 (1), audited L586
and L587, with L576/L577/L579 and L581/L584 for failure scope only.
L473's arithmetic proof qualifications and the non-effective carrier
remain. No cross-notebook input is needed. Full matching Mathlib
coverage is unchecked. No clipped integral or new lemma was derived
and no mathematical script was written for this uncovered target.

The nomination's literature gate is completed below. The next turn is
the unchanged bounded mathematical test, not another source comparison.
No creative central-Xi proof attempt is nominated: no actual-Xi transfer
mechanism has been identified, and this finite-family test remains a
quantitative specialization at the surrogate clipping interface.

## Completed source review, 31 October 2026

### Reused coverage and exact applicability

Reuse `2026-10-31-l586-l587-critical-application-audit.md` and its
completed application audits. L586 defines A(u), the actual span V,
the entry-function space E and C_I, and proves their identifications.
The exact references are Blekherman--Fialkow, *The core variety and
representing measures in the truncated moment problem*,
[arXiv:1804.04276v1, Proposition 2.1/Corollary 2.2, pp.5--6](https://arxiv.org/pdf/1804.04276v1#page=6),
and Bayer--Teichmann, *The proof of Tchakaloff's theorem*, Proc. AMS
134 (2006), 3035--3040,
[math/0502473v2, Corollary 2, pp.3--4](https://arxiv.org/pdf/math/0502473v2#page=3).
Strict positivity is on every nonzero nonnegative member of the actual
finite-dimensional function space; finite cubature presupposes an
integrable positive representing measure. Neither criterion is mere
PSD positivity. Fourier normalization, differing finite periods and
zero-frequency generators are covered in audited L586. Their sources
need no reproof. The changed task must still compute its own C(h) and
check its residual functional, including the zero mode and lag-one
entries. No such calculation is supplied by this review.

The source hypotheses in L587 remain adequate for the proposed later
assembly, but its present theorem has no clipped lower bound. Keeping
the offset bulk would require a separately justified extension with
probability normalization, fixed dictionaries, support, fourth costs
and one eventual real-height ray. Do not claim this extension from
source scope alone. This step reads only L587's hypotheses, conclusion
and fixed-dictionary construction, not its full unchanged audit again.

Reuse `2026-10-31-three-wave-stationary-bulk-review.md` for George
Csordas and Alain Escassut, *The Laguerre inequality and the distribution
of zeros of entire functions*, Ann. Math. Blaise Pascal 12 (2005),
331--345,
[Definitions 1.1/1.2, Theorems 2.1/2.2, pp.331--334](https://www.numdam.org/item/AMBP_2005__12_2_331_0.pdf).
Its first sign theorem assumes Laguerre--Polya membership; its converse
criterion requires all generalized Laguerre inequalities everywhere.
Neither premise is available for the proposed offset family. It is
therefore not an unconditional derivative inequality deciding this
clipped statistic. No real-zero or RH-equivalent premise is imported.
The same assessment's random-walk densities concern different joint
data and supply no frequency-weighted derivative conclusion here.

### Prescribed-atom bound: inspected primary result, not a joint test

Philipp J. di Dio and Konrad Schmuedgen, *The multidimensional truncated
Moment Problem: The Moment Cone*,
[arXiv:1809.00584v1, 3 September 2018](https://arxiv.org/pdf/1809.00584v1),
Section 3 setup/Definitions 5 and 9, pp.5--6; Lemma 22, p.11;
Section 10 Definition 74/Proposition 75 and proof, pp.28--29, were read.
For a pointed moment cone, the supremum removable evaluation mass is
bounded by inf L_s(p) over nonnegative p in the function span with
p(x)=1. Closedness makes these quantities equal, with a maximizing
mass and boundary residual. Compact X, continuous functions and a
strictly positive function in their span ensure closedness/pointedness.
The mass is assigned to an evaluation fibre, not necessarily a singleton.

Reuse its assessment in `2026-10-31-resonant-finite-k-relaxation.md`.
L586's actual E on compact I has continuous entries and contains 1;
use a basis and retain evaluation fibres since A is even. This supplies
no numerical bound, simultaneous sufficiency or strict joint remainder.
Both removed components still require checking together. No optimizer
or clipped integral was derived. Retrieval: v3 returned 404; v1 was
available, leaving no essential access blocker.

### Bounded search and failure comparison

Searches performed on 31 October 2026 included:

- `"Laguerre inequality" "positive part" periodic`;
- `"constant plus cosine" "Laguerre"`;
- `"Laguerre expression" integral inequality periodic`;
- `"Laguerre inequality" "integral" "periodic"`;
- `"truncated moment problem" prescribed atoms interior moment cone`;
- `"moment cone" "maximal mass" "dual"`;
- `"di Dio" "Schmuedgen" "maximal mass" "Theorem"`;
- `"Opial" "second derivative" "periodic" inequality`.

These searched the exact statistic's terminology, stronger derivative
sign/norm results and atom removal in finite moment spaces. Searches
returned general moment-cone work and unrelated Laguerre-polynomial,
Opial boundary-value and Fourier material. Only the primary results
specified above are relied on. The 1703.01497 atoms/core-variety paper
is an already assessed general lead, not a newly inspected deciding
theorem here. No unread abstract, search snippet or absence of hits
establishes a bound or novelty. No matching full Mathlib theorem was
checked; coverage is unknown, not asserted absent.

Read the L576/L577/L579 statements and their specific ATTEMPTS records;
reuse their canonical proofs without replay. Their equal-amplitude
independent-wave or uniform first/second-harmonic packet hypotheses
do not contain this fixed-offset family. Read L581/L584 hypotheses and
conclusions: an exact corrected-law stationarity defect and the
specified actual-Hardy discarded fourth budget do not exclude arbitrary
bounded periodic surrogate laws. Preserve every stop in its scope.
The bounded local comparison found no completed offset-family test.

### Authorized mathematical continuation and limits

DECISION EXPLORE approves exactly TARGET as a separate bounded attempt.
Use L473 (1)--(2),(6)--(9), audited L585 (1), L586 and L587; retain
their arithmetic-source qualifications. The target is unchanged,
including 0<b<a, 0<omega<=1/2 and exactly 1/288. Necessary scalar,
polynomial or matrix bounds may be tested first to seek a uniform
obstruction; positive feasibility requires the actual C_I interior.
Import the stated general results and justify their specialization;
elementary covariance/integral calculation is the missing application,
not a reason to reprove a general moment theorem.

A certified pair of strict residual feasibility and threshold attainment
continues this family to a separately covered assembly extension. A
uniform upper bound below the threshold abandons the family. A fit,
separate atom bounds, PSD matrix, smaller positive constant or interval
straddling 1/288 is inconclusive. Endpoints and limiting parameter
regimes must be controlled for any asserted uniform stop. This review
does not establish either outcome or spend a mathematical exploration
turn. Actual-Hardy nonlinear-law comparison and actual-Xi transfer
remain open even if the surrogate test succeeds; no RH candidate.
