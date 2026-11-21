# Far-time joining: source coverage1198

TARGET: Audit Polson v24 Theorem 7.4's far-time joining inequalities at T_N=20000N sqrt(1+log N) and tau_N=1/(4000000N), including N=1 and the separate N=3 choice.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused coverage1194/1196/1183 and application1113/1116; searched exact joining-audit, joining-inequality, joining-constant, joining-comparison and log-rho phrases in local literature, working, history and attempt paths. Read stops1117/1181/1193. External queries were "Polson" "1708.02653" "20000" "Hankel" and "Polson" "finite blocks" "interpolation" "7.4". No independent matching joining audit was located; search completeness and novelty are not claimed.
SOURCE_EVIDENCE: Directly read Nicholas G. Polson, On Hilbert's 8th Problem, arXiv:1708.02653v24, 11September2026, Theorem7.4/(21) and block definition printed p18; Lemma7.7/(26) and entire proof pp19-20; Lemma7.8/(27) p20; Lemma7.9/(28) and proof p21; entire Theorem7.4 joining proof p22. Reused the inspected standard tools in1194 and count/occurrence coverage1196. AppendixA's higher_hankel.py description p51 was read only as a certificate locator; no program was retrieved or executed.
COMPARISON: The source already asserts both the scalar joining bounds and the stronger conditional all-positive-time finite-block conclusion. C030h audits its conditional far-time bound, C030i supplies the actual occurrence/node/count interface, and C030b imports the complete finite theorem. None independently checks these parameter substitutions. Replaying the remaining elementary comparisons is justified by source reliability, with no new theorem beyond the source claimed; do not use Theorem7.4 itself to prove its own far-time hypotheses.
GAP: Independently verify every scalar C030h hypothesis at the stated two parameter choices, including the printed log-rho estimate and special rho3 margin. Keep Lemma7.7's entire near-time conclusion and margins imported. Source statements and proof cases are accessible; none of these joining comparisons is proved or refuted by1198.
REASON: Nomination1197 exposes a scope excluded by1196. This separate literature-only step resolves the exact tau_N denominator and near-time import boundary, and supplies the complete source comparison for a bounded arithmetic/hypothesis audit. New ready coverage awaits separate supervisor approval before research.
SCOPE: All integers N>=1, both parity blocks, actual-zero multiplicities, closed verified low interval and strict high cutoff; general parameters (21) and the separate N=3,T=10000,tau=10^-6 choice. Audit scalar thresholds, their applicability and time coverage only. No independent proof of Lemma7.7, explicit-formula identity, prime/archimedean estimates, source-code certificate, finite zero verification, enlarged degree cap, optimized constants or all-degree sign mechanism.

## Relevance and test

The main gap remains actual-Xi Q(q)>=0 for every polynomial degree
in L030-L032/C032a. Actual-theta signing and graph realization are
independent gaps. The single intermediate target is the joining
comparison inside the cited finite-block proof. Its plausible use is
to finish the far-time applicability check within C030b, relative to
the still-imported near-time theorem. It cannot remove the growing
verification-height premise or establish any all-degree conclusion.

Continue only with a uniform proof for all integer N>=1, with the
separate N=3 parameters checked explicitly. A sampled sweep is
insufficient. Preserve any failed comparison or mismatched hypothesis;
distinguish a failure of a printed auxiliary margin from a failure of
the sufficient threshold rho<1. No source bound passes merely because
this assessment is ready. A source error would affect this application,
not disprove RH.

## Source assertions and exact audit interface

