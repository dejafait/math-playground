# Joint two-shift dictionary: bounded coercivity test

TARGET: Test whether the joint two-shift arithmetic dictionary at N=floor(T^(1/5)) has a coefficient-uniform squared-norm lower bound c*T*log(T)*N^(-1/4)*(||c_-||_2^2+||c_+||_2^2), retaining the exact shifted moment main form and charged errors.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed changed-scope comparison in drafts/literature/2026-11-09-joint-two-shift-arithmetic-dictionary-scope.md, including its general-coefficient shifted-moment searches, primary theorem reads and local failure comparisons; no exact joint coercivity/projection result was found among the inspected sources and no originality is claimed.
SOURCE_EVIDENCE: https://arxiv.org/pdf/1706.04593v3 Theorem1.2 pp3-4, Section2.1 pp4-5, Sections3.1 and3.2.1-3.2.4 pp6-15 (relevant general-coefficient and weight cases), Section4.1 p19; complete theorem corroborated at https://arxiv.org/html/1706.04593v3 and corrected version identified at https://arxiv.org/abs/1706.04593v3. Equal-shift inputs reuse BCR https://arxiv.org/pdf/1411.7764v1 Theorem1 and L737/L927's audited weight application; Hardy normalization is https://dlmf.nist.gov/25.10#E3. Exact formulas and qualifications are retained in the completed scope comparison.
COMPARISON: The mixed-polynomial theorem supplies a coefficient-sensitive source framework for the two opposite-shift cross blocks. L926 controls only the unshifted divisor form; L927 supplies neither joint conditioning nor a sum-of-spaces projection theorem. The proposed lower norm bound remains the mathematical target, not an imported conclusion.
GAP: Assemble the exact two-block Hermitian main expression and homogeneous error, then seek or obstruct the stated lower margin uniformly in X and both moving complex vectors. A separate spectral comparison and error absorption are essential; no invertibility, positive gap or successful projection exclusion is presumed.
REASON: Essential moment-source coverage is adequate for one bounded attempt on cancellation between two amplified translates. The finite-conditioning and single-dictionary routes are complete; the new target changes the mixed space without repeating their proofs or the parked signed dyadic pilot.
SCOPE: L637's fixed w,u0,psi,g,Z; L=log T; T<=X<=2T; N=floor(T^(1/5)); U(t)=sum_(s=-1,+1) Z(t+s/L) sum_(n<=N)c_(s,n)n^(-it); weighted norm in L2(w_XT dt); all complex vectors c_s including T,X-dependent ones; a positive constant c independent of T,X and the vectors, beyond one common existential onset. No larger length, extra shifts, signed transfer or Xi signs.

This assessment is newly written after the invocation-start literature
gate. It requires the supervisor's separate approval before a research
invocation; no mathematics was performed or approved retroactively.

Essential local inputs are L637 (normalization, fixed data and smooth
phase method), L737 (finite logarithmic form and uniform weight/coefficient
application), audited L926 (one-block finite conditioning) and audited
L927 (unshifted application and its error accounting as a comparison).
L925 is not a premise. No cross-notebook input is proposed.

For the cross terms use the two-independent-polynomial case of
Pratt--Robles Theorem1.2, with shifts alpha=i*s/L, beta=-i*r/L,
s!=r. Retain its full two-term zeta/gcd expression, exact Hardy phase
and all three terms of its general-coefficient remainder. Specify
common source coefficient bounds after normalization, restore both
normalizing factors, and justify any padding and common smooth-weight
seminorms before claiming uniformity. Do not sum an entrywise error
without its dimension or coefficient cost. The different remainder in
BCR's unshifted theorem is not available for these cross blocks.

For equal-shift blocks use real translation and BCR under the ready
unshifted coverage; track the translated weight and coefficient phases.
The displayed Pratt--Robles pole annihilator is singular at zero shift
sum, so its printed formula is not a uniform proof through that sum.
For opposite shifts the sum is +/-2i/L; retain any logarithmic losses
inside a fixed positive source error allowance. No stronger collision
theorem or new arithmetic estimate is needed or presumed.

The bounded test is the lower norm bound in TARGET, with the full
source error absorbed. Success would allow comparison with the fixed
bump numerator to decide this realization mechanism. Failure must
identify an actual bad coefficient family, an unavoidable error/margin
obstruction in this application, or a specific unpaid finite estimate.
A failed crude triangle/row bound is not a disproof of the target.
If the stated bound remains unresolved, preserve the reasoning and
park this attempt unless a materially new comparison is identified;
do not expand the matrix, length or shift count to repeat it.

This is established-route development, not a promised new discovery or
a central creative Xi-sign argument. Remaining independent gaps include
signed weighted transfer, realization for other spaces and actual-Xi
all-degree mixed positivity L030-L032/C032a. Full matching Mathlib
coverage remains unchecked. The arithmetic theorem proofs remain named
imports, and no RH hypothesis or nonvanishing at the bump center is used.
