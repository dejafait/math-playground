# Full witness denominator — spacing coverage1436

TARGET: Test whether C019y's full real-witness denominator satisfies D<=CBq^2 for all sufficiently large integer d by controlling prime-product spacing of the original grouped J coefficients, retaining the four tapers, shifts and heat factors.
CHECKED: 2026-11-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1436's bounded sparse mean-square, prime-product spacing and variable-coefficient searches, local duplicate checks and stops1407/1408/1431 comparison are recorded in source-review1436. No matching full norm estimate was located; this is not a novelty claim.
SOURCE_EVIDENCE: Reused Montgomery--Vaughan G.16/(G.25)-(G.28), printed pp426-427, https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf ; read Matomaki--Teravainen2207.05038v2 Lemmas3.2-3.4/proofs, PDF pp12-13, https://arxiv.org/html/2207.05038v2 ; followed/read Heath-Brown1808.02947v1 Theorem4, Lemma4 proof, Lemma7 cases and Section4, https://arxiv.org/html/1808.02947v1 . Full hypotheses and exclusions are in source-review1436; source-notes1410's ordinary-moment exclusions remain reused.
COMPARISON: The improved mean-value bound retains a weighted near-neighbor correlation; Hilbert requires actual local spacing. Heath-Brown's general product bound retains eta/max-coefficient costs, and its prime-power bound has fixed prescribed coefficients and further non-diagonal costs. None directly supplies the moving-heat four-taper real norm at Bq^2; D0 is still only the audited resonant scale.
GAP: Bound the complete weighted near-product correlation or local-separation cost for J_(vs)=a_v*c_s, and justify the moving-amplitude and complex-to-real norm steps with all errors <=CBq^2 for absolute C. No such specialization, diagonal dominance or D>=D0 is established by this review.
REASON: Missing theorem comparison is now completed for this bounded target. Available primary statements and relevant proof cases justify one mathematical spacing/amplitude test without inaccessible premises; a direct import is insufficient. Newly completed coverage must receive separate supervisor approval before research.
SCOPE: C019y's original integer-d scales and real witness S=W(A+conjugate A), D=integral_D S^2; original prime set, p<r, c_s, J_(vs)=a_v*c_s and support R=L^4. One absolute C independent of d. No coefficient optimization, new smoothing of the time interval, RH premise, random phases or nonvanishing assumption.

LITERATURE_REASON: New specific lead is a direct bound for the positive witness norm through its prime-product frequency spacing, an independent missing denominator estimate. Existing coverage assesses generic separation tools and the full quotient, but does not settle the sharper sparse-support norm specialization or its known obstructions.

## Original nomination1435 (preserved)

The following records the nomination before review1436. Its requests for
source comparison are discharged by the completed review below; its
mathematical obligations and original target remain unchanged.

### Relevance and bounded test

The main gap remains L030--L032/C032a actual-Xi all-degree positivity.
The negative resonant numerator now has an independent audit, but the
signed full numerator and its actual-P comparison remain unresolved.
A full-denominator upper bound at the resonant scale would remove one
independent obstacle to testing the dual quotient and hence the proposed
paired-moment route. It cannot alone establish the quotient lower bound,
a paired-moment obstruction, root-deficit control or RH.

Essential local inputs are C019y (1) and its definitions of H,W,A,S,J
and full denominator; C019z (1),(2) and audited (3)--(4) identify the
coefficient norm and resonant scale only. The proposed analysis must keep
unordered distinct witness-prime pairs, both shifted phases, every
original tapered coefficient and both own heat times. No estimate for
actual P is an input or conclusion. C019y retains the exact off-diagonal
and nonconjugate denominator terms; they cannot be deleted by invoking
the positive total norm.

The source review should compare prime-product support with the precise
hypotheses and losses of sparse mean-square/spacing results, starting
from the reused separation statements. Retrieve exact theorem hypotheses
and relevant proof cases before reading broad source passages. Assess
whether a bound for the associated positive complex norm can dominate
the real witness norm at the stated scale while preserving variable
amplitudes. No such reduction is taken as an established estimate here.

The mathematical continuation, only after ready coverage and separate
approval, should test one explicit weighted spacing bound. Continue
only if its complete error is bounded by an absolute multiple of Bq^2,
or a precise obstruction identifies why that proposed bound cannot
reach the threshold. A bound with an unbounded power or logarithmic
loss is insufficient. A failure of an absolute spacing estimate would
stop that estimate, not disprove the denominator bound or RH.

Stops1407/1408 prohibit unpaid variation and diagonal budgets, and
stops1415/1416 prohibit transferring selected numerator signs to the
whole form. Stop1431 retains three exhausted mathematical explorations
for signed joint-divisor completion. This nomination does not reset or
reopen it. It also does not claim the denominator mechanism is novel:
the new target needs its own literature comparison. No justified new
creative mechanism for the central positivity gap is yet available;
source review must determine whether this independent norm test offers
a substantive development beyond generic separated-frequency bounds.
Full matching Mathlib coverage is unchecked.

## Completed review1436

See [the full source comparison](2026-11-18-jensen-full-denominator-spacing-source-review-1436.md)
for exact theorem hypotheses, versions, proof cases, actual queries,
access outcomes and remaining specialization obligations. The closest
inspected tool is Matomäki--Teräväinen Lemma 3.3: it replaces a generic
length loss with a sum of absolute weighted correlations of neighboring
coefficients. That sum, including unequal products, is the quantitative
task; a global support count does not evaluate it. Montgomery--Vaughan
G.16 offers a local-gap alternative. Both still require a paid treatment
of a_v(Y). Heath-Brown 4(iv)'s prime-power structure is relevant but
does not automatically preserve our distinct-pair heat coefficients and
four-taper coefficient norm. No source is rederived or specialized here.

EXPLORE authorizes only the unchanged denominator test after separate
coverage approval. Keep original C019y (1),(3)--(5) and C019z (2)--(4),
including audits1421/1433/1435. Pay the full real norm or a justified
dominating complex norm with every amplitude/separation cost. Retain
the absolute-C threshold and distinguish an oversized upper bound from
a proved obstruction. Signed numerator completion1431 stays parked;
actual-P error, full signed numerator and Xi transfer remain unresolved.
Outcome EXPLORATION is source comparison only, not a new norm estimate
or informative mathematical negative. Full matching Mathlib coverage
is unchecked. This target is established-tool development, not a new
creative mechanism at the central positivity gap.
