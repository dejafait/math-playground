# Entire-function dependence after the smoothed-law lift — review1301

TARGET: Review Borel-type theorems on finite linear relations among zero-free entire functions for the C032k lifted transforms, including whether pairwise nonproportionality suffices without a growth assumption.
CHECKED: 2026-11-17
DECISION: IMPORT
SEARCH_EVIDENCE: Review1301 searched the exact Borel/zero-free-entire dependence question, then followed Brownawell1976 reference5 to Narasimhan1971; a bounded notebook-local duplicate/failure screen and queries are recorded below.
SOURCE_EVIDENCE: Narasimhan1971 Theorem1/p271 and the complete one-variable proof in Section2/pp273-277, with prerequisite statements(1.1)-(1.3)/p272, were inspected; Brownawell1976 introduction/p968, Theorem1/p969 and SectionII/pp972-973 confirm the distinction between exponent and coefficient growth.
COMPARISON: Narasimhan Theorem1 directly covers finite families of zero-free entire functions with no proportional pair, even for polynomial coefficients; neither finite order nor a bound on the entire exponents is required. C032k states the needed global-entire and separation premises, but its local proof is not certified by this review.
GAP: No missing growth premise remains for the dependence theorem. Critical verification of C032k and the finite signed-measure application remain for a separate mathematical step; no finite-mixture exclusion is established in this literature turn.
REASON: An inspected primary theorem resolves the new source gap and makes a bounded local audit/application possible; another search for the same dependence statement is unnecessary. The result is classical coverage, not a new mathematical discovery.

## Nomination1300 retained (historical)

At nomination1300 this file nominated a source comparison only. It neither approved new
mathematical work nor asserted the truth or applicability of a named
dependence theorem. C032k's local proof also awaits critical review;
using it as the object of a source comparison does not certify it.

The exact functions to compare are

    exp(-b_sigma_j(w)), exp(-b_sigma_j(-w)), 1<=j<=r,

with finite r>=2 and distinct positive Gaussian half-variances. C032k
proves they are zero-free entire, normalized to one at zero, and
pairwise nonproportional. No bound on their entire-function order is
part of that conclusion. An exponential moment of a nonnegative
combination with real coefficients summing to one would force

    sum_j a_j [exp(-b_sigma_j(w))-exp(-b_sigma_j(-w))]=0

identically. Zero coefficients can be omitted, but at least one must
remain. The relevant source theorem must address a finite homogeneous
linear relation, not merely distinctness or mixture identifiability.

Essential local mathematical input is C032k, with C032j supplying the
actual laws, profiles, heat-time identity and qualified positivity
input. L018/L024 fix the divisor conventions through C032j. The
underlying preprint and finite-zero input qualifications persist.
Nonnegativity of the proposed combination, actual-Xi identification,
initialization and all-degree Q positivity remain unpaid. No theorem
from another notebook is needed.

The local query used `Borel.*(entire|exponential)`,
`zero-free entire.*(depend|sum)`, `entire lift`, and the displayed
profile/sinh pattern in drafts/literature and ATTEMPTS. The only
unrelated hit was the fixed-half-plane witness assessment of
24 October: its lines52-58 concern Borel-Caratheodory and three-circles,
not Borel-type linear dependence. This is a bounded local screen,
not a claim of novelty or external coverage.

Continue if a primary theorem with inspected hypotheses and proof
cases applies to these exact entire functions, or specifies a concrete
additional hypothesis that can be independently tested. If an
essential growth hypothesis is unavailable, retain that limitation;
do not replace the needed theorem by the false general inference
that distinct functions must be linearly independent. A successful
comparison would only support a later finite-mixture obstruction,
not RH. The former individual-law stop1297 remains scoped and intact.

## Completed source review1301

### Scope, sources and exact theorem

The requested object remains the finite constant-coefficient relation
displayed above, on the whole complex w-plane. This is not a theorem
about arbitrary distinct holomorphic functions, functions on a disk,
infinite sums, or width-dependent coefficients.

