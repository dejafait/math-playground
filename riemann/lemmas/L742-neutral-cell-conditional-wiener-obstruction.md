# L742: Conditional Wiener obstruction to summable neutral-cell coupling

## Hypotheses

Use L740's complete causal generator on the original complex space
\(X_L=L^2(0,L)\), with inner product linear in the first argument.
For smooth compactly supported functions in that interval set

\[
 H_L(u,v)=-\tfrac12(\langle A_Lu,v\rangle+
                              \langle u,A_Lv\rangle),
 \qquad E_L(u)=H_L(u,u).
 \tag{1}
\]

Let \(\ell=\log(3)/2\) and define

\[
 \mathcal N=\{f\in C_c^\infty(0,\ell):
          \int e^{x/2}f(x)dx=\int e^{-x/2}f(x)dx=0\}.
 \tag{2}
\]

All functions are extended by zero; put
\(F_f(t)=\int f(x)e^{-itx}dx\) and
\((\tau_m f)(x)=f(x-m\ell)\). For integers \(m\ge2\), let
\(L_m=(m+1)\ell\) and retain the original definition

\[
 \beta_m=\sup_{f,g\in\mathcal N\setminus\{0\}}
   \frac{|H_{L_m}(f,\tau_m g)|}
        {\sqrt{E_\ell(f)E_\ell(g)}}.
 \tag{3}
\]

L741 supplies the strictly positive diagonal energy on the length-ell
cell, including its qualification that Zhu's cited local sign
certificate was not locally replayed. No larger-window positivity
or larger-window closed-form domain is an unconditional input.

**Assume RH only for the conditional conclusions below.** Write
\(\mathcal Z\) for the distinct real ordinates of zeros of
\(\xi(1/2+it)\), and \(r_\gamma\) for their positive integer
multiplicities. The named external inputs are:

