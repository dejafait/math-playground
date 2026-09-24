# Lemma 341: a geometric obstruction to uniform endpoint phase-box returns

**Hypotheses.** Let y≥3, let p_1,…,p_d be all primes at most y,
and let 0<ε<π. On the torus 𝕋^d=(ℝ/(2πℤ))^d use normalized
Haar measure μ, which is Lebesgue measure divided by (2π)^d on
a fundamental cube. Put

v=(log p_1,…,log p_d),  Θ_y=Σ_(j=1)^d log p_j,
ρ=ε/π,  ϑ(a)=−av mod 2π,
B={θ: dist_(ℝ/(2πℤ))(θ_j,π)≤ε for every j}.

For H≥0 define the compact swept set

E_H=B+[0,H]v={θ+tv mod 2π: θ∈B, 0≤t≤H}.          (1)

A starting phase x belongs to E_H exactly when x−tv enters B
for some t∈[0,H]. In the endpoint application let

y=exp(6sqrt(r)),  ε=1/10,  H=exp(2r),

with r tending to infinity through positive real values. This is
L339's sufficient negative phase box. Write
c=(log 2)log(10π)/24>0.

**Conclusion.** For every y, ε and H as above,

μ(E_H)≤min{1, ρ^d[1+HΘ_y/(2ε)]}.                  (2)

Whenever the second bound is less than one, for every A_0≥0
there is b≥A_0 such that

ϑ(a)∉B for every a∈[b,b+H].                        (3)

Consequently any length H with a visit to B in every translated
interval [b,b+H], even if this is required only for all sufficiently
large b, necessarily satisfies

H≥(2ε/Θ_y)(ρ^(−d)−1).                             (4)

At the endpoint cutoff, for all sufficiently large r,

μ(E_(exp(2r)))≤exp(−c exp(6sqrt(r))/sqrt(r))<1.       (5)

The same upper bound holds eventually if log H=2r+O(1), with any
fixed bound on the O(1) term. Every uniform return length as in
(4) instead has

log H≥c exp(6sqrt(r))/sqrt(r).                      (6)

Thus actual empty translated intervals of length exp(2r) exist at
arbitrarily large starting heights for each fixed sufficiently large
r. This is an obstruction to the uniform full-box return target,
independent of the Fourier certificate in L340. It is not a lower
bound on the first visit from a specified starting height, and it
does not decide whether [a_n,2a_n] contains a visit, where
a_n=sqrt(4π²exp(4r)−25), r=2n.

L339 still gives negative endpoint arithmetic values of magnitude
at least ζ(2)²/(8r) at every visit, for large r. Avoiding its box
does not imply nonnegativity: the box is a sufficient condition,
not the whole negative set. No value at a_n, Laguerre sign,
zero-exclusion range, or RH candidate follows here.

**Proof.** We first prove the volume estimate without any
equidistribution assumption. Lift B to the translate by
(π,…,π) of Q=[−ε,ε]^d. Translation preserves μ, so it suffices
to bound the projection of

K=Q+[0,H]v⊂ℝ^d.

Every v_j is positive. For j=1,…,d let F_j be the face of Q
on which the jth coordinate equals ε. Then

K⊂Q ∪ ⋃_(j=1)^d (F_j+[0,H]v).                    (7)

To verify (7), write x=q+tv with q∈Q and 0≤t≤H. If x∉Q,
some coordinate exceeds ε, since every coordinate is at least
−ε. Define

t_0=max_j (x_j−ε)/v_j>0.

For every j, x_j≤ε+tv_j, so t_0≤t. Put q_0=x−t_0v.
The definition of the maximum gives q_(0,j)≤ε for every j
and equality for at least one. Also
q_(0,j)=q_j+(t−t_0)v_j≥−ε. Hence q_0 belongs to an F_j
and x∈F_j+[0,H]v, proving the covering.

The volume of each face prism is

vol(F_j+[0,H]v)=Hv_j(2ε)^(d−1).                    (8)

Indeed its jth coordinate determines t uniquely by
x_j=ε+tv_j. For every such coordinate in [ε,ε+Hv_j],
the other coordinates form a translate of [−ε,ε]^(d−1).
Fubini's theorem gives (8), including the zero-volume case H=0.
Subadditivity in (7) now gives

vol(K)≤(2ε)^d+HΘ_y(2ε)^(d−1).                     (9)

Projection to the torus cannot increase normalized volume.
To see this explicitly, partition K into its intersections with
the half-open cubes [0,2π)^d+2πk, k∈ℤ^d. Only finitely many
occur, since K is compact. Translate each piece into [0,2π)^d;
their union represents the torus projection. Subadditivity and
translation invariance bound its measure by vol(K)/(2π)^d.
Applying this to (9), and also using μ(𝕋^d)=1, proves (2).
This argument permits arbitrary overlaps and arbitrarily many
windings of the swept set.

