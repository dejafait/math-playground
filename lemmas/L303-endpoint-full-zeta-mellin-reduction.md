# Lemma 303: endpoint full-zeta Mellin reduction

**Hypotheses.** Let r>1, a be real, and use W_r, J_r and T_r(a) from L297. Define the finite cutoff sum over all positive integers

S_r(a)=Σ_(j,k≥1) W_r(j,k) exp(ia log(k/j)).

The sum is finite because W_r(j,k)=0 when jk≥exp(2r). For c>1/2 put

Z_r(a;c)=Γ(r+1)/(2r)^r · (1/(2πi)) ∫_(c−i∞)^(c+i∞)
 exp(2rz) z^(−r−1) ζ(1/2+z+ia) ζ(1/2+z−ia) dz,

using the analytic logarithm on Re z>0.

**Conclusion.** The integral is absolutely convergent, independent of c>1/2, real, and equals S_r(a). Uniformly for every real a as r→∞,

|T_r(a)−Z_r(a;c)|=O(r exp(−9r/128)).                 (1)

Consequently at the admissible parameters of L302,

I_n(a_n)=C₀ exp(Φ_*) (π/a_n)
 ·[Z_r(a_n;c)+O((1+r)²exp(−r/256))], r=2n.          (2)

The new error in (1) is little-o of the error scale in (2). This is a quantitative replacement of the finite Dirichlet polynomials by full zeta factors, not a replacement by |ζ(1+ia)|² or a positive lower bound.

**Proof.** L297 proves the decreasing-coordinate property of W_r and, for L≥0, the bound

Q_r(L):=exp(L/2)(1−L/(2r))_+^r ≤ exp(−L²/(8r)).    (3)

Let m=ceil(exp(3r/4)), N=m−1 and B=log N. Then J_r={1,…,N}, including when exp(3r/4) is an integer. For sufficiently large r, B>0. By a union bound and symmetry the absolute mass outside J_r² is at most

2 Σ_(j≥m,k≥1) W_r(j,k).

For any decreasing nonnegative function f, f(j)≤∫_(j−1)^j f(x)dx, and Σ_(k≥1) f(k)≤f(1)+∫_1^∞ f(y)dy. Applying these facts successively bounds this mass by

2 ∫_N^∞ W_r(x,1)dx + 2 ∫_N^∞∫_1^∞ W_r(x,y)dy dx.             (4)

Substitute x=exp(u), y=exp(v). The first integral is ∫_B^∞ Q_r(u)du. Since u/B≥1 there, (3) bounds it by

(4r/B) exp(−B²/(8r)).

The second integral is ∫_B^∞ (L−B)Q_r(L)dL, at most

∫_B^∞ L exp(−L²/(8r))dL=4r exp(−B²/(8r)).

Now N=exp(3r/4)+O(1), so B=3r/4+O(exp(−3r/4)) and B²/(8r)=9r/128+O(exp(−3r/4)). Thus (4) is O(r exp(−9r/128)). Every phase has modulus one, proving the same uniform bound on |S_r(a)−T_r(a)|. This is a discrete tail estimate; the continuous mass estimate alone would not justify removing the index cutoff.

For the integral identity use L298's scalar inversion formula, valid for real t and c>0:

t_+^r/Γ(r+1)=(1/(2π))∫_ℝ exp((c+iv)t)(c+iv)^(−r−1)dv.

Multiply by Γ(r+1)(2r)^(−r)(jk)^(−1/2)exp(ia log(k/j)) and set t=2r−log(jk). We may sum its right side over all j,k≥1 before integrating. Indeed the integral of the sum of absolute values is at most

Γ(r+1)/(2r)^r · exp(2rc)/(2π)
 ·[Σ_(j≥1) j^(−1/2−c)]² ∫_ℝ (c²+v²)^(−(r+1)/2)dv <∞.

Here 1/2+c>1 and r>0. Fubini therefore applies. The two absolutely convergent Dirichlet series are precisely the two displayed zeta factors, proving S_r=Z_r. This also proves absolute convergence and independence of c, without a contour shift or continuation across a pole. Symmetry under j↔k proves reality. This proof is valid even if c depends on r and remains strictly greater than 1/2; no bound uniform in c is asserted for the absolute-integrability majorant.

Combining the established identity with (4) proves (1). Substitution into L302 proves (2), since

r exp(−9r/128) / [(1+r)²exp(−r/256)]
 =r/(1+r)² · exp(−17r/256) →0.

All constants in the tail estimate are independent of a. No estimate for zeta at a growing imaginary part has been used. ∎

For example c=1/2+1/r keeps the zeta factors in their absolutely convergent half-plane, at real part 1+1/r. At z=c+iv they still have imaginary parts a+v and −a+v; they are conjugates only at v=0, apart from accidental equalities. The complex Mellin kernel still supplies no positive averaging measure. Estimating this coupled-height integral relative to a modulus square requires a new uniform arithmetic remainder estimate; (1) controls only the index-cutoff error. A lower bound dominating (1+r)²exp(−r/256) at a_n would suffice for endpoint positivity. No such bound is established, and lower indices and bounded exterior heights remain outside this reduction.

**Mathlib.** Full statement: not checked. Supporting zeta Dirichlet-series identity, Fubini, gamma/Fourier inversion and monotone sum-integral comparison: not checked. No library match is claimed. The scalar inversion formula is proved in L298; the full-series interchange and discrete tail bound are proved above.
