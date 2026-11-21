# Coverage assessment: the completion-parameter boundary index

TARGET: Assess whether an argument-principle theorem gives a full-multiplicity crossing index for G_u(s)=zeta'(s)+u(H'/H)(s)zeta(s), 0<=u<=1, on one L957-admissible interval, retaining all boundary and common-zero terms and requiring no bound on K.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step128 searched the exact completion family and zero-count homotopy, boundary-root argument principles and multiple-root crossings; narrow local xi/critical/boundary assessments and failures contain no matching ready index. Primary passages and representative exact queries are recorded below; no novelty or exhaustive absence is inferred.
SOURCE_EVIDENCE: Inspected Gantumur2015 Theorem20 p9; Eisermann author PDF compiled2012-04-01 Theorem1.5 p4, Corollary4.7/Remark4.8/Corollary4.9 p16 and Section5.2 p18; Boudabra–Markowsky2006.12545v1 Theorems2/4 and Section2/Lemma3 pp2–4. Reused step127's original completed-zeta source notes.
COMPARISON: The ordinary/generalized residue count excludes contour roots; Eisermann covers polynomial edge orders but excludes vertex roots for multiplicativity and all parameter-boundary roots for homotopy invariance; Boudabra–Markowsky supplies an unsigned intersection lower bound, not the requested signed parameter index. None directly supplies the full-order fixed-interval transfer.
GAP: No inspected theorem supplies the signed index with intermediate contacts, stationary corners and persistent common factors for this analytic family. Neither an independently estimable signed boundary datum nor an arithmetic saving is established; K=O(T), K=0 and global positivity remain open.
REASON: Stop these direct index imports on their inspected hypotheses, without declaring the completion mechanism impossible. Replace the global parameter-count construction by a separately assessed local terminal-root discriminator; derive no formula in this literature turn.
LITERATURE_REASON: Changed observable from a quantitative count bound to the local completion-parameter crossing index, whose essential boundary-contact and multiple-zero cases were not covered by the prior assessments.
SCOPE: Completed literature-only comparison for the exact fixed-interval target. EXPLORE records the bounded search without an adequate match; it does not approve an unrestricted index construction. The distinct local continuation is assessed separately in 2026-11-10-xi-completion-terminal-splitting-128.md.

## Original nomination and its stopping test

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. An intermediate index might let a later arithmetic test
distinguish a signed boundary loss from a large unsigned zero census.
It would not prove K=O(T), K=0, preservation at higher derivatives,
or any all-degree positivity statement.

Here H(s)=s(s-1)pi^(-s/2)Gamma(s/2)/2 is the actual completion factor.
Fix sufficiently large T and the same L957/L958 admissible positive
endpoints T<a<2T<3T<b<6T. In s-coordinates consider the left
half-strip rectangle 0<=Re(s)<=1/2, a<=Im(s)<=b. The endpoints
avoid Xi zeros, but Xi' may be stationary there; L958's closed-count
correction must be retained. Do not assume that intermediate G_u
have no zeros on its horizontal or vertical boundary. Keep or
justify every indentation, endpoint collar and common-zero order.
No simplicity, zero separation, RH or finite global nonreal census.

Start with exact searches for zero-count homotopy, boundary crossing
indices and the completed zeta combination. Retrieve precise theorem
hypotheses and essential multiple-root/contact cases before larger
proof extracts. Reuse step127's primary source notes; do not repeat
the completed derivative-count/proportion comparison or make Conrey
PDF access a dependency. If a standard theorem covers the target,
cite it and isolate only actual applicability obligations. Do not
derive an uncovered formula during that source review.

Continue only if the source produces a well-defined, full-order
local index with an explicit boundary datum that can support a
separate discriminating test. If it merely names the unknown
N'-N-E or assumes a zero-free entire parameter boundary, record
that exact limitation and abandon this proposed import. Failure
to find a theorem is exploration, not proof of impossibility.
The next mathematical target, if any, must be separately assessed.

Essential local inputs: L018, L023/L024, L957 and L958. They provide
the completion/genus, endpoint availability and terminal count
conventions; they provide no intermediate-parameter boundary
control or uniform epsilon limit. Full matching Mathlib coverage
unknown. No cross-notebook input. A creative proof attempt is not
yet justified: an independently estimable signed boundary term
and its bounded mathematical discriminator are still missing.

## Completed source comparison — step128, 10 November 2026

Outcome **NEGATIVE** is a source-scope result: the proposed direct
imports below fail the specified gate. It is not a counterexample
to an index theorem, a bound on K, or mathematics beyond the sources.
No lemma, mathematical script, PROOF or DAG was edited this turn.

### Residue counts and homotopy invariance

