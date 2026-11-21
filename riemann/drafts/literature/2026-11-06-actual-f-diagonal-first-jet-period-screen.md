# Actual-F quadratic diagonal: first-jet source screen

TARGET: Review source coverage for a first-jet test of whether quadratic diagonal vanishing of actual F constrains C868a's free period mean A beyond its value-trace identities in L868's full C1 class.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed targeted first-jet/normal-derivative/diagonal-vanishing searches in the named local proofs, 6 November assessments, histories and failure notes; external exact-system and stronger closed-form/jet/period searches listed below found no inspected matching period theorem. Reused the existing calibration and compact Fourier comparisons; failed searches establish no novelty.
SOURCE_EVIDENCE: Freshly inspected Lebl Basic Analysis II v6.3 Definition8.3.1/Proposition8.3.2 pp35-36, Theorem8.3.7 and complete proof p38, Definition8.3.8 p39, https://www.jirka.org/ra/realanal2.pdf ; Basic Analysis I Definition4.1.1 and Lemma4.2.2/proof, https://www.jirka.org/ra/html/sec_der.html and https://www.jirka.org/ra/html/sec_mvt.html ; SCV v4.4 AppendixC exterior derivative p223 and TheoremC.6/regularity remark/restricted proof p224, https://www.jirka.org/scv/scv.pdf . Reused compact Fourier/differentiation and calibration assessments at their stated scopes.
COMPARISON: Standard differentiability and chain rules cover local first-derivative operations at C1 regularity, not an actual-F period estimate or a global admissible extension. C868a/C868b establish value-trace and mode restrictions; L872/L873 do not test quadratic-diagonal normal first jets. Existing calibration/factorization results do not supply the missing variable-coefficient period bound.
GAP: A separate mathematical test must determine what the quadratic domination implies for first jets, whether closure turns that information into a restriction on A, and whether any restriction improves the threshold K=A+H>=-|M|. No such derivative identity or restriction is derived here.
REASON: Essential elementary calculus and exact-class overlap coverage is adequate for one bounded first-jet diagnostic. No matching theorem was found for direct import; the separately saved research continuation requires next-turn approval and does not authorize another stopped interchange or normal convolution.
LITERATURE_REASON: Invocation-start coverage was missing for the changed normal first-jet mechanism. This turn fills that named source gap while reusing the completed value-trace/Fourier/calibration reviews; it does not repeat browsing on the completed L872 audit.
SCOPE: Literature comparison only; retain the actual coefficient, global real C1 periodic q,r,h, h>=0, full domination and both closure equations. No C2 assumption, uniform derivative bound, restricted lift modes, C0 forcing hypothesis, zero simplicity, graph existence or RH may be added.

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. The candidate intermediate obstruction is the free mean
A in K=A+H, with H>=0 and required threshold K>=-|M|. Here K is
the constant angular mean of q+h, A is q's constant mean along
equal-radius tori, and M is the angular mean of actual F, with the
orientation and normalization of L868. A new restriction on A could
test the sharp-period problem without passing L872's moving Fejer
limit. A period result would still require its own implications for
graphs and Xi; those are not assumed solved.

Essential input IDs for the proposed comparison are L868, C868a
and C868b, with actual F inherited from L847. In particular

\[
 F(z_1,z_2)=-C G(z_1)G(z_2)(z_1-z_2)^2/(z_1^2z_2^2),
 \qquad z_j=R e^{x_j+i y_j},\quad C,R>0,
\]

and both equations r_xj=q_yj and (q+h)_xj=-r_yj hold globally.
The question is whether exploiting the squared diagonal factor
through first differentials, including normal directions, yields
period-sensitive information not already present in the value-trace
calculation. No particular differential identity is claimed here.
No zero of G is assumed simple or used to divide q,r by F.

