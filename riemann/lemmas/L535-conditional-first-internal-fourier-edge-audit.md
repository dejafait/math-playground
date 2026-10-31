# L535 — Conditional first internal Poisson Fourier edge audit

## Hypotheses

Work over the source's fixed arithmetic datum in \(\mathcal O=\mathbb
Z[\omega]\), with its conventions for primary representatives, norms
\(q_a\), zero-extended characters \(\chi_a\), Möbius coefficients and
fixed ray characters. Fix \(Z>1\), positive tolerances and losses
\(\eta,\tau,\pi_\beta,\pi_{\rm old}\), and one node and dyadic/ray/slot
pattern \(\sigma\) of the first Poisson transformation in the primary
source cited in the proof. All length parameters range over fixed bounded
sets. Fix their centers \(r,\ell,V,M,A_1,A_2,B,\delta,R,t,h_1,j\).
Actual ideals inside these blocks still vary. Put

\[
 s_a=r-A_a-B-t,\qquad
 \kappa_a=M-2r-2\ell-V-\delta+A_a+B-R/2,
 \qquad H_*=2r-2B-M+4\ell+2V+\delta-j+12\eta+\tau.       \tag{1}
\]

The following are explicit source contracts. This lemma does not audit
their arithmetic proofs, global availability or simultaneous realization.

1. The canonical block `eq:canonical-block` has the source's original
   coefficients and zero extensions, including both \(\beta(b_a,f)\)
   factors and their \((b_a,f)=1\) masks. The normalized row test is fixed:
   \(z\mapsto\Phi(q_z)\) is a radial Schwartz function on two real
   dimensions. The window \(W\) is smooth with compact support in
   \((0,\infty)\). Its normalized Fourier kernel is
   \(\mathcal K_1=\mathcal F\Phi\), expressed in squared radial norm,
   using the source's fixed nondegenerate pairing. It is not the transform
   of a test whose physical radial scale shrinks with \(Z\).
2. The primitive masked-Poisson, quotient-free extraction and slot-priority
   identities through `eq:first-poisson-column` and
   `eq:retained-cube-label` hold. In particular, with
   \(\mathfrak B=\operatorname{rad}(b_1b_2)\),
   \(n_a=\mathfrak A_a C u_a\), their formal column is
   \[
    \mu(u_a)\nu_a(u_a)\rho(u_a)\overline{\chi_{u_a}(hf^2E)}
      \chi_{u_a}(CJ)^4\chi_{u_a}(d_k)
      1_{(u_a,\operatorname{rad}q_0)=1}\mathfrak d_a(u_a). \tag{2}
   \]
   Here \(\nu_a\) is the fixed multiplicative ray character and
   \(\rho\) the source's multiplicative unit-modulus factor, with all
   prescribed zeros retained. The derived labels \(R_1,E,J,q_0\)
   depend on the old outer ideals, not the residual columns. The identity
   \(\xi(n)=\chi_n(J)^4 1_{(n,\operatorname{rad}q_0)=1}\)
   includes its zeros. All remaining factors are outer, defined by
   multiplication rather than division by a column value.
