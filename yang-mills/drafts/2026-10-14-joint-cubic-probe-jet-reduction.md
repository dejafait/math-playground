# Joint cubic probe-jet attempt — completed finite reduction

Approved target: determine whether L011's joint cubic probe-jet response
kappa_0(f_(i,1),r_1)-kappa_0(f_(i,1),r_0,S_3) has a finite a^3-scaled
limit for both actual L010 probes. Reuse the unchanged EXPLORE assessment
`literature/2026-10-14-joint-cubic-probe-jet-scale.md`.

Main gap: ultraviolet-uniform interacting reflected control, followed by
the independent continuum and infrared construction. This attempt seeks
a complete signed contraction of this particular two-term group as an
intermediate input; a finite identity alone will not settle its limit.

Local checks: L011(6),(10)–(13), L010(2)–(4), L018(1)–(3),
L155's full residual/color proof, L019's forest-change statement and
L022's coordinate-flow calculation have been read. ATTEMPTS/009 /010
/011 /038 retain the isolated-group, curvature-transfer, growing-loop
and nonvanishing obstructions. No matching contraction was found in the
targeted local search. Existing unfinished files are preserved.

The completed proof is canonical in
[L181](../lemmas/L181-joint-cubic-probe-jet-contraction.md).
It establishes the full signed reduction through an effective cubic
residual and a full-link Duhamel integral. All 19 exact rational checks
in `../scripts/combined-ward-response/joint-cubic-probe-certificate.json`
pass with zero error; these check finite algebra, not cutoff behavior.

L181 retains L022's full-coordinate flow identity, the actual cubic
triplet/clover probes, every physical face and the undamped gradient
kernel. Its effective residual is nonlocal. No near-zero-time uniform
majorant or cubic bound was obtained. No failed estimate is claimed
to disprove a limit. The unchanged ready assessment continues to cover
the original target; no new target is approved in this step.

Continuation test: a correct signed reduction with a controlled
full-spectrum cubic estimate and removable approximation errors would
support a limit calculation. Stop any estimate using an O(1) raw forest
covariance or deleting the near-zero-time interval. The f_(i,2),r_0
term, finer powers/logarithm, matching, reflected error <=c_box/2 and
continuum/infrared requirements remain unresolved.
