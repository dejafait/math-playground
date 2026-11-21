# Corollary 466j: actual-H chamber crossing violates the minimum principle

## Hypotheses

Use C466a's normalized probability density p=theta_1 and
h(s)=xi(1/2+sqrt(s))/xi(1/2), with Laplace transform 1/h(s),
and B(s)=log h(s), B(0)=0. Use only C466b's scalar actual-H
properties: H is C^1 on (0,infinity), H>0, H'<0,
integral_0^infinity H(t)dt<infinity, and

    B'(s)=integral_0^infinity exp(-st)H(t)dt,   s>0.       (1)

These retain C466a/b's L018 normalization, strip/symmetry, paired-product,
zero-counting and finite verified-zero source qualifications. They are
cited external inputs, not independently replayed here. No contact,
cofactor, nonzero kappa, complete monotonicity of H, RH, or PF premise
is assumed. In particular C466b's hypothetical contact hypotheses are
not required for this result.

Let mu_tau be the subordinator laws with Laplace transform
exp(-tau B(s)), as justified below. For two independent copies use
the backward convention

    T_tau G(x)=integral G(x1+u,x2+v) mu_tau(du)mu_tau(dv).

Put W={(x1,x2):x1<x2}. For f in C_c^infinity(W), let Ef equal f
on W, -f(x2,x1) on x1>x2, and zero on the collision line.
Only smooth tests supported away from that line will be used.

## Conclusion

There is an explicit nonnegative f in C_c^infinity(W) with f(z)=0
at z=(0,1) such that Ef is in C_c^infinity(R^2), hence in the
full-space generator domain, and

    A(Ef)(z)
      =-exp(-1) integral_(7/4)^(9/4) eta(4(t-2)) H(t)dt/t
      <=-(2/17)exp(-7/3)H(17/8)<0,                       (2)

where eta(u)=exp(-1/(1-u^2)) for |u|<1 and eta(u)=0 otherwise.
Consequently (T_tau Ef)(z)<0 for all sufficiently small tau>0.
The restriction of this independent-particle evolution to the
antisymmetric chamber representation does not preserve its full
nonnegative cone and fails its necessary positive minimum principle.

This stops unrestricted chamber-cone propagation. It does not rule out
a smaller cone with separately proved actual-law constraints, prove a
negative transition-density minor at tau=1, or refute any finite PF
claim about p. It supplies no actual contact, all-tau smooth density,
all-degree density sign, or implication resolving L030-L032/C032a.
This is an ordinary specialization of standard generator theorems;
no mathematical originality is claimed. The bounded independent replay
is recorded below; the inherited external scalar inputs remain citations.

## Proof

### Scalar measure, normalization and compensation

Define nu(dt)=H(t)dt/t on (0,infinity). The complete integrability check is

    integral min(1,t) nu(dt)
      =integral_0^1 H(t)dt+integral_1^infinity H(t)dt/t
      <=integral_0^infinity H(t)dt<infinity.             (3)

Also integral t nu(dt)=integral H<infinity, and
integral min(1,t^2)nu(dt)<infinity follows from (3). There is no
assumption that nu itself has finite mass near zero.

The identity B(0)=0 and continuity there follow from h(0)=1.
Integrate (1) from epsilon to s and let epsilon decrease to zero.
Tonelli for the nonnegative integrand, followed by monotone convergence,
gives

    B(s)=integral_0^infinity (1-exp(-st)) nu(dt), s>=0.  (4)

