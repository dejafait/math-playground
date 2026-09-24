# Lemma 325: below-five interior stationary sum with an additive error

**Hypotheses.** Use L323's exact theta summands F_jk and parameters

h=39/8, r=8n/3, p=2n=3r/4,
2πexp(2r+2iτ)=h+ia, a>0, 0<τ<π/4,
Φ_*=p log r+9r−h−2aτ, C₀=(8π²)²,

with integer n tending to infinity. Thus a~2πexp(2r). Put u=s+x, v=s−x and

D={u>r/20, v>r/20},
I_D=∫_D Σ_(j,k≥1) F_jk(s,x) ds dx,

where ds dx=(1/2)du dv is positive area measure. For x,y≥1 define

W_r(x,y)=(xy)^(−1/2)(1−log(xy)/(2r))^(3r/4)

when log(xy)<2r, and W_r(x,y)=0 otherwise. Define the finite real phase sum

S_r(a)=Σ_(j,k≥1) W_r(j,k)exp(ia log(k/j)).

The cutoff in W_r is part of its definition; its polynomial is not extended past that cutoff.

**Conclusion.** The theta expansion is absolutely integrable termwise on D for each sufficiently large admissible r, and

I_D=C₀exp(Φ_*) π/(2a) [S_r(a)+R_r],
|R_r|≤C(1+r)²exp(−r/200)=o(1).                         (1)

More explicitly the normalized error is bounded by a constant times

(1+r)²exp(r/24)a^(−1/10)
 +(1+r)²exp(−r/200)+exp(19r/80)a^(−1/2).                (2)

Thus the entire interior meets the required additive error o(exp(Φ_*)/a), uniformly over its growing theta indices. This is not a relative error against a proved positive S_r(a). No lower bound for that sum, Laguerre sign, or new zero-exclusion range is asserted.

**Proof.** First bound the coefficient mass and the moving-boundary tail. The function W_r decreases in each coordinate: on its positive support its logarithmic derivative with respect to log x is

−1/2−p/(2r−log(xy))<0,

and it tends continuously to zero at the cutoff. Put

Q_r(L)=exp(L/2)(1−L/(2r))^(3r/4), 0≤L<2r,

and extend it by zero. The inequality log(1−t)≤−t−t²/2, obtained by differentiation from t=0, gives

log Q_r(L)≤L/8−3L²/(32r)
 =r/24−3(L−2r/3)²/(32r)≤r/24.                       (3)

Monotone integral comparison twice and the substitutions x=exp(u), y=exp(v) yield

M_r:=Σ_jk W_r(j,k)
 ≤1+2∫₀^(2r) Q_r(L)dL+∫₀^(2r) LQ_r(L)dL
 ≤C(1+r)²exp(r/24).                                   (4)

In particular no bounded-mass or harmonic-mass estimate is assumed below five.

Fix ε=1/100. The tail needed for clipping is

Σ_(max(log j,log k)≥19r/20−ε) W_r(j,k)
 ≤C(1+r)²exp(−r/200).                                 (5)

To prove it, let K=ceil(exp(19r/20−ε)) and B=log(K−1). For large r, K≥2 and B≥47r/50, since K−1≥exp(19r/20−ε)/2. Monotonicity gives

Σ_(j≥K,k≥1) W_r(j,k)
 ≤∫_(K−1)^∞ [W_r(x,1)+∫₁^∞ W_r(x,y)dy]dx
 ≤∫_B^(2r) (1+L)Q_r(L)dL.                            (6)

For L≥47r/50 and L<2r,

(log Q_r)'(L)=1/2−(3r/4)/(2r−L)≤−11/53<0.

Also Q_r(47r/50)=exp(r[47/100+(3/4)log(53/100)]). To verify the rate exactly, put q=47/153. Integrating the geometric series for 1/(1−q²) gives

log(100/53)=2Σ_(m≥0)q^(2m+1)/(2m+1)
 >2(q+q³/3)>19/30.

The last rational difference is 39877/107447310. Consequently Q_r(L)≤exp(−r/200) throughout this tail. Equation (6), its transposed version, and a union bound prove (5). All sums here are finite because W_r has a product cutoff.

Next control the full nonstationary complement with the moving domains retained. For each j,k write

y=u−r+log j, z=v−r+log k,
α_j=log j−19r/20, α_k=log k−19r/20.

Then D becomes the rectangle y>α_j, z>α_k. L323's exact algebra gives

F_jk=C₀exp(Φ_*)exp(ia log(k/j)) H_jk(y,z)
      ·exp(if_a(y)−if_a(z)),
