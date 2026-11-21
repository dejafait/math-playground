# Direct integrated spectral specialization: audit coverage1583

TARGET: Critically audit C032z's direct explicit-formula specialization, including its Fourier normalization, strip constant, all-zero factor and uniform tail bounds.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact integrated-test search and primary theorem comparison in source-notes1582/1572/1555, with unchanged sigma,w,strip and actual-divisor hypotheses; the audit introduces no transform family or new bound target.
SOURCE_EVIDENCE: Chirre-Goncalves Math.Z.300(2022) Proposition5 p.1044 https://link.springer.com/content/pdf/10.1007/s00209-021-02820-9.pdf ; DLMF1.2.8 equations7.7.3 https://dlmf.nist.gov/7.7.E3 ,7.5.1 https://dlmf.nist.gov/7.5.E1 ,1.14.1-3 https://dlmf.nist.gov/1.14 and5.7.6 https://dlmf.nist.gov/5.7.E6 ; Haslinger Theorem2.39 pp.67-68 https://www.mat.univie.ac.at/~has/scriptneu.pdf .
COMPARISON: C032z specializes the previously covered general identities and inversion/explicit-formula hypotheses; this next task audits that reproduction, not novelty, source proofs or an evaluator. No changed source hypothesis or essential unread source has been identified.
GAP: Independently check C032z's compact exchanges, integration-by-parts boundary terms/constants, ordinary Fourier inversion at zero, factor2 divisor pairing, pole/prime signs and effective tail errors; corrections must remain within the stated parameter set.
REASON: The delicate transform/infinite-sum normalization is load-bearing for any later direct evaluation; a separate conceptual audit is needed before relying on this newly written specialization.
SCOPE: C032z in full, real sigma in[1,2], complex |w|<=2 and |Im(a)|<=3/4, actual complex divisor with multiplicity and retained zero-ordinate/counting/source qualifications; no numerical implementation, coefficient search or extension of scope.

This coverage received its separate literature-only approval in step1584
on 18 November2026; the mathematical correctness audit remains pending.
Source-notes1582 contains inspected theorem hypotheses and proof-case
coverage; no source search was rerun merely to approve a continuation.
The primary Dawson representation is used at A=1, avoiding any general
complex square-root scaling. The positive-exponential normalized
Fourier inversion convention must be converted explicitly to
exp(-2*pi*i*a*y). The source explicit formula, not its neighboring
RH-dependent lemma or upstream real-valued-only version, is the input.

The bounded audit passes if all claims(2)-(9) follow with their exact
constants and uniformity. If a claim fails, preserve the countercheck,
repair only within the assessed scope when possible, and state the
remaining obligation. Numerical plausibility is not verification.
Classification is REPRODUCTION. Full matching Mathlib coverage remains
unchecked/unknown. C032m/y are analytic inputs; C032q/dictionary1570 and
stops1571/1576/1581 are downstream context/comparisons, not extra premises.

The analytic result supplies neither O nor the dictionary certificate;
full odd cancellation, arbitrary variation, H_d=o(d), S_F=0 and
unsmoothed actual-Xi realization remain independent gaps. Probability
uses retain finite-zero, heat and fixed-v1 qualifications. No complete
RH candidate or new creative central-gap mechanism is claimed.


## Separate literature approval1584

LITERATURE_REASON: The supervisor explicitly required a separate approval
of newly written assessment1583 before the saved mathematical audit;
this is that gate turn, not an additional search for an unchanged ready
target or another derivation.

Reused notes1582/1572/1555, including their recorded exact queries,
inspected theorem cases and unread leads. Read C032z to map its claims
to covered tools, C032y's hypotheses/definitions and C032m's Haslinger
source passage. Compared the exact stops1571/1576/1581: their enclosure,
common-disk cost and finite-coordinate obstructions do not establish or
refute this direct-test audit. No duplicate theorem search or assertion
of novelty was added. The assessment's target and parameter set remain
unchanged. No essential unread source was identified.

Reopened primary publisher Proposition5, its full displayed formula,
Fourier definition and reference to Lemma8, and DLMF7.7.3 with its
contour derivation note,7.5.1,1.14.1-3 with complete inversion hypotheses,
and5.7.6 with its excluded arguments. The publisher statement requires
evenness and wider-strip decay, and does not add RH or reality. It has
no independent proof at that location. Reuse notes1572's upstream
real-valued-test qualification; do not import the adjacent RH lemma.
Haslinger's statement/proof coverage remains reused from C032m,
not freshly reverified. Live pages were inspected on18 November2026;
notes1582 retain their recorded DLMF version1.2.8 identification.

Corrected one source-note transcription: DLMF7.7.3 has i/sqrt(A)
multiplying F(z/sqrt(A)), not i alone. Source-notes1582 now reproduces
that factor and preserves this correction record. The assessed use is
A=1; no generalized scaling or mathematical lemma was changed.

DECISION remains SPECIALIZE for the exact saved audit, classified
REPRODUCTION when carried out. This gate approval repeats existing
source readiness, so completed outcome is STALLED rather than a new
mathematical advance. No claims(2)-(9), constants, exchanges or divisor
factors have been certified here. All their exact obligations remain
for the separate conceptual audit. No lemmas or scripts were edited.

Continue only by auditing those claims with C032m/y's actual complex
divisor, multiplicity, counting and zero-ordinate conventions. Success
requires every claimed normalization and uniform bound; a failure must
be preserved and repaired within scope or recorded as a precise
obstruction before numerical use. O and residual<1/2 remain downstream
unpaid targets; arbitrary variation, full cancellation, H_d=o(d), S_F=0
and unsmoothed Xi realization remain independent gaps. Mathlib full
matching coverage remains unchecked/unknown. No creative central-gap
mechanism is licensed by source approval alone.
