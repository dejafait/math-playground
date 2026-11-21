# Corollary C029h: verified-height reciprocal zero budget

## Hypotheses

Use L018's actual completion xi and C028b's exact normalization

    gamma_0>0, b_0=1, b_j>0,
    F(u)=sum_(j>=0) b_j u^j/j!=xi(1/2+sqrt(u))/gamma_0.

The square-root notation denotes the even entire series. Use C028g's
audited multiplicity-counted functional and limit

    S_F=sum_(F(w)=0) |Im(1/w)|<infinity,   H_d/d -> S_F.

All entire-function zeros have their analytic multiplicities. Import
the unconditional finite verification and unconditional ordinate-sum
theorem specified below. Set T=3*10^12 exactly. No RH, simplicity,
nonvanishing at ordinate T, effective degree onset or zero value for
S_F is assumed. The published finite computation is an input, not
independently rerun here.

## Conclusion

The approved fixed bound holds, with the stronger certified estimate

    0<=S_F<3*10^(-25)<10^(-23).

Consequently C028g gives lim_(d->infinity) H_d/d<3*10^(-25).
This is a reproduction/specialization of known verified-height and
weighted-zero-sum results, not a new zero-counting theorem or a proof
of RH. S_F=0, H_d=o(d), finite-degree signs and full signed-complement
payment remain unproved. This specialization passed independent
audit1974 below under the stated imported-input contracts.

## Proof

### Precise imported results

