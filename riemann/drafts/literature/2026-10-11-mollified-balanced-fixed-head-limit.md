# Proposed balanced fixed-head mollified coefficient

TARGET: Evaluate the fixed-N limit of B_N(H)=H^(-1) integral_[H,2H] M(t)|Z_N(t)|^2|P_H(t)|^2 dt with L395's mollifier, retaining both functional-equation diagonals and all response twists.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 71 reused the balanced leads and exclusions in 2026-10-11-mollified-fixed-head-mean.md, checked the specific L394/repeated-carrier stops and steps 62/63/70, and made two bounded fixed-rational-twist/ordinary-Hardy-jet queries; no inspected source supplies this exact response-head coefficient.
SOURCE_EVIDENCE: Directly inspected Young, A short proof of Levinson's theorem, Arch. Math. 95 (2010), 539–548, DOI 10.1007/s00013-010-0199-9, (2.1)–(2.3), Lemmas 3–7, both Lemma 5 off-diagonal orderings, Section 6 contour/residue proof and Section 7; Bui–Hall arXiv:2304.05178v1 Proposition 1 and Section 3 (6)–(8). Reused the recorded stronger BCR comparison without invoking it.
COMPARISON: Young covers the combined growing integer twists and both balanced diagonals; Bui–Hall and audited L395 cover ordinary-jet replacement. Their scalar evaluated coefficient omits the response twists. The inspected Mellin/residue method supports a fixed-prime-factor specialization attempt, not substitution of the scalar coefficient or an asserted value of B_N.
GAP: Compute the altered collision factors and their uniform small-shift asymptotic, cancel the two diagonal shift singularities, differentiate the complete coefficient and prove absolute signed-endpoint removal; the fixed-N limit and its sign remain unproved.
REASON: No essential source is missing for this bounded attempt. The changed finite arithmetic and its error proof are necessary local differences; import the analytic moment inputs and do not reprove them or repeat carrier approval.
LITERATURE_REASON: The balanced fixed-response coefficient was expressly outside step 62's approval; this gate turn compares its changed collisions, both diagonals and sharp signed endpoints using the recorded primary leads.
SCOPE: Fixed positive integer N before H tends to infinity, exponent 1/100, polynomial u^2, exact L395 ordinary jets and sharp [H,2H], all ordered response twists and both functional-equation terms; no growing N, complete signed-mean limit, sign or RH claim is preapproved.

## Proposal preserved from step 70

Essential inputs are L390's definitions, audited L395's weighted jet and
physical/tail bounds, and L396/L397's audited fixed-head carrier conclusion
for the downstream use. Write L(t)=log(2+t), f=F_0/A, and

    x=f, y=f'/L, z=f''/L^2,
    M=(z^2+3xz/2+x^2/16-y^2)/2,
    Z_N(t)=sum_(r<=N) r^(-5/2-it),
    P_H(t)=sum_(a<=H^(1/100)) mu(a)a^(-1/2-it)
                  (log(H^(1/100)/a)/log(H^(1/100)))^2.

The target includes every ordered r,s response pair and both mollifier
cutoffs, even when combined twists have gcd collisions. It concerns
ordinary height derivatives, with no derivative of the mollifier.
No cancellation, coefficient sign, RH, phase independence, common-zero
control or growing-N uniformity is assumed.

The main gap remains global actual-theta mixed positivity. A fixed-N
balanced coefficient could combine later with the vanishing carrier to
test a complete mollified signed mean. The N-to-infinity limit, its sign,
the total L367 margin and all global sign/count/RH gaps are independent
unresolved obligations; no conclusion about them is obtained here.

