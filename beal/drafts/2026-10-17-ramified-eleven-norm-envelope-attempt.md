# Ramified eleven-adic norm-envelope attempt

Gate: the pre-existing SPECIALIZE assessment
`literature/2026-10-17-ramified-eleven-full-image-on-t.md`; target unchanged.
Main gap: positive primitive integer emptiness. Intermediate test: whether
L088's universal square D/F norm and T's two rational eleven-adic Kummer
conditions force L073's omitted ramified full image. Containment would
retire that condition; an outside envelope tuple stops this sufficient
mechanism only. No global realization is assumed.

Checkpoint before writing the complete proof: fix s²=5, s=4 mod 11,
z²=-11, and embeddings z -> ±r^5/s. In square-class coordinates with
nonsquare unit -1, the norms L/Q11, L/M(+), L/M(-) send (a,b) to
(0,b), (a,b), (a+b,b), respectively. The sign difference is essential.
Writing the two rational Kummer choices as e1,e2, the envelope appears
to have the complete parameterization

    z_alpha=(-1)^(e1+e2+m),
    z_beta=(-1)^b r^m,
    z_gamma=(-1)^(b+e1+e2+m) r^m.

The full image from L073 is expected to be {(1,h,h): h in L*/L*²}.
The tuple e1=1,e2=0,m=b=0 gives (-1,1,-1) outside it, while both
norm equations hold. These calculations need the exact norm-basis,
exceptional-generator and exhaustive-equation checks in the canonical
write-up before being reported as established. No script or global
unit/class search is needed. Existing work and ATTEMPTS/033–039 remain.

Completed: all checkpoint calculations are justified in
[L089](../lemmas/L089-ramified-eleven-norm-envelope-obstruction.md).
The sixteen-element envelope projects to eight classes versus four in
the full subgroup; the displayed unit tuple is outside. Outcome NEGATIVE
for the sufficient certificate only, with no global realization claimed.
ATTEMPTS/040 records the stop. Independent critical review is pending.
