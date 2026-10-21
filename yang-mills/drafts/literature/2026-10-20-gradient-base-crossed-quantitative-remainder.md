# Gradient-base crossed quantitative remainder — source comparison

TARGET: Establish an O(N^(5/2) log(eN)^2) remainder for L104's complete gradient-base crossed pair R_gx after subtracting a^(-3)K_(i,G), for both actual probes.
CHECKED: 2026-10-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Read L102--L104's complete relevant proofs, gradient-base histories 128--130 and ATTEMPTS/028,029,032; searched exact local TARGET/COVERED_TARGET fields and the seven external queries below; reused ready reverse, left-crossed and complete-coefficient assessments. No inspected theorem supplies the matching remainder; this is no novelty claim.
SOURCE_EVIDENCE: Reused primary comparisons in the ready assessments; reinspected Benzi--Simoncini 1501.07376v1 Theorems 4.1--4.4 and section 5, Ginovyan--Sahakyan 1405.3568v1 Theorems 1--3 and Theorem 2's proof; inspected Klein--Reiss--Rosenberger 2510.11193v1 Hypothesis 1.1, Theorem 3.6 and its complete proof, (3.39)--(3.50).
COMPARISON: L102 and L103(6) already control the removed terms at O(N^(5/2)); L103(7) gives a uniform two-inverse error, while L104 only proves successive fixed-mass/degree limits. Inspected decay and trace theorems support a local test but do not cover this cumulative, ordered pinned trace at the requested rate.
GAP: Quantify the exact L103(5) cumulative trace against precisely L104(6), with compatible inverse, boundary, ordered coefficient, raw-sample and full heat errors; the endpoint and upper tail remain. These are unproved specialization obligations, not inaccessible essential sources.
REASON: Target-specific comparison now supports one later bounded attempt at exactly TARGET. EXPLORE approves research scope only, with no rate, parameter schedule or lemma proved here; separate supervisor approval is required before use of this newly ready assessment.
LITERATURE_REASON: The target is the gradient-base cumulative R_gx/G_R component, distinct from the previously assessed co-closed-base R_R and R_L; their ready assessments lack this exact ordered cumulative comparison.
SCOPE: Same SU(2) relative all-face cube, lower-rooted direction-1 forest, admitted even N, a=8/N, tau=1/16, stored coordinates, bare-first order and actual probes 3,6; complete source/end rows, constant indices and heat labels; no outside factor 3.

## Completed review

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. It completes a
new bounded source comparison, without establishing a mathematical rate
or progress beyond the sources checked. No lemma, mathematical script,
DAG or proof assembly changes. The current official target/version is
already recorded in `foundations/01-target-and-scope.md`; this step
does not select a new construction route. The interacting reflected
error <=c_box/2, ultraviolet axioms and infrared finite positive mass
remain the main gaps. This component could support quantitative L011
assembly, with the independent components and interacting estimate open.

### Exact existing reduction and uncovered comparison

L103(2),(5), in its own notation, specify the existing finite trace

    X_(k,t)=sum_(s>t) Xi_(k,s)+Xi_(k,t)/2,
    P_(i,N)=a^-1 sum_(k,l)c_(i;kl,a) sum_t t
      Tr[G X_(k,t) G W_t^T D_T^T Zeta_l(t) T].

This is a quotation of the mathematical input, not a new reduction.
In particular W is at t; X has an upper cumulative coefficient and is
not compact merely because W contains the compact displacement. The
actual raw b,q paths, both inverses, endpoint/clover filters and their
order remain. L104(6), including its physical lower-distance factor,
is the exact coefficient to subtract; L140's later scalar contraction
is not a replacement finite trace or a remainder theorem.

| Existing passage | Available input | Still needed for TARGET |
| --- | --- | --- |
| L102(2), proof sections 1--4; L103(6) | R_gx-P_(i,N)=O(N^(5/2)), including the O(N^2) exterior-circulation error | No reproof of those removed terms; retain their qualifications. |
| L103(7),(16)--(20) | Two-inverse error <=C_i N^3 epsilon^(1/4), for 0<epsilon<=1 and N sqrt(epsilon)>=1; full pinned scalar shells | Quantitative subsequent estimates compatible with this uniform finite error. |
| L104(7)--(12), proof section 1 | Exact cumulative coefficient, moving-cut half and omitted upper endpoint; fixed-label smooth convergence and global polynomial mode bound | A uniform quantitative coefficient comparison in the actual trace, including the upper axial tail and heat summability. |
| L104(13)--(15), proof sections 2--3 | Exact normalization; fixed-mass polynomial approximation; fixed-degree pinned-walk localization, freezing, quadrature and full heat convergence | Mass/degree dependence, all boundary rows and raw coefficient/heat errors at finite N. |
| L104(16)--(17), proof section 4 | Absolutely convergent symbol and successive mass removal | A finite-N remainder, not a varying mass substituted into the qualitative limit. |

