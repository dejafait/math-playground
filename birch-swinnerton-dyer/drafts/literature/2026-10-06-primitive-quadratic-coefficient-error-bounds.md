# Coverage request for a finite primitive quadratic-coefficient certificate

TARGET: Assess Stein--Wuthrich's ordinary modular-symbol error bounds for a finite certificate v_p(a_2-b)>=N>v_p(b) in L026's fixed primitive normalization, including period and unit-root precision.
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched “Stein Wuthrich Proposition 3.5 precision cn modular symbols error bound” and “Stein Wuthrich p-adic L series Neron period modular symbol normalization unit root precision”; inspected primary theorem/proof cases and Sage 10.8 primary documentation/source. Local L004/L026 and the 2026-09-25 certificate draft contain the nonvanishing implication but no finite-data error procedure.
SOURCE_EVIDENCE: Stein--Wuthrich, Math. Comp. 82 (2013), Section 3, pp. 1762--1765, Proposition 3.1, Lemma 3.2, Corollary 3.3, Lemma 3.4, Proposition 3.5 and Lemma 3.6 with proofs; Section 3.3, p. 1766. Sage 10.8 padic_lseries.py: alpha, ordinary series, _c_bound, _prec_bounds and _quotient_of_periods_to_twist; ell_modular_symbols.py: ModularSymbolSage initialization and scaling routines.
COMPARISON: Finite-polynomial convergence and adjacent coefficient-error control are known; L004 supplies exclusion of zero. The remaining specialization is uniform-tail and finite-unit-root bookkeeping at degree two, with exact Neron-normalized modular symbols and a certified uniform denominator bound as explicit inputs. No source guarantees a_2 nonzero.
GAP: No curve, exact period-normalization certificate, uniform denominator certificate or nonzero coefficient is produced. Numerical period rounding and a denominator bound inferred only from two polynomials are not approved inputs; arbitrary-generator coefficient conversion is outside scope.
REASON: Essential coverage is available for a conditional error-bound proof, not an unchecked software call. Reproduce only the finite-precision bookkeeping below; do not reprove modular-symbol convergence or infer uniform production from complex order two.
LITERATURE_REASON: At invocation start the target changed from the corank implication given a certified coefficient to finite-data error bounds producing its enclosure; the essential coefficient-wise precision statement had not been recorded or compared.

The main gap remains rational rank versus complex order. Essential local
inputs are L004's enclosure criterion and L026's exact coefficient
hypothesis; the primary lead is Stein--Wuthrich, *Algorithms for the
arithmetic of elliptic curves using Iwasawa theory*, Math. Comp. 82
(2013), 1757--1792,
[ordinary p-adic construction](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=5).
The lead has now been inspected at theorem and essential proof level;
the qualifications below delimit what can be reused.

The intermediate target is an explicit, checkable finite-error procedure
for the degree-two coefficient at a fixed good ordinary prime. Its
downstream use would be supplying L026's additional certificate in
individual cases. Continue if a stated bound controls all truncation,
period-normalization and unit-root errors for the primitive series.
Otherwise record the specific missing bound or normalization mismatch
and park dependent implementation. Approximate vanishing, unproved
period scaling and a coefficient of an imprimitive series fail the test.

Retain L026's non-CM, p>=5, ordinary/non-anomalous, residual surjectivity,
prime-to-p Manin/Tamagawa and local-torsion hypotheses when claiming
downstream applicability; retain residual-family nonvanishing, central
vanishing and sign +1 separately. A finite-error procedure alone need
not terminate with a nonzero coefficient. Uniform coefficient production
from complex order two, rational Kummer membership, finite Sha and
complex-order equality remain unresolved. Do not use the stopped
primitivity-to-F=0 inference in ATTEMPTS/021. This completed turn is
literature-only: no mathematical derivation or script was performed.
Mathlib coverage is not checked.

## Inspected primary input and qualifications

[Stein--Wuthrich, Section 3, pp. 1762--1765](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=6)
defines rational plus symbols using the real Neron period and constructs
P_n with powers of 1+p. Proposition 3.1 gives coefficientwise convergence.
Write a_(n,j)=[T^j]P_n, c_n=max(0,-min_j v_p(a_(n,j))) and
e_(n,j)=min_(1<=i<=j) v_p(binomial(p^n,i)). Proposition 3.5 states
v_p(a_(n+1,j)-a_(n,j)) >= e_(n-1,j)-max(c_n,c_(n+1)).
Its proof uses Corollary 3.3's monic divisor (1+T)^(p^(n-1))-1
and Lemma 3.4. Lemma 3.6 discusses bounded symbol denominators via
cuspidal torsion. The concluding displayed tail estimate uses the same
two c-values; boundedness alone does not explain that particular tail
constant. The extracted Lemma 3.6 proof also prints ord_p(1/alpha)>1,
incompatible with its ordinary unit-root convention. Neither
passage will supply a stronger constant without justification. Section
3.3 fixes v_p(alpha)=0. Only the ordinary case is covered here.

## Finite precision and normalization comparison

[Sage 10.8 primary source, padic_lseries.py](https://raw.githubusercontent.com/sagemath/sage/10.8/src/sage/schemes/elliptic_curves/padic_lseries.py)
was inspected at alpha, ordinary series and the precision helpers.
_prec_bounds uses e_(n-1,j) minus a uniform symbol denominator bound.
_c_bound returns zero in its irreducible branch; its general branch uses
cusp data or period comparison with rounding. Code is implementation
evidence, not a proof that every rounded period is exact. The untwisted
branch returns period quotient one and divides plus-series values by
the number of real components. Finite root precision and integer residue
representatives must be recorded independently; internal precision
padding is not itself a mathematical certificate.

[Sage 10.8 modular-symbol source](https://raw.githubusercontent.com/sagemath/sage/10.8/src/sage/schemes/elliptic_curves/ell_modular_symbols.py)
uses the least positive period, requiring comparison with the notebook's
total real Neron period. _find_scaling_L_ratio can fall back to
_find_scaling_period; the latter documents sign/power-of-two ambiguity
and uses rounded period ratios. __lalg__ also rounds a twist period
ratio. Central vanishing prevents normalization by the central value
alone. These are certification obligations, not a claim that numerical
outputs are wrong.

[Sage's ordinary-series documentation](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/padic_lseries.html#sage.schemes.elliptic_curves.padic_lseries.pAdicLseriesOrdinary.series)
specifies eta=0, no twist, gamma=1+p and interpolation with
(1-alpha^(-1))^2. These match foundations/05 after exact symbol scaling;
that ordinary multiplier must remain in the primitive series. No checked
source makes a_2 nonzero or identifies complex and p-adic orders.

## Approved difference and stop test

The separate continuation assessment is
[the conditional specialization scope](2026-10-06-quadratic-finite-error-specialization.md).
It retains exact Neron-normalized symbols and a certified uniform
denominator bound as inputs, and fixes kappa(gamma)=1+p. The proposed
proof must combine the known adjacent bound with that uniform constant
and certified simple-root Hensel precision. No new bound is proved here.
Replacing an uncertain tail constant by an explicit uniform bound is
the reason for this short reproduction. Continue only if the full
finite-error bound is proved with these inputs; otherwise isolate the
failure and park dependent implementation. L004/L026 are unchanged;
ATTEMPTS/021's stop evidence remains in force for its separate inference.
