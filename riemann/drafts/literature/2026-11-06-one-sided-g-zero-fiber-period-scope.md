# Actual G-zero fiber: proposed period source comparison

TARGET: Review whether vanishing of q,r on one actual nonzero G-zero fiber can control C868a's exceptional modes and yield K>=-|M| for L868's full C1 class.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded searches for the exact coefficient system, zero-fiber Fourier restrictions, and relative de Rham/closed-form period theorems; compared the named local one-sided and diagonal attempts and canonical L847/L868/C868a. Queries and actual readings below. No matching sharp-period theorem located; no novelty claim.
SOURCE_EVIDENCE: Reuse Rudin Theorem9.42 and Grafakos product Fejer/periodic differentiation coverage in 2026-11-06-diagonal-fourier-correction-audit.md; inspected Michor, Topics in Differential Geometry (April2008 manuscript), 11.15/11.16 pp140-141 and 31.16 pp424-425 with proofs https://www.mat.univie.ac.at/~michor/dgbook.pdf ; Titchmarsh, The Theory of the Riemann Zeta-function, 2nd ed. revised Heath-Brown (1986), Section10.2 pp256-258, Hardy theorem and first proof https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf . Exact scope and access qualifications below.
COMPARISON: Hardy supplies a usable actual nonzero G-zero by L018/L847's existing coordinate correspondence. Reused compact Fourier operations apply to C1 angular traces. Relative de Rham statements address smooth tangential restriction and local exactness, not coefficient domination, positivity, exceptional-mode bounds or the sharp K threshold. No inspected theorem settles the full class; the remaining test is not a reproof of those results.
GAP: Prove or refute K>=-|M| in the unchanged global C1 class by exploiting the single actual fiber; retain the zero and opposite-index modes and all original zeros. Fiber compatibility, the quantitative threshold and any global feasible construction remain unproved.
REASON: Essential source comparison is complete for one bounded compact-Fourier/closure test, not for an arbitrary new PDE, smoothing or global topology argument. The changed ready continuation requires separate approval before mathematics; the diagonal-only stop remains unchanged.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED proposal changed the zero-set input from the diagonal to a fixed actual G-zero fiber; existence of that input and relevant trace/period theorem scope had not been assessed.
SCOPE: Exactly L868's global real C1 q,r,h on R2 times T2, h>=0, q^2+r^2<=|F|^2, its two closure equations, fixed orientation and all F/J zeros; C868a's audited conclusions; no growth, bandwidth, absolute summability, holomorphicity, graph existence or assumption about the location or multiplicity of a nonzero zero of actual G.
COVERED_TARGET: Test whether vanishing of q,r on one actual nonzero G-zero fiber forces K>=-|M| for L868's full C1 class.

## Original nomination (source status superseded below)

The mathematical question behind this source review is whether the
full actual fiber z1=a, with the second coordinate unrestricted in C*,
adds enough control to bound K at -|M|. Existence and applicability of
an actual nonzero G-zero must be supplied from precise local or primary
inputs; no particular zero or multiplicity is asserted here. If a
theorem requires extra hypotheses, record that difference rather than
silently adding them. This is a proposal, not a derived trace identity
or a claim that the fiber controls the exceptional modes.

Essential local inputs for comparison are L847's actual G and F,
L868's audited system and period interface, and audited C868a. Read
only the relevant actual-G input when needed. L867 is a comparison
with the narrower absolute or radial-independent class, not an
additional premise that settles the full class. No cross-notebook
result is proposed. Full matching Mathlib coverage is unchecked.

Reuse the existing compact Fourier sources for unchanged operations.
Search the exact system and standard zero-divisor trace/closed-form
period terminology, and inspect primary theorem hypotheses and the
essential proof cases before approving a calculation. Distinguish
vanishing on a codimension-two fiber from vanishing on an entire
angular torus. Determine whether an imported theorem already gives
the proposed conclusion, or whether a bounded specialization or
exploration is justified. A source snippet or the old Fejer coverage
alone is not enough.

The discriminating mathematical target, if later covered, is the
sharp period inequality for the unchanged full class. Continue only
with a quantitative bound, an independent compatibility obstruction
on the previously uncontrolled modes, or a rigorous admissible
counterexample to the proposed fiber consequence. A formal trace
identity that leaves the same unrestricted mean does not justify
another unchanged attempt. Preserve
`ATTEMPTS/2026-11-06-fourier-diagonal-period-uncontrolled.md` and
`ATTEMPTS/2026-11-06-one-sided-dual-reduction-period-gap.md`.

A no-gain result would delimit this certificate route; a strict-gain
example would obstruct L847's positive graphs through L868. Neither
would settle graph realization by another route, higher Xi signs or
the main all-degree mixed-positivity gap. Creative discovery remains
a priority, but this uncovered proposal is not yet an approved new
central mechanism or a reason to label routine specialization creative.


## Completed literature-only comparison, 6 November 2026

The EXPLORE decision supersedes only the nomination's missing-source
status. Neither the fiber's effect on Fourier profiles nor a period
inequality was derived. The covered mathematical continuation requires
separate next-turn approval. No lemma or mathematical script was edited.

### Local overlap and retained failures

Read L847's actual-function hypotheses and graph/Stokes interface,
the complete L868 and C868a including their audits, and L018's exact
zero correspondence. Reused the two named Fourier assessments and
checked the one-sided reduction and Fourier/diagonal attempt notes,
plus their directly relevant histories. No completed fixed-G-zero-fiber
test was found in those records. This is a scoped duplicate check,
not an exhaustive novelty claim. The initial date-wide local search
was overbroad and truncated; it is not evidence for this conclusion.

