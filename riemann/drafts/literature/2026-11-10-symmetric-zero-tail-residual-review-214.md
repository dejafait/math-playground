# Direct symmetric zero-tail residual — completed source comparison

TARGET: Assess a direct symmetric-zero-tail proof of S_f(n)+lambda_n(sqrt(n))=O(sqrt(n) log n), using zero-counting with error instead of the failed horizontal majorant.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step215 searched direct Li-tail truncation, Riemann-von Mangoldt error, Li asymptotics/zero-counting and Oesterle terminology; screened November10 Li/zero assessments and attempts for cosine, arctan and ordinate-only comparisons. Reused reviews158/212/213 and L977's stop. Primary passages and unread leads are distinguished below; no novelty inference.
SOURCE_EVIDENCE: Read Hasanalizade-Shen-Wong arXiv2107.06506v1 Corollary1.2/(1.5), pp.1-3, Section2/(2.1)-(2.3), and its corollary proof p.15; Lagarias AIF57(5)(2007) Lemma4.4/(4.6)-(4.8), Theorem5.1/(5.1)-(5.4), pp.1708,1712-1713, with v4 Section5 cross-check; Arias de Reyna author version 31Jan2011, Theorem1 and full proof pp.4-5, plus normalization pp.1-3; NIST DLMF4.6.1 and its domain. Reused Voros's inspected conditional comparison.
COMPARISON: Unconditional counting with logarithmic error and the archimedean trend are covered. Arias de Reyna covers an arbitrary real-ordinate model, with a normalized l2 error, rather than the actual off-line tail or the requested pointwise rate. L977 still blocks direct contour import. The missing strip-displacement estimate is independently testable without RH.
GAP: The exact corrected residual is unproved: control off-line tail displacement, then a truncated Stieltjes remainder at the required pointwise rate, endpoints and the complete arithmetic normalization. A count asymptotic or an l2 error alone is not that residual. The growing finite-zero sum remains unsigned.
REASON: Essential new source coverage is now available for a bounded specialization attempt, not an import of the requested theorem. No new mathematical result, lemma or script is produced in this literature step; the narrower continuation has a separate assessment for next-turn approval.
SCOPE: Actual zeta, ordinary undivided Li coefficients, S_f as defined in L977 from (4.5)/(4.8), n>=2 asymptotically, weak zero cutoff |Im rho|<=sqrt(n), all multiplicities and off-line contributions, no RH or effective finite zero list. Constants may depend on the fixed zeta function, not n.
LITERATURE_REASON: Changed direct-tail mechanism after L977, requiring the previously unread primary zero-counting error and real-ordinate asymptotic proof; older contour and b_m assessments do not cover this replacement.

## Original nomination, step214

The following preparation text records the prior gate, superseded by
the completed comparison below. Its missing-coverage statements describe
the start of step215, not the final source decision.

## Relevance and bounded test

L030-L032/C032a positivity and L966 signed forcing remain the main
gap. L968's whole-coefficient lower bound at every positive exponential
rate is the downstream benchmark. A sound residual theorem could
separate that sign problem from a controlled zero tail; it would not
make the remaining finite-zero contribution nonnegative.

Review known Li asymptotics and direct symmetric-zero-sum proofs for
the exact formula above. Retrieve the primary zero-counting statement
with its error term and the relevant proof cases before relying on
it. Distinguish a theorem for the fixed zeta function from a result
uniform over arbitrary zero multisets. Compare conditional results
and corrected sign conventions with the published source. Do not
assume symmetry alone cancels all errors or replace off-line zeros
by critical-line points without a justified bound.

Continue only if source comparison supplies either a matching theorem
or a precise, independently testable tail estimate whose missing part
can be stated without RH. Otherwise stop this proposed justification
with its actual obstruction and select a different mechanism. Do not
retry the old b_m envelope or the parked Coffey2007 access route.

Essential continuation context is L977's definitions and audit,
L018's zero correspondence/symmetries, and L968's threshold. L975
identifies the ordinary Li germ; L976 is prior stop evidence, not a
positive premise. Zero-counting and tail-interchange inputs are not
yet covered here. No cross-notebook result is proposed. Full matching
Mathlib coverage is unknown.

This is source preparation for a possible standard asymptotic
specialization, not a creative sign-forcing mechanism. No justified
creative target is ready from this audit: neither a certified residual
nor an independent estimate for the actual growing finite-zero sum is
available. The next turn should compare sources, not derive this
formula under the present REVIEW_REQUIRED assessment.

## Completed comparison, step215, 10 November 2026

The review sought either an exact unconditional residual theorem or a
precise missing estimate. It found the latter. The original corrected
residual remains the research objective; no derivation is asserted here.

### Primary inputs actually inspected

