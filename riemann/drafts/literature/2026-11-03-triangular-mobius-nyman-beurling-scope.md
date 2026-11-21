# Triangular Mobius approximation — completed source comparison, step 227

TARGET: Assess unconditional source coverage for the triangular Mobius mollifier error E_N=O(1/log N), retaining all zero residues and separating RH-dependent estimates from usable inputs.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Scoped exact-terminology search found only this nomination and its history; external searches located primary sources and later leads below. No inspected source supplies unconditional E_N=O(1/log N); no novelty or impossibility claim.
SOURCE_EVIDENCE: Baez-Duarte math/0202141v2 Thm 1.1/(2.6), pp. 1,4--5; BCF 1211.5191v1 Thm 1/Lemmas 2--3/Section 3, pp. 2,6--9; Burnol math/0103058v1 Thm 1.1 p. 2; Maier--Rassias CMB 61 (2018) Thm 1.1/Section 3, pp. 623--627; Inoue JTNB 33 (2021) Prop 1 pp. 279,291--292 and Section 6 pp. 297--299. Inspected and unread scopes below.
COMPARISON: E_N and V_N match BCF exactly, but its quantitative theorem assumes RH and a negative moment entailing simplicity. The infimum criterion does not prove convergence of prescribed coefficients. Later claims retain RH, change coefficients or assume finitely many off-line zeros; none pays this unconditional estimate.
GAP: Unconditional full-line cancellation of the joint logarithmic-derivative, all-zero-residue and trivial-zero terms remains missing, including multiple zeros and tails. Inoue supplies an unconditional contour tool, not a norm bound; BCF's limiting convention needs an explicit audit.
REASON: Park direct implementation of the conditional asymptotic. A separately assessed compact-contour audit is independently testable with published tools. No covered noncircular creative norm mechanism emerged; no new result or mathematical script was derived.
SCOPE: Source comparison for the stated E_N only; no unconditional upper bound approved. The separate continuation covers compact-contour ordering, excluding any full-line norm interchange.

## Completed source comparison

The original nomination below is retained as history of the question.
No source acceptance label is used as a mathematical hypothesis.

### Criterion and admissibility

