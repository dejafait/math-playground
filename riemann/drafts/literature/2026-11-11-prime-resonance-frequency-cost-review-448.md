# Quantitative prime-return cost: completed source comparison

TARGET: Assess an explicit two-prime resonance-frequency lower bound for real |t|>=1 and max(||t*log(2)/(2*pi)||,||t*log(3)/(2*pi)||)<=delta, 0<delta<1/10, and compare its constants and scope with L744's fixed-family complete-energy floor.
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step449 read the full October4 Matveev assessment, canonical L365 and the relevant L743/L744 statements and energy estimates; compared the recorded prime-only and generic joint-energy stops. Targeted external searches located Laurent2008 Corollary2 and asymptotic irrationality-measure leads; exact queries and inspected passages below. No novelty inference.
SOURCE_EVIDENCE: Reuse Matveev2000 Corollary2.3 (2.4)-(2.6), with Sha1505.07147v6 Section2.4 (2.19) freshly checked; read Laurent2008 Acta Arith133 pp326-328, Corollaries1-2/Table1, and the positive-real proof case p347, DOI10.4064/aa133-4-3, original article in the linked full-text mirror. No source proof audit or real-frequency theorem is claimed.
COMPARISON: Explicit integer-logarithm separation is covered by Matveev and Laurent; continuous-frequency elimination and zero-coefficient cases would be an elementary specialization, not a new transcendence result. Neither source supplies the joint signed deficit missing from L744. Its fixed-family high-frequency floor already needs no return assumption; sharper return exclusion alone does not sign the bounded-frequency range.
GAP: No F(delta) has been derived or certified here. A later arithmetic application must eliminate t, bound its nearest integers and handle zero integers and the entire |t|>=1 range. More essentially, no implication from an unfavorable complete-energy vector to this prescribed simultaneous return is supplied; general supported tests and growing K/M remain outside L744.
REASON: Essential arithmetic source coverage is available, but the proposed direct sign transfer fails its relevance test: the sources constrain returns without paying the missing joint form. Park return-frequency-only signing; retain the cited separation as reusable supporting input, without performing a redundant specialization.
LITERATURE_REASON: This real continuous-frequency, two-prime return problem and its comparison to L744 lie outside the saved Gaussian regulator application and the conductor-spectrum review. Essential exact-target coverage is incomplete.
SCOPE: Literature comparison only, completed step449. SPECIALIZE records adequate arithmetic coverage, not an energy theorem or authorization to retry return-frequency-only signing. No new logarithmic-form derivation, lemma, script, return-time computation, growing-window theorem or retry of L752's matrix was performed.

The main gap remains actual-Xi positivity L030-L032/C032a, with the
independent L966/L968 and L984(H) conditions unresolved. A quantitative
return-cost bound could help test whether near-maximal arithmetic
coupling is confined to frequencies whose logarithmic energy is
already paid. This is a proposed intermediate use, not a proved
joint-energy inequality. L743's obstruction remains valid.

Essential continuation IDs: L743's complete prime-delay operator and
exact neutral-correction setting; L744's fixed K,M,chi, smooth compact
core and energy floor. L740/L741 fix the complete-energy conventions.
Use ||x|| for distance to the nearest integer. The restriction |t|>=1
is part of the target and must not silently become a sufficiently
large-frequency hypothesis. Cases where a nearest integer is zero,
the first nonzero return, and the delta range require explicit scope.

First inspect the saved Matveev assessment's detailed theorem statement
and its canonical L365 application, as a local comparison only; avoid
reproving known logarithmic separation. Compare stronger two-logarithm
results and known obstructions if existing coverage is inadequate.
Do not infer that L744's fixed-envelope floor covers arbitrary neutral
functions, all M, growing K or the bounded-frequency complement.

