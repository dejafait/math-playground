# Polynomial Jensen-wedge lead — completed central-scope comparison

TARGET: Identify and compare the polynomial Jensen-wedge source flagged but unread in step465, testing whether its exact shift/degree hypotheses supply a central signed estimate beyond the prescribed-primitive stop.
CHECKED: 2026-11-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Step473 identified Holland arXiv:2608.08682v1 by polynomial-shift Jensen searches, checked its version record and primary sign/stability cases, and compared the named primitive/q-Pascal stops; exact queries and limits below. No novelty inference.
SOURCE_EVIDENCE: Holland v1 (9August2026), Theorem1.1, Proposition2.2/full proof, (10)–(14), Proposition4.1/proof, Lemmas4.2–4.3/5.1/5.3–5.4, (51)–(57), Lemma7.3/root hypotheses, Lemma8.1/full proof, Lemma9.1/displayed recurrence argument and Section10; reuse step465's accepted Griffin comparison and step379's primitive review. No full manuscript or external convolution-source audit.
COMPARISON: Holland claims a polynomial large-shift region and uses a constructed simple-rooted model with a controlled multiplier, rather than prescribed-primitive descent. Its defect signs are eventual; Section10 expressly excludes every n<n0. No central signed estimate was found in the inspected cases.
GAP: The source supplies neither shift-zero model admissibility nor its critical-value multiplier bounds, and does not address repeated-root primitive compatibility. Actual all-degree central signs remain open.
REASON: Informative source-scope negative: stop importing the wedge as a central transfer. Its exact coefficient-matching equations suggest a distinct finite-shift feasibility question, requiring its own assessment; no estimate has been extended or proved here.
LITERATURE_REASON: Changed scope from Proposition3.7's analytic Taylor audit to an essential unread polynomial Jensen-wedge source that may reveal a new central mechanism; the ready Taylor assessment does not cover it.
SCOPE: Completed literature-only comparison of the recorded lead. EXPLORE records no adequate central import, not permission to perform shift descent or nominate unspecified mathematics; no lemma, numerical test or mathematical script was produced.

The nomination below was proposed in step472. Step473 completed its
separate source review; retain its original question and stopping test
as scope, not as an outstanding approval request for this same review.

Use `drafts/literature/2026-11-05-growing-order-post-import-discovery.md`
under "Search and evidence limits" for the exact recorded lead:
newer polynomial Jensen wedges were search hits, not inspected inputs.
Its bibliography/primary identity must be established rather than
invented. Reuse that assessment's accepted Griffin–Ono–Rolen–Thorner–
Tripp–Wagner comparison at its stated scope and numbering. Do not
repeat the earlier three-mechanism discovery as though it were new.

Main gap: actual-Xi all-degree mixed positivity. The intermediate aim
is to determine whether this newer shift/degree result contains an
independently justified signed remainder or critical-value estimate
that could support a bounded central test. A smaller positive shift
threshold alone is not a central transfer. Plausible downstream use is
to nominate a precise actual-coefficient sign mechanism for a separate
creative proof attempt; no such mechanism is asserted to exist yet.

For the actual coefficient normalization, retain L019/L021 and only
the ordinary-coefficient definition from L776, as matched in L786.
L790 is a contrast showing the available analytic tail estimate, not
an unshifted sign premise. No lemma proof outside those necessary to
match the newly identified source should be loaded initially.

Compare the exact source with
`ATTEMPTS/2026-11-04-theta-jensen-prescribed-primitive-source-stop.md`
and the selected shift-descent discussion of
`drafts/literature/2026-11-04-actual-jensen-mechanism-discovery.md`.
That stop records missing control of the actual prescribed constant,
input root reality, repeated-root compatibility and signed critical
values. It is not a ban on a changed representation, but a tail-only
theorem does not discharge those assumptions. L765/L774's separate
norm/accretivity stops also remain intact; no implicit reopening is
intended.

Continue only if the primary hypotheses and essential proof case expose
a concrete new signed estimate with a bounded discriminating test and
an explicit possible connection to the central gap. Prepare its exact
assessment for separate approval and creative routing if warranted.
Otherwise record the precise shift barrier, source overlap or access
limit and stop this lead; do not turn a smaller tail threshold into an
unsupported descent argument. This review cannot renew an exhausted
mathematical mechanism by renaming it. Full matching Mathlib coverage
is unchecked. No cross-notebook theorem input is requested.

## Completed comparison — step473, 2026-11-05

