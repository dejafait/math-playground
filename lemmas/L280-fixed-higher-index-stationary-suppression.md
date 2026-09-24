# Lemma 280: suppression at each fixed higher theta-index stationary point

**Hypotheses.** Use the shifted integral, r,h,τ,Φ_* and theta-series convention of L269. Let a→∞ with log a≤h≤2 log a. Fix positive integers j,k with jk>1, independently of a. Write b=log(jk)/2 and d=log(k/j)/2. For Re z>0 define the individual exact theta summand

T_j(z)=8π²j⁴ exp(9z/2−πj²exp(2z))(1−3/(2πj²exp(2z))).

Put s₀=r−b, x₀=d, p=(s−s₀+x−x₀)/√2, q=(s−s₀−x+x₀)/√2, and ε=1/100. Let J_jk be the integral of exp(−2aτ)s^(2n)T_j(s+x+iτ)T_k(s−x−iτ)exp(2iax) over |p|,|q|≤ε, with positive area measure.

**Conclusion.** Uniformly in the stated h range, for each fixed j,k,

J_jk=(8π²)² exp(Φ_*) W_jk exp(ia log(k/j)) [π/(2a)+o(1/a)],

W_jk=(jk)^(−1/2)(1−b/r)^(2n)>0.

In particular |J_jk|=o(exp(Φ_*)/a). The constants and the little-o may depend on j,k. This assertion does not bound the sum over growing indices or any complementary nonstationary regions, and proves no new global sign range.

**Proof.** Eventually s₀>0 and both real kernel arguments on the square are positive: at its center they are r−log j and r−log k. The individual series terms above are therefore exactly those in L269. Set v=(p+q)/√2 and c=2√2. On dropping the two lower-degree prefactors in T_j,T_k, direct substitution gives the normalized integrand

(8π²)² exp(Φ_*) W_jk exp(ia log(k/j)) A_b(p,q) exp(if(p)−if(q)),

f(y)=−(a/2)(exp(cy)−1−cy),
A_b=exp(S_b),
S_b=2n log(1+v/(r−b))+9v−(h/2)(exp(cp)+exp(cq)−2).

Indeed j²exp(2(s+x))=exp(2r+cp) and k²exp(2(s−x))=exp(2r+cq). The constant prefactor ratio is j⁴k⁴exp(−9b)=(jk)^(−1/2). The remaining constant oscillation is exp(2iad). The imaginary phase has its unique stationary point at p=q=0; no assertion of a stationary point for the full complex exponent is needed.

Here S_b(0)=0. Its two first derivatives at zero equal

[2n/(r−b)+9−2h]/√2=√2 n b/[r(r−b)]=O_b(1),

because n=r(h−9/2), h/r is bounded, and b is fixed. On the fixed square its Hessian is the negative diagonal matrix with entries 4h exp(cp),4h exp(cq), minus the positive semidefinite matrix with all entries n/(r−b+v)². Consequently

−C_b h I≤Hess S_b≤−c_b h I,
A_b≤C_b exp(−c_b h(p²+q²)),
|∇A_b|≤C_b(1+hρ)exp(−c_b hρ²),
|(A_b)_pq|≤C_b(h+1+h²ρ²)exp(−c_b hρ²),

where ρ²=p²+q². The Gaussian envelope follows by absorbing the O_b(ρ) linear term into half the negative quadratic term. These inequalities give a uniformly bounded mixed variation on every subrectangle, by the edge and double-integral Gaussian estimates proved in L278 (the additional constant terms have bounded integrals).

Apply the exact real phase substitution Y=g(p), Z=g(q) of L278, with inverse P. The new amplitude is B_b=A_b(P(Y),P(Z))P'(Y)P'(Z); its mixed variation remains bounded by the same chain-rule proof. On |Y|,|Z|≤R=a^(−2/5),

B_b=1+O_b(R+hR²).

L278's Fresnel primitive and rectangle argument thus gives the model integral π/(2a)+o(1/a): the absolute central replacement error is O_b(R³+hR⁴), and the complementary transformed rectangles and Fresnel tails cost O_b(1/(a^(3/2)R)+1/(a²R²)). Each is o(1/a), uniformly for h≤2 log a.

The discarded prefactors have product 1+O(1/a) throughout this square, since |πj²exp(2(s+x+iτ))| and |πk²exp(2(s−x−iτ))| are comparable to a. Their absolute contribution after normalization is O_b(1/(ah)), using the Gaussian envelope integral O_b(1/h). This is o(1/a). It proves the displayed asymptotic for the exact individual summands, without approximating the full theta kernel by one summand on this translated square.

Finally log(1−b/r)≤−b/r eventually, so

0<W_jk≤(jk)^(−1/2)exp(−2nb/r)
          =(jk)^(4−h)≤(jk)^4 a^(−log(jk)).

Since jk>1 is fixed this tends to zero, proving the required local suppression. ∎

The square lies in min(|s+x|,|s−x|)>r/4 eventually. At least one of its p,q coordinates relative to the principal square is displaced by log 2/√2, so it is outside that square; it is also far from the negative-s square. The contribution can carry a nontrivial complex phase. Fixed-index suppression cannot be interchanged with an infinite sum without a uniform majorant and control of overlapping patches and complements. Reflected sectors likewise require their own analysis.

**Mathlib.** Full statement: not checked. Supporting theta summand formula, real changes of variables, Fresnel primitives, and Gaussian variation estimates: not checked. No library match is claimed. L269 supplies the exact summand and parameter identities; L278 supplies the proved real phase substitution and oscillatory rectangle argument. The shifted amplitude and weight estimates are proved here.
