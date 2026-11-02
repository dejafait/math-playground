# Two-frequency signed specialization: working checkpoint

Approved invocation-start target and coverage: drafts/literature/2026-11-01-two-frequency-signed-specialization.md (SPECIALIZE). This is one research calculation, expected REPRODUCTION, not a new arithmetic theorem. Main gap: pointwise initial signs at unbounded heights and all-degree mixed positivity. Test only the nominated two-frequency average.

Read full L619, L620 and relevant L471/L018/L465 ranges; reused the completed source comparison and its failure boundaries. Retrieved primary Hughes–Young v2 Theorem 1.1/(11)–(17) and the complete-sum holomorphy remark. No additional literature assessment is being performed.

Partial reasoning, not yet a certified conclusion: the normalized coefficient square has diagonal coefficient |a_1|^2+|a_p|^2=1, and two conjugate cross terms. Each cross main term has p^(-1/2). The intended contour bound is O(T L^4/sqrt(p)) before normalized jet extraction, because the single-prime B factors should be bounded when log(p)/L is bounded. Retain all six terms; import their complete-sum holomorphy, use separated contour radii, and never differentiate a pole term at collisions. Do not replace p^(-shift) by 1.

Use source eta=1/88, T0=T. Expected raw cross source error O(T^(141/176)); verify length and exponent exactly. The Hardy phase cost can be bounded using the untwisted absolute fourth moments, since |a_1+a_p p^(-it)|^2<=2. This cost is O(T L^5) after signed extraction, deliberately too coarse to determine the fine cross sign but potentially sufficient relative to the positive diagonal T L^6/(840 pi^2). Completion curvature is expected O(T^(-1)L^4), with actual-Xi identity from L471. All these estimates still need a complete write-up.

Continuation/stop test: show the full signed integral divided by T L^6 differs from B_1(c0+c1 z) by o(1), uniformly over the stipulated coefficients, prime and X. A proof stops this particular sign detector. Failure to control a direction below the error is inconclusive; no localization, higher signs or RH follows. Next target after this calculation must be separately nominated, with audits/source review as necessary; PROGRESS.md remains the sole current next-action record.

Completed this bounded test: the full proof and precise actual/required
bounds are now canonical in L621, including source exponent 141/176,
prime local-factor bound <8 and a uniform positive lower spectral margin.
The provisional stop and its qualifications are recorded in ATTEMPTS.
No fine cross sign or pointwise implication is claimed. This working
checkpoint preserves the partial reasoning; it is not a second proof or
current continuation record. Separate critical review remains necessary.
