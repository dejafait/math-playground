# Negative discriminant set — proposed quantitative target

TARGET: Determine whether the actual physical discriminant satisfies meas{t in [H,2H]: D(t)<0} >= c H/(log H)^2 for some c>0 and all sufficiently large H, using L388 and unconditional fourth-moment bounds for ordinary critical-line jets through order two.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched unconditional fourth moments of zeta derivatives through order two, Conrey's general polynomial theorem, and negative-discriminant/Wronskian measure terminology; checked local moment assessments and total-assembly histories. Retrieved Conrey's primary PDF and readable Bui–Hall primary statements and essential derivative/sign-set proof cases. No matching full physical-discriminant measure theorem was established by this bounded search.
SOURCE_EVIDENCE: H. M. Bui and R. R. Hall, On the derivatives of Hardy's function Z(t), arXiv:2304.05178v1 (11 April 2023), Theorem 3 and its preceding defining asymptotic, Proposition 3 in Section 4.2, (7), (3)–(4), Sections 5–7, https://arxiv.org/html/2304.05178v1; Conrey, Q. J. Math. 39 (1988), 21–36, DOI 10.1093/qmath/39.1.21, introductory theorem/(7), Section 2 and proof endpoint cases (69)–(83), https://aimath.org/~kaur/publications/15.pdf, with OCR qualifications below. Read L370/L388, L366 (1)–(2), L367 jet definitions/(9), L368 (3)–(7), L380 (3)–(4), and L369 (6) and exact carrier formulas; reused prior Holder coverage.
COMPARISON: Bui–Hall's unconditional fixed-order Hardy fourth moments and small-complex-shift theorem cover the required critical-line derivative orders and sharp interval. Their sign-set inequality covers the concentration mechanism, but their Hardy-product sign theorems do not state this physical-discriminant conclusion. Conversion of the complete actual jets and an O((log H)^4) second-moment bound for Delta remain a separate application.
GAP: Prove the complete normalized second-moment budget, including ordinary order-two jets and the common envelope, then apply the known sign-set inequality with audited L388. The physical negative-set threshold, eventual D<=0, positive-part control and common-zero counts remain unproved.
REASON: Essential derivative, sharp-interval and sign-set source coverage is now adequate for one later REPRODUCTION specialization; import known moments and Cauchy–Schwarz rather than reprove them. No physical-discriminant estimate or new lemma is derived in this literature turn.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changes from one negative point to a quantitative measure bound and requires an essential unread fourth-moment derivative theorem; prior Young second-moment coverage does not suffice.
SCOPE: Fixed actual F_0,G,A of L366/L368/L380, L370 physical D and Delta, positive sharp [H,2H], unconditional jets through order two; no growing regulator or new zero hypothesis.

The main gap remains global actual-theta mixed positivity, with the
total L367 pencil margin and actual common-zero upper counts also open.
This proposed intermediate target tests whether L388's negative mean
can be confined to very small height sets. A quantitative size bound
could constrain such concentration in later discriminant arguments.
It would still supply neither eventual D<=0 nor positive-part control,
and would not locate points on the response grid or bound common zeros.

Essential local inputs for a later attempt are L388 and L370, with
the unchanged actual functions from L366/L368/L380. A possible source
lead is an unconditional fourth-moment upper bound for zeta derivatives
through order two (or an adequate complex-shift bound). This is an
unread lead, not an imported result. The next review must retrieve
primary hypotheses and essential derivative/endpoint cases, check
duplicates and obstructions, and compare the complete second-moment
budget for Delta with the proposed O((log H)^4) scale. No such budget
or implication has been proved in this proposal.

Continue only if the complete fixed-function bound and measure argument
have adequate source coverage at the proposed scale. If a missing jet,
weight or endpoint case prevents this, record the specific deficiency
before dependent calculation. Failure of this upper-bound certificate
would not disprove the measure target. Do not reopen persistently
blocked arbitrary sharp-Hardy access or treat its restricted companion
theorem as this input. The source and response-grid stops remain intact.

No RH, simplicity, noncoincidence, independent phases, eventual D sign
or common-zero count bound is assumed. Global positivity, low indices,
heights above forty and endpoint arithmetic margins remain unresolved.
Full matching Mathlib coverage is not checked. The preceding paragraphs
preserve the original pre-review proposal. The completed review below
supersedes its missing-coverage statements; the mathematical claim itself
remains unproved.

## Completed primary-source comparison — step 40

This is a LITERATURE / KNOWN_IMPORTED source-coverage advance, not a
new mathematical discovery. The exact TARGET is unchanged. No lemma,
mathematical script, DAG edge or argument in PROOF.md is added.

