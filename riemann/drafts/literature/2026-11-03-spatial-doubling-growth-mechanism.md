# Spatial doubling growth: source comparison

TARGET: Review the spatial doubling-growth mechanism B_sp(n)=o(n) at s=65/64 for L706's full-circle Jensen defect in the same fixed L703 family.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 158 completed the bounded Bernstein-index, logarithmic-integrability, Cartan, three-circles and signed-Cauchy-transform search recorded below, with local duplicate/failure comparison. No inspected source establishes the fixed-family sublinear growth estimate; no novelty claim follows.
SOURCE_EVIDENCE: Ramachandra, TIFR Lectures 85 (1995), Theorem 1.5.2 and complete proof p.27 https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr85.pdf ; reuse Ash--Novinger Theorem 4.8.3/Lemma 4.8.4 pp.33-36 and Corollary 4.7.4 p.27 https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesWithHyperlinks.pdf . Additional inspected primary comparisons and qualifications appear below.
COMPARISON: Three-circles convexity and boundary Poisson--Jensen cover the standard tools for a degree-independent growth-to-defect specialization, whose algebra and zero cases remain for research. None supplies B_sp=o(n) for the complete signed fixed-profile family. Generic degree bounds, real-ball small values, zero counts and angular endpoint dominance do not supply that estimate.
GAP: Write the cited transfer specialization without extra zero-free hypotheses, then test B_sp(n)=o(n) for the same fixed actual profile. No transfer constant, family asymptotic, positive limiting obstruction or full-circle defect estimate is proved in this literature turn.
REASON: The essential source comparison is now complete and accessible. A separate bounded mathematical attempt on the new spatial-growth mechanism is justified; the changed ready continuation receives separate approval before invocation. Preserve earlier stops and every independent amplitude/charge/realization gap.
SCOPE: Exactly TARGET, with the fixed L703 profile selected before n=12q+3, original L666 G_n, |u|=1/2, s=65/64, anchor, unit masses, inverse angle, j=0, both endpoints and all M=n/3 moments. No profile replacement, endpoint-only full-circle expansion, or automatic relative approximation is allowed.

The nomination below is preserved as the pre-review question. The completed
comparison and current source decision follow it in the step-158 section.

## Proposed test and its relevance

Keep the same actual family as in audited L706. Define the prospective
growth observable using normalized angular measure by

    S_(n,r)(u)=max_(|z|<=r) |G_n(u,z)|,
    B_sp(n)=mean_(|u|=1/2) log(S_(n,s)(u)/S_(n,1)(u)),
    s=65/64.

The proposed mathematical test, after source approval, is B_sp(n)=o(n)
along the entire allowed sequence. This is a new sufficient-mechanism
candidate, not a claimed equivalent reformulation of J_sp(n)=o(n).
The review must first check whether a bound of the form

    log S_(n,1)(u)-mean_(|z|=1) log|G_n(u,z)|
       <= C_s*[1+log(S_(n,s)(u)/S_(n,1)(u))]

is valid with a constant independent of n, degree and u, or identify
the correct replacement and its additional hypotheses. The displayed
comparison is a question for the source review, not an imported or
proved inequality. Standard terminology to investigate includes
Bernstein index, analytic growth estimates, and logarithmic norm
comparison. Primary theorem hypotheses and essential zero cases must
be inspected before mathematical use.

If a suitable transfer exists, small averaged spatial growth would be
a possible way to pay the angular complement left by L706. Coupled
with a separately proved angular lower bound for log S_(n,1), that
could improve L657's complete logarithmic accounting. Amplitude,
full charge, H/support, Xi realization and actual-Xi positivity all
remain independent and unproved. A positive lower limiting B_sp(n)/n
would stop this sufficient sublinear-growth mechanism, not disprove
sublinear Jensen defect or RH.

## Why this is a different proposed mechanism

The intended observation is growth in the spatial variable after
amplitude cancellation. It does not propagate an angular lower bound
from the paid arc, nor assume that endpoint dominance extends around
the angular circle. The finite resolvent representation has spatial
nodes strictly inside the unit circle. A later attempt must explicitly
check the proposed s against their maximal modulus and pay the exact
geometric remainder at that radius. Even if the absolute remainder
decays, it is not a relative error without a lower bound for the
normalizing complete signed polynomial.

No generic analyticity or nonzero-slice assertion alone is proposed
to imply sublinear growth. The prescribed signed weights and the same
fixed profile must supply any needed quantitative improvement. This
retains the lesson of C672a's auxiliary-coefficient counterexample and
L686's full-support clearing limitation. L683's already paid linear
root cost and the exact-arc conclusion of L706 remain intact.

