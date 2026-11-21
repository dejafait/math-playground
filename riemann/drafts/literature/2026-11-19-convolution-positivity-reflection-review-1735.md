# Convolution positivity reflection: source comparison1736

TARGET: Review whether convolution by C032u's nu_1 reflects positivity for finite real signed Borel measures of mass one on [0,infinity), distinguishing general counterexamples from this qualified law.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed bounded exact-property, signed-factor and compound-Poisson-inverse searches; inspected primary inverse formulas and relevant construction cases, and checked C032j/q/r/s/u/v, assessment1559, notes1552 and reverse-order stop1553. Exact query/source ledger is in 2026-11-19-convolution-reflection-source-notes-1736.md. No novelty inference from search failure.
SOURCE_EVIDENCE: Trabs2015 Section4.2 equation(4.8) p1636 and unnumbered finite-signed-inverse display p1637 https://www.numdam.org/article/AIHPB_2015__51_4_1620_0.pdf ; Cekanavicius--Vellaisamy2018 Section1 exponential-measure definitions/norm bound and proof of Theorem2.1 equations(23)-(24) https://www.vmsta.org/journal/VMSTA/article/114/read ; Bertoin2000 Theorem1.2(ii)/proof pp7-8 and finite-activity p9 https://www.maphysto.dk/oldpages/events/LevyBranch2000/notes/bertoin.pdf ; reuse Mimica2015 Propositions1.4(iv)/1.8 via assessment1559.
COMPARISON: No inspected theorem grants positivity reflection for nu_1. Finite signed compound-Poisson inverses are already known; the missing actual-law test is to select a finite submeasure of nu_1's own Levy measure and check signed mass, support, negativity and positive residual law. This differs from the width-difference factor in C032u and the stopped reverse Levy order. Trabs's score-operator density hypothesis and reflected kernel must not be imported as a theorem about nu_1 itself.
GAP: The exact implication remains undecided here. No actual-law counterexample, unrestricted positive remainder, continuum factorization or tail obstruction is proved. A separately approved bounded specialization can test the finite-subfactor inverse; all-Borel positivity and a negative Borel witness are required.
REASON: Source coverage supplies a concrete inverse-factor test instead of further generic order searches; perform its actual-law application only in a later research turn. This literature-only comparison changes no lemma or mathematical script and claims no new mathematics.
LITERATURE_REASON: Essential reverse-implication coverage was missing at invocation; forward compound-Poisson coverage was reused, while only the new signed-inverse lead and its applicability restrictions were inspected.
SCOPE: The exact qualified nu_1 of C032u on [0,infinity), and arbitrary finite real signed lambda of mass one on that half-line, allowing atoms and singular parts. Do not assume a density, a positive inverse, positivity of lambda, RH, J_eta=0 or a continuum factorization. Retain C032u's full external-input qualifications.

## Original nomination1735 (historical, superseded by the completed fields)

Search the precise positivity-reflection/order-embedding property of
convolution on finite signed measures and stronger applicable results.
Inspect primary theorem hypotheses and complete essential proof cases
before treating the implication as usable. Check existing C032u/v
and their source/attempt records for overlap. Reuse their adequate
compound-Poisson coverage instead of reviewing its forward construction.
No exact deconvolution theorem or counterexample is approved by this
nomination, and a failed search would not establish novelty.

The discriminating claim is exactly:

    lambda([0,infinity))=1, |lambda|([0,infinity))<infinity,
    nu_1*lambda>=0 on every Borel set  =>  lambda>=0.

The next turn is source comparison, not a derivation of this claim.
If sources invalidate a general positivity-reflection rule, distinguish
that obstruction from any theorem about the actual nu_1. Continue an
actual-law application only with an inspected theorem whose extra
hypotheses can be checked for this law, or nominate a separate bounded
mathematical test with its missing hypotheses explicit. Abandon the
automatic reverse inference if its source comparison fails; do not
replace positivity of a signed remainder by an assumption silently.

A future common-factor approach would seek to represent positive
signed-width outputs as a fixed law convolved with a positive remainder.
If that fixed law is also proved to lack exponential moments, this
could obstruct C032r's necessary moment condition. Neither the continuum
factorization, positive remainder nor tail premise is established here;
even a successful restricted test would leave actual-Xi realization and
L030-L032/C032a positivity open. C032u's two-width sufficient range
cannot be promoted to a converse or to the continuum.

This source review prepares a test of a different mechanism; it is not
already a justified creative proof attempt. Full matching Mathlib
coverage is unchecked and unknown. No cross-notebook input is proposed.
