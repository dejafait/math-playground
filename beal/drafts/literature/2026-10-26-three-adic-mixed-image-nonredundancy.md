# Local mixed-image nonredundancy test at 3: source assessment

TARGET: Determine whether the norm-trivial part of λ_B(Jac(B)(Q_3)) is contained in λ_E(E(Q_3)), or certify a class outside that image.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the L143 representation/audit and odd-prime Stoll coverage in the 11-adic assessment; searched local Tate-dual isogeny images, Prym norm/Kummer images, unramified double-cover descent and the actual quartic coefficients. Inspected general primary results below; no inspected theorem evaluates the requested two images for this instance. This is no novelty claim.
SOURCE_EVIDENCE: Bruin–Stoll, Two-cover descent on hyperelliptic curves, author manuscript dated 14 March 2008, Section 2 p.3 and Section 4 pp.6–10, including Lemma 4.4/proof, SquareClasses and LocalImage with branch, reciprocal-chart and termination explanations; Stoll, Acta Arith. 98 (2001), Lemmas 4.1,4.3,4.4 pp.250–251 and reused Section 6 coverage; Bruin–Poonen–Stoll, 74-page manuscript, Remark 6.5/Definition 6.7 p.16 and Section 6.3/Proposition 6.10 pp.17–20, reusing the audited proof; Schaefer corrected arXiv:1507.08325v1 Proposition 2.7/proof pp.9–10; Tate, ICM 1962 proceedings, Theorems 2.1–2.5 pp.289–290 and their proof discussions; Bruin arXiv:math/0408069v2 Proposition 2.2/proof pp.4–5. Exact links and applicability below.
COMPARISON: Known theory supplies a local coefficient interface and complete finite image algorithms, stronger than point sampling. Tate duality pairs dual cohomology groups, and Bruin identifies the Prym factor; neither inspected statement identifies this norm kernel with this elliptic image. A source-covered computation can decide the instance without a new general descent theorem.
GAP: Certify the Q_3 specialization and coordinate transport, complete local factorization and square-class arithmetic, the normalized elliptic image and sufficient Jacobian image coverage, then perform the norm-restricted finite comparison. No containment, mismatch, local dimension or new rank bound is computed in this literature turn.
REASON: Essential coverage is ready for one bounded specialization of known algorithms on the unchanged target, subject to the supervisor's separate approval of this changed assessment. The result would be local certification of known theory; its extra content over the norm condition remains unproved.
LITERATURE_REASON: The saved target had REVIEW_REQUIRED: its changed Q_3 hypotheses and complete elliptic-image comparison were outside the completed Q-rational L143 audit and the fixed 11-adic test.
SCOPE: Only the actual L110/L111/L142 curves, origins and maps over Q_3 and the L143 quartic coefficient quotient, with L138's odd model as needed; bounded algorithm and stop criteria below. No global class enumeration, rank claim, Abel-image sufficiency, other prime or rational-point classification.

## Exact proposed test and relevance

Use B: W²=11(T²−4)Q4(T) with q_+=(2,0) and
E: R²=−33Q4(T) with O_E=(2,165), where
Q4(T)=7+52T−6T²−64T³−25T⁴. Put k=Q_3 and
A_4,k=k[T]/(Q4). The proposed coefficient target is
A_4,k*/(k* A_4,k*²). Use the degree-zero divisor evaluations λ_B,
λ_E of L143 after verifying their local specialization. Norm-trivial
means that a representing quartic element has square norm in k.
The source review must check this convention in the scalar quotient.

The test asks whether an actual local B divisor class with that norm
property can fail to match *every* local elliptic coefficient class.
It compares genuine separate divisor-class images; it does not impose
the exact same-T point equations that made ATTEMPTS/062 automatic.
It does not revisit the saturated real or 11-adic quotients.

One certified mismatch would demonstrate content beyond a scalar norm
condition and motivate a later test on globally supported classes.
It would not itself exclude any global class: global realizability,
compatibility with L140/L141 and the retained marking would still
need proof. Conversely a theorem or complete local-image calculation
giving containment would stop this particular extra local filter.
Sampling points without complete image control cannot certify
nonmembership, and absence of a sampled mismatch cannot certify
containment. No mismatch or containment is asserted here.

## Original source-review plan, retained from the proposal

Search the exact containment and stronger descriptions under local
Tate duality, norm maps for unramified double covers, split Prym
isogenies and local fake-descent images. Check whether the condition
is already precisely the usual norm obstruction. Retrieve the primary
hypotheses and essential proof case of any applicable theorem; do not
infer the answer from finite-module dimensions or abstract isogeny
degrees alone. Reuse the generalized descent and rational-cycle
sources already assessed, reading only what changes over k.

If a theorem settles the target, select IMPORT and retain its exact
local hypotheses. Otherwise specify the source-covered finite image
test and its completeness criterion before approving calculations.
Missing essential coverage keeps this assessment REVIEW_REQUIRED or
SOURCE_BLOCKED. This proposal approves neither the local comparison
nor a creative exclusion mechanism.

