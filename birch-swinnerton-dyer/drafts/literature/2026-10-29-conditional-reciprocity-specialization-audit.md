# Source scope for a separate conditional-reciprocity audit

TARGET: Critically audit L130's conditional finite-local specialization, checking the actual coefficient's Q-descent, the common global integral scaling, finite-level local conditions and the passage to the rational Tate pairing.
CHECKED: 2026-10-29
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the unchanged step-540/541 assessment of this conditional mechanism and its duplicate/failure comparison; step 542 applies that coverage without a new discovery search or novelty claim.
SOURCE_EVIDENCE: Rubin, Euler systems, 1999 AWS manuscript, I.2.2 proof, I.3.4 and I.3.6--3.10, I.4.1--4.3, I.5.1/I.5.6, I.6.4/I.6.7 and I.7.3, https://swc-math.github.io/aws/1999/99RubinES.pdf ; Rubin, Euler systems and modular elliptic curves, Section 5, https://swc-math.github.io/aws/1999/99RubinDur.pdf ; Darmon--Fornea, published Mock plectic points, Definition 3.7 and following paragraph, https://www.cambridge.org/core/journals/journal-of-the-institute-of-mathematics-of-jussieu/article/mock-plectic-points/1FB89BA4F920603AEE9D624B3897E876 ; Fornea, Plectic Heegner classes v2, L123's audited construction, https://arxiv.org/html/2603.28327v2 . Inspected ranges and versions remain in drafts/source-notes/2026-10-28-retained-plus-reciprocity-coverage.md.
COMPARISON: The proposed audit uses the same assessed duality mechanism and original L123 hypotheses; it checks L130's applicability argument, not a new arithmetic theorem or an unconditional Selmer assertion.
GAP: A separate conceptual audit must verify that the actual global coefficient, finite local conditions and compatible finite pairings really give the written conditional conclusion; the assumed nonzero rational Kummer localization is still not supplied.
REASON: L130 now contains the covered specialization, so its delicate descent and finite-to-rational transfer need separate scrutiny before reliance; no new mechanism or source scope is approved here.
SCOPE: Only L130 under all original L123 hypotheses and its explicit P with nonzero p-localization; no construction of P, rational Kummer membership of z, nonvanishing, strictness, finite Sha or BSD comparison.

Step 543 (2026-10-29) completes the separate literature-only approval
for this exact audit target. SPECIALIZE is retained. Step 542's
mathematics is preserved and has not been independently audited here.
Ready source coverage is reused from the prior assessment, not inferred
from success of the new proof. No broader target is approved.

The audit should inspect L130 and the relevant L123 descent passages,
then compare the cited primary statements and conventions. The key
threshold is a valid single global rescaling and compatible finite
pairings at every p^n, with all away-p places and the real place
accounted for. In particular, do not substitute unramified finite-level
conditions at bad primes or assume that an integral lift of a rational
finite vector generates the local lattice. Review the normalization
R=res(z_p) without adding another projector factor.

Known theorem hypotheses and cases were read in step 540 and selectively
rechecked in step 542. The published away-p paragraph was retrieved
again to match the integral convention; Rubin's general local statements
suffice for the actual proof over Q. The B.2.4 rationalization is imported
through its explicit use in the inspected I.2.2 proof, not claimed to
have had its appendix proof replayed. L123's source construction and
step-515 audit remain imported premises; L128/L129 are not proof inputs.

Continue only if the conditional statement survives these transfers;
otherwise record the exact failed step and withhold its use. The result
would still leave independent arithmetic gaps. No Mathlib coverage has
been checked. This audit is conceptual, not a creative mechanism.

## Separate source-scope approval, step 543

LITERATURE_REASON: The supervisor requires separate approval of the newly saved audit target; comparison with the now-written L130 is needed to delimit its integral-to-rational and descent checks, without repeating discovery or performing the audit.

Read L130 completely and L123's full-integral/descent passage, and
reused the step-540 source note, step-541 recovery and step-542 history.
The duplicate and failed-route comparison remains applicable: this
target neither revisits the rational-exterior import failure nor uses
the held tower-action comparisons. No new discovery search or novelty
claim is made. Reopened both Rubin primary PDFs successfully; compared
their saved primary extracts at I.2.2's proof, I.3.8(i) with proof,
I.4.1--4.3 with the local orthogonality proof, I.7.2--7.3's statement
and arbitrary-Sigma proof case, and elliptic Section 5 through the
rational exponential/dual-exponential passage. The prior complete
I.7.3 proof coverage is reused, not claimed to have been replayed
in full this turn. Source version and printed page references remain
those recorded above and in the step-540 note.

These sources cover the proposed audit's inputs: I.2.2 invokes B.2.4
for rationalization; I.3.8(i) concerns induced finite conditions without
an unramified hypothesis, whereas (ii)'s unramified identification has
extra hypotheses; I.4.3 treats chosen orthogonal subspaces at p; and
I.7.3 explicitly handles arbitrary finite Sigma. Elliptic Section 5
states rational Kummer self-orthogonality and the exponential description
before its later integral evaluation. That evaluation is outside scope.
These are source comparisons, not verification of L130's application.

The audit must still check L123's imported descent versus the exact
b_K and R; a single global denominator for z and w; conditions at every
bad prime and the real place; and compatibility of the finite pairings
with the integral cup product and its rationalization. The rationalization
citation does not itself audit these transfers. No missing essential
source coverage was identified in this bounded comparison. B.2.4's
appendix proof remains unreplayed; L123/step-515 remains an imported
premise. Mathlib remains not checked.

The main gap is arbitrary rational rank versus analytic order. The
intermediate target is exactly this conditional-specialization audit;
its downstream use is reliance on conditional local membership while
isolating separate arithmetic gaps. Continue only if all listed transfers
hold with the original coefficient normalization; otherwise record the
failed transfer and withhold that use. Approval of scope supplies neither
the assumed nonzero rational Kummer localization nor coefficient
rationality, nonvanishing or strictness. No justified source-covered
creative mechanism supplying those inputs was identified in the reused
material. This required approval adds no mathematical result.
