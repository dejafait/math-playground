# Rational-three-isogeny eligibility — working record

2026-10-25, step 469. Work only on the prior SPECIALIZE target in
`drafts/literature/2026-10-25-marked-elliptic-three-isogeny-eligibility.md`.
Main gap: primitive positive exclusion in residual Beal signatures.
Intermediate target: a complete rational-root test of the three-division
polynomial on L112's actual short model. A positive result could open
smaller-field isogeny descent for the elliptic summand of L127; a negative
result stops that shortcut without bounding rank.

Inputs checked: L112's actual coefficients and nonsingularity, L127's
ordinary rank identity, ATTEMPTS/050–054, and the supplied prior source
assessment and its recorded duplicate search. No new source review or
general theorem derivation is needed. The rational root theorem and
Cremona III.3.8 p.99 are imported as assessed. Independent gaps include
global arithmetic, local completeness, upper ranks, marked lifts, original
integer recovery and other signatures. Unfinished L108 is preserved.

Test: factor a exactly, verify its prime factors/product, enumerate both
signs and denominators 1,3 in reduced form, evaluate the homogeneous
polynomial exactly and replay through independently organized arithmetic.
Stop before enumeration if full cumulative work exceeds 10000 factor
trial divisions or 200000 candidate inspections/evaluations. All failures
and reruns count; no sieve, backend probe or quartic retuning. Save full
candidate evidence and the cumulative ledger under scripts/pair-genus-two/.
Execution completed with one accounting repair and one complete rerun;
canonical proof and qualifications are in L130. All 3024 reduced
candidates have nonzero residuals and the replay agrees on every entry.
The initial report omitted postprocessing inspections; it is preserved,
and six additional record passes were charged before the rerun. Actual
cumulative work is 84/10000 factor trials and 69552/200000 candidate
work units, with no mathematical failures or cap violation. The
three-isogeny shortcut is closed, without a rank upper bound. Full
evidence: `scripts/pair-genus-two/three-isogeny-eligibility-certificate.json`
and `scripts/pair-genus-two/three-isogeny-eligibility-ledger.json`.
A different genus-two involution target is submitted as REVIEW_REQUIRED;
no mathematics for that new target was attempted.
