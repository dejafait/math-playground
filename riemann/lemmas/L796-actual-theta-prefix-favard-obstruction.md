# Lemma 796: actual theta-prefix Favard obstruction

## Hypotheses

Use the actual theta moments and polynomials of L795:

\[
 m_j=\int_0^\infty u^{2j}K(u)\,du,\quad
 R_j=\frac{j!m_j}{(2j)!m_0},\quad
 P_n(x)=\sum_{j=0}^n(-1)^j\binom nj R_jx^j.
\]

L021 supplies finite strictly positive moments. Use only the actual
gamma(0),...,gamma(3) enclosures of L791, with gamma(j)=j!m_j/(2j)!
and R_j=gamma(j)/gamma(0), as audited in step478. Their analytic error
bound, complex Cauchy coefficient estimate, evaluator and Decimal/backend
contracts are inherited from L778 through L791. They are not independently
reproved or formally verified here. None of L791's fitted model,
parameters, matching solution or model-root signs is a premise.

Set a=R_1, b=R_2, c=R_3, and let Q_n be P_n divided by its leading
coefficient, for 0<=n<=3. All these leading coefficients are nonzero.

## Conclusion

The unique monic-basis expansions through degree three are

\[
\begin{aligned}
 xQ_0&=Q_1+\alpha_0Q_0,\\
 xQ_1&=Q_2+\alpha_1Q_1+\beta_1Q_0,\\
 xQ_2&=Q_3+\alpha_2Q_2+\beta_2Q_1+\delta Q_0,
\end{aligned}
\]

where

\[
\begin{aligned}
 \alpha_0&=1/a,&\alpha_1&=2a/b-1/a,&\alpha_2&=3b/c-2a/b,\\
 \beta_1&=1/b-1/a^2,&
 \beta_2&=1/b+3a/c-4a^2/b^2,&
 \delta&=1/c+1/(ab)-2a/b^2.
\end{aligned}
\]

The following bounds are outward rational enclosures; every displayed
finite decimal denotes its exact rational value:

\[
\begin{split}
140.199017&\le\beta_1\le140.199018,\\
256.660342&\le\beta_2\le256.660343,\\
-645.225425&\le\delta\le-645.225424<0.
\end{split}
\]

Consequently the actual sequence cannot be a common nondegenerate
orthogonal polynomial sequence for a positive measure on R with finite
moments and positive polynomial norms. Already Q_0,...,Q_3 cannot be
pairwise orthogonal with positive norms for one positive Borel measure
with finite moments through degree six. This rules out that stronger
realization even before imposing positive support. It says nothing
against individual real-rootedness, a degree-dependent realization,
all-degree mixed positivity or RH. The result is a finite application
of a known necessary condition, not a new classification theorem.

## Proof

