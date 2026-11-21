# Lemma 836: effective residual-product envelope at shift 6002

## Hypotheses

Use the actual F, quotient g, M_s, m_1, p_j, R, q, T_s, d_s and d_1
of L835, including L834's simple positive packet and verified-height
input. Fix k=6002, put J=k+1=6003, and write

\[
p_j=4\gamma_j^2\quad(1\le j\le J),\qquad
T=\gamma_J,\quad
R=2(\gamma_k^2+T^2),\quad
a=\frac{R}{4T^2}=\frac{p_k+p_J}{2p_J}<1.
\]

The gamma_j are the first J positive ordinates, distinct and simple as
justified in L834, and T<H=3,000,175,332,800. Use L832's unconditional
genus-zero product, normalized by F(0)=1, and L467's imported inclusive,
multiplicity-counted zero envelope. Set b=0.34536 and d=8.08344, exactly.
No individual zero enclosure is assumed given. No RH assumption is made
above H, and no lower contour estimate is assumed.

For the optional certified evaluation interface, assume two rational
intervals [l,u] and [v,w], independently certified to enclose respectively
gamma_k and gamma_J **with these indices**, with 4<l<=u<v<=w<H.
The certificate must account for all earlier zeros; two unindexed sign
changes or approximate ordinates do not supply this input. Such numerical
records are not constructed or assumed available in this lemma.

## Conclusion

For q<s<1 define

\[
V(T)=\frac{\log(T/(2\pi))}{\pi T}
      +\frac{b(\log T+1/2)+d-J}{T^2},                    \tag{1}
\]
\[
\mathcal B(s)=\log\frac{1+sa}{1-a}
                +\frac{(1+s)R}{4(1-a)}V(T).            \tag{2}
\]

These quantities are finite and V(T)>0. Unconditionally for the actual
quotient of L835,

\[
\log(M_s/m_1)\le\mathcal B(s).                          \tag{3}
\]

The first omitted simple factor p_J is the logarithm in (2); every later
zero, with multiplicity and including possible off-line zeros above H,
is covered by the second term. No unknown zero sum or contour extremum
occurs on the right.

For the stipulated initial choice s=(1+q)/2, (3) yields the fully explicit
sufficient overlap expression

\[
\mathcal E_m=\mathcal B(s)+2\log T_s
  -\sum_{j=1}^k\log(s-x_j)-\sum_{j=1}^k\log(1-x_j)
  +(m+k+2)\log s,\qquad x_j=p_j/R.                      \tag{4}
\]

If an integer PF order m is separately justified, m+1>=k-1 and
\(\mathcal E_m<0\), then L835 supplies positivity at this shift for r>=m+1,
joining nonnegativity through r=m. Formula (4) retains **all** finite
products. It is a sufficient upper bound for L835(4), not an equality
with its actual left side. L832 establishes only m=6001 locally.

There is also a coarser evaluable version needing only the two indexed
intervals specified above. Put

\[
R_+=2(u^2+w^2),\quad
q_+=\frac{2u^2}{u^2+v^2}<1,\quad
a_+=\frac12\left(1+\frac{u^2}{v^2}\right)<1,\quad
s_+=\frac{1+q_+}{2}<1.
\]

Obtain any rational V_+>=V(T) by outward interval evaluation of (1) on
T in [v,w], with certified enclosures for pi and the real logarithms.
Necessarily V_+>0 for valid enclosures. Define a certified upper bound
B_+ for

\[
\log\frac{1+s_+a_+}{1-a_+}
            +\frac{(1+s_+)R_+}{4(1-a_+)}V_+,            \tag{5}
\]

and a certified upper bound C_+ for

\[
B_++2\log k+(2k-2)\log(1+q_+)
                    +k\log2-2k\log(1-q_+).            \tag{6}
\]

All finite packet costs have been bounded in (6), not omitted. Then

\[
\log\delta_r(s)\le C_+ +(r+k+1)\log s_+,
                        \qquad r\ge k-1.              \tag{7}
\]

In particular, the exact concrete certificate inequality for a separately
justified PF_m overlap using this coarse interface is

\[
C_+ +(m+k+2)\log s_+<0,\qquad m+1\ge k-1.             \tag{8}
\]

Rational upper bounds for the entire left side must be strictly negative
to certify (8); a floating-point preview or an interval containing zero
does not certify it. With finite indexed intervals (7) gives an effective
sufficient eventual rank by increasing r until its upper bound is
negative. No such intervals, rank, PF enlargement or overlap are
numerically certified here. Failure of (8) for a given majorant would
refute only that sufficient certificate, not positivity.

This is a **local standard-method specialization**, validated by the
separate conceptual audit of 2026-11-06 recorded below. It gives no new
general product/count theorem, no improvement to the cited zeta estimates,
no growing-shift signs and no RH conclusion. No numerical overlap is
validated by this audit.

