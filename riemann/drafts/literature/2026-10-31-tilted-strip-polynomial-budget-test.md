# Tilted finite strip-polynomial budget: source scope

TARGET: Determine whether real exponential tilting makes L571's strict norm certificate equivalent to D_1<0 for P_a(z)=(1+4*z^2)*(1-a*z^2), 0<=a<=4, by finding the optimal tilt and exact certification range; treat this solely as a finite strip-polynomial obstruction test.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded searches for Hardy-norm exponential tilts, quartic Laguerre/disk-Hardy comparisons and the exact polynomial expression found no inspected matching norm-versus-sign theorem. Narrow exact-expression/tilt checks in L469/L488/L489/L571 and the named shared-budget/Hardy assessments found no completed version of this norm diagnostic. Search details and limits are in drafts/2026-10-31-tilted-xi-norm-source-working.md; no novelty is claimed.
SOURCE_EVIDENCE: Csordas arXiv:1309.0055v2 https://arxiv.org/pdf/1309.0055v2, Definition 1.1/(1.3), p.2, first-sign counterexample before Remark 2.1, p.3, Proposition 2.3/(2.4)--(2.6), pp.3--4 and generating identity (2.11), p.4, with relevant proofs read. Reuse ready Hardy coverage in drafts/literature/2026-10-31-l571-independent-budget-audit.md, including https://arxiv.org/pdf/2412.11473v1 Section 4.1 and https://arxiv.org/pdf/1912.05715v1 Sections 3.1--3.2/Proposition 3.6; L571's thresholds are already independently audited.
COMPARISON: Known generating/sign identities and the H2 boundary/coefficient norm supply the tools. The source Gaussian example already refutes generic first-sign sufficiency; that is not the question being retested. The bounded difference is whether real tilt removes the failure of the strict sufficient norm certificate, within a finite polynomial subclass with other zeros retained. No inspected source computes its optimal tilted norm or exact certification interval.
GAP: Verify class membership and exact multiplicity, minimize the boundary norm over every real tilt, compare the resulting norm with L571's N_1 at r=1/2,m=1, and separately compare with the actual D_1 sign, including strict-budget and parameter endpoints. None of these calculations has been performed in this assessment.
REASON: This independently testable diagnostic replaces the unsupported unconditional Xi estimate by a bounded classical specialization. General Hardy theory and the known sign counterexample should not be reproved; the family-specific norm comparison is necessary to measure the certificate's lost information. Newly written readiness receives separate supervisor approval next turn.
SCOPE: Real 0<=a<=4, real lambda, F_(a,lambda)(z)=exp(lambda*z)*P_a(z), unit-circle normalized squared H2 norm as in L571, designated zeros +/-i/2 of exact order one, real symmetry and F(0)=1; other zeros explicitly allowed. No actual-Xi realization, Gaussian approximation, zero-free quotient, zero separation or height estimate is assumed.

The main gap remains all-degree actual-Xi positivity and unbounded-height
initial signs. The intermediate question is the precise norm-versus-sign
comparison for this finite family. It can decide whether a linear
exponential normalization alone is a faithful detector even in a small
strip-polynomial class. A failure would require independent information
on the remaining amplitude before applying the normalization to Xi;
success would only quantify a model certificate, not supply Xi data.

The Gaussian source example has order two. It motivates the comparison
but is not passed off as an order-one Xi countermodel. This test instead
uses a finite polynomial multiplied by a real linear exponential, the
kind of finite product expressly admitted in Csordas Definition 1.1.
The designated roots, other roots, real-strip location and exact orders
must be checked directly in the mathematical turn. Source (2.11) covers
the exponential's effect on first-sign coefficients. It does not choose
an optimal tilt or assert a norm bound.

The existing shared-budget comparison concerns distributing real-zero
charges among two displaced nonreal pairs; it does not optimize this
disk boundary norm. L571's sign-competitor extremizers are in a larger
neighborhood-analytic class. Their sharpness does not calculate the
infimum over the single tilt orbit of this specified polynomial. The
September inverse-curvature stops and L469's collision hypotheses are
different questions, not reasons to repeat or dismiss this test.

Use the known H2 coefficient norm/Parseval identity and elementary real
inequalities if sufficient. The linear projection and confluent-kernel
theorems need not be reproved or invoked for a calculation that reduces
to a finite polynomial. No Bessel analysis or mathematical script is
essential to the nominated test. Sign facts already covered by the
generating identity should be cited, not presented as new discoveries.
The additional DLMF Bessel reading in the parent working record is
unused optional coverage, not an essential input.

Continuation/abandonment test: determine the exact optimal norm and
strict certification range on the stated compact parameter interval.
Compare them with D_1<0. An explicit interval missed by every real tilt
is an informative obstruction to treating the norm test as an equivalent
first-sign detector; preserve it and stop that blanket claim. If there
is no such interval, record precisely the surviving finite-model range.
Either outcome leaves actual-Xi norm/residual control, center zeros,
all-height uniformity and higher signs unresolved. Do not enlarge the
model or repeat optimization scans without a materially new input.

Essential input ID: L571. L018 is needed only to explain the eventual
Xi obligation, not as a premise of this finite calculation. No
cross-notebook input. Full matching Mathlib coverage is unchecked.
This is a REPRODUCTION/classical calculation recommendation at
standard/high, not proof_attempt/creative. A central creative Xi target
still lacks a specified independent residual estimate or geometry test.