L872 is a contrast explaining the unpaid moving error; L873's
normal-convolution stop is another contrast, not a premise. The
new proposal does not smooth in a normal direction, truncate a
feasible lift, or assert a global Fourier derivative bound. Read
only the exact relevant proof and stop ranges during comparison.
In particular retain
`ATTEMPTS/2026-11-06-fourier-diagonal-period-uncontrolled.md` and
`ATTEMPTS/2026-11-06-g-zero-fiber-period-gap.md`.

The next source comparison should inspect primary C1 domination/
vanishing and differential-form or Fourier-closure hypotheses,
check whether an existing local result already covers this test,
and distinguish local derivative restrictions from a bound on the
global mean. Only then may a separate mathematical turn test the
candidate. A useful bounded test must either obtain a genuinely
additional restriction on A under the exact class or identify why
first-jet information leaves the period freedom untouched. Mere
reproduction of C868a's constant A or coefficient bounds is a stop,
as is an argument requiring unsupported second derivatives or
uniform control at infinity. No new theorem is derived or approved
in this nomination; Mathlib coverage is unchecked.

This is source preparation for an independently testable mechanism,
not a creative-attempt claim. A central creative nomination remains
unjustified until a period-sensitive test and its essential coverage
are identified. It does not restart the exhausted L872/L873
operations or reset their exploration evidence.

## Completed source comparison, 6 November 2026, step34

The preceding nomination is preserved as historical scope. Its missing-
coverage statements are superseded by the fields and comparison here.
This is one literature-only step, with no new lemma, mathematical
script, first-jet identity, period inequality or feasibility assertion.

### Exact input and duplicate/failure comparison

Read all of L868, C868a through the mode/value-trace/positivity proof,
C868b's hypotheses and fixed-fiber proof setup, and L847's actual-F
hypotheses. The actual G is entire, the coordinates are nonzero, and
R,C are fixed positive constants. The diagonal is x1=x2 AND y1=y2
modulo 2pi; equal angles at unequal radii do not constitute it.
No division by G, F or q is licensed, including at intersecting divisors.

Read both named ATTEMPTS notes in full. C868a's finite diagonal
subtraction fixes A but leaves its size unpaid. C868b's other fiber
bounds the exceptional correction modes but retains K=A+H. Inspected
L873's actual-trace paragraph: it differentiates only tangentially to
a fixed G-zero fiber before explaining why localization loses that
trace. L872's completed audit and its unpaid estimate(8) are reused
from the supplied checkpoint and ready assessment, not reproved.
These are contrasts, not premises for a new normal-derivative theorem.

Scoped searches used `first.jet`, `normal.derivative`,
`quadratic.*diagonal`, `diagonal.*vanish`, `Whitney`, `Fermat` and
`Hadamard` in the 6 November literature/history/ATTEMPTS paths.
They located the nomination, exchange-diagonal graph-jet reviews,
ordinary extremum reviews and fixed-fiber tangential calculations;
no completed matching dual-class first-jet test was located.
The graph-jet results have different unknowns and conclusions and
are not imported. No sibling notebook was read.

External bounded queries were:

- `"closed" "two-form" "quadratic" "diagonal" domination period`
- `"C1" "vanishing" "quadratic" derivative submanifold`
- `"closed differential forms" "vanishing" "first jet" periods`
- `"periodic" "r" "q" "h" "closed" "domination" differential form diagonal`

Results included unrelated incidence geometry, Lagrangian and Dirichlet-
form uses of these words. Those leads were not read as theorem inputs;
their snippets supply no mathematical evidence. More specific author-
source searches located the calculus texts below. The exact-system and
stronger-result comparison also reuses
`2026-11-06-oriented-one-sided-dual-period-test.md` and
`2026-11-06-one-sided-fourier-diagonal-period-test.md`, whose inspected
Harvey–Lawson, Ball–Currie–Olver, Helein and polynomial-factorization
hypotheses remain unchanged. No new matching theorem or novelty claim
is inferred from these searches.

### Primary operations and their applicability boundary

