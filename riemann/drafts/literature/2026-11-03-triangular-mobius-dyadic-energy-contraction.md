# Dyadic triangular Mobius contraction: completed source comparison, step 231

TARGET: Assess source coverage for an unconditional dyadic contraction E_(2N)<=(1-c/log N)E_N+C/(log N)^2 for the prescribed triangular Mobius polynomials, with fixed c>0,C>=0 and all sufficiently large integers N.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Scoped dyadic/contraction/Vasyunin/neutral-gradient searches found no duplicate; external exact and standard-terminology searches located Bettin–Conrey, Ehm and the later anchored Selberg-gradient work. Queries and inspected scope below; no novelty claim.
SOURCE_EVIDENCE: Bettin–Conrey ANT 7 (2013), (13) and Theorem 5/proof, pp. 225,239–241; Ehm arXiv:2405.06349v2, q=1 Theorem 2.1/proof, Proposition 1.1/Section 7.1 and Sections 8.1–8.3; bramble_trace paper 18/v3, definitions, (4),(8),(32)–(42) and Limitations. Parent conditional-norm assessment reused.
COMPARISON: Exact Gram formulas are unconditional; the arithmetic moment products and Gram remainder remain unpaid. Paper 18 controls a changed anchored correction in neutral probe spaces with K^(5/2)/N error, not the prescribed full dyadic update. No inspected theorem pays the contraction.
GAP: A signed, quantitative full-update estimate with the stated c,C,N_0 remains absent; neutral projection and complementary residual control cannot be identified. This is missing coverage of a bound, not a disproof of it.
REASON: Park the proposed contraction rather than approve a square expansion as a mechanism. A separately assessed audit of the published arithmetic neutral-tail interface is independently testable and may support later preconditioning; the baseline norm remains open.
SCOPE: Completed literature comparison only. EXPLORE records no adequate match, not permission to attempt the original contraction without a new concrete estimate; no lemma, mathematical script or theorem import is made here.

## Review result and source scope

The exact target above is preserved. **No contraction is established or
falsified.** The source gate's test fails to identify a quantitative
signed estimate for the prescribed update. This is an informative
route decision, not an impossibility theorem or an RH candidate.
The nomination below remains a proposal, not a ready mathematical task.

### Search and duplicate check

Notebook searches used `dyadic`, `Vasyunin`, `Gram`, `contraction`,
`neutral gradient`, `papers/18` and `2405.06349` in the relevant
triangular-Mobius assessments, ATTEMPTS, history and foundations.
No matching neutral-gradient result or dyadic estimate was recorded.
The separately inspected
[correlated-ratio stop](../../ATTEMPTS/2026-11-01-mobius-correlated-ratio-inconclusive.md)
concerns a different height-window derivative observable; its
separate-positive-moments warning still applies. It is not a global
ban on Mobius-weighted arithmetic arguments.

External queries included “Nyman Beurling Mobius logarithmic
coefficients norm Vasyunin autocorrelation dyadic convergence”,
“Mobius mollifier dyadic Nyman”, “Selberg approximation Baez
convergence” and “Vasyunin Mobius norm”. They found exact kernels
and changed-coefficient estimates, not the stated contraction.
Unsuccessful searches do not establish novelty or nonexistence.

### Exact kernels and the unpaid arithmetic terms

