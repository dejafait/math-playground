# Uniform root-product mechanism — source comparison completed

TARGET: Assess whether a fixed-radius Mahler-measure bound for polynomials with coefficients |a_j|<=1/j! can control the exact collected C_n of review297, including full-variable power-sum bookkeeping, the length cutoff and recovery of the absolute coefficient sum.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step300 searched Mahler measure/factorial coefficient bounds, Diamond-Steinig/Mahler overlap, Landau1905, symmetric-function logarithms and partition growth; read the primary sources below and checked review296/297, L999, stop299 and L667's distinct recovery obstruction. No inspected theorem states the exact C_n rate; no novelty inference.
SOURCE_EVIDENCE: Landau1905 https://www.numdam.org/item/10.24033/bsmf.760.pdf SectionsIV-VI pp255-259; exact modern statements/proofs at Mathlib commit428aa8288d061ec3ae75c1b85ac178e2cb9def23, Analysis/Polynomial/MahlerMeasure.lean; Macdonald1995 ChapterI Section2 (2.2),(2.4),(2.10)-(2.11') pp19-24; Akhtari-Vaaler arXiv:1810.12413v1 (1.10)-(1.12),Thm1.2 pp2-3; Hardy-Ramanujan1918 (1.32),Section2.3; Defant-Mastylo arXiv:1508.05556v1 (4)-(5),Thm3.1 and proof pp6-7. Ramaré Section2 coverage reused from review296/297.
COMPARISON: General complex-polynomial Mahler/L2, formal symmetric-function and Fourier tools cover the proposed ingredients; none identifies the cutoff polynomial or supplies its collected absolute norm. General Mahler-to-coefficient and multivariable norm estimates retain degree/support losses; direct Fourier recovery from a uniform torus bound is a distinct candidate. L667's individual inverse-row stop does not exclude it.
GAP: Specialize the imported tools to the entire review297 polynomial, including actual degree drops, repeated and boundary roots, both ordered families, the length cutoff and support counting; certify the fixed-radius threshold. No root-pair constant, C_n upper bound or rate is proved here.
REASON: Essential source coverage is now available for a bounded r=2 uniform root-pair/coefficient test. The target needs a local applicability argument, not a reproof of Landau, Fourier recovery or the partition theorem. The proposed specialization is saved separately for next-turn approval.
LITERATURE_REASON: Changed technique and essential unread source: a fixed-radius Mahler-measure or equivalent root-product theorem and coefficient-norm recovery, outside review297's finite rational/factorial scope.
SCOPE: Literature comparison only, completed in step300; no new lemma, mathematical script or derived analytic estimate. The original nomination below records the starting questions. The proposed research scope is in 2026-11-10-collected-root-product-specialization-review-300.md and requires separate next-turn approval.

## Original nomination (step299; starting questions)

The main gap is L030-L032/C032a actual-Xi positivity and L966/L968
signed forcing; the complete one-sided compensated prime-degree
bound L984(H) remains unpaid. The proposed target concerns only the
coefficient overhead in the exact formal T_n of review297, at nu=n.
Do not optimize its representation or change its ordered pairs,
factorials, mu multiplicity or full-vector collection convention.

Proposed source questions, not established statements: can a standard
Mahler-measure/coefficient inequality at a fixed radius control every
product of two reciprocal roots uniformly over the factorial-bounded
coefficient polydisc? Does the untruncated power-sum expression
control every vector retained by the length cutoff? Can one recover
the sum of absolute formal coefficients with sufficiently small
dimension/partition overhead to decide the zero-rate test? Retrieve
precise hypotheses, theorem/page numbers, essential root cases,
coefficient recovery and degree dependence; do not import model memory
as a theorem. Check stronger known results and obstructions. L999's
formal cubic algebra is local evidence, not an analytic root bound
or a full-variable proof.