Essential inputs are audited L143/L142/L127 for the embedded maps and
Q-interface, L110/L111/L113 for the actual models, and L138 for any
odd-model transport used. L140/L141 are downstream comparison filters,
not assumed product-image inputs. No cross-notebook theorem is used.
Remaining obligations include mixed global nonredundancy, complete
descent, Abel-image membership, point control, integer recovery and
the other primitive Beal signatures. Mathlib coverage for the proposed
local-image statement has not been checked.

## Completed source comparison — 2026-10-26, step 516

Recorded discovery queries included `local descent hyperelliptic p odd
complete image algorithm Stoll Bruin elliptic norm Prym local Tate duality`,
`Schaefer local descent images isogeny orthogonal complements Tate duality
explicit descent`, `"Prym" "local" "Kummer" image norm`,
`"unramified double cover" "local" "descent" "norm"`,
`"7+52T" "64T" quartic`, and `"norm-trivial" "Prym" "local" image`.
The inspected applicable results are listed below; searches supplied no
exact-instance containment theorem. Irrelevant search hits were not used.

The precise main gap remains control of residual primitive signatures;
this local target only asks whether a possible descent filter has content.
The current rank bound still misses the sufficient bound one by eight.
The intermediate output sought is an exact local inclusion decision, or
one actual norm-trivial B class with certified elliptic nonmembership.
Only a mismatch would justify later testing on globally supported classes.
Containment would stop this filter at 3. An incomplete computation settles
neither alternative. No global inference is approved by this assessment.

### Coefficient interface and norm convention

