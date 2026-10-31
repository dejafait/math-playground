# Lemma 571: sharp prescribed-pair disk-Hardy first-sign budget

## Hypotheses

Let 0<r<1 and let m>=1 be an integer. Let A_(r,m) be the class of
functions f holomorphic on an open neighborhood of the closed unit disk,
with f(conj z)=conj f(z), f(0)=1, and zeros of **exact** order m at each
of ir and -ir. Other zeros are allowed. Define

    N(f) = (1/(2*pi)) integral_0^(2*pi) |f(exp(i*theta))|^2 dtheta,
    D_1(f;0) = f'(0)^2 - f(0)*f''(0).

Thus N is the squared normalized H2 norm. Put

    q=r^2, b=q^m, c=m*(q^(-1)-q)>0,
    N_0=b^(-2),
    phi(c) = c^2                 if 0<c<=1,
             2*c-1              if c>=1,
    N_1=b^(-2)*(1+phi(c)).

For the conditional Xi interpretation only, use the actual Xi of L018.
Suppose gamma is real, d>0, Xi(gamma)!=0, and gamma+id and gamma-id
are zeros of exact multiplicity m. Fix R>d and put r=d/R. No simplicity,
separation, zero-free quotient, or information on other zeros is assumed.

## Conclusion

1. The minimum of N on A_(r,m) is N_0, attained uniquely by

       f_0(z)=b^(-1)*B(z),
       B(z)=((z^2+q)/(1+q*z^2))^m.

   In particular D_1(f_0;0)=-2c<0.

2. The minimum of N over the subclass with D_1(f;0)>=0 is N_1.
   It is attained with D_1=0 and exact prescribed order. The complete
   list of minimizers is f=b^(-1)*B*h, where

       h(z)=1-c*z^2                          if 0<c<=1,
       h(z)=1+u*z-z^2, u=+/-sqrt(2*(c-1))     if c>1.

   At c=1 the two descriptions coincide. Thus N_1>N_0.

3. For a squared-norm upper budget K, the class with N(f)<=K is
   nonempty exactly when K>=N_0. Every member has D_1<0 exactly for
   N_0<=K<N_1, among nonempty budgets. At K=N_1 zero defect is possible
   but positive defect is impossible. For K>N_1 positive defect is
   possible. More strongly, at every exact norm N>=N_0 a negative-defect
   function exists; at every exact norm N>=N_1 a zero-defect function
   exists; and a positive-defect function exists at exact norm N if and
   only if N>N_1. All these examples lie in A_(r,m).

4. Define the actual-Xi normalized boundary quantity

       N_Xi(gamma,R) = (1/(2*pi*Xi(gamma)^2))
           integral_0^(2*pi) |Xi(gamma+R*exp(i*theta))|^2 dtheta.

   Under the additional Xi hypotheses above, N_Xi>=N_0, and

       N_Xi(gamma,R)<N_1  implies  D_1(Xi;gamma)<0.

   No actual-Xi bound N_Xi<N_1, its uniformity, positive Xi sign, central
   zero case, or higher sign is established here. Sharpness is in the
   stated neighborhood-analytic class, not an assertion about Xi or the
   subclass of entire functions. This is an independently replayed local classical
   specialization, not a proof or disproof of RH or a novelty claim.

## Proof

### Imported tools and why a specialization is needed

