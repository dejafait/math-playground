# Joint null-row origin-sign test — completed source review

TARGET: Assess a null-row elimination test of L918's unpaid origin condition J>=0 for normalized d=2 PSD contacts with c2!=0 and 0<lambda<=1/20, retaining actual-theta moment constraints and distinguishing algebraic countermodels from actual contacts.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Step207 completed bounded exact/stronger searches for theta/Stein origin signs, reciprocal-logarithmic Hankel null vectors and moment-kernel elimination; checked L918/L874, prior density coverage, and steps193/195/199/204/206 plus the older root-elimination stop. Queries and inspected versus unread evidence follow; no novelty inference.
SOURCE_EVIDENCE: Ley-Swan ECP18(2013), paper7, Definition2.1/Theorem2.2 pp2-3 and both proof directions reread; Laurent, Sums of squares, moment matrices and optimization over polynomials, updated 2010-02-06, Lemma4.2 pp54-55 and Lemma5.2 pp68-69 with proofs, Theorem5.20 p75 hypotheses, Theorems3.12/3.15 pp35-36 statements. Exact links and scope below. No source supplies the origin sign.
COMPARISON: The known Stein operator gives zero means, not J>=0. Moment-kernel statements require the correct raw-moment matrix and, for ideal propagation, infinite data; a finite logarithmic H2 null vector does not license those additional premises. Joint finite-row algebra remains a distinct bounded test, with no guaranteed sign or finite certificate.
GAP: The exact joint-row reduction and independent sign of the resulting inverse-coefficient quadratic remain unpaid. Actual theta realization cannot be inferred from any relaxed algebraic countermodel; the full residual, contact existence and global continuation also remain open.
REASON: Coverage is adequate for one subsequent bounded elimination/sign-or-obstruction attempt, not for a sign import. This necessary origin test could screen the fixed W_* residual before any compact-sign work. No mathematics, lemma or script was added in this literature turn.

## Exact proposed scope and prerequisites

The main gap remains all-degree actual-Xi mixed positivity. At a
hypothetical actual d=2 contact, retain L918's complete hypotheses:
0<lambda<=1/20, real unit c with c2!=0, H2 PSD and all three null rows.
L019/L058/L874 define the actual density and coefficients. Let
a_n=[z^(2n)]1/g_lambda(z), with the same local normalization. L918(5)
defines J=sum_(i,j=0)^2 c_i c_j((i+j+2)a_(i+j+2)+a_(i+j+1)).
No contact is asserted to exist, and generic positive moment data are
not assumed to realize the actual theta family.

The proposed new mechanism is **joint exact elimination of the null
rows before a sign comparison**, instead of the old rowwise absolute
enclosure or the finite-head margin. The source review must read the
relevant canonical proof, reuse adequate density-method coverage,
check exact-statement duplicates and the recorded failures, then decide
whether this produces a genuinely different bounded mathematical test.
No elimination, sign derivation or countermodel search has been done
in step206. This file approves none of them.

A useful later test would either establish J>=0 under all the actual
premises by an explicit identity/bound, or exhibit a precisely qualified
algebraic obstruction showing that a proposed reduced premise set is
insufficient. An abstract countermodel cannot establish J<0 at an actual
contact. If the mechanism merely restates the unpaid actual sign without
a discriminating bound or an independently testable reduced-premise
obstruction, abandon it rather than repeat compatibility checks.

Even a positive origin result leaves nonpositivity of the residual on
the remaining compact interval, uniform contact control, higher-degree
signs and global continuation unresolved. These independent gaps must
not be hidden by a local coefficient result. Primary coverage and full
Mathlib availability for this sign target are not yet checked.

## Completed comparison — step207, 9 November 2026

The nomination above is preserved as the invocation-start specification;
its statements that coverage was incomplete describe step206. This section
and the updated fields record the completed review. No sign or elimination
has been derived here. The main gap, intermediate target, downstream use
and remaining independent gaps are exactly those in the nomination.

### Source scope

C. Ley and Y. Swan, *Stein's density approach and information inequalities*,
ECP18(2013), paper7, [final journal PDF](https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/2578/2199.pdf),
Definition2.1/Theorem2.2, pp2-3: reread the interval-supported normalized
positive differentiable density hypotheses, zero endpoint products, and
both proof directions. Sufficiency integrates the derivative; necessity
uses centered indicators. The rule supplies zero expectations, without
a pointwise sign or a polynomial solution guarantee. L918 already checks
the actual density's polynomial boundary limits and absolute integrability.
Reuse that interface; redoing it would not pay the origin coefficient.

