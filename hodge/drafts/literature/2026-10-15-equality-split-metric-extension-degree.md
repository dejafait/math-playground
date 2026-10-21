# Equality split fibre — metric extension and local degree source comparison

TARGET: Assess whether L100's totally geodesic stable branches force local classifying degree two at an isolated split fibre of the equality kernel.
CHECKED: 2026-10-15
DECISION: EXPLORE
SEARCH_EVIDENCE: Targeted singular hyperkahler quotient, reducible-instanton metric and trianalytic normalization searches located Mayrand and Verbitsky; reused the split-slice/stable-geodesy assessments and compared L094--L096/L099/L100 and the scoped complex-jet stops. No applicable metric extension or local-degree theorem was found in the inspected sources.
SOURCE_EVIDENCE: Mayrand, Complex Manifolds 9 (2022), 261--284, Theorems 1.1--1.4 pp. 262--263, complete proof of Theorem 1.3 p. 276 and local-model/Poisson proof cases Sections 4.3/4.9 pp. 277--278/282; Verbitsky alg-geom/9703016v1, Definitions 4.1--4.2/Remark 4.4 pp. 17--18, Proposition 6.1/Theorem 6.2 and proofs pp. 26--27, Section 10.2 pp. 37--38 and Proposition 10.3/proof pp. 38--39.
COMPARISON: Mayrand gives a complex-Hamiltonian/Poisson local model for a finite-dimensional integrable quotient, not an isometric normal form; an applicable finite-dimensional metric reduction of this ASD germ is also unestablished. Verbitsky requires a quaternionic action on the singular differential sheaf and two integrable induced structures, not merely a punctured hyperkahler metric. Neither source supplies the missing actual-germ degree-two bridge.
GAP: The retained family has a smooth unitary slice derivative and stable-open geodesy, but no checked singular metric extension, compatible local isometry or degree-forcing theorem. No claim that degree two is false, or that no such theorem exists, follows from this review.
REASON: Park this metric-extension mechanism: the new primary comparisons expose a precise hypothesis/conclusion mismatch and provide no independently evaluable degree test. Preserve the earlier bracket/Green and product-jet blocks; propose a separate integral gerbe obstruction review rather than another metric calculation.
LITERATURE_REASON: The saved changed target required essential singular-metric theorem coverage beyond the ready all-point slice and smooth stable-geodesy sources; this invocation completes that source comparison only.
SCOPE: Conditional equality kernel of L071/L093 at the fixed identical K3 metrics, a chosen split fibre in L096's finite possibly empty set, and L095's actual nonzero harmonic derivative. No split fibre is assumed to exist globally. L099's normalization conclusion and L100's stable-open geodesy are retained conditional inputs, not extension theorems at that point.

## Completed source review and route decision

This is a LITERATURE / NEGATIVE / NOVELTY_UNCHECKED step. The negative
result concerns feasibility from the checked sources, not nonexistence
of F or a mathematical counterexample. No new implication, lemma or
mathematical script is approved or derived here. The continuation test
in the original proposal below was not met.

