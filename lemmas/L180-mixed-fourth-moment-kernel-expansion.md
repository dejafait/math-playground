# Lemma 180: mixed fourth-moment kernel expansion

**Hypotheses.** Use the actual profiles p,q, sums F_v, phase θ, components
X,Y and normalized block average E_B of L179. In particular T=2πN²,
B=[2T−h,2T], h is comparable to N^(3/2), and p,q are fixed real C¹
profiles on [1,2]. Put τ=t−π/2, P=F_p, Q=F_q and

K_r(u)=h^(−1)∫_B exp(iτu−irθ(t))dt.

For n=(n_1,n_2,n_3,n_4) in the fourth power of the integer interval
I=[N,2N], and s∈{−1,1}⁴, set

w(n)=p(n_1/N)p(n_2/N)q(n_3/N)q(n_4/N),
u_s(n)=Σ_(j=1)^4 s_j log(n_j/N), r_s=(Σ_j s_j)/2.

**Conclusion.** The exact expansion is

E_B X²Y²=−(16N²)^(−1) Σ_(n∈I⁴) w(n)
                          Σ_(s∈{−1,1}⁴) s_3 s_4 K_(r_s)(u_s(n)).    (1)

Equivalently, it is 1/16 times the average of

4|P|²|Q|²−2Re(P² conjugate(Q)²)
+4Re[e^(−iθ)(P²|Q|²−|P|²Q²)]
−2Re[e^(−2iθ)P²Q²].                                             (2)

The available product-frequency counting and Hilbert estimate give

0≤E_B X²Y²≤C(1+N²/h)log(2N)=O(N^(1/2)log(2N)).                  (3)

This is the same order as the existing block fourth-moment upper bound.
No cancellation improvement or asymptotic for (1) is asserted.

**Proof.**

Put A=e^(−iθ/2)P and D=e^(−iθ/2)Q. Exactly,
X=(A+conjugate(A))/2 and Y=(D−conjugate(D))/(2i).
In expanding their squared product, the choice of D or conjugate(D)
in its two slots contributes the sign s_3s_4; the factor (2i)^(−2)
supplies the minus sign. Each of the four sums contributes N^(−1/2).
Their phases combine to τu_s−r_sθ. Integrating this finite expansion
proves (1), with no convergence issue. Pairing conjugate terms in
(A²+2|A|²+conjugate(A)²)(2|D|²−D²−conjugate(D)²)
proves (2). In particular the θ-dependent terms cannot be omitted.

Here is a direct application of the counting and Hilbert argument of
L171 to these signed profiles. For either v=p or v=q put

c_k=N^(−1)Σ_(m,n∈I:mn=k) v(m/N)v(n/N).

The squared sum F_v², up to a unit common phase, has coefficients c_k
and frequencies log k. Boundedness of v and L171's upper count of
ordered equal-product quadruples give

D_v=Σ_k |c_k|²≤C N^(−2) #{(m,n,l,j)∈I⁴:mn=lj}≤C log(2N).

This bound uses absolute values and requires no positivity of v.
The endpoint Hilbert argument in L171 likewise permits signed or complex
coefficients. Since k≤4N², it yields

E_B|F_v|⁴≤D_v+C N²D_v/h≤C(1+N²/h)log(2N).

Pointwise |X|≤|P| and |Y|≤|Q|. Cauchy–Schwarz applied to
|P|²|Q|² proves (3). This bypasses any unproved replacement of the
small L² errors of L179 inside a fourth moment.

To specify what remains in the exact expansion, K_0(0)=1, and for u≠0,

K_0(u)=[exp(i(2T−π/2)u)−exp(i(2T−h−π/2)u)]/(ihu).

Thus its balanced signs retain the exact product resonances and signed
off-diagonal terms. For r≠0 the phase derivative is

u−r log(a/N²), where a=(t−π/2)/(2π),

because θ'=log(a/N²). The derivative can vanish: for r=2 and all
positive signs, choose an interior t_0∈B, let a_0=a(t_0), and take
all four continuous ratios n_j/N=sqrt(a_0/N²). These ratios belong to
(1,2) for large N and give u=2log(a_0/N²). This observation is about
the continuous frequency range, not a claim of exact integer stationary
quadruples. It shows that a uniform derivative bound separated from zero
on the entire frequency range is unavailable. The elementary bound
|K_r|≤1 on its own loses all oscillation. The proof above therefore
establishes only (3); a sharper estimate must exploit additional signed
arithmetic information, possibly including these θ-dependent terms.
It does not prove that such an improvement is impossible. ∎

## Scope, verification

The exact mixed moment is now reduced to finite arithmetic kernels.
L179's approximate phase relations are not exact moment identities.
Neither a growing lower bound nor uniform boundedness follows from (3).
First-moment decay, uniform integrability, cutoff covariance and RH remain
unproved. The main argument is unchanged.

Verification: expansion signs, normalization N^(−2), conjugate pairing,
product count, signed Hilbert applicability, and θ' are checked above.
An independent finite complex-number check is reproduced by
`python3 scripts/heat/check_mixed_fourth_algebra.py`; it checks algebra,
not asymptotics.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
