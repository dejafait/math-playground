# Ordinary nonspin charge-minus-one factor — source comparison

TARGET: Assess exact-h locally free slope-stable existence for rank two with determinant k and c_2=-1, as the missing ordinary factor in L087's t=1 witness.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the minimal-factor, rank-five seed and real-stratum assessments; searched K3 primitive rank-two locally-free existence and the exact negative charge; checked local L080/L087 and ATTEMPTS/056 for overlap; retrieved primary nonemptiness, freeness exceptions, slope equality boundary and real chamber statements.
SOURCE_EVIDENCE: Yoshioka math/9907001v2 (7 February 2000), Theorem 0.1 and Section 0.2 p. 2, Proposition 0.5 and Section 1.1 p. 4, Lemma 1.5 and proof p. 5, Sections 3.1.3/3.2/3.3 pp. 15–16; O'Grady Algebraic Geometry 9 (2022), Definitions 1.1 and 3.1–3.3, Propositions 3.4/3.8/3.10 and relevant proofs pp. 2,8–10; Greb–Toma Algebraic Geometry 4 (2017), Theorem 6.6 and proof, Section 6.3.3 pp. 73–74.
COMPARISON: Primary results cover general integral-polarization sheaf existence and the locally-free exception list, together with real-stratum stability tools; their application to the exact h and changed charge still needs a separate mathematical specialization. L080's spherical defect-removal conclusion cannot be imported at this charge.
GAP: Check generality and strict slope stability, exclude the primitive freeness exceptions and obtain one simultaneously slope-stable locally-free point, then carry its stability to the identical real h and identify its determinant integrally.
REASON: Essential coverage for this actual-factor prerequisite is now adequate; import the general theorems and justify the changed numerical/chamber application without reproving them or assuming K_4/F existence.
SCOPE: L052's marked projective K3 S, unchanged real ample h, primitive k with k^2=-14 and NS(S) intersect h-perp=Zk; ordinary rank-two determinant O_S(k), c_2=-eta and strict h-slope stability. Only the individual factor existence specialization is covered; tensor stability, acyclicity, image identification, common kernel and transport are excluded.

LITERATURE_REASON: The charge-minus-one actual locally-free existence target lies outside the earlier spherical charge-minus-two seed and the audited half-adjoint necessary-constraint coverage.

## Gap, target and decision test

The universal primitive rational Hodge-class gap is unchanged. Locally,
L079's common kernel with the full negative tensor is unconstructed.
The intermediate target is the missing ordinary factor of L087's
Euler-number-one witness. L080 already supplies the other factor.
An actual second factor could make a later normalized tensor test
meaningful; it would not identify an actual image or construct F.

Continue with one theorem-application attempt if generality, freeness
and exact-real stability can all be checked under SCOPE. Stop at the
first failed hypothesis or unresolved bridge. A failure here would
park this ordinary witness, not the twisted alternatives, other
L079 branches or the Hodge conjecture. No existence conclusion is
established in this literature-only comparison.

## Inspected primary inputs

