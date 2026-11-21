# Coverage nomination: a quantitative first-derivative critical count

TARGET: Assess whether unconditional derivative zero-count or mollified-moment theorems imply K(a,b)=O(T) for Xi on L957-admissible intervals T<a<2T<3T<b<6T, with full critical multiplicities and no finite global nonreal census.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step127 reused the step114/123 Kim/shape/tilt reviews and L957/L958, searched Levinson–Montgomery derivative counts, Xi derivative mollifiers and stronger fixed-first-derivative results, and narrowly checked local completion-homotopy duplicates. Inspected primary passages are detailed below; failed Conrey PDF retrievals are distinguished from inspected sources.
SOURCE_EVIDENCE: Levinson–Montgomery, Acta Math.133(1974),49–65, Theorem1 p49 and complete Section2 proof pp51–52; Levinson, Bull.AMS80(1974),951–954, theorem and complete announced proof sketch pp951–953; Wu arXiv:1206.3737v2(18Sep2012), definitions p2 and Section3 pp6–8/(18)–(24). No K=O(T) theorem was found or imported.
COMPARISON: The first theorem controls zeta' on the left of the critical line, not the completed derivative; its proof uses a strict contour sign unavailable after merely replacing the function. The inspected direct Xi'-mollifier conclusions are fixed-proportion lower bounds for real zeros, not a signed difference of nonreal counts. L957's displacement estimate supplies endpoints only. None pays L958's full critical multiplicities or K=O(T).
GAP: The direct-import route stops: it needs either a signed completion-boundary transfer estimate or an independent arithmetic estimate of N'-N-E. Neither is in the inspected results. This is a source-scope negative, not a disproof of K=O(T) or a statement that no other theorem can prove it; K=0 is still stronger.
REASON: New primary-source scope evidence closes the proposed derivative-count/proportion imports. Park that mechanism; prepare a different, bounded completion-boundary crossing-index question rather than repeat unsigned-count or displacement comparisons. No new mathematical result is derived or approved here.
LITERATURE_REASON: Changed target from validation of a count identity to an unconditional O(T) estimate; the ready Kim and endpoint assessments do not cover derivative-count or derivative-mollifier bounds for K.
SCOPE: Completed bounded source comparison for the exact TARGET, uniform in the stated L957 intervals and retaining multiplicities. EXPLORE records that no adequate match was established, not permission to derive a new bound in this literature turn; it covers no unlisted mathematical continuation. The parked real-exponential-tilt source was not reopened.

The main gap remains actual-Xi all-degree mixed positivity,
L030–L032/C032a. The proposed intermediate target is quantitative
control of the first loss of nonreal pairs, now that L958's interface
is audited. An O(T) estimate would give a concrete scale for the
remaining exceptional critical data, useful in judging whether a
later signed arithmetic mechanism can reach K=0. Neither that estimate
nor a route from it to RH is claimed. Independent higher-derivative
and global transfer gaps remain.

The exact analytic object is f=Xi, with K defined by L958, including
even-order stationary zeros and all higher odd-order critical weights.
Choose the two positive endpoints supplied by L957 at scales T and
3T; they must also avoid real f zeros. Stationary endpoints of f are
permitted with L958's closed-count correction. No RH, simplicity,
global finite nonreal census or sign at a real critical point is a
premise. Reuse L018 and L023/L024 for the completion, genus and product;
no cross-notebook theorem is needed.

Two related primary-source leads suffice for a bounded review: a
derivative zero-count theorem that actually controls the difference
J-J', and a derivative-mollifier theorem with an explicit implication
for that same difference. The classical Levinson–Montgomery work on
zeta derivatives is only a search lead, not an inspected theorem or an
asserted result about Xi. Retrieve its precise hypotheses/conclusion
before its proof. If its observable is zeta', record the additional
completion-factor terms required for Xi' before considering transfer.
Do not assume that a count on one side of the critical line equals
Kim's difference of conjugate-pair counts.

Continue only if an inspected theorem yields the stated O(T) bound
or leaves one precisely identified, independently testable difference
with ready coverage. An applicable stronger bound should be imported.
Stop this particular import if it uses RH, simplicity, a finite global
nonreal census, or an unsupported identification of zeta' with Xi'.
If only displacement moments or unsigned separate counts are available,
record their exact shortfall and select a different mechanism; do not
repeat the completed Kim audit or relabel the missing K estimate.
Failure to find a theorem is exploration, not proof of impossibility.

There is no justified proof_attempt/creative yet: the missing ingredient
is an independent arithmetic estimate of the signed pair loss. This
review is intended to decide whether such an ingredient is available,
not to manufacture a creative target to meet a schedule. The parked
tilt source and existing countermodels retain their original scope.
Full matching Mathlib coverage is unknown.

## Completed comparison — step127, 10 November 2026

The preceding nomination is preserved. Outcome **NEGATIVE** refers to
the following specific import failures. There is no mathematical
counterexample to the desired bound and no advance beyond the checked
sources. No lemma, mathematical script, PROOF or DAG changed.

### Primary derivative-count theorem and essential proof cases

