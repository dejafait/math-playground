# Quotient-family identification — working record, step 258

The approved target is exactly the TARGET in
`drafts/literature/2026-10-16-quotient-affine-line-dual-kernel.md`.
Its unchanged SPECIALIZE coverage is reused. This is a proof attempt,
not additional literature work or a kernel-polynomial implementation.

The arbitrary-curve analytic-order/rank gap remains. The intermediate
target may supply the correct affine-line algebra for later L066 data;
it supplies no descent arithmetic. Audited L067/L068/L070/L071 are the
inputs. ATTEMPTS/035--036 remain parked; L069 and partial columns are
excluded. The source comparison found no existing local identification.

Working mechanism: at each direction C, the imported dual-isogeny theorem
identifies ker(hat(Phi_C)) with Phi_C(E[7]) and hence V/C. A nonzero coset
is the line P+C, with inverse Phi_C(P), independent of representative.
The family is a finite scheme over Spec(D), composed with Spec(D)->Spec(Q),
not a Weil restriction. Its full kernel has degree 56 over Q; its eight
identities must be removed to obtain 48 elements.

Convention test: [a] on the quotient sends H to aH, so the functional
lambda_H with H={lambda_H=1} changes by a^{-1}. Cartier duality is
Hom(C,mu_7). For a temporary primitive zeta and fixed pairing order
e_7(P,c), the exponent t obeys t_(g x)(g c)=chi_7(g)t_x(c).
No zeta is assumed rational. The completed applicability proof is now
canonical in `lemmas/L072-conductor389-quotient-affine-line-identification.md`;
this working record is retained without duplicating that proof. The
new assembly awaits separate critical audit.

Continue only if forward/inverse maps work for every direction and are
Galois compatible, with precisely the identity/through-zero exclusions
and these scalar/twist conventions. Otherwise retain the obstruction.
No incidence/norm, explicit dual-kernel polynomial, units/classes, local
bounds, Selmer containment, localization or rational membership is supplied.