- Suzuki, *Aspects of the screw function corresponding to the Riemann
  zeta-function*, [arXiv:2206.03682v4, pinned PDF](https://arxiv.org/pdf/2206.03682v4),
  internal date 31 May 2023, Theorem 1.1(2), Section 2.2 (printed p.7),
  and Sections 3.2–3.5, especially (3.3), (3.5), Proposition 3.1 and
  the distributional identity on printed pp.10–11. These give the
  compact-smooth zero pairing, with multiplicities. The order-one
  Hadamard product in Section 2.2 supplies
  \(\sum_\gamma r_\gamma/(1+|\gamma|^2)<\infty\).
  The differently dated served HTML is not substituted for this PDF.
- Suzuki, *Weil's quadratic form via the screw function*,
  [arXiv:2606.09096v3](https://arxiv.org/html/2606.09096v3),
  23 September 2026, Section 1.1's displayed definition of \(W\)
  and Sections 2.3–2.5, (2.5)–(2.10), for the same geometric
  normalization on compact smooth tests. Only compact-test formulas
  are used, not an inference of global temperedness from continuity.
- Cuny, Eisner and Farkas, *Wiener's lemma along primes and other
  subsequences*, [BUW-IMACM 18/22](https://imacm.uni-wuppertal.de/fileadmin/imacm/preprints/2018/imacm_18_22.pdf),
  4 January 2019, Theorem 1.1, printed p.1: for a finite complex
  Borel measure \(\mu\) on the unit circle, with
  \(\widehat\mu(n)=\int z^n d\mu(z)\), the Cesaro mean of
  \(|\widehat\mu(n)|^2\) tends to
  \(\sum_z|\mu(\{z\})|^2\). This theorem is imported, not reproved.

## Conclusion

The space \(\mathcal N\) contains a nonzero function. In fact, for
every fixed \(0\ne f\in\mathcal N\), put \(d_f=E_\ell(f)>0\).
Under RH the measure

\[
 \mu_f=\sum_{\gamma\in\mathcal Z}
       r_\gamma|F_f(\gamma)|^2\delta_{e^{i\ell\gamma}}
 \tag{4}
\]

is finite, positive and purely atomic, with total mass \(d_f\).
The complete causal pairing satisfies

\[
 h_m:=H_{L_m}(f,\tau_m f)=\widehat\mu_f(m),\qquad m\ge2,
 \tag{5}
\]

and consequently

\[
 \lim_{M\to\infty}\frac1M\sum_{m=2}^M|h_m|^2
   =\sum_{z\in\mathbb T}
       \left(\sum_{\substack{\gamma\in\mathcal Z\\e^{i\ell\gamma}=z}}
                r_\gamma|F_f(\gamma)|^2\right)^2
   =:s_f>0.
 \tag{6}
\]

Thus, still conditionally on RH,

\[
 \liminf_{M\to\infty}\frac1M\sum_{m=2}^M\beta_m^2
       \ge s_f/d_f^2>0,
 \qquad \sum_{m\ge2}\beta_m=\infty.
 \tag{7}
\]

This is a reproduction/specialization of the smooth Weil identity
and Wiener atom theorem. It supplies no new general spectral theorem,
no unconditional nonsummability statement, and no proof or disproof
of RH. The numerical size of \(s_f\) is not evaluated. The result
parks absolute summability as a proposed sufficient mechanism in the
RH setting; moment complements, adjacent interactions and an
unconditional global sign argument remain unresolved. The separate
conceptual audit in Section 5 (4 November 2026, step 282) passes for
this conditional specialization, with the source-computation
qualification from L741 retained.

## Proof

### 1. A neutral smooth profile and its positive denominator

Choose a nonzero \(\phi\in C_c^\infty(0,\ell)\) and put
\(f=\phi''-\phi/4\). Twice integrating by parts, with no endpoint
terms, gives
\(\int e^{ax}f(x)dx=(a^2-1/4)\int e^{ax}\phi(x)dx\).
This vanishes for both \(a=1/2\) and \(a=-1/2\).
If \(f=0\), then
\(0=\Re\int f\overline\phi=-\|\phi'\|_2^2-\|\phi\|_2^2/4\),
contrary to the choice of \(\phi\). Thus \(\mathcal N\ne\{0\}\).

Any such smooth function belongs to L740's generator domain on
every encompassing finite interval. Indeed
\(\Phi_u=(\mathbf1_{(0,\infty)}\log)*u\) has derivative
\((\mathbf1_{(0,\infty)}\log)*u'\); on a finite interval these
are continuous and the derivative is bounded by local integrability
of the logarithm and boundedness of \(u'\). Hence \(\Phi_u\) is
absolutely continuous with derivative in \(L^2\), as required.

The diagonal value in a larger interval is unchanged, since the
pairing integrates only on the support of the same function and
the causal kernels there are unchanged. L741's half-cell result
therefore gives \(d_f\ge c_*\|f\|_2^2>0\),
\(c_*=8.9\cdot10^{-18}\). Only this finite-cell input is used.

### 2. Complete smooth energy on each finite window

Here \(L\) is any finite positive number, and
\(u\in C_c^\infty(0,L)\). Set
\(a_n=\Lambda(n)/\sqrt n\) and
\(C_u(v)=\int u(x+v)\overline{u(x)}dx\).
The normalization identities in L741 Section 2 are kernel identities
independent of its chosen window. With

\[
 k(v)=\frac{2e^{-v/2}}{1-e^{-2v}},\quad
 r(v)=k(v)-\frac{e^{-v}}v,\quad c=\log(2\pi),
\]

they give, on these smooth tests,

\[
 A_Lu=(Bu)|_{(0,L)}+cu+R_Lu-4V_Lu
           +2\sum_{2\le n<e^L}a_nT_{\log n}u.
 \tag{8}
\]

Here \(B\) is the full-line multiplier \(-\log(1+it)\),
\(R_L\) is causal convolution by the integrable kernel \(r\),
and \(V_L\) is finite-interval causal convolution by \(\cosh(v/2)\).
Equation (8) follows from L740's full finite delay sum and
\(q(v)-(e^{-v}-1)/v=r(v)-4\cosh(v/2)\). It is not an
extension of a closed-form domain theorem to larger windows.

Plancherel and the transform of \(r\) calculated in L741 give
\(w(t)-c-\Re\widehat r(it)=\Re\psi(1/4+it/2)-\log\pi\),
where \(w(t)=\tfrac12\log(1+t^2)\). The finite-square pole
calculation and each delay pairing then give exactly

\[
 \begin{split}
 E_L(u)={}&\frac1{2\pi}\int_{\mathbb R}
       [\Re\psi(1/4+it/2)-\log\pi]|F_u(t)|^2dt\\
 &+2\Re\bigl(F_u(i/2)\overline{F_u(-i/2)}\bigr)
       -2\sum_{2\le n<e^L}a_n\Re C_u(\log n).
 \end{split}
 \tag{9}
\]

All integrals converge: the transforms are Schwartz on the real
axis, the symbol is logarithmically bounded by L741's integrable
\(r\) identity, and the pole kernel is bounded on each finite
square. The arithmetic sum is finite for each \(L\). A delay
\(\log n\ge L\) has zero correlation, including equality.
Thus (9) retains every contributing prime power.

For an explicit comparison with the cited geometric Weil formula,
put \(\widetilde u(x)=\overline{u(-x)}\), so
\(u*\widetilde u=C_u\). That formula is

\[
 \begin{split}
 W(C_u)={}&\int 2\cosh(v/2)C_u(v)dv
       -\sum_{n\ge2}a_n[C_u(\log n)+C_u(-\log n)]\\
 &-(\log(4\pi)+\gamma_E)C_u(0)\\
 &-\int_0^\infty\frac{k(v)}2
       [C_u(v)+C_u(-v)-2e^{-v/2}C_u(0)]dv.
 \end{split}
 \tag{10}
\]

The bracket is \(O(v)\) at zero; at infinity the correlation
is zero and the remaining term decays. To check its scalar against
(8), the archimedean energy in (8) is the limit as \(\epsilon\downarrow0\) of

\[
 \left[-c+\int_\epsilon^\infty e^{-v}\frac{dv}{v}\right]C_u(0)
        -\int_\epsilon^\infty k(v)\Re C_u(v)dv.
 \tag{11}
\]

Indeed use L741's truncated multiplier for \(B\) and then add
\(R_L\); its omitted integral on \((0,\epsilon)\) tends to zero
because \(r\in L^1\). Now

\[
 \int_\epsilon^\infty k(v)e^{-v/2}dv
  =\log\frac{1+e^{-\epsilon}}{1-e^{-\epsilon}}
  =-\log\epsilon+\log2+o(1),
\]

whereas
\(\int_\epsilon^\infty e^{-v}dv/v=-\log\epsilon-\gamma_E+o(1)\),
as established in L741's scalar normalization. The difference is
\(-\gamma_E-\log2\), proving the exact constant in (10).
The pole integral in (10) equals the pole product in (9) by
finite-support Fubini; \(C_u(-v)=\overline{C_u(v)}\) verifies
the prime coefficients. Hence

\[
 E_L(u)=W(u*\widetilde u).
 \tag{12}
\]

This supplies the requested smooth larger-window identity without
any use of a critical-axis logarithmic-derivative multiplier.
Polarization of the two Hermitian sesquilinear forms gives the
corresponding cross identity. For example, with linearity in the
first argument, the imaginary part of \(H_L(u,v)\) is
\([E_L(u+iv)-E_L(u-iv)]/4\); thus the diagonal identity determines
the complete complex pairing, not just its real part.

### 3. The finite atomic representation under RH

Suzuki's compact-smooth zero formula applied to (12), with RH now
assumed, yields

\[
 H_L(u,v)=\sum_{\gamma\in\mathcal Z}
               r_\gamma F_u(\gamma)\overline{F_v(\gamma)}.
 \tag{13}
\]

To specify the convention without relying on extracted overbars,
write \(\widehat u_+(z)=\int u(x)e^{izx}dx=F_u(-z)\).
Finite-support Fubini and a change of variable give
\[
 \widehat{u*\widetilde v}_+(z)
   =F_u(-z)\overline{F_v(-\overline z)}.
\]
Apply the source's definition (3.3),
\(W(\psi)=\sum_\gamma r_\gamma\widehat\psi_+(\gamma)\),
directly to this compact smooth convolution. Under RH all these
ordinates are real. Reindexing by \(\gamma\mapsto-\gamma\),
which preserves multiplicity, gives (13). No assertion about
\(|F|^2\) at a nonreal ordinate is made. This also specifies the
involution used in the geometric formula, independently of the
source's derivative-form notation in Proposition 3.1.

The convergence needed here is absolute, not formal. Smooth compact
support gives \(|F_u(t)|\le C_u(1+|t|)^{-2}\) for real \(t\),
by two integrations by parts. Together with the cited Hadamard
summability this bounds the absolute series in (13), and also
\(\sum_\gamma r_\gamma|F_f(\gamma)|^2\). Equivalently the
finite zero sums converge in total variation as measures after
weighting by \(|F_f|^2\). These bounds precede all phase regrouping.
We use smooth profiles throughout, so no nonsmooth approximation,
unbounded-window limit of form domains or unsmoothed spectral
measure is involved.

Taking \(u=v=f\) in the cell gives

\[
 \sum_{\gamma\in\mathcal Z}r_\gamma|F_f(\gamma)|^2=d_f>0.
 \tag{14}
\]

This proves that some atomic weight survives the two neutral
constraints. In particular no separate zero-density argument is
needed to show that the neutral transform is nonzero at a zero.
This use of the small-cell positivity does not assume the desired
unconditional global positivity. Alternatively the already cited
Suzuki Lemma 2.1 would rule out vanishing at all ordinates, but
that additional argument is not needed here.

For the translate, direct change of variable gives
\(F_{\tau_m f}(\gamma)=e^{-im\ell\gamma}F_f(\gamma)\).
Applying (13) on each encompassing finite interval proves (5).
The pole terms were included before specialization; neutrality
sets \(F_f(i/2)=F_f(-i/2)=0\), and the translate has the same
zero moments multiplied by nonzero exponential factors. Thus their
vanishing in this case is exact, not a deletion from the generator.

Definition (4) is now a well-defined finite positive Borel measure,
with mass (14). Equal lattice phases may occur for arbitrarily many
ordinates: the mass of any singleton is the convergent sum of all
its nonnegative weights. This cannot create cancellation. Since
at least one weight is positive, the resulting circle measure has
a positive atom. No independence or separation of the lattice
phases has been assumed.

### 4. Wiener and the original supremum

The finite-measure hypotheses of Cuny–Eisner–Farkas Theorem 1.1
are satisfied by (4). Its conclusion is (6) with the sum beginning
at \(m=1\). Removing that single bounded term and dividing by
\(M\) does not change the limit; in fact
\(|\widehat\mu_f(m)|\le d_f\) for every integer \(m\).
The sum of squared atom masses is finite, at most \(d_f^2\),
and strictly positive because one mass is positive. This proves (6).

The admissible choice \(g=f\) in the original supremum (3) gives
\(\beta_m\ge |h_m|/d_f\), hence the first statement of (7).
If \(\sum_m\beta_m\) were finite, then \(\beta_m\to0\),
so \(|h_m|^2\to0\) and its Cesaro means would tend to zero,
contradicting (6). This proves the second statement of (7).
No numerical approximations or mathematical scripts are used.

### 5. Separate conceptual audit, 4 November 2026, step 282

The audit reuses the assessed Suzuki and Wiener imports and L740/L741;
it does not reprove their general theorems. The primary statement of
Suzuki 2206.03682v4 (3.3), its positive Fourier convention on printed
p.9, Proposition 3.1 and the compact-test identity on printed p.11
were checked against Suzuki 2606.09096v3 Section 1.1 and Sections
2.3--2.5. In particular the latter displays both prime-power shifts
and the conjugate-reflection convention explicitly. The unambiguous
definition (3.3) and the transform computation above settle the
complex convention; no conclusion rests on a missing OCR overbar.
Cuny--Eisner--Farkas Theorem 1.1 and its finite-measure footnote were
checked in the pinned preprint. No new literature claim is made.

1. **Admissibility and a strictly positive denominator.** The
   construction \(\phi''-\phi/4\) has both zero moments by integration
   by parts. If it vanished, pairing with \(\phi\) would force
   \(\|\phi'\|_2^2+\|\phi\|_2^2/4=0\), so it is nonzero.
   For any smooth compact test \(u\), the zero extension is smooth,
   and on \([0,L]\)
   \[
    |\Phi_u'(x)|\le \|u'\|_\infty
                    \int_0^L|\log v|\,dv<\infty.
   \]
   This proves L740's actual AC and L2 conditions, including the
   value at zero, for each finite encompassing interval. Sums used
   in polarization are in the same domain. Causality and integration
   against the supported test make its diagonal independent of the
   encompassing interval. L741 therefore applies to the length-ell
   diagonal, with its original norm and its stated qualification.
   No large-window positivity or form-domain extension is used.

2. **Scalar and continuous contribution.** Substituting L740's
   \(q\) gives exactly \(q=-1/v+k-4\cosh(v/2)\); subtracting the
   damped logarithmic correction gives \(r-4\cosh(v/2)\).
   Thus (8) retains all terms. For the truncated multiplier of L741,
   its negative real pairing is
   \[
    \int_\epsilon^\infty \frac{e^{-v}}v
            [C_u(0)-\Re C_u(v)]\,dv.
   \]
   Adding \(-cC_u(0)-\Re\langle R_Lu,u\rangle\) gives (11),
   up to \(-\int_0^\epsilon r(v)\Re C_u(v)dv\), which tends
   to zero because \(r\in L^1\). The scalar difference is exactly
   \(-\gamma_E-\log2\); after \(-c\) it is
   \(-\log(4\pi)-\gamma_E\), as in the primary geometric formula.
   The bracket in (10) is integrable at zero since it is \(O(v)\)
   and \(k(v)=O(1/v)\); it decays at infinity. The Fourier symbol
   follows from L741's convergent transform of \(r\), at arguments
   with positive real part. There is no critical-axis xi'/xi limit.

3. **Pole product, both delays and complex polarization.** For
   \(C_{u,v}(s)=\int u(x+s)\overline{v(x)}dx\), finite-support
   Fubini makes the pole part of \(W(u*\widetilde v)\) equal to
   \[
    F_u(i/2)\overline{F_v(-i/2)}
      +F_u(-i/2)\overline{F_v(i/2)}.
   \]
   This reduces to (9)'s signed real product on the diagonal.
   For each \(d=\log n\), the causal contribution \(2a_nT_d\)
   to (1) is exactly
   \[
    -a_n[C_{u,v}(-d)+C_{u,v}(d)],
   \]
   since the two inner products translate opposite arguments.
   A delay \(d\ge L\) vanishes by disjoint supports, including
   equality. All remaining prime powers are present. The geometric
   kernel is real and even, so \(W(u*\widetilde v)\) is Hermitian
   and linear in \(u\). The polarization sign following (12) is
   correct for this convention. Neutrality removes the pole product
   only after these identities have been established.

4. **Spectral convergence and aliases.** The explicit transform
   computation preceding (14) yields (13) with the positive phase
   \(e^{im\ell\gamma}\) for the translated second argument.
   Two integrations by parts bound each real-axis transform by
   \(C(1+|\gamma|)^{-2}\). The product series is therefore absolutely
   summable using the cited Hadamard bound, with multiplicities.
   For \(u=v=f\) the weights are nonnegative under RH; their sum
   is \(d_f>0\) by (12)--(14). This proves finite total variation
   and a surviving atom before any lattice projection. The pushforward
   under \(\gamma\mapsto e^{i\ell\gamma}\) groups nonnegative
   weights, even for infinite alias classes. Each grouped mass is
   finite, and at least one is positive. Neither distinct phases
   nor a zero-density estimate is needed.

5. **Wiener and the actual beta_m.** The measure is finite on the
   unit circle, and its coefficient is defined with \(z^m\), exactly
   as in the imported theorem. Its mass bounds every coefficient by
   \(d_f\). Omitting \(m=1\) thus changes the average by at most
   \(d_f^2/M\). The squared-atom sum lies in \((0,d_f^2]\).
   The original supremum includes \(g=f\), so its termwise lower
   bound survives taking Cesaro averages and a liminf. Absolute
   summability of the nonnegative \(\beta_m\) would force these
   coefficients to tend to zero, contradicting the positive limit.
   If a supremum were infinite the nonsummability implication would
   already hold; no unproved finiteness assumption enters this step.

No coefficient, domain, convergence or logical failure was found.
The audit certifies the local reproduction/specialization (4)--(7),
not progress beyond the imported spectral and Wiener theory. RH is
essential to the positive circle-measure argument; no such measure
or unconditional beta_m conclusion is claimed for nonreal ordinates.
L741's cited computation is still unreplayed. No effective value of
\(s_f\), complement estimate, adjacent-block estimate or global sign
follows. The direct local mathematical inputs remain L740 and L741.

## Mathlib

Matching coverage for the complete causal/Weil identification and
this conditional neutral-cell Wiener specialization has not been
checked. No Mathlib theorem is claimed to supply the full result.
The classical Fourier and finite-measure inputs are the precise
named imports above; unknown Mathlib coverage is not evidence of
absence. The proof is an informally audited specialization, not a
formal verification or an independent replay of Zhu's computation.
