# First post-cutoff actual Gaussian error — completed source comparison

TARGET: Determine the exact positive-x sign transitions of E_(n,2n+1)(x)=P_(2n+1)(x)-Q_(n,2n+1)(x) for every integer n>=1 using the two moments beyond Gaussian exactness, with actual-theta applicability and without assuming reference hyperbolicity.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step546 searched the exact Gaussian moment-defect/sign target, monomial errors, Jacobi recurrence and Hermite divided differences; checked the named theta assessments, L795/L805/L806 and recorded stops; reused the ready Jensen comparisons. Queries, inspected sources and unread leads are recorded below; no novelty inference.
SOURCE_EVIDENCE: Gautschi OUP2004 Theorem1.27 and complete proof, pp10–11,(1.3.2)–(1.3.7), https://csclub.uwaterloo.ca/~pbarfuss/Walter_Gautschi_-_Orthogonal_Polynomials_-_Computation_and_Approximation_%282004%29.pdf ; de Boor author copy dated21June2021, Proposition7/Example6/Proposition21 and complete polynomial proofs, PDFpp2–6,(4),(8)–(9),(16),(20), https://ftp.cs.wisc.edu/Approx/deboor2.pdf ; reuse previously inspected Gaussian exactness and L795 DLMF18.5.12 normalization.
COMPARISON: Standard polynomial Hermite remainders and monic recurrence cover the algebraic method, including repeated interpolation nodes and unbounded positive measures with all moments. No inspected theorem directly states the normalized theta first-post-exact error transitions. This is conventional specialization, not a new quadrature theorem or an import of reference hyperbolicity.
GAP: Carry out the two monomial-defect specializations at orders2n and2n+1, verify their actual-theta signs and integrability, then combine the exact L795 coefficients to classify E for every n>=1 and x>0 including degeneracies. These calculations, transition locations and signs have not been derived in this review.
REASON: Essential polynomial-error and recurrence coverage is now sufficient for the unchanged bounded target. The actual integrated error is independent of the failed derivative-sign premise. Any root-barrier use still needs separate reference root geometry, margins and degree-uniform transfer; one error-sign test cannot supply them.
SCOPE: Approves only the unchanged TARGET for a later conventional mathematical specialization using L019/L021/L795 and L806 definitions. No numerical sweep, changed measure, truncation, reference-root premise or cross-notebook input. Step546 itself is literature-only and derives no theta error identity or sign.
LITERATURE_REASON: The invocation-start target was REVIEW_REQUIRED; the first two post-exact moment defects and polynomial remainder cases were essential unread coverage. This completes that gate rather than repeating the ready derivative assessment.

## Original nomination, retained

This is a nomination after completing the gate-approved derivative
classification. It does not approve or derive the new target. Before
research, search the exact statement and Gaussian moment-error,
orthogonal-polynomial and Jacobi-coefficient terminology; inspect
primary theorem hypotheses and the essential polynomial proof cases.
Reuse the earlier full-support Gaussian existence/exactness assessment
rather than rereading unchanged sources for orientation. If a known
result covers the target, import it and check only theta applicability.

The bounded mathematical test, if approved later, is the exact
positive-x sign-transition classification of this one degree family,
including degeneracies, for all n>=1. It must establish actual moment
defect signs or state their unresolved assumptions; a derivative's
sign changes are insufficient. No numerical degree sweep or repeated
two-node common-interlacer calculation is proposed. The local negative
result in L806 must remain qualified until independently audited.

Continue toward a root-barrier mechanism only if the integrated-error
classification provides a concrete sign region that can subsequently
be compared with independently justified reference barriers. Otherwise
record the limitation and park that use. Even a passing error-sign
test proves no reference root geometry or RH statement. No barrier
comparison is included in this proposed calculation's scope.

A protected creative central-gap target is not justified yet: the
signed theta mechanism has no independent reference root margins or
degree-uniform transfer estimate. This narrow moment-defect question
may be conventional specialization; do not label it creative to meet
a scheduling target. The next turn is a separate literature comparison,
which must either approve an exact bounded target or identify a source
or overlap obstruction. Full matching Mathlib coverage is unchecked.

