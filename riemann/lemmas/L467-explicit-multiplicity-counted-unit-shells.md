# Lemma 467: explicit multiplicity-counted unit shells

## Hypotheses

Let N(T) count all nontrivial zeta zeros with 0<Im(rho)<=T,
with multiplicity, and put N(0)=0. Logarithms are natural. Import
Chiara Bellotti and Peng-Jie Wong, *Improved estimates for the argument
and zero-counting function of the Riemann zeta-function*, arXiv:2412.15470v2
(7 July 2025), Theorem 1.1, printed p. 1:

    |N(T)-F(T)| <= E(T), T>=e,
    F(T) = T/(2pi) log(T/(2pi e)),
    E(T) = 0.10076 log T + 0.24460 log log T + 8.08344.

The [versioned primary source](https://arxiv.org/pdf/2412.15470v2)
and its Section 5, pp. 23–24, are the citation input. Its analytic
parameter and zero computations are not independently rerun here,
and no independent full-manuscript audit is asserted. Use the actual
Xi and its multiplicity-preserving zero correspondence from L018
only for the final Xi interpretation. No RH, simplicity or external
fixed-half-plane hypothesis is used.

## Conclusion

For every real u>=1,

    N(u+1)-N(u) <= 18 log(u+2).

For every real v>=0, the multiplicity-counted number of positive
ordinates gamma in the closed interval [v,v+1] is at most

    18 log(v+2).

Consequently A=18 is valid in L464 equation (6), for its multiset
of positive real parts of Xi zeros. This specializes a known count
theorem; it gives neither Laguerre signs nor an effective tail onset.

## Proof

For T>=e, set b=0.34536=0.10076+0.24460 and d=8.08344.
Since log log T<=log T (apply log x<=x for x=log T>=1),

    E(T)<=b log T+d.                                      (1)

First let w>=3. For x in [w,w+1], differentiation gives

    F'(x)=log(x/(2pi))/(2pi)<=log(w+2).

Indeed, when the numerator is negative the claim is immediate;
otherwise 2pi>1 and log(x/(2pi))<=log x<=log(w+2).
Integration and (1) therefore give

    F(w+1)-F(w)+E(w+1)+E(w)
      <=(1+2b)log(w+2)+2d
      <=(1+2b+2d)log(w+2)
      =17.85760 log(w+2)<18 log(w+2).                    (2)

The second inequality uses log(w+2)>=log 5>1. The decimal
arithmetic here is exact: 2b=0.69072 and 2d=16.16688.
Subtracting the lower bound for N(w) from the upper bound for
N(w+1) proves the half-open conclusion for w>=3.

For closed shells with v>=3, take 0<epsilon<v-e and apply the
source lower bound at v-epsilon and upper bound at v+1:

    N(v+1)-N(v-epsilon)
      <=F(v+1)-F(v-epsilon)+E(v+1)+E(v-epsilon).

Zeta zeros are isolated with finite multiplicities, and there are
finitely many in each compact positive-height strip. This also follows
from the entire completion L018: all nontrivial zeros are in the
bounded real-part strip, and the completion is not identically zero.
Thus N(v-epsilon) tends to N(v-), counting precisely ordinates
strictly below v. Continuity of F and E for T>=e gives

    #{gamma: v<=gamma<=v+1}
      =N(v+1)-N(v-)
      <=F(v+1)-F(v)+E(v+1)+E(v).

Equation (2) applies. Every occurrence is counted with multiplicity;
there is no generic-height restriction or loss of lower-endpoint zeros.

For the remaining heights, use the source only at T=4>=e.
As 4<2pi e, F(4)<0; also log 4<2, so (1) yields

    N(4)<=F(4)+E(4)<2b+d=8.77416<9.                    (3)

If 1<=u<3, monotonicity and nonnegativity give
N(u+1)-N(u)<=N(4)<9<18 log(u+2).
If 0<=v<3, every positive ordinate in [v,v+1] is counted by
N(4), so its count is <9<18 log(v+2). Here log 2>1/2,
as follows by integrating 1/x>1/2 on 1<=x<2; hence
18 log(v+2)>=18 log 2>9. No information about a first zero
or a numerical zero table is required. The elementary inequalities
e<3 and 2pi>4 also justify all the stated compact-height comparisons.

Finally L018 sends a zeta zero beta+i gamma to the Xi zero
gamma+i(1/2-beta), preserving multiplicity. Thus the same count
is exactly the multiset count in L464, including separate Xi zeros
having the same real part. This proves the asserted specialization. ∎

### Critical audit — 2026-10-26

The specialization passes an independent bounded audit under the saved
SPECIALIZE assessment. This verifies the elementary application, not
the source's numerical computations or its full analytic manuscript.
The theorem, constants and date above agree with the versioned primary
Theorem 1.1. Section 5's two height cases remain cited inputs under the
recorded source assessment; they are not replaced by sampled values.

The source's Section 3 opening, printed p. 9, identifies its symmetric
rectangle count with twice N(T) and applies the argument principle to
the entire completion. The argument principle counts zero orders, so
the source input is multiplicity-counted despite its set notation.
The source completion differs from L018's by a nonzero constant, which
does not change zeros or orders. The contour identity is used only at
heights with no boundary zero, not asserted through a boundary zero.
Even if the count estimate were initially obtained only at those
heights, its continuous envelopes F(T)±E(T) extend to the inclusive
count at every T>=e: choose non-ordinate heights T_j decreasing to T.
Finiteness of zeros in compact strips gives N(T_j)=N(T) eventually,
and continuity gives both inequalities at T. This also covers T=e.
Thus no endpoint convention for a contour or S(T) is an extra premise.

For the large-height comparison, differentiation of
T(log T-log(2pi)-1)/(2pi) gives precisely the derivative displayed
above. The negative-numerator case remains valid even when F decreases.
In the other case division by 2pi>1 only decreases the nonnegative
numerator. Hence its integral over a unit interval is bounded above
by log(w+2), with no assumed monotonicity of F. Both arguments of E
are at least e, and each logarithm is bounded by log(w+2). The constant
term 2d is absorbed using log(w+2)>1, with the correct direction since
d>0. Exact arithmetic gives 17.85760<18, leaving coefficient margin
0.14240; this holds for every real w>=3, not just sampled heights.

For v>=3, v>e ensures the permitted epsilons exist. The compact-strip
finiteness used for the left limit follows from L018 on a closed
rectangle containing 0<=Re(s)<=1 and the relevant bounded ordinates;
the entire completion is not identically zero since xi(1)=1/2.
Consequently the left-limit count excludes ordinates equal to v,
while N(v+1) includes its upper endpoint. Subtraction therefore counts
the entire closed interval, with every zero order retained. The
continuous expression on its right is exactly the one in (2).

The remaining ranges use only monotonicity and the single permitted
source height 4. The strict bound F(4)<0, log 4<2 and b>0 give
N(4)<8.77416<9. The integral of 1/x on [1,2] is strictly greater
than 1/2, so 18 log(v+2)>9 even at v=0. This proves compact coverage
for 0<=v<3 and also for 1<=u<3; the boundary u=v=3 is already in
the large-height case. Positive ordinates alone are counted when v=0.
No zero table, first-zero bound or simplicity premise enters.

Finally the affine map in L018 has nonzero derivative and is injective.
It preserves orders and sends Im(rho)>0 exactly to Re(z)>0. Distinct
zeros sharing an ordinate remain distinct Xi zeros or repeated
occurrences in its multiset; neither conjugate pairs nor repeated
zeros are merged. This is precisely L464's convention in (6).
The canonical mathematical input remains L018, so no DAG change is
needed. The arithmetic and invocation-start exact-target match are
recorded in drafts/audits/2026-10-26-l467-exact-arithmetic.json; that
bookkeeping is supplementary to the all-height proof above.

The verdict is local verification of a known-result specialization.
It supplies no new signs, numerical saddle onset, bounded-height/tail
overlap, or RH conclusion. Mathlib coverage remains unchecked.

## Mathlib

Not checked. No matching formal theorem for the full explicit count
or this specialization is claimed; unknown coverage is not absence.
