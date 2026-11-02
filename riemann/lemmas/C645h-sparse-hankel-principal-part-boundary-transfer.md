# Corollary 645h: sparse Hankel principal parts force a boundary residual

## Hypotheses

Fix

\[
 0<\delta<\tfrac12,\quad 0<\eta<\tfrac\delta2,\quad
 d=\tfrac32-\delta,\quad R=\tfrac32-\tfrac\delta2,\quad x=-d,
 \qquad n\in\mathbb Z,\ n\ge5.
\]

Set \(t_j=j/n\), \(0\le j<n\), and retain the complex product

\[
 B_n(z)=\prod_{j=0}^{n-1}\frac{R(z-it_j)}{R^2+it_jz}.
 \tag{1}
\]

Let \(Z\) be a finite set of distinct points in \(|a|\le R-\eta\),
containing \(x\) and avoiding all \(it_j\). Let \(r_a\) be positive
integers and put \(M=\sum_{a\in Z}r_a\). These integers specify
residues, not pole orders. Retain C645g's explicit constants

\[
 s=\delta/64,\quad A_\delta=1+\log(256R/\delta),\quad
 \rho_*=(d+2s)/R,\quad
 c_\delta=\frac{\sqrt{1-\rho_*^2}}{2s},\quad
 \kappa_\delta=\frac{\delta}{16A_\delta},
 \qquad M\le\kappa_\delta n.
 \tag{2}
\]

Let \(F\) be meromorphic on an open neighborhood of \(|z|\le R\).
Its complete pole set in that closed disk is exactly \(Z\); each pole
\(a\) is simple and has residue \(r_a\). Let \(P\) be holomorphic
on an open neighborhood of that disk and satisfy the exact interpolation

\[
                     P(it_j)=F(it_j)\quad(0\le j<n).
 \tag{3}
\]

All these data and their neighborhoods may depend on \(n\). No symmetry,
pole separation, degree bound on \(P\), actual-Xi realization or boundary
upper bound is assumed.

On \(|\zeta|=1\), define

\[
 g(\zeta)=\frac{B_n(x)[F(R\zeta)-P(R\zeta)]}{B_n(R\zeta)},
 \qquad
 q(\zeta)=\sum_{a\in Z}
       \frac{r_a B_n(x)}{R B_n(a)}\frac1{\zeta-a/R}.
 \tag{4}
\]

Use normalized circle measure \(d\theta/(2\pi)\), \(H^2\) with
nonnegative Fourier modes, and \(H^2_-\) with strictly negative modes.
For a bounded circle symbol \(v\), set
\(H_v f=P_-(vf):H^2\to H^2_-\).

## Conclusion

There is a function \(h\), holomorphic on a neighborhood of the closed
disk \(|z|\le R\), for which the full principal-part identity is

\[
 \frac{B_n(x)[F(z)-P(z)]}{B_n(z)}
   =B_n(x)\sum_{a\in Z}\frac{r_a}{B_n(a)(z-a)}+h(z).
 \tag{5}
\]

Here every grid singularity on the left is removed; the equality is
meromorphic at \(Z\). In particular,

\[
 H_g=H_q,\qquad
 \boxed{\displaystyle
 E_n:=\max_{|z|=R}|F(z)-P(z)|
       \ge\frac{c_\delta e^{-\delta n/8}}{|B_n(x)|}.}
 \tag{6}
\]

The anchor modulus is retained exactly:

\[
 |B_n(x)|=\prod_{j=0}^{n-1}
       \frac{R\sqrt{d^2+t_j^2}}{\sqrt{R^4+d^2t_j^2}}>0.
 \tag{7}
\]

This is a synthetic necessary boundary size. It supplies neither an
upper bound nor actual-Xi signs. A separate conceptual audit on
1 November 2026 verified the complete application below without a
mathematical correction; its checks are recorded at the end of the proof.
This local specialization is not an originality claim or an RH
resolution candidate.

## Proof

### Imported tools and the scope of the specialization

