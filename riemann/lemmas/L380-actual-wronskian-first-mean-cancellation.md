# Lemma 380: cancellation in the actual Wronskian first mean

## Hypotheses

Use the actual pair F_0,G and positive envelope A of L366, with
ordinary real derivatives and no positive regulator. For t>0 put
T=1+t, L=log(2+t) and

\[
 \mathcal W(t)=\frac{F_0'(t)G(t)-F_0(t)G'(t)}{A(t)^2T^2L},
 \qquad M_H=\frac1H\int_H^{2H}\mathcal W(t)\,dt.
\]

There is no RH, simplicity, independence, noncoincidence or discriminant
sign assumption. All asymptotic constants are uniform as H tends to
infinity for this fixed pair. The Wronskian convention here is the
negative of L370's convention.

## Conclusion

In L369's carrier notation, let

\[
 \mu_j=\sum_{n\ge1}\frac{(\log n)^j}{n^3}\quad(j=0,1),
 \qquad \mu_0=\zeta(3),\qquad \omega=\phi'.
\]

Define the exact diagonal term

\[
 D_H=\frac1{\pi H}\int_H^{2H}
       \frac{t}{T^2L}\left(\mu_0\omega+\frac{\mu_0}{2}-\mu_1\right)dt.
 \tag{1}
\]

Then

\[
 M_H=D_H+O\big(H^{-1/2}(\log H)^2\big),\qquad
 D_H=\frac{\zeta(3)\log2}{2\pi H}
                 +O\big((H\log H)^{-1}\big).
 \tag{2}
\]

In particular M_H tends to zero, with
\(M_H=O(H^{-1/2}(\log H)^2)\). The positive diagonal is smaller
than the available error envelope: their orders have ratio
\(H^{1/2}(\log H)^2\), tending to infinity. Thus (2) gives no sign
of M_H. This comparison concerns the proved error bound, not a lower
bound for the actual error. It stops this first-mean signing certificate;
it does not rule out sharper estimates, assert Wronskian vanishing,
or exclude noncommon zeros. No actual-theta positivity, zero-exclusion
range or RH conclusion follows. The separate critical audit below validates
these statements without strengthening the error or sign conclusion.

## Proof

This is a REPRODUCTION under the unchanged prior SPECIALIZE assessment
`drafts/literature/2026-10-08-actual-wronskian-first-mean.md`.
We specialize L369 (16), rather than reprove its scalar approximation
or mixed-mean theorem. No originality beyond the sources checked is
claimed. The necessary new calculation is the exact Wronskian algebra
and its weights, since L369 computes a different bilinear expression.

### Exact carrier cancellation, including zeros

Set, exactly as in L369 (4)–(6),

\[
 s=\tfrac14+it/2,\quad p=t^2+\tfrac14,\quad
 Q=p\Gamma(s)\pi^{-s}=Ae^{i\phi},\quad
 U=\zeta(1/2+it),\quad Z=\zeta(5/2+it),
\]
\[
 b=\frac{t^2/4-3/16-it/2}{\pi},\quad V=bZ,
 \quad r=e^{i\phi}U\in\mathbb R,\quad h=e^{i\phi}V.
 \tag{3}
\]

The smooth phase exists because Q is nonzero. L366 and L368 (3) give
F_0=−Ar and G=A Re h. L369 (5)/(9), by exact critical-line
reflection, gives

\[
 e^{2i\phi}U=\overline U,\qquad
 e^{2i\phi}U'=\overline U'-2i\omega\overline U,
 \quad \omega=\tfrac12\log(t/(2\pi))+O(t^{-2}),
 \quad \omega'=O(t^{-1}).
 \tag{4}
\]

The primes on the conjugates denote their real derivatives. These
identities hold at zeros of U; no division by U is involved. Carrier
bounds follow from the exact digamma/polygamma formulas in L369 (6),
so no asymptotic remainder is differentiated here.

For any common differentiable positive envelope, direct multiplication
shows

\[
 (Af)'(Ag)-(Af)(Ag)'=A^2(f'g-fg').
\]

Taking f=−r and g=Re h, and using that r and r' are real, gives

\[
 \frac{F_0'G-F_0G'}{A^2}
   =\operatorname{Re}(rh'-r'h)
   =\operatorname{Re}\{e^{2i\phi}(UV'-U'V)\}.
\]

The i omega contributions in r h' and r' h cancel exactly. Substitution
of (4), followed by V=bZ and V'=b'Z+bZ', yields the zero-safe identity

