# Hardy-translate error relative to its Gram form — completed source comparison

TARGET: Assess whether L637's complete signed moment remainder admits an o((log T)^5) bound relative to the actual Hardy-translate Gram form, uniformly over finite complex atomic measures and T<=X<=2T, including nearly coincident shifts.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded exact/Gram-relative/coalescing-shift searches; checked L637 Section 4 and its absolute-budget stop, the prior signed-window and two-height source assessments, L473 Section 1 and the distinct full-arithmetic-Gram failure. Query register and precise comparisons below. No matching unrestricted relative theorem identified; no novelty or absence claim.
SOURCE_EVIDENCE: Hughes--Young arXiv:0709.2345v2 Thm 1.1/(16)--(17), pp. 4--5; bramble_trace paper 36 displayed v4 Sections 8.1--8.4, Lemmas 9.1--9.5, Thms 9--10/(45a)--(49) and Cor. 11/(51)--(60), including complete relevant proof cases; Bettin arXiv:1111.0925v1 Thm 1 p. 2 and small-shift completion pp. 9--10; Hartmann--Lesch DOI 10.4171/DM/1060 Section 3 and Appendix A.2/(A.5)--(A.8), pp. 20--21. Details and qualifications below.
COMPARISON: Uniform absolute holomorphic remainders and degree-restricted errors relative to a leading fourth-moment kernel are available; individual translated-square transfer is available. None controls the complete error relative to the actual second-moment Gram form for arbitrary atom counts and coalescence. A fixed two-atom divided-difference test has source tools, but is not executed or established here.
GAP: The unrestricted inequality remains unproved. Its numerator needs cancellation-sensitive source and curvature estimates and its denominator needs actual-Gram control; polynomial degree-dependent constants and positive mixtures do not close these obligations. A bounded two-atom continuation is separately nominated.
REASON: Complete the changed-norm literature gate with a concrete coalescing two-atom test; do not infer failure of the actual remainder from the TV stop. Newly nominated continuation requires separate scope approval. No source-access blocker remains for that bounded test.
LITERATURE_REASON: The proposed error norm and uniformity over arbitrarily ill-conditioned finite translation dictionaries lie outside L637's ready absolute-error assessment; essential changed-target coverage is missing.
SCOPE: Source comparison only, retaining L637's exact w,T,X,L,Z,W, unnormalized finite complex translations and complete six-term main expression. No new window, amplifier, shift range, fixed-square surrogate or discarded completion term.

## Original exact question, retained

Retain all the hypotheses and definitions of L637, including L=log T,
fixed nonnegative smooth w, T<=X<=2T and

    mu=sum_j c_j delta_(s_j),   s_j in [-1,1],
    U_mu(t)=sum_j c_j Z(t+s_j/L),
    G_(T,X)(mu)=integral w((t-X)/T)|U_mu(t)|^2 dt,
    E_(T,X)(mu)=integral w((t-X)/T) W(t)|U_mu(t)|^2 dt
                                      -M_(T,X)(mu).

M is exactly L637 (18)--(19), with its complete holomorphic six-term
continuation, exact Hardy phase and derivative operator. The completion
curvature in W remains in E. The proposed threshold, not an estimate, is

    |E_(T,X)(mu)| <= eta(T) (log T)^5 G_(T,X)(mu),
    eta(T) -> 0,

uniformly over X and all such finite measures. Atom counts, coefficients
and locations may depend on T,X. Coincident atoms are combined as in
L637; nearly coincident atoms remain allowed. If G vanishes, the proposed
inequality requires E to vanish. No Gram eigenvalue lower bound or TV
bound is assumed. The power five is a proposed normalization to assess,
not a proved sufficient threshold for pointwise signs or asymptotic of G.

Main gap: actual-Xi initial pointwise signs at unbounded heights and
all-degree mixed positivity. A relative theorem could remove the TV
amplification from transfer of finite-observer moment formulas. Density
or realization of the microscopic bump, signed |W|-weighted approximation,
a useful main-term margin and error small enough for that margin remain
independent obligations. The proposed estimate alone implies none of
these without further proof.

## Bounded source test

Search the exact relative-form statement, covariance/Gram-normalized
moment terminology, stronger operator estimates and near-coincident-shift
obstructions. Reuse the ready absolute-moment coverage; read primary
hypotheses and relevant proof cases for the changed norm obligation.
Relevant local inputs would be L637 and L622, with L465's phase estimates
through them. Other full-Gram assessments are contrasts unless used.
No cross-notebook input is nominated; Mathlib coverage is unknown.

