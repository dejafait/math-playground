# Frozen even mode: source comparison850

LITERATURE_REASON: Nomination849 changes the stopped time-one defect test to the complete scalar form of one frozen vector. Its missing certification coverage requires this literature-only comparison.

## Checkpoint before completing the review

The supplied GOAL/PROGRESS/whole PROOF/DAG and assessment849 were used
directly. Targeted reads covered C759a(1),(5)-(6), Proof1/3/5, C759h
Proof1-2, C759i(1)-(2), the definition/assembly passages of script849,
working849 and stop849. Existing notebook changes are preserved. No
mathematical script was executed, coefficient evaluated, inequality
derived, or lemma changed. There is no cross-notebook input.

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
The intermediate diagnostic is the complete quotient of the one frozen
dyadic mode. Its possible use is to distinguish a real negative-form
candidate from an assembly artifact; sign/simplicity, parity and Xi
realization remain independent. Continue only with a complete rigorous
interval and positive denominator; a negative upper endpoint needs later
critical review, a positive lower endpoint rejects this indication, and
an interval crossing zero or unpaid contribution ends the fixed test.

The narrow duplicate search found already assessed numerical tools in
assessment655/comparison656, source-notes683 and source-notes686. Reuse
that general coverage rather than repeat its source-proof audits.
Johansson1802.07942v1 and the stable Arb2.23.0 callback contract have
also been retrieved. Newly inspected Zhu2608.24827v2 Sections10 and
11.3-11.4 explicitly distinguish proposal from full-form certification.
The source comparison and continuation decision are completed below.

## Source statements, hypotheses and inspected cases

**Complete form and its compact representation.** Reuse C759a's closed
realization and C759h Proof2's H1_0 membership for the prescribed basis.
The stored binary64 coefficients are to be read as exact dyadics in that
basis, not as certified spectral data. No norm has been computed here.

[Connes--Consani--Moscovici, *Zeta Spectral Triples*,
arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1),27November2025:
inspected Lemma3.1, (3.14)-(3.16), Proposition3.2 and its entire proof,
(3.19), and the derivation of (4.4). Proposition3.2 assumes smooth
functions on [0,L], lambda>1 and L=2log(lambda); its proof uses the
logarithmic Haar-measure isometry, translation invariance and convolution.
The passage to (4.4) integrates the exterior archimedean subtraction
exactly. Although (4.4) is printed for basis entries, (3.15) is the
general functional; the eventual specialization must justify its use on
the frozen piecewise polynomial through the existing closed domain.
Basis-entry tables alone do not perform that specialization. All pole
and prime terms keep their signs. No new compact identity is derived here.

