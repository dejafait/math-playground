# Two-atom moment coefficients under outward Pollaczek flow

TARGET: Test whether outward Meixner-Pollaczek Poisson flow preserves simple real-rootedness for degree-six alternating polynomials with two-atom [0,1] moment coefficients, using an exact certificate or one bounded search.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: The parent direct-theta discovery searched local Romik/Pollaczek/Hausdorff/flow duplicates and exact moment-restricted hyperbolicity/stronger-preserver queries; no matching result for this finite subclass was located in the bounded search. No novelty or exhaustive-coverage claim is made.
SOURCE_EVIDENCE: Romik, arXiv:1902.06330v3 (5 May 2019), equations (1.1)-(1.11), (3.1)-(3.5), Theorem 3.1 and Section 3.2 proof, Theorems 3.6-3.8 with relevant proofs, Proposition 3.9 and its entire reported example, (A.21)-(A.29); https://arxiv.org/html/1902.06330v3 . The finite test requires only the cited polynomial normalization, recurrence (A.27) and diagonal flow (3.26).
COMPARISON: The source's reported non-even cubic failure does not decide the even alternating two-atom moment subclass. L055/C055a/L057 concern Fourier shape and finite reciprocal-node signs, not this basis-specific outward-flow implication. The standard recurrence and flow are imported; only their restricted finite-dimensional preservation test is proposed.
GAP: Determine the stated degree-six implication or find an exact rational witness to failure; nonempty initial simple-hyperbolic cases must be certified. Neither a finite grid nor a positive result in this subclass establishes arbitrary measures, higher degrees, an actual-theta initial condition or RH.
REASON: This is an independently testable obstruction/invariant discriminator suggested by an inspected actual-theta coefficient formula, before considering a creative all-degree mechanism. No new mathematics is derived or approved for execution in the discovery turn; this newly saved ready continuation receives separate next-turn approval.
SCOPE: One standard algebraic calculation using a fixed degree and moment family; no zero-dynamics collision division, infinite-product interchange, entire-flow theorem or RH premise. New ready assessment, pending separate approval before research invocation.

## Exact finite target

Use Romik's normalization
f_n(x)=P_n^(3/4)(x;pi/2), f_0=1, f_1=2x, and the standard recurrence

    (n+1) f_(n+1)(x) = 2x f_n(x) - (n+1/2) f_(n-1)(x).

For real parameters 0<=q<=1, 0<=u<=v<=1 with v>0 and
m_3>0, define, without any moment-existence theorem,

    m_j = (1-q) u^j + q v^j,  j=0,1,2,3,
    p_r(t) = sum_(j=0)^3 (-1)^j m_j r^(2j) f_(2j)(t/2),  0<r<=1.

Here zeroth powers are 1, also at u=0. The displayed m_j are by
definition moments of the positive probability measure
(1-q)delta_u+q delta_v. Coincident or zero-weight atoms are allowed;
m_3>0 ensures degree six. No unproved moment characterization or
quadrature reduction of arbitrary measures is needed.

Test the implication: for 0<r_0<r_1<=1, if p_(r_0) has six distinct
real zeros, then p_(r_1) has all six zeros real, counting multiplicity.
Increasing r corresponds to decreasing Romik's tau=-log r; this is
the direction toward the undeformed Xi endpoint. The question is not
preservation for increasing tau. No initial hyperbolicity is assumed
for the actual Xi truncation.

Prefer a rational counterexample q,u,v,r_0,r_1 with an exact initial
simple-root count and an exact final deficit of real roots. A later
proof of preservation must cover the full real parameter domain above,
including its allowed atom degeneracies, and separately exhibit a
nonvacuous initial example. Do not treat a finite search as that proof.

## Evidence required and bounded stop

Import the recurrence and finite flow by their equation citations;
derive only degree-six coefficients and the needed exact root test.
Sturm's standard named theorem can certify the real-root counts;
gcd with the derivative handles repeated endpoints. The even polynomial
may be treated as a cubic in t^2, but that reduction and the positive-root
and multiplicity checks must be written out in the research step.
Numerical roots may screen candidates but cannot be the certificate.

One bounded attempt may combine an analytic examination with at most
10,000 explicitly recorded rational parameter tuples, all denominators
at most 32, and exact replay of every claimed witness. Record the tuple
selection, tested domain and initial-hyperbolicity successes as well as
failures. Stop earlier on a certified obstruction. If no witness or
universal proof is obtained, save the partial reasoning and classify
the outcome as inconclusive exploration; do not silently increase
degree, atom count or the search bound. An exact nonvacuity failure
would also change the route, but cannot follow from failed sampling.
Scripts, if subsequently authorized by the separate approval, save full
certificates and print only conclusions, bounds, failures and paths.

## Downstream use and unresolved assumptions

Romik (3.3) is the precise theta-derived lead for positive moment
coefficients; any later use for Xi must explicitly justify the map
y=((x-1)/(x+1))^2 and its normalization/integrability. This review does
not prove that specialization or replace that measure by two atoms.
The current subclass instead tests a proposed general sufficiency
inference on explicit examples. A negative certificate would show
that those restrictions alone are inadequate for an outward-flow
invariant. A positive theorem here would justify only a separate
comparison before extending the family. No independence/realization
for the actual theta measure or root behavior is asserted.

L018 fixes the eventual Xi variable; L024 and L030-L032/C032a identify
the main zero-reality/mixed-form gap. L055, C055a and L057 constrain
generic shape/finite-test shortcuts and are contrasts, not mathematical
premises of this polynomial question. There are no essential local
lemma inputs to the finite algebra beyond the imported standard basis
formulas. Actual-theta initial hyperbolicity, arbitrary moment measures,
all degrees, approximation/root stability and endpoint transfer remain
unresolved. Source Proposition 3.9's numerical proof is not used as a
certified theorem input. Matching Mathlib coverage is not checked;
no cross-notebook result or October half-plane premise is needed.
