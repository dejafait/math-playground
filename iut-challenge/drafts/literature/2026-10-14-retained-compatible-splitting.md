# Retained compatible splitting — primary comparison completed

TARGET: Test whether L057's retained cover over unchanged N admits the compatible splitting required by EtTh Definition 2.5(i), using its rational cusp sections and L054's field equalities without assuming a label for Q.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 207 searched exact compatible-splitting/Definition 2.5 terminology, followed Proposition 2.2 and Theorem 1.10 to Galois Sections Definition 4.1, and checked local duplicates/failures; queries and inspected ranges are in drafts/2026-10-14-retained-compatible-splitting-source-review.md.
SOURCE_EVIDENCE: Read Mochizuki EtTh, PRIMS45 (2009), https://ems.press/content/serial-article-files/41069?nt=1, Propositions 1.3/1.4 pp.245–248, dotted diagram/Definition 1.7 pp.253–254, Definition 1.9/Theorem 1.10/full proof/Remark 1.10.1 pp.255–257, Definitions 2.1/2.3/Proposition 2.2/full proof pp.261–264, Definition 2.5(i) p.265, Corollary 2.8/full proof pp.267–268; author Definition 2.5(i) p.36 and Theorem 1.10/Remark 1.10.1 pp.27–28 at https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Etale%20Theta%20Function%20and%20its%20Frobenioid-theoretic%20Manifestations.pdf; Galois Sections, NMJ179 (2005), author section 4/Definition 4.1(i–iii) pp.14–15 and Corollary 4.12/full proof pp.23–24 at https://www.kurims.kyoto-u.ac.jp/~motizuki/Galois%20Sections.pdf, retaining EtTh's primitive-twelfth-root correction.
COMPARISON: Proposition 2.2(ii) constructs an additional theta cover from a finite cusp-extension splitting with K^*/(K^*)^7 torsor of choices; Theorem 1.10(iii) supplies the required sign reduction under standard-type hypotheses. L053/L057 give the rank-one cover, not this choice. Known constructions cover an exact-object application; Corollary 2.8 cannot supply its own starting choice, and a mu_12 reduction cannot replace the theta-defined sign reduction.
GAP: Verify the local setup and standard theta normalization on unchanged N, match dotted/original cusp-torsor maps and their finite quotient, and apply Proposition 2.2(ii) to compatible sigma; no retained splitting, additional theta cover or Q label is yet proved. Full selected/theta and original numerical gaps remain.
REASON: Essential coverage is now available for a later mathematical specialization of this independent prerequisite, without reopening the parked marked-coordinate mechanism or deriving mathematics during this review.
SCOPE: Exactly TARGET using retained curve/fields/maps, cited theta normalization and actual cusp-torsor maps/finite quotient at level seven; REPRODUCTION only. No prescribed theta cover, Q label, all-place compatibility, new curve/field, IUT flaw or numerical bound is covered.

Main gap: original finite B>=A and actual input/action/pilot/essentiality.
Possible use: resolve or delimit one independent local native-type
prerequisite. Cusp labeling and full selected/theta data remain open.

Retain L052,L053,L054,L055,L056,L057 and inherited L045,L048,L051;
E_0/Q,F=Q(zeta_60,E_0[30]),K_glob=F(E_0[7]),Omega,u,w,
H=F_u subset N=(K_glob)_w,M>=max(M_tors,31),full 30-torsion,
fixed pointed Tate isomorphism,changed r=q_0 in Q_3,v_3(r)=30,
actual alpha,psi,gamma,kappa,a_N and seven rational sections.
Neither K_glob=N nor q_0=3^30 is assumed. Preserve source-version
and odd-level qualifications; neither c(1)=plus-or-minus Q nor
compatible splitting is a premise. No cross-notebook input is proposed.

Distinguish the native splitting from an abstract arithmetic
fundamental-group section and from L053's trivial cusp decomposition
image. A precise applicable theorem or precisely unmet compatibility
condition passes the literature test; repeating the cusp/graph argument
does not. No derivation or Mathlib match is asserted. Step 207 completes
source coverage; the supervisor may separately approve this changed
ready assessment before a research invocation. Precise hypotheses,
qualifications and the continuation test are in
`drafts/2026-10-14-retained-compatible-splitting-source-review.md`.
