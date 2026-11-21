# Complete correction: completed signed-enclosure source comparison — step438

TARGET: Assess primary-source coverage for a phase-preserving certified enclosure of C999i's complete correction Q on [1,3/2] x [40,45], using its explicit continued zeta product, and nominate one bounded test of a uniform strict sign versus certified opposite signs without assuming an event or residual sign.
CHECKED: 2026-11-11
DECISION: IMPORT
SEARCH_EVIDENCE: Step438 searched rigorous Hurwitz-zeta/Euler–Maclaurin/Arb/complex-ball terminology and Lagarias–Rains sign/interval terms; read the primary theorem and contracts below. Narrow local checks covered C999g/h/i, reviews435/436, stops427/429/430/436 and the nearby Radau-enclosure assessment411. No existing complete-Q sign certificate was identified; unsuccessful searches imply no novelty.
SOURCE_EVIDENCE: Johansson arXiv:1309.2877v1 (11 September2013), Section2/(5)–(14), Theorem1 and entire proof, printed pp2–4, Section3.1 p5, https://arxiv.org/pdf/1309.2877v1 ; Arb2.23.0 using.html Ball semantics, acb.html complex rectangles/powers/gamma/zeta, acb_hypgeom.html Gamma function, acb_dirichlet.html Riemann zeta function, https://arblib.org/ ; python-flint0.9.0 acb documentation. Reused Lagarias–Rains math/0104176v5 Theorem5.1/(5.1), p24, proof pp26–27, https://arxiv.org/pdf/math/0104176v5 . Exact links and qualifications below.
COMPARISON: Known continuation/error bounds and the complex-ball inclusion contract cover rigorous point and rectangle evaluation of the existing explicit product. They do not give its sign, guarantee a successful interval width, audit C999i independently, or pay the combined residual. C999g's unsigned allowance is a different failed observable/comparison.
GAP: A bounded implementation and certificate are still absent; no Q value, strict sign, opposite-sign witness or eventwise bound was computed. Runtime backend availability is unverified; the default python3 lacks python-flint. Full independent audit of C999i remains pending.
REASON: Essential enclosure-source coverage is now supplied. A finite known-method specialization is justified without a new sign theorem or a new central mechanism; its exact research nomination is in review438 and requires separate supervisor approval. Far-jump and curvature estimates remain independent.
LITERATURE_REASON: Changed target from exact Mellin matching to a signed enclosure; the essential unread coverage concerns rigorous complex zeta continuation and interval/rectangle error control, including retained phases.
SCOPE: Completed literature-only comparison for the original rectangle and complete product. No calculation, lemma, mathematical script, event search, jump-split estimate or rectangle change was performed. The bounded continuation is separately specified in review438.

## Original nomination retained

Essential local inputs are C999i, C999h definition(1) and its residual(3),
and C999g's normalization. C999f is not a premise. Inherited L018/L019
remain normalization inputs through those results; no cross-notebook
input is proposed. Before using the new formula as load-bearing
evidence, check C999i's factors, half-line split and transform domain
against the stated primary source; this is not an audit of its sign.

The main goal remains actual-Xi positivity, with L966/L968 forcing,
L984(H) and the capped C997s bridge separate. The intermediate target
is one signed explicit component, not positivity of a criterion or
of the full nonlocal residual. No point is assumed to be a collision.

Check the exact continued-zeta evaluation hypotheses and error bounds
in primary sources before selecting any backend. Reuse the inspected
Theorem5.1 without reproving it or treating its Dirichlet series as
convergent here. Check the named C999g comparison, review435 and
stop436 for duplication and the loss caused by separate absolute
estimates. Preserve the full complex product and rational compensation.
An unsigned modulus bound alone is insufficient.

The proposed discriminating test is a strictly positive or strictly
negative enclosure of Q over the whole stated rectangle, or two
rigorous opposite-sign witnesses in it. The latter stops only the
uniform-sign route; a non-strict or inconclusive enclosure establishes
neither alternative. This assessment does not carry out that test.
Require explicit certified error bounds before approving a calculation.

No justified creative central-gap mechanism is ready merely from this
identity. Even a uniform Q sign leaves the signed far-jump contribution
and the eventwise curvature comparison unpaid. Event existence,
nondegeneracy, multiplicities, initialization, other heights and global
transport remain open. Full matching Mathlib coverage is unknown.

## Completed source review — step438

The original nomination above is historical scope; the completed fields
and this section supply the present source decision. No mathematical
attempt has been made. A separate bounded nomination is in
[review438](2026-11-11-complete-correction-ball-test-review-438.md).

