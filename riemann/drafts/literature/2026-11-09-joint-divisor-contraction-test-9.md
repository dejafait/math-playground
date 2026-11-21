# Joint divisor-energy contraction: bounded continuation

TARGET: Test L928(11) by one analytic weighted-Schur estimate in common generalized-Jordan divisor coordinates at N=floor(T^(1/5)), retaining both full diagonal logarithmic forms and the exact Hardy phase.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed source comparison in drafts/literature/2026-11-09-joint-divisor-contraction-scope-8.md, including its exact complex-factorization/block-norm searches, primary statement/proof-case reads and recorded failure comparisons. No matching joint contraction theorem was identified among inspected sources; no originality claim.
SOURCE_EVIDENCE: https://arxiv.org/pdf/1403.5907v2 Section2 Propositions2.3/2.5 pp4-6 (complex incidence factorization); https://assets.press.princeton.edu/chapters/s8445.pdf Bhatia (2007) Propositions1.3.1/1.3.2 and Theorem1.3.3 pp13-14 (finite block criterion); https://grafakos.missouri.edu/preprints/multilinear_schur.pdf Section2 classical Schur theorem p2 (nonnegative kernel, positive weights, sigma-finite spaces). Direct primary statements rechecked in the separate approval below; L928's audited moment imports are unchanged.
COMPARISON: These sources cover finite factorization and a relative operator test, not L928(11). L737 already supplies the full logarithmic diagonal identity; L926 supplies only one-block conditioning. A new simultaneous application must keep the two energies and complex orientations throughout and cannot infer a joint margin from scalar or unscaled row bounds.
GAP: Carry out one common-coordinate analytic norm estimate and compare its actual bound or residual with a fixed strict contraction gap. No representation specific to L928, uniform eta, joint norm lower bound, bump projection or signed realization is established in this assessment.
REASON: New finite-tool coverage supports this one bounded mathematical attempt after separate approval; it does not justify another unchanged source search or a new arithmetic moment proof.
SCOPE: Audited L928 with fixed L637 w,Z, shifts +/-1/log T, N=floor(T^(1/5)), T<=X<=2T, arbitrary moving complex coefficient pairs, exact Hardy phase, both conjugate zeta terms and both full diagonal logarithmic forms. No enlarged length or shift set, source-shift limit, matrix grid, signed transfer or RH conclusion.

Originally prepared for separate approval; that literature-only approval
is completed below on 9 November 2026, step 10. No mathematical
derivation, spectral calculation or general theorem reproof was performed.

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. The intermediate target is the exact sufficient contraction
in L928(11), using the new simultaneous divisor-energy comparison.
Its plausible downstream use is a later fixed-bump joint projection
decision. Signed realization, transfer and all Xi signs remain independent
unresolved requirements even if this intermediate target succeeds.

Use full audited L928, L737's finite (6)-(10) with the step261 audit,
audited L926 and L927, and L637's Hardy convention and fixed weight.
L925 and any cross-notebook result are excluded as mathematical inputs.
The exact integrated diagonals are positive eventually by L928(4);
this is the only established invertibility needed for the finite block
test. No positivity of complex Jordan weights is an assumption.

The one attempt must apply the cited incidence formula to the complex
cross kernel and transport both diagonal energies into a genuinely
common coordinate system. Account for transpose versus adjoint,
coefficient phases, every logarithmic term and the exact time integral.
Generalized-Jordan refers to the arithmetic convolution weights, not
the Jordan canonical form of an operator. Import the cited general
factorization and block theorem; justify only their local application.
Do not create a lemma merely for rewriting a known finite identity.

Seek one weighted-Schur relative estimate for the resulting cross
operator against the two complete diagonal energies. Positive weights
and both weighted sum orientations must be stated and justified. A
coordinate change is generally nonunitary; its Euclidean norm alone is
not the relevant energy comparison. The audited L926 absolute inverse
majorant may be used only within its stated scope. Replacing complex
weights by their moduli must charge the resulting loss. The exact
Hardy phase is retained; deleting it requires a proved operator-scale
error, not an entrywise o(1) assertion.

