# Completed scope review: actual moment boxes in the origin contact test

TARGET: Assess adding L917's fixed panel-zero moment boxes to L921's joint-null-row relaxation, for an exact feasibility and J>=0 test at L918's degree-two contacts.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Step216 reused the inspected L918/L921 assessments and compared L917/L918/L921 with steps178/195/199/209/213 and covariance/heat-recurrence stops; six changed-scope exact/stronger queries found no inspected matching sign or feasibility theorem. Queries, source scope and unread leads are recorded below; no novelty inference.
SOURCE_EVIDENCE: Laurent, author manuscript updated 2010-02-06, Lemma4.2(i)-(iii) and proofs pp54-55, Theorems3.12 pp35-36, 3.15 p36 and 3.16 p37, https://homepages.cwi.nl/~monique/files/moment-ima-update-new.pdf ; retrieved exact polynomial/disequality hypotheses and nonstrict-positivity limitation. Reuse Ley-Swan Definition2.1/Theorem2.2 coverage and L037/L917's audited interval interface; full saved panel0 moment endpoints inspected.
COMPARISON: Known necessary raw-moment PSD and exact polynomial certificates cover the method, including singular contacts and c2!=0; they do not decide this fixed numerical set or J. L921 omits these numerical boxes, L917/L922's determinant stops do not decide contact-conditioned J, and compact strict-positivity theorems do not guarantee a certificate for J>=0.
GAP: Coverage for one fixed-box exact test is complete; its feasibility and J sign remain uncomputed. Finite box feasibility does not imply theta realization, and origin positivity alone leaves compact residual/flux, initialization/equality, other panels/degrees and global continuation unresolved.
REASON: The previously omitted actual-theta intervals give a separately testable finite strengthening; exact normalization, singular cases and certificate acceptance are now specified without a new calculation, lemma, determinant refinement or sign claim. The subsequent mathematical nomination requires separate approval.

The following nomination records the invocation-start scope from step215.
Its pending-review statements describe that earlier state. Step216 completes
only the source comparison below; no feasibility or sign calculation is made.

Use exactly L917's existing panel0, lambda in [0,1/5120], moments through
twelve and positive M0 lower bound. Proposed actual contacts satisfy
0<lambda<=1/5120, H2 PSD, H2 c=0, ||c||=1 and c2!=0, with L918's
unchanged J and coefficient conventions. The intended new information
is the necessary enclosure of y_k=M_(2k)/M0 from those saved full
moment intervals. No new quadrature, cutoff, parameter panel, degree,
precision or wider numerical search is proposed. The exact finite set
and normalization must be specified and assessed before a proof attempt.

Reuse `2026-11-09-l918-origin-joint-elimination-test.md` and
`2026-11-09-l918-origin-null-row-sign-review.md` for the inspected
finite-log, density and polynomial-certificate sources. Read only their
relevant theorem/proof cases and the fixed panel0 evidence. The former
assessment explicitly excludes L917 numerical bounds; it does not
preapprove this changed target. Check exact and stronger known results
and any local duplicate before approving a mathematical continuation.
Do not redo general covariance, heat-flow or cumulant searches.

Bounded future discriminator: first retain the possibility that the
strengthened contact constraints are infeasible. Seek an exact
infeasibility certificate, or an exact certificate J>=0 on the set, or
a verified box-compatible countermodel with J<0. A bounded failure to
obtain any of these is inconclusive; rejecting L921's old witness alone
is insufficient. A countermodel is not an actual-theta contact. A
feasibility certificate need not assert theta realization. No numerical
optimization output without a checked exact witness/certificate settles
the sign. Avoid dividing by c2 without retaining its nonzero, potentially
arbitrarily small value and all limiting cases.

Downstream use: infeasibility would exclude local d=2 contacts; a
conditional J sign would pay only L918's necessary origin condition.
The compact residual, actual flux, initialization/equality, other
panels/degrees, global continuation and L030-L032/C032a remain open.
Essential inputs are L019/L037/L058/L874/L917/L918/L921; L922 supplies
only the contrast and stop, not a positive sign premise. Decimal-library
correctness remains assumed if the L917 data are used. No cross-notebook
input is proposed. Full/supporting Mathlib coverage remains unchecked.