We next justify the forward-orbit density needed for (3),
including visits after any prescribed A_0. Let U be any nonempty
open subset of the torus. It contains an open coordinate box
of some radius δ∈(0,π) about η=(η_1,…,η_d). For integers m≥1
set

g_m(θ)=∏_(j=1)^d [(1+cos(θ_j−η_j))/2]^m,
q=cos²(δ/2)<1.

This is a nonnegative finite trigonometric polynomial bounded
by one, and g_m≤q^m outside that box. Its constant coefficient is

b_m=[binom(2m,m)/4^m]^d≥(2m+1)^(−d).                (10)

For one factor the formula follows by expanding
4^(−m)(2+exp(iu)+exp(−iu))^m; the constant coefficient is
4^(−m)binom(2m,m). Translating u changes no constant coefficient.
For the inequality, the largest of the 2m+1 binomial coefficients
whose sum is 4^m is the central one. Since d and δ are fixed,
choose m so large that b_m>q^m: an exponential decay q^m
is eventually smaller than (2m+1)^(−d).

For any nonzero integer vector k, unique prime factorization gives

ω_k=Σ_j k_j log p_j≠0.                             (11)

Otherwise the products of the primes with their positive and
negative exponents would be equal integers, forcing k=0.
Direct integration gives, for T>0,

|(1/T)∫_(A_0)^(A_0+T)exp(−iaω_k)da|
                                      ≤2/(T|ω_k|).

There are finitely many Fourier terms in g_m. Thus the average
of g_m(ϑ(a)) on [A_0,A_0+T] tends to b_m as T→∞. If the
forward orbit after A_0 never entered the chosen box, every
such average would be at most q^m, contradicting b_m>q^m.
It follows that the forward orbit visits every nonempty open
set after any A_0. This is a finite Fourier proof of density;
no quantitative rate uniform in d is asserted or needed.

If the second bound in (2) is less than one, the compact set
E_H has a nonempty open complement. By this density there is
b≥A_0 with ϑ(b) outside E_H. The defining equivalence in (1)
then gives (3), including both interval endpoints. Conversely,
if every interval starting after some A_0 contains a visit,
every point of the dense forward orbit after A_0 lies in E_H.
As E_H is closed, it must be the whole torus. In that case
1=μ(E_H)≤ρ^d[1+HΘ_y/(2ε)], which rearranges to (4).

It remains to compare the actual scales. L340 proves by a
central-binomial prime valuation argument the elementary bound

d≥(log 2)y/(2log y)  for y≥16.                     (12)

The trivial upper bound d≤y also gives Θ_y≤y log y. At
ε=1/10 put ℓ=log(10π)>0. For H=exp(2r) and large r,
HΘ_y/(2ε)≥1. Taking the logarithm of the second quantity
in (2), and using 1+x≤2x for x≥1, gives

log(ρ^d[1+HΘ_y/(2ε)])
 ≤−dℓ+2r+log Θ_y+log 10
 ≤−[(log 2)ℓ/2]y/log y
                      +2r+log y+log log y+log 10.  (13)

When y=exp(6sqrt(r)), the positive terms in (13) are
o(y/log y). They are therefore at most half of the magnitude
of the displayed negative term for all sufficiently large r.
This gives (5), since

[(log 2)ℓ/4]y/log y
                     =c exp(6sqrt(r))/sqrt(r).

Replacing 2r by 2r+O(1) in (13) proves the stated extension.
This includes lengths comparable to a_n, because
log a_n=2r+log(2π)+o(1) on r=2n.

Finally, at this ε and y one has ρ^d≤1/2. Equation (4) and
Θ_y≤y log y imply, for every uniform return length,

H≥ε ρ^(−d)/(y log y),
log H≥dℓ−log y−log log y−log 10
 ≥[(log 2)ℓ/2]y/log y−log y−log log y−log 10.

Again absorbing the lower-order terms by half of the leading
term proves (6). Its right side divided by 2r tends to infinity.
This is a necessary lower bound for a length that works for
every translate; it is not a necessary waiting time from every
individual starting height.

All density arguments fix r, hence d and H, before choosing
the arbitrarily late b. They impose no relation between that b
and the prescribed a_n. L339's box only supplies a sufficient
negative-sign condition, so neither the covering deficit nor
the empty intervals imply a sign for its complement. This
preserves the endpoint and low-index qualifications. ∎

**Mathlib.** Full statement: not checked. Coverage of the swept
box volume, torus projection, forward-orbit density and geometric
uniform-return obstruction is not checked. No full matching
theorem or absence from checked sources is claimed.

The finite Fourier density argument, including the binomial
mean and unique-factorization step, is proved above. The only
imported mathematical estimates are L340's elementary prime-count
bound and L339's conditional negative arithmetic consequence;
their qualifications are retained. No new library result or
external analytic theorem is imported. The volume proof and
asymptotic comparisons are analytic and need no numerical
prime table or computation of a return time.
