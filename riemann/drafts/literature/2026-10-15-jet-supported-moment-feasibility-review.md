# Jet-supported moment feasibility: completed source comparison

TARGET: Assess source coverage for a jet-supported moment feasibility test combining L401's full response-linear matrix with L410's five benchmarks on {Delta<=0 or Bcal>=0}.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 138 reused the October-12 matrix and October-14 atomic/duality assessments, searched the exact response-linear statistic, joint Hardy derivative moments and noncompact truncated moment feasibility, and compared the scoped October-12/14/15 failures; no inspected theorem decides this combined feasibility problem and no novelty is inferred.
SOURCE_EVIDENCE: Freshly inspected Bayer--Teichmann arXiv:math/0502473v2 Theorem 1, Corollaries 1--2, Remarks 1--2 and their proof cases, manuscript pp. 2--4; Bertsimas--Popescu final SIAM J. Optim. 15 (2005), Section 2/Theorems 2.1--2.2, pp. 784--785; reused the primary Hughes--Young/Bui--Hall/carrier and Curran--Heycock coverage identified below, within unchanged fixed-order scopes.
COMPARISON: Conditional measurable-map atomic replacement covers the enlarged finite coordinate list and preserves its support, but proves neither feasibility nor a separator. L401 fixes all 21 entries only to leading quartic scale; this does not license replacing exact Delta/Bcal by leading models in lower-scale constraints or at sign boundaries. A selected local-jet relaxation is specified below without asserting actual-function realization.
GAP: Test one simultaneous height-dependent law in the stated local-jet relaxation against all 21 entries, the five scalar benchmarks and the two jet envelopes; feasibility or a robust separating inequality remains unproved. Full actual joint distribution, clipped mean and regulator margin remain outside this test.
REASON: Essential coverage now suffices for one bounded mathematical attempt using imported atomic replacement and existing local identities; no new lemma, calculation or feasibility claim is made in this literature-only step.
LITERATURE_REASON: The added compatible-jet support and complete matrix were outside L410's assessed scalar scope; this turn checks the enlarged measurable map, normalization and duality qualifications rather than repeating ready zeta-moment research.
SCOPE: The explicitly selected local-jet relaxation below, with constants fixed before all real H tending to infinity; no independent-phase averaging, actual-phase visits, single global function, uniform height marginal, exact SDP duality or regulator conclusion.
COVERED_TARGET: Test simultaneous feasibility of L401's 21 matrix entries and L410's five benchmarks in the reviewed local-jet relaxation supported on {Delta<=0 or Bcal>=0}.

## Startup proposal retained

The following proposal was supplied at the start of step 138. Its pending
coverage language records that earlier state; the completed comparison
and precise scope below supersede that language only. Its mathematical
limitations and stopping evidence remain in force.

## Relevance and choice of mechanism

The main gap remains global actual-theta mixed positivity. The proposed
intermediate target tests whether the complete matrix contains
sign-sensitive information lost by the five scalar benchmarks. Its
downstream use is to decide whether existing information can support a
joint-sign argument or whether additional actual-family data are needed.
It cannot infer a regulator margin from joint signs: audited L413 rules
out that shortcut.

Three routes were compared. Repeating the sign-only shrinking-window
implication is exhausted by L413. Frozen scalar half-carrier-turn pairing
is stopped by audited L412. The selected alternative is feasibility of
a law on compatible jet and response variables with the full L401 matrix,
rather than five freely assigned scalar moments. L410's obstruction
remains intact; it neither realizes nor tests these added constraints.
This is a proposed discriminating change of information, not a successful
repair or a completed duplication search.

## Scope to resolve in the next source review

Essential input IDs are L367, L370, L390, L401 and L410. Use L410 to
locate the five constants and canonical moment inputs L388, L393, L405,
L406 and L409 only as needed. L401's X uses derivatives of F/A, whereas
L367's P_j are normalized ordinary F jets. Their conversion, the response
carrier variables and same-height normalization cannot be silently
identified. Require one probability law for each height parameter, fixed
growth/error constants and all 21 symmetric matrix entries at their
stated leading scale. Actual-phase realization is not assumed for an
abstract feasibility test. No lower-order term may be discarded without
its source estimate. Whether this formulation is adequate is unresolved.