E. Hasanalizade, Q. Shen and P.-J. Wong, *Counting zeros of the Riemann
zeta function*, [arXiv:2107.06506v1, 14 July 2021](https://arxiv.org/pdf/2107.06506v1#page=2),
Corollary 1.2, equation (1.5), p.2, states, for every T>=e,

    |N(T)-T/(2*pi)*log(T/(2*pi*e))|
        <=0.1038*log T+0.2573*log log T+9.3675.

Here N counts 0<Im(rho)<=T in the full strip. Section2, p.3,
identifies its symmetric count with the argument principle, including
zero orders. Thus this is multiplicity counting, not a count of distinct
ordinates. The stated corollary includes endpoints; its contour proof
first avoids them. No quantitative zero clearance or RH hypothesis is
imposed by the corollary. Its proof on p.15 treats large T via Theorem1.1
and the bounded range via the cited argument bound. Those numerical
inputs were not independently replayed. The inspected version is the
preprint; journal metadata identifies JNT235(2022),219-241,
DOI10.1016/j.jnt.2021.06.032, but no version identity is asserted.

J. C. Lagarias, *Li coefficients for automorphic L-functions*,
[AIF57(5)(2007), pp.1708,1712-1713](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=25),
Lemma4.4/(4.6)-(4.8) gives lambda_n=S_infty-S_f+delta.
Theorem5.1/(5.1)-(5.4) gives S_infty=(N/2)n log n+C_1 n+O(N(K+1))
for n>=K, K=max_j|kappa_j|^2 and
C_1=N*(EulerGamma-1-log(2*pi))/2+log Q/2.
The zeta parameters are N=1,Q=1,kappa=0,delta=1; its explicit zeta
constant is (5.4). Reuse L968's completion-normalization justification.
This unconditional trend theorem is separate from the failed Section6
import. It supplies neither off-line displacement nor a tail estimate.

J. Arias de Reyna, *Asymptotics of Keiper-Li Coefficients*,
[author version dated 31 January 2011, Theorem1, pp.4-5](https://personal.us.es/arias/56-2RHB.pdf#page=4),
concerns any nondecreasing positive sequence gamma_j whose counting
function equals T*log(T/(2*pi*e))/(2*pi)+O(log T). With
theta_j=arctan(1/(2*gamma_j)), it states

    (4/m)*sum_j sin^2(m*theta_j)
      =(log m+EulerGamma-1-log(2*pi))/2+y_m,
    (y_m) in l2.

Its complete proof splits the Stieltjes integral into the smooth term
and the counting error. The smooth term has O(log m/m) error; the
other is a sine Fourier coefficient of S(1/(2*tan y)), and is controlled
in l2. No pointwise O(log m/sqrt(m)) estimate is stated there.
The theorem is about a real sequence; the later Corollary2 identifies
it with actual Li coefficients under RH. The paper uses divided Keiper
coefficients; its footnote on p.1 and (6), p.2, specify the factor m.
An l2 assertion must not silently become the requested pointwise rate.

[NIST DLMF4.6.1](https://dlmf.nist.gov/4.6.E1), version1.2.8,
15 September 2026, gives the principal logarithm power series for
log(1+z), |z|<=1,z!=-1. Use only the interior |z|<1, with explicit
uniform remainder control, in the proposed displacement test. This
identity supplies an elementary tool, not that test's conclusion.

### Exact scope of the remaining test

Use the actual positive-ordinate zero multiset, repeating every zero
according to its order; repeated ordinates with different real parts
remain separate entries. The known real-ordinate model is

    K_n(t)=2-2*cos(2*n*arctan(1/(2*t))).

The proposed missing estimate is an absolute bound, uniform in n>=2,
for the sum over gamma>sqrt(n) of the difference between K_n(gamma)
and the actual conjugate-pair contribution

    2*Re[1-(1-1/(beta+i*gamma))^n].

The threshold sought is O(sqrt(n)*log n), with a constant independent
of n for fixed zeta. This is a target, not a theorem or an approved
derivation. A prospective proof must handle the full range 0<beta<1,
the n-dependent exponential, absolute summation and the weak cutoff.
Its source preparation is in
[review215](2026-11-10-offline-li-tail-comparison-review-215.md).
No need to approximate the phase further by n/t is established here.

This comparison would address only one part of the original residual.
The required pointwise truncated Stieltjes estimate and its matching
archimedean constant would still need verification. The low-height
actual contribution is retained, not replaced by its model. L968 needs
the whole Li lower bound at every positive exponential rate; a tail
comparison alone supplies no such sign control.

### Duplicates, stops and source limits

The narrowly screened November10 Li/zero records supplied no previous
tail-displacement proof. Review158 records Mazhouda-Smajlovic
arXiv1511.04603v1, Theorem2/(7): an exact all-degree ordinate-only
replacement encodes GRH. Reuse that inspected warning; no such equality
is proposed. The present test keeps an explicit tail error and all
low-height complex zeros. Reviews212/213 already compare Coffey's
identities and Voros's two conditional cases; they are reused rather
than reopened. L977's printed-contour stop and L976's coefficient
envelope stop remain intact. The Coffey2007 access route stays parked.

Queries included `Li coefficients zero sum truncation sqrt n Lagarias
O sqrt n log n tail`, `Riemann von Mangoldt formula explicit error
O log T theorem N(T) primary`, `Li coefficients asymptotic counting`,
and `Oesterle Li coefficients asymptotic direct proof zero counting
Arias de Reyna`. Search returned later improved counting constants
(arXiv2412.15470), not inspected and unnecessary here. Secondary pages
and external AI research notebooks were not used as theorem evidence.
No exact corrected-residual theorem was found among inspected sources;
this bounded search establishes no novelty or global absence claim.

The author-hosted counting PDF timed out; the arXiv v1 primary statement
and relevant cases were accessible, so this is not a persistent source
blocker. PDF screenshot calls returned placeholders; only primary text
was inspected. DLMF's TeX endpoint was unsupported; the HTML displayed
the formula and domain. Full matching Mathlib coverage is not checked
and remains unknown; no Mathlib theorem is imported.

Outcome: EXPLORATION, LITERATURE, NOVELTY_UNCHECKED. New source evidence
identifies a bounded standard specialization; neither the residual nor
a new lemma is proved. There is no justified creative sign mechanism:
even the tail estimate would leave the growing finite-zero sum unsigned.
The new ready continuation requires its separate next-turn approval.
