# Positive-real angular separator — completed bounded source comparison

TARGET: Test whether L666's complete product admits functions psi_n in normalized L2(T) with A_n(x)=1, Re A_n(x+i*y)>=0 for all |y|<=9/20 and ||psi_n||_2<=exp(n/100)*n^C for absolute C and onset, where n=12q+3 and A_n(a)=mean_u conjugate(psi_n(u))*W_a(u), via a positive-real analytic representation or a rigorous obstruction to that representation.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 47 searched Herglotz/Caratheodory positive-real representations, Cauchy-transform isometries and quantitative operator-range factorization; queries, primary reading and local duplicate checks are recorded below. No evaluated bound for this full product was identified; absence from this bounded search is not novelty evidence.
SOURCE_EVIDENCE: Bal--Martin--Naderi, Canadian J. Math. 77 (2025), 1570--1610, Section 2.1 and Lemmas 3.1--3.2 with proofs, pp.1574,1583--1584; Douglas, Proc. AMS 17 (1966), Theorem 1 and complete proof, pp.413--414, and distinct-domain extension p.415. The disk Herglotz formula permits finite positive measures and an imaginary constant; the Cauchy and Douglas norm statements require their own range hypotheses, not verified for W_a.
COMPARISON: Positive-real functions have a measure representation, while a controlled angular preimage requires a separate quantitative range estimate. Neither inspected theorem identifies the full W_a transform with its Cauchy-transform model or evaluates its inverse cost. The strengthened continuum target remains undecided, distinct from the recorded finite polar, scalar-mean and continued-value stops.
GAP: For the exact full W_a, identify an attainable normalized action nonnegative throughout the vertical interval and pay its complete angular L2 preimage norm at rate 1/100, or prove a stated obstruction. Parameter analyticity, action-range membership, sign orientation and uniform quantitative constants must be justified; no positive-real/action-range identity is assumed.
REASON: Essential representation and inverse-range source comparison is now sufficient for one bounded family-specific attempt, not a general new representation theorem. EXPLORE does not establish existence, nonexistence or the rate. This changed ready assessment requires separate approval before research; no essential source is blocked.
LITERATURE_REASON: Specific new lead: positive-real analytic representation of the pole-parameter action, with a strengthened continuum positivity constraint and a quantitative inverse-action cost. The prior assessment did not inspect this essential representation theory; further generic cone browsing is unnecessary.
SCOPE: Exactly TARGET for the full product and full ordinate interval below; one action-first positive-real construction and exact angular inverse-cost test, or a rigorous obstruction to that construction. Standard Herglotz and Douglas statements may be cited within checked hypotheses. No finite Fourier repair replay, scalar-mean calculation, assumed kernel identification, generic frame theorem, exponential surrogate or unproved norm equivalence is covered.

## Exact scope and intended use

Keep x=-5/4, U=121/64, t_j=j/n, n=12q+3, q>=1, and

    W_a(u)=product_(0<=j<n)
       [(x-t_j*u)/(a-t_j*u)] [(U*u-t_j*a)/(U*u-t_j*x)], |u|=1.

The j=0 factor is x/a; the denominator angle is retained. All means
and L2 norms are normalized. The test function psi_n may depend on n,
but not on y or on a displacement vector. The interval |y|<=9/20
contains all L666 ordinates and the anchor. The power C and onset must
be absolute. No mass cap is imposed on the nonnegative coefficients;
the original residues remain one.

The intended standard real-Hilbert duality application is to the real
part of the pairing with 1+sum b_a W_a: action 1 on the anchor and
nonnegative actions on every allowed node would give a cone lower bound
after paying the test function's entire norm. This is motivation from
the already assessed cone framework, not an established construction.
The b_a=1 Jensen application, H bound, support and actual-Xi mixed
positivity remain separate. A failed strengthened separator need not
refute the cone estimate or rule out displacement-dependent separators.

## Original source questions from step 46 (resolved in the comparison below)

Search the exact analytic positive-real/Herglotz terminology and stronger
representation results; retrieve primary theorem hypotheses and the
proof cases needed for the contemplated function space. Determine the
actual analyticity domain, normalization, boundary assumptions, allowed
measures/polynomial parts and any norm formula. An arbitrary analytic
positive-real function need not be an angular action A_n. Do not silently
identify those two classes or replace W_a by an exponential.

Reuse the prior general-cone source comparison. Check L666's full product,
C645o's exact angular residues, L673's positive approximants and C673d
Section 5's signed-mean specialization. Compare, without redoing, the
recorded finite Fourier polar repair in
`ATTEMPTS/2026-11-02-positive-cone-polar-finite-screen-inconclusive.md`
and the entrywise-Gram stop. Positivity of a Gram matrix or a sampled
action is not positivity of this continuum action. Check the existing
point/deweighting stops if the representation reduces to their costly
continued evaluation at u=0. Preserve those stops and their hypotheses.

## Bounded continuation test after coverage

