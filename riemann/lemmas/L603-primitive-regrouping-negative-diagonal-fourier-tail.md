# Lemma 603: primitive regrouping and a negative full diagonal Fourier tail

## Hypotheses

For n>=1 and u>=0 use the actual half-axis modes of L019,

\[
 q_n(u)=(8\pi^2n^4e^{9u/2}-12\pi n^2e^{5u/2})
              e^{-\pi n^2e^{2u}},\qquad k_n(u)=q_n(|u|)\quad(u\in\mathbb R),
 \qquad k(u)=\sum_{n\ge1}k_n(u).
\]

Thus k is the reflected actual theta kernel. Define ordered pair terms,
the full first associated kernel, and the Fourier convention by

\[
 B_{nm}(t)=\int_{\mathbb R}s^2 k_n(s+t)k_m(s-t)\,ds,\qquad
 A(t)=\int_{\mathbb R}s^2 k(s+t)k(s-t)\,ds,\qquad
 \widehat H(\xi)=\int_{\mathbb R}H(t)e^{i\xi t}\,dt.
\]

Let \(\mathcal P=\{(a,b):1\le a\le b,\ \gcd(a,b)=1\}\). The proposed
primitive families retain their multiplicities as follows:

\[
 P_{11}(t)=\sum_{d\ge1}B_{dd}(t),\qquad
 P_{ab}(t)=\sum_{d\ge1}[B_{da,db}(t)+B_{db,da}(t)]\quad(a<b).
\]

There are no other diagonal members of \(\mathcal P\). No spectral
positivity hypothesis is imposed on any family.

## Conclusion

These definitions give nonnegative continuous even integrable functions,
and the following equalities are legitimate:

\[
 A=\sum_{n,m\ge1}B_{nm}=\sum_{(a,b)\in\mathcal P}P_{ab},\qquad
 \widehat A(\xi)=\sum_{(a,b)\in\mathcal P}\widehat P_{ab}(\xi).
 \tag{1}
\]

The spatial sums converge pointwise and in L1; the Fourier sums converge
absolutely and uniformly in real \(\xi\). Put

\[
 d_n=q_n'(0)=-2v_n(8v_n^2-30v_n+15)e^{-v_n},\qquad v_n=\pi n^2,
 \qquad S=\sum_{n\ge1}d_n^2.
\]

Then \(0<S<\infty\), and for a finite explicitly defined constant
\(C\ge0\) in (9), every \(x\ge1\) satisfies

\[
 \left|\widehat P_{11}(2x)+2Sx^{-6}\right|\le Cx^{-8}.
 \tag{2}
\]

In particular, with \(X_0=\max\{1,\sqrt{C/S}\}\),

\[
 \widehat P_{11}(2x)\le -Sx^{-6}<0\qquad(x\ge X_0).
 \tag{3}
\]