M. Laurent, *Sums of squares, moment matrices and optimization over
polynomials*, [author's updated manuscript, 6 February 2010](https://homepages.cwi.nl/~monique/files/moment-ima-update-new.pdf):
Lemma4.2 pp54-55 gives raw moment/localizing PSD and support restrictions
from a kernel polynomial; read all three proof cases. Lemma5.2 pp68-69
uses an infinite moment matrix for its ideal/real-radical assertions;
read both proof parts. Theorem5.20 p75 needs rank equality with the
preceding truncation. Theorems3.12/3.15 pp35-36 describe polynomial
positivity/infeasibility certificates; their statements, not a degree
bound or full proof, were inspected. None supplies J's sign or finite
search completeness. No flat extension or representing measure for H2
is imported.

Application limits: L019/L058 define the actual probability law, whereas
H2 in L874 uses coefficients of its logarithm. The future test must
retain this distinction and use only the three supplied null equations;
extra shifted rows, support restrictions or higher-degree PSD need
independent justification. A polynomial certificate must be checked by
an exact identity and the signs of every multiplier. A failed bounded
certificate search is inconclusive. The actual theta moment curve is
not replaced by a finite semialgebraic relaxation without an explicit
scope qualification. These are source-comparison requirements, not a
new elimination or obstruction theorem.

### Duplicates, failures and searches

Read L918's full proof, L874's relevant complete coefficient/null/density
arguments, L019/L058, and L917's hypotheses, accepted enclosure conclusion
and finite coefficient conventions. Reuse the adequate density and
heat-contact assessments rather than reopen zero-dynamics, generalized
comparison or product/Jensen coverage. The older root-eliminating
Bezoutian assessment and its stop concern rational congruence/inertia,
not this origin quadratic; they warn against automatic sign transfer,
but are not a global ban on exact elimination. The older low-moment
origin-closure stop concerns a continued angular evaluation cost, not J.
No duplicate origin-sign proof was found in these relevant local paths.

Step193's absolute lower bound lost signed reserve. Step195's actual
third-minor intervals contain zero; that does not certify a contact.
Step199 stopped precisely at J. Step204 closed repeated tail approval;
step206 closed the fixed endpoint Rayleigh test. Their canonical stop
files were inspected and remain unchanged. L918 itself is unaudited;
its coefficient convention must be checked at the start of any attempt.

New bounded web queries (actual searches, not source claims):
`"Riemann" "Hankel" "null vector" heat`;
`"reciprocal" "logarithmic coefficients" "Hankel" positivity`;
`"theta" "Stein" "origin" positivity`;
`Laurent sums of squares moment matrices kernel polynomial ideal real radical equality constraints survey`;
`"Riemann" "Hankel" "Stein" contact sign`;
`"heat" "Hankel" "reciprocal" theta positivity`;
`"Hankel" "cumulants" "null" positivity exponential generating function`;
`"Riemann" "origin" "null rows"`.
The inspected primary texts above supply method scope, no exact match.
Hankel-transform hits concern another object. Search-only Hirschman-Widder,
new sparse-moment, and generic cumulant/criterion hits remain uninspected
leads and are not theorem or novelty evidence. They are not essential
inputs to finite algebra checked directly. Full and supporting Mathlib
coverage of this sign target is unchecked; no absence is asserted.

### Decision and next gate

One bounded joint-row sign test is justified by the still-unused signed
correlations, without redoing a determinant box or endpoint enclosure.
The precise subsequent mathematical target is saved in
`drafts/literature/2026-11-09-l918-origin-joint-elimination-test.md`.
It requires separate supervisor approval before invocation. Continue only
on a rigorously checked origin-sign certificate or a precisely scoped
reduced-premise obstruction; a residual unsigned expression ends the
attempt. No tuple/degree/band changes, sweep, head census, full residual
claim or automatic continuation follows. This completed literature turn
is EXPLORATION/NOVELTY_UNCHECKED, not a mathematical advance or informative
actual-family negative. It spends no mathematical exploration turn.
