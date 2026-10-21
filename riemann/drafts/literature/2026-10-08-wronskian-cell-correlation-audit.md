# Completed coverage review for the fixed response-cell correlation audit

TARGET: Critically audit L383's fixed response-cell correlation asymptotic, including nonzero phase harmonics, complex-shift jets, localization and the positive leading coefficient.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-statement/stronger-result queries and primary comparisons in drafts/literature/2026-10-08-wronskian-response-cell-signs.md and the approved fixed test; read L383 in full, relevant L381 moment/contour/audit ranges, and the recorded fixed-test failure; no duplicate critical audit or matching source theorem was identified in these records.
SOURCE_EVIDENCE: Young, A short proof of Levinson's theorem, Arch. Math. 95 (2010), 539-548, DOI 10.1007/s00013-010-0199-9, published PDF https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf; directly inspected (2.1)-(2.3), the paragraph after (3.4), Lemmas 4-5, (4.1)-(4.5), and the complete Lemma 5 proof, printed pp. 540-543; reuse L381's audited specialization and source coverage.
COMPARISON: Young permits the bounded small complex offsets and fixed rational twists used by L383; it does not evaluate Hardy jet covariances with the full response cutoff or prove the two-direction nonzero-harmonic bounds. Those explicit local specialization claims, including carrier cancellation, are the difference requiring mathematical audit.
GAP: Essential source coverage is ready for this exact audit; the signed jet constants, harmonic contour estimates, localization, limit order and positive coefficient remain unverified here.
REASON: Approve a separate bounded critical audit using the cited moment input and recorded scalar bounds, without reproving Young or treating source applicability as verification of L383.
LITERATURE_REASON: The newly proposed L383 audit was REVIEW_REQUIRED; its offset product contours and two-direction harmonic implementation must be compared with the existing coverage before mathematical review. No broader search or refreshed global-moment assessment is needed.
SCOPE: Exact L383 fixed shift pi/log H and specified cutoff; actual L366/L380 pair and normalization, eventual L372 response cells, ordinary real derivatives and H tending to infinity; independent verification only, with no RH, simplicity, noncoincidence, discriminant, fourth-moment or common-zero premise.

Essential mathematical input IDs: L366, L368, L372, L380, L381 and L382.
The subject is L383. Preserve the exact fixed shift and cutoff. Reuse
the primary-source coverage unless a precise changed hypothesis is
identified; no new source search is needed merely to fill a quota.

The completed coverage comparison below delimits the subsequent proof
audit; it does not verify the offset estimates or the harmonics. The later audit
must check the real-projection sign, sharp endpoints for signed moments,
all gcd collisions, the order of head/height/Fourier limits, zero-free
right-line Euler ratios, both carrier-canceling harmonics, connector
growth, and the four jet-covariance signs. L383 is a local reproduction,
not a claimed new source-level theorem or an RH candidate.

No RH, F_0 simplicity, noncoincidence, physical discriminant sign,
fourth moment or common-zero bound may be assumed. Common-free
localization, common-zero counts, global mixed positivity, the total
L367 margin, low indices, heights above forty and the endpoint margin
remain unresolved. Matching Mathlib coverage is not checked.

## Separate source/application comparison — 2026-10-08

The direct published Young PDF was accessible. Its weight assumptions are
0<=w<=1, support in [T/4,2T], and fixed-order derivative bounds at scale
T/log T. Lemma 5 has positive integer twists with product at most
T^(2 theta), theta<1/2, and complex shifts O(1/log T), with any fixed
implied constant. Lemma 4 also requires the shift real parts below 1/2.
Both functional-equation diagonals are retained. The off-diagonal proof
handles both frequency orderings by symmetry and repeated integration by
parts. The paragraph after (3.4) requires holomorphic errors uniform on
Cauchy contours, rather than differentiation of a real-shift estimate.

Compare these hypotheses with L383 section 2: scale T=2H; fixed heads
first; slow fixed-shape weights supported in [H/2,3H]; offsets on
|u|=1/log H and |v-h|=(pi+3)/log H, h=pi/log H; shifts alpha=iu,
beta=-iv. This lies within the cited fixed-constant small-shift scope.
The stated contours avoid the auxiliary shift-sum singularity; the
later audit must check their separation and the full holomorphic error
on the product disks. Check weight normalization or fixed rescaling
before importing the theorem. L381 section 2 and its separate audit
supply the inspected two-diagonal/Mellin-tail method, not an automatic
two-height jet theorem. The new four signed covariances must still be
verified independently, including coincident-offset endpoint majorants.

L383 section 3 instead proposes a holomorphic height-contour argument
for each fixed nonzero Fourier mode. Its shifts of height by +i or -i
are not the small shifts in Young. Reuse L381 (17)-(19) and its audit
for the paired digamma extension, fixed positive-strip bounds and
logarithmic-radius derivative disks; use L368/L372's recorded
right-half-plane Euler coverage for the full right-line factors and
their reciprocals. Ordinary Cauchy integral/derivative theorems,
sector-qualified Stirling and Fejer uniform approximation are named
standard inputs. No unread specialized harmonic theorem is invoked.
The following are mathematical audit obligations, not imported results:
the holomorphic reflection and square-root choices; right-line ratios
on the whole rectangle; the choice of opposite contour directions;
the horizontal and connector bounds for all fixed k, specifically
k=-1 and k=1 where the proposed carrier exponent is zero; and absence
of poles for each selected integrand. No contour estimate is endorsed
by this literature step.

Audit the remaining applicability claims in L383 sections 1, 2 and 4:
the sign convention from L380; the actual full phase rather than a
fixed Gram phase; eventual same-cell localization; incomplete endpoint
cost using L382's global envelope; both projection errors; all gcd
collisions; the signed smooth-to-sharp passage; uniform full tails;
and the sequential height/head/Fourier limits. Recompute the displayed
leading coefficient and its strict lower bound only in that later
mathematical audit. The source does not state either coefficient.

Duplicate/failure comparison reuses the prior response-cell assessment
and ATTEMPTS/2026-10-08-fixed-response-cell-negative-correlation.md.
The recorded first-mean, absolute response-grid and common-only reset
stops do not verify or invalidate this audit. The fixed negative test's
stop remains provisional on L383's critical review; a positive average
would still leave within-cell opposite signs undecided. No novelty is
inferred from the bounded search. Unread adjacent leads remain unused.

Continuation/abandonment test: perform one independent audit of this
exact statistic; retain its stopping conclusion only if every necessary
error is o(log H) and the positive coefficient survives. If an essential
estimate is uncontrolled at that scale, record the specific failure,
preserve the original proof and narrow reliance on it; do not vary the
shift/cutoff or invent a new mechanism in that audit. A precise repair
within the covered specialization is permitted, without assuming any
of the unresolved premises above. Plausible downstream use is a reliable
decision about this diagnostic before selecting another common-free
Wronskian test; neither outcome closes global mixed positivity.

Completed step: LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. This is a
new audit-scope comparison, not mathematical evidence for L383, a new
lemma or an RH candidate. The unchanged exact TARGET is now approved
for a later RESEARCH / REPRODUCTION proof audit. No lemma, mathematical
script, DAG or argument-assembly change is made here.
