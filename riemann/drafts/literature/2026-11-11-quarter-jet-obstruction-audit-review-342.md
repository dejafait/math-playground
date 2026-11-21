# Quarter-jet obstruction audit — source assessment

TARGET: Assess source coverage for a conceptual audit of C997l's quarter-jet obstruction, including the ellipse coefficients, lower-interval factor and original-TV rates.
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step343 read full C997l, reused reviews329/332 and audit334's working record, and compared the exact quarter-jet stop342. Targeted Bernstein-ellipse coefficient/Laurent searches reached Trefethen's primary ATAP chapter source and NIST DLMF; no inspected matching complete-response theorem was identified and no novelty is inferred.
SOURCE_EVIDENCE: Newly inspected Trefethen ATAP chap8.m, development branch retrieved 2026-11-11, Theorems8.1/8.2 and complete proofs, source lines104-169; NIST DLMF v1.2.8 (2026-09-15), 1.10(iii)/(1.10.6-7), annulus hypotheses and compact absolute/uniform convergence, and 18.5.1. Reuse review332's inspected Axler rank-nullity and finite-measure contracts and C997c's audited spectral specialization.
COMPARISON: Theorem8.1 covers the classical ellipse coefficient bound; Theorem8.2 covers the truncated Chebyshev projection error. DLMF18.5.1 covers finite polynomial evaluation at exterior real arguments. None supplies C997l's lower-interval factor, fractional degree budget or final original-TV rates; C997g/audit334 explicitly treats full jets only.
GAP: Independently audit C997l(1)-(20), especially the pole-free neighborhood, coefficient normalization, finite exterior sum, combined moments, degree/onset, both spectral supports and all uniform original-TV rates. These are local application obligations; essential source coverage is now available.
REASON: Primary approximation contracts fill the distinct source gap and justify a separate conceptual audit classified REPRODUCTION. This literature step neither verifies C997l nor derives any new response bound or broader packet obstruction.
LITERATURE_REASON: Newly written C997l uses fractional jets and a Laurent/Chebyshev approximant outside review332's full-jet audit scope; this separate comparison supplies the essential missing contracts without repeating the packet research.
SCOPE: Proposed audit of fixed kappa=1, degree<=n, fixed admissible A, original TV=1, m=floor(n/4) exact complete-response jets at 2, target z_star=1+i/8 and uniform closed J=[15/8,17/8] bounds. No smaller or approximate jets, varying parameters, general point inequality or actual-zero transfer.
COVERED_TARGET: Audit C997l's quarter-jet obstruction, checking the ellipse coefficients, finite lower-interval factor, combined spectral moments, fractional degree budget and both original-TV rates.

## Preserved nomination — step342

The following nomination was REVIEW_REQUIRED at step342. The separate
step343 comparison below supersedes that source gate only.

This file nominates a separate literature-only step. It does not
approve the audit, repeat the packet construction or reopen old stops.

The eventual audit should inspect C997l's hypotheses, feasibility and
target-maximizer compactness, its combined moments from C997c(4)-(6),
and its quantitative degree budget. C997e supplies only the real phase
and inherited fixed-A scope. C997g/audit334 and C997i/audit339 are
comparisons, not fractional-jet mathematical premises. C997k's unpaid
spectral tail is irrelevant to this proof. No cross-notebook input.

Reuse accessible primary contracts already recorded in review332:
Axler's Fundamental Theorem of Linear Maps and NIST DLMF1.9.30-31.
Retrieve only the missing essential primary Laurent/Chebyshev
coefficient statement and relevant proof case if those records do not
suffice. Compare exact known ellipse approximation results with the
proof's annulus 1/4<=|w|<=4, pole exclusion and finite evaluation for
real |y|<8. A general minimax theorem cannot silently replace this
specific combined-support estimate. No broad repeat search or quota
browse is requested; blocked nonessential weighted-source leads remain
nonessential.

Decisive later audit checks are whether ell=ceil(n/log(d)) and
N=floor(n/4)-1-ell leave the claimed degree and onset; whether the
complete response, rather than one asymptotic branch, annihilates Q;
and whether the rates -1/96 on J and -1/24 at the target survive the
original TV and both lower contributions. Nonzero target feasibility
is not needed for the obstruction. The source-comparison turn must
not itself derive new lemmas or certify the mathematical audit.

Independent point-bridge, selected/both-sign, C997a(8), original-assay,
reconstruction, signed-complement, regulator, L993, L984(H) and
actual-Xi gaps remain. Full matching Mathlib coverage is not checked.

## Separate literature-only comparison — step343, 11 November 2026

Main gap: L030-L032/C032a actual-Xi positivity and L966/L968 signed
forcing; L984(H) remains unpaid. Intermediate target is source coverage
for the exact C997l audit. A reliable subclass obstruction would guide
point-bridge packet selection after C997c branch recovery. It would
not settle the independent realization or signed-recovery gaps.

### Primary contracts actually inspected