Continue only if primary coverage yields an applicable, bounded,
independently testable uniform upper-bound target, with all remaining
specialization gaps explicit. If the proposed theorem fails its
hypotheses, constants or degree-uniformity, record that obstruction
and park this lead; do not infer a rate from n<=12 or repeat the
balanced slice. No particular constant or rate is preapproved.

Essential inputs: review297's exact definition, Ramaré's finite
coefficients and L999's canonical balanced cancellation; L998 is the
preserved contrast. L984, L981/L982 and L993 are downstream only.
Actual factor norms, signed correlations, Laguerre reconstruction,
prime powers, endpoints, compensation, complements and regulator/
infinite-zero control remain independent gaps. No RH or cross-notebook
input. Mathlib matching coverage unchecked.

A favorable uniform coefficient result could justify a separately
reviewed arithmetic-error interface; it would not itself establish
that interface or make an RH candidate. This auxiliary mechanism is
not classified as a creative attempt at the central arithmetic gap.

## Completed source review — step300, 10 November 2026

### Exact analytic inputs and proof cases

For any complex polynomial P, Landau's inequality is
M(P) <= (sum_j |[z^j]P|^2)^(1/2). There is no integrality,
monicity, coefficient-sign or zero-free-circle hypothesis.
The precise statements and complete proof were inspected in
[Mathlib source, pinned commit](https://github.com/leanprover-community/mathlib4/blob/428aa8288d061ec3ae75c1b85ac178e2cb9def23/Mathlib/Analysis/Polynomial/MahlerMeasure.lean):
`Polynomial.mahlerMeasure_le_sqrt_sum_sq_norm_coeff`,
`Polynomial.mahlerMeasure_mul`, and
`Polynomial.mahlerMeasure_C_mul_X_add_C` (the last assumes a!=0
and gives M(az+b)=max(|a|,|b|)). Zero polynomials are handled
separately. The L2 proof uses logarithmic integrability, removal of
finitely many circle zeros almost everywhere, Jensen and Parseval.
Multiplicativity and the linear formula allow repeated roots and
circle roots. Constant/degree-drop cases need separate local treatment;
one must not insert a possibly zero leading coefficient into a
monic-root formula. These supporting Mathlib theorems are present;
a matching full C_n theorem is unchecked and unknown. No Lean replay
was run.

[Landau's original paper](https://www.numdam.org/item/10.24033/bsmf.760.pdf),
*Bulletin SMF*33 (1905),251-261, SectionsIV-VI, printed pp255-259,
was also inspected. SectionIV separates the number of zeros inside
the radius from the number of roots being bounded; SectionV passes
to circle-zero cases by continuity; SectionVI discusses products
of the first zeros. OCR corrupts its displayed formulas. Screenshot
calls returned no inspectable images and a local download failed DNS.
Thus those displays are not used as exact-formula evidence; the
complete modern implementation above supplies the essential precise
inequality. This is not an essential source blocker.

### Formal algebra and coefficient recovery

[Macdonald, *Symmetric Functions and Hall Polynomials*,2nd ed.,1995](https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf),
ChapterI Section2, (2.2),(2.4),(2.10)-(2.11'), printed pp19-24,
gives the elementary product generating function, its finite-variable
specialization, algebraic independence, and Newton/power-sum
logarithmic derivatives. Read those statements and their accompanying
arguments. They work formally, including repeated or zero variables;
characteristic zero is available here. They do not identify review297's
length-truncated polynomial. That identification must be proved with
all 2n formal Y variables, not inferred from L999's cubic slice.

[Akhtari-Vaaler, arXiv:1810.12413v1,29 October2018](https://arxiv.org/pdf/1810.12413v1),
(1.10)-(1.12),pp2-3, defines normalized finite-torus Fourier
coefficients and recovers a trigonometric polynomial from its finite
support. This applies to any finite set of integer exponent vectors;
there is no dimension restriction or sign condition. The normalization
is essential when subsequently estimating an individual coefficient
by a uniform torus bound. Such an estimate alone does not bound its
absolute coefficient sum without controlling support size.

For comparison, their (1.3),Thm1.1 and Thm1.2 retain binomial
factors indexed by degree or ordered support rank. Thm1.2 additionally
requires a Q-independent ordering vector and finite support containing
the Fourier support. These statements were read; no claim that their
binomial losses are harmless is made. Their proof is unnecessary for
the proposed continuation, which uses finite Fourier recovery instead.

[Hardy-Ramanujan,*Asymptotic formulae in combinatory analysis*,1918](https://ramanujan.sirinudi.org/Volumes/published/ram36.html),
(1.11),(1.32),Section2.3 (2.31)-(2.33) and its concluding argument,
supplies p(N)<=exp(B sqrt(N)) for all sufficiently large positive
integers N and an absolute B. This weaker bound suffices as an input;
the sharp asymptotic need not be reproved. Identifying the relevant
formal support with a subset of partitions is still local bookkeeping.

### Stronger norm results and recorded obstructions

[Defant-Mastylo, arXiv:1508.05556v1,23 August2015](https://arxiv.org/pdf/1508.05556v1),
(4)-(5),Thm3.1 and its full proof,pp6-7, gives, for every finite
complex polynomial in m variables and every p>0,
||P||_Lp <= product_j Lambda(p,d_j) M(P),
where d_j is its degree in variable j and
Lambda(p,d)=|| (1+z)^d ||_Lp(T). Its sharp examples are products
of (1+z_j)^(d_j). The proof proceeds by induction, Fubini,
Fatou and Minkowski. This general reverse norm theorem retains
explicit coordinate-degree factors; it is not a dimension-free
coefficient-recovery theorem. No application of it to T_n is claimed.

Local comparison read review297 in full, relevant source/failure
passages of review296, L999 in full, stop299, and L667's hypotheses,
source imports and conclusion ranges. L998's unmerged growth and the
older arithmetic stops are retained through those exact references;
they do not decide the collected upper-bound question. L667/its
individual-finite-residue attempt concerns inverse interpolation rows
and a binomial coefficient-to-Mahler transfer. This proposal estimates
a whole formal polynomial uniformly before coefficient recovery;
it assumes no inverse rows, so that historical stop is not a global
ban. Its actual obstructions remain valid in their original scope.

Search strings included `Mahler measure polynomial coefficient bound
factorial coefficients Landau inequality Jensen polynomial`,
`Diamond Steinig identity generalized von Mangoldt Ramaré polynomial
roots coefficients`, `"Diamond" "Steinig" "Mahler"`, the title of
Landau1905, `Hardy Ramanujan 1918 ... partitions pdf`, and
`Macdonald symmetric functions power sums log generating elementary
symmetric functions pdf chapter 1 2.10`. Secondary search results were
discovery only. A Cambridge Mahler-measure excerpt returned503 and is
not imported. No inspected source states the exact C_n rate. This is
a bounded comparison, not exhaustive novelty certification.

### Decision and next bounded test

The available primary tools warrant SPECIALIZE coverage for the
separately saved r=2 test. This is an assessment of source scope,
not a derivation of a root-pair contraction, full-variable identity,
cutoff norm bound or asymptotic rate. In particular, an untruncated
torus estimate cannot simply be assigned to the truncated polynomial:
the retained full coefficients must first be identified and recovered.

The proposed test must certify its scalar factorial-series bound and
all degree dependence, then compare the resulting coefficient bound
with review297's zero-exponential-rate threshold. A favorable result
would remove only a formal coefficient-overhead obstruction toward a
separately assessed L984(H) arithmetic interface. Actual factor norms,
correlations, reconstruction, prime powers, compensation, endpoints,
complements and regulator/infinite-zero control stay open. If the
threshold or bookkeeping fails, preserve the failure and park this
fixed-radius lead rather than repeat the balanced witness. No central
creative target is justified by this auxiliary source comparison.
