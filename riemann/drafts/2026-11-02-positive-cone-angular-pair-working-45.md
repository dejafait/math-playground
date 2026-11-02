# Symmetric angular-pair factor: bounded attempt, step 45

Invocation-start coverage is the unchanged EXPLORE assessment
`drafts/literature/2026-11-02-displaced-positive-cone-distance.md`.
Work only on its exact cone target. The intermediate target is the
proposed angular-pair interpolation factor, which could improve L673's
nonnegative approximation past rate 1/100 and stop the sufficient
cone-to-Jensen route. Actual-Xi mixed positivity, the unit-residue H
application, support and Xi realization remain independent gaps.

Use L666's full W and L673's exact admissible phase nodes, ell_k,
rho=27/(100*n), c=10*pi/27 and residue remainder. C673c is an unaudited
comparison motivating this refinement, not an assumed obstruction for it.
The earlier gauge/strict-slack/contour stops remain preserved. A targeted
search found this proposed pair only in step 44's continuation, without
an existing derivation. Reuse the adequate source assessment; no new
general theorem or external source is needed for this family-specific test.

Test v=(-99+20i)/101 and its conjugate with

    A_n(z)=[W_(x+z)(v)*W_(x-z)(v)
             *W_(x+z)(conj(v))*W_(x-z)(conj(v))]^(1/4),
    A_n(0)=1,
    g_n(z)=(1-z/rho)*exp(-c*n*z)/A_n(z).

First justify one common analytic nonvanishing branch and positivity
at the imaginary nodes. Then test the necessary positive real crossing
and the band at height 3/20 against exponent -1/100. A rigorous obstruction
at either crossing stops this gauge's uniform absolute-contour criterion;
sampled values alone do not. Pursue a full continuous contour and finite-n
cost only if both necessary tests survive. This does not assume any bound
for kappa_e or a signed integral.

## Reasoning saved before calculation

For a general angle v, write each factor as
(1+beta_j*z)/(1-alpha_j*z), where alpha_j=1/(d+t_j*v)
and beta_j=-t_j/(U*v+d*t_j). For the chosen v and conj(v),
the possible poles of W_(x+z) have real parts at least
d-99/101=109/404>1/4. Its zeros have real parts at most
d-99*U/101<-3/5, for j>0. Reflections supply the opposite
singularities. Thus the central strip |Re z|<1/4 should provide a
simple connected, zero-free common domain enclosing all phase nodes.
The four-factor product is even, invariant under conjugation, and
positive on the imaginary axis, where it equals
|W_(x+i*y)(v)*W_(x-i*y)(v)|^2. Its normalized fourth root should
therefore be positive on that axis. These claims still need the exact
branch and residue applicability argument in any canonical result.

The proposed continuum exponent is

    E_pair(z,u)=F(z,u)
      -[F(z,v)+F(-z,v)+F(z,conj(v))+F(-z,conj(v))]/4
      -c*Re z+K(z).

The floating crossing diagnostic will guide, but cannot certify, a
continuous lower bound. No replacement of finite products by this
exponent is assumed in a norm inequality.

## Completed bounded attempt

Outcome NEGATIVE. The canonical proof is
`lemmas/C673d-angular-pair-real-crossing-stop.md`, which is unaudited.
The normalized fourth root exists on |Re z|<109/404, is positive at
the imaginary nodes, and supplies explicit positive coefficients with
L673's exact Cauchy remainder. Yet every enclosing Jordan contour in
that strip intersected with |x+z|>1 crosses a real s in (0,1/4), where
E_pair(s,-1)>-3/400. The required upper exponent is -1/100. This
stops this gauge's uniform absolute-contour criterion, not the cone or
the signed residual itself. No RH candidate or originality claim results.

The floating screen found minima about -0.006934 on the real crossing
and -0.009901 at height 3/20. Those are not proofs. The certificate
instead encloses 121 real samples exactly and uses the proved |f''|<132
bound on [0,6/25], then monotonicity plus a Lipschitz bound up to 1/4.
The full compact lower bound is -3499760611/500000000000; the remaining
tail is positive. All 18 exact checks passed. The complete summary,
checks and empty failure list were inspected; sample data and all exact
constants are saved in the full certificate. Neither mathematical script
failed; no external source was needed.

Reproduction:

    python3 scripts/one-sided-hankel/positive-cone-angular-pair-screen.py
    python3 scripts/one-sided-hankel/positive-cone-angular-pair-certificate.py

Both write their full JSON siblings. The screen is not a proof input.
The certificate's exact arithmetic routines were reused from step 44,
with a new exponent and real-interval coverage. The canonical proof
includes their analytic formulas and series remainders, independently
of C673c's unaudited crossing conclusion.

Park further angular-even-factor absolute-contour optimization after
the distinct single-angle and paired-angle stops. A materially different
test within the same ready cone target is the signed normalized angular
mean of this explicit paired residual. First derive its exact residue
formula with every factor retained. A certified rate for that mean slower
than exp(-n/100) would stop this explicit witness via its norm-one testing
functional, without an unjustified contour-supremum lower bound. Fast or
zero mean alone would not bound the full norm and would end this scalar
test unless it yields a concrete controlled signed-norm mechanism.

For that continuation use L666, L673 and C673d's displayed coefficients;
recheck the latter's unaudited branch/sign applicability. C673c and the
continued-value u=0 stop are comparisons only. This is the actual Fourier
coefficient on the circle, not rational continuation to u=0 across poles.
No moment noncancellation, Gram eigenvalue, finite-n exponent replacement,
original-residue change or Xi realization is assumed. The exact approved
Next action and its saved assessment remain unchanged; no new assessment
is written or approved in this research turn.
