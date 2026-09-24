# Lemma 343: a geometric return obstruction for the aggregate endpoint region

**Hypotheses.** Let r tend to infinity through positive real values.
Put L=sqrt(r), y=exp(6L), σ=1+1/(2L), and, for each prime p≤y,

q_p=p^(−σ),
d_r(p)=(log p)q_p(1+q_p)/(1−q_p)^3.

On the finite torus 𝕋^(π(y)) use normalized product Haar measure μ.
Write v=(log p)_(p≤y) and define the closed budget region

B_r(θ)=Σ_(p≤y)d_r(p)(1−cos θ_p),
A_r={θ: B_r(θ)≤L/32}.

This is L342's sufficient negative region, with
ω(p)=−exp(iθ_p). For H≥0 let

E_(r,H)=A_r+[0,H]v.

The actual relative phases are
φ_r(a)=(π−a log p)_(p≤y) mod 2π, so a starting phase belongs
to E_(r,H) exactly when its forward flow with velocity −v enters
A_r within time H. The coupled heights are
a_n=sqrt(4π²exp(4r)−25), r=2n.

**Conclusion.** For all sufficiently large r, with the starting
threshold independent of H, one has, for every H≥0,

μ(E_(r,H))≤min{1, (1+1344H sqrt(r))
                         exp(−exp(4sqrt(r))/2304)}.       (1)

In particular, eventually,

μ(E_(r,exp(2r)))≤exp(−exp(4sqrt(r))/4608)<1.              (2)

The same bound holds when log H=2r+O(1), with any fixed bound
on the O(1) term. For each fixed sufficiently large r, and every
A_0≥0, there is b≥A_0 such that

φ_r(a)∉A_r for every a∈[b,b+exp(2r)].                     (3)

Any length H that gives a visit in every translated interval
[b,b+H], even only for all sufficiently large b, must satisfy

H≥[exp(exp(4sqrt(r))/2304)−1]/(1344sqrt(r)),              (4)
log H≥exp(4sqrt(r))/4608                                 (5)

for all sufficiently large r. This logarithmic lower bound
exceeds the required 2r by a diverging factor.

Thus L342's enlargement does not restore uniform return on the
coupled height scale. This is a failure of that uniform target,
not merely of an absolute Fourier certificate. It does not locate
an empty interval near a_n or determine a first visit from a
specified starting height. A visit retains L342's negative
arithmetic consequence, but missing a sufficient negative region
does not sign its complement. No value at a_n, Laguerre sign,
zero-exclusion range, or RH candidate is obtained.

**Proof.** We first prove a lower bound for the total weight of
a thick prime shell. Put

I_r={p: exp(4L)<p≤exp(6L)},
M_r=Σ_(p∈I_r)d_r(p).

L338 derives from the standard Mertens third theorem the asymptotic

P(x):=Σ_(p≤x)1/p=log log x+B+o(1).

Write P(exp u)=log u+B+ε(u), where ε(u)→0. With
f_L(u)=u exp(−u/(2L)), Stieltjes partial summation gives

Σ_(p∈I_r)(log p)p^(−1−1/(2L))
 =∫_(4L,6L] f_L(u)dP(exp u)
 =∫_(4L)^(6L) exp(−u/(2L))du+o(L)
 =2L(exp(−2)−exp(−3))+o(L).                            (6)

For completeness, the error in the second equality equals

f_L(6L)ε(6L)−f_L(4L)ε(4L)
                         −∫_(4L)^(6L)f_L'(u)ε(u)du.

Its absolute value is at most
sup_(u≥4L)|ε(u)| times
|f_L(6L)|+|f_L(4L)|+∫_(4L)^(6L)|f_L'(u)|du=O(L).
This proves the stated o(L) without a quantitative prime remainder.
The convention (4L,6L] excludes the lower atom and includes the
upper one if an endpoint exponent is prime.

The constant in (6) is strictly larger than 1/6. An elementary
bound is 2<e≤5/2+(1/6)/(1−1/4)=49/18<11/4, using the
exponential series and bounding successive ratios in its tail.
The function 2(x−1)/x³ decreases for x>3/2. Hence

2(exp(−2)−exp(−3))=2(e−1)/e³
 >224/1331=1/6+13/7986.                               (7)

Since (1+q)/(1−q)^3≥1 for 0≤q<1, (6)–(7) imply

M_r≥L/6                                                     (8)

for all sufficiently large r.

We also need a uniform upper bound for each individual shell
weight. Since q_p≤1/p≤1/2,

d_r(p)≤12(log p)/p.

The function (log x)/x decreases on x>e. Consequently, for
L sufficiently large and p∈I_r,

d_r(p)≤48L exp(−4L).                                    (9)

Now regard the coordinates θ_p as independent uniform angles
under Haar measure, solely to compute the measure of a set in
this finite torus. Set X_p=1−cos θ_p. Direct integration gives

X_p≥0,  E X_p=1,  E X_p²=3/2.

For u≥0, e^(−u)≤1−u+u²/2: the difference has value and
first derivative zero at zero and second derivative 1−e^(−u)≥0.
For 0≤z≤1/2 it follows that

