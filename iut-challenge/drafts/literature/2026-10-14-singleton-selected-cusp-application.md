# Singleton selected-bad place — proposed applicability test

TARGET: Test a singleton selected-bad set at 3 and a full place section through w against IUT I Definition 3.1(e)-(f) for L053's unchanged global cover and cusp Q.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed global-quantifier screen in drafts/literature/2026-10-14-global-selected-cusp-quantifiers.md and its source review; the earlier native notes leave a complete section open, and ATTEMPTS/030,031 do not address this test with audited L057-L059.
SOURCE_EVIDENCE: Mochizuki IUT I May 2020, Definition 3.1(b)-(f), pp.61-63, Remark 3.1.3 p.65, primary author text read through the qualified reproduction; EtTh PRIMS 45 (2009), Definition 2.5(i) p.265 and cusp-label construction pp.268-269, read at https://ems.press/content/serial-article-files/41069?nt=1 ; precise links, complete inspected cases and access qualifications in drafts/2026-10-14-global-selected-cusp-source-review.md.
COMPARISON: Known definitions specify a section and the fixed cover/cusp predicates; audited L057,L058,L059 establish the retained local graph, splitting and sign label. The remaining work is an actual same-object applicability check and the full section construction, not a new general uniformization or simultaneous-place theorem.
GAP: Identify F_mod for this Q-defined curve, constrain the section to pass through actual w, and verify the resulting selected bad members and quotient-stack cusp without changing global U,Q. No result is yet proved for that proposed selection.
REASON: This is the smallest directly testable global selection compatible with the source scope; it can close the selected-place bookkeeping before any independent initial-data or numerical/pilot bridge is attempted.
SCOPE: Only Definition 3.1(e)-(f) for the proposed singleton; other clauses remain separate obligations and are not assumed verified by this assessment.

This ready assessment is newly written and requires separate approval
next turn. This literature step does not execute the mathematical test.

Use L053,L057,L058,L059 and inherited L045,L048,L051,L052,L054,L055,L056.
Retain E_0/Q, F=Q(zeta_60,E_0[30]), K_glob=F(E_0[7]), Omega,u,w,
H subset N, M>=max(M_tors,31), full 30-torsion, the fixed pointed
Tate isomorphism, changed q_0 in Q_3 with v_3(q_0)=30,v_3(3)=1,
and actual U,alpha,psi,gamma,0_B,Q,c. Neither K_glob=N nor
q_0=3^30 is assumed. Q denotes the actual point of ker(psi), not
an arbitrary generator of a newly chosen quotient.

The proposed proof must justify its field of moduli, extend the retained
place to a section over every moduli place, and track the actual cusp
through L053's inversion quotient and L059's sign identification. Cite
the exact definitions, reuse the audited local proofs, and derive only
the missing selection/application. A convenient full set of places
above 3 is not the required section. An arbitrary change of label by
a unit modulo seven does not pass. Local theta choices must satisfy
L058's retained hypotheses; do not assert a single global splitting.

Continue if precisely the same U,Q pass (e)-(f) under this selection.
Abandon that selection if the actual field of moduli, section constraint
or quotient-cusp marking forces an additional incompatible condition;
preserve its precise obstruction. If essential general coverage is
missing, leave the application open and name it REVIEW_REQUIRED.
No general theorem needs reproof and no computational certificate is
needed. Full matching Mathlib coverage has not been checked.

The all-F-place reduction and normalized q-order coprimality conditions
in (b)-(c), remaining initial-data predicates, actual input/action/pilot,
essentiality and finite B>=A are outside this test. In particular the
q-order clause concerns F-places, not the order at K_w. Adding another
selected bad moduli place would require checking the same fixed U,Q
there and is outside this coverage.
