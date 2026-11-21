# Lemma 718: exact gamma size interpolation and the direct Rice obstruction

## Hypotheses

Use L714's audited coefficients and exact signed K_n, for the original
fixed L703 profile. In particular

    U=121/64, A=27/10, d=5/4, u=(3+4i)/10,
    alpha=d+c_0=11/8, n=12q+3, q>=1, N=n-1,
    b_(n,j)=(-1)^j*n^N/[j!*(N-j)!]
                         *product_(k=1)^N (U-j*k/n^2),
    D_n=d*product_(k=1)^N (d+u*k/n)/(U*u+d*k/n),
    K_n=(n/A)*D_n*sum_(j=0)^N
       b_(n,j)*B_n(d+u*j/n)/(alpha+u*j/n).

Here B_n(a)=integral chi(v)exp(-n*a*v/A)dv, with its integral on
the positive real bump. This same nonnegative chi is supported in
I=[omega-delta,omega+delta], is one on the middle half of I, and
0<delta<1/3000. Its support is bounded away from zero: L703's
c_*>1/8 and w< c_* give omega-delta=2*pi*(c_*-w)>0.
No nonreal evaluation of chi or endpoint flattening law is allowed.

Use principal Log(nu) on Re(nu)>0 and the principal constant
Log(u/d). Put a=d/u, b=U*u/d, and define

    D(nu)=d*exp((nu-1)*Log(u/d))
       *Gamma(nu*(a+1))*Gamma(1+nu*b)
       /[Gamma(1+nu*a)*Gamma(nu*(b+1))],
    B(nu,s)=integral_I chi(v)*exp(-(nu*d+u*s)*v/A)dv,
    T_nu(s)=(s/nu)^(nu-1)
       *Gamma(U*nu^2/s)/Gamma(U*nu^2/s-nu+1),       s!=0,
    c_0(nu)=(U*nu)^(nu-1)/Gamma(nu),
    c_j(nu)=(-1)^j*T_nu(j)/[Gamma(j+1)*Gamma(nu-j)], j>=1.

For positive real j, the power in T_nu(j) means
exp((nu-1)*(log(j)-Log(nu))). When s is continued elsewhere,
its power is specified on a local branch. The symbol c_0(nu) is
an interpolation coefficient, distinct from the fixed resolvent
constant c_0=1/8; no formula below interchanges these meanings.

## Conclusion

1. The original size series sum_(q>=1) K_(12q+3)*z^q is holomorphic
   at least on |z|<48^(-12). This is a crude convergence bound, not
   a located singularity or a comparison with the actual residue.

2. At integer n, on a positively oriented finite contour C enclosing
   exactly 0,...,n-1 and excluding -alpha*n/u,

       K_n=-(n*D_n/A)/(2*pi*i) * integral_C
          [Gamma(-s)/Gamma(n-s)]*T_n(s)
                             *B(n,s)/(alpha+u*s/n) ds.       (1)

   Here T_n is its polynomial extension at zero. For every real
   noninteger nu>1, the continued integrand instead has infinitely
   many genuine poles at s_m=-U*nu^2/m accumulating at zero.
   Thus the direct gamma continuation does not satisfy the analytic
   coefficient-function hypothesis of the finite Rice contour.

3. Isolating zero and allowing all positive integer coefficient indices
   does give an exact holomorphic interpolation on Re(nu)>0:

       Ktilde(nu)=(nu/A)*D(nu)*sum_(j>=0)
                        c_j(nu)*B(nu,j)/(alpha+u*j/nu).      (2)

   The series and its interchange with the real bump integral converge
   absolutely, locally uniformly in nu. For every integer n>=2 the
   tail j>=n is zero and (2) is the exact finite L714 expression;
   in particular it agrees at every required n=12q+3.

4. This interpolation continues meromorphically across
   nu_0=8i/11, with a genuine simple pole there. Equivalently
   Phi(q)=Ktilde(12q+3) has a pole at q_0=-1/4+2i/33.
   This is a pole in the interpolated size, not in the variable z
   of the ordinary generating function. It can be removed by adding
   a function zero at every positive integer q, without changing
   any K_(12q+3) or the proved holomorphy on Re(q)>0.