Reuse the recorded primary passages and compare the changed hypotheses
before retrieving more source text. Relevant existing assessment:
`2026-10-11-mollified-fixed-head-mean.md`, especially its scope and balanced
moment section. Its SPECIALIZE decision expressly authorized only carrier
reduction, so it is not an approval for this coefficient. Young's
[published paper](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf),
Lemmas 5–7 and Section 7, supplies a concrete prior lead for the twist
formula and collision comparison; Bui–Hall
[Proposition 1 and Section 3](https://arxiv.org/html/2304.05178v1#S3)
supplies the recorded scalar/ordinary-jet lead. Neither coefficient may be
substituted without checking the fixed response twists. No theorem from
an unread source is a premise. Full matching Mathlib coverage is not checked.

The separate review should continue toward a mathematical attempt only
if the exact fixed-N coefficient can be addressed with controlled o(1)
normalized error and both functional-equation contributions retained.
If an essential source range or sharp-endpoint bound is missing, identify
it rather than discarding a term. An unsuccessful bound would not decide
the signed mean. Persistent source blocking calls for another independent
target, not repeated approval of the already audited carrier. Preserve
L390's absolute-contour failure, L394's negative fixed-quadratic-weight
result and the repeated-carrier-approval stop; none settles this balanced
coefficient. No mathematics on this new target was derived in step 70.

## Completed source comparison — step 71

This literature-only EXPLORATION changes the proposal to SPECIALIZE.
Known tools support an attempt; no coefficient or new result is established.
The target remains exactly the TARGET line above.

### Inspected primary statements and proof cases

Young, [*A short proof of Levinson's theorem*](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf),
published version, pp. 540–547: Lemma 5 assumes positive integer h,k,
hk<=T^(2 theta), fixed theta<1/2, complex shifts O(1/log T), 0<=w<=1,
support [T/4,2T], and w^(j)=O_j((T/log T)^(-j)). Both diagonals use
hm=kn; the second retains X_(alpha,beta,t) and shifts (-beta,-alpha).
Its error is O_(A,theta)(T^(-A)). Both unequal-order integration-by-parts
cases were inspected. Section 6 gives the Mellin factorization and contour
shift retaining s=0 while G cancels the other candidate pole. Lemma 7's
proof uses a classical zero-free region, reciprocal-zeta bounds, residues
and Euler–Maclaurin. Section 7 normalizes the original collision factor.
Lemma 3 and the Cauchy argument after (3.4) give scalar smooth moments
and normalized shift derivatives; pp. 544–545 extend the scalar combined
error holomorphically across alpha+beta=0. Import these analytic inputs.

Bui–Hall, [*On the derivatives of Hardy's function Z(t)*](https://arxiv.org/html/2304.05178v1#S3),
arXiv:2304.05178v1, 11 April 2023, printed pp. 6–8: Proposition 1
assumes fixed polynomials P,Q_1,Q_2, P(0)=0 and 0<vartheta<4/7,
with the specified Mobius mollifier and sharp [T,2T]. Its evaluated
shifted-derivative scalar moment has O(1/log T) normalized error.
Equations (6)–(8) retain the Hardy carrier derivatives, ordinary-jet
conversion and Schwarz control. L395's audited application already keeps
the second-derivative term, constant Hardy sign and L(t)/log H distinction.
This proposition has no response head.

### Applicability and the mathematical difference still to prove

Every ordered r,s<=N and a,b<=Y=H^(1/100) has h=ra, k=sb in Lemma 5;
no coprimality hypothesis is required. For fixed N the upper bound
N^2 H^(1/50) fits the fixed theta=1/50 twist range at T=2H eventually.
The double mollifier coefficient absolute mass is O(Y), with bounded
fixed-response mass, so the source's arbitrary-power error has summation
room. This checks hypotheses; it evaluates neither diagonal nor B_N.

The attempt must form the ram=sbn collision series with both degree-two
cutoffs and compare its Euler factors with (6.2). Only primes dividing rs
have a changed valuation constraint. No changed factor is computed here:
retain nonsquarefree r,s and all gcd collisions, prove local holomorphy
and convergence, and do not substitute Section 7's scalar A(0)=1.
The scalar Lemma 7 does not state this extension. Its method is available
for the required finite arithmetic specialization, with explicit contour
tails and residue errors. That local proof is necessary because the source
coefficient has different collisions; reproving its original theorem is not.

Keep X_(alpha,beta,t), its derivatives and the reflected diagonal until
their combined shift singularity is removable. Establish uniform combined
holomorphic errors before Cauchy differentiation, initially using annuli.
Ordinary order-two jets on each side require total shift order four.
Use L395's exact conversion and weighted bounds for freezing; do not
differentiate the mollifier or change algebraic squares to modulus squares.
Young's G depends on the shifts, so its annular formula by itself is not
a derivative theorem at alpha=beta=0.

### Signed endpoints: available method, application not yet proved

Use smoothing scale T=2H so both boundary neighborhoods fit the permitted
support, while keeping the actual length Y=H^(1/100). Section 6 works with
the actual length and log Y below a fixed exponent barrier; its proof is
the available way to justify this length at doubled height. Do not replace
it by (2H)^(1/100) or assume uniformity in a moving exponent.

For width comparable to H/log H, bound the signed smoothing error by a
positive smooth boundary majorant times the three weighted jet squares.
The scalar smooth moment and normalized derivatives provide the relevant
tool; the attempt must show an o(H) boundary envelope with the actual Y,
retaining the scalar error and both endpoints. L395's whole-interval O(1)
bound alone is insufficient for vanishing boundary error. The bounded
|Z_N|^2 may enter this absolute envelope, but positivity of M is unknown.
Bracketing the signed integrand itself is invalid. No new endpoint bound
is asserted here.

### Searches, duplicates and recorded failures

Reused step 62's assessment, step 63's source recovery and step 70's
carrier audit. Their scope excludes this coefficient; no local ready
balanced evaluation was found in those specific records. L397 concerns
a different collision sum. Preserve L390's absolute-contour failure,
L394's fixed-quadratic-weight obstruction and the repeated-carrier stop.
None determines this independently testable mollified balanced target.

Reuse the stronger BCR comparison in
`2026-10-11-arithmetic-resonator-discriminant.md`: its longer unshifted
arbitrary-polynomial range gives no automatic differentiated shifted error
and is unnecessary here. The BCY cross-mollifier coefficient remains
excluded by step 62's coefficient/cutoff/polynomial mismatches.

New queries: `mollified second moment zeta fixed rational twist Mobius
polynomial Young Lemma 5 arithmetic factor`; `twisted mollified second
moment zeta finite Dirichlet polynomial derivatives Hardy function`.
They located the inspected Bui–Hall article and recorded Robles–Roy–
Zaharescu lead. Longer/different mollifiers, discrete moments and the
perturbed-moment paper remain unread leads, not inputs. A bounded search
does not establish novelty. Full matching Mathlib coverage is not checked.

### Continuation/abandonment test

Approve one mathematical attempt at the unchanged fixed-N limit. Continue
this method only with evaluable complete arithmetic, uniform small-shift
o(1) normalized errors and absolute o(1) endpoint error. Stop the method
if a retained diagonal, contour tail, shift-extension or endpoint error
stays order one or larger; preserve the failure without deciding the mean
or dropping a term. No essential source blocker remains in the selected
analytic tools. Further unchanged source approval is unnecessary.

The main gap remains global actual-theta mixed positivity. A future
balanced evaluation could combine with L397's vanishing carrier to test
a complete fixed-head signed mean. Passing N to infinity, its complete
sign, the total L367 margin, eventual physical discriminant sign and actual
common-zero upper bounds remain separate gaps. No RH, growing N,
simplicity, disjointness or phase independence is used.
