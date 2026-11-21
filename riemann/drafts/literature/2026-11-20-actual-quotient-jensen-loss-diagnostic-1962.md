# Actual quotient Jensen-loss diagnostic1962

TARGET: Test whether a fixed positive-real interval forces a strictly positive ordered-limit Jensen excess for the actual q=1/2 quotient moment in C028d's central-payment comparison.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1962 checked exact quotient/fractional/Jensen terminology and local height/entropy stops, and compared primary norm/convexity inputs. See drafts/literature/2026-11-20-reference-normalized-fractional-source-notes-1962.md for queries and limits; no exact actual-family loss theorem was found and no novelty is inferred.
SOURCE_EVIDENCE: Cover--Thomas, Elements of Information Theory (1991), Theorems2.6.1-2.6.2 pp24-26, https://sites.stat.columbia.edu/liam/teaching/neurostat-spr11/papers/EM/Cover%26Thomas-Ch2.pdf; integrability-qualified Jensen, https://www.statlect.com/fundamentals-of-probability/Jensen-inequality; O'Sullivan arXiv:2007.13582v2 Introduction(1.2)/Section3.1, https://arxiv.org/html/2007.13582v2. Reuse C028f's ready actual order-growth bound and C028g's finite-height limit, not conditional hyperbolicity. Relevant source statements/proof cases are recorded in source-notes1962.
COMPARISON: Known convexity and growth tools cover the method; the unproved difference is their quantitative fixed-interval application to the actual P_d and changing uniform measure. C029e only treats a numerator reference cost. Torus norm bounds and strictness without a rate do not settle this diagnostic.
GAP: Check quotient-moment finiteness with all multiplicities, the exact normalized excess, and whether one fixed interval yields a positive lower bound surviving d first and A last. No degree-root asymptotic or excess bound is asserted in this assessment.
REASON: A bounded standard-method specialization can discriminate the changed normalization before any full upper-estimate attempt. It uses ready actual-family inputs and does not depend on Carbery--Wright or a real-root premise. Newly written ready continuation requires separate approval next turn; no mathematics is invoked here.
SCOPE: Only the actual C028d Q_d(y)=P_d(y-b_1), d>=3, q=1/2, fixed A>=max(1,2sqrt(M)) with M from C028e, nu_(A,d) uniform on [-Ad,Ad], all multiplicities, and the proposed fixed interval y in [b_1+1,b_1+2]. REPRODUCTION. Full upper payment, shrinking-q variants, new reference laws and RH are outside the approved method scope.

## Proposed bounded test; no mathematical conclusion

Keep the observable in assessment1961 and define a diagnostic excess

    Z_(d,A)=integral |Q_d(y)/y^d|^(1/(2d)) dnu_(A,d),
    D_(d,A)=4Ad log Z_(d,A)
              -d^(-1) integral_(-Ad)^(Ad) f_d(y)dy.

The test is whether

    liminf_(A->infinity) liminf_(d->infinity) D_(d,A)>0.

First verify finiteness, positivity almost everywhere, log integrability
and the exact Jensen factors; zero and all real roots remain null-set
exceptions, not excluded cases. Then test the fixed-positive-x
degree-root behavior of P_d on x in [1,2], using its positive coefficients
and C028f's entire-growth bound. Translate only through y=x+b_1.
If a uniform interval statement is justified, test a quantitative
exponential convexity remainder, retaining the probability mass of that
interval as d changes. C028d/e/g may control the mean term; neither
the full positive partition integrand nor its complement may be silently
discarded in a signed comparison.

These are proposed operations and intermediate questions, not derived
identities or estimates. Import source theorems rather than reprove
them. Any quantitative application belongs to the later mathematical
step. A fixed-degree strict inequality alone does not meet the test.

Continue this fixed-q payment only if the actual loss is shown compatible
with the required zero upper threshold, together with a separately
reviewed upper-control idea. A strictly positive ordered-limit lower
bound would instead stop this normalization; explicitly check its
implication using C028d/e and H_d>=0 before declaring that stop.
If neither alternative is established in the bounded attempt, preserve
the partial reasoning and park it pending a materially new input.
No theorem in this review declares the loss positive or zero.

Essential inputs: C028d/e/f/g with unchanged b_j, b_1, M and all
multiplicities. C029e and stops1959/1961 motivate comparison only and
are not positive lower bounds for this observable. Unresolved obligations:
finite quotient moment, quantitative interval behavior, degree-uniform
mean/remainder control and the final ordered-limit sign. A positive
loss is not an actual off-line zero; a vanishing loss is not the missing
actual partition upper estimate. Full matching Mathlib coverage is
unchecked/unknown.
