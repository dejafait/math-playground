# Double-zero weighted-flow source audit — assessed continuation948

TARGET: Audit the full weighted Jacobian and local uniform integrability of the stopped raw flow for S(q)=-2 log q with q(0,r)=ir, distinguishing fixed physical time from T=tau r^2.
CHECKED: 2026-11-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Source review948 searched logarithmic-zero flow, double-zero Jacobians and Vandermonde collision integrability; compared C466k scope947 and the preserved nomination947. It found the source's simple-zero normal calculation and full variational law, but no ready exact statement for this signed double-zero stopped model; no novelty claim.
SOURCE_EVIDENCE: TNV JHEP10(2017)100, arXiv1706.03822v2 https://arxiv.org/pdf/1706.03822v2 Section2.2 (2.19)–(2.21), footnotes1–2 p6, AppendixB (B.1)–(B.5) p22; LY PRD103(2021)114509 https://doi.org/10.1103/PhysRevD.103.114509 IV.A–IV.B pp4–6 (10)–(21); direct published PDF and recovery949 inspection below.
COMPARISON: Known conjugated-gradient and Jacobian laws cover the calculation machinery. The precise remaining specialization is the double zero, imaginary initial normal line, signed differential, stopped branch and small-time absolute-mass control. This audit tests source applicability, not a new sign mechanism or an actual-h theorem.
GAP: The complete pre-collision solution, hitting locus, fixed-time Jacobian, stopped weighted density and uniform-integrability bound have not been computed here. Analytic remainders, tangential coupling, actual h, homology, global signs and Xi transfer are outside this assessment.
REASON: A vanishing Vandermonde does not by itself justify ignoring singular parameterizations; source footnotes make the weight-times-Jacobian comparison load-bearing. One exact normal-model audit is justified before any collision regularity obstruction is reused. Separate source approval completed in recovery949; only the stated frozen-model audit is covered.
SCOPE: One complex normal variable, flat metric, raw upward conjugated-gradient flow, zero analytic background, real r on a fixed finite interval, no actual-function specialization or modified metric; reproduction only.

## Inputs and why the specialization is needed

Reuse the primary inspection and URLs in
[source review948](2026-11-14-collision-flow-source-nomination-947.md).
TNV's simple-zero calculation neglects its regular remainder; this
target defines an exact frozen model instead of importing that
approximation as an actual-function theorem. A single squared pair
factor motivates multiplicity two. No assertion that freezing
approximates the actual n-variable flow is licensed. The selected
normal coordinate has unit Euclidean metric; any application to
original pair coordinates must separately check that normalization.
No new mathematical result or normal-flow solution is derived here.

