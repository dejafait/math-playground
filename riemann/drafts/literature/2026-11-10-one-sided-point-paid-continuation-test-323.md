# One paid upper-half-plane point-continuation test — ready nomination

TARGET: Test C997c's one-sided point inequality at 1+i/8 by upper-half-plane continuation, with a fixed positive TV-error exponent and subexponential amplification of data on [15/8,17/8], uniformly over finite complex slope measures.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse completed review322's step323 bounded searches, exact-range comparison and recorded-failure check; no matching theorem or exact-range obstruction was established, and no novelty is claimed.
SOURCE_EVIDENCE: Grabovsky–Hovsepyan, Theorem2.7/(2.20)-(2.22), published pp149-150, Section5 pp162-168, https://sites.temple.edu/yury/files/2023/06/general_curve.pdf ; Trefethen, Lemma2.1 p904 and Theorem5.2/proof p908, https://people.maths.ox.ac.uk/trefethen/trefethen_ac.pdf ; Demanet–Townsend, Theorem2 pp3-4 and Section6.3-6.4 pp20-22, https://math.mit.edu/icg/papers/stable-extrapolation.pdf . Review322 records the completed comparison. Reuse C997c(1),(4)-(6) and audit322, L997(4), C997a(1)-(2) and reviews312/318/320; standard named Plancherel and finite-complex-measure Fubini are available tools.
COMPARISON: Known conditional continuation estimates do not pay the original slope-TV norm or settle the fixed-kappa/every-epsilon rates. Their unrestricted worst cases do not supply slope measures. Only the explicit quantitative specialization below is nominated.
GAP: Justify any Hardy/domain-norm hypothesis from C997c's complete finite integral and account for its n dependence before testing the requested additive estimate. Exact-range realizability is essential for any impossibility conclusion.
REASON: Source coverage is ready for one bounded established-route development attempt. This newly written continuation receives separate approval next turn; no research or quantitative specialization was performed in step323.
SCOPE: One proof attempt on the exact inequality below, using upper-half-plane conditional continuation and the already proved positive spectral representation. No new branch extraction, primal slope construction, selected-response identity, full-quartet strip-truncation replay or actual-Xi transfer is covered.

For every integer n>=2 use C997c(1) exactly, I=[7/4,9/4],
Gamma_in=[15/8,17/8], z_star=1+i/8, every finite complex Borel
measure mu on I and V=||mu||_TV. Keep both integration intervals,
both beta contributions in cosh(3t/8) and K's -1. The question is
whether fixed finite C and kappa>0 exist such that for every epsilon>0
there are finite C_epsilon,N_epsilon with

    |H_n^+(z_star;mu)| <= C*exp(-kappa*n)*V
           + C_epsilon*exp(epsilon*n)
                       *sup_(gamma in Gamma_in)|H_n^+(gamma;mu)|

for all integers n>=N_epsilon and every mu. The same C and kappa must
work for all epsilon; constants are independent of n and mu. No norm
or positivity premise on mu beyond finite complex TV is allowed.

After separate approval, save partial reasoning before development.
Use the exact positive-frequency representation already in C997c(4)-(6).
For any application of the cited H2 theorem, justify density/membership,
global norm, interval rescaling and local data norm from that representation.
A bounded-domain alternative may use the inspected three-lines/propagation
contracts only with a paid domain norm. A carrier removal or weighting
requires an exact identity and all its original-V and data costs; none
is supplied by this nomination. Import the standard theorem, proving
only the necessary specialization. Do not reproduce its general proof.

Passing evidence is a complete fixed-kappa/every-epsilon inequality.
If this continuation certificate retains a positive exponential
amplification rate, or supplies only a conditional fractional-power
estimate with no paid conversion, record precisely that limitation and
stop the certificate. It does not prove every operator impossible.
An impossibility claim instead requires a rigorously admissible sequence
of slope measures and bounds incompatible with the displayed quantifiers.
No unrelated Hardy extremizer, scalar multiplier optimum, finite fit
or failed upper envelope can replace that evidence. A failed test may
remain inconclusive and need not create a lemma. Repeating it requires
a materially new input, informative obstruction or refined mechanism.

Main gap: L030-L032/C032a actual-Xi positivity and L966/L968 signed
forcing, with L984(H) unpaid. A passing point estimate could make local
branch recovery useful for a later selected-response test. Essential
inputs are L997(4), C997c(1),(4)-(6), its audit322 and the cited sources;
C997a(1)-(2) provide context, not an assumed selected-response equality.
Both-sign/selected normalization, original assay feasibility, actual
reconstruction, signed recovery, infinite-zero complements, regulator
uniformity, L993 and L984(H) remain independent gaps. No cross-notebook
input or RH candidate. Mathlib matching coverage is unchecked and unknown.

## Separate source approval and URL repair — step324, 10 November 2026

The unchanged TARGET is approved for one research turn under EXPLORE.
The direct primary URLs are now included in SOURCE_EVIDENCE; all three
PDFs were accessible on this date. This is the requested recovery repair,
not an additional search for a mathematical mechanism. Reused review322's
proof-case inspection and recorded-failure comparison; no new theorem,
specialization, extremizer or rate conversion is claimed.

Rechecked Grabovsky–Hovsepyan Theorem2.7 (PDF page10, printed p149):
upper-half-plane H2 membership, unit global norm and boundary L2 data
norm are explicit premises. Trefethen Theorem5.2 (PDF page8, printed
p908) retains the global unit sup bound and the geometry and analyticity
hypotheses inherited from Theorem5.1; its connecting-arc proof is on the
same page. Rechecked both sampling cases of Demanet–Townsend Theorem2
(PDF page3, manuscript p3); its real extrapolation target and ellipse
bound remain outside a direct application here. Versions are the same
author-hosted copies identified in review322, not newly versioned results.

No source directly proves the nominated slope-TV inequality or supplies
an admissible slope-measure counterexample. Readiness means coverage for
the bounded test, not that its conclusion holds. The exact target,
quantifiers, essential input IDs, independent unresolved assumptions and
continuation/abandonment criteria above remain unchanged. Mathlib matching
coverage remains unchecked. No lemmas or mathematical scripts were edited.
