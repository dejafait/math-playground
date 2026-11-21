# Explicit moving-time heat sum: proposed specialization1373

TARGET: Test the uniform O(Y_-^(-1/4)) approximation of C019j's heat reference by the explicit real deformed Riemann-Siegel sum S_d on the closed band [T/sqrt(2*d),T/sqrt(d)], retaining the moving cutoff and gamma-only normalization as specified in assessment1373.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1373 completed the signed-block source comparison in assessment1372 and searched the local November17 Jensen assessments/working notes/failures for Riemann-Siegel and deformed-sum claims; earlier1367/1368 identify the theorem but do not prove this rate or explicit reduction. No originality claim.
SOURCE_EVIDENCE: https://arxiv.org/html/1904.12438v2 (5)-(24), Corollaries6.4-6.5/(68)-(74), Proposition6.6 and its y=0-relevant bound derivations; C019j statement and scale formulas (8) were inspected. The Gaussian formula's source coverage is reused from1368. Primary formulas and domain were read during review1373; source arithmetic estimates are to be cited, not reproved.
COMPARISON: The effective theorem covers the full required pointwise domain at arbitrarily small positive time, unlike a fixed-time asymptotic or real-zero theorem. The proposed difference is the coupled-scale specialization, conversion from source B_t to m(Y), real conjugate sum and uniform error through cutoff jumps; none is claimed proved here.
GAP: Prove or refute the displayed uniform approximation, including all three source errors, branch/conjugation conventions, integer cutoff thresholds and one d-independent onset. Signed moments, sample margins and counts remain separate.
REASON: Select a covered, independently testable analytic subtarget after the direct signed-block imports fail. Explicit phases and coefficients could support a later new arithmetic mechanism. This newly written assessment receives separate next-turn approval; no calculation or theorem application is performed in its creation turn.
SCOPE: Actual xi with C019j's exact T,m,H_t; integer d tending to infinity; the entire closed band; no RH, simple zeros, division by zeta, frozen time, heat real-zero theorem or effective onset. This is ordinary source specialization, not creative research.
LITERATURE_REASON: The next target changes from (A) to an explicit uniform finite-sum reduction; the current review read its essential effective-source errors. Separate continuation approval is required before research under a newly written assessment.

## Exact proposed test

Retain C019j's T and positive m(Y), and put

    Y_-=T/sqrt(2*d), Y_+=T/sqrt(d), t=t_d(Y)=Y^2/(2*d).

Use precisely Polymath v2's M_t and alpha from (6)-(10), with its
principal-log conventions. This M_t is a gamma-based source function,
not nomination1372's arithmetic mollifier. To avoid that collision write
G_t(s)=M_t(s) in this proposed test. Set

    s_-(Y)=1/2-i*Y,
    s_*(Y)=s_-(Y)+(t/2)*alpha(s_-(Y)),
    N_d(Y)=floor(sqrt(Y/(2*pi)+t/16)),
    S_d(Y)=(16/m(Y))*Re{G_t(s_-(Y))*
              sum_{1<=n<=N_d(Y)} exp((t/4)*(log n)^2)*n^(-s_*(Y))}.

Here n^(-s) uses the real logarithm of n. This N_d denotes only the
source cutoff, not C019j's positive scale N_d(q). The proposed assertion
is the existence of absolute C,d_0>0 with

    sup_{Y_-<=Y<=Y_+} |8*H_{t_d(Y)}(2*Y)/m(Y)-S_d(Y)|
       <= C*Y_-^(-1/4)                           for d>=d_0. (B)

(B) is a nominated specialization, not a result of this literature turn.
Essential local inputs are C019j and its L018/L021 conventions. Polymath
v2 Theorem1.3/Corollary6.5 is the additional named standard input.
No other notebook or local saddle-sign theorem is invoked.

## Applicability work reserved for the mathematical turn

Check the x=2Y,y=0 substitution in (14)-(19)/(68), the factor16 and the
conjugate gamma factors. Keep the exact t(Y) in every coefficient.
Use the effective theorem's domain (5), not a fixed-t asymptotic, and
verify its hypotheses uniformly with one onset from C019j's scales.
Bound the conversion 8*|B_t(2Y)|/m(Y) and all of e_A,e_B,e_C,0 using
the printed bounds (23)-(24). Do not drop the Riemann-Siegel remainder.
No source proof needs reproduction: only the unprinted scale conversion
and combined rate are to be derived. The theorem is pointwise even
when N changes; retain each actual floor value and check that the
claimed uniform bound also holds exactly at those thresholds.

Continue if the complete estimate proves (B); a larger nonvanishing
error or a wrong normalization is a decisive failure of this test.
No zero of H_t or zeta is divided out. An effective numerical d_0 is
not requested. A proof would expose an explicit arithmetic observable
for future signed tests and preserve C019j's zero-safe interface; it
would supply no sign margin, disjoint-block count, actual Jensen root
count, bulk separation, all-degree hyperbolicity or RH resolution.
Those gaps must remain recorded. Matching Mathlib coverage is unchecked.
