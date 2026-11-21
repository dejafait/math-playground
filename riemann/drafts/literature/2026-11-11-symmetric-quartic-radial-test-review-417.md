# Symmetric quartic: bounded real-radius obstruction test

TARGET: Test whether the specified reflection-symmetric quartic completion has bounded (1-r)^2 real-radius cumulative Li germ while violating L984's every-epsilon coefficient lower envelope.
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step417's bounded signed-Taylor, Li/Tauberian, polynomial/counterexample and real-axis searches in 2026-11-11-real-radius-li-recovery-review-416.md. Scoped local comparison found review245's different prime-band quartet diagnostic and L984's actual-Xi sufficiency argument, not this exact radial model. No novelty claim.
SOURCE_EVIDENCE: Flajolet-Sedgewick Complex Asymptotics (8May2004), TheoremIV.6 p29/PDF37 and partial-fraction proof inspected in step417, https://algo.inria.fr/flajolet/Publications/ch4567.pdf#page=37 ; reuse TheoremIV.3(ii), pp15-16, and L984's previously inspected standard Taylor/local-zero/continuation contracts. Full source comparison and qualifications reside in review416.
COMPARISON: Rational coefficient extraction and Pringsheim cover the tools, not the proposed model's full normalized cumulative observable. L984 is a template for a conditional argument, not a theorem about arbitrary polynomial completions. Recheck every model hypothesis and finite prefix; no actual-zeta estimate follows.
GAP: Establish or refute both stated model properties, including positive-real regularity and interior-pole survival for the exact logarithmic derivative. No model coefficient estimate or counterexample is proved in this assessment.
REASON: A finite independently testable obstruction separates weak radial growth from coefficient control without assuming Taylor convergence up to one. This known-tool specialization follows the direct-import scope rejection; the newly written ready assessment needs separate next-turn approval before mathematical invocation.
SCOPE: Only the explicitly defined quartic below, the ordinary undivided coefficients of its normalized local logarithm and their partial sums starting at degree2. No prime realization, Euler product, actual xi growth, simple actual zeros or RH assumption.

## Exact proposed experiment

Define, for this future test only,

    Q(s)=((s-3/4)^2+1)*((s-1/4)^2+1),
    xi_Q(s)=Q(s)/(2*Q(1)),
    H_Q(z)=2*xi_Q(1/(1-z)).

Define ordinary coefficients ell_n by the local identity

    log H_Q(z)=sum_(n>=1) (ell_n/n)*z^n,

using the logarithm with value zero at the origin, if its required
normalization is verified. Define d_n=sum_(k=2)^n ell_k and set

    F_Q(z)=[z*H_Q'(z)/H_Q(z)-ell_1*z]/(1-z).

All local identities, symmetry, reality, normalization, zero orders,
domain and pole qualifications are obligations of the next test,
not conclusions established here. Verify explicitly that the local
Taylor coefficients of F_Q are exactly d_n, including degrees0/1.

The two simultaneous thresholds to test are

    sup_(0<=r<1) (1-r)^2*|F_Q(r)| < infinity,

and failure of

    for every epsilon>0 there exists finite D_epsilon>=0
    with d_n>=-D_epsilon*exp(epsilon*n) for every n>=2.

Provide a rigorous bound in the first statement, not a sample of
radial values. For the second, either give an exact negative
subsequence with a sufficient rate, or apply the imported Pringsheim
theorem after checking the correction, finite positive Taylor radius,
uncancelled pole and regular positive point. Do not apply the
actual-zeta conclusion of L984 as a generic theorem.

The model is intended to test whether reflection symmetry, reality,
positive-real zero exclusion, positive integer zero orders and this
weak radial bound suffice for coefficient recovery. Each retained
property must be verified. It is a polynomial completion, not actual
xi: it need not retain order-one growth, gamma factors, zero counts,
an Euler product or the arithmetic identity in L984. Even a successful
test would address only an inference from the explicitly retained
properties, not a zeta-specific Tauberian theorem with stronger input.

## Coverage, stopping test and downstream use

Import rational coefficient extraction, rather than reprove the general
partial-fraction theorem. If the rational function is improper, retain
its polynomial part and finite exceptional coefficients. If using
Pringsheim, import its named theorem and prove only the model's
applicability; preserve every positive integer multiplicity. A real-axis
bound on a meromorphic quotient must not be called Abel summability
beyond its Taylor radius.

This is a REPRODUCTION calculation, not a creative central mechanism.
The bounded decision is whether both displayed thresholds hold for
this one Q. If they do, record the exact limited obstruction and park
weak-radial-only recovery. If either fails, record that failure rather
than enlarge the family during the attempt. A useful downstream
consequence would be identifying what stronger zeta-specific input a
future real-axis approach must supply. L984(H), actual-Xi positivity,
forcing and the capped E_n bridge remain unresolved in either case.

Review245 used an off-line quartet to test moving prime-band response;
this test uses the complete cumulative logarithmic-derivative germ
and its real-radius growth. It makes no zero-dominance or prime-band
claim. The direct-import stop417 is source-scope evidence, not an
already proved model obstruction. Existing stops235/240/284 remain
unchanged. No cross-notebook input and no mathematical script are
needed. Full matching Mathlib coverage is unchecked and unknown.

Do not execute this new target in step417. Separate approval next turn
must confirm this exact scope before the bounded mathematical test.