If a primary theorem supplies both representation and the required cost,
import it with exact applicability. Otherwise authorize only the precise
family-specific difference established by the comparison. The proposed
creative mechanism is to choose a positive-real action first and solve
for a small angular representer, rather than solve an unconstrained
finite Gram system and repair signs afterward. This is a proposal, not
a claim that such a function or a useful inverse exists.

The decisive evidence would be an exact representer with continuum sign
control and norm <=exp(n/100)*n^C, or an independently testable obstruction
to this representation at that cost. A known expensive representer,
qualitative existence or a finite optimizer is insufficient. Stop this
strengthened representation route if its unavoidable cost exceeds the
threshold; distinguish that stop from a counterexample to the cone bound.
Do not repeat the parked scalar-mean calculation. If the comparison does
not reveal a concrete bounded mechanism, decline this nomination and
record the exact blocker rather than label routine work creative.

Step 46 nominated this target without coverage. Step 47 supplies the
comparison below, without any new lemma, mathematical script or theorem.
Separate approval of this changed assessment remains required. Full
matching Mathlib coverage has not been checked.

## Completed comparison — 2 November 2026, step 47

### Primary representation and range statements actually inspected

J. Bal, R. T. W. Martin and F. Naderi, *A reproducing kernel approach
to Lebesgue decomposition*, Canadian Journal of Mathematics 77(5)
(2025), 1570--1610, DOI 10.4153/S0008414X24000488,
[published open-access version](https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/D6C85487ABC9D29C3F79208BEED1F1B9/S0008414X24000488a.pdf/reproducing_kernel_approach_to_lebesgue_decomposition.pdf).
Read Section 2.1, p.1574, and Section 3 through Lemma 3.2 and its
complete proof, pp.1583--1584. For holomorphic H on the disk with
Re H>=0, the named Herglotz theorem gives

    H(z)=i*Im H(0)+integral_T (zeta+z)/(zeta-z) dmu(zeta),

where mu is a unique finite positive regular Borel measure; no boundary
density or L2 assumption is required. Its mass is Re H(0). In contrast,
their Cauchy transform acts on H2(mu), the L2(mu) closure of analytic
polynomials, using the kernel (1-z*conjugate(zeta))^(-1). Lemmas 3.1--3.2
prove holomorphy and an isometry onto the transform's own RKHS. The
proof uses uniform difference quotients, density of kernel vectors,
injectivity on H2(mu), and the induced inner product. It does not assert
an isometry from normalized angular L2 to an independently specified
space of positive-real functions. The measure, kernel and norm must all
be matched before using that conclusion here.

