# Normalized logarithmic-theta Q_3 — bounded endpoint test

TARGET: Determine the leading nonzero asymptotic sign of L821's normalized Q_3 at both real endpoints, using origin Taylor data through order eight and the exact full n=1 term at infinity, with differentiated actual-theta errors strictly dominated by the leading term.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step632 endpoint comparison in 2026-11-05-log-theta-endpoint-sign-scope.md searched the exact observable, stronger original-coordinate Wronskian results and endpoint statements; no inspected matching sign theorem, no novelty claim. Step610 confluence and step614 audit reused.
SOURCE_EVIDENCE: Csordas https://arxiv.org/pdf/1309.0055v2 (4.2)/Theorem4.1 p10; DLMF https://dlmf.nist.gov/20.2#E3 and https://dlmf.nist.gov/20.2#ii, https://dlmf.nist.gov/20.7#E32, https://dlmf.nist.gov/2.1#ii; Nuttall https://publish.uwo.ca/~jnuttall/det3CAEXP_2.pdf Theorem2.2/proof p4 for coordinate exclusion. Step632 local L016/L019/L021 and L821 proof/audit coverage reused; precise qualifications remain in its assessment.
COMPARISON: Standard theta regularity and the known full-first-summand method support a quantitative specialization; no checked theorem supplies this second-logarithmic Q_3's first nonzero endpoint term or its differentiated relative remainder. Original-coordinate RR3 is insufficient.
GAP: Calculate the two first nonzero terms or record bounded inconclusiveness, with all cancellations and four differentiated remainders controlled; no endpoint sign, global TN3 or Xi transfer is assumed.
REASON: One actual-kernel necessary-condition test is source-ready for separate approval. It uses audited identities and a known asymptotic method; it is not a new central sign-transfer mechanism or an RH result.
LITERATURE_REASON: Supervisor recovery requires direct source URLs in the ready assessment; this turn repairs that omission and verifies the cited regularity passages without repeating discovery or calculating endpoint signs.
SCOPE: Exactly the existing normalized order-three translation observable at v tending to minus/plus infinity. No compact-domain enlargement, minor grid, new normalization, all-real reference-zero argument, global sufficiency theorem or unbounded integral transfer.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
the asymptotic sign of the existing Q_3 at its two real endpoints.
Plausible downstream use: a negative sign excludes global TN3 for
T(x,y)=H(x-y); a positive sign retains only this necessary endpoint
condition. Global nonconfluent signs, lower oscillation, the unbounded
Laguerre interface, mixed/shifted sufficient signs and all degrees
remain independent unresolved claims.

Use exactly L821's H(v)=e^v K(e^v)/m_0, increasing collocation tuples,
and equations(1)–(5), with K from L019, m_0>0 from L021 and
theta-series/modular regularity from L016. The original proof and
step614 audit have been read. Existing L821 compact constants do
not apply outside 1/4<=u<=2. No cross-notebook input is needed.

At u=e^v tending to zero, use Taylor information for the actual K
through order eight, including any odd terms unless their vanishing
is justified. Import Csordas Theorem4.1's parity only after carrying
the recorded coordinate scaling, or use L016's existing modular
identity. Do not reprove a known general parity or analyticity
theorem. Record all cancellations in Q_3; coefficient positivity,
nonzero curvature or nondegeneracy must not be presumed. Control
the Taylor remainder through each of the four D=u d/du derivatives
used in L821, by analytic Taylor estimates with a justified
neighborhood or direct higher-series bounds. Taylor's theorem
cannot be differentiated merely on the basis of a scalar O-error.
If every term tested through this order cancels or its sign remains
unenclosed, preserve the expressions and mark this endpoint
inconclusive; do not extend the order in the same attempt.

At u tending to infinity retain the complete n=1 summand from L019,
including its polynomial prefactor, rather than just exp(-pi exp(2u)).
Use L821's stable factorization/recurrence or an exactly justified
equivalent. Derive separate n>=2 bounds for every required derivative
through order four, with explicit u,c dependence and positive
denominator control; compact majorants and an undifferentiated
relative error are insufficient. Form the base Q_3 exactly before
selecting its leading nonzero asymptotic term, then propagate all
actual-tail errors through the nonlinear expression. This is a
known-method specialization to this coordinate, not a claim of
new full-first-summand machinery. It concerns no Fourier zero
location of the n=1 reference and does not repeat that stopped test.

For each endpoint, seek a nonzero leading term and a rigorous bound
on the final Q_3 remainder eventually at most half its magnitude.
An explicit finite onset is helpful but not required if a proved
error-to-leading-term limit supplies eventual strict domination.
A negative sign abandons global TN3 for this translation kernel;
positive signs establish only eventual endpoint positivity. If
cancellation or differentiated domination remains unresolved,
report that endpoint inconclusive with its exact residual, without
assuming the other endpoint failed. No fitted moments, floating
point plots, grid extension or unapproved alternate test is needed.

Any actual endpoint proof belongs in a canonical lemma with full
hypotheses, qualifications, citations and Mathlib status. Full
matching Mathlib coverage is unchecked. Known sources do not
settle the missing quantitative terms; reproducing their regularity
as a discovery is excluded. Proposed completed classification is
REPRODUCTION. This assessment was newly written in step632. The separate
recovery review in step633 supplies direct source URLs and confirms the
existing SPECIALIZE decision for this exact target; it performs no mathematics.

## Direct-source verification — step633, 2026-11-05

Reused step632's search, duplicate and recorded-failure comparison rather
than repeating discovery. Opened the versioned Csordas PDF above and read
(4.2), all five statements of Theorem4.1 and its attribution paragraph on
printed p10 (PDF page10). Its parity, strip analyticity and qualitative
derivative decay support the recorded regularity scope, not a relative
error after Q_3 cancellation. The originating CNV proof remains unread;
no new claim of its verification is made and it is not essential to the
already proved local-series route.

Opened DLMF20.2 and read (20.2.3) and the two analyticity paragraphs in
20.2(ii); opened 20.7 and read the principal-root convention and (20.7.32);
opened 2.1(ii) and read Ritt's sector hypotheses. The distinction between
fixed-z analyticity in tau and fixed-tau analyticity in z remains essential.
Ritt's sector result remains uninvoked: all four differentiated errors
still require direct bounds or a justified local analytic Taylor series.
These live pages were retrieved on 2026-11-05; their release identifier
was not checked. The direct Nuttall author PDF is accessible; the prior
Theorem2.2/proof comparison is reused, without a new theorem audit.

Disposition: the URL omission is repaired and the exact bounded target
retains SPECIALIZE coverage. This is a process repair, not new literature
evidence for an endpoint sign, a mathematical advance, or a novelty claim.
No mathematical dependency, proof, lemma or script changed. The following
calculation must read the relevant canonical proofs before invoking them.
