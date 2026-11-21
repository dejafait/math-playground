# Full-theta right ray: reproduction nomination1640

TARGET: Reproduce Kawano v1's right-ray allowance T_right(p)<=A_+ L^(9/2)/r with A_+<0.096514 on C048c's full closed sector, for the normalized absolute full-theta integral defined in assessment1639.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse completed step1640's exact-ray duplicate/failure search and primary comparison in 2026-11-19-mellin-right-tail-source-notes-1640.md; exact manuscript/horizontal and Kawano/Mellin/tail queries found the primary source, without a matching independent theorem or novelty claim.
SOURCE_EVIDENCE: Kawano Preprints.org202611.0383v1, posted4November2026, DOI10.20944/preprints202611.0383.v1, https://www.preprints.org/manuscript/202611.0383/v1 , Section5.2(28)/Lemma5.1(i)/proof(31) with both sigma cases; AppendixB phi/C_n/B_+ and real t>=1 series estimate; AppendixC domain, width, A_+ and monotonicity, directly read19November2026. Reuse Devroye, Non-Uniform Random Variate Generation(1986), ChapterVII Section2.6 pp299-300, https://luc.devroye.org/chapter_seven.pdf , as assessed in the November5 right-tail scope.
COMPARISON: The source separately assigns A_+<0.096514 to the right tail and derives B_+ by an absolute full-mode tangent envelope on s>=d. Application to this exact T_right requires a justified specialization; AppendixB's different width/cells and L801's different saddle/domain do not transfer numerical bounds.
GAP: Verify full-ray admissibility, complete-theta domination, right phase bound in both real-part cases, positive endpoint decay rate, convergence, exact normalization, A_+ constants and all-sector uniformity; no such tail bound was derived during literature review.
REASON: Accessible source cases and ready effective-envelope coverage permit an independent reproduction without the blocked full-contour import; a citation alone does not certify this preprint's parameter-specific constant or the stronger operational absolute observable.
SCOPE: Newly written ready continuation for separate next-turn approval; REPRODUCTION only, not creative work. Only the exact T_right below and C048c sector are covered; no left tail, global contour, inversion, zero count or sufficient-sign conclusion.

Retain C048c's r=|p|, L=log r>=12, Re p>=-r/(4L),
w=W_0(2p/pi), u_0=w/2, d=1/(3L), h_p,g,K,A_0 and principal
branches. With C048f's R_modes and L799's strip-series identity, use

    T_right(p)=integral_d^infinity
      |K(s)[1-3/(2pi exp(2(u_0+s)))+R_modes(u_0+s)]
             exp(h_p(u_0+s)-h_p(u_0))| ds
                     / |sqrt(pi/A_0)|.

This is initially a nonnegative improper integral, possibly infinite.
No convergence is presumed. The exact source coefficient sought is

    y_0=exp(12)/12^4,
    A_+=[(3/2)exp(1/8)sqrt(6/pi)/(62/25)]
                    sqrt(y_0)exp(-(19/45)y_0).

This is a single right-ray allowance, not the sum of horizontal tails.
Source-notes1640 records the absolute-majorant scope inference and
its qualifications. Establish that scope explicitly; never replace
the integral of the modulus by the modulus of the integral.

Use the whole-ray checklist in source-notes1640. Any use of source(31)
requires stating its hypotheses and checking the complete right-side
argument, including negative Re p and reflection; the preprint's
quantitative inequalities are claims to reproduce, not assumed facts.
C048c's finite estimates do not automatically extend to this ray.
Keep all exact scalar inequalities and numerical evidence in a canonical
result/certificate if the later research attempt needs them. No script
was written or run in this review. Full matching Mathlib coverage is
unchecked.

Continue if the uniform absolute-integral threshold is proved on the
closed, unbounded sector with exact normalization and rigorous endpoint
constant evidence. Otherwise record the precise failed majorant or
missing assumption; failure of a sufficient envelope alone does not
refute T_right or RH. No repeat of blocked supplement searches.

The main gap is L030-L032/C032a actual-Xi all-degree positivity.
This component could help a later full-theta Mellin remainder; left
tails, assembly, zero counts, inversion and sufficient mixed signs remain
independent. No identified central Mellin-to-sign test justifies a
creative nomination. The appropriate next research purpose is
established-route development, not a claim of new mathematics.

