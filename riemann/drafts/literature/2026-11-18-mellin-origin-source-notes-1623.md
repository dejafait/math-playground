# Origin source extraction1623

Primary source: K. Kawano, *Logarithmic Inequalities of Arbitrary Order
for the Riemann Xi Coefficients*,
[Preprints.org202611.0383v1](https://www.preprints.org/manuscript/202611.0383/v1),
posted4November2026. Read18November2026. The site labels v1 not
peer reviewed. All displayed estimates below are **source claims**,
not verified conclusions of this notebook step.

## Exact audit specification

Use C048a's established notation and primitive, with
\(p=\sigma+i\tau\), \(r=|p|\), \(L=\log r\),
\(w=W_0(2p/\pi)=U+iV\), \(y=V/2\), \(a=\min(y,1/4)\).
For upper-half-plane points, denote the existing primitive by

\[
 O_y(p)=\sum_{n\ge0}\frac{c_n(ia)^{2p+2n}}{p+n}
             +2\int_{ia}^{iy}z^{2p-1}\Phi(z)\,dz.
\]

The source's low-horizontal split is at real coordinate one;
Lemma5.1's horizontal phase argument starts at \(x\ge1\), and
AppendixB's origin paragraph treats \(0\le x\le1\).
Accordingly the proposed component is specified as

\[
 E_o(p)=O_y(p)+2\int_0^1(x+iy)^{2p-1}\Phi(x+iy)\,dx.
\]

This defines the future audit's grouping using C048a; it is not a new
bound. At \(y=0\), set \(O_0=0\) and retain the convergent real
integral from zero to one. Reflection uses the downward formula.

Source (28) fixes, with branches continued from positive real p,

\[
 S(p)=\frac{8\pi^{5/2}e^{9w/4}}{\sqrt{p(1+w)}}
       \exp\{2p\operatorname{Log}(w/2)-2p/w\}.
\]

On \(L\ge12,\ \sigma\ge-r/(4L)\), AppendixC assigns

\[
 \frac{|E_o(p)|}{|S(p)|}
 \ \le\ 10^{19}L^{5/2}\sqrt r\,e^{-r/32}
 \ <\ 10^{-4}\frac{L^{9/2}}r.                 \tag{A: to audit}
\]

The first inequality makes explicit which component its combined
relative bound refers to; neither inequality is proved here.

## Primary cases and quantitative premises inspected

Section5.1 (26):
\(|c_n|\le10^8 4^n\), \(|c_n|\le10^{15}2^n\),
from Cauchy circles \(1/2\) and \(1/\sqrt2\).
AppendixB's full-mode estimate is
\(|\Phi(x+it)|<10^6L^3\) for \(0\le x\le1, |t|\le V/2\).
Its finite band is \(7.5\le L\le12.3\); its allowance is
\(B_o=10^{12}L^3\sqrt r e^{-r/32}\), not (A).

For that band let \(u=\underline U_8\), \(h=\overline U_8\),
\(W_*=(h^2+(\pi/2)^2)^{1/2}\), from the eight enclosing updates
printed at the start of AppendixB. Its origin formulas use

\[
 Z=\frac1{1+(\pi/4)^2}-\frac2u-\frac2{u^2},\quad
 \alpha_1=\frac\pi{12(1+1/u)},\quad
 \alpha_2=\frac\pi{4(1+1/u)}.
\]

The three horizontal loss coefficients displayed there are

\[
 \alpha_1 Z,\qquad
 1.98\alpha_2 Z-\frac{\log(W_*/(2\alpha_2))}{2L},\qquad
 1.6\log\frac{u}{2\sqrt2}-\frac{\pi/2+2}{u}.
\]

The first two vertical coefficients are

\[
 \tfrac12(\pi-\pi/u-\pi/u^2),\qquad
 .99(\pi-\pi/u-\pi/u^2)
       -\frac{3+2\log(W_*/2)}{4L}.
\]

AppendixB asserts they exceed \(1/32\) on its closed cells, using
\(|p+n|\ge|\tau|\) and the principal-power factor \(e^{-\pi\tau}\).
Those finite cell assertions are not inputs for unbounded L.

AppendixC replaces finite-band geometry by
\(U\ge3L/4, |w|\le1.01L, \cos V\ge1/L\). Its cases are:

| Case in the upper half-plane | Source's stated control |
| --- | --- |
| \(\sigma\ge0,\tau\ge r/2\) | \(y\ge0.235\); phase loss \(>r/32\) |
| \(\sigma<0\) | \(y\ge0.7,\tau\ge0.99r\); loss \(\ge r/2\) including adverse real part |
| \(\tau<r/2\) | \(\sigma\ge0.8r\); direct integration of the origin power; loss \(\ge r\) |

It uses (26) for the primitive and gives (A). For continuation of the
normalized envelope from \(L=12\), it displays the logarithmic
derivative \(3/2-2/L-e^L/32<0\). This has been read, not checked.

## Comparison and limits of the extraction

C048a proves equality and branch admissibility, with no numerical
Lambert clearance or coefficient constant. L804/audit538 establishes
a different endpoint allowance: \(s\), the shifted saddle equation,
outward height and its Gaussian denominator differ. Its standard
Taylor-subtraction method is reusable, its inequality is not.
Assessment535 supplies the already inspected Zagier/DLMF continuation
and Cauchy hypotheses. Assessment511 supplies the no-automatic-uniform-
saddle comparison and retained global-import stop. These are duplicate
safeguards, not new proof work.

A future audit must pay the complete theta sum, both Cauchy constants
actually used, the intervening vertical segment when y>1/4, the
modulus of S, negative real parts, small positive heights, zero height,
reflection and the closed boundaries. It may prove only the needed
versions of the source's auxiliary estimates, but must disclose any
correction. Moving-height analyticity is not an available premise.
Failure of an absolute majorant would not refute (A) or RH.

No essential text was inaccessible. AppendixC.1 differentiation,
the total saddle budget, finite zero certificates and inverse-density
conclusions are not imported. The archive remains unread and is not
needed for the bounded component proposed here. No new mathematics,
lemma or mathematical script was produced. Full matching Mathlib
coverage is unchecked/unknown.