The next literature turn should reuse the parent assessment's actual
readings, compare the strongest relevant growth/log-mean theorem and
known obstructions, and either nominate a precise bounded attempt or
stop this mechanism with evidence. It must not derive and approve a
new transfer lemma in that same turn. Full matching Mathlib coverage
for this proposed mechanism has not been checked.

## Prospective routing after a separate source gate

If the comparison supports the exact test, nominate
proof_attempt/creative, deep_research/max. The precise obstruction is
the current positive linear loss on the angular complement; the new
bounded test is the full-circle spatial growth ratio above with both
signed sums and all moments retained. Evidence of o(n) growth or a
rigorous positive limiting growth rate would change the local route
decision. This is prospective only: the immediate next task is
literature_comparison, standard/high, because the analytic transfer
has not been covered. No creative-attempt credit is claimed today.

## Completed comparison — 3 November 2026, step 158

This completes the saved review, with decision EXPLORE for the remaining
family estimate. It is a literature EXPLORATION, not a mathematical
bound or a novelty determination. No lemma or mathematical script was
written or modified. The working checkpoint is
`drafts/2026-11-03-spatial-doubling-source-working-158.md`.

### Primary theorem statements and applicability

K. Ramachandra, *On the Mean-Value and Omega-Theorems for the Riemann
Zeta-Function*, TIFR Lectures **85**, Springer (1995),
[Theorem 1.5.2 and complete proof, printed p.27](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr85.pdf#page=1),
states, for f analytic on a neighborhood of the closed annulus and
0<r1<r2<r3, with Mi=max_(|z|=ri)|f(z)|,

    M2^(log(r3/r1)) <= M1^(log(r3/r2))*M3^(log(r2/r1)).

The inspected proof applies the maximum-modulus principle to integer
powers of f times integer powers of z, then passes through rational
exponents. It does not take a holomorphic logarithm of f or exclude
zeros. For a nonzero polynomial all three maxima are positive;
constant slices are allowed. The radii 1/2, 1, 65/64 meet its strict
inequalities. Disk and circle maxima agree by the maximum-modulus
principle. Thus this is the applicable convexity input, rather than a
degree estimate. No reproof of three-circles is called for.

Reuse R. B. Ash and W. P. Novinger, *Complex Variables* (2004),
[Theorem 4.8.3 and Lemma 4.8.4, printed pp.33-36](https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesWithHyperlinks.pdf#page=94),
and Corollary 4.7.4, p.27, as assessed in step 154 and used in L706.
The second Poisson--Jensen version covers analytic nonzero functions
on a neighborhood of the closed disk, with boundary zeros included
through explicit boundary factors. Its nonzero interior evaluation
is bounded above by the Poisson integral of the boundary logarithm;
the zero terms have the correct nonpositive sign. The kernel has
normalized mass one. L706 supplies nonzero polynomial slices, so a
maximizer on the inner spatial circle is a permitted evaluation even
when the constant coefficient vanishes. Multiplicities, actual degree
drops and zeros on either comparison circle impose no zero-free premise.

These inspected standard inputs cover the tools for the proposed
degree-independent transfer. The necessary specialization is to
compare the three spatial maxima and then use the inner maximizing
value in the boundary inequality, with constants depending on the
fixed radii. Its algebra and the zero-growth case must be written
and checked in research; no new transfer theorem or numerical
constant is established in this review. In particular a bare
Poisson inequality evaluated at a maximum on the unit boundary
would not be a permitted interior evaluation.

### Other inspected comparisons and a source qualification

A. Brudnyi, [*Traces of Subharmonic Functions to Fractal Sets*,
arXiv:math/9908121v1](https://arxiv.org/pdf/math/9908121v1),
23 August 1999: inspected Theorem 1.1, p.2, Proposition 3.1 and its
complete proof, pp.5-6, and Lemma 3.5/(3.6), p.8. Proposition 3.1
states that a nonpositive subharmonic v on D1 with sup_Dr v>=-1,
fixed r<1, has v>=c(r)log(H/e) outside disks of total d-power radii
at most (2H)^d/d. Singularities are permitted through smoothing and
Riesz potentials. This is relevant small-value coverage, not a bound
for the signed family. The proof prints f=u on D1 after a construction
that only preserves u on the smaller disk, and its final comparison
of negative logarithmic factors is questionable. These apparent
errors are recorded, not silently repaired. No constants or theorem
from that proof are load-bearing here; the independent three-circles
and boundary-Poisson inputs avoid this source issue. No new reproof
or source-access blocker is required for the chosen continuation.

F. Nazarov, M. Sodin and A. Volberg,
[*Local dimension-free estimates for volumes of sublevel sets of
analytic functions*, arXiv:math/0108213v2](https://arxiv.org/pdf/math/0108213v2),
4 November 2001: inspected the main theorem, pp.1-2, and Lemma B,
p.3. The theorem uses a bounded analytic function on a complex ball,
real-ball volume, epsilon<=1/4, and an exponent containing
48*epsilon^(-3)*log(1/|F(0)|). Lemma B uses a real interval and
equal nonzero endpoint values. These statements cannot be quoted
directly for arclength measure on a spatial circle or an unproved
central-value bound. Their proofs are not imported or independently
audited. The extra central-value and geometry conditions are why
they are comparisons rather than the selected transfer inputs.

Yu. Ilyashenko, [*Variation of argument and Bernstein index for
holomorphic functions on Riemann surfaces*, arXiv:math/0601043v1](https://arxiv.org/pdf/math/0601043v1),
3 January 2006: inspected Section 1's growth-and-zeros statement and
Bernstein-index definition, pp.1-2, and Lemma 2/proof, p.6.
The index is log(sup_U|f|/max_K|f|); its zero-count and argument
estimates do not themselves state a circle-logarithm comparison.
Geometric-gap and factor-removal hypotheses cannot be dropped. No
theorem or literal constant from this paper is used here.

A. Brudnyi, [*Local inequalities for plurisubharmonic functions*,
Ann. Math. **149** (1999), 511-533,
arXiv:math/9903199v1](https://arxiv.org/pdf/math/9903199v1): inspected
Definition 1.1 and Theorem 1.2, pp.511-512, including the classical
polynomial doubling inequality (1.3). The latter's exponent is
polynomial degree. The real-ball Remez statement and fixed finite
analytic-span bounds are not bounds uniform over the present growing
number of spatial moments. Its supporting proof was not audited.

### Search record, duplicate tests and remaining difference

The bounded external searches combined the exact strings/terms
`Bernstein index`, `log-integrability`, `logarithm L1 circle Remez`,
`analytic growth Mahler measure`, `subharmonic Cartan circle`,
`On a BMO-property for subharmonic functions`, `Ahlfors regular`,
`signed power sums polynomials Bernstein index`, `Fourier gap Bernstein`,
`truncated Cauchy transform maximum modulus`, and
`Hadamard three circles theorem proof`. Primary theorem retrieval
then followed only the relevant hits above. University-hosted
Ramachandra was initially inaccessible by its bare URL, but the
indexed page reference returned the actual theorem and complete proof.
An inaccessible Citeseer copy of Brudnyi was replaced by the arXiv
version. No essential source remains blocked.

Unread leads include Brudnyi's *On a BMO-property for subharmonic
functions*, the algebraic-function Bernstein--Remez papers, and the
monograph *The Cauchy Transform*. No assertion about their precise
theorems or inadequacy is based on a snippet. The selected elementary
tools make these leads nonessential. Tao's three-circles exercises
and search summaries were not used as theorem evidence; the full
Ramachandra statement/proof was obtained instead. No exact theorem
for this fixed-family B_sp limit emerged; failed searches do not
certify originality.

Reuse the parent assessment's root, norm, torus-integrability and
zero-asymptotic comparisons. The local reads of L666, L703, L706,
L657, L683 and L686 plus the saved clearing and endpoint-extension
stops distinguish this observable. The already recorded C672a
generic angular-propagation failure is not a spatial-growth
counterexample. L683 has an absolute small-spatial-circle norm and a
degree cost; L686 clears replacement poles. L702 stops omitting the
signed interior globally. L706 pays only a fixed angular arc. None
estimates the amplitude-cancelled ratio of the same complete
polynomial at two spatial radii on the full new angular circle.

### Exact bounded continuation

The separately saved
[research scope](2026-11-03-spatial-doubling-growth-attempt-scope.md)
retains the same proposed family and observable. Following separate
approval, one mathematical attempt should first record the routine
cited transfer and then seek B_sp=o(n), or a rigorous positive lower
limiting growth rate for the same fixed profile. Analyticity alone,
absolute geometric-tail decay, generic linear-degree bounds and
finite numerical samples cannot decide this test. At the enlarged
radius the complete finite geometric remainder and its normalization
still need payment; no relative approximation is presumed.

The prospective new mechanism is spatial growth after amplitude
cancellation, not reproving the standard transfer. Its possible
downstream use is to pay L706's complementary Jensen defect before
L657's complete logarithmic accounting. Angular amplitude, full
charge, H/support, Xi realization and actual-Xi positivity remain
independent gaps. A positive B_sp/n lower limit stops only this
sufficient growth mechanism. Inconclusive work must preserve its
partial reasoning and specify a new input before repetition.

Full matching Mathlib coverage for the averaged family statement
and this exact transfer specialization is not checked. The parent's
recorded Mahler-measure support is not such a theorem. No new
formalization claim is made, and coverage is not a completion gate.
