# Plectic rationality source review

Date: 2026-10-26. Literature-only step 511; no lemma or mathematical
script is authorized. The target remains the exact action assessed in
`drafts/literature/2026-10-26-plectic-rational-exterior-source-review.md`.

The central gap is rational Kummer membership and nonvanishing for an
actual strict class over Q; the complex-order comparison is independent.
The intermediate target is a proved rational exterior-square producer.
Such an object could support L005's rank lower bound after justified
descent and strict contraction. Continue only if primary theorems supply
an independently testable arithmetic construction; abandon direct import
if rationality, Q-descent, or nonvanishing is only conjectural or assumes
the missing rank/Sha conclusion.

Local inputs inspected: full L005 and L122; ATTEMPTS/003, /004, /030;
foundations/08. The latter records that cohomological specialization of
diagonal cycles does not itself give a Chow-valued specialization to
points. Existing unfinished notebook changes are preserved.

Primary sources inspected:

- Fornea–Gehrmann, *Plectic Stark–Heegner points*, arXiv:2104.12575v1
  (26 April 2021), Sections 1.1, 1.4: general determinant rationality is
  Conjecture 1.3, rather than a theorem. Published in Advances in
  Mathematics 414 (2023), 108861, DOI 10.1016/j.aim.2023.108861.
- Fornea–Gehrmann, *On the algebraicity of polyquadratic plectic points*,
  arXiv:2203.15998v1 (30 March 2022), Assumptions 1.1, 1.5, 1.7,
  Theorems A–C, Corollaries 4.6–4.7, Theorems 5.1–5.2 inspected.
  This is a substantive proved algebraicity exception; its precise
  determinant construction in Theorem 5.3 and its complete proof were
  subsequently inspected, preprint pp.15–16. Published IMRN 2023 (22), 19237–19265,
  DOI 10.1093/imrn/rnad091; the inspected full text is the v1 preprint.
- Fornea, *Plectic Heegner classes*, arXiv:2603.28327v2 (13 April 2026),
  Section 1.1 hypotheses, Theorems A–C, Conjectures 1.9–1.10,
  Proposition 2.18, Theorem 2.20, and Corollary 4.24 with proof inspected.
  A global H^1 factor is proved; global Selmer membership and determinant
  rationality are separately conjectured. The descent in Theorem 2.20
  concerns the Shimura-curve covering, not a theorem giving Q-points.

## Precise scope of the proved polyquadratic exception

