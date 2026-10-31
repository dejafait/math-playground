# Finite-rectangle collision barriers — completed source comparison

TARGET: Compare Polymath v2 Proposition 3.3's barrier hypotheses with excluding real multiple zeros of F on 1/100<=lambda<=11/200 and |x|<R_0, identifying the first independently uncertified premise.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the positive-transition comparison; searched Proposition 3.3 / zero barrier and de Bruijn-Newman barrier / multiple zeros; read the primary statement and complete first-contact cases, then Section 8.1–8.2's parameter and verification domains. Scoped local searches found no prior completed interior-barrier comparison. No stronger inspected collision-exclusion theorem was found; no novelty inference follows.
SOURCE_EVIDENCE: D. H. J. Polymath, arXiv:1904.12438v2 (4 August 2019), Proposition 3.3 and proof, printed pp.15–16; Theorems 1.2 and 3.2; Section 8.1–8.2 parameter/verification-domain paragraphs, printed pp.37–39; https://arxiv.org/html/1904.12438v2 and https://arxiv.org/pdf/1904.12438v2 . Planat arXiv:2609.37164v2 (7 October 2026) was located and its primary abstract/version inspected only; its theorem/proof is an unread lead, not an imported result.
COMPARISON: Proposition 3.3 excludes zeros at positive imaginary height at one final time; it asserts no real-zero simplicity. C493a controls only the spatial tail on positive source times 1/25<=t<=11/50. It supplies neither the initial cap nor the full intermediate-time barrier from t=0. At a finite-verification barrier the final-time region also extends far below C493a's spatial cutoff.
GAP: First there is a conclusion mismatch (positive-height exclusion versus real multiple-zero exclusion). For a tail-placed barrier at the small-height parameters of interest, the first undischarged premise is (i), zero-time zero exclusion through X near 2R_0; for a finite-verification placement, independent final canopy and intermediate barrier certificates are missing. No uniform y_0->0 or shifted-time theorem is supplied.
REASON: Informative negative comparison closes this direct application route. The proposition is useful for certified upper bounds on Lambda but does not fill the selected interior collision gap from available inputs. This is source-scope evidence, not a counterexample to a theta-specific barrier or RH.
SCOPE: Literature-only comparison; EXPLORE records the bounded unsuccessful theorem match, not approval to derive a new barrier. No lemma, mathematical script or new mathematical result is produced. The original nomination is retained below.
LITERATURE_REASON: The target changed from auditing a global spatial tail to comparing interior collision exclusion; the ready tail assessment covered no such implication.

## Exact primary premises and conclusion

Use the source H_t, not a redefined time origin. Proposition 3.3 assumes
 t_0,X>0 and 0<y_0<=1. Its three zero-free regions are exactly:

1. H_0: 0<=x<=X, sqrt(y_0^2+2t_0)<=y<=1.
2. H_(t_0): x>=X+sqrt(1-y_0^2), y_0<=y<=sqrt(1-2t_0).
3. H_t: X<=x<=X+sqrt(1-y_0^2),
   sqrt(y_0^2+2(t_0-t))<=y<=sqrt(1-2t), 0<=t<=t_0.

Conclusion: H_(t_0) has no zero at any real x and y>=y_0.
Theorem 3.2 then gives Lambda<=t_0+y_0^2/2. This is an import by
precise citation, not a new barrier derivation.

The proof handles the right boundary using (iii), the imaginary axis
using kernel positivity, repeated first contact using Proposition
3.1(ii), and simple first contact using the paired velocity sum.
The separating height is Y(t)=sqrt(y_0^2+2(t_0-t))>0; its derivative
is -1/Y(t). It does not test a repeated zero on the real axis.
The printed repeated-contact sentence says x+i*y_0 although the
preceding contact point is x+i*Y(t_1); this source notation discrepancy
is not a license to treat the proof as a real-axis endpoint theorem.
No independent audit or repair of the source proof is claimed here.

## Applicability comparison and decision