This is preparation of an established-route strengthening, not a
protected creative attempt. No source-ready new signed kernel identity
was identified in the audit; the automatic covariance and theta-heat
recurrence stops remain pertinent. A genuinely creative continuation
requires such a materially different, explicit mechanism and its own
bounded test, rather than relabeling this finite specialization.

LITERATURE_REASON: The proposed target adds actual-theta numerical constraints expressly absent from the previous joint-row scope; a separate exact-hypothesis approval is required, reusing adequate sources.


## Completed source comparison — step216, 9 November 2026

The main gap, downstream use and independent unpaid signs remain those
specified above. The exact intermediate target reviewed here is adding
only the existing panel-zero moment information to the L921 relaxation.
This review does not test the old witness against the box, calculate J,
or infer that contacts exist. The mathematical nomination is saved in
`drafts/literature/2026-11-09-actual-box-origin-feasibility-test.md`.
It is ready as source coverage, subject to the separate next-turn approval.

### Source statements and changed hypotheses

Reuse the complete density-method comparison in
`2026-11-09-l918-origin-null-row-sign-review.md` and the direct-source
repair in `2026-11-09-l918-origin-joint-elimination-test.md`.
Ley and Swan, ECP18(2013), paper7, Definition2.1/Theorem2.2 pp2-3,
https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/2578/2199.pdf,
requires a differentiable positive normalized interval density and
vanishing endpoint products for its test function. Only the zero-mean
identity is relevant; it supplies no sign of J. Its hypotheses and both
proof directions were already inspected. No fresh density reproof or
full audit of L918 is needed for this finite test; its coefficient/sign
interface was separately checked in L921's step211 audit.

Opened the primary author manuscript of M. Laurent, *Sums of squares,
moment matrices and optimization over polynomials*, updated 6 February
2010, https://homepages.cwi.nl/~monique/files/moment-ima-update-new.pdf.
Printed page numbers are one greater than zero-based PDF page indices.
Reread Lemma4.2(i)-(iii), printed pp54-55, including its proofs. A
representing measure through order 2t gives raw moment PSD; support in
g>=0 and t>=ceil(deg(g)/2) gives localizing PSD. The kernel-support
conclusion concerns the raw matrix, not the logarithmic H2. Use exactly
the previously justified specialization v=u^2, t=3, g(v)=v. The new boxes
do not convert these necessary conditions into a representation theorem.
No infinite-kernel ideal, flat extension or extra logarithmic row is used.

Retrieved Theorem3.12(i)-(iv), printed pp35-36, and the full statement
of Theorem3.15, printed p36. The latter applies to finite polynomial
systems f_r!=0, g_l>=0, h_j=0. Its alternative certificate is an identity
consisting of a product of even powers of the f_r, a preordering sum
of sums of squares times products of the g_l, and arbitrary polynomial
multiples of the h_j. The preordering definition (3.12) and the
certificate interpretation immediately preceding Theorem3.15 were read.
This covers the nonzero-coordinate and strict-sign cases without an
invertible block or a lower bound for |c2|. Import the named theorem by
citation; its general real-algebraic existence proof is not reproduced.
Only exact identity soundness is needed for accepting a proposed finite
certificate. No degree bound, rational-coefficient existence guarantee,
solver accuracy or finite-search completeness is imported.

Retrieved Theorem3.16, printed p37, with its immediately following
qualification: compact K and strict positivity permit a preordering
representation; nonnegativity does not have that general guarantee.
The present c2!=0 set is not assumed closed, and the target is J>=0,
including zeros. Thus that stronger-looking compact theorem does not
remove the certificate/search gap. An infeasibility certificate for the
set with J<0 is an admissible way to certify J>=0; all strict and nonzero
conditions must be retained. The future attempt must check the actual
identity and every coefficient/sign, not just invoke the theorem.

### Fixed numerical interface — inspected, not recalculated

L917 is the canonical conditional enclosure, accepted in step197 under
L037. Read its hypotheses, finite log conventions, complete-inclusion
argument and audit qualifications. L037 supplies positive interval
division. The complete fourteen endpoint strings at
`scripts/heat/low-time-h2-uniform-195.json`, JSON pointer
`/panels/0/moments`, and `/panels/0/lambda` were inspected with the shared
JSON inspector using --full. All seven saved lower endpoints are positive;
the mass lower endpoint is greater than 0.49712. The parameter interval
is exactly [0,0.0001953125]=[0,1/5120]. No certificate was regenerated.

