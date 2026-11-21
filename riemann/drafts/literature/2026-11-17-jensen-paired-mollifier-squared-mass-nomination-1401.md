# Fixed paired mollifier — squared-mass nomination1401

TARGET: Test the O(B) squared-mass bound for C019r's fixed actual-Jensen weighted pair, including every moving-heat channel and the actual-P transfer.
CHECKED: 2026-11-17
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: Reuse the recorded paired/twisted searches and failures comparison in nomination1393/review1394 and source-notes1394; no new search in audit1401. Review1394 explicitly parked squared mass while approving only the first mean; this nomination does not extend that approval.
SOURCE_EVIDENCE: Previously inspected https://arxiv.org/pdf/1609.02539 (recorded v1, Theorems1.1-1.2 pp2-4 and Section2.1-2.4 pp6-10), https://arxiv.org/html/2304.05178v1 (Proposition2 and proof (10)-(14)), and https://arxiv.org/html/1604.00517v1 (Lemma3 proof (2.8)-(2.9)); exact comparison preserved in nomination1393/review1394. No new primary extraction or application is certified here.
COMPARISON: C019r's retained first mean and weighted V squares do not establish the squared weighted pair's fourth-order moment. The prior ordinary twisted fourth-moment sources have different heat, coefficient or taper hypotheses and unevaluated main terms; the fractional product cannot be identified with a truncated Mobius mollifier without proof.
GAP: Coverage for the exact second (M2) inequality, its moving-heat and moving-floor specializations, arithmetic main terms and weighted actual-P error must be assessed separately before calculation.
REASON: Audit1401 retains M1 and removes the reason for parking this independent moment, but the previous ready scope explicitly excluded squared mass. Reuse the existing inspected sources, then resolve only the essential missing scope; do not approve and derive the new moment in one turn.
SCOPE: Exactly C019r/C019m P,T,d,X,q,B,h,D and W; all sufficiently large integer d; L=floor(X^(1/1000)), unchanged alpha coefficients and linear taper, own heat times and both true floors, no RH or random-law premise.
LITERATURE_REASON: The target changes from a signed pair mean and weighted single squares to the squared weighted pair; this is essential coverage outside ready1398, not repeated literature on M1. The unread Selberg import remains parked unless its precise proof is shown to be essential.

## Exact proposed test and scope

Let Q_d(Y)=P(Y)P(Y+h)W(Y), with every symbol exactly as in C019r.
The one proposed target is an absolute C and integer onset d_0 such that

\[
 \int_D Q_d(Y)^2\,dY
 =\int_D P(Y)^2P(Y+h)^2|M(Y)M(Y+h)|^4\,dY\le CB
 \qquad(d\ge d_0).
\]

This is nomination1393's second (M2) inequality. It is a question, not
a consequence proved here. C019r now supplies the first inequality
after an independent conceptual audit, with its exact fixed observable.
Its O(XqA) bound is for integral V(Y+j)^2 W(Y)dY, a different
quantity. No inference from that bound to the displayed target is made.

The essential local context is C019r and its C019l/p/q reductions,
with C019m's actual normalization and C019j/k,L018/L021 inherited
through it. Both true floors, the gamma normalization, the shift and
the heat times must survive a proposed actual-P comparison. The linear
taper and fractional coefficients are fixed; neither an untapered
convolution identity nor a different standard mollifier can replace
them without a paid specialization.

The plausible use is quantitative opposite-sign pair density together
with the retained negative first mean. An actual density argument,
ordered disjoint selection, the reciprocal root map and separation
from existing bulk roots remain later independent obligations toward
the unbounded Jensen deficit and L030-L032/C032a. None is derived
in this nomination.

The bounded continuation test is whether primary-source comparison
supports a concrete calculation of this exact moment with paid
arithmetic and heat-transfer errors. If coverage becomes adequate,
a later mathematical turn should test the displayed O(B) bound or
produce an incompatible rigorous growth lower bound. Failure of an
absolute upper estimate alone does not refute the bound. A persistently
blocked historical import should be parked while a genuinely independent
finite-sum or other covered target is assessed; repeated access searches
are not a new mechanism.

The immediate invocation is literature-only, standard/high theorem
comparison. Reuse review1394's inspected primary statements and relevant
proof cases, checking all six ordinary fourth-moment terms and the
coefficient/taper restrictions before requesting larger passages. Any
ready continuation receives its separate approval; this document
neither approves the mathematics nor performs it. A subsequent proof
route must be chosen from the mechanism actually supported, without
calling an ordinary specialization creative merely to satisfy scheduling.

Stops1345/1355/559/1387/1391 and parked(A) retain their scopes. No
cross-notebook input is proposed. Full matching Mathlib coverage is
unchecked. No lemma or mathematical script is created for this target.