The full diagonal family is therefore not positive definite. Separate
positive definiteness of every complete primitive family cannot establish
the first Xi sign. This does not decide the total first sign: by L233,
\(\widehat A(2x)=\Xi'(x)^2-\Xi(x)\Xi''(x)\). Inter-family compensation,
all-frequency total signs, and higher-degree signs remain unresolved.

## Proof

### Summability and primitive regrouping

Use L356's half-axis derivative envelope, its equation (1): for every
integer r>=0 there is a finite constant \(M_r\) such that

\[
 \sum_{n\ge1}|q_n^{(r)}(u)|\le
 M_r e^{u/2}e^{-\pi e^{2u}/2}\qquad(u\ge0).
 \tag{4}
\]

In particular the sum of the boundary derivatives is absolutely
convergent, and for every integer j>=0,
\(\sum_n\int_0^\infty u^j|q_n^{(r)}(u)|du<\infty\).
The latter follows by integrating (4), since its right side times any
polynomial in u is integrable. Termwise differentiation on compact
half-axis intervals is part of the same envelope argument. Each mode
is positive on the half-axis by L019, so \(0\le k_n\le k\), and k has
all absolute moments and bounds \(k(u)\le C_Be^{-B|u|}\) for every B>0.

More explicitly, the polynomial recurrence in L356 gives, separately
for every n and r,
\(|q_n^{(r)}(u)|\le C_r e^{u/2}e^{-\pi n^2e^{2u}/2}\).
On 0<=u<=R this is at most
\(C_r e^{R/2}e^{-\pi n^2/2}\). This summable bound justifies local
uniform differentiation at every fixed order, including the one-sided
boundary values. On the unbounded half-axis, substituting y=e^(2u)
in the weighted envelope reduces its integral to a constant times
\(\int_1^\infty (\log y)^j y^{-3/4}e^{-\pi y/2}dy<\infty\).
It also gives the vanishing polynomial-weighted boundary terms used
below. Orders through six suffice for this proof; no uniformity in
the derivative order is asserted or needed.

All exchanges below invoke Tonelli for nonnegative functions or Fubini
after the displayed absolute-integrability bounds. The precise standard
input is Durrett, *Probability: Theory and Examples*, author version 5,
11 January 2019, [Theorem 1.7.2 and proof, pp.38–40; counting-measure
corollary, p.41](https://math.duke.edu/~rtd/PTE/PTE5_011119.pdf).
Counting measure on the countable index sets and Lebesgue measure are
sigma-finite. Complex Fourier factors are handled by applying the
integrable version to real and imaginary parts. These standard measure
theorems are imported, not reproved.

For each fixed t, Tonelli expands A into the nonnegative \(B_{nm}\).
Every ordered positive pair (n,m) has the unique multiplier
\(d=\gcd(n,m)\) and the unordered primitive pair
\((a,b)=(\min(n,m)/d,\max(n,m)/d)\). If a<b, the two ordered
orientations are distinct and both occur; if a=b then a=b=1 and only
(d,d) occurs. This proves the pointwise regrouping in (1).

The change of variables \(u=s+t,v=s-t\), whose absolute Jacobian is
1/2, gives for every integer j>=0

\[
 \sum_{n,m}\int_{\mathbb R}|t|^j B_{nm}(t)\,dt
 =2^{-j-3}\int_{\mathbb R^2}|u-v|^j(u+v)^2 k(u)k(v)\,du\,dv
 <\infty.
 \tag{5}
\]

The finiteness uses only polynomial moments of k. In particular the
sum of all pair L1 norms equals \(\|A\|_1<\infty\). Every subfamily
has finite mass, the regrouping converges in L1, and
\(\sum_{(a,b)}|\widehat P_{ab}(\xi)|\le\sum_{(a,b)}\|P_{ab}\|_1\)
uniformly in real \(\xi\). Thus the Fourier regrouping in (1) is also
absolutely and uniformly convergent. The same argument applies to
\(\widehat P_{11}=\sum_n\widehat B_{nn}\).

For clarity, continuity is not inferred just from L1 convergence. On
every compact interval of arguments the mode series converges uniformly:
the polynomial bound used in L356 gives
\(|q_n(u)|\le C_R e^{-\pi n^2/2}\) for 0<=u<=R. Hence every selected
double subseries \(\sum k_n(u)k_m(v)\) is locally uniformly convergent
and continuous. For |t|<=R its defining s-integrand is dominated by

\[
 s^2 k(s+t)k(s-t)\le C_B^2 s^2e^{-2B|s|},
\]

an integrable function independent of t. Dominated convergence proves
continuity of each family and of A. Replacing s by -s shows
\(B_{nm}(t)=B_{mn}(t)\); replacing t by -t shows
\(B_{nm}(-t)=B_{mn}(t)\). Thus every ordered pair term and every
family is even. These identities do not remove either ordered
orientation from an off-diagonal family's definition.

### Uniformly summable Fourier remainders

Write \(F_n(x)=\widehat k_n(x)=2\int_0^\infty q_n(u)\cos(xu)du\).
The moment bounds justify differentiating this original integral twice:

\[
 F_n'=-2\int_0^\infty u q_n(u)\sin(xu)du,\qquad
 F_n''=-2\int_0^\infty u^2 q_n(u)\cos(xu)du.
 \tag{6}
\]

We do not differentiate an asymptotic remainder. For a smooth half-axis
function h with all the derivatives and decay used here, put
\(C_x(h)=\int_0^\infty h(u)\cos(xu)du\) and
\(T_x(h)=\int_0^\infty h(u)\sin(xu)du\). Integration by parts yields

\[
 C_x(h)=-\frac{h'(0)}{x^2}+\frac{h'''(0)}{x^4}
                      +x^{-4}C_x(h^{(4)}),
\]
\[
 T_x(h)=\frac{h(0)}x-\frac{h''(0)}{x^3}
              +x^{-5}[h^{(4)}(0)+C_x(h^{(5)})],
\]
\[
 C_x(h)=-\frac{h'(0)}{x^2}+\frac{h'''(0)}{x^4}
              -x^{-6}[h^{(5)}(0)+C_x(h^{(6)})].
 \tag{7}
\]

Every boundary term at infinity vanishes by (4) and the analogous
polynomial-weighted bounds. These formulas also follow successively
from \(C_x(h)=-x^{-1}T_x(h')\) and
\(T_x(h)=x^{-1}h(0)+x^{-1}C_x(h')\), so their signs retain the
reflected half-axis boundary contribution.

Define nonnegative constants, with L1 norms on [0,infinity),

\[
 a_n=2\bigl(|q_n'''(0)|+\|q_n^{(4)}\|_1\bigr),
\]
\[
 b_n=2\bigl(|(u q_n)^{(4)}(0)|+\|(u q_n)^{(5)}\|_1\bigr),\qquad
 c_n=2\bigl(|(u^2q_n)^{(5)}(0)|+\|(u^2q_n)^{(6)}\|_1\bigr).
\]

All three sequences are in l1. Indeed the boundary terms in b_n and
c_n are respectively \(4q_n'''(0)\) and \(20q_n'''(0)\). The product
rule gives
\((u q_n)^{(5)}=u q_n^{(5)}+5q_n^{(4)}\) and
\((u^2q_n)^{(6)}=u^2q_n^{(6)}+12u q_n^{(5)}+30q_n^{(4)}\).
Thus (4) and its weighted integral consequences bound the sum of each
norm and each boundary absolute value. Also \(\sum_n|d_n|<\infty\)
by (4) at r=1 and u=0.

Apply the first formula in (7) to q_n, the second to u q_n, and the
third to u^2q_n in (6). Their boundary data include
\((u q_n)(0)=0\), \((u q_n)''(0)=2d_n\),
\((u^2q_n)'(0)=0\), and \((u^2q_n)'''(0)=6d_n\). Consequently,
simultaneously for every n and x>=1,

\[
 F_n=-2d_n x^{-2}+r_{0n},\quad
 F_n'=4d_n x^{-3}+r_{1n},\quad
 F_n''=-12d_n x^{-4}+r_{2n},
\]
\[
 |r_{0n}|\le a_nx^{-4},\qquad
 |r_{1n}|\le b_nx^{-5},\qquad
 |r_{2n}|\le c_nx^{-6}.
 \tag{8}
\]

This is a uniform summability statement for the actual infinite family,
not a passage from an uncontrolled finite-truncation error term.

### The full diagonal sign

Each k_n is real, continuous, even and faster than exponentially
decaying. L233 therefore applies individually and gives
\(\widehat B_{nn}(2x)=[F_n'^2-F_nF_n'']/4\). From (8),

\[
 \widehat B_{nn}(2x)=-2d_n^2x^{-6}+R_n(x),
\]

where, for x>=1,

\[
 |R_n(x)|\le\frac14\left[
 |d_n|(8b_n+2c_n+12a_n)x^{-8}
 +(b_n^2+a_nc_n)x^{-10}\right].
\]

For example the exact numerator error is
\(8d_nx^{-3}r_{1n}+r_{1n}^2+2d_nx^{-2}r_{2n}
 +12d_nx^{-4}r_{0n}-r_{0n}r_{2n}\); the leading coefficient is
\((16-24)d_n^2/4=-2d_n^2\). Define

\[
 C=\frac14\sum_{n\ge1}
 \left[|d_n|(8b_n+2c_n+12a_n)+b_n^2+a_nc_n\right]<\infty.
 \tag{9}
\]

Finiteness follows from the l1 bounds: products of two nonnegative l1
sequences have finite sum, since either factor is bounded by its l1
norm. The same argument gives \(S=\sum d_n^2<\infty\).
For an explicit audit of this inference, set
\(d_*=\sum|d_n|\), \(a_*=\sum a_n\), \(b_*=\sum b_n\),
and \(c_*=\sum c_n\), all finite by the preceding bounds. Then
\[
 S\le d_*^2,\qquad
 C\le\tfrac14\{d_*(8b_*+2c_*+12a_*)+b_*^2+a_*c_*\}<\infty.
\]
Thus no summation of a mode-dependent unspecified big-O constant is
being assumed.
For positivity, direct differentiation of the actual q_n gives
\(q_n'(0)=(-16v_n^3+60v_n^2-30v_n)e^{-v_n}\).
For n=2, \(v_n=4\pi>12\), and
\(8v_n^2-30v_n+15=v_n(8v_n-30)+15>0\), so d_2<0.
Thus \(S\ge d_2^2>0\).

Now sum the preceding error bound using the already proved absolute
Fourier interchange for \(P_{11}\). This proves (2). If
\(x\ge\max\{1,\sqrt{C/S}\}\), then \(Cx^{-8}\le Sx^{-6}\);
(3) follows, including equality at the threshold. By the necessity
proved in L233, a continuous integrable positive-definite function has
nonnegative Fourier transform everywhere. Therefore \(P_{11}\) is
not positive definite.

This specialization of L234/L356's boundary method rejects the
separate-primitive-family positivity threshold, which required every
\(\widehat P_{ab}(\xi)\ge0\). It does not reject (1): all spatial
summands remain nonnegative and every regrouping remains legitimate.
Nor does it reject the total first sign. The diagonal expression is a
sum of self-pair spectra, whereas the spectrum associated with
\(\sum_n k_n\) includes all off-diagonal terms. Removing those terms
would remove the very compensation still needed. No RH counterexample,
all-degree positivity, or numerical onset is claimed. This is a local
specialization of an established method; no originality beyond the
sources checked is asserted.

Independent conceptual audit, 31 October 2026: the unique gcd
partition, both off-diagonal orientations, compact domination and
weighted L1/Fourier interchanges were checked against their complete
majorants. The three identities (7) were replayed from the two
one-step integration-by-parts formulas, and (8) was checked from the
original differentiated integrals, not from asymptotics. The boundary
product-rule factors 4, 20, 5, 12 and 30 and the full product error in
(9) survive review. The frequency 2x, factor 1/4 and coefficient -2S
agree with L233; the total-kernel identification there uses F=2Xi,
whereas each individual mode uses F_n. The positive term d_2^2 and
the condition x^2>=C/S give strict negativity even at X_0. No defect,
changed hypothesis, stronger sign bound or numerical onset was found.
The added envelope and total-norm details make the reviewed estimates
explicit; the conclusion and its mathematical inputs are unchanged.

## Mathlib

The full primitive-family theorem and the summed diagonal-tail bound:
**not checked**. No matching theorem or absence claim is asserted.
The reused L356 method has supporting smooth-series and Gaussian
summation references, but those are not matches for this result.
The measure-theoretic input here is the precisely cited Durrett theorem;
its full corresponding Mathlib coverage was not checked in this step.
