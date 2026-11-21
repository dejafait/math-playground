# Corollary 34q: Ramanujan's gamma multiplier has no finite positive convolution inverse

## Hypotheses

Use the real source variable t and define

    w(t) = |Gamma((-1+it)/4)|^2/(1+t^2),
    v(t) = w(0)/w(t).

The proposed inverse is restricted to convolution by a finite positive
Borel measure nu on R, with Fourier convention

    hat(nu)(t) = integral_R exp(-itx) dnu(x).

Specifically, it would invert the normalized Fourier multiplier w(t)/w(0),
so it must satisfy hat(nu)=v. The gamma arguments here are never poles;
Gamma has no zeros, so w and v are finite and strictly positive.

## Conclusion

The exact analytic bound is v(1)>=4>1, whereas a finite positive measure
with hat(nu)(0)=v(0)=1 must have |hat(nu)(1)|<=1. Consequently the
proposed finite positive convolution inverse does not exist. The
positive-definiteness matrix at frequencies {0,1} has determinant
1-v(1)^2<=-15.

## Proof

The precise source multiplier is the gamma weight in Atul Dixit,
*Transformation formulas associated with integrals involving the Riemann
Xi-function*, Monatsh. Math. 164(2) (2011), 133-156,
[author manuscript](https://adixit.people.iitgn.ac.in/wp/wp-content/uploads/2025/11/transformation_formulas.pdf),
Theorem 1.1, equation (1.6), manuscript pp. 1-2. That identity assumes
alpha,beta>0 and alpha beta=1; its cosine uses source variable t and its
Xi argument is t/2. The present test is at source t=1. The scalar outside
the integral cancels in normalization. Only this explicit weight is
used, not the shifted-parameter identity or its differentiation.

Import Gamma(z+1)=z Gamma(z) from
[NIST DLMF 5.5.1](https://dlmf.nist.gov/5.5.E1) and
|Gamma(x+iy)|<=Gamma(x) for x>0 and real y from
[NIST DLMF 5.6.6](https://dlmf.nist.gov/5.6.E6).
The nonpole and nonvanishing facts are the standard Gamma properties in
[DLMF 5.2(i)](https://dlmf.nist.gov/5.2#i).
Write A=Gamma(3/4)>0 and B=|Gamma(3/4+i/4)|>0. Recurrence at -1/4 gives

    |Gamma(-1/4)|^2 = 16 A^2,
    w(0) = 16 A^2.

At z=(-1+i)/4, |z|^2=1/8. Recurrence therefore gives

    |Gamma((-1+i)/4)|^2 = 8 B^2,
    w(1) = (8 B^2)/2 = 4 B^2.

The modulus bound applies at x=3/4>0, y=1/4 and gives B<=A. Thus

    v(1) = (16 A^2)/(4 B^2) = 4 A^2/B^2 >= 4.

In particular both the recurrence factor and the original denominator
1+t^2 have been retained. No Euler integral at real part -1/4 is used.

The forward implication of Bochner's theorem, as stated and proved in
Gregory Fasshauer, [Chapter 2, Theorem 2.2.1, printed pp. 10-11](https://www.math.iit.edu/~fass/603_ch2.pdf),
says that a finite positive measure has a positive-definite Fourier
transform. Use the probability convention above, absorbing the source's
positive Fourier normalization constant. If hat(nu)=v, then nu(R)=1.
Its positive-definiteness matrix at {0,1} would be

    [ 1     v(1) ]
    [ v(1)  1    ],

because v is real and even. Its determinant must be nonnegative, giving
|v(1)|<=1. But the computed bound makes that determinant at most -15.
This contradiction proves the stated nonexistence. This is a two-point
specialization of known Gamma and Fourier-positivity tools, not a
reproof of Bochner's theorem or a claim of new general mathematics.

The obstruction also excludes an unnormalized finite positive inverse
with transform 1/w: multiplying its measure by w(0)>0 would yield nu.
It does not exclude signed measures, distributions, inverses valid only
on restricted actual data, paid correction terms, or another modular
identity. No signed parameter coefficient or Xi mixed sign is proved.
The relevance is to one proposed transfer toward L030-L032/C032a;
these are context, not mathematical premises of this result. The
all-degree, global and actual-data identification gaps remain open.

### Independent audit, 21 November 2026 (2078)

The proof checks under the exact finite-positive-Borel-measure contract.
The source's variable is t, with Xi argument t/2; normalizing the
multiplier at zero gives w/w(0), whose multiplicative inverse is w(0)/w.
Changing the global scalar in Dixit's identity therefore cannot change
the normalized test. No assertion that w itself is a probability
characteristic function is needed.

For every real t the gamma argument has real part -1/4 and cannot be a
nonpositive integer. DLMF 5.2(i) consequently ensures finiteness and
nonvanishing; 1+t^2 is positive. The recurrence is used only at nonpoles.
At t=0 its squared modulus factor is 1/16; at t=1 it is 1/8, followed
by division by 2 from the original denominator. Thus the two displayed
values of w, and v(1)=4 A^2/B^2, have the correct direction and factors.
The sole modulus inequality is applied at real part 3/4, in its stated
positive-real-part domain. Gamma conjugation at that real part follows
from the Euler integral in DLMF 5.2.1 by complex conjugation; recurrence
then gives the evenness of w and v used in the matrix. This uses no
integral at real part -1/4 and no limit interchange.

Finally, in the specified Fourier convention, evaluation at zero gives
nu(R)=v(0)=1. The cited forward Bochner implication gives a Hermitian
positive semidefinite two-point matrix; real even v gives exactly the
matrix displayed above. Its determinant is 1-v(1)^2<=1-16=-15, strictly
below the necessary lower bound zero. Equivalently, positivity and
mass one give |integral exp(-ix) dnu(x)|<=1 directly by the triangle
inequality. This independently checks the same necessary condition,
without using Bochner's converse or assuming RH. Scaling a putative
measure with transform 1/w by the strictly positive number w(0) also
checks the unnormalized qualification. No repair of the statement or
proof is required; this is verification of a standard specialization,
not an additional mathematical discovery or an exclusion of the other
operations listed above.

## Mathlib

Full matching coverage for this specialized multiplier obstruction is
unchecked; unknown availability is not evidence of absence. The proof
uses the precise standard sources above. No Mathlib theorem is claimed
as a matching formalization.