[Suzuki, *Weil's quadratic form via the screw function*,
arXiv:2606.09096v2](https://arxiv.org/html/2606.09096v2), arXiv version
17August2026, internal date24August2026: inspected Sections2.3-2.4,
(2.3)-(2.7) and the complete-form comparison following (2.7). The
quadratic formulas apply to H1_0(-a,a). Read the cutoff/integration by
parts and endpoint cancellation in (2.4), the shifted terms in (2.5),
and the regularized digamma comparison. These support the existing
normalization; no small-window positivity or heuristic Section7 input
is used. They do not supply the frozen vector's integral or error bound.

**Certified integration, reused rather than reproved.** Ready assessment655,
completed comparison656, and source-notes683 cover Trefethen,
*Approximation Theory and Approximation Practice*(2013), Chapter19,
Theorem19.3/(19.8), PDFpp153-154, with full proof inspected there:
[primary book PDF](https://people.math.ethz.ch/~hiptmair/Seminars/RAP_22/TRE13.pdf).
Its hypotheses are bounded holomorphic continuation to the Bernstein
ellipse, rho>1, bound M. Its (n+1)-point rule, n>=1, has the stated
(64/15)M rho^(-2n)/(rho^2-1) error. Retain affine scaling, exact point
count and node/value rounding. It does not cover a panel crossing a
piece boundary or an unresolved endpoint. Source-notes686 separately
assesses Conrad's Taylor remainder Theorems1.1/1.2 and complete proofs
pp1-4, [primary PDF](https://kconrad.math.uconn.edu/blurbs/analysis/TaylorRemainder.pdf).
That supplies a standard remainder tool, not the missing origin bound.
There is no reason to reprove either general theorem.

[Johansson, *Numerical integration in arbitrary-precision ball arithmetic*,
arXiv:1802.07942v1](https://arxiv.org/html/1802.07942v1),22February2018:
reused683 and reread Sections2/2.1, all algorithm branches, and3.2.
It requires enclosing evaluation on complex boxes and holomorphy checks.
Direct interval bounds, certified Gaussian bounds and bisection preserve
inclusion. Evaluation limits may return a wide enclosure. Requested
tolerances do not bound total cancellation error. Improper integrals
require separately justified truncations. No convergence rate or
execution time for this vector is imported.

The [Arb2.23.0 acb_calc contract](https://arblib.org/acb_calc.html),
callback and Integration sections, was read: finite endpoints, bounded
path integrand, rejection of nonholomorphic boxes, caller-selected
precision, and cumulative error qualifications. The existing683
arithmetic/node coverage remains usable. Current FLINT3.7.0-dev docs
advertise a revision partly generated by an LLM; use the stable contract
and primary paper, not a new constant inferred from that revision.

## Stronger results, overlap and reason to reproduce

[Zhu, *Weil positivity in compact windows*,
arXiv:2608.24827v2](https://arxiv.org/html/2608.24827v2),2September2026:
inspected Theorem1.2 and Sections10,11.1,11.3-11.4, including
Remark11.5/11.7 and (17). The source already describes independent
interval re-evaluation of an arbitrary proposed vector on the complete
geometric side, and records false float64 negative indications and
tail-model failures. Its explicit calculations use trigonometric modes;
they do not enclose this quartic-polynomial vector. The positive theorem
at radius0.8 does not cover radius1. Reported upper bounds at radius1
do not give a lower bound on every vector. Its supplements were not
replayed and are not needed for the generic quadrature import.
This overlap makes the nominated work a REPRODUCTION, not a new
variational principle, a new certification method or evidence of novelty.

C744m already imports Vincent Liu's Theorem A, Section3 equation(3),
printed pp3-4 of the14September2026 manuscript, in the complete C759a
normalization: Q(g)>=2^-151||g||^2 for smooth compact tests in(-1,1).
Its canonical source qualifications and archive pin remain in C744m;
the source arithmetic has not been replayed locally. Reuse assessment492's
inspected scope. C744m itself specializes to smooth neutral three-cell
tests; it is not an already-written application to this nonsmooth frozen
vector. The closure/application argument for this vector is deferred,
not newly established during this literature turn. A negative enclosure
would require review against this existing stronger source claim as well
as against the complete-form normalization. A source-backed positive
expectation does not certify the actual quotient's size.

The proposed reproduction is justified by the particular suspect
assembly: its mass conditioning and stiffness asymmetry leave the
negative matrix indication unsupported. An independent scalar check
tests that concrete artifact. There is no reason to reproduce an entire
window-positivity theorem or to recompute an eigenvector. C759a's
constant trial is a different test function. Stops822/829/831 concern
kernel, eigenfunction and graph-norm requirements; stop849 concerns
time evolution. None supplies this scalar certificate, and none is
reopened. No duplicate frozen-vector enclosure was found in the scoped
November13 even-family search.

## Ready scope and unpaid specialization

SPECIALIZE: one direct scalar evaluation is source-covered as a known
method. Use exactly column0 of modal_coefficients from NPZ849 in the
recorded ordered basis v,(1-x^2)P_0,...,(1-x^2)P_508. The polynomial
degree may reach510; 508 is the last Legendre index before multiplication.
The source covers neither a coefficient change nor a mode search.

The selected implementation is the compact autocorrelation representation
of the full form, using the cited general geometric functional. It must
construct the exact piecewise polynomial and its autocorrelation with
all breakpoints, prove applicability and normalization, certify the
positive squared norm, and enclose both pole evaluations and all five
shift correlations n=2,3,4,5,7. It must regularize the origin before
certified panel integration, verifying every needed complex neighborhood
or explicit Taylor remainder and all arithmetic. No coefficient,
breakpoint, regularized integrand, ellipse or target-specific error
constant is computed in this review. These are the identified
specialization tasks, not additional unassessed mechanisms.

The infinite archimedean subtraction must be included through the cited
exact exterior term; compact support alone does not make that subtraction
zero. This selects a full geometric evaluation, not a Fourier cutoff
with an unproved tail. If any endpoint is excluded numerically, its
entire omitted integral needs a rigorous bound. A sampled error, a
requested precision or a matrix entry cannot replace that evidence.

The subsequent certificate must store the exact input identity, complete
form contributions, norm, analytic and rounding bounds, failures and
final interval. Print only its decisive bounds and artifact path.
Sign discrimination is not promised. A negative upper endpoint is an
UNVERIFIED CANDIDATE requiring a later independent audit, including the
source-coercivity conflict; it is not an off-line zero certificate.
A positive lower endpoint rejects this one indication. A zero-containing
interval or unpaid contribution ends this one fixed test. Precision or
panel refinement may address this same certificate only within its one
bounded attempt; no time, mode, basis or parameter sweep is covered.

Matching Mathlib coverage was not checked. No formal-verification or
absence claim is made. The signed spectral and actual-Xi links remain
open; this known scalar diagnostic supplies no justified creative
central-gap mechanism. Recommend calculation/standard/high for the
exact continuation, after its separate source-gate approval. The
new ready assessment does not authorize calculation in this turn.

## Bounded search and outcome

Queries: `Johansson rigorous numerical integration arbitrary precision
ball arithmetic Petras 2018 acb_calc_integrate` and `Weil quadratic form
compact support autocorrelation archimedean integral Connes Consani
Moscovici 2511.22755 Lemma 2.3`. Local searches used November13 even-family
assessments/stops for frozen modes, Rayleigh/negative Ritz, quadrature,
Petras and1802.07942. These led to reusable683/686/655 coverage and the
newly inspected Zhu scalar-certificate comparison. The named October30
support-enlargement assessment and C744m were read solely to compare
stronger fixed-window inputs. No sibling notebook or global checkpoint
search occurred. Search hits not inspected (slides, secondary reports,
general quadrature libraries) are not theorem evidence.

Outcome: local source coverage is now ready for one standard-method
specialization. No original mathematical advance, quotient interval,
spectral sign, norm certificate or counterexample is established.
