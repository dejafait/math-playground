# Signed remainder — bounded energy test

The unchanged ready assessment is
`literature/2026-10-12-cubic-residual-action-cubic-scale.md`.
The main gap remains the ultraviolet-uniform interacting reflected
comparison, followed by continuum and infrared construction. The
intermediate test is whether L156's E,E sector admits a global
Hodge-energy norm estimate with uniformly bounded signed remainder.
Such an estimate could avoid raw forest covariance growth when closing
cubic boundedness. Continue only if the actual signed covariance order
provides the required gain; abandon this global norm shortcut if an
exact relative-energy packet grows. This tests the approved complete
cubic response, without changing its target or claiming vanishing.

Unfinished reasoning saved before verification: with P=Sigma L and
Q=I-P, let Z=Sigma^(-1/2) D_0 Phi Sigma^(1/2). Since Phi D_0=I
on pinned vertices, ZQ=Q and QZ=Z. Thus the energy-normalized signed
remainder W=Sigma^(-1/2) E Sigma^(-1/2) should have blocks
[-I,-X;-X^T,I], X=QZP. On the co-closed constant axial-edge mode
times a transverse Dirichlet scalar eigenvector of eigenvalue lambda,
the lower prefix is s/sqrt(N lambda). The pinned upper end contributes
N e_(N-1) to the axial Dirichlet Laplacian of s. This predicts
||X u||^2=N/lambda+2(N-1)+lambda(N-1)(2N-1)/6, growing as N^3
at the lowest transverse frequency. The identity, boundary convention,
and comparison with the actual E,E order remain to be verified.

Essential inputs being checked: L018 L026 L155 L156 L157. L158/L159
retain the mixed branches and are contrasts, not premises for the
packet calculation. ATTEMPTS/009, /011 and /036 remain within their
recorded scopes. This packet is not either actual probe or a signed
response lower bound. E is never an independent Gaussian noise.

Completed: [L160](../lemmas/L160-signed-remainder-hodge-energy-norm-obstruction.md)
proves the exact signed blocks and Theta(N^(3/2)) global Hodge-energy
norm. The upper estimate retains the entire component-1 spectrum;
the lower estimate uses the actual constant axial/lowest transverse
mode and its pinned upper endpoint. All 61 exact identities and 20
complete rational packet checks pass with zero error; certificate:
`scripts/combined-ward-response/signed-remainder-energy-certificate.json`.
Those finite checks do not certify either actual probe or an asymptotic.
The uniform global signed-remainder shortcut is abandoned in
ATTEMPTS/037; the actual E,E contraction remains open. Continue the
unchanged ready response target using its Hodge blocks inside the
full tensors, before inequalities, with T_i and V_i retained.