David J. Platt and Timothy S. Trudgian, *The Riemann hypothesis is
true up to 3 times 10^12*, Bull. London Math. Soc. 53 (2021), 792-797,
[arXiv:2004.09765v1, Theorem 1 and Section 2, PDF pp.2-3](https://arxiv.org/pdf/2004.09765v1),
verify the critical-line location of the full nontrivial-zero divisor
through the required height. Section 2 reports verified height
H=3,000,175,332,800>T. We use only that every nontrivial zero with
0<Im(rho)<=T has Re(rho)=1/2. The strict margin H>T also covers
an ordinate exactly T. The verification counts the full divisor, not
just a list of line zeros. No simplicity conclusion is needed.

Richard P. Brent, David J. Platt and Timothy S. Trudgian,
*Accurate estimation of sums over zeros of the Riemann zeta-function*,
Math. Comp. 90 (2021), 2923-2935,
[DOI 10.1090/mcom/3652](https://doi.org/10.1090/mcom/3652),
[arXiv:2009.13791v1, Theorem 1, PDF p.2; definitions, Lemmas 1/3 and Section 4, PDF pp.4-9](https://arxiv.org/pdf/2009.13791v1),
give the following unconditional infinite-tail theorem. For nonnegative
C^2 phi on [T_0,infinity), with phi'<=0, phi''>=0,
2*pi<=T_0<=T and integral_T^infinity phi(t)log(t/(2*pi))dt finite,

    sum'_(gamma>=T) phi(gamma)
      = (1/(2*pi)) integral_T^infinity phi(t)log(t/(2*pi))dt
          -phi(T)Q(T)+E_2(T),
    |E_2(T)|<=2(A_0+A_1 log T)|phi'(T)|
                  +(A_1+A_2)phi(T)/T,
    A_0=2067/1000, A_1=59/1000, A_2=1/150.

Here gamma ranges over positive ordinates of every nontrivial zero,
with multiplicity, including distinct zeros sharing an ordinate. The
prime gives half weight at T and full weight above T. In this source
Q=N-L, with midpoint N at zero ordinates, and

    L(t)=t/(2*pi)*(log(t/(2*pi))-1)+7/8.

Its Lemma 1/footnote 1 supplies |Q(t)|<=0.28 log t for t>2*pi*e.
Lemma 3's endpoint case and Section 4's infinite endpoint justify the
displayed conventions and infinite sum. These statements and essential
proof cases were inspected in source-notes1971; reuse that assessment
without rederiving the theorem or silently replacing its N convention.

### The entire squared-zero divisor

Write a nontrivial zeta zero as rho=beta+i gamma and set
v=rho-1/2. L018 gives 0<beta<1 and the same multiplicity for xi.
C028b's identity is xi(1/2+v)=gamma_0 F(v^2).
There is no zero with gamma=0: if such a zero existed, v would be
real and F(v^2)>0, since its convergent series has positive
coefficients and constant term 1. This contradicts the identity.
In particular v=0 is not a zero and F(0)=1.

For any zero w of F, both square roots v,-v are nonzero and nonreal.
Indeed a real v would again give F(v^2)>0. They give the two xi
zeros 1/2+v and 1/2-v, exactly one with positive imaginary part.
Conversely every positive-ordinate zeta zero yields w=v^2. If two
such zeros gave the same w, their v values would differ only by sign;
the negative sign reverses the ordinate and so cannot give a second
positive-ordinate representative. Thus this is a bijection between
the distinct positive-ordinate zeta zeros and the distinct F zeros.

The local derivative of v->v^2 at either square root is 2v!=0.
Composition with this map preserves vanishing order, as does the
nonzero factor gamma_0. Together with L018 this proves that the
bijection preserves every multiplicity. It does not divide a positive
ordinate count by two. In particular the two upper-half-plane zeros
beta+i gamma and 1-beta+i gamma, when beta!=1/2, give conjugate
distinct F zeros; both must be counted.

Put delta=beta-1/2, so |delta|<1/2 and gamma>0. The contribution is

    w=(delta+i gamma)^2,
    |Im(1/w)|=2|delta|gamma/(gamma^2+delta^2)^2<=gamma^(-3).

The equality follows by taking the imaginary part of
(delta-i gamma)^2/(delta^2+gamma^2)^2; the bound follows from
2|delta|<=1 and (gamma^2+delta^2)^2>=gamma^4. It is zero when
delta=0. Finite verification therefore kills every term with
0<gamma<=T, including its full multiplicity at gamma=T. Reindexing
the nonnegative, convergent C028g sum by the established bijection gives

    S_F<=sum_(gamma>T) gamma^(-3)
         <=sum'_(gamma>=T) gamma^(-3).                 (1)

The second inequality adds half of the nonnegative endpoint mass;
it neither assumes that T is not an ordinate nor deletes an endpoint.
The vanishing of the original low weights and the direction of this
inequality are separate facts. No RH at heights above T is used.

### Weighted tail and exact arithmetic

Apply the imported theorem with T_0=2*pi and phi(t)=t^(-3).
This is C^2 and positive on its domain, phi'=-3t^(-4)<0 and
phi''=12t^(-5)>0. Its required integral is finite and elementary:

    integral_T^infinity t^(-3)log(t/(2*pi))dt
       = [log(T/(2*pi))+1/2]/(2T^2).

Integration by parts gives this identity, with upper endpoint zero
because t^(-2)log t tends to zero. The elementary bounds pi<4,e<3
give 2*pi*e<24<T, so the stated Q estimate applies at T, including
its midpoint convention. Taking upper signs in the theorem and (1),

    S_F <= [log(T/(2*pi))+1/2]/(4*pi*T^2)
              +(7/25)log T/T^3
              +[6(A_0+A_1 log T)+A_1+A_2]/T^4.        (2)

Here is a rational certificate for (2), without floating-point
roundoff. Archimedes' elementary bounds give 3<pi<4. The exponential
series gives e>1+1+1/2+1/6+1/24=65/24>8/3. Since

    8^10=1073741824>1062882000=18000*3^10,

we have e^30>18000^3=5832000000000>T, hence log T<30.
Also log(T/(2*pi))<log T. Therefore the three terms in (2) are
bounded above, respectively, by

    61/(24T^2),   42/(5T^3),   24/T^4,

with strict inequalities; for the last one the exact constant is
6(A_0+30A_1)+A_1+A_2=69263/3000<24.
As T>=1000,

    42/(5T)+24/T^2<=8424/1000000=1053/125000<1/24,

the last comparison being 25272<125000. Combining these bounds gives

    S_F<62/(24T^2)=31/(12T^2)
        =(31/108)*10^(-24)<3*10^(-25),

since T^2=9*10^24 and 310<324. This proves the fixed approved
threshold, with a rigorously smaller bound. No mathematical program,
polynomial root computation or effective degree limit is needed.

### Scope, duplicates and traps

C028g already establishes convergence and identifies S_F. It is an
input here, not a newly proved convergence theorem. C028f's separate
uniform polynomial tail is used through that audited limit; no
effective K is needed for this numerical entire-divisor estimate.
C029f/C029g's fixed-interval logarithmic statements and stop1966 are
contrasts only. This proof changes neither their scope nor any stopped
metric or shifted-Jensen mechanism.

The achieved estimate is a small nonnegative budget, not a zero budget.
A hypothetical very high off-line zero can have a nonzero contribution
below this fixed number. No exclusion of such a zero follows, no
finite verified height is sent to infinity, and no rate or finite-degree
sign follows from C028g's limit. The all-degree actual-Xi positivity
gap, S_F=0 and full-complement signed payment remain independent open
obligations. Repeating finite-height refinements cannot by itself close
these gaps.

### Independent application audit1974

20 November 2026, under the unchanged SPECIALIZE assessment1972.
The PT/BPT theorem statements, versions and essential endpoint proof
cases are reused from source-notes1971. This audits the application,
not the source theorems or published finite computation. The existing
C028b normalization and C028g/audit1522 full-limit theorem are inputs;
C028f/audit1518 is used through that limit and is not reaudited here.

**Whole divisor.** Positivity and convergence of F's actual series
give F(x)>=1 for real x>=0. The identity with xi therefore excludes
every real v zero, including v=0. Every F zero w is nonzero, and
its two square roots are nonreal with opposite, nonzero imaginary
parts. Exactly one has positive imaginary part. L018 turns it into
exactly one positive-ordinate nontrivial zeta zero. Conversely squaring
rho-1/2 recovers w; equality of squares permits only the two opposite
roots, so distinct positive-ordinate representatives cannot collide.
The derivative 2v is nonzero at both roots; factoring F locally as
(u-w)^m times a nonvanishing holomorphic factor shows explicitly that
F(v^2) has order m there. L018 preserves that same multiplicity.
Thus the full positive-ordinate divisor, including two distinct zeros
sharing an ordinate, is counted once each, with no factor 1/2.

**Weight and endpoint.** For real delta and gamma>0, inversion of
(delta+i gamma)^2 gives imaginary part
-2delta*gamma/(delta^2+gamma^2)^2. L018 supplies |delta|<1/2,
which bounds its modulus by gamma^(-3). At delta=0 the weight is
exactly zero. PT's verified H=3000175332800 exceeds the exact
T=3000000000000, so every original weight through T vanishes,
including any multiplicity at T. The strict ordinate sum above T
is bounded by BPT's primed sum because their difference is exactly
one half of the nonnegative ordinate mass at T. This comparison
does not assert nonvanishing at T or replace midpoint N by an
inclusive counting convention. Nonnegative sums and C028g's finite
sum justify the stated reindexing without a conditional rearrangement.

**BPT interface.** On [2pi,infinity), t^(-3) is nonnegative C^2,
its first derivative is -3t^(-4), and its second is 12t^(-5).
The tail integral is finite; integration by parts has zero upper
endpoint and gives the value in the proof. The imported midpoint
Q bound applies since 2pi*e<24<T. The absolute error term becomes
[6(A_0+A_1 log T)+A_1+A_2]/T^4, while -phi(T)Q(T)
is bounded above by (7/25)log T/T^3. These are exactly (2),
with the stated denominator powers and without a sign assumption on Q.

**Exact certificate.** Independently multiplying gives
3^10=59049 and 18000*59049=1062882000<1073741824=8^10.
The displayed exponential-series lower bound therefore proves
log T<30, without a decimal logarithm. Since pi>3 and
log(T/(2pi))<30, the main term is strictly less than 61/(24T^2).
The other two coefficients satisfy

    (7/25)*30=42/5,
    6*(2067/1000+30*59/1000)+59/1000+1/150
        =69263/3000<24.

For T>=1000 the residual after factoring T^(-2) is at most
42/5000+24/1000000=1053/125000<1/24, with the last
comparison equivalent to 25272<125000. Hence the strict bound
31/(12T^2) follows. At this T it is (31/108)*10^(-24),
strictly below 3*10^(-25) because 310<324. Every integer and
rational comparison in the original certificate passes; no threshold
or argument repair and no mathematical program were needed.

Audit result: accept the stated fixed bound and its limiting consequence
under the exact input contracts. No direct mathematical input changed.
This validates a reproduction/specialization of the cited results;
it supplies neither a result beyond those methods nor vanishing of S_F,
an effective degree rate, finite-degree signs or RH. The absolute
budget cannot exclude a hypothetical sufficiently high off-line zero.

## Mathlib

Not checked. Availability of a full matching formal theorem for this
specialization, the published finite verification or the BPT theorem
is unknown. No absence or formal verification is claimed. The general
results are imported with precise citations; the square-map interface,
multiplicity and endpoint handling and rational arithmetic are supplied
explicitly above.