[Yoshioka, *Irreducibility of moduli spaces of vector bundles on K3
surfaces*, math/9907001v2](https://arxiv.org/pdf/math/9907001v2),
7 February 2000: Theorem 0.1 requires primitive positive rank,
algebraic first class and general ample H. It gives nonemptiness
for Mukai square at least -2 and irreducibility. Section 0.2's
condition (♮) requires equality slopes to imply equality of
normalized first classes. Lemma 1.5 includes the non-strict bound
v^2/2 >= ell(v)^2, where ell(v)=gcd(rank,c_1); its inspected proof
covers rank/ell>1. Proposition 0.5 retains Theorem 0.1's hypotheses.
Its exception list is clarified in Section 3.3: rank one;
v=(rank v_0)v_0-eta; or v=ell v_0-(ell+1)eta with rank v_0=1,
where v_0 is spherical. Section 3.1.3's statements and rank-one
hull proof, and Section 3.2's equality case, were read. Line-bundle
twists must be retained when comparing exceptions. Two nonempty
open loci require a common point; primitive irreducibility is
available, unlike in the earlier nonprimitive charge-four problem.

The canonical L087 witness already records discriminant ten,
Mukai square two and first class k; L080 records k's primitivity
and nondivisibility by two. These are comparison inputs, not
existence evidence. The later proof should verify the vector,
ell(v), exception exclusions and simultaneous loci explicitly.
It may instead show every Gieseker-stable point at the chosen H
is slope-stable after checking (♮) and the rank-one first-class
condition. No new defect-stratum calculation is required by this
source comparison. L080's argument that every defect is impossible
is not approved for reuse with the changed square.

[O'Grady, *Modular sheaves on hyperkähler varieties*, Algebraic
Geometry 9 (2022), 1–38](https://content.algebraicgeometry.nl/2022-1/2022-1-001.pdf):
Definition 1.1 and Definitions 3.1–3.3 apply to surface sheaves;
a-walls are orthogonal to integral classes xi with -a<=xi^2<0,
and their union is locally finite and closed in the real ample
cone. For rank two on a K3, a is the discriminant. Proposition
3.10 bounds a saturated equality-slope class and retains its
zero-class exception. Read its Hodge-index/discriminant/Bogomolov
proof and the bounded crossing and chamber proof in Propositions
3.8/3.4. The numbered stability statements use ample divisors;
real endpoint stability will use the following separate input.
The changed wall parameter must be checked against L052's actual
perpendicular lattice, not L080's old six-wall bound.

[Greb–Toma, *Compact moduli spaces for slope-semistable sheaves*,
Algebraic Geometry 4 (2017), 40–78](https://content.algebraicgeometry.nl/2017-1/2017-1-003.pdf#page=34):
Theorem 6.6 provides finitely many rational linear walls on compact
subsets of P(S) for fixed full topological invariants. Within one
chamber it preserves stability and semistability uniformly for all
torsion-free sheaves. On a surface P(S)=Amp(S). Read the complete
theorem proof and Section 6.3.3's explicit inclusion of lower-
dimensional strata. The proposed application must choose an
integral ray in h's actual relative stratum for these changed
invariants; arbitrary nearby H is insufficient. Artificial walls
through h need not be excluded. This reuses the assessed real-
stratum method, not L080's different invariant-specific conclusion.

## Search, overlap and qualifications

Queries: `Yoshioka irreducibility moduli spaces vector bundles K3
surfaces 9907001 locally free Proposition 0.5`; `O Grady Modular
sheaves hyperkahler varieties rank two walls discriminant`;
`K3 locally free primitive 2 Yoshioka Proposition 0.5`;
`"K3" "rank two" "c_2=-1" stable bundle` and the `c2=-1` variant.
The direct primary PDFs above were accessible as complete line text.
A Greb–Toma screenshot fetch timed out; no screenshot verification
is claimed or needed for the readable theorem/proof text.

Search hits for O'Grady's *Moduli of sheaves and the Chow group of
K3 surfaces*, Yoshioka's twisted-moduli paper and real bundles on
other K3 examples were not inspected as additional matching inputs.
No novelty or nonexistence is inferred from the exact-charge search.
The prior minimal-factor existence/audit and rank-five assessments
remain valid in their scopes; their general sources are reused.

Targeted local searches/read ranges found no canonical construction
of this factor. L080 is the different spherical seed; L087 and
ATTEMPTS/056 stop the necessary half-adjoint index filter. Their
ordinary numerical witnesses are retained, and construction of an
individual factor is a different independently testable target.
No index filter is reopened. All unfinished work is preserved.

Full matching and supporting Mathlib coverage: not checked; unknown
availability is not absence. A later successful specialization
would be REPRODUCTION, not a claim of new mathematics beyond the
inspected sources. No lemma, mathematical script, DAG edge or
PROOF.md argument is changed. This ready changed assessment is
subject to the supervisor's separate next-turn approval before
mathematical invocation; no additional discovery is presently needed.
