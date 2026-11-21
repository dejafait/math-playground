# Theta-power collision orientation: uncovered analytic target

TARGET: Assess whether Lagarias–Rains's centered theta-power family G(w,t)=xi_Q(w,w/2+i*t) admits an independently controlled sign for G_w*G_tt at nondegenerate real double zeros with 1<=w<=3/2 and 40<=t<=45, comparing the exact parameter derivative with the recorded heat-flow and affine-pencil collision obstructions before nominating one bounded analytic test.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step426 searched exact theta-power/two-variable-zeta/parameter-derivative/collision/monotonicity terms, checked the named theta/two-variable assessments and theta failure records, and reused reviews132,421,423 and the affine-pencil audit. No inspected source signs this product; failed searches establish no novelty.
SOURCE_EVIDENCE: Lagarias–Rains math/0104176v5 https://arxiv.org/pdf/math/0104176v5 Theorem2.1/(2.6)-(2.10) printed pp8-9, unshifted Theorem4.4/Lemmas4.5-4.7/(4.5)-(4.9) pp21-24, and entire Section8 p44; published AIF53(2003),1-68 https://www.numdam.org/item/10.5802/aif.1939.pdf Sections4.2 and8 pp26-31,56-57 compared. Lessard https://www.math.mcgill.ca/jplessard/ODEs_files/saddle_node.pdf Definitions1-2/Theorem1 p2; prior proof-case coverage reused. Details below.
COMPARISON: Entire-family and compact integral estimates license differentiation, not the collision sign. Section8 depends on a numerical departure and prints reflection by1; use Theorem2.1's reflection by w. Heat-energy, event-atom and affine-pencil arguments do not transfer. A uniform sign test for the centered parameter derivative is an independent sufficient component, not a collision certificate.
GAP: Neither G_w nor G_tt has an established sign in the box; no event, nondegeneracy, connectivity or global transport is established. A proposed uniform G_w>0 test must control cancellation and all tails, independently of curvature and event equations.
REASON: Complete this source comparison without importing an unpaid orientation. Park automatic product-sign transfer; nominate one bounded analytic test of an independently specified factor. Its separate assessment requires next-turn approval before research.
SCOPE: Completed literature-only step. No root search, installation retry, new evaluator, inequality derivation, lemma or mathematical script. The rectangle is a test domain, not a theorem range. No cross-notebook input.

The central gap remains L030-L032/C032a actual-Xi positivity, with
forcing and L984(H) still unpaid. The prospective intermediate target
is a signed, actual-family collision estimate, not a theorem that simple
zeros continue locally. A mere fold identity with an unpaid sign will
not establish such an estimate. The source review must determine the
favorable orientation with the moving center retained; no sign convention
or local-to-global implication is supplied by this nomination.

Use L018/L019 for the actual w=1 normalization and theta convention.
The exact family is the external Theorem2.1/(2.9) input, with both rational
terms and the completion retained. G uses reflection by w, not by1.
The earlier ready fixed-slice assessment covers no collision sign.
The prior comparisons to inspect narrowly are
`drafts/literature/2026-11-10-theta-collision-coercivity-discovery-132.md`
and `drafts/literature/2026-11-05-polya-local-collision-mechanism-test.md`;
follow only the exact failures relevant to a proposed import. They
establish neither a universal prohibition nor permission to rename an
unpaid coercivity estimate. The generator-to-Li stop422 is preserved;
no generator positivity is offered as this sign's premise.

At a prospective event retain G=G_t=0, G_tt!=0 and G_w!=0.
Existence of any such event in the rectangle is not assumed or known.
Primary sources must support the needed parameter differentiability,
real-valued centered family and fold criterion before a mathematical
test is nominated. Compact domination must include w differentiation
and its theta logarithm. Do not substitute a partial derivative at
fixed s for differentiation along s=w/2+i*t.

Continue only if the review identifies a separately estimable signed
component and a discriminating analytic test, or an inspected theorem
already supplies the required orientation. Abandon automatic transfer
if it presumes the desired sign, all-real zeros, parameter connectivity,
or the failed numerical backend. If no independent signed mechanism
emerges, record that concrete limitation and choose another target;
do not spend a proof turn merely deriving the generic fold criterion.

No creative proof target is ready. Essential sign coverage is missing,
so source comparison takes priority; a later creative nomination would
need its own precise obstruction, new input and bounded decisive test.
Full matching Mathlib coverage remains unchecked and unknown.

## Completed source comparison — step426

The preceding nomination is retained as the question reviewed. No
signed inequality, zero or new lemma is established in this step.
The main gap remains actual-Xi all-degree positivity L030-L032/C032a;
the forcing and L984(H) gaps remain independent. A local signed
collision input could support a later continuation argument, but does
not initialize such an argument or address its other heights and seams.

### Exact source scope and the moving center

