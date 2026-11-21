# Prescribed exchange-diagonal data — exact collar source comparison

TARGET: Determine whether L848's prescribed h,b admit a smooth periodic exchange-equivariant radial graph whose full oriented pullback is exactly real and nonnegative on a uniform neighborhood of the diagonal.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the ready full-phase and diagonal-audit assessments and the recorded averaged-extension failure; searched prescribed-data special Lagrangian Cauchy problems, noncharacteristic analytic PDE existence, vanishing holomorphic forms and Briot–Bouquet PDEs. Inspected primary statements and relevant proof cases listed below; no matching prescribed actual-G collar theorem was located in this bounded search, without a novelty claim.
SOURCE_EVIDENCE: Chaperon (9 January 2007), Section 2 pp4–7; Bryant–Chern–Gardner–Goldschmidt–Griffiths, EDS Chapter III Theorems 2.1–2.2 pp70–74 and Example 3.5/Theorem 3.6 pp79–80; Gérard–Tahara, PRIMS26(1990), Main Theorem(I) p981 and Theorem1 pp983–987; Bacani–Tahara, PRIMS48(2012), assumptions(A1)–(A3)/(2.3)–(2.4) and Theorem2.1 pp900–902. Exact citations, hypotheses and scope below.
COMPARISON: Analytic Cauchy and singular-PDE results supply conditional local existence methods, not this graph. L847/L848 do not yet verify an analytic solved normal form, a regular exterior differential system, or the singular theorem's coefficient conditions. Standard special Lagrangian extension adds an unrequested symplectic equation and uses a constant nonvanishing volume form. The negative antipodal value concerns only L848(6).
GAP: Derive and test an admissible exact phase formulation through the collision zero, with these precise h,b; establish actual solvability or a scoped incompatibility, then periodic/exchange compatibility, a uniform collar and a smooth torus extension. No existence, noncharacteristic, singular-exponent or convergence claim for the actual data is accepted by this review.
REASON: Essential source comparison is now sufficient for one bounded mathematical attempt at the unchanged target. Reuse the audited full determinant and evaluator; import a standard existence theorem only after proving its exact hypotheses, rather than reprove it. A failed normal-form method alone will not disprove collar existence.
LITERATURE_REASON: The exact prescribed-jet collar problem was outside the completed audit; its potentially degenerate local phase equation needs essential theorem-level comparison rather than another general contour search.
SCOPE: Fixed r=2,k=1, actual G,R,C and oriented omega of L847, exactly h,b of L848(4), real smooth periodic exchange-equivariant u, all zeros retained. A later bounded attempt may derive an exact local equation, test analytic desingularization/noncharacteristic or Briot–Bouquet hypotheses, and attempt a construction or explicit compatibility obstruction; finite jets alone do not settle the target. No theorem applicability or regularization is preapproved as true.

## Completed comparison, 6 November 2026

The main gap remains L030–L032/C032a all-degree mixed positivity for
actual Xi. The intermediate target is exactly TARGET above. A successful
collar would provide a local piece for a future coupled contour, leaving
global sign/gluing, other orders/shifts and transfer to that positivity
unresolved. This is a source review, with no new mathematical derivation.

### Local inputs, overlap and failures

Read L847's hypotheses, conclusions and complete full-pullback/homotopy
argument through (5); read L848's hypotheses, conclusions and proof
passages for (3)–(6), (12)–(14), including the sector and branch
qualifications. Reused the completed audit recorded in the checkpoint;
no certificate was rerun. Its positive K is a diagonal limit, not a
collar theorem. Its data are stated smooth; any stronger real-analytic
regularity needed for a theorem must be justified in the mathematical
application. Do not silently replace G by its polynomial evaluator.

Read the relevant comparison sections of
`2026-11-06-actual-g-radial-graph-full-phase.md` and
`2026-11-06-actual-g-exchange-diagonal-audit.md`, and
`ATTEMPTS/2026-11-06-exchange-diagonal-averaged-extension-stop.md`.
Targeted searches for Cauchy–Kowalevski, Cartan–Kähler, Briot–Bouquet,
Fuchsian, prescribed jets and exact collars in the named actual-G and
exchange literature/history/failure paths located no earlier solution
of this target. This bounded duplicate check does not certify novelty.

L847 excludes product graphs globally. L848(7) excludes one explicit
extension globally. Neither excludes another coupled graph near the
diagonal. Reuse the Lawrence–Yamauchi and Lotay–Pacini hypothesis
comparisons from the full-phase assessment: they still do not supply
prescribed-data realization through the retained collision zero. Those
sources and the evaluator's analytic/software contracts need no refresh.

### Primary local-existence and obstruction comparisons