## Completed comparison — step546, 5 November 2026

The original pending language above is historical. The TARGET is
unchanged. The main gap remains actual-Xi all-degree mixed positivity;
the intermediate target is the first post-exact integrated Gaussian
error. A possible downstream use is a signed root barrier, provided
its reference and margins can later be justified independently.

### Primary statements and proof cases

Walter Gautschi, *Orthogonal Polynomials: Computation and Approximation*,
OUP, first edition (2004), [Theorem1.27, pp.10–11](https://csclub.uwaterloo.ca/~pbarfuss/Walter_Gautschi_-_Orthogonal_Polynomials_-_Computation_and_Approximation_%282004%29.pdf),
(1.3.2)–(1.3.7). For a positive measure with all finite moments and
positive-definite polynomial inner product, its monic polynomials obey

    q_(k+1)(v)=(v-alpha_k)q_k(v)-beta_k q_(k-1)(v),
    q_(-1)=0, q_0=1,
    alpha_k=integral v*q_k(v)^2 dnu / integral q_k(v)^2 dnu,
    beta_k=integral q_k(v)^2 dnu / integral q_(k-1)(v)^2 dnu (k>=1).

Read the full proof, including k=0,1 empty sums: expansion in the
orthogonal basis and symmetry of multiplication eliminate the lower
terms; inner products identify both coefficients. Infinite support
gives the infinite index range. The adjacent finite-support bound,
Theorem1.28, is not imported. Reuse Theorems1.6/1.19/1.45/1.46
(pp.1–3,7,21–23) from step539 and Theorem1.48/corollary
(pp.23–24) from step543; do not reprove Gaussian existence,
positive weights or degree2n-1 exactness. These are tools for the
moment-error specialization, not its completed theta sign answer.

Carl de Boor, *Divided differences*, Surveys in Approximation Theory1
(2005),46–69; inspected [author copy dated21June2021](https://ftp.cs.wisc.edu/Approx/deboor2.pdf),
whose internal pagination is1–23. Proposition7 (PDFp.3), Example6
(PDFpp.4–5),(16), and Proposition21 (PDFp.6) apply to arbitrary
polynomials and arbitrary real or complex centers, with repetitions.
Writing w_N(z)=product_(i=1)^N(z-t_i), the Hermite interpolant H_N
of degree<N satisfies the imported identity

    p(z)=H_N(z)+w_N(z)*Delta(t_1,...,t_N,z)p.

Read the full factor-divisibility/uniqueness proof, the polynomial
quotient argument and its extension to coincident centers by
continuity, and the finite-dimensional inverse-map continuity proof.
Repeated centers impose derivative conditions. Thus Gaussian double
nodes require no division by a vanishing node difference. This is a
polynomial identity; it imposes no finite integration interval or
smooth-function mean-value hypothesis. Only its later integration
against nu requires moment checks.

The author copy's Proposition25/Example7, PDFpp.8–9, and its
bidiagonal path argument were also inspected. The extracted (27)
displays an index inconsistent with the nearby degree convention;
it is not a load-bearing formula here. Use polynomial division and
(16), not an unchecked transcription of (27). No correction of that
formula or new divided-difference identity is claimed this turn.

Franco Zivcovich, *Fast and accurate computation of divided differences
for analytic functions, with an application to the exponential
function*, DRNA12 (2019),28–42,
[Sections1–2, pp.28–30](https://www.maths.tcd.ie/EMIS/journals/DRNA/pdf/zivcovich_2019_fac.pdf),
was read for the Newton/monomial basis comparison. It states a
complete-homogeneous coefficient formula and points to an earlier
theorem. That earlier theorem was not retrieved; this source is a
comparison lead, not an essential imported proof. The de Boor
polynomial quotient and Gautschi recurrence suffice independently.

### Applicability, overlap and remaining difference

The local proofs L019/L021/L795 were read: nu is the actual pushforward
under v=u^2 of K(u)du/m_0, has full positive-half-line support and all
finite moments, and uses the stated factorial-normalized Laguerre
average. These are exactly the previously verified measure hypotheses;
there is no finite-support replacement. L806 supplies definitions of
q_n,h_n,Q,E and the recorded cutoff; its unaudited derivative
classification is not needed to import the source identities.
The future proof must explicitly check finite absolute polynomial
integrals and strictness using actual support, retain the x/4 and
factorial factors, and handle n=1 and x=0 separately. Merely citing
an unspecified mean-value remainder would not locate a transition.

Ready known-Jensen coverage was reused from
[step495](2026-11-05-central-hermite-theta-gram.md), its known-degree
comparison: Griffin–Ono–Rolen–Zagier,
[1902.07321v2](https://arxiv.org/pdf/1902.07321v2),
Theorem2,(1)–(2),Section5.2, already covers degrees1–8 at all
nonnegative shifts, with the recorded factor8 normalization. Reuse
[step473](2026-11-05-polynomial-jensen-wedge-central-scope.md) for
Holland [2608.08682v1](https://arxiv.org/html/2608.08682v1),
Theorem1.1/Proposition2.2 and their stated eventual-shift and
independent-model hypotheses. Neither assessed conclusion is a
first-post-exact quadrature-error classification, nor an automatic
shift-zero, all-degree root-sign transfer. These manuscripts were
not independently audited again. Small-degree hyperbolicity would
be known overlap, not new progress from the proposed calculation.

Targeted duplicate/failure checks covered the named theta Gaussian
assessments and ATTEMPTS, L795/L805/L806, the step545 history and
the relative-root-disk stop. They located no existing treatment of
these two post-exact moment defects beyond this nomination. Preserve
L795's full-support interlacing stop, L796's prefix Favard stop,
L805's compressed pair stop and L793's unpaid actual-transfer
premises. The new calculation uses neither common interlacing nor
a constant-sign whole-support derivative. This bounded search is
not evidence of originality or of a universal source absence.

Searches included `Gaussian quadrature error monomials degree 2n+1
orthogonal polynomial norm sum nodes`; `Gauss quadrature error moments
complete homogeneous symmetric polynomials 2n+1`; `Jensen polynomials
Riemann xi Gauss quadrature moment error`; `"Gaussian quadrature"
"moment errors"`; `"Gaussian quadrature" "moment defect"`;
`"Gauss quadrature" "monomial" "recurrence coefficients" error`;
`"Gauss quadrature" "error functional" polynomial division`; and
`"divided differences" "monomials" "complete homogeneous" de Boor`.
Hits on classical Gauss–Legendre errors, anti-Gauss rules and numerical
moment algorithms were not imported. The GORZ/Holland comparisons
already supply the relevant stronger Jensen scope, so broader Jensen
proof rereads were unnecessary. DLMF3.3/3.5 were opened for navigation;
their generic formulas add no transition theorem and are not new inputs.

### Approved bounded continuation and stopping test

SPECIALIZE approves the exact TARGET above, not an expanded degree
sweep or a reference-root construction. First obtain the two
polynomial moment-error identities from the cited Hermite/exactness
method (or equivalent finite polynomial division), then check the
required signs using the actual measure and combine the L795
coefficients. State any unproved sign assumption rather than hide it.
The conventional specialization is needed because no inspected
theorem directly states the target in this theta normalization;
there is no need to reprove the imported general theorems.

Success for this target means a complete all-n positive-x transition
classification with degeneracies and actual-law applicability, not
a numerical preview. Continue toward root barriers only after a
concrete sign region can be compared with independently justified
reference values. Otherwise record the limitation and park that
dependent use; do not count a sign classification as reference
hyperbolicity or mixed positivity. Higher-degree errors, margins,
all-degree transfer and RH remain open even if this test succeeds.

No justified creative target is ready: this review supplies standard
finite polynomial tools, not a new theta cancellation mechanism or
independent degree-uniform reference margins. Do not relabel the
specialization creative to meet a scheduling target. No lemma or
mathematical script was written, and PROOF/DAG are unchanged. Full
matching Mathlib coverage remains unchecked; no formalization or
absence claim is made. No mathematical exploration budget was spent
or reset by this literature comparison.
