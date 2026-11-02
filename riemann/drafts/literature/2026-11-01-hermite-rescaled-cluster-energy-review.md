# Hermite-rescaled cluster energy — completed source comparison

TARGET: Assess the Hermite-rescaled cluster energy -sum_{i<j} log(|r_i(t)-r_j(t)|^2/|t|) at an isolated finite real heat multiple zero, and specify one sextic heat-family test of a sign-definite finite-part production law.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed the bounded heat-zero/Hermite/discriminant/finite-free-entropy searches recorded below and reused the adjacent pair-energy/flux comparisons. New primary finite-free and Weyl-chamber cases give an explicit real-rooted/full-configuration scope mismatch; no matching selected-complex-cluster production/coercivity theorem was located. No novelty inference.
SOURCE_EVIDENCE: Hall–Ho, Letters Math. Phys. 115:60 (2025), Proposition 3.1 with full proof and Section 3.3, https://doi.org/10.1007/s11005-025-01946-9 ; Garza-Vargas–Srivastava–Stier, arXiv:2602.15822v2 (17 September 2026), Definition 1.1, (1.3), Section 2.2/Lemma 2.5, Lemma 6.1 with full proof, https://arxiv.org/html/2602.15822v2 ; Voit–Woerner, arXiv:1910.07888v1, Lemmas 2.2–2.4 and Theorem 2.8 with its boundary proof, https://arxiv.org/html/1910.07888v1 ; Polymath arXiv:1904.12438v2, Proposition 3.1(i)–(ii) with proof, https://arxiv.org/html/1904.12438v2 . Scope comparisons only.
COMPARISON: The finite-free entropy proof squares real velocities for a whole real-rooted polynomial; Hall–Ho distinguish holomorphic complex heat-root motion from Coulomb gradient flow. Weyl-chamber separation goes forward from a real collision, not through its complex side. None supplies the requested modulus-gap finite-part sign or the omitted external-factor control for a selected local cluster.
GAP: No source-supported sign dE/dt<=0 for negative t, complete selected-cluster production law, or independent bridge to L617's full-potential cusp has been established. The finite part and sextic sign remain uncalculated; arbitrary residual drift is neither proved nor excluded.
REASON: Park this specified normalization as a collision-coercivity route because it fails the nomination's independent-bridge test, not because all normalizations are impossible. Preserve the exact two-value sextic discriminator without approving or performing it. Seek actual-theta forcing data separately rather than another universal heat-energy extension.
LITERATURE_REASON: Essential coverage is missing for a changed functional and collision normalization, not for the already assessed reference-gap energy or finite off-root PDE.
SCOPE: Literature-only source comparison of the exact TARGET. EXPLORE records a completed bounded search and its scope limit; it licenses no calculation on the parked energy. The separate actual-theta nomination is REVIEW_REQUIRED.

## Completed review — 1 November 2026

The main gap remains actual-Xi all-degree mixed positivity at unbounded
heights. The intermediate target was a sign-definite production law for
the specified isolated cluster, with a plausible use in controlling
L617's collision defect. A finite residual sign alone does not exclude
a collision. The test required both collision-valid hypotheses and an
independent defect-control bridge. The newly inspected sources do not
pass that test; no mathematical production formula is derived here.

### Primary hypotheses and essential proof cases

