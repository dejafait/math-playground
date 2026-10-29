# Moving-anchor cutoff critical audit — approved source scope

TARGET: Critically audit L468's uniform moving-anchor cutoff, including logarithm losses, the finite-rectangle transfer, the full integer bound and zero-multiplicity quantifiers.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared the full written L468 and L266 general interface with the existing construction assessment; searched moving-anchor, finite-rectangle and uniform-logarithm terms in the relevant local assessment/audit paths and checked the recorded fixed-anchor failure. Reused the construction assessment's exact-statement and stronger-result searches rather than repeating discovery for an unchanged theorem target.
SOURCE_EVIDENCE: Reopened Ramachandra (1995), Theorems 1.5.1, 1.5.2 and 1.6.1, printed pp. 26-29 (PDF pp. 36-39), reading the statements and interpolation/coefficient proof cases; reopened DLMF 5.11.9 including its bounded-real-part uniformity sentence. Reused inspected Grava Lemma 4.16 and the registered external premise; no new external-manuscript audit.
COMPARISON: The explicit radius-dependent inequalities and bounded-domain principle cover the tools actually invoked in L468; gamma uniformity covers moving bounded real parts. Neither the source theorems nor L461 supply L468's uniform quotient or integer cutoff by citation. The completed finite-rectangle application and one-onset quantifiers require a separate conceptual audit.
GAP: No essential unread source is identified for this exact audit. Check all uniform constants, both circle heights, anchor, geometric prefactor, integer ceiling and multiplicity quantifiers. The external premise and its import closure remain locally unaudited; no initial signs or effective onset follow.
REASON: Approve the unchanged exact audit as a REPRODUCTION of quantitative source applications. This source-only approval does not validate L468 and does not extend the authorized scope to an endpoint theorem, changed zero-free premise or external-manuscript verification.
SCOPE: Conditional actual-Xi statement with d=(log log T)^(-1/2), eta=3/8+d, R=3/8+2d, T=2+|a| sufficiently large, arbitrary nonreal displacement within the retained closed zero strip, and arbitrary central multiplicity.
LITERATURE_REASON: The completed finite-rectangle application and explicit C=3 ceiling bound create a new audit scope; compare it against existing primary coverage before the audit, reusing adequate sources without repeating broad searches.

## Bounded review and source comparison

The main gap remains initial Xi signs at unbounded heights and global
mixed positivity. The newly written
[L468](../../lemmas/L468-moving-anchor-uniform-witness-cutoff.md)
would narrow the initial range a later sign estimate must cover.
It is a REPRODUCTION under the same locally unaudited external
Theorem 1.1, September 30, 2026, at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, strict Re(s)>7/8.
No numerical onset, boundary exclusion or initial sign is asserted.

Reuse [the construction assessment](2026-10-26-moving-anchor-explicit-rate-coverage.md).
Its primary source inequalities expose the radius dependence,
bounded-domain maximum modulus and gamma uniformity. This separate
source turn compared them with the completed proof's actual uses;
no additional essential source is identified. The scope is ready for
mathematical audit, without a claim that the application passes.

The reopened [Ramachandra text](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr85.pdf#page=36)
requires an analytic closed annulus for Theorem 1.5.2; its proof uses
integer powers and rational approximation. Theorem 1.6.1, equation
(1.6.1), assumes analyticity on the closed disk and a boundary
real-part bound; its coefficient proof displays the radius-gap loss.
Theorem 1.5.1 treats bounded domains, so no unbounded-strip growth
theorem is needed for the finite-rectangle application. Its stated
nonconstant case must be complemented by the trivial constant case
when applying a non-strict bound. These hypotheses are audit checks,
not a verification here of the domains chosen in L468.

[DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9) explicitly states uniformity
for bounded real parts as the imaginary part tends to either infinity.
It covers the type of moving gamma arguments used here; it does not
control zeta or compact-height minima. Grava's December 29, 2024 notes,
Lemma 4.16, printed p. 42 (PDF p. 46), and its Cauchy proof are reused
from the construction assessment for L266's circle coefficient bound.
No fixed positive lower bound on the nonreal displacement is among
L266's general hypotheses. The specialized theta bounds later in L266
are outside this audit's needed interface.

Local overlap and failure coverage is reused from the construction
assessment: L461 has fixed parameters; the preserved L462 failure
concerns fixed anchors below their threshold. Neither is a duplicate
of the moving-parameter conclusion or a ban on this audit. No matching
cutoff is imported from Titchmarsh's RH-conditional Theorem 14.2.
The audit reproof is justified by changed uniformity quantifiers,
not by originality. The pinned external theorem remains an explicit
conditional input; its verification is outside this target.

After that gate, the proposed conceptual audit should check:

- The logarithm's disk neighborhoods, Euler normalization, Borel factor,
  exact three-circles exponent and uniform loss at all comparable heights.
- The preliminary full-rectangle growth, analytic power, damping signs,
  horizontal suppression and bounded cost when undoing damping locally.
- Both shifted heights on the complex y-circle, the anchor's uniform
  Stirling lower bound and the independence from compact-height minima.
- The full L266 quotient, geometric factor, ceiling monotonicity, one
  onset and quantifiers over small b and central multiplicity.

Continue if each step holds with one uniform set of constants. A gap
must be repaired within these hypotheses or recorded as a limitation
of this implementation, without assuming an endpoint or new source
premise. Preserve L462's fixed-anchor stop. The audit remains distinct
from an independent audit of the external half-plane manuscript.

Mathlib status is unchanged: full matching coverage is unchecked;
the Euler-logarithm and documented strip results are supporting APIs,
not a formal proof of this cutoff.