Jiří Lebl, *Basic Analysis II*, v6.3, 15 May 2026,
[Definition8.3.1/Proposition8.3.2, pp35-36](https://www.jirka.org/ra/realanal2.pdf#page=35),
[Theorem8.3.7 and proof, p38; Definition8.3.8, p39](https://www.jirka.org/ra/realanal2.pdf#page=38):
differentiability is approximation by a real linear map with remainder
o(norm of increment), uniquely determined. The chain rule requires
open domains, domain inclusion and differentiability at the two
evaluation points. Read its whole remainder proof, including zero
intermediate increment and the bounded quotient for nonzero increment.
The partial-derivative definition permits coordinate difference
quotients. The notebook's C1 functions and smooth local logarithmic
charts meet these regularity hypotheses. Establishing the particular
quadratic bound and its consequences is reserved for research; no
Taylor theorem with second derivatives is imported.

Lebl, *Basic Analysis I*, author HTML inspected 6 November 2026,
[Definition4.1.1](https://www.jirka.org/ra/html/sec_der.html) and
[Lemma4.2.2/proof](https://www.jirka.org/ra/html/sec_mvt.html):
read the derivative limit and both interior-extremum cases. These
support ordinary one-variable reasoning when its hypotheses are
verified; neither says that merely vanishing on a submanifold forces
normal derivatives to vanish. The target must use domination, not
silently replace value vanishing by stronger jet data. Reuse the
already inspected Theorem4.2.4/Proposition4.2.6 for any finite-interval
constancy step. A guessed `sec_derivative.html` URL failed; the exact
linked `sec_der.html` and PDF were accessible, so no blocker persists.

Lebl, *Tasty Bits of Several Complex Variables*, v4.4, 31 May 2026,
[AppendixC, pp223-224](https://www.jirka.org/scv/scv.pdf#page=223):
freshly read the coefficient formula for exterior differentiation,
TheoremC.6, its subsequent lower-regularity remark, and its restricted
FTC/Fubini proof with induced boundary orientation. The displayed
theorem assumes smooth compact oriented manifolds-with-boundary and
smooth forms; the remark mentions reduced regularity without stating
a precise general C1 theorem. No new C1 Stokes application or global
extension is justified from that remark here. L868's existing closure
system and period interface are retained as local inputs. The proposed
diagnostic only substitutes into those first-order equations; it does
not differentiate them again or need a new Stokes theorem.

For any compact coefficient/trace operations, reuse
`2026-11-06-diagonal-fourier-correction-audit.md` and
`2026-11-06-l872-moving-trace-audit-review.md`: Rudin Theorem9.42
and Grafakos's product Fejer and periodic integration-by-parts inputs
at the cited editions/pages/direct URLs. Their compact C1 hypotheses
were already checked. They do not grant global angular summability,
moving-radius control or preservation of feasible domination by
approximants. No additional source inspection on that unchanged scope
was needed. Full matching and supporting Mathlib coverage remain
unchecked; no absence claim is made.

### Bounded continuation and stop

The exact research target and reused coverage are saved in
`2026-11-06-actual-f-diagonal-first-jet-test.md` for separate next-turn
approval. It asks for a first-order diagnostic, not an already proved
rigidity principle. Continue only with an additional restriction
relevant to A or a precise demonstration of where this necessary-data
test loses that information. Merely reproducing constant A or H bounds
does not supply threshold leverage. If only formal jet or trace data
can be varied, that is evidence about the necessary-data reduction,
not a countermodel in the full global actual-F class.

Stop rather than add C2, a global derivative/growth/tail bound, C0
forcing, zero simplicity, RH or a global extension premise. A failure
to derive a bound in one calculation is not proof that no full-class
bound exists. Quantitative period control, graph realization and Xi
signs remain unresolved. Creative priority was considered: an
elementary first-order diagnostic on this established route does not
yet justify a new central creative mechanism. No exploration or
recovery counter is reset by this source step.