No Lindelof growth bound, finite z-singularity, signed exponential rate
or comparison with P_n is established. In particular no singularity
inside exp(-12*r_P) is certified; the audit of L714 (6) is separate.
The obstruction is to this direct finite-contour continuation, not to
all Rice, regularization or size-generating-function methods. This is
an unaudited, family-specific calculation using standard gamma tools,
not a new general interpolation theorem or certified originality.
Complementary spatial defect, other response terms, amplitude/full
charge, H/support, realization and Xi signs remain unresolved.

## Proof

### 1. Imported tools and the exact finite contour

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-03-signed-bump-size-generating-function.md`.
P. Flajolet and R. Sedgewick, *Mellin transforms and asymptotics:
Finite differences and Rice's integrals*, Theoret. Comput. Sci.
144 (1995), 101--124, [Section 2, Lemma 1 and its residue proof,
pp.104--105](https://algo.inria.fr/flajolet/Publications/FlSe95.pdf#page=4),
supplies the finite-contour template and its analyticity requirement.
Its fixed-function unbounded-contour theorems are not applied.

The standard Euler gamma function is meromorphic with simple poles
at -m of residue (-1)^m/m! and has entire reciprocal, as recorded in
[DLMF 5.2(i)](https://dlmf.nist.gov/5.2#i). Use the gamma recurrence
[DLMF 5.5.1](https://dlmf.nist.gov/5.5#E1) and the sectorial Stirling
expansion [DLMF 5.11.1--5.11.3](https://dlmf.nist.gov/5.11#i).
The latter two inputs and their sector restrictions were already
assessed in `drafts/literature/2026-11-03-signed-bump-remainder-rate.md`.
Only bounded shifts in a positive-real large argument are used below;
no growing-shift gamma asymptotic is imported. The local residue,
power branches and compact-uniform estimates below are the necessary
specialization to this array. We also use the standard Weierstrass
locally-uniform convergence theorem for holomorphic functions.

For integer n, recurrence gives the meromorphic identity

    T_n(s)=(s/n)^N*product_(k=1)^N (U*n^2/s-k)
          =n^N*product_(k=1)^N (U-s*k/n^2).                (3)

It is a polynomial, including at zero. Also recurrence gives
D(n)=D_n and c_0(n)=b_(n,0). The gamma kernel in (1) has residue
(-1)^(j+1)/[j!*Gamma(n-j)] at j=0,...,n-1 and no other poles:
Gamma(-s)/Gamma(n-s) is the reciprocal of
(-s)(1-s)...(n-1-s). B(n,s) is entire by compact support and
differentiation under the real integral on compact parameter sets.
A small contour about [0,n-1] excludes the resolvent pole, which
has negative real part. Substitution of (3) and the residues proves
(1), including its minus sign and the j=0 coefficient. This verifies
the cited finite Rice specialization; it makes no size continuation.

For later comparison the original generating germ does exist. For
0<=t<=1,

    |(d+u*t)/(U*u+d*t)| <= (d+|u|)/(U*Re(u))=1120/363<4.

Thus |D_n|<=d*4^N. All U-j*k/n^2 are positive and at most U for
the retained indices. Consequently

    sum_j |b_(n,j)| <= (n*U)^N*2^N/N! <= e^n*(2*U)^N,

where n^N/N!<=e^n follows from one term of the exponential series.
Moreover |B_n(d+u*j/n)|<=||chi||_1 and
|alpha+u*j/n|>=alpha. Since U<2 and e<3,

    |K_n| <= [d*||chi||_1/(A*alpha)]*n*(16*e)^n
            < [d*||chi||_1/(A*alpha)]*n*48^n.             (4)

The q-series therefore converges absolutely and locally uniformly
for |z|<48^(-12). This upper bound cannot locate its boundary.

### 2. Noninteger coefficient poles cannot be ignored

Fix a real noninteger nu>1. At s_m=-U*nu^2/m, m>=1, the argument
U*nu^2/s of the numerator gamma function is -m and its derivative
is -m^2/(U*nu^2), which is nonzero. The denominator gamma argument
is -m-nu+1, not an integer, so it is finite and nonzero. On every
local power branch at s_m the power is also nonzero. Hence T_nu
has a simple pole at each s_m, all accumulating at zero.

The other factors in the attempted version of (1) cannot cancel
all these poles. At s_m<0, Gamma(-s_m) and Gamma(nu-s_m) are
finite and strictly positive. Further,

    B(nu,s_m) -> B(nu,0)>0,
    alpha+u*s_m/nu -> alpha!=0.

The first strict inequality follows from chi>=0 and its nonempty
plateau. Thus every sufficiently large m is a genuine pole of the
full continued integrand. A holomorphic coefficient function on a
neighborhood of the retained interval, including zero, is impossible.
Every contour interior containing zero contains some of these poles;
the finite residue calculation cannot silently retain only the
nonnegative integer residues. A power branch cut at zero would be
another issue, not a way of removing these local poles.

This argument applies at noninteger real sizes arbitrarily close to
every permitted n. It disproves the needed domain assertion for this
direct gamma continuation. It does not exclude contours that omit
zero, add explicit cut terms, or use a different representation.

### 3. A genuine convergent workaround, with its unproved growth

For Re(nu)>0 all c_j(nu) are holomorphic. In the numerator gamma
factor U*nu^2/j cannot be a nonpositive integer: nu^2 cannot be
negative real or zero in that half-plane. Reciprocal gamma factors
are entire. The stated branches of the powers are holomorphic.
Likewise D(nu) is holomorphic and nonzero: a,b,a+1,b+1 all have
positive real part, so the possible gamma poles at nu=-m/(a+1),
-(m+1)/b, -(m+1)/a or -m/(b+1) are outside Re(nu)>0.
Finally alpha*nu+u*j has positive real part there.

Here is a compact-uniform coefficient bound, including compact sets
that contain integer nu. For sufficiently large j, recurrence gives

    (-1)^j/[Gamma(j+1)*Gamma(nu-j)]
      =Gamma(j+1-nu)
         /[Gamma(j+1)*Gamma(nu)*Gamma(1-nu)].             (5)

The identity is meromorphic and holds at integers by continuation.
For a compact E in Re(nu)>0 the fixed-shift specialization of Stirling
in a sector about the positive real axis gives, uniformly on E,

    Gamma(j+1-nu)/Gamma(j+1)=j^(-nu)*(1+O_E(1/j)).

This also follows by subtracting the two sectorial log expansions:
Log(j+1-nu)=log(j)+(1-nu)/j+O_E(j^(-2)); the remaining Stirling
remainders are O_E(1/j). No shift grows with j. With x=U*nu^2/j,
the gamma recurrence at zero and the entire reciprocal give

    Gamma(x)=j/(U*nu^2)+O_E(1),
    1/Gamma(1-nu+x)=1/Gamma(1-nu)+O_E(1/j).

Combining these additive, uniform estimates with (5) proves

    c_j(nu)=C(nu)+O_E(1/j),
    C(nu)=nu^(-nu-1)/[U*Gamma(nu)*Gamma(1-nu)^2].         (6)

In particular the c_j are uniformly bounded on E. Formula (6) is
not a relative estimate at an integer, where C(nu)=0; the additive
form is essential. For j large,

    |1/(alpha+u*j/nu)|
       <= max_E|nu|/[alpha*min_E Re(nu)+Re(u)*j].

Let v_-=omega-delta>0. The absolute summands in the real bump
integral for (2) are bounded, uniformly on E, by a constant times

    chi(v)*exp(-Re(u)*j*v_-/A)/(1+j).

This is summable and integrable. Absolute Fubini, local uniform
convergence and the stated holomorphic convergence theorem prove
(2)'s analyticity and the permitted interchange. At integer n,
T_n(j) is the finite polynomial (3); for j>=n the reciprocal
Gamma(n-j) is zero, so c_j(n)=0. For j<n it is exactly b_(n,j).
Thus (2) has proved integer agreement, rather than merely formal
agreement of an asymptotic expansion.

These are estimates on fixed compact sets of sizes. They do not
bound Phi(q)=Ktilde(12q+3) as |q| tends to infinity. Theorem 2 of
P. Flajolet, S. Gerhold and B. Salvy, *Lindelof representations and
(non-)holonomic sequences*, [arXiv:0906.1957v2, 17 December 2009,
pp.5--6](https://arxiv.org/pdf/0906.1957v2#page=5), additionally
requires |Phi(q)|<=C*exp(a_*|q|) on Re(q)>=1/2 for some a_*<pi.
No such estimate, including the factor 12, has been proved here.
Its analytic continuation conclusion would still not locate the
desired finite singularity. The source's Lemma 1, p.7, uses left
interpolation poles in an expansion at infinity, not as finite
generating-variable singularities.

### 4. A real interpolation pole that is not a size-series locator

The preceding series continues meromorphically to a neighborhood of
nu_0=i/sqrt(U)=8i/11. Indeed Log(nu) has a local branch there
agreeing with the right half-plane. For j>=2 the numerator gamma
argument at nu_0 is -1/j, not a pole; for j=1 it is -1, a simple
pole. The c_0(nu) term is holomorphic there. The proof of (6) is
uniform also on a sufficiently small closed disk about nu_0 that
avoids zero. For large j the resolvent denominator is bounded
below by Re(u)*j-alpha*max|nu|; the finitely many remaining
denominators are nonzero at nu_0. Thus the sum of all j!=1 terms
is holomorphic on a smaller disk.

For completeness D is finite and nonzero there. Its four gamma
arguments, in numerator then denominator order, are

    16/11+20i/11,   14/25+33i/100,
    27/11+12i/11,   -11/25+1163i/1100.

None is a nonpositive integer. The residue of c_1 at nu_0 is

    r_1=(1/nu_0)^(nu_0-1)
             /[2*U*nu_0*Gamma(nu_0-1)*Gamma(-nu_0)]!=0. (7)

The two minus signs, from (-1)^1 and the residue of Gamma at -1,
cancel; the derivative of U*nu^2 is 2*U*nu_0. Also

    alpha+u/nu_0=77/40-33i/80!=0,
    B(nu_0,1)=integral_I chi(v)*exp(-v/9)*exp(-16i*v/33)dv.

Multiplication of this last integral by exp(16i*omega/33) gives
strictly positive real part: it is at least

    cos(16*delta/33)*integral_I chi(v)*exp(-v/9)dv>0.

The narrow support and positive plateau justify this assertion
without any endpoint law or oscillatory asymptotic. Therefore

    Res_(nu=nu_0) Ktilde(nu)
       =(nu_0/A)*D(nu_0)*r_1*B(nu_0,1)/(alpha+u/nu_0)!=0. (8)

Only j=1 has a pole here, so the holomorphic remainder cannot
cancel it. This proves the genuine simple interpolation pole.

Write r_q for (8) divided by 12 and q_0=(nu_0-3)/12. The function

    J(q)=r_q*sin(pi*q)/[sin(pi*q_0)*(q-q_0)]

vanishes at every positive integer, is holomorphic on Re(q)>0,
and has residue r_q at q_0. Hence Phi-J agrees with exactly the
same K_(12q+3) and removes this pole. This does not assert that J
preserves an additional Lindelof growth class; no such class has
been established. It proves that the interpolation pole, under
the properties actually proved here, is not an invariant
singularity of the coefficient sequence's ordinary generating
germ. A genuine finite z-obstruction is still missing.

## Mathlib

Full matching coverage of this exact array interpolation, compact
convergence and Rice-domain obstruction has not been checked.
The imported gamma, residue and holomorphic-convergence facts are
supporting mathematics, not a claimed matching Mathlib theorem.
No inference of absence or completed formal verification is made.