L104's polynomial proof genuinely handles pinned collars and the
cumulative coefficient at fixed parameters. It does not state a
quantitative bound for growing polynomial range or vanishing mass.
The bound on its frozen integrand and dominated convergence alone
do not fill this gap. These are scope comparisons, with no new
estimate or parameter choice derived in this literature turn.

### Primary sources and applicability

Reuse `2026-10-19-left-crossed-quantitative-remainder.md` and
`2026-10-19-reverse-crossed-quantitative-remainder.md`; their conclusions
about other traces are not imported. Benzi--Simoncini,
[*Decay bounds for functions of matrices with banded or Kronecker structure*](https://arxiv.org/pdf/1501.07376v1),
v1, 29 January 2015, printed pp. 6--8 and 11--12: Theorems 4.1--4.2
use Hermitian positive semidefinite matrices with bounded spectrum;
polynomial propagation yields two distance/time regimes. Theorem 4.4
requires positive definiteness and a Laplace--Stieltjes function,
retaining the smallest eigenvalue in three time ranges. Section 5
uses graph distance and permits dimension-uniform finite sections
when the function has no nearby spectral singularity. Reinspection
included the finite-propagation proof and both regimes. Applied to
the scalar pinned transverse Laplacian with positive mass, these are
supporting localization tools. They give neither uniform mass removal
nor the complete ordered cumulative trace bound. A three-dimensional
graph must use graph distance, not a dimension-independent bandwidth
from lexicographic indexing. No general theorem needs reproof.

Reuse the reverse assessment's scalar comparison: Lawler--Limic,
[*Random Walk: A Modern Introduction*](https://www.math.uchicago.edu/~lawler/srwbook.pdf),
Cambridge, 2010, Theorem 4.3.1, Corollary 4.3.3, pp. 81--84,
and Theorem 6.3.8(a), p. 131, with its recorded harmonic-measure
proof. Its transient symmetric finite-range scalar walk and interior
harmonic-difference hypotheses support Green/energy estimates.
The local scalar normalization is Delta=6(I-P_walk). This does not
identify the ordered product with a scalar Green diagonal or impose
scalar Dirichlet conditions on every relative link component. Only
this assessed source scope is reused; no new vector specialization
or boundary estimate is established here.

Ginovyan--Sahakyan,
[*On the trace approximations of products of Toeplitz matrices*](https://arxiv.org/pdf/1405.3568v1),
v1, 14 May 2014, printed pp. 5--6, Theorems 1--3, and pp. 8--9,
Theorem 2's proof: real symmetric scalar circle symbols in
Lip(p,gamma), Lip(q,gamma), 0<gamma<=1 and 1/p+1/q<=1/2 yield
O(n^(-gamma+zeta)) normalized error for every zeta>0 for the squared
two-factor Toeplitz product. The proof uses a four-symbol correlation,
Holder continuity and Dirichlet-kernel bounds. The singular-symbol
case imposes alpha_1+alpha_2<1/2 and derivative bounds. This is
supporting comparison only: there is no established reduction of the
three-dimensional, position-dependent, cumulative pinned product to
these hypotheses. Neither its scalar rate nor the singular-symbol
case supplies TARGET by citation.

A new relevant lead was checked rather than inferred from its abstract:
Klein--Reiss--Rosenberger,
[*Weyl asymptotics for pseudodifferential operators in a discrete setting*](https://arxiv.org/pdf/2510.11193v1),
v1, 13 October 2025 (text dated October 14), Hypothesis 1.1, printed
p. 3, and Theorem 3.6 with complete proof, pp. 15--16,
(3.39)--(3.50). Hypothesis 1.1 assumes a real smooth symbol in
S^0(m,epsilon_0), m>=1, ellipticity of a+i, a uniform essential
lower bound above sup J for a bounded open J, and a full symbol
expansion. For f in C_c^infinity(J), Theorem 3.6 gives trace-class
functional calculus and a trace expansion with normalized O(epsilon)
error controlled by finitely many derivatives. Its proof localizes
compact symbol support and uses trace-norm remainder estimates.
This is a stronger smooth whole-lattice trace framework, but TARGET
has not been represented as f(P_epsilon) under those hypotheses.
Pinned-boundary transfer, the cumulative insertion and any small-mass
derivative losses still need justification. The theorem is not imported;
no uniform small-mass claim follows. Here its epsilon is lattice
spacing, distinct from L103's inverse mass.

Reuse `2026-10-17-complete-coefficient-quantitative-remainder.md` for
Adams--Lee, [0709.0781v3](https://arxiv.org/pdf/0709.0781v3),
section II (7)--(15), Appendix A (A1),(A11)--(A18). Its negative
lattice-degree, infrared-finite translation-invariant integral result
has no established identification with this pinned trace. The ready
other/other assessment's flowed Ward/renormalization comparisons also
remain supporting context, not an isolated bare-component rate.
There is no reason to reprove these frameworks. No inaccessible source
is essential to the proposed bounded local test. Full matching and
supporting Mathlib coverage for TARGET are **not checked**; unknown
availability is not absence.

### Search, duplicates and continuation test

External queries on 2026-10-20:

- `"trace" "gradient" "cumulative" "lattice" "remainder" resolvent`
- `"locally Toeplitz" "trace" "error" singular symbol`
- `"semiclassical" "discrete" "trace" "resolvent" variable coefficients remainder`
- `"On the trace approximations of products of Toeplitz matrices"`
- `"gradient-base" "crossed" trace`
- `"Weyl asymptotics for pseudodifferential operators in a discrete setting"`
- `"lattice" "Green" "trace asymptotics" "boundary"`

The inspected primary comparisons are above. Generalized locally
Toeplitz abstracts, Chanzy's two-dimensional scalar rectangle paper
and other search hits were not read at theorem level and provide no
coverage. No matching or stronger applicable theorem was inspected;
a bounded search does not establish novelty or global absence.

Notebook-scoped exact TARGET/COVERED_TARGET searches found only this
registration for R_gx/L104. The gradient histories 128--130 end with
the qualitative limit. Later reverse and left-crossed quantitative
assessments concern distinct orders; they are reusable tool coverage,
not duplicate gradient-base rates. Preserve ATTEMPTS/028 (reverse
operator norm), 029 (termwise projection commutation) and 032
(separate first absolute moments). Their mechanisms were read in
full. They do not prove signed growth, defeat joint energy/kernel
estimates or ban the current target. No exhausted approach is reopened.

After separate approval, a single bounded attempt at exactly TARGET
may test an ordered joint Green/energy comparison of L103(5) with
L104(6), importing the existing removed-term and inverse errors.
The discriminating result is a uniform finite bound for the retained
trace within C_i N^(5/2)log(eN)^2, or a useful partial comparison with
one explicit remaining error. Every mass, degree, source count and
mode polynomial must be exposed before any mesh-dependent choice.
Abandon a particular shortcut if it needs a stopped projection/moment
premise, loses the cumulative endpoint or upper tail, or leaves an
uncontrolled mass-dependent constant. An insufficient upper bound
is not a lower bound or a disproof of TARGET.

Essential continuation inputs are L102 L103 L104, with L028 L080
L087 L088 L097 for signed layer, actual exterior, relative and
heat conventions. Any optional quantitative modal input must match
the raw traversal slots separately and retain its audit qualification;
L222's endpoint-averaged diagnostic conclusion is not transferred.
Unresolved assumptions are the quantitative joint kernel/boundary,
coefficient and heat comparisons and their compatibility with inverse
removal. None is approved as true here. There is no outside factor 3,
transpose transfer from R_R/R_L, or change in probe normalization.
Mathematical exploration usage remains zero of three; this is a
literature comparison, not a calculation attempt.

## Original registration — preserved scope record

The following registration predates the completed review above. Its
source-comparison request is discharged, subject to separate supervisor
approval of the newly ready assessment. Its warnings remain relevant.

The main gap remains the interacting reflected error <=c_box/2,
ultraviolet construction with the required axioms, and infrared
control with finite positive mass. The proposed intermediate rate
could contribute one component to quantitative L011 assembly; neither
that assembly nor the independent component rates are assumed.

Essential input IDs are L102 L103 L104; L080 L088 L097 specify the
imported actual exterior and relative conventions. Preserve SU(2),
the relative all-face cube, lower-rooted direction-1 forest, admitted
even N, a=8/N, tau=1/16, stored coordinates, bare-first order and
probes 3,6. Retain every source/end row, allowed constant index,
actual coefficient level and full heat label. The target concerns
the gradient-base R_gx and G_R, not the co-closed-base R_R.
There is no outside factor 3.

The next turn is literature-only for exactly TARGET. Read L103's
exact reduction and L104's proof cases before selecting a quantitative
specialization. Reuse existing scalar resolvent, pinned spectral and
finite trace assessments where their hypotheses really match; record
essential missing coverage rather than assuming the reverse trace's
assessment covers this cumulative signed insertion. Check duplicate
rates and relevant recorded failures. In particular fixed-mass
qualitative convergence does not justify a varying-mass schedule,
and neither projection commutation nor factorwise absolute moments
may be assumed from smooth coefficients.

The later discriminating mathematical test, only after coverage is
ready, is an estimate of

    |R_gx(i,N)-a^(-3)K_(i,G)| <= C_i N^(5/2)log(eN)^2

against precisely L104(6), with constant independent of N. A controlled
partial comparison with a concrete remaining error may justify
continuation. An uncontrolled mass-dependent localization constant or
a lost cumulative endpoint must be identified rather than hidden;
failure of an upper-bound method is not signed growth. No derivation,
new parameter schedule or approval of that estimate is made here.
The existing reductions, coefficient convergence and shell/energy
estimates remain unresolved imports for the future specialization.
Full matching and supporting Mathlib coverage is not checked.
