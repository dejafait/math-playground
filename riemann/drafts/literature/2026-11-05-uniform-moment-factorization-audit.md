# Uniform moment factorization — conditional conceptual audit gate

TARGET: Audit the contour and relative-error inference in Michalowski v1 Lemma3.6 for k>=10^9 and |z-k|<=k/20, taking its preceding bounds as explicit cited hypotheses and identifying any unverified constants.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step465 reused step385 and named coefficient stops, checked exact source and correction terms, and read the complete selected proof and antecedents; no prior audit at this exact scope was identified in those selected records.
SOURCE_EVIDENCE: Michalowski arXiv:2607.16795v1 Section3, Lemmas3.1–3.6 and complete proofs, Proposition3.7; Theorem1.1 and Sections4–6 provide downstream context. Primary URL and scope below.
COMPARISON: The factorization is a source claim, not a new theorem. This checks its analytic inference conditional on printed tube/saddle/derivative bounds; it neither assumes those independently audited nor imports the whole cubic wedge.
GAP: Verify the complete normalized error budget and analytic branches, or isolate the precise failed inference. Antecedent constants remain qualified; no actual-I zero-free disk is yet locally verified.
REASON: An independently testable analytic input underlies the growing-order source result. A conditional conceptual audit can validate or stop this interface without reopening L765/L774 or inventing an all-degree sign estimate.
SCOPE: One conditional proof audit; no enlarged scan, wedge optimization, whole-manuscript certification or new central positivity mechanism. Newly written ready assessment requires separate next-turn approval.

Primary source: W. Michalowski,
[arXiv:2607.16795v1, Section3](https://arxiv.org/html/2607.16795v1#S3),
*An explicit uniform cubic wedge for consecutive Toeplitz minors of the
Riemann xi coefficients*, 18 July 2026. Numbering binds to v1.

Use L019/L021 and L786's already checked kernel normalization; L776
only fixes ordinary coefficients. The source scalar saddle-map K
is not L019's theta kernel K. Write Phi for the source kernel, with
K_local(u)=4 Phi(u/2). No Fredholm or zero-count premise is used.

The source defines I(z)=integral_0^infinity u^(2z) Phi(u)du,
the real first-summand saddle u_k, sigma_k=sqrt(u_k/k), and the full
phase Psi_z(u)=2z log(u)+log(Phi(u)). Its full saddle is u_s(z).
The claim under audit is

    I(z)=exp(Psi_z(u_s))*sqrt(2pi/(-Psi_z''(u_s)))*(1+epsilon(z)),
    |epsilon(z)|<0.018, integer k>=10^9, |z-k|<=k/20.

Antecedents are Lemmas3.1–3.5's tube nonvanishing, analytic saddle and
localization, horizontal concavity, and local second/third derivative
bounds. State each actually used bound as a precise cited hypothesis,
with its domain; distinguish rounded from certificate-only constants.
These were read, not independently audited. Ancillary code is unnecessary
for a conditional inference check; naming a certificate is not its replay.
If stronger constants are essential and cannot be justified from inspected
input, record the conditional limitation rather than assume success.

Bounded test: check contour deformation at zero/infinity, transition
to the full phase, local complex Gaussian comparison, both horizontal
tail regions and radial connector in one normalization. Track the
nonzero main-term lower bound and principal square-root analyticity.
The sum must yield relative error strictly below 0.018 throughout
the disk. Sampling is insufficient. Do not differentiate an unknown
remainder or assume I nonvanishing to define its logarithm.

Continue only if the inference follows under explicit antecedents;
record a conditional reproduction retaining remaining assumptions.
Otherwise isolate the first failed inequality/domain or unpaid constant
and stop propagation. A valid changed constant is distinct from the
printed one; do not silently repair the theorem or pursue a second
mechanism within the audit.

Plausible use: Proposition3.7's uniform Taylor control for growing-order
coefficient tails. Antecedent constants, other wedge gates, bounded k/r,
other indices and global signs remain independent gaps. L765/L774 are
contrasts, not inputs. No creative route or RH candidate is asserted.
Full Mathlib matching coverage is not checked.
