# Signed phase endpoints — bounded attempt

Prepared STEP_ID: 2026-11-02-localized-logarithmic-research-06.
Reuse the unchanged EXPLORE assessment
`literature/2026-11-02-localized-logarithmic-joint-moment.md` and its
exact paid-arc target. No source refresh or new target is being approved.

Main gap: uniform H-versus-D comparison for arbitrary dense integer
support, with actual-Xi realization and signs independently open.
Intermediate target: control both signed endpoints of L661's census
using c_0(1), c_1(1), then pay their complete spatial Mahler cost and
L658's angular localization. This tests whether the census can defeat
the approved criterion; L651 is downstream motivation only.

Preserve L649's full grid, conjugated angle, common poles, positive
integer residues, normalized means and exact squared-residue D. Here
only specialize to L661's n=6q+3, phase mesh pi, unit residues, and
phi_n(Y_n)=pi*n/6. No inference of symmetry for general families.

Read L649's definitions and inverse-transfer limitation, L657's clearing
and divisor conclusions, L658's full localization argument, L659's
envelope/resonant-census conclusions, L661's complete contour proof,
L651's joint-response conclusions, and the scoped prior endpoint,
monomial and logarithmic failure records. Reuse the supplied primary
source assessment. Existing notebook changes remain untouched.

Test: prove max(|c_0(1)|,|c_1(1)|)>=c exp(-81n/6250) beyond one
onset, with the rest of the signed contour o(|W_(x+iY_n)(1)|).
The first-coefficient Mahler cost is at most log(M-1), not a generic
exponential degree loss. An uncontrolled signed remainder or failure
to compare the full paid expression with D prevents a conclusion.

Unfinished reasoning saved before detailed proof: set h=1/8 and
w_n(y)=W_(x+iy)(1). On the rectangle, with A=1/(d+t), b=t/(U+dt),
the derivative in s of log|w_n(r+is)| is sum[f(b)-f(A)], where
f(c)=c(1+cs)/((1+cs)^2+c^2*r^2). Aim to certify f'>=2/5 and
sum(A-b)>=3n/10, giving upper decay exp(-3ns/25). Lower growth
at most exp(n|s|), together with |S_n(r+is)|<=exp(-6ns/5),
would control both horizontal edges and all vertical tails.

If Y_n tends to Y>0, v=lim phi_n'(Y_n)/n>0 and
p=lim (log w_n)'(Y_n)/n, the right vertical integral divided by
w_n(Y_n) should tend to J=2v integral_R exp(i*p*t)/(1+exp(-2v*t)) dt.
Need prove J!=0 with its complex phase, not infer it from its absolute
integral. Reflection gives the left contribution as minus the conjugate.
The two coefficients should then recover respectively Im(J*w_n(Y_n))
and Im((x+iY_n)*J*w_n(Y_n)). This matrix is nonsingular only because
Y stays positive. These are proposed formulas, not established bounds.

Continue only after complete tail domination, kernel denominators,
orientation, limiting multiplier and full root cost are checked.
No computation or absolute contour cost alone is evidence for H.

## Completed bounded attempt

The full derivation is now canonical in
[L662](../lemmas/L662-signed-phase-endpoint-pair-paid-log-bound.md).
The proposed bounds pass: the horizontal rate is 3/200, larger than
81/6250; the limiting signed multiplier is nonzero; the two endpoint
rows have determinant proportional to Y>0. Paying the full roots and
arc measure gives excess >=9n/50000-5log n-C. This excludes the exact
half-turn census as an all-arcs counterexample beyond an existential
onset. No claim about arbitrary integer support or Xi follows.

The exact script and certificate are
`scripts/one-sided-hankel/signed-phase-endpoint-bounds.py` and its JSON
sibling. All 15 checks and the full comparisons were inspected, with
no failures. Earlier floating-point checks of A^+-b^+ only suggested
the four rational bin bounds; they are not proof evidence. The exact
certificate records those bounds and the required thresholds.

The independent conceptual audit remains open. Its critical issues
are the moving-endpoint dominated limit, the complex multiplier and
left-edge orientation, the two-coefficient inversion, and the full
spatial/logarithmic loss, together with inherited L658/L661 inputs.
Reuse the existing paid-arc assessment unchanged; no new mathematical
scope or ready assessment was created in this turn.