**Readable primary coverage.** Bui–Hall, *On the derivatives of Hardy's
function Z(t)*, the fixed [arXiv v1](https://arxiv.org/html/2304.05178v1)
dated 11 April 2023 (published in Bull. London Math. Soc., DOI
[10.1112/blms.12859](https://doi.org/10.1112/blms.12859)), defines the
ordinary Hardy function by its gamma phase. Theorem 3 and the defining
asymptotic immediately before it give the fourth product moment for
fixed nonnegative derivative orders k,l,m,n, with scale
T(log T)^(k+l+m+n+4) and error O(T(log T)^(k+l+m+n+3)). Its conclusion
is unconditional. Taking all four orders equal covers orders zero,
one and two; no growing derivative order is licensed. Theorem 1's
3/25 sign proportion is for ZZ'', not D, and is not imported for D.

Read Proposition 3 (Section 4.2): the sharp [T,2T] four-zeta-shift
integral has a bounded four-dimensional exponential integral main term
at scale T(log T)^4 and error O(T(log T)^3), uniform for each complex
shift O(1/log T). Read (7), Section 5's holomorphic Cauchy-contour
paragraph and Section 7's Theorem 3 deduction. The proof takes fixed
orders on contours of radius comparable to 1/log T. These are adequate
derivative and endpoint cases. Proposition 3's proof is explicitly
omitted by the authors; their Theorem 3 proof uses it, rather than a
conjectural moment formula. No mollifier is needed for this input.
Read the complete sign-set Cauchy–Schwarz deduction (3)–(4), including
its required sign of the first integral and positivity of the squared
integrand. Its application to Delta is still to be written locally.

**Older primary source and extraction qualification.** J. B. Conrey,
*The fourth moment of derivatives of the Riemann zeta-function*,
Q. J. Math. Oxford (2) **39** (1988), 21–36, DOI
[10.1093/qmath/39.1.21](https://doi.org/10.1093/qmath/39.1.21),
[author-hosted PDF](https://aimath.org/~kaur/publications/15.pdf):
retrieved the introductory polynomial theorem and derivative-moment
definition (7), pp. 21–22, Section 2's fixed-polynomial and variable-log
discussion, pp. 26–29, and the endpoint/variation proof cases
(69)–(83), pp. 33–35. This is a stronger classical derivative-moment
lead, not a new result. The browser extraction corrupts mathematical
glyphs, including rendering zeta as xi and losing parts of constants;
screenshots returned placeholders, and the shell PDF download failed
at DNS. No unread image or corrupted coefficient is treated as evidence.
The ready coverage relies on the legible Bui–Hall theorem and its proof
cases instead. Exact reconstruction of Conrey's coefficient is unnecessary
for this upper-bound application and is not a pending essential blocker.

**Local applicability and remaining specialization.** L380 fixes
f=-exp(i phi)zeta(1/2+it) as a real function. Its phase is that of
p Gamma(1/4+it/2) pi^(-1/4-it/2), where p>0; compare it with
Bui–Hall's Hardy definition, retaining any constant branch sign. The
research turn must explicitly justify this identification for ordinary
derivatives. Orders are fixed at j=0,1,2 throughout.

The existing physical jets are P_j=F_0^(j)/(A L^j) and
V_j=G^(j)/(A T^2 L^j), not derivatives of divided functions. L366 (2)
and L367 (9) already bound every V_j uniformly. L368 (3)–(5) retains
the full complex polynomial b and the complete right-line series through
two derivatives; finite-head substitution is unnecessary. L370 (3)
is the zero-safe exact polynomial in these jets, including the entire
common envelope. A prospective implementation may use that identity
directly, or L370 (4) with g=G/A and its entire curvature correction.
Neither implementation may replace g by G/(AT^2) inside differentiated
minors without restoring the derivatives of T^2.

The later calculation must bound the normalized physical P_j fourth
moments by the known fixed-order Hardy moments, retaining A'/A and
A''/A. The exact gamma modulus formula, controlled digamma input and
full q estimate are available in L366/L368/L369/L370; a gamma-only
curvature is not the common-envelope curvature. On [H,2H] compare
the pointwise L=log(2+t) with the source's log H using bounds on the
entire interval; do not differentiate a normalized jet as though its
divisors were constant. Closed endpoints have measure zero for these
integrals. Cumulative moments can be restricted by nonnegative
integrands; a sharp signed subtraction of two asymptotics is not needed
for an upper bound. No extra sharp-weight theorem is required.

The discriminating test remains the proposed complete budget
H^(-1) integral_[H,2H] |Delta|^2 dt = O((log H)^4). This is a target
scale, not a result proved by this review. The known sign-set method
should then be applied to -Delta with the full L388 negative first
mean, whose coefficient is strictly positive after negation and whose
error is o(log H) for all H. Continuity gives measurability; no zero
division, RH, simplicity, phase independence or disjointness is needed.
The resulting physical measure claim, if established, must be stored
with its full application proof in a canonical lemma in a research turn.

**Duplicates and recorded stops.** Narrow searches of the October
total-assembly, signed-residual, derivative-square and Wronskian
assessments/histories found no completed quantitative D-negative-set
result. The September 26 fourth-moment target concerns an atomic
weighted rational grid, a different object; its failed sampling budget
is not an obstruction to this continuous-height moment. The earlier
Bui–Hall comparison in the October 8 noncommon-Wronskian assessment
already distinguished Hardy sign sets from common-free localization.
That warning remains: a size bound for D<0 supplies no grid visit,
common-free Wronskian zero or common-zero upper count. The sharp-Hardy
source stop and the grid/phase-return stops remain preserved; none is
reopened. Exact-discriminant searches produced unrelated algebraic
discriminants, not a matching theorem. Failed searches prove no novelty.

**Decision and continuation test.** SPECIALIZE approves only this
fixed-function target and its ordinary-jet concentration application.
Continue with a separate mathematical turn after supervisor approval
if all jet conversions meet the stated complete second-moment scale.
Stop this certificate if a retained term exceeds that scale, identify
the term and achieved budget, and do not interpret certificate failure
as a disproof of the measure target. Even success leaves the main
mixed positivity, total pencil margin, eventual D<=0, positive-part
control, common-zero upper counts, low indices, heights above forty
and endpoint arithmetic margin unresolved. No RH candidate follows.

**Mathlib.** Reuse the inspected supporting Holder documentation in
`2026-10-08-wronskian-signed-mass.md`; it is inequality support only.
Full matching derivative-moment or physical-discriminant coverage is
not checked. No Lean verification or claim of library absence is made.
