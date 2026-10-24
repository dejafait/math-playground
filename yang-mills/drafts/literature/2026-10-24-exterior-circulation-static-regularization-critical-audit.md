# Exterior-circulation static regularization audit — source coverage

TARGET: Critically audit L273(3)--(5)'s ordered mass/projection comparison against L272(3), retaining both mixed orientations and every relative source/end row.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the production and boundary-transfer assessments; read L272 and L273 in full, L242 hypotheses, section 3 through (13) and its isometry audit passage, L095 section 4 (14) and its full-spectrum proof, L088 (3)--(5), L110 definitions and section 1, and L111 hypotheses and section 1. Narrow searches of history/450,453--456, the exterior rate assessment and production working record distinguish production and downstream audits from this independent L273 audit; no duplicate verdict was found there. Read ATTEMPTS/030/032.
SOURCE_EVIDENCE: Reused the recorded primary inspections in the production and boundary-transfer assessments, with their versions and theorem references detailed below; no new external passage was retrieved. The operative general inputs for this finite audit are the finite-dimensional self-adjoint spectral theorem, singular-value calculus, rectangular trace cyclicity and Schatten Holder inequalities. L242(13)'s complete pinned vertex shell proof and L095(14)'s relative edge shell proof are now inspected local inputs, not external theorems asserting L273.
COMPARISON: Known finite spectral and trace-ideal results cover the methods, while L242(13) supplies the precise pinned projection allowance on the stated vertex space. They do not certify L273's two literal words, circulation placements, logarithmic inverse error or full response count. L274's accepted transfer imports L273(5); it is not an independent L273 verdict.
GAP: Independently verify L272(3) to L273(3), both rectangular orders, one- and two-circulation inverse errors, the three projection-error placements, full spectral/row/heat counts and exactly one L272 allowance in (5). The unresolved work is mathematical audit of this application, not missing essential literature coverage.
REASON: Exact target-specific source and hypothesis coverage is sufficient for a later bounded audit under SPECIALIZE; this approves scope only, not correctness. Retain L272 and all other imported audit qualifications and the completed L274 conditional verdict.
SCOPE: Same relative SU(2) cube, admitted sufficiently large even N, a=8/N, tau=1/16, lower-rooted forest, stored coordinates, bare-first order, both probes/words, original coefficients, all source/end rows, upper pin, constant own-direction indices and full heat sums; retain all imported qualifications.
LITERATURE_REASON: The saved REVIEW_REQUIRED target separates L273's upstream mass/projection audit from the accepted L274 boundary transfer; complete its missing vertex-shell and relative-domain coverage using existing sources before mathematical work.

The main gap remains interacting continuum existence and finite positive
infinite-volume mass. Auditing this intermediate estimate could discharge
one upstream premise of L274/L275 and later transverse-H/L011 rate
assembly; L272 and independent construction requirements remain unresolved.

Essential input IDs are L273 L272 L123 L088 L095 L110 L111 L242.
The two reused assessments are
`2026-10-24-exterior-circulation-quantitative-remainder.md` and
`2026-10-24-exterior-circulation-boundary-transfer-critical-audit.md`
in this directory. This completes the preceding coverage proposal;
the mathematical audit itself remains unperformed in this turn.

## Known inputs and exact scope comparison

The finite-dimensional self-adjoint spectral theorem applies to real
symmetric positive relative Hodge matrices and to the pinned vertex
matrix d^*d. Singular-value calculus applies to rectangular D and d.
Schatten Holder, including trace-norm/operator-norm duality and
Hilbert--Schmidt duality with bounded intervening factors, concerns
compatible finite-dimensional maps; it does not require the response
or its coefficient matrices to be positive. Rectangular trace cyclicity
requires the two products to be endomorphisms of their respective
spaces. These are standard named inputs, not original estimates to
reprove. Their precise application to each word is the audit target.

L242 uses transverse incidence T, vertex matrix Delta_0=T^T T and
P_delta=T(Delta_0+delta I)^(-1)T^T. Its section 3, (13), states
||P-P_delta||_HS <= C N^(3/2)delta^(3/4), for 0<delta<=1 and
N sqrt(delta)>=1. The inspected proof includes every pinned vertex
mode m in {1,...,N-1}^3, its low and high spectral shells and empty
high ranges. Its later audit passage identifies the nonzero singular
values through V_0=T Delta_0^(-1/2), an isometry. This supplies the
specific result L273 cites. L273's d is this same relative incidence,
not a scalar gradient with changed edge conditions. The later audit
must check this identification in the literal words; no reverse-trace
response bound from L242 is imported.

