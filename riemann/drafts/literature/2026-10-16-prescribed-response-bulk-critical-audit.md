# Source coverage for the prescribed-response bulk critical review

TARGET: Critically audit L419's prescribed-response negative-cone bulk construction, including its fixed weight, measurable support and simultaneous moment calibration.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 154 reused step-150 prescribed-response and step-146/148 mixed-moment assessments; read L419, relevant L368/L369/L390/L410/L414/L416/L418 ranges and the two October-16 failed lifts. Targeted Schur--Horn/equal-diagonal constructive searches identified the primary Carlen--Lieb proof below; no completed matching bulk audit was found in these scoped records and no novelty is inferred.
SOURCE_EVIDENCE: Read Carlen--Lieb arXiv:0904.0734v2, Horn theorem following (1.1) and its full proof through (1.2), pp. 1--2; checked DLMF 1.2.8 equations 25.2.1, 27.4.1--3, 5.11.2, the relevant complex remainder paragraph of 5.11(ii), and 5.15.8. Reuse the already inspected Bui--Hall and selection-framework sources described below.
COMPARISON: Schur--Horn covers pointwise equal-diagonal existence for a real symmetric matrix, not a Borel family, the strict translated cone margin or the prescribed-response calibration. Existing absolute-series/gamma and mixed-moment coverage has unchanged hypotheses. L419's simultaneous construction still needs a separate proof audit; L416's adjustable response is no substitute.
GAP: Audit the fixed power-weight threshold and finite-head gamma limit, Borel matrix branches, uniform strict support after translation, both first means, exact odd cancellation, all 23 quartic errors and common constants/onset. Retain L418 as an unaudited input with its rare cubic unresolved.
REASON: Essential coverage is adequate for one bounded critical proof audit of the unchanged TARGET; the reviewed sources do not already establish L419 or full prescribed-response feasibility. No proof audit, new lemma or mathematical calculation was performed in this literature turn.
LITERATURE_REASON: The new separate critical-audit target includes L419's fixed modulus weight and measurable strict-cone construction, which have not had audit-scope approval; reuse the existing primary inputs without repeating unchanged browsing.

The main gap remains actual negative-Bcal clipping and L413's regulator-
scale/full-error margin toward global mixed positivity. The intermediate
review tests whether L419 genuinely removes the independent bulk
obligation at the prescribed actual response. Its downstream use is to
retain or repair that input before relying on it to isolate the rare
cubic threshold. Do not treat a successful audit as full feasibility.

Essential inputs are L368, L369, L390, L410, L414, L416 and L418.
The earlier step-150 assessment already covers the conditional setting;
reuse it rather than reopen the blocked signed-clipping search. Inspect
the exact source hypotheses only where the new audit requires them.
In particular no critical-jet independence, conditional zeta-moment law,
height relocation or adjustable response amplitude is available.

Check C_j^(1/j)->zeta(5/2)^2, the strict S threshold and fixed k,
the finite-head then tail limit for the gamma harmonic, normalization
against 1-p, the Borel equal-Rayleigh-value construction including
equality branches, the uniform strict Delta margin after translation,
both tiny odd tolerances and the O(log H) bulk cubic identity. Verify
all quantifiers for every sufficiently large real H and all 23 quartics.
No independently chosen coordinate law may substitute for the same kernel.

Continue by validating or repairing an actual error within this scope;
reject the partial claim if a required uniform bound or exact calibration
cannot be justified. Preserve L418's unresolved condition
F_lambda(H)=beta_* (log H)^2+o((log H)^2), the lack of actual/global
critical realization and every regulator/global positivity gap.
Full matching Mathlib coverage is not checked. The preceding paragraphs
retain the proposed audit obligations; step 154 below supplies source-scope
approval only, superseding the proposal's REVIEW_REQUIRED status.

## Completed source comparison — 2026-10-16, step 154

This is LITERATURE / NOVELTY_UNCHECKED / literature_comparison, with
outcome EXPLORATION. It adds a primary matrix comparison and approves
the exact saved review scope. It establishes no new mathematical input
to the RH argument, and does not certify the construction.

### Primary matrix result and its precise limits

