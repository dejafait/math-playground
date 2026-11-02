# Universal one-height storage witness: working record

Approved target: test for one centered finite-second-moment measure with
full covariance K, clipped mean at least 1/288, and zero expectation of
every globally C1 positively degree-two homogeneous one-height derivative.
Reuse `literature/2026-10-31-general-homogeneous-storage-scope.md`.
Main gap remains actual-Xi all-degree signs at unbounded heights.

31 October 2026, partial reasoning saved before the full check:
let theta be uniform on [0,2pi], let k independently equal 1/12 with
probability 1/6 and -7/60 with probability 5/6, and put
X=sqrt(2)cos(theta), Y=sin(theta)/sqrt(6), Z=kX.
Then E k=-1/12 and E k^2=1/80. The candidate same-height second
matrix is K_0. Conditional mean Z=-X/12 makes the expected derivative
U_x Y+U_y Z the derivative along the closed ellipse, up to the constant
-1/sqrt(12). This should cancel for every C1 U by the chain rule,
without an angular basis or C2 assumption.

For k=1/12, XZ-Y^2=cos(2theta)/6; for k=-7/60 it is nonpositive.
Candidate clipped mean: (1/6)(1/6)(1/pi)=1/(36pi)>1/288.
Use L473's Schur construction with this changed first marginal to
restore all of K; check centering, all blocks, quadratic W cancellation
via L589, and full-trace implication explicitly. The law is bounded
but has a continuous phase; no finite-atom claim or path realization.

Outstanding at save: full hypotheses/growth and covariance checks,
canonical proof, route checkpoint. If they pass, stop this certificate
class, not general periodic feasibility or Xi signs. If they fail,
retain the failed calculation and classify the bounded test honestly.

Completion: the checks passed in the construction argument, now
canonical in L592. Its exact law, all-U cancellation, full-K extension,
integrability and cost implication are written there. Outcome NEGATIVE:
the full nominated class misses the threshold. This is not an independent
audit; separate conceptual audit coverage is nominated in PROGRESS.md.
No numerical or mathematical script was needed. Earlier working
reasoning above is retained as the interruption checkpoint.