**Analytic Cauchy problem.** Marc Chaperon, *On the Cauchy-Kowalevski
theorem*, dated 9 January 2007,
[Section 2, unnumbered theorem p4 and proof pp4–7](https://webusers.imj-prg.fr/~marc.chaperon/Chaperon_Cauchy_Kowalevski.pdf#page=4).
For real or complex Banach spaces E,F, analytic f near the initial
1-jet and analytic initial germ u0, the solved system
partial_t u=f(t,x,u,partial_x u), u(0,x)=u0(x), has a unique local
analytic solution. Read the zero-data reduction, rescaled integral
equation and final implicit-function/uniqueness argument. The source
also gives the analytic implicit function theorem in Section1,
Corollary1 p2, assuming an invertible partial derivative.

For our problem an analytic solved normal system and compatible data
have not been established. L847(4) is an implicit full-density condition;
the diagonal collision is retained. A bare invocation of this theorem
would skip its main application obligation. A later attempt may test a
changed-variable or normalized formulation, but must justify its
equivalence through the zero and its derivative condition. Smooth data
or a formal expansion alone do not invoke this theorem. No reproof of
Cauchy–Kowalevski is needed.

**Exterior differential systems.** R. L. Bryant, S. S. Chern, R. B.
Gardner, H. L. Goldschmidt and P. A. Griffiths, *Exterior Differential
Systems*, MSRI Publications18, Springer, 1991,
[Chapter III, Theorems2.1–2.2, pp70–74](https://sites.math.duke.edu/~bryant/MSRI-v18-Bryant-Chern-et-al.pdf#page=70).
Theorem2.2 requires an analytic differential ideal, a connected analytic
Kähler-regular p-dimensional integral P with r(P)>=0, and an analytic
codimension-r(P) restraining manifold containing P and transverse to
its polar spaces. It yields a locally unique (p+1)-dimensional analytic
integral in that restraining manifold. Read the polar-rank reduction
to a solved Cauchy system and propagation of the remaining equations.
Regularity/transversality for our vanishing form remain unverified;
analyticity alone does not satisfy this theorem.

In [Example3.5/Theorem3.6, pp79–80](https://sites.math.duke.edu/~bryant/MSRI-v18-Bryant-Chern-et-al.pdf#page=79),
the ideal is generated by the standard symplectic form and
Re(dz1 wedge ... wedge dzn). Every analytic isotropic (n-1)-submanifold
extends uniquely locally to an n-dimensional integral. Read the
polar-space computation and following smooth-data caveat. This uses
the standard nonvanishing form and an additional symplectic condition.
It does not prescribe our full normal data or handle our density zero;
no coordinate equivalence or collar conclusion is imported.

**Singular analytic PDE, including resonance.** R. Gérard and H.
Tahara, *Holomorphic and Singular Solutions of Nonlinear Singular First
Order Partial Differential Equations*, Publ. RIMS **26** (1990),
979–1000, DOI10.2977/PRIMS/1195170572,
[Main Theorem(I), p981; Section1 Theorem1 and proof, pp983–987](https://ems.press/content/serial-article-files/42545?nt=1#page=3).
The equation is t partial_t w=H(t,x,w,partial_x w), with H holomorphic,
H(0,x,0,0)=0 and H_v(0,x,0,0)=0. If
rho(0)=H_w(0,0,0,0) is not a positive integer, a unique holomorphic
solution with w(0,x)=0 exists. Section1 also proves convergence of
formal solutions with coefficients holomorphic on a common polydisk;
this does not assert formal existence in resonant cases. Read the
nonresonant recurrence/majorant and the positive-integer compatibility
cases through the following remarks on p987. Higher tangential
derivatives are outside that theorem, as its Remark1 emphasizes.

No such reduction or coefficient computation for our actual phase
equation is established. If this form arises later, check all its
hypotheses and any resonance compatibility, rather than silently
assuming nonresonance or convergence. The stronger classification of
sectorial singular solutions is unnecessary for a smooth two-sided
collar and is not imported. Tahara's 2009 paper, PRIMS45,393–449,
[Section1 A1–A3 and Theorem1.1, p394](https://ems.press/content/serial-article-files/41073?nt=1#page=2),
was read to follow its reference to this original source; its
coupling-equivalence Theorem1.4 is not an input.

**A different singular class does not remove the conditions.** D. B.
Bacani and H. Tahara, *Existence and Uniqueness Theorem for a Class of
Singular Nonlinear Partial Differential Equations*, Publ. RIMS **48**
(2012),899–917, DOI10.2977/PRIMS/90,
[Section2, assumptions(A1)–(A3), (2.3)–(2.4), Theorem2.1, pp900–902](https://ems.press/content/serial-article-files/41185#page=2).
Read these hypotheses, the function-space definitions and the
characteristic estimate used in Section3. Here t>=0 is real, H is
continuous in t and holomorphic in x,w,v, H(0,x,0,0)=0,
H_v(0,x,0,0)=x gamma(x), gamma(0)!=0. The inhomogeneity and
H_v(t,0,0,0) are O(mu(t)), for a positive increasing continuous weight
with integral mu(t)/t finite. With negative real parts of both
H_w(0,0,0,0) and gamma(0), the theorem yields a unique weighted
solution, holomorphic in x and C1 for t>0, on a shrinking domain.
Neither these conditions nor smooth two-sided extension through t=0
are supplied for our problem. It is scope evidence, not a fallback
existence theorem for arbitrary degenerate data.

### Search, readiness and bounded mathematical decision

Queries actually issued included:

- `special Lagrangian Cauchy problem prescribed real analytic curve holomorphic volume form zeros Bryant Cartan Kahler`;
- `Cauchy Kowalevski theorem first order fully nonlinear noncharacteristic initial hypersurface lecture notes theorem`;
- `"holomorphic" "volume form" "vanishing" "Cauchy" contour`;
- `"Briot-Bouquet" partial differential equation existence theorem Tahara analytic t du dt`;
- `Gérard Tahara 1990 singular nonlinear partial differential equations Briot Bouquet holomorphic solution 1990 pdf`;
- `"prescribed" "holomorphic" "2-form" "degenerate" "real" graph`;
- `"Cauchy problem" "vanishing" "holomorphic volume"`.

No inspected theorem matches TARGET directly. This does not show that
none exists. The author's Hiroshima introductory PDF timed out; its
snippet was not evidence. The accessible original Gérard–Tahara paper
supplies the needed analytic theorem and resonance cases. PDF screenshot
calls produced no readable images (two timed out); the cited textual
statements/proof cases were inspected instead. Search hits for later
systems, sectorial classifications and 2019/2020 uniqueness papers are
unread leads, not assumed inputs; they are unnecessary for the bounded
first formulation test. No essential source blocker persists.

The decision is EXPLORE, not an imported solution or novelty claim.
The exact target is unchanged. One later mathematical attempt may use
the full L847 determinant, prescribed L848 data and the inspected local
methods to test an exact formulation and its solvability. Preserve the
original orientation, exchange symmetry, periodicity and every zero.
A construction must give an actual smooth graph, a single epsilon>0
for the whole diagonal, exact Im q=0 and Re q>=0 there, and a smooth
periodic extension to the torus. Any compactness or patching argument
must first have compatible actual local solutions; it cannot create
exact reality from jets. A contradiction must name the forced
compatibility condition and its failure for these data. Failure of one
gauge, normal form or theorem hypothesis stops only that mechanism.
Formal jets, a sampled residual and the accepted positive K alone do
not pass the target's test.

Essential inputs are L018/L775, audited L778(2)–(5) with step433's
analytic/software qualifications, L847(1)–(4), and audited L848(1)–(14).
All theorem-applicability, exact-collar, uniformity, gluing, global-sign
and RH gaps remain open. Full matching Mathlib coverage is unchecked.
No cross-notebook input is used. This review changes no canonical
lemma, mathematical script, DAG edge or argument in PROOF.md.
Newly ready coverage receives a separate approval next turn; this
literature step does not invoke the proposed mathematics.

## Original nomination — preserved; source readiness superseded above

## Exact proposed test and relevance

Keep actual G,R,C,omega and the original dt wedge ds orientation of
L018/L775/L847. Prescribe exactly h,b of audited L848(4), retaining
the collision zero and every actual-G zero. Ask for a real smooth
2pi-periodic u with u_2(t,s)=u_1(s,t), diagonal value h and normal
derivative b, and some epsilon>0 such that q_u is exactly real and
nonnegative whenever the circular distance between t and s is below
epsilon. The graph must still be defined smoothly on the whole torus;
no sign is requested outside that collar. Do not replace exact reality
by positive real part, a finite Taylor expansion or sampled residuals.

The main gap is L030–L032/C032a all-degree mixed positivity. A uniform
exact collar could turn accepted diagonal data into a usable local piece
of a future coupled contour. It would leave global gluing, all-angle
reality/sign, other orders/shifts and uniform transfer unresolved.
Conversely a rigorously scoped incompatibility would redirect this
prescribed-data construction while preserving L848 and other graphs.

The later mathematical decision test is either an actual construction
with controlled regularity, a single uniform epsilon and the exact
full-density condition, or a specific proved obstruction to these data.
Formal jets alone, a positive leading coefficient or compactness without
an exact-reality construction do not pass. No expansion, PDE
noncharacteristic claim or convergence argument was derived in this
nomination. The next invocation must first assess the required standard
methods and relevant known obstructions, then approve or narrow the
target for a separate mathematical turn.

The essential local inputs are L018/L775, audited L778's evaluator
with step433 software qualifications, L847(1)–(4), and audited
L848(1)–(14). L847's product stop and the recorded averaged-extension
stop remain at their stated scopes. No cross-notebook theorem is used;
full matching Mathlib coverage is unchecked.
