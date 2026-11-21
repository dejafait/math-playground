# Clustered residues instead of individual pole clearance: source assessment

TARGET: Test a clustered-residue contour replacement for C744s's clearance certificate, seeking a two-cell length from T,delta,f0,M0 and explicit complete zero-count/profile bounds without individual zero separation.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step520 searched clustered signed residues, separation-free exponential-sum detection, Turan/Nazarov propagation and explicit complete zero counts; inspected the primary statements and essential cases below and compared C645d and the named local stops. No matching fixed-budget two-cell length theorem was found in the inspected sources; this is not a novelty claim.
SOURCE_EVIDENCE: Reuse Suzuki and Boas at the versions/locations in 2026-11-11-certified-two-cell-length-audit-517.md; Beck et al. Section8.1 Theorems8.1.5/8.1.7 and proofs https://complexanalysis.org/web/sec_residue-thm.html ; Nazarov Algebra i Analiz5:4(1993), TheoremI p.5 and Section4.1 pp.57-60 https://www.mathnet.ru/eng/aa397 ; Bellotti-Wong arXiv:2412.15470v2 Theorem1.1, Sections3/5, Table2 and introductory footnotes1-2 https://arxiv.org/html/2412.15470v2 . Exact scope and access details below.
COMPARISON: Residue calculus preserves signed cluster sums, while finite-sum propagation compares whole-function suprema rather than isolating a coefficient. Complete counts are available, but they are not weighted-tail or noncancellation bounds. C744r's actual Fourier-product residues permit a distinct constrained test; generic inverse-Blaschke noncancellation is already stopped by C645d.
GAP: Derive or obstruct one quantitative cluster functional for the actual a_z, with full-complement control and the explicit H2 transfer cost. No such lower bound, contour, tail certificate or length from T,delta,f0,M0 has been proved here; all numerical profile data remain obligations.
REASON: Primary coverage is adequate for one bounded test on the unchanged target, using the specialization limits below. Generic tools are cited rather than reproved; a useful qualified intermediate bound is allowed. Approval does not assert that the proposed phase or contour inequalities hold, and preserves every prior stop.
LITERATURE_REASON: The target now replaces individual pole isolation with a cluster contour. Existing ready scope covers only the isolated selected residue under supplied clearance; the new cancellation and complete-count hypotheses need primary theorem and essential proof-case comparison.
SCOPE: Ready source coverage for the exact TARGET and the bounded test below: C744r(5),(8)-(14), C744s(8)-(12), unconditional L742/L744 identities, neutral f0 with ||f0||_2=1 and ||f0||_H2<M0, T>=1 and a hypothetical zero with |Re z0|<=T and -Im z0>=delta, 0<delta<1/2. Preserve the prescribed M0, full complement, multiplicities and at most two occupied cells. No individual gap, rightmost zero, favorable complex weight or uniform profile estimate is an input.

The following nomination records step519's then-pending source gate.
Read primary theorem hypotheses and load-bearing proof cases before
approving any derivation. A finite exponential-polynomial theorem would
need an explicit comparison with the infinite spectral complement and
the norm cost of realizing its test inside C744r's strict-slack family.
Do not assume positive spectral weights, a rightmost zero or a lower
bound on pairwise zero separation. Source version, multiplicity and
endpoint conventions are essential for any numerical count input.

The proposed bounded research test, if separately approved, is whether
one contour containing a selected off-line cluster admits a quantitatively
nonzero residue functional and a complete-complement estimate that can
replace the selected-pole disk chain. Continue only with both inequalities
under explicit data, or a useful qualified intermediate input. Stop this
mechanism if cancellation or the realization cost requires an unpaid
separation, tail or sign assumption; retain the exact failed inequality.
No such inequality is derived in this nomination.

The signed-neutral Gram-dual stop concerns unpaid growing norm costs;
the screw-remainder stop concerns a removed complement. Both remain in
force. A clustered contour is merely a distinct candidate to compare,
not evidence that these costs disappear. C744s's valid conditional
formula remains available regardless of the outcome.

Downstream use is a finite-window exclusion test given independent
positivity. It cannot establish that positivity by itself. The audit
does not justify a new central sign-producing mechanism: C744r remains
an equivalent criterion and C744s a conditional detector. This candidate
is therefore not labeled proof_attempt/creative. Full matching Mathlib
coverage is unchecked. No cross-notebook theorem is proposed.

## Completed source comparison — 11 November 2026, step520

This invocation was literature-only. Read C744r Sections2-4 and C744s
Sections1-4; reused the
step518 Boas and step516 Suzuki/source comparisons. The relevant old
generic cancellation obstruction is C645d, not a theorem about the
actual coefficients a_z in C744r. Its hypotheses and conclusion were
read, together with the signed-neutral Gram-dual and screw-remainder
stop records. No old stop is promoted to a ban on cluster contours.

