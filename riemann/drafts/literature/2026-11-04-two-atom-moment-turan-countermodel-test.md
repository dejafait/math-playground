# Two-atom moment-compatible countermodel — bounded construction gate

TARGET: Attempt a moment-compatible D_(5,4)<0 countermodel in b_n=(1+w r^n)/(2n)! on r=p/16 (1<=p<=15), w=2^j (-8<=j<=8), using exact screening and a complete position-dependent Turan certificate for at most one survivor.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step411's completed moment-compatible comparison searched exact factorial/moment/Turan/Toeplitz and two-atom/cosh/infinite-log-concavity combinations; no matching result for this family was located. Its primary evidence and search limits are recorded in 2026-11-04-moment-compatible-turan-minor-comparison.md; no novelty inference.
SOURCE_EVIDENCE: Direct primary PDFs https://arxiv.org/pdf/2610.12237v1 (Xie–Zhang–Zhang, Section2.1, Lemma2.1 p.5, Theorem2.3 pp.6–7, Corollaries2.5–2.6 pp.7–8) and https://arxiv.org/pdf/0808.1065v2 (McNamara–Sagan, Lemma2.1 p.4) were accessed in step412; statements and relevant proofs agree with step411 scope. No family-specific countermodel is imported.
COMPARISON: Explicit atomic moments separate the positive-measure obligation from the missing all-order obligation. The index-dependent criterion offers a concrete certificate method; a finite screen and a fixed number of iterates cannot complete it. Real-rootedness is not an allowed premise.
GAP: No grid point, determinant sign, analytic curvature bound, stopping function, finite boundary certificate or normalization transfer has been verified. The combined countermodel remains a proposed construction.
REASON: This is one finite, independently falsifiable test of the added moment constraint, using a materially new all-order certificate method rather than reusing L772's unrestricted tail. Failure ends this bounded family attempt without claiming a sign theorem for all positive measures.
SCOPE: Only the grid, minor and all-order certificate obligations below; no actual-Xi sign, theta realization, arbitrary atomic measures, other determinant orders or grid expansion is covered. Prepared in step411; direct-source recovery review approved this unchanged target in step412. Research remains deferred to the next invocation.

LITERATURE_REASON: Supervisor recovery identified missing direct source URLs in this ready assessment; step412 repairs that evidence field and checks the cited statements, without repeating discovery.

## Direct-source recovery review (step412)

On 2026-11-04 both versioned PDFs above opened successfully. Rechecked
Xie–Zhang–Zhang Section2.1 and Lemma2.1, including the first-failure
proof and fixed-support boundary qualification; Theorem2.3 and
Corollaries2.5–2.6, including their proofs, branch convention and
integer-interpolation qualification. The source requires positivity
through each position’s stopping depth; an infinite depth requires
already established positivity at that position. Corollary2.6 requires
holomorphy near the closed disk, reality on its real diameter,
Re h_0 >= eta > 0 throughout the disk and eta R^2 >= 128.
It does not certify those hypotheses for this family.
McNamara–Sagan Lemma2.1 and its preceding proof require a nonnegative
sequence with the factor inequality at every index; they do not turn
a finite tail sample into a global certificate.

This is a citation/process repair and separate approval of the existing
EXPLORE gate, not a new theorem comparison or mathematical advance.
Step411’s bounded duplicate/overlap search and L772 stop evidence remain
in force; no expanded search, new lemma or calculation was performed.
Mathlib coverage remains unchecked. The exact target, grid and closure
obligations below are unchanged.

## Mathematical purpose and inputs

The main gap remains actual-Xi exceptional signs and all-degree mixed
positivity. The proposed intermediate result would refute their inference
from positive moments plus entire convergence plus strict infinite
log-concavity alone. It would leave actual-theta realization and actual-Xi
signs unresolved. Failure would give evidence only about this grid and
this certificate method.

Essential notebook inputs are the conventions of L021 and the generic
obstruction L772. The completed step411 comparison contains the primary
citation, exact half-line stopping hypotheses, disk bound, source-proof
read limits and finite-atomic qualification. L738 is a contrast, not an
all-order premise; L766 and Liu–Mao are unused. No cross-notebook input.
The quoted actual a_n convention differs by 1/(8*4^n); any claimed
normalization invariance must be justified during research.

For each parameter point, propose the positive measure
mu=delta_1+w delta_r on [0,infinity). Its proposed moment coefficients
are exactly those in TARGET. This is the definition of the construction,
not a verified lemma. The research turn must justify positivity, the
moment identity and entire convergence. It must use zero extension only
at negative indices, with every iterate taken on the full half-line.

## One bounded attempt and its decision test

There are 255 rational parameter points. First compute
D_(5,4)=det[b_(4+j-i)]_(i,j=0)^4 exactly at every point. For negative
determinants only, check positivity through depths1–4 at indices0–8
using enough initial entries for every dependency. Do not truncate the
sequence at the largest stored index or replace its right tail by zeros.
These tests are necessary screens; they are not an all-order certificate.
Retain exact signs and failures, including zero determinants/iterates.

If no point survives, end the attempt with that precisely bounded
negative or inconclusive result. Do not widen parameters during the
same attempt. Otherwise select at most one survivor, in increasing
p and then increasing j, and attempt the full all-order certificate
from the assessed local stopping criterion. It must include a proved
tail cutoff, valid analytic/sequence agreement on all required shifted
indices, admissible logarithm branches, quantitative disk lower bounds,
and finite boundary stopping certificates with the original n=0
boundary. An index-dependent depth may be used; there must be a proof
covering every n and every subsequent iterate.

Continue this bridge only with a complete joint certificate or a
materially new, discriminating input. If the selected point fails any
required inequality, record the failing index/depth/bound. If the
analytic closure is unfinished, save that reasoning and its precise
unpaid condition; do not call a finite survivor a countermodel or
renew the route merely by checking more iterates. The local criterion
is sufficient, not necessary, so failure of its hypotheses does not
exclude all-order positivity by another mechanism.

Write full finite certificates under scripts/coefficient-countermodel/;
print only counts, actual/required bounds, failures and paths. A later
proof, if completed, belongs in its own canonical lemma with the source
citation, all qualifications and honest Mathlib coverage. No construction
or mathematical script was written in the preparing literature turn.
This is difficult development using a known criterion, not a creative
actual-Xi mechanism. No full matching Mathlib result was checked.
