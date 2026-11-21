# Corollary C028b: reciprocal Jensen height obstruction and RH equivalence

## Hypotheses

Use the actual completion Xi of L018 and the positive moments of L021.
Use precisely the unshifted reciprocal polynomial R_d defined in C028a:

    gamma_j=j! M_(2j)/(2j)!>0,
    F(u)=sum_(j>=0) (gamma_j/gamma_0) u^j/j!,
    J_d(x)=sum_(j=0)^d binom(d,j) gamma_j x^j,
    R_d(x)=sum_(j=0)^d binom(d,j) gamma_j x^(d-j).

Integers d tend to infinity through d>=3. Define

    H_d=sum_(j=1)^d |Im z_j(R_d)|,

where all roots are counted with algebraic multiplicity. For the
conditional bound only, suppose w is a fixed nonreal zero of F with
multiplicity m>=1. No actual nonreal zero, RH, Laguerre--Polya membership,
simple-root hypothesis or effective onset is an unconditional premise.

## Conclusion

For each such hypothetical fixed zero,

    liminf_(d->infinity) H_d/d >= m |Im(1/w)| > 0.

For this actual family, the assertion H_d=o(d) is equivalent to RH.
If RH holds, the stronger statement H_d=0 for every d>=3 holds.
Neither H_d=o(d) nor RH is established here. This is a specialization of
known Jensen convergence, Rouche stability and the Jensen criterion;
no originality beyond those checked sources is claimed.

## Proof

### Imported analytic inputs and applicability

