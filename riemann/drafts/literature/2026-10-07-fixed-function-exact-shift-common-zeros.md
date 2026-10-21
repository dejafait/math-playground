# Coverage: fixed-function exact-shift common zeros

TARGET: Test whether one fixed even real entire function P of order at most one, with P(0)>0 and only simple real zeros outside [-40,40], can have unbounded positive common zeros of P(t) and Re[P(t-2i)/(5/2+it)].
CHECKED: 2026-10-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact common-zero, imaginary-shift, real-zero product and interpolation searches completed; scoped local duplicate/failure searches found L375's finite family and L068's different sparse-product obstruction, but no matching fixed-function result; inspected and unread sources are distinguished below.
SOURCE_EVIDENCE: Read Katkova–Tyaglov–Vishnyakova arXiv:1608.03924v2, Proposition 1.1 and Theorem 1.2 pp. 2–3 and Theorem 2.2 with complete proof pp. 4–5; Cardon (2002), Theorem 2 and complete proof, author PDF pp. 1–2; Laine (1993), Theorems 1.2.3–1.2.4 and growth remarks pp. 7–8; Walker (2002), Lemma 3 with complete proof pp. 112–113 and three-term scope pp. 110–111; reused the ready Lagarias scope comparison.
COMPARISON: Inspected results localize shifted-output roots or construct products with prescribed zeros; none inspected settles infinite common zeros of the unshifted P and its exact divided shifted projection. L375 has the wrong quantifier; L068 has nonreal roots and a different objective.
GAP: A single admissible P with exact common zeros tending to infinity remains unconstructed and unexcluded; simultaneous cancellation after all factors, convergence, complete simple zero set and order at most one require proof.
REASON: Primary operator and canonical-product coverage permits one bounded test of this exact target; citation alone does not settle it, and a failed search does not establish novelty.
SCOPE: One fixed even real entire comparison function, order at most one (order zero allowed), positive at zero, all zeros real and simple outside [-40,40], and exact shift -2i/divisor 5/2+it. Sparse paired-real-root products with adjustable close pairs are an approved candidate mechanism, not an established construction. No count asymptotic, Fourier kernel, physical discriminant, response sign or actual-zeta premise is covered.

## Primary theorem comparison

