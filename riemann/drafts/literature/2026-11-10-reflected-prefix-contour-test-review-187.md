# Reflected angular prefixes of the complete Bell contour — approved bounded coverage

TARGET: Test reflected-prefix cancellation on |x-1/4|=1/2 for L966's complete Bell sum by proving or rigorously refuting B_n(theta)>=(2theta/pi)d_1G(h) for all n>=2 and 0<=theta<=pi/4.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step187's completed paired-contour comparison searched the exact observable, regularized Li/Bell contours and angular-prefix/reflection inequalities; scoped L966/Q_eta duplicate checks found no matching prefix theorem. This bounded search does not certify novelty.
SOURCE_EVIDENCE: Direct primary URLs: https://dlmf.nist.gov/1.9.E30 and https://dlmf.nist.gov/1.9.E31 (Cauchy hypotheses/formulas rechecked step188); https://arxiv.org/html/math/0404213v2 Sections2-3 and https://arxiv.org/html/2204.01036v2 Sections2.2-2.3 (prior full comparison reused, conditional scope rechecked). DLMF 2.4 coverage at https://dlmf.nist.gov/2.4#iv is reused from review186; no source proves TEST.
COMPARISON: Cauchy covers the coefficient-representation tool after normalization checks; the proposed reflection-prefix domination is not a consequence of that tool or of conjugation. The inspected Li contours use different kernels and retain off-line residues; their positive asymptotic branch cannot be imported unconditionally. L967/L969/C969a concern different pointwise theta payments.
GAP: Determine whether actual-theta analytic phase permits this fixed n-uniform signed prefix payment, or certify one strict violation. The full contour identification and prefix inequality remain obligations; complementary arcs and all-index positivity are not covered conclusions.
REASON: Step188 separately approves only a bounded investigation of the specified rule after repairing the missing direct primary URLs; the target and hypotheses are unchanged. This is an independently falsifiable intermediate cancellation test at the central gap, rather than another finite-index Q certificate or an assumed all-degree sign.
SCOPE: Actual L966 F,G,d_k, eta(n)=1/(64*9^n), b=1/4, h=64*9^n, integer n>=2; fixed radius rho=1/2, reflected prefixes 0<=theta<=pi/4. Only local contour verification and the stated signed comparison or a rigorous counterexample; no moving contour, RH, simplicity, Stieltjes measure, unknown zero data or global logarithm.

## Proposed test definitions — not established mathematics

Use exactly L966's finite rational coefficients d_k, entire F, and
G(x)=F'(x)/F(x). Retain every d_k; do not keep selected Bell partitions.
For each integer n>=2 set rho=1/2 and define on the real angular interval
0<=t<=pi the following proposed coefficient kernel and real density:

    W_n(t)=sum_{k=1}^n d_k rho^(1-k) exp(-i(k-1)t),
    J_n(t)=(1/pi) Re[ G(b+rho exp(it)) W_n(t) ],
    B_n(theta)=integral_0^theta [J_n(t)+J_n(pi-t)] dt.

These definitions specify a future test. No identity identifying their
full integral with L966's Bell sum is proved in this literature turn.
The later attempt must verify that identification by DLMF1.9.30-31
applied to G, including k=1, factorials, orientation, the rho Jacobian,
conjugation of the actual function, and all multiplicities inherited
from L966. It must leave -d_1G(h) outside this coefficient integral.
The contour is x=b+rho exp(it), 0<=t<=2pi, positively oriented.
L966's established zero-free neighborhood |x-b|<1 contains this closed
circle and its interior with room to spare. There is no deformation
across unknown zeros and no global logarithm. The integrals here are
finite compact-path integrals; any later use of theta integrals inside
them needs the compact majorant already available in L966, with the
quotient denominator bounded away from zero on the whole circle.

The proposed uniform comparison is precisely

    B_n(theta) >= (2theta/pi) d_1 G(h)
       for every integer n>=2 and every theta in [0,pi/4].    (TEST)

The h on the right is 64*9^n at the same index, not an independent
fixed evaluation point. Both the entire signed kernel and this distant
subtraction are prescribed. G(h)=I_1(h)/I_0(h)>0 is already established
in L966, not a new sign premise.

## Why test this, and what remains unresolved

