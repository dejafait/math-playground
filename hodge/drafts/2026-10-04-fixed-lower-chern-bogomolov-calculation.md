# Fixed lower-Chern Bogomolov calculation checkpoint

Date: 2026-10-04. One mathematical specialization under the prior
SPECIALIZE assessment `drafts/literature/2026-10-04-fixed-lower-chern-stability-test.md`.
The target is exactly the saved arbitrary-rank test, with no change
to L044's chamber, first character or full second character.

The main gap is a compatible representative that could transport the
cubic action into the fourth NS-fixed RM direction. The intermediate
test is the cited necessary stability inequality. A violation stops
these lower data across ranks and independently of higher characters;
satisfaction would leave local freeness, stability and transport open.
L045 excluded one rank-two K-class, whereas this test fixes only
c_1=0 and beta=ch_2=2[C]+B_c. It is not a repeated rank-truncation test.

Import Perego, arXiv:1910.01867v1, Corollary 6.42, p. 118, with
trivial twisting and zero auxiliary B-field. For rank r>0 and n=4,
polystability implies semistability and requires
integral_X ((r-1)c_1^2-2r c_2) Omega^2 <= 0. Since c_1=0,
c_2=-beta and the tested expression is 2r integral_X beta Omega^2.

Write h=omega_c, s=q(h,h)>0, e_1=eta tensor 1 and
e_2=1 tensor eta. L044 supplies beta=4e_1+4e_2+tau_D, with
D|_N=2A_c+4pi_K. Its actual ample eigenvector lies in W and has
A_c h=lambda h, where 1<lambda<3/2. Thus D h=2lambda h.
The full mixed tensor's transcendental part has zero pairing with
h tensor h by orthogonality of T and N; this does not discard either
pure point component. The product polarization satisfies
Omega^2=s(e_1+e_2)+2h tensor h. Hence

integral_X beta Omega^2 = 8s+2q(h,Dh)=(8+4lambda)s>0.

The inequality is violated at every positive rank. Higher characters
do not occur in it. This stops polystable locally free realizations
of these exact lower data, not arbitrary representatives of the
cubic action or algebraicity of the already algebraic class.

Verification completed: exact arithmetic in Q[t]/(t^3+t^2-2t-1)
contracted 4G^{-1}+gB_0g^t directly against v=lambda omega_c,
including the 4 id contribution from 2[C]. It checked Dv=2lambda v,
lambda^2 s=4lambda^2+12lambda+2 and
lambda^2 integral_X beta Omega^2=64lambda^2+136lambda+32.
The direct contraction and eigenvector expression agree; every
coefficient in the last two polynomials is positive. The command
used Python's exact fractions and the existing matrix helpers,
with no new mathematical script or decimal root sampling.

Completed full proof:
[L046](../lemmas/L046-fixed-lower-chern-bogomolov-exclusion.md).
This is REPRODUCTION / NEGATIVE, not a new discovery beyond the
checked literature. No source review, residue search or pure point
correction calculation was made. The next numerical correction
target is already explicitly covered by the unchanged assessment.
