# Source review of actual-response disjointness

TARGET: Assess known results and obstructions for eventual absence of common real zeros of the actual F_0 and regulator response G in L366.
CHECKED: 2026-10-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact/common-zero, shifted-xi and Gram/phase searches on 2026-10-07 plus scoped duplicate/failure checks found adjacent projection theorems, but no matching eventual F_0/G exclusion in the inspected primary statements; queries and unread leads below.
SOURCE_EVIDENCE: Lagarias arXiv:math/0601653v2, Lemmas 2.1–2.2 and relevant complete proofs pp. 4–8, Theorem 2.1(1) and common-zero proof pp. 7–8, https://arxiv.org/pdf/math/0601653v2; Xiannan Li arXiv:0904.1051v1, Theorems 1–2 p. 3, phase-level opening p. 4, equation (2) and Remark pp. 6–7, https://arxiv.org/pdf/0904.1051v1; L018, L024, L366 (1), L368 (1)–(2), L372 (2)–(4) and its saved audit history inspected for local scope.
COMPARISON: Lagarias excludes common zeros of two projections of the same shifted function, not of unshifted xi and the response with its variable divisor; Li also compares shifted real/imaginary projections. Neither establishes actual-family noncoincidence.
GAP: Eventual absence of t with F_0(t)=G(t)=0 remains unproved; no inspected result controls the shifted real projection at every unshifted critical-line zero, and no actual counterexample is certified.
REASON: Exact primary hypotheses now rule out a direct import from the available projection theorems; a bounded geometric test retaining the shift/divisor is proposed separately before any actual-family proof claim.
SCOPE: Fixed zero-regulator functions of the real frequency t defined by L366 (1); no positive regulator, assumed simplicity of critical-line zeros, RH, D≤0 or common ODE may be used to assert eventual disjointness.

This separate literature-only review is now complete. The main RH gap remains global
actual-theta mixed positivity and the total L367 signed margin. Establishing
eventual disjointness would discharge one hypothesis of L374; actual D≤0
and the signed arithmetic count comparison would still be independent gaps.

L366's exact real-frequency definitions are

\[
 F_0(t)=2\xi_c(1/2+it),\qquad
 G(t)=-(t^2+1/4)\operatorname{Re}
       \frac{\xi_c(5/2+it)}{5/2+it},
\]

where \(\xi_c(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)/2\)
is the entire completion. These are quotations of the local identities,
not a new derivation. The concrete source question is whether a primary
theorem excludes the simultaneous vanishing of these two specified real
functions on an eventual ray, or supplies an independently testable
intermediate noncoincidence assertion. Nonvanishing of the complex
completed zeta expression on Re s=5/2 cannot simply be substituted for
nonvanishing of its real projection.

Essential local inputs are L366's exact identity
and definitions; L018 only as needed for its standard completion
conventions. L368's strict response Laguerre bound and audited L374
provide downstream context, not premises proving disjointness. Review
the relevant primary statements and hypotheses before proposing any
new phase argument. The saved generic-pair comparison assessments may
be reused within their scope; they do not approve this actual-family target.
No cross-notebook mathematical input is proposed. Full matching Mathlib
coverage is not checked.

Continuation/abandonment test: import a precisely matching primary result
if one is found, or approve only a bounded independently testable target
whose exact residual gap is documented. If the inspected results require
RH, a common ODE, an unproved zero noncoincidence, or supply only density
information, record the mismatch and do not treat it as eventual
disjointness. A persistent essential source blocker requires parking its
dependent proposal and choosing an independent target. No theorem,
counterexample or actual-family mathematical attempt is claimed here.

## Primary hypotheses and essential proof cases

