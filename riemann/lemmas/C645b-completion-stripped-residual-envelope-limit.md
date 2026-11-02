# Corollary 645b: the completion-stripped convexity envelope misses the logarithmic grid

## Hypotheses

Retain L645 and C645a's fixed \(\delta\in(0,1/2)\), stipulated simple
zero \(\rho=\beta+i\gamma\), \(\beta=1/2+\delta\), \(\gamma\ge e^5\),
and unchanged \(s_*=2+i\gamma,a=3/2,d=a-\delta,R=a-\delta/2\), nodes,
matrix \(K_n\), \(A_\delta,q_\delta,\lambda_\delta\). Set

\[
 G(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2),\qquad g(s)=G'(s)/G(s),
 \quad u=\tfrac14-\tfrac\delta4,\quad v=\tfrac14-\tfrac\delta2.
\]

For a fixed integer \(n\ge1\), temporarily assume \(K_n\succeq0\).
Let \(P\) be any holomorphic positive-real interpolant on
\(\Re s>1/2\) supplied by L645: \(\Re P\ge0\) and
\(P(s_j)=F(s_j)\). It may depend on \(n\); constant purely imaginary
interpolants are included. No lower bound for \(|\zeta'(\rho)|\),
existence of such zeros, actual PSD or multiple-zero extension is assumed.
All asymptotics below fix \(\delta\), and all logarithms are natural.

## Conclusion

On a neighborhood of the unchanged closed disk \(|s-s_*|\le R\),
\(G\) is holomorphic and nonzero. The exact quotient is

\[
 Z_P(s)=\frac{\xi'(s)-P(s)\xi(s)}{G(s)}
       =\zeta'(s)+(g(s)-P(s))\zeta(s),                 \tag{1}
\]
\[
 Z_P(s_j)=0,\qquad Z_P(\rho)=\zeta'(\rho)\ne0.         \tag{2}
\]

For every fixed \(\epsilon>0\), there are positive constants
\(C_{\delta,\epsilon},D_{\delta,\epsilon}\) and a height onset,
independent of \(n,P\) and the stipulated zero, such that

\[
 0<\mathcal M_P:=\max_{|s-s_*|=R}|Z_P(s)|
 \le U_{\delta,\epsilon}(\gamma)
 :=C_{\delta,\epsilon}\gamma^{u+\epsilon}\log\gamma,
 \qquad
 0<|\zeta'(\rho)|\le D_{\delta,\epsilon}\gamma^{v+\epsilon}.
                                                               \tag{3}
\]
Temporary PSD therefore entails the necessary inequalities

\[
 1\le \frac{\mathcal M_P}{|\zeta'(\rho)|}q_\delta^n
   \le \frac{U_{\delta,\epsilon}(\gamma)}{|\zeta'(\rho)|}
          q_\delta^n.                                  \tag{4}
\]

The contraction obeys the sharper elementary comparison

\[
 0<\lambda_\delta<\frac{5\delta}{24}<\frac\delta4.       \tag{5}
\]
For \(N=\lfloor\log\gamma\rfloor\), the **explicit upper envelope's**
normalized test quantity satisfies

\[
 \frac{U_{\delta,\epsilon}(\gamma)}{|\zeta'(\rho)|}q_\delta^N
 \ge \frac{C_{\delta,\epsilon}}{D_{\delta,\epsilon}}
       \gamma^{\delta/4-\lambda_\delta}\log\gamma
 > \frac{C_{\delta,\epsilon}}{D_{\delta,\epsilon}}
       \gamma^{\delta/24}\log\gamma \longrightarrow\infty.       \tag{6}
\]
The limit means uniformly along any stipulated zeros at this fixed
displacement above the common onset; their existence is not asserted.

Thus this convexity/positive-real upper envelope cannot certify a
negative eigenvalue at the logarithmic grid through (4): the sufficient
strict condition \(U_{\delta,\epsilon}q_\delta^N<|\zeta'(\rho)|\)
eventually fails. This does **not** prove that
\(\mathcal M_P q_\delta^N/|\zeta'(\rho)|\) is forced to exceed one
without PSD, that the actual residual test fails, or that \(K_N\) is PSD.
Unlike C645a, this result supplies no unconditional polynomial lower
bound on the actual residual norm. Actual signs and RH remain open.
This specialization of imported analytic estimates passed a separate
critical audit on 1 November 2026, as recorded below. It is not a new
zeta growth theorem beyond the sources checked. The obstruction uses
the factorwise upper bound \(q_\delta^N\); no obstruction for the exact
finite Blaschke product is asserted.

## Proof

### Imported estimates and applicability

Reuse the source assessment saved before this calculation. The inputs are:

* NIST DLMF, version 1.2.8 (15 September 2026),
  [5.2(i), 5.2.2](https://dlmf.nist.gov/5.2#i): gamma has no zeros,
  its poles are the nonpositive integers, and \(\psi=\Gamma'/\Gamma\).
  [5.11.2](https://dlmf.nist.gov/5.11.E2) and the complex remainder
  paragraph of [5.11(ii)](https://dlmf.nist.gov/5.11#ii) give
  \(\psi(z)=\operatorname{Log}z-1/(2z)+O(|z|^{-2})\) uniformly
  on fixed closed sectors \(|\arg z|\le\pi-\vartheta\),
  \(\vartheta>0\). This is a direct digamma estimate, not a
  differentiated uncontrolled Stirling remainder.
* S. M. Gonek, *Mean values of the Riemann zeta-function and its
  derivatives*, Invent. Math. **75** (1984), 123–141, Section 2,
  equation (20), printed p.127 and its following Cauchy-estimate
  paragraph ([author-hosted published PDF](https://sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf)).
  Its unconditional cases, for \(\nu=0,1\), give
  \[
   |\zeta^{(\nu)}(\sigma+it)|
    \ll_{\nu,\epsilon}|t|^{(1-\sigma)/2+\epsilon}
       \quad(0\le\sigma\le1),
   \qquad
   |\zeta^{(\nu)}(\sigma+it)|\ll_{\nu,\epsilon}|t|^\epsilon
       \quad(\sigma>1).
  \]
  Use their uniform bounded-real-part form with epsilon slack, including
  the junction \(\sigma=1\). The inspected Cauchy paragraph supplies
  derivative uniformity by taking a fixed small circle and allowing a
  smaller epsilon in the zeroth-order estimate; its slight real-part
  displacement is absorbed in the displayed epsilon. We use a compact
  real-part range strictly above zero, so those circles can stay in
  \(\sigma>0\), and the high imaginary parts avoid the pole at 1.
  Neither RH nor selected heights from the adjacent logarithmic-derivative
  formula are hypotheses of (20).
* The absolute Dirichlet series and reciprocal series on \(\Re s=2\)
  in DLMF [25.2.6](https://dlmf.nist.gov/25.2.E6) and
  [27.4.3/5](https://dlmf.nist.gov/27.4) imply
  \[
   |\zeta'(2+it)|\le B_1:=\sum_{m\ge2}(\log m)m^{-2}<\infty,
   \quad |\zeta(2+it)|\ge1/\zeta(2).
  \]
  Termwise differentiation is valid by locally uniform absolute
  convergence in \(\Re s>1\), and the derivative series converges
  absolutely on this line. No reciprocal series in the strip is used.
* L645's imported finite Pick, Borel–Caratheodory and finite-Blaschke
  bounds, with the exact source citations in its proof. In particular
  the Blaschke input is S. Zakeri, *A Course in Complex Analysis*,
  [Notes and Comments, Section 8.3](https://zakerimath.com/CAbook/COM.html),
  complete finite-division argument after Example 8.33 (accessed
  1 November 2026). Only its ordinary bounded holomorphic version is
  needed; there is no weighted zero-set theorem or positivity of
  \(P-g\) being assumed.

These standard results are imported rather than reproved. The new local
work is their domain check, uniform quotient estimate and exponent
comparison. L258's growth-priced Taylor witness and C644a's fixed reserve
remain comparisons, not mathematical inputs to this calculation.

### Analytic domain, completion drift and uniformity in the interpolant

On the closed disk, \(\Re s\ge2-R=1/2+\delta/2>1/2\) and
\(\Im s\ge\gamma-R>0\). Its positive distance from the real axis
excludes every pole of \(\Gamma(s/2)\), the polynomial zeros \(0,1\)
and the zeta pole at 1. The exponential \(\pi^{-s/2}\) and gamma
have no zeros there. These properties persist on a neighborhood of the
compact disk inside \(\Re s>1/2\). Thus \(G,g,\zeta,\zeta',P\)
are holomorphic there and \(G\ne0\). L018's exact factorization
\(\xi=G\zeta\) gives (1). At each node \(\xi\ne0\), L645's
interpolation makes its numerator zero. C645a's exact identity (7)
at the stipulated simple zero gives
\(\xi'(\rho)/G(\rho)=\zeta'(\rho)\ne0\). This proves (2).

Every \(s/2\) on this disk has \(|\arg(s/2)|<\pi/2\) and modulus
comparable to \(\gamma\), uniformly over the disk as \(\gamma\to\infty\).
The digamma sector may therefore use the fixed \(\vartheta=\pi/2\).
The exact identity and the imported expansion yield, with the principal
logarithm on the right half-plane,

\[
 g(s)=\frac1s+\frac1{s-1}-\frac12\log\pi+\frac12\psi(s/2)
     =\frac12\operatorname{Log}\frac{s}{2\pi}+O(\gamma^{-1}).
                                                               \tag{7}
\]
Consequently \(\max|g(s)|\le\tfrac12\log\gamma+B\) on the disk
for a fixed constant \(B\) at sufficiently large heights. At its center,
the safe-line estimates give

\[
 |F(s_*)|\le |g(s_*)|+|\zeta'(s_*)/\zeta(s_*)|
           \le \tfrac12\log\gamma+B+\zeta(2)B_1.          \tag{8}
\]
L645's Borel–Caratheodory bound is valid for **every** such finite
positive-real interpolant, including the purely imaginary constant case:

\[
 |P(s)|\le A_\delta(1+|F(s_*)|),\qquad |s-s_*|\le R.   \tag{9}
\]
Equations (7)–(9) bound \(|g-P|\) by \(B_\delta\log\gamma\)
on the entire closed disk, independently of \(n\) and the choice of \(P\).
We bounded a difference by its two moduli; we did not assume it retained
the positive-real property or a favorable cancellation.

### Full-circle norm and unchanged zero contraction

An explicit uniform-in-\(P\) circle bound, before asymptotic estimates,
is

\[
 \mathcal M_P\le M_1+
       \bigl(g_R+A_\delta(1+|F(s_*)|)\bigr)M_0,         \tag{10}
\]
where \(M_\nu=\max_{|s-s_*|=R}|\zeta^{(\nu)}(s)|\) for
\(\nu=0,1\), and \(g_R=\max_{|s-s_*|=R}|g(s)|\).
No maximum was divided by a varying \(G\).

On this circle \(\sigma\in[1/2+\delta/2,7/2-\delta/2]\) and
\(t\in[\gamma-R,\gamma+R]\). Hence the maximum of
\(\max\{(1-\sigma)/2,0\}\) is exactly \(u\).
The imported uniform estimates, with \(t\) comparable to \(\gamma\),
give \(M_0+M_1\le B_{\delta,\epsilon}\gamma^{u+\epsilon}\).
Combining this with (7)–(10) proves the first bound in (3) with a
positive fixed \(C_{\delta,\epsilon}\). At \(\rho\), the same
derivative estimate has exponent \((1-\beta)/2=v\), giving the
second bound with a positive fixed \(D_{\delta,\epsilon}\).
Constants and onsets can be enlarged to a common one; they do not
depend on the zero, \(n\) or the interpolant. The same epsilon is
permitted in both bounds.

The maximum principle extends the boundary norm \(\mathcal M_P\)
throughout the disk, and (2) implies \(\mathcal M_P>0\). Its nodes
and the evaluation point have exactly L645's coordinates \(it_j\)
and \(-d\). Apply the imported finite-Blaschke bound to \(Z_P\):

\[
 |\zeta'(\rho)|\le\mathcal M_P
       \prod_{j=0}^{n-1}\left(\frac{R^2(d^2+t_j^2)}
                                  {R^4+d^2t_j^2}\right)^{1/2}
       \le\mathcal M_P q_\delta^n.
\]
All zeros are internal, the quotient is holomorphic on a neighborhood
of the closed disk, and the specified derivative is nonzero. Division
therefore gives (4), with precisely the unchanged contraction.

### Exponent comparison and what it does not imply

L645 gives \(\lambda_\delta>0\). Its formula also gives exactly

\[
 \lambda_\delta
 =\frac12\log\left(1+
   \frac{(R^2-d^2)(R^2-1)}{R^2(d^2+1)}\right).
\]
The fraction is positive. Since \(R-d=\delta/2\),
\(\log(1+x)<x\) for \(x>0\) gives

\[
 \lambda_\delta
 <\frac\delta4\frac{R+d}{d^2+1}\left(1-\frac1{R^2}\right)
 <\frac\delta4\frac32\frac59=\frac{5\delta}{24}.
\]
Here \(R+d<3\), \(d>1\), and \(1<R<3/2\) imply respectively
\((R+d)/(d^2+1)<3/2\) and \(0<1-R^{-2}<5/9\).
This proves (5) for every allowed fixed displacement.

Because \(N\le\log\gamma\),
\(q_\delta^N=e^{-\lambda_\delta N}\ge\gamma^{-\lambda_\delta}\).
Divide the **defined** upper envelope in (3) by the derivative upper
bound there. The epsilons cancel, \(u-v=\delta/4\), and (5) proves
(6), including its strict positive exponent gap. Above an existential
onset this quantity exceeds one strictly. This conclusion remains a
statement about a sufficient test, not about actual finite matrix signs.

In particular (3) has direction \(\mathcal M_P\le U\). A lower
bound on \(U/|\zeta'(\rho)|\) cannot be transferred to
\(\mathcal M_P/|\zeta'(\rho)|\). The proof has not transplanted
C645a's lower bound for a different completed maximum to this residual.
The deterministic gamma cost cancels in (1)–(2), but the resulting
absolute estimates still do not reach the prescribed grid.

For a quantitative description of the remaining gap, suppose one could
separately prove, uniformly in the admissible \(P\), a residual saving
\(\mathcal M_P\le C\gamma^{u+\epsilon-\kappa}\log\gamma\)
and a derivative lower bound
\(|\zeta'(\rho)|\ge c\gamma^{v-\eta}\), \(c>0\), \(\eta\ge0\).
Since \(N>\log\gamma-1\), these would make the exact residual
test strictly less than one eventually provided

\[
             \kappa>\delta/4-\lambda_\delta+\epsilon+\eta.
                                                               \tag{11}
\]
Indeed its upper bound would be
\((C/c)e^{\lambda_\delta}\gamma^{\delta/4-\lambda_\delta+
\epsilon+\eta-\kappa}\log\gamma\), which tends to zero. Neither
estimate is established here. Even a derivative matching its convexity
upper exponent would require a residual power saving greater than
\(\delta/4-\lambda_\delta>\delta/24\), apart from epsilon slack.
A derivative lower bound alone cannot rescue the displayed unsaved
envelope. This identifies the scale of the missing input, not a
licensed continuation to derive it or an assertion that it is true.

### Independent critical audit — 1 November 2026

**Verdict: accepted with no mathematical repair or stronger estimate.**
The audit reused the invocation-start SPECIALIZE assessment and its
inspected primary-source statements. It checked the specialization
against L018, L645 and C645a; it did not reprove those source theorems
or retrieve them again. The following details record the load-bearing
checks, including the precise limit of the stopping result.

1. **Analytic quotient and zero values.** The disk's left edge is
   \(1/2+\delta/2>1/2\) and its bottom edge has positive imaginary
   part. Thus its distance from \(0,1\), every gamma pole, and the
   zeta pole is positive. Compactness supplies a neighborhood within
   the positive-real interpolant's domain on which \(G\ne0\).
   L018's factorization holds throughout this neighborhood. The
   quotient in (1) is consequently holomorphic even at zeros of zeta;
   it is not a logarithmic derivative there. At the sample nodes,
   \(\xi\ne0\) and finite interpolation makes the numerator zero.
   At \(\rho\), \(\zeta=0\) and C645a (7) gives exactly the
   nonzero value \(\zeta'(\rho)\). Simplicity licenses division
   only; no quantitative lower bound follows from it.
2. **Completion drift and every admissible interpolant.** The points
   \(s/2\) have positive real part, argument in the fixed closed
   sector \(|\arg z|\le\pi/2\), and modulus comparable to
   \(\gamma\). The imported digamma remainder is therefore uniform.
   Substitution into the exact expression for \(g\) leaves the
   rational correction \(1/(2s)+1/(s-1)+O(\gamma^{-2})\),
   which is \(O(\gamma^{-1})\) on the disk. The bounded imaginary
   part of the principal logarithm justifies the stated modulus
   bound. The absolute and reciprocal series used at the anchor are
   both restricted to \(\Re s=2\). L645's Borel–Caratheodory
   argument applies to \(-P\), with positive upper bound 1 on
   the larger radius-\(a\) disk, and its center is a node for every
   \(n\). Hence (9) includes singular Pick data and purely imaginary
   constant interpolants and has no hidden dependence on \(n,P\).
   Subtracting \(g\) does not preserve positivity and is never
   treated as doing so.
3. **Uniformity across real part one.** Put
   \(p(\sigma)=\max\{(1-\sigma)/2,0\}\). This continuous
   function is \(1/2\)-Lipschitz, including at 1. For a requested
   \(\epsilon>0\), take a fixed Cauchy radius
   \(r=\min\{1/8,\epsilon\}>0\) and use the imported
   zeroth-order bound with slack \(\epsilon/2\). The small circles
   centered anywhere on the large circle, or at \(\rho\), have
   real parts strictly above \(3/8\) and bounded above, and
   imaginary parts comparable to \(\gamma\). On each such circle,
   \(p(\sigma')\le p(\sigma)+r/2\). The inspected Gonek cases
   on both sides of 1 and at 1 therefore bound the zeroth derivative
   by a constant times
   \(\gamma^{p(\sigma)+\epsilon/2+r/2}
   \le\gamma^{p(\sigma)+\epsilon}\).
   Cauchy's estimate introduces the fixed factor \(1/r\), absorbed
   in the constant, and proves the required derivative uniformity.
   The high circles avoid the pole. Thus the circle exponent is
   \(u\), the zero exponent is \(v\), and the same final epsilon
   can be used in both estimates. Constants and onsets remain
   independent of the stipulated zero, \(n\), and \(P\), while
   dependence on fixed \(\delta,\epsilon\) is allowed.
4. **Blaschke contraction and the strict gap.** The samples satisfy
   \(|it_j|<1<R\) and the evaluation point satisfies \(d<R\).
   The maximum principle and (2) give \(\mathcal M_P>0\), so
   the imported finite-zero bound applies to this analytic quotient.
   Its exact factors are those of L645 (6); there is no division of
   a circle maximum by a varying completion factor. Direct subtraction
   gives
   \[
   q_\delta^{-2}-1
    =\frac{(R^2-d^2)(R^2-1)}{R^2(d^2+1)}>0.
   \]
   With \(R-d=\delta/2\), the strict logarithmic inequality gives
   exactly the first bound in the proof of (5).
   The independent inequalities \(R+d<3\), \(d^2+1>2\),
   and \(1-R^{-2}<5/9\) yield
   \(\lambda_\delta<5\delta/24\). All denominators are
   positive on \(0<\delta<1/2\); the endpoints are not included.
5. **Envelope direction, floors, and the conditional saving test.**
   For \(N=\lfloor\log\gamma\rfloor\),
   \(q_\delta^N\ge\gamma^{-\lambda_\delta}\), including
   integral \(\log\gamma\). Dividing the defined positive
   \(U\) by the derivative upper bound gives a lower bound on
   \(U/|\zeta'(\rho)|\). The epsilons cancel, leaving
   \(u-v-\lambda_\delta=\delta/4-\lambda_\delta
   >\delta/24\), proving (6). In the separate hypothetical
   saving calculation, the opposite bound
   \(q_\delta^N<e^{\lambda_\delta}\gamma^{-\lambda_\delta}\)
   follows from \(N>\log\gamma-1\) and gives precisely (11).
   The proposed residual saving and derivative lower bound are
   unproved assumptions, not inputs to the established obstruction.
6. **Exact scope of the stop.** Write, solely to identify the
   quantity already in the proof,
   \[
   B_{\delta,n}=\prod_{j=0}^{n-1}b_\delta(j/n),\qquad
   b_\delta(t)^2=\frac{R^2(d^2+t^2)}{R^4+d^2t^2}.
   \]
   L645's monotonicity check gives
   \(B_{\delta,n}\le q_\delta^n\). Therefore a lower bound
   on \(Uq_\delta^N/|\zeta'(\rho)|\) says nothing about
   a lower bound on \(UB_{\delta,N}/|\zeta'(\rho)|\).
   Likewise \(\mathcal M_P\le U\) prevents transferring (6)
   to the actual residual. Neither the exact-product contraction
   rate nor a lower bound on \(\mathcal M_P\) is proved here.
   The accepted obstruction is only the displayed convexity envelope
   combined with the factorwise \(q_\delta^N\) bound. It is not
   a failure theorem for every unchanged-disk certificate.

The audit validates this qualified local input and preserves the separate
C645a completed-growth and C644a fixed-reserve stops. It makes no claim
of progress beyond the imported analytic estimates, actual matrix signs,
existence of off-line zeros, uniformity as \(\delta\to0\), or an
extension to multiple specified zeros. L258 and C644a remain comparisons
only. The direct mathematical inputs are unchanged, so the DAG row needs
no modification. All checks were analytic; no numerical test or script
was needed. Any exact-product improvement is a separately gated target.

## Mathlib

Supporting Borel–Caratheodory is present as `Complex.borelCaratheodory`
at the frozen commit and with the positive-bound hypotheses cited in
L645 ([documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/BorelCaratheodory.html#Complex.borelCaratheodory)).
Full matching coverage for this quotient comparison, Gonek's estimates,
the gamma/digamma specialization and finite-Blaschke division has not
been checked; no absence is claimed. No Lean replay, numerical evidence
or mathematical script is used. The separate audit above checks the
informal specialization; it is not a formal verification.
