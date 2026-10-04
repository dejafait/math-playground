# L015 — Degree-67 lists and residual linear factors

## Hypotheses

Take Q=65537, E=F_Q, F=F_{Q^28}, and H<=E^* of order n=1024,
as in C012a. Put k=64 and A=66. Messages have degree strictly less
than k in each of m>=1 rows. Use the closed simultaneous column-Hamming
metric from the [pinned model](../foundations/02-pinned-list-model.md).
The list threshold is epsilon*|F|=Q^28/2^128.

For a subset S of H let e_j(S) be its j-th elementary symmetric sum.
For b,c,d in E write

\[
 R_{b,c,d}(X)=X^{67}-bX^{66}+cX^{65}-dX^{64},
 \qquad Y_{b,c,d}(x)=(R_{b,c,d}(x),0,\ldots,0).
\]

Let M(b,c,d) be the entire list size at this center with at least
66 simultaneous agreements. Define the incidence count

\[
 I(b,c,d)=\left|\left\{(S,z):S\subseteq H,\ |S|=66,\ z\in E,
 \ e_1(S)+z=b,\ e_2(S)+ze_1(S)=c,
 \ e_3(S)+ze_2(S)=d\right\}\right|,                    \tag{1}
\]

and let

\[
 Z(b,c,d)=|\{T\subseteq H:|T|=67,
                         (e_1(T),e_2(T),e_3(T))=(b,c,d)\}|.
\]

## Conclusion

Every candidate is represented by a pair in (1) through the polynomial
tuple

\[
 \left(R_{b,c,d}(X)-(X-z)\prod_{x\in S}(X-x),0,\ldots,0\right).
                                                               \tag{2}
\]

Every row of every such candidate has coefficients in E, even though
messages are allowed over F. The agreement set is S when z is outside
H or in S, and is S union {z} when z is in H but outside S. A candidate
with 66 agreements has one representation; a candidate with 67 has
67 representations. Therefore, for every m>=1,

\[
 M(b,c,d)=I(b,c,d)-66Z(b,c,d),\qquad
 0\le M(b,c,d)\le I(b,c,d).                            \tag{3}
\]

For v=(v_1,v_2,v_3) in E^3 define the unordered moment fiber

\[
 P_s(v)=|\{S\subseteq H:|S|=s,
                 \sum_{x\in S}x^j=v_j\ (j=1,2,3)\}|.
\]

Put v=(b,b^2-2c,b^3-3bc+3d). Then the exact moment version of (3) is

\[
 M(b,c,d)=\sum_{z\in E}P_{66}(v_1-z,v_2-z^2,v_3-z^3)
                       -66P_{67}(v).                 \tag{4}
\]

These formulas cover every degree-exactly-67 scalar center over E,
with the other rows zero, after a scalar normalization and translation
by a message polynomial. They give the exact average over E^3:

\[
 \overline M=\frac{Q\binom{1024}{66}-66\binom{1024}{67}}{Q^3},
 \quad
 \max_{b,c,d}M(b,c,d)\ge\lceil\overline M\rceil.         \tag{5}
\]

The exact arithmetic comparison is

\[
 2^{316}<\lceil\overline M\rceil<2^{317}<2^{320}
       <Q^{28}/2^{128},\qquad
 \frac{11094}{100000}
 <\frac{\overline M}{Q^{28}/2^{128}}
 <\frac{11095}{100000}.                               \tag{6}
\]

Thus this averaging lower certificate is inconclusive for unsafety.
No maximum fiber or uniform upper bound below threshold is proved.
The full-code bound t_star<=958 from C012a is unchanged.

## Proof

