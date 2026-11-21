# Conditional far-time bound: source coverage1194

TARGET: Audit Polson v24 Lemma 7.9's conditional interpolation-tail bound (28) for every N>=1 and both parity blocks, retaining its separated-node, counting, height and time hypotheses.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1194 reused1108/1113/1183; searched exact Lemma7.9/interpolation-tail phrases in local lemmas, assessments, working notes, attempts and history. External searches were "Polson" "Far range by interpolation", "heat trace" "Lagrange interpolation" "Hankel" zeros, "1708.02653" "7.9" interpolation, and "Polson" "interpolation" "counting function" Hankel. No separate matching audit was located; neither completeness nor novelty is inferred.
SOURCE_EVIDENCE: Nicholas G. Polson, On Hilbert's 8th Problem, arXiv:1708.02653v24, 11 September2026, https://arxiv.org/pdf/1708.02653v24#page=21, full Lemma7.9/(28) and proof printed p21; Lemma7.8/(27) p20; Lemma6.4 proof p14 and count(10),(13) p13; joining proof p22 read for scope. Directly inspected NIST DLMF3.3(i)/(3.3.1),8.2.2,8.4.8,8.4.11 on2026-11-16; exact links below.
COMPARISON: The preprint already asserts the requested conditional result. Lagrange interpolation and the integer incomplete-gamma identity cover standard tools; they do not certify its weights, endpoint treatment or constants. Independent auditing is justified by the still-imported far-time input in C030b, not by a novelty claim.
GAP: Independently verify the entire conditional estimate and positivity inference below. Node existence from Lemma7.8, the actual-zero count, Theorem7.4's scalar joining comparisons and zero verification remain separate inputs, outside this audit.
REASON: All essential source proof cases for this bounded conditional audit are accessible. Coverage is ready for separate supervisor approval next turn; no inequality has been proved, refuted or independently certified in1194.
SCOPE: General conjugation-invariant locally finite occurrence spectrum under the exact hypotheses below; all real coefficient vectors, N=1, epsilon=0,1, multiplicities and gamma=T endpoint. Standard interpolation, weighted Cauchy-Schwarz, finite-sum integration by parts and incomplete gamma may be used. No actual-Xi node-selection/count proof, bound optimization, Theorem7.4 joining audit, all-degree extension or new signing mechanism.

## Exact source object, hypotheses and claimed estimate

These are the preprint's assertions for future checking, not results
established by this literature turn. Let N>=1 be an integer, epsilon
in{0,1}, tau>0 and T>=max(1000,150N). The spectrum is a multiset of
pairs (gamma,a) with gamma>0, one exponent occurrence per positive
ordinate occurrence, with multiplicity. Conjugation preserves occurrences
and multiplicities. Require

    Re(a)>=gamma^2-1/4,  |a|<=gamma^2+1/4,
    a is positive real whenever gamma<=T,
    N_*(r)=#{occurrences with gamma<=r}<=r^2 for every r>=T.

Assume the spectrum contains N distinct selected real nodes a_j with

    10000<a_j<=D_N=22500N^2,
    |a_j-a_l|>=10000|j-l|  (j!=l, 1<=j,l<=N).

Retain the source threshold conditions

    tau*T^2>=4N,  T^2>D_N+1/4,
    S_N=sum_(j=1)^N 1/[((j-1)!(N-j)!)^2]
       =binom(2N-2,N-1)/((N-1)!)^2,
    rho_N(T,tau)=(4/10000)(3/10000)^(2N-2)
       *S_N*T^(4N)*exp(-(T^2-D_N-1/4)*tau)<1.       (28)

For nonzero P in R[X], deg(P)<N and t>=tau, the proof defines

    L_epsilon(P,t)=sum_(j=1)^N a_j^epsilon exp(-a_j*t)P(a_j)^2.

Its parity-specific claimed absolute tail ratio is

    [sum_(gamma>T) |a^epsilon exp(-a*t)P(a)^2|]/L_epsilon(P,t)
      <=2^(epsilon+1)*10000^(-epsilon)*(3/10000)^(2N-2)
        *S_N*T^(4N-2+2epsilon)*exp(-(T^2-D_N-1/4)*t).

The source uses the epsilon=1 expression to dominate both parities
by rho_N(T,tau). Its claimed full algebraic-square form is at least
(1-rho_N(T,tau))*L_epsilon(P,t)>0. The corresponding raw moment
matrix is [sum_a a^(r+s+epsilon) exp(-a*t)]_(0<=r,s<N).
No modulus-square substitution in that full form is licensed.
The zero polynomial has zero form and is not a strict-positivity test.

## Primary proof cases read and standard inputs