J. C. Lagarias, *Zero spacing distributions for differenced L-functions*,
Acta Arith. 120(2) (2005), 159–184, DOI 10.4064/aa120-2-4,
[arXiv v2](https://arxiv.org/pdf/math/0601653v2), 30 January 2006:
Lemma 2.1(1) proves |ξ(s+h)|>|ξ(h+1−conj(s))| for h≥1/2,
Re s>1/2, by comparing Hadamard factors using 0<Re ρ<1.
Part (2), covering all h>0, assumes RH and is unused. Lemma 2.2
requires an entire E satisfying the strict reflected half-plane modulus
inequality; its conclusion concerns the two components of that E.
Theorem 2.1(1) gives simple interlacing zeros for constant-angle
shifted-xi projections when |h|≥1/2. The final proof paragraph excludes
a common zero because both components would vanish at the same shifted
argument outside the zero strip. Read these complete relevant proof cases.

G's right line corresponds to h=2, satisfying the shift-size hypothesis
for the source's functions. F_0 is unshifted, rather than the other
component of ξ(s+2). Also 1/(s+2) is a variable factor inside G's
projection, not a constant-angle rotation, and the entire-E hypothesis
is not automatic for the divided expression. Thus the theorem does not
apply to the pair. This is a comparison, not an import or a reason to
reprove the named theorem. The modulus argument suggests testing a
geometric inference, but does not sign the needed real projection.

Xiannan Li, *The argument of the Riemann ξ function off the critical
line*, [arXiv v1](https://arxiv.org/pdf/0904.1051v1), 7 April 2009:
Theorem 2, p. 3, concerns real/imaginary projections on the same line
Re s=1/2+λ, λ>0. For each B>0 an exceptional set in [T,2T]
has measure O(T/log^B T) and contains O(T/log^B T) projection
zeros; outside it zeros are simple, interlace and are regularly spaced.
Read the phase-level opening p. 4, phase-derivative conclusion (2)
p. 6 and Remark pp. 6–7. In the λ>1/2 case, bounded ζ′/ζ
removes the exceptional-set issue for those shifted projections.
Theorem 1 likewise concerns shifted sums/differences. Neither the
general density statement nor the right-line case compares with F_0.
No RH-equivalence claim about our disjointness target follows.

L372 already supplies the response-specific phase levels, including the
full divisor/carrier correction and eventual simple crossings; its audit
is recorded in `history/2026-10-06-response-zero-count-critical-audit.md`.
The overview's older pending-audit phrase is not a new mathematical gap.
L368 allows G=0, while L374 assumes disjointness. None is a bound for
G's value at F_0 zeros. Existing arguments are unchanged.

## Discovery, duplicates and unread leads

Queries included `Riemann zeta zeros "real part" "5/2" common zeros`,
`"xi" "shifted" "common zeros" Lagarias`, `Lagarias "Zero spacing
distributions" common zeros`, `zeta shifted real imaginary parts
common zeros Ki Li argument xi`, `"zeta" "common zeros" "shifted"
real imaginary`, `"xi" "noncoincidence" zeros`, and Gram-point
nonvanishing/zero-conjecture searches. The finite-model lead was
screened with `Hermite Biehler theorem real rooted polynomial P(x+ih)
real imaginary zeros original polynomial` and exact common-zero/shift
queries. Search snippets locate sources; they are not theorem evidence.
The bounded search establishes neither novelty nor a literature-wide
claim that eventual disjointness is unknown.

Reuse the ready response-count and generic-pair assessments. Scoped
searches and reads of the two weak-count ATTEMPTS retain L371/L373's
stops. Those arbitrary-pair examples do not preserve the exact shift
relation. L018 fixes completion/reflection and L024 the unconditional
paired product. No recorded exact-shift polynomial obstruction was
found in the scoped material checked; no all-notebook search was made.

Unread leads: Gonek–Ki, *Pair correlation of zeros of the real and
imaginary parts of the Riemann zeta-function*, was located at
https://www.sciencedirect.com/science/article/am/pii/S0022314X1730416X
but article retrieval failed. https://aimath.org/~kaur/publications/u1.pdf
returned a scanned Gram-curve PDF without extracted text; a narrow
shell retrieval failed DNS. Neither supplies inspected theorem evidence
or an essential premise here. No persistent essential source blocker
is claimed. Additional HB bibliography hits remain unread leads.

## Decision and continuation

Outcome: EXPLORATION, with no imported input, new mathematics or actual
noncoincidence result. Park direct use of shifted-pair noncoincidence
for F_0/G; this is not a global ban on an arithmetic approach.
The next proposed assessment is
`drafts/literature/2026-10-07-exact-shift-polynomial-noncoincidence.md`.
It tests a pointwise geometric inference while preserving the divisor,
instead of repeating the arbitrary-pair count counterexamples. Its
new ready continuation receives separate supervisor approval next turn.
No polynomial example has been derived or certified in this turn.
Even a successful finite-model obstruction would not refute eventual
disjointness for the actual pair or for each fixed finite polynomial.
Actual D≤0, signed count comparison, total margin and the global
mixed positivity gap remain open. Full matching Mathlib coverage is
not checked; no cross-notebook input was read.
