# Integrated coprime pole pair: audit coverage approved in step2085

TARGET: Critically audit C034s's finite square-cutoff identity and complete integrated conjugate-pole principal part, checking whether its noncancellation conclusion stays local and leaves the one-sided GC12 upper unresolved.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Step2085 reused the exact-object searches and primary readings recorded in drafts/literature/2026-11-21-coprime-mellin-source-notes-2082.md and source-notes2080, then compared all of C034s with that coverage and C034r's kernel passages; targeted local checks included stops2076/2077/2079/2084 and recovery2083. No duplicate audited integrated-pair result was identified in these checked paths; no new web search or novelty claim.
SOURCE_EVIDENCE: Reused inspected primary coverage: Bhowmik--Essouabri--Lichtin Lemma1 and extraction proof/Theorem1, author proof PDF pp4-8 https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/multieuler.pdf ; Ramare2016 Theorem1.1 and endpoint proof pp109-110,116 https://numdam.org/item/10.5802/ambp.356.pdf and 3 October2021 addendum Theorem1.1/Note1/proof pp1-4 https://ramare-olivier.github.io/Maths/TruncatedPerron-5-Addendum-04.pdf ; Van Hemert v1.0.0 GC12-GC18 and fixed-band proof https://raw.githubusercontent.com/LeonardSEO/riemann-xi-zero-detection/refs/tags/v1.0.0/paper/paper.tex . Full citations, hypotheses and reading limits are in source-notes2082/2080; C034r supplies the local actual-kernel specialization.
COMPARISON: The sources cover extraction and inversion techniques, not C034s's prime-dependent remainder, exact finite two-cutoff identity, height-chain correction or integrated local principal part. A separate audit can check those claimed specializations using the already covered standard tools; no missing essential source theorem or adequate exact import was identified. This approves an audit, not C034s or its stop.
GAP: Independently verify C034s(11)-(18), especially the finite-R identity (13), its connection to the limiting local germ (17), arbitrary multiplicity and the strictly local scope of (18). The one-sided GC12 upper, global contour estimates and cancellation with other terms remain outside this assessment.
REASON: The new claim-level comparison below discharges the nomination's coverage gate without repeating the mathematical test. EXPLORE permits independent conceptual audit of the exact target; no new lemma, reproof, mathematical script or canonical input is produced in this literature turn.
SCOPE: Exactly TARGET, with C034s as the audited claim and C034r as its actual-kernel input; q=2 and the specified fixed bump; conditional finite-order zero m>=1, 0<delta<1/2; both cutoffs, all pre-shift errors and ordered limits. No global asymptotic, Omega result or signed-upper contradiction is covered.
LITERATURE_REASON: The audit of newly completed C034s required separate coverage approval after2084. Step2085 compares its precise claims with reusable2081/2082/2080 coverage; no essential unread theorem was identified, so no redundant external retrieval is needed.

## Requested scope and decision test

The proposed audit concerns C034s only, with C034r's actual kernel and
fixed nonzero bump as its mathematical input. L030-L032/C032a explain
the main-gap relevance; they are not premises in the residue calculation.
The GC12 sum is defined explicitly. GC13/GC18 remain source-inspected
but locally unaudited; their validity is not assumed in C034s.
No cross-notebook theorem is requested.

Check the absolute initial region and normal Euler-product convergence;
positivity at the conjugate pair; the sharp-window Fourier normalization;
both Perron boundary errors and their product; the shifted-height chains;
the order of the T and R limits; local holomorphy and full Taylor polar
part for arbitrary m>=1, 0<delta<1/2; and the scope of the resulting
negative route decision. In particular, no rightmost-zero, zero separation
uniform in all zeros, simplicity or RH premise may enter.

Continue using the stop only if the actual integrated local numerator
and both cutoffs survive audit and the claim remains strictly local.
An error in the representation, positivity, multiplicity accounting or
scope must be repaired or must retract only the affected conclusion,
preserving the original attempt. No global M_K asymptotic, Omega theorem,
one-sided-upper contradiction, high-primitive estimate or mixed-form
transfer is part of this audit. Full matching Mathlib coverage is unknown.

After the separate coverage comparison below, this is a proof_audit/conceptual_audit:
the difficult point is the relationship between a local two-variable
principal part and a finite signed quantity, not routine arithmetic.
The preceding scope was nominated in2084. Step2085 supplies coverage
approval below; the critical mathematical audit remains unperformed.

## Separate source comparison2085

This is a literature-only review, not a replay of the proof. Read the
whole canonical C034s to identify its claims, and C034r's hypotheses,
conclusion, theta/input bounds and weighted multiplier passage. Reused
the primary theorem readings and queries in source-notes2082/2080 and
the direct-access record2083. The same series and kernel were searched
there; the audit does not enlarge their mathematical hypotheses.
No new internet search is needed solely because a local proof now exists.

