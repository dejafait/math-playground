# Critical audit of the fixed two-prime-band coercivity proof

TARGET: Critically audit L933's fixed two-prime-band joint Hardy coercivity proof, including the exact principal map, downward divisor inverse, all cutoff and negative-branch leakage, and uniform comparison with T*log(T)*N^(-1/4)*S.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the unchanged fixed-map tool and duplicate/failure coverage in drafts/literature/2026-11-09-two-prime-band-extraction-test-22.md and drafts/literature/2026-11-09-two-prime-band-joint-extraction-21.md; no additional search, new source inspection, or novelty claim. The proposed task audits the same bands, dictionary, shifts, windows and arbitrary complex-vector class.
SOURCE_EVIDENCE: Reused inspected primary statements: Hughes July2017 Theorem2.2 pp18–19 https://personal.maths.manchester.ac.uk/jm/wiki/uploads/LMS/Hughes-lectures.pdf#page=20 ; Montgomery–Vaughan TheoremG.14 p422 https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=434 ; Tao Notes8 Lemmas2.3/2.6 pp4–6 https://www.math.ucla.edu/~tao/247b.1.07w/notes8.pdf#page=4 ; Rosser–Schoenfeld Theorem5 p70 https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf#page=7 ; DLMF27.5.2–3 https://dlmf.nist.gov/27.5#E3 ; L926's divisor bound https://terrytao.wordpress.com/2008/09/23/the-divisor-bound/ and Schur theorem Section2 p2 https://grafakos.missouri.edu/preprints/multilinear_schur.pdf . Prior proof-case qualifications remain in the reused assessments.
COMPARISON: The sources cover the standard tools, not L933's combined result. The new proof claims a paid coefficient-uniform singular margin; the audit must verify each specialization and every residual contribution without treating that claim as an imported theorem. No differentiation of the Riemann–Siegel error or rapid decay across sharp cutoffs is covered.
GAP: Independently check L933(1)–(30), especially uniqueness and all divisor collisions, the inverse orientation and squared norm, actual alpha_s, near-product smoothness versus far-product endpoint charges, the negative-phase derivative gap, and the simultaneous uniform onset. The actual joint lower norm and the downstream L928 comparison are still unaudited.
REASON: Step25 separately reviewed the saved nomination against L933 and the reused source assessments; SPECIALIZE is ready for exactly the named conceptual audit. No essential source blocker was found. This approves audit scope only, not L933 or any new theorem.
SCOPE: Only L933's stated fixed w, shifts +/-1/log T, N=floor(T^(1/5)), T<=X<=2T and the two original prime bands. Arbitrary moving complex vectors, all cutoff crossings, every branch and the exact Hardy phase must remain. No changed bands, longer dictionary, numerical grid, stronger contraction claim, or signed-Xi assertion.

This continuation record is a nomination, newly written after the bounded
mathematical attempt. The current research used the pre-existing step22
EXPLORE assessment; this record did not authorize that attempt. Separate
approval of the new audit scope is next-turn work under the shared rule.
No independent audit is claimed here and no new source theorem is derived.

The main gap remains L030–L032/C032a actual-Xi mixed positivity.
The immediate intermediate use is to secure the claimed joint lower norm
needed by L928's projection comparison. Even a successful audit supplies
only an unsigned estimate; signed realization and transfer remain open.

Essential mathematical inputs to inspect narrowly are L637 (actual Hardy
normalization, undifferentiated Riemann–Siegel and smooth phase bounds),
L926 (already checked scalar divisor and finite Schur tools), and L928
(the unchanged coefficient class and its charged moment error, used only
after the actual norm is established). L737 is inherited window context,
not an extra theorem needed by the extraction. The candidate conclusion
being audited is L933, not an assumed input. There is no cross-notebook
input and no use of L925/L929/L930/L932 as theorems.

The audit should reconstruct the following load-bearing comparisons
directly from the canonical proof rather than from its overview:

- Distinct (p,m) give distinct outputs; every resonant product is below
  the actual cutoff; alpha_s is retained with a justified lower modulus.
- Both prime bands jointly control both coefficient channels. The
  downward divisor inverse must have the displayed row/column orientation
  and a squared, not unsquared, N^(1/8) bound.
- All off-products with j*n<=2H receive smooth estimates only after
  cutoff inactivity is proved. Every complementary positive term and
  the entire negative branch retain their internal endpoint charge.
