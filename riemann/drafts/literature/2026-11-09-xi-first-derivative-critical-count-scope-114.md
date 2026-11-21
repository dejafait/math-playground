# Single-step actual-Xi critical-count source nomination

TARGET: Determine whether Kim's critical-point theorem yields a finite-rectangle balance between the nonreal-zero counts of Xi and Xi' with explicit boundary terms, without assuming RH or finitely many nonreal Xi zeros.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step115 searched the exact title/DOI, theorem/Jensen-disk terminology and endpoint coverage; scoped local checks found no prior inspected Kim count assessment. Reused step114 and the November4 extrema/Jensen comparisons. Complete primary Section2 was obtained through the published-PDF mirror after AMS403; no novelty inference.
SOURCE_EVIDENCE: Young-One Kim, Proc. Amer. Math. Soc.124(3)(1996),819–830, DOI10.1090/S0002-9939-96-03083-3: definitions pp819–820, Theorem1 p821 and complete proof pp822–823, plus Theorems2–3 statements and Example2 p829. Corrects the nomination's last page829 to830. Primary PDF and exact formulas below; Pólya's original referenced real-count proof was not independently inspected.
COMPARISON: Theorem1 gives a local count balance without RH or a finite global nonreal-zero count, but assumes endpoints outside the union of closed Jensen disks. It does not license arbitrary zero-free vertical boundaries. L018 and L023/L024 supply relevant Xi strip/genus facts; disk-free endpoints, critical-zero estimates and global zero-loss transfer remain separate.
GAP: Conditional source coverage is ready; no arbitrary-boundary correction formula or unbounded sequence of admissible Xi endpoints is supplied. Actual critical-zero counts and all-degree mixed positivity remain open. The fixed-height Xi specialization is not proved in this literature turn.
REASON: Record a useful source-scope negative for the boundary-zero-avoidance-only application, retaining the conditional theorem. Test the newly exposed endpoint hypothesis separately rather than repeating high-derivative smoothing or claiming zero loss.
SCOPE: Original finite-rectangle question unchanged. SPECIALIZE covers only the conditional use of Theorem1 with a,b outside J(f), its multiplicity definition and explicit endpoint-sign cancellation. It does not approve removing that hypothesis, asserting actual-Xi endpoint existence, or deriving a general contour-defect theorem.
LITERATURE_REASON: A new finite-region first-derivative count target has no primary coverage. The source's fixed-compact high-derivative summary is insufficient; this essential hypothesis comparison precedes any mathematics.

## Relevance and bounded discriminator

Main gap is L030–L032/C032a actual-Xi all-degree mixed positivity.
The intermediate source question asks whether the loss of nonreal zeros
in **one** differentiation can be measured by actual real critical-point
data plus explicit contour/boundary obligations. This would identify a
signed datum missing from forward smoothing. If applicable, it could
support a later test of whether actual-Xi differentiation loses any
nonreal-zero information. No zero-loss estimate, inverse theorem,
all-degree sign or route to RH is asserted.

First retrieve the named primary theorem and its essential cases;
compare exact statement, stronger results and local duplicates before
larger extracts. Check the use of finite versus infinite nonreal-zero
counts and whether exclusion of Jensen disks, zero-free boundary lines,
or global Laguerre–Polya membership is a premise. Boundary-zero avoidance
is an obligation, not an established choice uniform in T. If the cited
paper only supplies eventual high-derivative local reality, record that
failure of scope and park this count application; do not repeat the
cosine comparison or derive a replacement theorem during literature work.

Continue only on a precise applicable finite-region balance retaining
every boundary term. Abandon this source application if it requires RH,
an unproved finite global nonreal-zero census, or an unsupported all-real
first derivative. Retrieve a directly cited primary count theorem only
when its exact role is essential; unread references stay leads.

Continuation inputs: L018 for actual-Xi analyticity/order/symmetries and
zero-strip facts (read its needed ranges only if the source applies);
L030–L032/C032a for relevance, not assumed signs. Reuse step114 and the
November4/5 derivative/Jensen comparisons. L738 is a contrast about a
generic admissible Fourier kernel, not an input proving this balance.
No cross-notebook use. Mathlib full matching coverage unknown.

Even successful coverage leaves actual critical-point estimates,
boundary control, uniform/global transfer and all mixed signs unresolved.
The next turn is literature_comparison/standard/high. A creative central
attempt requires an independent signed input and a bounded mathematical
test; neither is approved by this nomination.

## Completed source review — step115, 9 November 2026

The nomination above is retained as history. Outcome **NEGATIVE** is
the source-scope finding below, not a refutation of the conditional
theorem, the desired arbitrary-boundary identity, or RH. No lemma,
mathematical script, PROOF or DAG was changed. Classification is
NOVELTY_UNCHECKED: this is source comparison, with no new result claimed.

### Inspected primary input

