# Three-particle complete current — working981

Invocation-start assessment980 is EXPLORE for the exact complete-current
target. This is one proof_attempt/development, not a new source review.
Preserve C466x/audit979, C466u and the contrasting C466t stop.

## Saved partial reasoning before full proof

On a survivor, v_0=-2 sum_(k!=j)(z_j-z_k)/|z_j-z_k|^2, hence
Re sum_j conjugate(z_j)(v_0)_j=-6. Therefore
(||X||^2)'=-12+2 Re sum_j conjugate(X_j) conjugate(H_j),
and ||X(t)||<=||u||+M_1 t. The strict buffer puts the whole
surviving path in the closed Euclidean ball of radius
r_*=sqrt(3)a+M_1 T_0<R. Compact continuation can exclude outer
events without a unique collision endpoint.

C466x supplies ||f_0||^2>=8P and the real symmetric pair spectra.
For exterior degrees k=3,4 the same single-frame trace estimate is
mu_k<=4P+kM_2<=||f_0||^2/2+kM_2. The imported all-degree compound
growth bound applies to velocity and parameter columns together.
With f=f_0+h, ||h||<=M_1, retain fractional damping via
||f-h||^2/2 <= 3||f||^2/4+3||h||^2/2.
Writing w=|F(X)| and w_0=|F(iu)|, w'=-||f||^2w, this suggests
w V_k(t)<=exp((kM_2+3M_1^2/2)t) w_0^(3/4) w^(1/4) V_k(0).
For all complete minors with a time column, V_k(0)<=||v(iu)||.
The factor w_0^(3/4)||v(iu)|| is bounded even at initial triple
coincidences: |Delta(u)|^(3/2) times a sum of simple pair poles.

Use eta_epsilon=theta(w/epsilon), zero-extended, theta=0 below1
and1 above2. Monotonic w implies every earlier w>epsilon on
its nonzero set. Together with the strict buffer, the paths lie
in K_epsilon={||z||<=r_*, |F(z)|>=epsilon}, a compact subset of U.
The C466u compact-continuation argument should then prove locally
interior survivor support, including all initial diagonals.

The ambient covector ||d|F|||=w||f||. The full four-form estimate
gives cutoff coefficient <=8||chi||_infinity||theta'||_infinity
exp((4M_2+3M_1^2/2)T_0)(2epsilon)^(1/4)
w_0^(3/4)||v(iu)|| ||f|| on epsilon<w<2epsilon.
By monotonicity, integral_shell ||f||^2 dt<=log2; Cauchy-Schwarz
then gives integral_shell ||f|| dt<=sqrt(T_0 log2).
This would pay the entire differential, with an O(epsilon^(1/4))
bound and no pairwise shell-residence hypothesis.

Still to verify in the canonical write-up: every complete coefficient,
support proof at arbitrary finite lifetime, truncated/flat shell cases,
all constants and orientation in the weak limit. This draft is not
yet a claimed theorem. No mathematical script is needed for these
symbolic inequalities. No sign, global assembly or Xi transfer follows.

## Completion note

The saved reasoning above is preserved as the preliminary checkpoint.
The full proof, constants, support and weak-limit checks are now in
[C466y](../lemmas/C466y-three-particle-complete-localized-current.md).
Its independent conceptual audit remains pending; this working note
does not replace the canonical proof or assert an RH candidate.