After the proposed coefficient identification has been verified, the
reflection t versus pi-t partitions the conjugate-paired upper circle
into a parameter interval [0,pi/2]. The proposed prefix bound reaches
only pi/4. Its endpoint is designed to pay half the h-subtraction.
A separate signed lower bound for the interval [pi/4,pi/2] would still
be needed, as would the full downstream sign argument. The test neither
assumes that complementary bound nor claims RH. No deduction of these
prospective consequences is offered in place of the missing proof.
The fixed uniform h charge is a trial allocation to these angular
prefixes, not an imported positivity principle.

Unlike pointwise nonnegativity of a theta tensor or its marginal, TEST
permits negative density within an integrated prefix. Unlike asserting
nonnegativity of the full contour, it is a stronger, separately
falsifiable statement on a proper part of the path. Actual theta
information must do work: analyticity or conjugation alone cannot
establish the comparison. Its plausible use is a first signed payment
input for an eventual complete contour transport, with the unpaid
complement explicitly left open.

Continue only with a uniform analytic argument for TEST, or a
substantial rigorous intermediate bound that discriminates this
fixed pairing and allocation. One explicit n>=2 and theta in (0,pi/4]
with a rigorously negative margin in TEST is decisive abandonment
evidence for this fixed rule. Numerical previews are not certificates;
if used to locate a candidate violation they require rigorous full
error bounds for the complete G, coefficients, angular integral and
h-term. Do not replace a failure by a larger onset, change the reflection
or allocate a different charge within the same attempt. No further
finite-index proof of Q_eta(n)>0 is authorized by this assessment.
If no bound or violation is obtained, preserve partial reasoning and
reassess before repeating; ordinary exploration/recovery rules apply.

## Coverage and approval qualifications

The standard Cauchy application is known mathematics and must be cited,
not presented as a creative result. The new research purpose is the
actual-theta n-uniform signed comparison (or a discriminating obstruction
to it), for which the bounded search established no matching theorem.
A future research classification may be POTENTIALLY_NEW, with precisely
that limited meaning; originality is unverified. No mathematical test
was run or new representation derived in step187. The step187 nomination received separate literature approval in step188;
only this bounded target is ready for a later research invocation.

Essential inputs are L966(2)-(4),(12),(14), L019 and inherited
L018/L024/L026. L967/L969/C969a delimit different failed payments;
L968 is downstream only and L970 is an existing finite base case.
The source comparison and precise links are in the completed step187
assessment named above. No cross-notebook input or essential inaccessible
source is used. Full matching Mathlib coverage is unknown; no absence
claim is made. All-degree signs and complementary angular payment
remain unresolved regardless of any local prefix success.

## Step188 — direct-source recovery and separate approval

LITERATURE_REASON: The supervisor required direct source URLs in this ready
assessment. This limited source/metadata repair preserves TARGET and reuses
the adequate step187 comparison; it is not a renewed discovery search.

The primary [Cauchy formula](https://dlmf.nist.gov/1.9.E30) and
[derivative formula](https://dlmf.nist.gov/1.9.E31), DLMF 1.9.30-31,
were reopened on 10 November 2026. Their hypotheses require continuity
on the closed contour and its interior, analyticity inside, and an
interior evaluation point. The derivative formula covers positive
derivative orders; the first formula covers order zero. The prior
DLMF version record (1.2.8) is retained, not independently revalidated.
L966's local-product proof supplies the proposed domain; explicit finite
coefficient normalization and conjugate pairing remain work for the
mathematical attempt. No contour identity is derived here.

[Voros 2004 v2](https://arxiv.org/html/math/0404213v2), Section2,
(6)-(7), uses a different secondary-zeta contour enclosing poles 1,...,n.
Section3 explicitly qualifies its saddle assertions.
[Voros 2022 v2](https://arxiv.org/html/2204.01036v2), Sections2.2-2.3,
(13)-(20), concerns ordinary Keiper/Li coefficients; its (19)-(20)
positive asymptotic branch explicitly assumes RH. Reuse the full
conditional-case comparison in review186; no new theorem is imported.

Local duplicate/failure evidence is also reused from review186's scoped
L966/Q_eta check and complete L967/L969/C969a comparison. A narrow
step188 search in the recorded Li/resolvent attempt files located the
existing step168 boundary-spreading stop, not a prefix theorem. No
new evidence of novelty or mathematical obstruction was obtained.

Decision: retain EXPLORE for the exact saved TEST and authorize its
later bounded mathematical investigation, with all original error,
h-term, fixed-allocation and abandonment requirements intact. This
turn is STALLED as mathematical/source-comparison progress: it repairs
source traceability and completes separate approval, without a new
inequality, negative example, lemma or script. Full matching Mathlib
coverage remains unknown. PROOF.md and DAG.md remain unchanged.
