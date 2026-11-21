# Gaussian extension: completed source comparison1630

TARGET: Audit Kawano v1's Gaussian-extension allowance T_ext(p)<=0.099276 L^(9/2)/r on L>=12, Re(p)>=-|p|/(4L), where T_ext is the normalized pair of omitted horizontal complex Gaussian tails for C048c's A_0 and d.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused comparison1627/source-notes1627, November5 Gaussian assessments, full L800/audit and global-import stop; exact Kawano/Gaussian-extension/0.099276 query found the primary preprint. Broader complex Gaussian tail/Re/erfc search mostly returned probability results, not matching inspected theorems. No novelty inference.
SOURCE_EVIDENCE: Kawano Preprints.org202611.0383v1, posted4November2026, DOI10.20944/preprints202611.0383.v1, https://www.preprints.org/manuscript/202611.0383/v1 , Section5.2(28)/Lemma5.1(i)/reflection convention; AppendixB paragraph preceding B_g and displayed B_g; AppendixC opening curvature/width and A_g/monotonicity paragraph. Directly reinspected NIST DLMF7.7.6 https://dlmf.nist.gov/7.7.E6 and7.8.1-7.8.2 https://dlmf.nist.gov/7.8.E1 https://dlmf.nist.gov/7.8.E2 on2026-11-19. Complete relevant extraction and qualifications: 2026-11-19-mellin-gaussian-extension-source-notes-1630.md.
COMPARISON: Source B_g charges the pair of omitted real-parameter Gaussian tails with the same complex normalization; AppendixC assigns A_g<0.099276 on the saved domain and width. Gaussian integration/Mills bounds cover the method, while the uniform parameter/constant comparison remains reproduction. L800 uses a different rotated contour, width and real curvature; automatic transfer stays unavailable.
GAP: Prove or rigorously fail the unchanged exact T_ext threshold using audited C048c(9)-(10) and its normalization; pay two-tail multiplicity, convergence, curvature direction, normalization loss, unbounded-L monotonicity and the exact endpoint constant. None is newly proved in this literature turn.
REASON: The missing primary definition, coefficient and proof cases are accessible and match the proposed component. SPECIALIZE permits a separate known-method reproduction, not import of aggregate(29) or a new mathematical discovery.
SCOPE: Completed literature-only step1630 for unchanged TARGET; permitted future classification REPRODUCTION. Separate next-turn approval precedes mathematics. No other theta mode, horizontal tail, full remainder, zero count, inversion or sufficient sign theorem is covered. Full matching Mathlib coverage unchecked.

## Completed comparison1630

The [source extraction1630](2026-11-19-mellin-gaussian-extension-source-notes-1630.md)
supplies the missing primary cases and exact A_g formula. The target
below is retained verbatim. Its source-scope test passes; its mathematical
inequality remains unproved locally. Only a separate reproduction is
ready for approval. The earlier REVIEW_REQUIRED nomination is preserved
in history1629; this replaces its incomplete source decision.

## Prospective test and relevance

The main gap remains L030-L032/C032a actual-Xi all-degree algebraic-square
positivity. One audited extension cost could contribute to a future full
theta-Mellin remainder, without supplying a zero count, inversion theorem
or sufficient mixed-sign implication.

Use the same p, r, L, principal Lambert branch w, u_0=w/2 and
d=1/(3L) as C048c. The nominated quantity is

    A_0=4p(1+w)/w^2,
    T_ext(p)=|integral_{(-infinity,-d) union (d,infinity)}
                       exp(-A_0 s^2) ds| / |sqrt(pi/A_0)|.

The integration variable is real and the square root is the principal
Gaussian branch. The prospective threshold is
T_ext<=0.099276 L^(9/2)/r on the full closed C048c sector, including
both imaginary signs, positive real p, permitted negative real parts,
the radial boundary and unbounded L. This source reading now passes
comparison1630; it is not a newly proved bound or an imported full remainder.

Essential local input: C048c's audited geometry, curvature and exact
normalization, with C048a's branch and C048b's geometry as needed for
hypothesis verification. No full-theta tail estimate or source total
allowance is a premise. The relevant prior comparison rejects automatic
L798-L800 transfer; it does not prohibit a correctly assessed new test.

The literature decision test is whether the primary source's definition
and hypotheses match this exact quantity and preserve the stated cost.
The definition and hypotheses match in comparison1630; the precise
method is recorded in source-notes1630 for separate reproduction approval.
If a later check finds a mismatch, preserve it and refine the
target before mathematical work. Failure of a proposed absolute majorant
alone would not refute T_ext or RH. Other theta modes, horizontal tails,
full remainder assembly and the all-order sign bridge remain independent.

Full matching Mathlib coverage is unknown. No new central creative
mechanism is justified merely by the local estimate; the missing
Mellin-to-sign implication still needs a specific new testable input.
