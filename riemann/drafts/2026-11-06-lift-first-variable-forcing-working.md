# Lift-first four-frequency working record

2026-11-06. Approved target: attempt a lift-first four-frequency
variable-forcing countermodel with full zero-fiber closure and a
negative Green form at mass H. Prior assessment:
`drafts/literature/2026-11-06-lift-first-variable-forcing-green-test.md`.
Main gap: L030-L032/C032a actual-Xi mixed positivity. This screens
the positive-correction implication, not the period bound or RH.

## Initial unfinished candidate (superseded by the correction below)

C868b chooses a=-4 gamma^2, so its actual phase is phi=pi. Set
X=x1-ell, Y=x2-ell. Let p be L869(7)'s even C1 cutoff, and define

    alpha(t) = (p(t)+p(t-12))/2,
    f(t) = (p(t-50)-p(t-38)-p(t-62))/8,
    m(X,Y) = H(1+3 X^2(X-Y)^2).

The candidate forcing, divided by H, is

    m/H + 2 alpha(X) cos(y1) + 4 f(Y) cos(y2)
        + 2 f(X+Y) cos(y1+y2) + 2 f(Y-X) cos(y1-y2).

The fiber coupling is 2f(Y)-f(Y)-f(Y)=0 at y1=pi.
It arises by imposing the trace's tangential condition first.
On |X-Y|<=1, support separation should leave at most one angular
term active, with absolute amplitude <=1. On |X|<=1, alpha=1/2
and the fiber factorization plus a Taylor bound should give the
uncorrected forcing/H >= -33 X^2/16. Elsewhere its lower bound
is -1. The displayed mean correction is intended to cover all
three regions, while equaling H on both prescribed lines.

Write A=G*alpha, V=G*f, G(t)=exp(-|t|)/2. The proposed lift is
the finite profile construction S_n=B_n, q_n=B_n'', r_n=iB_n',
with zero modes S_0=K, q_0=K-m, r_0=0 and
K=H(1+2 A''(0)). This should cancel q,r on the full fiber.
No restriction on the allowable lift class is used; one finite
lift would suffice as an existence witness.

At (X,Y)=(12,50), put kappa_d=(G*p)(d). The proposed exact form is
H(4-7 kappa_0+kappa_12-kappa_24), which would be <-H from
kappa_0>6/7, 0<=kappa_d<=1. These algebra and regularity claims
still require complete written verification. This is not an audit
or a claim of actual-F admissibility.

Continuation inputs: L869 cutoff/Green convention, C869a's
tangential trace reasoning, C868a's closure/profile interface,
C868b's phase selection; all original assumptions of the approved
assessment remain. Actual-F domination, other zeros/diagonal,
K>=-|M|, graph realization and Xi signs remain unresolved.

## Factor-of-two correction during the same bounded attempt

The initial Green-form expansion above is incorrect: each of the
two repeated axis differences contributes -4b, not -8b, and each
diagonal difference contributes +2b, not +4b. The correct form is
4H-4b_(1,0)-4b_(0,1)+2b_(1,1)+2b_(1,-1). Thus the initial
amplitude 1/8 does not supply the claimed negative witness.
Preserve that provisional calculation as rejected, not as evidence.

Use instead beta=6/25, f=beta(p(t-50)-p(t-38)-p(t-62)), and
m=H(1+30 X^2(X-Y)^2), with the same alpha. The refined bounds are
|f|<=6/25, |f'|<=9/25, and Lip(f')<=36/25. For |X|<=1,
the uncorrected forcing/H is >=-(144/5)X^2; support separation
still gives nonnegativity for |X-Y|<=1, and the global lower
bound is -48/25. These bounds would establish h>=0 with the
revised mean and retain both mean identities.

With these amplitudes the corrected exact form is
H(4-(122/25)kappa_0+(14/5)kappa_12-(24/25)kappa_24).
The bounds kappa_0>6/7, 0<=kappa_24, and kappa_12<1/1024
give a strict margin <-H/6. The tail bound follows from
kappa_12<exp(-9)/2 and exp(9)>2^9. The same finite Green lift
still cancels on the entire fiber; its zero mode is unchanged.
These are the revised claims for the canonical full verification,
not a claim of independent audit or actual-F admissibility.
