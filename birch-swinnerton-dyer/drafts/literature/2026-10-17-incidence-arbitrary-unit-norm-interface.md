# Arbitrary supplied-unit incidence norm — source comparison complete

TARGET: Specify and justify a complete incidence-norm certificate for an arbitrary supplied unit of L067's point algebra, including seventh-power-class compatibility over the entire line algebra.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the general-incidence and coordinate-norm assessments; compared L065 items 1–2, L066 items 1–5, L067's full power basis, L074's full projections and L075's matrix/norm scope; checked ATTEMPTS/034–036 and histories/270–275. Targeted searches and primary passages inspected are recorded below; no novelty inference from search.
SOURCE_EVIDENCE: Schaefer–Stoll author long version 2001-06-13, Section 2 pp.3–4, Section 3 p.5, Corollary 7.9 and Proposition 7.10 with its complete incidence proof and matrix paragraph pp.18–19; Stacks Section 31.18 tag 0BCX definition/unit observation and Lemma 31.18.6 tag 0BD2 complete proof; Mathlib Algebra.norm and Algebra.norm_eq_matrix_det/Algebra.norm_algebraMap_of_basis signatures inspected 2026-10-17. Reuse Bär Section 2.1 and determinant proof-case coverage from the coordinate-norm assessment.
COMPARISON: The unit norm, multiplicativity and induced seventh-power-class map are known; L065/L066 already specify their conditional descent use. No new interface lemma is warranted. Complete supplied-input arithmetic and independent replay on the audited entire incidence algebra remain necessary; two coordinate determinants do not perform that verification.
GAP: No arbitrary supplied unit/inverse, its full multiplication matrix/norm or exact seventh-power witness has been replayed. This assessment fixes the finite contract, not a power-class basis, arithmetic descent certificate or universal software-correctness theorem.
REASON: Missing unit/power-class coverage is resolved by primary sources and duplicate comparison. One bounded RESEARCH/REPRODUCTION implementation of the unchanged supplied-input certificate target is approved; import the general results and do not create a redundant conditional handoff lemma.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED concerned a broader input scope than the audited coordinate norms. Reuse ready determinant/incidence coverage and inspect only the missing unit, power-class and complete-input obligations.
SCOPE: Fixed conductor-389 curve at seven; arbitrary supplied rational representatives/inverses in L067's entire point algebra, L074's entire I/B and all B coordinates, with supplied seventh-power equality witnesses. Excludes finding all power classes, arbitrary power-membership decision, B/I fieldness, local arithmetic and Selmer membership.

## Relevance and discriminating test

The main gap remains rank E(Q)=m(E) for arbitrary E/Q with m(E)>=2.
The intermediate target is a complete supplied-unit norm certificate,
potentially useful for imposing L066's necessary incidence constraint on
later complete global generators. No such generators are supplied.
Continue only if complete input/inverse, matrix and norm evidence passes
independent replay within the limits below. Failure parks this finite
implementation, not full descent. An exact norm without a root witness or
faithful quotient evidence is not a successful seventh-power test.

## Primary statements, hypotheses and proof cases