f_a(t)=a(t−exp(2t)/2),
H_jk=(jk)^(−1/2)((2r−log(jk)+y+z)/(2r))^p
 ·exp((9/2)(y+z)−(h/2)(exp(2y)+exp(2z)−2)) E,
E=(1−3exp(−2y)/(2V_+))(1−3exp(−2z)/(2V_-)),
V_±=πexp(2r±2iτ), |V_±|=sqrt(a²+h²)/2.                (7)

The polynomial argument is positive on D. The translations have Jacobian one in du dv, so the measure in (7) is (1/2)dy dz. L323's tangent-polynomial derivative estimate on the whole positive quadrant gives, for d,e∈{0,1},

|∂_y^d∂_z^e H_jk|≤C(jk)^(−7/8) M(y)M(z),
M(t)=(1+exp(2t))exp(h t−(h/2)(exp(2t)−1)).             (8)

For clarity, this estimate only uses the bounds for the first two derivatives of P(w)=(w/(2r))^p by Cexp((3/8)(w−2r)). Replacing P by this exponential gives the factor (jk)^(4−h)=(jk)^(−7/8) exactly. Differentiating the remaining exponentials gives factors 9/2−h exp(2y) and 9/2−h exp(2z), absorbed in M. The original factors E_j(u) and their first derivatives are bounded for u≥0; hence (8) uses no division by a possibly vanishing E and no summation of the divergent unweighted powers.

Define B(α)=sup_(t≥α)M(t)+∫_α^∞ M(t)dt. Substitution q=exp(2t) gives

M(t)=exp(h/2)(1+q)q^(h/2)exp(−hq/2), dt=dq/(2q).

The supremum and integral over the whole line are finite, since h>0. For q≥1 the polynomial factors, both before and after division by q, can be absorbed into exp((h/2−1)q), since h/2>1. Thus

B(α)≤C if α≤0, and B(α)≤Cexp(−exp(2α)) if α≥0.         (9)

Let J=exp(19r/20). Equations (9) and exp(2α_j)=(j/J)² imply

Σ_(j≥1) j^(−7/8)B(α_j)≤C J^(1/8).                    (10)

Indeed the head is bounded by 1+∫₁^J x^(−7/8)dx≤8J^(1/8). The decreasing tail is bounded by a first term and an integral of x^(−7/8)exp(−(x/J)²); substitution x=Jt bounds it by C J^(1/8). This also covers nonintegral J.

Equation (8) therefore proves the absolute-integrability estimate

Σ_jk ∫_(α_j)^∞∫_(α_k)^∞ |H_jk(y,z)|dy dz
 ≤C J^(1/4)=Cexp(19r/80)<∞.                           (11)

After the translations this is exactly a sum of integrals on the same original sector D. The exact theta series there and Tonelli/Fubini justify termwise integration for each parameter, without interchanging a limit in r with this bound.

On any rectangle in the translated domain, (8) bounds its rectangular variation (upper corner value, two upper-edge derivative integrals, and mixed-derivative area integral) by

C(jk)^(−7/8)B(α_j)B(α_k).                            (12)

The primitive of exp(±if_a(t)) on any interval is O(a^(−1/2)); on an interval wholly outside [−ε,ε] it is O(a^(−1)). These are the elementary bounds in L323: f'_a=a(1−exp(2t)) is monotone, one removes |t|≤a^(−1/2), and on each remaining side integration by parts bounds the integral by reciprocal endpoint slopes and the variation of 1/f'_a. Those slopes have size at least a constant times sqrt(a), or at least a constant times a on either fixed tail.

Assign to each summand the square Q_jk={|y|,|z|≤ε}. The complement of Q_jk in its translated D is at most four rectangles: the two y tails with all z, then the two z tails with |y|≤ε. Empty rectangles contribute zero. One coordinate in each rectangle has the tail primitive bound. Anchor the primitives at the lower endpoints of a finite truncation and integrate by parts in both coordinates. Their product is O(a^(−3/2)); the upper corner and both upper edges remain in (12), while the lower terms vanish. Passing to unbounded rectangles is allowed by (11). If K_jk denotes the original summand integral over D outside Q_jk, (10)–(12) show

Σ_jk |K_jk|≤Cexp(Φ_*)a^(−3/2)exp(19r/80).              (13)

This includes every boundary term and every theta index, even when its stationary point is outside D.

It remains to evaluate the clipped patches uniformly. Such a patch is nonempty only if log j,log k<19r/20+ε. For these indices put ℓ=log(jk) and d_jk=2r−ℓ. Then

d_jk>r/10−2ε≥r/11

for sufficiently large r, and W_r(j,k)>0. On the full fixed square, including any part outside D, factor (7) as

