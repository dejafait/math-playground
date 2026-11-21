# Corollary 466m: explicit normalized opposed-slice error, without a density certificate

## Hypotheses

Use the actual function, density and conventions of C466a/C466k/C466l:
\(h(z)=\xi(1/2+\sqrt z)/c_0\), \(c_0=\xi(1/2)>0\),
\(p=\theta_1\), \(x=B'(1)>0\), \(S=3x\), and the opposed
slice \(K\) of C466l. In particular \(p\) is a probability density,
smooth on the real line, zero on the nonpositive half-line, positive
on the positive half-line, with Laplace transform \(1/h\) on
\(\operatorname{Re}z>0\). Retain the imported density construction,
strip, symmetry, paired-product, zero-counting and verified-low-zero
qualifications in C466a. Those external certificates are not replayed.
No RH, global PF assertion, extra verified zeros, simplicity or
independence after conditioning is assumed.

## Conclusion

Put \(R_* = \exp(\exp(256))\). Then
\[
 \left|K(r)|h(1+ir)|^2-2\pi p(S)\right|
       \le e^S |r|^{-1/16}\qquad(|r|\ge R_*).                 \tag{1}
\]
Thus, **if a numerical lower bound** \(p(S)\ge m>0\) is certified,
one may take
\[
 R(m)=\max\left\{R_*,\frac{\pi}{2S},
                    \left(\frac{e^S}{\pi m}\right)^{16}\right\} \tag{2}
\]
in the requested error bound \(\le\pi m\). No such numerical \(m\)
is obtained here. The target pair \(m,R\) is therefore incomplete.
The enormous explicit analytic threshold is not a practical compact
sign certificate; intervening frequencies, the full marginal, higher
orders and Xi transfer remain open. The development from attempt936
passed the separate step939 audit below under the inherited inputs;
C466n separately supplies the numerical density lower bound.

## Proof

### Effective expansion of the full function

Normalize the logarithm by its value at 1:
\[
 D(z)=\log h(z)-\log h(1),\qquad d(v)=\operatorname{Re}D(1+iv).
\]
The analytic branch is real on the positive axis. C466k's tilted
probability density gives
\[
 h(1)\ge1,\qquad |h(1+iv)|\ge h(1),\qquad d(v)\ge0.          \tag{3}
\]
Indeed \(1/h(1)=\int e^{-u}p(u)du\le1\), and
\(h(1)/h(1+iv)\) is a characteristic function. The nonvanishing
and conjugate symmetry used here are part of the inherited inputs.

Let \(q=\sqrt z\), principal branch, and \(w=q/2+1/4\).
For \(\operatorname{Re}z\ge0\), \(|z|\ge16\), one has
\(|q|\ge4\), \(\operatorname{Re}q\ge |q|/\sqrt2\),
\(|w|\ge |q|/2\) and \(|\arg w|\le\pi/4\).
Use C466a's exact completion formula and import the log-Gamma
remainder in [DLMF 5.11.1 and 5.11(ii)](https://dlmf.nist.gov/5.11):
\[
 \log\Gamma(w)=(w-\tfrac12)\log w-w+\tfrac12\log(2\pi)+E_\Gamma(w),
 \quad |E_\Gamma(w)|\le\frac{\sec^2(\arg(w)/2)}{12|w|}
                              \le\frac1{3|q|}.              \tag{4}
\]
This is the empty-Bernoulli-sum case inspected in review935; it is a
bound on the analytic logarithm, not a principal logarithm of a
Gamma value. The definition of Gamma by its Euler integral is used
below only at positive real arguments and for its elementary modulus
bound. The absolutely convergent zeta series and Euler logarithm
are the same inputs as in C466a and review935; see
[DLMF 25.2.1 and 25.2.6](https://dlmf.nist.gov/25.2).

Here are the remaining errors in the completion, so that (4) is not
mistaken for a bound on the whole function. Put \(u=1/(2q)\).
The convergent logarithmic power series gives
\[
 \left|(q/2-1/4)\log(1+u)-1/4\right|
 \le\frac1{8|q|}+\frac{|q|/2+1/4}{8|q|^2(1-1/8)}
 \le\frac1{4|q|},
 \quad \left|\log(1-1/(4q^2))\right|\le\frac1{3|q|^2}.
\]
For \(s=q+1/2\), \(\sigma=\operatorname{Re}s>3\), absolute
convergence of the logarithmic Euler product and an integral comparison give
\[
 |\log\zeta(s)|\le
 \sum_{n\ge2}\frac{n^{-\sigma}}{1-n^{-\sigma}}
 \le\frac{2^{-\sigma}}{1-2^{-\sigma}}
           \left(1+\frac2{\sigma-1}\right)
 <3\,2^{-\sigma}\le\frac2{|q|}.
\]
For the last inequality use \(\sigma\ge 2|q|/3+1/2\):
\(3y2^{-(2y/3+1/2)}\) decreases for \(y\ge4\), and its
value at 4 is less than \(12/8<2\). Thus the logarithms of all
completion factors give
\[
 D(z)=G(z)+C+E(z),\qquad
 G(z)=\frac{\sqrt z}{2}\left(\log\frac{\sqrt z}{2\pi}-1\right)
                              +\frac78\log z,
 \quad C=\tfrac14\log(\pi/2)-\log\xi(3/2),
 \quad |E(z)|\le\frac3{\sqrt{|z|}}.                         \tag{5}
\]
The errors just bounded sum to at most
\((1/3+1/4+1/12+2)/|q|<3/|q|\). Constants and branches in
(5) follow by expanding \(\log w=\log(q/2)+\log(1+1/(2q))\)
in C466a's exact formula. Agreement on the positive axis fixes the
analytic identity on this connected sector. In particular no
derivative of \(E\) has been taken.

The elementary bounds
\[
 \frac1{24}<\xi(3/2)<3,\qquad -2<C<4                       \tag{6}
\]
need no enclosure of \(c_0\). Indeed
\(\xi(3/2)=(3/8)\pi^{-3/4}\Gamma(3/4)\zeta(3/2)\),
\(1<\zeta(3/2)<3\), and
\(4/(3e)<\Gamma(3/4)<4/3+e^{-1}<2\). Combine these with
\(e<3\) and \(1/4<\pi^{-3/4}<1\). They imply (6), since
\(\log24+\tfrac14\log2<4\).

For \(0\le v\le16\), the exact completion also gives
\[
                         0\le d(v)\le10.                   \tag{7}
\]
In fact \(1\le\operatorname{Re}\sqrt{1+iv}<3\), so the real
Gamma argument lies in \([3/4,7/4]\). Its modulus is at most
\(\Gamma(a)\le4/3+\int_1^\infty t e^{-t}dt<3\) there;
the zeta modulus is at most \(\zeta(3/2)<3\). The polynomial
factor has modulus less than 17 and the pi factor has modulus at
most one. Dividing the bound \(17\cdot9/2\) for the completion
by \(\xi(3/2)>1/24\) gives a ratio less than 1836, whose
logarithm is less than 10. The lower bound is (3).

### Explicit real-axis remainder and the three frequency ranges

Set
\[
 \kappa=\frac1{4\sqrt2},\qquad
 \lambda=-\frac{\log(2\pi)+1+\pi/4}{2\sqrt2},\qquad
 g(v)=\kappa\sqrt v\log v+\lambda\sqrt v+\frac78\log v+C.
\]
In particular \(1/8<\kappa<1/4\) and \(|\lambda|<3/2\).
For every \(v\ge16\), (5) implies the explicit estimate
\[
 d(v)=g(v)+\rho(v),\qquad |\rho(v)|\le4\frac{\log v}{\sqrt v}.
                                                                    \tag{8}
\]
To check the change from \(1+iv\) to \(iv\), differentiate only
\(G\):
\[
 G'(z)=\frac{\log(\sqrt z/(2\pi))}{4\sqrt z}+\frac7{8z}.
\]
On \(z=a+iv\), \(0\le a\le1\), its modulus is at most
\(\log v/\sqrt v\). For example the numerator logarithm is
bounded by \(\tfrac12\log v+7/2\), and \(v\ge16\) pays the
remaining \(7/(8v)\). The segment has length one; add
\(3/\sqrt v\) from (5). The real part of \(G(iv)+C\) is
exactly \(g(v)\). This proves (8), including the adverse argument
term in \(\lambda\).

Write \(W(v)=\sqrt v\log v\), \(T=e^{256}\),
\(R_0=e^{65536}\), and \(\epsilon=2^{-10}\). For \(v\ge T\),
(6) and (8) imply
\[
 \frac9{10}\kappa W(v)\le d(v)\le\frac{11}{10}\kappa W(v). \tag{9}
\]
Indeed the relative error is at most
\(12/\log v+7/\sqrt v+32/(\sqrt v\log v)+32/v<1/10\).
The first term is less than \(1/20\), and the other three sum
to less than \(1/100\) at and beyond \(T\).

For \(r\ge R_0\), define
\[
 H_r(t)=\frac{e^{iSt}}{h(1+it)}
      \frac{|h(1+ir)|^2}{h(1+i(t+r))h(1+i(t-r))},\qquad
 J_r(t)=d(t+r)+d(t-r)+d(t)-2d(r).
\]
The function \(d\) is even, and
\(|H_r(t)|=h(1)^{-1}e^{-J_r(t)}\le e^{-J_r(t)}\).
We claim the all-frequency estimates
\[
 |H_r(t)|\le e^2\ (|t|\le T),\qquad
 |H_r(t)|\le e\exp[-W(|t|)/4096]\ (|t|\ge T).              \tag{10}
\]
Here and below the ranges meet without omitting \(t=\pm r\).

For \(0\le t\le r/2\), direct differentiation of \(g\) gives
\[
 g''(v)=-\frac{\kappa\log v+\lambda}{4v^{3/2}}-\frac7{8v^2}.
\]
On \([r/2,3r/2]\) its modulus is at most
\(2\log r/r^{3/2}\). The triangular-kernel second-difference
formula, with mass \(t^2\), and the value bound (8) give
\[
 d(r+t)+d(r-t)-2d(r)
 \ge-\frac{2t^2\log r}{r^{3/2}}-\frac{24\log r}{\sqrt r}. \tag{11}
\]
For completeness the error sum is at most
\([8\sqrt2(\log r+1)+8\log r]/\sqrt r\le24\log r/\sqrt r\).
This last quantity is at most one on \(r\ge R_0\).

If \(T\le t\le\epsilon r\), the elementary decreasing function
\(y^{-3/2}(1+\log y)\), \(y\ge1\), gives
\[
 \frac{2t^2\log r}{r^{3/2}}
 \le2\epsilon^{3/2}(1+\log(1/\epsilon))W(t)
 \le\frac\kappa4 W(t).
\]
The coefficient on the middle expression is less than \(1/2048\),
whereas \(\kappa/4>1/32\). Equations (9)-(11) give
\(J_r(t)\ge\kappa W(t)/4-1\), sufficient for (10).
If \(0\le t\le T\), (3) and (11) give \(J_r(t)\ge-2\):
\(2T^2\log r/r^{3/2}\le1\) on \(r\ge R_0\). Also
\(T\le\epsilon R_0\), so these ranges cover the small part.

For the comparable range, uniformly in \(0\le a\le3\),
\[
 |d(ar)-\kappa\sqrt r\log r\sqrt a|
                      \le4\sqrt r+3\log r+20.              \tag{12}
\]
If \(ar\ge16\), use \(|\sqrt a\log a|\le2\),
\(|\lambda|<3/2\), and
\(|d(v)-\kappa W(v)|\le(3/2)\sqrt v+2\log v+4\)
from (8). Their sum is at most
\((7/2)\sqrt r+2\log r+7\). If \(ar<16\), (7) gives
the bound \(10+\log r\). This proves (12), including \(a=0\).

For \(s=t/r\in[\epsilon,2]\), put
\(f(s)=\sqrt{1+s}+\sqrt{|1-s|}+\sqrt s-2\).
It satisfies \(f(s)\ge1/64\) on this interval. On
\([\epsilon,1]\) it is concave and hence bounded below by its
endpoint values; \(f(\epsilon)\ge\sqrt\epsilon-\epsilon
=31/1024\), while \(f(1)=\sqrt2-1\). On \([1,2]\)
it is increasing. By (12), the error in
\(J_r(t)/(\kappa\sqrt r\log r)\) relative to \(f(s)\) is
at most
\[
 \frac{160}{\log r}+\frac{120}{\sqrt r}
           +\frac{800}{\sqrt r\log r}\le\frac1{128}
                                  \qquad(r\ge R_0).
\]
For instance the first term is less than \(1/256\), and the
remaining terms sum to less than \(1/256\). Thus
\(J_r(t)\ge\kappa\sqrt r\log r/128\). Since
\(W(t)\le2\sqrt2\sqrt r\log r\) here, this gives
\(J_r(t)\ge W(t)/2048\). This includes \(t=r\), using
the compact bound rather than a large-argument expansion at zero.

Finally, when \(t\ge2r\), (3) and (9) imply
\[
 J_r(t)\ge\kappa\left(\frac95-\frac{11}{5\sqrt2}\right)W(t)
                                      \ge W(t)/4096.
\]
Here \(d(t-r)\ge0\), \(W(t+r)\ge W(t)\), and
\(W(r)\le W(t)/\sqrt2\). The parenthesized coefficient
exceeds \(1/5\), since \(8\sqrt2>11\). Evenness completes
(10). Notice also, directly from (3) and (9),
\[
 |h(1+it)|^{-1}\le1\quad(t\in\mathbb R),\qquad
 |h(1+it)|^{-1}\le e^{-W(|t|)/4096}\quad(|t|\ge T).        \tag{13}
\]

### A uniform integrated error with no unspecified constants

Let \(r\ge R_*\), \(L=\log r\ge e^{256}\), and \(A=L^2\).
In particular \(A\ge T\), \(A\le r/2\), and \(r\ge R_0\).
For \(|t|\le A\), compare the two logarithm differences in the
ratio defining \(H_r\), using (5). On the relevant vertical
segments, \(|G'|\le2L/\sqrt r\); this follows from its explicit
formula and \(r/2\le|z|\le2r\). Each difference of two remainder
values has modulus at most \(6\sqrt2/\sqrt r\le9/\sqrt r\).
Consequently the ratio is \(e^{\Delta_r(t)}\), with
\[
 |\Delta_r(t)|\le\frac{4AL+18}{\sqrt r}
                         \le\frac{5L^3}{\sqrt r}\le1.
\]
Conjugate symmetry identifies its numerator with
\(h(1+ir)h(1-ir)\), so no modulus replaces either denominator's
phase. Since \(|e^z-1|\le2|z|\) for \(|z|\le1\), (13) gives
\[
 \int_{-A}^{A}\left|H_r(t)-\frac{e^{iSt}}{h(1+it)}\right|dt
                       \le20L^5 e^{-L/2}.                  \tag{14}
\]
For \(|t|\ge A\), \(\log|t|\ge2\log L\ge512\), so
\(W(|t|)/4096\ge\sqrt{|t|}/8\). Equations (10) and (13),
and \(e+1<4\), yield
\[
 \int_{|t|>A}\left|H_r(t)-\frac{e^{iSt}}{h(1+it)}\right|dt
 \le8\int_A^\infty e^{-\sqrt t/8}dt
 =128(L+8)e^{-L/8}.                                       \tag{15}
\]
For every \(L\ge1024\),
\(40L^5\le e^{7L/16}\) and
\(256(L+8)\le e^{L/16}\). One may check their logarithms
at 1024 using \(\log2<1\); the differences then increase,
with derivatives \(7/16-5/L>0\) and \(1/16-1/(L+8)>0\).
Thus the sum of (14)-(15) is at most \(e^{-L/16}\).
All estimates hold for every \(r\) above the stated threshold,
not just along a sampled sequence.

C466l(11) and C466k(7) at \(y=S\) give exactly
\[
 K(r)|h(1+ir)|^2=e^S\int H_r(t)dt,\qquad
 2\pi p(S)=e^S\int\frac{e^{iSt}}{h(1+it)}dt.
\]
Absolute convergence is covered by the preceding bounds. Their
difference proves (1) for positive \(r\); evenness gives negative
\(r\). Equation (2) is then immediate, but it is conditional on
the as-yet-uncertified numerical lower bound for \(p(S)\).

The cited Stirling and Dirichlet-series estimates are imported known
mathematics. The local contribution is their explicit assembly for
this three-factor integral, including moving zero-frequency arguments.
Review935 did not identify a full matching theorem; that bounded
comparison is not an originality certification. No numerical density
inversion or certificate for the target pair was asserted in attempt936;
the subsequent critical audit is recorded below.

The supporting exact scalar checks can be reproduced with
`python3 scripts/reciprocal-tail/effective_tail_936.py`. All 14 rational
inequalities passed; the full record is
`scripts/reciprocal-tail/effective-tail-936.json`. It checks the
displayed scalar thresholds, including the comparable-range error
against 1/128 and the two integrated-error budgets. It does not verify
the analytic implications, external density inputs, or p(S), and is
not a certificate for the requested m,R pair. The proof of the
all-frequency statement remains the argument above.

### Critical audit, 14 November 2026, step939

The stated all-frequency conclusion passes under its exact hypotheses.
This verifies an existing local partial result; it supplies no stronger
onset or new result beyond the proof being audited. Source coverage is
reused from nomination937/approval938 and review935, including the
empty-sum log-Gamma remainder case. The density construction and its
external zero/counting certificates remain qualified imports.

In (5), the completion constant is
\(\tfrac14\log(\pi/2)-\log\xi(3/2)\): normalization divides
by \(\xi(3/2)\), not by \(c_0\). The \(7/8\) coefficient and
the negative argument term in \(\lambda\) agree with the full
completion. The four error coefficients sum to \(8/3<3\).
All logarithms used in comparing nearby values are analytic branches
fixed on the positive axis. The compact estimate (7) uses the full
Gamma and zeta factors; (3) uses only the given positive Laplace law.
Thus neither bound assumes RH or a monotone modulus.

The horizontal segment in (8) stays at modulus at least v. Its
explicit-part derivative is bounded by \(\log v/\sqrt v\);
\(\log v\ge\log16>8/3\) pays the additional
\(3/\sqrt v\). No derivative of the remainder is used.
For (11), the triangular kernel has mass \(t^2\). On
\([r/2,3r/2]\), the bound for \(g''\) and the three value
errors give exactly the two stated deficits. Their decrease beyond
\(\log r=65536\) pays both compact-small-frequency estimates.

In (12), \(|\sqrt a\log a|\le2\) for \(0\le a\le3\),
with its continuous value at zero. For ar<16 the separate bound
\(10+\log r\) applies, so no large-argument formula is evaluated
at zero. The four terms in J have total absolute coefficient five;
dividing their errors by \(\kappa\sqrt r\log r\), using
\(\kappa>1/8\), gives precisely the displayed
\(160/\log r+120/\sqrt r+800/(\sqrt r\log r)\).
It is below 1/128, while the concavity/monotonicity argument gives
\(f\ge1/64\). The conversion to W(t)/2048 uses the exact
\(\kappa=1/(4\sqrt2)\). The far-range coefficient exceeds 1/5
because \(121<128\). Together these bounds cover every t,
including the moving t=+/-r neighborhoods.

For (14), the two complex logarithm differences retain the denominator
phases and have combined error at most \(5L^3/\sqrt r\).
The interval length 2A and \(|e^z-1|\le2|z|\) produce
\(20L^5e^{-L/2}\). At A=L^2, the two-sided tail from (10),(13)
is \(128(L+8)e^{-L/8}\); its substitution and factor eight
were checked. The two logarithmic inequalities at L=1024, followed
by their positive derivatives, bound each contribution by half of
\(e^{-L/16}\). Finally \(L\ge e^{256}\) ensures all earlier
thresholds and \(A\le r/2\) simultaneously. C466l(11) and
C466k(7) supply the same factor e^S, with no missing h(1) or c0.
Evenness covers negative r.

All 14 scalar checks in `scripts/reciprocal-tail/effective-tail-936.json` were rerun exactly;
their full bounds and justifications were inspected alongside these
analytic implications. They are supporting arithmetic, not a substitute
for the argument. C466n's step939 audit supplies the remaining m and
checks its use in (2); the entire compact middle and Xi transfer remain
unpaid. The direct local inputs in the existing DAG row are unchanged.

## Mathlib

Full matching coverage is unchecked. Supporting logarithmic-series,
Gamma, zeta, integration and real-calculus facts are not a formalization
of (1). No declaration-name or absence claim is made; unknown coverage
does not establish absence.
