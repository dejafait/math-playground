# Right horizontal theta-Mellin tail: research nomination

TARGET: Attempt the standalone right horizontal theta-Mellin bound T_R(s)<=(14u/sqrt(Q))exp(-(77/50)Qd^2) on all D using a full-ray amplitude majorant and an effective concave endpoint envelope.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step522's exact-ray duplicate/failure search and completed comparison in 2026-11-05-mellin-right-horizontal-tail-scope.md; no new discovery or novelty claim.
SOURCE_EVIDENCE: paper23 v1 Section3 Lemma2 (10)–(14); Devroye, Non-Uniform Random Variate Generation (1986), ChapterVII Section2.6, pp299–300, tangent envelope preceding Theorem2.6 and first integral of its proof, https://luc.devroye.org/chapter_seven.pdf; exact statements and cases inspected in step522. DLMF2.3(iii)/2.4(iii) provide the recorded asymptotic comparison only.
COMPARISON: The effective endpoint method covers real infinite rays pointwise without a fixed-phase asymptotic constant. Neither it nor the source's combined horizontal allowance establishes the actual theta-amplitude, phase hypotheses or requested constants.
GAP: Verify full-ray admissibility, theta-amplitude control, real-phase concavity, quantitative negative endpoint slope, absolute convergence and the normalized numerical comparison throughout D; all remain mathematical obligations.
REASON: Independent known-method source reproduction can be attempted without the blocked global contour, left endpoint or supplementary derivations. A citation alone cannot pay the parameter-specific hypotheses.
SCOPE: Newly written ready research nomination; separate supervisor approval is required next turn. No estimate or convergence proof is established by this file.

Use exactly L797's D and x=u+ih, L798's Q,d,S_s,A,a and principal
C=sqrt(2pi/A), and L799's theta series P on U. Put z_R=x+da and retain
the full complex numerator:

    T_R(s)=|integral_0^infinity exp(2s Log(z_R+t)) P(z_R+t) dt|
             / |4pi^2 exp(S_s(x)) C(s)|.

The sole threshold is

    T_R(s)<=(14u/sqrt(Q))exp(-(77/50)Qd^2), s in D.

This spends the whole printed horizontal allowance on the right tail.
It is not the two-tail claim, a continued-M identity or an RH criterion.
The main gap remains actual-Xi all-degree mixed positivity; a paid
right-tail component could help a separately assessed Mellin approximation.
Left tails, continued endpoint, global deformation, assembly,
quotient/inversion, certificates and sufficient signs remain open.
L800 is finite-Gaussian context only; no cross-notebook input is proposed.

Follow step522's full-ray applicability checklist. Cite the imported
standard tangent-envelope principle precisely and justify its use for an
unnormalized real phase before assuming integrability. Bound amplitude
separately; do not assume log-concavity of complex P or its modulus.
L799's local bound cannot be extended by assertion. Cover both closed
boundaries of D, both signs of h, h=0 and unbounded u. L798's finite
endpoint decrement is available; horizontal slope/global concavity remain
unpaid. Keep hypotheses and limitations in any canonical result, with
Mathlib full matching coverage recorded as unchecked unless inspected.

Continue if a rigorous effective envelope pays the threshold on all D.
If its concavity/slope/amplitude hypotheses or sufficient bound fail,
record the exact obstruction and retire that method unless materially
new input is identified; distinguish this from refuting T_R or RH.
Do not invoke unread Derivations42/43/65/87 or repeat supplement searches.
Numerical samples do not establish uniformity. No script is presently
needed. This is REPRODUCTION of a source component, not creative work.
