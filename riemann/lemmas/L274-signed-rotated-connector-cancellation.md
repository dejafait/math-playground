# Lemma 274: signed rotated connectors cancel below the main scale

**Hypotheses.** Use the saddle quantities, actual holomorphic two-form ω, and simultaneous square rotation of L273. Thus a→∞, h~√a(log a)², d=n/r²=O(h/r), b=4h+d+4ia, θ=(arg b)/2, R=κh/a, and 0<κ<1/4 is fixed. Put

Q(p,q)=(bp²+2dpq+conj(b)q²)/2,
G=2π/√(det B),   C₀=(8π²)².

Orient the parameter cube [0,θ]×[−R,R]² by dα∧dy∧dz and its four side faces by the induced boundary orientations. The connector sum means the integral over these four faces together, with these orientations, under p=e^(−iα)y, q=e^(iα)z. Changing all orientations changes only its sign.

**Conclusion.** Both quadratic patch integrals, using dy dz orientation, satisfy

J₀:=∫_[−R,R]² exp(−Q(y,z)) dy dz=G+o(1/a),
Jθ:=∫_[−R,R]² exp(−Q(e^(−iθ)y,e^(iθ)z)) dy dz=G+o(1/a).

The quadratic connector sum and the actual connector sum obey respectively

|∫_sides exp(−Q) dp∧dq|=o(1/a),
|∫_sides ω|=o(exp(Φ_*)/a).

More explicitly, the normalized quadratic error relative to 1/a is bounded by a constant times

E=1/(√a R)+a hR⁴+(h/a)²+exp(−c aR²)=o(1).

For the actual connector sum add η=O(aR³+a^(−1)+exp(−c' h))=o(1) to this relative bound. This is a local cancellation theorem, not an estimate of the entire complementary contour or a new Laguerre positivity range.

**Proof.** The estimates proved in L273 give R→0, aR²→∞, hR²→0, aR³→0 and d=O(h/r)=O(h). Write A=4h+d. On the original real square,

Q(y,z)=2ia(y²−z²)+H(y,z),
H(y,z)=A(y²+z²)/2+d yz.

H is nonnegative, since its matrix has eigenvalues A±d≥4h, and H≤C hR². The elementary inequality 0≤1−exp(−H)≤H therefore gives

|J₀−|F_R|²|≤C hR⁴,
F_R=∫_(−R)^R exp(−2ia y²)dy.                         (1)

We include the needed Fresnel calculation. For a>0 the improper integral exists and

F∞=∫_ℝ exp(−2ia y²)dy=e^(−iπ/4)√(π/(2a)),
|F_R−F∞|≤C/(aR).                                    (2)

Indeed integration by parts using (exp(−2ia y²))'=−4ia y exp(−2ia y²) bounds each tail from R to infinity by C/(aR). To evaluate the integral without an unjustified limit, replace 2ia by ε+2ia with ε>0. The Gaussian formula ∫_ℝ exp(−z y²)dy=√π/√z holds for Re z>0: both sides are holomorphic there (domination on compact subsets justifies differentiating the integral), and equality for positive real z extends by the identity theorem, with the principal square root. The same integration by parts bounds each damped tail by C/(|ε+2ia|R), uniformly in ε≥0. Convergence on finite intervals and this uniform tail estimate permit ε↓0, proving (2).

Consequently

||F_R|²−π/(2a)|≤C[a^(−3/2)/R+a^(−2)/R²].             (3)

Since √a R→∞, the second term is bounded by the first eventually. Also L272 gives

det B=16a²+16h²+8hd,
G=π/(2a)[1+O((h/a)²)].                              (4)

Combining (1)–(4) proves |J₀−G|≤C E/a.

On the rotated square Q=(|b|(y²+z²)+2dyz)/2. Its real symmetric matrix has eigenvalues |b|±d~4a. Its full-plane Gaussian integral is G by L272, and the tail outside the square is at most C exp(−c aR²)/a. This follows by bounding the density by exp(−c a(y²+z²)) and integrating outside the radius-R disk. Thus |Jθ−G|≤C exp(−c aR²)/a.

For the orientation identity, the form Ω=exp(−Q)dp∧dq is closed: holomorphy makes its exterior derivative zero in two complex dimensions. Pull it back to the compact real parameter cube and apply Stokes. On each end face dp∧dq=dy∧dz; the end at θ has positive boundary orientation and that at zero negative orientation. Hence

∫_sides Ω=J₀−Jθ.                                    (5)

Corners are allowed in the elementary Stokes theorem for a rectangular cube, and no limit or infinite deformation is used. This proves the quadratic connector bound.

To transfer it to the actual integrand, u=(p+q)/√2 and x=(p−q)/√2 give ds∧dt=du∧dx=−dp∧dq. The uniform complex Taylor and theta-series estimates established in L273 yield on the entire homotopy

ω=−C₀ exp(Φ_*) exp(−Q)(1+ε(p,q)) dp∧dq,
sup|ε|≤C[aR³+a^(−1)+exp(−c' h)]=η.                  (6)

These are complex relative estimates, before taking moduli: the analytic phase remainder is O(aR³), and each kernel/model ratio is 1+O(a^(−1))+O(exp(−c' h)). All points stay inside the theta strips with clearance at least a fixed multiple of h/a, as proved in L273. The argument establishing its upper bound also gives ∫_sides |Ω|≤C/a (sum of four faces). Therefore (5)–(6) imply

|∫_sides ω|≤C exp(Φ_*)(E+η)/a.                       (7)

Finally, at this scale,

1/(√a R)=O((log a)^(−2)),
a hR⁴=O((log a)^10/√a),
(h/a)²=O((log a)^4/a),
aR²~κ²(log a)^4,
aR³=O((log a)^6/√a).

Every relative error tends to zero, proving (7) is the required little-o estimate. The signs assigned to individual faces are essential; the absolute mass result of L273 remains valid. ∎

In index terms this test lies at n~(1/2)√a(log a)³. It removes a local connector obstruction below L271's sufficient threshold but does not establish signs at that scale. The unrotated region outside the radius-R patch is not suppressed by the available modulus envelope, since hR²→0. A separate oscillatory estimate there remains necessary, as do the smaller indices and bounded heights required by the full witness target.

**Mathlib.** Full statement: not checked. Supporting complex Gaussian evaluation, identity theorem, integration by parts, Stokes theorem, and Gaussian tail estimates: not checked. No library theorem match is claimed. The Fresnel evaluation and tail bound are proved above rather than imported without a named reference. L272 supplies the quadratic diagonalization and determinant, and L273 supplies the strip-contained homotopy, complex model estimate, and absolute connector bound.