Entrywise estimates, fixed atom counts, separation assumptions or losses
of an inverse Gram eigenvalue do not settle the proposed uniform bound.
Record any such restricted result precisely and explain what it can test.
Do not divide L637's TV bound by G without a proved comparison or infer
a true-error lower bound from its absolute-envelope obstruction.

The review should identify an applicable theorem, approve one bounded
test with all source inputs, or park this exact mechanism for a specified
obstruction/source gap. A possible discriminator is the generalized
error/Gram quotient along nearly coincident finite translation atoms;
no quotient limit, high-derivative interchange or bound is derived or
approved here. Generic matrix countermodels alone cannot refute the
actual Hardy kernel. Persistent failure needs an independently testable
mechanism, not renewed TV accounting.

The preceding bounded-source-test description was the startup nomination.
It authorized only this literature step, not a mathematical derivation.
The completed comparison follows; no mathematical exploration counter is reset.

## Completed comparison — 1 November 2026

The main gap and proposed o(L^5)G threshold above are unchanged. This
review supplies no relative estimate and no pointwise sign information.
The local comparison is new coverage for the changed norm, not new
mathematics beyond the inspected sources. Mathlib matching coverage is
not checked; no absence claim is made.

### Primary theorem scopes and the relevant proof cases

1. **Absolute shifted moment.** C. P. Hughes and M. P. Young,
   *The twisted fourth moment of the Riemann zeta function*, J. reine
   angew. Math. 641 (2010), 203--236,
   [arXiv:0709.2345v2, Theorem 1.1/(16)--(17), pp. 4--5](https://arxiv.org/pdf/0709.2345v2#page=4).
   Coprime h,k obey hk<=T^(2/11-epsilon); all four complex shifts are
   O(1/log T). The nonnegative smooth weight is supported in [T/2,4T],
   with fixed derivative bounds O_j(T0^(-j)) and
   T^(1/2+epsilon)<<T0<<T. The complete six-term main expression has
   absolute error O(T^(3/4+epsilon)(hk)^(7/8)(T/T0)^(9/4)). Read the
   p. 5 holomorphy remark: singular terms cancel only in the full sum,
   with CFKRS Lemma 2.5.1 cited for its integral representation.
   Reuse L637's already assessed h=k=1, T0=T, epsilon=1/100,
   exact-phase/complex-weight application via L622. No reproof of this
   arithmetic theorem is needed. Its statement does not provide a norm
   estimate for a sum over translation atoms. Cauchy derivative bounds
   remain absolute bounds until an appropriate denominator is controlled.

2. **The closest norm-relative result.** bramble_trace,
   *Signs and uniform filtered positivity in fourth moments of Hardy's
   function*, [paper 36, displayed v4, 21 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/36),
   Sections 8.1--8.3, Theorems 9--10, Lemmas 9.1--9.5 and
   (40)--(49). These are manuscript theorem inputs, not independently
   certified by this review or by the accompanying finite controls.
   For nonnegative nonzero fixed w in C_c^infinity((0,1)),
   0<delta<1/13, T<=X<=2T, T^(12/13+delta)<=H<=T and real
   polynomial P of degree <=d, set V=p+(d+1)^2. The arithmetic
   main expression differs relatively from its positive leading kernel
   B_t^+(P) by O((V/L)^2), provided CV/L<=1/2, in (45a).
   The complete source remainder is controlled separately by (46)--(47):

       eta_T << T^(-1)+T^(3+sigma)/(H^(13/4)L^4),
       relative source cost <= C(2p+1)(2p+1)! V^2(d+1)^2
           (2+sqrt(5))^(2d)(d!)^2
           exp(O((p+d+1)/L)) eta_T.

   Theorem 10 requires p+d<=13delta L/(32 log L) and
   V<=L/omega(T), omega(T)->infinity. Its relative denominator is the
   window average of B_t^+(P), not the actual unweighted translation
   Gram form G in this question. Theorem 9 permits fixed p and
   d<=L^(1/2-epsilon), 0<epsilon<1/2.

   Read the load-bearing cases: common invariant expansion and finite
   coefficient extraction (40)--(43); uniform sine spectrum and
   polynomial tail cutoff in Lemma 9.2; ordinary derivative including
   endpoint values and the primitive identity in Lemma 9.4; odd
   first-pair allocations vanish, while even allocations retain the
   signed kernel with lowered order in Lemma 9.5. Its derivative cost
   depends on V and is used before absolute values. In Section 8.3,
   the source itself stays on fixed microscopic circles; exact-phase
   replacement contributes to eta_T, and Cauchy factorials plus
   coefficient coercivity give (47). These restrictions cannot be
   dropped for an arbitrary exponential sum just because its individual
   frequencies lie in [-1,1]. No uniform derivative estimate for that
   unrestricted class is stated or derived here.

3. **Actual translations, with a different quantifier.** The same
   source's Corollary 11/(51)--(60), Section 8.4, fixes p and assumes
   |h|<=13delta/(10240e log log T), with the same window hypotheses.
   It gives relative error O((log log T)^(-2)) for the single-square
   integral of the order-p Laguerre expression times Z(t+h)^2,
   relative to its explicit positive profile J_p(hL). Read the full
   proof: raw-derivative L4 estimate (55), finite Taylor replacement
   with signed-integral control (56), fixed-circle source error (58),
   explicit-main large contour and clustered denominators, and the
   diagonal exponential kernel/primitive comparison (59)--(60).
   The closing qualification expressly covers positive mixtures of
   squares, not arbitrary signed linear combinations of translated
   values. Thus this is relevant overlap, not an import of the target.
   It does not identify L637's exact E or its actual second Gram norm.

4. **Actual second-moment input for a bounded test.** Reuse the saved
   scope in `2026-10-28-two-height-hardy-jet-moment-coverage.md`,
   especially its shifted-second-input section, and the conversion
   in L473 Section 1/(4)--(6). Refreshed Sandro Bettin,
   *The second moment of the Riemann zeta function with unbounded
   shifts*, Int. J. Number Theory 6 (2010), 1933--1944,
   [arXiv:1111.0925v1, Theorem 1, p. 2](https://arxiv.org/pdf/1111.0925v1#page=2)
   and the pertinent small-|Im(a-b)| completion, pp. 9--10.
   For complex a,b with Re a,Re b=O(1/log Y), c=a-b, its primitive
   to height Y is the integral of the complete bracket

       zeta(1+c)+zeta(1-c) chi(1/2+a+it)chi(1/2-b-it),

   with error O((sqrt(Y)+sqrt(|Im a|)+sqrt(|Im b|))log^2 Y).
   The theorem specifies the full limiting bracket at c=0. Only
   |a|,|b|<=C/log T with Y comparable to T is relevant here; the
   large-imaginary-shift range is unnecessary. The small-shift proof
   uses its chi comparison away from small shifted heights and
   integration by parts; the other sign of the imaginary endpoint is
   handled in (9). We import the theorem, not a new arithmetic proof.

   The future test must keep the source shifts fixed across primitive
   endpoints, apply partial integration for w_XT and the bounded
   analytic Hardy phase, and combine the pole terms before Cauchy
   extraction. L473 treats a sharp dyadic window and fixed derivative
   orders; the exact L637 smooth-window divided-difference application
   is a specialization still to do. Cauchy and compact-support
   holomorphy supply tools, not the sought Gram lower bound. No
   smooth-window theorem or limiting quotient is proved in this review.

5. **Coalescence tool.** Luiz Hartmann and Matthias Lesch,
   *Divided differences and multivariate holomorphic calculus*, Doc.
   Math., online-first 2026, [DOI 10.4171/DM/1060, Section 3 and
   Appendix A.2, (A.5)--(A.8), pp. 20--21](https://ems.press/content/serial-article-files/52597).
   Read the recursive formula, Genocchi--Hermite simplex integral and
   residue-contour representation. The integral formula assumes that
   the closed convex hull of the nodes is contained in the open
   holomorphy domain; the contour lies in that domain and encloses the
   nodes once. Section 3 states holomorphy in all node variables,
   including collisions. These standard tools permit a coalescence
   test without first replacing signed differences by total variation.
   Applying them to the complete L637 error and to its actual Gram
   form, with separate variables for the two observer slots, is future
   mathematical work. They do not themselves prove a relative bound.

### Duplicate and failure comparison

L637's TV stop excludes use of its sufficient absolute envelope for
microscopic bump realization; it is not a true-error lower bound.
The signed-short-interval review already knew the polynomial and
single-translation conclusions. Here the additional comparison is their
exact norm/quantifier mismatch with the proposed complete remainder.
L473's second kernel is existing source specialization, not a fresh
local discovery. Its abstract clipped-mass countermodel does not refute
the new actual-Hardy quotient.

Read `ATTEMPTS/2026-11-01-full-gram-signed-jet-budget-inconclusive.md`
and the relevant working continuation: those concern amplified
Dirichlet-frequency coefficients and a different arithmetic Gram form,
not cancellation between Hardy translations. The failed absolute Cauchy
half-budget does not settle this target. Scoped searches of these
assessments, translate reviews and failure records found no existing
coalescing two-Hardy-atom relative-remainder result. This is a bounded
duplicate check, not an exhaustive absence claim. No other notebook was
read or used.

### One bounded continuation, without a proof

Keep L637's exact w,T,X,L,Z,W,M,E,G. For 0<|h|<=1/2 consider only

    mu_(h,c)=c0 delta_0+c1 (delta_h-delta_0)/h,
    c0,c1 complex, (c0,c1)!=(0,0).

This is a two-atom subfamily of the original target, including the
potentially near-null antisymmetric direction. Its test is to prove or
refute |E(mu_(h,c))|<=eta(T)L^5 G(mu_(h,c)), eta(T)->0, uniformly
in h,c,X. h may depend arbitrarily on T. Do not take a formal quotient
at h=0; the test must justify any confluent extension and a lower bound
for the entire actual two-dimensional Gram form. Retain the exact
six-term expression, phase and curvature. No bound or nondegeneracy is
asserted here.

Bettin plus the saved phase scope cover the second-moment tools;
Hughes--Young plus L637/L622 cover the full numerator, and the cited
holomorphic divided-difference formulas cover coalescence. Fixed-order
Cauchy/L4 and partial integration are standard tools already present.
No new literature source is essential to attempt this bounded test.
It is an ordinary fixed-dimensional specialization, not a creative
mechanism or a theorem beyond the sources checked. Successful handling
of this family would test whether first coalescence itself is an
obstruction; it would leave unbounded atom counts and higher-order
near-null directions entirely open. Success is not sufficient evidence
to continue unrestricted atom growth without a new discriminating test.
Failure must identify an actual error/Gram direction or failed uniform
hypothesis, not merely an oversized absolute envelope.

The nomination is saved separately as REVIEW_REQUIRED for the next
scope approval. This literature-only step has not derived, approved
as correct, or executed its mathematics. The unrestricted target is
preserved as unresolved; no global abandonment or impossibility is
recorded. No lemma, DAG, overview or mathematical script was changed.

### Search and access record

Queries actually issued:

- `Riemann zeta shifted fourth moment uniform shifts Gram matrix relative error nearly coincident shifts`
- `Hardy Z translates moment kernel relative quadratic form error finite differences`
- `"zeta" "Gram" "relative" "shifted" moment error`
- `"zeta" "confluent" "moments" shifted`
- `"Hughes" "Young" "divided differences" zeta`
- `"Hardy" "translates" "Gram" zeta`
- `"zeta" "finite differences" "fourth moment"`
- `shifted second moment Hardy Z function complex shifts uniform derivatives sine kernel Atkinson theorem`
- `divided differences holomorphic Hermite Genocchi integral formula theorem`

Kösters [arXiv:0803.1141v2, Theorems 1.1--1.2,
pp. 3--4](https://arxiv.org/pdf/0803.1141v2#page=3) was inspected as
known sine-kernel overlap: fixed real shifts scaled by log t, not the
uniform complex smooth-window estimate required at coalescence.
Dutta--Ghoshal--Rajkumar [arXiv:2408.04247v1, Theorems 1.3--1.4,
p. 4](https://arxiv.org/pdf/2408.04247v1#page=4) supplies a broader
second-zeta-moment/kernel lead; its application requires meromorphic
functions holomorphic in an upper half-plane and decay/integrability.
Only the statements were read, not their proofs; it is not used and
is unnecessary given Bettin. Kovaleva arXiv:2401.13725 was found by
its abstract; an attempted v2 HTML URL returned 404. Its theorem and
proof remain unread and nonessential. Other search hits were not used
as theorem evidence.

The rStation Markdown download was rejected by the browser's content-type
handler, but all relevant HTML theorem and proof passages were readable.
A direct shell HTTP read failed DNS resolution and a PDF screenshot timed
out; browser text supplied the cited statements and relevant proof cases.
These are access limitations of redundant formats, not essential source
blockers. No API key or paid access was used.
