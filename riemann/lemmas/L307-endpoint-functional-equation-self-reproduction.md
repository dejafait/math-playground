# Lemma 307: endpoint functional-equation self-reproduction

**Hypotheses.** Let r=2n tend to infinity through even integers, r≥6. Put X=exp(2r), a=sqrt(4π²X²−25), q=a/(2π), A=r!/(2r)^r, and retain S_r(a) from L303. Define

F_a(z)=ζ(1/2+z+ia)ζ(1/2+z−ia),
χ(s)=2(2π)^(s−1)sin(πs/2)Γ(1−s),
C_a(z)=χ(1/2+z+ia)χ(1/2+z−ia).

Every vertical integral below is oriented upwards. Set

R_0=A [z^r] {X^z F_a(z)},
R_p=2A Re[X^(1/2+ia)(1/2+ia)^(−r−1)ζ(1+2ia)],
J=A/(2πi) ∫_(Re z=−1) X^z z^(−r−1) C_a(z)
                  ζ(1/2−z−ia)ζ(1/2−z+ia) dz.

Here [z^r] denotes a Taylor coefficient at zero, not a derivative without its factorial.

**Conclusion.** All displayed integrals converge absolutely and

S_r(a)=R_0+R_p+J.                                           (1)

The integral J has the absolutely justified dual expansion

J=Σ_(j,k≥1) (jk)^(−1/2) exp(ia log(j/k)) H_r(jk),
H_r(m)=A/(2πi) ∫_(Re z=−1) (Xm)^z z^(−r−1) C_a(z) dz.       (2)

At the stated endpoint parameters,

R_p=O(exp(−r²)),
J=−S_r(a)+O(sqrt(r)(2e)^(−r)),
2S_r(a)=R_0+O(sqrt(r)(2e)^(−r)).                            (3)

The remainders in (3) are little-o of (1+r)²exp(−r/256). Thus the functional-equation transform reproduces the original signed sum with opposite sign in its dual term. Its central residue is an unsigned high Taylor coefficient; it is not a positive pole main term. This does not prove that S_r(a) is nonzero, positive, or negative.

**Proof.** We use Riemann's functional equation in the form [DLMF 25.4.2](https://dlmf.nist.gov/25.4.E2), and the standard complex Stirling expansion [DLMF 5.11.3](https://dlmf.nist.gov/5.11.E3). These are supporting identities and estimates, not a reference for this lemma's conclusion.

First shift L303's integral from Re z=1 to Re z=−1. For each fixed a and r the only possible singularities crossed are the pole of z^(−r−1) at zero and the simple zeta poles at 1/2±ia. The Taylor coefficient defining R_0 is their zero residue, including possible cancellation. The other two residues are conjugate and sum to R_p.

Here are sufficient growth bounds to justify the shift without a hidden horizontal integral. Euler summation with one Bernoulli correction gives, for Re s>−1,

ζ(s)=1/(s−1)+1/2+s/12
 −s(s+1)/2 ∫_1^∞ B_2({x})x^(−s−2) dx,

where B_2(t)=t²−t+1/6. This follows by twice integrating the bounded periodic Bernoulli remainder in the usual sum-integral formula, first in Re s>1 and then by analytic continuation. The integral converges locally uniformly in Re s>−1. Its bounded integrand gives ζ(s)=O_a((1+|Im s|)²) uniformly on −1/2≤Re s≤3/2 away from the pole. Along the two horizontal edges at height ±T with T>2a+2, the product is therefore O_a(T⁴). The remaining factors are O_r(T^(−r−1)); the edge lengths are bounded. Their integrals vanish as T→∞. On the left line, the functional equation gives F_a(z)=C_a(z)F_a(−z). There the reflected zeta factors are bounded by ζ(3/2), and Stirling plus continuity on bounded height intervals gives

|χ(−1/2+it)|≤C(1+|t|),
|C_a(−1+iv)|≤C(1+a+|v|)².                                 (4)

Consequently the left integral converges absolutely for r>2, proving (1). Expanding the two reflected zeta factors into their absolutely convergent Dirichlet series is justified by (4) and the majorant ζ(3/2)² times the integrable kernel. This proves (2), including absolute convergence of the integrated series. Apparent gamma singularities in other presentations of χ introduce no extra poles into the original integrand.

Next approximate the gamma factor on the left line. Uniformly for t→+∞, substitution in complex Stirling gives

χ(−1/2+it)=(t/(2π)) exp(iψ(t))(1+O(1/t)),
ψ(t)=t−t log(t/(2π))+π/4.