[Polson v24, Lemma7.9, printed p21](https://arxiv.org/pdf/1708.02653v24#page=21)
was read in full, including the weighted interpolation line, separated
product estimate, counting-function integration, finite factorial sum,
both parity factors and final positivity inference. The web extraction
contained the complete displayed expressions; an image-less screenshot
return was not counted as additional evidence.

[DLMF3.3(i), equation3.3.1](https://dlmf.nist.gov/3.3#i) gives the
unique degree<=n interpolant at n+1 distinct nodes, explicitly allowing
real or complex nodes. It covers the polynomial interpolation identity
used with n=N-1; no complex analytic remainder theorem is required.
Weighted Cauchy-Schwarz is a standard named finite-dimensional input.
Check its use with the positive selected-node weights, rather than
reproving a general interpolation theorem.

[DLMF8.2.2](https://dlmf.nist.gov/8.2.E2) defines the upper gamma
integral. [DLMF8.4.8](https://dlmf.nist.gov/8.4.E8) states
Gamma(n+1,z)=n!*exp(-z)*e_n(z) for nonnegative integer n;
[DLMF8.4.11](https://dlmf.nist.gov/8.4.E11) defines
e_n(z)=sum_(k=0)^n z^k/k!. Here only positive real z and integer
parameters occur. Their applicability and normalization must be checked;
there is no branch-continuation issue to import.

The exact scalar tail claim to audit is the source's chain, with
m=2N-2+epsilon:

    sum_(gamma>T) gamma^(2m)*exp(-gamma^2*t)
      <=2t*integral_T^infinity r^(2m+3)*exp(-r^2*t) dr
      =exp(-T^2*t)*sum_(j=0)^(m+1)
          [(m+1)!/(m+1-j)!]*T^(2(m+1-j))*t^(-j)
      <=2*T^(2m+2)*exp(-T^2*t).

The source's stated reasons are t*T^2>=4N>m and successive-term
ratio <=(m+1)/(t*T^2)<=1/2. This is source extraction, not a passed
check. Lemma6.4's relevant finite-count integration argument was also
read. In the audit, justify that argument for arbitrary occurrence
locations by finite sums/ordinary integration and passage to the limit;
retaining boundary terms is necessary to verify the source's strict
cutoff. Do not cite an integer-index Abel formula as an exact theorem
for arbitrary real ordinates. This elementary replay is justified by
the endpoint/multiplicity reliability question, not for a new result.

## Delimited audit obligations and provenance

Check selected-node strictness for every nonzero P, with repeated
occurrences in the rest of the spectrum still counted. Track the
factorial separation denominator and all weights, including the
N=1 empty product and0!. Check absolute convergence of every fixed
matrix entry/tail before regrouping conjugates. For integration, use
N_*(r)-N_*(T) for the strict tail and prove the endpoint at infinity
vanishes; an occurrence exactly at T belongs to the low part. Then
check the finite gamma sum and its geometric majorant, the two parity
prefactors and powers, time monotonicity and the real full-form bound.
No audit verdict is given by this list.

Lemma7.8/(27), printed p20, obtains one occurrence in each interval
(100j,100j+50] from count(10); real selected squared nodes additionally
use line verification through150N. Count(13), printed p13, supplies
N(r)+1<r^2 for actual zeta zeros at r>=1000. Their source proofs were
read to locate assumptions, not independently certified. The conditional
Lemma7.9 audit assumes its nodes and count. C030g's coarse O(T log T)
count alone is not a substitute for this exact r^2 bound at the stated
cutoff. C030e covers the independent near-zero assembly. C030b's
finite application and C030a's transfer are not to be reaudited here.

The Theorem7.4 joining proof p22, including N=1 and the special N=3
height10000/time10^-6 case, was read only to delimit downstream use.
Do not include its log-rho scalar comparisons in the present audit.
An actual-Xi use retains finite line verification; no all-height RH
or simplicity premise is permitted. A successful general-spectrum
check would validate one conditional source input, not certify its
entire zeta application or close L030-L032/C032a.

## Search limits, recorded stops and Mathlib

Local reading/application1108/1113/1116 is reused. Search located no
independent matching Lemma7.9 audit; the L895 multi-pair inverse-power
interpolation certificate is a different target. Stops1117/1181 and
screen1193 remain unchanged: finite-block data do not automatically
extend to all degrees, and no paid uniform signed-prime mechanism is
ready. This conditional reliability test does not reopen those routes.
No justified central creative target emerged; no routine source audit
is relabeled creative to fill a scheduling preference.

The Dufour moments-note URL surfaced as an optional Stieltjes reference,
but direct retrieval timed out; it is unread and unused. Search snippets
and secondary pages support no mathematical conclusion here. Essential
source coverage is accessible through the primary cases and standard
inputs above; this optional timeout is not a blocker. MIT Lecture16
was opened as an Abel locator but adds no input to this target.

Inspected the supporting Mathlib documentation
[Mathlib.NumberTheory.AbelSummation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/AbelSummation.html),
particularly sum_mul_eq_sub_sub_integral_mul: nonnegative ordered
real endpoints, differentiability throughout the closed interval,
integrable derivative, and a natural-number coefficient sequence.
It supports integer-index Abel summation, not the full arbitrary-real
spectrum estimate. Full matching Mathlib coverage for Lemma7.9 is
unchecked; no absence claim or formal verification is made.

Continue only with a complete proof audit under these hypotheses.
Success means an exact conditional proof; failure means an explicit
invalid bound, unmet hypothesis or counterexample, preserved with any
partial work. A source flaw would affect this route, not disprove RH.
No finite numerical sweep suffices for all N or all coefficient vectors.
The newly written ready target requires separate supervisor approval
before any mathematical invocation;1194 performs no derivation.
