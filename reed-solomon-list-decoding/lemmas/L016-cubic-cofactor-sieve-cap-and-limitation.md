# L016 — Cubic-cofactor sieve cap and its absolute-sum limitation

## Hypotheses

Use L015's fixed instance: Q=65537, E=F_Q, F=F_{Q^28}, H<=E^* of
order 1024, k=64, A=66, and every interleaving width m>=1. Centers
have a degree-exactly-67 scalar polynomial over E in the first row and
zero in all remaining rows. Messages have degree strictly less than 64.
Use the closed simultaneous column-Hamming metric of the
[pinned model](../foundations/02-pinned-list-model.md). Put

\[
 \tau=Q^{28}/2^{128},\quad C=\binom{1024}{66},\quad
 D_2=\binom{579}{66},\quad D_3=\binom{835}{66}.
\]

Fix psi(t)=exp(2 pi i t/Q). For u=(u_1,u_2,u_3) in E^3 put

\[
 f_u(X)=u_1X+u_2X^2+u_3X^3,\quad
 F_A(u)=\sum_{\substack{S\subseteq H\\|S|=A}}
                       \psi\left(\sum_{x\in S}f_u(x)\right),\quad
 R(u)=\sum_{z\in E}\psi(f_u(z)).
\]

For nonzero u let r(u) be the degree of f_u. Define the particular
absolute-value allowance obtained by using one sieve cap in each class:

\[
 \mathcal E_{\rm abs}=Q^{-3}\left(
   D_2\sum_{r(u)=2}|R(u)|+D_3\sum_{r(u)=3}|R(u)|\right).
                                                               \tag{1}
\]

## Conclusion

Uniformly over these centers, the entire list size M satisfies

\[
 M\le\lfloor U\rfloor,\quad
 U=\frac C{Q^2}+\frac{513(Q-1)}{Q^2}D_2
                        +\frac{769(Q-1)}Q D_3,\quad
 320297< U/\tau <320298.                               \tag{2}
\]

Thus (2) does not certify that this family lies below threshold. It
also gives no list above threshold. A stronger limitation of this
specific method is

\[
 \sum_{u_3\ne0}|R(u)|^2=Q^3(Q-1),\qquad
 \mathcal E_{\rm abs}\ge\frac{Q-1}{769}D_3>35496\tau.   \tag{3}
\]

Consequently substituting the same D_3 for every cubic F_A(u) and
then taking absolute values cannot certify the threshold, even with
exact cofactor magnitudes. This is a lower bound on that method's
allowance, not a lower bound on the actual Fourier error or list size.
It does not rule out correlated cancellation, smaller nonuniform
subset-sum bounds, or effective use of L015's subtractive term.

Integer rounding is not the decisive loss: the rational square-root
refinement described below gives an upper-to-threshold ratio between
294741 and 294742, and its analogous absolute allowance is greater
than 32749 times threshold. No full-code grid bound changes.

## Proof

