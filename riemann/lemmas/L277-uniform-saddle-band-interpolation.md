# Lemma 277: uniform interpolation between the saddle sign ranges

**Hypotheses.** Use the actual theta integral I_n(a), saddle parameters r,h,τ, phase Φ_*, and matrix B of L269. Let a→+∞, write L=log a, and let n≥1 be an integer such that

√a L²≤h≤a^(3/4)L³.

**Conclusion.** Uniformly over these integers, with the positive square root,

I_n(a)=(8π²)² exp(Φ_*) 4π/√(det B) · (1+o(1)).

Consequently D_n(Ξ;a)>0 throughout this range eventually. In combination with L271, for every fixed C>0 the same asymptotic and positivity hold uniformly for

ceil(√a L³)≤n≤Ca.

Evenness gives the corresponding assertions for |a|→∞. The lower threshold still diverges; this does not prove every sign required by L266.

**Proof.** We extend the estimates underlying L273–L275, checking their hypotheses again rather than applying their narrow-band statements outside their ranges. Fix 0<κ<1/4, and set

R=κL²/√a,   ε=√(ML/h),

where M>0 is a sufficiently large fixed constant chosen below. The exact saddle identities give

r=(1/2)log(a/(2π))+(1/4)log(1+(h/a)²)~L/2,
n=r(h−9/2),   d=n/r²=O(h/r),
δ=cos(2τ)=h/√(a²+h²),   det B=16a²+16h²+8hd~16a².

All statements here and below are uniform on the stipulated interval. In particular h/a→0, n≤a eventually, n≥c√a L³, and δ^(−5)≤C_1 a^(5/2). The elementary radius checks are

R≤κh/a,   aR²=κ²L⁴→∞,
aR³=κ³L⁶/√a→0,
hR²≤κ²a^(−1/4)L⁷→0,
a hR⁴≤κ⁴a^(−1/4)L^11→0,
(R/ε)²=hR²/(ML)≤(κ²/M)a^(−1/4)L⁶→0.

Also ε→0, with its maximum at the lower endpoint of the h interval. These checks allow the inner square to stay fixed in h even while the outer square shrinks.

For the inner square put u=s−r, p=(u+x)/√2, q=(u−x)/√2 on the shifted contour t=x+iτ. Define b=4h+d+4ia and θ=(arg b)/2. The quadratic form is

Q(p,q)=(bp²+2dpq+conj(b)q²)/2.

Use the homotopy p=e^(−iα)y, q=e^(iα)z, 0≤α≤θ, |y|,|z|≤R. Its maximum imaginary displacement in either kernel argument is at most √2R. The original strip clearance is ρ=(1/2)arctan(h/a)~h/(2a). Since R≤κh/a and √2κ<1/2, the whole homotopy has clearance at least c h/a. Real parts of its kernel arguments are r+O(R), so for v=πexp(2(s±t)) one has |v| comparable to a and Re v≥c h. The exact theta series in L269 gives kernel/model ratio 1+O(a^(−1)+exp(−c h)). The third derivatives of the analytic phase are O(a+n/r³)=O(a) throughout the homotopy. Taylor's formula therefore gives a complex relative error

η=O(aR³+a^(−1)+exp(−c h))=o(1)

between the actual holomorphic form and (8π²)² exp(Φ_*) times its quadratic form, with the fixed coordinate orientation understood.

We now verify signed connector control. On the original real square,

Q(y,z)=2ia(y²−z²)+H(y,z),
H=(4h+d)(y²+z²)/2+d yz≥0,   H≤C_2 hR².

Thus its quadratic integral J₀ differs from |∫_(−R)^R exp(−2ia y²)dy|² by O(hR⁴). The Fresnel evaluation and tail estimate proved in L274 give

J₀=π/(2a)+O(1/(a^(3/2)R)+hR⁴).

Here the smaller squared-tail term is absorbed because √a R→∞. The full rotated Gaussian value is G=2π/√(det B)=π/(2a)[1+O((h/a)²)]. On the final rotated square Q is real positive definite, with eigenvalues |b|±d comparable to a. Its integral Jθ consequently differs from G by O(exp(−c aR²)/a). Hence

|J₀−G|+|Jθ−G|≤C_3 E/a,
E=1/(√a R)+a hR⁴+(h/a)²+exp(−c aR²)=o(1).

The signed sum over the four connector faces equals J₀−Jθ by Stokes, with the orientations in L274. The absolute mass of these faces is still O(1/a): on each face the Jacobian has modulus R, and the real exponent is