Reuse primary assessments behind L401 and L410 after checking scope.
L401 cites Hughes--Young, arXiv:0709.2345v2, Theorem 1.1, (12)--(17),
and the ordinary-jet/carrier sources in its proof. L410 cites
Bayer--Teichmann, arXiv:math/0502473v2, Corollary 2, pp. 3--4.
These are leads for the changed target, not freshly inspected primary
theorems here. Atomic replacement is conditional on an existing
integrable law; it proves neither feasibility nor strong duality on an
unbounded support. Matching Mathlib coverage has not been checked.

Continue to a separately approved mathematical test only if a precise,
source-supported formulation permits either an explicit compatible law
on the stated support or a rigorous separating inequality. Abandon this
formulation if unavailable higher moments, actual joint distribution
laws or uncontrolled errors are needed merely to state the constraints;
record the exact missing input rather than repeating retrieval. No law,
separation result or actual joint sign is asserted here. Actual clipping,
regulator-scale occurrence and the full-error margin, common-zero upper
counts and global positivity remain unresolved.

## Completed comparison — 2026-10-15, step 138

This is a LITERATURE / NOVELTY_UNCHECKED / literature_comparison step.
The advance is usable source coverage and a specified bounded test,
not a law, separation theorem, new zeta moment or mathematical derivation.
No lemmas or mathematical scripts were modified or run. The newly
specified continuation is for a later invocation; supervisor approval
and routing remain separate from this completed source review.

### Primary inputs and the exact limits of their use

