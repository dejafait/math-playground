# Full three-prime law: working checkpoint, step 249

Approved target: Construct or obstruct one signed intermediate law matching every separately fixed log-2/log-3/log-5 cubic cosine coefficient while retaining all L437 constraints.

Prior coverage: `literature/2026-10-19-full-three-prime-signed-law-feasibility.md`
(EXPLORE, supplied before invocation). RESEARCH / proof_attempt;
classification POTENTIALLY_NEW means only that this limited comparison
did not supply the complete construction.

Main gap: global mixed positivity remains unproved. This diagnostic tests
whether the entire three-prime cubic family forces the favorable joint
sign in the selected relaxation. Inputs are L435's bounded continuous
signed density and coefficients, L436's fixed P,I, L437's audited
directions and correction bounds, L431's original tolerances, and
L429/L419/L421's cutoff, Borel matrix and high-component interfaces.
The sign-only/radial failures do not cover these two changed directions.

Candidate mechanism saved before full verification: write f=beta W,
phi=(1,cos(theta_2),P), d=(beta,gamma_2,beta I). Let
G_H=E_H phi(theta(t))phi(theta(t))^T and
r_H=d-E_H[f(theta(t))phi(theta(t))]. If G_H has a uniform positive
lower eigenvalue eventually, set a_H=G_H^(-1)r_H and
f_H=f+a_H^T phi. Then all three old tests are exact at finite height.
Qualitative averaging should give a_H->0 and uniform f_H-f->0,
which would preserve every fixed-character limit without a rate.
Use positive/negative parts of f_H on L437's two supported directions.

Continuation/abandonment test: prove the Gram lower bound, boundedness,
Borel dependence, every old O(log H) cubic error, and all probability,
covariance, support, envelope and cap estimates for the same real-H
family. Do not replace an old tolerance by a weaker limit. Failure of
one of these obligations leaves the proposed law incomplete. Success
would settle this diagnostic's limitation, not justify automatic prime
enlargement. Actual/global realization, actual clipping, capped
nondegeneracy, L413's regulator margin and mixed positivity remain open.

Initial checkpoint status was verification in progress; the text above
preserves the proposed mechanism before its completion.

Completed attempt: the full proof is now canonical in
`../lemmas/L438-full-three-prime-signed-intermediate-counterlaw.md`.
Its (5) proves Gram positivity, (6)--(8) give bounded continuous
calibration and all fixed-character limits, and (9)--(20) verify the
same supported probability family and every original tolerance. No
quantitative full-density averaging theorem or mathematical script was
needed. This is a local ADVANCE, awaiting a separate critical audit;
it is not established originality or progress on RH positivity.
The next assessment is separately marked REVIEW_REQUIRED rather than
approving the newly written proof's audit scope in this research turn.
