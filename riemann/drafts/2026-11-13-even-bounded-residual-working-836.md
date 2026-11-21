# Fixed shift32 specialization working836

Approved target: assessment834's complete even bounded-forcing resolvent
specialization; no shift or forcing sweep. Main gap remains actual-Xi
mixed positivity; this is only a possible residual-enclosure ingredient.

Current proof plan (unverified until canonical write-up): use the killed
supported Fourier reference G with symbol half log(1+t²). C759a's common
smooth-core closure and L515's part-form identification should identify G
exactly. Symmetrize L741's one-sided r into rho(x)=r(|x|)/2, so
A_e=G-cI-R_rho-primes+2c_h<c_h,.>, c_h=cosh(x/2).
Bound each perturbation on L2 and L-infinity consistently: scalar <3,
remainder <5, five paired prime shifts <10, even pole <6; total <24<32.
Reference L2 Laplace resolvent has L-infinity norm <=1/32 by testing
against L2 (hence L1) dual functions. Neumann series then converges in
L-infinity and L2, giving M=1/8 and identifying the L2 inverse. This
avoids C0 or Bochner-integral assumptions in L-infinity. Need check
signs, pole factor, exact reference/core and every limit before conclusion.

Inputs: C759a(1),(5)-(6), C759h Proof1-2, L741(13),(16), L515
reference/core; primary GRv1 Section2, FOT4.4.2-4.4.3,
Jacob-Zwart Proposition5.2.4(a), Engel-Nagel III.1.3.
No positivity, isolation, endpoint-relative sign or Xi realization follows.

Completed: canonical C759k proves the fixed test with M=1/8. The
common conservative perturbation norm is <24, the required threshold32.
The full proof and qualifications supersede the provisional plan above;
no independent critical audit has yet been performed.