Eric A. Carlen and Elliott H. Lieb, *Short proofs of theorems of Horn
and Mirsky on diagonals and eigenvalues of matrices*,
[arXiv:0904.0734v2](https://arxiv.org/pdf/0904.0734v2), 13 May 2009,
pp. 1--2, Horn's theorem immediately after (1.1), proof through (1.2).
For two finite real sequences, spectral majorization of the desired
diagonal is necessary and sufficient for realization by real orthogonal
conjugation of the diagonal eigenvalue matrix. The proof uses a two-by-two
rotation and induction, deleting a matched coordinate and embedding the
smaller orthogonal matrix. Those proof cases were read. The equal-diagonal
case is the standard constant-trace-average specialization. In the later
audit identify the matrix as L419's real symmetric S_H J S_H and verify
that specialization, rather than claim a new equal-diagonal theorem.

This source asserts pointwise existence, not Borel dependence on a
parameter or continuity across coincident diagonal/eigenvalue branches.
L419's coordinate algorithm therefore has a legitimate additional role:
check its radicand, nonzero denominators, equality branches and deterministic
choices directly. No eigenvector selection premise is covered. Import
the general theorem by citation; do not reprove it to inflate the outcome.
The original Horn paper, Amer. J. Math. 76 (1954), 620--630, is identified
in the primary paper's reference [2] but was not independently read.
Mirsky's unrestricted eigenvalue/diagonal theorem is not a substitute
for orthogonal conjugation and is not used.

### Absolute right-line and gamma inputs

Checked the online NIST DLMF, version 1.2.8 (2026-09-15), accessed
2026-10-16. [25.2.1](https://dlmf.nist.gov/25.2#E1) gives the zeta
series for Re s>1. [27.4.1--3](https://dlmf.nist.gov/27.4#E1) states
the multiplicative Euler product under absolute convergence and its
zeta specialization in the same half-plane. These domains cover L419's
fixed 5/2 line. They support the fixed integer-power series, not an
unproved critical-line phase distribution. The audit must verify the
full coefficient majorants and the order of the finite-prime and large-j
limits in L419's existing C_j argument. No height-dependent power k is
covered or required.

[5.11.2](https://dlmf.nist.gov/5.11#E2),
[5.11(ii)](https://dlmf.nist.gov/5.11#ii) and
[5.15.8](https://dlmf.nist.gov/5.15#E8) supply sectorial digamma and
separate trigamma expansions, with complex digamma remainder control.
The arguments 1/4+it/2 stay in a closed sector away from the negative
axis. Reuse L369 (6)'s phase-of-Q bounds, not phase-of-Qb bounds; no
asymptotic remainder may be differentiated without control. The new
weight requires only fixed-frequency integration followed by a uniform
absolute tail limit. Its cancellation is still to be audited locally.

### Reused moments and framework, with no changed hypotheses

Reuse the inspected Bui--Hall source in
[step 146](2026-10-15-compatible-jet-second-moment-scope.md) and
[step 148](2026-10-15-compatible-jet-second-moment-critical-audit.md):
*On the derivatives of Hardy's function Z(t)*, Bull. Lond. Math. Soc.
55 (2023), 2304--2323, DOI 10.1112/blms.12859,
[arXiv:2304.05178v1](https://arxiv.org/pdf/2304.05178v1#page=1),
Introduction p. 1, equation (1) and preceding odd-order display.
It covers unconditional ordinary derivative pairs through order two;
L416's separately audited sharp weighted specialization supplies the
six constraints. Do not reinterpret them as moments conditional on the
actual response. No underlying unread Hall theorem is a new premise.

Step 148 also records the inspected Hughes--Young Theorem 1.1/(12)--(17),
Bui--Hall quartic and Curran--Heycock absolute-envelope inputs. L419
requires no new twisted moment, growing cutoff or shifted derivative
order: the existing actual quartic data are retained through L418's
homogeneous rare component, while the proposed bulk errors are lower
order. Checking that preservation, every one of the 23 coordinates and
the absolute bounds remains part of the mathematical audit. L418 has
no separate critical audit; verify its load-bearing mass, second-moment,
first-mean and homogeneity claims as needed, without evaluating its cubic.

Reuse [step 150](2026-10-15-compatible-jet-actual-response-marginal.md),
including its inspected Jaskiewicz--Nowak Theorem 1 and Aumann Theorems
1--4 with their integrability and measurable-graph qualifications.
They preserve moments of an existing supported kernel or give selections;
they do not create the required moments. L419 uses explicit finite Borel
atoms instead, so neither purification nor a new conditional independence
theorem is an essential import. A global atomic replacement would lose
the uniform height marginal and remains outside scope.

### Duplicate/failure comparison and the bounded audit decision

Read L419's full construction and the relevant input definitions;
compare L416's audited freedoms with L418's exact actual graph. The
October-16 sign-only lift remains undecided because sign-restricted
integrals are unevaluated. The capped-radial record retains its cubic
failure and original missing-bulk obligation; L419 claims only the latter
as partial progress. Neither record supplies a completed audit of L419,
and neither is a global prohibition on this different calibration.
No cross-notebook input or blocked signed-clipping search was reopened.

The queries were `Schur Horn theorem real symmetric matrix equal diagonal
orthogonal conjugation Horn 1954 primary paper` and `equal diagonal real
symmetric matrix constructive proof continuous measurable orthogonal basis
Schur Horn`. Broader Schur--Horn extensions and the Leite--Richa--Tomei
1999 paper were search leads, not inspected theorem inputs. No failed
search establishes novelty; a full matching construction was not supplied
by the inspected sources.

SPECIALIZE approves one later proof audit of exactly TARGET. Continue
by validating the claimed partial bulk or repairing a specific error
within that scope. Abandon reliance on it if its fixed-weight threshold,
Borel support, exact odd cancellation or common uniform constants cannot
be justified. A verified bulk would isolate the independent rare-cubic
condition F_lambda(H)=beta_* log^2 H+o(log^2 H); it would not establish
that condition. Actual/global critical realization, actual clipping,
L413's full-error regulator margin and global mixed positivity remain
unresolved. Full matching and supporting Mathlib coverage were not checked
in this source review; unknown coverage is not absence.