Its finiteness also follows directly from (3). Thus the Bernstein
parameters are killing a=0 and finite-variation drift b=0. Import
R. L. Schilling, R. Song and Z. Vondracek, *Bernstein Functions:
Theory and Applications*, De Gruyter, first edition (2010),
Theorem 3.2, p15, and Theorem 5.2 with Definition 5.4, pp35-36
([edition-specific book text](https://dokumen.pub/bernstein-functions-theory-and-applications-9783110215311-9783110215304.html)).
The first gives the unique Bernstein representation; the latter give
the convolution semigroup and subordinator convention. Because B(0)=0,
the laws have mass one, with no killing. At tau=1 their Laplace transform
is 1/h, so uniqueness of Laplace transforms identifies mu_1 with
p(u)du, not the non-unit normalization Theta=p/xi(1/2).
No regularity of mu_tau for other tau is used.

In the characteristic convention E exp(i xi S_tau), (4) gives exponent
tau integral(exp(i xi t)-1)nu(dt). The integral is absolutely
convergent by (3). This is the standard subordinator convention in the
cited construction. In the compensated convention with cutoff t<1,
write it as

    i xi d+integral (exp(i xi t)-1-i xi t 1_(t<1))nu(dt),
    d=integral_0^1 t nu(dt)=integral_0^1 H(t)dt.         (5)

Thus the compensated drift is d, although the drift b in (4) is zero;
the Gaussian coefficient is zero. Dropping d while keeping compensation
would describe a different process.

Independence makes the joint characteristic exponent the sum of the
two scalar exponents. Its Levy measure is the sum of the pushforwards
of nu under t->(t,0) and t->(0,t), its Gaussian matrix is zero, and
its compensated drift vector is (d,d). In particular there is no
additional simultaneous two-coordinate jump measure. The Euclidean
cutoff |y|<1 on these axes is exactly t<1.

Import R. L. Schilling, *An Introduction to Levy and Feller Processes*,
[arXiv:1603.00251v2](https://arxiv.org/pdf/1603.00251v2),
Lemma 6.3, pp37-38, and Theorem 6.8, p39, equation (6.8).
These put every G in C_c^infinity(R^2) in the full-space generator
domain and give, with the preceding parameters,

    AG(x)=d(partial_1 G+partial_2 G)(x)
      +sum_(i=1)^2 integral_0^infinity
        [G(x+t e_i)-G(x)-t partial_i G(x)1_(t<1)]nu(dt)
      =sum_(i=1)^2 integral_0^infinity
        [G(x+t e_i)-G(x)]nu(dt).                       (6)

The last equality cancels the finite compensation integrals using (5).
For t<1 the uncompensated difference is bounded by
t sup|partial_i G|, and for t>=1 by 2 sup|G|; (3) proves absolute
convergence. Taylor's theorem bounds the compensated integrand near
zero by a constant times t^2. Thus both forms of (6) are valid, without
a hidden principal value or a finite-jump-rate assumption. This is an
applicability calculation, not a reproof of either general theorem.

### A smooth test and every coordinate-jump contribution

Define on R^2

    F(x1,x2)=eta(4(x1-1))eta(4(x2-2)),
    f=F restricted to W,
    G(x1,x2)=F(x1,x2)-F(x2,x1).

The standard bump eta is smooth including at |u|=1: every interior
derivative is its exponential times a rational function with only
finite-order endpoint poles, and the exponential dominates every such
pole, so all endpoint derivatives tend to zero. Hence F is smooth.
Its support lies in [3/4,5/4] times [7/4,9/4], whose coordinate gap
is at least 1/2. Thus f is nonnegative, compactly supported in W,
and G is exactly Ef, smooth and compactly supported on the full space.
At z=(0,1) it vanishes on a neighborhood; all its local derivatives
and its value there are zero. Lemma 6.3 applies without any assertion
about a chamber generator core or boundary regularity of its domain.

For the first coordinate, for every t>0,

    G(z+t e_1)=G(t,1)
      =eta(4(t-1))eta(-4)-eta(0)eta(4(t-2))
      =-exp(-1)eta(4(t-2)).                            (7)

This vanishes for t<=1 (before or at collision), for 1<t<=7/4,
and for t>=9/4; it is negative precisely on 7/4<t<9/4.
All nonzero terms are jumps past the other particle. At the endpoints
the bump vanishes. In contrast, for the second coordinate and all t>0,

    G(z+t e_2)=G(0,1+t)
      =eta(-4)eta(4(t-1))-eta(4t)eta(-8)=0.           (8)

Equations (7)-(8) account for both whole positive jump axes. The
subtracted G(z), both compensation derivatives, drift and Gaussian
terms are zero as well. Substitution into either version of (6)
proves the equality in (2). Its integral is over a compact interval
away from zero, where H/t is positive and continuous.

On [15/8,17/8], |4(t-2)|<=1/2, so eta(4(t-2))>=exp(-4/3).
Also H(t)>=H(17/8)>0 by monotonicity, and 1/t>=8/17.
That interval has length 1/4. Keeping just its positive integral
inside the negative expression proves the bound in (2), including
its strict sign. The achieved threshold is strictly below zero, the
opposite of the nonnegative generator value required at this minimum.

### Consequence and exact scope of the stop

By the generator-domain assertion,
(T_tau G-G)/tau converges in the C_0 norm to AG as tau decreases
to zero. Evaluating at z with G(z)=0 and (2) gives T_tau G(z)<0
for all sufficiently small positive tau. Identical independent laws
also make T_tau commute with coordinate exchange, so it maps
antisymmetric functions to antisymmetric functions. Its restriction
to W therefore is the relevant antisymmetric evolution; its failure
of cone preservation follows from this single f>=0.

For comparison only, the smooth zero extension of f is F, not G.
Both F(z+t e_1) and F(z+t e_2) vanish for every t>0, and F is zero
near z, so AF(z)=0. This illustrates the lost crossing term. It is
not an identification of the antisymmetric evolution with a killed
process, or a claim about the domain of a killed generator.

The sign proof uses the actual positive jump density, with no possible
uncounted positive jump contribution for this test. It does not show
that this test belongs to any specially constrained actual-density
orbit. Small positive tau is not tau=1, and no negative minor at the
latter time follows. Higher-order signs, initial/boundary control and
the Xi interface remain unresolved. The known general generator
results are imported precisely; only this scoped specialization is
added to the notebook. The source comparison and duplicate/failure
review are reused from assessment920 and comparison919/completion920.

### Independent bounded replay — 14 November 2026, step924

The audit used the unchanged assessment922, separately approved in
step923, and the inspected theorem records in comparison919/completion920
and review921. It checked the full proof above, not just its displayed
negative integral. No failed premise was found within this scope.

In particular, (1) is used only with the scalar C466a/b hypotheses;
neither a contact nor C466i enters the argument. The integral of H
controls both ranges in (3), as well as the finite first moment of nu.
Integrating B' from epsilon to s gives the integrand
exp(-epsilon*t)-exp(-s*t); as epsilon decreases to zero this increases
to 1-exp(-s*t). B(epsilon) tends to zero by h(0)=1. This verifies (4)
without an exchange of a signed or divergent integral. The parameters
a=b=0 are in the Bernstein convention; d=integral_0^1 H is the
nonzero compensated drift. Its cancellation in (6) is exact. The
independent two-coordinate law has only the two axis measures, and
Schilling's Euclidean cutoff agrees with the scalar cutoff on each.
The cited full-space domain theorem therefore applies in dimension two.

The support rectangle of F has distance from collision bounded below
by its coordinate gap 1/2, so antisymmetric extension introduces no
boundary singularity. At (0,1), both F and its transpose vanish on a
neighborhood. The first entire jump ray gives precisely the transposed
bump with a minus sign, since eta(-4)=0 and eta(0)=exp(-1).
The second entire ray vanishes because its two terms contain eta(-4)
and eta(-8), respectively. These statements include all jumps after
collision, not just small jumps. Thus there is no omitted positive
axis contribution and no remaining local term.

For the quantitative check, 4(t-2) lies in [-1/2,1/2] on
[15/8,17/8], whose length is (17-15)/8=1/4. The factors in the
positive integral are bounded below by exp(-4/3), H(17/8), and
8/17. Multiplying by exp(-1) gives exactly
(1/4)(8/17)exp(-1-4/3)H(17/8)
=(2/17)exp(-7/3)H(17/8)>0. The preceding minus sign reverses the
inequality, as stated in (2).

Finally, norm convergence in the full-space generator definition
implies pointwise convergence of T_tau G(z)/tau to this strictly
negative number because G(z)=0. It yields negativity for every
sufficiently small positive tau, without a density assumption at those
times. Exchange symmetry justifies restriction to antisymmetric
functions, but supplies no propagation of that negative value to
tau=1. The audited conclusion is failure of the unrestricted chamber
cone only. Actual time-one minors, smaller invariant cones, global
PF and the Xi interface remain unresolved. The scalar external
counting and verified-zero certificates were not independently audited.

## Mathlib

Full matching coverage of the subordinator construction, compensated
generator-domain theorem, antisymmetric chamber test and minimum-
principle failure has not been checked. No formalization or absence
claim is made. The cited analytic theorems, not a Mathlib homepage
or merely supporting differentiation facts, are the imported inputs.
