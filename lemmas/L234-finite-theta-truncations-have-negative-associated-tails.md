# Lemma 234: finite theta truncations have negative first associated tails

**Hypotheses.** Let N≥1 be an integer and, for u≥0, put

f_N(u)=Σ_{n=1}^N (8π²n⁴e^(9u/2)−12πn²e^(5u/2)) exp(−πn²e^(2u)).

Define k_N(u)=f_N(|u|), F_N(x)=∫_R k_N(u)e^(ixu)du, and
A_N(t)=∫_R s²k_N(s+t)k_N(s−t)ds. Write d_N=f_N'(0).

**Conclusion.** d_N>0, and, for fixed N as x→+∞,

F_N(x)=−2d_N x^(−2)+O_N(x^(−4)),
F_N'(x)=4d_N x^(−3)+O_N(x^(−5)),
F_N''(x)=−12d_N x^(−4)+O_N(x^(−6)),
Â_N(2x)=−2d_N² x^(−6)+O_N(x^(−8)).

In particular A_N is not positive definite for any finite N. This is not an assertion about the sign for the infinite actual theta kernel.

**Proof.** First verify the exact cancellation for the infinite series. With ψ and its transformation from L016, define A(u)=e^(u/2)ψ(e^(2u)) for every real u. The theta transformation gives

A(u)−A(−u)=−sinh(u/2).

The series is smooth on every compact real u interval by the differentiated Gaussian bounds in L016. Apply 2D²−1/2 to this identity: its right side vanishes, and the second derivative commutes with reflection. Thus K(u)=2A''(u)−A(u)/2 is smooth and even on R, and K'(0)=0. On u≥0 it is the series in L019. Local uniform differentiated convergence gives Σ_{n≥1}K_n'(0)=0.

For v=πn², direct differentiation of K_n(u)=4v_n(2v_n−3)e^(u/2−v_n), v_n=πn²e^(2u), gives

K_n'(0)=(−16v³+68v²−30v)e^(−v)
        =−2v(2v−1)(4v−15)e^(−v).

Every term with n≥2 is strictly negative, since π>3 implies v>12. The differentiated sum converges absolutely. Consequently

d_N=−Σ_{n>N}K_n'(0)>0

for every N≥1. The even extension k_N has right derivative d_N and left derivative −d_N; its first derivative has jump 2d_N at zero.

For completeness the Fourier asymptotics are obtained independently for each derivative, without differentiating a big-O remainder. Every derivative of f_N and of u^j f_N, for fixed j, decays faster than every exponential on [0,∞), and is integrable: each is a finite sum of polynomial factors in e^(u/2) and u times exp(−πn²e^(2u)). Repeated integration by parts therefore has no boundary term at infinity. For any such smooth function h, six integrations give

∫_0^∞ h(u)cos(xu)du=−h'(0)x^(−2)+h'''(0)x^(−4)+O_h(x^(−6));

five integrations give

∫_0^∞ h(u)sin(xu)du=h(0)x^(−1)−h''(0)x^(−3)+O_h(x^(−5)).

The remainders are bounded by fixed boundary derivatives and L¹ norms of derivatives of h. These statements require only fixed h and x≥1.

Apply the cosine formula first to h=f_N. Differentiation under the original Fourier integral is justified by the absolute moments, so

F_N'=−2∫_0^∞ u f_N(u)sin(xu)du,
F_N''=−2∫_0^∞ u² f_N(u)cos(xu)du.

For h=u f_N, h(0)=0 and h''(0)=2d_N. For h=u² f_N, h'(0)=0 and h'''(0)=6d_N. The three claimed expansions follow. Their products yield

F_N'²−F_N F_N''=(16−24)d_N² x^(−6)+O_N(x^(−8)).

L233 applies because k_N is continuous, even, and superexponentially decaying; it does not require differentiability at zero. Its identity divides the last expression by four. Since d_N>0, the negative leading term dominates for all sufficiently large x (depending on N). The positive-definiteness necessity proved in L233 then excludes positive definiteness of A_N. ∎

The required threshold for this approximation strategy was Â_N(ξ)≥0 for every real ξ. Instead every N has an eventually strictly negative spectrum. There is no uniform-in-N assertion about the onset frequency: d_N→0, and the infinite kernel cancels the cusp exactly. In fact the same integration by parts with the smooth even infinite K makes its Fourier transform decay faster than every inverse power, since all odd boundary derivatives vanish and all derivatives are integrable by L016. Thus the finite-N leading tail cannot be passed to N=∞. No negative value for the actual theta spectrum, all-degree mixed bound, or RH disproof follows.

**Mathlib.** Not checked for the full statement or supporting Fourier asymptotics and integration-by-parts results. The theta transformation is supplied mathematically by L016; its existing supporting Mathlib references are not a match for this full statement. General documentation: https://leanprover-community.github.io/mathlib4_docs/
