# Family 003 uniform high-probe margin — next source gate

TARGET: Assess source coverage for a bounded conditional audit of the positive, target-independent margin m supplied by prop:parameter-order in the final common-signal application of OpenAI family 003 at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a, keeping the underlying arithmetic estimates explicit.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the October 21 overlap assessment/register and family003-zeta-audit-scope review; searched the family003 assessments, working audit and dated family003 histories for parameter-order, late-height-closure and margin overlap. The parameter argument is already in the primary manuscript; L531 excludes it. Direct label searches retrieved its complete proof and relevant endpoint, outer-row, principal, moment-mesh and late-height statements; no novelty search claim is made.
SOURCE_EVIDENCE: OpenAI September 30 manuscript at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a, prop:parameter-order complete statement/proof (rendered lines 15331–15576) and final application (15577–15585); part-II-bootstrap (6402–6425), principal-residue-interface (5806–5926), late-height-closure (6129–6187), plain statement (11803–11894), detector-counts statement and relevant capacity/zero-capacity/height cases (14334–14665), and final normalization/exponent/range passages (14667–15324). Stable labels, exact URL and source-asserted contracts follow.
COMPARISON: The manuscript already states and proves the parameter selection. L531 covers only the downstream analytic reduction. A later independent audit is justified to check conditional loss allocation and quantifier order under explicit unaudited arithmetic contracts; it would be REPRODUCTION, with no stronger zero-free conclusion or discovery claim.
GAP: Independently verify the finite real-loss/mesh/slot selection and late height closure yielding the source's common m and sigma=m/2, conditional on its stated arithmetic bounds and uniformity. This review supplies source scope, not an audit verdict or verification of those bounds.
REASON: Complete accessible primary passages now isolate a bounded conditional audit and its unverified inputs. Missing whole-manuscript verification does not block this conditional target; proving the arithmetic contracts would require a different assessment.
SCOPE: Only the primary parameter proposition and directly necessary final substitutions under beta_*>7/8. No new arithmetic estimate, H construction, full manuscript audit, Dirichlet transfer, formal build, or new half-plane claim.

LITERATURE_REASON: The complete primary hypotheses, parameter inequalities and proof cases of prop:parameter-order are essential unread coverage for this changed target; the ready Section 2 assessment does not cover them.

## Invocation-start nomination, preserved

The following paragraphs record the original coverage question. Their pending
coverage language is superseded by the completed source review below.

The main gap remains actual-Xi all-degree positivity. The intended downstream
use is to test whether the common positive gap required by the verified
conditional reduction is actually supplied at the final application. The
existing source review names omega=Delta/2 and sigma=m/2; those substitutions
are leads, not a verification that a suitable m exists uniformly in eta.

Essential inputs for continuation are L531's precise conditional hypothesis,
the pinned manuscript's prop:parameter-order, and the final common-signal
application. L452/L461 identify the downstream branch and are not premises
for proving a new zero-free statement. No cross-notebook input is proposed.

The source-review test is to retrieve the exact proposition and relevant
proof cases, identify all margin inequalities and their dependencies, compare
them with the final substitution, and nominate one bounded audit only if
that coverage is complete. A missing arithmetic theorem must remain explicit;
the review must not silently promote the external zero-free conclusion to an
input. If the scope cannot be isolated, record the precise blocker and choose
a different independently testable target instead of repeating this review.

This nomination authorized no calculation or new lemma and entered this turn
as REVIEW_REQUIRED. No justified creative arithmetic bridge
is prepared by this audit, and the historical modulation stop is retained;
routine parameter specialization must not be relabeled creative. Full
matching Mathlib coverage of the parameter argument is unchecked.

## Completed source review — 2026-10-30

All mathematics below reports source statements and proof organization.
No coefficient identity, exponent inequality or uniformity claim was
independently verified in this literature-only turn.