R. G. Douglas, *On majorization, factorization, and range inclusion
of operators on Hilbert space*, Proceedings AMS 17(2) (1966), 413--415,
DOI 10.1090/S0002-9939-1966-0203464-1,
[scan of the original paper](https://galaxy.agh.edu.pl/~rudol/Operat/DouglasFactorizationLemma.pdf).
Read Theorem 1 and its entire proof on pp.413--414, and the first
added-in-proof extension on p.415. For bounded Hilbert-space operators
A,B, it equates ran A subset ran B, AA*<=lambda^2 BB* for some
lambda>=0, and A=BC with C bounded. The reduced solution has range
in closure(ran B*) and satisfies

    ||C||^2=inf{mu: AA*<=mu BB*}.

The proof constructs the solution perpendicular to ker B and uses the
closed graph theorem for range inclusion; the quantitative direction
extends B*f -> A*f continuously and takes its adjoint. Distinct domain
Hilbert spaces with a common codomain are explicitly allowed on p.415.
Unbounded Theorem 2 is not imported. Closure of a range is not a
substitute for the exact inclusion. The source provides a criterion,
not an estimate of the majorization constant for this product.

An ancillary proof check used *Introduction to Univalent Functions*,
spring 2015 notes, [Section 16, Theorem 16.2 and Corollary 16.3](https://integraali.com/courses/univalent_functions/unis2015.pdf),
printed pp.81--82 (PDF pages 81--82, counting from one). The title page
does not name an author; these notes are supporting exposition, not the
primary paper above. Read the full displayed proofs: normalized positive
harmonic functions yield probability measures by radial means, Helly
selection and the Poisson formula; Fourier uniqueness identifies the
measure; the holomorphic version restores the imaginary constant. This
checks the normalization and singular-measure case, and supplies no
inverse angular norm estimate. No general representation theorem is
reproved in this notebook.

### Exact comparison and the family-specific difference

The required positivity is on the closed segment x+i[-9/20,9/20].
Herglotz requires positivity on a two-dimensional open domain. Choosing
such an extension is a sufficient construction strategy, not an
equivalence with the segment constraint. A failure of the stronger
extension alone cannot exclude the original segment target.

L673 Section 2 already records the full product in the pole parameter
and its pole-free rectangle; L666 Section 2 records the angular poles.
Use those exact identities, including x/a and all denominator angles.
Any parameter change to the disk, its domain, normalization at x and
endpoint continuity must be proved in the subsequent attempt. Angular
meromorphy and parameter holomorphy concern different variables.
C645o's interior angular residues rule out simply identifying the
angular mean with a disk value. No new domain or transform identity
is proved by this source comparison.

The prospective inverse problem is to make a selected Herglotz action
belong to the actual W transform range with the required preimage cost.
A later use of Douglas must specify Hilbert domain/codomain spaces,
verify boundedness of the exact transform, and preserve conjugation:
psi -> mean conjugate(psi)*W is conjugate-linear in psi. One may change
variables to conjugate(psi) only with the resulting pairing conventions
written explicitly. Equality merely almost everywhere in an interval
L2 codomain does not by itself verify A(x)=1 or either endpoint;
the actual actions' continuity/analyticity must supply that bridge.

The Herglotz measure may be singular and lives on a parameter-domain
boundary. The requested psi lives in normalized angular Lebesgue L2.
The two spaces cannot be identified by notation. Even an exact
Cauchy-transform representation pays the source's induced RKHS norm,
which has not been compared to the angular preimage norm. An abstract
range criterion with an unknown constant is also insufficient. The
missing family-specific membership and quantitative inverse estimate
are the precise differences authorized for exploration; the sources
do not settle or obstruct them at exp(n/100)*n^C.

### Local duplicate and failure comparison

Reused the completed Moreau/NNLS comparison in
`2026-11-02-displaced-positive-cone-distance.md`; its general qualitative
cone theory need not be searched again. Read the relevant L666 and L673
hypotheses, conclusions and exact parameter formula, C645o Section 2,
and C673d Section 5. L673's audited rate-1/200 positive approximants
remain compatible with the requested rate-1/100 separation. No sharper
rate is inferred. C673d's five-size signed mean remains a diagnostic.

Compared the finite polar, entrywise-Gram and continued-zero-evaluation
failure records, plus L668's hypotheses and complete-cost conclusion.
The first has uncertified floating repairs and no asymptotic norm;
the second has an actual negative cross entry; the third pays the
ambient continued-evaluation loss across common poles. L668 concerns
a specified spatial inverse-weight interpolant, not every angular
action. These are scope comparisons, not fresh audits or global bans.
If an action-first candidate reduces to one of these very same
functionals and ambient costs, preserve that obstruction and do not
rename the calculation as a new mechanism.

### Search and access record

Queries executed on 2026-11-02 included:

- `Herglotz representation theorem positive real part disk theorem proof measure Hardy norm`
- `positive real rational function reproducing kernel Hilbert space Herglotz representation inverse operator range norm`
- `Herglotz representation theorem disk positive real functions proof site:arxiv.org pdf`
- `Douglas 1966 On majorization factorization range inclusion operators pdf`
- `"A reproducing kernel approach to Lebesgue decomposition" pdf`
- `"positive real" "Cauchy transform" "L2" representation norm inverse`
- `"Herglotz" "operator range" norm representation`
- `"positive real" rational product "angular" separator pole`
- `"Herglotz" "Blaschke" "positive" "range" representation L2`

The published Bal--Martin--Naderi paper, its arXiv:2312.01961v2
HTML counterpart, the original Douglas scan and the indicated notes
were accessible through the web tool. An attempted arXiv v3 URL was
absent and the AMS-hosted Douglas PDF returned 403; the accessible
original scan supplied Theorem 1 and all its proof cases. Local PDF
downloads failed at DNS resolution, so no downloaded source artifact
is claimed. These access failures do not block the inspected inputs.

Searches also surfaced nonstationary/operator-valued Herglotz theory,
Clark model-space realizations, multivariable representations and network
positive-real realization. Their essential theorems were not inspected
and are not approved inputs. None was needed for this scalar bounded
attempt. A future change requiring one of them needs its own review.
No matching full-product cost theorem was identified; this is not a
claim of exhaustive discovery or originality. Mathlib coverage of the
full target or these named theorems was not checked.

### Bounded mechanism and approval boundary

After separate approval, attempt the action-first construction once:
use the positive-measure parametrization to select an action, then
identify its exact full-product angular preimage before estimating its
norm. Finite positive atomic parameter measures may be tested as an
ansatz, with their boundary-pole compatibility checked; they are not
assumed to exhaust actions or yield admissible preimages. The bounded
test is exact representability with continuum sign control and the
complete rate-1/100 cost, or an explicit quantitative obstruction to
the specified representation. A finite fit or an unevaluated Douglas
constant is not a successful test.

Continue with this mechanism only after an exact attainable action and
a useful paid estimate, or a materially refined independently testable
range construction. If the attempt supplies neither, preserve its
partial reasoning and park that ansatz; do not repeat generic Herglotz
searches or the previous finite polar repair. A proved excess cost
for a specified ansatz stops that ansatz; only a proof covering every
admissible segment action could obstruct the full strengthened target.
Even that would not refute the displacement-dependent cone bound.
The b_a=1 application, H estimate, support and actual-Xi realization
remain separate unresolved steps. No mathematical construction,
specialization theorem, norm bound or RH candidate was established
in this literature-only step.