Schaefer–Stoll, *How to do a p-descent on an elliptic curve*, Trans. AMS
356 (2004), 1209–1231, DOI 10.1090/S0002-9947-03-03366-X, is used with
numbering exclusively from the
[author long version dated 13 June 2001](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf#page=19).
Section 2 assumes an odd prime over a number field; Section 3 allows
products of separable fields. Corollary 7.9 requires scalar and incidence
kernels, with A(S,p) for unramifiedness. Proposition 7.10 already induces
the unit-class map by point pullback and incidence norm. Its proof uses
the full fiber product; its matrix paragraph gives det(h(M_t)) for any
polynomial in a point-algebra generator. These statements and paragraphs
were inspected; reuse earlier cohomological proof-case coverage. No p=3
slope formula or maximal residual Galois-image hypothesis is imported.

K=Q,p=7 meets that setup. L067 supplies the whole A and short-coordinate
generator t=Y with its invertible full power-basis transport. L074 supplies
the exact incidence projection and basis (1,X,...,X^6) over all of B.
Here B is the line algebra, not L070's direction field or L067's separately
named two-coordinate presentation. Keep L072's inverse ordinary-functional
indexing and Cartier convention. No fieldness of B or I is needed.

[Stacks Section 31.18, tag 0BCX](https://stacks.math.columbia.edu/tag/0BCX)
defines a multiplicative norm and explicitly observes that it sends units
to units. [Lemma 31.18.6, tag 0BD2](https://stacks.math.columbia.edu/tag/0BD2)
constructs it for finite locally free maps of constant positive degree by
the multiplication determinant, independently of basis and compatibly
with arbitrary base change. The definition/unit passage and full proof
were read. The degree is seven on the whole Spec(B), by L074.

The imported map is nu:A^*->B^*, nu(a)=N_(I/B)(i(a)). Its representative
convention on seventh-power classes is nu(a b^7)=nu(a)nu(b)^7 for units
a,b; Proposition 7.10 supplies the induced A^*/A^{*7}->B^*/B^{*7} map.
This is not a rational-linear norm A->B. Only the induced exponent-seven
group map is F_7-linear. No new norm, unit or quotient theorem is proved
here. Reuse the coordinate-norm construction/audit assessments for the
complete Laplace and Bär Faddeev–LeVerrier proof cases over commutative
Q-algebras; no determinant reproof or source refresh is needed.

## Duplicates, failures and searches

L065 item 2 already requires exact power-class kernel checks or an actual
cohomology preimage. L066 item 3 already permits this constraint in faithful
quotient coordinates on every global generator. Neither supplies arithmetic
instances. Repeating those implications would repeat ATTEMPTS/034's stopped
interface route, so import them without a new abstract interface lemma.
The remaining nonredundant obligation is verification of supplied units,
their full multiplication matrices, actual norms and any asserted roots.

L075's audited mu_Y is usable in the source's generator-polynomial rule;
its two determinant values cannot be combined linearly to obtain general
norms. Independent reconstruction must use L074's full point pullback,
not assume correctness of a polynomial-evaluation implementation.
ATTEMPTS/035–036 stop different translation-column presentations, which
are not inputs or resumed here. Source coverage is ready; the remaining
task is concrete arithmetic verification, not another scope audit.

Queries on 2026-10-17 included
`site.stacks.math.columbia.edu norm finite locally free multiplicative units determinant`
and `"Schaefer" "Stoll" "norm" "Proposition 7.10"`.
Followed the primary Stacks definition/proof and author's unit-class/matrix
statement; reuse the broader terminology, stronger-result and software
searches in `2026-10-16-conductor389-seven-incidence-maps.md` and
`2026-10-17-incidence-coordinate-norm-certificate.md`. Other search leads
were not used as theorem evidence. No originality/absence claim is made.

## Complete finite contract for one bounded implementation

These are obligations for the known construction, not new verified data
or a proposed general seventh-power decision algorithm.

1. Accept exact length-48 rational vectors a,a_inv in L067's full
   (1,t,...,t^47) basis. Check a*a_inv=1 in the entire algebra, with all
   basis transports and full pullback to I. Reject zero, malformed shape,
   missing coordinates and noninverses before determinant work. Sampled
   embeddings and an input's nonzero label do not certify a unit.
2. Retain all 2352 rational coefficients of the 7-by-7 B multiplication
   matrix of i(a). A producer may evaluate the input polynomial in mu_Y;
   an independent verifier reconstructs its seven columns by multiplying
   the transported i(a) with every basis element in L074. Retain all 48
   B coordinates, including both V components and all zeros. Compute and
   compare the full 48-coordinate determinant by the two known methods,
   with complete minors/recurrence evidence. Terminal zero alone is
   insufficient. No division by a possibly nonunit B entry is permitted.
3. For a claimed change of representative, accept complete b,b_inv,a_prime
   and check b*b_inv=1 and a_prime=a*b^7 in A. The imported theorem gives
   compatibility. If their norms are saved, certify each as in item 2
   and check their compatibility identity on all B coordinates. Finite
   controls test implementation only; the universal law is imported.
4. A positive incidence-kernel claim additionally needs full beta,beta_inv
   in B with beta*beta_inv=1 and beta^7=nu(a), checked coefficientwise,
   or independently certified faithful B^*/B^{*7} coordinates. A norm
   alone needs no beta. Failure of a proposed beta rejects that witness
   only, not power membership; absence of beta proves no nonidentity
   claim. Certified nonmembership requires separate quotient evidence
   outside this implementation's scope. B/I fieldness cannot replace it.
5. For eventual L066 use, instantiate the contract on every independently
   complete global generator and express the results in faithful target
   quotient coordinates. Selected controls supply no global power-class
   basis, constraint matrix, containment or upper-dimension certificate.

One implementation attempt may exercise this parameterized contract on
the mixed input a=X+Y and representative-change input b=1+Y, including
a*b^7. These are proposed controls, not claimed arithmetic S-units or
independent power classes. Construct and verify their inverses and norms
in that later attempt; none is computed here. Include scalar 2 with norm
convention 2^7, and a positive root-witness control only where the root is
actually supplied (the scalar case suffices). Do not claim a mixed input's
unknown norm class is trivial. Corrupt one inverse, one odd-V matrix
coefficient and one norm coefficient as explicitly limited named-condition
rejections, preserving originals.

Before execution save design, unfinished reasoning, complete input paths
and original hashes. Use a fresh scripts/seven-torsion/ directory with
one producer stage <=180 seconds and one independent verifier stage
<=180 seconds, each under an external <=181-second watchdog; combined
fresh output <=134217728 bytes including reports/logs. Stages include all
chosen controls and their evidence: no retry, cap extension or retrospective
subdivision. Reuse accepted audits, preserve their complete inventoried
originals and stopped drafts, and stop at the first cap/failed identity.
Save full certificates; print only actual/required bounds, failures and
paths. Generic-input code with finite tests is not a universal correctness
theorem. Add a canonical lemma only for nonredundant complete finite
evidence; otherwise retain the implementation result in drafts.

## Mathlib and remaining qualifications

[Algebra.norm](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Norm/Defs.html#Algebra.norm)
is explicitly a monoid homomorphism for a ring algebra over a commutative
ring. The inspected `Algebra.norm_eq_matrix_det` accepts a finite basis,
and `Algebra.norm_algebraMap_of_basis` fixes the scalar power. These are
generic support, not verification of the torsion/incidence identifications
or code. The domain hypotheses in `Norm.Basic` zero/nonzero criteria may
not be assumed for B or I. Full matching Mathlib coverage for this finite
certificate and power-class handoff was not checked; no absence claim.

Essential inputs are L067 and audited L074 with L070/L071/L072/L073 and
complete incidence-269/audit-271 evidence, plus audited L075 and complete
coordinate-norm-273/audit-275 evidence. No cross-notebook input, L069 or
stopped columns are used. Actual arithmetic units, global S-unit/class
completeness, descent functions, local identifications/bounds, Selmer
containment, other L026 premises, successful localization, rational
membership, divisible-Sha removal and arbitrary-curve comparison stay open.
This review closes source coverage and clarifies the necessary arithmetic
verification without changing a proof argument, lemma or mathematical script.
