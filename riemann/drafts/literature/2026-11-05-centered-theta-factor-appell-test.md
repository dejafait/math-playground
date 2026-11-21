# Centered theta factors — bounded Appell compatibility test

TARGET: Test whether the unique additive self-convolution factors of the centered monic actual-theta P_2 and P_3 satisfy Q_3' = 3Q_2 in common coordinates, using L791's audited coefficients through j=3.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step627's uniform-symbol comparison searched finite-free Appell square roots and degree compatibility; narrow local screen found no exact centered-factor lowering test. Reuse fixed-degree inversion/preservation from step620 and the current orientation comparison; no novelty claim.
SOURCE_EVIDENCE: Campbell https://arxiv.org/html/2412.20488v3 Section1.4/(1.24)–(1.26) and (1.1); Marcus–Spielman–Srivastava https://arxiv.org/pdf/1504.00350v2 Definition1.1/(1)–(2), printed pp.2–3; Arizmendi–Perales https://arxiv.org/pdf/1611.06598v2 Propositions3.4/3.6 and proofs, printed pp.7–8; directly rechecked in step628, reusing step620 qualifications and 2026-11-05-theta-additive-degree-compatibility.md.
COMPARISON: One common constant-coefficient differential symbol implies the Appell derivative relation. Fixed-degree coefficient inversion permits constructing the two unique factors without assuming real roots. Centering first addresses L824's actual proposal; testing the uncentered leading coefficient alone would miss this scope. No specialized factor or mismatch has been derived here.
GAP: Derive exact centered degree2/3 factor identities and uniqueness, then decide whether their derivative defect vanishes using complete audited coefficient evidence. An equality at this prefix does not prove an all-degree symbol or signs.
REASON: Step628 repairs missing direct source URLs and confirms the saved source scope; SPECIALIZE remains ready for the unchanged calculation target. No calculation is licensed in this literature-only recovery turn; the next invocation may use this repaired assessment subject to supervisor acceptance.
SCOPE: Degrees2/3 only; L019/L021/L795 actual law, L791 gamma through j=3 under L778/step433/step478 contracts; monic centering before symmetric additive inversion; one shared coordinate system, no adjustable degree-dependent dilation, no new quadrature, degree sweep, LP assertion or reciprocal convolution transport.

## Exact test and downstream use

The main gap is actual-Xi all-degree mixed positivity. A common symbol for
these factors is one possible uniform realization; rejecting its necessary
compatibility condition would prevent investing in an inapplicable sign
theorem. This is a routine known-method specialization, not a central
creative mechanism or a test of RH itself.

For each d=2,3 divide L795 P_d by its nonzero leading coefficient and
translate the resulting monic polynomial so the degree-(d-1) coefficient
vanishes. Define Q_d as its real monic symmetric additive self-convolution
root by the finite coefficient equations. Derive the exact equations and
uniqueness, including all coefficient constraints, before using an interval
defect. Do not import the unaudited L823 calculation or its signs.

The source Appell relation requires Q_3'=3Q_2 for a common symbol in these
fixed coordinates. Compare the entire derivative polynomials. A certified
nonzero coefficient excludes that common constant-coefficient symbol.
Exact equality passes only this necessary test; intervals containing zero
are inconclusive absent an exact identity. No sign conclusion follows from
equality. Do not repair a failure by degree-dependent rescaling, change
orientation or sweep further degrees in this attempt. A common affine
change may be discussed only with an explicit invariance justification;
no new family of adjustable normalizations is within scope.

The source's reciprocal Jensen orientation must remain separate from the
centered monic orientation used here. No factor transport through reversal
is assumed. Failure excludes neither degree-dependent factors nor a
variable-coefficient differential realization, other positive realizations,
actual polynomial hyperbolicity, or RH. Any new mechanism needs its own
source coverage. Uniform factor signs and mixed/shifted transfer remain
unresolved even if compatibility passes.

Inspect the full relevant gamma endpoints in
`scripts/central-jacobi/fixed-model-certificate-476.json` and complete
load-bearing audit evidence in `scripts/central-jacobi/audit-478/audit-report.json`.
The inherited L778 analytic error/software contract and step433 audit remain
premises; a preview or midpoint is insufficient. If those contracts do not
support an input, stop with that limitation; no replacement evaluator is
approved. L824 is motivation only; no cross-notebook input. Full matching
Mathlib coverage is unchecked. New formulas and any rigorous arithmetic
belong in a later canonical lemma with its actual mathematical inputs.

## Direct-source recovery review — step628

LITERATURE_REASON: The supervisor identified missing direct source URLs in
this ready assessment. This bounded review repairs that exact issue rather
than reopening discovery or changing the mathematical target.

The three versioned primary links in SOURCE_EVIDENCE were retrieved on
2026-11-05. Campbell v3 is dated 18 December 2025; its displayed (1.1)
is the derivative condition. Section1.4 distinguishes Jensen orientation
from the reversed Appell orientation and allows a formal differential
symbol in (1.26). Thus this necessary compatibility test does not require
assuming an entire Laguerre–Pólya symbol. Such a sign assumption remains
essential for an automatic all-degree real-rootedness conclusion.

Marcus–Spielman–Srivastava v2 (3 July 2019), Definition1.1, admits complex
polynomials of degree at most d and fixes d in the coefficient operation;
its differential form is (2). Theorem1.3 additionally requires real-rooted
degree-d inputs. Arizmendi–Perales v2 (7 March 2017), Proposition3.4,
gives coefficient/cumulant inversion; Proposition3.6 applies to monic
degree-d polynomials. Their proofs on printed pp.7–8 use formal series
and partition inversion, not an assumed positive root law. These source
statements support the planned algebraic test but do not certify signs
of its factors. No specialized identity or factor is derived here.

Reuse step620 for the prior exact-statement search and fixed-degree
qualifications, and step627 for the orientation comparison and recorded
automatic-import failures. No new duplicate or obstruction is claimed.
The local interval evidence was intentionally not loaded: it is essential
to the future arithmetic, not to this URL/source-scope repair. The
continuation retains all L791/L778 contracts and the complete-evidence
inspection requirement above. Mathlib matching coverage remains unchecked.