Johansson, *Rigorous high-precision computation of the Hurwitz zeta
function and its derivatives*, [arXiv:1309.2877v1](https://arxiv.org/pdf/1309.2877v1),
11 September2013; published in *Numerical Algorithms*69 (2015),253–270,
[DOI](https://doi.org/10.1007/s11075-014-9893-1): read Section2,
equations(5)–(14), Theorem1 and its whole proof, printed pp2–4,
and Section3.1, p5. The theorem assumes s=sigma+i*tau,
a=alpha+i*beta, positive integers N,M, alpha+N>1 and sigma+2M>1.
It bounds the Euler–Maclaurin remainder coefficientwise by (12),
using J_k, C and K from (13)–(14). Its proof controls periodic
Bernoulli polynomials, the logarithm and argument of a+t, and the
remaining integral. Section3.1 requires the hypotheses at every
point of each input ball and adds remainder bounds to output radii;
otherwise the error is infinite. For Riemann zeta, a=1. This is a
continuation algorithm, not a convergent Dirichlet series in our strip.
No new specialization bound is derived here.

Use the immutable [Arb2.23.0 inclusion contract](https://arblib.org/using.html#ball-semantics),
not just current generated documentation. It encloses all exact outputs
for all inputs in the balls, including rounding. The same page's
Overestimation discussion explains why greater precision need not fix
dependency loss. [acb.h](https://arblib.org/acb.html) defines independent
real/imaginary radii, and its Powers section uses exp(y*log(x)); positive
real bases 2 and pi have no branch ambiguity. Its gamma and zeta
sections identify the corresponding library calls. Retaining complex
balls through multiplication keeps phase; modulus-only bounds do not.
This is a numerical library contract, not formal verification of its code.

[acb_dirichlet.h, Riemann zeta function](https://arblib.org/acb_dirichlet.html#riemann-zeta-function)
contracts acb_dirichlet_zeta to compute the continued zeta value by an
automatic algorithm. Its unsigned bound routine is a different API and
cannot certify the requested signed observable. The current
[FLINT3.7.0-dev zeta page](https://flintlib.org/doc/acb_dirichlet/acb_dirichlet_zeta.html),
generated6 November2026, was cross-checked: it states the pole case is
indeterminate. Its generated-text warning is why it is not the sole
source. [acb_hypgeom.h, Gamma function](https://arblib.org/acb_hypgeom.html#gamma-function)
contracts the full gamma evaluator; the truncated Stirling-sum helper
alone is not that evaluator. The Taylor routine can report failure;
the complete default evaluator includes algorithm choice. Do not use
an unbounded truncation or confuse log Gamma with log of Gamma.

[python-flint0.9.0 acb](https://python-flint.readthedocs.io/en/latest/acb.html)
identifies gamma(), zeta(), exp(), log() and the complex-ball interface;
[arb constructors](https://python-flint.readthedocs.io/en/latest/arb.html)
accept exact dyadic tuples and outward-rounded radii.
[Global context](https://python-flint.readthedocs.io/en/latest/general.html#global-context)
controls bit precision. These are wrapper contracts, not observed
runtime behavior. Default python3 has no installed python-flint;
pkg-config is unavailable and the narrowly checked usual local paths
did not establish a usable backend. No package was installed. A later
attempt must record actual wrapper/library versions, or a concrete
availability blocker; no unvalidated floating-point fallback is approved.

Source alignment: directly reread Lagarias–Rains Theorem5.1/(5.1),
printed p24, and the Mellin/continuation proof pp26–27; reuse review436
for the rest. The source has -s^2/8 and completed-zeta arguments s/2
and -s/2, as transcribed in C999i. Its Mellin domain is Re(s)>0,
and the intermediate series requires Re(s)>2. The local half-line
split retains 1/s^2 in C999i(4); the full product is to be evaluated,
without adding the rational correction a second time. This alignment
check is not a separate full critical audit of C999i's proof.

Applicability obligations for the proposed test: with s=w/2+i*t,
the zeta input rectangles are [1/4,3/8]+i[20,45/2] and their negatives;
the gamma inputs are their halves. Thus they avoid the zeta pole,
the completed-zeta poles and the nonpositive-integer gamma poles.
Require outward input containment, finite outputs, and strict sign
predicates at runtime. Zeta zeros are permissible because no division
by zeta is proposed. Source hypotheses must cover the entire input
rectangles, not only midpoints. No derivative interpolation is needed
if a finite cover is evaluated by the inclusion contract.

The narrow duplicate/failure comparison found no ready Q certificate.
Stops427/429 concern unsigned G_w comparisons; stop430 lacks a positive
mixed-product weight; stop436 lacks an eventwise curvature and combined
far-jump/pole budget. This proposed observable neither repeats those
comparisons nor repairs their missing conclusions. Assessment411's
rigorous integration contract does not supply a complete-Q sign.
Broad search hits outside primary sources were not used as theorems.
No absence/novelty claim follows from these searches.

Decision: source coverage supports the separately nominated finite
ball calculation, subject to backend availability and the pending
identity audit. No source predicts which sign test will succeed.
Even a successful uniform sign cannot determine G_w*G_tt: the signed
far-jump term and event curvature remain unpaid. Mathlib matching
remains unknown; no formal or RH success is asserted. No justified
creative target is available from these numerical contracts alone.
