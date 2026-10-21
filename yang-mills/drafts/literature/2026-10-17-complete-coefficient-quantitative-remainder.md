# Complete coefficient — quantitative remainder source comparison

TARGET: Assess whether the existing component-limit proofs yield an O(a^(-5/2) log(1/a)^2) remainder for the complete L011 order-g^2 coefficient for both actual L010 probes.
CHECKED: 2026-10-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Screened L218's finite partition, L079 sections 2–5, L090 sections 3–4, L101(3) and proof section 2, L216's statement and L217 section 6; searched the active notebook for quantitative/L079/Reisz matches and inspected ATTEMPTS/023–025. External queries and inspected primary passages are recorded below.
SOURCE_EVIDENCE: Reused the 2026-10-16 complete-cubic assessment and the 2026-09-27 fixed-box locality assessment; rechecked Adams–Lee 0709.0781v3 section II and Appendix A (A1), (A11)–(A18), and inspected Lawler–Limic Random Walk: A Modern Introduction sections 1.1, 4.3 and 4.6 as recorded in the narrower continuation assessment.
COMPARISON: The inspected proofs establish no complete O(a^(-5/2) log(1/a)^2) remainder. L079 has a qualitative pinned comparison, L101 retains O(N^(27/10)) before its remaining limit, and L217's collar/fiber/finite-ball limits have no jointly uniform rate. None is a lower bound or a disproof of the proposed complete rate.
GAP: The first selected missing estimate is a quantitative version of L079's comparison with its finite-mesh diagnostic; independent L101 and other component errors remain. The whole coefficient cannot be assigned a rate by finite assembly of the currently stated inputs.
REASON: New source-scope evidence rules out the proposed automatic rate extraction and selects one independently testable pinned-trace estimate; no new bound is derived and no essential source is blocked.
LITERATURE_REASON: The proposed quantitative remainder is outside the completed cubic-limit assessment; the rate hypothesis, rather than the probes or geometry, has changed.

This is a completed literature-only comparison, not a rate theorem or
an assertion of novelty. The original quantitative target is preserved.
The decision authorizes exploration only within separately assessed
scope; it does not license a complete-coefficient rate calculation.

The main gap is still ultraviolet-uniform interacting matching with
reflected error <=c_box/2, followed by continuum axioms and infrared
finite positive mass. The intermediate target would give an explicit
subcubic scale, unlike the current qualitative remainder. That could
support a later coupling/remainder comparison, but would not itself
establish finite matching or a cutoff-uniform perturbation expansion.
The threshold is a rate to assess, not a predicted consequence of L220.

## Local comparison and first obstruction

L218 proof sections 1–2 give the existing exact finite partition.
L220's accepted cancellation is imported without repeating its audit.
For the proposed threshold, the following inspected inputs already
prevent automatic quantitative assembly:

| Input | What its existing argument supplies | Missing quantitative information |
| --- | --- | --- |
| L079(2), proof sections 2–5 | Differentiated-source l2 convergence, monopole energy convergence, coefficient freezing and the complete heat sum, giving a^3 J_(i,N)-2 gamma D_(i,a) -> 0 | Section 2 fixes a spectral cutoff and polynomial degree before refinement; section 3 fixes a radius before removing the energy tail. No uniform N-dependent modulus is given. Section 5 explicitly disclaims a rate. |
| L090(13)–(17), proof sections 3–4 | Successive mass, projection and finite-range approximations and a zero cubic limit | Mass-dependent constants and subsequent localization errors are not bounded jointly at the requested rate. A vanishing mesh limsup at fixed parameters is insufficient. |
| L101(3), proof section 2, (10)–(12) | A complete heat-summed O(N^(27/10)) static-replacement error | This stated allowance is above N^(5/2) log(eN)^2. It supplies no lower bound; improving it or finding cancellation in the complete coefficient remains possible. The static trace still needs its own quantitative comparison. |
| L217 proof section 6 | After refinement at fixed delta,R,L: limsup scaled error <= C_i delta+C_i/R+C_(i,R)/L^2 | The finite-ball constants may depend on delta, with no uniform rate. The text explicitly takes the limits successively. L215's O(a^-5/2) plateau replacement does not provide rates for L216's or L217's subsequent limits. |