Use a branch of log q on each nonsingular trajectory; the weight
exp(-S)=q^2 is single valued. The specified dynamics is
\(\dot q=\overline{S'(q)}\), with \(q(0,r)=ir\), for
\(0<|r|<a\), fixed \(a>0\). Up to the first hit of zero, let
\(J(T,r)=\partial_r q(T,r)\), with T held fixed.
For the oriented positive initial squared-normal factor use
\[
 W_T(r)=-q(T,r)^2 J(T,r)/i.
\]
The proposed stopped density is zero on initial points that have
already hit zero. This is a definition to audit, not a claim that
the stopped map is a classical solution through its singularity or
that its undefined derivative can be multiplied by zero.

## Bounded audit and decisive evidence

Determine the exact maximal pre-collision solution and hitting time;
retain the full fixed-T Jacobian and test the one-sided traces of
the total weighted density at the hitting boundary. Do not replace
J by its modulus inside the signed density. Absolute values are
appropriate only when estimating mass. Check whether extending
the density by zero is consistent with those weighted traces and
with ordinary change of variables on the surviving normal interval.
Keep the motion of outer endpoints explicit: this local audit does
not assert integral invariance for a segment with moving endpoints.

Seek an explicit finite bound for the absolute mass and, for some
explicit \(T_0>0\), the threshold
\[
 \lim_{\delta\downarrow0}\ \sup_{0\le T\le T_0}
 \int_{|r|<\delta}|W_T(r)|\,dr=0.
\]
Also check genuine uniform integrability on \((-a,a)\), including
moving hitting boundaries: provide an integrable envelope or a
uniform bound over measurable subsets of vanishing length. Origin
control alone is insufficient. Record separately the behavior at
fixed positive T and after evaluation at \(T=\tau r^2\), for fixed
nonnegative tau. Find the pre-hit tau range rather than assume it.
The Jacobian is always taken at fixed T before that substitution;
differentiating the composite variable-time curve would change the
question. No arbitrary Taylor-jet fit is within scope.

Continue only if the calculation supplies explicit weighted bounds
or an informative failure of this stated threshold. Smoothness of
the divided coefficient and constancy of action phase alone are
nondiscriminating. If the model is integrable, record only that the
collision-singularity objection fails in this control; an actual-h
perturbation target would require a changed assessment, not automatic
approval. If it fails, record precisely the missing mass estimate
and do not infer failure of every contour mechanism. Do not iterate
normal-model calculations without a materially new question.

This is an ordinary source/hypothesis audit, not a protected creative
attempt. A central new global signed-contour mechanism is still
unavailable: neither a necessity theorem for smooth divided phase
nor actual-h/global continuation estimates have been justified.
C466a/k/l supply motivation and conventions only, not unproved
flow estimates. No cross-notebook input is used. Full matching
Mathlib coverage has not been checked; unknown is not absence.

## Direct-source approval — recovery949, 14 November 2026

This literature-only repair preserves TARGET, DECISION and SCOPE.
The separate approval requested at step948 is completed here; no
normal-model solution, Jacobian or bound has been calculated.

Primary URLs opened and load-bearing passages reinspected:

- Tanizaki–Nishimura–Verbaarschot,
  [arXiv:1706.03822v2 PDF](https://arxiv.org/pdf/1706.03822v2),
  27 September 2017, printed pp6 and22, Section2.2
  (2.19)–(2.21), footnotes1–2, AppendixB (B.1)–(B.5).
  [Primary HTML](https://arxiv.org/html/1706.03822v2), Section2.2
  and AppendixB, renders conjugations clearly; HTML(73) is PDF(B.5).
  The real-parameter variation is at fixed flow time. Flat metric
  gives the conjugated Hessian acting on the conjugated Jacobian.
  The logarithmic example explicitly drops nonsingular terms;
  footnotes qualify deletion by weight-times-Jacobian behavior.
  This is machinery and a warning, not the double-zero mass theorem.
- Lawrence–Yamauchi,
  [published primary PDF](https://scoap3-prod-backend.s3.cern.ch/media/files/62831/10.1103/PhysRevD.103.114509.pdf),
  published 14 June 2021, IV.A–IV.B, printed pp5–6, (12)–(21).
  The inspected collision paragraph permits continuous nonsmooth
  manifolds; IV.B retains the Jacobian contribution to phase and
  distinguishes local from between-piece cancellations. Its (19)
  illustration explicitly requires proper evolution to treat zeros.
  Its collision wording does not replace the TNV weighted check.

Applicability is restricted to nonsingular trajectories of the
specified flat raw vector field with real initial parameter.
The imaginary initial line and double multiplicity require their
own specialization. Neither deleted-region convention licenses
classical continuation through zero. No global invariance is
imported for the finite segment with moving endpoints. The stopped
signed density, all measurable-set uniform-integrability bound and
fixed-time/scaled-time distinction remain exactly the future test.

Reuse source review948's searches and duplicate/failure comparison;
no new discovery search or new mathematical claim is made. The
existing smoothness/action-phase stops are not reopened. This
repair is STALLED as mathematical progress: it supplies direct
locators and approval, not a new theorem or negative result.
Full matching Mathlib coverage remains not checked.
