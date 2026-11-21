# Corollary 785a: the reciprocal determinant is the original coefficient minor

## Hypotheses

Let g(z)=sum_(j>=0) c_j z^j be a real-coefficient power series near zero,
with c_0>0, and let 1/g(z)=sum_(j>=0) u_j z^j locally. It suffices instead
to use formal power series over the reals with this nonzero constant term.
Set

    H=[[u_2,u_3],[u_3,u_4]],
    T=[c_(2+j-i)]_(i,j=0,1,2).

For the actual-Xi specialization use only L776's ordinary coefficient
normalization G(w)=sum a_j w^j, a_0>0, and D_(3,2)=det[a_(2+j-i)].
Put g(z)=G(varrho z), varrho>0. Here varrho is the positive scalar called
R in L776; it is not the residual matrix called R in L785.

When transferring the result to that residual matrix, assume all of
L785's additional hypotheses: sigma>1, g holomorphic near the closed
sigma-disk, and exactly two distinct simple negative roots a,b in (-1,0)
and no other zeros in that closed disk. These additional hypotheses are
not needed for the coefficient identity itself.

## Conclusion

There are exact identities

    det H = u_2 u_4-u_3^2 = -det T/c_0^5,                 (1)
    det H = -varrho^6 D_(3,2)/a_0^5                     (2)

in the stated specialization. Both include zero determinants. Thus the
reciprocal determinant has the opposite sign to the original minor,
including simultaneous vanishing. It supplies no independent sign test.

Under L785's hypotheses its residual matrix, denoted here by script R,
satisfies

    det(script R)=-(det E)^2(b-a)^2 det T/c_0^5.          (3)

Equation (3) is conditional on the root grouping; (1)-(2) do not establish
that grouping. No full inertia, positive definiteness, actual-Xi sign,
global grouping, all-order or other-minor conclusion is asserted.

## Proof

**Imported identity and scalar applicability.** Use I. G. Macdonald,
*Symmetric Functions and Hall Polynomials*, second edition, Oxford (1995),
I.2 (2.6)-(2.9'), pp.21-23, and I.3 (3.4)-(3.7'), pp.41-42
([inspected primary-book transcription](https://djvu.online/file/evBrSjuw4lsEJ)).
These supply H(t)E(-t)=1 and the ordinary/dual Jacobi-Trudi identities

    det[h_(lambda_i-i+j)] = det[e_(lambda'_i-i+j)].

Here h_0=e_0=1 and negative subscripts mean zero. The two determinant
sizes are at least the lengths of lambda and its conjugate lambda'.
As recorded in the completed source assessment, I.2 (2.8) permits scalar
specialization by arbitrary h_j; no positive alphabet is required.
The identities are polynomial identities, and their proof uses inverse
unit triangular coefficient matrices, not inverse selected minors.
We import this identity rather than reprove it. The prior ready review is
`drafts/literature/2026-11-05-reciprocal-minor-duality-specialization.md`;
the inspected source cases are recorded in
`drafts/literature/2026-11-05-reciprocal-minor-duality-comparison.md`.

Take h_j=c_j/c_0. The normalized generating series is H(t)=g(t)/c_0,
so E(t)=1/H(-t)=c_0/g(-t). Consequently

    e_j=(-1)^j c_0 u_j.

All uses are through degree four, in formal power series at zero; neither
analytic continuation nor convergence at a root is involved. Apply the
import with lambda=(2,2,2), lambda'=(3,3). Its two permitted sizes are
three and two, respectively, and its matrices are exactly

    [h_(2+j-i)]_(i,j=0,1,2),   [[e_3,e_4],[e_2,e_3]].

The first determinant is c_0^-3 det T. In the second matrix substitute
e_3=-c_0 u_3, e_4=c_0 u_4, e_2=c_0 u_2. This gives

    c_0^-3 det T
      =c_0^2 det[[-u_3,u_4],[u_2,-u_3]]
      =c_0^2 (u_3^2-u_2 u_4)
      =-c_0^2 det H.

For an explicit orientation check, reversing the two columns of H gives
[[u_3,u_2],[u_4,u_3]] with determinant -det H. Transposing gives
[[u_3,u_4],[u_2,u_3]]. Negating its first row and then its second column
gives the normalized e-block above; the two sign changes cancel.
Thus exactly one reversal contributes the minus sign; there is no
unpaid cofactor sign. Division by c_0^2 yields (1). No entry or determinant
of either selected block was divided by. In particular singular and zero
blocks remain covered by the imported polynomial identity.

**Radius and normalization.** In the actual specialization,
c_j=varrho^j a_j and c_0=a_0. With

    A=[a_(2+j-i)]_(i,j=0,1,2), S=diag(1,varrho,varrho^2),

one has T=varrho^2 S^-1 A S entry by entry. Since varrho>0, S is
invertible and det T=varrho^6 det A=varrho^6 D_(3,2). Combining with
(1) proves (2). Only the defining series and positivity of a_0 from
L776 are used; its admissible-radius, logarithm and Fredholm conclusions
are not premises of this algebraic specialization.

Finally L785 gives script R=(E W)H(E W)^T with
W=[[1,-b],[1,-a]], det W=b-a, and E positive invertible. Taking
determinants and using (1) proves (3), without inverting a selected
minor. This last use retains every analytic hypothesis of L785.

**Meaning and limits.** The positive factors c_0^5, a_0^5 and varrho^6
show that det H<0 is precisely D_(3,2)>0 in the actual normalization,
and det H=0 is precisely D_(3,2)=0. The identity therefore closes the
proposed independent algebraic signing route: controlling this
determinant has not paid a different theta inequality. It does not
settle the full inertia problem from a determinant. Actual-Xi grouping,
global/all-order positivity and other mixed minors remain unpaid.
This is a known-theorem application, with no claim of mathematical
novelty beyond the inspected sources. No numerical or symbolic script
is needed for the displayed finite substitution.

## Mathlib

Full matching Jacobi-Trudi or local-specialization coverage is not
checked; no presence or absence claim is made. The mathematical input
is the precisely cited polynomial identity and its scalar specialization,
with L776's normalization and L785's conditional congruence as stated.