H_jk=W_r(j,k) A_jk(y,z) E,
A_jk=exp(p log(1+(y+z)/d_jk)+(9/2)(y+z)
          −(h/2)(exp(2y)+exp(2z)−2)).                 (14)

For large r, d_jk+y+z≥r/12 on the square. The ratios p/(d_jk+y+z) and p/(d_jk+y+z)² are uniformly bounded; the logarithmic term itself is bounded by the mean value theorem. Thus A_jk and its derivatives through order two are bounded uniformly in every nonempty clipped index pair, and A_jk(0,0)=1. On this square E−1 and its first and mixed derivatives are O(1/a). In particular, applying two unrestricted primitive bounds and the rectangular variation identity to any clipped rectangle gives

|C_jk|≤Cexp(Φ_*)W_r(j,k)/a,                           (15)

where C_jk is its original summand integral. The same bound applies to a full assigned square. There are finitely many nonempty clipped patches.

Here is a quantitative uniform evaluation of a full square. Use the smooth increasing real change

Y=g(y), Z=g(z),
g(t)=sgn(t)sqrt((exp(2t)−1−2t)/2), g'(0)=1.

The quotient of the radicand by t² extends smoothly and positively through zero, so g and its inverse have bounded required derivatives on the fixed interval. It changes the phase to −aY²+aZ². The transformed A_jk including its Jacobian has bounded first and mixed derivatives, value one at (0,0), and uniformly bounded rectangular variation. Put ρ=a^(−2/5). Replacing this amplitude by one on |Y|,|Z|≤ρ costs O(ρ³). On the at most four remaining rectangles one Fresnel primitive is O(1/(aρ)), the other O(a^(−1/2)); integration by parts bounds them by O(a^(−3/2)/ρ). The constant central integral differs from the product of the opposite full Fresnel integrals π/a by O(a^(−3/2)/ρ+a^(−2)/ρ²). Finally the transformed factor E−1 has variation O(1/a), so its signed integral is O(a^(−2)). These are the real phase and elementary Fresnel calculations used in L323, with the uniform derivative bounds now supplied by (14).

Since ρ³=a^(−6/5), a^(−3/2)/ρ=a^(−11/10), and a^(−2)/ρ²=a^(−6/5), the full square integral J_jk therefore satisfies

J_jk=C₀exp(Φ_*)exp(ia log(k/j))W_r(j,k)
       ·[π/(2a)+O(a^(−11/10))].                      (16)

The factor 1/2 is exactly the Jacobian from du dv to ds dx. No constant in this error depends on the growing indices.

Call a pair good if log j,log k<19r/20−ε. Its full square lies in D, so C_jk=J_jk. Summing the error in (16) over good pairs and using (4) costs, after normalization by C₀exp(Φ_*)π/(2a), at most

C(1+r)²exp(r/24)a^(−1/10).                            (17)

Every other nonempty clipped pair has max(log j,log k)≥19r/20−ε. Its contribution is bounded by (15) and (5). Replacing the good leading sum by the full S_r(a) has the same tail bound (5), including all indices outside the geometric stationary domain. Hence the normalized clipped sum differs from S_r(a) by at most the first two terms of (2). This replacement is justified by a tail tending to zero in absolute mass, not by a fixed-index limit.

Termwise integration and the summand-wise partition give I_D=Σ_jk(C_jk+K_jk). Adding (13) proves (2). Since a~2πexp(2r), its first term is O((1+r)²exp(−19r/120)) and its third is O(exp(−61r/80)). Both rates are strictly faster than 1/200. This proves (1) at the required scale. Symmetry under j↔k makes S_r(a) real; swapping u,v conjugates the exact sector integrand and preserves D, so I_D and R_r are real as well. ∎

The stationary family in L323 is retained in this main sum, rather than discarded as a boundary error. L324 and C294b separately control the smaller same-sign boundary and mixed sectors. A whole-plane assembly must retain their reflection and normalization factors, and positivity would still require a positive arithmetic margin exceeding its total error. Neither the exponential mass bound (4) nor the additive approximation proves such a margin. The statement is only on the displayed admissible parameter sequence; no rounding to an integer n at every height is asserted.

**Mathlib.** Full statement: not checked. Supporting monotone sum-integral comparison, logarithmic inequalities, geometric-series integration, Fresnel integrals, smooth inverse substitution, rectangular integration by parts, and Tonelli/Fubini: not checked. No full or supporting library match is claimed. L323 supplies the exact below-five summands, normalization, tangent derivative and primitive bounds, and the real phase calculation; their index-dependent use is checked above. The coefficient mass, clipping tails, moving-domain sum, and uniform interior approximation are proved here. L299–L300 are endpoint precedents, not inputs applied outside their hypotheses; no result requiring h≥5 is invoked at h=39/8.