No cluster functional, estimate, lemma or mathematical script was
derived or written. The pending mathematical test is still quantitative
cluster noncancellation plus a paid complete complement within the
fixed budget. PROOF.md and DAG.md are unchanged by this review.

### Primary statements and essential cases

Beck, Marchesi, Pixton and Sabalka, *A First Course in Complex Analysis*,
[Section8.1](https://complexanalysis.org/web/sec_residue-thm.html),
Theorems8.1.5 and8.1.7(1), unversioned online text, inspected
11 November2026: a simple positively oriented closed contour in a
simply connected domain, with finitely many interior isolated
singularities and analyticity elsewhere including the boundary,
integrates to 2pi i times the sum of every residue. Read the proof
by disjoint small circles and Cauchy-Goursat, and the Laurent-series
simple-pole limit proof. This supplies no lower bound on that sum.
Any future holomorphic weight must be checked on the whole enclosed
region; additional weight poles cannot be omitted.

Nazarov, *Local estimates for exponential polynomials and their
applications to inequalities of the uncertainty principle type*,
Algebra i Analiz **5**:4(1993),3-66 (English translation, St Petersburg
Math J **5**:4(1994),663-717),
[primary Russian PDF](https://www.mathnet.ru/php/getFT.phtml?jrnid=aa&option_lang=eng&paperid=397&what=fullt),
TheoremI, printed p.5: for finite p(t)=sum_(k=1)^n c_k exp(lambda_k t),
complex c_k,lambda_k, bounded real interval I and measurable E subset I
of positive measure,

    sup_I |p| <= exp(|I|max_k|Re lambda_k|)
                 (A|I|/|E|)^(n-1) sup_E |p|,

with an absolute A. Read Section4.1 pp.57-60: Proposition4.1's complex
case, Lemma4.2's disk zero count and proof, and Lemma4.3's product
bound/proof completing the case. No exponent separation is imposed.
TheoremI's formula is also legible in the primary journal's
[Russian record](https://www.mathnet.ru/rus/aa397); PDF formula OCR
alone is inadequate. Section1.1 p.10 separately discusses coefficient
norm estimates using a separation condition. This theorem propagates
a known function norm; it does not supply a coefficient-based anchor,
infinite-complement bound or numerical A certified here. It is comparison
coverage, not a ready numerical detector input.

Bellotti and Wong, *Improved estimates for the argument and zero-counting
function of the Riemann zeta-function*,
[arXiv:2412.15470v2](https://arxiv.org/html/2412.15470v2),
7 July2025, Theorem1.1: for T>=e, counting nontrivial zeros with
0<Im(rho)<=T, let m(T)=T log(T/(2pi e))/(2pi). Then both

    |N(T)-m(T)| <= 0.10076 log T+0.24460 log log T+8.08344,
    |N(T)-m(T)| <= 0.11200 log T+0.12567 log log T+3.77417.

Read Section3's argument-principle convention (multiplicities),
Theorem1.2's parameter hypotheses, and Section5's full high/low-height
split: Table2 above30610046000; below it, Platt's bound and (5.1).
Theorem1.1 is cited directly, without redoing its parameter optimization
or computational inputs. Introductory footnote1 corrects HSW's constant
9.3675 to9.4925; footnote2 states how the older Trudgian conclusion
remains valid despite its proof error. Do not infer its invalidity.
This is count coverage, not individual separation, a weighted tail,
profile control or a nonzero residue functional. Its v1 constants
are not substituted for v2.

For source provenance, also read Hasanalizade-Shen-Wong,
[arXiv:2107.06506v1](https://arxiv.org/pdf/2107.06506v1),
14 July2021, Corollary1.2, Section2's argument-principle convention,
and its complete proof in Section5, pp.14-15 including Table2.
Its printed count constant9.3675 is not approved, in view of the
correction above. Trudgian1208.5846v2 Theorem1/Corollary1 and (2.5)
were inspected but remain unused. Thus the step516 version ambiguity
is bypassed with an exact later primary theorem, not repaired by
mixing published and preprint constants.

### Reuse, duplicates, and failures

The exact Suzuki complete conjugate pairing and Boas continuation
coverage in the step518 assessment remain adequate. The step516
Danesh two-interval and unrestricted theta-selector comparisons are
reused: neither supplies this prescribed H2 budget and first length.
No new zero-free region or reciprocal-zeta continuation is proposed,
so the October quasi-RH register is not an input to this step.

C645d's read hypotheses/conclusion and its audited ATTEMPTS record
exclude the old universal positive-unit-residue/inverse-Blaschke
shortcut. They do not model the actual a_z in C744r or obstruct every
cluster weight. The step671 de Boor assessment was read for comparison:
its Proposition25, Proposition35 and contour formulas (49)-(52)
retain coupled analytic data but supply no lower bound for this sum.
Its Toeplitz relative-matrix target is not reopened or imported.

Read the named signed-neutral Gram-dual and screw-remainder stops:
growing norm cost and removal of the complement remain unpaid.
Also compared the signed-bump common-phase stop for L717: it concerns
a growing inverse kernel on a fixed outer plateau. The proposed finite
disk test below uses C744r's freely chosen small-support profile and
its actual Fourier products; it does not assume the stopped outer
kernel has a common phase. The centered-gap common-sign stop likewise
concerns different normalized residues. No older stop is erased.

### One bounded mathematical continuation

The unchanged TARGET is EXPLORE-ready, not a theorem import. Attempt
one constrained cluster functional, rather than infer noncancellation
for arbitrary complex coefficients. Start with C744r's existing
nonnegative smooth bump eta and neutral phi=eta''-eta/4. Test whether
one can quantify a common phase and a strictly positive projected sum
for the actual

    a_z=r_z F_phi(z)conj(F_phi(conj(z)))

over a small disk about z0, with controlled profile seminorms. Choosing
eta real is an allowed proposed test, not a demonstrated bound.
Keep its width, support, derivative costs and any distance from the
zeros of the neutralizing factor explicit. In particular do not infer
a uniform lower bound for that factor merely from T and delta.
Synthetic residues independent of phi cannot settle this constrained
test. If it succeeds only with additional certified data, state that
qualified intermediate conclusion and the unpaid uniformity gap.

For a contour continuation of that same test, seek an enclosing radius
and complete-complement estimate from explicit counts/profile bounds.
An upper count can be used in a proposed radius-selection argument,
but no such construction was derived here. Counts count multiplicity;
they are not proof that a computed list is complete or a contour clear.
Under rho=1/2+iz, the source height is Re(z), not Im(z). Account for
both signs by the existing conjugation/negation conventions; numerical
endpoints must match the source or be chosen away from zeros.

Retain every pole in G and the finite integral J_H. A cluster functional
of G-J_H must explicitly control its J_H contribution under C744s(8),
the whole exterior sum, and any continuation or weight norm. Do not
silently reuse C744s's selected-pole holomorphy after enclosing more
poles. Nazarov cannot be applied to the infinite h by dropping its
tail, nor can its two-supremum inequality manufacture the missing
anchor. If no numerical propagation constant is available, use only
the already assessed Boas theorem or stop that subroute.

Continue on an explicit nonzero lower bound and a complete boundary
estimate giving a checkable length inequality, or a useful rigorously
qualified intermediate bound. Abandon this proposed construction at
the first unpaid separation, common-phase assumption, weighted tail
or profile/weight norm; retain the failed inequality. Do not count a
new unknown clearance or residue constant as resolving the requested
uniformity. No actual-Xi sign, zero or finite numerical witness follows
from the present review.

### Search and access record

Queries: `Nazarov local estimates exponential polynomials Turan lemma
1994 pdf`; `Turan power sum arbitrary coefficients close exponents
lower bound separation cluster residues`; `clustered poles contour
residue noncancellation exponential sums finite signed coefficients
separation free lower bound`; `Trudgian improved upper bound argument
Riemann zeta function critical line II 2014`; and `Hasanalizade Shen
Wong explicit zero counting Riemann zeta 2022 Theorem 1.1 arxiv`.
The Bellotti-Wong lead was followed to its primary v2 theorem and
proof cases; it is not an unread search snippet. Marx's summary,
MathOverflow and search-result alleged RH proofs were not used as
theorem evidence. No absence or originality claim follows from search.

The author-hosted Nazarov PDF failed and its PS was unsupported; the
journal's Russian PDF then provided the primary theorem/proof cases.
A guessed journal ID returned an unrelated Kitaev article and was
discarded. A requested HSW v2 returned404; its submission history lists
only v1. No repeated access loop or unresolved essential source blocker
remains for this bounded test. PDF screenshot requests returned only
labels through the tool wrapper, so no visual verification is claimed;
the legible primary HTML formula plus primary PDF text was inspected.
No large certificate was generated or used.

Full matching Mathlib coverage remains unchecked. Standard residue
calculus, explicit-formula pairing, three-circles and cited counts
should be imported by their precise references in any eventual
canonical lemma; no reproof is justified. The phase/contour bound is
the unproved specialization, and a bounded attempt does not certify
novelty. No cross-notebook theorem was read. Actual-Xi positivity,
non-neutral coverage, C744q's margin and all-window assembly remain
independent. No justified sign-producing creative mechanism follows
from this detector review; development routing is appropriate.
