# Corrected Pólya reference — completed shift-residual source comparison

TARGET: Assess source coverage for a finite imaginary-shift annihilator of L814's corrected Pólya G and a noncircular residual comparison for F, separating equal-scale Bessel identities from actual-theta forcing.
CHECKED: 2026-11-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Step589 checked fixed-argument Bessel order recurrences, imaginary-shift comparison/preserver terminology and inhomogeneous zero comparison; reused the corrected-reference and equal-scale failure assessments and October7 fixed-function preserver assessment. No adequate actual-theta forcing comparison was located in this bounded search; no absence or novelty theorem is claimed.
SOURCE_EVIDENCE: NIST DLMF1.2.8 (2026-09-15), 10.25(ii) modified-cylinder notation, 10.29.1 and 10.32.9; Katkova--Tyaglov--Vishnyakova arXiv:1608.03924v2 (3 September2016), Theorem2.2 and proof pp4--5, with prior inspected proof cases reused; Gasper0801.2996v1 (19 January2008), (3.1) and prior (3.5)--(3.6) scope. Direct sources and applicability below.
COMPARISON: The recurrence is an exact known identity for one fixed Bessel argument. The preserver theorem assumes a Laguerre--Polya input and concerns its shifted output; it is neither an inverse theorem nor an inhomogeneous comparison. Actual F lacks that paid input. Neither result controls L814's residual or collision curvature sign.
GAP: A scalar annihilator for the corrected combination, an independently signed actual-theta forcing estimate and a comparison-to-collision implication remain unproved. No transferable residual discriminator was found, so the nominated continuation test fails at source scope, without proving mathematical impossibility.
REASON: Park the reference-annihilator sign-transfer mechanism under its nominated test. A known-method recurrence calculation alone would not justify continuation. Preserve the algebraic lead and finite evidence; nominate a different actual-theta unequal-argument product source question separately.
SCOPE: Completed literature-only comparison for L814's normalized pair. EXPLORE records bounded source discovery, not approval of a dependent operator construction or collision sign. No lemma or mathematical script was written. Full matching Mathlib coverage unchecked.
LITERATURE_REASON: The changed target needed unread primary recurrence/notation and a forcing-comparison applicability check; older ready preserver coverage was reused rather than researched as a new result.

The main gap is actual-Xi all-degree mixed positivity. L814's local
deformation route lacks an independent sign for W'=F G''-G F'' at
F G<0,W=0. Its existential relative-error bound restates that sign.
L816's audited finite exclusions supply no relative signed estimate.

The proposed intermediate input is an exact finite difference relation
in imaginary shifts of x for the corrected Pólya reference G, together
with a usable, independently testable comparison condition on the same
operator applied to F. The motivation is the fixed-argument modified
Bessel order recurrences behind the reference transform. The precise
shift sizes, coefficients, regularity and boundary terms must come from
primary statements and their justified specialization. No three-term
closure, reality property, annihilator or sign-preserving implication
is asserted here. An operator identity alone would be insufficient.

Its plausible downstream use would be to replace an uncontrolled
absolute remainder by a structured forcing term in a zero/sign
comparison. That implication is a separate unresolved obligation;
it must not be silently inferred from the reference's recurrence.
The source step must decide whether a primary comparison theorem or
a genuinely new, bounded residual discriminator makes this plausible
for the actual pair. It may approve a later creative proof attempt only
after recording that precise discriminator and its essential coverage.

Continuation/abandonment test: retrieve primary recurrence hypotheses
and the load-bearing cases of a proposed comparison theorem; identify
one exact residual property that can be tested without assuming the
desired collision sign. Continue only if this property differs from
L814's existential payment and the old equal-scale identity. If the
sources merely restate the desired sign, need the missing global
real-zero premise, or provide no transfer beyond fixed-scale families,
park this mechanism with that specific obstruction. Do not respond by
reopening the inaccessible1927 proof or extending the numerical census.

Duplicate/failure context to reuse narrowly:
`2026-11-05-polya-corrected-reference-collision-scope.md` records the
restricted symmetric-shift Hilfssatz and the blocked corrected-reference
extension; `2026-11-01-signed-theta-cancellation-discovery.md`, mechanism3,
records that paired Bessel squares do not supply unequal-scale theta
cross terms. These are constraints, not imported positivity results.
The changed proposal concerns a reference annihilator and its actual
inhomogeneous residual; simply applying the old square identities again
does not qualify. No novelty claim follows from the narrow local search.

Essential continuation inputs: L814; L815/L816 only as qualified finite
numerical context, not as premises for a global shift comparison.
Any deeper dependency must be read in the active notebook as needed.
Unresolved assumptions: applicability of an exact difference operator,
complex-shift convergence and boundary accounting, an independently
controlled residual, the comparison-to-collision implication, common
and degenerate events, infinity, and all-degree sufficiency. The old
backend qualifications remain on the numerical context only. No
cross-notebook theorem is used. Step588 nominated this assessment;
step589 completes the comparison below without deriving new mathematics.

