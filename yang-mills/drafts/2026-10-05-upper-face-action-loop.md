# Upper-face axial action-loop test

Completed attempt YM-20261005-040-upper-face-action-loop, under the
unchanged SPECIALIZE assessment `drafts/literature/2026-09-26-current-target.md`.
The main gap is the full remaining response coefficient and its cutoff
dependence. This bounded attempt tests O(1) for the upper-face axial
one-internal-action-pair class. Its downstream use would be to exclude
another selected class as an unsuppressed logarithmic source. Continue
with an isolated bound if every active-edge contraction is controlled;
otherwise retain the exact failed estimate and reassess cancellations.

Inputs read: L025's ordered tensor, L026's pinned path lift and relative
spectrum, L027's interior two-edge comparison, and L028's quantitative
residual consistency and all-mode exterior expansion. L008, L009,
L018 and L023 supply the operators used by L028. ATTEMPTS/011–012
remain in force; they do not cover the upper-face three-edge vertex.
The supplied source comparison remains applicable; no fresh source
claim or general renormalization theorem is being rederived.

At axial level N-1 the ordered entries are (A,0,-B,-T), where A and B
are full axial path sums at neighboring transverse vertices and T is
the lower transverse link. The upper transverse link is fixed.
Unlike the interior case, both axial coordinates survive. Their smooth
stored lifts can be O(1), since the upper potential is pinned to zero.
The complete three-edge polynomial, covariance and signed contraction
must be retained. The completed calculation is canonical in
[L029](../lemmas/L029-upper-face-axial-action-loop.md).

Independent unresolved requirements: the other plaquette and pairing
classes, other jets and L019 cancellations, finite matching, reflected
error <= c_box/2 on a specified trajectory, continuum fields, full
reflection positivity, infrared control and finite positive mass.

Outcome: NEGATIVE / POTENTIALLY_NEW. The actual three-edge quartic has
a growing common-path quadratic Wick coefficient, unlike the interior
vertex. The pinned upper-face exterior has a real O(1) smooth common
path column. L029 supplies the exact full contraction and only an
O(a^(-2)) absolute-sum bound, short of O(1); this is not a lower bound
or a computation of signed growth. The result changes the immediate
test from extending interior difference estimates to evaluating the
actual signed upper-face class. No general literature theorem was
reproved, and no originality beyond the checked comparison is asserted.

Verification: the rational BCH and all six covariance-coefficient
identities have identically zero polynomial differences in
`scripts/combined-ward-response/upper-face-action-certificate.json`.
The complete `/checks` value was inspected. The analytic proof of the
covariance and rate estimates is in L029, not in a numerical preview.
No actual probe values or asymptotic fits were produced in this step.

Continuation under the unchanged assessment: evaluate L029's complete
signed upper-face contraction for both actual probes at N=24 and N=32,
resolving the HH and remaining channels and checking numerical and
heat-truncation errors. Inputs are L003, L008–L011, L018, L023, L025,
L026, L028 and L029; L019 remains the cancellation framework.
Inspect a^2 times the totals only as a discriminating diagnostic,
not as proof of a limit or power law. A significant HH contribution
would prioritize its signed asymptotics or a compensating jet; a
resolved cancellation would identify the specific term needing an
analytic identity. If errors or the two meshes cannot distinguish
these alternatives, record that limitation without assigning a log.
The failed interior-scaling extension is retained in ATTEMPTS/013.
