# Equality determinant pullbacks — critical-audit coverage

TARGET: Critically audit L107's determinant pullbacks, integral interpretation and same-stratum ample-cone compatibility.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact determinant discovery/comparison in 2026-10-15-equality-determinant-line-positivity.md and calculation assessment; searched L107, L097, the placement audit assessment and ATTEMPTS/065 for changed hypotheses, duplicates and stop conditions. No broader discovery search is needed for this unchanged audit scope.
SOURCE_EVIDENCE: Reusable primary inputs are Huybrechts–Lehn (1997), Theorem 8.1.5, Definition 8.1.9, Proposition 8.1.10, Theorem 8.1.11, Remark 8.1.12(i), Section 8.3 and Proposition 8.3.1(ii), pp. 180–185/195–197, https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf ; Abe (2017), Section 10.1, pp. 151–152, https://doi.org/10.1017/nmj.2016.50 ; Stacks 30.17.2, https://stacks.math.columbia.edu/tag/0B5V . For the rational relative stratum, reuse Greb–Toma, Algebraic Geometry 4 (2017), Theorem 6.6/proof p. 74 and Section 6.3.3 p. 75, https://content.algebraicgeometry.nl/2017-1/2017-1-003.pdf ; these passages and Stacks 0B5V were retrieved again in this approval turn. Prior complete determinant extractions are reused, not claimed newly reread.
COMPARISON: The inspected whole-semistable descent, fixed-determinant surface positivity, alternating family GRR, finite pullback and uniform relative-stratum inputs cover the audit without changed hypotheses; the exact integral calculation and neighborhood specialization still require mathematical verification.
GAP: No essential source gap remains for the stated audit. Independently check L107 equations (2)–(6), integral Picard interpretation and the permitted polarization choice; no source directly certifies that full conditional specialization.
REASON: This separate literature-only comparison approves the unchanged audit scope by reusing adequate evidence. L107 remains unaudited; known frameworks should be imported, with only the family-specific applicability and calculation checked next turn.
LITERATURE_REASON: Separate approval of the newly proposed critical audit of L107; reuse existing source evidence, with additional extraction only for an identified essential gap.

The proposed audit must check the determinant-of-alternating-pushforward
sign, the point term in both u_i, the absence of a degree-six character,
the relative Todd cancellation, and the full integral correspondence
orientation. Check the whole-space/fixed-determinant application at
possibly nonempty Z, integral Picard triviality, and finite pullback
onto the reduced image. Then check that shrinking L097's actual
rational wall-stratum neighborhood preserves every required property
while enforcing ampleness of D(alpha), before denominator clearing.

Essential local inputs are L071, L097 and audited L098; L099 is not
needed. F existence remains an assumption. The finite split set may
be empty. No universal sheaf, generic H, constant cohomology ranks,
image normality or whole-space L_1 ampleness is available. A successful
audit would preserve a compatibility stop, not reopen the filter or
construct a common kernel, transport or primitive Hodge realization.
Full matching Mathlib coverage remains not checked.

## Separate scope comparison (2026-10-15)

The determinant discovery and statement/proof-case extraction in
[the earlier assessment](2026-10-15-equality-determinant-line-positivity.md)
are adequate for this exact target. The audit adds no genericity,
primitivity, universality or constant-cohomology hypothesis. In
particular, check membership of both u_i in the whole-space descent
domain K_{c,H}, rather than invoking stable-open descent alone. The
fixed-determinant restriction and the sufficiently-large positive
exponent remain essential. Abe supplies a legible sign convention,
not a quadric-specific positivity theorem on this K3.

The relative-stratum source evidence is reused from
[the placement audit assessment](2026-10-12-equality-global-placement-critical-audit.md).
Greb–Toma's Theorem 6.6 fixes topological invariants and a compact
subset of P(X), and provides finitely many rational linear walls
with uniform slope-(semi)stability in each chamber. Its proof uses
the finite hyperplanes obtained in Lemma 6.4. Section 6.3.3 explicitly
includes chambers of smaller dimension. On this surface P(X) is the
real ample cone. The extra rational equality k.alpha=0 and shrinking
inside D-inverse of the ample cone are local applicability checks;
Proposition 6.7 is not imported as a theorem guaranteeing those extra
conditions. The audit must check their preservation before scaling.

Stacks 30.17.2 is the finite-surjective ampleness criterion for schemes
proper over a Noetherian ring. Its application is to the reduced
projective image, not surjectivity onto the entire moduli space.
L098 is an audited local input; neither L099 nor image normality
is required. Standard K3 torsion-freeness, the exponential sequence,
Lefschetz (1,1), rank-two Chern identities and linear continuity are
the elementary supporting inputs to inspect, without reproving the
published determinant theorems.

ATTEMPTS/065 records the completed compatibility stop; ATTEMPTS/064
concerns the different gerbe filter. No duplicate exclusion or new
mathematical consequence is claimed in this source comparison. The
continuation test is to preserve that stop if the integral pullbacks
and permitted-neighborhood argument withstand independent checking,
or identify an exact load-bearing error. It is not to iterate the
same compatible filter. No primary-source blocker or unread essential
lead remains in this scope. Full matching Mathlib coverage is not
checked. No lemma, DAG, proof overview or mathematical script is
changed in this literature-only turn.