These are sufficient obstructions to importing the proposed rate from
the **existing statements and recorded estimates**. They do not show
that those proofs cannot be strengthened, or exclude a better joint
finite-mesh cancellation. No exhaustive rate audit of all other inputs
is claimed or needed to identify this first missing estimate.

The unchanged cubic assessment's flow/Ward source comparisons are
reused: renormalized positive-time finiteness and formal improvement
expansions do not provide this bare all-face forest remainder.

## Primary theorem comparison

Adams–Lee, *Structure of logarithmically divergent one-loop lattice
Feynman integrals*, Phys. Rev. D 77 (2008) 045010,
[0709.0781v3](https://arxiv.org/pdf/0709.0781v3), 5 December 2007:
rechecked section II, printed pp. 5–7, (7)–(15), and Appendix A,
printed pp. 19–23, (A1), denominator bounds and (A11)–(A18).
For the specified four-dimensional Brillouin-zone integrals, smooth
scaled numerator/denominator, polynomial continuum limits, nonnegative
denominator with the stated growth and sole zero, infrared finiteness,
and negative lattice degree give an error <=c(p)a log(1/a), for
0<a<=a_0(p). The proof separates small, intermediate and ultraviolet
regions; its constants depend on the external parameters. This is not
a theorem about the pinned forest trace, spatially varying coefficients
or uniform external heat summation. Those identifications and bounds
are absent. Section VI (56)–(57), printed p. 18, describes broader
power/log expansions as expectations and extension directions, not a
proved rate for general divergent integrals. Reproving (A1) would not
settle this comparison.

The supporting scalar Green-function sources and their exact scope
are recorded in
`2026-10-17-first-pair-pinned-trace-quantitative-rate.md`.
They support a concrete local test, not a full response theorem.

New external queries on 2026-10-17:

- `Adams Lee structure one loop lattice perturbation theory integrals logarithmically divergent 2008 power corrections`
- `finite volume lattice Green function quantitative convergence Dirichlet differentiated Green function rates dimension three`

The queries located the primary Adams–Lee paper and numerical,
homogenization and other Green-function leads. Those other search
results are not inspected theorem inputs. No novelty or absence claim
is inferred from this bounded search. No inaccessible theorem is an
essential premise of the selected continuation.

## Relevance, duplicate/failure check and bounded continuation

The original target could help a future coupling/remainder comparison,
but even its proof would not establish a uniform interacting expansion,
finite matching, reflection positivity or finite positive mass.
L079 is the first selected rate gap because its reduced trace is
already exact and its sources remain in a fixed physical interior.
The next test keeps D_(i,a) at finite mesh; it does not also assume a
rate for D_(i,a)->D_i. Its assessment names the exact target and test.

Local searches found no existing quantitative L079 result. Historical
ATTEMPTS/023–025 stop right-row shear with generic norms, deletion of
the upper axial correction, and axial-profile/absolute-norm power gains.
The selected test instead starts after L078's exact covariance
cancellation and quantifies L079's pinned Green comparison. None of
those failed replacements is revived. L101 is a distinct remaining
obstacle even if this test succeeds.

Outcome: NEGATIVE source-scope evidence for automatic rate extraction,
with no mathematical counterexample, new lemma or mathematical script.
The narrower ready assessment is newly written and requires the
supervisor's separate approval before its mathematical invocation.

Continue only if the selected signed comparison has an N-explicit
bound uniform over its interior sources and summable over all actual
heat coefficients. Abandon this particular quantitative transfer if
its required norm estimate fails or necessarily loses the threshold;
record the exact obstruction rather than repeating qualitative limits.
A missing interacting uniform coupling expansion, boundary or mode-tail
estimate is not assumed.
Retain both actual probes, the relative cube, straight forest, admitted
even meshes a=8/N, fixed tau=1/16, all faces/end rows, constant modes,
upper jumps, both residual subtractions and complete heat sums.
Independent finer asymptotics, reflection positivity, continuum and
infrared requirements remain unresolved. Mathlib coverage for this
new quantitative target is not checked.
