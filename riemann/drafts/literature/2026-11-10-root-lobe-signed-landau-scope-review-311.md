# Signed low-zero aggregation — completed source comparison312

TARGET: Assess whether unconditional Landau-Gonek zero-sum estimates supply selector-sensitive signed control of C988a's finite low-zero lobe aggregate at every-epsilon subexponential scale, rather than reconstructing the unpaid arithmetic sum.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step312 reused weighted reviews253/254, C988a and selector stops307/308; searched uniform Landau-Gonek, nearest-prime-power refinements, ordinate cancellation and exact Laguerre/zero-sum terms. Inspected Ford-Zaharescu math/0405459v2 Lemma1 and relevant Section3 proof cases, and Ford-Soundararajan-Zaharescu0805.2745v3 Section1 qualifications. No matching selected-lobe theorem was located; no novelty inference.
SOURCE_EVIDENCE: Ford-Zaharescu, arXiv:math/0405459v2 (30September2004), Lemma1/(3.1) p7, both near-prime-power cases p7 and beta-to-ordinate comparison/(3.8) pp8-9, https://arxiv.org/pdf/math/0405459v2 ; Ford-Soundararajan-Zaharescu0805.2745v3 (10January2009), Section1 pp3-5/(1.5)-(1.6), https://arxiv.org/pdf/0805.2745v3 . Reuse Gorodetsky Lemma5.2/AppendixA and Montgomery-Vaughan coverage through reviews253/254/309.
COMPARISON: The unconditional uniform formula retains the nearest-prime-power resonance and unsigned error. Its fixed-frequency ordinate results and RH-qualified extensions do not supply the growing-degree positive-lobe selector bound. The weighted formula remains representation coverage with unpaid arithmetic prefixes; exact root endpoints do not by themselves remove an interior resonance or pay a selector estimate.
GAP: The every-epsilon bound for S_n remains unproved and unrefuted. No inspected theorem supplies cancellation uniformly in the moving u range, with actual beta weights and the nonlinear selector. No post-integration source-error estimate is newly calculated here.
REASON: Park direct payment by these Landau-Gonek imports: a representation or an ordinate theorem outside its hypotheses is not the missing signed resource. This is new source-scope evidence for the changed target, not a mathematical lower bound or an impossibility theorem. No further absolute-tail refinement or repeat endpoint calculation is nominated.
LITERATURE_REASON: The target changes from fixed-degree absolute convergence and high-tail arithmetic to degree-uniform signed aggregation with a nonlinear lobe selector; review309 does not cover that hypothesis or conclusion.
SCOPE: Completed literature-only comparison of the exact S_n below, n>=2, actual zeros with analytic multiplicity, closed low cutoff exp(n) and complete exact-root intervals. EXPLORE records a parked import, not approval to derive S_n or an adaptive filter in this turn.

## Exact resource to compare, not a claimed result

Use C988a's K_n, complete interval collection I_n, T_(n,I) and
V_(n,I), all actual nontrivial zeros with analytic multiplicity, and
the closed low cutoff |Im(rho)|<=exp(n). The candidate resource is

    S_n=sum_(I in I_n) max{
          -Re(sum_(rho, |Im(rho)|<=exp(n)) T_(n,I)(rho))
          -V_(n,I), 0}.

The proposed threshold is: for every epsilon>0 a finite nonnegative
C_epsilon exists with S_n<=C_epsilon*exp(epsilon*n) for every
integer n>=2. This is an unpaid target, not a new assertion or
approved research subtarget. It is intended for comparison with
C988a's high-tail bound and future positive compensated lobe control.
Clipped pieces, both logarithmic complements and L984(H) remain
independent unresolved obligations even if this resource were supplied.

The specific mechanism to assess is cancellation in finite complex
zero-height exponential sums before taking the lobe positive part.
Keep beta=Re(rho) in every exponential, preserve the full zero
multiplicity and all prime-power proximity/error terms, and require
uniformity for u in the moving range [n,2n], height exp(n) and the
actual complete-root interval collection. A fixed-u estimate or an
RH-conditional estimate does not match these hypotheses. No inference
of a signed estimate from C988a's absolute tail is permitted.

## Discriminating source test and preserved stops

First reuse reviews253/254: do not replay their endpoint error
calculation or re-import the same formula as a new advance. Compare
the changed observable with the primary theorem's exact output.
Continue only if a named unconditional result supplies cancellation
that remains useful after the lobe selector, or identifies a concrete
new intermediate estimate with an independently testable gain. If
the result merely reconstructs the original unpaid prime sum, or
needs RH, an unpaid selector norm, or an uncontrolled proximity term,
record that precise obstruction and park this direct mechanism.
Do not nominate another absolute-tail refinement.

