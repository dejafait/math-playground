# One-step canonical child energy — completed source comparison

TARGET: Audit the one-step canonical child admissibility and energy exponent through eq:inverse-step-loss in family 003 at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a, using L535/L536 with arithmetic, source-witness and principal/tail estimates retained as contracts and without assuming the canonical reduction conclusion.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused both ready Fourier assessments and searched the family003 assessments, audit notes and histories for canonical-moment, canonical-energy, inverse-step-loss and child admissibility; no completed matching child-energy audit was located. Exact web queries for canonical marked estimate plus Quasi-Riemann and for the pinned commit plus canonical supplied no usable independent matching theorem. Source-label searches located the actual statement and essential proof cases; no novelty is inferred.
SOURCE_EVIDENCE: Read the pinned primary TeX definitions 6819–6872, full lem:canonical-moment and eq:canonical-energy 8753–8796, node invariants 9230–9264, block/reduction and full-support conventions 9406–9487, source-witness identity 9711–9731, second lengths 10049–10138, full child admissibility cases 10299–10492, polynomial 10532–10556, and positive-child/energy-loss/aggregate-loss cases 10702–10832. Bibliographic framework references were identified, not independently imported.
COMPARISON: The source explicitly claims the target conditional reduction with loss 40 eta+tau+pi; it provides the exact coefficient class, independent full windows, clipping, two margins and normalization to be audited. L535/L536 already cover the conditional common Fourier interfaces but do not prove these remaining application obligations. This is source-claimed mathematics; any successful next audit is conditional reproduction, with no new zeta bound or originality claim.
GAP: Independently verify that the actual children meet the complete canonical class and source-witness margin/row requirements, then check the normalization and single aggregate loss using the uniform smaller-row energy hypothesis; do not assume lem:canonical-moment or eq:canonical-reduction-contract as the conclusion being tested.
REASON: Essential unread source coverage has now been supplied and compared with the local interface outputs. A separate application audit is justified because simply citing the full canonical theorem would bypass the exact reduction under review. This assessment approves coverage only, not mathematical correctness, and receives separate next-turn approval before research.
SCOPE: One nonterminal canonical node and its fixed dyadic/ray/slot branches through eq:inverse-step-loss, with ell+V>=d>0, eta<=d/16 and c_node>7eta. Restrict the parent to the exact canonical coefficient class and its two margins at least c_node; use L535/L536 with their existing arithmetic, source projection, fixed-support, fibre/count and principal/tail contracts. Assume only a uniform canonical energy bound for admissible strictly smaller-row children, not the parent theorem, full induction or final reduction. No cross-notebook input.
LITERATURE_REASON: The full canonical-moment coefficient/support hypotheses and canonical-energy normalization were essential unread inputs beyond the ready second-edge assessment; the present review supplies those inputs without repeating its Fourier audit.

