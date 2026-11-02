# Exact even rational gauge: bounded attempt, step 44

Invocation-start coverage is the unchanged EXPLORE assessment
`drafts/literature/2026-11-02-displaced-positive-cone-distance.md`.
The only target is its exact affine nonnegative cone distance. The main
gap remains actual-Xi mixed positivity. This test could give a countersequence
to the sufficient rate-1/100 cone bound; unit-residue H, support and Xi
realization would remain independent gaps.

Use L666's exact W and L673's admissible phase nodes, interpolation weights,
and Cauchy remainder. Test the proposed gauge

    g_n(z)=(1-z/rho)*exp(-c*n*z)/sqrt(W_(x+z)(-1)*W_(x-z)(-1)),
    c=10*pi/27, rho=27/(100*n), g_n(0)=1.

The prior quartic screen and C673a/C673b stops were inspected as comparisons,
not assumed premises. The exact rational factor is a different test, not
further quartic tuning. No new literature theorem is required for the
assessed interpolation mechanism. No originality claim follows from coverage.

First establish the branch and signs on a pole-free strip. Then test the
continuous exponent, including the even part of the exact W, against
-1/100. A real-crossing obstruction would stop this sufficient contour
estimate; a sampled value would only guide the proof. Continue on a fully
paid countersequence or rigorous obstruction/refined mechanism; otherwise
park this gauge. Neither a favorable branch nor angular maximum is assumed.

## Reasoning saved before the calculation

For V_n(z)=W_(x+z)(-1), possible poles lie at z=d-t_j (including
z=d from j=0), and zeros at z=d-U/t_j for j>=1. Thus both V_n(z)
and V_n(-z) are holomorphic and nonzero on |Re z|<1/4. Their product
is even, equals one at zero, and is |V_n(iy)|^2 on the imaginary axis.
The normalized square-root branch should therefore be positive on that
axis and preserve the phase-node signs. This needs a complete canonical
argument before being reported as a result.

The candidate limiting exponent is

    F(z,u)-(F(z,-1)+F(-z,-1))/2-c*Re z+K(z).

At a positive real crossing and u=-1 this reduces to the odd part of
F(s,-1), minus c*s, plus K(s). Testing this one-dimensional necessary
condition precedes any two-dimensional contour design. All finite-product
costs and any asymptotic conclusion remain unresolved at this checkpoint.

## Completed bounded attempt

Outcome: NEGATIVE. The full proof and its exact qualifications are in
`lemmas/C673c-exact-even-factor-angular-crossing-stop.md`. The branch,
positive nodal factor and Cauchy remainder are valid, but the uniform
absolute-contour exponent criterion fails on every contour in the stated
common branch/pole-free class once q>=15000. This does not decide kappa_e
or bound the signed integral. C673c awaits a separate critical audit.

The initial real-crossing diagnostic found a sampled minimum about
-0.01006695, so the real axis alone did not give the proposed stop.
The new angular diagnostic exposed a worse band near Im(z)=3/20. The
certificate then used one exact angle (-99+20i)/101, complete rational
sample intervals and proved between-sample/height errors. It gives
E_*>=-31639257/25000000000>-1/500 on the entire crossing band, versus
required upper -1/100. All 101 samples and 15 exact checks passed.
The canonical proof supplies both analytic coverage and the node forcing
the contour crossing; the script alone does not prove those arguments.

Artifacts and commands:

    python3 scripts/one-sided-hankel/positive-cone-exact-even-screen.py
    python3 scripts/one-sided-hankel/positive-cone-exact-even-certificate.py

Each script writes its complete .json sibling. The first is floating design
only. An initial transient design command lacked scipy and failed before
calculating; the retained screen uses explicit integrated logarithms and
does not require scipy. The certificate uses only standard-library exact
fractions. Complete summary and all checks were inspected with the scoped
JSON reader; no preview was substituted for the certificate or analytic proof.

Park this single-angle even-factor gauge's uniform absolute-contour test.
The new obstruction is angular: factoring the even response at u=-1
leaves a fixed nearby angle costly. A concrete refinement for a later
attempt is to replace that factor by a symmetric four-factor product
at u_*=(-99+20i)/101 and its conjugate. First test its real crossing
and the same horizontal band before any contour optimization. This is
a proposed different gauge, not a claimed improvement or derived result:

    A_new(z)=[W_(x+z)(u_*)*W_(x-z)(u_*)
              *W_(x+z)(conj(u_*))*W_(x-z)(conj(u_*))]^(1/4),
    g_new(z)=(1-z/rho)*exp(-c*n*z)/A_new(z), A_new(0)=1.

Its branch, imaginary-axis signs, both crossing costs, continuous angular
error and finite-n bounds are unresolved. Essential inputs are L666 and
L673; C673c is the newly proved but unaudited comparison motivating this
refinement. Reject it if either necessary crossing test rigorously misses
-1/100; otherwise seek a fully paid contour bound. No same-gauge contour
search is justified by this record. The exact ready cone target and
literature assessment are unchanged, so no new source gate is approved here.
