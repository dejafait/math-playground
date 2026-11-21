# Lemma 979: truncated arctangent-model counting-error bound

## Hypotheses

Use the actual nontrivial zeta zeros of L018. Let

    N(t)=#{rho: 0<Im(rho)<=t},
    M(t)=t*log(t/(2*pi*e))/(2*pi),
    E(t)=N(t)-M(t),                                      (1)

where every zero is counted according to its order, including different
real parts at a common ordinate. For every integer n>=2 set T=sqrt(n)
and, for t>0, put

    theta_n(t)=2*n*arctan(1/(2*t)),
    K_n(t)=2-2*cos(theta_n(t)).                           (2)

Use the right-continuous counting function in (1). The integral below
is over (T,infinity), complementary to the weak finite head gamma<=T.
No RH, simplicity, avoidance of zero ordinates, finite zero list,
positivity of dE or Li-coefficient sign is assumed.

## Conclusion

There is a finite constant C_E, independent of n, such that
|E(t)|<=C_E*log t for every t>=sqrt(2). For any such constant,

    I_n=integral_(sqrt(n),infinity) K_n(t) dE(t)
       =-K_n(T)*E(T)-integral_T^infinity E(t)*K_n'(t) dt,  (3)
    |I_n|<=C_E*[4*log T+2*n*(log T+1)/T]
         <=C_E*(1+sqrt(2)+2/log 2)*sqrt(n)*log n.         (4)

The Stieltjes integral is well defined and absolutely integrable
against the total variation of dE for each fixed n. In particular,

    sum_(rho: Im(rho)>sqrt(n)) K_n(Im(rho))
       -integral_sqrt(n)^infinity
            K_n(t)*log(t/(2*pi))/(2*pi) dt
        =O(sqrt(n)*log n),                              (5)

with multiplicities and one fixed-zeta O-constant independent of n.
This pays only the model counting-error tail. It gives no finite-head
sign, ordinary-Li/arithmetic assembly, or RH conclusion.

## Proof

### Imported counting and integration theorems