**Singular quotient local models.** Maxence Mayrand, *Stratification of
singular hyperkahler quotients*, Complex Manifolds **9** (2022),
261--284, DOI 10.1515/coma-2021-0140,
[published primary text](https://d-nb.info/1267352590/34#page=2).
Read Theorems 1.1--1.4, pp. 262--263. The setup is a smooth
finite-dimensional hyperkahler manifold with a compact tri-Hamiltonian
group; Theorems 1.2--1.4 additionally require its action to extend
holomorphically to the complexification for one induced structure.
Theorem 1.1 describes smooth orbit-type pieces. Theorem 1.4(iv) is
a biholomorphic, orbit-type-preserving, holomorphic-Poisson local
model by a linear complex-symplectic reduction. Read the complete
Theorem 1.3 proof, p. 276, Proposition 4.2's quotient construction,
pp. 277--278, and Proposition 4.14's proof, p. 282. The normal form
matches the complex symplectic form by holomorphic Darboux--Weinstein;
it does not match all three Kahler forms or the metric. The introduction,
p. 262, explicitly distinguishes a symplectic moment normal form from
a hyperkahler one. The arXiv v2 (22 November 2020) introduction,
[PDF p. 2](https://arxiv.org/pdf/1807.05992v2#page=2), states the
missing first-Kahler-form compatibility particularly explicitly.
No general theorem is reproved.

For this target there are two separate applicability gaps. L094's
finite-dimensional obstruction zero set is not an established smooth
hyperkahler manifold with a tri-Hamiltonian stabilizer action. The
infinite-dimensional connection space and gauge group do not directly
meet Mayrand's finite-dimensional/compact-group hypotheses. Even an
independent complex-Poisson identification would not transport L100's
metric geodesy to an isometric quadratic quotient. Thus the theorem
cannot be used here as a singular geodesic-uniqueness or antipodal
identification theorem. This is a scope comparison, not a proof that
such an identification is impossible in this particular germ.

**Normalization of hypercomplex varieties.** Misha Verbitsky,
*Hypercomplex varieties*,
[alg-geom/9703016v1, 12 March 1997](https://arxiv.org/pdf/alg-geom/9703016v1#page=17).
Read Definitions 4.1--4.2 and Remark 4.4, printed pp. 17--18,
Proposition 6.1/Theorem 6.2 and their complete proofs, pp. 26--27.
A quaternionic action on the real analytic differential sheaf and
integrability of two distinct, nonopposite induced structures are
required. Theorem 6.2 makes the normalization smooth and hypercomplex;
it is not a metric extension theorem. Its proof uses local homogeneity
and regularity of normalized local rings before gluing structures.
Section 10.2, pp. 37--38, starts with a stable bundle, so its
moduli application does not include the central polystable sum here.
Read Proposition 10.3 and its proof, pp. 38--39: for a generically
free finite action preserving a hypercomplex variety, free outside
a nonempty finite fixed set, the structure on the free quotient
does not extend as a hypercomplex-variety structure to the quotient.
This distinguishes that definition from an orbifold structure.

L100 supplies neither of the singular differential-sheaf hypotheses.
L099 already identifies a smooth normalization, but that is not a
descent of quaternionic operators to the original image's differential
sheaf. The theorem cannot supply its own hypotheses from the puncture.
Proposition 10.3 is a warning against that inference, not a counterexample
to the proposed classifying-degree statement and not an identification
of the actual image with a finite quotient. No such image description
has been assumed or proved.

**Local comparison and prior failures.** Read L094/L095's full
hypotheses and conclusions, L096's hypotheses, conclusion and actual
slice setup, L099's normalization statement, and L100's hypotheses
and conclusion. Reuse the primary all-point ASD slice assessment
2026-10-12-equality-split-local-slice.md and the smooth stable-geodesy
assessment 2026-10-14-equality-stable-geodesy-critical-audit.md with
history/264. Neither is refreshed unnecessarily. L095's derivative
lives before quotienting; L100's covariant identity lives on U only.
Neither is a removable-singularity result.

Read L103/L105/L106's hypotheses and conclusions as contrasts, with
L104's conditional degree-two scope supplied by the overview. L103
bounds the degree for its selected complex first jet and ordinary
analytic GIT image; L105 even supplies a chosen degree-one complex
family. L106 excludes that prescribed second jet as a product jet.
These facts do not decide the degree of the actual equality-family
germ. The failures preserved in the normal-curvature assessment and
history/291 still concern unavailable analytic data. None is reopened.

Queries included “Verbitsky singular hyperkahler moduli polystable
bundles trianalytic normalization locally homogeneous singularities
metric”, “reducible instanton moduli space L2 metric tangent cone
hyperkahler quotient local isometry geodesic”, “totally geodesic
subvariety singular hyperkahler quotient normalization orbifold degree
two”, “Verbitsky Hypercomplex varieties normalization singularities
moduli polystable”, and “Mayrand local structure singular hyperkahler
quotients metric local normal form”. Search snippets were discovery
only. Braam--van Baal's *Instanton moduli as a novel map from tori
to K3-surfaces* was located as a special torus/orbifold lead; its
essential proof was not read and no theorem from it is imported.
No inaccessible source is used to support a conclusion, and the
bounded search establishes no exhaustive absence or novelty.

Full matching Mathlib coverage remains **not checked**. No canonical
lemma or argument changes: DAG.md and PROOF.md remain untouched.
The separate next proposal concerns an integral universal-sheaf gerbe
obstruction, rather than a metric extension; its coverage is missing
and is explicitly REVIEW_REQUIRED in its own assessment.

## Original proposal retained as startup reasoning

The following paragraphs record the proposal before this source review;
the completed decision above supersedes their pending-review language.

The main gap is universal primitive Hodge realization. The intermediate
question is whether an actual split fibre is compatible with the already
conditional normalization and stable-open metric conclusions. Its plausible
downstream use would be restricting the reducible locus of this one kernel
recipe. Even exclusion of every split fibre would leave all-stable kernels,
other correction pairs, actual mixed action, transport and the universal
target unresolved.

The proposed test is local degree two for the actual classifying germ,
not existence of a complex family with degree one or two. Read L094/L095's
actual tangent hypotheses, L096's isolation result, L099's normalization
argument and L100's stable-open scope before the later comparison. L103--
L106 are contrasts to check: complex approximation, a selected second jet
and a necessary product identity must not be substituted for a metric
extension or the actual germ. These are local notebook inputs only.

This proposal is materially different from the parked normal-curvature
and flat-source product-jet targets: it asks for a singular metric/germ
comparison usable without their missing evaluated bracket/Green data.
That independence is a feasibility requirement, not an established fact.
The earlier blocks remain in force if the proposed theorem still needs
those data. Reuse the inspected primary statements and reopen only the
essential reducible metric hypotheses/proof cases. No new source approval,
lemma, local-degree implication or metric extension has been proved here.

Continuation test: continue only with a precise primary theorem or a
covered independently testable implication from the actual reducible
metric germ to local degree. Abandon this mechanism if available results
require a smooth target, assume the desired extension, or need the same
unavailable analytic data. Do not infer an orbifold normal form from
quadratic complex formality, geodesy on a puncture or tangent symmetry.

Mathlib full matching coverage is not checked; no absence or novelty
claim is made. This proposal is solely the next-review record.