The main gap remains L030-L032/C032a actual-Xi all-degree algebraic
mixed positivity. The intermediate target is verification or correction
of C034s's local obstruction and finite representation. Its plausible
use is deciding whether automatic pole removal can contribute to a
low-primitive-sector upper compatible with C034r's detection threshold.
It does not pay the high sector, scale errors, full source energy or
mixed-form transfer. These are independent unresolved steps.

| Claims to audit | Existing coverage and limit | Required audit work, not performed here |
| --- | --- | --- |
| C034s(2)-(3), (10): extraction and local nonvanishing | Bhowmik--Essouabri--Lichtin, cited Lemma1 and Theorem1: analytic exponents with fixed integer coefficients and a holomorphic Euler remainder. GC12's prime-dependent p/(p+1) is outside that direct statement. | Check the displayed factors, absolute initial region, compact normal convergence and every nonvanishing condition directly. No generic theorem is imported as proof of the claimed positive value. |
| C034s(8)-(9): actual Fourier density | Standard named Fourier inversion, correlation/convolution and Plancherel; C034r fixes the normalization and input regularity. Kowalski A.3.1-A.3.2, read in2082, concerns smooth Mellin inputs, not this sharp window. | Check the actual window identity, Fourier signs and factors, L1 justification and positive mass; retain the window's endpoints and cusp. No smooth-window replacement is authorized. |
| C034s(11)-(13): two finite square cutoffs | Ramaré Theorem1.1 assumes kappa>0 above absolute convergence, complex coefficients and T>=1, retaining both series and short-interval errors and endpoint choices. Its theorem is not the displayed two-variable formula. | Audit C034s's own classical Perron specialization and tail argument, x=K+1/2, all absolute majorants, both single errors and their product. Its claim for T>0 must rest on its own argument, not an extension of the cited T>=1 theorem. |
| C034s(13)-(14): shifted-height chains | The cited Perron theorem supplies no two-variable ratio-integrated height correction. The 2021 addendum qualifies good-height/measure statements and does not supply a simultaneous choice for this expression. | Check orientations and endpoints, finite-contour Fubini, the absolute-domain bound and first T then R limit. Do not replace these with a generic good-height assertion. |
| C034s(15)-(18): local principal part | Standard named Taylor expansion and residue theorem, with holomorphic parameter integration. The checked sources contain no matching integrated-pair conclusion. | Check the bidisk, finite multiplicity, local nonvanishing, single as well as double polar terms, finite-R convergence and residue coefficient. Distinguish a claim under audit from an imported theorem. |
| Scope of the route stop | The source comparison2082 already distinguishes an arithmetic pole, an integrated local germ and a global signed-sum contribution. Van Hemert GC13/GC18 retain independent decomposition/error and upper-bound obligations. | Determine whether (13) supports precisely the local statement claimed, without asserting an uncanceled contribution to the whole sum, a rightmost zero or a global shift. |

For exact citations and source versions, reuse source-notes2082:
Bhowmik--Essouabri--Lichtin, *Forum Math.*19(2007),1111-1139,
DOI10.1515/FORUM.2007.044, author proof PDF pp4-8 (not assumed final
pagination); Ramaré, *Ann. Math. Blaise Pascal*23(2016),109-128,
DOI10.5802/ambp.356, plus the dated addendum; and van Hemert,
v1.0.0, 11 October2026, DOI10.5281/zenodo.23295277, tagged TeX
GC12-GC18 lines11613-11702, fixed-band lines11124-11317.
The tagged manuscript is not treated as independently verified.
Delabarre's natural-boundary statement and its unread long proof do not
become essential inputs to an interior local audit. No source is silently
upgraded from a read statement to a verified proof.

## Duplicates, failures and continuation test

The scoped searches/readings found the prior mechanism nomination2081,
its source comparison2082 and the producing result2084, rather than an
independent verification of C034s. They do not establish novelty.
Stops2076/2077 concern a universal positive inverse and identity-only
development; stop2079 concerns other direct imports. None prohibits
checking this actual signed-kernel calculation. Stop2084 is the precise
claim awaiting audit; its failure must not be used as a premise to
validate itself. Preserve all of these records.

Continue using the local stop only if the finite-cutoff representation,
integrated principal part, coefficient and stated qualifications survive
independent audit. A substantive error requires correction or retraction
of the affected conclusion in a later research turn, preserving the
original argument. If the local statement survives but no global shift
is paid, the audit must leave the one-sided upper unresolved. Success
would establish reliability of this local input, not RH or an advance
beyond all existing literature.

Essential input is C034r's actual kernel; C034s is the object to check.
L030-L032/C032a give relevance only; C034q and the prior stops are
contrasts. No cross-notebook input, RH, simplicity, rightmost-zero
assumption or uniform zero separation is authorized. GC13/GC18 are
source-inspected but locally unaudited. Full matching Mathlib coverage
remains unchecked; supporting classical tools are named above.

Outcome2085: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED, actual task
literature_comparison. The new evidence is the claim-level source/scope
comparison, not a mathematical verification or a newly found theorem.
No essential source-access blocker remains. The exact unchanged TARGET
is ready for one proof_audit/conceptual_audit turn; this review neither
reruns the stopped mechanism nor approves a global residue argument.
