# Accelerated-section coefficient norm — separate audit assessment

TARGET: Audit Jerby arXiv:2405.12557v2 Corollary2.2's unweighted ell2 convergence for a_N(k)=sum_(n=k-1)^N 2^(-n-1)binom(n,k-1), 1<=k<=N, against the step vector, and prove convergence or an asymptotic obstruction without changing the cutoff.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The step28 discovery searched exact arXiv identifier/corollary, accelerated Spira coefficient/norm and correction terminology, and notebook-local Hasse-Sondow/Jerby/Spira duplicates. The explicit claim was found in the primary PDF; no matching correction or completed local audit was found. No novelty inference.
SOURCE_EVIDENCE: Jerby arXiv:2405.12557v2, 25March2025, Section2 Proposition2.1/(10)-(18), full finite regrouping proof, Corollary2.2/(19), printed pp5-7, Section3/(21)-(23), p8; DLMF26.3.2-26.3.5 binomial conventions, generating functions and Pascal recurrence, including their displayed domains. PDF text confirms formulas; visual screenshot verification is not claimed.
COMPARISON: This tests the source's own explicit coefficient convergence before any actual-height approximation or zero/sign transfer. Standard binomial identities cover the tools; the original claim is under audit and cannot be its premise. Neither L318's arbitrary-phase obstruction nor L484's different growing Euler-product Haar norm decides this finite binomial norm.
GAP: Determine the actual asymptotic behavior of the stated unweighted norm under the exact cutoff. No coefficient has been evaluated and no contradiction proved. Even convergence would supply no Xi sign, derivative error or zero-stability theorem.
REASON: Adequate primary definitions and elementary finite-sum tools permit one separate REPRODUCTION consistency audit. No new source-dependent saddle estimate is needed. This newly written assessment awaits separate supervisor approval before mathematical invocation.
SCOPE: Integer N>=1, k=1,...,N, source coefficient(13), source step coefficient(18), ordinary unweighted ell2. Test exactly these coordinates with zero extension; record the triangular endpoint issue separately without silently correcting it or changing the cutoff/norm. No RH, real-root premise, height equidistribution, exponential remainder or conjectural approximation is assumed.

The main gap remains L030-L032/C032a. This intermediate target vets
an arithmetic approximation interface proposed for later low-index sign
work. An independently correct smoothing transfer might help choose a
long arithmetic head. It would still require a sufficient signed bound,
complex/derivative remainder control, zero stability and all-degree
assembly. An incorrect coefficient convergence would park this particular
accelerated-to-step justification, not every use of Euler smoothing.

Binding source: Y. Jerby, *On the approximation of the Hardy Z-function
via high-order sections*, [arXiv:2405.12557v2 PDF](https://arxiv.org/pdf/2405.12557v2),
printed pp6-8 for(12)-(23); the arXiv version record is25March2025.
The source explicitly says ell2, not normalized or amplitude-weighted
ell2. Its formula(12) sums k<=N, whereas the preceding triangle(10)
also contains the k=N+1 coordinate after relabeling. The selected test
uses only the common first N coordinates. Retain that qualification;
do not repair the triangle or source's norm during the audit.

Let a_N and b_N be vectors indexed by positive integers, with

    a_N(k)=sum_(n=k-1)^N 2^(-n-1)binom(n,k-1), 1<=k<=N,
    a_N(k)=0, k>N,
    b_N(k)=1, 1<=k<=N; b_N(k)=0, k>N,
    delta_N^2=sum_(k=1)^N (a_N(k)-1)^2.

These are definitions and the proposed test, not a newly derived
identity or bound. Corollary2.2 asserts delta_N->0 along N=floor(t/2).
A rigorous nonvanishing lower bound along an unbounded integer sequence
would falsify this reading. A finite experiment alone does not.
Use exact finite sums and, if useful, an elementary binomial-tail
interpretation whose normalization must be proved. Do not rely on a plot,
rounding-sensitive subtraction, a preview or an unproved limit exchange.
No script is necessary; if used after approval, save its full certificate
and print only actual/required bounds, failures and artifact paths.

Import only the standard identities at
[DLMF26.3.2](https://dlmf.nist.gov/26.3.E2),
[26.3.3](https://dlmf.nist.gov/26.3.E3),
[26.3.4](https://dlmf.nist.gov/26.3.E4) and
[26.3.5](https://dlmf.nist.gov/26.3.E5), retaining nonnegative integer
indices and |x|<1 for the infinite generating function. Their reproof is
unnecessary; the source-specific finite-sum/norm specialization is exactly
what needs checking. No statistical limit theorem is essential.

Essential mathematical input is the explicit source coefficient array
and elementary binomial identities; no local theorem input is needed.
L030-L032/C032a are downstream context only. L318/L484 and the parked
pair/GHS routes are contrasts, not premises. No cross-notebook input.
Upstream Jerby1910.05754's saddle proof and the unread journal version
are not prerequisites for auditing this exact arXiv coefficient claim.
If a different coefficient definition, cutoff or norm is proposed, save
it as a new REVIEW_REQUIRED target instead of changing this audit.

Continue toward approximation/sign work only if this source interface
survives and the still-missing analytic/sign premises are separately
covered. Otherwise preserve the obstruction and park this interface.
Record any result canonically with full qualifications; do not turn a
source correction into a claim about actual-Xi signs or RH. Full matching
and supporting Mathlib coverage are unchecked. Suggested routing is
proof_audit/routine_audit, standard/high, not creative.