3. Principal restoration and discarded-tail estimates justify taking
   the masked, principal-restored *formal* nonzero-frequency component
   with \(y=hf^2E\) and \(\mathcal B_1(h)=1_{0<q_y\le Z^{H_*}}\).
   The mask is independent of the residual columns. The off-coprime
   extension uses the formal conductor product and the existing zero
   extensions; mutual-gcd inversion then writes \(u_a=t'x_a\), retaining
   \((x_a,t')=1\). This is not a primitive Poisson assertion for newly
   introduced noncoprime pairs. Bare-\(h\) dyads come from a single
   partition independent of \(f,E\).
4. All retained cutoffs, fresh column cutoffs \(\omega_{x,a}\), and larger
   cutoffs \(\Omega_{1,\alpha}\) have fixed compact normalized supports
   inside \((0,\infty)\), with uniform smooth seminorms. The larger ones
   equal one on the full retained supports; the fresh column cutoffs
   equal one on the quotient supports of the old \(W\)-windows. The
   fixed-depth support construction precedes the threshold in \(Z\).
   In particular \(|\log_Z q_a-a_{\rm cen}|\le\eta\) is only a coarse
   consequence, not permission to use supports growing as \(Z^\eta\).
5. After taking absolute values in a positive sum, the outer arithmetic
   magnitudes, including the two original \(\beta\)'s, are bounded by
   \(C Z^{\pi_\beta}w(f)w_o^+\). Here \(w(f)\ge0\) has the original
   divisor bound and \(w_o^+\) is the absolute assigned-slot product on
   the source's retained old reconstruction set \(\mathfrak O_\sigma\).
   It is independent of \(y\). For fixed such reconstruction, the
   old-label fibre bound `eq:inverse-old-label-fibre` is
   \[
     \sum_{f^2E\mid(y)}w(f)\le C_{\pi_{\rm old}}Z^{\pi_{\rm old}}
           \quad(0<q_y\le Z^{H_*}).                         \tag{3}
   \]
   The source's representative convention makes \(h=y/(f^2E)\)
   unique. Its uniformity uses the bounded range of \(H_*\).
   This is an assumed arithmetic fibre estimate, not Fourier mass.

Any later terminal arithmetic bounds remain separate contracts; none is
needed to prove the analytic inequality below. No entire recursion or
desired normalized child exponent is assumed as established here.

## Conclusion

For this single pattern the first transformed component has the source's
exact nine-dimensional Fourier separation and its positive output
`eq:inverse-first-transform-output`. The coefficient density is common
to all actual outer ideals and rows in that block. For every fixed real
height order \(H\ge0\), its weighted absolute mass is bounded by finite
seminorms of the fixed input tests, with **additional scale exponent zero**
independent of \(H\).

The factors \(Z^{\pi_\beta+\pi_{\rm old}}\) and
\(Z^{\kappa_a+9\eta/2}\) remain explicit in the positive output. The
varying indices inside the child row sums are not counted a second time
as coefficient-measure indices. No sector sum, second transformation,
recursive exponent defect, initialization, arithmetic contract or whole
marked-moment theorem is verified by this statement.

This is a conditional reproduction of a source-claimed interface. It
narrows one internal-interface obligation in the context of L533/L534;
neither of those lemmas is a mathematical input to this proof. It does
not imply an unconditional zeta estimate, Xi positivity or RH.

## Proof

Primary source: OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re(s)>7/8*, September 30, 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[build/paper.tex](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
Precise source locations are `lem:smooth-calculus` (retrieval lines
1019–1055, proof 1123–1139), `lem:kernel-seminorms` (1250–1313),
`eq:indexed-coefficient-measure` and the following normalization rules
(8932–9094), `eq:canonical-block` and the fixed-support/Fourier rules
(9406–9558), and the first extraction through positive output
(9559–10048). In particular the tested formulas are
`eq:inverse-first-root-kernel`, `eq:inverse-first-profile`,
`eq:inverse-first-polynomial`, `eq:inverse-first-separated`,
`eq:inverse-first-majorant` and `eq:inverse-first-transform-output`.
Labels identify the cited formulas; line numbers are retrieval aids.

The smooth Fourier calculus and normalized radial-kernel bounds are
imported from the two named source lemmas. The checks below specialize
them to the actual profile and verify its use. Reproducing this interface
is necessary because importing the final marked estimate would assume
the application being audited. Its underlying arithmetic proofs remain
the explicit contracts above.

### Common profile and exact normalization

Use independent ambient coordinates

\[
 \boldsymbol z=(z_{A_1},z_{A_2},z_C,z_d,z_R,z_t,z_h,z_{x_1},z_{x_2})
 =\left(\frac{q_{\mathfrak A_1}}{Z^{A_1}},
 \frac{q_{\mathfrak A_2}}{Z^{A_2}},\frac{q_C}{Z^B},
 \frac{q_{d_k}}{Z^\delta},\frac{q_{R_1}}{Z^R},
 \frac{q_{t'}}{Z^t},\frac{q_h}{Z^{h_1}},
 \frac{q_{x_1}}{Z^{s_1}},\frac{q_{x_2}}{Z^{s_2}}\right).   \tag{4}
\]

The letter \(z\) distinguishes these positive real coordinates from the
arithmetic row \(y=hf^2E\). Set
\(A=Z^{M+h_1-\delta-R-2t-s_1-s_2}>0\). The profile is

\[
 \begin{split}
 F_\sigma(\boldsymbol z)={}&Z^{-9\eta/2}
 \prod_\alpha\Omega_{1,\alpha}(z_\alpha)
 z_d^{-1}z_R^{-1/2}z_t^{-1}(z_{x_1}z_{x_2})^{-1/2}\\
 &\cdot W(z_{A_1}z_Cz_tz_{x_1})
       \overline{W(z_{A_2}z_Cz_tz_{x_2})}
 \mathcal K_1\left(A\frac{z_h}{z_dz_Rz_t^2z_{x_1}z_{x_2}}\right).
                                                               \tag{5}
 \end{split}
\]

All parameters of (5) are fixed before actual ideals are summed. The
actual norm of \(R_1\), although derived from other ideals, is a coordinate
of the profile; its dependence is not omitted. By (2), the other derived
labels and \(b_a,f\) occur only in characters, outer coefficients,
individual cutoffs or masks. Relations between the nine norms restrict
evaluation points of (5), not the definition of its transform.

The formal root is

\[
 \frac{Z^{M-r-2\ell-V}}
 {q_{d_k}\sqrt{q_{R_1}}q_{t'}\sqrt{q_{x_1}q_{x_2}}}
 =Z^{(\kappa_1+\kappa_2)/2}
   z_d^{-1}z_R^{-1/2}z_t^{-1}(z_{x_1}z_{x_2})^{-1/2}.       \tag{6}
\]

Indeed its central exponent is
\(M-r-2\ell-V-\delta-R/2-t-(s_1+s_2)/2\);
substituting (1) gives
\(M-2r-2\ell-V-\delta-R/2+(A_1+A_2)/2+B\), the average
of the two \(\kappa_a\). The kernel argument becomes the argument in
(5) by direct substitution in
\(Z^Mq_h/(q_{d_k}q_{R_1}q_{t'}^2q_{x_1}q_{x_2})\).
Also \(q_{n_a}/Z^r=z_{A_a}z_Cz_tz_{x_a}\).

Thus multiplying (5) by
\(c_1c_2\), where \(c_a=Z^{(\kappa_a+9\eta/2)/2}\), restores
the complete root and the old smooth factors: the single
\(Z^{-9\eta/2}\) cancels the single combined \(Z^{9\eta/2}\).
There is no remaining real root in either separated column.

### Modes, masks and exact identity

Write \(\varepsilon_1=1,\varepsilon_2=-1\). For fixed Fourier
frequency \(\boldsymbol v\in\mathbb R^9\) and outer reconstruction,
the columns supplied by multiplicative extraction at \(t'\) are

\[
 \begin{split}
 P_a(y;\boldsymbol v)=\sum_{x\ {\rm sf}}{}&
 \mu(x)\nu_a(x)\rho(x)\overline{\chi_x(y)}
 \chi_x(CJ)^4\chi_x(d_k)1_{(x,\operatorname{rad}q_0t')=1}\\
 &\cdot\mathfrak d_{I_a}(x)\omega_{x,a}(q_x/Z^{s_a})
          (q_x/Z^{s_a})^{\varepsilon_a i v_{x_a}} .        \tag{7}
 \end{split}
\]

The extracted factors are

\[
 B_a(t';y)=\mu(t')\nu_a(t')\rho(t')\overline{\chi_{t'}(y)}
       \chi_{t'}(CJ)^4\chi_{t'}(d_k)
       1_{(t',\operatorname{rad}q_0)=1}.                   \tag{8}
\]

Coprimality in (7) justifies the multiplicative factorization of (2).
The additional \(\mu(t')\) from mutual-gcd inversion is outer, separate
from the two occurrences in (8). Slots are allocated by the contracted
priority identity, with their original individual coefficients; no
character is divided at a zero.

The full finite outer index set \(\Omega_\sigma\) consists of
\(b_1,b_2,\mathfrak A_1,\mathfrak A_2,C,d_k,t',f,h\) and assigned
slot primes, subject to the original reconstruction and support relations.
In particular \(\mathfrak A_a\mid\mathfrak B\),
\((C,\mathfrak B)=1\), \(d_k\mid C\mathfrak B/R_1\); the labels
\(R_1,E,J,q_0\) are not additional free indices. Let \(e_\sigma\)
be the contracted outer product containing \(w(f)\), both \(\beta\)'s,
their original masks, extracted zero masks and finite Gauss/unit/ray
factors, excluding (8) and the displayed Möbius factors below. Let
\(\mathcal A_\sigma\) retain the assigned-slot coefficients and masks
with conjugation on side two, and \(\psi^{\rm out}_\sigma\) retain
the outer dyad cutoffs. With \(O=\{A_1,A_2,C,d,R,t,h\}\), define

\[
 w_\sigma(\omega;\boldsymbol v)=
 e_\sigma\mu(d_k)\mu(t')B_1(t';y)\overline{B_2(t';y)}
 \mathcal B_1(h)\mathcal A_\sigma\psi^{\rm out}_\sigma
       \prod_{\alpha\in O}z_\alpha^{iv_\alpha}.           \tag{9}
\]

Here \(B_1(t';y)\) and the mask \(\mathcal B_1(h)\) are distinct.
Define \(\widehat F_\sigma\) by the ordinary Fourier transform of
\(F_\sigma(e^{\boldsymbol u})\), with kernel
\(e^{-i\boldsymbol v\cdot\boldsymbol u}\). Fourier inversion gives

\[
 \mathcal T_{1,\sigma}=(2\pi)^{-9}
 \int_{\mathbb R^9}\widehat F_\sigma(\boldsymbol v)
 \sum_{\omega\in\Omega_\sigma}w_\sigma(\omega;\boldsymbol v)
       c_1P_1(y;\boldsymbol v)\overline{c_2P_2(y;\boldsymbol v)}
 \,d\boldsymbol v.                                      \tag{10}
\]

To check (10), expand the two finite column sums. Their modes are
\(z_{x_1}^{iv_{x_1}}\) and
\(\overline{z_{x_2}^{-iv_{x_2}}}=z_{x_2}^{iv_{x_2}}\).
Together with the seven outer modes these give all nine inversion
coordinates. Larger cutoffs equal one on every retained support. When an
old \(W\)-factor is nonzero the fresh column cutoff equals one; when
it is zero both the restored profile and the old expression vanish.
Equations (6)–(8) therefore restore every term of the masked formal
expression. The rapid Fourier decay proved below justifies the integral;
all pre-enlargement sums are finite at each fixed \(Z\).

Neither the sharp \(\mathcal B_1\) nor an indicator involving the
column-dependent kernel ratio enters (5). Both original \(\beta\)
factors, all punctures and the old-label multiplicity are still present
in (9). No support has yet been enlarged using a signed inequality.

### Uniform mass at every finite order

Let \(D_\alpha=z_\alpha\partial_{z_\alpha}\). The logarithmic support
of (5) is a fixed compact rectangle. For the kernel monomial let
\(e_h=1,e_d=e_R=-1,e_t=-2,e_{x_1}=e_{x_2}=-1\) and the other
exponents be zero. For any multi-index \(\boldsymbol a\),

\[
 D^{\boldsymbol a}\mathcal K_1(A\boldsymbol z^{\boldsymbol e})
 =\left(\prod_\alpha e_\alpha^{a_\alpha}\right)
  (u\partial_u)^{|\boldsymbol a|}\mathcal K_1(u)
       \big|_{u=A\boldsymbol z^{\boldsymbol e}}.           \tag{11}
\]

If a derivative falls in a coordinate absent from the monomial the
corresponding term is zero. There is no factor \(A^{|\boldsymbol a|}\)
outside the Euler derivative. By `lem:kernel-seminorms`, each fixed
Euler derivative is bounded on \([0,\infty)\) by finitely many
Schwartz seminorms of the normalized radial test. More explicitly, at
small \(u\) it is a polynomial combination of smooth Fourier
derivatives in the radial variable, and is bounded also at zero; at
large \(u\) its polynomial factors are controlled by Schwartz decay.
Equivalently \(u\partial_u=(\xi\cdot\partial_\xi)/2\) on the
radial Fourier transform. This covers arbitrarily small and arbitrarily
large positive \(A\), including the transition between them.

Euler derivatives of each real inverse power in (5) are fixed constants
times that same power, bounded on the fixed box. Euler derivatives of
either \(W\) monomial are controlled by its logarithmic seminorms.
Leibniz's rule, the fixed cutoff seminorms and (11) therefore give, for
every integer \(m\),

\[
 \max_{|\boldsymbol a|\le m}\|D^{\boldsymbol a}F_\sigma\|_\infty
 \le C_m Z^{-9\eta/2}\mathfrak S_{k(m)}^{b(m)},            \tag{12}
\]

where \(\mathfrak S_k\ge1\) collects the finitely many input smooth
and Schwartz seminorms; \(k(m),b(m)\) are finite and independent of
\(Z,A\) and all actual ideals. Inherited fixed normalized twists, if
present in those input tests, contribute only polynomial height factors,
with finite degrees depending on \(m\). They do not change the scale
exponent. This conclusion depends essentially on the fixed normalized
support and fixed radial-test contracts; it would not follow from
\(|\log_Zq_a-a_{\rm cen}|\le\eta\) alone.

For completeness, the particular smooth-calculus application uses an
integer \(m_0\) with \(2m_0>H+9\). Integration by parts on the compact
logarithmic support yields

\[
 (1+|\boldsymbol v|^2)^{m_0}\widehat F_\sigma(\boldsymbol v)
 =\widehat{(1-\Delta)^{m_0}F_{\sigma,\log}}(\boldsymbol v).
\]

Its absolute value is at most the fixed support volume times the
derivative bound (12) at order \(2m_0\). Since
\(\int_{\mathbb R^9}(1+|v|)^H(1+|v|^2)^{-m_0}\,dv<\infty\),

\[
 \int|\widehat F_\sigma(v)|(1+|v|)^H\,dv
 \le C_H Z^{-9\eta/2}\mathfrak S_{k_H}^{b_H}
 \le C_H\mathfrak S_{k_H}^{b_H}.                          \tag{13}
\]

Thus the required coarse exponent is \(\delta^{\rm mass}=0\) at
every fixed order, not a power of \(Z\) that increases with \(H\).
The small scalar in (13) occurs once in an already expanded quadratic
expression. We neither square that gain nor place another copy outside
the measure. The claimed coarse bound needs no small-amplitude gain.

### Positive enlargement and identification of the measure

For each fixed mode apply weighted Cauchy to the *whole*
\(\Omega_\sigma\) sum in (10):

\[
 \left|\sum_\omega w_\sigma U_1\overline{U_2}\right|
 \le\prod_{a=1}^2\left(\sum_\omega |w_\sigma||U_a|^2\right)^{1/2},
 \qquad U_a=c_aP_a.                                      \tag{14}
\]

Now the hypotheses on absolute outer magnitudes apply. The outer modes
have modulus one. The zeros of (8) and retained dyad cutoffs can be
bounded above; their removal is an inequality between nonnegative
sums. There is no factorization assumption on \(\beta(b,f)\).
For fixed old reconstruction, (7) depends on \(f,h\) only through
\(y\). Changing variables to that row and using (3) bounds the old
\(f,h\) multiplicity once. The support restriction becomes
\(0<q_y\le Z^{H_*}\), and the original \(-V\) normalization stays in
\(\kappa_a\). In particular no separate old-label count is left over.

Let \(\Phi_+\ge0\) be a fixed radial Schwartz majorant of the unit
ball. Remove only eligibility restrictions allowed by a nonnegative
upper bound, leaving the outer set

\[
 o=(b_1,b_2,\mathfrak A_1,\mathfrak A_2,C,d_k,t';
                     \text{assigned old slot primes})\in\mathfrak O_\sigma,
\]

with its individual supports, source reconstruction relations independent
of \(f,h,x\), assigned priority masks and \((C,J)=1\). Then

\[
 S_a(v)=\sum_{o\in\mathfrak O_\sigma}w_o^+
       \sum_{y\in\mathcal O}\Phi_+(q_y/Z^{H_*})|P_a(y;v)|^2
\]

is a positive squared row norm, and each factor before its square root
in (14) is at most
\(C Z^{\pi_\beta+\pi_{\rm old}}c_a^2S_a(v)\).
Here the row polynomial retains the dependence on \(o\) specified in
(7); it has not become independent of \(C,J,q_0,d_k,t'\).
The row sum converges: at fixed \(Z\) the column and outer sums are
finite, character magnitudes are at most one, and \(\Phi_+\) decays
faster than the lattice count. Adding \(y=0\) only increases the
positive sum, using the source's zero extension there. If the original
ball is empty, the masked component is zero and the inequality is
trivial; no claim about the later Poisson scale is needed in that case.

Taking the absolute Fourier integral in (10) and using (14) now gives

\[
 |\mathcal T_{1,\sigma}|
 \le C Z^{\pi_\beta+\pi_{\rm old}}
 \int_{\mathbb R^9}|\widehat F_\sigma(v)|
        \prod_{a=1}^2\left(Z^{\kappa_a+9\eta/2}S_a(v)\right)^{1/2}dv.
                                                               \tag{15}
\]

The constant includes \((2\pi)^{-9}\). Each side of (14) contains
the same single outer loss; taking two square roots in (15) gives one
\(Z^{\pi_\beta+\pi_{\rm old}}\), not its square.

For `eq:indexed-coefficient-measure` at this edge, take the discrete
index family to be a singleton (the already fixed \(\sigma\)) and
the common density to be \((2\pi)^{-9}|\widehat F_\sigma(v)|dv\).
Equation (13) verifies its mass hypothesis with exponent zero. The
commonness follows from (4)–(5): even when the row measure is enlarged
to the one defining \(S_a\), this Fourier density is the one fixed
on the original block, independent of \(o,y\). Its measurability and
integrability follow from the compact smooth logarithmic profile.
The density is used once against a product of row norms. No additional
squared-density or row-dependent selection measure is introduced.

The indices \(o,y\) are already summed inside \(S_a\). Neither they
nor the removed \(f,h\) can be added to the coefficient-measure index
set. Subsequent counting of \(q_0,J\), or summation over patterns
\(\sigma\), needs its own stated normalization and exponent audit.
The source's adjacent `eq:fixed-cube-count` is not used in (15), so it
is not implicitly verified here. Likewise the child's arithmetic
estimate and `eq:indexed-exponent-defect` remain to be checked before
the indexed propagation corollary can be applied to the full recursion.

The bounded audit therefore passes at exactly the stated conditional
interface, without enlarging any input contract.

## Mathlib

Full matching Mathlib coverage for this arithmetic first-transform edge
has not been checked. The source Fourier inversion, integration by
parts, radial Schwartz bounds and weighted Cauchy are analytic inputs;
their generic formal counterparts would not by themselves formalize
the contracted arithmetic, masks, support construction or recursion.
No absence claim or formal verification claim is made.
