# Six-singleton evaluation and antipodal isolated anchors

STEP_ID: 2026-10-11-mca-152-antipodal-isolated-anchor-test

Ready assessment: `literature/2026-10-10-triangle-twelve-recovery-bound.md`,
unchanged EXPLORE target. Main local gap: exclude thirteen additional
triangle recoveries; other patterns, extraction and definitions remain.
Intermediate test: bound simultaneous isolated disjoint-P scalars for
every triangle whose three singleton pairs are antipodal. L066 requires
four such full anchors in a thirteen-additional violation. Continue if a
complete restricted-family bound is below four, or a verified survivor
shows this mechanism insufficient; do not infer a uniform triangle bound.

Scoped duplicate/failure check: L057/L065/L066, the pair and three-row
attempts, and ATTEMPTS/025. The old 56 antipodal assignments chose only
one shared triple each. No complete shared-label sweep is recorded.
The present structured sweep checks every ordered shared triple for
every ordered antipodal-pair assignment, modulo justified subgroup scaling;
it is not another unstructured sample or a formal common-root test.
L060–L064 and their pending audits are not inputs. Reuse the ready
recurrence/Lagrange coverage; no external source refresh is necessary.

Unfinished reasoning saved before implementation: set S(X) to the product
of the six singleton factors, f=f_K, and u_Y=sum_Y f(y)/S'(y),
u_Z=sum_Z f(z)/S'(z). For K disjoint from P, L057's projected scalar
is mu=u_Z/u_Y, independent of P. Put
T_Y(X)=sum_Y f(y)S(X)/[S'(y)(X-y)], and similarly T_Z.
For an eligible isolated scalar, B=T_Z-mu T_Y has degree at most four.
Direct substitution in L057 (6) gives beta_x^Y/c_x=T_Y(x)/f(x),
and likewise for Z, for each x in P. Thus R(x)=B(x)/f(x) gives
p=(1-R(a))/(1+mu), q=-R(b)/mu, r=R(c).
All denominators are nonzero: shared labels avoid S and K, and
mu!=0,-1. The mathematical purpose is efficient evaluation of the
complete restored equations, not treating projected compatibility as
recovery. All zero fourth weights are to remain in the count; E=0 is
omitted only to enlarge it.

Planned bounded certificate: normalize the Y antipodal pair to {1,96}
by subgroup multiplication. There are 7*6=42 ordered Z,W choices,
720 ordered shared triples per choice, and 715 disjoint-P supports per
triple. Save every projected rejection or isolated weight row in a packed
certificate, with a JSON coverage/threshold summary. Independently replay
the original L057 projected and beta equations, then first-four inversion
and all eight moments of every gated row. Scalar sets, rather than support
counts, determine maxima. Both-zero rows are marked but not counted in
this isolated-only test; L066 retains them separately. No mathematical
conclusion is established yet.

## Completed result

[L067](../lemmas/L067-antipodal-triangle-isolated-anchor-bound.md) contains
the full identities, coverage argument, certificate format, reproduction
commands and qualifications. The complete sweep and original-equation
replay agree on every one of 21,621,600 rows, with 15,367,752 all-eight-moment
checks and 3,568,320 zero-weight rows retained. Maximum isolated disjoint-P
scalar count is three against required four. A separately recovered
three-scalar fiber has full weights and original finite parameters 24,40,46.
Thus the mechanism succeeds for all antipodal singleton pairs by L066;
it does not control arbitrary singleton pairs. The full certificate and
complete comparison are saved under `scripts/triangle-recovery/antipodal-*`.

Outcome ADVANCE, RESEARCH, POTENTIALLY_NEW (only the assessment's limited
meaning), actual task calculation. No novelty or global count improvement
is claimed. The next concrete action is critical audit of L067, with a
new REVIEW_REQUIRED assessment requiring separate approval next turn.
Preserve the older sampling stop and pending computational audits.