## Primary statements and applicability (step589)

[NIST DLMF, 10.32.9](https://dlmf.nist.gov/10.32.E9) states

    K_nu(a)=integral_0^infinity exp(-a cosh t) cosh(nu t) dt,
    |arg a|<pi/2.

The order nu is complex. The argument a=2pi is allowed, covering the
Bessel ingredients after the previously specified t=2u substitution.
This is applicability of a cited representation, not a new G formula.

[DLMF 10.29.1](https://dlmf.nist.gov/10.29.E1) uses a modified-cylinder
symbol whose K branch is exp(nu*pi*i)K_nu, as defined in
[10.25(ii)](https://dlmf.nist.gov/10.25#ii). Thus its K recurrence reads

    K_(nu+1)(a)-K_(nu-1)(a)=(2nu/a)K_nu(a).

Each adjacent exponential factor changes sign, explaining this necessary
notation conversion. Integer order shifts become imaginary-frequency
shifts under t=2u. This does not assert a scalar annihilator for the
corrected two-cosh combination; that elimination was not performed.
Argument derivatives elsewhere in 10.29 are not frequency derivatives.
The source is DLMF1.2.8, release 15 September2026; all the needed HTML
equations, restrictions and symbol definitions were inspected.

O. Katkova, M. Tyaglov and A. Vishnyakova,
*Linear finite difference operators preserving Laguerre--Pólya class*,
[arXiv:1608.03924v2](https://arxiv.org/pdf/1608.03924v2),
Theorem2.2, printed pp4--5, concerns meromorphic M. For **every
f in the Laguerre--Pólya class**, f(z+i)+M(z)f(z-i) has only real zeros
or is identically zero iff M has modulus strictly below one in the
upper half-plane and strictly above one in the lower, or is constant
of modulus one. Its sufficiency proof compares canonical-product
moduli, separating inputs with a zero from zero-free Gaussian/exponential
inputs. Identically zero outputs are allowed. Complete proof cases
were already inspected in
`2026-10-07-fixed-function-exact-shift-common-zeros.md`; that coverage
is reused, with the changed actual-F applicability checked here.

This is a forward preserver with a real-zero input premise. It does
not recover input reality from output reality, compare forced and
homogeneous recurrences, or bound W' for two different transforms.
Applying it to F would require an unpaid premise. Applying it to a
known model concerns that model's output only. No specialization or
reproof is needed to identify this mismatch.

Gasper's [v1 paper](https://arxiv.org/pdf/0801.2996v1), (3.1), proves
reality for a symmetric shifted Bessel sum by strict off-axis comparison
within a common-argument family. The earlier assessment covers its
corrected-reference identification (3.5)--(3.6). These supply no actual-F
inhomogeneous comparison. The November1 equal-scale square stop remains;
no unequal-scale cross-term payment is inferred.

## Search record and route decision

Queries included `"imaginary shifts" "comparison" "zeros" Bessel
difference`, `"Riemann" "inhomogeneous" "difference equation" Bessel
Polya`, `"imaginary shifts" "Sturm" comparison`, `"difference operator"
"imaginary" "real zeros" entire comparison`, `"Bessel" "Pólya"
"difference equation"`, and `"imaginary shifts" "Sturm comparison"
residual`. Follow-ups used the exact preserver title and
Bessel/inhomogeneous/real-zero terms. Search snippets are not theorem inputs.

The Pólya1926 PDF initially opened; targeted follow-up requests timed
out. Its already inspected HilfssatzII scope is reused. No new proof
case is claimed from those failed requests. DLMF's TeX endpoints were
unsupported, but its relevant HTML was successfully read; recurrence
coverage is not blocked. The inaccessible1927 extension was not reopened.

A residual/Green-function follow-up surfaced discrete quantum mechanics,
Volterra/phase-kernel leads and a forced-xi-inverse discussion. The last
discussion's introductory definitions were read for scope only: it
concerns a Mellin-moment inverse, not a comparison for this F,G. No
theorem or certificate from those incidental leads is imported; the
other leads remain unread.

Local detailed reads concerned L814's definitions, convergence and
relative-bound obstruction; the corrected-reference, equal-scale,
October7 exact-shift and approved local-collision assessments; and the
affine-sign failure record. No numerical replay was relevant. No
sibling notebook, scheduler state, shared file or mathematical script
was read or edited as a mathematical input.

Outcome: a source-scope NEGATIVE, not a no-go theorem for difference
methods. The comparison identifies the preserver's missing input and
the recurrence's limited role. No operator/residual transfer meets the
nominated continuation test, so dependent work is parked. Reopening
needs a forced comparison with verified hypotheses or a materially new
independently testable signed estimate, not formal closure alone.

The separate nomination `2026-11-05-actual-theta-unequal-product-scope.md`
asks about actual modularly paired cross terms instead of a reference
recurrence. It remains REVIEW_REQUIRED. No change to PROOF or DAG is
warranted by this source comparison. Full matching Mathlib coverage
was not checked; no new mathematical result needs a lemma file.
