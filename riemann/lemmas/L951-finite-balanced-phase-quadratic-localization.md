# Lemma 951: explicit quadratic localization of the finite balanced phase

## Hypotheses

Use exactly L939(10)'s scalar phase. Let

    sqrt(2/3)<=r<=2, -r<=s<=11r,
    f_r(s)=exp(2r(sqrt(1+s/r)-1)), h_r(s)=f_r(s)-1-s.             (1)

The square root is the nonnegative real square root, including at
s=-r. For the constrained statement let y_1,...,y_12 be real,
sum_i y_i=0, and y_i>=-r. Put z_r(y)=sum_i h_r(y_i).
No arithmetic-library, theta truncation, signed-density sign, contact,
real-zero or RH assumption is used.

## Conclusion

Uniformly on the whole closed scalar domain (1),

    h_r(s)>=s^2/512.                                            (2)

Consequently, on the whole closed constrained simplex,

    z_r(y)>=(1/512)sum_(i=1)^12 y_i^2.                           (3)

In particular zero is its unique constrained minimum. This applies
to L939's exact phase in L938's fixed density when 8<=E<=48 and
r=sqrt(E/12), retaining all twelve coordinates.

This is a new explicit input in the notebook, obtained by elementary
specialization of cited Taylor formulas under the previously approved
EXPLORE scope. It is not a claim of originality beyond the sources
checked. The independent step101 audit below accepts the full closed
domain and constrained transfer. It supplies no bound for the signed amplitude or its integral,
no payment of L949's remaining m-B allowance, and no effective
infinite-energy join or RH sign conclusion.

## Proof

### Imported calculus and the square-root substitution

