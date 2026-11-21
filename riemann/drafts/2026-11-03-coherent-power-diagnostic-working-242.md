# Approved power-profile calculation: working checkpoint

Completed calculation: full proof is canonical in
`lemmas/L733-coherent-power-variance-envelope-prefix-obstruction.md`.
The reasoning below preserves the pre-write checkpoint; the separate
audit remains outstanding.

Target is exactly the prior EXPLORE assessment
`literature/2026-11-03-prime-variance-coherent-power-diagnostic.md`.
No external-source refresh, arithmetic reconstruction or changed profile.

For b=9/10, split the increment integral at y=h. On [0,h],
concavity gives Delta<=h^b; on [h,x], Delta<=b h y^(b-1).
The sum is <=(81/80)h^2 x^(4/5)-(1/80)h^(14/5).
For every fixed c>0 the full cited envelope has positive summand
E_c(x)=exp(-(log x)^(1/3)/(c(log log x)^(1/3))).
The ratio to x h^2 E_c is O(x^(-1/5)/E_c)=o(1), uniformly in h.
The final proof must retain the other summand and quantify this limit.

For exact weights w_j=j/(j+1), write a=1+z and t_j=j^(-1/10).
Completion of the complex square yields minimum C-B^2/A, with
A=sum w_j=N+1-H_(N+1), B=sum j^(9/10)/(j+1),
C=sum j^(4/5)/(j+1). Integral comparison and summable correction give
B=(10/9)N^(9/10)+O(1), C=(5/4)N^(4/5)+O(1), A=N+O(log N).
Thus C-B^2/A=(5/324)N^(4/5)+O(1). Need canonical write-up and review
of constants, all finite N endpoints and complex drift before final.

This is an envelope-only model. It has no Euler product or prime-power
support, and no asserted October-input compatibility. L732 supplies
only the chosen functional's definition; its zero theorem is not used.
The four triangular-family assessments/stops were searched for this
specific profile and envelope; no matching diagnostic was found.
The prior interval assessment supplies exact theorem statement/proof
coverage. No numerical evidence or mathematical script is required.