The prior sharp-endpoint Landau representation is not itself such
a gain. Complete root endpoints change the test and remove its
leading endpoint samples, but whether that change helps the SIGNED
resource is exactly the unanswered comparison; no reopening success
is claimed. Preserve stops233/235/243/302/305/306/307/308 and the
earlier endpoint evidence. This is a bounded source question, not
a relabeling of the unpaid window-square majorant or a universal
individual-lobe sign claim.

Canonical mathematical inputs for any later approved attempt would
be C988a, L985's finite connection and audited L988. Existing Landau
coverage is a source lead, not a new DAG input. Full matching Mathlib
coverage is unchecked and unknown. No cross-notebook input or
creative mathematical approval was claimed in the step311 nomination.
The comparison below completes that source question, without a derivation.

## Primary theorem and relevant cases inspected in step312

[Ford and Zaharescu, On the distribution of imaginary parts of zeros
of the Riemann zeta function, arXiv:math/0405459v2](https://arxiv.org/pdf/math/0405459v2#page=7),
Lemma1/(3.1), p7 (published J. reine angew. Math.579 (2005),145-158),
states for real x,T>1, with q_x a nearest prime power,

    sum_(0<gamma<=T) x^rho
      =-Lambda(q_x)/(2*pi)*(exp(i*T*log(x/q_x))-1)/(i*log(x/q_x))
       +O(x*log^2(2*x*T)+log(2*T)/log(x)).

At x=q_x the quotient is T; zeros have multiplicity as defined p2.
Read both |x-q_x|>=1 and <1 proof cases, retaining the resonance.
The remaining contour proof is cited there to Gonek; no independent
audit of that inherited argument is claimed. Read pp8-9: the
beta-to-ordinate conversion uses delta=50*loglog(T)/log(T) and
delta*log(x)<1. This condition does not cover our moving range.
Theorem1 instead fixes alpha and the test; proof constants may
depend on both. No uniform selected-lobe conclusion is stated.

[Ford, Soundararajan and Zaharescu, On the distribution of imaginary
parts of zeros of the Riemann zeta function, II, arXiv:0805.2745v3](https://arxiv.org/pdf/0805.2745v3#page=3),
Section1 pp3-5, labels (1.5), the uniform ordinate assertion on
T^2/(log T)^5<=x<=T^A, a conjecture. Page4 quotes the unconditional
complex-zero formula (1.6), keeps the nearest prime power, and
distinguishes division by sqrt(x) on RH from the density comparison.
Its unconditional small-frequency consequence is restricted to
log(x)=o(sqrt(log T)). Theorems2-4 assume RH and additional
conjectures. These qualifications do not cover the present moving
beta-weighted selector; no claim about subsequent literature follows
merely from this paper. No conditional result is imported.

Gonek's [1985 paper, pp92-97, Theorem1](https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/8-landau-form.pdf)
was revisited as a lead. The scan exposed no readable proof text;
screenshot calls returned references without images, and local
retrieval failed DNS. No new Gonek proof inspection is claimed.
The accessible Ford-Zaharescu statement and its explicit resonance
cases suffice for this output-scope comparison; the independently
ready weighted representation uses Gorodetsky. No essential access
blocker remains for the decision. Unread extensions are not inputs.

## Target comparison and decision

C988a has already paid its absolute high-zero tail. The target S_n
asks for positive parts of finite low-zero lobe responses including
-V, not a pointwise bound for sum x^rho. Neither inspected primary
output contains a one-sided estimate uniform over that selector.
Restoring weighted prefixes with Gorodetsky returns the previously
unpaid arithmetic quantity. Exact root endpoints remove C988a's
leading boundary samples but impose no source hypothesis about the
arithmetic inside each interval. No integral of a source error,
new partition identity, bound for S_n or counterexample is derived.

Queries included `Gonek A Formula of Landau theorem 1 x T`,
`Ford Zaharescu distribution zeros Landau Lemma 1 x T`,
`Landau Gonek uniform unconditional exponential sums zeros`,
`Landau Laguerre zeros sum`, and `Landau Gonek positive weighted
sums zeros`. No exact-weight match was found. Ford-Zaharescu's
author-hosted text later timed out; its versioned arXiv primary text
resolved that issue. Search snippets and unread extension leads
are not theorem inputs. Full matching Mathlib coverage is unchecked.

Disposition: NEGATIVE source-scope evidence, NOVELTY_UNCHECKED,
not a new prime estimate. Park this direct import while preserving
the unpaid target and stops233/235/243/302/305/306/307/308. The main
gap L030-L032/C032a and L966/L968, L984(H), clipped lobes, both
complements and regulator/infinite-degree passages remain open.
No PROOF/DAG change or cross-notebook input is needed.

A distinct [review312 nomination](2026-11-10-adaptive-slope-spectral-separation-review-312.md)
asks whether degree-dependent signed slope measures with a controlled
norm avoid audited L997's fixed positive-bump obstruction uniformly
over a competing ordinate interval. This changes the mechanism; it
is REVIEW_REQUIRED, with no constructed weights, new cancellation
or mathematical approval. Preserve the original fixed-bump stop.
