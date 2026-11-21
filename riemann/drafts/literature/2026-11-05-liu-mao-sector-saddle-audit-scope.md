# Liu–Mao sector saddle input — completed source-scope review

TARGET: Review the essential contour and saddle-error cases of Liu–Mao 2610.04972v1 Lemma3.2 to scope an independent audit of the sector bound |Log(H/H_*)|<=32/T<0.051 used by L830.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the quantitative-curvature assessment, L830 and step655; searched the notebook's Liu–Mao assessment/working/history paths for Lemma3.2 coverage and step410's recorded obstruction; opened the exact versioned primary statement and all essential proof cases, with PDF equation/page cross-checks. No novelty inference or repeated all-iterate search.
SOURCE_EVIDENCE: Yanxin Liu and Jianxi Mao, arXiv:2610.04972v1 (4 October 2026), https://arxiv.org/html/2610.04972v1 and https://arxiv.org/pdf/2610.04972v1; Lemma3.1 (3.1)–(3.7), Lemma3.2 (3.8), complete Sections3.1.1–3.1.3 (3.9)–(3.51), printed pp.8–31, including all contour, local Gaussian, distant-left, vertical and theta-tail cases.
COMPARISON: The source explicitly covers L830's full sector and unchanged threshold, with relative error 30/T and logarithmic error 32/T. L830 proves only their conditional finite-difference consequence; L790's different geometry/range is no substitute. A separate reproduction audit must check the stated bounds, absolute integrals, branch matching and convergence; this review imports no unconditional estimate.
GAP: Essential proof-case access and audit scope are now resolved; mathematical correctness of the sector estimate remains unverified locally. Determinant comparison, exceptional mixed signs, all-degree uniformity and bounded indices remain separate gaps.
REASON: Complete source coverage now supports a bounded independent audit of a load-bearing premise, rather than another source search or the completed L830 audit. Verification of the preprint's exact effective constants and analytic interchanges justifies reproduction; no improved theorem is sought.
SCOPE: Completed literature comparison only. The following are source claims and audit obligations, not new derivations or verification. No lemmas or mathematical scripts changed; the separately saved ready audit nomination is subject to supervisor approval next turn.

## Original nomination retained

The exact functions H, H_*, w=W_0(2z/pi), a=Re w and T=|z|/a,
the sector |arg z|<=pi/4, |z|>=4000, and principal branches are in
canonical L830. Its proof is conditional on the full Lemma3.1–3.2
sector interface, not on an assumed zero-free region for Xi.

Read the primary statement first, then the contour deformation and
individual error cases needed by the final assembly. Track the
normalizing factors and complete sector, including endpoints; source
assertions are not independent verification. Reuse the already
inspected final assembly rather than restarting the Proposition3.5
or all-iterate literature search. Record exact equations and any
remaining unread cases before nominating a bounded mathematical audit.

Continue only if the actual sector estimate reduces to explicit,
independently checkable obligations with all essential coverage
available. If an essential source case is inaccessible or a premise
cannot be matched, preserve the exact blocker and park that dependent
audit. A source failure does not refute (3.8) or RH.

The plausible downstream use is to discharge L830's actual-coefficient
premise before attempting a determinant comparison. Even a fully
verified sector estimate would leave that comparison, all-degree
exceptional signs and bounded indices unresolved. L018/L021/L776 fix
the local normalization; L772/step410 blocks the generic positivity
bridge; L790 is only a distinct estimate for comparison. No
cross-notebook result is proposed. Mathlib matching remains unchecked.

No justified creative transfer is being approved here: a certified
actual-theta premise and a quantified determinant-error mechanism are
still missing. This nomination does not reopen the unrestricted
Turan-to-minor route or claim that a curvature bound supplies a sign.

## Completed review — step656

The exact original target above is unchanged. The saved scope test
passes: every essential case is available and reduces to explicit
obligations. This is progress in local coverage only. No inequality
below was independently proved this turn. The primary source supplies
the result already; novelty is neither sought nor inferred.

### Sector, conventions and contour

Use the H, H_*, W_0 and principal-branch definitions in L830 without
changing normalization. Lemma3.1 (3.1)–(3.7) supplies a>=6,
|b|<=pi/4, 1<=|w|/a<1.009, T=(pi/2)e^a |w|/a>630,
pi e^a<=2T and T<=|z|/6. Its argument-continuity case and both
sector edges must be checked; a merely real-axis estimate is insufficient.

Section3.1.1 (3.9)–(3.13), printed pp.10–12, uses
phi(u)=2z Log(u)-pi e^u and beta in {5/4,9/4}. For each beta,
J_beta is deformed from the positive ray to [0,ib] followed by
ib+[0,infinity). The source gives the small quarter-circle estimate
O_z(epsilon^(2 Re z+1)) for each sign of b, handles b=0 directly,
and bounds the far joining segment by a polynomial in R times
exp(beta R-pi e^R/sqrt(2)). Audit these limits and orientations;
uniformity in z of those particular limiting constants is not claimed.

The horizontal pieces are [-a,-a/2], [-a/2,-1/10],
[-1/10,1/10] and [1/10,infinity) in y=u-w, plus the vertical
piece. The endpoint u=0 is a limit, including when b=0.

### Gaussian and error obligations

