# Lemma 488: Polymath's common real/simple tail on compact positive times

## Hypotheses

Let F(lambda,z) be the exact theta heat family of L058, with kernel K
as in L019 and the Xi normalization of L018. Fix real numbers
0<a<=b<=1/8. This result uses the named external asymptotic and strip
theorems identified below; their underlying saddle estimates are not
independently reproved here. No RH or assumption t>Lambda is made.

## Conclusion

There is an absolute existential constant C_*>0 such that, with

    R(a) = (1/2) exp(C_*/(4a)),

every zero of F(lambda,z) with a<=lambda<=b and |Re z|>=R(a) is real
and simple. All nonreal or multiple zeros on this interval therefore
lie in |Re z|<R(a), |Im z|<=1/2. Each fixed slice has finitely many
such zeros. No numerical value for C_* or R(a) is asserted.

This is a restricted specialization and proof replay of a known theorem,
not progress beyond the published tail result. It supplies neither
exclusion of finite collisions nor a bound uniform as a decreases to
zero. No claim for lambda>1/8 or all-height reality is included.

## Proof

### Precise source inputs and audit scope

D. H. J. Polymath, *Effective approximation of heat flow evolution of
the Riemann xi function, and a new upper bound for the de Bruijn–Newman
constant*, Research in the Mathematical Sciences 6 (2019), article 31,
[arXiv:1904.12438v2, 4 August 2019](https://arxiv.org/html/1904.12438v2)
([versioned PDF](https://arxiv.org/pdf/1904.12438v2)). Theorem 1.5(i)–(ii),
pp.9–10, is the result being specialized. Its convention immediately
after part (iv) makes all implied constants absolute, independent of t.
The proof replay below accepts Proposition 9.1(i), pp.56–58, and
Lemma 9.2, pp.58–59, and checks the subsequent localization/count on
pp.59–60, equations (102)–(104). It is not a full-manuscript audit.

In source notation

    H_t(z) = integral_0^infinity exp(tu^2) Phi(u) cos(zu) du,
    Phi(u) = sum_{k>=1} (2pi^2 k^4 exp(9u)-3pi k^2 exp(5u))
                         exp(-pi k^2 exp(4u)).

The nonvanishing comparison function is M_t(s)=exp(t alpha(s)^2/4)M_0(s),
where alpha=M_0'/M_0 and M_0 is source (6); its domain is
C minus (-infinity,1]. Equations (6)–(10) show that M_t is holomorphic,
nonvanishing and respects conjugation for real t. Only values far
from its branch cut occur below.

Proposition 9.1(i) states that for 0<t<=1/2, |y|<=10, x>=200 and
x>=exp(C_0/t),

    H_t(x+iy) = (1+O(x^(-kappa_0 t))) M_t((1+y-ix)/2)
              +(1+O(x^(-kappa_0 t))) M_t((1-y+ix)/2),           (1)

with absolute C_0,kappa_0>0. Lemma 9.2 gives, for any fixed bounded
neighborhood x+iy=X+O(1) of a sufficiently large real X,

    M_t((1+y+ix)/2)
      = M_t((1+iX)/2)
        exp((i(x-X)+y)(A_X+i beta)+O(log X/X)),
    A_X = (1/4)log(X/(4pi)),       beta=pi/8,                  (2)

and a continuous phase

    arg M_t((1+iX)/2)
      = (t pi/16)log(X/(4pi)) + 7pi/8
        +(X/4)log(X/(4pi))-X/4+O(log X/X).                    (3)

Here the bounded neighborhood will always have radius at most two;
all constants can consequently be fixed once, uniformly in t.

We also accept N. C. de Bruijn, *The roots of trigonometric integrals*,
Duke Math. J. 17 (1950), 197–226, Theorem 13, in the form restated as
Polymath Theorem 3.2: if H_(t0) has no zero with Im z>y0>0, then for
t>t0 it has no zero with Im z>sqrt(max(y0^2-2(t-t0),0)).
The source's H_0(z)=xi(1/2+iz/2)/8 and L018 give the initial strip
|Im z|<=1. Conjugation and this theorem therefore give |Im z|<=1
for every zero at 0<t<=1/2. The original 1950 proof is not audited.

The reproof of the small-circle step is warranted because source (104)
displays O(|y| log x_n+x_n^(-ct)), which alone has no strict comparison
margin on a circle of radius c/log x_n. We retain the exact holomorphic
factor in (102) instead. No stronger saddle estimate is required.

### Phase centers and a holomorphic comparison

Define the source phase function

    g(X,t)=X/(4pi) log(X/(4pi))-X/(4pi)+11/8
           +(t/16)log(X/(4pi)).

For every sufficiently large integer n let X=x_n(t)>4pi satisfy
g(X,t)=n. Such a center is unique, since

    g_X(X,t)=(1/(4pi))log(X/(4pi))+t/(16X)>0.

Put M=M_t((1+iX)/2), A=A_X and w=z-X=u+iy. By (3),

    arg M=pi(n-1/2)+O(log X/X),
    conjugate(M)=-M exp(eta_0),       |eta_0|<=K log X/X,      (4)

where eta_0 may be chosen purely imaginary. Indeed conjugate(M)/M
is exp(-2i arg M), so this conclusion retains equality of moduli.

Choose once 0<kappa<=min(kappa_0,1), and write

    E(X,t)=X^(-kappa t)+log X/X.

Combining (1), (2), conjugation and (4), for |w|<=2 and sufficiently
large X>=exp(C_x/t), gives

    H_t(X+w)=M exp(-beta w)
       [-exp(-iAw)(1+d_-(w))+exp(iAw)(1+d_+(w))],
    |d_-(w)|+|d_+(w)|<=K E(X,t).                            (5)

To verify the common factor, the first exponent in source (102) is
(-iu+y)(A-i beta)=-iAw-beta w, and the second is
(iu-y)(A+i beta)=iAw-beta w. Thus exp(-beta w), rather than just
exp(-beta u), is retained exactly. The errors in (1) are relative to
their respective summands; (2) has exponential errors O(log X/X),
and exp(v)=1+O(v) for bounded small v. Also x=X+u is comparable to X.
Increasing C_x above C_0 ensures x>=exp(C_0/t) throughout |w|<=2.
These observations justify (5) with absolute constants.

In particular the holomorphic function

    Q(w)=H_t(X+w)/(2i M exp(-beta w))

satisfies

    |Q(w)-sin(Aw)|
      <=K_1 E(X,t)(|exp(iAw)|+|exp(-iAw)|).                  (6)

No holomorphy of a selected pointwise d_+ or d_- is assumed or needed:
Q-sin(Aw) itself is holomorphic. Its denominator is nowhere zero.
Since t<=1/2 and kappa<=1, log X/X<=K_0 X^(-kappa t) for X large.
Consequently E(X,t)<=K_2 exp(-kappa C_x) on X>=exp(C_x/t).
All fixed smallness requirements below can be met by increasing C_x.

### Strict circle count, including multiplicity

Fix an absolute number 0<d<=1/8 and use the circle |w|=d/log X.
For large X,

    1/8 <= A/log X <= 1/4,
    d/8 <= |Aw| <= d/4.

For complex q with |q|<=1/4, the sine series gives
|sin q-q|<=|q|^3 exp(|q|)/6<|q|/2; the bound follows by comparing
the absolute remainder to sum_{j>=3}|q|^j/j!.
Thus |sin(Aw)|>=d/16 on the circle. In (6) the two exponentials
have moduli at most exp(d/4). Increase C_x so that

    2 K_1 exp(d/4) E(X,t) < d/32.                           (7)

This is a strict Rouche comparison. The function sin(Aw) has exactly
one zero in the disk, the simple zero w=0, since its other zeros are
the nonzero integer multiples of pi/A. Rouche's theorem counts one
zero of Q, hence H_t, WITH MULTIPLICITY. There are no boundary zeros.
Conjugation preserves this disk and the zero set, so its unique zero
is real. Its multiplicity is one. This does not rely on part (i) of
the source theorem and therefore avoids a circular reality inference.

The same argument works for the source proof's circle d/log n:
for sufficiently large X, X<=g(X,t)<=X^2 uniformly in 0<t<=1/2.
Hence log X<=log n<=2log X, and the lower bound above becomes
|sin(Aw)|>=d/32. Decrease the strict error allowance accordingly.
Both circle conventions have the required multiplicity-one count.

### Exhaustion of all high zeros

Let z=x+iy be any zero at sufficiently large x, and choose a nearest
phase center X=x_n(t) in real distance. The global strip gives |y|<=1.
We verify the phase restriction implicit in source (i), not just an
O(1) restriction on Au.

Uniformly at large X, g_X is comparable to log X. On [X-1,X+1]
its integral over either unit interval is greater than one, so the
neighboring centers lie in that interval. The mean value theorem first
gives their distances O(1/log X). On this smaller interval,

    g_X(v,t)=A/pi+O(1/X).

Another mean value application therefore gives each neighbor distance
(pi/A)(1+O(1/(X log X))). Since X is nearest, x lies between the two
midpoints to its neighbors. For sufficiently large X this proves

    |Au| <= 3pi/4,       |u|=O(1/log X),       X=x+O(1/log x). (8)

At the zero, use (1)–(2) before replacing conjugate(M) by -M.
The two summands have the common factor exp(-beta w), equal base
moduli |M|, and respective factors exp(-iAw+eta_-) and
exp(iAw+eta_+), where |eta_-|+|eta_+|<=K E(X,t). Such logarithms of
the relative errors exist because the errors have modulus below 1/2.
Equality of the two summand moduli gives

    Ay+Re eta_- = -Ay+Re eta_+,      |Ay|<=K E(X,t).          (9)

Thus (6), now evaluated at this zero, has bounded exponential factors
and implies |sin(Au+iAy)|<=K_3 E(X,t). For real v,s,

    |sin(v+is)|^2=sin^2 v+sinh^2 s.

On |v|<=3pi/4, concavity of sine on [0,3pi/4] gives
|sin v|>=(2sqrt(2)/(3pi))|v|, while |sinh s|>=|s|.
Together with (8), these bounds prove

    |z-X| <= K_4 E(X,t)/A <= K_5 E(X,t)/log X.               (10)

Increase C_x once more so K_5 E(X,t)<d. Then the zero lies strictly
inside the already counted disk. It is therefore real and simple.
This proves complete exhaustion, not merely a statement about a
selected sequence or a density-one collection. It also recovers the
source's weaker O(x^(-ct)) localization, since (10) is stronger.

### Coupled thresholds and compact time

Here is an explicit order of choices avoiding a hidden x/n assumption.
First fix all constants in (1)–(10), including C_x. On all sufficiently
large X the elementary inequalities X<=g(X,t)<=X^2 hold uniformly:
divide the displayed formula for g by X and by X^2, using t<=1/2.
Choose an absolute C_n>2(C_x+1). If n>=exp(C_n/t), then
X>=sqrt(n)>=exp(C_n/(2t)), so the count and its entire disk satisfy
the required x-threshold, after absorbing fixed small-X restrictions.

Conversely, take an absolute C_*>C_n+1, also large enough for those
fixed restrictions. For any zero with x>=exp(C_*/t), the nearest
center obeys X>=x/2 by (8). Hence

    X >= (1/2)exp(C_*/t) >= exp(C_n/t),
    n=g(X,t)>=X>=exp(C_n/t).

The second inequality in the first line uses t<=1/2 and C_*-C_n>1.
Thus every zero in this larger x-tail is eligible for both the disk
count and the source's n-threshold. Enlarging an absolute constant
here changes no quantifier. The inequalities and strict boundary
comparison hold at threshold equality as well.

Finally L019's kernel gives K(2u)=4 Phi(u), term by term. In L058's
absolutely convergent defining integral, substitute the variable 2u:

    F(lambda,z)=8 H_(4lambda)(2z).                           (11)

This also agrees at lambda=0 with L018 and source (1). Multiplication
by 8 and the nonzero linear substitution 2z preserve zero multiplicity.
For a<=lambda<=b put t=4lambda. Then 4a<=t<=4b<=1/2 and

    exp(C_*/(4a)) >= exp(C_*/t).

Thus Re z>=R(a) is in the common source tail. Evenness of F, supplied
by L058, reflects the assertion to Re z<=-R(a), preserving simplicity.
The strip scales to |Im z|<=1/2. On a fixed slice, all remaining zeros
are in a compact rectangle and are finite, since F(lambda,0)>0 by L058
and isolated zeros of a nonzero entire function cannot accumulate there.
This proves the conclusion.

### Qualifications and verification

The designated audit passes using (102)–(103), not a strict comparison
inferred from the coarse printed (104). The latter estimate is not
claimed false; it is simply insufficient alone for its following count.
Checked analytically: the complex exponential factor, absolute error
margin, multiplicity, nearest-center phase interval, whole-strip
exhaustion, n/x thresholds, reflection and closed compact-time endpoints.
No numerical script or numerical certificate is relevant to these checks.

The common tail removes the escape-to-infinity obstacle only for nonreal
or multiple zeros on the stated compact positive-time interval. L126's
general quantifier warning and L128's finite-domain limitations remain
valid. No global Dini-sign claim or finite-collision exclusion has been
derived here. The underlying asymptotic theorems remain cited inputs.
The local replay passed the separate independent audit below on
2026-10-30. The underlying source proofs remain accepted imports.

### Separate independent critical audit — 2026-10-30

This audit accepts precisely Proposition 9.1(i), Lemma 9.2 and the cited
de Bruijn strip theorem, rather than accepting the conclusion of
Theorem 1.5 as a premise of the replay. The primary statements, (6)–(10),
(26) and (102)–(104) agree with the transcriptions above. Constants are
absolute in the source's convention. No additional asymptotic hypothesis
or assumption of all-real zeros is needed for the following checks.

For w=u+iy, one has -iu+y=-iw and iu-y=iw. Multiplication by A-i beta
and A+i beta, respectively, gives -iAw-beta w and iAw-beta w. Thus both
summands share the same nowhere-zero holomorphic factor, including its
imaginary part. Equation (4) contributes only a small phase error.
If the two relative errors have modulus bounded by K E, dividing by
2i M exp(-beta w) gives (6) by the triangle inequality. It is immaterial
whether the chosen error representatives are holomorphic: the difference
of Q and sin(Aw) is holomorphic on a neighborhood of the closed disk.
The points used by M_t stay away from its branch cut.

On |w|=d/log X, |Aw| lies in [d/8,d/4]. The absolutely convergent sine
series gives the stated remainder bound and hence |sin(Aw)|>=d/16.
The comparison error is strictly less than d/32 after (7); the ratio
is less than 1/2, not just bounded by an unspecified constant.
Since d/4<pi, no other sine zero lies in the disk. Rouché counts one
zero with multiplicity and none on the boundary. Conjugation then
forces reality, and count one forces simplicity. The alternate radius
d/log n only halves the lower bound and requires a smaller fixed error
allowance. Neither argument uses prior reality of the selected zero.

For exhaustion, the phase geometry is independent of the asymptotic
zero formula: g is increasing and unbounded, and its derivative exceeds
one on every sufficiently high unit interval, uniformly in t. Bracketing
a sufficiently high x between consecutive centers therefore first puts
its nearest center at distance at most one, so X is itself large.
The two mean-value estimates in (8) then apply without having assumed
the n-threshold. They put x in the nearest center's midpoint interval
and give |Au|<=3pi/4, including a midpoint tie. At any zero the two
nonzero summands have equal modulus. Small relative errors admit
logarithms, so (9) follows before any estimate of the sine at that zero.
It bounds exp(±Ay) uniformly. Now (6), the exact sine-modulus identity
and the lower bound for real sine on [-3pi/4,3pi/4] give
A|w|<=C E. Choosing K_5 E<d places this arbitrary zero strictly inside
the disk already counted. This covers the whole strip, not only zeros
chosen initially near a phase center.

For clarity, all fixed large-X restrictions can be imposed before the
coupled thresholds. Choose a uniform X_0 beyond them and with g(X,t)<=X^2
and g(X,t)>=X for X>=X_0. Enlarge C_x for the strict errors, x>=200,
the source bound throughout |w|<=2, and exp(2C_x)>=X_0+2. Choose C_n
with C_n>2(C_x+1) and exp(2C_n)>sup_{0<=t<=1/2}g(X_0,t). This supremum
is finite from the explicit formula for g. Thus n>=exp(C_n/t) first
forces X>X_0 by monotonicity, and only then is n<=X^2 used to obtain
X>=exp(C_n/(2t)). There is no inference from an inequality outside its
large-X range. Finally choose C_*>C_n+1 large enough for the elementary
nearest-center geometry at x>=exp(C_*/t). That geometry gives X>=x/2;
the margin C_*-C_n>1 and t<=1/2 give X>=exp(C_n/t). Hence n>=X is in
the required index tail. Constants used to establish the geometry do
not depend on C_n or C_*. All earlier strict inequalities remain strict
when x or n equals its lower threshold.

The termwise kernel identity K(2u)=4 Phi(u) and L058's absolute
convergence justify (11), including its factor 8. The changes t=4lambda,
z_source=2z preserve multiplicity and give exactly the stated R(a).
Evenness handles the negative tail. The strip and the nonzero entire
slice justify finiteness of the remaining exceptional zeros. The closed
time endpoints, including b=1/8, are within the accepted source range.

Verdict: the replay and restricted specialization pass, with no changed
mathematical conclusion or failed comparison found. The expanded order
of choices above makes explicit the small-X exclusion already required
by the proof. This independently verifies the retained local input for
L489; it is reproduction of the cited tail theorem, not an improvement
beyond it. The saddle estimates and original strip proof remain
unaudited, C_* remains nonnumerical, and no finite collision or zero-time
limit is excluded. No numerical calculation is used as evidence.

## Mathlib

Full matching coverage has not been checked. No claim of absence is made.
Rouche's theorem, the argument principle, conjugation and isolated-zero
arguments are standard supporting mathematics; no particular Mathlib
declaration is asserted to formalize this source theorem or specialization.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
