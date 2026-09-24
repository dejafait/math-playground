# Lemma 272: rotated saddle geometry and theta-strip clearance

**Hypotheses.** Use the saddle quantities and Hessian B of L269, with a→+∞ and integers 1≤n≤Ca for fixed C>0. Put d=n/r², b=4h+d+4ia, θ=(arg b)/2, and ρ=π/4−τ. At the positive saddle write u=s−r and t=x+iτ. Consider specifically the linear real two-plane

p=(u+x)/√2=e^(−iθ)y,   q=(u−x)/√2=e^(iθ)z,   y,z real.

The conclusions below concern this plane and its square patches; they are not an obstruction to every possible contour.

**Conclusion.** On this plane the quadratic form becomes

(u,x)B(u,x)^T=|b|(y²+z²)+2dyz.

Its eigenvalues |b|±d are comparable to a, and its Gaussian integral is exactly 2π/√(det B). The entire closed square |y|,|z|≤R lies within both theta strips |Im(s+t)|, |Im(s−t)|<π/4 if and only if

√2 sin θ R<ρ,   where ρ=(1/2)arctan(h/a).

The same inequality puts the whole linear rotation homotopy inside those strips. In this range θ→π/4 and ρ~h/(2a), so the largest permitted R has order h/a. Such squares can contain a fraction 1−o(1) of the rotated Gaussian mass if and only if h/√a→∞. A radius R=√(M log a/a) with fixed M>0 is admissible exactly when it satisfies the displayed clearance inequality; a sufficient asymptotic condition is h/√(a log a)→∞.

These statements establish local geometry only, not a deformation identity for the full theta integral or a new Laguerre sign range.

**Proof.** The saddle equation gives

r=(1/2)log(a/(2π))+(1/4)log(1+(h/a)²),   h=n/r+9/2.

Since r≥(1/2)log(a/(2π)) and n≤Ca, h/a=O(1/log a). Consequently r~(1/2)log a, d=O(h/r)=o(a), θ→π/4 and ρ~h/(2a). The identity for ρ follows from τ=(1/2)arctan(a/h) and positive a,h.

The real orthogonal change (u,x)↦(p,q) converts B into

[[4h+d+4ia, d], [d, 4h+d−4ia]].

Substituting the two opposite rotations makes both diagonal entries |b| and leaves the off-diagonal entries d. Thus the resulting matrix A is real positive definite for large a, with eigenvalues |b|±d~4a. Moreover det A=|b|²−d²=16(h²+a²)+8hn/r²=det B. The rotations have determinant one in (p,q) coordinates. Choosing the orientation inherited from the original real plane, the real Gaussian integration formula therefore gives 2π/√(det B), with positive sign. This is also the original complex Gaussian value in L269; it does not assert an identity for the nonquadratic integrand.

The kernel arguments on the rotated plane are

s+t=r+√2 e^(−iθ)y+iτ,
s−t=r+√2 e^(iθ)z−iτ.

Their imaginary parts are τ−√2 sin θ y and −τ+√2 sin θ z. On the closed square their maximum absolute values are both τ+√2 sin θ R. This proves the exact necessary and sufficient strip condition. For the homotopy replacing θ by vθ, 0≤v≤1, sin(vθ)≤sin θ, so the same condition suffices throughout. For the radii under consideration R=o(1), the real part of s remains near r>0 as well, avoiding the model phase logarithm's cut.

To prove the mass assertion, normalize exp(−(y,z)A(y,z)^T/2) to a probability density and scale Y=√a y, Z=√a z. Since A/a→4I, these Gaussian densities converge to a nondegenerate Gaussian, with uniform Gaussian tail bounds. A square contains mass tending to one exactly when √a R→∞: sufficiency follows from those tail bounds; necessity follows along any subsequence where √a R is bounded, since the limiting Gaussian assigns positive mass outside every bounded square. The supremum of admissible √a R is asymptotic to h/(2√a). Therefore an admissible choice with mass tending to one exists exactly when h/√a→∞. If that ratio tends to zero, every admissible square instead has mass tending to zero. Substitution of R=√(M log a/a) proves the final clearance statements. On that radius the omitted Gaussian mass is O(a^(−cM)) for an absolute c>0, by the eigenvalue bounds. ∎

In index terms, the mass condition is n/(√a log a)→∞. Thus this particular strip-contained square rotation cannot directly cover fixed n, or even n=o(√a log a). Polynomially small Gaussian tails at the stated radius require h at least a sufficiently large constant times √(a log a), hence n on the scale √a(log a)^(3/2) or larger. This is below L271's sufficient threshold, but geometry alone proves no improvement. Boundary pieces connecting the original and rotated patches, nonquadratic errors there, and the global complement still require estimates. Crossing the strip would require additional analytic information not used here; no natural-boundary theorem is asserted.

**Mathlib.** Full statement: not checked. Supporting matrix changes of variables, real Gaussian integrals, and holomorphic deformation results: not checked. No library theorem match is claimed. The matrix and strip calculations are proved here; L269 supplies the saddle setup, theta strip, and original Gaussian identity.