[Fornea–Gehrmann, arXiv:2203.15998v1](https://arxiv.org/pdf/2203.15998v1),
Sections 1.1–1.3, 3.2, 4.3, 5 (preprint pp.2–6, 8–9, 14–16).
Here A is the elliptic curve and E is a number field, not the notebook's
elliptic-curve variable. Required data include

\[
 E/F\text{ CM},\quad F/F_0\text{ Galois with group }(\mathbf Z/2)^t,
 \quad E=FE_0,\quad [E_0:F_0]=2,\quad r=|S|=2^t.
\]

Assumptions 1.1, 1.5, 1.7 require unramified conductor in E/F;
multiplicative reduction at the inert primes in S; square-free residual
inert conductor with the specified archimedean parity; all nontrivial
subextensions of F/F_0 ramified; its ramified primes split in E_0;
A is base change of modular A_0/F_0 with conductor unramified in F/F_0;
S is the set above one prime wp totally split in F; and the corresponding
square-free/parity Heegner condition over F_0. Section 4 additionally
uses a character pulled back from E_0 and a conductor supported at
totally split primes (Assumption 4.1). The trivial character is sufficient
for the present comparison.

Theorem B gives, for that character,

\[
 w\in\bigwedge^r_{\Omega}(A(E)\otimes\Omega),\qquad
 N_{S/\wp}\operatorname{pr}_S^-(P_{A,S})
 =N_{S/\wp}\operatorname{pr}_S^-(\det w),
 \quad [\Omega:\mathbf Q]=2.
\]

Theorem 5.3 extends this to characters when p does not split in their
coefficient field; the coefficient extension splits at p. Its proof
wedges Heegner points on the different quadratic twists of A_0, uses
the character-table determinant, and rescales using the square root
from Corollary 4.7. These are algebraic coefficients, not arbitrary
p-adic coefficients. Remark 1.10 gives norm injectivity on the indicated
partial-Frobenius eigenspace for degree-one wp. Theorem A/5.1 uses
nonzero projected norm to give both ranks equal to r over E; the proof
reduces to the rank-one twisted Heegner-point theorem (Proposition 3.1).
Theorem C/5.2's trivial-character converse retains the additional
algebraic-rank expression rho_A(S)=r. None states the Q-exterior-square
producer sought here. The published OUP full-text endpoint failed;
claims above are deliberately tied to the inspected v1, not silently
attributed to an uninspected final version.

## Partially global construction, including its descent

[Fornea, arXiv:2603.28327v2](https://arxiv.org/html/2603.28327v2),
Sections 1.1–1.2, 2.3, 4.3–4.4. A/F is modular, F totally real, E/F CM,
and its conductor is unramified in E. The inert conductor is square-free
(1.1). The incoherent set consists of inert multiplicative p-adic primes,
with parity as in Definition 1.2, and |S_cal|=r-1. Assumption 1.4 requires
p>=5 and residual image containing SL_2(F_p). For conductor c prime to
the curve conductor and an anticyclotomic character chi, Theorem A gives

\[
 \kappa^\chi\in
 \left(\bigotimes_{v\in S_{\rm cal}}H_f^1(E_v,V_p(A))\right)
 \otimes_{\mathbf Q_p}H^1(L_c,V_p(A))^\chi.
\]

Corollary 4.24's full proof uses Galois invariance, reciprocity and a
character sum to descend to L_c, an abelian extension of E. Theorem 2.20
is descent along a Shimura-curve covering at fixed field; neither is
descent to rational points over Q. Conjectures 1.9 and 1.10 separately
assert the global Selmer criterion and rational determinant comparison.
Theorem B recovers mock invariants after a partial-Frobenius projection
when F=Q and S_cal={p}. Comparisons B/C also require 1.5: split conductor
primes have inertia degree one, avoid the different, and exponent <=2.
C requires an auxiliary p-adic w outside S_cal and 1.7: no p-th roots of
unity in F_w and Tate parameter not a p-th power. It is not a statement
about localizing the global factor at the same prime in S_cal. Full
defining integrals and same-prime localization have not been audited.

## Mock specialization and its strongest inspected rank theorem

[Darmon–Fornea, *Mock plectic points*, JIMJ 24 (2025), 2107–2131](https://doi.org/10.1017/S1474748025000179),
Section 3, Theorem 3.8 with proof and Conjectures 3.12–3.13 inspected in
the published HTML. The simplified setting has curve conductor p,
imaginary quadratic K of class number one, and p inert in K. The proof
of the Selmer criterion uses Kolyvagin derivatives and local Neron
component groups. The determinant regulator remains Conjecture 3.13;
Selmer membership is not presented as rational Kummer membership.
The author offprint titled *Mock plectic invariants* has earlier
conjecture numbering (3.11–3.12); use the published numbering here.

[Fornea–Gehrmann, arXiv:2311.03100v2](https://arxiv.org/html/2311.03100v2)
(2 December 2024), Assumptions 1.1–1.2, Theorem 1.3/3.4 with proof,
Proposition 2.11 with proof, Remark 1.4, Conjecture 2.16 inspected.
It allows N=p N^+ N^-, N unramified in imaginary quadratic K, p inert
and multiplicative, N^- square-free with an even number of factors,
K different from Q(i), Q(sqrt(-3)); additionally p>=5, surjective E[p],
and ramification at ell|N^- with ell^2=1 modulo p. Under

\[
 L(A/K,1)=0,\qquad \mathcal Q_K\ne0,
\]

the theorem gives p-Selmer corank two over K, plus its stated maximum
condition for the two quadratic twists over Q. The proof bounds corank
by three through the Euler system and uses parity. Remark 1.4 requires
finite p-primary Sha to replace Selmer coranks by rational ranks.
Conjecture 2.16, not the theorem, supplies the exterior regulator.
No finite-Sha premise has been imported to close the notebook's gap.

## Decision and coverage limits

Reject the direct Q-rational-exterior import from these inspected
theorems. This is an informative negative source comparison, not a
nonexistence theorem for plectic geometry. Multiplicative reduction at
the construction prime also fails L005's good-reduction hypothesis;
changing that threshold requires its own justification. Nonvanishing,
point membership, Q-descent, and the complex-order comparison remain
separate. All Mathlib coverage is **not checked**; no new theorem or
reproof is recorded.

Searches performed: "plectic Heegner points rationality exterior power
theorem Fornea Gehrmann"; "plectic Stark Heegner points rationality
conjecture theorem elliptic curves"; "plectic rationality 2026 elliptic";
"plectic algebraicity plus Gehrmann"; exact Iwasawa-paper title; and
the 2026 class title combined with "alternating" and "localization
diagonal", plus "plectic corestriction strict". Local plectic/mock/
polyquadratic searches found only the startup continuation. Search hits
and MathDB summaries were not used as theorem evidence. Non-Archimedean
plectic Jacobians, Hernandez–Molina's plus-part lead and the general
Nekovar–Scholl framework are not theorem-level assessments here.

A narrower possible mechanism is the same-prime localization of the
2026 partially global class after projecting both factors to Q-invariants.
That is a proposed local test, not a proved cancellation. Essential
construction/proof coverage for it is missing, so it receives a separate
REVIEW_REQUIRED assessment. No mathematical exploration budget was used.