The primary reference is Raghavan Narasimhan,
*Un analogue holomorphe du théorème de Lindemann*, Annales de
l'Institut Fourier **21** (1971), no.3, 271-278,
[doi:10.5802/aif.391](https://aif.centre-mersenne.org/articles/10.5802/aif.391/),
[original journal PDF](https://www.numdam.org/item/10.5802/aif.391.pdf).
Theorem1, printed p271: for holomorphic f_1,...,f_p on C^n with
f_i-f_j nonconstant for i!=j, the functions exp(f_i) are linearly
independent over C[z_1,...,z_n]. The same page states the equivalent
zero-free-function formulation: a dependent finite family has a pair
with constant quotient. There is no growth restriction.

Read Section1's Nevanlinna statements(1.1)-(1.3), p272, and all of
Section2's one-variable proof, pp273-277. Its cases are induction
through a zero Wronskian, or Cramer's rule when that Wronskian is
nonzero. In the latter case the polynomial factors account for the
finite poles; the logarithmic-derivative estimate, outside a finite
measure exceptional set, bounds the determinants. The resulting
O(log r) characteristic invokes criterion(1.1), giving rationality
and the contradiction with nonconstant exponent differences. These
are source proof cases, not a local reproof. Only n=1 is needed.

The end-of-paper bounded-domain example, p277, was also read:
global entirety is essential, not a disposable hypothesis. This is
why the lift in C032k must be audited before application. No claim
about the paper's separate algebraic-independence theorem is used.

W. Dale Brownawell, *The algebraic independence of certain exponential
functions*, Canadian Journal of Mathematics **28** (1976), no.5,
968-976, [doi:10.4153/CJM-1976-094-9](https://doi.org/10.4153/CJM-1976-094-9),
is corroborating coverage. Read the introduction/p968, Theorem1 and
coefficient-ring definition/p969, and the one-variable argument in
SectionII/pp972-973. The growth bounds in its extensions constrain
the coefficient ring; they do not impose finite order on the
exponents. Its introduction explicitly identifies the Borel theorem
over constants and Narasimhan's stronger polynomial-coefficient form.
Reference5/p976 leads to the primary theorem used here. The more
general multivariable extension is unnecessary.

### Applicability comparison and limits

C032k was read in full, as was C032j; no further detailed local proof
was needed for this source comparison. In the proposed application,
the f_i in Theorem1 would be -b_sigma_j(w) and -b_sigma_j(-w),
for a finite collection of distinct positive widths. C032k states
global entirety, value zero at the origin, and pairwise distinctness
of these exponents, then pairwise nonproportionality of their
exponentials. Those are exactly the properties to verify in the
mathematical audit. In particular, unknown entire-function order is
not an extra obligation. Constant real coefficients are inside the
source's polynomial coefficient ring. Zero coefficients can be
omitted; the sum-one condition is the existing nontriviality premise.

The relevant local statements are the entire lift and separation in
C032k, not merely C032j's individual-law tail divergence. The theorem
does not supply the lift, positivity of a signed measure, its moment
criterion, or the source heat-positivity input. It will not replace
critical review of those statements. The intended later application
must use the complete relation F(w)-F(-w), including both signs,
and avoid subtracting divergent moments of the individual measures.

No new mathematical assertion about the smoothed laws is proved
here. The finite-mixture question is retained for the next audit,
with the C032j preprint qualifications, actual-zero conventions and
finite-zero/counting imports unchanged. L030-L032/C032a initialization,
singular blocks, identification, realization and all-degree signs
remain open. No canonical lemma, DAG row, PROOF argument or
mathematical script was changed. Full matching Mathlib coverage is
unchecked and unknown; no Mathlib result is imported.

### Searches, duplicates, failures and access

External queries actually used were:

- `Borel theorem linearly independent zero free entire functions no growth condition exponential sum theorem`
- `Narasimhan "Un analogue holomorphe" 1971 pdf`
- `Borel "Sur les zéros des fonctions entières" 1897 357 396 pdf`

The notebook-local screen used `Narasimhan`, `Brownawell`,
`Borel.{0,90}(depend|entire|exponential)`, and
`zero.free entire.{0,90}(depend|relation)` in drafts/literature,
ATTEMPTS, foundations and the specific step1300 history. Only the
current nomination matched the needed theorem; unrelated measurable
Borel-dependence and Borel-Caratheodory records were excluded.
Assessment1298/review1299 was read for the exact signed-law scope;
the recorded stop1297 concerns the individual-law surrogate and is
not a global ban on this finite signed-combination question. Its
stop text was searched, not treated as fresh source evidence.
No other notebook was read. A failed search is not a novelty claim.

Yum-Tong Siu's 2024 Math213a notes, *Logarithmic Derivative Lemma*,
pp13-14, supplied an initial Borel partition-statement lead. They
are not the primary import. Borel1897 and Nevanlinna1929 were
identified bibliographically through Brownawell; their original
texts were not inspected and are not claimed as inspected coverage.
Cambridge PDF text was accessible, although screenshot attempts
returned a timeout/403; the Narasimhan journal text was accessible
throughout the necessary statement, proof and limiting example.
There is no remaining essential access blocker.

### Continuation gate

The source comparison has met its continuation test: an inspected
primary theorem applies to the precise type of relation without an
unpaid growth hypothesis. The local premises remain subject to audit.
The next target and covered source scope are nominated in
`drafts/literature/2026-11-17-smoothed-law-borel-application-audit-1301.md`;
its separate approval is left to the next invocation. Stop at any
failed global-entire, moment-equivalence or separation premise;
otherwise use the citation and its specialization, without reproving
the Borel theorem or claiming RH progress beyond the scoped surrogate.
