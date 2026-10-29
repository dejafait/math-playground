# Step 495 — coupled factor proof working record

2026-10-25. Approved target and source scope are the unchanged SPECIALIZE
assessment `drafts/literature/2026-10-25-two-additional-row-factor-compatibility-review.md`.
Task: RESEARCH / REPRODUCTION / proof_attempt. Main gap: uniform twelve-row
compatibility. Bounded target: two additional rows on the same C155a factors.
Useful downstream output: joint-image obstructions before further row gates.

Inputs read: audited L156 and C155a statement, L109 actual maps/recovery
conditions; inherited L155/L153 qualifications. Existing unfinished changes
are preserved. Assessment's duplicate comparison is reused; ATTEMPTS/041–043,
/048–049 read directly. No rank-only exclusion or certificate replay planned.

Working construction, not yet a proved result: stack the actual c,d maps
on each factor Z=A,B into F_Z:Z -> T_c direct-sum T_d. For proposed image
lines choose normalized nonzero t_c,t_d. Let e_c=(t_c,0),e_d=(0,t_d).
Choose each row's active factors, one or both. For a factor active twice,
normalize its c-image to t_c; its d-image is lambda*t_d, lambda nonzero.
The shared-lift condition is [e_c]+lambda*[e_d]=0 in coker F_Z.
Explicitly solve this one-scalar equation, retaining empty cases; then
all representatives are section(e_c+lambda*e_d)+ker F_Z. For one active
row require its padded vector in im F_Z; for no active rows use P(ker F_Z).
This couples the two rows through the stacked image, not independent lifts.

Continuation test: prove exhaustiveness, uniqueness after normalization,
all nine active-factor patterns, zero restrictions and E-rationality, with
explicit scalar sets rather than implicit equations. Abandon as incomplete
if any shared-scaling branch cannot be resolved. No census, solver, coding
gate removal, global product assertion or radius claim is authorized.

Completed: the construction is proved in L157, including all nine
strata, the explicit scalar trichotomy, joint coset reconstruction and
its unique inverse. Manual checks included every active-set table entry,
u=0/v nonzero (reject lambda=0), v=0/u nonzero (empty), zero joint
kernels, zero restrictions and inactive-factor projective charts.
No independent finite-input audit or numerical evidence was used.
This is a local ADVANCE / REPRODUCTION, awaiting separate critical review;
no quadruple is evaluated or excluded and no radius changes. The next
audit scope is proposed as REVIEW_REQUIRED, not self-approved here.
