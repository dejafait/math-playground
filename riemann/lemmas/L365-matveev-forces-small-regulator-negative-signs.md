# Lemma 365: Matveev forces negative signs at every small fixed regulator

**Hypotheses.** Use the analytic statements and definitions of L364
for L357's Gaussian-regulated Fourier family F_epsilon, with
epsilon=R^(-2). In particular A(x)>0 is its exact gamma envelope,
m_R>0 is its template derivative margin, and N_H, K_H, beta_H and
Delta_H are those of L364. Numerical interval certificates are not
inputs to this statement. All logarithms are natural.

Import E. M. Matveev, *An explicit lower bound for a homogeneous
rational linear form in the logarithms of algebraic numbers. II*,
Izvestiya: Mathematics 64:6 (2000), 1217–1269, Corollary 2.3,
(2.4)–(2.6), [journal record and DOI](https://www.mathnet.ru/eng/im314).
The additive form used here is explicitly restated in Min Sha,
*Effective results on the Skolem Problem for linear recurrence
sequences*, [arXiv:1505.07147v6](https://arxiv.org/pdf/1505.07147v6),
2 October 2018, section 2.4, equation (2.19), pp. 12–13:
for n>=2, nonzero algebraic alpha_j in a number field of degree D,
integer coefficients b_j, B=max_j |b_j|>=1, and fixed principal
logarithms, let

\[
 A_j\ge\max\{D h(\alpha_j),|\log\alpha_j|,0.16\},\qquad
 \Lambda=\sum_{j=1}^n b_j\log\alpha_j\ne0.
\]

Then

\[
 \log|\Lambda|>
 -2^{6n+20}D^2\left(\prod_{j=1}^n A_j\right)
       \log(eD)\log(eB).                                      \tag{1}
\]

Here h is the absolute logarithmic height. This is a cited arithmetic
input; neither the transcendence theorem nor a multiplicative-form
variant is reproved or substituted for it.

**Conclusion.** L364's condition (LF) holds unconditionally, for
example with the single universal constant C=20. Explicitly, for every
real N>=2, K>=1 and nonzero prime-indexed integer vector k with
|k_p|<=K,

\[
 \left|\sum_{p\le N}k_p\log p\right|
 \ge\exp\{-\exp(20N\log(N+2))\log(2+K)\}.                     \tag{2}
\]

There is epsilon_*>0 such that for every fixed
0<epsilon<=epsilon_* there is H_epsilon<infinity for which every
H>=H_epsilon admits an actual x in [H,2H] satisfying

\[
 \frac{F_\varepsilon'(x)^2-F_\varepsilon(x)F_\varepsilon''(x)}{A(x)^2}
       \le-\frac{m_{\varepsilon^{-1/2}}^2}{2}<0.                \tag{3}
\]

In particular no common epsilon_0>0 makes the first Laguerre
combination nonnegative on the whole real axis for every
0<epsilon<=epsilon_0. This conclusion concerns the regulated
family. It asserts no actual-theta sign, off-line zeta zero,
uniform onset in epsilon, or higher Laguerre sign.

**Proof.** First prove the arithmetic specialization. Remove every
zero coefficient and enumerate the remaining distinct primes as
p_1,...,p_n. There is at least one such prime and n<=N. The real
logarithmic form is nonzero: if it vanished, exponentiating would
give prod_j p_j^(k_(p_j))=1, contradicting unique factorization
unless every coefficient were zero. Negative coefficients cause
no difficulty because they merely put primes in the denominator.

If n=1, the absolute value of the form is at least log 2>=1/2.
The right side of (2) is at most exp(-log(2+K))<=1/3, since
exp(20N log(N+2))>=1. Thus (2) holds in this case without applying
the n>=2 statement.

For n>=2, apply (1) with alpha_j=p_j, D=1 and b_j=k_(p_j).
Positive rational primes lie in Q, have h(p_j)=log p_j, and their
principal logarithms are the real log p_j. Also log p_j>=log 2>0.16.
Consequently A_j=log p_j is admissible. The coefficient norm satisfies
1<=B<=K, and log(eD)=1. Every source hypothesis is therefore met,
with no complex branch choice or conjectural arithmetic premise.

Since log(2+K)>=log 3>1 and B<=K,

\[
 \log(eB)=1+\log B\le2\log(2+K).                              \tag{4}
\]

Define V_N=max{1,log N}. Then prod_j log p_j<=V_N^n<=V_N^N.
To absorb the remaining factor, use n<=N, N>=2, log 2<1,
log V_N<=log(N+2) and log(N+2)>=log 4>1. These elementary
inequalities give

\[
 \begin{aligned}
 \log\left(2^{6n+21}\prod_{j=1}^n\log p_j\right)
 &\le(6N+21)\log2+N\log V_N\\
 &\le17N+N\log(N+2)\\
 &\le18N\log(N+2)\\
 &\le20N\log(N+2).
 \end{aligned}                                                \tag{5}
\]

For the middle bound, 21<=21N/2 and 6+21/2<17. Products
containing log 2<1 are bounded above by V_N^N, not bounded
below by it. Combining (1), (4) and (5) yields

\[
 \log|\Lambda|>
 -\exp(20N\log(N+2))\log(2+K),
\]

which proves (2). The same C=20 works for every N,K and every
allowed vector, including vectors with only one nonzero coefficient.

Now fix any sufficiently large R in the range of L364. All constants
in what follows may depend on this fixed R. Apply (2) separately to
every nonzero vector defining Delta_H. Their set is finite, so

\[
 \Delta_H\ge e^{-Q_H},\qquad
 Q_H=\exp(20N_H\log(N_H+2))\log(2+K_H).                        \tag{6}
\]

There is no need to select one vector uniformly in H. The lower
bound in (6) is uniform over the entire finite set at that H.

Set y=log log H. L364's proved growth comparison (17), with R
held fixed, states

\[
 N_H=O_R(\sqrt y),\quad
 \log K_H=2y+O_R(\log(y+2)),\quad
 \log\beta_H^{-1}=O_R(y^{3/2}).                               \tag{7}
\]

In particular,

\[
 Q_H\le\exp\{O_R(\sqrt y\log(y+2))\}\,O_R(y)=o(e^y).
                                                                    \tag{8}
\]

To check the last comparison, take the logarithm of its ratio to
e^y: it is at most
-y+O_R(sqrt(y) log(y+2))+O_R(log(y+2)), which tends to
minus infinity because log(y+2)/sqrt(y) tends to zero.
Also y^(3/2)=o(e^y), and e^y=log H. Equations (6)–(8) imply

\[
 \begin{aligned}
 \log(H\Delta_H\beta_H)
 &\ge\log H-Q_H-\log\beta_H^{-1}\longrightarrow+\infty,\\
 \log(\sqrt H\,\beta_H)
 &=\tfrac12\log H-\log\beta_H^{-1}\longrightarrow+\infty.
 \end{aligned}                                                \tag{9}
\]

Thus both precise return requirements of L364,
H Delta_H beta_H>=8 and sqrt(H) beta_H>=96, hold for every
sufficiently large H at this fixed R. Its unconditional visit/sign
implication now gives (3). We use its full Gaussian-tail control,
its joint prime/gamma Fourier bump and its sign transfer; qualitative
density alone would not justify this shrinking-window conclusion.
The gamma angle, omega and arithmetic phases are all evaluated at
the same actual x supplied by that implication.

The sufficiently-large-R range is R>=R_0 for some finite R_0>1,
as in L364 and its template input. Take epsilon_*=R_0^(-2).
Every fixed 0<epsilon<=epsilon_* corresponds to a fixed
R=epsilon^(-1/2)>=R_0, so (9) and L364 supply an H_epsilon.
Neither (8) nor (9) is asserted uniformly in R. This proves the
stated order of quantifiers:

\[
 \exists\varepsilon_*>0\ \forall\varepsilon\in(0,\varepsilon_*]
 \ \exists H_\varepsilon\ \forall H\ge H_\varepsilon
 \ \exists x\in[H,2H]\quad\text{such that (3) holds}.
\]

If a common global-first-sign threshold epsilon_0>0 existed,
choose epsilon=min{epsilon_0,epsilon_*}/2. Equation (3) contradicts
its nonnegativity assertion because A(x)^2>0. This stops that
certificate without requiring a regulator-independent onset. L357's
O(epsilon) absolute error does not transfer the sign at these
regulator-dependent, potentially escaping frequencies to actual theta;
no relative-error comparison with A(x)^2 is supplied. ∎

This is a **REPRODUCTION**: Matveev's known arithmetic bound is
imported by precise citation, and only its prime specialization and
composition with the existing analytic return lemma are proved here.
The inspected source statements are not a match for the full Gaussian
sign conclusion, but no originality beyond the checked literature is
claimed. The earlier elementary separation failure is preserved; its
weaker certificate is not a lower bound on actual return times.

**Mathlib.** Full quantitative logarithmic-form bound, specialization
(2) and Gaussian sign conclusion (3): **not checked**. Supporting
height, prime-factorization, finite Fourier and gamma coverage is also
**not checked** in this step. Matveev's Corollary 2.3 and Sha's (2.19)
are supporting arithmetic results, not library references or a match
for (3). No full matching theorem or library absence is asserted;
general reference is
[Mathlib](https://leanprover-community.github.io/mathlib4_docs/).