L. N. Trefethen, *Approximation Theory and Approximation Practice*,
SIAM, 2013, Chapter8, Theorems8.1/8.2, equations(8.1)-(8.3).
Read the [primary chapter source](https://raw.githubusercontent.com/chebfun/ATAP/development/chap8.m),
source lines104-169, including both complete proofs. Retrieved
2026-11-11 from the Chebfun ATAP development branch; no commit hash
or edition identity for that branch was independently established.
The [author's book page](https://people.maths.ox.ac.uk/trefethen/ATAP/)
identifies the 2013 and 2019 editions and the publishable chapter format.
Theorem8.1 assumes analytic continuation to the open Bernstein
rho-ellipse, rho>1, with a uniform bound M. It gives
|a_0|<=M and |a_k|<=2M*rho^(-k) for k>=1.
Its proof treats both holomorphy across the boundary and the merely
open-annulus case via smaller circles. Theorem8.2 gives the projection
error <=2M*rho^(-N)/(rho-1); the interpolant has a different bound.
Its proof uses the full tail (4.8), also inspected in the
[primary Chapter4 source](https://github.com/chebfun/ATAP/blob/development/chap4.m).
Thus projection coefficients, not sampled interpolation coefficients,
are the relevant contract. No general approximation theorem needs a
new proof here.

NIST DLMF, version1.2.8, release2026-09-15, retrieved2026-11-11:
[1.10(iii), equations1.10.6-7](https://dlmf.nist.gov/1.10#iii).
Read the full annulus statement: holomorphic f on
r_1<|w-w_0|<r_2, 0<=r_1<r_2<=infinity, and a coefficient contour
of radius strictly between r_1 and r_2, traversed positively once.
The Laurent series converges absolutely and uniformly on compact
subsets. The future audit must justify an open neighborhood of the
closed annulus before placing its contour at radius4; analyticity only
on the open annulus would require the limiting-circle case instead.
Reuse review332's Cauchy1.9.30-31 coverage; the Laurent contour need
not enclose a holomorphic disk.

[DLMF18.5.1](https://dlmf.nist.gov/18.5.E1), same version and date,
states T_j(y)=(w^j+w^(-j))/2 for y=(w+w^(-1))/2, with w complex
and nonzero. The displayed y is real, which suffices for C997l's
lower-interval evaluation. Both real exterior sides and y=+/-1
must be included. This polynomial identity permits evaluation of
the finite truncation outside [-1,1]; it does not permit summing the
infinite Chebyshev series at those exterior arguments.

Trefethen's [2016 author example](https://www.chebfun.org/examples/approx/EntireBound.html)
was also inspected as a corroborating coefficient statement, not as
the proof source. Search-result text from a third-party book mirror
was not used. The Oxford first-six-chapters PDF was opened to locate
the chapter structure, not as evidence that Chapter8 was read there.
No essential source remains inaccessible.

### What the citations cover, and what remains to audit

C997l's Laurent c_j convention must be matched with the source's
Chebyshev a_j convention, retaining the exceptional constant term.
The sources cover this coefficient/truncation mechanism under their
analyticity and norm hypotheses; they do not verify the proposed B_s,
the pole exclusion or the numeric estimates (10)-(12). Applying them
requires retaining the n- and z-dependent M rather than treating an
analytic family as uniformly bounded without a charge.

The audit must check the finite lower-support polynomial sum using
the real exterior identity, then check its product with the proposed
lower-interval factor and its allocated degree. Neither Theorem8.2
nor an approximation estimate on [-1,1] supplies that distant-support
cost. C997l(8)-(9),(13)-(15) and the complete, combined moment identity
(7),(16) therefore require independent verification. The two spectral
measures cannot be cancelled independently. The rates claimed in
(18)-(20), including the target's imaginary part, original TV=1 and
constants uniform in P and fixed admissible A, are still unaudited.
The current comparison performs none of those calculations.

Reuse review332's Axler *Null Spaces and Ranges*, Fundamental Theorem
of Linear Maps, PDF pp17-24, for linear existence, and its Axler MIRA
9.10/9.41(b) and Tao Theorem43 coverage for the finite complex measures.
The existing C997c audit322 supplies the exact spectral representation
and variation bounds; its narrower J support needs its displayed
density formula (4), not a newly assumed Fourier envelope. C997e
supplies the real phase and fixed admissible-A scope only. Compactness
of the normalized finite-dimensional kernel must still be justified;
neither rank-nullity nor existence implies a nonzero target.

### Duplicate/failure comparison and bounded decision

Read C997l in full, C997c's spectral proof range, C997e's parameter
statement, review329, review332 and audit334's working record, plus
stop342 and the preserved fractional-jet working record. Reuse
review332's failure comparison315/316/318/327/331 without reopening
their proofs. C997g's audited full-jet Taylor construction is a useful
comparison, not a theorem about fewer jets. C997i's large-A stop and
C997k's unpaid spectral tail are not premises. Review329's weighted
norm/growth tools do not decide this complete-response integral; no
repeat search of its blocked nonessential sources is warranted.

Queries included `Trefethen Approximation Theory Approximation Practice
Theorem 8.1 8.2 Chebyshev coefficients Bernstein ellipse pdf`, `NIST
DLMF Laurent series annulus 1.9 Chebyshev polynomial complex variable
18.5`, and a targeted search for the primary ATAP chapter source.
Exact-response and two-interval discovery evidence is reused from
reviews329/332; no inspected theorem directly supplies the claimed
fractional-jet stop. This is not evidence of novelty.

SPECIALIZE for the exact COVERED_TARGET, a later conceptual audit using
known tools, classified REPRODUCTION. Continue to accept the scoped
stop only if all (1)-(20) survive the complete-support, degree and
uniform-rate checks. Repair or withdraw any failed assertion while
preserving its original evidence; do not optimize or extend the
parked design in that audit. The next invocation receives this newly
ready continuation for separate approval. No lemma, mathematical
script, DAG edge or PROOF.md argument changed in this literature turn.
Full matching Mathlib coverage is unchecked; no absence is inferred.
There is no cross-notebook mathematical input.