Reuse the accepted L143 audit and its representation assessment. The
[Bruin–Poonen–Stoll manuscript](https://math.mit.edu/~poonen/papers/genus3.pdf),
*Generalized explicit descent and its application to curves of genus 3*,
Forum Math. Sigma 4 (2016), e6, DOI 10.1017/fms.2016.1, treats a nice
variety over a field k. Definition 6.7 requires n invertible in k and
nonempty finite étale Δ; it is not restricted to number fields. Thus
k=Q_3, n=2, and the unchanged separable quartic are within its scope.
The audited divisor identities and finite pairings must be transported,
not replaced by an assertion based only on isogeny degree. No new
polarization identity is needed for the coefficient route.

Remark 6.5 moves cycles off the bad supports; Proposition 6.10 and (8)
compare their evaluations with cohomology in the scalar quotient. Its
proof uses the equivariant cycle pairing and exact rows, so its field
hypotheses do cover Q_3. The earlier full proof review is reused, with
the fake-datum definition, moving case and relevant diagram rechecked.
[Schaefer's corrected version](https://arxiv.org/pdf/1507.08325v1),
*Computing a Selmer group of a Jacobian using functions on the curve*,
Math. Ann. 310 (1998), 447–471, Proposition 2.7/proof, explicitly includes
the completion case. The actual rational base points supply index one.
These are theorem applicability checks; the Q_3 instance of L143 still
belongs in the mathematical certificate, rather than being silently
added to its Q-only lemma here.

Use the algebra of Q4, not of a polynomial with an unrecorded twist.
Bruin–Stoll's Section 2 defines norm constraints on the even-degree
square-and-scalar quotient. Degree four is therefore the relevant
source convention. The mathematical attempt must compute the induced
norm map and quotient the full diagonal Q_3* image, keeping valuation
and residue bits. In particular the source's raw point map μ for E has
the leading-coefficient norm coset; the requested λ_E is its degree-zero
normalization by μ(O_E). The raw coset must not be compared to λ_B.
Likewise L138's odd-model full norm kernel has no scalar quotient.
Projection, actual η transport and normalization must be certified before
using it as a source for λ_B. No local norm value is evaluated here.

### Complete local images available from primary algorithms

[Bruin–Stoll, *Two-cover descent on hyperelliptic curves*](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
Math. Comp. 78 (2009), 2347–2370, DOI 10.1090/S0025-5718-09-02255-8;
the inspected 19-page author manuscript is dated 14 March 2008.
Section 4 assumes a characteristic-zero complete discretely valued
field with finite residue field, an integral squarefree f, and its full
irreducible factorization. These assumptions include the actual quartic
E over Q_3; smoothness comes from the recorded model, not good reduction.
Section 2 includes even-degree branch and infinity values. Lemma 4.4
provides a disk precision criterion for constant factor square classes.
Its proof and both recursion cases were read: ordinary disks have fixed
nonzero factor classes; a remaining linear-factor neighborhood is covered
by its pre-recorded branch value. LocalImage separately covers integral
coordinates, the reciprocal chart and rational infinities. Its final
explanation gives equality with the entire point image, after the scalar
quotient. Thus it applies to all E(Q_3), whose points also represent all
elliptic degree-zero classes using the given origin. This algorithm does
not, for genus two, claim that base-field curve points generate Jac(B).

For B reuse the inspected odd-prime coverage in
`drafts/literature/2026-10-26-pair-eleven-adic-filter.md`, with its fixed
11-adic candidate restrictions replaced only for this newly assessed
target. [Stoll, *Implementing 2-descent for Jacobians of hyperelliptic
curves*](https://www.impan.pl/shop/en/publication/transaction/download/product/83397),
Acta Arith. 98 (2001), 245–277, DOI 10.4064/aa98-3-4, assumes monic
integral squarefree odd-degree f. L138 supplies exactly that model.
Lemmas 4.1 and 4.3 identify the full Kummer map and branch-factor values;
Lemma 4.4(1) gives dimension m−1 at any odd local prime, including bad
reduction, where m is the number of irreducible local factors. The
statements and proof/reference cases on pp.250–251 were rechecked.
Use the theorem directly, not a new proof from formal groups. Reaching
that dimension with actual divisor images certifies a complete image
before projection; rational two-torsion need not itself survive mod 2.
The source's Section 6, pp.267–272, permits degree-at-most-genus divisors
and extension fields. Its prior proof review is reused; a degree-one-only
search that falls short must remain incomplete. Odd-residue local square
criteria and Hensel coverage are also reused from the 11-adic assessment.

### Duality and Prym comparisons: scope limits

[Tate, *Duality theorems in Galois cohomology over number fields*](https://math.stanford.edu/~conrad/BSDseminar/refs/TateICM.pdf),
Proc. ICM Stockholm 1962 (1963), 288–295, Section 2, Theorems 2.1–2.5
and proof discussions pp.289–290, supplies finite-module and abelian
local duality. Theorems 2.4–2.5 have integral/unramified or abelian-scheme
hypotheses. They cannot be applied to the present bad-prime image merely
because 2 is invertible. Their conclusions concern dual objects; none
states the requested inclusion between these two separate coefficient
images after a quartic norm restriction. No orthogonality identification
of the actual embeddings, or automatic containment, is inferred here.

[Bruin, *The arithmetic of Prym varieties in genus 3*](https://arxiv.org/pdf/math/0408069v2),
arXiv:math/0408069v2, 31 May 2006, Section 2.2 Proposition 2.2/proof
pp.4–5, identifies the split Prym by actual pullbacks. This is already
used by L127/L142. Its statement is not a computation of local rational
images of the norm or connecting maps. Rechecking it revealed no direct
answer to the norm-restricted image question. Fisher's elliptic
local-duality Lemma 2.4, found in search excerpts but not independently
read in its primary PDF, is a narrower unread lead, not a
substitute for the actual product embeddings. Schaefer–Wetherell's
isogeny-to-Jacobian algorithm remains an unread alternative; it is not
essential because the two inspected image methods give an independent
complete-image route. No absence-of-theorem or novelty claim is made.

### One bounded mathematical attempt prepared for separate approval

Keep TARGET verbatim. First certify the local coefficient interface,
full factorizations and exact square-class models for all algebra factors
and diagonal scalars. Use Hensel/Newton or exact local-field certificates,
not factorization modulo 3 alone. If this cannot be certified, stop before
an image exclusion. Retain all original curve constants and origins.

For E implement the cited disk method with complete branch and reciprocal
charts; record every split and terminal cell, its solvability evidence
and constant-image precision inequality. For B begin with the actual
branch-factor divisor values and, if needed, degree-one witnesses with
rational X=a/b, |a|<=12 and 1<=b<=12, on the odd model, proved to exist
by the local square test. These are only lower-image witnesses. This
bounded first attempt does not open an extension-field or unbounded
point search. Certify the full B image only if its pre-projection span
attains m−1; otherwise record the actual/required dimension shortfall.

Cap the elliptic recursion at 4096 processed cells and depth 24 in each
chart. These are workload stops, not asserted sufficient mathematical
precision bounds. Preserve the frontier and failure reason if either
cap is reached; do not treat an unfinished tree as complete. Exact field
arithmetic or available backend failure is also a stop, not a reason to
retry the parked backend routes or invoke a service/API key.

A mismatch requires an actual B divisor class (or a specified product
of actual classes), square norm, and nonmembership in a certified complete
E image modulo all scalars. Full B coverage is unnecessary for that
direction. Containment requires full B coverage and verified elliptic
representatives for every norm-trivial projected class; a smaller
elliptic witness subgroup suffices only if it already covers them all.
Never infer either conclusion from a deficient span on the side needing
an upper bound. Compare the images as subsets in precisely the same
finite quotient and save representatives and full membership evidence.

Scripts, if used next turn, must save a full certificate and independent
replay evidence in `scripts/pair-genus-two/`, printing actual/required
image dimensions, terminal/frontier counts, the inclusion or mismatch,
failures and artifact paths. No such script or result is written now.
Any nonredundancy is local only: global realization, compatibility with
L140/L141, Abel membership, point control and integer recovery remain
unresolved. Existing ATTEMPTS/062 and the saturated real/11-adic stops
remain intact. No duplicate of this complete 3-adic comparison was found
in the specific current input files searched. Full matching Mathlib
coverage was not checked; that is not evidence of absence.

This is routine specialization of established descent algorithms. A
creative global exclusion has no justified bounded target yet because
the needed mixed nonredundancy is precisely what this test must decide.
No new theorem, local calculation or mathematical script is produced by
this source review. The original proposal and its prior REVIEW_REQUIRED
state are recorded in history/515; this changed ready assessment requires
the supervisor's separate approval before its mathematical invocation.
