# Cumulative-density zero-count route: domain comparison completed

TARGET: Review cumulative-density Laplace zero-count criteria for U(E)=integral_0^E v(t)dt, including transform-domain and endpoint-mass restrictions, and select one bounded actual-density test.
CHECKED: 2026-11-09
DECISION: IMPORT
SEARCH_EVIDENCE: Step79 reused the step46 Laplace assessment, searched cumulative/primitive and exact-object terms in the relevant November9 assessments and stops, and inspected the primary convergence/derivative/translation formulas and the complete Bhaskar–Song proof. Queries, access limits and the distinct nominated test are recorded below; no novelty is inferred.
SOURCE_EVIDENCE: NIST DLMF1.14.17–19,21,27, including the subsection-wide Re(s)>alpha restriction; Bhaskar–Song arXiv:1309.5056v3 Definition3, Theorem4 and complete proof p14, DOI10.1214/14-AOS1264. DLMF4.2.19 and standard Taylor's theorem cover the proposed finite exponential approximation. These are known methods, not an actual-density sign theorem.
COMPARISON: Raw U is bounded but need not decay; the cited derivative identity supplies its Laplace comparison on s>0, corresponding to lambda<0. No zero-total-mass condition is available to extend that integral argument to [0,1/20]. A fixed exponentially tilted primitive is a distinct domain-correct candidate; its specialization and signs have not been derived here.
GAP: The raw-primitive shortcut has an unpaid endpoint/domain condition. A later tilted-primitive test still needs complete weighted error bounds; global primitive variation, parameter endpoint signs, a tail join and all-degree transfer remain open. No U or tilted-U crossing theorem is established by this review.
REASON: Import the standard domain restriction and retire the unsupported raw-U substitution on positive lambda; nominate one bounded tilted cumulative test rather than retrying pointwise ratio or field mechanisms.
LITERATURE_REASON: The supplied REVIEW_REQUIRED target lacked essential primitive/transform-domain and endpoint-mass coverage; the existing density-level assessment did not cover this changed observable.
SCOPE: Completed source comparison only; no lemma, mathematical script, numerical test or new zero-count specialization was produced. The original nomination below is retained as history; the completed comparison supersedes its pending language.

## Purpose and bounded review

The main gap is L030–L032/C032a all-degree mixed positivity for actual
Xi. The intermediate purpose is to determine whether an integrated
sign certificate can help the fixed actual-H2 Laplace zero-count route
without requiring pointwise global crossing of v. No complete route
to all degrees is asserted. This is a nomination for a new source
comparison, not approval of a creative proof attempt or a domain sweep.

Use exactly L938's v and its M_0^12 normalization, and define only the
proposed observable U(E)=integral_0^E v(t)dt. L938 gives the existing
exact finite-polynomial primitive and full cell error estimates;
L946 supplies the now-audited compact crossing certificate, not a
global sign theorem. L939's eventual positive-tail input, including
its canonical audit qualifications and lack of an effective join,
must be checked before any use. C938a's stopped monotonicity is for
the component densities V_plus/V_minus; do not silently replace that
statement by cumulative masses. L940/L941's pointwise balancing
obstructions and L942/L943's restricted field/candidate failures
remain preserved. They are comparisons, not assumed premises.

First reuse the existing Laplace assessment and inspect only the
necessary primary theorem hypotheses and relevant proof cases for
primitive/cumulative versions of variation diminution or zero counts.
Search exact standard terminology and stronger results. Pay particular
attention to the sign convention s=-lambda, the required lambda range,
the possible nonzero limiting mass of U, boundary terms, and whether
the theorem controls zeros with multiplicity. Do not assume that
L938's rapid decay of v is also rapid decay of U. Do not assume an
unknown H2 sign to discharge an endpoint-mass condition. A theorem
limited to an irrelevant parameter half-line is not adequate coverage.

