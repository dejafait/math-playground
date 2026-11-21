# Finite shear attempt — working checkpoint, 7 November 2026

Invocation target and ready coverage: the unchanged TARGET in
`literature/2026-11-07-paired-fiber-finite-replacement-test.md`.
The main gap is L030–L032/C032a actual-Xi all-degree mixed positivity.
Test a finite second-component trace shear, together with a first-component
depinning extension, against the complete strip mass. Strict decrease could
exclude this conditional paired configuration from a minimizer, if one exists.

Essential inputs read: L847's actual full form, L879's phase line and radial
variation, and the complete load-bearing boundary arguments of L888/L889.
The exact endpoint reduction L889(17)–(19) checks algebraically: the
holomorphic w derivatives and the b' terms cancel, with no remaining a'
term. This use does not independently audit either entire lemma. Parent
source/failure comparison and attempt65/69/77 were read; no new source
coverage or cross-notebook input is needed for the unchanged target.

One proposed finite field has v2=B*(y2-m2)*chi(y1,y2), with compact support
inside the clean strip and B finite, outside the small-trace box if feasible.
Its first component must depin at least one fiber. The required inequality is
the signed interface term <-E, with E the full nonnegative interior cost;
all collars and endpoint det(I-iD(u+v))!=0 are obligations. A negative
coefficient alone is not success. Investigate the shear's paid mass before
choosing its first component; no finite admissibility or sign is yet proved.

Preserve the pinned, small-trace and fixed-bump stops at their stated scopes.
Configuration existence, a full extension with strict negative mass, endpoint
nondegeneracy, minimizer compactness/existence, other contacts, L868's sharp
bound, higher signs and Xi transfer are unresolved. This is unfinished
reasoning, not a theorem, obstruction or accepted outcome.

## Candidate finite-shear obstruction — reasoning saved before write-up

At a contact write p=partial_1 u1, k=partial_2 u2, H=|partial_1 s|.
The exact affine dependence at a=0,b=0 is W(0,0,B)=w+cB, where
w=H*(1-p^2)/(1+p^2)^2 and
c=H*[k*(1-p^2)+2p]/[(1+k^2)*(1+p^2)^2]. If c is nonzero at each
fiber at a common y0, a finite B_gamma with |B_gamma|>1 makes both
coefficients strictly negative. This is an additional conditional subclass,
not a property proved for actual data. Nonzero c is not supplied by L879.

Choose disjoint narrow x cutoffs xi_gamma around the two fibers and set
b=sum B_gamma*(y-y0)*xi_gamma(x)*psi((y-y0)/h). At the pinned endpoint
(u1,u2+b), write P=u1,x, T=u1,y, N=u2,x, K=u2,y. Then
J_b/(1-iP)=1-i*(K+b_y)+T*(N+b_x)/(1-iP).
Since T=0 at each fiber, narrow x support makes |T*N|<1/4;
narrow y support makes |T*b_x|<1/4 even for finite large B_gamma.
Its real part is then >1/2, proving endpoint J_b!=0 on support.

At y=y0, b=b_x=0 and b_y=B_gamma*xi_gamma. Hence
Q_b/Q=1-B_gamma*xi_gamma*(P+i)/J. At the fiber the imaginary part
of (P+i)/J equals 1/(1+k^2)>0. An adjacent off-zero point therefore
has strictly positive phase cost. The full pinned cost e=E(0,b)>0.

Take a fixed first field A= sum xi_gamma(x)*zeta((y-y0)/h_a), with
h_a small enough that W remains negative on both nonzero traces.
For v_tau=(tau*A,b), the interface term is negative but >=-C*tau^2.
Compact smoothness gives E(v_tau)>=e-L*tau. A finite tau satisfying
L*tau<=e/4 and C*tau^2<=e/4 leaves mass difference >=e/[2*(2pi)^2].
The norm bound tau*sup||H_b^{-1}D(A,0)||<1/2 checks the final Jacobian.
These estimates retain the full supports and collars. They stop a fixed
finite shear followed by sufficiently small depinning, even with negative
interface flux; they do not settle jointly scaled supports/amplitudes.

All proposed inequalities above still require the canonical proof's complete
hypotheses, constants and sign checks. No independent audit is claimed.

## Completion

The complete conditional construction and estimates are now canonical in
L890. Its finite endpoint has negative interface flux but strictly positive
full mass difference. The reasoning above is retained as the pre-write-up
checkpoint; it does not replace L890's hypotheses or qualifications.
The fixed-shear construction is stopped at this scope. A common shrinking
scale for both components is untested and is the proposed refinement within
the unchanged ready finite-replacement target.
