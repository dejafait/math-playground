# Full-theta right-ray conceptual audit nomination1641

TARGET: Audit C048g's absolute full-theta right-ray bound T_right(p)<=A_+ L^(9/2)/r, including negative-Re(p) phase control, all-mode domination, convergence, closed-sector uniformity and the exact A_+<0.096514 certificate.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step1642 reused assessment1640 and source-notes1640 exact-ray duplicate/failure searches, read C048g for scope and the preserved global-import stop, and rechecked the primary passages below. No new discovery search or novelty claim.
SOURCE_EVIDENCE: Kawano Preprints.org202611.0383v1, posted4November2026, DOI10.20944/preprints202611.0383.v1, https://www.preprints.org/manuscript/202611.0383/v1 , Section5.2(28), Lemma5.1(i), right-side proof(31) with both sigma cases, AppendixB full-mode/B_+ envelope, AppendixC domain/width/A_+; ready source-notes1640 reused, (31) and A_+ rechecked during reproduction1641. Devroye(1986), ChapterVII Section2.6 pp299-300, envelope before Theorem2.6 and first proof integral, https://luc.devroye.org/chapter_seven.pdf , coverage reused.
COMPARISON: C048g reproduces the source's exact one-ray allowance for the operational absolute integral; it uses C048c geometry and L799's strip identity, independently verifying full-ray hypotheses and constants. It neither imports L801's different saddle/domain bound nor invokes a global contour identity.
GAP: Independently audit the proof's negative-real-part case, full absolute-series envelope, positive tangent decay rate, exact normalization and radial monotonicity; replay and scrutinize the rational coefficient certificate. No additional mathematics is approved by this audit nomination.
REASON: Separate literature approval completed in step1642; unchanged target and adequate reused primary coverage authorize the next conceptual audit. This readiness confirmation is STALLED, not a mathematical advance or verification of C048g.
SCOPE: Only C048g and its exact fixed-scalar certificate, on r=|p|, L=log r>=12, Re p>=-r/(4L), w=W_0(2p/pi), u_0=w/2, d=1/(3L), with C048c principal branches and normalization. REPRODUCTION, not creative research. No left ray, full assembly, inversion, zero count or sufficient-sign conclusion.

The main gap remains L030-L032/C032a actual-Xi all-degree positivity.
This component could contribute to a future full-theta Mellin remainder,
while C028b's H_d=o(d), C028g's S_F=0 and a sufficient sign bridge
remain unpaid. A successful audit does not resolve those independent gaps.

Essential input use is C048c's geometry/branch estimates and L799's
general strip-series proof and identity(4), not its rotated saddle bounds.
C048g defines the full factor explicitly in the same R_modes notation
as assessment1640. No external or cross-notebook theorem is newly needed.
Full matching Mathlib coverage remains unchecked.

Read C048g's complete proof and the precise input ranges used. In its
phase proof, check that Q<=v_0 holds on the entire right ray when
Re p<0 even after Q ceases to be positive; inspect reflection and the
real-p endpoint. Do not silently assume global monotonicity of Q.
Check all modes and the unbounded s interval, the principal Log domain,
the use of sqrt(|A_0|/pi), and that (1) is an integral of the modulus.
Absolute convergence must follow from a proved positive tangent rate.

Audit the analytic inequalities lambda>(62/25)r/L^3,
v_0 phi(d)>(19/45)r/L^4, 9d/2<=1/8 and the monotonicity reduction
to y_0. Inspect the complete scalar algorithm and relevant exact evidence
in scripts/mellin-horizontal-local/right_ray_constants_1641.py and .json;
decimals or bounded previews alone are not verification. A separate
implementation may be used if it checks a meaningful independent risk.
The script checks constants only, not the analytic sector argument.

Continue if all hypotheses, normalization, infinite-ray estimates and
the strict coefficient bound survive. Otherwise record and repair a
specific mathematical error within the approved scope; failure of a
sufficient envelope alone is not a counterexample to T_right or RH.
Preserve the historical global-import stop and do not reopen blocked
supplement searches. No central creative sign mechanism has yet been
specified; this delicate complex-phase audit has conceptual_audit purpose.

## Separate literature approval1642 — 19 November 2026

LITERATURE_REASON: Required separate approval of the newly nominated audit;
no changed mathematical target and no additional general literature search.

The live [primary manuscript](https://www.preprints.org/manuscript/202611.0383/v1)
still identifies Version1, posted4 November2026, not peer reviewed.
Rechecked Section5.2(28), Lemma5.1(i), and proof(31): the source explicitly
treats both signs of Re p and the persistence of nonpositivity after Q
crosses zero. AppendixB supplies the full-mode estimate for real t>=1
and the positive-envelope right-tail construction. AppendixC supplies
the L>=12 sector, width1/(3L), separate A_+ allocation and radial reduction.
These passages match the prior assessment; no source-scope change was found.

C048g was read in full to delimit the audit, with C048c's geometry and
normalization displays and L799's strip identity. This was a scope check,
not independent verification of their arguments. The operational integral
of the modulus still requires its own justification: the printed global
relative-error statement does not by itself certify it. The scalar program
and full certificate remain unread in this turn and must be inspected in
the mathematical audit; their reported success is not adopted as evidence.

Assessment1640/source-notes1640 retain the exact-target searches and
L801 mismatch. The preserved global-import stop was read; neither a
full-contour identity nor a blocked supplement is needed for this audit.
Devroye coverage is reused without another read. Full matching Mathlib
coverage remains unchecked. No additional theorem or mathematical result
is imported in this approval.

DECISION remains SPECIALIZE. The exact TARGET and SCOPE above are now
approved for a separate REPRODUCTION conceptual audit, using C048c and
L799 only as the stated mathematical inputs. Retain the explicit test
above; if a load-bearing claim fails, document that claim rather than
inferring a counterexample to the ray bound or RH. This confirmation
repeats readiness and is therefore STALLED under the shared outcome rule.
No lemma, certificate, mathematical script or argument overview changed.
