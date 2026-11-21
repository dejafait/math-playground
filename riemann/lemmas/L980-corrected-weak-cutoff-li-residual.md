# Lemma 980: corrected weak-cutoff arithmetic Li residual

## Hypotheses

Use the actual nontrivial zeta zeros of L018, with all orders, and
L013's exclusion of real nontrivial zeros. For integers n>=2 set

    G_n(s)=1-(1-1/s)^n,
    T=sqrt(n),
    H_n=lambda_n(T)=sum_(rho: |Im rho|<=T) G_n(rho).

The finite sum includes every zero at the cutoff with its full order.
Use L977's ordinary, undivided arithmetic convention

    -zeta'(1+s)/zeta(1+s)-1/s=sum_(j>=0) eta_j s^j,
    S_f(n)=sum_(j=1)^n binom(n,j) eta_(j-1).

The Laurent expansion is local at zero. No RH, simple-zero condition,
zero-avoiding cutoff, finite zero table or Li sign is assumed.

## Conclusion

For one finite constant C depending only on the fixed zeta function,

    |S_f(n)+lambda_n(sqrt(n))|<=C*sqrt(n)*log n,    n>=2. (1)

This is the corrected plus-sign residual with a weak cutoff. It is
a standard specialization/assembly of the cited smooth and arithmetic
identities and L978-L979, classified REPRODUCTION. It supplies no
lower bound for the actual growing finite head, no whole-Li sign,
and no RH conclusion. It does not import the stopped Section6 contour
argument audited in L977. Written in step221, 10 November 2026;
separate conceptual audit in step223 accepted (1) without a
mathematical correction, as detailed below.

## Proof

### Imported arithmetic identity and smooth trends

Import J. C. Lagarias, *Li coefficients for automorphic L-functions*,
Ann. Inst. Fourier **57**(5) (2007), 1689-1740,
DOI 10.5802/aif.2311. Its ordinary coefficients and radial star sum
are defined in [(1.1)-(1.5), p.1690](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=3).
For the self-dual trivial GL(1) representation, Definition4.3,
[(4.5), Lemma4.4/(4.6)-(4.8), pp.1708-1709](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=21),
give the exact identity

    lambda_n=S_infty(n)-S_f(n)+1.                       (2)

Here S_infty is the source's archimedean term. Its unconditional
[Theorem5.1, (5.1)-(5.4), pp.1712-1713](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=25),
specialized to N=Q=1, kappa=0 and K=0, gives

    S_infty(n)=P(n)+O(1),
    P(n)=(n/2)*log n+c*n,
    c=(EulerGamma-1-log(2*pi))/2.                       (3)

These exact conventions and constants were inspected in review218
and approved in review219 before this attempt. In particular (2)
uses (4.5)/(4.8), not the inconsistent alternating remark (4.13).
The pole term delta is 1 and is retained. The source explicitly
includes this GL(1) case and its completion 2*xi on p.1697. By L018
this has exactly the actual zeta zeros with their orders. Multiplying
xi by 2 leaves the ordinary coefficients unchanged: its added
constant logarithm contributes the nth derivative of
s^(n-1)*log(2), which is zero for n>=1. Thus these are the same
ordinary coefficients as L964/L968, with no division by n. Those
lemmas supply normalization context only; none of their conditional
sign conclusions is used.