The following formulas are extracted source claims for the later
audit, not new derivations. Theorem7.4/(21),
[printed p18](https://arxiv.org/pdf/1708.02653v24#page=18), sets

    tau_N=1/(4000000*N),
    T_N=20000*N*sqrt(1+log N),  N an integer >=1.

In particular N multiplies 4000000 in the denominator. The theorem
assumes that ALL nontrivial zeros with 0<Im(rho)<=T_N are on the
line. Its alternative N=3 clause assumes verification through10000
and joins at10^-6. No simplicity or absence-of-cutoff-zeros premise
appears. The finite verification theorem itself is an external input,
not an object of the proposed audit.

Use the actual squared exponents and occurrence convention of C030i.
C030h, reproducing Lemma7.9/(28), has the scalar interface

    N>=1 integer, tau>0, T>=max(1000,150N),
    D_N=22500*N^2,
    S_N=sum_(j=1)^N 1/[((j-1)!(N-j)!)^2]
       =binom(2N-2,N-1)/((N-1)!)^2,
    Delta=T^2-D_N-1/4>0,
    tau*T^2>=4N,
    rho_N(T,tau)=(4/10000)*(3/10000)^(2N-2)
                  *S_N*T^(4N)*exp(-Delta*tau)<1.

C030i already checks the positive low exponents, selected distinct
nodes, separation and exact occurrence count under its height
hypotheses. It does not check these scalar thresholds. The later
audit must explicitly show that the chosen T meets its height
interface, so verification through T also supplies verification
through150N. Both parities are then covered by C030h, with repeated
occurrences retained and gamma=T low, gamma>T high. Do not replace
the full algebraic-square form by a modulus-square form.

The entire joining proof,
[printed p22](https://arxiv.org/pdf/1708.02653v24#page=22), asserts,
with L=1+log N,

    tau_N*T_N^2=100*N*L,
    (D_N+1/4)*tau_N<N*L,
    log T_N<10+(3/2)*log N.

It cites L<=N, log20000<10 and S_N<=4^(N-1), drops the factors
less than one in(28), and states

    log rho_N(T_N,tau_N)
      <2N+40N+6N*log N-99N*L
       =-57N-93N*log N<=-57N.

These are the exact claimed thresholds to replay. Justify every
dropped factor and factorial/binomial estimate; include N=1,
empty products, 0!, strictness and logarithm domains. The source's
general argument must not silently start at N=2. Verify Delta>0
and the height and tau*T^2 hypotheses explicitly rather than infer
them solely from the source's sentence that all hypotheses follow.

For the separate N=3 case, that proof asserts

    T=10000, tau=10^-6, D_3=202500, S_3=3/2,
    tau*T^2=100>=12, rho_3(T,tau)<10^-12.

Check these assertions and every other C030h scalar hypothesis under
this separate choice. No floating-point preview certifies the strict
rho3 bound. An elementary analytic comparison or a complete rigorous
interval/rational certificate may be used after approval; only finite
scalar calculations are involved here, with the all-N reduction
proved in prose. No mathematical script is written in1198.

## Precise retained near-time import

[Lemma7.7/(26), printed pp19-20](https://arxiv.org/pdf/1708.02653v24#page=19)
is retained as a preprint theorem input. For epsilon in{0,1},
p real of degree<N and q(x)=x^epsilon*p(x^2), define

    ||q||_G^2=integral_R exp(-x^2)*|q(x)|^2 dx,
    Q_(N,t)^epsilon(p)=4*pi*t^(epsilon+1/2)
           *sum_(i,j=0)^(N-1) v_i*v_j*t^(i+j)*c_(i+j+epsilon)(t),
    c_k(t)=(-1)^k*W^(k)(t),
    r_N=1-1/(2N),
    C_N=r_N^(-(2N-1))/(sqrt(pi)*sqrt(1-r_N^2)),
    eta_N(t)=1-280*C_N*sqrt(t)
          -4*pi*C_N*sqrt(t)*exp((4N-1)*t/4)
          -(4^N/48)*exp(-(log2)^2/(24t)).

The imported lemma states, for 0<t<=log2/180,
Q_(N,t)^epsilon(p)>=eta_N(t)*||q||_G^2, eta_N decreases,
eta_N(tau_N)>0.7 for all N>=1, and eta_3(10^-6)>1/4.
Its proof uses the explicit formula, Lemma6.1's archimedean bound,
Lemma7.6's Gaussian estimates and a prime-sum estimate. It lists
three error margins at tau_N and at the separate N=3 time; those
margins and the underlying analytic proof remain imported together
with the lemma. They acquire no independent audit status here or
from a later successful far-time scalar audit. C030e's near-zero
assembly and the Gaussian work recorded under1183 do not by
themselves certify the full Lemma7.7.

The later joining audit may use this cited near-time assertion
without reproving it. Check that the chosen joining time is within
its stated time domain. The shared positive endpoint must be covered
by the two ranges 0<t<=tau and t>=tau; no assertion at t=0 is needed.
Coefficient scaling and trace identification are already imported
through the existing finite application; do not broaden this step
into another audit of C030a or the full source theorem.

## Search limits, stops, certificate and Mathlib

The exact-phrase local search found the nominations and exclusions
in1193-1197 and the earlier application1113/1116, but no independent
matching parameter audit. Prior assessments are reused while their
targets and assumptions stay fixed. The external queries surfaced
a computing_rh summary pointing to the same result; that summary
was not opened or used as theorem evidence, and its underlying
book is an unread lead. No independent stronger result was inspected.
The exact primary source already contains the target assertion.

AppendixA,
[printed p51](https://arxiv.org/pdf/1708.02653v24#page=51), describes
verification/higher_hankel.py and its forty/sixty decimal interval
runs, including the special eta3 and rho3 margins. That description
is neither a local replay nor a certificate inspected in this turn.
The proposed scalar audit can independently verify the comparisons;
the source program is not an essential missing input or a reason
to repeat source retrieval before mathematics.

Stops1117/1181/1193 retain their original evidence: finite all-time
signs do not automatically give all degrees, the quantitative class
bridge lacks its stated transfer, and the degree/time signed-prime
screen lacks a coefficient-uniform signed estimate. None is a global
ban on different mechanisms. This source review supplies no concrete
new signed input or independently bounded central transfer test, so
there is no justified creative target to nominate in place of the
ready scalar audit. No source blocker persists; Rosser-original
retrieval stays parked because C030i already provides the required
actual-zero input by another inspected primary counting theorem.

Full matching Mathlib coverage for the joining statement is not
checked. Availability is unknown, not asserted absent. A formal
library search is not essential to this arithmetic/hypothesis replay.
No new lemma, mathematical calculation or RH candidate is produced
by this literature-only step. Separate approval is required before
invoking the newly ready continuation.
