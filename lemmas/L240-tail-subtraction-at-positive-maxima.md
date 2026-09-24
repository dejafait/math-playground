# Lemma 240: a quantitative tail-subtraction test at positive maxima

**Hypotheses.** Use F, F_N, E_N, ε_N and B_N from L237–L238, and R_N and a_N^* from L236. Suppose r is a real point with F'(r)=0 and κ=−F''(r)>0. Put d=E_N(r)−F(r), s=E_N'(r), and c=κ+E_N''(r). For the first assertion assume d>0.

**Conclusion.** The exact identity is

R_N(r)=c/(2d)−s²/(2d²).

In particular, if |E_N''(r)|≤κ/2 and s²≤κd/4, then

a_N^*≥R_N(r)≥κ/(8d).

Here is a sufficient moving-frequency version. Fix T>0 and suppose along a sequence N→∞ there are positive maxima r_N with |r_N|≤TB_N, κ_N=−F''(r_N)>0 and d_N=E_N(r_N)−F(r_N)>0, satisfying

ε_N/(κ_N B_N²)→0,
ε_N²/(κ_N d_N B_N²)→0,
d_N/κ_N→0.

Then a_N^*→∞ along that sequence. Existence of such maxima for actual theta is not asserted.

The exact quadratic model Q(h)=−d−s h−c h²/2, with c>0, has effective deficit D=d−s²/(2c). If D>0, its ratio (QQ''−Q'²)/(2Q²) has global supremum c/(2D), attained at h=−s/c. Thus a small tail slope shifts the relevant maximum; it must not be discarded without comparison to the deficit.

**Proof.** At r the values of F_N and its first two derivatives are −d, −s and −c, respectively. Substitution in L236 gives the identity. Under the two inequalities c≥κ/2 and s²/(2d²)≤κ/(8d), whereas c/(2d)≥κ/(4d). Subtraction proves the lower bound, and F_N(r)=−d≠0 permits comparison with its supremum.

On |r|≤TB_N, the C² profile in L238, together with the chain rule, gives |E_N'(r)|≤C_T ε_N/B_N and |E_N''(r)|≤C_T ε_N/B_N², with constants independent of N. The first sequence assumption therefore eventually gives |E_N''(r_N)|≤κ_N/2. The second gives E_N'(r_N)²≤κ_N d_N/4 eventually. The established bound and the third assumption prove divergence. This argument evaluates an exact identity at the given points; it does not require a uniform Taylor approximation around moving maxima.

For the separate quadratic assertion complete the square:

Q(h)=−D−(c/2)(h+s/c)².

Writing y=h+s/c, differentiation gives

(QQ''−Q'²)/(2Q²)
= c[D−cy²/2]/[2(D+cy²/2)²].

For v=cy²/(2D)≥0 this equals (c/(2D))(1−v)/(1+v)². The last fraction is at most 1, with equality at v=0: subtracting its numerator from its denominator gives 3v+v²≥0. This proves the global supremum. The model assertion is algebraic and is not an error estimate for actual F_N. ∎

The required bound for the proposed first-level approximation is a_N^*→0. The exact identity shows that even a single sequence satisfying the displayed peak conditions would contradict that bound. Conversely, failure of these sufficient conditions does not prove vanishing widths. L237 concerned one fixed multiple zero; this test concerns possibly moving, strictly positive maxima and explicitly retains the tail slope. Neither the needed peak-height encounter nor the curvature comparison has been established for theta. No all-degree positivity or RH conclusion follows.

**Mathlib.** Not checked for the full statement or supporting differentiation and limit results. No matching theorem is claimed. General documentation: https://leanprover-community.github.io/mathlib4_docs/