**Known result and the local specialization.** The
[prior SPECIALIZE assessment](../drafts/literature/2026-10-04-degree-sixty-seven-linear-cofactor.md)
approves the cofactor dictionary and its later effective-count test.
Import the scalar incidence/exact-root framework of Gao,
[Counting polynomials over finite fields with prescribed leading coefficients and linear factors, arXiv:2105.12845v3](https://arxiv.org/html/2105.12845v3),
2022-11-10, Section 2, Proposition 1 and Theorem 1, equations (7)-(8),
and Gao and Li,
[Improved error bounds for the distance distribution of Reed-Solomon codes, arXiv:2205.02277v1](https://arxiv.org/html/2205.02277v1),
2022-05-04, Theorems 4-5, printed pp. 4-5, equations (7)-(14).
These distinguish chosen-root incidences from exact agreement counts
for arbitrary domains. Li and Wan,
[Distance Distribution in Reed-Solomon Codes, arXiv:1806.00152v3](https://arxiv.org/html/1806.00152v3),
2019-07-30, Theorem 5.1 and its proof through equation (5.2), printed
pp. 10-13, explicitly use a monic root product times a residual factor.
Their full-field error estimates are not applied to the proper H.

The verification below specializes this known dictionary, including the
source's possible sign-convention difference, the residual coefficient
field, simultaneous interleaving and the 66-versus-67 multiplicities.
It does not reprove the general counting theorems. This is REPRODUCTION,
not a claim of progress beyond the checked literature.

**Cancellation and agreement sets.** The first four terms of the
root product g_S for a 66-subset are

\[
 g_S(X)=X^{66}-e_1(S)X^{65}+e_2(S)X^{64}-e_3(S)X^{63}
                       +\text{lower terms}.
\]

Multiplication by X-z gives coefficients

\[
 (X-z)g_S=X^{67}-(e_1+z)X^{66}+(e_2+ze_1)X^{65}
                           -(e_3+ze_2)X^{64}
                           +\text{terms of degree less than }64.
\]

Exactly (1)'s three conditions cancel every term of degree at least 64
in (2). Its first row is therefore a valid message, and its coefficients
are in E. At an evaluation column its difference from the center is
(X-z)g_S in the first row and zero in the other rows. This product's
distinct roots in H are exactly S, together with z if z belongs to
H outside S. If z belongs to S it is a repeated root and adds no
agreement column. Thus (2) always belongs to the required closed ball.

**Completeness over F.** Let (p_1,...,p_m) be an F-valued message tuple
with at least 66 simultaneous agreements, and choose any 66-element
subset S of its agreement columns. The monic polynomial R-p_1 has
degree 67. The factor theorem forces division by g_S, and the quotient
is a monic linear polynomial X-z with z initially in F. Comparing its
degree-66 coefficient gives

\[
 z=b-e_1(S)\in E.
\]

The degree-65 and degree-64 comparisons give the other two conditions
in (1). Hence p_1 equals (2)'s first row and has coefficients in E.
Every other p_j vanishes on S and has degree at most 63, so the
nonzero-polynomial root bound forces p_j=0. In particular neither the
ambient extension nor the interleaving width introduces further candidates.

**Incidence multiplicities.** The same root bound permits only 66 or
67 distinct agreement roots for a candidate. If there are 66, S must
be its entire agreement set, and its quotient fixes z uniquely. Thus
the candidate is represented once, including the repeated-root case.
If there are 67, write that full root set as T. Monicity and degree
give R-p_1=g_T. Comparing leading coefficients identifies T with one
of the subsets counted by Z. Conversely, every such T gives the valid
candidate R-g_T with exactly T as its agreement set. For each of the
67 choices of a root z in T, S=T minus {z} represents this candidate.
There are no other representations.

Different polynomial messages of degree less than 64 have different
evaluation words on 1024 distinct points, again by the root bound.
Thus the polynomial count is the codeword count. If M_66 denotes the
number with exactly 66 agreements, the incidence identity is

\[
 I=M_{66}+67Z,\qquad M=M_{66}+Z.
\]

Subtracting proves (3). Merely equating I with the list would overcount
each fully split 67-root difference by 66.

**Moment coordinates.** Q>3, so Newton's first three identities give

\[
 p_1=e_1,\qquad p_2=e_1^2-2e_2,\qquad
 p_3=e_1^3-3e_1e_2+3e_3.                              \tag{7}
\]

The map from (e_1,e_2,e_3) to (p_1,p_2,p_3) is triangular and
bijective, since 2 and 3 are invertible in E. For a fixed residual root z,
the constraints (1) prescribe

\[
 e_1=b-z,\quad e_2=c-bz+z^2,\quad
 e_3=d-cz+bz^2-z^3.
\]

Substitution into (7) yields p_j=v_j-z^j for j=1,2,3.
Equivalently, (X-z)g_S has the roots S and one further copy of z;
Newton sums add z^j even when z already belongs to S. Summing the
fixed-z moment fibers counts I, while applying (7) to a 67-subset
identifies Z=P_67(v). Formula (4) follows. The residual sum ranges
over E, not over the much larger field F.

**Every degree-67 center.** Write any f in E[X] of degree 67 uniquely as

\[
 f=aR_{b,c,d}+h,\qquad a\in E^*,\quad \deg h<64.
\]

The bijection p_1=h+a\widetilde p_1 on scalar messages preserves
the first-row agreement equation with f and R, respectively.
Other rows of a candidate with 66 agreements must be zero by the
argument above. Thus the entire tuple list has exactly M(b,c,d)
members. This includes nonmonic centers and arbitrary lower coefficients.
It applies over F as well as E because a is nonzero in both fields.

**Averaging and the actual threshold.** Every pair consisting of a
66-subset S and a residual root z in E contributes to exactly one
triple (b,c,d), determined by (1). Every 67-subset contributes to
exactly one triple in Z. Summing (3) over the Q^3 triples therefore gives

\[
 \sum_{b,c,d}M(b,c,d)=Q\binom{1024}{66}-66\binom{1024}{67}.
\]

Finite averaging and integrality prove (5). In particular, the mean
is smaller than the incidence mean binomial(1024,66)/Q^2 by the factor

\[
 1-\frac{66\cdot958}{67Q}=\frac{4327751}{4390979}.
\]

The integer/rational certificate below checks (6) by clearing
denominators. For example, the averaging lower bound is exactly

```text
237072121557391801719718231055195813911582641578585239026567557786832456880701985814097976318668
```

C012a supplies 2^320<Q^28/2^128<2^321. The corrected lower certificate
is about 0.111 times the threshold, so it supplies no unsafe witness.
It is a lower bound on the maximum, not an upper bound on any actual
fiber. Both a certified large fiber and a uniform upper comparison
remain possible later outcomes. Formula (4) makes the approved
three-moment/cofactor upper test precise; no character bound is applied
in this step.

**Independent checks.** Run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/verify_linear_cofactor.py`.
Output is saved in `scripts/coefficient-fibers/linear-cofactor-results.json`.
The fixed-instance checks use exact binomial integers and rational
threshold comparisons; they do not enumerate the 1024-point fibers.

On the order-8 subgroup of F_17 with k=2, A=4, the script checks all
17^3 leading-coefficient centers. It compares the pair construction
and multiplicity correction with independently exhausted degree-less-than-2
messages, and verifies the three power-sum signs. Representatives cover
the residual root outside H, repeated in S, and in H outside S.
For those representatives it exhausts scalar messages over F_{17^2}
using the basis 1,alpha with alpha^2=3, and also views the two components
as a width-two prime-field tuple. No candidate has a nonzero second
component. A nonmonic center with a nonzero lower translation checks
the normalization. These finite checks support the dictionary's
applicability; the factor/root proof gives the general every-m claim.

## Mathlib

Full degree-67/proper-subgroup/interleaved list dictionary and ambient
threshold comparison: **not checked** in Mathlib. Formal coverage of
the cited incidence/exact-root and residual-factor results: **not checked**.
Supporting Newton identities, factor and root theorems, finite-field
extensions and elementary counting: **not checked**. The direct primary
links above support the scalar framework, not a full matching library
theorem. The pinned ArkLib definitions are **present** as recorded in
the model; they fix the code and metric but do not establish this count.
