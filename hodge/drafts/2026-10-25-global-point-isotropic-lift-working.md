# Step 547 — Actual global point-isotropic lift working record

Invocation-start gate: SPECIALIZE in
`literature/2026-10-25-global-point-quotient-isotropic-lift.md`, supplied
verbatim and reused. Work only on its exact target; no new source search.
Main gap: uniform primitive Hodge realization, including existence of F.
Intermediate target: decide surjectivity of the actual fourfold Serre
null cone to H^0(B,W), retaining L116's trace-adjoint retraction.
Downstream use: test whether scalar isotropy alone can constrain the
point bracket; actual polynomial/geometric compatibility remains separate.
Continue/abandon test: prove every point vector lifts isotropically or
find a vector without a lift; failure to control the actual restriction
must remain a gap rather than being replaced by chosen matrices.

Inputs read: L116 in full; L071 hypotheses/conclusion and character
specialization; L109 hypotheses, actual pairing normalization and trace
adjoint; L164 hypotheses/conclusion; relevant L108/L111 pairing passages.
Duplicate/failure check: ATTEMPTS/068,/077,/080,/092 and step 545's
recorded primary-theorem comparison. No repeated Leray differential,
positivity import or full-section vanishing is attempted. Preserve all
pre-existing uncommitted and unfinished work.

Proposed specialization, not yet separately audited: put K=H^1(B,M),
H=H^2(X,V), U=H^0(B,W), i=H^2(j), R=H^2(r), A=H^2(a).
L116 gives Ri=id and ker A=im i, with A surjective. The actual
adjoint construction of r should give Q(x,iu)=S(Rx,u), where
S=Q restricted along i and is Serre_B composed with b, including the
fixed shift sign. Hence S is nondegenerate and ker R=(im i)^perp.
M=T_B direct sum N ensures dim K>=20; no assumption on t or Z.
For w in U, y=x-iRx is the unique lift with Ry=0. A vector e in K
with S(e,e)!=0 then permits a complex square root c satisfying
c^2 S(e,e)=-Q(y,y), producing y+c i(e). No uniform or polynomial
choice of c is asserted. The remaining work is to write the actual
adjunction/shift sign and normalization precisely and retain vacuous U=0.

Completed bounded test: the full proof and all sign/normalization
qualifications are now in L165. It establishes surjectivity of the
actual Serre null cone onto U and parks scalar-isotropy-only exclusion.
Outcome NEGATIVE / REPRODUCTION; no independent bracket or geometric
compatibility claim. Separate critical audit remains pending. The new
audit assessment is REVIEW_REQUIRED, not approved in this proof turn.
