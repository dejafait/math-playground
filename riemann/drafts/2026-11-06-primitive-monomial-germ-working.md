# Primitive/monomial construction working checkpoint

6 November 2026. Invocation-start target and SPECIALIZE coverage are in
`literature/2026-11-06-primitive-monomial-local-germ.md`. This is the first
mathematical attempt on that construction; the fixed-cutoff range route
remains parked. No numerical or cross-notebook input is used.

Main gap: L030-L032/C032a all-degree actual-Xi mixed positivity. Target:
a local radial germ through an explicitly hypothesized nonzero pair
(zeta,eta), with G(zeta) of finite multiplicity n>=1 and
G(eta)(zeta-eta)!=0. Possible use: a local building block near a divisor
crossing, without any assertion about global extension or higher orders.
Continue only with an actual smooth germ, transverse first coordinate,
invertible original angular projection and exact punctured positivity.

Partial reasoning saved before completing the domain/sign checks:
write w=z_1-zeta, G(zeta+w)=w^n g(w) and
H(w,z_2)=C g(w)G(z_2)(zeta+w-z_2)^2/((zeta+w)^3 z_2^3).
Then omega=w^n H dw wedge dz_2, with H nonzero near (0,eta).
The jointly holomorphic primitive v=integral_eta^z_2 H(w,t)dt
should give omega=w^n dw wedge dv and a local holomorphic inverse
z_2=h(w,v), with h_w(0,0)=0 and h_v(0,0)=1/H(0,eta).

Candidate surface: v=A w+i conjugate(w)^(n+1)/(n+1), with
A=-i H(0,eta) eta/zeta. Its exact pullback in w=x+iy is
2|w|^(2n) dx wedge dy. The tangent has dz_2/dw=-i eta/zeta.
Consequently the two original angle differentials are
Im(dw/zeta) and Im(-i dw/zeta), whose real determinant is
1/|zeta|^2>0. Continuity and the real analytic inverse theorem should
give the radial reparametrization with its correct orientation.

Still to record carefully: joint convergence of the primitive, both
inverse domains, shrinking one neighborhood to retain every nonzero
factor, transversality and the unremoved J zero. Expected exact formula
in angle coordinates is J=-2 conjugate(w)^n/(H z_1 z_2 det DTheta),
so FJ=2|w|^(2n)/det DTheta. This is a candidate derivation, pending
completion, not an independent audit or a complete RH candidate.

Completion: the joint primitive, both inverses, original angular
orientation and retained Jacobian have now been checked in the full
proof canonical in `lemmas/L855-primitive-monomial-positive-radial-germ.md`.
The local test succeeds for every fixed n>=1. This checkpoint preserves
the partial reasoning; L855 supersedes it and still awaits independent
audit. No global extension or all-degree sign is inferred.