\[
 \mathcal W=
 \operatorname{Re}\frac{
  b(\overline U Z'-\overline U'Z+2i\omega\overline U Z)
                  +b'\overline U Z}{T^2L}.
 \tag{5}
\]

In particular reflection restores the displayed 2i omega term; simply
dropping all carrier terms would be incorrect. The complete complex
polynomial b and its derivative remain. The common A' cancels exactly;
the envelope curvature involves second derivatives and does not enter
this first-jet identity. No product of real parts was replaced by an
unsupported modulus square or assigned a factor one half.

### Applicability of the existing weighted mean

Write d=T^2L and define the complex weights

\[
 \alpha=b/d,\qquad \beta=2i\omega b/d,\qquad \gamma=b'/d.
 \tag{6}
\]

On [H,2H], b=O(H²), b'=O(H), b''=1/(2π), omega=O(log H),
omega'=O(1/H). Also T'=1, L'=1/(t+2), so

\[
 \frac{d'}d=\frac2T+\frac1{(t+2)L},\qquad
 \alpha'=b'/d-\alpha d'/d,
\]
\[
 \beta'=2i(\omega'\alpha+\omega\alpha'),\qquad
 \gamma'=b''/d-\gamma d'/d.
 \tag{7}
\]

Consequently, uniformly on the interval,

\[
 |\alpha|=O((\log H)^{-1}),\quad
 |\alpha'|=O((H\log H)^{-1}),\qquad
 |\beta|=O(1),\quad |\beta'|=O(H^{-1}),
\]
\[
 |\gamma|=O((H\log H)^{-1}),\quad
 |\gamma'|=O((H^2\log H)^{-1}).
 \tag{8}
\]

Thus each has a uniformly bounded
\(\sup|w|+\int_H^{2H}|w'|\), as required by L369 (15).
These are bounds on the complex derivatives. They include variation
of T and L, and all terms of b. The sharper bounds for alpha and
gamma do not reduce the O(1) variation bound needed for beta.

Import L369 (16) for derivative total order at most two:

\[
 \langle w\overline U^{(a)}Z^{(c)}\rangle_H
   =i^a(-i)^c\mu_{a+c}\langle w\rangle_H
            +O(C_w H^{-1/2}(\log H)^2).
 \tag{9}
\]

Only (a,c)=(0,0),(0,1),(1,0) are used. Its proof retains the fixed
x=3H truncation, analytic Cauchy jet bounds, pole correction, the full
infinite right-line sum, all n=m collisions including n=m=1, and every
off-diagonal range. Its primary scalar input is J. Arias de Reyna,
*On the approximation of the zeta function by Dirichlet polynomials*,
arXiv:2406.16667v1, [Theorem 6 and proof, pp. 5–6](https://arxiv.org/pdf/2406.16667v1#page=5).
The hypotheses x>0, sigma≥0, 0<Im s≤x hold on L369's fixed-cutoff
Cauchy disks. The right-line series is
[DLMF 25.2.1](https://dlmf.nist.gov/25.2#E1) on Re s=5/2>1.
Carrier derivatives use [DLMF 5.11.2](https://dlmf.nist.gov/5.11#E2),
the sector/remainder qualifications of
[5.11(ii)](https://dlmf.nist.gov/5.11#ii), and
[5.15.8](https://dlmf.nist.gov/5.15#E8), at 1/4+it/2 in a fixed
sector away from the negative real axis. These citations are reused
through the proved local input; they are not Wronskian theorems.

Apply (9) separately to the four terms in (5). The constants for
bar U Z', bar U' Z and bar U Z are −i mu_1, i mu_1 and mu_0.
The uniform variation bounds (8) therefore give

\[
 M_H=\operatorname{Re}\left\langle
   \frac{-2i\mu_1 b+2i\mu_0\omega b+\mu_0 b'}{T^2L}
                              \right\rangle_H
             +O(H^{-1/2}(\log H)^2).
 \tag{10}
\]

This accounts for every projection/carrier term before averaging.
Using Im b=−t/(2π) and Re b'=t/(2π), its real diagonal numerator is

\[
 2\mu_1\operatorname{Im}b
       -2\mu_0\omega\operatorname{Im}b+\mu_0\operatorname{Re}b'
       =\frac t\pi(\mu_0\omega+\mu_0/2-\mu_1).
\]

This proves (1) and the first part of (2). In particular the nominal
t² carrier contribution has purely imaginary diagonal and contributes
zero to its real part. The smaller imaginary part of b and the real
part of b' supply the remaining diagonal.

### Scale comparison and stopping test

Uniformly for t in [H,2H], (4) implies

\[
 \frac\omega L=\frac12+O((\log H)^{-1}),\qquad
 \frac{t}{(1+t)^2}=\frac1t+O(t^{-2}).
\]

The integrand in (1), including its factor 1/pi, is consequently
\(\mu_0/(2\pi t)+O(1/(t\log H)+t^{-2})\).
Integration and division by H give the second part of (2), since
\(\int_H^{2H}dt/t=\log2\). In particular D_H is eventually positive.
Combining the two bounds proves the asserted vanishing mean.

The required sign test was a main term separated from its proved
error. Its achieved diagonal is of order 1/H; its available error
envelope is of order H^{-1/2}(log H)². Hence that test fails. We do
not rescale M_H by H and claim a limit: (10)'s rescaled error grows.
The proven vanishing mean is weaker cancellation information and
does not establish either sign of W, independence, disjointness or a
noncommon witness. Even both signs alone would leave the common-only
reset obstruction recorded in L373. Higher moments or localizations
are not proved here and require their own coverage. ∎

### Separate critical audit, 2026-10-08

The audit uses the prior SPECIALIZE coverage in
`drafts/literature/2026-10-08-wronskian-first-mean-audit.md`.
It validates (1)–(10) and the limited conclusion with the cited local
inputs. No repair to the mathematical argument is required.

L366 (1) and L368 (3) give F_0=−Ar and G=A Re h with the same
positive A and no extra factor two. Thus f'g−fg'=−r'Re h+r Re h',
with the opposite sign to L370's W. Differentiating
e^(2iφ)U=bar U gives e^(2iφ)U'=bar U'−2iω bar U at every point,
including U=0. This verifies both the minus sign on bar U'Z and the
plus sign on 2iω bar UZ in (5). No division by F_0, G, U or Z is
needed; common zeros do not invalidate the identity.

Exactly b'=t/(2π)−i/(2π), b''=1/(2π),
ω=(Re Ψ(s)−log π)/2 and ω'=−Im Ψ'(s)/4. The separately controlled
carrier estimates in L369 therefore justify (7) without differentiating
an O term. Equation (8) bounds sup|w|+∫|w'| by O(1/log H), O(1)
and O(1/(H log H)) for α, β and γ respectively. Each complex C¹
weight, including −α, satisfies L369 (15) uniformly in H. The derivative
of T²L has both terms in (7), and all of b and b' are retained.

The four applications of L369 (16) are α bar UZ', −α bar U'Z,
β bar UZ and γ bar UZ, whose diagonal integrands are respectively
−iμ_1α, −iμ_1α, μ_0β and μ_0γ. Only orders (0,1), (1,0) and
(0,0) occur. The full finite-by-infinite sum has zero frequency exactly
at n=m. At n=m=1 the derivative terms vanish and the last two terms
remain. L369 (12)–(18) retains the analytic fixed-cutoff and pole errors,
omitted diagonal tail, and all three off-diagonal ranges. Its complex
weight hypothesis is precisely the one verified here. Summing its four
error bounds proves (10), with no stronger oscillatory estimate assumed.

Taking real parts uses Re(−2iμ_1b)=2μ_1 Im b and
Re(2iμ_0ωb)=−2μ_0ω Im b. The real quadratic part of b contributes
zero. Its imaginary part −t/(2π) and Re b'=t/(2π) give exactly (1).
Then ω/L=1/2+O(1/log H) and the dyadic integral of 1/t give the
positive coefficient ζ(3)log 2/(2π) in (2).

The bound for M_H−D_H tends to zero but is larger in scale than D_H.
It is neither a signed lower bound for M_H nor an actual-error lower
bound; multiplying by H does not produce a limiting positive mean.
This validates the stopped certificate, not a prohibition on sharper
first moments. L373 is obstruction context only, not an input to these
identities or estimates. Independence, higher moments, common-free
localization, discriminant sign and actual-theta positivity remain open
in this argument. This audit verifies an existing specialization; it
establishes no new moment theorem.

## Mathlib

Full matching coverage of the actual-pair Wronskian mean and its
moving-weight specialization is **not checked**. No absence claim is
made. Formal differentiation or integration identities alone would
not supply the analytic weighted mean or a noncommon-zero witness.
