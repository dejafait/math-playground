# Large-level theta concentration test — 2026-09-23

Gap: exterior signs D_n(Ξ;a)≥0 through the height-only K(a) of L266. Intermediate target: obtain these signs from concentration of the positive associated kernel near t=0. Plausible use: combine an explicit sign range with the negative-witness bound to exclude possible nonreal centers. Remaining steps include all lower indices and a uniform height range.

The discriminating test is whether the sufficient threshold 2a²V_n≤1 in [L267](../lemmas/L267-associated-kernel-variance-sign-test.md) reaches relevant n≤K(a), not merely arbitrarily large n. L253/L254 obstruct separate signing and index pairing; this test instead uses the total positive kernel before Fourier transformation. L255 covers a compact interval already. The finite-level counterexamples remain relevant and no generic sufficiency inference is made.

The standard-library script `python3 scripts/laguerre/concentration_probe.py` computes even moments by positive quadrature, then the exact variance formula. It uses mesh sizes 0.002 and 0.001 on 0<u<4, eight theta terms, and floating-point arithmetic. The meshes agree in the displayed digits, but no truncation, cancellation, or roundoff error certificate is supplied. These are discovery data only:

| n | estimated V_n | sufficient |a| ceiling |
| --- | --- | --- |
| 1 | 0.0206917096 | 4.9157163 |
| 4 | 0.0160396919 | 5.5832489 |
| 16 | 0.009260672893 | 7.3479083 |
| 64 | 0.004118767878 | 11.017964 |
| 128 | 0.002565575887 | 13.960230 |
| 256 | 0.001547018694 | 17.977828 |

For scale, L266's exact A(a) and the standard identity |Γ(1+ix)|²=πx/sinh(πx) give

log A(a)=−π|a|/2+5log|a|+O(1),
K(a)=π|a|/(2log 4)−5log|a|/log 4+O(1).

Thus the required cutoff grows linearly in height. No corresponding rigorous asymptotic for V_n has been proved here. The probe suggests V_n is of order log n/n, which would require levels of order a²log|a| for this sufficient test, far beyond the witness cutoff. This heuristic is explicitly not a theorem. For example n=128 reaches only height about 14 in the probe, whereas height 100 has a numerical K(a) of about 100.

Assessment: EXPLORATION, one unresolved turn of three. L267 records the exact elementary reduction, not a substantive exterior sign theorem. No rigorous negative range result or new certified exterior signs are claimed. Do not extend the table or present it as positivity evidence. Continue once with a rigorous saddle/concentration estimate for V_n to decide whether this particular bound merits further work. A failed sufficient test would not refute actual theta positivity or concentration methods with oscillatory cancellation.