All entries in this table are the source's bounds, not this review's
findings about their validity. M_beta=e^(phi(w)+beta w)G and
G=sqrt(2pi) kappa^(-1/2), kappa=-phi''(w).

| Case | Precise source location | Quantity to check |
| --- | --- | --- |
| Gaussian branch and normalization | (3.17)–(3.22) | Re kappa>1.4T, \|kappa\|<=7T/3, \|G\|>=sqrt(6pi/7)T^(-1/2)>1.64T^(-1/2) |
| Gaussian truncation | (3.23)–(3.24) | relative error <=8.8 exp(-0.007T)/sqrt(T) |
| Local remainder, \|y\|<=1/10 | (3.25)–(3.30), (3.30) on printed p.16 | \|c_3\|<=0.4T, \|R_4\|<=0.1T\|y\|^4; odd terms cancel before modulus; \|E_loc,beta\|/\|G\|<=14.4/T+1.3/T^2 |
| Horizontal tails | (3.32)–(3.37), ending printed p.19 | strict concavity on [-a/2,infinity); normalized sum of absolute integrals <=12.6 exp(-0.0063T)/sqrt(T) |
| Distant left | (3.38)–(3.41), ending printed p.21 | argument term nonpositive for both b signs; action drop <-0.58\|z\|; normalized absolute integral <1/(100T) |
| Vertical | (3.42)–(3.43) | sign(b)=sign(Im z), integrand modulus <=1; Re phi(w)>2\|z\| and relative contribution <1/(100T) |

The local remainder proof supplies all four even Gaussian moments
(orders 2,4,6,8), the explicit coefficients before rounding, and
the domination exp(-0.6Ty^2). The forthcoming audit must verify
these coefficients rather than merely reuse rounded (3.30).

### Theta remainder and absolute-integral issue

Section3.1.2, printed pp.22–28, treats k>=2, not just the first
theta term. It states local uniform convergence in |Im u|<pi/2
and the bounds needed to repeat the contour shift. Audit convergence
and small/far joining limits separately from the pointwise comparison.
With r=Re(e^u)>=1/sqrt(2), (3.44)–(3.46) give the positive-series
majorants 17e^(-4pi r) and 5e^(-4pi r), and the comparison factor
20(2pi^2)e^(-3pi r) against |exp(phi(u)+9u/4)|.

The three regions in (3.47)–(3.49) each cost <0.01/T relative
to 2pi^2|M_(9/4)|; (3.50) adds them to 0.03/T. The large
horizontal region uses an absolute main-integrand integral <2
after normalization, then the factor exp(-(3pi/sqrt(2))e^(a/2)).
The distant-left region retains the extra factor 20; the vertical
region uses |E_theta(it)|<4 and |(it)^(2z)|<=1.

Load-bearing distinction: printed p.25 displays a chain with the
absolute integrals between the complex-integral modulus and its
tail bound. The last inequality requires the stronger estimate
proved through the pointwise envelope in the derivation of
(3.34)–(3.37). It does not follow solely from the displayed
bound on |I_-|+|I_+|. The full relevant derivation was read;
future verification must preserve that stronger form. This is an
identified audit obligation, not a claim of a source error or a repair.

### Assembly and source limits

Reuse the previously inspected Section3.1.3, printed pp.28–31:
(3.51) states |J_beta/M_beta-1|<24/T. Its budget is
14.4/T+1.3/T^2+(8.8e^(-0.007T)+12.6e^(-0.0063T))/sqrt(T)
+2/(100T); the exponentials are bounded at T=630 using monotonicity.
The source fixes the Gaussian square-root identity by agreement on
the positive axis, identifies 2^(1-2z)2pi^2 M_(9/4)=H_*, and
charges J_(5/4) <0.8/T. Together with 0.03/T it obtains <30/T,
then uses Log(1+v), |v|<1/21, to give <32/T<0.051.
Audit nonvanishing and holomorphy on a neighborhood of the closed
sector without assuming a single uniform neighborhood width.

The versioned HTML was read through every essential proof case;
PDF text confirms the statement and selected equation/page locations.
The unsuccessful direct shell download was a DNS failure; the web
HTML/PDF access succeeded, so no essential source is blocked.
The bibliography points to Corless et al., *On the Lambert W
function*, Adv. Comput. Math. 5 (1996), 329–359, Section4,
and Folland, *Harmonic Analysis in Phase Space* (1989), AppendixA,
Theorem1, for principal-W geometry and complex Gaussians. Those
external texts were not newly inspected; standard named principal-W,
Gaussian-integral, Cauchy and holomorphic-limit results may be cited
precisely in the audit. The preprint's all-iterate and finite-computer
certificate portions remain outside this review. Mathlib matching
is unchecked; supporting standard analysis is not full coverage.

The ready nomination is
`2026-11-05-liu-mao-sector-independent-audit.md`. It seeks local
reproduction of this known claim only. A pass can remove L830's
sector assumptions, but gives no mixed-minor implication, RH proof,
bounded-index certificate or all-iterate import. Continue only if
every case and constant holds with the stated full-sector hypotheses;
otherwise record the first precise failure and park the dependent
unconditional claim. L772/step410 and the earlier source comparison
remain intact. No new creative bridge is justified before obtaining
a certified analytic premise and a determinant error mechanism.
