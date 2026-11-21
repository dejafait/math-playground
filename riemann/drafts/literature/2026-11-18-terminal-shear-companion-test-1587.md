# One-terminal-shear companion compression test1587

TARGET: Test whether the last-three compression for B=D(I+t E_(d,d-1))A_d(I+t E_(d,d-1))^(-1)D^(-1) forces a uniform c*d trace-norm floor for every positive diagonal D and real t, or admits an explicit degree-dependent sequence with compression cost o(d).
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded discovery1587 compared signed-log integration, real-node barycentric pencils and the specified terminal shear; exact queries, narrow duplicate/failure checks and comparison are in drafts/literature/2026-11-18-root-height-mechanism-source-notes-1587.md. No existing calculation of this exact sheared compression was located; this is no novelty claim.
SOURCE_EVIDENCE: Reopened Schmeisser2002 Section3 definitions/Lemma1 pp211-212 https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf ; reuse primary coverage1523/1524 for Higham2021 identity(*) https://nhigham.com/2021/03/23/what-is-a-companion-matrix/ and Watrous2018 Section1.1(1.168),(1.175),(1.179)-(1.181) pp32-34 https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf . Exact scope/read limits are in source-notes1587; no new general matrix theorem is needed.
COMPARISON: The imported height majorization and compression cover arbitrary square matrices after a verified similarity. Audited C028h covers positive diagonal scaling only; its terminal-three cost formula cannot be reused for this non-diagonal shear without new multiplication and optimization. Known results do not evaluate the proposed finite actual-coefficient cost.
GAP: Verify the shear inverse and similarity, compute only the last-three Hermitian compression, and decide whether its unrestricted normalized infimum stays bounded away from zero or has an explicit o(d) parameter sequence. Neither the compressed formula nor any floor/escape is established here; full cost and H_d=o(d) remain unpaid.
REASON: This is one independently testable extension with specified changed support, rather than another positive-diagonal rescaling. A surviving floor would park this one-shear family; an escaping compression would identify only a regime needing a separate full-cost assessment. This newly written ready target requires separate next-turn approval and is not invoked in its own literature step.
SCOPE: C028h's actual centered companion A_d of C028d, integers d>=3 tending to infinity, C028a's S_2,S_3>0 and established c_(d,1),c_(d,2),c_(d,3); S_d(t)=I+t E_(d,d-1), t arbitrary real, D arbitrary positive diagonal, both allowed to depend on d. Compress (B-B*)/(2i) onto coordinates d-2,d-1,d. No RH, real/simple roots, diagonalizability, bounded t, bounded conditioning or full-cost upper bound is assumed.

## Exact bounded task and downstream threshold

E_(d,d-1) is the matrix unit in row d, column d-1; the orientation is
fixed. D follows the shear on the left as printed in TARGET. Preserve
this order when taking the Hermitian imaginary part; its trace norm is
not similarity invariant. Use the Schatten trace norm throughout.
Verify the inverse and the characteristic-polynomial preservation, rather
than assuming a root-dependent or positive symmetrizer exists. Real
translation from C028d preserves heights, and Schmeisser's majorization
is the existing full-matrix height interface, including multiplicities.

The compression is E*[(B-B*)/(2i)]E with the coordinate inclusion E.
Watrous's p=1 ideal inequality permits a lower bound for the full cost
from this compression, with factor one. Do not invert this implication.
All exterior couplings remain present in the full matrix, even if they
do not enter the compressed calculation. No fourth coordinate, extra
shear, generic GL optimization, coefficient sweep, numerical root solve
or changed actual family is included in this single target.

The full cost would need to be o(d) to pay C028b's RH-equivalent height
criterion. A useful negative test is one fixed c>0 and finite onset,
allowed to depend only on the fixed actual coefficients, with compressed
cost>=c*d for every allowed D,t in every sufficiently large degree.
That stops this one-shear majorant, without lower-bounding actual heights.
If the compression can instead have cost/d->0, give explicit ratios and
t_d valid through the full degree limit, with rigorous bounds; a few small
degrees or an optimizer output is insufficient. This abandons the proposed
compression obstruction only. It neither gives a full-cost upper bound
nor authorizes further research without its own assessment. If neither
test is resolved in one coherent attempt, save the remaining optimization
and stop without extending the family or running a sweep.

C028f/g's uniform root tail and S_F limit give no upper payment here.
C028a/c, C028h and the primitive/derivative stops are contrasts retained
at their exact scopes; their floors are not actual-root lower bounds.
Import the named standard inputs, and supply only the new finite matrix
multiplication and optimization in a later research step. No reproof of
the generic majorization or norm inequality is justified. Matching Mathlib
coverage is unchecked/unknown, not asserted absent.

Classification for later mathematics: REPRODUCTION. Routing: calculation,
standard/high. This is a known-method finite specialization; it is not a
justified creative upper-payment mechanism. The central creative blocker
is still an independent estimate of the complete cost by o(d), or another
estimate forcing the limiting nonreal mass S_F to vanish.
