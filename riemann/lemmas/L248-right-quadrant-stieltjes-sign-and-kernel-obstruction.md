# Lemma 248: the right-quadrant Stieltjes sign and its signed theta kernel

**Hypotheses.** Let K, F(z)=Ξ(i√z), and G=F′/F be the actual theta objects of L242, with F defined by its entire power series as in L246. Fix z=x+iy with x≥0 and y>0, and write its principal square root as w=a+ib, so a≥b>0. Set

C_z(u)=cosh(wu),   D_z(u)=u sinh(wu)/(2w),

J_z(u,v)=½ Im[D_z(u) conjugate(C_z(v))+D_z(v) conjugate(C_z(u))].

**Conclusion.** F(z)≠0, and the absolutely convergent identity

Im G(z)=|F(z)|^(−2)∫₀∞∫₀∞K(u)K(v)J_z(u,v)du dv<0

holds. For every such z, J_z takes both signs on open subsets of (0,∞)² of positive K(u)K(v) measure. The strict integrated right-quadrant sign also holds for both nonreal-zero examples of L247. It therefore does not imply a positive Stieltjes representation or RH.

**Proof.** The superexponential bound of L019 dominates any fixed exponential times any polynomial in u. Thus the integral of C_z is entire in z (its apparent square-root dependence is removed by its power series), and its derivative is the integral of D_z. Compact complex parameter sets admit integrable exponential-polynomial majorants, including at z=0. The integral agrees with F on the positive axis by L242 and hence everywhere by the identity theorem. Products of these integrable bounds justify Fubini for F′(z) conjugate(F(z)); symmetrizing in u,v proves the displayed identity wherever F≠0.

We first test the pointwise sign without estimating the weights. Since C_z(0)=1 and D_z(0)=0,

J_z(u,0)=u/[4(a²+b²)] [a cosh(au) sin(bu)−b sinh(au) cos(bu)].

At u=π/(2b) this is strictly positive, and at u=3π/(2b) it is strictly negative. Continuity extends each sign to an open rectangle with u>0 and v>0 sufficiently small. K is strictly positive there by L019, so both rectangles have positive weighted measure. The boundary evaluation is used only to locate interior rectangles, not as an assertion of positive mass on v=0.

For the integrated sign use the unconditional product and locally uniform logarithmic differentiation established in L246:

F(z)=F(0)Π_j(1+z/α_j²),   G(z)=Σ_j 1/(z+α_j²).

That lemma gives Σ_j|α_j|^(−2)<∞ and |arg α_j²|<1/4. Thus writing α_j²=A+iB gives A>|B| and A>0. Every product zero −α_j² lies strictly in the left half-plane. The locally uniformly convergent product has no other zeros: away from its factors' zeros its tail has an absolutely convergent logarithm. Consequently F(z)≠0 on x≥0. On each compact subset there, the series for G converges absolutely locally uniformly, since sufficiently large |α_j| have |z+α_j²|≥|α_j²|/2.

Real squared nodes A>0 contribute Im(1/(z+A))=−y/((x+A)²+y²)<0. Nonreal nodes occur in conjugate pairs with equal multiplicities. Put q=x+A. Directly combining the two imaginary parts gives

Im[1/(z+A+iB)+1/(z+A−iB)]
=−2y(q²+y²−B²)/[(q²+(y+B)²)(q²+(y−B)²)]<0,

because q≥A>|B|. Absolute convergence permits this pairing. The zero set is nonempty by L246, proving strict negativity of the total sum.

For L247's polynomial example the squared nodes are 25 and 1599/16±5i, all satisfying A>|B|. Its cosine-augmented example adds the positive real nodes λ_n=10000π²(n+1/2)² with summable reciprocals. The same calculation therefore gives strict negativity throughout x≥0,y>0 for both examples. L247 proves that neither has a positive Stieltjes representation and both have nonreal zeros. This proves the claimed insufficiency. ∎

The achieved sign covers the entire closed right half of the upper half-plane, but the Stieltjes target requires holomorphy and nonpositive imaginary part on the full upper half-plane. Indeed a positive Stieltjes integral satisfies Im G(x+iy)=−y∫|x+iy+t|^(−2)dν(t)≤0 wherever y>0. The integrability contract in L247 justifies this identity. The conjugate-pair numerator above can change sign when x is negative; its right-quadrant proof gives no continuation of the inequality there. Nor does holomorphy on the right exclude poles on the left. The positive and negative theta-integrand regions do not contradict the integrated sign and give no quantitative obstruction to a different cancellation argument.

**Mathlib.** Not checked: coverage of the full statement, holomorphic parameter integration, and the supporting product and conjugate-pair identities was not checked. No matching library theorem is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/
