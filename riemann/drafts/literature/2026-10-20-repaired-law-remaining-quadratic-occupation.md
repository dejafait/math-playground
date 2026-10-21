# Source coverage: remaining quadratic occupation tests of the repaired law

TARGET: Evaluate the complete compact-height prime-2 occupation residuals of L441's unchanged repaired law for the tests eta(t/H)sin(t log 2)xy/log(2+t) and eta(t/H)sin(t log 2)y^2/log(2+t).
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 264 reused the step-256/260/262 occupation and Poisson assessments, searched the scoped October 19--20 assessments/history/failure records for the two test polynomials and changed raw entries, and searched externally for occupation-measure quadratic xy/Liouville and Hardy/zeta occupation tests. No inspected source evaluates these complete repaired-law residuals; the search establishes no novelty.
SOURCE_EVIDENCE: Rechecked Lasserre--Henrion--Prieur--Trelat arXiv:math/0703377v1, Sections 2.1--2.3, (2.7), (2.10)--(2.12), pp. 3--5, and Aistleitner--Berkes--Seip, JEMS 17 (2015), Section 3, p. 1527, finite character identity and Lemma 1 (23), including its iterated-circle justification; read L424's ordinary dynamics, L438 (9)--(17), L440's full-second/weighted-Poisson and angular interfaces, L441's exact perturbation and completed audit record, L419's exact forms and K, and L429's original threshold conditions.
COMPARISON: The necessary identity accepts arbitrary C^1 tests on fixed compact state/control boxes, hence does not restrict the test to x^2. Finite Poisson coefficients and local averaging tools are ready. None evaluates the new complete xy/y^2 residuals; L440's special zero-angular-mean cross-entry proof does not cover every raw entry, and L441 cancels only its stated x^2 residual.
GAP: Calculate both exact transport polynomials and their complete signed raw-second averages under L441's unchanged law, retaining slow derivatives, all rare terms, translation, the full covariance and bounded recentered perturbation; prove the required weighted estimates under the original cutoff or identify an unresolved signed term. No residual formula, value, sign or new estimate is established here.
REASON: Essential coverage is adequate for one later REPRODUCTION specialization on this exact target. The change is in polynomial tests and law-specific estimates, not in the imported identity's hypotheses; approval does not assert those estimates succeed or authorize a new law, cutoff or realization theorem.
LITERATURE_REASON: The two changed test polynomials were explicitly REVIEW_REQUIRED at invocation; the prior ready records approved only the x^2 separation, repair and audit. This comparison resolves that changed scope without repeating a ready calculation target.
SCOPE: Both tests in TARGET only, with L440's eta, fixed omega=log 2, ordinary x=f,y=f'/log(2+t),z=f''/log(2+t)^2 for f in C^2, and exactly L441's complete Borel family on the full eventual real-H ray; necessary compatibility only.

## Target and use

Global mixed positivity remains the main gap. The proposed intermediate
target examines the two remaining members of the quadratic test block in
x,y after the x^2 test has been repaired. Its plausible downstream use is
to determine whether that same representative meets these additional
necessary kinematic identities, or to isolate a new explicit defect.
This is a different test of the unchanged repaired law, not a repetition
of L440's separation of the old law or a claim of trajectory sufficiency.

Use precisely L440's eta, height interval, ordinary normalized trajectory
coordinates and fixed prime frequency. The full test functions appear in
TARGET; no derivatives or residual formulas for them have been derived
in this turn. The law is exactly L441's, including its reselected Borel
bulk atoms. Do not introduce a new covariance correction, change the
cutoff, or assume that atom choices are continuous.

## Source comparison and exact applicability