Cormac O'Sullivan, *Zeros of Jensen polynomials and asymptotics for the
Riemann xi function*, arXiv:2007.13582v2, 9 December 2020,
[Section 1, (1.2), and Section 3.1, Theorem 3.1 with its proof sketch,
Corollary 3.2](https://arxiv.org/html/2007.13582v2#S3.SS1), supplies:

* the locally uniform Jensen limit g_d(Phi;u/d)->Phi(u) for entire Phi;
* the Jensen hyperbolicity criterion for real entire genus 1* functions;
* its application to Theta(u)=xi(1/2+sqrt(u)), a real entire function
  of order 1/2, including shift n=0.

The first limit is also Craven--Csordas, *Jensen polynomials and the
Turan and Laguerre inequalities*, Pacific J. Math. 136(2) (1989),
241--260, [Lemma 2.2, pp.244--245](https://msp.org/pjm/1989/136-2/pjm-v136-n2-p03-s.pdf),
with derivative index p=0. The legible formula in O'Sullivan is sufficient;
no OCR-obscured formula from that older PDF is needed. These theorems
are imported, rather than reproved.

Terence Tao, *Math 246A, Notes 4: singularities of holomorphic functions*,
11 October 2016,
[Theorem 37 (Rouche's theorem)](https://terrytao.wordpress.com/2016/10/11/math-246a-notes-4-singularities-of-holomorphic-functions/),
counts zeros with multiplicity when holomorphic functions f and f+g
on a neighborhood of a simple closed contour and its interior satisfy
|g|<|f| on the contour. We apply it only to a small circle and entire
functions. No proof of that imported theorem is needed here.

To identify the actual input, L021 gives

    F(-z^2)=Xi(z)/gamma_0,    F(0)=1.

The entire series for F follows directly from the even entire Xi
series: its absolute convergence at any u follows by taking |z|^2=|u|
in that series. Since Xi(z)=xi(1/2+iz), comparison of its Taylor
coefficients gives xi^(2j)(1/2)=M_(2j). Thus Theta=gamma_0 F is exactly
O'Sullivan's (1.2), with the same gamma_j, not a derivative shift or a
Gaussian product. The notation sqrt(u) specifies this even entire
series and does not require a global square-root branch. Multiplication
by the nonzero real constant gamma_0 changes no zeros, order or genus.
Order 1/2 places F in the genus 1* scope of the cited criterion;
membership in the Laguerre--Polya class is not assumed.

### Reciprocal scale and multiplicities

Set Q_d(u)=J_d(u/d)/gamma_0. The imported Jensen limit gives Q_d->F
uniformly on every compact subset of C. Both J_d and R_d have degree
exactly d, with nonzero leading and constant coefficients, because
gamma_0,gamma_d>0. Thus neither polynomial has a zero at zero. For u!=0,

    Q_d(u)=(u/d)^d R_d(d/u)/gamma_0.

The map u->d/u has nonzero derivative away from zero, and the prefactor
is nonzero there. Hence it gives a bijection, preserving multiplicities,
between all d roots of Q_d and all d roots of R_d. If u is such a root,
the corresponding R_d root is z=d/u. Since d is positive and real,

    H_d/d=sum_(Q_d(u)=0) |Im(1/u)|.                 (1)

This is an identity for complete finite root multisets. In particular,
normalizing R_d by gamma_0 or J_d by gamma_0 does not change the statistic.

### A fixed nonreal zero forces the lower bound

Let w be as in the conditional hypothesis and put a=|Im(1/w)|. Since
w is nonreal, w!=0 and a=|Im w|/|w|^2>0. F is not identically zero
because F(0)=1, so w is isolated and has finite multiplicity m.

Fix 0<epsilon<a. Continuity of u->|Im(1/u)| away from zero and isolation
of w permit choosing a radius r>0 such that the closed disk
D={u:|u-w|<=r} avoids zero and the real axis, contains no other zero of
F, and satisfies

    |Im(1/u)| >= a-epsilon   for all u in D.

Its boundary is zero free for F, so eta=min_(boundary D)|F|>0.
Uniform convergence there gives an integer d_0, enlarged to at least
max(3,m), such that for every integer d>=d_0,

    |Q_d-F|<eta<=|F|   on boundary D.

Rouche's theorem, with f=F and g=Q_d-F, therefore gives exactly m zeros
of Q_d in the interior of D, counting multiplicities. Entirety verifies
the holomorphy hypotheses on a neighborhood of the entire closed disk;
strict comparison verifies the boundary hypothesis. Applying (1) and
retaining these m nonnegative terms gives, for every d>=d_0,

    H_d/d >= m(a-epsilon).

Consequently liminf H_d/d>=m(a-epsilon). This is true for every
0<epsilon<a, so letting epsilon decrease to zero proves the displayed
bound. The disk and onset may depend on epsilon and on the fixed w;
no uniform onset, labeled root convergence, simple-root assumption,
moving contour or interchange of infinite zero sums is used.

### Both implications of the height criterion

First suppose H_d=o(d). The lower bound rules out every nonreal zero
of F: any one would imply liminf H_d/d>0, contradicting H_d/d->0.
All coefficients of F are positive, so its convergent real series gives
F(x)>0 for every x>=0. Every zero of F must therefore be negative real.

If Xi(z)=0, the identity F(-z^2)=Xi(z)/gamma_0 shows that -z^2 is a
negative real zero of F. Thus z^2 is positive real. Writing z=x+iy gives
2xy=0 and x^2-y^2>0; these force y=0. Every Xi zero is real. L018's
exact zero correspondence then gives RH. This argument uses the actual
positive coefficients, rather than assuming that a general real entire
function with no nonreal zeros automatically has only negative zeros.

Conversely, suppose RH. By L018 every Xi zero is real. If F(w)=0,
choose any z with -z^2=w. Then Xi(z)=0, so z is real, and w=-z^2<0
because F(0)=1. Thus Theta=gamma_0 F has only real zeros. Apply
O'Sullivan's Corollary 3.2 with n=0: every J_d=J^(d,0) is hyperbolic.
The hypotheses are precisely the actual Theta convention and order
checked above. Its roots are nonzero, so inversion preserves their
reality and makes every R_d hyperbolic. Hence H_d=0 for every d>=3,
which implies H_d=o(d).

### Scope and remaining gap

The two implications make the proposed sublinear height payment a full
RH criterion in this actual unshifted family. No upper estimate has
been supplied. The conditional lower bound supplies no actual nonreal
zero and hence no disproof. C028a's divergent Gaussian coefficient upper
bound is compatible with either possibility and is not an input to the
height lower bound beyond fixing the polynomial convention. L763/L764's
changed series and the inverse-differentiation/prescribed-primitive
stops are contrasts, not mathematical premises. No sum over several F
zeros, rate of convergence or further root-distribution claim is made.

## Mathlib

Not checked. Full matching theorem availability is unknown, including
the actual reciprocal-height specialization and Jensen criterion.
No absence or formal verification is claimed. The imported results have
precise citations above; the local scaling, multiplicity, liminf and
actual-zero specialization are proved explicitly here.
