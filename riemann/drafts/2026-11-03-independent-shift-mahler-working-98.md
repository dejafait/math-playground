# Independent-shift complete logarithmic homotopy — working step 98

Invocation-start gate: `drafts/literature/2026-11-03-independent-shift-mahler-homotopy.md`, EXPLORE, read in the supplied snapshot. Exactly its TARGET is being tested; no further source review or broader norm claim is authorized by this note.

Main gap: actual-Xi all-degree mixed positivity and unbounded-height signs. Intermediate target: for L666's fixed family and independent real |e_m|<=1/8, prove A_n(e)>=A_n(0)-n/100-C log n with absolute C/onset, or give an admissible asymptotic violation. Downstream: L690's audited base and L661's diagonal envelope leave positive linear margin if this loss is paid. H/support/realization and actual signs remain independent gaps.

Read inputs: L657 definitions and Sections 2–3 (complete K/Q, nonzero slices, integrability and complete angular Jensen charge); L666 hypotheses and Section 6 (straight admissible path, original residues, bounded individual logarithmic derivatives but uncontrolled signed energy); L690 hypotheses/conclusion and Section 5 (audited common-shift base); L665 hypotheses/conclusion and its recorded stop. Existing working-tree changes are preserved.

Bounded mechanism: examine whether the fixed anchor and the nonanchor displacement restriction force a complete numerator-charge lower comparison, rather than differentiating log G through its zeros. The interior denominator charge P_n is independent of e; exterior denominator factors and m_0 variation still need exact accounting. No conclusion or differentiability of A_n is presumed.

Continue only with the target bound, a useful partial complete-charge estimate with the remaining losses explicit, or an actual admissible asymptotic violation. A formal Jensen identity, pointwise single-term comparison, unweighted root count or finite screen alone is inconclusive. Preserve any failed inequality and refine the mechanism before repetition.

## Refined bounded subfamily test

Test e_m=alpha for m>=0 and e_m=beta for m<0, independently |alpha|,|beta|<=1/8. This remains inside the approved homotopy cube, includes common shifts and L665's outward-pair displacement, and is not L664's complementary two-offset family. The full independent cube remains the target; success here would be partial complete-charge control only.

Subtract L690's common-beta response. The difference is represented on the right half of its moving rectangle by K_alpha,n-K_beta,n. The outer edges have the already proved exponential contour bound. On the central vertical edge y=i*s/n the kernel difference decays at both ends. Formally the limiting scalar response is

    H_(alpha,beta)(g)=1+(i*Omega/(2*pi))*integral_R
      exp(-g*s)*[1/(1+exp(-Omega*s-2*pi*i*alpha))
                 -1/(1+exp(-Omega*s-2*pi*i*beta))] ds,
    Omega=20*pi/27,
    g(u)=-integral_0^1 [1/(x-t*u)+t/(U*u-t*x)] dt.

The integral is analytic for |Re g|<Omega. At g=0, direct endpoint evaluation suggests H(0)=1-alpha+beta>=3/4. To make this a proof, check all contour signs and residues, a fixed complex angular annulus, uniform central domination and n-limit, nonconstancy of g, compact parameter uniformity and logarithmic convergence through boundary zeros. Do not infer a complete mean from pointwise convergence or a finite screen.

Relevant additional reads: L690 Sections 2–4 (complete pointwise contour envelope and kernel), L663 hypotheses and contour scope, L664 hypotheses (distinguishes the two-offset family), and L670/L671's clearing stops. The shared analytic annulus and limiting scalar argument are unfinished; no bound has yet been claimed.

## Completion

The full proof is now canonical in `lemmas/L691-two-half-displacement-complete-logarithmic-bound.md`. It establishes an O(1) complete logarithmic and angular zero-charge loss uniformly for the two independently shifted halves and their straight paths, with existential absolute constants/onset. It does not establish the full-cube target. The split-contour limit, central tails, analytic nonidentity and logarithmic convergence through circle zeros are written out; the 11 rational support checks pass. No derivative of the singular response logarithm is used. A separate audit is pending under the new REVIEW_REQUIRED assessment; this note's earlier unfinished checkpoints are retained as development history.