Young-One Kim, *Critical points of real entire functions and a conjecture
of Pólya*, Proc. AMS **124**(3)(1996),819–830,
[DOI](https://doi.org/10.1090/S0002-9939-96-03083-3),
[published PDF mirror](https://scispace.com/pdf/critical-points-of-real-entire-functions-and-a-conjecture-of-3sul01urof.pdf).
The printed title, journal, page numbers and copyright match the primary
paper. Read pp819–823 through the complete Theorem1 proof, the separate
Theorems2–3 statements, and Example2 p829. Abstract aggregators only
located the paper. AMS returned403; JSTOR supplied no text; mirror PDF
text succeeded. Screenshots returned429 and were not verification.

**Hypotheses and conclusion (Theorem1, p821).** Nonconstant real entire
f of genus1*; real a<b outside J(f). Genus1* means exp(-alpha z²)g(z),
alpha>=0, g real entire of genus<=1. J(f) is the union of the **closed**
disks with center Re(c) and radius |Im(c)| for nonreal zeros c. The
strip-wide nonreal counts 2J and 2J' of f and f' are finite between a,b;
the critical-zero count of f' in [a,b] is K=J-J'. Neither a global strip
nor finitely many nonreal zeros globally is a Theorem1 premise.

**Multiplicity convention (pp819–820).** At a real zero x of f' of
multiplicity m with f(x)!=0, its critical multiplicity is m/2 for even
m; for odd m it is (m+1)/2 or (m-1)/2 according as
f(x)f^(m+1)(x)>0 or <0. Common zeros are excluded from this critical
count. Thus K counts a sign-sensitive selection with multiplicities;
it is not the number of all real stationary points.

**Essential boundary proof (Section2, pp822–823).** Put
B=(sgn(f'(a)/f(a))-sgn(f'(b)/f(b)))/2 when the ratios are nonzero.
For Kim's contour, W=(2pi)^(-1)Delta arg(f'/f)=B by (2.4).
His cited Pólya real-count formula is 2K=N'-N-B; argument principle
gives N'+2J'=N+2J+B. These are the source's equations before cancellation.
Kim uses half-height (b-a)/2, Jensen containment of nonreal derivative
zeros, and (2.3) off the disks; he handles zero endpoint ratios by the
stated endpoint reduction. The real-count equation is imported there
from G. Pólya, *Some problems connected with Fourier's work on
transcendental equations*, QJM Oxford Ser.1(1930),21–34, pp29–30.
That original proof remains unread; Kim's named theorem is the citation,
not a purported independent reproof. The strict sign in (2.3) needs
the nondegenerate zero/quadratic case; a pure exponential has zero
imaginary logarithmic derivative and trivial counts. This qualification
does not certify any Xi endpoint.

### Exact applicability limits and local comparison

L018 establishes reality, evenness and the strict zero strip
|Im z|<1/2. L023 gives order<=1; L024 supplies the Hadamard/genus-one
representation, without real-zero assumptions. These are the appropriate
existing inputs for a later conditional specialization; L018 alone did
not state the required genus fact. The canonical proofs were read in
full. L030/L032/C032a were read for relevance, never as assumed signs.

The requested geometry has fixed half-height1/2, whereas Kim's proof
uses (b-a)/2. A specialization must justify equality of the counted
zero sets using the strict Xi strip and Jensen's derivative containment,
and must account for boundary zeros/multiplicities. It cannot simply
copy the contour or replace ±T outside J(Xi) with boundary-zero avoidance.
The source provides the conditional theorem and the exact endpoint
terms, **no estimate for a boundary crossing a Jensen disk**. We have
not disproved the existence of another general boundary formula.

Theorem3 adds rho+2rho_C<2 and therefore cannot be used without an
unproved bound on the nonreal-zero convergence exponent. Theorem2 is
about high derivatives and supplies no first-step critical count bound.
These stronger-looking conclusions do not remove the exposed premise.
The earlier November4 actual-Xi sign comparison remains applicable:
kernel shape, finite signs and RH-conditional curvature formulas do not
give the required signed critical data. L738 is a contrast only.

Example2 p829 treats exponential times real trigonometric polynomials
through periodic counts, a distinct boundary mechanism. It suggests a
bounded test of whether the **general** Xi-like properties can force
disk-free endpoints. A narrow duplicate check found L052's explicit
trigonometric prefactor zeros and L057's fixed-Hankel masking family;
neither asserts Jensen-disk coverage. Reuse their elementary zero
calculation; do not replay their kernel-concavity or Hankel arguments.

This source review closes one essential coverage gap, but establishes
no new Xi sign, actual endpoint, zero-loss estimate, or RH candidate.
Full matching Mathlib coverage is not checked/unknown. No reproof is
needed merely to cite Kim; a later model certificate is justified only
to test the endpoint implication that the source does not supply.

Queries: exact title/DOI plus pdf; Kim critical zeros theorem Jensen;
Jensen disks real axis cos; Jensen disks cover strip entire. No adequate
endpoint-existence theorem or exact prior countercertificate was located;
this bounded result implies neither novelty nor absence. Unread cited
papers remain leads. No cross-notebook input or zero-free-region work.

### Route decision and discriminator

Retain the conditional count interface; park its application based solely
on boundary-zero avoidance. No independent signed estimate is ready for
a creative central attempt. The separate bounded endpoint test is
prepared in `2026-11-09-kim-disk-free-endpoint-test-115.md`; it receives
separate next-turn approval. A countermodel would reject only the
generic endpoint shortcut; actual-theta endpoint existence and every
mixed sign would remain unresolved. Mathematical exploration usage:0;
no budget reset or scheduler edit.
