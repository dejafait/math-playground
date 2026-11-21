# C759m: Known time-one smoothing for the complete even Weil operator

## Hypotheses

Let I=(-1,1), with Lebesgue measure, and let E and R_I denote zero
extension and restriction. Use the Fourier transform
hat f(t)=integral f(x)exp(-itx)dx. Let A_e be the self-adjoint operator
on real even L2(I) associated with exactly C759a(1),(5)-(6): the
complete unneutralized closed Weil form. Both original pole
functionals and all five overlapping prime powers n=2,3,4,5,7 are
retained. Let G be C759k's killed reference, with exponent
Psi(t)=half log(1+t²), Levy density exp(-|x|)/(2|x|), and the
smooth-core closed form C759k(2). Write b=log(2pi) and
a_n=Lambda(n)/sqrt(n), where Lambda(p^j)=log p.

The prior IMPORT assessment
`drafts/literature/2026-11-13-complete-even-time-one-smoothing-review-843.md`,
completed in comparison844, covers this exact applicability check.
This imports bramble_trace, *Boundary traces and support variation
for localized Weil operators*, paper67 v1, 27 October2026,
[Section3.1 (3.4)-(3.6), Section3.2 (3.7)-(3.8)](https://rstation.ai/problems/riemann_hypothesis/papers/67).
L515 supplies the already audited general signed-measure statement
and stronger-norm justification. No new smoothing theorem is claimed.

## Conclusion

Set

\[
 M_1=\gamma+\frac\pi2+2\log2
       +2\sum_{n\in\{2,3,4,5,7\}}\frac{\Lambda(n)}{\sqrt n}
       +8\sinh1,\qquad B=\frac{e^{b+M_1}}{\sqrt2}.             \tag{1}
\]

Then

\[
 \|e^{-A_e}f\|_\infty\le B\|f\|_2
 \quad\text{for every real even }f\in L2(I).                 \tag{2}
\]

Every eigenvector u in D(A_e), A_e u=lambda u, satisfies

\[
 \|u\|_\infty\le e^\lambda B\|u\|_2.                        \tag{3}
\]

These are essential supremum bounds and statements about equivalence
classes, including every vector in every eigenspace. There is no
positivity, simplicity, isolation or sign assumption. Only time1 is
asserted; no all-small-times smoothing, boundary trace, positive trial
margin, parity ordering or Xi realization follows. The constant is
the source's fixed-support variation majorant, not C759k's budget24.

## Proof

### Exact finite measure before even restriction

L741(13),(16) and C759k(4)-(5) give

\[
 \rho(x)=\tfrac12r(|x|)
 =\frac{e^{-|x|/2}}{1-e^{-2|x|}}-\frac{e^{-|x|}}{2|x|}
 \quad(x\ne0),\qquad \widehat\rho(t)=\Re\widehat r(it).
\]

The value at0 is immaterial. In particular rho is integrable, by
L741's absolute-integrability proof; its normalization is half the
one-sided r followed by even extension. It is exactly the density
of nu_r in the cited source (3.4). On the whole line define

\[
 \mu(dx)=\rho(x)dx+
 \sum_{n\in\{2,3,4,5,7\}}a_n
       (\delta_{\log n}+\delta_{-\log n})(dx)
       -2\cosh(x/2)\mathbf1_{|x|\le2}\,dx.                  \tag{4}
\]

This is a finite real even signed Borel measure. Source (3.6), with
support-radius upper bound A=1, supplies
||rho||_1<=gamma+pi/2+2log2. Hence its triangle bound is

\[
 \|\mu\|_{\rm TV}\le\|\rho\|_1+2\sum_n a_n+
 \int_{-2}^{2}2\cosh(x/2)dx
 \le\gamma+\pi/2+2\log2+2\sum_n a_n+8\sinh1=M_1.           \tag{5}
\]

The source's density bound is imported, not inferred from an operator
norm. Independently L741 gives ||rho||_1<=log2+4, which also verifies
finiteness without the sharper source constant. No cancellation of
signed densities is required in (5).

Let C_mu f=R_I(mu*Ef). Each atomic pair in (4) acts as
a_n[Ef(x-log n)+Ef(x+log n)] on I. Thus it is exactly C759k's J,
including both zero-extension masks. The list is exhaustive since
log7<2<log8; the other integers below8 with nonzero Lambda are
2,3,4,5. The density rho gives exactly C759k's R.

For x,y in I, |x-y|<2. Therefore compression of the last density in
(4) has kernel -2cosh((x-y)/2), without a truncation error. Its
negative in G-bI-C_mu is the positive operator of the two original
poles. Explicitly its quadratic form on real f is
2F_f(i/2)F_f(-i/2), as in C759a(1). For even f,

\[
 \int_I2\cosh((x-y)/2)f(y)dy
 =2\cosh(x/2)\int_I\cosh(y/2)f(y)dy=Pf(x),
\]

since the sinh moment vanishes. Consequently on the even space
C_mu=R+J-P and G-bI-C_mu=G-K=A_e. The cutoff in (4) is essential:
an uncut whole-line cosh density would not be a finite measure.

### Closed realization, restriction and the imported bound

The preceding identities initially agree on the smooth compact core.
C759a Proof1 and C759k Proof5 identify its closure with the supported
logarithmic Fourier space. This is the killed reference's part-form
domain, translated from L515's interval (0,2). Translation preserves
the Fourier weight and both norms; there is no Fourier or time factor.

C_mu is bounded self-adjoint on L2, with norm at most ||mu||_TV.
Thus the two closed forms differ by the bounded form represented by
bI+C_mu. A form functional is represented by an L2 vector for one
form if and only if it is for the other. Their full operators
therefore have the same domain D(G) and differ by -bI-C_mu. This
is the domain identification already checked in C759k(5)-(6), Proof5.
Reflection commutes with G and C_mu, since the reference and mu are
even. Its even subspace is reducing; the full operator's restriction
and restricted semigroup are precisely A_e and exp(-t A_e).
No formal multiplier equality is substituted for this domain check.

Apply L515(1) to this translated interval, with c=b and the finite
measure (4). Its hypotheses impose neither positivity of C_mu nor
commutation of compressed convolution with G. With M=||mu||_TV,
the bound is exp(b+M)/sqrt2. L515(7)-(10) already justify the Dyson
sum in the stronger operator norm L2-to-L-infinity: the jth term
at time1 has norm at most M^j/(j!sqrt2), and its tail tends to0
there. The length2 embedding into L2 identifies that sum with the
L2 semigroup. This is the audited passage being imported, not an
inference from L2 perturbation convergence alone. Equation (5) and
restriction to even data give (2), exactly the source's (3.7) at a=A=1.

Finally the spectral theorem gives exp(-A_e)u=exp(-lambda)u for
every eigenvector; (2) gives (3), the source's (3.8). This does not
assert that eigenvalues are simple or that an eigenvector has a sign.
It supplies the boundedness prerequisite for a later application of
C759l to genuine eigenvectors. That later boundary application and
all sign/isolation/Xi questions are outside this import.

### Separate applicability audit, 13 November2026, step847

The unchanged IMPORT assessment
`drafts/literature/2026-11-13-complete-even-time-one-import-audit-845.md`,
approved846 before this invocation, covers this check. Equations(1)-(5)
pass without correction. This verifies a local known-result import;
it establishes no theorem beyond the inspected sources. The primary
paper67 v1 statements are reused from comparison843 completed844,
"Exact inspected overlap"; no fresh primary retrieval is claimed.

**Density and variation constant.** L741(13) is
r(t)=2exp(-t/2)/(1-exp(-2t))-exp(-t)/t for t>0. Thus its
half-density even extension is precisely the source's nu_r recorded
in paper67(3.4), with no additional factor2. Absolute integrability
permits even symmetrization, and its Fourier transform is
integral_0^infinity r(t)cos(xt)dt=Re hat r(ix). L741(16) then gives
the exact multiplier correction used in C759a(5), not merely an
asymptotic symbol comparison. The sharper density majorant
gamma+pi/2+2log2 is the explicit source import in(3.6), as recorded
in comparison844; it is not derived from L741's log2+4 estimate.
Each atom has positive mass a_n, so the atomic variation is exactly
2 sum_n a_n. The absolute integral of the negative pole density is
integral_(-2)^2 2cosh(x/2)dx=8sinh1. The triangle inequality therefore
gives exactly(5) and the stated M_1, even if the two densities cancel
on part of their support. C759k's norm budget24 is not used here.

**Masks and both poles.** A pair of atoms at +/-log n compresses
to precisely the two masked zero-extended translations in C759k(4).
The exhaustive nonzero list below exp2 is 2,3,4,5,7; in particular
Lambda(4)=log2 and Lambda(6)=0. No translation is made periodic.
Every difference x-y for x,y in I has absolute value less than2.
Thus the truncated density in(4) supplies the entire kernel
-2cosh((x-y)/2); endpoint choices for its density have no effect.
For real f its opposite quadratic form equals
2(integral exp(x/2)f(x)dx)(integral exp(-x/2)f(x)dx), exactly the
two original pole functionals. The odd sinh moment vanishes on even
data, leaving +P in A_e. Consequently C_mu=R+J-P and
A_e=G-bI-R-J+P on the even restriction, with the required signs.
The whole-line cut-off makes the measure finite before compression.

**Both domain identifications and parity.** C759a Proof1 and C759k
Proof5 check that the compact smooth core closes to the full supported
logarithmic Fourier space: support contraction followed by mollification
approximates every supported weighted vector, and completeness plus L2
convergence preserves that support in the converse direction. Hence
the reference part form and the complete form have the same form
domain. For a vector f in this domain, their form functionals differ
by the L2 functional represented by (bI+C_mu)f. Each functional is
L2-representable if the other is, proving both operator-domain
inclusions by the form representation theorem. This verifies the
closed realization, rather than assuming that core identities alone
determine an operator. Translation from (0,2) preserves the Fourier
weight and norms. Reflection commutes with the reference form and
the bounded even measure convolution, hence with their operators
and semigroups. Its even subspace is reducing. This pays the even
restriction without any ground-state or simplicity premise.

**Stronger norm and every eigenvector.** Apply the already audited
L515(1),(7)-(10) with c=b and M=||mu||_TV. At time1 its jth
term has L2-to-L-infinity norm at most M^j/(j!sqrt2), and the
factorial tail tends to0 in that operator norm. On I the inequality
||h||_2<=sqrt2||h||_infinity identifies this limit with the L2
Dyson sum. Thus the bound exp(b+M)/sqrt2 applies to this very
closed operator. Replacing M by its majorant M_1 gives(2).
No commutation of compressed operators, L-infinity C0 assumption
or all-small-times smoothing is used. Every genuine eigenvector
lies in the identified operator domain and satisfies
exp(-A_e)u=exp(-lambda)u by the spectral theorem. This proves(3)
for each vector of every eigenspace, as a bound on equivalence classes.

No dependency changes are needed: L515, L741, C759a and C759k
are precisely the mathematical inputs already recorded in the DAG.
C759l is a prospective use only. Its forcing application, ground-state
sign and simplicity, isolation, trial margin, parity ordering and
actual-Xi mixed positivity remain outside this audited import.

## Mathlib

Full matching Mathlib coverage was not checked. L515 and C759k record
the named bounded-perturbation, spectral, Plancherel and killed-part
inputs and their source qualifications. No particular Mathlib
declaration has been inspected here; unknown availability is not
evidence of absence, and no Lean verification is claimed.