Continuation test: require an explicit primary inequality applicable
to the real-frequency conditions, constants and exception range that
can actually be compared with L744's floor. Record if it only gives
an asymptotic return restriction already irrelevant after the fixed
floor, or cannot control the joint signed deficit. In that case park
this nomination without pretending that an irrationality statement
supplies full energy positivity. Any later attempt must identify the
additional quantitative saving sought before it is approved.

No justified creative central attempt is yet ready: the proposed link
between return exclusion and a signed whole-form estimate is missing.
This review prepares a bounded decision about that link; it does not
route a standard Matveev specialization as creative. Full matching
Mathlib coverage is unchecked. No cross-notebook input is needed.

## Completed review: 11 November 2026, step449

The preceding nomination is preserved as the invocation-start question.
The completed decision is the single-line metadata above. The main gap
is still actual-Xi positivity L030-L032/C032a, not irrationality of a
ratio of prime logarithms. L966/L968, L984(H), and C997s's bridge remain
independent unresolved conditions. This step establishes no new lemma.

### Exact arithmetic input and scope

The October4 assessment was read completely, including its Matveev
parameter definitions and access qualifications, followed by L365's
arithmetic specialization. Its different fixed-regulator sign application
is not transferred. Matveev's Corollary2.3, Izv. Math.64:6 (2000),
1217-1269, supplies the additive form, not the exponential-minus-one
form. The saved original-theorem evidence is reused. The freshly opened
[Sha v6](https://arxiv.org/pdf/1505.07147v6), pp12-13, Section2.4,
(2.19), confirms the general coefficient dependence log(eB), with
integer coefficients, a nonzero form, degree D, principal logarithms,
and A_j>=max{D h(alpha_j),|log(alpha_j)|,0.16}. It has no large-B-only
exception. Positive primes are rational, with real principal logarithms
and heights log p, as already justified canonically in L365. Using
this source requires no reproof of its transcendence estimate.

**Sharper two-logarithm comparison.** Michel Laurent, *Linear forms in
two logarithms and interpolation determinants II*, Acta Arith.133 (2008),
325-348, [publisher record](https://doi.org/10.4064/aa133-4-3),
[original article mirror](https://scispace.com/pdf/linear-forms-in-two-logarithms-and-interpolation-23tmjmyto5.pdf).
Read pp326-328, especially Corollary2/Table1, and its positive-real
proof case p347. For multiplicatively independent alpha_1,alpha_2>1,
positive integers b_1,b_2 and real logarithms, put
Lambda=b_2 log(alpha_2)-b_1 log(alpha_1),
D=[Q(alpha_1,alpha_2):Q], log A_i>=max{h(alpha_i),log(alpha_i)/D,1/D},
and b'=b_1/(D log A_2)+b_2/(D log A_1). Corollary2 gives

    log|Lambda| >= -C_2 D^4 max{log b'+0.38,m/D,1}^2 log A_1 log A_2.

Table1 includes (m,C_2)=(10,25.2),(30,17.9). The latter has a larger
cutoff; its smaller coefficient is not uniformly preferable. The real
proof chooses h=max{D(log b'+0.38),m,D},
a_i=(rho+1)D log A_i and Table3's parameters. This is an inspected
cited theorem, not an independently certified proof or new bound.

For the proposed two-prime application, the field and height conditions
are known; multiplicative independence is justified by unique prime
factorization. A later application would have to introduce nearest
integers for the two real phases, eliminate the continuous variable,
track the resulting error and coefficient bound, and split off cases
where a nearest integer is zero. Those are unperformed obligations,
not exceptions silently removed from the target. In particular the
source does not itself state F(delta) for all real |t|>=1. Its height
floor 1/D differs from Matveev's 0.16; substituting log2 without checking
this floor would be invalid. No first-return threshold is certified.

Search results also led to Rhin-type and Wu-Wang irrationality-measure
claims. Their original theorem statements, effective constants and
exception thresholds were not inspected; they remain unused leads.
An asymptotic exponent for log3 or a rational linear combination is
not automatically the explicit, all-range two-phase statement sought.
No claim of optimal constants or exhaustive literature coverage is made.

### Comparison with the complete form: why this nomination is parked

L744's exact identity (6), correction estimates (12)-(17), and conclusion
(4) were inspected. Its full arithmetic mass C_prime retains every
prime power below exp(L), with coefficient two, and its pole term
vanishes by the exact complex-linear correction. For fixed K,M,chi,
the certified lower bound is log(|t|/(2pi))-C_prime-epsilon(t),
epsilon(t)=O_(K,M,chi)(1/|t|), beyond its stated t0. These constants
are independent of the envelope within that fixed family, but not of
K,M or chi. No numerical floor onset for a concrete family is supplied
by the current target, which specifies none of those parameters.

A return-time theorem would only restrict a particular carrier's phases.
L744 already pays the sufficiently high carriers without that restriction.
Neither inspected arithmetic theorem states that a large Rayleigh value
of the delay sum forces the proposed pair of phases for an arbitrary
supported test, nor controls the archimedean/arithmetic correlation at
bounded carriers. There is no inequality comparing that deficit to the
remaining negative part of the full energy. Thus no claimed constants
from these papers fill the missing link. This is a source-to-target
scope conclusion, not an impossibility theorem for a future joint bound.

The prime-only equality in audited L743 and the step284/285 stop remain
valid; the generic joint-energy import stop286 and conductor stop448
also remain. The changed real-frequency problem is not a duplicate of
L365's Gaussian regulator application, but deriving its known arithmetic
specialization alone would not repair those failures. Park it as a
standalone signing strategy. Reopening requires a new quantitative
implication linking a bad complete-energy vector to the arithmetic
return/deficit, with a threshold in L744's exact family or an independently
justified replacement. A historical stop is not a ban on that new work.

### Search/access record and next nomination

Queries: `Laurent Mignotte Nesterenko 1995 deux logarithmes Corollaire 2
24.34 pdf`; `Laurent linear forms two logarithms 2008 Corollary 2 17.9
pdf`; `Rhin log 2 log 3 irrationality measure 8.616 explicit lower bound`;
`Laurent Linear forms in two logarithms and interpolation determinants II
pdf 2008`; `Mignotte A corollary to a theorem of Laurent 1998 22`.
The journal record confirms Laurent's identity/DOI. Its original text
was readable in the mirror. Guessed ICM Laurent download failed;
Mignotte1998's ICM PDF returned403, so its snippets are not theorem
evidence. The Laurent p347 screenshot timed out; the complete relevant
positive-real text case was read. No access failure blocks the adopted
Matveev/Laurent statements. Full proofs and numerical tables were not
independently replayed.

The next nomination changes mechanism from recurrence arithmetic to
finite-support operator geometry. A narrow search in the prime/neutral/
energy assessments and stops located the already inspected
Haagerup-de la Harpe input in
[the centered-jet assessment](2026-11-01-centered-first-jet-numerical-radius.md).
That assessment concerns L627's different rational compression; it does
not approve a new delay-sum application. Its exact Theorem1(1) input is
a lead to reuse before new browsing. The half-Beckner allocation stop
L746 and negative localization defect L750 were checked as contrasts;
neither is a theorem about replacing L744's crude arithmetic mass by a
finite-support numerical-radius bound. The new review must check whether
that replacement is already subsumed, whether it supplies a meaningful
saving, and all integer-endpoint cases. It is uncovered, not approved
mathematics or a justified creative central mechanism yet.

Mathlib: matching quantitative logarithm/continuous-return and complete
joint-energy results remain unchecked. No library absence is asserted.
Completed classification: LITERATURE / KNOWN_IMPORTED; outcome NEGATIVE
for the proposed direct signing route. Only local source scope progressed.
No mathematical exploration budget was used or reset, no cross-notebook
input was read, and no RH candidate is asserted.
