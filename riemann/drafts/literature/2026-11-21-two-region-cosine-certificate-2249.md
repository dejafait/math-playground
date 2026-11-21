# Fixed two-region actual-theta certificate2249

TARGET: Attempt the fixed two-region certificate J_x>0 on [14,29/2] times [0,1/16] and I_x>0 on [14,29/2] times [1/16,1], including complete derivative/index/spatial tails, the u=0 extension, and the actual-root interface to C919m.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded exact/stronger Fourier-division, shifted-cosine and divided-difference searches plus scoped2230-2248 duplicate/failure checks; no matching sign theorem identified. Full record in drafts/literature/2026-11-21-two-region-cosine-source-notes-2249.md; no novelty inference.
SOURCE_EVIDENCE: Direct primary URLs: https://kconrad.math.uconn.edu/blurbs/analysis/diffunderint.pdf ; https://dlmf.nist.gov/3.5.ii ; https://openstax.org/books/calculus-volume-1/pages/5-3-the-fundamental-theorem-of-calculus . Reconfirmed during recovery2250; previously inspected Strang--Herman Calculus1 Section5.3 Theorems5.4-5.5; Conrad Differentiating under the integral sign Theorem12.3 p16 and Examples12.1-12.2; Tao245B notes0 Theorem3(4)-(5),Theorem4(1)-(2). Reuse2230/2234/2232 for Csordas1309.0055v2 Theorems4.1-4.5, Tuck2006 pp133-135, DLMF3.5(ii),(3.5.6)-(3.5.8), and Strang--Herman Calculus2 Theorem6.7; exact links/hypotheses and unread-original qualifications are in source notes2249.
COMPARISON: The known tools cover calculus and validated integration; C919m supplies the exact derivative/origin interface and derivative decay, C919n only a root-qualified origin neighborhood, C919o the exterior u>=1. None establishes these two fixed signed boxes or their effective differentiated tails. Specialize only those missing bounds and the exact assembly; do not reprove imported general theorems.
GAP: Both strict rational box margins, cancellation-preserving endpoint evaluation, uniform differentiated theta/spatial tails, closed-cell numerical errors and root-qualified gluing remain unproved. Arbitrary removal and actual-Xi all-degree positivity remain independent gaps.
REASON: The nomination now has essential ordinary-tool coverage and a specific unpaid compact interval. A bounded calculation can discriminate its fixed certificate; another generic-model audit, finite-root count or unchanged approval cannot.
SCOPE: Actual L019 K and L058 Xi; observables exactly as nomination2248, split1/16 and closed x bracket[14,29/2] unchanged. Root conclusions only for14<x<29/2,Xi(x)=0,multiplicity allowed. Reuse C919m/C919o for the analytic interfaces, C919n as local context, C919f for methods/contracts only. No census, zero-free region, arbitrary-removal or all-degree theorem.

## The unchanged observables

    I_x(u)=integral_0^infinity K(t+u) cos(xt)dt,
    J_x(u)=integral_0^infinity [(K(t+u)-K(t))/u] cos(xt)dt (u>0),
    J_x(0)=integral_0^infinity K'(t) cos(xt)dt (proposed extension).

These definitions nominate a test, not a proved continuity or sign.
The necessary specialization and precise source qualifications are in
[source notes2249](2026-11-21-two-region-cosine-source-notes-2249.md).
The endpoint must use cancellation before error estimation; separate
absolute errors divided by u are disallowed as a bound through zero.

Before a sign pass, save the analytic plan and one fixed computational
setup, including the finite derivative orders, cutoffs, meshes, Taylor
orders, precision and required positive rational thresholds. Prove all
regularity/interchange conditions and explicit omitted-region bounds
for the chosen integrands; C919f's undifferentiated moment constants
are not automatically reusable for translated K'. Every derivative
actually used needs complete tails. Uniform lower bounds must cover
every closed cell of both boxes and include all faces and u=0.

Reuse the existing arithmetic contracts only after checking their actual
use. Save the full certificate; print bounds, thresholds, failures and
paths. Distinguish an inconclusive enclosure from a certified nonpositive
value. Retain a failure without shrinking the box, moving the split or
automatically retuning the run. A nonroot countervalue rejects only the
stronger box assertion. Claim one-removal decrease only after proving
the actual-root conversion and both joins, including u=1.

If positive margins cannot be certified in this bounded attempt, record
the precise failed region or bound and preserve the unfinished analysis.
No assertion about RH follows either way. The result would be an ordinary
source-covered local specialization; REPRODUCTION is the intended
classification, not certified originality. Full matching Mathlib coverage
is unchecked. Conrad refers out for his proof; Tao omits the general
proofs; original Wintner/Spira proofs and optional Spigler remain unread.
None is falsely reported as independently recertified.

This continuation was written during literature step2249. Recovery2250
completed its separate source-URL check and retained SPECIALIZE for the
unchanged target. No calculation or new mathematical derivation was
performed during preparation or recovery. See the recovery history for
the exact statement checks; source notes2249 retain the full comparison.
