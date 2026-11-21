# Fixed-arc prescribed-vector test — working checkpoint, step 163

Invocation target and prior gate: exactly the TARGET in
`literature/2026-11-03-spatial-cancellation-arc-attempt-scope.md`,
saved EXPLORE before this turn. Reuse its primary-source comparison;
no new external theorem or profile choice is proposed.

Main gap: actual-Xi all-degree positivity. Local intermediate target:
one fixed positive-measure arc on |u|=1/2 where the complete signed
S_(n,1) is at most A_n exp(-epsilon n), epsilon>0, eventually uniformly.
Downstream use would be an obstruction only to L707's stronger
averaged absolute-envelope budget, not to B_sp=o(n), J_sp=o(n), or RH.

Retain L666's exact product, j=0 factor, unit masses, W_x=1, inverse
angle, both finite endpoints and all M=n/3 moments, for the one L703
profile fixed before n. L706's nonzero slices and integrability and
L707's definitions are the interfaces. L707's transfer is unaudited;
no relative remainder is assumed. L657's amplitude/full-charge
accounting, H/support and realization remain independent.

Prior stops checked: L707's growing Lagrange upper certificate does
not prove cancellation; L705/L706 control signed endpoints only on
their stated inner arc; the Gevrey paired-tail absolute-variation stop
does not allow stretched-exponential tail errors to be treated as
exponentially small. Generic near-nullvectors and the radius-one
Fourier gap are not substitutes for this prescribed-vector test.

Attempt in progress: examine the exact product as a function of the
spatial ordinate after removing its common angular factor. Identify
where its absolute envelope concentrates, then test whether the full
finite signed sum can be bounded below that envelope at a positive
exponential rate. An endpoint or resolvent approximation must pay its
complete interior and geometric remainder relative to A_n.

Continuation/abandonment test: accept only a uniform positive rate on
one fixed arc, or preserve a material mechanism refinement with a
concrete analytic obstruction. A point sample, vanishing arc, absent
rate or unpaid remainder is inconclusive. One prior mathematical
EXPLORATION is recorded; this attempt has not yet earned a reset.

Promising refinement, not yet a conclusion: at the real point u=1/2
the exact positive zero/exponential factors concentrate at
omega_0=A integral_0^1 [1/(d+t/2)-t/(U/2+d*t)]dt. L703's Fourier
correction is zero away from its two narrow prescribed bumps, rather
than equal to -1 as at the radius-one gap center. If omega_0 has a
strict off-bump margin, the complex-measure/comb treatment in L698
can be adapted to show that the full finite resolvent approaches the
anchor resolvent exponentially near u=1/2. Its spatial continuation
and exact M-term remainder must still be paid. This uses existing
finite convolution, Fourier and three-circles tools, with the changed
center and every hypothesis verified; it is not an application of
L698's different-radius conclusion.

Independently, the derivative at y=0 of the limiting log modulus of
W_(x+iy)(u) is -Im integral f_u. The radial derivative of integral
f_r at r=1/2 is positive. A fixed small positive angular tilt should
therefore give positive log modulus at some fixed negative ordinate.
A retained lattice node approaches that ordinate. If both estimates
hold on a common fixed arc, they give the required relative separation.
The remaining checks are the exact L703 width margin, complete comb
pairing, all endpoints, spatial poles, and order of constant choices.

Completed: the full proof and citations are canonical in
`lemmas/L708-inner-arc-absolute-envelope-cancellation-obstruction.md`.
The fixed-arc test gives a positive-rate separation and hence a
positive linear lower bound for the stronger averaged budget. The
auxiliary exact-rational certificate is
`scripts/one-sided-hankel/spatial-cancellation-arc-163.json` (15 checks,
no failures). It does not verify the analytic proof. The completed
outcome is NEGATIVE for that sufficient subroute, with L708 unaudited.
The next separate conceptual audit reuses the same exact prior target
and assessment; no new mathematical scope or ready assessment is written.