L095 section 4, (14), records the transverse relative edge spectrum:
each component has its own index in {0,...,N-1} and its other two
indices in {1,...,N-1}. Its shell proof retains all components and
normal end edges, gives no zero eigenvalue, and states
Tr Delta_T^(-1)<=C N^3. This differs from the all-positive vertex
indices in L242. Both are essential to assessing L273's singular-value
and shell arguments. Import their stated estimates and qualifications;
do not silently replace relative edge conditions by scalar Dirichlet
conditions or independently re-audit all upstream results here.

L272(3) is the exact massless static trace being audited; its full proof
was inspected for scope. Its (4) is one combined O(N^2 log(eN))
allowance for the original response, including f,f, both axial endpoint
deficits and the two-level replacement. Its own correctness remains an
imported pending audit. L110's exact C_k,F_k split and L111(1)'s H_s D
factorization fix the rectangular domains and both generator orders.
L088(5) bounds the unprojected f_k/a^2, b_k/a and q_k/a entries with
one polynomial heat envelope. These are suitable existing inputs for
checking L273(8); a bound only after projection would not suffice.
L123 remains the canonical original response and coefficient convention.

## Reused primary literature and exclusions

The production assessment records inspected Lawler--Limic, *Random
Walk: A Modern Introduction* (Cambridge, 2010), Proposition 4.6.2(a),
printed p. 97 and its transient proof, and Lemma 6.3.3, pp. 127--128,
including its finite-set reduction and d>=3 proof case:
https://www.math.uchicago.edu/~lawler/srwbook.pdf.
Those are scalar killed-Green and source-difference results with their
stated interior/source hypotheses; they do not supply a vector relative
mass/projection trace estimate. No fresh inspection or direct use of
those theorems is claimed in this review.

The boundary-transfer assessment records Benzi--Simoncini,
*Decay bounds for functions of matrices with banded or Kronecker
structure*, arXiv:1501.07376v1, 29 January 2015, printed pp. 12--15,
Theorem 6.1, Corollaries 6.2--6.3 and their proofs; section 6.2
(6.3)--(6.4), Remark 6.6 and section 5's finite-section qualification:
https://arxiv.org/pdf/1501.07376v1.
Its banded Hermitian positive-semidefinite tensor factors and
Laplace--Stieltjes bounds retain spectral/small-eigenvalue dependence.
These support the later localization method, not L273's exact finite
algebra or its error budget. No matrix-decay theorem is needed as an
extra premise for this narrow audit. The reused scalar Toeplitz,
translation-invariant lattice power-counting and positive-flow-time
Ward comparisons likewise assert no matching result for these two
pinned, variable-coefficient rectangular words. No essential unread
lead or source-access blocker remains for the saved audit scope.

The narrow duplicate check found production L273/history/450 and
later audits importing it, not an independent L273 acceptance.
ATTEMPTS/030 rules out putting varying masses into a qualitative
fixed-mass limit; ATTEMPTS/032 rules out separate first absolute
moments of projected alternating kernels. Neither forbids testing
L273's uniform finite spectral inequalities, and neither proves them.
The current target does not need an external novelty search or a
reproof of general spectral machinery. Full matching and supporting
Mathlib coverage remain **not checked**; unknown is not absent.

## Later audit and decision test

The later mathematical test should accept only a bound uniform before
the schedule, with errors O(N^3[epsilon log(e/epsilon)+delta^(3/4)])
for the literal two words and exactly one L272 allowance in (5).
Otherwise isolate the first failed identity, domain or bound without
claiming signed growth. Preserve ATTEMPTS/030/032, both orientations,
every source/end row and all independent pending audit qualifications.
Check compatible domains in both mixed orientations before any mass
or projection replacement; distinguish exact P,Q from non-idempotent
P_delta,Q_delta. Check all three projection placements and retain the
circulations on the respective inverse errors before taking norms.
Test the original finite inequalities before substituting
epsilon=N^(-1/2), delta=N^(-2/3); retain the original normalization,
complete polynomially weighted heat sums and every relative row.

If one identity, domain or allowance fails, preserve the production
proof and record that first failure with a concrete repair test. An
insufficient upper bound is not signed growth. A successful narrow
audit would clear only this imported premise of L274/L275; L272,
the other upstream audits, complete quantitative assembly and all
interacting/continuum/infrared requirements would remain unresolved.

Completed LITERATURE / NOVELTY_UNCHECKED / EXPLORATION: this is new
target-specific coverage comparison, not a mathematical advance or a
novelty claim. Mathematical exploration usage remains zero of three.
The sole next action remains TARGET verbatim, now under SPECIALIZE
for a separate mathematical proof_audit (REPRODUCTION if applicable)
after the supervisor's separate approval. No lemma, mathematical
script, argument overview or DAG is changed by this review.
