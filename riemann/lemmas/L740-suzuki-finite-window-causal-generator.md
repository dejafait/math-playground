# L740: Finite-window causal realization of Suzuki's parameter family

## Hypotheses

Fix \(0<L<\infty\), and use the original complex Hilbert space
\(X_L=L^2((0,L),dx)\). The parameter \(\theta\) is real and nonnegative.
Use L018's completion
\(\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)/2\).
For \(\theta>1\), use Suzuki's continuous complete causal kernel
\(K_\theta\) and the operator \(K_\theta[t]\) as specified in L618:

\[
 \int_0^\infty K_\theta(x)e^{-px}\,dx
 =\exp\left(-2\theta\frac{\xi'(p+1/2)}{\xi(p+1/2)}\right),
 \qquad \Re p>\tfrac12.                                      \tag{1}
\]

This is Suzuki, *Integral operators arising from the Riemann zeta
function*, [arXiv:1907.07302v2](https://arxiv.org/pdf/1907.07302v2)
(6 March 2020), Theorem 1.2 and (1.10), with \(p=-iz\).
L618 also supplies the absolutely convergent identity
\(-\zeta'/\zeta(s)=\sum_{n\ge2}\Lambda(n)n^{-s}\) for \(\Re s>1\).
Here \(\Lambda(p^k)=\log p\) for prime powers and is zero otherwise.
No zero-free continuation beyond that half-plane is an input.

The named functional-analytic imports are:

- Carvalho-Neto and Fehlberg Júnior, *The Riemann--Liouville fractional
  integral in Bochner--Lebesgue spaces I*,
  [arXiv:2108.02291v2](https://arxiv.org/pdf/2108.02291v2)
  (5 December 2021), Theorems 22, 27 and 28, printed pp.19,22--27:
  only the finite-interval scalar complex \(p=2\) semigroup and generator
  statements are used. No \(p=\infty\) assertion is imported.
- Schnaubelt, *Evolution Equations*,
  [19 March 2026 version](https://iana.math.kit.edu/downloads/iana3/schnaubelt/Skripten/evgl-skript.pdf),
  Theorem 3.4, printed pp.74--76: bounded perturbations of a \(C_0\)
  generator retain its domain and generate a \(C_0\)-semigroup.
- [NIST DLMF 5.9.13](https://dlmf.nist.gov/5.9.E13), the digamma
  Laplace identity for \(\Re z>0\), using the principal logarithm.

## Conclusion

There is a causal \(C_0\)-semigroup \(S_L(\theta)\) on \(X_L\),
with \(S_L(0)=I\), such that for every \(\theta>1\)

\[
 (S_L(\theta)f)(x)=\int_0^x K_\theta(x-y)f(y)\,dy.            \tag{2}
\]

Its closed, densely defined generator has the exact domain

\[
 \begin{split}
 D(A_L)&=\{f\in X_L:\ \Phi_f\in AC[0,L],\quad
                          \Phi_f'\in X_L\},\\
 \Phi_f(x)&=\int_0^x\log(x-y)f(y)\,dy,
 \end{split}                                                  \tag{3}
\]

where the continuous representative of \(\Phi_f\) is intended.
It automatically has \(\Phi_f(0)=0\). There is no additional trace
condition on \(f\), and no right-endpoint condition at \(L\).
Write \(\gamma=-\psi(1)\) for Euler's constant and set, for \(x>0\),

\[
 \begin{split}
 h(v)&=\frac1{1-e^{-v}}-\frac1v,\\
 q(x)&=\frac{e^{-x/2}-1}{x}
       +2e^{-x/2}\bigl(h(2x)-1\bigr)-2e^{x/2},\\
 (T_af)(x)&=\mathbf1_{x>a}f(x-a),\qquad a\ge0,\\
 (Q_Lf)(x)&=\int_0^x q(x-y)f(y)\,dy,\\
 P_L&=2\sum_{2\le n<e^L}\frac{\Lambda(n)}{\sqrt n}T_{\log n}.
 \end{split}                                                  \tag{4}
\]

Then on (3),

\[
 \boxed{\quad A_Lf=\Phi_f'+(\gamma+\log(2\pi))f+Q_Lf+P_Lf.\quad}
                                                                  \tag{5}
\]

Here the rational completion terms and the digamma term are included
in \(Q_L\); \(P_L\) is the entire arithmetic contribution on this
window. A delay exactly equal to \(L\) is the zero operator and may
equivalently be included. With

\[
 b_L=\frac L2+4(e^{L/2}-e^{-L/2})
          +2\sum_{2\le n<e^L}\frac{\Lambda(n)}{\sqrt n},         \tag{6}
\]

one has \(\|Q_L+P_L\|\le b_L<\infty\) and, for \(\theta>0\),

\[
 \|S_L(\theta)\|\le
    \frac{L^\theta}{\Gamma(1+\theta)}
    \exp\bigl(\theta(\log(2\pi)+b_L)\bigr).                  \tag{7}
\]

All norms in (5)--(7) are the original unweighted \(L^2\) norms.
For \(t=L/2\), translate the active space \(L^2(-t,t)\) to \(X_L\)
by \((Uf)(r)=f(r-t)\), and put \((R_Lg)(r)=g(L-r)\). On the
orthogonal decomposition
\(L^2(-\infty,t)=L^2(-\infty,-t)\oplus L^2(-t,t)\),

\[
 K_\theta[t]=0\oplus U^{-1}S_L(\theta)R_LU,
 \qquad \|K_\theta[t]\|=\|S_L(\theta)\|\quad(\theta>1).       \tag{8}
\]

This is a finite-window specialization of the named source results,
not a claim of novelty beyond the sources checked. The separate conceptual
audit below (4 November 2026, step 274) passes for this identification,
including its extension to parameter zero. No dissipativity, contraction,
window-uniform bound, innerness or Xi mixed sign is asserted.

## Proof

### 1. The complete logarithmic symbol

On \(\Re p>1/2\), put \(s=p+1/2\). L018 and L618 give

\[
 \begin{split}
 g(p):=-2\frac{\xi'}{\xi}(p+1/2)
 ={}&\log\pi-\psi((p+1/2)/2)
       -\frac2{p+1/2}-\frac2{p-1/2}\\
   &+2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}e^{-p\log n}.
 \end{split}                                                  \tag{9}
\]

The Euler series is absolutely convergent there. All differentiations
are in the zero-free Euler half-plane, with locally uniform convergence
as justified in L618. No logarithm of ξ is continued through a zero.

DLMF 5.9.13, with its integration variable changed to \(2x\), gives

\[
 -\psi((p+1/2)/2)
 =-\log(p+1/2)+\log2
       +\int_0^\infty2e^{-x/2}h(2x)e^{-px}\,dx.              \tag{10}
\]

The principal logarithms in (10) have their ordinary scaling relation,
since \(\Re(p+1/2)>0\). For \(\Re p>0\), the elementary identity

\[
 \log p-\log(p+1/2)
 =\int_0^\infty\frac{e^{-x/2}-1}{x}e^{-px}\,dx               \tag{11}
\]

follows by writing the quotient as
\(-\int_0^{1/2}e^{-ux}\,du\), applying absolute Fubini, and
integrating \(-1/(p+u)\) in \(u\). Also the Laplace transforms of
\(-2e^{-x/2}\) and \(-2e^{x/2}\) are respectively
\(-2/(p+1/2)\) and \(-2/(p-1/2)\), with the latter requiring
\(\Re p>1/2\). Thus (9)--(11) give exactly

\[
 g(p)=-\log p+c+\widehat q(p)
       +2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}e^{-p\log n},
 \qquad c=\log(2\pi),\quad \Re p>1/2.                      \tag{12}
\]

In particular, the scalar \(cI\), both rational completion terms,
the shift by \(1/2\), and all prime-power delays are retained. The
additional scalar \(\gamma I\) in (5) belongs to the unshifted
fractional-integral generator, not to μ below.

### 2. Finite-window perturbation and the exact domain

The inequalities \(1-e^{-v}<v\) and \(e^v-1>v\) imply
\(0<h(v)<1\) for \(v>0\). Also
\(|e^{-x/2}-1|/x\le1/2\). Consequently

\[
 |q(x)|\le\tfrac12+2e^{-x/2}+2e^{x/2}\quad(x>0),
 \qquad
 \int_0^L|q(x)|dx\le\tfrac L2+4(e^{L/2}-e^{-L/2}).         \tag{13}
\]

In particular the apparent singularities cause no local
integrability problem. Young's convolution inequality, after extending
\(f\) by zero, bounds \(\|Q_L\|\) by that integral. Each delay has
norm at most one, and \(P_L\) is a finite sum; this proves (6).

Let \(J_L(0)=I\), and for \(\theta>0\) let

\[
 (J_L(\theta)f)(x)=\frac1{\Gamma(\theta)}
                     \int_0^x(x-y)^{\theta-1}f(y)\,dy.
                                                                  \tag{14}
\]

The \(p=2\) cases of Carvalho-Neto--Fehlberg Theorems 22,27,28,
with \(t_0=0,t_1=L,X=\mathbb C\), say that this is a \(C_0\)
semigroup, with domain (3) and generator
\(G_Lf=\gamma f+\Phi_f'\). These source results, rather than a
formal differentiation of the singular kernel, are the domain input.

For clarity about its endpoint, every \(f\in X_L\) has

\[
 |\Phi_f(x)|\le\|f\|_{L^2(0,x)}
           \left(\int_0^x|\log u|^2du\right)^{1/2}
             \longrightarrow0\quad(x\downarrow0).             \tag{15}
\]

The convolution is continuous on \([0,L]\): zero-extend \(f\) and
\(\mathbf1_{(0,L)}\log x\), both in \(L^2(\mathbb R)\), and use
translation continuity in \(L^2\) and Cauchy--Schwarz for their
convolution. Thus the representative in (3) is unambiguous and has
zero left trace. The imported theorem imposes no trace on \(f\)
itself and no vanishing condition at the upper endpoint. This also
explains why replacing the domain by a guessed Dirichlet domain would
not be the same generator.

Set \(B_L=Q_L+P_L\). Causal convolution operators and causal delays
commute with \(J_L(\theta)\) and with one another on a fixed window.
Indeed, zero extension and convolution of measures supported in
\([0,\infty)\) give this by Fubini; all relevant kernels have finite
mass or total variation on \([0,L]\). Discarding output beyond \(L\)
does not change a later output below \(L\), because there is no negative
delay. The assertion first follows for bounded \(f\), then for all
\(X_L\) by the bounded-operator estimates.

Define

\[
 S_L(\theta)=e^{c\theta}J_L(\theta)e^{\theta B_L},
 \qquad \theta\ge0.                                         \tag{16}
\]

Commutation proves the semigroup law. Norm continuity of the bounded
exponential and strong continuity of \(J_L\) prove strong continuity
at zero, and hence everywhere. The bounded perturbation theorem
applies to \(G_L+cI+B_L\). Its domain is exactly \(D(G_L)\).
One can also see this domain equality directly from (16): the strong
derivative at zero for \(S_L(\theta)f\) exists if and only if that for
\(J_L(\theta)f\) exists, by multiplying by the norm-differentiable
\(e^{-\theta(cI+B_L)}\). The derivatives differ by \((cI+B_L)f\).
This proves (3) and (5), and closedness and density follow from the
generator theorem. No equivalent norm is substituted for \(X_L\).

Young's inequality gives
\(\|J_L(\theta)\|\le L^\theta/\Gamma(1+\theta)\).
Together with \(\|e^{\theta B_L}\|\le e^{\theta b_L}\), this proves
(7). The right side is locally bounded as \(\theta\downarrow0\);
more explicitly, for each \(f\in X_L\),

\[
 \|S_L(\theta)f-f\|
 \le\|J_L(\theta)\|\,
       \|(e^{\theta(cI+B_L)}-I)f\|
       +\|J_L(\theta)f-f\|\longrightarrow0.                 \tag{17}
\]

This is strong convergence, not a claim of operator-norm convergence.

### 3. Identifying the entire kernel, not just a scalar derivative

It remains to show that (16) corresponds to (1). Define a locally
finite signed measure on \([0,\infty)\) by

\[
 \mu(dx)=q(x)dx+
          2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}(dx).
                                                                  \tag{18}
\]

For any fixed \(a>1/2\) its exponentially weighted total variation is
finite. In fact (13) gives

\[
 \|\mu\|_a:=\int_0^\infty e^{-ax}d|\mu|(x)
 \le \frac1{2a}+\frac2{a+1/2}+\frac2{a-1/2}
       +2\sum_{n\ge2}\Lambda(n)n^{-a-1/2}<\infty.            \tag{19}
\]

The sum converges by \(\Lambda(n)\le\log n\) and the integral test.
Weighted total variation is submultiplicative for convolution on the
positive half-line, by absolute Fubini. Therefore

\[
 E_\theta=\sum_{k=0}^\infty\frac{\theta^k}{k!}\mu^{*k},
 \qquad \mu^{*0}=\delta_0,\qquad
 \|E_\theta\|_a\le e^{\theta\|\mu\|_a},                    \tag{20}
\]

converges in that measure norm. This weighted measure space is used
only for an absolutely convergent transform identification. It is
not a weighted replacement for the Hilbert space in (3)--(8).

For \(\theta>0\), let
\(j_\theta(x)=\mathbf1_{x>0}x^{\theta-1}/\Gamma(\theta)\).
Its weighted \(L^1\) norm is \(a^{-\theta}\). Thus

\[
 k_\theta(x)dx=e^{c\theta}(j_\theta(x)dx)*E_\theta           \tag{21}
\]

is absolutely continuous and has finite weighted \(L^1\) norm. The
convolution series converges in that norm, so it defines a genuine
locally integrable causal kernel. Measures (20) defined using different
\(a>1/2\) agree locally: every partial sum is the same, and weighted
norm convergence implies total-variation convergence on each compact
interval. Thus no choice of transform line changes (21).

The Laplace transform of (21), justified termwise by (19)--(20), is

\[
 \int_0^\infty k_\theta(x)e^{-px}dx
  =e^{c\theta}p^{-\theta}e^{\theta\widehat\mu(p)}
  =e^{\theta g(p)},\qquad \Re p>1/2,                        \tag{22}
\]

with the principal power and the usual gamma integral for \(j_\theta\).
For any such \(p\), choose \(a\) strictly between \(1/2\) and \(\Re p\)
to apply the absolute bounds. Equations (12) and (18) give the second
equality; this retains the complete arithmetic exponential, including
all convolution powers, not a linearized or truncated kernel.

For \(\theta>1\), Suzuki's growth and support hypotheses imply
\(e^{-ax}K_\theta(x)\in L^1(\mathbb R)\), extending it by zero
for \(x<0\), for every \(a>1/2\). The same is true of (21). On
\(p=a+iu\), equations (1) and (22) give identical Fourier transforms
of these weighted \(L^1\) functions. The standard injectivity theorem
for the Fourier transform on \(L^1(\mathbb R)\) gives
\(k_\theta=K_\theta\) almost everywhere. Equality almost everywhere
suffices for the integral operators. This uses no unweighted
full-line \(L^2\) multiplier theorem and no contour displacement.

To match (21) to (16), let \(\rho_L(\nu)\) be causal convolution
by a measure \(\nu\) followed by restriction to \((0,L)\). For a measure
with finite weighted norm it has the bound
\(\|\rho_L(\nu)\|\le|\nu|([0,L))\le e^{aL}\|\nu\|_a\).
Causality and Fubini, as above, imply
\(\rho_L(\nu*\eta)=\rho_L(\nu)\rho_L(\eta)\).
The atom at zero acts as \(I\), and an atom at \(L\) acts as zero.
Consequently

\[
 \rho_L(\mu)=B_L,\qquad
 \rho_L(E_\theta)=e^{\theta B_L},\qquad
 \rho_L(j_\theta(x)dx)=J_L(\theta).                         \tag{23}
\]

The estimates just given justify passage of the convergent series
through \(\rho_L\). Now (21), (23) and (16) show that convolution
by \(k_\theta\) on \((0,L)\) is exactly \(S_L(\theta)\). This
proves (2), not just equality of formal symbols. At parameter zero
the convolution construction has \(j_0=\delta_0\), \(E_0=\delta_0\)
and \(S_L(0)=I\); (17) supplies its rigorous strong-limit meaning.
No continuity of Suzuki's functions down to zero is assumed.

### 4. Reflection and the inactive subspace

Put \(t=L/2\). As in L618, causality implies that an input supported
in \(({-\infty},-t)\) has zero output for \(x<t\), and that the
output vanishes for \(x<-t\). Thus the active space is exactly the
subspace \(L^2(-t,t)\) for purposes of the block formula; possible
further kernel nullvectors are irrelevant to this decomposition.

For \(g\in X_L\), translate \(x=r-t,y=v-t\). For \(\theta>1\),

\[
 \begin{split}
 (UK_\theta[t]U^{-1}g)(r)
    &=\int_0^L K_\theta(r+v-L)g(v)dv\\
    &=\int_{L-r}^L K_\theta(r+v-L)g(v)dv\\
    &=\int_0^r K_\theta(r-y)g(L-y)dy
      =(S_L(\theta)R_Lg)(r).
 \end{split}                                                  \tag{24}
\]

These equalities first hold on bounded functions and extend to \(X_L\)
by boundedness. Both \(U\) and \(R_L\) are unitary in the unweighted
norm, which proves (8). In particular, \(S_L\) has a parameter
semigroup law, while (24) does not assert one for the reflected
operators. The extension \(S_L(\theta)R_L\) tends strongly to \(R_L\)
at zero, and on the full original space its block extension tends to
zero on the inactive subspace. It does not tend to the identity on
that full space. This retains the distributional reflection at zero
and all finite-window projections.

### Qualifications and continuation threshold

The approved construction test is met: (22) is the complete transform,
(6) is explicit finite-\(L\) perturbation control, (3) is the actual
domain with its left trace, (17) is the strong parameter-zero limit,
and (8) identifies the original reflected operator in its original
norm. The source theorems are imported; only this actual-kernel
specialization and its applicability have been proved here.

The constants in (6)--(7) depend on \(L\). They give neither
\(\Re\langle A_Lf,f\rangle\le0\) nor any fixed-parameter
all-window contraction. No positivity follows from the sign or
absolute size of any individual scalar, convolution or delay term.
L739's square-order obstruction remains a contrast, not an input to
this proof. Its stopped argument is not reopened. A later energy
mechanism requires separate assessment, the total form on (3),
every scalar and boundary contribution, and an independently justified
signed estimate. Xi mixed positivity and RH remain unresolved.

### Separate conceptual audit (2026-11-04, step 274)

**Result: pass with the stated hypotheses and quantifiers.** No correction
to (1)--(24) is needed. This validates a local analytic input; it proves
no stronger estimate and no new sign. The review uses the complete L018
and L618 proofs and the previously inspected primary sources listed
above. It is not an independent verification of the entire Suzuki
manuscript. The following checks address the possible analytic failures.

1. **Exact domain and topology.** Theorem 28, printed p.23, was directly
   rechecked with its proof on pp.23--27: set the source endpoints to
   \(0,L\), the Banach space to \(\mathbb C\), and the exponent to 2.
   Its absolute-continuity criterion and scalar \(-\psi(1)=\gamma\)
   are exactly (3) and the stated \(G_L\). The source's last displayed
   pointwise limit alone would not suffice for a generator. Its preceding
   averaged-semigroup identity does give the required norm limit: with
   \(h=\gamma f+\Phi_f'\in X_L\),

   \[
   \left\|\frac{J_L(\alpha)f-f}{\alpha}-h\right\|_2
   \le\frac1\alpha\int_0^\alpha
                  \|J_L(v)h-h\|_2\,dv\longrightarrow0.
   \]

   This clarifies applicability, without reproving the source theorem.
   Only its valid p=2 case is used; no p=infinity density assertion is
   needed. Equation (15) and convolution continuity fix the left trace
   for every f in X_L before any domain restriction. No trace of f or
   upper-endpoint vanishing has been introduced.

2. **Bounded perturbation and both domain inclusions.** Integrating the
   envelope in (13) gives \(L/2+4(e^{L/2}-e^{-L/2})\); the two
   exponential endpoints cancel their constants. Delays with a<L have
   norm at most one and a delay with a=L is zero almost everywhere.
   Hence B_L is bounded in the unweighted norm. For C=cI+B_L,

   \[
   \frac{S_L(\theta)f-f}{\theta}
   =e^{\theta C}\frac{J_L(\theta)f-f}{\theta}
      +\frac{e^{\theta C}-I}{\theta}f.
   \]

   Norm differentiability and invertibility of \(e^{\theta C}\) show
   that either strong derivative exists exactly when the other does.
   This checks both domain inclusions without a formal derivative of
   \(x^{\theta-1}/\Gamma(\theta)\). The gamma bound in (7) and the
   exponential bound use the same norm; no similarity or renorming is
   used to infer a sign.

3. **Complete symbol and branches.** With s=p+1/2 the two rational
   derivatives of s(s-1) give -2/(p+1/2) and -2/(p-1/2).
   DLMF's substitution v=2x contributes the factor 2 and scalar log 2
   in (10). The negative integrand in (11) has transform
   log p-log(p+1/2), with both principal logs in the right half-plane.
   Together with log pi these give exactly c=log(2*pi), q and the
   positive arithmetic coefficient 2 Lambda(n)/sqrt(n). Euler's gamma
   constant is already in G_L and is not counted a second time in c
   or mu. No quotient is evaluated outside Re(s)>1.

4. **Full convolution and compression.** For a>1/2, (19) bounds total
   variation, not merely the signed mass. For positive-half-line measures
   nu,eta, absolute Fubini bounds the weighted variation of nu*eta by
   \(\|\nu\|_a\|\eta\|_a\); consequently every convolution
   power in (20) is included with an absolutely summable norm. Convolution
   of the weighted L1 density j_theta with the weighted finite measure
   E_theta is L1. On a fixed window, the total variations of both
   factors restricted to [0,L) are finite. In a double convolution
   contributing at x<L, both delays and their sum are nonnegative and
   less than L. Thus restriction of an intermediate output cannot remove
   any contribution to that x. Fubini first for bounded inputs, and the
   Young bounds followed by L2 density, prove the homomorphism in (23).
   This also justifies commutation in (16) and passage of the entire
   exponential series through rho_L. Endpoint atoms have the actions
   explicitly stated in the proof.

5. **Identification and parameter zero.** Locally consistent weighted
   limits define one kernel. For each chosen p with Re(p)>1/2 there
   is a valid absolute majorant with 1/2<a<Re(p), so (22) holds on
   the whole stated half-plane. For Fourier uniqueness on a fixed
   line Re(p)=b>1/2, use a<b in that bound. Both exponentially weighted
   functions on the line b are L1 by (21) and Suzuki's growth estimate.
   Their equal Fourier transforms therefore imply equality almost
   everywhere. This suffices for all finite-window operators and requires
   no global unweighted multiplier. At zero the limit is (17), using
   strong continuity and locally bounded J_L, not convergence of j_theta
   to an L1 function or convergence of S_L to I in operator norm.

6. **Reflection and quantifiers.** The inactive input/output blocks
   vanish because x+y<0 there. In the active block the change y=L-v
   has bounds 0<y<r, giving S_L(theta)R_L in that order. Right
   multiplication by the onto unitary R_L preserves the operator norm,
   proving equality in (8), not just one inequality. For each fixed
   vector the extension tends to \(0\oplus U^{-1}R_LU\).
   No Suzuki continuous-kernel assertion for theta<=1 and no reflected
   semigroup law is inferred. Every estimate keeps L fixed; (6)--(7)
   cannot be read as an all-window contraction.

The direct local inputs of this audit are already those used in the
proof; the DAG row stays unchanged. L739 and the earlier composition
stop are contrasts only. The total signed form, uniform window control
and mixed positivity remain unproved. A structural documentation check
does not certify any of these analytic checks.

## Mathlib

Full coverage of this finite-window Suzuki realization and the precise
logarithmic generator domain has not been checked; availability is
unknown. The named external theorems above are informal imports, not
Lean verifications. L618 records supporting Euler-product coverage,
including
[`riemannZeta_eulerProduct_exp_log`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/EulerProduct/DirichletLSeries.html#riemannZeta_eulerProduct_exp_log).
That support does not formalize (3), (16), (22) or (24). No claim of
Mathlib absence or of a formal proof is made.