N. Levinson and H. L. Montgomery, *Zeros of the derivatives of the
Riemann zeta-function*, Acta Math. **133** (1974),49–65,
[DOI10.1007/BF02392141](https://doi.org/10.1007/BF02392141),
[published PDF](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6174-11511_2006_Article_BF02392141.pdf).
Read Theorem1 p49 and the whole Section2 proof pp51–52, plus the
separate conditional Theorems7–8 p51. In Theorem1, N_-(Y) and
N'_-(Y) count zeta and zeta' zeros in 0<sigma<1/2, 0<t<Y, and
N'_-(Y)=N_-(Y)+O(log Y). The proof uses the argument principle,
including indents at critical-line zeros; its count is not restricted
to simple zeros. It handles a negative-real-part contour sequence
and its absence separately before bounding horizontal arguments.
Theorems7–8 instead assume a finite left-half-plane census or RH.
Those assumptions are inadmissible here.

**Applicability difference.** The completed derivative is not zeta'.
The source identity in Levinson's paper below is
xi'=H'zeta+Hzeta', with H=s(s-1)pi^(-s/2)Gamma(s/2)/2.
Thus the required zero observable is zeta'+(H'/H)zeta. The
Levinson–Montgomery proof's strict real-part sign for zeta'/zeta
on its indented critical boundary is not an assertion for this
observable. Reality of xi on that line makes xi'/xi purely imaginary
away from zeros. Replacing the contour sign by zero does not justify
its winding argument. No bound on the resulting critical-boundary
crossings, uniformly in a,b, was supplied. Small horizontal argument
errors for the original function do not repair that missing boundary
term. This is a hypothesis/observable comparison, not a new transfer
theorem or a claim that transfer is impossible.

### Primary mollifier results for the actual completed derivative

N. Levinson, *Zeros of derivative of Riemann's xi-function*, Bull.
Amer. Math. Soc. **80** (1974),951–954,
[DOI10.1090/S0002-9904-1974-13591-3](https://doi.org/10.1090/S0002-9904-1974-13591-3),
[published PDF mirror](https://scispace.com/pdf/zeros-of-derivative-of-riemann-s-xi-function-4t1v5o8k6d.pdf).
Read the theorem p951 and its complete announced proof sketch
pp951–953. For U=T/log^10 T, it places more than 70% of xi' zeros
in T<t<T+U on the critical line. Equations(1)–(3) keep completion
derivatives. The proof controls an auxiliary argument using a
mollified mean square; its final numerical bound is a proportion,
not a comparison with xi's nonreal count. It does not state the
uniform signed critical-count estimate sought here. The sketch is
not independently reconstructed or treated as a full proof of a
stronger assertion.

Stronger inspected direct lead: Xiaosheng Wu, *Distinct zeros of the
Riemann zeta-function*, [arXiv:1206.3737v2](https://arxiv.org/pdf/1206.3737v2),
18 September2012. Read p2's full versus distinct-count conventions
and Section3 pp6–8, including (18)–(24) and the final parameter
choice. It states N_{xi',c}(Y)>=0.86957 N(Y), without asserting
simplicity of these line zeros. Its auxiliary eta includes completed
derivatives; the argument inequality (18) is a lower bound for
line zeros, and (23) retains a Y log Y times logarithmic-moment
penalty. This is still a fixed-proportion bound, not a lower bound
for nonreal xi' zeros relative to nonreal xi zeros. No numerical
optimization or audit of Wu's analytic approximations was performed;
we need only the exact scope of its stated conclusion, and import
no new bound from it.

**Threshold comparison.** L958 requires the upper bound
N'-N-E=O(T) on the same interval, equivalently J-J'=O(T), with
full orders. A lower bound for N' supplies neither that signed
upper bound nor a lower bound for J'. Total-count asymptotics and
fixed proportions have a T log T scale; their leading terms are
not estimates for the difference of the two line counts. Subtracting
unrelated lower bounds would be invalid. This exact mismatch already
prevents the import, before localization to arbitrary L957 endpoints.
Even a larger fixed proportion would leave the same logical issue.

### Duplicates, access qualifications and next mechanism

Queries included `Levinson Montgomery zeros derivatives Riemann zeta
function 1974 xi derivative number nonreal zeros`, `Xi derivative
zeros critical line mollifier number zeros O(T) Conrey Ghosh`, exact
Conrey1983 titles, and Xi derivative anomalous-zero terminology.
The exact local searches covered the saved step114/123 count reviews,
step119 endpoint review and the relevant ATTEMPTS; a narrow
completion/homotopy/parameter search in drafts/literature and ATTEMPTS
found no matching assessed completion-parameter crossing target.
This does not establish novelty.

Conrey, J.Number Theory **16** (1983),49–74 (I), and **17** (1983),
71–75 (II), were identified by primary-PDF search text at AIM
publications/3.pdf and4.pdf. Direct opens returned404; the II
Scispace page returned429 and its attempted PDF was inaccessible.
These remain partially retrieved leads, not inspected full theorems
or approved numerical constants. AMS's Levinson PDF returned403;
the published mirror above supplied the actual paper. Shell curl
could not resolve AIM. No API key, credential or paid access was used.
Wu's later, directly inspected fixed-proportion conclusion supplies
the comparison needed here; completion of Conrey retrieval is not
essential to this source-scope negative. No claim of a current
best-known proportion or exhaustive theorem absence is made.

L957's audited weighted-displacement input and L958's audited balance
are reused, not reproved. Existing theta-shape, real-exponential-tilt,
generic endpoint and unsigned allocation stops retain their scope.
The new proposed mechanism tracks zeros through the **completion
parameter**, rather than estimating unsigned counts separately or
moving a real exponential tilt. Only its source coverage is nominated
next: a finite-interval, full-multiplicity crossing index at the
singular completed endpoint. No crossing formula, arithmetic saving,
uniform epsilon limit or mathematical continuation is approved now.
Independent K=0, higher-derivative and global positivity gaps remain.
Full matching Mathlib coverage is unknown; no cross-notebook input.
