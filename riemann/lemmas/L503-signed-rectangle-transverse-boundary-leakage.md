# Lemma 503: signed rectangle transverse boundary leakage

## Hypotheses

Fix R>0. For real T sufficiently large set

    L=log T, a=log L/pi, b=a/4, B=L/(4pi),
    lambda=pi/(2a), beta=lambda*b=pi/8, sigma=2pi R,
    K(x)=1-(sin(pi x)/(pi x))^2, K(0)=0.

Let f be even entire and real on R, with

    f(z)=integral_R phi(v) exp(2pi i v z) dv,
    phi in C_c^infinity(R), supp phi subset [-R,R],
    Re f(x+iy)>=1 for |x|<=a and b<|y|<B.             (H)

There is no sign restriction elsewhere and no uniform bound on the
derivatives of phi. Write

    u(x,y)=Re f(x+iy), N=integral_R |f(x)| dx,
    M=integral_R |f(x)| K(x) dx,
    F(y)=integral_{-a}^a u(x,y) cos(lambda x) dx,
    P(y)=u(a,y)+u(-a,y),
    Q=-integral_0^b exp(-lambda y) P(y) dy.             (1)

For explicit constants define

    eta_R=1/(8R+2), k_R=inf_{|x|>=eta_R} K(x), A_R=2/k_R,
    S_R(y)=sinh(sigma y)/(pi y) for y>0, S_R(0)=2R,
    C_0=(1+coth(beta))/2, h=2b, H=(B+h)/2,
    epsilon_R(L)=4 C_0 exp(-lambda h) S_R(h)
                 /[lambda (exp(lambda(B-h))-1)],
    D_L=(2/lambda)(exp(-beta)-exp(-lambda H)),
    q_R(L)=4 exp(sigma b)/(pi sigma b).                 (2)

The finite inequalities below require L>1 and B>h. All sufficiently
large L meet these conditions. No local lemma, zeta estimate, actual-zero
positivity or zero-spacing assumption is used.

