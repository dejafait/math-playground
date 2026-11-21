# Fixed weighted Fourier deficit — completed source review

TARGET: Test whether the fixed positive Fourier-deficit trace on C759a's W is below 4-C-P_120-11/200, using weight (4-m(t))_+ and every omitted sine mode.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step801 searched positive-operator diagonal traces, Hilbert-Schmidt Fourier compression, Weil/digamma/sine-complement/negative-part traces and weighted localization; compared the named local stops and current Li paper45/v2. Exact queries and inspected/unread distinctions are below; no exact threshold match or novelty claim.
SOURCE_EVIDENCE: Read Hamhalter Classes of Operators (10 April2008), Definitions5.1/5.5/5.6, Proposition5.2 and Section5 integral-kernel proof/Proposition5.10, printed pp18-23; Bell Trace class operators (18 April2016), Section8 and Theorems18/19/26 with proofs. Reuse C759a Sections1-3 and L744(8), with existing scalar-enclosure coverage; compare Li45/v2 Theorem1.1 and Sections2-5.
COMPARISON: Positive diagonal trace domination is known machinery; no inspected result evaluates this fixed level4, integer-sine120-complement trace or proves its strict threshold. C759a/C759b stop different sufficient estimates; Li's full-window positivity uses different bases/costs and gives no matching shifted bound.
GAP: The concrete compression identification, complete weighted sine-tail identity/enclosure, explicit support cutoff and strict numerical comparison remain unproved. Coupling, Schur sign, parity ordering and Xi/global bridges remain independent.
REASON: Step801 completes the previously missing primary trace coverage and duplicate comparison; approve one fixed calculation as REPRODUCTION under known machinery, without deriving the new specialization or asserting a favourable value.
SCOPE: Fixed interval(-1,1), fixed120-mode odd complement, fixed level4, actual m(t)=Re psi(1/4+it/2)-log pi, all omitted sine modes, full original C and P_120; no carrier/envelope/cutoff sweep, reduced prime coefficient, neutrality, full parity theorem or Xi conclusion.

LITERATURE_REASON: The invocation-start target was REVIEW_REQUIRED: positive-compression/trace coverage and exact duplicate comparison were missing; this turn pays that source gate, not an additional review of a ready calculation.

## Step800 nomination, preserved; approval below supersedes its pending gate

Keep C759a's W, Fourier convention and supported form domain. Let
kappa_4(t)=(4-m(t))_+, where x_+=max(x,0). The proposed positive
compression on W has quadratic form

    integral_R kappa_4(t)|F_w(t)|^2 dt/(2*pi).

The proposed complete diagonal trace to examine is

    T_4 = sum_(j=121)^infinity integral_R
          kappa_4(t)|F_(sin(pi*j*x))(t)|^2 dt/(2*pi).

The independent question is whether this object is a justified trace
bound with T_4 < 4-C-P_120-11/200. Here C and P_120 are exactly
C759a(2); no arithmetic improvement is proposed. The intended use is
a positive complementary floor for Q-11/200. Its sufficiency and
quantitative value must be established after coverage approval, not
assumed here. Keep the test at the stated level4 and120-mode split.

Read primary hypotheses for positive-operator diagonal trace bounds
and the appropriate Fourier compression/trace-class statement, or
identify an adequate previously assessed elementary alternative.
Check support and integrability of kappa_4 using the actual symbol,
the full sine tail including any apparent removable denominators,
interchanges, normalization and closed-form-domain applicability.
Compare exact known results and recorded failures before approving
the calculation. Standard trace theory alone supplies no threshold.
Do not substitute a finite sine matrix or a trace preview for a
complete upper certificate. Mathlib matching coverage is not checked.

## Comparison of possible continuations

1. A further unweighted arithmetic improvement is closed at3/2 by
   the independently audited C759b. Neither another carrier nor a
   changed cutoff supplies a different authorized test.
2. A full form-dual Schur/coupling calculation could retain more
   correlations, but C759a and the4 November generic joint-energy
   source stop leave its positive complementary input unpaid. The
  4 November direct-payment stop concerns a different window and
   cannot itself rule out the present fixed-W question.
3. The fixed weighted deficit trace addresses that missing complement
   through the actual Fourier-symbol loss rather than reducing the
   prime operator. Select this bounded question. No exact coverage or
   favourable numerical value is inferred from the local search.