O. Katkova, M. Tyaglov and A. Vishnyakova, *Linear finite difference
operators preserving Laguerre–Pólya class*,
[arXiv:1608.03924v2](https://arxiv.org/pdf/1608.03924v2),
3 September 2016. Proposition 1.1 and Theorem 1.2 treat polynomial
and entire coefficients. Theorem 2.2, pp. 4–5, states that for
meromorphic M, f(z+i)+M(z)f(z−i) has only real roots or is identically
zero for every Laguerre–Pólya f iff either |M(z)|<1 when Im z>0
and |M(z)|>1 when Im z<0, or M is constant of modulus one.
Read its necessity and sufficiency cases, including zero-free
Gaussian/exponential inputs and inputs with a zero. The proof compares
moduli off the axis; it imposes no noncoincidence with the original f
on the real axis. It therefore does not settle TARGET. No coefficient
specialization is proved here. PDF extraction confuses non-strict
inequality symbols; no conclusion uses its extracted endpoint symbols
in Theorem 1.2.

D. A. Cardon, *Convolution operators and zeros of entire functions*,
Proc. Amer. Math. Soc. 130(6) (2002), 1725–1734,
DOI 10.1090/S0002-9939-01-06351-1,
[author manuscript](https://mathdept.byu.edu/cardon/papers/convolutions_and_zeros.pdf).
Theorem 2 (Pólya, Hilfssatz II), manuscript pp. 1–2, assumes positive
a, a real entire G of genus zero or one, at least one real zero,
and no nonreal zeros. It concludes that G(z+ia)+G(z−ia) has only real
zeros. Its complete short proof compares product moduli above and
below the axis. This localizes output roots; it does not locate common
roots with G, supply the variable divisor, or construct our fixed
function. The author's publication list confirms the publication
metadata; the manuscript header is a placeholder. No reproof or import
is needed.

I. Laine, *Nevanlinna Theory and Complex Differential Equations*,
de Gruyter Studies in Mathematics 15 (1993),
[publisher preview](https://api.pageplace.de/preview/DT0400.9783110863147_A19976604/preview-9783110863147_A19976604.pdf),
printed pp. 7–8 (zero-based PDF pages 14–15). Theorem 1.2.3 gives a
canonical product with precisely the prescribed zero sequence of finite
convergence exponent λ, for nonnegative integer genus k>λ−1.
Theorem 1.2.4 is Weierstrass factorization; the following remarks
identify the minimal canonical factor's order with the zero convergence
exponent and state the finite-order Hadamard restriction. These are
standard starting inputs, not shifted-phase interpolation results.
A future use must verify the chosen sequence and genus hypotheses;
compact convergence alone is not an order bound. The referenced Ash
proofs were not retrieved; no strengthening is assumed.

P. Walker, *The zeros of linear combinations of translates of
polynomials*, J. Austral. Math. Soc. 72 (2002), printed pp. 109–117,
DOI 10.1017/S1446788700003621,
[primary PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/51694D4CB803E81CD15B7D413411F217/S1446788700003621a.pdf/zeros_of_linear_combinations_of_translates_of_polynomials.pdf).
Read the three-term scope and phase definitions, pp. 110–111, then
Lemma 3 with its complete proof, pp. 112–113. Its hypotheses are a
finite polynomial with distinct real roots and positive shift c;
it locates symmetric-shift output zeros in intervals defined by root
angles. It does not state disjointness for our divisor or an infinite
construction. The cited 1997 *Separation of Zeros of Translates of
Polynomials and Entire Functions*, JMAA 206, 270–279,
DOI 10.1006/jmaa.1997.5232, remains an unread lead: its publisher
full-text request failed. The abstract was not used as theorem
coverage. That failure is not an essential blocker for the bounded
construction test; no assertion of that paper is a premise.

Reuse the ready Lagarias comparison from
[the quartic audit assessment](2026-10-07-exact-shift-quartic-audit.md).
Its complementary shifted components are not this pair. No rereading
or reproof of that source was needed.

## Search, duplicates and recorded failures

Queries included `real entire function real zeros common zeros imaginary
shift real part polynomial divisor`, `Laguerre Polya entire functions
imaginary shifts interlacing zeros original zeros difference operator`,
`entire canonical product prescribed zeros interpolation sparse real
zeros phase`, `"real entire" "common zeros" "difference" Laguerre`,
`"real entire" "common zeros" "imaginary" shift`,
`"entire" "5/2" "common zeros" polynomial`, and
`"real zeros" "canonical products" "interpolation" sparse`.
Follow-ups searched the exact operator title, Cardon's primary PDF,
canonical-product order/exponent statements and Walker's cited title.
Random entire products, differential operators and spectral interpolation
were search leads only; none was used as a matching theorem.

The scoped local search covered common-zero and sparse-product phrases
in this notebook's lemmas, drafts, ATTEMPTS and history. Read L375 in
full, L068's statement and full proof, the relevant quartic-audit
assessment range and the exact-shift stop note. L375 remains the audited
finite-family contrast. L068 proves a fixed order-zero sparse product,
but with nonreal roots and an upward-interaction objective; it is not a
duplicate solution. Its convergence, nonvanishing-tail and growth
arguments are available for conditional reuse with changed hypotheses
checked. No heat conclusion is a premise. The earlier pointwise/family
stop does not ban this different fixed-function quantifier. No
cross-notebook input was read; unfinished work is preserved.

## Approved bounded test and limits

The main gap is global actual-theta mixed positivity and L367's total
signed margin. Actual disjointness, physical D≤0 and the signed count
comparison are independent unresolved steps. The intermediate target
is the exact TARGET above. A fixed-function obstruction would limit
geometry-only eventual disjointness; a matching exclusion theorem
could identify usable hypotheses. Neither would resolve those independent
gaps or supply an RH counterexample.

The discriminating threshold is one admissible P and exact common
zeros t_j tending to infinity, or a theorem excluding such a sequence
under the literal hypotheses. The next mathematical attempt may test
widely separated real-root pairs with adjustable within-pair spacing.
This is a proposed mechanism, not a lemma or an assertion that
multiplying L375's quartics preserves their common zeros. Continue on
proving simultaneous exact cancellation for one limiting product,
together with convergence, growth and its complete simple zero set.
Finite-stage solutions, small residuals or zeros escaping between
different functions do not meet the threshold. If the adjustment scheme
loses earlier conditions or lacks a uniform solvability/convergence
estimate, record the failure and reassess that mechanism; do not infer
a general exclusion theorem. No mathematics or scripts were produced
in this literature-only step.

No Riemann–von Mangoldt count, Fourier kernel, actual-theta arithmetic,
D≤0 or response Laguerre sign is assumed. Full matching Mathlib coverage
was not checked; availability is unknown. EXPLORE licenses the exact
saved target next invocation, not novelty or a completed construction.