The exact conventions are already proved in L488 and used in C493a:
F(lambda,z)=8 H_(4lambda)(2z). Thus the available tail, in source
coordinates, begins at |Re w|>=2R_0=X_0+3, X_0=4*pi*exp(10000),
on 1/25<=t<=11/50. It includes both spatial edges and gives simplicity.
L058 supplies no missing oscillatory sign; L489 and C489a isolate a
possible finite multiple zero but do not exclude it. Their qualifications
and conditional transition premises are retained.

There are two meaningful barrier placements, neither completed by the
tail. If X is placed at or beyond 2R_0 so positive-time spatial control
can be used, premise (i) at small y_0 asks for a zero-time
low-cap certificate to an enormous new height. Neither C493a nor the finite-RH
input cited in L466 supplies it. Premise (iii) also runs from zero time,
not merely over C493a's positive band. Choosing y_0 to make the cap
empty does not supply real-axis or small-time control.

If X is placed within the established finite verification range, the
initial cap can instead be discharged by that named input. The next
unverified premise is then (ii): its region begins near X rather than
near exp(10000). C493a leaves the intervening canopy uncovered, and
(iii) needs its own certificate. These are independent quantitative
certification tasks, not consequences of spatial-tail simplicity.

The inspected source Section 8 uses t_0=y_0=0.2 and
X=6*10^10+83952-0.5, with separate final-region and barrier verifications.
Those parameter domains lead to its already imported Lambda<=0.22.
They are not certificates at smaller final times or smaller imaginary
heights. No source certificate is silently extended to new parameters.

Even supplying (i)–(iii) at one positive y_0 would leave real repeated
zeros outside the conclusion. Setting y_0=0 violates the hypotheses;
a limit would require new uniform premises. Starting the theorem at
lambda=1/100 would likewise change its stated H_0 hypothesis and is
not an import of Proposition 3.3. A strict upper threshold below the
bottom of the selected band would be a different useful target, but
none is supplied by the inspected applications. Consequently abandon
the direct proposition-plus-C493a collision-exclusion application.
This does not prohibit future independently certified barrier estimates.
Times below 1/100, zero-time control and all-degree positivity remain open.

## Duplicates, failures and continuation

Reused drafts/literature/2026-10-30-positive-transition-finite-collision-reduction.md;
its Proposition 3.3 discussion supported first contact, not exclusion.
The exact L489/C489a statements and C493a proof were inspected. L466's
Platt–Trudgian Theorem 1 citation supplies finite verification only.
The backward-energy and positive-endpoint inverse-gap stops in ATTEMPTS/
remain intact; this comparison neither fixes their endpoint loss nor
reopens the unread CSV proof. No generic shape argument is proposed.
Full matching Mathlib coverage is not checked; supporting local
analyticity is not a formalized global barrier theorem.

The narrow stronger-result search located Michel Planat, *Collective
Contraction in the de Bruijn--Newman Heat Flow: Off-Zero Logarithmic
Derivatives and Certified Barrier Refinements*, arXiv:2609.37164v2,
https://arxiv.org/abs/2609.37164v2 . Only its abstract/version was read.
The advertised bridge from off-zero observations to collective zero
interaction could expose a different, quantitative input; neither its
validity nor its small-height/multiplicity scope is assessed here.
Its claimed numerical improvement and base certificates are NOT imported.
Exact identifier/title searches in local literature/heat/attempt/history
paths found no existing assessment of this source. Unrelated search
claims were not accepted as theorems.

Next review is nominated separately in
2026-10-30-collective-contraction-collision-scope.md. A potentially useful
intermediate input would be a noncircular off-zero bound valid as the
highest nonreal zero approaches a real collision. Continue only if the
primary theorem supplies an independent certifiable quantity in this
regime; abandon this application if it assumes missing zero-free/gap
control or requires a fixed positive-height buffer. No new mathematics
or creative proof attempt is approved by this nomination.

Original nomination: compare a spatial-barrier mechanism against the
finite rectangle, retaining C493a, L058 and L489/C489a and R_0 above;
continue only for an independent theta-specific certification premise.
The comparison now meets its abandonment test for the direct application.