The negative-height formula is its complex conjugate. For |v|≤b:=a^(1/4), multiply these two formulas at t=a+v and t=a−v. The amplitude ratio to q² is 1−v²/a², and Taylor's theorem, using ψ'(a)=−log q and ψ'''(t)=−1/t², gives

ψ(a+v)−ψ(a−v)=−2v log q+O(|v|³/a²).

The remainders are uniform since a±v≥a/2. Hence

|C_a(−1+iv)−q^(2−2iv)|≤C q²(1+v²)/a,  |v|≤b.             (5)

The exponent error here is small; the bound follows from |exp(iu)−1|≤|u| and |v|/a≤1. Denote by J_0 the integral defining J with C_a(z) replaced by q^(−2z). After using the absolute Dirichlet bound, (5) bounds the central contribution to |J−J_0| by

C A q²/(Xa) ∫_R (1+v²)^(-(r−1)/2) dv = O(A),              (6)

because q²/(Xa) is bounded at these parameters and the integral is uniformly bounded for r≥6.

For |v|>b, use (4) for J and |q^(−2z)|=q² for J_0. Since b≥1, the two tails together are at most

C A X^(−1) [(1+a)² b^(−r)/r + b^(2−r)/(r−2)].             (7)

This follows by bounding (1+a+|v|)² by C((1+a)²+v²) and integrating v^(−r−1) and v^(1−r). As log a=2r+O(1), log b=r/2+O(1), and log A=−(1+log 2)r+O(log r), (7) is O(exp(−r²/3)) for sufficiently large r. In particular it is O(A). Equations (6)–(7) prove J=J_0+O(A) with a constant independent of r along the endpoint sequence.

It remains to identify J_0, including its sign and cutoff. Write Y=q²/X=X−25/(4π²X). For real t, left-line inversion gives

(1/(2πi))∫_(Re z=−1) exp(tz)z^(−r−1) dz
 =−(-t)_+^r/r!                                             (8)

when r is even. One direct justification is to substitute z=−w in the parametrized vertical integral. It becomes (−1)^(r+1) times the right-line inversion at −t; L298's inversion, as used in L303, gives (8). The integrals are absolutely convergent, and t=0 gives zero. Applying (8) termwise is legitimate by the same reflected Dirichlet majorant. Thus

J_0=−Σ_(j,k≥1) (jk)^(−1/2) exp(ia log(j/k))
                         (log(Y/(jk))_+/(2r))^r.           (9)

This is a finite cutoff sum. At Y=X it is exactly −S_r(a), because exchanging j and k reverses the phase without changing the sum.

For completeness the tiny difference between Y and X is also controlled before any absolute sum of cutoff weights is taken. Let δ=log(Y/X)=O(X^(−2)). In the integral expression for J_0, replacing Y by X changes Y^(−z) to X^(−z). Along z=−1+iv, differentiation with respect to log Y bounds the difference by C X |δ||z|. Expanding the reflected zeta factors only to bound their absolute sum gives

|J_0(Y)−J_0(X)|≤C A X |δ| ζ(3/2)²
                             ∫_R (1+v²)^(−r/2)dv
                       =O(A/X).                           (10)

The intermediate Y values are comparable to X, so this derivative bound is uniform. Combining (6)–(10), and r!=sqrt(2πr)(r/e)^r(1+O(1/r)), proves the asserted estimate for J.

Finally, ordinary first-order Euler summation at s=1+2ia with cutoff N=ceil(2a) gives |ζ(1+2ia)|≤C log(2+a): the finite harmonic sum is O(log N), the integral term N^(1−s)/(s−1) is O(1/a), and the remainder is O(|s|/N). Therefore

|R_p|≤C A X^(1/2)a^(−r−1)log(2+a)=O(exp(−r²)).             (11)

Indeed its logarithm is −2r²+O(r). Substitution in (1) proves the last line of (3). Since 1+log 2>1/256, comparison with the required endpoint error proves the stated little-o assertion. ∎

This test excludes discarding the dual term merely because the two remote poles are small: the dual is the original unknown signed coefficient with a minus sign, up to a much smaller error. It does not exclude a new lower bound for R_0, but (3) supplies none. Such a bound would still be the missing arithmetic sign input. No endpoint sign range, all-degree positivity, or RH candidate follows.

**Mathlib.** Full statement: not checked. Supporting zeta functional equation, complex Stirling formula, Euler summation, residue theorem and Mellin inversion coverage: not checked. No Mathlib theorem match is claimed. The direct DLMF links above are standard supporting results, not matches for the full statement. L303 supplies the original Mellin identity and the scalar inversion used here; the contour, summation, gamma-product comparison and scale estimates are proved above.
