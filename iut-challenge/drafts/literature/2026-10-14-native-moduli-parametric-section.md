# Native moduli field retained — independent section/cusp test

TARGET: Construct a full section of V(K_glob) onto the native V(F_mod) through w, select the singleton {w restricted to F_mod}, and test Definition 3.1(e)-(f) for L053's unchanged cover and the quotient cusp of Q without identifying F_mod with Q.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step 216's section/subset screen and step 217's targeted gap check; no recorded result constructs this section/application. ATTEMPTS/030,031 concern different covers or coordinates.
SOURCE_EVIDENCE: https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf, May 2020, Definition 3.1(b)-(f), printed pp.61-63, inspected through https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf with existing version qualifications; https://ems.press/content/serial-article-files/41069?nt=1, EtTh PRIMS 45 (2009), section 2 opening and Definition 2.1 p.262, Definition 2.5(i) p.265, complete relevant clauses inspected. Source details in drafts/2026-10-14-singleton-selected-cusp-coverage-repair.md.
COMPARISON: Definition 3.1(e) specifies the natural surjection of place sets and its section; (e)-(f) test the fixed cover and cusp at selected bad members. L053,L057,L058,L059 supply only the retained global cover and its local type and sign. Explicit field identification is unnecessary for this narrower conditional application and remains parked.
GAP: Actually choose the section through w over the native named F_mod, determine the singleton selected bad fiber, and track the same Q through inversion to its quotient cusp; no application is proved here.
REASON: This obligation is independently testable with covered source definitions even while explicit field-of-moduli identification remains source-blocked; it removes that source dependency without asserting F_mod=Q.
SCOPE: Conditional only on F_mod being the native field already specified by IUT I; no computation or replacement of its definition, no full initial-data claim, no other selected bad places.

This newly written ready assessment requires separate approval next turn.
It authorizes only the exact TARGET after that approval; this turn derives
no section, quotient-cusp statement or new lemma.

Retain L053,L057,L058,L059 and inherited L045,L048,L051,L052,L054,
L055,L056, E_0/Q,F=Q(zeta_60,E_0[30]),K_glob=F(E_0[7]),Omega,u,w,
H subset N,M>=max(M_tors,31),full 30-torsion,fixed pointed Tate
isomorphism,changed q_0 in Q_3,v_3(q_0)=30,v_3(3)=1,actual
U,alpha,psi,gamma,0_B,Q,c. Neither K_glob=N nor q_0=3^30 is
assumed. In particular w is an actual place, not a completion field.

Use the place surjection in 3.1(e) and ordinary selection from its
nonempty fibers, constrained at the retained w. The selected bad
moduli place is the actual restriction of w, rather than an asserted
identification with a named place of Q. Test its residue characteristic
and the local type using the unchanged completion and audited inputs.
Track the quotient cusp under the existing inversion; an arbitrary
new generator does not suffice. Use L058's local splitting only.
Continue if the same cover/cusp passes; preserve any forced conflicting
marking or hypothesis. A new essential theorem requires REVIEW_REQUIRED.
Full Mathlib coverage is not checked. All-F-place q-order, other initial
data, actual input/action/pilot/essentiality and finite B>=A remain open.