Christian Bayer and Josef Teichmann, *The proof of Tchakaloff's Theorem*,
Proc. Amer. Math. Soc. 134 (2006), 3035--3040,
DOI [10.1090/S0002-9939-06-08249-9](https://doi.org/10.1090/S0002-9939-06-08249-9),
[arXiv:math/0502473v2](https://arxiv.org/pdf/math/0502473v2), 4 May 2005,
Corollary 2, pp. 3--4: for a positive measure concentrated on a measurable
set, an N-coordinate measurable map with integrable norm has its integrals
preserved by at most N positive atoms in that set. Include a constant
coordinate to preserve finite total mass. Theorem 1's proof handles a
full-dimensional cone by supporting hyperplanes and reduces the other
case to its supporting subspace; Corollary 2 pushes forward and lifts
the atoms. These cases were read directly. Import this theorem by
citation; no reproof is needed. It presupposes an existing measure,
supplies no uniform atom positions, and does not decide our constraints.

Dimitris Bertsimas and Ioana Popescu, *Optimal Inequalities in Probability
Theory: A Convex Optimization Approach*, SIAM J. Optim. 15 (2005),
780--804, DOI [10.1137/S1052623401399903](https://doi.org/10.1137/S1052623401399903),
[final author PDF](https://web.mit.edu/dbertsim/www/papers/MomentProblems/Optimal-inequalities-in-probability-theory-A-convex-optimization-approach-SIAM15.pdf),
Section 2, pp. 784--785, Theorems 2.1--2.2: a pointwise majorant gives
weak duality by integration; strong duality requires an interior feasible
moment vector. Attainment is explicitly not automatic. The pointwise
inequality and its integration proof were read directly. The earlier
compact semialgebraic/SOS comparison in the October-14 assessment is
reused; it does not supply an exact solver here. Our response coefficients
depend on height and our moment data have asymptotic tolerances. No
interiority, uniform compactness, strong duality, optimizer or complete
SOS characterization is imported. A separator must be checked directly.

Reuse the ready primary coverage in
[the matrix assessment](2026-10-12-response-linear-weight-family.md),
[its source-scope audit](2026-10-12-response-linear-family-critical-audit.md),
[the scalar assessment](2026-10-14-cubic-benchmark-moment-obstruction.md)
and [the cubic transfer assessment](2026-10-13-cubic-physical-replacement.md).
These are reused readings, not fresh external retrievals this turn:

- Hughes--Young, J. reine angew. Math. 641 (2010), 203--236,
  [arXiv:0709.2345v2](https://arxiv.org/pdf/0709.2345v2), Theorem 1.1,
  (12)--(17), pp. 4--5, holomorphy remark and (46)--(58). Its four
  shifts are O(1/log H), coprime twists satisfy hk<=H^(2/11-epsilon),
  and smooth weights have the stated derivative scale
  H^(1/2+epsilon)<<T_0<<H. Fixed heads and widths precede height
  limits. L401's audited complete matrix already makes this application;
  no growing head, growing derivative order or extra critical factors
  are proposed here.
- Bui--Hall, [arXiv:2304.05178v1](https://arxiv.org/html/2304.05178v1),
  Theorem 3/defining asymptotic, Proposition 3 and Sections 5/7,
  supplies fixed-order quartic jet coverage. L390/L401 retain its sharp
  envelope and ordinary phase conversion. The modified-Gonek and
  Bourgain inputs in the matrix assessment control its signed carriers;
  this review neither changes their rectangle nor recomputes a carrier.
- Curran--Heycock,
  [arXiv:2403.00902v1](https://arxiv.org/html/2403.00902v1), Theorem 1.1/(2)
  and Section 4, covers fixed order two and absolute power three with
  k=3/2, sum h_j<=k. L406 already transfers this to the ordinary Hardy
  jets. No new moment, conjectural random-matrix law or sixth-moment
  asymptotic is needed to state the test.

L401 (1)--(5), its full matrix and audited endpoint/full-tail passage;
L410's five constraints and constants; L367 (1)--(3), (9), (15);
L370 (3)--(8); L390 (4)--(5); L405 (2)--(7); L406 (1), (6)--(7);
and L368 (1)--(4) were inspected for the local normalization/support
comparison. No canonical proof or coefficient was re-audited this turn.

### Selected local-jet relaxation for the later test

This specifies constraints to be tested, rather than proving their
simultaneous feasibility. It retains necessary local information and
does not claim to capture all properties of the actual functions.
For each real H sufficiently large let ell=log H. One law is to govern
states (t,x,y,z,v_0,v_1,v_2,a,h), with H<=t<=2H. Use the actual known
envelope A(t), alpha_A=A'/A, q=(log A)'', T=1+t and L=log(2+t).
The letters a,h here are the response coordinates of L401; write
a_* for the positive first-moment constant called a in L410.

Copy L370's product-rule conversion, without identifying the two jet
conventions:

    P_0=x,
    P_1=y+(alpha_A/L)x,
    P_2=z+2(alpha_A/L)y+((q+alpha_A^2)/L^2)x,
    V_0=v_0,
    V_1=v_1+(alpha_A/L)v_0,
    V_2=v_2+2(alpha_A/L)v_1+((q+alpha_A^2)/L^2)v_0.

Here X=(x,y,z) means (f,f'/L,f''/L^2); v_j means
(G/A)^(j)/(T^2 L^j); P,V mean the normalized ordinary jets in L367.
These equations are the existing product formulas with pointwise divisors,
not differentiation of P,V,T or L. They express compatibility at one
height and do not impose a single global pair of functions.

Use the exact physical polynomials from L367/L370/L405:

    ell_F=P_1^2-P_0 P_2, Ccal=V_1^2-V_0 V_2,
    Bcal=2P_1 V_1-P_0 V_2-P_2 V_0,
    Delta=Bcal^2-4 ell_F Ccal,
    omega=(ax,ay,az,hx,hy,hz), U=x^2+y^2+z^2.

The selected support requires Delta<=0 or Bcal>=0, with both axes
included. Also retain these already established necessary bound forms:

    |P_j|<=E_j T^(1/2)L^(-j), |V_j|<=D_j, j=0,1,2;
    Ccal>=1/(128 pi^2 zeta(5/2)^2);
    zeta(5/2)^(-2)<=a^2+h^2<=zeta(5/2)^2;
    |v_0-ca|, |v_1+ch/2|, |v_2+ca/4|<=K/L, c=1/(4pi).

E_j,D_j,K are fixed positive finite constants, selected before H;
one may enlarge bounds by fixed factors, with that choice recorded.
Their actual numerical values are not known. A model exploiting generous
values refutes only an inference from these qualitative bound forms,
not a theorem assuming smaller specified constants. The Ccal bound is
L368's eventual bound; the annulus is its absolute Euler-product bound;
the response errors are L390 (4), including the full derivative tails.
Curvature is retained through the conversion and exact polynomials.
Do not replace these errors by zero or turn the carrier coordinates
into independent random variables. Their joint law is to be chosen,
without assuming independence or any phase visit theorem.

Impose all the following on this same law, not on separate projections:

    E Delta=-a_* ell+o(ell),
    E Delta^2=b_* ell^4+o(ell^4),
    E(Delta Bcal)=beta_* ell^2+o(ell^2),
    E(Delta Bcal^2)=kappa_* ell^4+o(ell^4),
    E |Bcal|^3=O(ell^(9/4)),
    E[Delta omega_i omega_j]
       =(c^2 Psi/zeta(2)) C_ij ell^4+o(ell^4), 1<=i<=j<=6,
    E U^2=O(ell^4), E U^(3/2)=O(ell^(9/4)).

C is exactly the full rational matrix in L401 (2), in its stated order;
Psi and a_*,b_*,beta_*,kappa_* are exactly L410 (2), with stars only
to avoid coordinate-name collisions. No rounding or sign-only matching
is allowed. The 21 entry conditions are the finite symmetric-matrix
form of L401 (1) with fixed basis vectors; no H-dependent optimizing
vector or new uniform-in-vector theorem is assumed. Every little-o
remainder has its stated scale as H tends through all real values,
and all O constants and an eventual onset are independent of H.
The future attempt must exhibit/check these quantifiers, not merely fit
a moment vector at one H. All listed expectations must be absolutely
integrable. U envelopes are L390/L401 and L406's existing bounds.

In particular a leading-response substitution incurs errors of different
scales: L401 (5) permits quartic O(ell^3), whereas L406's absolute cubic
replacement costs O(ell^(5/4)). Neither is an o(ell) error for the first
Delta mean. The later test must use exact Delta/Bcal for that constraint
and for the support, including near either axis. This review makes no
new transfer estimate and no claim that a limiting homogeneous model
lifts to the physical normalization.

For conditional atomic replacement the measurable coordinate list is

    (1,Delta,Delta^2,Delta Bcal,Delta Bcal^2,|Bcal|^3,
     (Delta omega_i omega_j)_(i<=j),U^2,U^(3/2)).

There are 29 coordinates. Bayer--Teichmann Corollary 2 applies at each
H to an existing integrable law on the stated Borel support, retaining
the actual finite envelope integrals as well as all signed moments.
Thus the later test may seek at most 29 atoms; this is a citation-based
conditional reduction, not an existence proof or a claimed minimal count.
It does not preserve a continuum of additional constraints. In particular
no uniform t marginal, actual Euler-series relation between different
heights, exact shifted-divided response realization, or actual critical
jet law is imposed. The test uses the displayed necessary relationships
only. L369's separate first Bcal mean is also not among these selected
five benchmarks; feasibility would not settle an enlarged test adding it.

### Search, decision and continuation threshold

Fresh locator queries included `"Bayer" "Teichmann" "Corollary 2"
Tchakaloff`, `"truncated moment problem" "unbounded" "support" Richter
feasibility`, `"response-linear" "discriminant" "moment" zeta`,
`"Hardy" "joint moments" derivatives fourth moment sign`, and
`Bertsimas Popescu optimal inequalities probability theory Theorem 2.2
strong duality moment pdf`. Exact-statistic searches produced no
inspected matching feasibility theorem. Richter/core-variety and
variational moment results were locator leads only, not read as theorem
inputs. Random-matrix joint-moment and conjectural Hardy-law results
are not unconditional sources for this support constraint. No novelty
claim follows. The ready scalar assessment already inspects the Richter
variant and compact optimization limitations; no repeated broad search
or inaccessible-source campaign is needed.

Scoped local searches and the cited assessment/attempt passages show
that L410 omits these jet/matrix conditions, L413 omits averaged moments,
and L412 stops one scalar pairing. None is a duplicate solution of this
combined test, and their stop evidence remains unchanged. There is no
new reason to reopen the unchanged clipped-asymptotic source search.

Continue with exactly COVERED_TARGET in one bounded mathematical attempt:
either certify an explicit law family meeting every condition with fixed
constants, or certify a pointwise separating inequality with a quantitative
gap surviving all allowed asymptotic errors. Do not reprove the atomic
theorem. A failed atom ansatz or numerical infeasibility report establishes
neither alternative. If merely stating or checking a proposed construction
requires an unproved actual joint law, phase return, unavailable higher
moment or uncontrolled lower-order replacement, retain that failure and
park that implementation. Do not weaken the constraints silently.

A feasible family would stop only this selected-information joint-sign
inference. An impossibility result could motivate a joint-sign theorem
only after checking that the actual-family constraints and all errors
fit the separating inequality. Either outcome would leave the actual
negative-Bcal clipped mean, L413's regulator-scale/full-error obligation,
common-zero upper counts and global mixed positivity unresolved. RH stays
IN_PROGRESS. Full matching Mathlib coverage remains not checked; neither
library absence nor formal verification is claimed. PROOF.md and DAG.md
need no edit because the mathematical argument has not changed.
