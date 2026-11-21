# Fixed support-grid NNLS attempt731

Invocation-start assessment729/comparison730 is SPECIALIZE for exactly the
saved Next action. Main gap: L030-L032/C032a actual-Xi positivity and
signed S3. This attempt addresses kernel preparation only, potentially
feeding C998u's full signed derivative-measure scalar. It neither supplies
the scalar nor the other independent signs, H2, or Xi transfer.

Fixed prescription before calculation: retain j=0,...,255 exactly;
compress the64 blocks J=2^k, k=8,...,71, using degree34 and129 candidate
indices j_i=J+floor(i(J-1)/128), i=0,...,128. These are original support
points, including both extreme original atoms. Use80-digit Decimal
Lawson--Hanson active-set normal-equation NNLS, secondary cap387 and
total main/secondary cap774 per block; no precision/grid adaptation.
Candidate arithmetic is not proof. Stop on failure, unresolved
conditioning, residual budget failure, or complete work above10^8.
The first block J=256 is an early feasibility test; exact rational
enumeration there is paid, not a free use of728 coefficients. Do not
generate the remaining blocks after an informative failure.

The residual is required in the ORIGINAL nu_J inner product of C998v(3),
not in the candidate-grid norm. Fix epsilon<=5e-19 for each block.
Use Piazzon--Sommariva--Vianello2017 Proposition1.2 and Trefethen ATAP
Theorem8.2, as read in assessment729. On the Bernstein ellipse rho=5,
Re(t+3)>0, hence |exp[-J(t+3)r]|<=1 for r>=0 including zero.
The degree34 approximation bound is E<=5^-34/2. Since nu_J mass<1,
the imported residual theorem bounds a block's original-kernel error by
[5^-34+epsilon(1+5^-34)]/(4J). Summing k=8,...,71 and multiplying by
B^2=2^46 gives less than2^37 times the bracket. Add the unchanged
tail2^46/(4*2^72-3). Exact comparison with1e-7 is to be saved.
This is a standard source specialization, not a new residual theorem.

A failure may be certified without computing an orthonormal basis:
an exact rational polynomial q of degree<=34, nonnegative on every
candidate, with negative original nu_J integral, separates the moment
target. Cauchy--Schwarz in the original measure bounds every feasible
orthonormal residual below by -integral(q)/||q||_nu. Full original
moments through68, or equivalent direct original-support sums, must
be used. A candidate-grid norm is not evidence. This elementary finite
application is within the approved original-measure residual test.

Continue only on a certified residual plus the stated uniform budget,
positivity and complete all-work/storage ledger; otherwise stop this
fixed prescription. Neither a residual failure nor a separator proves
actual exponential error above1e-7 or rules out other candidate grids.
Preserve729's bisection stop,100-digit failure and prior route evidence.
No justified creative signed remote-plus-induced S3 mechanism has yet
been nominated. Save completed evidence below before choosing a new
target and its separate source gate.

## Completed bounded attempt

C998w is canonical for the three finite rules, the original-Gram
inverse-residual proof, source specializations and exact qualifications.
The fixed grid passed the first THREE blocks J=256,512,1024:35 positive
original-support weights each, original-orthonormal residual squared
<3e-155, and13 validation checks each. Raw Chebyshev residuals and
NNLS stationarity were not used as a certificate. All69 original
moments were generated exactly and the entire35-by35 inverse error
was checked outward. No728 coefficients were read or priced as free.

The separator diagnostic did not find an obstruction: its original
integral was positive in all three instances. The preliminary first-block
certificate preserves those failed negative-integral discriminator tests;
they are not mathematical failures of the feasible grid. Initial k=10
serialization exceeded Python's4300-digit integer conversion limit;
writing the selected complete exact values resolved this output issue.
The final per-k certificates have no failed validation checks.

This turn stops at a partial feasibility checkpoint, NOT at a negative
route verdict or a successful full construction. Moving to the61
remaining blocks requires implementing the covered finite-moment
preparation rather than support enumeration, propagating its errors
through original-Gram validation and paying the complete work/storage
ledger. That preparation has not been implemented here. The script's
direct-support entry point is bounded at J<=4096; only k=8,9,10 were
run. Original-value storage is69J Fraction entries, plus the129-square
candidate Gram and validation arrays; no byte upper bound is claimed.

Conditional on ALL64 block residuals<=5e-19, the exact prescribed
uniform bound is<7.245e-8, but this premise and the10^8 complete-work
cap remain unproved. Three passing small blocks do not prove feasibility
at large J, nor any full scalar or sign. Outcome EXPLORATION records
this unfinished fixed-prescription attempt without promoting its small
instances to a full preparation result or a central-gap advance.

Continuation retains the exact approved target and unchanged assessment729;
no additional source review is needed for that covered specialization.
Keep the degree34,129-index grid,80-digit candidate solver,100-digit
validator,387/774 iteration caps and residual5e-19 fixed. Stop on a
failed block, unpaid essential hypothesis or above-cap complete ledger;
otherwise validate remaining blocks and account for every preparation,
candidate,arithmetic/control and storage cost. C998w and its three
certificates are reusable finite inputs, not evidence for untested blocks.
The continuation is still routine numerical specialization, not creative
signed remote-plus-induced S3 domination. No justified independent
central creative mechanism was supplied by this test.
