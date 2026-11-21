# Complete three-particle current — bounded attempt nomination980

TARGET: Attempt the complete localized Stokes identity for C466x's three-particle raw flow under sqrt(3)a+M_1 T_0<R, proving outer-exit exclusion, full-form L1_loc control and vanishing collision/initial-diagonal cutoff flux, or exhibit an admissible defect.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed review980 in 2026-11-14-three-particle-complete-current-review-979.md records changed-scope searches, C466x/C466u duplicate comparison, C466t's earlier-stop obstruction and closure979. No inspected exact or stronger theorem or admissible counterexample was identified; no novelty inference.
SOURCE_EVIDENCE: Reuse TNV https://arxiv.org/pdf/1706.03822v2 Appendix B (B.1)-(B.5) p22 and Section2.2 raw-blow-up cases; Teschl https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf Lemma2.14/Corollary2.15 p52 and Theorem6.1/proof pp189-190; WKM https://arxiv.org/pdf/2008.10321v2 Section3.1 (29), Theorem4/Proposition5 and proofs pp8-9, rechecked980. HP https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6102-11511_2008_Article_BF02838327.pdf Theorem2.1/Lemma2.2 pp40-41, Theorem4.1(b) pp45-46, Theorem5.2/proof pp48-49 is reused from review960. Newly compared Harvey–Lawson https://www.math.stonybrook.edu/~blaine/FiniteVolFlows.pdf math/0101268v1 Definition1.1/Theorem1.2/proof pp4-5. Full applicability/access qualifications are in review980.
COMPARISON: Local ODE and all-degree real compound tools cover compact survivors. C466x supplies the spatial input and C466u a different single-divisor complete proof; neither imports this identity. General removability, finite-volume-flow and rough-transport results require unpaid mass, geometry, regularity or trace assumptions.
GAP: Establish the exact buffer exclusion, complete three-/four-form integrability and defect-free cutoff passage for the coupled three-divisor raw flow, including triple collisions and all initial coincidences, or refute the exact statement admissibly.
REASON: Review980 supplies essential changed-scope coverage for one established-route proof/defect attempt, subject to separate approval next turn. No new specialization, buffer estimate or weak identity has been derived or approved as a theorem.
SCOPE: Exactly the fixed-data statement and sufficient test below; no added symmetry, separation, regular lifetime/preimage, endpoint uniqueness, changed metric, restart, sign or actual-Xi assumption.

## Exact statement to attempt, unproved

Fix real 0<a<R, finite T_0>0, M_1,M_2>=0 and complex H_0.
Let H be holomorphic on B={z in C^3: |z_j|<R}, H(0)=H_0,
with whole-B Hermitian bounds ||grad H||_2<=M_1 and
||D^2H||_op<=M_2. No symmetry or separability of H is assumed.
Put Delta=product_(i<j)(z_j-z_i), S=-2 log Delta+H and
F=Delta^2 exp(-H). Logarithmic derivatives define the raw vector
field on U=B minus {Delta=0}. Keep the unit flat metric,
dot X=conjugate(grad S), X(0,u)=iu for pairwise distinct
u in I=(-a,a)^3, and the first maximal lifetime [0,tau(u)) in U.
Assume exactly the proposed strict buffer sqrt(3)a+M_1 T_0<R.

On Q=(0,T_0) times I let
D={(t,u) in Q: Delta(u)!=0, t<tau(u)} and Psi=X on D only.
For every real or complex chi in C_c^infinity(B), retain

    Omega=F dz_1 wedge dz_2 wedge dz_3,
    beta=Psi^*(chi Omega),
    gamma=Psi^*(dchi wedge Omega).

These are complex-valued real differential forms. Beta includes
its spatial coefficient and all three coefficients containing dt;
gamma is the full four-form. Orientation is
dt wedge du_1 wedge du_2 wedge du_3. Bars mean coefficientwise
zero extension from D to Q, including every stopped parameter
and every initial diagonal; no stopped-map derivative is defined.

The target is: no first outer exit at a time <=T_0 for the
specified distinct initial data, all coefficients of bar(beta)
and bar(gamma) belong to L1_loc(Q), and

    d bar(beta)=bar(gamma) in distributions on Q.

No unique limiting endpoint, regular first-hit surface, collision
restart or weak boundary trace may be assumed. Include triple
collisions and tests meeting the intersection of initial diagonals.
Compact test support removes external Q edges only. The gamma term
must remain; no sign or conserved global integral is asserted.

## One bounded proof/defect test

First prove or refute outer-exit exclusion using the actual singular
ODE and the stated strict buffer, with M_1=0 and simultaneous limiting
events retained. M_1 is a bound on grad H, not full raw velocity.
No continuation outside B or through Delta=0 is licensed.

If exclusion holds, use the assessed compact-survivor variational
and arbitrary-k compound tools to investigate every needed weighted
minor, including velocity columns and exterior degrees three/four.
Do not reprove known tools or repeat the spatial bound as if it paid
the complete form. Justify all stronger singular estimates explicitly;
no independent-pair coordinate treatment is assumed. C466x is the
existing spatial input; C466u's complete proof is a comparison whose
new applicability requires proof, and C466t is the preserved earlier-
grazing obstruction rather than a premise implying this statement.

One sufficient weak-limit test is to construct smooth survivor
cutoffs eta_epsilon, 0<=eta_epsilon<=1, tending to1 on D, with
locally interior survivor support after zero extension. For compact
tests, prove coefficientwise L1 convergence of eta_epsilon beta and
eta_epsilon gamma to their zero extensions and, for every scalar
phi in C_c^infinity(Q),

    integral_D phi d eta_epsilon wedge beta ->0.

This is an unproved threshold, not a derived criterion or estimate
in this literature step. All collision and initial-diagonal fluxes,
including triple intersections, must be paid by the full differential.
Do not transfer C466u's one-shell residence bound to this flow without
proof. Another rigorous weak-limit method may replace these cutoffs
only if it establishes the same complete identity. HP's homogeneous
removability theorem cannot silently settle the inhomogeneous equation.

Continue upon a complete justified identity or an admissible nonzero
distributional defect/nonintegrable coefficient. Failure of one
sufficient estimate is a narrower method stop, not a counterexample.
Preserve partial reasoning before lengthy work. Return after this one
coherent attempt; no supplementary sign search or spatial-bound audit.

## Relevance and routing

The main gap remains L030-L032/C032a actual-Xi all-degree algebraic-
square positivity. This could pay one intersecting-divisor boundary
step in later signed contour assembly. Actual-H realization, phases,
signed/global assembly and all-order signs remain independent. No
implication to actual-Xi positivity or RH candidate is claimed.
Matching Mathlib coverage is unchecked, not absent; no cross-notebook
input. Primary source gaps essential to the selected local cutoff
method are covered; HP's transient recheck timeout is not a blocker.

Nominate proof_attempt/development, deep_research/xhigh. This is a
difficult established-tool extension across coupled singular divisors,
not a new central creative mechanism. Such a mechanism remains
unjustified because the bridge to actual-Xi signed positivity has not
been specified. Expected research classification is POTENTIALLY_NEW
only in the bounded-search sense, not certified originality. This
new ready continuation receives separate source approval next turn;
review980 itself is not a mathematical attempt or that approval.
