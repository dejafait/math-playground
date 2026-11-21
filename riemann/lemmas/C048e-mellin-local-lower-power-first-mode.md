# Corollary C048e: the finite horizontal lower-power first-mode allowance

## Hypotheses

Let p be complex, r=|p|, L=log r>=12, with Re p>=-r/(4L).
Use C048c's principal branches and definitions

\[
 w=W_0(2p/\pi),\quad u_0=w/2,\quad d=1/(3L),\quad
 h_p(u)=2p\operatorname{Log}u-\pi e^{2u},\quad
 g(u)=8\pi^2e^{9u/2}/u,\quad K(s)=g(u_0+s)/g(u_0),\quad
 A_0=4p(1+w)/w^2.
\]

The variable s is real, and the integral below is oriented from -d to d.
Define precisely

\[
 T_{\rm low}(p)=\frac{\left|\int_{-d}^d K(s)
       \frac{-3}{2\pi e^{2(u_0+s)}}
       e^{h_p(u_0+s)-h_p(u_0)}\,ds\right|}
       {|\sqrt{\pi/A_0}|}.
                                                        \tag{1}
\]

The square root is principal. This is the notebook's operational
finite-integral definition of the lower-power mode1 contribution.

## Conclusion

Throughout this full closed sector,

\[
 T_{\rm low}(p)\le C_{\rm low}\frac{L^{3/2}}r
 <\frac{783}{425}\frac{L^{3/2}}r
 <2\frac{L^{3/2}}r,\qquad
 C_{\rm low}=\frac{29}{25}\frac34\frac{18}{17}
                         \sqrt{\frac{1800}{799}}.        \tag{2}
\]

