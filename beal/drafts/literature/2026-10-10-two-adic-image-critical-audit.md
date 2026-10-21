# Two-adic image equality — critical-audit source coverage

TARGET: Critically audit L046's two-adic factorization, full-fiber nonemptiness and singleton connecting-image equality.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact two-adic/fourth-power/X0(11)/54a1 searches in drafts/literature/2026-10-10-two-adic-fourth-power-image.md; read that full assessment, foundations 15 and 17, L046, the L033/L034 audit assessments, relevant L033 interfaces, ATTEMPTS/014 and histories 114–115. No fresh external search or novelty claim.
SOURCE_EVIDENCE: Reused inspected Schaefer–Stoll June 13, 2001 manuscript Lemmas 4.2–4.5 pp.6–7, Clark's accessible 161-page notes Theorem 1.75/Corollary 1.77 p.57 and Theorem 2.8/Proposition 2.9/Corollary 2.10 pp.64–65, FNS June 10, 2019 Section 7.2 pp.25–28 and Lemma 7.12's 54a1 case pp.32–33, and the prior finite-flat/reconstruction coverage specified below; no new primary retrieval is claimed.
COMPARISON: The existing prime-to-residue-characteristic isogeny, simple-root lifting and Eisenstein/integer-ring theorems cover all general tools used in L046. They do not certify its explicit coefficient bounds, field identification, reconstruction or common-witness fiber; these require the independent mathematical audit.
GAP: Source coverage is ready, but L046's actual specialization and exact certificate have not been independently verified. Global eleven quotient classes, five twist emptiness claims and infinitely many signatures remain unresolved.
REASON: Approve one bounded critical audit of the completed specialization using adequate existing coverage; import general theorems rather than reprove them, and do not reopen the exhausted additional two-adic filter merely because its audit passes.
SCOPE: Exactly L046 under L032–L034's models, maps and dual-kernel identification, with the entire twelve-dimensional local algebra, every factor and exceptional evaluation, one complete regular fiber and common primitive scalar witnesses; no global arithmetic, other twist or broader local classification.
LITERATURE_REASON: This newly written exact audit target required separate source-scope approval; the prior ready mathematical assessment is reused, with no repeated browsing to meet a quota.

## Primary inputs and applicability obligations

Schaefer–Stoll, *How to do a p-descent on an elliptic curve*,
Trans. AMS **356** (2004), 1209–1231,
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X),
[long author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
June 13, 2001, Lemmas 4.2–4.5, printed pp.6–7.
For theta:E -> E' with kernel of exponent p, at a finite place not
above p, Lemma 4.5 identifies the connecting image with unramified
cohomology when neither curve's Tamagawa number is divisible by p;
Lemma 4.2 gives its size as the number of rational kernel points.
The prior assessment inspected the Frobenius/inertia-invariant and
formal-group arguments. Lemma 4.4's supporting reference [24], Lemma
3.8, was not separately read; the stated source theorem is imported.
The audit must use theta:E1 -> E0 with kernel mu_5, not the constant
forward kernel, and check good reduction and actual residue fields
on both complete factors. L033's audited pairing, normalized map and
good-divisor evaluations are reused, including T and O. No general
descent reproof or global point/Selmer equality is authorized.

Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields
and Adeles*, [author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
accessible 161-page version, revision date unidentified: Theorem 1.75
and Corollary 1.77, printed p.57, cover simple residue-root lifting
and uniqueness over a complete valued field; Theorem 2.8, p.64,
covers Eisenstein irreducibility over a DVR, and Proposition 2.9 and
Corollary 2.10, p.65, identify the integral closure, uniformizer,
residue field and total ramification. Their inspected hypotheses
cover both Q2 and finite complete extensions. The audit must check
integrality and unit derivatives separately for each normalized
equation, including the unit eleventh-root equation identifying the
field. A fourth-root derivative at two is not covered. No assumption
that arbitrary degree-eleven Eisenstein fields are identical is approved.

Freitas–Naskręcki–Stoll, *The generalized Fermat equation with
exponents 2,3,n*, Compositio Math. **156** (2020), 77–113,
[final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
June 10, 2019, Section 7.2, printed pp.25–27, Table 5 and (7.4),
supplies the modular transport/model interface used by L033–L034.
The prior two-adic assessment read pp.25–28 and the full 54a1 cusp
case of Lemma 7.12 on pp.32–33. FNS's Lemma 7.6 excludes this cusp
domain and concerns square classes; its later global two-Selmer
elimination is not imported here. Those results cannot replace the
proposed fifth-isogeny/fourth-power audit.

The L034 audit assessment records inspected [Stacks 0CCL, Lemma
53.2.4](https://stacks.math.columbia.edu/tag/0CCL) (finiteness of the
nonconstant proper curve map), [0CCK, Lemma 53.2.3](https://stacks.math.columbia.edu/tag/0CCK)
(flatness with normal target) and [02K9, Lemma 29.49.2](https://stacks.math.columbia.edu/tag/02K9)
(finite local freeness over the locally Noetherian target).
Their setting covers this smooth projective curve map to P1 over Q,
provided the map and degree are correct. L034's audited elimination
and reconstruction identities are mathematical inputs, not a generic
license to identify every eliminated polynomial with a fiber.

## Exact audit target and discriminating test

Essential local inputs are L032's 54a1 branch, L033's K, curves,
dual kernel and good-divisor map, L034's complete modular map, L046,
and scripts/two-adic-image/image-certificate.json. No cross-notebook
input is used. The audit should inspect complete load-bearing values
with the shared JSON inspector, not infer correctness from flags or
previews. Independently verify the polynomial rescaling, all thirteen
shifted-fiber coefficients and valuations, both Hensel normalizations,
and the reconstruction identity; a rerun of the construction alone is
not independent verification. No mathematical script runs in this review.

Check that the linear and Eisenstein factors exhaust degree twelve,
that the maximal integer rings really have residue field F2, and that
the unit-root identification proves the stated field isomorphism.
Check the direction and hypotheses of the singleton-image theorem.
For the displayed scalar, check the two root equations, distinctness,
degree eleven from the fractional valuation, every conjugate, all
reconstruction denominators and the finite-flat length argument.
Retain every exceptional evaluation in the unrestricted theorem.
Check both primitive identities with the same c and the required
mod-eight condition; restricted nonemptiness cannot be inferred from
a trivial unrestricted image alone. This specifies verification of
existing claims, without deriving or approving their truth this turn.

The main gap remains positive primitive global emptiness. The
intermediate target is this exact audit. Confirmation would justify
retiring the additional two-adic connecting-class filter and avoid
redundant local searches; a concrete defect would require repair or
parking the affected assertion. Continue only if every load-bearing
interface is covered and independently checkable; an essential new
source gap returns to literature review. Success closes no global
gap and does not reopen ATTEMPTS/008–014. The historical stop is
specific to this filter, not a ban on all two-adic mechanisms.

This is a STALLED source-scope/process completion: no new mathematical
result, independent audit or advance beyond checked literature is
claimed. Mathematical exploration usage remains 0/3. Mathlib matching
and supporting coverage are not checked; unknown is not absence.