Tsogtgerel Gantumur, *Isolated singularities and meromorphic functions*,
16 April 2015, [author notes](https://www.math.mcgill.ca/gantumur/math249w15/residue.pdf),
Theorem20 p9: f is a nonzero meromorphic function on Omega, g is
holomorphic, and the piecewise C1 loop is null-homotopic in Omega;
Ord(f,z)=0 at every contour point. The weighted order sum equals
the integral of gf'/f divided by 2pi i. Its proof computes the
residue as g(c)Ord(f,c). Multiplicity is already included; allowing
contour roots is not. Thus it cannot by itself justify the proposed
parameter-boundary passage.

Michael Eisermann, *The Fundamental Theorem of Algebra made effective:
an elementary real-algebraic proof via Sturm chains*,
[author preprint](https://pnp.mathematik.uni-stuttgart.de/igt/eiserm/publications/roots.pdf),
compiled 1 April 2012; published bibliographic counterpart:
Amer. Math. Monthly119(9)(2012),715–752,
[DOI10.4169/amer.math.monthly.119.09.715](https://doi.org/10.4169/amer.math.monthly.119.09.715).
Numbering here refers to the inspected preprint. Theorem1.5 p4
counts polynomial interior roots with full order and edge roots
with half order, assuming no vertex root. Corollary4.7 and Remark4.8
p16 retain the vertex restriction: the latter exhibits a product
with a fixed vertex root for which multiplicativity fails.
Corollary4.9 explains counting through linear factors. Section5.2,
Theorem5.4 and Corollary5.5 p18 require the whole homotopy to avoid
zero on the boundary. The proof cancels opposite parameter edges
and applies the zero-free rectangle lemma on subdivisions.

These restrictions matter here. G_u is not a polynomial in s;
no polynomial-replacement certificate was imported. L957's endpoint
choice controls Xi, not every G_u. L958 expressly allows stationary
endpoints, which correspond to possible completed-derivative corner
zeros. Neither the half-edge convention nor a formal polynomial
approximation removes the needed common-factor/corner and uniform
boundary analysis. We do not transfer homotopy invariance through
zero, or claim an integer closed count from half weights alone.

### An analytic extension that genuinely permits boundary zeros

Maher Boudabra and Greg Markowsky, *A variant of Cauchy's argument
principle for analytic functions which applies to curves containing
zeroes*, [arXiv:2006.12545v1](https://arxiv.org/pdf/2006.12545v1).
The retrieved PDF has cover date25 November2021 and v1 footer
19 June2020; this identifies the inspected artifact without
assuming that the differing dates specify a later arXiv revision.
Read Theorem2 p1, its entire Section2 proof and Lemma3 pp2–4,
and Theorem4 pp4–5. For nonzero holomorphic f and a smooth Jordan
curve inside its domain, Theorem2 gives at least 2m+lambda distinct
preimages of any line through zero on the curve: m is the interior
zero count and lambda the boundary count, both with orders.
Theorem4 handles piecewise smooth curves with a ceiling correction
using each boundary root's order and interior angle.

The proof indents outward around each boundary zero and controls
the local angular derivative using its factorization into a power
and a nonvanishing factor. These are explicit multiple-root and
corner cases, not an assumed simple transverse crossing. The
conclusion is nevertheless an unsigned lower bound on intersections
for one function; it supplies neither their signed cancellation nor
parameter crossing directions, and no common-factor bookkeeping
between G_u slices. Thus it does not meet the nominated index test.

### Search, comparison and route decision

Representative exact queries were `"zeta" "completion" "homotopy"
zeros derivative`, `"argument principle" "boundary zeros" parameter
crossing multiplicity theorem`, `"zeros" "crossing" "argument
principle" "parameter" theorem boundary analytic`, `"generalized
argument principle" "boundary zeros" theorem`, `"argument principle"
"zeros on" contour generalized paper`, `"Eisermann" "winding"
"boundary" zeros`, and `"Kim" "critical multiplicities"
"perturbation"`. Local searches were confined to relevant xi,
critical and boundary source/failure paths. Step127's derivative-count
comparison and direct-import stop were reused. No other notebook
was read, and no Conrey-access retry was needed.

A multiple-imaginary-root Puiseux paper and delay-system-specific
crossing results appeared as leads; their theorems were not inspected
and are not coverage. The ESAIM2020 parametric second-order delay
paper was opened at its title page only and supplies no imported
theorem. The general local-power and Rouché machinery, rather than
those specialized systems, suffices for the separately proposed
terminal-root test. Its inspected supporting statements and remaining
specialization are in the next assessment.

The global index import is parked: no independently testable signed
boundary term was supplied. The narrower continuation asks whether
the local u->1- branch count is only a different description of
Kim's existing critical weight. Equality would be a concrete reason
to stop seeking an independent sign gain from that local splitting;
a different term would need its own later assessment. No answer is
derived here, and no global parameter formula is approved.
All intermediate-boundary, endpoint-collar and uniformity obligations
remain open. Full matching Mathlib coverage is unknown. The main gap
L030–L032/C032a and the higher/global transfer gaps are unchanged.