**Known inputs and scope.** The
[saved SPECIALIZE assessment](../drafts/literature/2026-10-04-degree-sixty-seven-linear-cofactor.md)
explicitly approves this upper-test subtarget. Import Lai, Marino,
Robinson and Wan,
[Moment subset sums over finite fields, arXiv:1910.05894v2](https://arxiv.org/pdf/1910.05894v2#page=6),
2019-10-19, Proposition 1, printed p. 6: a nontrivial additive character
sum of a polynomial of degree r on {x^d:x in E} is at most r sqrt(Q)
when the characteristic does not divide r and (d+1)^2<=Q. Import
Li and Wan,
[Counting polynomial subset sums, arXiv:1507.06329v1](https://arxiv.org/pdf/1507.06329v1#page=5),
2015-07-22, Theorem 2.1 and Corollary 2.2, printed p. 5, for the
weighted distinct-coordinate sieve, and Lemma 2.7, p. 7, for its cycle
polynomial. These inputs are cited, not reproved.

The local work checks the three-moment/cofactor Fourier normalization,
phase degrees and cycle lengths, applies the imported estimates and
tests their finite constants. L015 supplies the entire-list dictionary,
normalization of all degree-67 centers, extension-field completeness and
every-m applicability. This is REPRODUCTION of known scalar tools,
with an informative negative comparison, not a novelty claim.

**Cofactor Fourier formula.** Let v be the first three power sums
corresponding to the normalized center's prescribed coefficients, as
in L015, and let P_s(v) denote its unordered moment fiber. Orthogonality
gives

\[
 P_A(v)=Q^{-3}\sum_{u\in E^3}\psi(-u\cdot v)F_A(u).
\]

L015's incidence formula, including the repeated-root cases, therefore is

\[
 I(v)=\sum_{z\in E}P_A(v-(z,z^2,z^3))
     =Q^{-3}\sum_u\psi(-u\cdot v)F_A(u)R(u),\quad
 M(v)=I(v)-66P_{67}(v)\le I(v).                        \tag{4}
\]

At u=0, F_A(0)=C and R(0)=Q, so the trivial term is C/Q^2.
For degree-one phases, R(u)=0 by complete-field additive orthogonality.
This eliminates their contributions, rather than paying a factor Q
for each residual root. No usable positive lower bound for P_67 is
supplied here, so (4)'s nonnegative subtraction is discarded only for
this upper test; I is not equated with the list.

**Phase and cycle bounds.** The monomial image x^64 on E is H union
{0}, with (64+1)^2=4225<=Q. For r=2 or 3, Proposition 1 and deletion
of the zero term give

\[
 \left|\sum_{x\in H}\psi(f_u(x))\right|
            \le r\sqrt Q+1.
\]

For the complete residual sum, use the same proposition with d=1;
its image is E and (1+1)^2<=Q, so |R(u)|<=r sqrt(Q).
The exact comparisons 4Q<513^2 and 9Q<769^2 yield respectively

\[
 \begin{array}{c|cc}
 r&\text{H cycle cap}&\text{complete cofactor cap}\\\hline
 2&514&513\\
 3&770&769
 \end{array}                                          \tag{5}
\]

Here the displayed integers are strict upper bounds. Every sieve
cycle length j is between 1 and 66<Q, so f_{ju}=j f_u retains its
degree and nontriviality. The characteristic does not divide 2 or 3.
Thus every cycle uses the same valid cap for its phase class.

Apply the imported weighted sieve to the symmetric ordered weight
\(\prod_i\psi(f_u(x_i))\) on H^A. Division by A! gives the unordered
sum F_A(u). For a permutation sigma the cycle factor is
\(\prod_{\gamma} \sum_{x\in H}\psi(|\gamma| f_u(x))\).
The triangle inequality and the imported constant-weight cycle identity
give

\[
 |F_A(u)|\le\frac1{A!}\sum_{\sigma\in\mathfrak S_A}
                         w_r^{\#\text{cycles}(\sigma)}
       =\frac{w_r(w_r+1)\cdots(w_r+A-1)}{A!}=D_r,
 \qquad w_2=514,\quad w_3=770.                        \tag{6}
\]

The arbitrary-domain sieve is applicable on H. No subfield hypothesis,
independence of moment coordinates, or full-field root-domain formula
is used. In particular A! has not disappeared from the count.

There are Q(Q-1) degree-two parameters and Q^2(Q-1) degree-three
parameters. Substitution of (5)--(6) into (4) proves the cap U in (2).
Integrality gives the floor. L015 then transfers it to the entire
normalized or translated center list over F for every m>=1.

**Limitation even with exact cofactor magnitudes.** Complete-field
orthogonality, with z,w both in E, gives

\[
 \sum_{u\in E^3}|R(u)|^2
 =\sum_{z,w}\sum_u\psi\bigl(u_1(z-w)+u_2(z^2-w^2)
                                     +u_3(z^3-w^3)\bigr)=Q^4.
\]

Indeed the u_1 sum already forces z=w; each of the Q diagonal pairs
then contributes Q^3. Restricting to u_3=0 similarly gives Q^3, since
there are two character coordinates. Subtraction proves the norm
identity in (3), without requiring an individual cubic sum formula.
Because |R(u)|<769 for u_3!=0,

\[
 \sum_{u_3\ne0}|R(u)|^2\le769\sum_{u_3\ne0}|R(u)|,
 \quad
 Q^{-3}\sum_{u_3\ne0}|R(u)|\ge(Q-1)/769.
\]

Using the nonnegative quadratic part in (1) proves its lower bound.
The triangle calculation based on (6) has allowance exactly (1)
before its cofactor magnitudes are capped. Its cubic portion alone
already exceeds the desired threshold, so evaluating those magnitudes
exactly cannot rescue this constant-weight absolute-value calculation.
This is not a claim that (6) is attained, that any phases align, or
that an actual error is large. Smaller or correlated Fourier estimates
are not constrained by this allowance.

**Exact comparisons and refinement.** Integer binomial multiplication
and rational arithmetic verify

\[
 2^{292}<D_2<2^{293},\quad 2^{328}<D_3<2^{329},\quad
 2^{338}<U<2^{339},\quad 2^{320}<\tau<2^{321},
\]

and, with all denominators cleared,

\[
 320297\tau<U<320298\tau,\quad
 416\tau<D_3<417\tau,\quad
 35496\tau<(Q-1)D_3/769<35497\tau.                    \tag{7}
\]

For comparison, the existing unconditional support bound L001 already
gives \(\lfloor C/\binom{960}{2}\rfloor\); its ratio to tau is between
1050 and 1051. It is stronger than (2), and also exceeds threshold.
Thus the new cap does not improve the notebook's list upper bound.
The useful result is the limitation of the screened calculation, not
a tighter list estimate. L001 is a comparison, not an input to (2)--(3).

For an independent refinement set t=256+1/512, so t^2>Q, and
replace w_r by rt+1 and the cofactor cap by rt. Define
\(D_r^*=\prod_{j=0}^{65}(rt+1+j)/66!\). The same proof applies to
these rational weights, giving

\[
 U^*=C/Q^2+2t(Q-1)D_2^*/Q^2+3t(Q-1)D_3^*/Q,
 \quad 294741\tau<U^*<294742\tau<U.
\]

The exact norm identity yields the corresponding allowance lower bound
\((Q-1)D_3^*/(3t)\), strictly between 32749 tau and 32750 tau.
Thus simply removing the integer rounding still misses the threshold.

**Checks and limits.** Run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/verify_cubic_cofactor_upper.py`.
Its results are saved in
`scripts/coefficient-fibers/cubic-cofactor-upper-results.json`.
All fixed-instance comparisons above are exact integer or rational
certificates, not numerical evidence of actual lists. The script does
not enumerate the 1024-point fibers.

On the order-8 subgroup of F_17 with A=4, an exact three-coordinate
group-ring computation compares the signed permutation sieve with
distinct ordered tuples, including the A! conversion. Convolution with
the residual curve agrees with direct subset/cofactor incidence counts.
An independent exact cyclotomic calculation over every u_3!=0 verifies
the complete-cofactor norm identity; no floating-point amplitudes enter.
These audit the new normalization and method-limitation calculations.
They do not replace the cited estimates or resolve the degree-67 lists,
arbitrary-center maximum, or sharp full-code boundary.

## Mathlib

Full cubic-cofactor/proper-subgroup/interleaved threshold statement and
the absolute-sum limitation: **not checked** in Mathlib. Formal coverage
of the cited monomial character estimate and weighted sieve: **not checked**.
Supporting character orthogonality, the Parseval calculation, cycle
polynomials, finite-field cyclicity and exact binomial arithmetic:
**not checked**. The direct primary links above are supporting scalar
results, not a full matching theorem. The pinned ArkLib model definitions
remain **present** as recorded in foundations/ and do not prove this cap.