## Proof

**Imported results and need for this specialization.** L832 records
Olga M. Katkova, *Multiple positivity and the Riemann zeta-function*,
[arXiv:math/0505174v1](https://arxiv.org/pdf/math/0505174v1), (6),
printed p.3, and the Hadamard passage in Theorem1's proof, pp.5–6.
After its positive variable rescaling and the sign change from G to F,
this supplies

\[
F(z)=\prod_{\nu}(1-z/p_\nu),\qquad
\sum_\nu |p_\nu|^{-1}<\infty,
\]

with multiplicities and compact convergence; F(0)=1 leaves no extra
constant or exponential factor. L834 supplies the actual simple packet,
square map and separation. L467 imports Chiara Bellotti and Peng-Jie
Wong, *Improved estimates for the argument and zero-counting function of
the Riemann zeta-function*,
[arXiv:2412.15470v2](https://arxiv.org/pdf/2412.15470v2), Theorem1.1,
printed p.1, with the Section5 cases on pp.23–24. Precisely, for t>=e,

\[
N(t)\le\frac{t}{2\pi}\log\frac{t}{2\pi e}
            +0.10076\log t+0.24460\log\log t+d
\le U(t):=\frac{t}{2\pi}\log\frac{t}{2\pi e}+b\log t+d.\tag{9}
\]

The second inequality uses log log t<=log t. N includes all positive
ordinates up to and including t, counting orders. Source computations
are imported, not rerun. The optional sharper Brent–Platt–Trudgian
zero-sum theorem is not used. The inspected literature does not already
give (2) for L835's quotient. Only the elementary specialization below
is derived, to replace its unknown analytic ratio by specified data;
the general product and count theorems are not reproved.

**1. A tail bound with its full endpoint term.** The source specialization
in L467 gives N(4)<9. Since N(T)=J=6003, necessarily T>4>e. N(T)=J
includes the simple zero at T and all k earlier zeros, with no other
zero at that height; this is L834's verified simple ordering, not an
additional count hypothesis about the unknown tail.

For any U_0>T, finite partial summation, retaining both endpoints, gives

\[
\sum_{T<\gamma\le U_0}\gamma^{-2}
 =\frac{N(U_0)}{U_0^2}-\frac{N(T)}{T^2}
                         +2\int_T^{U_0}\frac{N(t)}{t^3}\,dt.\tag{10}
\]

One can verify (10) for each individual ordinate lambda: its contribution
when lambda<=T is zero on both sides, since
U_0^(-2)-T^(-2)+2 integral_T^U_0 t^(-3)dt=0. For T<lambda<=U_0,
its right side is U_0^(-2)+2 integral_lambda^U_0 t^(-3)dt=lambda^(-2).
This also covers lambda=T and lambda=U_0, and is repeated for each
unit of multiplicity. Thus no generic-height assumption or half weight
at T has been introduced.

The count envelope gives N(U_0)=O(U_0 log U_0), so the first term tends
to zero. It also makes the improper integral absolutely convergent.
Taking the monotone limit of the nonnegative finite sums in (10), then
using (9), gives

\[
S(T):=\sum_{\gamma>T}\gamma^{-2}
 =-\frac{J}{T^2}+2\int_T^\infty\frac{N(t)}{t^3}\,dt
 \le-\frac{J}{T^2}+2\int_T^\infty\frac{U(t)}{t^3}\,dt
 =V(T).                                                     \tag{11}
\]

For the final equality, the main-count term integrates to
log(T/(2pi))/(pi T):
integral_T^infinity log(t/(2pi e))/t^2 dt=log(T/(2pi))/T.
The other two integrals are
2 integral_T^infinity log t/t^3 dt=(log T+1/2)/T^2 and
2 integral_T^infinity t^(-3)dt=1/T^2.
Their boundary terms at infinity vanish. This proves (1) and keeps
the essential subtraction -J/T^2. There are further verified zeros
above T by L834's imported count N(H)>J; hence S(T)>0 and V(T)>0.

**2. Counting the correct product factors.** As in L834, each nontrivial
zero rho=beta+i gamma with gamma>0 gives one zero
p=-4(rho-1/2)^2 of F, with the same multiplicity. Its reflected
negative-height zero gives the same factor, not another factor.
There are no zero-height zeros. On positive-height representatives the
map is injective: equality of the squares forces rho'=rho or rho'=1-rho,
and the latter has negative height. Distinct positive-height off-line
zeros at the same ordinate therefore remain distinct factors. In all
cases

\[
|p|=4(\gamma^2+(\beta-1/2)^2)\ge4\gamma^2.             \tag{12}
\]

After removal of the first k factors, the first omitted one is precisely
p_J=4T^2, simple. Every other representative has gamma>T, including
any off-line zeros above H. In particular its t_p=R/|p| satisfies
0<t_p<a<1. By (11)–(12),

\[
\sum_{p\ne p_J\text{ in the residual product}}t_p
                  \le\frac R4 S(T)\le\frac R4 V(T).    \tag{13}
\]

No unverified high zero has been discarded or treated as real.

**3. Modulus bounds and compact limits.** Exhaust the residual zeros by
finite multisets (conjugation-invariant if desired), including p_J.
For every such finite product g_A and every |z|=s, triangle inequality
gives |g_A(z)|<=prod_(p in A)(1+s t_p). For |z|=1, reverse triangle
inequality gives |g_A(z)|>=prod_(p in A)(1-t_p)>0. For 0<=t<=a<1,

\[
\log(1+st)-\log(1-t)
 \le st+\frac{t}{1-t}\le\frac{1+s}{1-a}t.              \tag{14}
\]

Here log(1+st)<=st, and
-log(1-t)=integral_0^t (1-u)^(-1)du<=t/(1-t).
For the last comparison multiply by 1-a:
s(1-a)+(1-a)/(1-t)<=s+1. There is no logarithm of a complex quantity.

Moreover sum t_p<infinity and t_p<=a<1, so
sum -log(1-t_p)<=sum t_p/(1-a)<infinity. Thus the scalar lower
products converge to a strictly positive number, not zero. The scalar
upper products converge too since sum log(1+st_p)<=s sum t_p.
Compact convergence of the genus-zero products gives g_A->g uniformly
on both circles, after the finite k factors have been removed. This
last removal can also be made directly in the convergent residual
product, avoiding division at its removable points. Passing the modulus
inequalities to the limit therefore gives simultaneous bounds for M_s
and m_1 with a positive lower product. Subtract their real logarithms,
retain the exact first omitted scalar factor, and apply (14) to all
later factors:

\[
\log(M_s/m_1)
 \le \log\frac{1+sa}{1-a}
       +\sum_{p\ne p_J}\left(\log(1+s t_p)-\log(1-t_p)\right)
 \le \log\frac{1+sa}{1-a}
                    +\frac{1+s}{1-a}\frac R4 V(T).
\]

This proves (2)–(3). The minimum and maximum are over different circles;
the argument supplies uniform bounds on each circle separately and
does not assume that their extremizers coincide.

**4. Finite factors and the certified data interface.** Substitute (3)
in L835(4) to obtain the sufficient expression (4). No finite factor
has canceled. For an endpoint-only bound, 0<x_j<=q<s<1 gives

\[
T_s=\sum_{i=0}^{k-1}B_i\Lambda_i
                   \le k(1+q)^{k-1},\qquad
d_s\ge(s-q)^k,\quad d_1\ge(1-q)^k.
\]

There are exactly i+(k-i-1)=k-1 factors in each B_i Lambda_i;
each is at most 1+q because s<1. For s=(1+q)/2, s-q=(1-q)/2.
Consequently

\[
\log\mathcal C(s)\le\mathcal B(s)+2\log k
 +(2k-2)\log(1+q)+k\log2-2k\log(1-q).                 \tag{15}
\]

In particular even the coarse version pays for k packet factors in
each lower product and the whole k-term numerator sum.

The indexed intervals imply R<=R_+, q<=q_+, a<=a_+ and s<=s_+.
For q use the exact identity q=2 gamma_k^2/(gamma_k^2+T^2),
increasing in gamma_k and decreasing in T; for a use
a=(1+(gamma_k/T)^2)/2. These identities retain the correlation defining
the exact R; no unrelated rational radius replaces it. u<v ensures
q_+<1 and a_+<1 even if separate interval division of R/(4T^2) would
overestimate its upper bound. Every term of (2) is increasing in each
of its positive variables s,a,R,V when the others are fixed, so (5)
is an upper bound for \(\mathcal B(s)\). All logarithms have positive
arguments separated from zero by specified rational numbers. Standard
outward interval arithmetic for real logarithms and pi yields finite
rational V_+, B_+, C_+; no infinite zero sum is part of that evaluation.
Cancellation in (1) can affect sharpness but not validity of its upper
interval bound. It does not require V to be monotone on [v,w].

The remaining q terms in (15) are increasing on (0,1), so replacing
q by q_+ gives (6). Finally L835 gives exactly
\(\log\delta_r(s)=\log\mathcal C(s)+(r+k+1)\log s\). Since r+k+1>0 and
log s<=log s_+<0, (7) follows. Setting r=m+1 proves the sufficiency
of (8), with exponent m+k+2, and the required strict inequality.
For any finite C_+, the right side of (7) tends to minus infinity;
thus a sufficient integer rank is computable **given** the certified
indexed intervals. This is an interface, not a claim that those
records or the overlap certificate have already been supplied.

No use is made of enlarged finite-PF applicability. L835 supplies the
conditional sign transfer, and L832 only the established PF6001 range.
Even a successful later overlap at this one k would leave all growing
shifts and the main all-degree mixed-positivity gap unresolved. The
step659 hybrid-ratio and step667 signed-composition stops are not
reopened; neither mechanism is a premise here.

### Conceptual audit — 2026-11-06

The independently scoped audit passes (1)–(8) without a mathematical
correction. The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-06-residual-envelope-audit-scope.md`.
The cited product and count theorems, the actual simple packet in L834
and the relative bound in audited L835 are retained as inputs; their
source computations and complete manuscripts are not re-audited here.
This validates a local specialization, not new product or count theory.

**Endpoint and integral check.** At the selected ordinate T the inclusive
count is exactly J, not J-1 or J-1/2. In (10) every zero at or below T
contributes zero, including the one at T; a zero at U_0 contributes
U_0^(-2). Repeating these identities for each order validates the formula
even if later ordinates coincide. The count bound controls both the
vanishing upper endpoint and the integrable tail. As an independent
check of the integrated expression, put W(T)=V(T)+J/T^2. Differentiation
of (1), with J held fixed, gives

\[
W'(T)=\frac{1-\log(T/(2\pi))}{\pi T^2}
       -\frac{2(b\log T+d)}{T^3}
      =-\frac{2U(T)}{T^3},\qquad W(T)\longrightarrow0.
\]

Thus the main coefficient, the b/2 term and the full -J/T^2 subtraction
in (11) are correct. Positivity of V(T) follows from the actual remaining
verified zeros and S(T)<=V(T), without a decimal estimate of T.

**Product and limiting check.** The normalization G(-z)/a_0 leaves
F(0)=1, and L832's genus-zero product has no unaccounted exponential.
On positive-height representatives p=-4(rho-1/2)^2 is injective and
preserves orders, while reflection to negative height gives the same
factor. L834's simple ordering makes p_J the only residual factor at
height T. All others have gamma>T, and (12) gives (13) with factor R/4,
not R/8 and not R/2. This retains every possible off-line factor.

The full residual sum of t_p is finite, including the separate t_(p_J)=a.
The estimate -log(1-t_p)<=t_p/(1-a) bounds the sum of the nonnegative
lower-product logarithmic costs. Consequently their exponentiated
negative sum is strictly positive. This step is stronger than finite
nonvanishing and justifies the limiting lower bound uniformly on the
unit circle. Compact convergence supplies the actual quotient after
removable division; the scalar upper product is also finite. Taking
maximum and minimum on the two separate circles is therefore legitimate.
Applying (14) only after removing p_J gives exactly (2), with no omitted
first factor and no complex logarithm branch.

**Interval and overlap check.** Each summand B_i Lambda_i has exactly
k-1 factors, giving T_s<=k(1+q)^(k-1). The two denominator products each
contain k factors. With s-q=(1-q)/2 this yields the coefficient k log2
and the full cost -2k log(1-q) in (15). Substitution r=m+1 in L835's
exponent r+k+1 is m+k+2, with strict negativity required throughout.

For the endpoint interface, q=2 gamma_k^2/(gamma_k^2+T^2) is increasing
in gamma_k and decreasing in T, and a=(1+(gamma_k/T)^2)/2 has the same
directions. Hence u<v certifies q<=q_+<1 and a<=a_+<1, while w gives
R<=R_+. These are simultaneous upper bounds on quantities defined from
the exact R; they need not be simultaneously attained. The expression
(2) is increasing in s,a,R,V on the positive domain V>0, a<1. Interval
evaluation of V must retain the negative -J/T^2 term with outward
rounding but needs no monotonicity of V. All further replacements in
(6) increase the upper bound. Since r+k+1>0, replacing log s by
log s_+ also increases it, proving the direction in (7).

For an effective rank, the rational s_+<1 allows a certified logarithm
upper bound that is itself strictly negative, after refinement if
necessary. A fixed finite C_+ then makes the upper bound negative for
some integer r. This verifies computability conditional on the stipulated
indexed data, not possession of that data or of a numerical rank.
An interval enclosing zero does not prove (8), and a failed sufficient
bound does not prove a negative minor. L832 still supplies only PF6001
locally; no enlargement, actual overlap or growing-shift result is
established here. The direct mathematical inputs in the DAG are unchanged.

## Mathlib

Full matching coverage has not been checked; no absence claim is made.
Finite partial summation, real logarithm inequalities, uniform compact
product convergence and interval estimates are standard supporting
mathematics. The complete actual-Xi envelope, source constants, indexed
zero-data interface and conditional overlap specialization are not
claimed to be formalized. The conceptual audit above is informal and
does not change this unchecked formal-coverage status.
