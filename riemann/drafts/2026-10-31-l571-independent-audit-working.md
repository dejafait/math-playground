# L571 bounded independent replay

Approved target: audit the existing L571 thresholds, exact-order endpoint
functions and conditional Xi rescaling. Prior SPECIALIZE assessment:
`literature/2026-10-31-l571-independent-budget-audit.md` (relative to drafts).
Essential inputs L571 and L018; L463 supplies only the D_n convention.

Main gap: actual-Xi all-degree positivity. Intermediate target: validate
this conditional first-sign budget, without supplying an actual-Xi norm
bound. Downstream use would require that separate quantitative bound at
a nonzero pair center. Continue only if the complete endpoint and
exact-order replay passes; correct or withdraw any failing assertion.

Replay in progress, saved before final documentation:

- B has poles only at +/-i/r. Its circle modulus is one and B(0)=b.
  The quotient b*f/B is analytic across the prescribed zeros and is
  nonzero there exactly when the prescribed orders are exact.
- With real coefficients h=1+u*z+v*z^2+..., the norm identity and
  D_1=u^2-2v-2c hold. Taylor radius >1 justifies Parseval directly.
- For x=u^2, the constrained objective is x+(c-x/2)^2 up to 2c,
  and x thereafter. Completing the square gives the two stated minima.
  The boundary c=1 has the unique solution x=0,v=-1.
- At the equality polynomials, Re h(ir)=1+min(c,1)*q>0.
  Higher-coefficient equality requires all Taylor coefficients >=3 vanish.

Completed: all three exact-norm families give the claimed norm increments
and signs, with positive real part at the prescribed zeros. Xi rescaling
has the positive multiplier R^2/Xi(gamma)^2, even for Xi(gamma)<0.
Full audit evidence and qualifications are canonical in L571, in its
dated independent-audit subsection. No defect or new theorem was found.
No script, external browsing or Xi norm estimate was needed.
