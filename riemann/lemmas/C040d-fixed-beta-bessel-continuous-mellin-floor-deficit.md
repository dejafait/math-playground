# Corollary 40d: fixed beta-Bessel continuous Mellin floor deficit

## Hypotheses

Use exactly C040c's fixed F(t)=1F2(3/2;1,100;-t^2/4) and its
normalized cosine density m(u), supported on [0,1]. In particular,
with B=B(3/2,197/2),

    p_B(s)=s^(1/2)(1-s)^(195/2)/B,  0<s<1,
    m(u)=(2/pi) integral_(u^2)^1 p_B(s)/sqrt(s-u^2) ds,  0<=u<1.

The density is zero for u>=1, nonnegative, bounded, and has mass one.
For real p>0 define

    I_F(p)=integral_0^1 u^(2p-1)m(u) du,
    G_F(p)=1/p+I_F'(p)/I_F(p)-I_F'(p+1)/I_F(p+1).

Here primes differentiate the real parameter p. Set
eta=15287777/250000000, a_0=1/20, and
Lambda=[4329/1000,4331/1000]. An admissible inverse density means
a continuous real function on [0,infinity) of exponential growth,
whose Laplace transform equals G_F(p) on a real right half-line of
absolute convergence. Requiring equality
and convergence for every p>0 is a stronger admissibility convention
and gives the same uniqueness conclusion below.

## Conclusion

The defining Mellin integrals are finite, positive and differentiable
for all p>0, and

    I_F(p)=(2 Gamma(100)/pi) Gamma(p+1)Gamma(p)
                         /[Gamma(p+199/2)Gamma(p+1/2)],          (1)
    G_F(p)=1/(p+199/2)+1/(p+1/2)-1/(p+1).                     (2)

The unique admissible continuous inverse density is

    k_F(a)=exp(-199a/2)+exp(-a/2)-exp(-a),  a>=0.             (3)

Its transform converges absolutely and equals G_F(p) for every p>0.
Uniformly for lambda in Lambda,

    -0.018260432763 <= k_F(a_0)-eta exp(-lambda a_0)
                       <= -0.018255508064 < 0.                (4)

Thus this fixed model fails the displayed quantitative lower premise
already at the prescribed a_0, for every allowed lambda. No retuning,
other sample, full source upper bound, or actual-Xi assertion is made.
This is a local specialization of beta/gamma/Laplace identities, not
a claimed new general theorem or a counterexample to RH.

## Proof

### Continuous Mellin identity and differentiation

Work directly from the nonnegative double integral defining m;
integer coefficient moments are not interpolated. Tonelli first gives,
as an identity of possibly infinite nonnegative integrals,

    I_F(p)=(2/pi) integral_0^1 p_B(s)
                 integral_0^sqrt(s) u^(2p-1)/sqrt(s-u^2) du ds.

For s>0 substitute u=sqrt(s)v. The inner integral becomes
s^(p-1/2) integral_0^1 v^(2p-1)(1-v^2)^(-1/2)dv.
Substitution w=v^2 and Euler's beta integral give

    I_F(p)= B(p,1/2)/pi * B(p+1,197/2)/B(3/2,197/2).       (5)