Continue this mechanism only if the actual relative bound is at most
1-eta for one fixed eta>0 uniformly eventually in T,X and both vectors,
or a quantitatively adequate alternative joint margin survives the
L928(3)-(5) error scale. A partial bound must display its actual size,
its required size and the unresolved operator term. An explicit
unavoidable loss in this selected majorant is a reason to stop that
majorant, not a proof that contraction or the original joint lower
bound is false. Merely expressing the unpaid inequality in new
coordinates supplies no advance. Do not follow an inconclusive bound
with unscaled row estimates, more matrix samples or larger dictionaries.

Preserve the two-shift unpaid-coercivity stop, step226 and the finite
conditioning approval-loop closure. The new analytic common-energy
comparison is the only basis for reopening this intermediate question.
No further attempt is justified without materially new input or an
informative residual obstruction. Save partial reasoning before lengthy
work; report an honest unsuccessful attempt if the comparison remains
unpaid. Mathematical exploration counters are not reset by this review.

This is proof_attempt/development: a difficult finite application within
an established moment route. It is not a central creative Xi-sign
mechanism. The sources give no signed realization premise justifying
that classification. Full matching Mathlib coverage is unchecked;
standard supporting matrix facts are not formal verification of the
joint theorem. No RH candidate or conclusion is proposed.


## Separate source approval and URL recovery — step 10

LITERATURE_REASON: The supervisor reported missing direct source URLs in this ready assessment. This bounded recovery verifies and attaches the three essential primary interfaces; it does not reopen the unchanged moment-source search or invoke mathematics.

All three direct PDFs above were accessible. Reused the completed scope-8
comparison and the L926 conditioning review/audit for searches, overlap
and failures. No new search for an already covered theorem was needed.
The two-shift unpaid-coercivity, step226 and finite approval-loop stops
remain as recorded in scope-8; they do not supply this simultaneous bound.

Mattila v2: read Section2's complex-valued-function and locally finite
lattice hypotheses, incidence-convolution definitions, and Proposition2.5's
complete statement. It gives E D E^T for a meet-closed ordered set.
The divisor lattice and natural prefix fit those algebraic hypotheses,
as already compared in scope-8. This is a transpose identity; it asserts
no positivity of complex convolution weights. The local cross-kernel
application is still work for the approved attempt. Proposition2.3 is
supporting context, not a required extra positivity theorem. The PDF
header identifies v2, 5 November2015, while its cover says 5 July2021.
A screenshot request for p6 timed out; the complete extracted statement
and definitions were accessible, so this is not essential missing coverage.

Bhatia: read pp12-14's finite complex Hilbert-space/operator-norm setup,
Proposition1.3.1 and its SVD proof, Proposition1.3.2's positive-definite
congruence proof, and both proofs of Theorem1.3.3. For strictly positive
A,B and arbitrary complex V, the positive block with off-diagonals V,V*
is equivalent to A >= V B^(-1) V*, or relative operator norm <=1.
Only the nonsingular case is needed, using the audited L928(4) diagonals;
no singular-case continuity argument is imported. This source supplies
neither a strict margin nor the specific common-coordinate representation.

Grafakos--Torres: read Section2's full classical theorem (a)-(c),
including its preceding measure/kernel hypotheses. It assumes a
nonnegative kernel on sigma-finite measure spaces and 1<p<infinity.
Finite counting measure with p=2 is within scope. Condition(c) requires
positive finite functions on both spaces and both transpose-oriented
weighted inequalities, for every B>A. The subsequent multilinear theorem
is not the imported result. A complex matrix needs an explicitly charged
nonnegative majorant; this source does not justify dropping its phase.
The already audited local finite Schur proof may be reused without a
general theorem reproof.

Approval: retain EXPLORE for exactly TARGET and SCOPE. This repairs the
URL omission and completes the separate approval, with no new mathematical
result, contraction evidence or originality claim. No full Mathlib match
was checked. The next invocation should perform the one saved analytic
test; no further unchanged literature approval is requested. Continue only
on the stated fixed strict margin or an adequate error-scale alternative;
otherwise report the quantitative residual and stop that estimate. The main
Xi positivity gap, downstream projection use, essential local input IDs
and independent unresolved assumptions remain exactly as stated above.