The discriminating review test is to identify a cited theorem whose
hypotheses leave one concrete, bounded actual-density estimate with
plausible downstream use, together with the remaining global join
and endpoint obligations. If every available criterion requires the
same unresolved pointwise crossing, an unknown target-equivalent
sign, or an unpaid endpoint/domain condition, reject this proposed
shortcut explicitly. A useful negative theorem comparison is enough;
do not manufacture a new lemma or repeat the old field fits.

Essential possible inputs are L938, C944a and L946; C938a and
L939-L943 are scoped comparisons or qualified potential tail inputs.
No cross-notebook theorem is nominated. Degree/precision changes,
new sign experiments and mathematical scripts are not authorized by
this REVIEW_REQUIRED assessment. Numerical execution trust, other
energies, contacts, parameter signs, degrees, initialization and
realization remain unresolved unless already explicitly covered.

Discovery priority is retained. A later genuinely new actual-density
mechanism may merit proof_attempt/creative only after its source
coverage is approved, with a precise bounded test and escalation.
The present blocker is missing theorem-level coverage for the
primitive and its parameter domain; it is not a quota or a global ban.
Full and supporting Mathlib coverage for this new target is unchecked.

## Completed comparison — 9 November 2026, step79

### Primary statements and essential proof cases

Reuse the inspected Tokarev comparison in
`2026-11-09-actual-h2-signed-convolution-discovery-45.md`; it is not
an additional multiplicity theorem for primitives. Reopened
[Bhaskar–Song v3](https://arxiv.org/pdf/1309.5056v3), dated
1 December2014, Ann. Statist.42(6),2469–2493,
DOI10.1214/14-AOS1264: Definition3 on reprint pp7–8, Theorem4 on
p9, and the complete proof on p14. The hypotheses are a nonzero
piecewise-continuous function with finitely many sign changes;
zero intervals are ignored and roots are counted with multiplicity.
The proof treats the constant-sign case, exponential conjugation,
multiplication by the distance from a first crossing, differentiation,
and Rolle's theorem. Its convergence/differentiation qualification
from step46 remains essential. This theorem bounds zeros of the
transform of the supplied function, not of an arbitrary derivative.
It does not certify the missing sign variation of U.

[DLMF §1.14(iii)](https://dlmf.nist.gov/1.14#iii), read
9 November2026: (17) defines the sign convention; (18)–(19) impose
piecewise continuity and an exponential growth bound and give the
analytic half-plane. The sentence after (19) retains Re(s)>alpha
throughout the subsection. Formula (21) is exponential translation.
Formula (27) requires continuity of f on the closed half-line and
piecewise continuity of f', and includes the initial value f(0+).
It does not remove convergence or boundary requirements.
Also inspected [DLMF4.2.19](https://dlmf.nist.gov/4.2#E19), the
exponential power series. A later finite test may use standard
Taylor's theorem with Lagrange remainder; no exponential enclosure
or actual integral was calculated in this turn.

The local applicability comparison is as follows. Write
F(lambda)=M_0(lambda)^12 det H2(lambda), retaining L938's convention.
L938(1),(2) identify the total signed mass m with F(0). Absolute
integrability makes U bounded with limiting mass m; continuity gives
U'=v and U(0)=0. Applying the cited derivative identity to U is
therefore a comparison on s>0. In that domain it reads
L(v)(s)=s L(U)(s). The desired lambda interval is [0,1/20], so its
s=-lambda interval is [-1/20,0]. The available comparison has no
overlap with that interval.

If m is nonzero, U has a nonzero constant limit: its defining
Laplace integral does not converge at s<=0, and the upper boundary
term cannot be deleted there. No assertion that the actual m is
nonzero is made. Conversely, importing m=0 would import F(0)=0,
an unproved determinant equality, rather than a harmless convention.
One may not continue the quotient analytically and then apply a
variation theorem outside the integral's convergence domain.
Subtracting m would change the initial value to -m, so (27) retains
an additive m term; zeros no longer follow merely from variation of
the centered primitive. These are scope checks on the cited formula,
not a new primitive theorem. No sign of m was computed or assumed.

### Distinct bounded nomination, without its mathematical execution

The selected candidate replaces only the observable, not v:

    b=1/10,  U_b(E)=integral_0^E exp(bt)v(t)dt.

The proposed domain test is to use the cited integration and
translation rules at s=b-lambda>0. This is why b is fixed strictly
above 1/20; it was not fitted to sign data. The prospective relation
between F and the transform of U_b, and any multiplicity-preserving
zero-count consequence, must be justified later with the actual
boundary terms. Boundedness of U_b, local dominated differentiation
on s>0 and the nonvanishing factor s are the obligations to check.
No sign of the limiting tilted mass F(b) is supplied or required as
a zero-mass premise. At lambda=b the argument would again require
separate treatment. We do not assert a theorem at that boundary.

For this mechanism select exactly the two-point endpoint diagnostic
specified in `2026-11-09-l938-tilted-primitive-endpoint-test-79.md`.
Its intended signs are U_b(1/4)<0<U_b(4), with full actual-kernel
and exponential errors. The method uses the already fixed L938
polynomial, not a new theta fit. Neither sign has been evaluated.
If paid, this is a useful compact integrated sign contrast that could
combine with L946's derivative geometry. It is not a full crossing
count, and neither a global join nor determinant endpoint signs
would follow from two samples. A failed sign or inconclusive bound
ends this proposed compact join test without refining b, energies or
budgets. It does not refute an eventual primitive crossing or RH.

This elementary source specialization and endpoint calculation is
not classified creative. The blocker to a justified central creative
proof nomination is still a concrete global primitive sign/variation
mechanism and paid join; the bounded diagnostic tests feasibility
before such a nomination. Independent gaps in contacts, other
parameters, degrees, initialization and realization remain.

### Search, duplicate comparison and access record

Local reads were restricted to L938's representation/primitive/error
ranges, C938a's statement and endpoint proof ranges, L939's statement
and audit qualification, L946's statement/method ranges, and relevant
L940–L943 statements plus the identified November9 assessments.
The ratio-endpoint assessment61 explicitly concerns densities, not
cumulative masses. The endpoint-head-margin assessment concerns a
Rayleigh quotient at lambda=0, not U_b. L943's failed field candidate
does not obstruct this different integrated observable. No duplicate
tilted cumulative endpoint test was identified in the paths checked;
that is not evidence of originality. L939's eventual positive density
has no effective join here and was not used to discharge one.

External queries included `Laplace transform cumulative integral sign
changes generalized Descartes primitive zeros boundary terms`,
`Jameson zeros Laplace transforms cumulative integral Descartes rule
signs 4.5`, `Laplace transform cumulative sign changes`, and exact
Jameson/Bhaskar–Song terms. Further signed-measure/tail-integral terms
returned probability-tail identities with different hypotheses; none
was imported as a signed-density sign theorem. Search results alone
did not establish a stronger cumulative criterion for this exact v.

Jameson, Math. Gazette90(518)(2006),223–234,
[DOI10.1017/S0025557200179628](https://doi.org/10.1017/S0025557200179628),
remains an unread antecedent: the publisher page supplied bibliographic
information, not Lemma4.5. Lancaster access failed. It is not an
essential blocker because Bhaskar–Song's entire relevant proof was
read as extracted primary text. A PDF screenshot timed out or yielded
no inspectable image; no image-only assertion is used. Direct shell
downloads failed DNS and supplied no evidence. DLMF statements and
their domain sentence were available in primary extracted text.

No full or supporting Mathlib match for the cumulative criterion was
checked. No new lemma, mathematical script, DAG input, or PROOF
assembly was written. This is an informative negative source-domain
comparison plus a separate future nomination, not a mathematical
advance beyond the cited sources.
