# Step 182 — released-zero shell calculation in progress

Main gap: arbitrary-center safety at 68 agreements; 67-agreement safety is independent.
Approved target: Test full anchored distance-five shell feasibility at L053's fixed pairs with nonnegative invariant triple coefficients, Boolean repetitions and only forbidden-distance zeros.
Gate: drafts/literature/2026-10-12-five-shell-without-incidence-zero.md, SPECIALIZE, saved before this invocation.
Inputs: L053 fixed rho,p_i; L054 full region/product dictionary; L055 Schur normalization. Preserve ATTEMPTS/035,036,037 and their separate stops.

One bounded attempt: release (2,3), maximize the normalized shell row sum using all 35 nonconstant product inequalities and 21 nonnegative relation contributions. Reconstruct an exact rational witness or dual from a proposed basis; test the constant requirement 4982733184/5. No solver status is evidence.

Represented orbit consistency: if B,C are in the shell of A, their distances from A are both five and their mutual distance is r+q. A different anchor in the unordered triple represents it in a distance-five shell only if r+q=5. In that case all pair-only regions have size r, all private regions have size q=5-r, and common size 63-r; every anchor choice has the same (r,q). For r+q not five there is only one eligible anchor. Interchanging B,C preserves r,q in every case. No distinct relation identifications arise. Verify this dictionary with explicit finite supports and all six permutations.

Continue/park test: a rational witness with row sum at least 4982733184/5 and all modes nonnegative parks the shell alone as an exclusion diagnostic. An exact dual strictly below this requirement excludes the shell without the old incidence zero. Otherwise preserve the precise unresolved finite constraints and report EXPLORATION.

No off-shell or other-anchor PSD, global triple extension, actual-label zeros, extra scalar constraints, full SDP value, uniform useful bound, representing measure or RS realization is claimed. Full Mathlib coverage not checked. This is a local reproduction/specialization of assessed tools, not a novelty claim.

Completed outcome: exact witness and matching dual found after 26 proposed-basis pivots; all 1826 independent checks pass. The full proof and citations are canonical in L056. The attained row sum is twice the fixed Schur requirement. Park shell-only exclusion; no off-shell/global extension was constructed. Next scope is a separate critical audit, pending literature approval in PROGRESS.md.