Lagarias–Rains, *On a Two-Variable Zeta Function for Number Fields*,
[arXiv:math/0104176v5, 7 July 2002](https://arxiv.org/pdf/math/0104176v5),
Theorem2.1/proof pp8-9, supplies the entire completion and reflection.
Its (2.9), with both rational terms retained, is the evaluator source:

    Z_Q(w,s)=-1/s+1/(s-w)
      +integral_0^1 (theta(1/r^2)^w-1)
                        (r^(-s)+r^(-(w-s))) dr/r,
    xi_Q(w,s)=s(s-w)Z_Q(w,s)/(2w).

Theorem4.4 and (4.5), using only y=0, give the source definitions

    h(w,x)=(theta(exp(2x))^w-1)/w,
    gamma(w,x)=(d_x^2+w*d_x)h(w,x),
    xi_Q(w,s)=1/2 integral_R gamma(w,x) exp(s*x) dx.

These are source formulas, not reproofs. No shifted-contour prefactor
is imported: review421 already records that qualification. Read the
positive-half-line estimates and modular reflection in Lemmas4.5-4.6,
the subtracted boundary terms in Lemma4.7, and both integrations by
parts in (4.6)-(4.9). The compact bounds apply for complex w as well
as real w. Cauchy's integral formula on a slightly larger compact
w-neighborhood is the standard route to parameter-derivative bounds;
mere smoothness at a single real parameter is insufficient. The bounds
are qualitative, with no supplied effective cancellation margin.

For applicability, the centered derivative means the ordinary chain
rule operator (partial_w + (1/2)partial_s) applied to xi_Q, evaluated
at s=w/2+i*t. It is not partial_w at fixed s. In the unshifted integral
the differentiated object is exp(w*x/2)*gamma(w,x), including the
exponential and the w appearing in gamma's differential operator.
Differentiating theta^w includes theta^w*log(theta). These are standard
calculus requirements identifying the observable, not an evaluated
derivative or a sign estimate. Any subsequent explicit formula and
effective domination proof belong to the mathematical attempt.

Theorem2.1's reflection, together with conjugation of its real-theta
integral, supports use of a real-valued centered family for real w,t.
The w=1 slice agrees with L018; L019 fixes the theta normalization.
No heat equation in w is stated by these results. At 1<=w<=3/2 the
center avoids s=0,w; even there the rational terms and completion may
not be dropped during differentiation. The entire completion also
controls parameter neighborhoods without introducing a pole premise.

The [published version](https://www.numdam.org/item/10.5802/aif.1939.pdf),
Ann. Inst. Fourier53(2003),1-68, Sections4.2 and8, was compared for
theorem and collision scope. The legible arXiv formulas are used where
the publisher's text extraction loses mathematical expressions. The
published Section8 retains the numerical premise and the printed
reflection by1; it does not repair the missing sign estimate. No
numerical coordinates from that discussion are accepted as certified.

### Fold orientation and failures that cannot pay it

Lessard's [author manuscript](https://www.math.mcgill.ca/jplessard/ODEs_files/saddle_node.pdf),
Definitions1-2/Theorem1, printed p2, assumes a simple kernel and
nonzero parameter and quadratic derivatives transverse to the range.
In the scalar setting these are G=G_t=0, G_w!=0, G_tt!=0. Use analytic
regularity here, not the printed C1 wording to dispense with second
derivatives. Prior contraction proof coverage is reused; no ODE
implementation or interval-certificate theorem is applied this turn.

The already proved local implicit-function orientation in L814's
orientation paragraph is the comparison: a positive product gives
two nearby real zeros on the smaller-parameter side, a negative product
on the larger-parameter side. Thus positive G_w*G_tt would be favorable
for decreasing w. This is a local convention, not a sign theorem for
this family. Boundary events require an extension neighborhood; no
two-zero count inside the closed test box is licensed. Degenerate
events and higher multiplicities remain outside this fold test.

Read review132 and the exact pair-energy/event-atom failure records.
The former retains its small-gap singularity in a real-simple regime;
the latter supplies no extra collision atom. Reused the completed
semiconcavity comparison; no such audit was repeated. Read the ready
Pólya collision assessment, its failure record, and L814's orientation
and relative-bound qualification. Choosing a free comparison coefficient
after seeing the unknown event sign merely restates it. These failures
apply to their stated mechanisms, not to all parameter deformations.

Section8's numerical departure is not an effective certificate for
G=G_t=0, nondegeneracy, the direction of a local fold or analytic branch
transport. Reviews422-423 already delimit that numerical premise; the
backend failure425 supplies no mathematical evidence about any sign.
The generator-to-Li stop422 is retained as a different-observable stop.
The positive convolution input assessed in review421 concerns negative
w and the w=0 generator; it supplies no positive-w collision product.

### Bounded search and resulting nomination

Queries used included `Lagarias Rains two variable zeta function double
zeros bifurcation theta powers real zeros w`, `"xi" "Lagarias"
"Rains" "collision" zeros`, `"Lagarias" "Rains" "double" "zeros"
theta derivative`, `"two-variable zeta" "zeros" monotonicity`,
`"theta" "power" "zeros" "Lagarias" collision sign`,
`"Lagarias" "Rains" "critical line" "derivative"`,
`"theta power" "parameter derivative" zeta zeros`, and
`"two-variable zeta" "sign" "derivative"`. Nonmatching search hits
were locators only, not theorem evidence. No matching sign result was
located in the inspected primary passages. This is not a novelty claim.

Local checks were restricted to the named theta/two-variable reviews,
theta failure records and the specific heat/affine comparisons above.
They found no completed uniform centered-parameter-derivative sign test.
No sibling notebook or cross-notebook result was consulted.

Automatic transfer of the product sign is parked. An independently
testable component is instead the **unconditional** proposed inequality
G_w(w,t)>0 on the same rectangle. It can be tested from the exact
differentiated integral without assuming an event, curvature sign or
branch. The discriminant is a proved uniform positive margin versus
one rigorously certified nonpositive value; a failure rejects only
this uniform sufficient-component route. An inconclusive absolute
bound is neither result. This changes the tested statement, rather
than spending a proof turn on the generic fold identity.

A positive result would still need an independently controlled G_tt
at events for the desired product; a negative result would not refute
the product restricted to events. Existence, higher multiplicities,
all heights, initialization, global transport and w=1 arithmetic remain
unpaid. No independently established sign or new cancellation mechanism
is available yet, so creative routing is not justified merely by this
nomination. The separate bounded analytic assessment is
`2026-11-11-theta-power-centered-derivative-sign-test-426.md`.
It requires separate approval next turn; no mathematical attempt has
been made here. Full matching Mathlib coverage remains unchecked.
