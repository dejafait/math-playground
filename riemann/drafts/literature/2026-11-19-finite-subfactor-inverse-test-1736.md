# Finite-subfactor signed inverse: specialization nominated1736

TARGET: Test whether the signed inverse of the compound-Poisson factor with Levy measure ell_1(t)dt restricted to [1,3/2] gives a mass-one counterexample to positivity reflection by C032u's qualified nu_1.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact-property and signed-inverse comparison1736; narrow local C032j/q/r/s/u/v and reverse-order stop1553 checks found no actual-law duplicate. Exact queries and source scope are in 2026-11-19-convolution-reflection-source-notes-1736.md; no novelty claim.
SOURCE_EVIDENCE: Trabs2015 Section4.2 equation(4.8) p1636 and unnumbered reflected signed inverse p1637 https://www.numdam.org/article/AIHPB_2015__51_4_1620_0.pdf ; Cekanavicius--Vellaisamy2018 Section1 exponential-measure definitions/norm estimate and proof Theorem2.1(23)-(24) https://www.vmsta.org/journal/VMSTA/article/114/read ; Bertoin2000 Theorem1.2(ii)/proof pp7-8 and finite-activity p9 https://www.maphysto.dk/oldpages/events/LevyBranch2000/notes/bertoin.pdf ; Mimica2015 Propositions1.4(iv)/1.8 reused via1559.
COMPARISON: Known finite-signed exponential inverses and positive Levy construction cover the tools, not this law's subfactor, its half-line inverse support, negative witness or positive residual identification. Specialize those differences only; no reproof of the general inverse or subordinator theorem.
GAP: Verify finite nonzero restricted Levy mass, positive integrable residual, mass-one finite signed half-line inverse, a strictly negative Borel witness and all-Borel positivity after convolution by actual qualified nu_1. No continuum factor, moments, J_eta cancellation or Xi realization is concluded.
REASON: A bounded actual-law test replaces unsupported general reverse positivity; this ready nomination is newly written and needs separate approval next turn before mathematical invocation. No calculation or derivation has been performed here.
SCOPE: C032j/u's exact qualified nu_1, no killing/drift, interval [1,3/2], arbitrary finite real signed half-line measures allowed; retain all actual-divisor, multiplicity, conjugation, finite-height, heat and fixed-v1 assumptions. No density of nu_1, RH or exponential moments.

## Exact permitted specialization after separate approval

Import the signed exponential framework and finite-activity inverse from
source-notes1736, accounting for Trabs's reflected kernel and using zero
drift. Check the restricted measure P and its positive residual against
Bertoin's hypotheses; use the reused Laplace uniqueness theorem only
with its finite positive hypotheses, or justify signed equality by its
Jordan components. Prove all needed convergence, normalization and
support claims rather than relying on transform positivity.

The discriminating output is a rigorous counterexample to the exact
positivity-reflection implication: lambda(X)=1, |lambda|(X)<infinity,
lambda(A)<0 for a specified Borel A, while nu_1*lambda is a probability
on every Borel set. The proposed short jump interval may isolate a
negative term; this remains a proof obligation. Failure of any check
stops this construction, without proving the reverse implication.

A result would rule out an automatic positive-remainder inference in a
potential common-factor/tail attack on C032r. It would neither decide
C032q nor establish any actual-Xi sign. No mathematical script is needed.
Classify a successful application as REPRODUCTION, not certified novelty
or a creative central mechanism. Full Mathlib matching coverage is unknown.