The future fixed-box definition uses the exact rational values of those
finite decimal strings: for k=1,...,6 use the interval
[lower(M_(2k))/upper(M0), upper(M_(2k))/lower(M0)] for y_k, with y0=1.
This is precisely L037's positive interval-division specialization;
it is not a new enclosure theorem. Endpoints are not midpoint values,
and no rounded abbreviated number may replace them. Normalized
coefficients stored elsewhere also contain factorials; they are not y_k.
A later implementation must save/check the exact ratios and its source
endpoints. This review has computed none of those ratios.

The independent ratio boxes deliberately discard the shared denominator
and lambda correlations. They are necessary conditions on actual moments
through order twelve, not equality with the theta curve. The closed
panel covers all stipulated positive lambda as well as zero; do not
replace it by data at zero or exclude a box face. No parameter variable
or fitted tilt law is introduced into the finite relaxation. The local
conclusion for any actual contact remains conditional on L019/L037/L058/
L874/L917/L918 and the audited L921 coefficient interface. Decimal-library
correctness remains an inherited assumption. No new quadrature, wider
panel, higher degree, precision change or determinant run is authorized.

### Exact/stronger comparison, duplicates and failures

Reused the adequate earlier joint-row searches. New actual queries were:
`"Riemann" "Hankel" "moment bounds" positivity contact`;
`"reciprocal" "logarithmic" "Hankel" "moment" theta`;
`"Laurent" "Theorem 3.12" "3.15" Positivstellensatz`;
`"Riemann theta" "moment" "semialgebraic"`;
`"logarithmic Hankel" "contact"`;
`"Hankel" "interval moments" "positive semidefinite"`.
The primary source comparison is the Laurent text above, not a snippet.
Generic moment-problem, Hankel-transform and numerical low-rank hits do
not supply this origin inequality. Search-only recent cumulant-lifting,
quintic-obstruction and RH-project hits remain uninspected leads; no
result, applicability or novelty claim is based on them. Nothing essential
to the finite certificate test depends on these leads. Additional searches
for the standard principal-minor criterion added no input; retain the
standard real-symmetric principal-minor form of Sylvester's criterion
already used and checked in L921, rather than reprove it.

The relevant canonical statements and stops were compared. L921's exact
negative tuple concerns a relaxation expressly omitting every numerical
actual-theta bound. It does not settle this stronger premise set.
Step195/L917 loses sign in the third minor after interval propagation;
step213/L922 retains parameter correlations but still fails its fixed
determinant threshold. Neither is a contact-conditioned J test. Their
stops are preserved and neither computation is reopened. L918/step199
stops at this very necessary origin sign and does not refute every
actual-law approach. C874a/step178 has lambda in [1/4,1/2], outside the
present panel, so its empty-domain evidence cannot be transferred.
The covariance and theta-heat recurrence stops still block an automatic
sign import. No duplicate of this fixed-box joint-row test was found in
the relevant local paths. A historical stop is not a global ban.

### Decision, bounded use and limitations

EXPLORE approves coverage for one fixed-box exact certificate-or-witness
attempt after a separate approval. No inspected theorem already decides
the finite set, so no sign is imported and no novelty is asserted.
The nominated assessment specifies all raw/logarithmic PSD constraints,
normalization, all three rows, nonzero cases, J convention, certificate
and witness formats, and the inconclusive stop. Rejecting L921's old
witness is insufficient. Infeasibility would exclude only these local
d=2 contacts; J>=0 would pay only the necessary origin condition, not
W_*<=0 on the compact interval or its flux. A negative finite witness
would identify another premise gap, not an actual negative contact.

No justified new signed identity emerged to nominate as a protected
creative mechanism. This is a finite strengthening using known methods;
relabeling it creative would not meet the shared requirement. A genuinely
new central mechanism still needs a specified, source-reviewed input.
Full matching and supporting Mathlib coverage remain unchecked, not
asserted absent. No lemma, mathematical script, PROOF or DAG was changed.
Outcome EXPLORATION / LITERATURE / NOVELTY_UNCHECKED records new scope
comparison, not a mathematical advance or an informative sign result.