J. B. Lasserre, D. Henrion, C. Prieur and E. Trelat, *Nonlinear optimal
control via occupation measures and LMI-relaxations*, SIAM J. Control
Optim. 47 (2008), 1643--1666, DOI 10.1137/070685051,
[arXiv:math/0703377v1](https://arxiv.org/pdf/math/0703377v1),
Sections 2.1--2.3, pp. 3--5, (2.7), (2.10)--(2.12), supplies the
necessary integrated C^1 identity with both terminal values. Its setting
has smooth dynamics, compact state/control sets and bounded measurable
controls. These are the only source claims used; no optimization or
sufficiency theorem is imported.

Apply that source with state (x,y) and control z, using L424's already
proved ordinary dynamics. At each fixed H a C^2 trajectory fits finite
compact boxes; the law's finite-H bounds also make the tested integrals
well-defined. The boxes need not be uniform in H. Both proposed tests
are C^1 on them, including the zero extension of L440's eta. Endpoint
vanishing follows from the same eta, independently of the polynomial.
The arbitrary-test statement therefore covers both tests. It does not
give their law averages, uniform integrability, or a trajectory for a
kernel. No z derivative or third derivative of f is required. Only the
test and ordinary dynamics are differentiated; H, cutoff, probabilities,
calibration coefficients and the selected Borel basis are held fixed.
Writing the two explicit specializations is deferred to mathematics;
reproving the general occupation theorem is unnecessary.

C. Aistleitner, I. Berkes and K. Seip, *GCD sums from Poisson integrals
and systems of dilated functions*, JEMS 17 (2015), 1517--1546,
DOI 10.4171/JEMS/537, [published primary text](https://ems.press/content/serial-article-files/32047?nt=1),
Section 3, p. 1527, identity before Lemma 1 and (23), supplies finite
polydisc character moments for positive radii below one; its justification
integrates successively over the coordinate circles. The arbitrary
multi-indices and complex coefficients in Lemma 1 impose no sign
restriction on a later fixed trigonometric multiplier. The finite radii
in L429 are p^(-1/2). No infinite critical-line Euler product is imported.

L440's direct finite-Fourier estimate (8)--(12), with original cutoff
size control, is the local moving-height input. The source's finite
Haar formula alone is not such an estimate. Apply the written estimate
only within its hypotheses; any new weighted comparison remains an
explicit mathematical obligation under the same cutoff. L440 (13)--(16)
also supplies quantitative angular averaging, including bounded
measurable zero-mean angular functions and Lipschitz amplitudes. Whether
the newly needed entries have those means or require a different signed
bound is unproved. No new actual-zeta second-moment theorem is essential
to evaluating a conditional law already given by its full raw matrix.
The ready fixed-twist sources remain available at their recorded scope,
but are not used to assume an actual sine limit.

## Local comparison, duplicates and recorded failures

The ready assessments reused are
`drafts/literature/2026-10-19-prime-two-quadratic-occupation-test.md` and
`drafts/literature/2026-10-20-bounded-covariance-repair-critical-audit.md`.
The former records the primary quadratic-growth integrability comparison
and fixed-twist hypotheses; its smooth-test caveat is unchanged. The C^1
source above suffices, so no new smooth approximation theorem is needed.

L438 (9)--(17) gives every high/intermediate raw second and the translated
bulk matrix, not merely six integrated numbers. L441 (2)--(6) changes
only the specified recentered xy covariance, retaining those components.
The completed step-263 audit is reused as a local input, not rerun here.
L419's K and exact response forms distinguish raw moments from centered
covariance. Continuity of the reselected atoms is not available and not
needed for these quadratic integrals.

L440's signed intermediate xy estimates (17)--(22) exploit particular
angular means and tie control. They are not blanket estimates for other
entries: L438's absolute intermediate second budget is O(sqrt(log H)).
Retain it until a justified signed comparison or the exact coefficient
makes it negligible. Exact integrated seconds do not imply conditional
or prime-weighted cancellation. The same restriction applies to the
full constant covariance correction and bounded mean products.

Scoped local searches found no completed evaluation of these two tests.
L439 and `ATTEMPTS/2026-10-19-full-poisson-law-gaussian-occupation.md`
stop the fixed Gaussian nonzero-limsup diagnostic, not polynomial tests.
L440's separation of the old law and L441's x^2 repair remain valid at
their original scope. L428's bounded normalized-density obstruction
does not reject this unchanged growing-Poisson law. No stop is removed.

Fresh external queries were `"occupation measure" "xy" "quadratic"
Liouville`, `"Hardy" "occupation" "quadratic" zeta`, and
`"GCD sums from Poisson integrals" "23"`. The useful primary lead was
the published Poisson text, inspected as specified above. Other search
hits supplied no inspected theorem for the exact residual target and
are not mathematical inputs. Search failure is not evidence of novelty.

## Decision test and approved continuation

SPECIALIZE approves exactly TARGET for one later RESEARCH / REPRODUCTION
calculation attempt. Success means a complete
asymptotic residual or a rigorous nonvanishing obstruction for each test,
with all raw second terms and slow derivatives retained on the full
real-H ray. A bound that cannot resolve the scale-one comparison is an
unfinished estimate, not evidence of nonzero residual or impossibility.
Continue only with a concrete remaining signed term and a discriminating
bound; an unresolved calculation does not license another repair.

Essential inputs: L441's exact changed conditional raw second matrix and
step-263 audit; L440's complete occupation and weighted-Poisson interfaces;
L438's full rare/mean/covariance interfaces; L419's exact J,b,K; L429's
original cutoff. If exact intermediate entries require expansion, read
only the needed L421/L437 direction formulas. These are local inputs;
no cross-notebook result is intended.

Unresolved and not assumed: the values of the two residuals, exact
finite-H cancellation, other occupation identities, actual sine limits,
growing-character uniformity, actual/global realization, actual clipping,
capped nondegeneracy, L413's full-error regulator margin and global mixed
positivity. Full matching Mathlib coverage has not been checked. This
coverage record contains no new mathematical derivation or novelty claim.
