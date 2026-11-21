# Conjugate-orbit determinant remainder — completed source comparison

TARGET: Assess whether conjugate-orbit grouping in the Cauchy-Binet expansion of actual det H2(lambda) on 0<=lambda<=1/20 supplies a signed remainder estimate beyond L919's absolute matrix bound.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Step2146 searched infinite Cauchy-Binet absolute convergence, Hermite weighted trace forms, subdiscriminant Vandermonde sums and de Bruijn/Hankel conjugate-tail terminology; checked the specific local head/tail, endpoint, connected-partition and H2 stop records. No inspected source supplies the requested actual signed triple remainder; this is bounded search evidence, not novelty or impossibility.
SOURCE_EVIDENCE: Read Akemann-Aygun-Wurfel arXiv:2305.19852v1 Lemma2.2/(2.16), p8; Roy (6Feb2005) Sections1-2, Propositions1-3, pp1-2; Ding-Qi-Wei arXiv:1505.02528v4 Section3.2, pp10-12, especially the conjugate-block identity p12; Nie Lecture11, Theorem4 and distinct-root proof p2; Polymath arXiv:1904.12438v2 Theorem3.2 and its citation-only proof. Reuse existing paired-product/Jensen coverage and L919(1),(8)-(10), rather than reprove them. Direct citations and scope below.
COMPARISON: Known Cauchy-Binet covers complex algebraic products with absolute convergence; Hermite/Vandermonde identities retain indefinite conjugate blocks. They supply no theta-specific cancellation or head-dominating determinant error. A different one-sided tail-defect specialization can test an improved required matrix margin without assuming remote reality.
GAP: No signed triple remainder, actual head determinant, head census/reality/separation or strict margin is paid. A later infinite expansion must verify all convergence hypotheses and multiplicities; a known identity alone supplies no sign. The separate proposed one-sided estimate has not been derived or evaluated.
REASON: Complete the required source review without manufacturing a lemma. Park automatic triple-orbit signing and nominate one fixed quantitative conjugate-pair defect test; do not claim all determinant grouping mechanisms impossible. The remaining test uses known algebra and a standard strip theorem, not a justified new creative mechanism.
SCOPE: Completed literature-only review for the actual L019/L058/L063/L874 family, degree two, closed band [0,1/20] and radius100 head/tail split. Original nomination below is preserved as history. No mathematical derivation, lemma, script, new strip theorem or H2 sign was produced. The separately assessed next target requires next-turn approval.
LITERATURE_REASON: The proposed signed determinant-orbit observable differs from both the approved fixed-slice strictness audit and the assessed absolute operator-norm tail; essential coverage is missing.

## Completed review — step2146

The main gap is L030-L032/C032a actual-Xi all-degree algebraic mixed
positivity. The reviewed intermediate target was a signed bound on the
three-by-three determinant's complete omitted-zero contribution. Such
a bound could lower the cost of a finite-head positivity argument;
head certification, its quantitative margin and all other degrees
would remain independent obligations. No determinant expansion or
signed bound was proved in this literature turn.

### Primary statements and essential qualifications