**Imported necessary condition.** NIST DLMF, Section18.2(iv),
[equation18.2.11_5](https://dlmf.nist.gov/18.2#E11_5) and
[equation18.2.11_6](https://dlmf.nist.gov/18.2#E11_6), gives the monic
three-term recurrence and beta_n=h_n/h_(n-1)>0 for a nondegenerate
positive-measure orthogonal sequence. The measure qualifications are
in [Section18.2(viii)](https://dlmf.nist.gov/18.2#viii). We import the
necessary direction, not the existence or uniqueness of a measure from
a finite prefix. Section18.2(vi)'s real-zero theorem explains the proposed
downstream use of orthogonality; no converse from individual roots is
used. Source hypotheses and the orthogonal-Jensen classification were
assessed in `drafts/literature/2026-11-05-theta-average-favard-interface.md`.
The calculation below is the only additional specialization needed.

**Exact normalization and expansion.** Directly from the binomial
definition, using R_0=1,

\[
 P_0=1,\quad P_1=1-ax,\quad P_2=1-2ax+bx^2,\quad
 P_3=1-3ax+3bx^2-cx^3.
\]

Their leading coefficients are 1,-a,b,-c, respectively. Positivity of
the moments makes a,b,c strictly positive. Thus

\[
 Q_0=1,\quad Q_1=x-1/a,\quad
 Q_2=x^2-2ax/b+1/b,\quad
 Q_3=x^3-3bx^2/c+3ax/c-1/c.
\]

Comparison of descending powers of x in xQ_n, n=0,1,2, gives exactly
the coefficients in the conclusion. For example, the x^2 comparison
at n=2 gives alpha_2=3b/c-2a/b; the x comparison then gives
beta_2=1/b-3a/c+(2a/b)alpha_2=1/b+3a/c-4a^2/b^2. The constant
comparison gives

\[
 \delta=1/c-\alpha_2/b+\beta_2/a
        =1/c+1/(ab)-2a/b^2.
\]

The basis is monic with distinct degrees, so these expansions are unique.
The program also expands all three residual identities exactly in the
Laurent polynomial ring Q[a^(+/-1),b^(+/-1),c^(+/-1),x]. Each residual
has no nonzero monomials. This is a finite coefficient calculation,
not a new theorem about orthogonal polynomials.

**Certified actual data and arithmetic.** The input is
`scripts/central-jacobi/fixed-model-certificate-476.json`, fields
`gamma/0` through `gamma/3`. Its SHA256 is
`2b429e4029fd7f50b30ea61b43d1be5aa22155b4c680c69440a716ff26643b2e`.
The step478 audit is `scripts/central-jacobi/audit-478/audit-report.json`.
The program checks that input hash, all original hashes recorded by the
audit, its PASS/no-failures status and its nineteen selected provenance,
coefficient-error, gamma-enclosure and positivity checks. These checks
identify the previously audited data; they do not replace or redo the
analytic evaluator audit. The full selected gamma intervals were
inspected, without substituting rounded approximations or model data.

All finite-decimal endpoints are parsed as exact fractions. For intervals
[l,u] and [r,s], addition uses [l+r,u+s], multiplication uses the minimum
and maximum of the four endpoint products, and reciprocal uses
[1/s,1/r] only when zero is excluded. These rules enclose every value
in the Cartesian product; correlations among the actual gamma values
can only make that product larger. There is no numerical rounding in
these operations. Compute a,b,c by interval division by gamma(0), then
evaluate each displayed alpha, beta and delta formula once. Every
denominator interval gamma(0), a, b, c, a^2, b^2 and ab has strictly
positive lower endpoint. For orientation conservative lower bounds
are gamma(0)>0.49, a>0.02, b>0.0004 and c>0.00001, which also bound
their required products away from zero. Complete exact denominator
and monic-divisor enclosures are retained in the output certificate.

To obtain the displayed rational bounds, multiply each exact lower
endpoint by 10^6, take its integer floor and divide by 10^6; use the
integer ceiling for each upper endpoint. The resulting beta and delta
enclosures are exactly those in the conclusion. No dependency-driven
rearrangement, fresh quadrature, precision change or degree extension
was needed. Both beta tests pass, while the forbidden-coefficient test
fails strictly. The failure is not inferred from a small approximate
residual or an interval that meets zero.

Run `python3 scripts/central-jacobi/favard_prefix_504.py` from this
notebook. The complete certificate is
`scripts/central-jacobi/favard-prefix-certificate-504.json`: exact input
intervals, input/program/audit hashes, nineteen selected audit checks,
symbolic formulas and zero residuals, every denominator, all recurrence
coefficients, full rational output enclosures, required values and
criterion failures. Outcome: ORTHOGONALITY_OBSTRUCTION; verification
failures: none. Python integer/Fraction implementation remains a
computer-assisted informal calculation, not formal verification.

**Application and scope.** Under common positive-measure orthogonality,
the necessary three-term recurrence at n=2 forbids Q_0 in xQ_2, so it
requires delta=0. For the finite-prefix assertion the same local
hypotheses suffice: pairing the displayed identity with Q_0 gives
delta*h_0, whereas symmetry gives
<xQ_2,Q_0>=<Q_2,xQ_0>=<Q_2,Q_1+alpha_0Q_0>=0. All other terms
paired with Q_0 vanish by the assumed orthogonality, and h_0>0.
Finite moments through six justify these pairings. This explicitly
checks the finite-prefix applicability of the cited necessity, without
reproving Favard's global theorem. The certified negative delta is a
contradiction. In particular arbitrary positive support, infinite
support, or an absolutely continuous density cannot rescue the common
measure premise. Failure of this premise is not failure of a necessary
condition for RH: common orthogonality was only a stronger sufficient
mechanism for real roots. Independent Xi signs remain open.

### Independent finite audit, 5 November 2026 — step506

Reused the approved SPECIALIZE assessment
`drafts/literature/2026-11-05-theta-prefix-favard-audit.md`. No mathematical
defect was found. This audit establishes the reliability of the existing
finite obstruction under its inherited contracts; it adds no new theorem
beyond the checked necessary condition.

**Normalization and local necessity.** L021's ordinary even coefficient
is (-1)^j m_j/(2j)!. With L791's convention for G, its ordinary w^j
coefficient is m_j/[8*4^j*(2j)!], hence gamma(j)=j!m_j/(2j)! exactly.
Dividing by gamma(0)=m_0 gives the stated R_j, and the leading
coefficients through degree three are precisely 1,-a,b,-c. The audit
retains L791's complex Cauchy estimate E_G/1600^j, rather than applying
an error estimate valid only on a real interval. It imports no fitted
model coefficients or model-root claim.

For the finite measure claim, finite absolute moments through six make
all products of Q_0,...,Q_3 integrable and make multiplication by x
symmetric in the particular pairings used. Orthogonality in the n=2
identity gives <xQ_2,Q_0>=delta*h_0. The n=0 identity instead gives
<Q_2,xQ_0>=<Q_2,Q_1+alpha_0 Q_0>=0. Thus delta=0 since h_0>0.
This uses neither an infinite extension nor an infinite-support
convention from the global Favard theorem. Moments through degree six
also make all four assumed squared norms finite. The contradiction is
therefore valid under the finite-prefix hypotheses as written.

**Independent arithmetic and complete evidence.** Run
`python3 scripts/central-jacobi/audit_506.py`. The checker imports neither
step504's interval class nor its symbolic implementation. It uses exact
Fraction endpoint tuples and integer polynomials with nonnegative
exponents. Clearing the three recurrence residuals by a, a^2*b and
a*b^2*c respectively gives the zero integer polynomial in each case;
all clearing factors are nonzero. For the last identity the forbidden
coefficient has numerator a*b^2+b*c-2*a^2*c and denominator a*b^2*c,
which agrees with the formula above.

The checker reads every endpoint of the four original gamma intervals,
rechecks their Cauchy-enlarged coefficient provenance and normalization,
checks the nineteen selected step478 records and the inherited hashes,
and compares every rational denominator, monic divisor, alpha, beta and
delta interval in the original certificate with its independent result.
It verifies the complete criterion/verification records and the outward
rounding of every displayed bound. The full delta endpoints were also
inspected using the bounded JSON inspector with --full on that field;
no rounded preview was treated as a certificate.

The fresh complete evidence is
`scripts/central-jacobi/audit-506/audit-report.json`: PASS, 45 checks,
no verification failures. Both beta intervals are strictly positive and
the reproduced delta enclosure is [-645.225425,-645.225424], strictly
below the required zero. Original scripts and certificates were not
overwritten; their hashes remain unchanged. This is independent finite
arithmetic checking, not independent attestation of the inherited
transcendental backend or formal verification of Python/Fraction.
The common-measure route stop is retained without a degree extension;
individual roots, other realizations and all-degree Xi signs remain open.

## Mathlib

Full matching-result coverage is unchecked, as are the specific monic
Favard theorem and theta-prefix interval specialization. No absence
claim or formal theorem is asserted. The local proof uses the cited
orthogonal-polynomial necessity, finite polynomial algebra and rational
enclosures, with the inherited analytic/software qualifications above.
