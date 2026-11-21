# Full-theta recurrence concentration: source gate completed1934

TARGET: Determine whether the full-theta monic recurrence satisfies max_(1<=j<=n) beta_j / sum_(j=1)^n beta_j -> 0, without assuming a recurrence asymptotic.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1934 searched the exact theta recurrence question, Erdos/exponential-weight terminology and the Levin--Lubinsky title; scoped local comparisons and queries are recorded in drafts/literature/2026-11-20-full-theta-concentration-source-notes-1934.md.
SOURCE_EVIDENCE: Levin--Lubinsky, J.Approx.Theory144(2007),260-281, author manuscript16April2006, Definition1.2(a)-(e)/Theorem1.3 pp4-5, https://lubinsky.math.gatech.edu/Research%20papers/LevLub05Apr06.pdf ; Szego, Orthogonal Polynomials,4th ed.(1975),Theorem3.1.2,p39, https://djvu.online/file/Nk6YlVBVuENXs ; exact hypotheses and inspected proof ranges are in source-notes1934.
COMPARISON: The inspected theorem controls model recurrence coefficients relative to their MRS interval; the extremal-norm principle permits a bounded density comparison. Existing C028o/p/w do not supply the exact ratio limit, and the theorem is not yet applied to theta.
GAP: Prove a global degree-independent comparison with the specified smooth model, verify its class hypotheses and model scale bounds, then transfer squared norms and prove the exact maximum-to-sum limit. No actual recurrence asymptotic is assumed or established.
REASON: Essential primary coverage missing at nomination1933 is now available for one bounded specialization attempt. This literature turn approves the unchanged target and specified method only; every new theta/model estimate remains for a separate research turn.
SCOPE: The unchanged even probability dmu_0(x)=K(|x|)dx/(2*M_0), with K from L019, monic p_j, k_j=integral p_j^2 dmu_0 and beta_j=k_j/k_(j-1)>0; n tends through positive integers. No atoms, affine scale or actual-root-reality premise enters this intermediate claim.
COVERED_TARGET: Determine whether the full-theta monic recurrence satisfies max_(1<=j<=n) beta_j / sum_(j=1)^n beta_j -> 0, without assuming a recurrence asymptotic.

## Why this specific input

Attempt1933 kept the full shared Uvarov system and obtained the exact
centered three-residual formula in C028w. Its uniform weights>=1,4,27
show that a vanishing-cost sequence must approach a specified normalized
cubic/quartic pair. They do not determine whether the two-site image
approaches or avoids that pair, and they supply no upper bounds on the
weights. This is the precise unpaid step, not a proved family stop.

The proposed maximum-to-sum limit tests whether the base recurrence
can concentrate its squared off-diagonal size in a few entries. It is
a candidate input for distinguishing a diffuse base contribution from
the effects of two moving atoms. This is a plausible downstream use,
not a theorem transferring the proposed limit to the modified system.
The two-site shape limit, control of its norms and residual rates,
omitted full costs, C028b's H_d=o(d), and actual-Xi positivity all remain
independent obligations. No new parameter family or mass is introduced.

## Required comparison and discriminating test at nomination1933

Nomination1933 required assessing this exact claim before mathematical
work. Review1934 identified a primary theorem for general exponential
weights. Verifying every weight and regularity hypothesis for the
proposed comparison remains a research obligation; the actual theta
density is not identified with the model weight.
The target asks only for the ratio limit, not a full asymptotic formula.
The proposed theorem application still requires its precise applicability
to be proved. Existing finite formulas and T_n->infinity do not suffice.

Continue if source coverage licenses a concrete proof of the ratio
limit or an informative counterexample/obstruction for this exact
weight. A proof of limsup(max beta_j/sum beta_j)>0 would reject this
candidate diffuse-base input. A general positive recurrence example
does not refute the theta claim. An unresolved essential hypothesis
must remain explicit; source review must not derive a new estimate.

The inaccessible1993 mass-point asymptotic lead in source-notes1931
remains parked. This base-only question does not authorize another
access-only retry or importing its unread conclusions. Reuse adequate
coverage1931/1934 instead of repeating its discovery. This nomination
was not ready in1933. The separate review1934 now accepts one attempt
using the primary theorem, smooth comparison weight and extremal norms
specified in source-notes1934. It does not certify any new estimate.

Essential local inputs are L019/L021 for the measure, C028o/p for
recurrence conventions and prior bounds, C028w for the partial cost
reduction, and source-notes1931/1934 for finite and asymptotic source scope. C028a/b
retain the actual coefficient convention and main height gap. No
cross-notebook theorem, numerical certificate or Mathlib matching
coverage is imported; the latter remains unchecked.
