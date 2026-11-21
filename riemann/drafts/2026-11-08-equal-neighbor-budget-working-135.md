# Step135 — approved finite first-lobe calculation in progress

Target is exactly the saved EXPLORE assessment's J at x=16,y=0.
The gap is actual-Xi all-degree mixed positivity. This finite allocation
can at most test one ingredient of local signed compensation; other
lobes/heights, complete signed remainder and higher mixed signs stay open.
No global Fourier positivity or RH conclusion is licensed.

Read L898, L019/L020 and L312/L036/L037 in full; reuse step133/134's
literature and duplicate/failure comparison. No fresh source search or
cross-notebook theorem input. Existing changes remain untouched.

Calculation plan: put t=(u+v)/2, q=u-v (absolute Jacobian 1).
The unnormalized marginal is
rho(q)=integral_R t^2 K(|t+q/2|)K(|t-q/2|) dt.
Evenness in t permits 2 times the positive-t integral. With b=pi/32,
the numerator is the sum of q integrals on [0,b], [b,3b], [3b,5b]
with weights 1,1,1/2. The first weight includes the symmetric half
of I0. This formula and all errors still need a canonical proof/check.

Use fixed rational lobe parameters so no uncertain endpoint is dropped.
Direct interval boxes are already source-covered; numerical diagnostics
are only for selecting a finite resolution, not proof. Kernel arithmetic
may reuse L037's documented Decimal contracts. Need bound the full theta
and transverse spatial tails, enclose A0(0)>0 and preserve half shares.
U<0 stops universal nonnegative budgets for this allocation; L>0 passes
only this cell; zero-straddling is inconclusive. No automatic sweep.

Nonrigorous numpy diagnostic of this exact cell (not evidence for sign):
unnormalized numerator about -0.000374. Use it only to choose resolution.
For a certified real-box method set h=pi/(64M), t in [ih,(i+1)h],
q in [2jh,2(j+1)h]. All lobe boundaries and reflected seams are covered
by interval inclusion. Precompute head K4 on |[i-j-1,i-j+1]h| and
[(i+j)h,(i+j+2)h]; integrate the separable 2t^2 and signed cosine
weights exactly on each box. Each q box has a fixed cosine sign.
Cut t at pi/2, retain all theta/spatial omissions as symmetric errors.
Normalize using A0=2*(integral_0^infty K)*(integral_0^infty u^2 K).
All these formulas and the resource conservation still require final
canonical documentation, arithmetic replay and scoped validation.

Completed later in this step: the first rigorous M=32 grid encloses J
strictly below zero, with full tails and a positive normalizer. Complete
proof, resource accounting and trust qualifications are canonical in
L904; the full certificate is saved under scripts/theta-marginal/.
No refinement or additional cell was attempted. Stop fixed equal shares;
next changed allocation has REVIEW_REQUIRED coverage. Separate critical
audit of L904 is outstanding. This file preserves the preliminary plan,
not an additional current checkpoint or a second proof.
