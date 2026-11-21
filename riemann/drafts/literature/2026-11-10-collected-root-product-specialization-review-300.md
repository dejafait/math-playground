# Fixed-radius collected-coefficient specialization — proposed ready scope

TARGET: Test the fixed-radius r=2 Landau root-pair mechanism on review297's exact C_n, proving full-variable power-sum and length-cutoff bookkeeping and a degree-uniform absolute-coefficient bound sufficient to decide the zero-rate test.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed step300 comparison in 2026-11-10-collected-root-product-bound-review-299.md searched exact/stronger Mahler, Fourier, symmetric-function and partition results and checked review296/297, L999, stop299 and the distinct L667 inverse-row stop; no inspected theorem decides exact C_n.
SOURCE_EVIDENCE: Mathlib pinned source https://github.com/leanprover-community/mathlib4/blob/428aa8288d061ec3ae75c1b85ac178e2cb9def23/Mathlib/Analysis/Polynomial/MahlerMeasure.lean (Landau,multiplicativity,linear factor); Macdonald1995 I.2 (2.2),(2.4),(2.10)-(2.11'); Akhtari-Vaaler https://arxiv.org/pdf/1810.12413v1 (1.10)-(1.12); Hardy-Ramanujan1918 (1.32),Section2.3; Ramaré2009 Section2/(12)-(18) reused via review297. Complete primary links, hypotheses and inspected proof cases are in completed review299.
COMPARISON: Known analytic/formal tools cover ingredients, not the exact cutoff and norm conclusion. General coefficient/Mahler and reverse torus-norm theorems retain degree/support losses. The proposed finite Fourier recovery needs an independently certified uniform bound and support accounting.
GAP: Establish the full-variable identity and retained-coefficient correspondence, specialize a fixed-radius root-pair estimate, and verify its threshold plus coefficient-count overhead. No favorable constant or C_n rate is assumed.
REASON: Source coverage now supports one bounded quantitative specialization. The full result must be proved in a later research turn; source theorems should be imported and only applicability/reconstruction proved locally.
SCOPE: Exactly review297's C_n at nu=n, both ordered partition families, all factorials and full exponent vectors retained; fixed radius r=2, actual polynomial degree at most 2n, finite algebra and torus coefficient recovery only. No new representation, arithmetic estimate or RH hypothesis. Newly written ready assessment; separate next-turn approval required before research.

Use review297's complete definitions of K_n,H_n,c,w,T_n,b_n,C_n.
L999 supplies only the existing cubic/balanced calculation and a
contrast; it is not a theorem for all vectors. Preserve L998 and
the balanced-witness stop299. The main gap remains L030-L032/C032a
actual-Xi positivity and L966/L968 forcing; L984(H)'s compensated
one-sided prime-degree bound is unpaid.

Proposed research obligations, not results of step300:

- Work with E_Y(t)=1+sum_(j=1)^(2n) Y_j t^j/j! and independent Y_j.
  Relate the complete formal logarithm coefficients, Newton power
  sums and the two-family expression with correct signs/factors.
  Prove correspondence for every retained exponent vector, including
  the total-length cutoff, ordered pairs, mu multiplicity and n=1.
- Apply imported Landau/multiplicativity/linear-factor theorems to
  E_Y(2t) uniformly for |Y_j|<=1. Check actual degree drops,
  constant/linear cases, repeated roots and roots on the radius.
  Treat roots as a multiset; global continuous root labels are not
  an available assumption. Test whether a rigorously certified scalar
  factorial-series estimate supplies a degree-independent reciprocal
  root-pair contraction. No constant is preapproved.
- Use finite Fourier coefficient recovery on the full Y torus and
  the length-cutoff correspondence. Control the number of retained
  full vectors using the imported partition bound. Account for every
  factor depending on n. Do not assume that deleting monomials
  contracts the supremum norm. No finite sample decides the rate.

Continue only if all obligations yield C_n<=K_epsilon exp(epsilon*n)
for every epsilon>0 with finite K_epsilon and all n>=1 (or a stronger
rigorous bound). A rigorous positive limsup would reject the zero-rate
claim. Failure of this upper-bound test alone is inconclusive about
the true rate: record the exact failed threshold/identity and park
this fixed-radius mechanism unless a materially new input is supplied.
No arbitrary radius optimization is part of this bounded attempt.

A favorable result permits only a separately reviewed arithmetic-error
interface. L984, L981/L982 and L993 are downstream context, not inputs
paying actual factor norms, signed correlations, Laguerre reconstruction,
prime powers, endpoints, compensator, complements or regulator/infinite
zero control. No cross-notebook input. Supporting Mahler Mathlib coverage
is verified at source level; full matching C_n coverage is unchecked.
Expected classification REPRODUCTION; task calculation, standard/high.