[Bettin–Conrey, *Period functions and cotangent sums*, ANT 7 (2013)](https://msp.org/ant/2013/7-1/ant-v7-n1-p08-p.pdf),
formula (13), p. 225, evaluates the full weighted twisted second
moment for coprime positive h,k through finite Vasyunin sums.
Theorem 5, pp. 239–241, extends this to |Re(a)|<1; a=0 recovers
that kernel by a removable limiting value. Its proof splits the
kernel into symmetrically truncated contour integrals, then uses
the functional equation and Estermann series. This is not a theorem
on the Mobius-weighted dyadic interaction; no sign estimate for
that interaction follows just from an exact kernel. No new
specialization or conditional interchange is performed here.

[Ehm, *On certain Gram matrices and their associated series*,
arXiv:2405.06349v2, 13 May 2024](https://arxiv.org/html/2405.06349v2),
Theorem 2.1, q=1, gives the full Gram kernel for all real u,v>0.
The proof's residue shift, sum interchange and endpoint residues
were read. Proposition 1.1 and Section 7.1 cover the linear term;
Sections 8.1–8.3 retain the correlated moment products and a
series remainder. Their estimates do not pay the target.
Proposition 8.1 changes the coefficients to center moments;
it is not a result for the prescribed triangular coefficients.
The source expressly warns that convergence of centered factors
alone does not control their products. HTML equation numbers
used here refer to the HTML version; the PDF's later numbering
differs. The source's introductory RH-equivalence wording for
this prescribed family is not imported: the free-coefficient
criterion and its linear-term limit do not supply the needed
prescribed-family upper bound.

### A quantitative estimate with different scope

[bramble_trace, *Fixed and growing neutral gradients of the anchored
Selberg–Mobius approximant*, paper 18/v3, 22 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/18),
defines anchored rho_m and two neutral constraints. Its uniform
neutral theorem (32)–(35) asserts projection error O(K^(5/2)/N)
and second-order descent for a changed approximant when
K^(5/2)/N tends to zero. Definitions, complete Gram formula (4),
divisor identity (8), the proof (36)–(42), and Limitations were
read. Cancellation occurs before bounding the periodic tails;
weighted jump inversion supplies the coefficient cost.
This controls neutral observations, not the complete update
supported through 2N. The unrestricted estimate (42) retains
moment errors. Baseline and complementary norms remain
unestimated. The anchored norm is not the original E_N;
no equality or transfer between them is assumed. These claims
are source statements awaiting local audit, not accepted inputs.

### Reuse, unread leads and decision

Reuse the [parent assessment](2026-11-03-triangular-mobius-nyman-beurling-scope.md)
for BCF's RH/negative-moment restrictions, admissibility and
Burnol's lower bound. Do not retry its inaccessible refinement.
Paper 47/v1 Section 7 statements were inspected only as a
classical-oscillation lead for anchored prefix errors; its proof
is unread and no theorem is imported. Baez-Duarte math/0011254v1's
abstract concerns different natural approximants; its divergence
claims were not transferred to the triangular taper. Other search
hits and the original Vasyunin paper remain unread leads.

The useful new comparison is the precise two-constraint/probe-range
limitation of an actual signed arithmetic estimate, alongside Ehm's
unpaid products. It changes the route from seeking a full dyadic
bound to checking a noncircular arithmetic interface. There is no
source-access blocker and no justified creative norm mechanism yet.

The separate continuation assessment is
[the neutral-tail audit](2026-11-03-neutral-arithmetic-tail-audit.md).
It nominates a bounded audit of absolute regrouping and jump
inversion, with the prime-kernel functional explicit; it omits
representer identification, density, saturation and norm decay.
Newly written coverage receives separate approval next turn.
A later creative attempt needs a materially new estimate for the
complement or for the actual full update, not repeated kernel algebra.
Mathlib matching coverage was not checked; no absence claim.

## Original nomination retained

## Proposed target, not a derived or approved result

Use the actual zeta function (L018) and the triangular coefficients
defined in L728. Put

    r_N(t)=1-zeta(1/2+it)*V_N(1/2+it),
    E_N=(1/(2pi))*integral_R |r_N(t)|^2/(1/4+t^2) dt.

The question concerns fixed constants c>0, C>=0, N_0>=2 and the
displayed contraction for every integer N>=N_0. These constants
are sought, not asserted. A useful eventual bound would drive the
norm toward zero along dyadic scales; the recurrence implication
must be checked if a later mathematical target is approved. The
known approximation criterion then supplies the possible downstream
connection to RH. Finiteness of E_N is covered by the parent source
comparison; no smallness or positivity estimate is thereby imported.

The proposed mechanism is the signed Hilbert-space interaction of
r_N with zeta*(V_(2N)-V_N), using the exact arithmetic coefficients
and fractional-part Gram kernel. Merely expanding a square cannot
pay that interaction. Inspect sources on the Gram kernel, weighted
Mobius correlations and known behavior of this particular taper
before deciding whether any test of its sign is justified. These
are source leads, not inspected theorems or a novelty claim.

## Source review obligations and bounded decision

Retrieve precise primary hypotheses and the proof cases controlling
the signed mixed term and the update's squared norm. Compare any
available conclusion to the stated contraction, retaining the full
height range. An infimum over freely chosen coefficients, a finite
height average, a different taper, or an estimate assuming RH does
not establish this target. Reuse the parent's conditional-norm
limitations; do not retry the blocked refinement for this purpose.

Pass to mathematics only if the review identifies a concrete
noncircular arithmetic estimate with a quantitative threshold and
a bounded falsification or proof test. Otherwise record the precise
overlap, obstruction or missing estimate and select a different
mechanism. No ready creative attempt is claimed merely from this
proposal. If the only output is the same norm bound rewritten as
a cross term, that is not sufficient justification for approval.

Potential creative relevance: actual signed arithmetic correlations
could pay the full-line norm gap left untouched by L728. Essential
coverage is the present blocker. Any future proof_attempt/creative
nomination must name the specific mixed-term inequality and its
bounded test; none has been derived or approved this turn.

The compact proof in L728 and actual-zeta setting of L018 are the
local inputs. Full-line exchange, N-uniform control and all proposed
contraction constants remain unresolved. No cross-notebook input.
Mathlib coverage of this target has not been checked.