Use the usual Hilbert projection/minimum-norm principle. Primary coverage
is G. J. Groenewald, S. ter Horst and H. J. Woerdeman, *Optimal
interpolation in Hardy and Bergman spaces: a reproducing kernel Banach
space approach*, [arXiv:2412.11473v1](https://arxiv.org/pdf/2412.11473v1),
16 December 2024, Lemma 2.15 and Theorem 2.16 (PDF pp.9--10), the H2
boundary norm/kernel in Section 4.1 (p.13), and the Hilbert matrix formula
(5.5) (p.27). Theorem 2.16 uses distinct point evaluations, so it is not
invoked as a theorem about confluent constraints. The derivative-kernel
and independence tools are in Trieu Le, *Inner functions in weighted
Hardy spaces*, [arXiv:1912.05715v1](https://arxiv.org/pdf/1912.05715v1),
12 December 2019, Sections 3.1--3.2 and Proposition 3.6 (PDF pp.11--12),
specialized to all weights one. These supply the linear projection tools;
neither source is cited as stating the nonlinear sign threshold here.

In this symmetric two-root setting an explicit finite factor reduces the
problem to orthogonal Taylor coefficients, so no confluent inverse matrix
or coalescing-node limit is needed. We compute that reduction and the
remaining scalar constrained minimum. This is the identified nonlinear
specialization of the prior assessment; it does not reprove general
Hardy interpolation theory.

### Exact factorization and the jet

The only poles of B are at +/-i/r, outside the closed disk, and its only
zeros there are +/-ir, each of order m. On |z|=1,

    |z^2+q|^2=1+q^2+2*q*Re(z^2)=|1+q*z^2|^2,

so |B(z)|=1. For any admissible f put h=b*f/B. Division at the two
designated zeros is removable; h is holomorphic on a neighborhood of
the closed disk, real symmetric, and h(0)=1. Moreover

    h(ir)!=0 and h(-ir)!=0,                               (1)
    N(f)=b^(-2)*N(h).                                    (2)

Conversely any such h with (1) gives an admissible f=B*h/b. If necessary
shrink the neighborhood to avoid the two poles of B; they are a positive
distance from the closed disk. Other zeros of f remain unrestricted.

Expand h=1+u*z+v*z^2+sum_(k>=3) a_k*z^k with real coefficients.
Analyticity on a neighborhood of the compact closed disk gives a Taylor
radius strictly greater than one. The series converges absolutely and
uniformly on the unit circle. Orthogonality of exp(i*k*theta), first for
partial sums and then by uniform convergence, gives

    b^2*N(f)=1+u^2+v^2+sum_(k>=3) a_k^2.                 (3)

This argument justifies the boundary integral and does not interchange
an unbounded family or a merely pointwise convergent series.
The finite factor has expansion

    B(z)/b = ((1+z^2/q)/(1+q*z^2))^m
           =1+c*z^2+O(z^4).

Consequently f'(0)=u, f''(0)=2*(v+c), and

    D_1(f;0)=u^2-2*v-2*c.                                (4)

In particular no factorial or modulus-square substitution enters the
definition of D_1. The nonlinear condition is imposed after retaining
real coefficients; no symmetry averaging is used.

### The two minima and all equality cases

Equation (3) implies N(f)>=b^(-2), with equality exactly when h=1.
This h satisfies (1), and (4) gives -2c, proving the first claim.

For D_1>=0 put x=u^2>=0. Equation (4) requires v<=x/2-c.
For fixed x the least possible v^2 is (c-x/2)^2 when 0<=x<=2c,
and zero when x>=2c. Thus the least possible value of u^2+v^2 is
the minimum over x>=0 of

    F(x)=x+(c-x/2)^2  for 0<=x<=2c,
         x            for x>=2c.

For 0<c<=1, on the first interval

    F(x)=c^2+(1-c)*x+x^2/4,

whose unique minimum is c^2 at x=0. On the second interval
F(x)>=2c>c^2, since 0<c<=1. The minimizing v is -c.
For c>1, on the first interval

    F(x)=2c-1+(x-2*(c-1))^2/4.

The unique minimizing x=2*(c-1) lies strictly between 0 and 2c;
the minimizing v=-1. On the second interval F(x)>=2c>2c-1.
At c=1 the first computation still gives x=0 and v=-1 uniquely.
Finally (3) requires every a_k=0 for equality. This proves the stated
list of possible minimizing h and the lower bound N>=N_1.

Every listed minimizer satisfies the exact-order condition. If c<=1,
h(ir)=1+c*q>0. If c>1,

    h(ir)=1+q+i*u*r,

has positive real part, and h(-ir) is its conjugate. These are polynomials,
so the resulting rational f extends across the closed disk. They have
D_1=0 by (4). Thus the lower bound is a true attained minimum in the
exact class, not just an infimum for relaxed multiplicities. Since
phi(c)>0, the sign-forcing interval has positive length for every allowed
r and m.

### Exact norms, strict signs, and budget endpoints

For every N>=N_0 take

    h(z)=1+t*z^3,  t=sqrt(b^2*N-1)>=0.

Then N(B*h/b)=N by (3), D_1=-2c by (4), and h(ir)=1-i*t*r^3
has real part one, so exact order is retained. This also verifies that
the entire interval [N_0,N_1) is populated.

For zero defect let h_* be any minimizer above. For every N>=N_1 set

    h(z)=h_*(z)+t*z^4,  t=sqrt(b^2*(N-N_1))>=0.

Orthogonality gives exact squared norm N and (4) still gives zero.
Writing a=min(c,1), the real part at ir is 1+a*q+t*q^2>0.
Thus (1) holds, including when t=0.

For a positive defect, fix N>N_1 and set

    epsilon=sqrt(a^2+b^2*(N-N_1))-a>0,
    h(z)=h_*(z)-epsilon*z^2.

The z^2 coefficient of h_* is -a. The norm increases by
b^(-2)*(2*a*epsilon+epsilon^2)=N-N_1, while (4) gives
D_1=2*epsilon>0. The real part of h(ir) is 1+(a+epsilon)*q>0.
Conversely no positive-defect member can have N<=N_1: the lower bound
for nonnegative defect gives N>=N_1, and all equality cases at N_1
have zero defect. All examples remain neighborhood analytic with exact
prescribed order. The upper-budget and exact-norm assertions follow,
with no vacuous claim for K<N_0.

### Conditional actual-Xi interpretation

L018 gives that Xi is entire and real symmetric with real values on the
real axis. Under the additional hypotheses set

    f(z)=Xi(gamma+R*z)/Xi(gamma).

This f belongs to A_(r,m) with r=d/R: normalization is legitimate because
Xi(gamma)!=0, and affine substitution preserves the designated exact
multiplicities. Its squared boundary norm is N_Xi. Direct differentiation
gives

    D_1(f;0)=(R^2/Xi(gamma)^2)*D_1(Xi;gamma).

The prefactor is positive, so the sufficient strict inequality transfers
exactly. The convention agrees with the coefficient of y^2 in
f(iy)f(-iy). This application does not use L463's conditional tail
positivity, any zero-free manuscript, or L474's aggregate estimate.
None supplies the missing upper bound N_Xi<N_1. A central real zero
would invalidate this normalization and is not covered. Sharpness
examples in the wider analytic class do not imply possible Xi signs.

### Independent bounded audit, 31 October 2026

Reconstructed the displayed factorization, norm identity and scalar
minimum without assuming their conclusions. The removable quotient is
analytic on some neighborhood of the whole closed disk, since the only
zeros of B in it are the prescribed ones and its poles have modulus
1/r>1. Real symmetry makes u,v and every a_k real. The coefficient of
z^2 in B/b is m(q^(-1)-q), hence the second derivative is 2(v+c).
The two completed-square expressions for F include x=0, x=2c and c=1;
their second-interval minima exceed the claimed minima strictly. Thus
there are no omitted equality cases and no nonzero tail at equality.

Independently substituting the three exact-norm families gives norm
increments t^2, t^2 and 2*a*epsilon+epsilon^2 in N(h), respectively,
and defects -2c, 0 and 2*epsilon. Their values at ir have real parts
1, 1+a*q+t*q^2 and 1+(a+epsilon)*q, respectively. Each is positive,
so no endpoint or arbitrarily large norm in these families loses exact
multiplicity. The first family covers N=N_0, the second covers N=N_1,
and the third requires and realizes precisely N>N_1. This verifies
nonempty budgets and both strict endpoint exclusions, not merely their
infima. Every f constructed is rational with all poles outside the disk.

Finally L018 supplies exactly the entire and real-symmetry inputs used
by the conditional normalization. Affine rescaling multiplies D_1 by
R^2/Xi(gamma)^2>0, including when Xi(gamma)<0. No additional input from
L463 is used: its displayed coefficient convention at n=1 is the same
f'(0)^2-f(0)f''(0). The audit found no defect in the stated analytic
class. It validates only the conditional tool; no actual-Xi upper bound,
entire-class sharpness or global sign inference has been added.

## Mathlib

Full matching theorem and supporting coverage not checked; availability
is unknown, not asserted absent. The full result combines a finite
inner factor, Taylor/Parseval orthogonality, a scalar quadratic minimum,
exact-multiplicity nonvanishing and endpoint constructions. General
Hilbert projection or Hardy-space support would not alone establish
the nonlinear threshold. [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
