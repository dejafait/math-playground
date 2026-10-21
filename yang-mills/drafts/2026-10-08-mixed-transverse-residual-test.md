# Direct transverse mixed residual test

STEP_ID: YM-20261008-083-mixed-transverse-residual-test

Reuse the unchanged SPECIALIZE assessment
`literature/2026-09-26-current-target.md` for the saved full response
target. This bounded intermediate attempt tests
R_0T=G^(1/2) E_0^T A_0 I_T Sigma_T^(1/2), with threshold O(1).
An actual retained growing mode would abandon this full-vector
operator estimate, without implying growth of L064's signed response.
A bound would allow composing the two input blocks in their actual
path/multiplier order; no complete contraction would yet be settled.

Inspected the actual stencils and spectrum in L018, L026, L028,
L040–L041, L064–L065, the matrix-free RelativeBox implementation,
history/082, and ATTEMPTS/018–020. The latter stop generic residual
norm/localization closures; none supplies a direct transverse block
test. Ready primary-source coverage is reused, with no reproof of
general flow renormalization or stress matching.

Unfinished reasoning saved before computation: for frozen coefficients
and zero axial wave number, the generator sends component 1 into
transverse components with direction-dependent endpoint/clover filters.
The resulting vector need not be a discrete gradient. Its transverse
curl can therefore survive in the symmetric cross-component residual,
at order 1/a. The actual u_1 has zero axial mean, so a constant right
axial profile would miss this mechanism. Test a right axial profile
supported where u_1=x_1>0, retaining the constant left axial row and
a compact transverse carrier with unequal average filters. Use the
dual energy inequality to test the whitened norm without mistaking
a finite diagnostic for a proof. Coefficient derivatives, both Q
forms, all generator outputs and physical endpoints must be retained.

Essential inputs: L008, L009, L018, L026, L028, L040 and L065;
L060–L064 fix the downstream contraction. L011/L019 remain essential
for full response assembly. No mixed full-vector bound, signed
response growth, a² limit, log coefficient, finite matching or
reflected error <=c_box/2 is assumed. Other/other cubics, all nine
placements at logarithmic scale, nonlinear jets and forest compensation,
continuum fields, full reflection positivity, infrared control and
finite positive mass remain unresolved.

Completed: L066 proves c/a<=||R_0T||<=C/a. The frozen carrier
(0,pi/2,pi,0) yields the component-2 cross symbol
-i sqrt(2)u_1/a. A compact positive right axial profile and a smooth
transverse envelope give a positive limit of the a-scaled dual ratio.
The finite-shift argument bounds the full coefficient/envelope error
in l² by O(1), retains Q_3/Q_6 and physical endpoints, and supplies
the proof for the actual displacement. The four binary64 diagnostics
agree with the complete residual decomposition; they are not the proof.

Outcome: NEGATIVE / RESEARCH / REPRODUCTION. Abandon the uniform
full-vector residual estimate (ATTEMPTS/021); keep L065's axial bound.
The obstruction does not settle any actual signed trace. Within the
unchanged approved response target, test only the direct transverse
part of L064's K_1 path/path trace (equation (16)), using

    W_X^dir=sqrt(N) G E_0^T A_0 I_T Sigma_T,
    S_kl^dir=-Tr[K_1 Q_l (W_X^dir)^T E_+^T M_(Th_k)].

Here Q_l takes the direct transverse field at all levels to its actual
alternating paths; fixed rows remain zero. The identity is just (16)
with the right lift restricted to its direct summand. Essential inputs
are L018, L026, L060–L066, with L062's complete heat coefficients.
Seek an O(N²) estimate or a retained nonzero stronger-power coefficient
after the actual signed heat sum; another unrestricted residual norm
or arbitrary test matrix will not decide this contraction. Do not
assume a limit or a cancellation. The right axial-path summand, first
pair, other endpoint monomials, all nine logarithmic placements and
L011/L019's complete jets remain independently unresolved.