Primary source: OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re(s)>7/8*, September 30, 2026,
[pinned build/paper.tex](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
The former pending assessment is superseded only as a coverage decision.
No application verdict, new lemma or calculation was produced in this
literature-only turn. Source labels are the precise locators; retrieval
line numbers are aids for the pinned file.

## Complete theorem hypotheses and comparison

The source's `lem:canonical-moment` fixes bounded nonnegative ranges of
M,N,V,z_0, a fixed slot cap, and c_*>0. Its squarefree label f avoids S
and has norm comparable to Z^V. Its weight w(f) is nonnegative, depends
on f alone and satisfies one fixed bound C d_O(f)^C; neither its choice
nor C depends on Z, rows or other averaged variables. The estimate is
uniform over all such weights, moving moduli and frozen outer ideals.

The column coefficient is precisely bar(alpha)(n) gamma_2(n), multiplied
by a genuine multiplicative finite ray character nu whose full defining
modulus has prime support in S, a radical indicator puncture rho, the
displayed moving characters chi_n(k) chi_n(f)^4, the product-form mark,
and a smooth annular test W(q_n/Z^N). No extra residual b(n) is allowed,
even if bounded and independent of k,f. Nu, rho, slot lists and individual
prime coefficients are independent of both current averaging variables.
The source allows k to be a general nonzero element, not necessarily
squarefree or prime to S. Every character power retains its zero on
nonunits, including powers divisible by six (6819–6823).

The precise mark `old-eq:4.2` (6861–6864) sums over tuples from disjoint
prime lists the product of individual coefficients times 1_{p_i|n}.
Its nominal total slot length is at most z_0. Subcollections retain that
cap. Pointwise divisor domination alone is insufficient for this class.
A fixed puncture may depend on earlier frozen ideals but is the indicator
of coprimality with one squarefree radical, independent of k,f.

With F_0=N+V and Q=log_Z q_(r_rho), the theorem requires
F_0-M-Q-z_0>=c_* and 4F_0-3M-6z_0>=c_*.
Its energy is the f-weighted row sum of the squared column, normalized
by Z^(-V) outside and Z^(-N/2) inside. It asserts E<<Z^(F_0+epsilon),
with finite smooth-seminorm dependence and fixed polynomial height cost,
uniform over the allowed frozen data and slot subcollections.
This is a transcription of the source statement, not its import as a
verified theorem or a premise for the parent step.

The relevant local outputs have the following matching data and remaining
checks. These are comparison obligations for the next turn, not proofs.

| Canonical requirement | L535/L536 output and audit obligation |
| --- | --- |
| Exact coefficient, genuine finite ray character | L536 (8) has bar(alpha) gamma_2 and nu_i bar(vartheta). Restrict the parent to canonical data and check that this is a genuine fixed ray character with no moving prime in its defining modulus; the extraction identities remain contracts. |
| Radical indicator puncture fixed before k,f | L536 fixes gamma=(q_0,t',r_g) and rho_gamma=rho 1_(n,rad(q_0)t'r_g)=1. Its interface permits the inherited rho; for the canonical application require the original rho itself to be a radical indicator, not an arbitrary unit-modulus factor. Bound the actual radical using source witnesses, not count balls. |
| Product-form marks, original fixed cap | L536 retains d'_a. Source 10321–10333 asserts that old survival exclusions are supplied by the new characters/puncture, so these are original subcollections. Check this assertion under the slot/extraction contracts rather than replacing it with a divisor bound. |
| Fixed label-only weight | L536 (15) supplies D_K(f)=d_O(f)^(9+4K), with K fixed by the slot cap. This is the source's stated candidate w; do not move gamma-dependent C_K into it or count f again. |
| Full independent annular windows | Source 10334–10360 uses fresh columns and full I_f, included in the fixed-depth window family before Z is large. L536 assumes these supports; added positive terms need no parent reconstruction. Check bounds on the full supports, without assuming old product identities for added terms. |
| Nonnegative lengths and uniform tests | Retain nonempty row/column gates, M_ch=M_c+eta, V_c>=0, N_ch=max(0,N_c), delta_N in [0,6eta]. Source clipping 10361–10383 bounds 1<=Z^delta_N<=b and uses W'_a(z)=omega_n,a(Z^delta_N z) z^(epsilon_a i zeta_a). L536 covers the clipping interface; no second root enters W'_a. |
| Two positive margins, shorter rows | Source transition and source-witness claims 10423–10487 must be applied to every gamma in Gamma_sigma. They are not proved by the already audited Fourier density. |
| Height uniformity and common measures | L535/L536 give every fixed joint weighted Fourier moment with zero additional Fourier exponent. Apply the child hypothesis with finite seminorms and fixed polynomial height cost, uniformly in gamma and sector data; no cutoff-dependent Z power may replace these costs. |

## Essential proof cases now read

The source freezes F=N+V and the actual Q at a node; it never replaces F
by an actual column norm (`eq:inverse-fixed-invariant`, 9230–9243).
Its remaining blocks satisfy ell+V>=d (9422–9424). The conditional
reduction statement (9426–9450) assumes the energy estimate uniformly
only for children with 0<=M'<=M-d, N',V'>=0, F'<=F+11eta and both
margins at least c_node-7eta, with eta<=d/16. That assumption is the
allowed smaller-row input; the parent conclusion is not an input.

The source fixes Gamma_sigma as a structural projection before current
rows, labels or modes. Each triple must have a source witness retaining
the exact cube reconstruction and divisibility d_2|g' (10400–10422).
The relevant arithmetic lead `eq:inverse-cube-actual` (9711–9721) records
actual cube lengths, not independently rounded centers. Source
`eq:inverse-center-inequalities` keeps the errors g-theta>=-2eta and
j<=2ell+3eta. Its new-puncture bound is Q_new<=Q+D_c+4eta, where
D_c=ell+A_i+t+g-theta+V. Count balls alone do not supply that bound.

The exact source transition `eq:canonical-transition` states
F_c=F-D_c-2ell+j, M_c=M-2D_c-2ell+j, F_c-M_c=F-M+D_c, and
4F_c-3M_c=4F-3M+2(A_i+t+g-theta+V)+j.
The subsequent claimed margins are at least c_node+delta_N-5eta and
c_node+4delta_N-7eta. The claimed row decrease is
M-M_ch>=2(ell+V)-8eta>=2d-8eta, and F_ch<=F+11eta.
These are the precise thresholds to independently test, including
positivity of the retained margin; none is certified in this review.

Source `eq:inverse-positive-child` (10728–10750) identifies the raw
positive sum H with Z^F_ch E for the same row ball, or with an upper
bound using a larger fixed canonical row ball. Source
`eq:canonical-prefactor` states kappa_i+lambda_c+C_c+2F_c=F.
The energy passage (10775–10812) assumes E<<Z^(F_ch+epsilon_child),
then claims the exponent
F+28eta+2delta_N+tau+pi+epsilon_child
<=F+40eta+tau+pi+epsilon_child.
It explicitly attributes two delta_N terms to restoring normalization
and to the child exponent. Each geometric mean retains the same loss,
and each discrete count and normalized mass occurs once.

The source's aggregate-loss paragraph (10813–10829) allocates
pi_beta, pi_old, pi_count, pi_fib and the finite-union dyadic losses
inside one pi, by choosing the free input exponents after bounded
scale ranges are fixed. Pi hides neither eta nor tau. The next audit
must retain that finite allocation as an explicit contract or check its
one-step application; it may not give each constituent a fresh pi.
Principal/tail estimates remain contracts, with the source claiming
first principal Z^(M+pi) and second at most Z^(F+26eta+tau+pi).

## Literature reuse, qualifications and next test

Reuse the first- and second-edge assessments and L535/L536; their exact
Fourier statements need no renewed literature search. Targeted local
searches found the pending nomination and the explicit exclusions in
the preceding records, not a duplicate completed energy audit. Preserve
the documented hazards: a count-ball child domain, parent identities on
independently added terms, deleted survival masks, duplicated root or
discrete mass, or a Z exponent increasing with height order.

The source cites Heath-Brown, *A mean value estimate for real character
sums*, Acta Arith. 72 (1995), 235–275, Section 2
([DOI](https://doi.org/10.4064/aa-72-3-235-275)); Heath-Brown,
*Kummer's conjecture for cubic Gauss sums*, Israel J. Math. 120 (2000),
97–124, Section 4 ([DOI](https://doi.org/10.1007/s11856-000-1273-y));
and Goldmakher–Louvel, *A quadratic large sieve inequality over number
fields*, Math. Proc. Camb. Phil. Soc. 154 (2013), 193–212, Sections 4–7
([arXiv](https://arxiv.org/abs/1112.1642)). Their bibliographic entries
and source comparison were read; the original papers are unread framework
leads, not substitute theorems imported here. No inspected independent
stronger result certifies this particular child interface. The source's
own canonical theorem is stronger than the one-step target but citing its
conclusion would defeat the stated independent application test.

Pass the separately approved audit only if every canonical hypothesis
matches and the displayed one-step loss follows under exactly the
specified contracts and smaller-row input. Narrow or stop on any
unmatched coefficient, puncture, support, surviving mark, normalization,
margin or order-uniformity condition. A pass would remove one conditional
recursive obligation; depth/initialization, arithmetic proofs, all full
coordinates, auxiliary accounting, bootstrap, H, import closure and
actual-Xi all-degree positivity remain open. Mathlib coverage for the
matching recursive interface is not checked; no absence claim is made.
No creative central-sign mechanism is prepared by these conditional
moment inputs, which provide no actual-Xi sign bridge. No new lemma or
mathematical script was written. Direct curl failed DNS; the primary web
reader supplied the needed theorem and proof cases, so access is not blocked.