Precisely, import [NIST DLMF5.12.1](https://dlmf.nist.gov/5.12#E1),
whose hypotheses Re(x)>0 and Re(y)>0 hold here for (p,1/2),
(p+1,197/2), and (3/2,197/2). The v-endpoint exponents are
2p-1>-1 and -1/2>-1; the s exponents after taking its moment are
p>-1 and 195/2>-1. Hence both beta integrals are finite and positive
for every p>0, proving the same facts for I_F. On expanding the beta
ratios, Gamma(197/2) cancels and the constant is
Gamma(100)Gamma(1/2)/(pi Gamma(3/2))=2Gamma(100)/pi,
by gamma recurrence at 1/2, proving (1).
This normalization is independent of p
but the two p-dependent gamma factors in each numerator/denominator
must all be retained.

For differentiation under the original integral, take any compact
[epsilon,M] inside (0,infinity). C040c bounds m by the finite constant
C=4/(pi B). On 0<u<1, both the integrand and its p derivative are
bounded in absolute value, uniformly in p on this compact set, by

    C u^(2epsilon-1),  2C u^(2epsilon-1)|log u|,

respectively. Their integrals are C/(2epsilon) and
2C/(2epsilon)^2. Dominated differentiation gives
I_F'(p)=2 integral_0^1 u^(2p-1)log(u)m(u)du. The endpoint u=0
is a null set, with no endpoint atom. No assertion at p=0 is needed.

### Ratio and unique continuous inverse

Write ell(p)=log I_F(p). All gamma arguments in (1) are positive,
so differentiation of that identity gives

    ell'(p)=psi(p+1)+psi(p)-psi(p+199/2)-psi(p+1/2).

Import gamma/digamma recurrence
[DLMF5.5.1-2](https://dlmf.nist.gov/5.5#E2): in particular
psi(z+1)-psi(z)=1/z away from its poles. There are no such poles
at the four positive arguments above. Taking ell'(p)-ell'(p+1)
therefore gives

    -1/(p+1)-1/p+1/(p+199/2)+1/(p+1/2).

Adding 1/p proves (2), including its index shifts and signs.
For p>0, direct integration of each exponential in (3) gives (2).
Absolute convergence is justified by |k_F(a)|<=3 and
integral_0^infinity 3exp(-pa)da=3/p. The function in (3) is real,
continuous on [0,infinity), and bounded, hence of exponential growth.

Import Laplace uniqueness for continuous functions of exponential
growth from [NIST DLMF1.14(iii), equations17-19 and subsection
Uniqueness](https://dlmf.nist.gov/1.14#iii). If another admissible
density h has |h(a)|<=C_h exp(c_h a) eventually, continuity bounds
it on the remaining compact interval. Both transforms converge
absolutely on Re(p)>max(0,c_h). They agree on an eventual real half-line
inside that domain by admissibility (intersect also with the half-line
in h's transform hypothesis); equivalently their holomorphic transforms
agree on the whole half-plane by the identity theorem. The cited
uniqueness theorem gives h=k_F on [0,infinity). Continuity is essential
for pointwise equality: an arbitrary change on a null set would not
preserve this admissibility requirement. Thus a different admissible
inverse density cannot repair the failed pointwise floor at a_0.

### One exact scalar enclosure

The arithmetic certificate is
`scripts/beta-bessel/continuous-floor-1178.json`, reproduced by
`python3 scripts/beta-bessel/continuous-floor-1178.py`.
All enclosure arithmetic uses Python integer fractions. For x>=0 put
S_n(x)=sum_(j=0)^n (-x)^j/j!. Taylor's integral remainder is

    exp(-x)-S_n(x)=(-1)^(n+1)/n!
                     integral_0^x exp(-t)(x-t)^n dt.

Consequently S_41(x)<=exp(-x)<=S_40(x) for every x>=0; this does
not assume the first Taylor terms are decreasing. Evaluate only at

    199/40, 1/40, 1/20, 4329/20000, 4331/20000.

Combining the first three intervals with the signs in (3) gives

    0.030989006467 <= k_F(1/20) <= 0.030989006468.

Because eta>0 and exp(-lambda/20) decreases with lambda, the last
two endpoint enclosures give, uniformly on Lambda,

    0.049244514531 <= eta exp(-lambda/20) <= 0.049249439230.

The script subtracts the exact rational intervals before any rounding,
giving (4). The displayed decimals are outward enclosures, not inputs
to the computation; their enclosure directions are also verified by exact
rational comparison. A coarser entirely rational check, recorded in the
certificate, is -184/10000<D(lambda)<-181/10000<0. All ten checks
pass with no failures, including the required threshold sup D<0.
Every partial sum and all exact density, floor and deficit bounds
are retained in the certificate. The complete load-bearing rational
bounds and check fields were inspected at production. The independent
critical audit below subsequently verifies this arithmetic and the
analytical hypotheses.

### Critical audit and independent enclosure — step1180

The approved assessment1178 covers exactly this fixed model, a_0,
lambda interval and lower premise. No defect was found. The audit
replayed the continuous integral, rather than inferring it from integer
moments: u=sqrt(s)v contributes s^(p-1/2), so multiplication by
p_B(s) leaves s^p(1-s)^(195/2). The two beta integrals therefore
have precisely the arguments in (5). Expanding both beta factors
gives denominator Gamma(p+199/2)Gamma(p+1/2) and the constant
in (1). As a separate normalization check, p=1/2 gives

    I_F(1/2)=(2Gamma(100)/pi)Gamma(3/2)Gamma(1/2)/Gamma(100)=1,

consistent with the mass of m. The bound C u^(2epsilon-1) and its
single-log derivative bound are integrable for every epsilon>0,
including p+1 as needed. Thus the four digamma terms are legitimate.
Taking their differences at p and p+1 contributes respectively
-1/(p+1), -1/p, +1/(p+199/2), +1/(p+1/2); the explicit +1/p
cancels exactly. No p=0 endpoint or differentiation of divergent
integrals is used.

For uniqueness, continuity upgrades the eventual exponential bound on
h to a bound on the entire nonnegative axis, after changing its
constant. The transforms are holomorphic on the indicated common
right half-plane: on every compact subset, exp(-pa)h(a) and each
fixed p derivative are dominated by a polynomial in a times a
strictly decaying exponential. Equality on an eventual real half-line
has accumulation points inside that domain, so the identity theorem
applies before importing DLMF uniqueness. The candidate k_F is
continuous at a=0 as well as elsewhere. Hence the cited theorem
gives pointwise equality, not merely equality almost everywhere.
This checks the admissibility issue needed for the single-point stop.

The independent arithmetic certificate is
`scripts/beta-bessel/continuous-floor-audit-1180.json`; reproduce it
with `python3 scripts/beta-bessel/continuous-floor-audit-1180.py`.
The original producer and certificate were not overwritten or rerun.
All original parameters, five exponential endpoints, complete assembled
density/floor/deficit endpoints, displayed rational decimal bounds,
threshold and predicates were inspected. Every one of its 210 stored
Taylor terms is additionally checked by the direct formula
(-x)^j/j!, using powers and factorials instead of its recurrence.

For an independent enclosure of the same five exponentials, put

    P_64(x)=sum_(j=0)^64 x^j/j!,
    T_65(x)=x^65/65!,  r(x)=x/66,
    R(x)=T_65(x)/(1-r(x)).

All five fixed arguments satisfy 0<x<=199/40<66. The positive
exponential series has first omitted term T_65; each ratio after
that term is x/(j+1)<=x/66<1 for j>=65. Its entire omitted tail
is consequently at most R by comparison with a geometric series.
Thus P_64<=exp(x)<=P_64+R, with strictly positive endpoints, and

    1/(P_64+R)<=exp(-x)<=1/P_64.

All quantities in these inequalities are exact rationals except the
enclosed exponential. Reciprocation reverses the endpoints. The
certificate verifies that each new interval lies inside the producer's
S_41/S_40 interval; those original bounds are separately reproduced
from all 42 terms, without any alternating-series monotonicity premise.
Combining the intervals with the signs in (3), positive eta and the
decrease of exp(-lambda/20) gives (4). Both exact deficit endpoints
are inspected in full in the audit certificate. All original ten
predicates are recomputed rather than trusted, and the displayed
outward decimal directions are checked by rational comparison.
All 52 audit checks pass with no failures. In particular the new
interval also satisfies

    -184/10000 < D(lambda) < -181/10000 < 0,

and is contained in the displayed interval (4), uniformly on Lambda.
This is independent verification of a local known-method specialization,
not a new general transform theorem or an actual-Xi sign. The fixed
compatibility route is closed without any new sample or retuning.

### Scope relative to the source premise and central gap

Kawano, *Logarithmic Inequalities of Arbitrary Order for the Riemann
Xi Coefficients*, [Preprints.org202611.0383v1, posted4November2026](https://www.preprints.org/manuscript/202611.0383),
Theorem1.2/(5)-(9), supplies the comparison premise
k(a)>=eta exp(-lambda a), with precisely the constants above.
It is an unrefereed preprint. No truth of its actual-theta theorem,
specified zero of J, upper envelope, or numerical certificates is
imported or independently verified here. This result compares only
the explicitly stipulated lower premise to C040c's fixed model.
Known general transform identities are imported; (5), its full
normalization, the rational ratio and the scalar enclosure are the
necessary model specialization under assessment1177.

C040c's qualitative counterexample remains intact. Since it fails
this additional necessary hypothesis, it supplies no counterexample
to a bridge that assumes that hypothesis as well. Conversely, (4)
does not prove such a bridge, does not establish the floor for actual
theta, and does not produce any actual-Xi logarithmic Hankel sign.
The all-polynomial positivity of L030-L032/C032a remains unresolved.
The named results there explain relevance and are not mathematical
inputs to this density calculation. No zero or RH-equivalent sign
was assumed in deriving (1)-(4).

## Mathlib

Full matching coverage is not checked; availability remains unknown.
No Lean proof or matching theorem is asserted. Beta/gamma recurrence
and continuous Laplace uniqueness are imported from the precise
references above, rather than attributed to an uninspected Mathlib
result. The exact rational certificate verifies arithmetic only;
the analytical identity and uniqueness are justified in this proof.