Continuation test: source review must either identify adequate
coverage for the exact complete trace test, or name a concrete
hypothesis/scope obstruction. If approved later, one rigorous bound
strictly below the stated threshold would justify retaining this
sufficient estimate. A proved threshold miss would stop this trace
majorant without implying failure of the actual complementary floor;
an inconclusive enclosure is not a miss and supplies no sign.

C759a supplies the fixed definitions, domain and costs; L744(8) is
the existing symbol-bound input to check if used. C759b is the reason
for abandoning the arithmetic3/2 route, not an input to the proposed
trace inequality. The existing C759a/C759b/L743 stops are preserved.
Independent gaps remain in form-dual coupling, finite Schur sign,
actual parity ordering, even simplicity/sign, Xi realization with
multiplicities and shifted/global mixed positivity L030-L032/C032a.
These missing bridges prevent treating this local proposal as a new
creative central RH mechanism. This is a nomination, not new approved
coverage; the next invocation must be literature-only for this target.

## Completed source comparison — step801, 13 November2026

This separate literature turn approves the unchanged TARGET for one
RESEARCH / REPRODUCTION calculation. The historical pending wording
above describes step800 only. No compression identity, new bound,
numerical value or complementary floor was proved in this review.

### Primary trace coverage actually read

Jan Hamhalter, *Classes of Operators on Hilbert Spaces*, extended
lecture notes dated10 April2008, [author PDF](https://math.fel.cvut.cz/en/people/hamhalte/malta07.pdf),
printed pp18-19, Definitions5.1/5.5/5.6 and Proposition5.2: a positive
bounded operator on a complex Hilbert space has an extended nonnegative
diagonal trace independent of its orthonormal basis; finiteness is the
positive trace-class condition. Read the accompanying proof and the
square-integrable-kernel discussion, pp22-23, Proposition5.10: a kernel
in L2(X times X) for sigma-finite X defines a Hilbert-Schmidt operator
with that kernel norm. The printed statement concerns a single measure
space, not an unqualified rectangular Fourier transform. The proposed
calculation can instead use the positive diagonal criterion directly;
it need not reprove a general kernel theorem or assume a rectangular
extension without explanation.

Jordan Bell, *Trace class operators and Hilbert-Schmidt operators*,
18 April2016, [author's full notes](https://jordanbell.info/LaTeX/mathematics/traceclass/),
Section8, Theorems18/19/26 and their complete proofs were read. For a
bounded operator, Section8 defines trace class by summability of the
absolute-operator diagonal; Theorem19 gives absolute diagonal summation
and basis independence once trace class holds. Theorem26 gives operator
norm at most trace norm. For a positive trace-class operator the latter
is its trace. These are supporting standard results, not an evaluation
of the proposed Fourier compression. The cited book matches in Bell
are Conway, *A Course in Operator Theory*, p88 Propositions18.8/18.9;
the book itself was not separately inspected. Bell's proofs use
Hilbert-Schmidt factorization/absolute summability and the compact
positive spectral theorem, respectively.

The Reed--Simon VI.6 scan was located, but supplied no readable theorem
text in this retrieval; the attempted local download failed DNS.
No claim relies on that scan or its search snippet. The two readable
author sources above pay the needed abstract coverage, so this access
failure is nonessential and requires no retry.

### Applicability obligations approved for the later calculation

C759a Sections1-3 fix the supported logarithmic form domain, real odd
space W, unit-norm integer sines, Fourier measure dt/(2*pi), complete
prime cost C and projected negative pole cost P_120. Its audited
Section6 and assessment793 retain the core and normalization checks.
Reuse Suzuki's realization and the existing digamma remainder through
that coverage; do not import its small-window sign at a different
parameter. L744(8) is an all-real scalar bound independent of its
modulation-family application. Its logarithmic lower estimate is an
appropriate input for certifying the support cutoff of kappa_4, and
its global estimate covers the origin. The fixed line Re(z)=1/4 has
no digamma poles. No new quantitative cutoff is asserted here.

The later calculation must construct the bounded positive compression
on the complexification of W (and restrict its form to real W), prove
the displayed diagonal sum represents its trace, and establish
finiteness before invoking trace-norm domination. Its multiplier needs
measurability, boundedness and integrability. Pay these using the actual
symbol and an explicit cutoff; a nonnegative integrand permits Tonelli,
whereas a signed interchange needs its own justification. Verify the
resulting lower-form implication on the entire C759a domain, retaining
both C and P_120 and the exact shift11/200. This is the concrete
specialization still to prove, not a theorem imported by this approval.

For the all-mode enclosure, C759a(7)-(8) already supplies the integer-sine
Fourier formula and a complete inverse-square-tail comparison in its
stated frequency range. Certify a cutoff inside that range before
using its denominator estimate; otherwise justify the transform at
every removable denominator using its defining integral. A finite
mode sum needs a complete upper tail to certify success. Monotone
partial sums may certify a lower bound for a miss. Do not treat a
failed upper-bound comparison as evidence of a miss. Bound the actual
weighted integral and every enclosure/remainder error; sampling,
uncontrolled quadrature and a finite sine matrix are insufficient.
Reuse the already assessed scalar/rounding conventions in C759a
Section5 and assessment793; their old numerical outputs are not new
digamma-integral enclosures. No particular quadrature or tail bound is
asserted here. Reproof of general trace theory is unnecessary; the
fixed projection, normalization and complete numerical bound require
the specialization rather than a citation alone.

### Duplicate and failure comparison

The narrow local comparison read C759a's full statement and relevant
proof, L744's scalar-input paragraph and Section2, assessments791-793/795,
the4 November joint-energy assessment and its stop, and the direct
archimedean-payment stop. No matching weighted trace was found there.
C759a's scalar two-region estimate fails; C759b's independently audited
arithmetic obstruction closes the3/2 replacement. Neither computes the
present weighted deficit. The direct-payment counterexample is at
L=4log3 with a different compensated resource. Generic Schur algebra
still requires a paid complement. These remain scoped failures, not
global prohibitions on the present fixed-W test.

Also inspected Hongmin Li, *Cutoff-free
positivity of localized Weil forms through the (log11)/2 threshold*,
[paper45/v2](https://rstation.ai/problems/riemann_hypothesis/papers/45),
9 November2026, Theorem1.1, (2.1)-(2.5), Lemma3.1/proof and Sections4-5
through (5.5). It asserts strict positivity for0<a<=(log11)/2 without an
explicit coercivity constant. Its odd basis is half-integer, with400
retained modes and boundary responses/covariance tails. This covers
unshifted positivity at a=1, not this integer-sine120-complement trace
or floor above11/200. The supplement was not replayed and no certificate
imported. Historical source-access stops do not deny this readable version.

The related [uniform-tail discussion](https://rstation.ai/r/riemann_hypothesis/posts/42),
opening Lemma A and its displayed modulation proof, concerns the
unweighted finite-codimension arithmetic block. This is overlap
evidence for retaining C759b's stop, not a proof about the present
weighted full energy; none of its numerical tables is imported.

Exact new queries: `positive operator trace orthonormal basis sum
diagonal trace class Hilbert Schmidt Fourier compression`;
`"Weil" "digamma" "sine" "trace" operator positivity`;
`"Weil" "Fourier" "deficit" trace digamma`;
`"digamma" "trace" "positive part" Weil`;
`"Weil" "sine" "complement" operator trace`;
`"Fourier" "negative part" "trace" compression symbol localization operator`.
Other returned summaries/knowledge indexes and unrelated localization
papers were not inspected as theorem inputs. No failed search proves
novelty; no broader source archive or cross-notebook proof was read.

### Decision and continuation

SPECIALIZE is ready for the exact saved TARGET. Full matching Mathlib
coverage remains unchecked; the primary inputs concern standard trace,
Fourier and scalar-asymptotic machinery, not a formalized fixed threshold.
The new evidence is completed source coverage and a concrete stronger-
source comparison, not a new mathematical result beyond those sources.

One rigorous full upper enclosure strictly below4-C-P_120-11/200
justifies retaining this sufficient complementary estimate; a proved
lower enclosure at or above the threshold stops this trace majorant.
An overlapping enclosure is inconclusive and gives no spectral sign.
Keep level4,120 retained integer sines, every omitted mode and the
original costs fixed. Independent coupling/Schur, parity, even
simplicity/sign and Xi/global positivity gaps remain. No justified
creative central mechanism is ready: the missing full-energy/Xi bridge
prevents classifying this ordinary trace specialization as creative.
Next work defaults to the approved calculation, without another
unchanged-scope literature turn.