Import Taylor's theorem with integral and Lagrange remainders from
NIST DLMF, live Section1.4 as inspected on 9 November 2026,
[equations1.4.35–1.4.37](https://dlmf.nist.gov/1.4#E35).
These formulas require C^(n+1) on the relevant closed interval.
Every use below is for the exponential or its composition with a
linear real map on a finite interval, hence is C^infinity there.
The source theorem is imported, not reproved. The need for a local
derivation is the explicit uniform constant and the nonconvex
square-root phase, which the general Taylor theorem does not state.
Source comparison and the exact approved scope are recorded in
`drafts/literature/2026-11-09-balanced-phase-finite-localization-97.md`.

Set

    tau=sqrt(1+s/r)-1, a=2r.

Since r>0, the exact scalar domain implies

    -1<=tau<=sqrt(12)-1,
    s=r tau(tau+2),
    h_r(s)=exp(a tau)-1-a tau-r tau^2.                           (4)

Apply the integral remainder to v -> exp(a tau v) on [0,1]:

    exp(a tau)-1-a tau
       =a^2 tau^2 integral_0^1 (1-v)exp(a tau v)dv.              (5)

This identity includes tau=0. At s=-r we have tau=-1, and (4)–(5)
still apply to a smooth exponential. No derivative of the square
root at that endpoint has been taken.

### Two exact exponential bounds

Write P_7(-b)=sum_(k=0)^7 (-b)^k/k! for b>0. The Lagrange
remainder in the imported theorem gives

    exp(-b)=P_7(-b)+exp(-theta b)b^8/8!, 0<theta<1,

so the last term is strictly positive. Exact rational arithmetic gives

    P_7(-13/8)=2070516883/10569646080
             =25/128+6132883/10569646080 >25/128,
    P_7(-2)=41/315=1/8+13/2520 >1/8.                            (6)

Thus exp(-13/8)>25/128 and exp(-2)>1/8. These are analytic
inequalities with positive remainders, not rounded exponential values.

Let delta(r)=r-1+exp(-2r). For r>=13/16,

    delta'(r)=1-2exp(-2r)>0,                                   (7)

because exp(2r)>=1+2r>=21/8>2. The first inequality is the
first-order Taylor lower bound at a nonnegative argument. Also
(13/16)^2=169/256<2/3 and 13/16>4/5. Hence every admissible r
is greater than both 13/16 and 4/5.

### Nonpositive scalar coordinates

If -1<=tau<=0, then exp(a tau v)>=exp(-a v) for 0<=v<=1.
Equation (5), applied also at tau=-1, therefore gives

    exp(a tau)-1-a tau
       >=tau^2(exp(-a)-1+a).

Subtracting r tau^2 in (4) yields

    h_r(s)>=delta(r)tau^2.                                    (8)

For sqrt(2/3)<=r<=1, (6)–(7) imply

    delta(r)>=delta(13/16)>-3/16+25/128=1/128.

Here 1<=tau+2<=2 and r<=1, so s^2<=4tau^2. Consequently
h_r(s)>=(1/128)tau^2>=s^2/512.

For 1<=r<=2, (6)–(7) instead give

    delta(r)>=delta(1)=exp(-2)>1/8.

Now s^2<=16tau^2, so h_r(s)>=(1/8)tau^2>=s^2/128>=s^2/512.
Both arguments are valid at tau=0 without division by tau.

### Nonnegative scalar coordinates

If tau>=0, the integral in (5) is at least 1/2. Thus

    h_r(s)>=r(2r-1)tau^2
            =(2-1/r)r^2 tau^2 >=(3/4)r^2 tau^2,               (9)

using r>=4/5. The domain in (4) gives
tau+2<=sqrt(12)+1<5. Therefore s^2<=25r^2 tau^2 and

    h_r(s)>=(3/100)s^2>=s^2/512.

The comparison 3/100>1/512 is exact. This includes s=0, where
h_r(0)=0 and both sides of (2) vanish. Together with (8), it proves
(2) at every point of the closed domain, including s=-r and s=11r.

### Exact constrained-simplex applicability

For any coordinate y_i in the hypotheses,

    y_i=-sum_(j!=i)y_j<=11r.

Thus every one of the twelve coordinates lies in the scalar domain
[-r,11r]. Summing (2) proves (3), including at the faces and at zero.
If y is nonzero, its sum of squares is positive, proving uniqueness
of the constrained minimum.

To check the energy correspondence, use L939's exact variables
x_i=r^2+r y_i, x_i>=0, sum_i x_i=E=12r^2. They give
y_i>=-r and sum_i y_i=0. Conversely these conditions give such
nonnegative x_i. The condition 8<=E<=48 is precisely
sqrt(2/3)<=r<=2. The open integration domain of L939 is contained
in this closed simplex. No factor, signed polynomial, normalization,
Jacobian or boundary mass is changed by the scalar estimate. In
particular a phase estimate on a face is not an integral estimate
for L939's possibly singular amplitude on that face.

### Finite arithmetic check and qualifications

The full rational sums in (6) are the arithmetic proof.
`scripts/heat/l951-balanced-phase-rational-check-99.json` records all
their terms, exact differences from the required lower bounds, and
the remaining rational comparisons. It contains no sampled phase
values or floating-point exponential approximations. Reproduce with
`python3 scripts/heat/l951-balanced-phase-rational-check-99.py`.
The script checks only finite arithmetic; (4)–(9) and the domain
argument above supply the analytic proof.

The L940 signed-amplitude obstruction and L950 oversized fixed-row
cost concern different objects and remain unchanged. The independent
obligations are signed-amplitude/local remainder control, local-ball
fit for an integral application, full-theta and boundary mass, the
effective infinite-energy join, head/global variation, other signs
and degrees, contacts, initialization and realization. In particular
(2)–(3) alone say nothing about the sign of v(E).

### Independent closed-domain audit — step101, 9 November 2026

Accepted under the unchanged SPECIALIZE scope in
`drafts/literature/2026-11-09-l951-finite-phase-audit-99.md`.
This is verification of the local specialization, not a new general
theorem or an originality claim. The source coverage is reused from
the approved assessment; no broader Taylor or Laplace result is assumed.

**Identities and source hypotheses.** In (4), squaring tau+1 gives
s=r(tau^2+2tau) exactly, and a=2r converts -s into
-a tau-r tau^2. Taylor's integral remainder for
F(v)=exp(a tau v) has F''(v)=(a tau)^2 exp(a tau v), giving
(5) with the stated prefactor and no assumption on the sign of tau.
F is smooth on the entire interval [0,1], also when tau=-1 or0.
For (6), the eighth derivative of exp(x) is positive throughout
[-b,0]; its degree-seven remainder is exp(-theta b)b^8/8!>0.
No differentiability of sqrt at s=-r is used in either application.

**Complete finite arithmetic.** Replayed the rational checker and
inspected every term and all five checks in its complete /checks
certificate value. Both sums agree with (6). In particular
10569646080/128=82575360 and
2070516883-25*82575360=6132883>0;
41/315-1/8=(328-315)/2520=13/2520>0.
The endpoint comparison is 169*3=507<512=256*2.
The remaining comparisons are (1/8)/16=1/128>=1/512 and
3/100>1/512 since1536>100. The replay reports zero failures.
These checks certify finite rational arithmetic only.

**Uniform analytic comparisons.** The positive-argument first-order
Taylor bound gives exp(2r)>=1+2r>=21/8>2 on r>=13/16.
It follows that delta'(r)>0 on that whole interval. Thus the lower
endpoint need not be approximated: sqrt(2/3)>13/16>4/5, so the
delta comparisons made on both parameter subintervals are valid.
For -1<=tau<=0, multiplication of tau>=-1 by av>=0 proves
the exponential comparison inside (5). Subtraction then gives
exactly r-1+exp(-2r), not a derivative or a quotient at zero.
On r<=1, s^2<=4tau^2 and delta(r)>1/128 give the required1/512.
On r>=1, s^2<=16tau^2 and delta(r)>1/8 give the stronger1/128.
Both cases include r=1; r=2 is included in the latter.
For tau>=0, the integral is at least1/2, giving
r(2r-1)tau^2. Since r>4/5, its ratio to r^2 tau^2 is at
least3/4 without dividing by tau. Also
tau+2<=sqrt(12)+1<5. Therefore the positive-coordinate
constant3/100 is valid up to s=11r. At tau=0 all displayed
bounds hold directly with both sides zero. At tau=-1 the
nonpositive proof is valid as written. This verifies the entire
closed domain rather than a sampled or punctured interval.

**All twelve coordinates and scope.** From sum y_i=0 and each of
the other eleven coordinates being at least-r, each y_i<=11r.
Hence summing the scalar bound is valid on every face, including
vertices. At zero z_r=0; at every nonzero feasible vector its sum
of squares is positive. This proves the asserted unique minimum.
L939(10)'s definitions match (1) exactly, and its substitution
x_i=r^2+r y_i gives a bijection of the closed constrained domains
at E=12r^2. The endpoints E=8,48 give exactly r=sqrt(2/3),2.
No Jacobian or Hessian factor enters a pointwise phase inequality.
The sole direct local mathematical input remains L939 for the phase
and coordinate definitions; no DAG change is needed. This audit
does not verify L939's asymptotic anew or any integral application.
The boundary singularities in its amplitude, all signed errors and
L949's exact remaining allowance remain separate obligations.

## Mathlib

Full matching coverage of (2)–(3) has not been checked. Supporting
coverage for the exponential Taylor formulas and finite-simplex
algebra has also not been checked. This records unknown availability,
not an absence claim. No Lean or other formal proof is asserted.