Import also J. Arias de Reyna, *Asymptotics of Keiper-Li Coefficients*,
[author version, 31 January 2011, Theorem1 proof, pp.4-5](https://personal.us.es/arias/56-2RHB.pdf#page=4).
The inspected smooth term in that proof is

    J1(m)=2/(pi*m)*integral_0^infinity
          sin^2(m*arctan(1/(2*t)))*log(t/(2*pi)) dt
         =(log m+EulerGamma-1-log(2*pi))/2
             +O(log m/m).                              (4)

This is the smooth integral estimate alone. Its normalized l2
counting-error conclusion and its RH corollary are not imported.
The theorem's positive-ordinate multiplicity/counting setting is
available for actual zeta from L018 and the counting input in
L978-L979. Formula (4) itself is an explicit integral independent of
the actual zero locations. No proof of the source's full smooth
asymptotic is repeated: only its normalization and cutoff change
are needed below. Constants in (3)-(4) are independent of n.

### Agreement of the radial sum with paired height summation

For rho=beta+i*gamma with gamma>0 let

    A_n(rho)=G_n(rho)+G_n(conjugate(rho))
            =2*Re G_n(rho),
    K_n(t)=2-2*cos(2*n*arctan(1/(2*t))).

L018 preserves orders under conjugation. There are no real zeros
by L013, so every nontrivial zero belongs to exactly one such pair,
counting repeated entries by order. For fixed n, L978 proves
absolute convergence of sum_(gamma>T) |A_n(rho)| and of the model
tail sum K_n(gamma). The head is finite: its zeros lie in a compact
rectangle and are zeros of L018's nonzero entire completion. Hence
the sum of |A_n(rho)| over all positive-ordinate entries is finite.

For every finite radial bound R, the restriction |rho|<=R contains
both members of each conjugate pair or neither, with equal orders.
Thus its sum of G_n is exactly the corresponding finite sum of A_n.
As R tends to infinity these pair sets exhaust all positive-ordinate
entries. Absolute convergence of the paired series implies that their
limit is the same as its height exhaustion. If the source uses a
strict radial boundary, the same argument applies to that exhaustion.
This is an argument about complete conjugate pairs, not a claim of
absolute convergence of the unpaired G_n series. It identifies the
source's radial star sum with

    lambda_n=H_n+R_n,
    R_n=sum_(rho: Im rho>T) A_n(rho).                    (5)

In (5), every entry at gamma=T belongs to H_n and none belongs to
R_n. Distinct positive-ordinate zeros sharing an ordinate remain
separate entries; no critical-line replacement is made in H_n.

### Smooth normalization, endpoints and the removed interval

Define the Lebesgue integrals

    B_n=integral_0^infinity K_n(t)*log(t/(2*pi))/(2*pi) dt,
    D_n=integral_0^T K_n(t)*log(t/(2*pi))/(2*pi) dt.

The estimates in L979 give 0<=K_n(t)<=min(4,n^2/t^2) for t>0.
Near zero, 4*(|log t|+log(2*pi))/(2*pi) is integrable. Near infinity,
n^2*(log t+log(2*pi))/(2*pi*t^2) is integrable for each fixed n.
Thus B_n is absolutely convergent at both improper endpoints and
D_n is absolutely convergent at zero. No limiting zero sum is used
to define either integral.

The exact identity 2-2*cos(2u)=4*sin^2 u gives, with the same
absolutely convergent integral as (4),

    B_n=n*J1(n)=P(n)+O(log n).                          (6)

In particular the factor n is essential. The ordinary Li trend
in (3) matches (6) with precisely the same constant c.

Since T=sqrt(n)>1, direct integration gives

    integral_0^T |log t| dt=T*log T-T+2,
    |D_n|<=2/pi * integral_0^T |log(t/(2*pi))| dt
          <=2/pi * [T*log T+T*log(2*pi)+2]
          =O(sqrt(n)*log n).                           (7)

The constants here are independent of n>=2; log n>=log 2>0 and
T>=sqrt(2) absorb the linear and constant terms. The smooth measure
has no atom at T, so its interval convention does not change D_n.

### Tail errors and exact arithmetic assembly

Put V_n=sum_(rho: Im rho>T) K_n(Im rho). L978, retaining the actual
complex zeros, gives

    |R_n-V_n|<=C_disp*sqrt(n)*log n.                    (8)

L979 gives, with the right-continuous count including full orders,

    V_n-integral_T^infinity K_n(t)*log(t/(2*pi))/(2*pi) dt
        =O(sqrt(n)*log n).                             (9)

The counting integral underlying (9) is over (T,infinity); this is
exactly complementary to the weak head in (5), even when T is a
zero ordinate. L979 proves absolute integrability against the
variation of its signed counting-error measure, so (9) requires no
unsigned-to-signed inference or conditional rearrangement.

All sums/integrals in these equalities have now been justified.
Combining (7)-(9), then (6), yields

    R_n=B_n-D_n+O(sqrt(n)*log n)
        =P(n)+O(sqrt(n)*log n).                        (10)

Finally substitute (5) into the exact arithmetic identity (2):

    S_f(n)+H_n=S_infty(n)+1-R_n.                       (11)

Equations (3) and (10) prove (1). The retained constant 1 is absorbed
by sqrt(n)*log n on n>=2. If either source asymptotic begins only
at a larger fixed index, finitely many smaller integers are absorbed
in the same fixed-zeta constant: their S_f and H_n are finite and
sqrt(n)*log n is positive. No effective numerical value of C is
asserted. Every infinite limit above is for a fixed n; no interchange
with n tending to infinity is needed.

The head remains the actual complex finite sum. In particular (1)
does not control H_n from below, and (5) gives no whole-Li lower
bound at L968's threshold without such additional information.
L977's contour-majorant failure, L976's inverse-envelope stop and
the parked Coffey2007 route are unaffected. This calculation closes
the specified residual-assembly gap locally, not the main positivity
gap L030-L032/C032a or the signed forcing in L966. It claims no
mathematical novelty beyond the sources checked.

### Separate conceptual audit, step223, 10 November 2026

The exact target was reviewed under the prior SPECIALIZE coverage in
review221, separately approved in step222. This audit read the complete
proofs of L013, L018 and L978-L980, and L977's convention/stop record.
It reused reviews216/218/219 rather than opening a new source search.
The following checks concern this residual only.

The cited primary Lagarias PDF was rechecked at (1.1)-(1.5),
Definition4.3 and Lemma4.4 including its proof, Theorem5.1/(5.1)-(5.4),
and the trivial GL(1) completion on p.1697. The derivative definition
initially corresponds to lambda_(-n); the source's self-dual identity
lambda_(-n)=lambda_n removes that distinction here. Thus neither
negative-index convention nor the factor 2 in the completion changes
(2). Its delta=1 and the nonalternating eta convention are correct.
N=Q=1, kappa=0 gives K=0 in Theorem5.1, hence exactly (3).

The cited Arias author PDF was rechecked at the divided normalization
on pp.1-2 and the smooth part of the Theorem1 proof on pp.4-5. That
part estimates an explicit integral: its logarithmic endpoint
remainders are integrable and its displayed error is O(log n/n).
No RH hypothesis from the later corollary is needed for this integral.
The factor 4 in K_n=4*sin^2(n*arctan(1/(2*t))) gives B_n=n*J1(n),
so both the leading term and the linear constant in (3),(6) agree.
The arithmetic identity and smooth estimate remain cited inputs;
their full general proofs are not claimed as new local results.

L978 and L979 were replayed where load-bearing, and their canonical
proofs now record the audit. The paired absolute convergence applies
to each positive-ordinate entry, including distinct real parts at a
common ordinate. Each finite radial set is invariant under conjugation
with orders, so (5) follows by exhaustion of an absolutely summable
series of pair contributions. No rearrangement of the unpaired series
is used, and its absolute convergence is not assumed.
L013 excludes missing real contributions and L018 makes the finite
head finite, conjugation invariant and real.

At gamma=T the entire conjugate-pair contribution remains in H_n.
The right-continuous N(T) in L979 excludes the corresponding full
counting atom from its tail, and the smooth measure has no atom there.
Therefore the head, the actual tail and the model tail have exactly
complementary endpoint conventions without a height perturbation.
Absolute integrability at both smooth endpoints, the removed-interval
bound (7), and the total-variation justification in L979 all hold.

Finally (8)-(10) use only constants fixed independently of n; the
fixed-n upper limits precede the n-uniform inequalities. Substitution
in (2) gives exactly S_f+H_n=S_infty+1-R_n, verifying the plus sign
in (1). The positive denominator sqrt(n)*log n on n>=2 absorbs the
constant and any finite initial range. No mathematical formula or
DAG input changed. This accepts a relevant existing local input,
classified REPRODUCTION, without strengthening its order or claiming
progress beyond the cited sources. The actual head lower bound,
L030-L032/C032a and L966's signed forcing are still unresolved.

## Mathlib

Full matching coverage of (1), the source smooth asymptotic and the
ordinary arithmetic identity has not been checked and remains unknown.
No Mathlib theorem is imported and no Lean verification is claimed.
Elementary integration and summation infrastructure alone would not
supply the external zeta identities. Supporting references recorded
in L013/L018 and L978/L979 are not a formalization of this assembly.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
