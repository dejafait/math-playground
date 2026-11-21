# Near-left full-theta allowance: reproduction nomination1644

TARGET: Reproduce Kawano v1's near-left allowance T_nearleft(p)<=A_- L^(9/2)/r with A_-<0.091191 on C048c's full closed sector, for the normalized absolute full-theta integral on -1<=s<=-d defined in source-notes1644.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step1644's exact-side search, L802 statement comparison and November5 left-scope/audit records in 2026-11-19-mellin-left-allowance-source-notes-1644.md; the primary match was Kawano, with no matching canonical bound or novelty inference.
SOURCE_EVIDENCE: Kawano Preprints.org202611.0383v1, posted4November2026, DOI10.20944/preprints202611.0383.v1, https://www.preprints.org/manuscript/202611.0383/v1 , Section5.2(28)/Lemma5.1(i)/left-side proof(31) including both sigma cases and reversed integration, AppendixB C_n/B_-/B_f and real theta-tail bounds, AppendixC domain/width/A_- and monotonicity, inspected19November2026. Reuse Devroye(1986), ChapterVII Section2.6 pp299-300, https://luc.devroye.org/chapter_seven.pdf , left-envelope coverage from the completed November5 assessment.
COMPARISON: The source's split at s=-1 and nonnegative tangent majorant support the chosen absolute finite component; this interpretation must be justified explicitly. AppendixC prints the coefficient, but AppendixB's finite-band constants and L802's different saddle/height/normalization do not transfer numerical bounds.
GAP: Prove whole-segment admissibility, complete-theta domination, left phase and its cases, tangent direction/rate, exact absolute normalization, A_- coefficient and closed-sector uniformity; no allowance was established during review.
REASON: Essential coverage is accessible for an independent known-method reproduction without the stopped global import; citation alone cannot pay the operational observable and quantitative hypotheses.
SCOPE: Newly written ready continuation for separate next-turn approval. REPRODUCTION only; no distant-left/origin allowance, full-contour identity, inversion, zero count or sufficient mixed-sign conclusion.

Use exactly C048c's r=|p|, L=log r>=12, Re p>=-r/(4L),
w=W_0(2p/pi)=U+iV, u_0=w/2, d=1/(3L), h_p,g,K,A_0 and
principal branches. Use F and T_nearleft as defined in
source-notes1644, including the entire n>=2 series and integral of
moduli on [-1,-d]. The exact constant sought is

    y_0=exp(12)/12^4,
    A_-=[(3/2)sqrt(6/pi)/(133/54)]
                           sqrt(y_0)exp(-(1007/2430)y_0).

Follow source-notes1644's full checklist. Prospective inputs are
C048c geometry/normalization and L799 general strip convergence and
identity(4). C048g is a comparison and downstream companion, not a
left-side premise; L802's audited inequality is not imported.
State any additional inputs. No global contour, continued origin,
L801 inequality or unread supplement may be assumed. Extending a
scalar envelope integral to -infinity must not extend the source's
x>=1 phase domain or finite-segment theta estimate there.

Kawano's quantitative inequalities are conclusions to verify, not
assumptions. Check both real-part cases, both signs of Im p, real p,
both angular boundaries, L=12 and unbounded L. Keep rigorous constant
evidence in a canonical result/certificate if needed; sampling cannot
establish uniformity. Matching Mathlib coverage is unchecked.

Continue only with a uniform proof paying this threshold or an
informative obstruction to its sufficient majorant. Record failures
without refuting the observable or RH; repeating a failed mechanism
requires materially new input. No mathematics was derived in preparing
this nomination. L030-L032/C032a actual-Xi positivity remains the main
gap; distant-left/origin, assembly, zero counts, inversion and sufficient
signs remain independent. This is established-route reproduction.