This is REPRODUCTION of the local allowance claimed in K. Kawano,
*Logarithmic Inequalities of Arbitrary Order for the Riemann Xi
Coefficients*, [Preprints.org202611.0383v1, posted4November2026,
DOI10.20944/preprints202611.0383.v1](https://www.preprints.org/manuscript/202611.0383/v1),
Section5.2(28)/Lemma5.1(i), AppendixA.2(A3), AppendixB's B_low
display immediately after B_g, and AppendixC's lower-power allowance
between the distant-left-tail and other local-mode allowances.
The primary cases are retained in source-notes1633; the unchanged
SPECIALIZE assessment1633 covers this exact target. The source uses
no printed symbol T_low: (1) specifies the local absolute allowance
being verified. AppendixB's different finite-band width and cell data
are not imported. Verification is needed because the effective source
claim was not an established local theorem; the proof below specializes
the known Gaussian method using audited C048c estimates.

The coefficient calculation is slack in reproducing the claimed2,
not a claimed new Mellin method. This pays only (1); other local theta
modes, horizontal tails, full remainder assembly, zero counts,
inversion and sufficient actual-Xi mixed signs remain unresolved.
It supplies neither RH nor an unverified complete candidate.

## Proof

C048c proves that the full segment lies in Re u>1, |Im u|<pi/4,
that g(u_0) and A_0 are nonzero, and that Re A_0>0. Hence every
factor in (1) is defined and continuous on the compact interval;
the integral is an ordinary absolutely convergent finite integral.
Its established estimates (6), (10), (12), (19) give, respectively,

\[
 |w|<L,\qquad |A_0|<6r/L,\qquad |K(s)|\le29/25,
 \qquad
 \Re\{h_p(u_0+s)-h_p(u_0)\}\le-b_*s^2,
 \quad b_*:=\frac{799}{300}\frac r{L^2}>0.             \tag{3}
\]

For the last estimate, C048c writes the phase difference as
-A_0s^2+Z(s); its (19) bounds -Re(A_0)s^2+|Z(s)|,
which bounds the real part in (3). No smallness of Z at the endpoints
is assumed.

The exact Lambert identity pi e^w=2p/w and 2u_0=w imply

\[
 \frac{-3}{2\pi e^{2(u_0+s)}}=-\frac{3w}{4p}e^{-2s}.
                                                        \tag{4}
\]

Thus the negative sign and the factor4 in the denominator are retained
before taking absolute values. Since p is nonzero and |s|<=d,

\[
 \left|\frac{-3}{2\pi e^{2(u_0+s)}}\right|
 =\frac{3|w|}{4r}e^{-2s}
 \le\frac{3L}{4r}e^{2d}.                              \tag{5}
\]

The triangle inequality, (3) and (5) therefore yield

\[
 \left|\int_{-d}^d K(s)
       \frac{-3}{2\pi e^{2(u_0+s)}}
       e^{h_p(u_0+s)-h_p(u_0)}ds\right|
 \le\frac{29}{25}\frac{3L}{4r}e^{2d}
                         \int_{-d}^d e^{-b_*s^2}ds
 \le\frac{29}{25}\frac{3L}{4r}e^{2d}\sqrt{\pi/b_*}.
                                                        \tag{6}
\]

Only the nonnegative real Gaussian majorant is extended to the real
line. Its full integral is sqrt(pi/b_*), by the standard real Gaussian
integral, equivalently [NIST DLMF7.7.6](https://dlmf.nist.gov/7.7.E6)
with positive real coefficient a=b_*, its other parameters zero,
followed by even reflection of the half-line integral. Positivity in
(3) supplies its hypothesis; exponential decay gives absolute
convergence. No equality between an oscillatory integral and its
absolute majorant is asserted.

For a nonzero complex A_0 the modulus of its principal square root
satisfies |sqrt(pi/A_0)|=sqrt(pi/|A_0|). Dividing (6) by this modulus
and using (3) gives

\[
 T_{\rm low}(p)
 \le\frac{29}{25}\frac{3L}{4r}e^{2d}
                                      \sqrt{|A_0|/b_*}
 \le\frac{29}{25}\frac34 e^{2/(3L)}
                   \sqrt{\frac{1800}{799}}\frac{L^{3/2}}r.
                                                        \tag{7}
\]

For every L>=12, 0<2/(3L)<=1/18. The exponential power series
gives e^t<sum_(n>=0)t^n=1/(1-t) for 0<t<1: termwise
t^n/n!<=t^n, with a strict inequality already for n=2.
Consequently e^(2/(3L))<18/17. Also sqrt(1800/799)<2 because
1800<4*799=3196, with all quantities positive. These comparisons
and (7) prove (2), since exactly

\[
 \frac{29}{25}\frac34\frac{18}{17}\,2
 =\frac{783}{425}<2\quad(783<850).                    \tag{8}
\]

These are exact comparisons, with no numerical quadrature or grid.
The bounds apply on the entire ray L>=12; (3) is uniform throughout
the sector and (5) applies at both endpoints s=+-d. For Im p<0,
C048c's branches and phase/amplitude estimates respect conjugation:
the real s interval is unchanged, and the integral in (1) is
conjugated, so its modulus and normalization are unchanged. The
positive-imaginary and negative-imaginary angular boundaries are
already included in (3). If Im p=0, the sector forces p>0; no step
divides by Im p or Im w. Thus real p, r=e^12, both angular boundaries
and unbounded L are all covered. No contour deformation, theta-series
interchange or full-path estimate is used.

### Independent audit1635 (19 November2026)

The unchanged SPECIALIZE assessment1633 covers the exact integral (1)
and threshold in (2). This audit independently checked the argument
above against C048c's stated premises and source-notes1633; no
mathematical repair was required. This is validation of a reproduced
source component, not a new result beyond the sources checked.

Multiplying pi e^w=2p/w by e^(2s) gives the denominator in (4),
so the correction is -3w e^(-2s)/(4p), with no missing factor2
or extra frequency-cell variable. For real |s|<=d,
e^(-2s)<=e^(2d). C048c's phase decomposition and (19) imply
Re(h_p(u_0+s)-h_p(u_0))<=-b_*s^2 even when |Z(s)| is large.
Its separate bound on K therefore gives exactly the integrand
majorant in (6). Continuity on the compact segment justifies the
triangle inequality; only the positive real Gaussian is extended.
The full Gaussian already includes both signs of s, so it needs
no further factor2.

For any square root z of pi/A_0, |z|^2=pi/|A_0|. Thus the
normalization loss is sqrt(|A_0|/b_*), not its reciprocal or a
ratio using Re A_0 in place of |A_0|. Its squared upper bound
is exactly (6r/L)/((799/300)r/L^2)=(1800/799)L. Multiplication
by L/r gives L^(3/2)/r in (7). The positive-real specialization
of DLMF7.7.6 has b_*>0 and zero remaining parameters, as required.

Finally t=2/(3L) lies in (0,1/18] for every finite L>=12.
The series comparison is strict also at t=1/18; hence e^t<18/17.
The independent scalar checks are 1800<3196 and
29*3*18*2/(25*4*17)=783/425<850/425=2. None requires an
upper bound for L. All denominators are nonzero by C048c;
its uniform estimates include both angular boundaries and r=e^12.
Conjugation preserves the principal Lambert and Log branches here
and the principal Gaussian root, since A_0 is in the right half-plane.
Thus (1) is invariant under conjugating p. Real p in the sector is
positive. This checks reflection, real-axis and endpoint cases
without an extra angular or height assumption.

The only direct local input remains C048c. This audit uses no contour
change, infinite theta-mode sum, numerical script or new interchange.
It validates only the finite correction (1); all qualifications after
(2) remain in force. The slack in C_low does not establish any bound
on omitted modes or a sufficient mixed-sign bridge.

## Mathlib

Full matching coverage of this moving-sector, normalized finite
Mellin correction has not been checked. The supporting Gaussian
input is cited precisely above; Mathlib coverage of that supporting
specialization has not been checked either. Unknown coverage is not
evidence of absence. The only direct local mathematical input is
C048c, and the remaining comparisons are given explicitly in (4)-(8).
