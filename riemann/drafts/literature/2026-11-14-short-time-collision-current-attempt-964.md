# Short-time complete current — bounded attempt nomination964

TARGET: Attempt the complete localized Stokes identity under C466s with M_1 T_0<min{R-a,L-b}, proving outer-hit exclusion and controlling every complete-form coefficient and collision/initial-axis cutoff flux, or exhibit an admissible defect.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Source review964 completed the changed short-time scope comparison in assessment963; reused exact/stronger extension searches960 and compared local current records and stop961. No matching short-time theorem was identified; no novelty certification.
SOURCE_EVIDENCE: Teschl author-hosted preliminary ODE text, Lemma2.14/Corollary2.15 p52 and Theorem6.1/proof pp189–190 https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf; Wu–Kanevskiy–Margaliot arXiv:2008.10321v2 Section3.1 Proposition5/proof p9 https://arxiv.org/pdf/2008.10321v2; Harvey–Polking Acta Math.125(1970)39–56 Theorem2.1/Lemma2.2 pp40–41 and Theorem5.2 pp48–49 https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6102-11511_2008_Article_BF02838327.pdf; Tanizaki–Nishimura–Verbaarschot arXiv:1706.03822v2 Section2.2/AppendixB https://arxiv.org/html/1706.03822v2#S2.SS2. Exact hypotheses and inspected proof cases reused from reviews960/964; targeted source recheck965 below.
COMPARISON: Known local ODE/compound/cutoff tools cover compact smooth survivors; no inspected source supplies the short-time complete zero-extension identity. Derive only the missing singular-flow applicability and weak limit, not the known machinery or C466s's audited spatial estimate.
GAP: Outer-hit exclusion under the precise buffer condition, full beta/gamma L1_loc, and zero collision/initial-axis weak cutoff error remain unproved; no trace, regular lifetime or post-exit map is assumed.
REASON: Completed literature-only review964 supports one bounded established-route attempt after separate approval next turn. The restriction changes the mechanism of audited stop961 without rescinding it, and the proposed weak identity is independently falsifiable.
SCOPE: Exact C466s data and unit raw physical-time flow, finite T_0>0 with the strict displayed restriction, arbitrary compact ambient smooth chi, complete forms on survivors, compact tests in Q, coefficientwise zero extension at first stopping and r=0. No changed metric or regular hitting-surface premise.

## Exact question to test, unproved

Use C466s's real 0<a<R, 0<b<L, finite nonnegative M_1,M_2,
fixed complex H_0 and holomorphic H on B={|q|<R,|z|<L}, with
H(0,0)=H_0, ||grad H||_2<=M_1 and ||D^2H||_op<=M_2.
Keep S=-2 log q+H, dot X=conjugate(grad S), initial X(0,r,s)=(ir,s)
and I=(-a,a) times(-b,b). The local logarithm defines the same
single-valued vector field on U=B minus{q=0}. Tau is the first
maximal lifetime in U, not a later return time.

Add exactly T_0>0 and M_1 T_0<min{R-a,L-b}. On
Q=(0,T_0) times I let D_H be t<tau(r,s), r!=0, and define
Psi=X on D_H only. For arbitrary smooth scalar chi compactly
supported in B, retain

    Omega=q^2 exp(-H) dq wedge dz,
    beta_chi=Psi^*(chi Omega),
    gamma_chi=Psi^*(dchi wedge Omega).

The question is coefficientwise L1_loc of both zero extensions to Q
and d bar(beta_chi)=bar(gamma_chi) distributionally on Q.
The complete two-form includes dt wedge dr, dt wedge ds and dr
wedge ds; gamma is the full pulled-back three-form. Orientation is
dt wedge dr wedge ds. There is no flow map at r=0 or after exit.
No statement of signed integral invariance or positivity is included.

## One bounded proof/obstruction test

First establish or refute exclusion of prior |q|=R and |z|=L
hits throughout this time range for the entire initial rectangle.
The velocity is singular near q=0, so a bound on the regular part
alone cannot be cited as a full-speed bound. Retain M_1=0 and
possible simultaneous limiting events. A first-hit proof must use
the actual raw ODE and the existing endpoint classification; no
continuation outside B is licensed by the buffer premise.