Primary citation: OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane
Re(s)>7/8*, September 30, 2026,
[pinned TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
Line coordinates here are the web tool's rendered retrieval locations,
not PDF pages or physical TeX line numbers. Labels identify stable passages.

### Exact hypotheses and intended conclusion

The source's `eq:part-II-bootstrap` invokes its earlier 11/12 theorem:

    beta_*=7/8+Delta, 0<Delta<=1/24,
    kappa=2 beta_*-1=3/4+2 Delta<=5/6.

The supremum is over primitive finite-order Hecke functions over Q(sqrt(-3)),
excluding poles, as in L531. Retained bins have delta=2a-1<=kappa; the floor
is a=51/100, delta=1/50. The final section fixes h=13/16, ell=1/6,
l_x=17/48, l_y=23/48, d_min=1/100 and C(s)=s-11/16. The earlier 11/12
bound remains an unaudited premise; the final 7/8 conclusion is not a premise.

`prop:parameter-order` claims that geometry, real losses, capacity decrements,
slot system, amplitude/bin widths and extension precede eta. For each
primitive eta, fixed arithmetic data, tau_eta, N_eta and Z_0,eta may then
depend on eta. Its conclusion bounds J_II,eta by exponent C(7/8)+omega
and J_II,eta-f_II,eta by C(beta_*)-sigma, for all sufficiently large real Z.
Both functions are independent of analysis height T_1. Only omega and sigma
must be common: implied constants and thresholds need not be conductor-uniform.

### Margin inventory and all final proof cases

The normalization at 14716–14844 uses the same c_S A_T(Z) on both sides.
It asserts eventual nonvanishing and subpower growth of the inverse normalizer,
and principal approximation exponent 0<kappa_P<(7/8)min_i ell_i. For even K
and ell_i=ell/K the source chooses

    m_P=kappa_P=7/(96K), m_w=23/960, m_z=13/9600.

The principal remainder exponents are C(beta_*)+(1+h)e-m_w+epsilon,
C(beta_*)+e-m_z+epsilon and C(beta_*)+e-m_P+epsilon. The complete
`lem:principal-residue-interface` statement/proof (5806–5926) was retrieved:
global correction bounds, nonzero subpower normalizer, uniform residue error,
w/z poles and the separate main/error integrals. Those input claims are
not independently audited by this review or the proposed parameter audit.

`lem:high-bin` (14858–14993) gives the moderate-bin exponent as a supremum
over pointwise occurring (R,q), 0<=q<=delta/2, with an error coefficient
independent of eta on fixed real ranges and a fixed slot system. It assumes
buffered-bin, detector-dyad, prime-bound and cumulative height-allocation
hypotheses, and a discarded tail Z^B T_1^(-N) with B fixed before N.
Its statement and final exponent accounting were read; the underlying
internal contour and arithmetic estimates remain explicit contracts.

The source cases at 14994–15324 were read in full:

- Floor delta=1/50: E(h)<=-7/1200 and positive frequency slope.
- Small rows: full quotient-free correction and outer-row contract give
  m_small=63/800 before losses, with height degree zero.
- Large rows: exponent B_0+(h+zeta)(1+epsilon)-zeta z_infinity+epsilon,
  B_0=53/32, made small by fixed z_infinity after positive zeta.
- Live equality delta=alpha=5/6: separate no-slot amplified count R=1-delta,
  including r near or above 1; no marked estimate with shrinking strict margin.
- Interior 1/50<delta<alpha: detector-counts supplies
  R<=R_*+Delta/4+epsilon_row. `lem:balanced-endpoint` and the complete
  polynomial-certificate proof (15138–15214) assert -E_*>=49/440640.
  `eq:adaptive-endpoint` then compares E_actual(h)-Delta with zero,
  not E_actual(h). Its algebra remains a later audit question.
- d_min<=d<=1/2 uses no selected primes and exponent <=-49/14400;
  1/2<=d<=h uses positive slopes and prime supply; h<d<=h+zeta costs
  at most 2 zeta. The live equality endpoint remains separate.

The resulting source margins are

    m_hi=(51/64)Delta, m_high=min(m_hi,63/800),
    m=(1/4)min(m_high,m_w,m_z,m_P),
    omega=Delta/2, sigma=m/2.

These are extracted claims, not new bounds. Dependence on positive Delta
and fixed pretarget choices is allowed; a lower bound as Delta tends to zero
is not asserted or required by the source's family-supremum argument.

### Choices and essential conditional inputs

The complete proof at 15331–15576 first requests moment/capacity high costs
below m_high/8, then a uniform mesh, then even K with
2 ell/K<min(mesh,b_round,1/185). Disjoint smooth prime windows then fix m_P.
Later powers, amplitude width and e have high cost below m_high/8 and obey

    (1+h)e+epsilon_pr<m_w/4,
    e+epsilon_pr<m_z/4, e+epsilon_pr<m_P/4.

It requests zeta<min(1/48,m_high/16), then z_infinity and the common Euler
cutoff, and a normalization/dyad loss below m_high/8. It claims more than
3m_high/8 and 3/4 of each principal margin survive before choosing m.
The proposed audit must test existence in this order, not just cite its claim.

The complete `lem:plain` statement/context at 11803–11894 retains common
row/mask zero extensions, finite-ray coefficients, disjoint prime supports
and exclusion of inducing characters in Theta for positive slots. For
kappa<1 it assumes beta_*<=(1+kappa)/2; the application uses dynamic
kappa=2 beta_*-1, not a premise beta_*<=7/8. Its mesh depends only on
bounded real ranges and the requested loss, uniformly in kappa in [3/4,1].
Seminorm and height orders may depend on fixed slot count. Mesh independence
of slot count is essential to choosing K later. Its deep fourth-moment proof
is unread and remains an explicit assumption for the conditional audit.

The complete `prop:detector-counts` statement (14370–14405) and relevant
capacity, zero-capacity and height proof cases (14514–14665) were read.
They require prime supply strictly above 7/37, fine mesh and decrements
depending only on losses, Delta and bounded ranges, plus actual witness and
height conditions. They give finite height degrees uniform over moving rows,
the Delta/4 capacity allowance and separate no-slot limits. Witness, marked
moment, no-slot amplification and row-count proofs remain unaudited inputs.

The normalizer and Euler correction contracts, including H contraction for
the same excluded set as the physical probe, remain unverified inputs.
The parameter proof's retained A_eta and discarded scale degree B_eta must
be finite and independent of external order N. Detector ceiling tau_0,eta
is fixed after internal orders but before N and Z. The source's ceiling
argument and internal/external-order distinction (15516–15556) were read;
their underlying arithmetic uniformity is not independently verified here.

The complete `lem:late-height-closure` statement/proof (6129–6187) chooses
tau_eta<=min(d_min/100,tau_0,eta,m/[4(A_eta+1)]), then integer N satisfying
B_eta-N tau_eta<C(beta_*)-m/2, then the threshold. It assumes increasing N
changes only external seminorms, not retained orders or scale powers.
This distinction must remain explicit: extracting this conditional closure
does not verify that every preceding estimate supplies that independence.

### Decision, comparison and continuation test

The manuscript already proves the named proposition. A successful independent
check would be REPRODUCTION, not a new theorem. L531 explicitly excludes
these margins; the targeted local family003 search found no completed audit.
This is a bounded overlap search, not an absence claim about every notebook
file. The modulation failure in
ATTEMPTS/2026-10-30-weil-nullvector-modulation-source-stop.md is preserved.
It neither blocks this conditional audit nor supplies a creative arithmetic
bridge to RH.

Coverage now supports one conditional audit of real choices and late-height
closure. Continue only if the contracts suffice for all losses, endpoints
and choices to preserve one m>0 independent of eta. Record failure for
circular choice, a coefficient requiring eta too early, an omitted endpoint,
or a missing uniformity hypothesis. Do not promote an unaudited arithmetic
estimate to a verified conclusion. Source access is not blocked.

The [new audit assessment](2026-10-30-family003-uniform-margin-critical-audit.md)
binds the precise continuation and awaits separate next-turn approval.
No mathematics was executed here. Full matching Mathlib coverage is unchecked;
L531's Fourier support does not cover this arithmetic selection. No Lean build,
formal import closure, first-stage proof, transfer, new half-plane claim,
initial Xi signs or RH resolution has been verified.