G. Akemann, N. Aygün and T. R. Würfel, *Generalised unitary group
integrals of Ingham-Siegel and Fisher-Hartwig type*,
[arXiv:2305.19852v1, 31 May 2023, Lemma 2.2, (2.16), PDF p8](https://www.sfb1283.uni-bielefeld.de/preprints/sfb23036.pdf#page=8),
states infinite Cauchy-Binet for complex arrays indexed by finitely
many rows and integer columns. The sums must converge absolutely.
The products use ordinary transpose, with no complex conjugation.
The paper states the identity and refers to Mehta, *Matrix Theory*
(1989), reference29, for finite and infinite versions; that book was
not read. Consequently the inspected source covers the identity's
statement, not a quantitative or uniform determinant remainder.
L919's convergent entry sums are relevant inputs, but a future
application must explicitly pay the determinant-series absolute
convergence and any uniform regrouping. No trace-class theorem is
needed merely because the number of zero indices is infinite: the
determinant still has size three. No such application is performed here.

M.-F. Roy, *Subdiscriminants of symmetric matrices are sums of squares*,
[note dated 6 February 2005, Sections1-2, Propositions1-3, pp1-2](https://drops.dagstuhl.de/storage/16dagstuhl-seminar-proceedings/dsp-vol05021/DagSemProc.05021.20/DagSemProc.05021.20.pdf),
defines subdiscriminants using the multiset of roots, with multiplicity,
and proves the Newton-sum determinant identity by finite Cauchy-Binet
and the Vandermonde formula. Its sums are algebraic squares. The
real sum-of-squares conclusion later in the note concerns the
characteristic polynomial of a real symmetric matrix, via a separate
real Gram factorization; it is not a theorem that arbitrary real
polynomials have nonnegative subdiscriminants. Neither that conclusion
nor the unweighted Newton-sum formula directly signs L874's shifted,
weighted reciprocal-node matrix. Repeated equal nodes give vanishing
Vandermonde minors, not a license to delete their multiplicities from
the matrix. Only this existing finite identity is being cited.

W. Ding, L. Qi and Y. Wei, *Inheritance Properties and Sum-of-Squares
Decomposition of Hankel Tensors: Theory and Algorithms*,
[arXiv:1505.02528v4, 17 September 2015, Section3.2, printed pp10-12](https://arxiv.org/pdf/1505.02528v4#page=10),
gives a general finite Hankel decomposition and its real form. Read
the nonsingular-leading-block context and the displayed conjugate
block calculation on p12. For real vectors u,v and real a,b, the sum
of the rank-one term with vector u+iv, coefficient a+ib, and its
conjugate has real middle block

    2 [[a,-b],[-b,-a]]

in the real vectors u,v. This is the source's identity, not a new
specialization derived here. Its block has zero signature when its
coefficient is nonzero. In particular conjugate pairing retains
opposing signs. The finite decomposition's nonsingularity and rank
hypotheses are not asserted for the infinite actual-zero system.
Only the displayed elementary pair identity is a prospective input.
An all-positive decomposition is an additional condition, not a
consequence of reality of the Hankel entries.

J. Nie, [*Lecture11: Univariate Polynomials and Hermite Form*,
Theorem4 and its distinct-root proof, p2](https://mathweb.ucsd.edu/~njw/Teaching/Math271C/Lecture_11.pdf#page=2),
independently displays the weighted form with real polynomial q,
complex roots x_j, ordinary algebraic squares, and the same conjugate
blocks. The proof assumes distinct roots; its repeated-root case is
left as an exercise. We use the displayed distinct-root comparison
only, not an unproved multiplicity extension or an infinite inertia
criterion. With more than three zero nodes, full Hermite signature
does not automatically give the signature of our three-row truncation.

The published Ding-Qi-Wei PDF initially opened, but subsequent requests
timed out. The author arXiv v4 above was accessible. No version identity
with the published paper is assumed. The Nie and Roy passages and
the v4 block identity suffice; this is not a persistent source blocker.
Knill arXiv:1306.0062v3 Introduction(1) was also read as a finite
Cauchy-Binet cross-check; its pseudo-determinant results are unused.
The CMU thesis infinite-formula lead returned502 and is unused.

### Reuse, comparison and route decision

Read L019/L058/L063, L874's definition and local analytic normalization,
and L919's complete product/count/tail/norm proof through its
conditional margin. Reuse the ready product/Jensen assessments cited
there. The relevant exact bounds are L919(8)-(10), including all
complex zeros with multiplicity and the strict radius100 complement.
Boundary zeros belong to the finite head. L920's fixed-direction
endpoint certificate remains inconclusive and unaudited; its head
upper endpoint is not a positive lower margin. No certificate or
mathematical program was rerun.

The finite-head/tail and endpoint assessments, L917's moment-box stop,
the tail approval-loop stop, and the connected-partition assessment
were compared. The source identities above explain an algebraic
expansion but supply no actual-theta inequality for its signed orbit
sums. In particular neither a real determinant nor conjugate grouping
turns algebraic squares into modulus squares. This review does not
prove that a theta-specific triple cancellation is impossible.
It finds no independently signed triple remainder satisfying the
nomination's continuation test, so a triple-expansion-only attempt
is parked pending a specific additional estimate.

A materially different quantitative test is available from the
source pair identity: retain the positive real-vector contribution
and bound only the opposing imaginary-vector contribution in the
tail matrix. The geometric input is the standard de Bruijn strip
theorem as stated in Polymath,
[arXiv:1904.12438v2, Theorem3.2](https://arxiv.org/html/1904.12438v2#S3).
Read its full statement: an upper zero-height bound y0>0 at t0 gives
the bound sqrt(max(y0^2-2(t-t0),0)) for t>t0; its proof cites de Bruijn,
Theorem13, rather than supplying a new proof. The same section applies
it using the ordinary critical strip at t0=0. The proposed test uses
only that standard theorem, L018's ordinary critical-strip input and
L919's already justified F(lambda,z)=8H_(4lambda)(2z).
No stronger zero-free region or positive-time real-tail theorem is
being sought. Conversion to local units and effective constants
remain work for the future specialization.

The separate assessment
`2026-11-21-h2-one-sided-conjugate-tail-budget-2146.md` fixes the
test: a uniform lower matrix bound E>=-epsilon I with epsilon<B/100,
at exactly L919's R,D and time band. This is a proposed threshold,
not an achieved estimate. It changes the required head tolerance
rather than just refining the old absolute norm. A successful bound
could later be paired with a separately certified head margin above
epsilon. It supplies no head census, reality, separation, determinant
margin or global H2 sign by itself. If it fails, preserve its actual
bound and stop this fixed test without a parameter sweep.

### Search record and classification

Queries included `Hankel Hermite matrix subdiscriminants sum squared
Vandermonde complex conjugate roots theorem`, `Cauchy Binet infinite
matrices absolute convergence determinant trace class exterior powers`,
`de Bruijn Newman heat flow zeros Hankel determinant conjugate pairs
positivity`, `Hermite matrix weighted trace form nonreal conjugate roots
signature theorem pdf`, and the narrower Hankel/strip/one-sided-tail
variants. Local searches were restricted to the nominated H2, complete
zero-tail, reciprocal-Hankel and conjugate-related assessment/attempt
paths. A Li symmetric-zero-tail match was inspected and is about Li
asymptotics, not this matrix. No matching completed one-sided H2 tail
budget was found in this bounded comparison. No novelty follows.
Unrelated Bessel/Hankel-transform results, secondary pages, external
AI notebooks and recent coefficient-dynamics leads were not used.

Full and supporting Mathlib coverage for this changed signed
determinant target was not checked; availability is unknown. No
cross-notebook mathematical result is used. Outcome is EXPLORATION,
LITERATURE, NOVELTY_UNCHECKED: new source coverage and an actionable
quantitative test, with no mathematical advance or informative
actual-family negative bound. No mathematical exploration increment
is spent by this literature step. A creative attempt is not yet
justified: the concrete available continuation is known algebra plus
a standard strip/count specialization, and a genuinely new signed
theta-triple mechanism remains unspecified.

## Preserved nomination — relevance and proposed bounded test

The main gap is still L030-L032/C032a. A signed, cancellation-preserving
bound for this first three-by-three logarithmic Hankel determinant
could give a lower-time intermediate input and a prototype for higher
degrees. It would leave a certified real head, its quantitative margin,
other degrees, tangency and the endpoint/global assembly unresolved.

Prospective inputs are L019, L058, L063 and L874 for the actual family,
product and coefficient convention, and L919 for the existing complete
tail bounds. Inspect only relevant proof ranges when testing their use.
L920, L917, L922 and L938 record contrasts/stops, not positive premises.
C874f identifies the known-slice overlap and supplies no lower-time
real-zero hypothesis. There is no cross-notebook input.

The candidate is to keep the algebraic determinant expansion over
reciprocal-zero triples, grouped in complete complex-conjugation
orbits, before estimating the contributions involving omitted zeros.
The prospective payoff is a strict head contribution exceeding a
complete signed error, or a termwise/orbit inequality that removes
the leading absolute loss. This paragraph proposes a test; it does
not assert an expansion, its convergence, an inequality or a margin.
In particular a squared complex Vandermonde is not a modulus square.

First compare primary infinite Cauchy-Binet/compound determinant
hypotheses, real-entire zero symmetries and existing stronger estimates.
Reuse ready product/Jensen coverage rather than researching it again.
Multiplicity, boundary zeros at radius100 and every remaining zero
must be accounted for. A selected real triple is not a complete real
head, and no zero tracking or head isolation is licensed by this note.

Continue only if the review identifies a specific independently
testable conjugate-orbit estimate with a strict comparison threshold,
and shows that it is materially different from the stopped absolute
head-margin calculation. Retire this candidate if the only available
bound is the same absolute norm, assumes all zeros real, needs an
unpaid head precision without changing that bottleneck, or merely
restates a known finite determinant certificate. An informative
negative result is acceptable; a new lemma is not required.

## Prior stops and prospective routing

The exact local comparisons read at nomination are
`2026-11-09-low-time-h2-finite-zero-domination-review.md`,
`2026-11-09-low-time-h2-complete-zero-tail-budget.md`,
`2026-11-09-h2-endpoint-head-margin-feasibility-review.md`, and
`2026-11-06-theta-connected-partition-interface.md`.
The associated ATTEMPTS records retain the fixed moment-box,
shared-Taylor, endpoint-Rayleigh and energy-cell failures. No stopped
script was rerun. Connected partition identities alone supply no sign;
they are not the proposed zero-triple grouping. This narrow comparison
is not a completed duplicate or literature search for the new target.

The immediate task is literature_comparison, standard/high. If adequate
coverage permits a genuinely new signed grouping at the central gap,
prepare a separate proof_attempt/creative target, deep_research/max.
Its escalation must name the actual obstruction: conjugate reciprocal
zeros contribute algebraic squares of mixed sign, and the old absolute
tail loses the positive head margin. The bounded test must specify the
orbit inequality and complete error-versus-head threshold. If sources
already provide that estimate, classify its application as reproduction
instead. No research target is approved in this nomination.