If that succeeds, test whether the autonomous velocity and real
parameter variations can be handled by the cited compact-interval
variational/compound machinery, with all needed exterior degrees.
Working961's suggestion is preserved as an unproved idea. Justify
complete coefficient estimates and every use of the singular weight;
the known spatial envelope alone does not settle this target.

Seek smooth cutoffs eta_j inside D_H, 0<=eta_j<=1, approaching1
on survivors and avoiding collision/stopping and initial-axis loci.
The requested sufficient proof goals are local L1 convergence of
eta_j beta_chi and eta_j gamma_chi to their zero extensions, and

    integral_{D_H} phi d eta_j wedge beta_chi ->0

for every smooth compactly supported scalar phi on Q. These are
proof obligations, not established estimates. An alternative rigorous
weak-limit method is allowed if it pays the same complete identity.
Retain the inhomogeneous gamma term, all orientations, tests meeting
r=0 and all collision preimages. Compact time/parameter test support
removes external Q edges only; it does not prove any interior trace
vanishes. HP's homogeneous theorem needs a justified formulation
before use for this inhomogeneous equation.

Continue only upon paying all these obligations. A rigorous
admissible defect detected by compact chi/test, or a nonintegrable
complete coefficient, refutes the restricted identity. Failure of
one convenient norm estimate is merely a failed method. Save partial
reasoning before lengthy work, and return after this one attempt.
Do not repeat the unchanged outer-grazing universal target, or treat
a fixed-time absolute-density replay as progress on the current.

C466s and audited C466t are the essential local inputs/obstruction
comparison. Preserve stops927/932/941/947/948/959/961. Matching
Mathlib coverage is unchecked; no cross-notebook theorem is used.
Source review964's exact evidence is retained in assessment963,
including access qualifications. This newly written ready nomination
receives separate approval next turn; no proof is supplied here.

This is proof_attempt/development using established machinery,
appropriately deep_research/xhigh. A successful local identity would
pay a boundary step; long-time restart, metric, intersecting divisors,
global signed integration, all-degree signs and actual-Xi transfer
remain independent. No central creative sign mechanism has yet been
justified because the implication to actual determinant positivity
is missing. No RH candidate or originality certification is claimed.

## Separate approval and direct-URL repair965 — 14 November2026

The supervisor required direct source URLs in this ready assessment.
The SOURCE_EVIDENCE line now contains them rather than only a local
assessment reference. This is a process repair and separate approval
of the unchanged target, not new mathematical evidence or a new lemma.
EXPLORE remains appropriate for one bounded proof/defect attempt.

Reopened the primary URLs above. Read Teschl's Lemma2.14 proof,
Corollary2.15 and Theorem6.1 proof at the cited pages; continuation
still requires an interior accumulation point, and smooth flow is
asserted only on its open maximal domain. Read WKM Proposition5 and
its compound-evolution/Coppel proof; its all-k bounds do not provide
a singular endpoint estimate. Read TNV Section2.2 (2.21)–(2.23) and
footnotes1–2: its fixed-time weighted-Jacobian discussion does not
supply this complete inhomogeneous current identity. No expanded
search or changed mathematical scope was needed.

The Harvey–Polking PDF opened and its introduction was readable;
two subsequent theorem-find requests timed out. Reused the already
inspected theorem hypotheses and cutoff/Green proof cases in
assessment959/review960, primary-comparison section, rather than
claiming a fresh theorem-page inspection. This transient recheck
failure does not remove the retained essential coverage or create
a source blocker. TNV AppendixB coverage is likewise reused.
Mathlib full matching coverage remains unchecked.

No specialization, exclusion bound, mixed-minor bound or weak flux
limit was derived. C466s and audited C466t remain the essential local
inputs; stop961 and unfinished working961 remain preserved. The
exact target, continuation test and independent gaps above are
unchanged. The next invocation can use this separately approved
EXPLORE assessment for mathematics; no further literature is needed
unless its hypotheses or required tools change.