- The full undifferentiated remainder is controlled homogeneously in S;
  no estimate is merely entrywise before a missing dimension factor.
- The principal/residual comparison implies the required scale at one
  common onset for every X and moving vector. L928's main-form conclusion
  must be downstream, without assuming its previously missing margin.

Continue with the retained lower norm only if these checks pass. If one
fails, correct L933 within the same scope or record the precise failed
inequality and its implication. A losing upper bound is not a negative
eigenvector. Do not reopen the earlier termwise-Schur or inverse-polynomial
routes merely to fill a gap. Full matching Mathlib coverage remains
unchecked. Proposed purpose is proof_audit/conceptual_audit: interacting
phases, cutoff endpoints and collective inverse control require analytic
scrutiny, but this is not a complete RH candidate audit.


## Separate continuation approval — step25, 9 November 2026

LITERATURE_REASON: The supervisor requires separate approval of the newly saved audit continuation; reuse the existing primary-tool coverage and compare it with the completed proof, without reopening mathematical discovery.

Completed LITERATURE / NOVELTY_UNCHECKED, outcome STALLED: this is a
required scope approval, not new mathematical evidence or a new source
result. DECISION remains SPECIALIZE. The historical nomination above
is retained; its pending-approval language is superseded by this section.
The unchanged TARGET is now ready for one conceptual proof audit.

Read L933's complete statement and proof (1)–(30) solely to inventory
its imports and audit obligations. Reused the step22/23 assessment and
source-link recovery, the full step22 two-band comparison, and the
finite-conditioning source review. These contain the inspected primary
statements, proof cases, exact URLs and qualifications; no fresh web
search or source reinspection is claimed or needed for unchanged tools.
Read L637's normalization/imports and (19)–(20), L926's standard-input
scope, and L928's hypotheses and charged comparison. No claimed
principal bound, inverse bound or leakage bound was verified this turn.

The source-to-obligation comparison is adequate: Hughes Theorem2.2
covers the undifferentiated real-height expansion, including cutoff
crossings; Montgomery–Vaughan G.14 covers finite separated real
frequencies and arbitrary complex vectors; Rosser–Schoenfeld Theorem5
covers the reciprocal-prime asymptotic; DLMF27.5.2–3 covers finite
inversion; Tao's divisor bound (3) and Grafakos–Torres Section2 cover
the scalar and finite weighted-Schur tools; Tao Notes8 Lemmas2.3/2.6
cover interval boundary terms and smooth full-window decay separately.
Every changed finite-map specialization remains an audit obligation.
The prior exact manuscript overlap for L926 is not coverage of L933's
different downward transform or its two-channel analytic conclusion.

One citation-location issue needs explicit audit attention. L933 item1
calls L637(19)–(20) its smooth phase family. Those equations define a
moment expression and its remainder; the neighboring text instead
refers to L622(7)–(8). Narrowly inspected L622 Section2, (7)–(8),
which states the fixed-order gamma-phase derivative bounds and explains
the analytic-sector/Cauchy argument and balanced phase weights. This
is an inherited local source-scope clarification, not an audit of that
argument or a derivation of L933's eta_s bounds. The future audit must
verify the specialization and correct the canonical citation if valid;
a pointer mismatch alone is not evidence that the coercivity fails.
L622 is reached through L637, with no new cross-notebook input.

Rechecked the conditioning-approval-loop and joint termwise-Schur
attempt records. The former stops repeated finite approvals after a
successful estimate; the latter stops the separate-modulus majorant,
not a full combined extraction. Reuse step22's inverse-polynomial and
other duplicate/failure comparison. These are contrasts, not inputs or
reasons to repeat an exhausted bound. No band, length or grid change.

Continue directly with the exact TARGET; no further unchanged source
approval is justified. Essential inputs remain L637, L926 and L928;
L737 is provenance and L933 is the claim under audit. Inherited L622
phase estimates must be checked where used. Principal separation,
inverse orientation and squared norm, cutoff and negative-branch
charges, homogeneous remainder and common onset all remain unverified.
Retain L933's margin only if the complete audit passes; otherwise
correct the exact error within scope or record the failed inequality.
No theorem or mathematical script was written; PROOF.md and DAG.md
remain unchanged. Mathlib full matching coverage is unchecked. The
main mixed-positivity gap, projection, signed realization and transfer
remain open; no RH candidate or novelty certification is claimed.