The invocation-start
[SPECIALIZE assessment](../drafts/literature/2026-11-01-sparse-hankel-principal-part-transfer.md)
covers exactly these data, (4), and the proposed conclusions (5)--(6).
Import the local simple-pole decomposition from M. Beck et al.,
*A First Course in Complex Analysis*, online unversioned
[Theorem 8.1.7(i), including its simple-pole proof](https://complexanalysis.org/web/sec_residue-thm.html):
a simple pole of residue \(r\) has local expression
\(r/(z-a)\) plus a holomorphic function. That primary case was inspected
in the saved source review; it is not reproved here.

For the normalized Hardy spaces, contractive orthogonal projection,
finite principal-part decomposition and Hankel convention, use
L. Baratchart, S. Chevillard and T. Qian, *Minimax principle and lower
bounds in H2-rational approximation*, J. Approx. Theory **206** (2016),
17--47, [Section 2 pp.18--21; (17)--(19) pp.24--25;
analytic-term removal in (25) pp.27--28](https://www.must.edu.mo/images/SCSE/qiantao/QianTao_P147.pdf),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004).
The saved review inspected these passages. No Nehari/AAK norm-distance
identity is needed here: only the definition of \(H_v\), removal of a
bounded analytic multiplier, and the one-sided contraction bound are
used. The multiplier hypothesis is verified below for every input.

C645g supplies the quantitative norm bound. The checks of this particular
quotient, grid, transformed residues and scaling are necessary because
the sources do not assert (5) for the specified \(F,P,B_n\).
C645f's rational-factor calculation is a restricted predecessor, not
an application of its one-to-three-pole theorem to this larger family.
C645d's scalar cancellation remains a comparison, not a premise.

### 1. Every grid point is removable

The parameter bounds imply \(1<d<R<3/2\) and \(R>5/4\). For
\(|z|\le R\),

\[
 |R^2+it_jz|\ge R^2-t_jR\ge R^2-R>0.
 \tag{8}
\]

Thus all denominators in (1) are nonzero on the disk and, by compactness
and finiteness, on some neighborhood of it. The zeros of \(B_n\) there
are exactly the distinct grid points. Each is simple, since

\[
 B_n'(it_j)=\frac{R}{R^2-t_j^2}
       \prod_{\ell\ne j}\frac{Ri(t_j-t_\ell)}{R^2-t_\ell t_j}
       \ne0.
 \tag{9}
\]

Every denominator in (9) is positive because \(R^2>1\); every displayed
numerator is nonzero. This includes \(j=0\). Hence \(B_n(a)\ne0\)
for every \(a\in Z\), and in particular \(B_n(x)\ne0\).

Write \(W=F-P\). At each grid point \(b=it_j\), grid avoidance
ensures that \(W\) is holomorphic. Equation (3) gives \(W(b)=0\),
so locally \(W(z)=(z-b)w_j(z)\) with \(w_j\) holomorphic.
Also \(B_n(z)=(z-b)b_j(z)\), with \(b_j\) holomorphic and
\(b_j(b)=B_n'(b)\ne0\). Therefore

\[
 \mathcal A(z):=\frac{B_n(x)W(z)}{B_n(z)}
        =B_n(x)\frac{w_j(z)}{b_j(z)}
 \tag{10}
\]

extends holomorphically through that point. This accounts for every
one of the \(n\) grid nodes, without a degree restriction on \(P\).
Before removal the possible residue would be
\(B_n(x)[F(it_j)-P(it_j)]/B_n'(it_j)=0\); (10) establishes actual
removability rather than merely vanishing residue.

### 2. Every genuine pole is removed by the stated principal parts

At \(a\in Z\), the imported simple-pole rule and holomorphy of \(P\)
give \(W(z)=r_a/(z-a)+v_a(z)\) with \(v_a\) holomorphic.
The multiplier \(k(z)=B_n(x)/B_n(z)\) is holomorphic near \(a\).
Writing \(k(z)=k(a)+(z-a)\widetilde k_a(z)\) gives

\[
 \mathcal A(z)=\frac{r_a B_n(x)}{B_n(a)(z-a)}
                  +\text{a function holomorphic near }a.
 \tag{11}
\]

No conjugation or residue modulus has been introduced. At the anchor,
the coefficient is exactly \(r_x\). In physical disk coordinates,
the definition of \(q\) in (4) gives

\[
 Q(z):=q(z/R)=B_n(x)\sum_{a\in Z}
                      \frac{r_a}{B_n(a)(z-a)}.
 \tag{12}
\]

Indeed \((z/R-a/R)^{-1}=R/(z-a)\) cancels exactly the \(1/R\)
in each amplitude of \(q\). Thus \(Q\) has exactly the principal
parts (11). Define \(h=\mathcal A-Q\) away from the finite exceptional
set. At each genuine pole (11) removes its only singular term; all
other summands of \(Q\) are holomorphic locally, since \(Z\) is
distinct. At each grid point \(Q\) is holomorphic by grid avoidance,
and (10) removes the singularity of \(\mathcal A\).

There are no other singularities in the closed disk: its complete
pole list for \(F\) is stipulated, \(P\) is holomorphic, and (8)--(9)
account for the grid quotient. In particular all functions in this
difference are holomorphic locally at each boundary point, since
\(|a|\le R-\eta<R\) and \(|it_j|<1<R\). The original neighborhood
hypotheses and these local removals give a holomorphic extension of
\(h\) on an open set containing the whole closed disk. Compactness
then permits a smaller such set containing a disk \(|z|<R+\epsilon\)
for some \(\epsilon>0\). Possible poles of \(F\) outside the original
closed disk cause no difficulty: choose this smaller set inside the
union of the pole-free boundary neighborhoods and the interior removal
neighborhoods. No uniform \(\epsilon\) in the moving data is asserted.
This proves (5), with a bounded remainder on the closed disk.

### 3. The analytic part vanishes for every Hardy input

Set \(u(\zeta)=h(R\zeta)\). It is holomorphic on a neighborhood
of the closed unit disk, so its boundary values are bounded and have
no negative Fourier modes. Restricting (5) to the boundary yields

\[
                         g=q+u.
 \tag{13}
\]

The symbols \(g,q\) are continuous and bounded there: all their
genuine poles lie strictly inside the disk, and \(B_n\) is nonzero
on its boundary. For completeness, the bounded analytic multiplier
premise holds for every \(f\in H^2\), not just \(f=1\).
Choose analytic polynomials \(p_k\to f\) in circle \(L^2\), by
truncating its nonnegative Fourier series. The Taylor series of \(u\)
converges uniformly on the closed disk, so every \(up_k\) belongs
to \(H^2\). Moreover,

\[
 \|up_k-uf\|_2\le\|u\|_\infty\|p_k-f\|_2\longrightarrow0.
 \tag{14}
\]

The nonnegative Fourier subspace \(H^2\) is closed in \(L^2\),
so \(uf\in H^2\) and \(P_-(uf)=0\). Applying the imported projection
convention to (13) proves \(H_gf=H_qf\) for every \(f\in H^2\).
Both operators are bounded, since their symbols are bounded. Thus
\(H_g=H_q\) as bounded operators with the stated domain and codomain.
Neither uniform control of \(\|u\|_\infty\) over the data nor removal
of \(P\) alone was assumed or used.

### 4. The boundary comparison and exact normalization

For \(|z|=R\), direct expansion gives, for each real \(t=t_j\),

\[
 R^2|z-it|^2=R^4+R^2t^2-2R^2t\operatorname{Im}z
                         =|R^2+itz|^2.
 \tag{15}
\]

Together with (8) this proves \(|B_n(z)|=1\) on the entire circle.
At \(x=-d\), direct evaluation of each modulus gives exactly (7).
The boundary residual has no pole and is continuous, so \(E_n\) exists
and is finite. The rescaling \(z=R\zeta\) maps the unit circle onto
this circle, whence

\[
                       \|g\|_\infty=|B_n(x)|E_n.
 \tag{16}
\]

The projection \(P_-\) is contractive in the normalized \(L^2\) norm.
For every \(f\in H^2\),

\[
 \|H_gf\|_2\le\|gf\|_2\le\|g\|_\infty\|f\|_2.
 \tag{17}
\]

Consequently \(\|H_g\|\le\|g\|_\infty\); equality with this
particular boundary representative is neither needed nor asserted.
All hypotheses of C645g coincide exactly with (1)--(2) and (4),
including positive integer residues, distinct grid-avoiding poles,
clearance, \(n\ge5\), normalized measure and strictly negative modes.
Its audited bound is \(\|H_q\|\ge c_\delta e^{-\delta n/8}\).
Using (13)--(17) therefore gives

\[
 c_\delta e^{-\delta n/8}\le\|H_q\|=\|H_g\|
                  \le |B_n(x)|E_n,
\]

which proves (6) after division by the nonzero anchor modulus.
No additional factor \(R\) is introduced by the circle parametrization:
the symbol already has the scale (12), and the final estimate uses
operator and supremum norms, not a physical contour integral.

### Qualifications and remaining gap

This establishes the approved full residual transfer for any finite
family satisfying the small total-residue census (2), including arbitrarily
close distinct poles. It does not extend to higher-order poles, weaken
exact interpolation, assert a uniform analytic-remainder bound, or supply
any actual-Xi input. Empty small-\(n\) census cases remain empty, as
in C645g. The complex amplitudes in (4) can still exhibit C645d's scalar
cancellation; the full Hankel norm need not cancel with that scalar.

A contradiction would require an independently justified boundary upper
bound \(U_n\) under these same hypotheses with
\(|B_n(x)|U_n<c_\delta e^{-\delta n/8}\). No such bound is proved.
Actual-Xi census with this coefficient, contour selection and clearance,
and interpolant realization remain separate gaps, as does the main
all-degree mixed-positivity/sign problem. The result is a local
specialization of standard complex-analysis/Hardy tools and C645g,
not progress beyond the sources checked or a complete RH argument.

### Independent conceptual audit — 1 November 2026

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-01-c645h-boundary-transfer-audit.md`
approved this exact audit. The complete proof (1)--(17) was checked
against C645g's quantitative statement (1)--(6), its application
qualification, and the parent's inspected primary-source statements.
The following is a verification of the stated specialization, not a
new bound, a fresh audit of those source proofs, or a second audit of
C645g's already audited quantitative proof.

* **Parameters and nonempty cases.** The hypotheses give
  \(R-d=\delta/2>\eta\), so the anchor lies in the permitted pole
  disk. Also \(d+2s=R-15\delta/32<R\) and \(d+2s>0\), so
  \(0<\rho_*<1\), \(c_\delta>0\), and
  \(\kappa_\delta>0\). These are exactly C645g's constants.
  Since \(x\in Z\) and \(r_x\ge1\), \(M\ge1\); for
  \(\kappa_\delta n<1\) there are no admissible data. The result
  makes no existence claim in those cases and no uniform claim as
  \(\delta\) tends to zero.
* **All grid nodes.** The denominator estimate (8) includes
  \(t_0=0\). The derivative (9) has no zero factor: its distinct
  node differences are nonzero and its real denominators exceed zero.
  Exact interpolation and holomorphy give local divisibility by the
  corresponding linear factor, so (10) proves removability, including
  when the numerator has higher vanishing order. Vanishing residue
  alone would not have sufficed without this local argument.
* **All genuine poles and the collar.** The complete pole list is
  essential. The holomorphic multiplier at each pole gives precisely
  (11), with its complex phase intact; distinctness makes every other
  principal part holomorphic there. After subtracting them, the grid
  nodes are also regular. Every boundary point is regular by the
  original neighborhood hypotheses and interior clearance. These
  compatible local extensions give an open set containing the compact
  closed disk; it contains some larger concentric open disk. Thus the
  collar argument does not assume a lower bound for its width or
  neglect an exterior pole accumulating at a boundary point.
* **Scaling.** Substitution in (4) gives exactly (12). In physical
  coordinates the anchor residue is \(r_x\); in unit-disk coordinates
  it is \(r_x/R\). The factor \(1/R\) is therefore necessary and
  correctly retained. No conjugate, absolute residue, or pole order
  \(r_a\) is substituted for the stated simple-pole residue.
* **Every Hardy input.** The collar gives a Taylor series for
  \(u=h(R\,\cdot)\) converging uniformly on the closed unit disk.
  For each fixed set of data its boundary norm is finite. Polynomial
  approximation and (14) then place \(uf\) in the closed
  nonnegative-mode subspace for every \(f\in H^2\). This proves
  the bounded-operator identity, rather than only the identity on the
  constant input. Uniform control of the remainder as \(n\) varies
  is unnecessary for this argument.
* **Norm and direction.** Expanding (15) gives the same cross term
  \(-2R^2t\operatorname{Im}z\) on both sides. Hence (16) holds
  exactly, and contractivity gives
  \(c_\delta e^{-\delta n/8}\le\|H_q\|=\|H_g\|
  \le |B_n(x)|E_n\).
  The normalized circle measure and Fourier subspaces match C645g.
  Neither a physical arclength factor nor a norm/distance equality is
  inserted; division by the strictly positive modulus (7) proves (6).

Verdict: the stated full principal-part transfer and boundary lower
bound are valid under the complete hypotheses, with no correction or
strengthening. Only C645g's quantitative theorem is used as a local
mathematical input; the other corollaries mentioned above are comparisons.
C645d's scalar cancellation and C645b's qualified envelope stop remain
unaffected. No degree bound or positive-real property of P, actual-Xi
census, uniform collar, new zero-free premise or boundary upper bound
has entered the argument. The independent upper-bound threshold in the
preceding qualification remains strictly \(|B_n(x)|U_n<
c_\delta e^{-\delta n/8}\); equality would not give a contradiction.
This audit establishes the reliability of this local bridge, not
progress beyond the cited general tools or a resolution of the sign gap.

## Mathlib

Full matching Mathlib coverage is **not checked**; availability is unknown.
No Mathlib theorem is claimed to formalize (5), the bounded multiplier
application or (6). The precise informal inputs and their inspected scope
are cited above. Documentation validation is not Lean verification.