[Baez-Duarte, math/0202141v2](https://arxiv.org/pdf/math/0202141v2),
Theorem 1.1, p. 1, identifies RH with closure of integer fractional-part
dilations in L2(0,infinity). Equation (2.6) and its adjacent Mellin
identity, p. 4, identify the full-line norm. Finite coefficients a_n
correspond to chi+sum a_n rho_n, rho_n(x)={1/(nx)}, with transform
(1-zeta(s)sum a_n n^(-s))/s. Thus V_N is admissible and E_N finite.
The criterion concerns the infimum d_N^2 over all coefficients:
d_N^2<=E_N, so the proposed decay would imply RH. It establishes
neither that bound nor its converse for this prescribed family.
The norm-convergence cases on pp. 4--5 were inspected; their
RH-to-closure direction assumes RH. The alternate math/0205003v1
Theorem 1.1/proof scope was also read, not used unconditionally.

### Exact overlap and retained residues

[Bettin--Conrey--Farmer, arXiv:1211.5191v1](https://arxiv.org/pdf/1211.5191v1),
Theorem 1, p. 2, gives this E_N asymptotic to
(2+EulerGamma-log(4pi))/log N under RH and
sum_(|Im rho|<=T)|zeta'(rho)|^(-2)<<T^(3/2-delta), delta>0.
The source explicitly says this entails simplicity. Lemma 2, p. 6,
states unconditionally, for 0<Re(s)<1,

    V_N=1/zeta-zeta'/(log(N)*zeta^2)+(sum_rho R_N+F_s(1/N))/log N,
    R_N(rho,s)=Res_(z=rho) N^(z-s)/(zeta(z)*(z-s)^2),
    F_s(1/N)=pi*N^(-s)*sum_(k>=1)
      (-1)^k*(2pi)^(2k+1)*N^(-2k)/((2k)!*zeta(2k+1)*(2k+s)^2).

Retain every distinct nontrivial zero via the residue operator,
including multiple/off-line zeros. Lemma 3/(4)--(5), pp. 6--7,
uses RH and the moment bound for near/far tails. Theorem 1's proof,
(6)--(7), pp. 7--9, uses Lindelof and epsilon<delta/10: its pair term
is O(log(N)^(-2)); a contour-crossing mixed term supplies the main
constant. These estimates are conditional. Lemma 2 leaves its infinite
zero-sum convention/horizontal limits unspecified. Do not infer
absolute convergence or an L2 interchange. Use positive 1/N in F_s;
do not import unqualified entire-in-z wording for z^s.

Audit annotation, step 229: the displayed F_s above preserves BCF v1's
printed formula. Its prefactor pi is inconsistent with the same page's
zeta'(-2k) formula; the correct prefactor is 1/pi. The corrected residue
normalization and complete compact ordered-limit proof are in
[L728](../../lemmas/L728-compact-triangular-mobius-contour-identity.md).
This repairs the identity, not the conditional norm asymptotic.

### Lower bounds and a hypothetical quartet

[Burnol, math/0103058v1](https://arxiv.org/pdf/math/0103058v1),
Theorem 1.1, printed p. 2, is the multiplicity-squared continuous
approximation lower bound. BCF records its discrete form
liminf log(N)d_N^2>=sum_(Re rho=1/2)m(rho)^2/|rho|^2.
This pays no upper bound; neither simplicity nor equality is imported.

[Maier--Rassias, CMB 61 (2018), 622--627](https://doi.org/10.4153/CMB-2017-070-3),
Theorem 1.1, pp. 623--624, assumes exactly the off-line quartet
sigma0+-i gamma0,1-sigma0+-i gamma0 and the same negative moment.
Its stated E_N is N^(2sigma0-1)/log(N)^2 times a real trigonometric
polynomial in 2gamma0 log N, with relative error
O_epsilon(N^(1/2-sigma0+epsilon)). No actual zero is certified.
Section 3's cases, pp. 625--627, were inspected. Definition 2.6
displays only the right pair in the off-line sum; its Sigma
normalizations also need checking against (3.1). No exact implementation,
nonzero leading coefficient or positivity claim is imported pending
audit. The theorem's hypotheses cannot justify dropping off-line zeros.

### Available unconditional contour input

[Inoue, *Some explicit formulas for partial sums of Mobius functions*,
JTNB 33 (2021), 273--315](https://www.numdam.org/item/10.5802/jtnb.1162.pdf),
Proposition 1, p. 279: alpha>=13, T>=T0(alpha),
1<=Q<=(log T)^(alpha/4) permit t in [T,2T] with

    max_(1/2<=sigma<=2, chi primitive of modulus <=Q)
       |L(sigma+i*t,chi)|^(-1)<=exp(C*alpha*(log log(Q*T))^2).

Q=1 includes zeta. Neither RH nor simplicity is assumed.
The proof's two sigma cases, pp. 291--292, and Section 6's
horizontal/left-edge cases, pp. 297--299, were inspected. This can
replace derivative assumptions for contour-height selection. The
shifted squared Perron kernel, compact uniformity and order of limits
still need a local applicability argument, nominated separately.
No unconditional full-line norm bound is supplied by this theorem.

### Later leads: scope and access

[bramble_trace, paper 48/v2, 24 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/48),
Theorem 1/(5)--(6), claims the optimal infimum constant under RH
without simplicity or derivative moments, with changed zero-dependent
coefficients. Section 9 assumes finitely many off-line zeros.
Statement and Section 1.1 were read; proof unaudited and unimported.
This is not an unconditional theorem for the prescribed V_N.

[span_of_dilates, paper 4/v1, 16 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/4),
Theorem G, retains finitely many off-line zeros, simple line zeros
and the negative moment, and changes coefficients/target. Lemmas 3--4
were inspected for contour hypotheses; their good heights use the
finite-off-line assumption. Source proofs remain unaudited.

[Veltri, Zenodo 22647730/v1, 7 September 2026](https://zenodo.org/records/22647730)
advertises a weaker moment hypothesis while retaining RH. Record read;
primary PDF/TeX retrieval failed, including direct-download DNS failure
and the content endpoint. Exact theorem/proof unread: no refinement
imported, no repeated access task selected. It is unnecessary for the
independent compact-contour test. Other search snippets are leads only.

### Decision and limitations

Informative negative for directly implementing the conditional
asymptotic, not a disproof of the bound or RH. The unpaid full residual
requires unconditional cancellation; a finite window, isolated residue
estimate or optimized infimum does not certify E_N. No new half-plane
or reciprocal-series continuation is claimed; GOAL.md's separate
baseline remains mandatory before such work. L018 fixes actual zeta;
L727/L471/L399 remain contrasts. No cross-notebook input.

The separate compact-contour assessment is
`drafts/literature/2026-11-03-triangular-mobius-compact-contour-audit.md`.
Pass: a complete finite-contour identity and justified compact limit
without extra zero assumptions. Fail: name the unpaid edge or limit
and park that identity. Even a pass leaves the full-line norm open.
A creative norm attempt remains blocked by the lack of a covered,
noncircular cancellation mechanism, not by the inaccessible refinement.
Mathlib matching coverage not checked; no absence claim. No lemma,
mathematical script, DAG or main argument changed.

## Original nomination (retained)

## Exact question and possible use

Let mu be the Mobius function. For integer N>=2 propose

    V_N(s)=sum_(1<=n<=N) mu(n)*(1-log(n)/log(N))*n^(-s),
    E_N=(1/(2*pi))*integral_(-infinity)^infinity
          |1-zeta(1/2+i*t)*V_N(1/2+i*t)|^2/(1/4+t^2) dt.

Compare with E_N<=C/log N for some absolute C and all sufficiently
large N. This is a proposed threshold only: no bound or interchange
has been derived. First verify the exact function space and criterion
relating this approximation to RH, including admissibility of this
polynomial family. This is a potentially full-strength RH route, not
an elementary lemma assumed to hold. Import the criterion precisely
and keep its approximation estimate open. A theorem assuming RH
cannot pay that estimate unconditionally.

The intermediate output is a source-level identification of the actual
unproved residue/remainder estimate for this explicit family. Its
downstream use could be one bounded arithmetic test addressing another
form of the central gap. No such test is approved today. If this
family is already obstructed under the proposed assumptions, retain
that evidence rather than reprove its known limitation.

Retrieve primary hypotheses and essential proof cases first: the exact
Nyman-Beurling/Baez-Duarte criterion, the named Bettin-Conrey-Farmer
triangular-polynomial lead, stronger results and known obstructions.
Check versions, theorem numbers, multiplicities, convergence of the
full real-line integral, contour shifts, all off-line residues and
assumptions on zeta'(rho) or inverse-derivative moments. A finite
ordinate cutoff or height-window mollified mean does not certify E_N.
These are next-review obligations, not claims of inspected sources.

Before any reciprocal-series continuation or zero-free estimate, obey
GOAL.md's baseline and narrowly read its specified overlap assessment
and external-input register. No new half-plane claim is made here.
No API key, cross-notebook result or source-status label is an input.

## Three mechanisms and decision

1. **Another local-product tail improvement:** do not select. L727's
   audit certifies 14/log T, Q''<=0 and zero-safe transfer, but leaves
   its signed margin (5) unpaid. The completed source comparison found
   no such margin in the product or hybrid-factorization inputs. The
   stop is recorded in `ATTEMPTS/2026-11-03-l727-tail-only-signing-stop.md`.
   A changed cutoff or Taylor subtraction alone is no new signed input.

2. **Ordinary moments for pair-divided negative mass:** do not select.
   Reuse L471 and `ATTEMPTS/2026-10-27-displacement-weighted-negative-mass-test.md`:
   the ordinary fourth-moment substitution loses the positive displacement
   power and yields d^(-3/2). No new pair-divided estimate is supplied.
   `ATTEMPTS/2026-11-03-fixed-profile-xi-realization-source-stop.md`
   also preserves the separate missing pole-matching input; do not retry it.

3. **Full-line triangular Mobius approximation:** select source review.
   This changes the observable and arithmetic coefficients: approximate
   1 by zeta times a specified Dirichlet polynomial rather than sign a
   local zero block or realize a synthetic profile. L399 treats a
   quadratic taper of length H^(1/100) and a signed discriminant averaged
   on [H,2H]; its negative mean is not an obstruction theorem for E_N.
   The local Beurling hits concerned Beurling-Deny, Beurling-Selberg and
   Beurling-Sobolev objects. No exact saved match was found; this proves
   neither novelty nor viability.

## Continuation and abandonment test

Nominate mathematics only if primary statements and essential proof
cases identify a noncircular, independently testable arithmetic difference
with an explicit quantitative threshold. Import an already known result
with only its needed applicability check. If the desired decay uses RH,
assumed simple zeros, an unproved inverse-derivative moment or dropped
off-line residues, name that assumption and park the direct implementation.
Do not turn a conditional asymptotic into an unconditional theorem.
Persistent essential source inaccessibility calls for independent work,
not repeated retrievals. A review need not produce a new lemma.

L018 fixes actual zeta/Xi. L727 is the completed route's interface;
L471/L399 are contrasts only. None establishes this norm estimate.
The approximation criterion and quantitative tools remain unimported.
Full matching Mathlib coverage is unchecked. No lemma, calculation
or mathematical script for the new target was written.

Creative work remains a priority, but essential coverage is missing.
A creative invocation would need a specific new arithmetic mechanism
beyond restating the criterion, a bounded test and separate approval.
