# Delsarte support certificate — proposed ready continuation

TARGET: Test whether the basic Delsarte LP for A(1024,10,68) certifies B_m(956/1024)<=65537^28/2^128 for every m>=1, using exact rational certificates.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Delsarte constant-weight LP/Hahn theorem statements; local scoped searches found no earlier Delsarte certificate. This is a known-method application, not a novelty claim.
SOURCE_EVIDENCE: Read Kang–Kim–Toan arXiv:1108.5104v1, Section II.A, Remark 3, Theorems 4–5 and equations (8)–(14), pp. 1–2; cross-checked Best et al., CWI scan 6624D, Section 4.2, Theorem 21/equations (11)–(13), printed p. 18.
COMPARISON: L001 and C001b give distinct 68-support incidence vectors with distance at least 10; the Delsarte inequalities apply independently of m and evaluation labels. Their optimized finite-instance value is unknown and need not improve the nested-floor bound.
GAP: Produce a rigorous upper certificate at or below the threshold, or an exact feasible primal witness showing that this basic LP cannot certify it; numerical solver output alone does neither.
REASON: Independently test a standard distance-distribution bound after the triple-transfer review found no usable quantitative theorem; no new counting theorem or unreviewed enhanced LP constraint is authorized.
SCOPE: Basic constant-weight Delsarte LP only, parameters n=1024,d=10,w=68; exact rational primal/dual checks, arbitrary centers, every m>=1, no enhanced constraints or claim of sharpness.

## Primary input

Byung Gyun Kang, Hyun Kwang Kim and Phan Thanh Toan,
[Improved Linear Programming Bounds on Sizes of Constant-Weight Codes](https://arxiv.org/pdf/1108.5104v1),
v1, August 25, 2011, Section II.A, pp. 1–2, Theorems 4–5:
for d even, d<2w<=n, the average distance counts a_i=A_{2i}
satisfy a_i>=0 and sum_{i=d/2}^w q(j,i,n,w)a_i>=-1, 1<=j<=w,
where

q(j,i,n,w)=sum_{h=0}^i (-1)^h binom(j,h) binom(w-j,i-h)
binom(n-w-j,i-h)/(binom(w,i)binom(n-w,i)).

The bound is 1+floor(max sum a_i). Counts average over ordered pairs,
with A_0=1. The ordinary binomial convention assigns zero outside its
range. These are imported Delsarte inequalities, not rederived here.
Original Delsarte sources cited by the paper remain unread.

The independent cross-check is M.R. Best, A.E. Brouwer, F.J. MacWilliams,
A.M. Odlyzko and N.J.A. Sloane,
[Bounds for binary codes of length less than 25](https://ir.cwi.nl/pub/6624/6624D.pdf),
CWI scan, Section 4.2, printed p. 18, Theorem 21. Its theorem has general
n, not a restriction to the small-parameter tables in the title. Use the
readable Kang–Kim–Toan normalization for implementation; do not infer
formula signs from the CWI OCR alone. No additional inequalities from
later sections or external tables are covered here.

## Existing support dictionary and bounded test

The main gap is arbitrary-center safety at 68 agreements. C001b already
selects exactly 68 common agreement columns per candidate, permitting extra
agreements, and L001 ensures distinct supports meet in at most 63 points.
Their incidence vectors therefore have distance
2(68-|S intersection S'|)>=10. This checks the cited theorem's
specialization to (1024,10,68); no subfield descent, scalar projection or
new theorem is required. The alphabet here is the binary support alphabet,
not the received-word field. The resulting certificate bounds the whole
candidate family uniformly in m. Essential inputs are L001, C001a and
C001b; C001a retains C012a/L019 and the ambient threshold. L020 motivates
the route change but supplies no LP constraint.

Set i=5,...,68 and j=1,...,68 in the displayed formula. A numerical solver
may discover a certificate but cannot verify one. A nonnegative rational
dual vector y satisfying -sum_j y_j q(j,i,1024,68)>=1 for every i
would bound sum a_i by sum y_j. Verify all 64 inequalities exactly and
compare 2^128(1+floor(sum y_j))<=65537^28, including safe equality.
Alternatively an exactly feasible rational primal vector with
1+floor(sum a_i)>65537^28/2^128 rules out a sufficient certificate from
this basic LP, without proving an actual large code or unsafe RS list.
These are the standard LP primal/dual verification obligations, not a
computed certificate. Save full exact coefficients, witnesses and checks
under scripts/finite-support/ in the future research turn; print only
bounds, failures and paths. Do not run that calculation during approval.

Continue if a verified upper certificate decides index 956. Abandon this
basic LP as a threshold certificate if a verified primal witness exceeds
threshold; retain any meaningful lesser improvement honestly. Solver or
rational reconstruction failure is unresolved work, not mathematical
exhaustion. The determinant transfer, 67-agreement safety, exact list
maximum and ABF equivalence remain open. Full matching Mathlib coverage:
not checked. This newly written ready assessment needs a separate approval
turn before invocation; no calculation or lemma was produced here.
