# Prime sextic product — bounded application audit

Approved target: the prime sextic product in the saved SPECIALIZE assessment.
Main gap: actual-Xi all-degree positivity; downstream use is one finite-Gauss
input in L546/L548, not coefficient, composite or analytic closure.
Test: exact equality in both residue degrees; stop discharge on an unresolved
phase, conjugation or normalization mismatch. Norm agreement does not suffice.

Saved reasoning before canonical write-up: let H=chi_p, rho=H^2, eta=H^3.
L556 supplies the nontrivial additive character psi and transport of Conrad's
Gauss identities. Euler cyclicity gives exact order six, so H, H^2, H^3,
H^4 are nonprincipal. Cohen Lemma 4.9 gives H(4)J(H,H)=J(H,eta).
Conrad gives tau_1^2=J(H,H)tau_2 and tau_1 tau_3=J(H,eta)tau_4.
All tau_j used are nonzero. Thus tau_1 tau_4=H(4)^(-1)tau_3 tau_2.
The inverse cubic pair is tau_2 tau_4=P, since H^2(-1)=1.
Eliminating tau_4 gives tau_1 tau_2=H(4)^(-1)tau_3 tau_2^3/P.
Division by P yields the exact requested normalized identity.

Cohen is used as an imported theorem for all odd finite fields; the mixed
identity is not reproved. Its principal-character convention does not arise.
No use of L556's cubic-unit evaluation is needed, only its field/additive
normalization and standard finite-field product identities. Inert P=ell^2
uses sqrt(P)=ell, not sqrt(ell). No numerical experiment is required.

Duplicate/failure check: saved assessment and narrowly read prime histories
identify this as retained, not discharged, in L546/L548; the ready cubic scope
excludes it. No new failure is found. The supplied independent source coverage
is reused without new browsing or a new finite-field theorem.

Completed: canonical L557 records the proof and source/Mathlib qualifications.
Direct DAG input is L556 for its field/additive normalization; L546/L548
are downstream interfaces, not mathematical premises. The audit passes
without using the cubic-unit evaluation. Outcome ADVANCE / RESEARCH /
REPRODUCTION, actual task proof_audit. The next all-exponents Fourier
target is separately REVIEW_REQUIRED; no mathematics for it was attempted.