E exp(−zX_p)≤1−z+3z²/4
             ≤1−5z/8≤exp(−5z/8).                       (10)

Take λ=exp(4L)/(96L). By (9), z=λd_r(p)≤1/2 on I_r.
Independence and the finite product in (10) therefore give

E exp(−λΣ_(p∈I_r)d_r(p)X_p)≤exp(−5λM_r/8).             (11)

All omitted terms of B_r are nonnegative. On B_r≤L/16 the
shell sum is at most L/16, so its negative exponential is at
least exp(−λL/16). Integrating this elementary indicator bound
and using (8) and (11) yields

μ{B_r≤L/16}
 ≤exp(λL/16) E exp(−λΣ_(p∈I_r)d_r(p)X_p)
 ≤exp[−λ(5M_r/8−L/16)]
 ≤exp(−λL/24)
 =exp(−exp(4L)/2304).                                  (12)

No probabilistic assumption about the actual height orbit has
been made; product Haar measure is used only in (10)–(12).

To pass from a single region to its continuous sweep, the
total-weight estimate proved in L342 gives

D_r:=Σ_(p≤y)d_r(p)≤6L+o(L)≤7L

for all sufficiently large r. Since log p≤6L, the derivative
along the flow obeys, for every θ and real t,

|d/dt B_r(θ+tv)|
 =|Σ_(p≤y)d_r(p)(log p)sin(θ_p+t log p)|
 ≤6L D_r≤42L².                                        (13)

This is a global Lipschitz bound and permits arbitrary windings
on the torus. Put Δ=1/(1344L). If θ∈A_r and 0≤t≤H, let
j=floor(t/Δ). Then 0≤t−jΔ<Δ, and (13) gives

B_r(θ+(t−jΔ)v)≤L/32+42L²Δ=L/16.

Thus, including all boundary points,

E_(r,H)⊂⋃_(j=0)^(floor(H/Δ)) ({B_r≤L/16}+jΔv).          (14)

The number of grid points is at most 1+1344HL. Translation
invariance of Haar measure and (12) prove (1); the bound by one
is automatic. Only finite unions and products are involved.

For log H=2r+O(1),

log(1+1344HL)=2r+O(log r)
                         =o(exp(4sqrt(r))).

Subtracting exp(4sqrt(r))/2304 in (1) and absorbing this
smaller term by half of it proves (2) and its stated extension.
In particular log a_n=2r+log(2π)+o(1), so lengths comparable
to a_n have the same comparison. The constants are sufficient;
no optimal exponential rate is asserted.

The set E_(r,H) is compact, being the continuous image of the
compact product A_r×[0,H]. L341 proves that the forward orbit
−av mod 2π visits every nonempty open set after any prescribed
height, for this finite vector of prime logarithms. Its finite
Fourier proof uses unique prime factorization to exclude zero
nonconstant frequencies. Translating the orbit by the constant
vector (π)_(p≤y) gives the same property for φ_r.

When the right side of (1) is below one, the complement of
E_(r,H) is a nonempty open set. Choose b≥A_0 with φ_r(b)
in that complement. If φ_r(b+t) belonged to A_r for some
t∈[0,H], then φ_r(b)=φ_r(b+t)+tv would belong to E_(r,H),
a contradiction. Taking H=exp(2r) proves (3).

Conversely, if every interval [b,b+H] starting after some A_0
contains a visit to A_r, then φ_r(b)∈E_(r,H) for every such
b. Density and closedness force E_(r,H) to be the whole torus.
Equation (1) then implies

1≤(1+1344HL)exp(−exp(4L)/2304),

which rearranges to (4). For large r, putting K=exp(4L)/2304
and using exp(K)−1≥exp(K)/2 gives

log H≥K−log(2688L)≥K/2.

This is (5); exp(4sqrt(r))/(9216r)→∞ proves the claimed
comparison with 2r.

Throughout the density argument r, the prime set and H are fixed
before choosing b. No bound relates the resulting b to a_n.
L342's negative arithmetic margin holds at visits, but its
criterion is only sufficient. Neither the measure deficit nor
these empty intervals determines any sign outside A_r. ∎

**Mathlib.** Full statement: not checked. Coverage of the
weighted exponential-moment inequality, prime-shell lower bound,
time-grid sweep and aggregate-region return obstruction is not
checked. No full matching theorem or absence from checked sources
is claimed. The moment and covering inequalities are proved above.

The supporting reciprocal-prime asymptotic is proved in L338
from the standard Mertens third theorem recorded in foundations.
Its retained reference is Ross G. Pinsky, *Probabilistic Proofs of
Some Generalized Mertens' Formulas Via Generalized Dickman
Distributions* (2018),
[equation (1.1), p. 2](https://arxiv.org/pdf/1809.04888#page=2).
That source was checked earlier and is not rechecked here; its
Mathlib coverage is not checked. It supports (6), not the full
return obstruction. L342 supplies the total-weight bound and the
conditional arithmetic interpretation; L341 supplies the proved
forward-orbit density. No new library result or external estimate
is imported, and no numerical return-time calculation is needed.