Import E. Hasanalizade, Q. Shen and P.-J. Wong, *Counting zeros of the
Riemann zeta function*, arXiv:2107.06506v1, 14 July 2021,
[Corollary 1.2, equation (1.5), p.2](https://arxiv.org/pdf/2107.06506v1#page=2):

    |E(t)|<=0.1038*log t+0.2573*log log t+9.3675,
                                                        t>=e. (6)

Its full-strip count includes orders and the upper endpoint; Section 2,
(2.1)-(2.3), p.3, and the corollary proof, p.15, are the source scope
checked in the saved assessments. Its bounded-height numerical inputs
are external theorem inputs, not independently replayed here. For t>=e,
log log t<=log t and 1<=log t, so (6) gives
|E(t)|<=9.7286*log t. On the compact interval [sqrt(2),e], N(t)<=N(e)
and M is bounded. Thus one possible fixed choice is

    C_E=max(9.7286,
      [N(e)+max_(sqrt(2)<=t<=e)|M(t)|]/log(sqrt(2))).      (7)

Finiteness of the count also follows from L018's entire nonzero
completion and isolated zeros in a compact rectangle. Formula (7)
covers all small integers with sqrt(n)<e without any zero-table input.

Import G. B. Folland, *Real Analysis: Modern Techniques and Their
Applications*, 2nd ed., Wiley, 1999, section 3.5,
[Theorem 3.36, p.107](https://djvu.online/file/NPF4BEtSuqdFA).
For F,G in NBV, one continuous, it gives

    integral_(a,b] F dG+integral_(a,b] G dF
        =F(b)G(b)-F(a)G(a).                             (8)

NBV here means globally bounded variation, right continuity and zero
limit at minus infinity (p.103). The finite-interval absolutely
continuous measure identity is Theorem 3.35, p.106. These tools were
inspected in review216; the specialization below verifies their
hypotheses rather than treating the unbounded global E as NBV.

### Kernel estimates and the finite identity

Differentiating (2) at positive t gives

    theta_n'(t)=-n/(t^2+1/4),
    K_n'(t)=-2*n*sin(theta_n(t))/(t^2+1/4).

Consequently, for every t>0,

    |K_n'(t)|<=2*n/t^2,
    0<=K_n(t)<=min(4,n^2/t^2).                          (9)

The second bound uses arctan u<=u for u>=0 and
2*(1-cos v)<=v^2 for real v. No small-phase assumption is made near T.

Fix a finite U>T. On [T,U], E is right-continuous and of bounded
variation: N is a finite step function with positive integer jumps,
and M is continuously differentiable. Extend E by zero below T and
by the constant E(U) above U. This extension is in NBV; its possible
jump at T has size E(T). Extend K_n continuously by zero on
(-infinity,T-1], by the linear ramp from 0 to K_n(T) on [T-1,T],
by K_n on [T,U], and by K_n(U) above U. This extension is continuous
and in NBV. It has finite variation because its middle piece is C^1
on a compact interval. Both extensions have zero limit at minus
infinity, so (8) applies. On (T,U], their measures are dE and
K_n'(t)dt, respectively. We obtain exactly

    integral_(T,U] K_n dE
      =K_n(U)*E(U)-K_n(T)*E(T)
         -integral_T^U E(t)*K_n'(t) dt.                 (10)

The extension's jump at T is outside this integration interval.
In particular E(T) contains every zero at T, rather than a left limit
or half-weight value. Zeros at U are included. Multiplicities enter
as their full jumps throughout; no endpoint is assumed regular.

### Infinite limit and the n-uniform estimate

For fixed n, (7) and (9) give

    |K_n(U)*E(U)|<=C_E*n^2*log U/U^2 -> 0,
    integral_T^infinity |E(t)*K_n'(t)| dt
      <=2*C_E*n*integral_T^infinity log t/t^2 dt
      =2*C_E*n*(log T+1)/T<infinity.                   (11)

Thus (10) has a limit for arbitrary real U tending to infinity,
including sequences of zero ordinates, and proves (3).
For the stronger total-variation assertion, L978 proves absolute
convergence of sum_(gamma>T) K_n(gamma) for this exact kernel and
multiset, for each fixed n. Also M'(t)=log(t/(2*pi))/(2*pi), and (9)
shows integral_T^infinity K_n(t)*|M'(t)| dt<infinity: the finite lower
portion is continuous and bounded, and its tail is bounded by a
constant times n^2*log t/t^2. Since dE=dN-M'(t)dt locally, its total
variation is at most dN+|M'(t)|dt. These two finite integrals prove
absolute integrability on (T,infinity) and justify the split in (5).
This use of L978 is only its convergence result, not any sign or
replacement of the actual finite head.

Finally |K_n(T)|<=4, so (3) and (11) give the first inequality in (4).
Substitute T=sqrt(n) to write its right side as

    C_E*[2*log n+sqrt(n)*log n+2*sqrt(n)].               (12)

For all n>=2, 2/sqrt(n)<=sqrt(2) and 2/log n<=2/log 2.
Dividing (12) by sqrt(n)*log n proves the stated second inequality.
The same C_E works for every n. The upper-boundary limit was taken
for each fixed n; no uniform limit in n or interchange of an n-limit
with a zero sum is needed.

This is a standard specialization of the cited counting error and
finite signed integration by parts, classified REPRODUCTION under the
prior SPECIALIZE assessment. No novelty beyond the checked sources is
claimed. In particular |E|=O(log t) has never
been used as a bound for the variation of E, and no l2-to-pointwise
inference is used. L977 supplies context for the corrected cutoff
conventions, and L968 a downstream whole-Li threshold; neither is a
mathematical premise of this proof. Smooth-model/arithmetic constant
matching, the ordinary Li assembly and actual finite-head signs remain
unresolved by this lemma. Written in step218, 10 November 2026.

Separate conceptual audit in step223 accepted (3)-(5) without a
formula correction. It replayed the small-height constant (7), the
derivatives in (9), both finite NBV extensions and their endpoint
values, and the fixed-n limit (11). The extension of E may jump at T
and U; the continuous extension of K_n is the hypothesis needed in
(8). The lower jump is excluded and the upper jump included in (10).
The variation argument uses dN+abs(M')dt, with each weighted integral
finite, and does not infer variation control from a bound on E.
The constants in (12) and (4) are independent of n. This is local
proof verification under the cited counting and finite-interval
integration theorems, not a new counting theorem or effective bound.

## Mathlib

Full matching coverage of (3)-(5), and formal coverage of the cited
zero-counting theorem, have not been checked and remain unknown.
No Mathlib theorem is imported. Generic integration-by-parts support
would not itself provide the multiplicity-counting input or this
uniform truncated specialization.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