The stopped diagonal calculation controls nonzero sums of the two
angular indices by H, leaving the zero mode and opposite-index
profiles away from equal radii. L868's bump has K=0; its presence
does not refute the desired inequality. The radial-independent
subclass theorem requires precisely that extra hypothesis. Preserve
both named ATTEMPTS records; neither is overcome by this review.

### A usable actual zero: known input, not a new theorem

[E. C. Titchmarsh, *The Theory of the Riemann Zeta-function*,
second edition revised by D. R. Heath-Brown, Oxford (1986),
Section 10.2, pp256-258](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=133),
states Hardy's theorem: infinitely many zeta zeros lie on Re(s)=1/2.
Read that statement and its first proof through its final contradiction,
including the eventual-sign hypothesis and the parameter-limit step.
Only the named theorem is imported; there is no need to reproduce it.

For applicability choose a nonzero ordinate gamma supplied by that
theorem. L018 identifies the corresponding xi zero; in L847's existing
formula choose a=-4 gamma^2, so a!=0 and either square root is
+/-2i gamma. Reflection makes the two choices equivalent and yields
G(a)=0. This is the necessary coordinate specialization of a known
input, not a new zero certificate or location assertion. No prescribed
ordinate, multiplicity or RH assumption is needed. A future canonical
proof must cite Hardy at this location when using that input.

### Primary period and trace comparison

[Peter W. Michor, *Topics in Differential Geometry*, April 2008
manuscript, 11.15/11.16, pp140-141;
31.16, pp424-425](https://www.mat.univie.ac.at/~michor/dgbook.pdf#page=150):
relative de Rham cohomology uses smooth forms whose pullback to a
closed submanifold vanishes. Read the exact sequence and its
partition-of-unity extension proof. The relative Poincare lemma
gives a primitive near a submanifold; read its tubular contraction
proof, including regularity at contraction parameter zero and the
stronger ambient-vanishing case. These statements contain neither
a global primitive nor a positivity or quantitative period estimate.
Their smooth-form setting does not by itself cover arbitrary C1
feasible triples. No smoothing that preserves domination is supplied.

The proposed fiber fixes both x1=log(|a|/R) and y1=arg(a), leaving
z2 unrestricted. It is a closed smooth real-codimension-two
submanifold, not an angular two-torus. Coefficient vanishing there
must not be replaced by vanishing for every y1 at that radius.
Tangential restriction of a form and vanishing of selected ambient
coefficients are different hypotheses. Checking the former alone
does not complete the proposed coefficient/period test.

Reuse exactly the compact C1 differentiation, periodic integration
by parts and uniform product Fejer reconstruction already inspected
in `2026-11-06-diagonal-fourier-correction-audit.md`: Rudin,
*Principles of Mathematical Analysis*, 3rd ed., Theorem 9.42,
pp236-237, and Grafakos, *Classical Fourier Analysis*, 3rd ed.,
Proposition 3.1.10, Corollary 3.2.2 and Theorem 3.3.9(a),
pp180-183,196-197, with that assessment's direct URLs and corrections.
For each fixed compact radial set the current C1 functions meet
those hypotheses. Uniform reconstruction allows restriction to a
fixed angular coordinate; no absolutely convergent unweighted
coefficient identity or admissible finite approximation is imported.
Any further PDE uniqueness or global regularization theorem would
need a new hypothesis comparison before use.

### Search and access record

Queries included `closed differential form vanishes submanifold
restriction relative de Rham cohomology period torus`, `relative
de Rham cohomology submanifold closed forms pullback zero long exact
sequence lecture notes pdf`, `"zero fiber" "Fourier" "period"
closed forms`, `"C1" "closed" "forms" "vanishing" "periods"
torus`, and exact-system probes using `"q+h"`, `"r"`, closedness
and torus periods. Results led to the inspected Michor text; none
inspected matched L868's domination/closure system or supplied its
sharp period threshold. This bounded search does not establish
absence from the literature or originality.

For the actual-zero input searched Hardy 1914 and followed the
precise Section 10.2 statement/proof in Titchmarsh. The original
Hardy-Littlewood Acta PDF on Project Euclid returned a service
challenge; the archive text and attempted Numdam endpoint did not
open. Those are uninspected leads, not supporting evidence.
Michor's UCI mirror intermittently timed out; the author's URL
above supplied the complete selected statements/proofs. A retry of
Lebl's SCV PDF timed out; its already assessed C1 Stokes input in
L868 remains reusable and was not promoted to a new fiber theorem.
No essential access blocker remains for the compact operations in
the covered test. Matching Mathlib coverage is unchecked.

### Bounded continuation and decision test

After separate approval, perform exactly COVERED_TARGET using L018,
L847, audited L868 and C868a, the known Hardy input and the reused
compact Fourier operations. No fiber trace identity or propagation
law is preapproved as true. The existing full-class constraints
remain necessary everywhere, including every other F zero and all
J zeros. There is no assumption of graph existence, bandwidth,
growth control, holomorphicity, or higher regularity.

Continue only if the attempt proves K>=-|M|, supplies an independent
compatibility obstruction on the previously uncontrolled modes with
an explicit downstream use, or constructs a rigorous globally
admissible counterexample to the inequality. Finite-mode evidence
or a trace relation leaving the same free mean is insufficient.
If only that happens, save the reasoning and stop this fiber
mechanism without resetting the inherited exploration budget.
A no-gain result would delimit this certificate route; a strict-gain
certificate would obstruct the L847 graphs via L868. Neither supplies
graph realization, higher Xi signs or all-degree mixed positivity.
This is established-route development, not an approved new central
Xi-sign mechanism or certified original mathematics.
