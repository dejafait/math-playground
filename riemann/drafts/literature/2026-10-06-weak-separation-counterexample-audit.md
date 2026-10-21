# Coverage for the exact weak-separation counterexample audit

TARGET: Critically audit L371's exact analytic-pair counterexample, including physical discriminant normalization, common-zero multiplicities and the unbounded distinct-zero deficit after every finite onset change.
CHECKED: 2026-10-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the exact differential-pencil/Sturm/Obreschkoff searches and local duplicate screen in 2026-10-06-discriminant-zero-interlacing.md and 2026-10-06-discriminant-weak-separation.md; reopened their three primary sources for this audit's hypothesis comparison.
SOURCE_EVIDENCE: MIT 18.034 Spring 2009 Lecture 9 Theorem 9.1 and complete proof, printed pp. 1–2; Borcea–Brändén–Shapiro Master4 §3.1 printed p. 9 definitions and Theorems 9–10; DLMF §1.13(i), equations 1.13.1–1.13.6; full L371 proof and L370 (1)–(2), normalization discussion and L367 (1)–(3) read for audit scope.
COMPARISON: The inspected common-ODE and hyperbolic-polynomial results do not decide this arbitrary analytic-pair obstruction; the saved exact elementary proof therefore needs a direct critical audit, rather than a separation-theorem import.
GAP: Verify the existing proof's ordinary jets, positive physical divisor, zero multiplicities, Wronskian degeneracies and exact finite-onset count subtraction; this review does not certify those computations.
REASON: Approve the newly specified audit by reusing adequate separation coverage; no new lemma, broader hypothesis or blocked arithmetic input is needed.
SCOPE: Audit only the saved L371 real entire pair under D≤0 and strict L(G)>0, counting distinct zeros with closed endpoints and arbitrary fixed finite onset; no actual-family representation or quantitative response bound is included.
LITERATURE_REASON: The new continuation requires separate approval of its critical-audit scope; reuse the ready weak-separation comparison and check its applicability instead of reopening the blocked actual-count route.

## Primary-source comparison

[MIT 18.034, Spring 2009, Lecture 9](https://ocw.mit.edu/courses/18-034-honors-differential-equations-spring-2009/0cdeb657491010f0f8c60aa49f2d5248_MIT18_034s09_lec09.pdf),
Theorem 9.1, printed pp. 1–2 (PDF pages 2–3), was reopened with its
complete proof. It concerns independent solutions of one second-order
homogeneous ODE with continuous coefficients. Its proof uses a
nowhere-zero Wronskian to force alternating signs between successive
zeros. L371's abstract hypotheses include neither that equation nor
Wronskian nonvanishing. This is a hypothesis comparison, not an import.

J. Borcea, P. Brändén and B. Shapiro, *Pólya–Schur master theorems for
circular domains and their boundaries*, [author manuscript Master4](https://staff.math.su.se/shapiro/Articles/Master4.pdf),
§3.1, printed p. 9 (PDF page 9), definitions and Theorems 9–10 were
reopened. The Wronskian characterization presupposes hyperbolic
polynomials and degree difference at most one. Hermite–Biehler uses
stability of f+ig; Obreschkoff uses hyperbolicity of all real linear
combinations. Their strict clauses additionally exclude common zeros.
A first differential-pencil inequality does not supply those premises.
Only these statement-level comparisons are used; their proofs are not
imported. The manuscript revision date remains unverified.

[NIST DLMF §1.13(i)](https://dlmf.nist.gov/1.13#i), equations
1.13.1–1.13.6, online display retrieved 2026-10-06, was reopened.
Equation 1.13.4 uses the physical Wronskian convention of L370.
Abel's identity and the fundamental-pair equivalence concern solutions
of the same equation with analytic coefficients. They do not warrant
nonvanishing for an arbitrary analytic pair. The current release number
is not recorded. The definition is supporting terminology; no ODE
result is imported into the proposed audit.

## Local scope, relevance and test

The main gap remains actual-theta global mixed positivity and L367's
total signed margin relative to its remainder. The intermediate target
is a critical audit of the already written L371 obstruction, not another
separation lemma. Its downstream use is to decide whether the generic
bounded distinct-count route must remain stopped, and to identify what
extra actual-family information would be essential before reopening it.

The complete L371 proof was read to identify the audit obligations,
without performing that audit in this literature-only step. L370
(1)–(2) and its physical divisor discussion, with L367 (1)–(3), cover
the requested normalization. Any use of a normalized-function
Wronskian must retain the envelope curvature term; the audit can instead
use the ordinary physical jets throughout. The existing failed-route
record ATTEMPTS/2026-10-06-weak-discriminant-distinct-count.md and its
history were checked. L371 already contains this example, so another
lemma duplicating it is unnecessary. The original source search found
no matching arbitrary-pair theorem; that does not establish originality.

Continue by auditing each displayed identity, exact zero list and
multiplicity, the endpoints in [π,2πn], and subtraction of fixed counts
on half-open initial intervals for every fixed onset. Confirm that the
claim uses distinct counts rather than multiplicity counts, and that
physical normalization changes only by a strictly positive divisor on
the audited eventual ray. Retain the generic-route stop if all these
checks succeed. If a sign, count, normalization or hypothesis fails,
record and repair or withdraw the affected conclusion; do not silently
replace it by a simplicity or no-common-zero variant. This is the
continuation/abandonment test, not its outcome.

Essential inputs are L371's full proof and L370 (1)–(2), with L367
(1)–(3) for coefficient conventions. No common-zero restriction for
actual theta, signed S(t) comparison, G counting law, total margin or
higher positivity has been proved by this review. Those independent
gaps, the actual-count source blocker, sharp-mean blocker and L365 stop
remain untouched. Unread arithmetic leads in the original assessment
are irrelevant to this bounded audit and remain unread.

DECISION EXPLORE permits the subsequent critical audit with classification
REPRODUCTION or POTENTIALLY_NEW, without certifying novelty or correctness.
Full matching Mathlib coverage is not checked; unknown availability is
not evidence of absence. No lemma, mathematical script, DAG edge or
argument overview changed in this literature-only step.
