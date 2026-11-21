# Neutral prime-delay Rayleigh diagnostic: proposed continuation

TARGET: Test whether cellwise exponential neutrality leaves the upper L2 Rayleigh supremum of each complete finite prime-delay operator unchanged, using simultaneous phase recurrence and smooth moment correction.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 283's three-mechanism comparison searched exact neutral/prime-delay norm terminology, finite-codimension numerical ranges and truncated-translation modulation; a narrow local duplicate search found only different screw-form finite-codimension results. No full matching theorem was located. This does not establish novelty; this new assessment requires separate approval next turn.
SOURCE_EVIDENCE: L740 (4)/(5) fixes all finite arithmetic delays; Zhu arXiv:2608.24827v2 Lemma 3.2/Remark 3.3 supplies the distinct sharp pointwise-comb obstruction; Li Hongmin rStation 45 v1 (2.3), Sections 4–6 supplies finite partial-shift operator control; Clark Geometry of Numbers, current 159-page author PDF, Theorem 13.3/Corollary 13.4, printed p.72 supplies simultaneous approximation. Primary statements and relevant source proof cases were inspected in step 283; precise scope below and in the parent comparison.
COMPARISON: Known phase recurrence and standard Fourier decay support a finite-window obstruction diagnostic, while the support-compressed arithmetic operator is different from the pointwise comb. No inspected theorem directly identifies its smooth cellwise neutral Rayleigh supremum. Test only that difference; import Dirichlet simultaneous approximation and the Riemann–Lebesgue lemma instead of reproving them.
GAP: Equality of the two suprema below is unproved. Essential checks are arbitrarily large simultaneous returns, density of cell-interior smooth tests for the bounded arithmetic form, and exact small smooth correction of both moments in each cell. No energy-normalized equality, complete Weil sign, all-window estimate or RH implication is supplied.
REASON: This independently testable diagnostic determines whether neutral moments alone can lower the prime-only L2 operator cost before attempting a global coherent estimate. It is materially different from summable beta, relative boundary flux and the Möbius Gram-dual tail. It is a specialization/obstruction test, not a nominated creative proof of the central sign gap.
SCOPE: Each fixed integer K>=2, ell=log(3)/2, L=K ell; the entire bounded self-adjoint arithmetic operator below on original unweighted complex L2(0,L), with both exponential moments imposed separately on every smooth cell. No assertion uniform in K, no reduced delay set, and no replacement of the complete energy by its arithmetic component in a positivity claim.

## Proposed exact test, not an established result

Use L740's zero-extended delays

    (T_a u)(x)=1_(x>a) u(x-a),   0<x<L,
    B_L = sum_(2<=n<exp(L)) Lambda(n)/sqrt(n) (T_log(n)+T_log(n)^*).

This fixes the sign convention: B_L is the self-adjoint arithmetic
component entering the complete smooth energy with a minus sign.
Every prime power is retained. A delay exactly L is zero and may
also be included. Define L742's neutral smooth space N on (0,ell),
with integral e^(x/2)f(x) dx = integral e^(-x/2)f(x) dx = 0,
and let

    U_K = {sum_(j=0)^(K-1) f_j(x-j ell) : f_j in N}.

The single proposed threshold is

    sup_(0!=u in U_K) <B_L u,u>/||u||_2^2
        = sup_(0!=u in C_c^infinity(0,L)) <B_L u,u>/||u||_2^2
                                                        (proposed).

All tests may be complex. This is an unconditional arithmetic question
for each fixed K, not a proposed assertion of full Weil positivity.
The claimed equality is neither derived nor approved for execution
in its nomination turn. No value of either supremum is asserted.

## Source comparison and import boundaries

[Clark, Geometry of Numbers with Applications to Number Theory](https://plclark.github.io/PeteLClark/Expositions/geometryofnumbers.pdf),
Theorem 13.3/Corollary 13.4, printed p.72 of the author-hosted 159-page
PDF, accessed 4 November 2026, is the standard Dirichlet simultaneous
approximation input for any finite list of real numbers. Corollary 13.4:
for integers M>1 and n>=1 and real theta_j, some integer 0<m<M has
max_j ||m theta_j||<=M^(-1/n). No independence hypothesis is needed.
Its general theorem proof invokes Minkowski and leaves some details to
the reader; this is a theorem import, not a replayed source proof.
Specializing phases to the finitely many log n/(2*pi), with an appropriate
modulation convention, and obtaining frequencies tending to infinity
remain explicit application obligations. Small-denominator returns
alone do not establish the latter. The standard named Riemann–Lebesgue
lemma applies to L1 functions; its hypotheses must be checked for every
moment pairing used. No quantitative decay rate is required by this target.

[Zhu, arXiv:2608.24827v2](https://arxiv.org/html/2608.24827v2),
Lemma 3.2/Remark 3.3, concerns an unrestricted pointwise finite prime
comb, not its compression to supported tests with exact moments. It
warns that a lower bound on that comb has the wrong sign for a lower
Weil bound. It does not establish the proposed equality. Its recurrence
argument is a lead, not a substitute for the support and correction checks.

[Li Hongmin, rStation 45 v1](https://rstation.ai/problems/riemann_hypothesis/papers/45),
(2.3) and Section 6, uses bounded partial shifts/reflections and exhaustive
four-step row bounds at one specified support. It supplies operator
geometry that pointwise comb estimates ignore; it neither removes neutral
moment constraints nor evaluates either proposed supremum. Sections 4–5
retain the complete complement. Its source computation is not replayed.

The parent [completed discovery comparison](2026-11-04-neutral-cell-coherent-mechanism-discovery.md)
records the searches, factorization prerequisites, real-zero-remainder
stop, mandatory October baseline and comparison with earlier failures.
No inaccessible lead is essential to this diagnostic. Full matching
Mathlib coverage is unchecked; supporting Hilbert/Fourier facts are not
a claim of a matching theorem. If proved, report a standard-mechanism
specialization/REPRODUCTION, without claiming certified originality.

## Bounded continuation and abandonment test

The intended test is a simultaneous-modulation construction with exact
smooth moment correction on each of the finitely many cells. A later
attempt must verify all three missing checks in GAP, retain all delays,
and bound the change of the arithmetic Rayleigh value in the original L2
norm. It must not silently replace exact neutrality by asymptotic neutrality.
This paragraph specifies an attempt, not its proof or a guaranteed outcome.

If equality is proved, abandon only the hypothesis that these moments
alone give a strict improvement of this prime-only supremum. Its plausible
downstream use is to avoid an unpaid improvement in a finite-section Weil
lower certificate and require joint arithmetic/archimedean control instead.
If a strict gap is rigorously found, quantify it and assess its usefulness
against that complete form's costs in a separately covered target. If the
construction fails, preserve the failing hypothesis; do not infer a strict
gap from failure to prove equality. One bounded attempt suffices before
reassessment if it produces neither equality nor a discriminating witness.

Essential local inputs are L740's delays, L741's original norm conventions,
and L742's exact neutral space; L742's RH assumption/conclusion is a
contrast only and is forbidden as a premise. The local positivity seed's
unreplayed source computation is unnecessary for this prime-only test.
The complete energy's logarithmic Fourier cost is not preserved by mere
L2 modulation. Thus the conclusion, if obtained, cannot be promoted to
an energy-normalized beta statement or a stop on all phase-preserving
mechanisms. Moment complements, adjacent/full signed interactions,
all-window positivity and actual Xi mixed signs remain open.