The supporting standard input is Fourier inversion on Schwartz functions.
For Green's identity the approved source is S. Axler, P. Bourdon and
W. Ramey, *Harmonic Function Theory*, second edition, author PDF dated
17 July 2020, (1.1)/(1.2), printed p. 4,
[primary PDF](https://axler.net/HFT.pdf#page=12). Its smooth-domain
statement motivates the identity; the rectangle formula, including its
corners and every face, is justified by one-dimensional integration by
parts below. The weighted norm conversion below is an elementary
specialization for this single isolated weight zero, not a reproof of
the general Logvinenko--Sereda theorem in the source assessment.

## Conclusion

Both N and M are finite, 0<k_R<=1, and N<=A_R M. The full first-mode
balance gives the necessary signed side-gap estimate

    Q >= D_L-(1+epsilon_R(L))N
      >= D_L-A_R(1+epsilon_R(L))M,                     (3)

while the unconditional Fourier norm estimate gives

    |Q| <= q_R(L) N.                                  (4)

Consequently

    M >= D_L/[A_R(1+epsilon_R(L)+q_R(L))].             (5)

Here epsilon_R(L)=O_R(L^R exp(-pi L/(8 log L))) tends to zero,
and D_L=(2 exp(-beta)/lambda)(1-exp(-pi L/(16 log L))).
In particular, for all sufficiently large L, uniformly in f,

    M >= c_R (log L)^2 L^(-R/2),
    c_R=R exp(-beta)/(8pi A_R)>0.                     (6)

Thus a family with M<=C log L L^(-c), for fixed R,C,c>0, must have
c<R/2. This excludes the endpoint c=R/2 as well as larger c. It does
not exclude any positive c<R/2, prove existence, or give the sought
nonvanishing cost lower bound.

For every such hypothetical small-cost family, (3) requires

    liminf_{T->infinity} [lambda exp(beta) Q/2] >= 1.   (7)

In particular the weighted integral of the negative part of P in
0<y<b is at least (1-o(1))2 exp(-beta)/lambda. This is a necessary
negative side leakage of order a, not an available construction or an
upper bound on that leakage. A positive upper horizontal flux only
strengthens (3); the adverse part is quantitatively retained below.

This is the local result of one bounded boundary test. It has not had
a separate critical audit. The existing source comparison did not
identify this exact combination; no originality claim is made. There
is no consequence here for weighted actual-zero counts, moving-test
errors, individual Xi signs, or RH.

## Proof

### Real-axis integrability and the zero of K

Repeated integrations by parts in the compactly supported smooth
Fourier integral show that f restricted to R is Schwartz. All boundary
terms vanish, including when the support reaches +/-R, because phi is
globally smooth and zero outside its support. Thus N is finite and,
as 0<=K<=1, so is M. Fourier inversion with the stated 2pi convention
gives phi(v)=integral_R f(x) exp(-2pi i v x) dx, whence |phi(v)|<=N.
In particular |f(x)|<=2R N for real x.

The inequality |sin t|<|t| for t!=0 shows K(x)>0 for x!=0.
Continuity on the compact set eta_R<=|x|<=1 and the bound
K(x)>=1-1/pi^2 for |x|>=1 show k_R>0. Also K<=1. Since

    integral_{|x|<eta_R} |f(x)| dx
       <=4R eta_R N <=N/2,

we obtain M>=k_R N/2 and hence N<=A_R M. The constants depend only
on the fixed R, not on T, f or Fourier derivative bounds. No sign of f
on the real axis is used.

For y>=0 the same bound on phi yields

    |f(x+iy)| <= N integral_{-R}^R exp(-2pi v y) dv
               =N S_R(y).                            (8)

The formula at y=0 is its continuous limit. All differentiations in
finite x,y rectangles are justified directly by compact Fourier support.

### Projection and all four faces

Put psi(x)=cos(lambda x). Then psi>=0 on [-a,a], psi(+/-a)=0,
psi'(a)=-lambda and psi'(-a)=lambda. Since u is harmonic,
two ordinary integrations by parts give

    F''(y)=-integral_{-a}^a u_xx psi dx
           =lambda^2 F(y)-lambda P(y).                (9)

There is no omitted side derivative: the u_x psi terms vanish at
both endpoints because psi is zero there; the remaining u psi'
terms produce precisely -lambda P. Define

    J(y)=exp(-lambda y)(F'(y)+lambda F(y)).

For any finite 0<=s<t, (9) implies

    J(t)-J(s)=-lambda integral_s^t exp(-lambda y)P(y)dy. (10)

Equivalently apply the two integrations by parts to the harmonic test
v(x,y)=psi(x)exp(-lambda y) on [-a,a] times [s,t]. In Green's form
integral_boundary (u D_n v-v D_n u), the top contribution is -J(t),
the bottom contribution J(s), and the two vertical contributions sum
to -lambda integral_s^t exp(-lambda y)P(y)dy. On a vertical face
v D_n u is exactly zero, while D_n v=-lambda exp(-lambda y) on
both faces. On the horizontal faces both value and normal-derivative
terms occur in J. This direct rectangular calculation needs no
smooth-corner limit and omits no derivative term.

Reality of f on R implies f'(x) is real there, so u_y(x,0)=0 and
F'(0)=0. Also |F(0)|<=N. Continuity from (H), at fixed x including
the vertical endpoints, gives u>=1 on the closed rectangle
[-a,a] times [b,B]. Consequently

    F(y)>=integral_{-a}^a psi dx=2/lambda,
    P(y)>=2                         (b<=y<=B).        (11)

Neither inequality is extended into the gap 0<=y<b. The lower
rectangle is compatible by the given reality/evenness symmetries;
only the upper rectangle and the real-axis derivative are needed.

### The adverse upper flux is small

The exact solution of (9), for b<=s<=t<=B, is

    F(t)=F(s)cosh(lambda(t-s))
         +F'(s)sinh(lambda(t-s))/lambda
         -integral_s^t sinh(lambda(t-y))P(y)dy.        (12)

Solving backwards from h to b gives

    F(b)=F(h)cosh(lambda(h-b))
         -F'(h)sinh(lambda(h-b))/lambda
         -integral_b^h sinh(lambda(y-b))P(y)dy.

Because F(b)>=0 and the last integral is nonnegative, and h-b=b,

    F'(h)<=lambda coth(beta)F(h).                    (13)

Apply (12) from h to H and again drop only its nonnegative subtracted
integral. For w=lambda(H-h)>=0,
cosh w+coth(beta)sinh w<=C_0 exp(w). Thus

    F(H)<=C_0 exp(lambda(H-h))F(h).                   (14)

Applying (12) from H to B and using F(B)>=0 gives, with d=B-H>0,

    F'(H)>=-lambda coth(lambda d)F(H).

It follows that

    J(H)/lambda
      >=-[coth(lambda d)-1]exp(-lambda H)F(H)
      >=-2 C_0 exp(-lambda h)F(h)
          /[exp(lambda(B-h))-1]
      >=-epsilon_R(L) N.                             (15)

The second inequality uses (14), F(H)>=0 and
2d=B-h; the last uses F(h)<=2N S_R(h)/lambda from (8).
This estimates only the possible negative part of the top flux.
An arbitrarily large positive value of J(H) is retained as favorable
in the lower bound; no small absolute upper-flux claim is needed.

The constants in (2) are explicit. Indeed lambda h=pi/4,
sigma h=R log L and

    lambda(B-h)=pi L/(8 log L)-pi/4,
    epsilon_R(L)=16 C_0 exp(-pi/4) sinh(R log L)
       /[pi^2 (exp(pi L/(8 log L)-pi/4)-1)].           (16)

This proves its asserted asymptotic for fixed R, since
L/(log L)^2 tends to infinity. There is no uniform assertion for
R growing with T.

### The necessary signed leakage and its available upper bound

Set s=0 and t=H in (10) and use F'(0)=0. Splitting only at b gives
the exact identity

    F(0)+Q = integral_b^H exp(-lambda y)P(y)dy
             +J(H)/lambda.                          (17)

The integral on the right is at least D_L by (11). Equations (15),
(17) and F(0)<=N imply (3). The value of D_L in the conclusion follows
from lambda H=beta+pi L/(16 log L).

There is also a completely unconditional estimate for the gap term.
By (8) and exp(-lambda y)<=1,

    |Q|<=2N integral_0^b S_R(y)dy.                   (18)

For 0<=y<=b/2, S_R(y)<=2R exp(sigma y), so the integral over this
part is at most exp(sigma b/2)/pi. For b/2<=y<=b,

    S_R(y)<=exp(sigma y)/(2pi y)
           <=exp(sigma y)/(pi b),

and its integral is at most exp(sigma b)/(pi sigma b).
The elementary inequality x exp(-x/2)<=2/e<1 for x>0 shows that
the first bound is also at most exp(sigma b)/(pi sigma b).
Substitution into (18) proves (4). This bounds the complete signed
gap term in absolute value; it does not assume its sign or discard
one face. Combining (3) with Q<=|Q| proves (5).

### Threshold comparison and limitations

For each fixed R, choose L large enough that B>h,
exp(-pi L/(16 log L))<=1/2, epsilon_R(L)<=1 and q_R(L)>=2.
Such an onset exists because R>0 is fixed. Then D_L>=exp(-beta)/lambda
and 1+epsilon_R(L)+q_R(L)<=2q_R(L). Hence (5) gives

    M>=pi sigma b exp(-beta)/(8 lambda A_R) exp(-sigma b)
      =sigma a b exp(-beta)/(4 A_R) exp(-sigma b)
      =c_R (log L)^2 L^(-R/2),

as claimed. Against the desired upper bound C log L L^(-c), the
ratio of this lower bound to that upper bound is

    (c_R/C)(log L)L^(c-R/2).

It tends to infinity if c>=R/2, and to zero if 0<c<R/2.
The latter fact is only compatibility with this necessary bound, not
evidence that a detector exists. In particular (6) tends to zero and
does not achieve the nonvanishing target for any fixed R>0.

Finally divide (3) by 2exp(-beta)/lambda and substitute
N<=A_R C log L L^(-c). Since lambda log L=pi^2/2, the error from
N is O_{R,C}(L^(-c)), and epsilon_R(L)->0. This proves (7).
The negative part of P has weighted integral at least Q because
Q is its integral minus the corresponding positive-part integral.
No estimate here improves (4) to O_R(a M) under (H). Such a bound
would be new required information, not a consequence of this proof.

## Mathlib

Full coverage of this weighted signed-rectangle statement has not been
checked. Fourier inversion, elementary harmonic integration by parts
and hyperbolic-function identities are standard supporting facts;
no matching Mathlib theorem name is asserted. Unknown coverage is not
evidence of absence. All finite-rectangle and weight specializations
used for this result are proved above.
