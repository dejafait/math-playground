# L545 — Primary ideal cubic large-sieve import

## Hypotheses

Let O=Z[omega], omega=exp(2 pi i/3), and lambda=1+2omega.
All ideals below are nonzero integral ideals prime to lambda. Write
q_a=N(a). Use the retained primary conventions: O is a PID and each
such ideal a has exactly one generator a^# congruent to 1 modulo 3.
These generators multiply. This is the arithmetic convention in L544's
hypotheses; its quadratic theorem and retained quadratic reciprocity
identity are not inputs here.

For primary elements use the usual cubic residue symbol, extended by
zero when numerator and denominator have a common prime. On a prime
denominator pi not dividing 3 it is the cubic root of unity congruent
to x^((N(pi)-1)/3) modulo pi for pi not dividing x; extend
multiplicatively over denominator factors. Put (x/1)_3=1, including
x=1. For primary ideals define (v/u)_3=(v^#/u^#)_3. In particular,
(1/u)_3=1, and collisions have value zero. The inverse of a nonzero
symbol is its conjugate; inverse notation at collisions means zero,
rather than division by zero.

Let U,V>=1 be real. Rows u and columns v are ideal-squarefree and
prime to lambda, with q_u<=U and q_v<=V. Let z_v be arbitrary complex
coefficients on any fixed subset of these columns, independent of u.
No exclusion of primes above 2 or of conjugate-prime pairs is imposed.
Import Heath-Brown's Theorem 2 in the manuscript version cited below.

## Conclusion

For every epsilon>0,

\[
 \sum_{\substack{u\ {\rm sf},\ (u,\lambda)=1\\q_u\le U}}
 \left|\sum_{\substack{v\ {\rm sf},\ (v,\lambda)=1\\q_v\le V}}
          z_v(v/u)_3\right|^2
 \ll_\epsilon (UV)^\epsilon
       \{U+V+(UV)^{2/3}\}\sum_v|z_v|^2.                 \tag{1}
\]

Fixed row restrictions and fixed coefficient supports are allowed.
The same charge holds for the conjugated matrix or its transpose,
with the corresponding row/column lengths. This supplies L542 (2)
under its retained identification of chi_P(j)^(-2) with the stated
cubic-symbol orientation. No new reciprocity identity is proved here.
This is an application of a known theorem, with no improved bound.
It supplies neither arbitrary two-index masks nor a nonsquarefree
extension, structural reflection, global closure or Xi positivity.

## Proof

The imported result is D. R. Heath-Brown, *Kummer's conjecture for cubic
Gauss sums*, Israel J. Math. 120A (2000), 97–124, Theorem 2,
[DOI](https://doi.org/10.1007/s11856-000-1273-y). The inspected version
is the undated 26-page
[author manuscript](https://www.researchgate.net/profile/Roger-Heath-Brown/publication/254847691_Kummer%27s_conjecture_for_cubic_Gauss_sums/links/54db67950cf2ba88a6901164/Kummers-conjecture-for-cubic-Gauss-sums.pdf),
printed pp. 3–4. Its theorem gives the factor
(MN)^epsilon{M+N+(MN)^(2/3)} for arbitrary complex coefficients,
with both sums restricted to squarefree elements congruent to 1
modulo 3. The journal typesetting and full analytic proof are not
independently audited. The ready source comparison also inspected
Section 4 pp. 15–16 (support and orientation), Lemma 7's common-divisor
argument pp. 19–20, and Section 6 pp. 20–22 (primitive/CRT cases).
None of those arguments is reproved or strengthened in this application.

### Ideal-to-element bijection and coefficient norm

The map a -> a^# is a bijection between integral ideals prime to
lambda and elements congruent to 1 modulo 3: existence and uniqueness
are the retained primary convention, and an element congruent to 1
modulo 3 is prime to lambda. Its principal ideal recovers a.
Factorization in the PID shows that a is ideal-squarefree exactly
when a^# has no squared prime-element divisor. Further,
N(a^#)=N((a^#))=q_a. Thus neither squarefreeness nor either norm
cutoff changes. In particular ideal-squarefreeness does not require
squarefreeness of the rational integer q_a.

Define c_n=z_v if n=v^# for an allowed column v, and c_n=0 for all
other elements n. There is exactly one n for each column and no
associate multiplicity, so

\[
 \sum_{\substack{n\equiv1\ (3)\\n\ {\rm sf}}}|c_n|^2
       =\sum_v|z_v|^2.
\]

Every nonzero c_n lies in N(n)<=V. With M=U and N=V in Theorem 2,
the row bijection and the definition (v/u)_3=(v^#/u^#)_3 identify
the two finite quadratic norms exactly, proving (1).

### Support, zeros and units

The primary condition removes only lambda-prime factors. In particular
the prime above 2 is allowed (the ideal (2) has primary generator -2).
If the distinct primes above a split rational prime are both factors
of an index, the element is still squarefree; the resulting repeated
rational-norm factor is irrelevant. No rational-prime-squarefree
restriction has been substituted for the theorem's element condition.

A common prime ideal of u and v corresponds exactly to a common
prime-element factor of u^# and v^#. The source symbol then vanishes
exactly as in (1); no deletion of colliding entries is needed. The
unit ideal corresponds to the single primary unit 1. Empty products
give (x/1)_3=(1/u^#)_3=1. Theorem 2's stated squarefree-primary
support includes this unit; its statement has no nonunit restriction.

For 1<=U or V in any bounded range, the same finite-support theorem
applies, with norm-one indices retained. Empty supports contribute
zero. Fixed column restrictions were already implemented by zero
extension. Restricting the final nonnegative row sum can only decrease
it. There is no inference of monotonicity for a column sum inside an
absolute square. An additional fixed prime exclusion, such as L542's
good supports, is precisely such a row/column restriction; it is not
necessary for (1) itself. A mask varying jointly with u and v is not
covered by this argument.

### Complex conjugation and transpose

Let A have rows u, columns v and entries (v/u)_3 on the full finite
cutoffs, including collision zeros. Put
Q=C_epsilon(UV)^epsilon{U+V+(UV)^(2/3)}. The theorem says
||Az||_2^2<=Q||z||_2^2 for every complex vector z.
For its entrywise conjugate, bar(A)z=overline(A bar(z)), so the
same bound holds without any change of coefficient norm. Finite
Hilbert-space duality gives ||A^*y||_2<=sqrt(Q)||y||_2:
test against unit z and use |<y,Az>|<=||y||_2||Az||_2.
Since A^t=overline(A^*), conjugation then gives the same bound for
A^t, with U,V interchanged; the charge is symmetric in U,V.
Thus transpose is not incorrectly identified with adjoint for these
complex entries. Symbol inversion is bar(A) on noncolliding entries,
and its zero extension agrees at collisions. Fixed unit-modulus row
or column factors also preserve the norm, by diagonal isometries.

The direct matrix in (1) needs no reciprocity swap at all. L542 uses
its retained arithmetic identification with this matrix or the stated
conjugate/transpose conventions. Any different index-dependent phase
not covered by that identification would need a separate justification;
no arbitrary phase invariance is asserted. Its coefficient norm is
unchanged by every operation just used, and no length or logarithmic
loss occurs. All operations are finite.

## Mathlib

Coverage of the full cubic large sieve and this primary-ideal
specialization has not been checked. No matching Mathlib theorem is
claimed. Supporting algebra, residue symbols or finite-dimensional
duality alone would not establish the imported analytic estimate.