**Complex polynomial dynamics.** Hall–Ho, *The heat flow conjecture for
polynomials and random matrices*, version of record, 26 May 2025,
[Proposition 3.1 and Section 3.3](https://doi.org/10.1007/s11005-025-01946-9):
for a degree-N polynomial evolving by p_tau=p_zz/(2N), locally distinct
roots satisfy z_j'=-N^(-1) sum_(k!=j)(z_j-z_k)^(-1). The proof uses the
implicit function theorem and p''/p' at a simple root; its pair-difference
identity (3.7) explicitly retains every other root. The second-order
proof cancels the complete antisymmetric triple sum. Section 3.3's
Coulomb equations instead contain conjugate denominators. Consequently
the cited real gradient-flow dissipation is not the complex heat-root
law. The polynomial is defined at collisions, but the displayed root
ODE requires simplicity. No source formula is applied at t=0, to an
infinite zero sum, or to a cluster after discarding other roots.

**Finite free entropy.** Garza-Vargas, Srivastava and Stier, *Finite Free
Information Inequalities*,
[arXiv:2602.15822v2](https://arxiv.org/html/2602.15822v2), 17 September 2026:
Definition 1.1 uses real root vectors and
chi_n=2/[n(n-1)] sum_(i<j) log|alpha_i-alpha_j|. Equation (1.3) gives
its scalar rescaling law. Section 2.2 uses exp(-s partial_x^2/2),
s>=0, preserving real-rootedness; Lemma 2.5's differentiated motion
requires simple roots. Lemma 6.1, with variance-one Hermite convolution,
uses exp(-s partial_x^2/[2(n-1)]), and states chi_n'=Phi_n/2.
Its complete proof (6.1) and subsequent three displayed equalities
differentiate all pair gaps and end with (2/n) sum_i (alpha_i')^2.
These are squares of real velocities, not modulus squares for complex
velocities. At an unsmoothed repeated initial root the displayed
logarithms/reciprocals are singular; this review imports no finite
classical derivative at that endpoint. The selected cluster on the
negative-t side in L059/L060 is outside the real-rooted hypothesis.
Neither time normalization nor restricting a whole-root identity to
that cluster is a theorem of this source.

**Hermite scaling and collision boundary.** Voit and Woerner,
*The differential equations associated with Calogero–Moser–Sutherland
particle models in the freezing regime*,
[arXiv:1910.07888v1](https://arxiv.org/html/1910.07888v1), 17 October 2019
(the generated HTML also displays a different internal date):
(2.1) is the repulsive reciprocal-gap ODE in a real ordered Weyl
chamber. Lemmas 2.2–2.4 supply Hermite self-similar solutions and radial
normalization; the latter proof uses a confined logarithmic potential
for the whole real configuration. Theorem 2.8 allows every closed-chamber
initial point and places the solution in the open chamber for positive
time. Its full boundary proof passes to elementary symmetric coefficients,
uses their polynomial evolution and discriminant, and compares scaled
limits with the Hermite solution. It proves forward separation from a
real boundary configuration, not a sign through a complex cluster.
No printed time-change or confined-potential constant is imported or
reproved here. This avoids treating that different normalization as
the nominated energy.

**Actual heat splitting.** D. H. J. Polymath,
[arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2), 4 August 2019,
Proposition 3.1(i) uses a paired convergent zero sum at a simple zero;
(ii) covers a repeated zero of finite order m>=2 and gives Hermite-scale
splitting on both sides. Its full proof uses the backwards heat equation,
Taylor expansion, simple Hermite roots, the inverse function theorem
and Rouche counting. Error constants depend on the collision. This
matches the role already played by L058/L059/L060 after their stated
normalization; it supplies no subleading cluster production sign or
external-factor estimate. No higher-order expansion is inferred from
the leading O(|t|) error.

A further source inspected only for scope is Cuenca–McSwiggen,
*The rectangular finite free heat flow*,
[arXiv:2606.06859](https://arxiv.org/html/2606.06859), June 2026,
Proposition 2.8 and proof, Corollary 3.1 and its displayed proof:
the ordered positive variables obey a gradient flow for (27), with
additional log r_i and log(r_i+r_j) terms, giving positive entropy
production. This is a different differential operator, domain and
functional. It is not a theorem for the nominated complex cluster.
Later Fisher-information and collision results were not proof-audited
and are not inputs. No primary manuscript is declared fully audited.

### Exact discriminator retained, but not performed

For a=+1/100 and a=-1/100, retain exactly

    H_a(t,z)=exp(-t partial_z^2)[(z^2-1)^2(1+a z^2)].

The proposed test would isolate the two roots at z=1 as t tends to zero,
justify their simplicity/counting for nonzero t, retain all other roots
or the nonvanishing local factor, and test the fixed orientation

    d/dt [-log(|r_1(t)-r_2(t)|^2/|t|)] <= 0,  t<0.

It would need an actual limiting derivative, or a signed remainder on
an explicit negative interval; numerical samples or a root preview do
not decide it. Include a=0 only as a calibration, not a parameter sweep.
One positive derivative would reject this universal orientation. If both
values passed, that would validate only these test objects, without
actual-theta realization or a cusp-control implication. The source
comparison supplies neither that implication nor an independent theta
bound. Therefore the required bridge is missing and this test is not
approved as a continuation of the present coercivity nomination.
No sign, finite part, counterexample or freely adjustable drift is proved.

### Duplication, failures and routing

Reuse the ready reference-gap assessment
`2026-11-01-collision-renormalized-log-energy.md` and flux assessment
`2026-11-01-collision-boundary-flux-discovery.md`; their primary proofs
are not re-audited. Read L058/L059/L060 in full, L487's statement and
initial polynomial/root passage, and L617's statement and source/preparation
passage. L487/L616/L617 remain contrasts at their exact scope. L616's
traces and L617's completed audit are reused through the ready adjacent
comparison, not replayed. In particular this review does not claim
L487's full proof was newly audited. Scope-checking nearby ready audits
found that C489a, C493a, L469/L470/L474/L486/L528 already have canonical
audits despite older overview qualifiers; do not schedule them again
merely to obtain a mathematical turn. L573's unaudited cap result belongs
to the stopped L575 residual route and is not a collision continuation.

The new evidence is the finite-free proof's real-velocity squares,
the whole-real-configuration normalization and the explicit complex
Coulomb/heat distinction. This changes the proposed import decision;
it is a source-scope NEGATIVE, not a mathematical impossibility theorem.
No derivation, lemma, script, source-proof repair or RH progress beyond
the cited scope is claimed. Full matching and supporting Mathlib
coverage remain unchecked.

Search queries included `heat polynomial zeros Hermite scaling collision
logarithmic energy discriminant monotonicity`; `"backward heat" "zeros"
"discriminant"`; `"polynomial" "heat" "discriminant" "monotone"`;
`"zeros" "heat equation" "rescaled" "energy"`; `"Hermite" "zero dynamics"
gradient flow logarithmic`; `"Calogero" "heat equation" "zeros" "gradient"`;
`"finite free heat flow" "gradient flow" entropy`; `"finite free" "entropy"
"Hermite" heat`; and `"differential equations associated" "Calogero" Voit`.
Search results, model memory and secondary summaries are leads only.
The located *When Finite Free Curves Split* and exceptional-Hermite
papers were not inspected and support no conclusion. Exact-statement
non-discovery is not proof of novelty or nonexistence.

The next source nomination changes the input mechanism to the actual
Jacobi orbit of L608, not another normalization of a generic heat energy.
It must compare the recorded theta-curvature and reciprocal-Stein stops
before selecting any calculation. The specific missing ingredient is
control of the nonvanishing analytic factor using independently checkable
actual-kernel data, followed by a defect-control implication. No creative
invocation is ready without those data. The new assessment is
`2026-11-01-actual-jacobi-collision-factor-discovery.md`; it is separate
and REVIEW_REQUIRED. No exploration/recovery counter is reset here.

## Original nomination, preserved as historical scope

Use F of L058 and a hypothetical isolated real zero of finite order m>=2
at lambda_*>0. Put t=lambda-lambda_* and let r_1(t),...,r_m(t) be
exactly the nearby roots counted with multiplicity, as a multiset;
for nonzero small real t their distinctness must be justified by the
local splitting inputs. The prospective energy is precisely the TARGET
sum with this signed t and the real natural logarithm of the positive
gap quotient. It does not use an arbitrary reference configuration,
global zero labeling, an infinite pair sum or an unchosen counterterm.
No regularity or limiting value at t=0 is asserted by this nomination.

The proposed bounded question is whether a source-supported production
law implies dE/dt<=0 on a sufficiently small negative-t interval from
the exact heat equation and stated independently checkable hypotheses.
Fix this orientation before any test; do not reverse it after a failure.
If another sign is the only natural source conclusion, record the
difference and assess its relevance before approving mathematics.
Retain the analytic factor/external cluster effect rather than dropping
it as lower order without a proved estimate.

A proposed later discriminator is the explicit one-parameter family

    P_a(z)=(z^2-1)^2(1+a z^2),
    H_a(t,z)=exp(-t partial_z^2)P_a(z),

with proposed test values a=1/100 and a=-1/100 and candidate cluster
at (t,z)=(0,1). The exponential is the terminating
polynomial heat operator. This defines test objects only; no claim
about their roots, imaginary-axis sign, strip, flux, energy derivative
or their realization by Xi is made. The two stated values do not
authorize a parameter sweep. Include the base a=0 solely for comparison
with L487, not to repeat its old energy or L616's trace calculation.

Essential inputs for a later attempt: L058/L059/L060 for exact
normalization and splitting, and L487/L616/L617 as preserved contrasts.
No cross-notebook input. Do not derive the proposed production formula
in the source turn. First search the exact statement, Hermite-scaled
zero dynamics, discriminant/cluster energy terminology and stronger
known results; read primary hypotheses and the relevant collision cases.
Reuse adequate unchanged assessments rather than browse them again.

Main gap: actual-Xi all-degree signs and collision exclusion. A useful
intermediate input would separate universal collision scaling from
nonuniversal cluster forcing and identify a sign condition with a
specific defect-control use. A finite residual sign alone is not
collision exclusion. Actual-theta forcing, all-height uniformity,
tails, initial signs and zero time remain independent gaps.

Continue only if the source comparison provides a defined production
law or a bounded derivation/countermodel target with a plausible
defect-control bridge. Otherwise park this specified subtraction;
do not produce a lemma simply because its finite part is computable.
Any approved finite specialization is REPRODUCTION/development unless
a genuinely new central mechanism is separately justified. No creative
invocation is ready from this nomination. Mathlib coverage is unchecked.
