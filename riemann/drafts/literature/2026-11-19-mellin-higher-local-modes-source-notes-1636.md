# Higher local theta modes: source comparison1636

Inspected19November2026: K. Kawano, *Logarithmic Inequalities of Arbitrary
Order for the Riemann Xi Coefficients*, Preprints.org202611.0383v1,
posted4November2026, DOI10.20944/preprints202611.0383.v1,
https://www.preprints.org/manuscript/202611.0383/v1 . The redirect identifies
Version1, not peer reviewed. These notes record claims and scope;
they prove no new bound.

## Primary evidence

Read Section5.2(28)/Lemma5.1(i), AppendixA.2(A3), AppendixB's local
definitions, absorption, normalization, B_modes and series proof sentence,
and AppendixC through its remaining-local-mode allocation. B's domain is
7.5<=L<=12.3, width7/(10L); C uses L>=12, Re p>=-r/(4L), width1/(3L).
A3 includes a frequency-cell perturbation factor, excluded here.

AppendixB, unnumbered display immediately after the B_g discussion:

    B_modes=32 M (1+3W_*exp(2d)/(4r))
                    exp(-3v exp(-2d)) sqrt(mathcal A/b_*).

Its symbols bound |K| by M, |w| by W_*, |A_0| by mathcal A,
v_0=pi exp(U)cos V below by v, and absorbed curvature below by b_*.
Prerequisites include b_*>0 and u/2-d>1. The next display states

    sum_(n>=2) n^4 exp(-(n^2-1)t) <=32exp(-3t), t>=1.

The proof sentence cites consecutive-term ratios. The companion
all-mode estimate has hypothesis t>0; it does not replace t>=1 above.
AppendixC assigns112sqrt(L)exp(-5r/L^2) to remaining local modes.
No separate detailed higher-mode proof or supplement is cited there.

## Scope comparison and reusable mathematics

T_modes is the notebook's operational definition, retained verbatim in
assessment1635. Reading B_modes as an absolute local allowance is an
inference from its Gaussian normalization and separately allocated
horizontal tails, not an author-stated identity for T_modes.
The later reproduction must prove this application. AppendixB's cells
and width cannot be imported into C's sector.

Read C048c hypotheses and proof(3)-(19). Those passages establish the
matching phase, amplitude, geometry, exact S normalization,
segment containment, |K| and absorbed curvature. The n>=2 sum is
expressly excluded from its conclusion. Reuse that work without a
new leading-mode audit. C048e concerns only the negative first mode.

Read L799 hypotheses, conclusion, strip-convergence argument, identity(4),
and amplitude proof through Gaussian normalization. Its holomorphy and
normal convergence on |Im z|<pi/4 are stated independently of its saddle
parameter; identity(4) separates the same higher-mode factor. These
are reusable supporting results, subject to identifying the original
kernel normalization. Its final amplitude estimate additionally assumes
its own saddle, rotated diameter, different width and curvature. Those
hypotheses differ from T_modes, so that numerical allowance does not
transfer. Its ratio argument is a method precedent, not a completed
specialization. No cross-notebook input is involved.

Reuse inspected DLMF7.7.6 coverage from source-notes1630/1633 and C048c:
real integration endpoint, Re a>0, principal square root. For a future
absolute Gaussian integral the coefficient must be positive real;
C048c(19) supplies that curvature. Keep sqrt(|A_0|/pi) in the
normalization. No new Gaussian theorem or tail search is needed.

The remaining verification tasks are specified in assessment1635:
legitimate full-series use, real theta parameter t>=1 throughout the
segment, absolute finite-integral domination, and coefficient/exponent
comparisons on the full closed sector including unbounded L. They were
not calculated here. SPECIALIZE supports later reproduction of
the printed component; it does not certify the preprint's estimate.
Full matching Mathlib coverage is unchecked, not absent.

## Duplicates, failures and discovery record

Scoped searches for higher-mode/B_modes/T_modes/local-mode terms in
Mellin literature, history and attempt paths found the nomination and
previous exclusions, not a matching canonical proof. Reused the
L798-L800/fixed-phase comparison in source-notes1627 and read
ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md.
Whole-path domination, uniformity and endpoints remain unpaid there.
This local target neither resolves nor contradicts that stop.

Queries: `"202611.0383" "modes"`;
`"Kawano" "theta" "112" Mellin`;
`"202611.0383" "B_modes"`;
`"Logarithmic Inequalities of Arbitrary Order" "theta" "modes"`;
`"sum" "n^4" "32" "e" theta saddle Mellin`.
The relevant primary match was the manuscript. Other hits supplied
no inspected stronger theorem and were not used. No novelty
claim follows from this bounded search. Existing assessments
suffice for the unchanged general saddle/Gaussian method.

The scope test passes with the operational-definition qualification.
A failed sufficient majorant alone would not refute T_modes or RH.
Horizontal tails, full assembly, zero counts, inversion and sufficient
mixed signs remain independent. There is still no specific tested
central Mellin-to-sign mechanism to justify creative routing from this
component. Separate approval of the changed ready assessment precedes
the next mathematical attempt; none was performed now.