Primary: Jonathan Holland,
[*A new hyperbolicity wedge and a joint semicircle limit for Jensen
polynomials of Riemann's xi-function*, arXiv:2608.08682v1](https://arxiv.org/html/2608.08682v1),
submitted 9 August 2026. The checked abstract record lists only v1.
Theorem1.1 asserts distinct negative roots for integer d>=1,n>=0
subject to n^3 log^2(n+2)>=K d^5, for an unspecified absolute K>0.
Section10 chooses K to exclude every n<n0. This improves the claimed
shift range compared with the accepted Griffin theorem reused from
step465, but supplies no central conclusion. No result is imported
into the canonical proof in this literature turn.

Source gamma is defined by xi(1/2+z)=sum gamma(j)z^(2j)/j!. This matches
the established local sequence gamma(j)=8*4^j*j!*a_j using L776's
ordinary coefficient definition only. Source (10)–(14) retain the
moment factorials; Section4 discusses Griffin et al.'s common factor8.
The gamma ratios are not raw-moment or ordinary-coefficient ratios.

Read Proposition2.2 and its full signed proof. Its degree-d model p
must have simple positive roots, d>=5 and p(0)!=0. Its multiplier must
be holomorphic near the closed radius-2r tube around [0,d], have real
integer values, agree with 1 through index4, have positive last value,
and differ from 1 uniformly by epsilon<16. At every critical point
it further assumes |y^k p^(k)(y)/p(y)|<=r^k for 0<=k<=d.
Finite Newton interpolation and Cauchy bounds give relative
critical-value error <epsilon/16<1. The proof also checks endpoint
signs at zero and positive infinity. It does not justify repeated
model roots by an unstated limit. This is a conditional stability
criterion, not an actual-Xi central estimate.

Read Proposition4.1's sectorial proof, Lemmas4.2–4.3 including finite
differences, and Lemmas5.1/5.3–5.4 including the polygamma signed-defect
case. Both defect signs are eventual. Exact formulas (37)–(38) do not
assert positive parameters at n=0. Lemma6.1 solves (51)–(52) only
eventually; (57) further requires A>=8B, B,D>=K_r d and
4d<=C-D<=D/4. Section7's Jacobi-factor argument imposes degree-dependent
root hypotheses, not scalar positivity alone.

Read Lemma8.1's complete proof. Its logarithm is justified within a
large-shift sector; (81) bounds the multiplier by
C_def*d^(5/2)/(n^(3/2)*log(n+2)) on the entire required tube.
Lemma9.1's displayed recurrence/maximum argument was inspected, not
independently replayed; it also retains the wedge and eventual onset.
Section10 treats d<=4 by exact matching and d>=5 by Proposition2.2,
always after enforcing n>=n0. Theorem1.2 is an empirical limit in the
same region, not a transfer to its complement.

The central-import test fails: the inspected source supplies no
prescribed-primitive critical values or bounded-shift replacement for
the model/multiplier estimates. In particular n=0,d>=1 never satisfies
Theorem1.1's hypothesis. This is new local source coverage and an
informative scope negative, not a refutation of the theorem or progress
beyond it. The exact matching equations could still be tested under
different hypotheses. L765/L774's norm/accretivity stops remain intact.

A distinct finite question is central feasibility of the exact matching
system at degree five. That would test a representation prerequisite,
not prove a new Jensen sign: small-degree hyperbolicity is already known.
Even success leaves multiplier bounds, growing-degree admissibility,
repeated-root issues and all-degree mixed positivity unresolved.
Missing growing-degree signed control still blocks a creative attempt.

Queries: Jensen polynomials Riemann xi hyperbolicity polynomial bound
degree shift; Jensen polynomials polynomial hyperbolicity wedge n d
recent; "2608.08682" correction erratum; Riemann xi Jensen Jacobi
comparison "shift" "zero"; Riemann xi "Laguerre defect" "Jacobi".
No correction was established; absence is not proved. Planat's
DOI10.3390/math14111884 remains an uninspected lead. Indexed criticisms
and secondary laboratory pages were not used as theorem evidence.
Narrow local searches located earlier unread Holland mentions and
the named primitive/q-Pascal stops, not an exhaustive duplicate census.

No complete manuscript, original finite-free convolution-source,
semicircle-proof or explicit-constant audit is claimed. Mathlib coverage
is unchecked. No new mathematical lemma or script, cross-notebook input
or counter reset. Initial notebook-scoped status output was oversized;
it was not used as exhaustive mathematical evidence.
