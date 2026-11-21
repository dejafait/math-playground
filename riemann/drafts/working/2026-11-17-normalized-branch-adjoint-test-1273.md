# Normalized branch adjoint test1273 — working checkpoint

Approved target: the unchanged normalized threshold in review1270,
ready1271. Use C032f's bounded A,B and common compact core; do not
repeat those proofs. Test the specified g=A*(0,exp(-u)) for membership
in ran B*. Nonmembership would force delta=0; membership of one g
would not prove a uniform bound. Main gap and downstream limits are
unchanged: actual-Xi all-degree positivity, source metric, completed
transport, signing, realization and initialization remain open.

Inputs read: C032e/C032f in full, working/stop/history1272, and
review1266's primary transform conventions and hypotheses. The supplied
ready assessment is reused; no new external theorem is being assumed.

Proposed bounded test: analytically continue a hypothetical B*y=g to
the whole real line, justify its bilateral Laplace transform for each
real r>0, and retain both transforms Y_-(r),Y_+(r) of the unknown L2
inputs. With F(r)=integral exp(rt)Psi_ext(t)dt=2Xi(2ir), the anticipated
equation is

    [alpha F(r-1/8)-beta F'(r-1/8)]Y_-(r)
  + [alpha F(r+1/8)-beta F'(r+1/8)]Y_+(r)
    = [F(r+1/8)+F'(r+1/8)]/(r+1),

where alpha=1-c, beta=1+c. This is not yet a proved criterion here.
The key checks are noncompact-input strip domination, absolute Fubini,
the transform signs/scaling, and the actual L2 Laplace-transform class.
A pointwise scalar solution is insufficient. The positive-real axis
is the first discriminating test; common zeros or a violated L2 bound
could obstruct membership. Save any failure without treating it as a
decision on delta. After this second attempt reassess the mechanism.

Completed1273: C032f (12)-(25) contains the full noncompact-input
continuation and exact coupled transform criterion, retaining actual
L2 transforms in both components. The positive-real coefficients have
no common zero and the necessary preimage-norm lower bound is finite;
an infinite bound would have excluded membership. Neither membership
nor delta is decided. Pointwise scalar solutions are not asserted to
be transforms of admissible inputs.

Outcome EXPLORATION, classification REPRODUCTION. No numerical run,
new external source or independent audit. This is the second bounded
mathematical attempt since readiness1271, with no budget reset. Park
the adjoint witness pending a new controlled inverse or separating
obstruction. Next is separately gated central-sign source discovery
in review1273. Preserve the exact-compact and Green-source stops.