T(α)(R²+z²)/2+d(±R)z,
T(α)=(4h+d)cos(2α)+4a sin(2α)≥c(h+aα).

Because dR²=O(hR²)=o(1), integration bounds this mass by

C_4 R(2R)∫_0^∞ exp(−c aαR²)dα≤C_5/a.

Multiplying by η transfers the signed estimate to the actual form with additional error O(exp(Φ_*)η/a). Its rotated patch also has absolute mass O(exp(Φ_*)/a). Stokes therefore shows that the actual original inner patch contributes

(8π²)² exp(Φ_*)[G+O((E+η)/a)].

The coordinate map has ds∧dt=−dp∧dq; the inherited orientation cancels this fixed sign, as in L274. No individual connector is discarded in modulus.

For the surrounding real square annulus R≤max(|p|,|q|)≤ε, use the exact phase from L275, with v=(p+q)/√2:

exp(Φ−Φ_*)=A(p,q)exp(if(p)−if(q)),
f(y)=−(a/2)(exp(2√2y)−1−2√2y),
A=exp(S),
S=2n log(1+v/r)+9v−(h/2)(exp(2√2p)+exp(2√2q)−2).

The conditions needed in that proof are ε→0, r→∞, and n/r²=O(h/r); all hold uniformly here. Direct differentiation gives −C_6 h I≤Hess S≤−c h I, ∇S(0)=0, and |S_pq|≤C_6 h. Thus A and its first and mixed derivatives have exactly the Gaussian bounds (1) in L275, whose integrated mixed variation on every rectangle is uniformly bounded by scaling with √h. Since |f''| is comparable to a, the primitive estimates there are C_7/√a on every subinterval and C_7/(aR) on each tail interval. Partitioning the annulus into four rectangles and applying the finite-rectangle integration identity in L275 gives model mass O(1/(a^(3/2)R)). The actual kernel/model error on this real square is O(a^(−1)+exp(−c h)); its modulus integral is O(1/h). Consequently the actual annulus contributes at most

C_8 exp(Φ_*)[1/(a^(3/2)R)+(a^(−1)+exp(−c h))/h].

Relative to exp(Φ_*)/a this is O(L^(−2)+h^(−1)+(a/h)exp(−c h))=o(1) uniformly.

Finally the outer p,q square contains the u,x square of radius e=ε/√2. Its reflection contains the analogous negative-saddle square. The absolute integral over the complement of the two outer squares is therefore at most the complement estimate for the two smaller u,x squares. The envelope comparison in L269, equations (7)–(10), applies with radius e: h≥1, e→0, r→∞, and e/(r−e)≤exp(−1/2) uniformly. It gives the bound

C_9 δ^(−5) exp(Φ_*)[(r+1)²exp(−c h e²)+exp(−n)].

The first term controls both radial and transverse exterior regions; the second retains the polynomial factor in the swapped boxes near s=0, |x|=r. Thus no competing envelope maximum is omitted. Dividing by exp(Φ_*)/a and using he²=(M/2)L bounds the result by

C_10 a^(7/2)[L²a^(−cM/2)+exp(−c'√a L³)].

Choose fixed M with cM/2>5. This tends uniformly to zero. All local limits above remain valid for this choice. By exact evenness in s, the negative outer square contributes equally to the positive one. Summing the patches, annuli, and exterior proves I_n(a)=(8π²)²exp(Φ_*)[2G+o(1/a)], as asserted. The integral is real, G~π/(2a)>0, and the multiplier relating I_n to D_n in L269 is positive.

For the claimed combined n interval, split at N₁=ceil(a^(3/4)L³). On ceil(√a L³)≤n<N₁ one has n≤a eventually and hence r~L/2 uniformly from the saddle identities. It follows that

h≥(2+o(1))√a L²>√a L²,
h≤(2+o(1))a^(3/4)L²<a^(3/4)L³.

Thus the interpolation just proved applies. On N₁≤n≤Ca use L271. Both statements have the identical positive leading term and uniform little-o error, so their union is uniform. This checks overlap in the actual index, without equating h and n. Evenness completes the proof. ∎

The achieved range starts at a sublinear but unbounded index. L266 requires every index from 1 through its height-only cutoff; lower indices and bounded exterior heights remain unresolved. No RH candidate is obtained.

**Mathlib.** Full statement: not checked. Supporting Stokes theorem, Fresnel and Gaussian integration, finite-rectangle integration by parts, theta estimates, and uniform asymptotics: not checked. No library match is claimed. The Fresnel and rectangle estimates used above are proved in L274 and L275; the theta and global envelope estimates are proved in L269. L271 supplies the higher-index range used only in the combined conclusion.
