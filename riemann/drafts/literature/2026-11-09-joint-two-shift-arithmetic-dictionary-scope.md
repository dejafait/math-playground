# Joint two-shift arithmetic dictionary: completed source comparison

TARGET: Assess source coverage and recorded obstructions for uniform bump projection onto the joint two-shift arithmetic dictionary {Z(t+s/log T)n^(-it):s in {-1,1},n<=floor(T^(1/5))}, with L637's fixed bump and T<=X<=2T.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched shifted twisted-second-moment/general-coefficient terminology and exact Hardy bump/joint dictionary projection terminology; inspected Pratt--Robles v3 and followed its BCR reference, reusing the unshifted assessment and the short-dictionary, finite-approval-loop, step226 and collective-row stops. No inspected source settles joint coercivity or this projection; no novelty or exhaustive absence claim.
SOURCE_EVIDENCE: https://arxiv.org/pdf/1706.04593v3 Theorems1.1-1.2 pp3-4, Section2.1 pp4-5, Section3.1 pp6-7, Section3.2.1 pp10-14, Sections3.2.2-3.2.4 pp14-15 and Section4.1 p19; https://arxiv.org/html/1706.04593v3 corroborates the complete mixed theorem and coefficient/weight cases; https://arxiv.org/abs/1706.04593v3 records the corrected Theorem1.2 statement. Reuse BCR https://arxiv.org/pdf/1411.7764v1 Theorem1 and its previously inspected weight cases for equal-shift blocks; reopened https://dlmf.nist.gov/25.10#E3 for Hardy normalization.
COMPARISON: Pratt--Robles Theorem1.2 covers small complex shifts and two independent general polynomial coefficient sequences with an explicit mixed remainder. This supplies the missing cross-moment source, but not a joint lower spectral bound. Its remainder differs from BCR's unshifted remainder. L926 controls one unshifted divisor form; L927 and L637 do not control cancellation between the two amplified blocks.
GAP: The full two-shift Hermitian main form, restored coefficient factors, exact Hardy phase and mixed remainder must be assembled and compared in a later mathematical attempt. Joint conditioning and vanishing bump projection remain unproved; neither is imported from the moment theorem or the separate dictionary exclusions.
REASON: Essential arithmetic source coverage now supports one bounded cancellation-sensitive joint coercivity test. Import the named moment results rather than reprove their arithmetic estimates. Preserve the fixed shifts, length, bump and moving-vector uniformity; do not infer a joint conclusion from separate spaces or approve a new lower bound in this literature turn.
LITERATURE_REASON: The invocation-start target was REVIEW_REQUIRED because the unshifted assessment excluded shifted cross moments and between-block cancellation; Pratt--Robles supplies relevant newly inspected coverage for those changed moment hypotheses.
SCOPE: Exact fixed L637 w,u0,psi,g,Z; shifts s=-1,+1 only; N=floor(T^(1/5)); X in [T,2T]; two arbitrary complex coefficient vectors depending on T,X; weighted L2(w_XT dt). No larger length, growing number of shifts, signed weighted transfer or RH claim.

## Invocation-start nomination, preserved

The prospective source-review instructions below are historical. The
completed comparison following them supersedes their missing-coverage
description; it establishes no new joint estimate.

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
The proposed intermediate question is whether this joint dictionary can
approximate the specified microscopic bump, despite the established
obstructions for the separately studied dictionaries. Its downstream use
is a decision about a concrete actual-function realization mechanism;
even success at approximation would leave signed transfer and Xi signs
unpaid. A vanishing projection bound would close this joint mechanism
at the exact fixed parameters, not settle all mixed dictionaries.

The next turn is literature-only. Inspect exact primary shifted/twisted
second-moment statements and the proof cases needed for their coefficient
and weight uniformity; identify precise versions and direct URLs. Check
the relevant recorded failures narrowly before approving an application.
The unshifted BCR theorem is not permission to substitute a shifted
cross term. Do not infer a bound for the sum of two dictionary spaces
from the two separate exclusion results, or assume Gram invertibility.
An essential unavailable cross-block input must be recorded honestly.

Continue only if known results settle the exact question, or supply a
coefficient-uniform joint moment/error statement supporting one bounded
Gram/projection test. Otherwise record the precise missing cross-block
estimate and park the dependent calculation; do not expand matrix size
or repeat the unshifted or step226 pilots. The two-shift question has
not been mathematically attempted or approved in this audit turn.

Canonical local inputs to inspect later are L637, L737, L926 and L927.
The approved unshifted audit assessment remains unchanged. The possible
new obstruction is between-block cancellation, rather than the already
paid finite inverse bound. There is not yet a source-supported central
creative proof target; source comparison must precede any such routing.
No cross-notebook input is proposed. Full matching Mathlib coverage is
unknown, and the absence of a matching filename is not a novelty claim.

## Completed comparison — 9 November 2026

This is one LITERATURE / NOVELTY_UNCHECKED step, outcome EXPLORATION.
It identifies an adequate arithmetic input and a bounded application
question, without deriving a new main form, lower bound or projection
theorem. L030-L032/C032a, signed transfer and actual-Xi signs remain open.

### Local overlap and recorded failures

Read L637's fixed-data statement and translate/phase argument; L737's
finite logarithmic form, Schur bound and step261 coefficient/window
audit; L926's conclusion and qualifications; and L927's application
and separate audit. Reused the longer-dictionary scope/test/audit
assessments. The short-dictionary stop excludes one unshifted space;
the completed longer-dictionary result excludes another. Neither
controls their shifted joint space. L637's atomic total-variation
cost is not an amplified joint Gram estimate.

Read the finite-conditioning approval-loop closure and the collective
unscaled-row stop. The latter's failed row dominance is not a negative
eigenvalue. Reused the step226 failure comparison already recorded in
the longer-dictionary assessment: finite positive dyadic trials give no
scalable negative family or full spectral bound. The collective and
two-frequency signed arithmetic assessments concern a different
four-factor signed observable and do not settle this second-moment
question. No stopped pilot or unchanged approval loop is reopened.

### Primary theorem, including its mixed-coefficient case

Kyle Pratt and Nicolas Robles, *Perturbed moments and a longer
mollifier for critical zeros of zeta*, Research in Number Theory 4,
article 9 (2018), DOI
[10.1007/s40993-018-0103-4](https://doi.org/10.1007/s40993-018-0103-4).
Use [arXiv:1706.04593v3](https://arxiv.org/pdf/1706.04593v3),
1 June 2018, Theorems 1.1-1.2, printed pp. 3-4, not the abstract's
misprinted second zeta orientation. The
[version record](https://arxiv.org/abs/1706.04593v3) explicitly reports
a correction to Theorem 1.2; the earlier statement is not imported.
The publisher landing page supplies bibliographic data only; its full
text is restricted. The primary arXiv PDF and HTML were accessible.
Shell download failed DNS resolution; that did not block these reads.

Here is the general-coefficient part of Theorem 1.2 in renamed source
variables. Let A(z)=sum_(m<=M) a_m m^(-z),
B(z)=sum_(n<=K) b_n n^(-z), M=Y^theta1, K=Y^theta2, restricted
here to fixed 0<theta1,theta2<1, with the source's general coefficient bounds a_m<<_eta m^eta,
b_n<<_eta n^eta. The smooth weight Phi is supported in [1,2]
and satisfies Phi^(j)<<_j(log Y)^j. For complex
alpha,beta=O(1/log Y) with alpha+beta!=0, put
delta=alpha+beta, d=gcd(m,n).
The theorem states

    integral zeta(1/2+alpha+it) zeta(1/2+beta-it)
               A(1/2+it) conjugate(B(1/2+it)) Phi(t/Y) dt
      = sum_(m<=M,n<=K) a_m conjugate(b_n)/lcm(m,n)
          * d^delta/(m^alpha*n^beta)
          * integral [zeta(1+delta)
                 +zeta(1-delta)*(2*pi*m*n/(t*d^2))^delta]
                        Phi(t/Y) dt + O(E),
    E=Y^(1/2+eta)*(M*K)^(1/4)
       +Y^(3/20+eta)*(M*K)^(7/10)*(M+K)^(1/4)
       +Y^eta*(M*K)^(7/8)*(M+K)^(1/8).

Real positive bases use their real logarithms. Constants retain the
coefficient-bound and weight dependence. The arithmetic estimates are
named imports, not independently certified. No special Mobius/Feng
coefficient hypothesis is imposed in this branch. The explicit
Theorem 1.2 avoids relying on an unstated polarization of a nonreal
shifted observable. Theorem 1.1 has a different stated remainder;
neither is permission to use BCR's smaller unshifted remainder here.

Read the approximate-functional-equation setup, Section 2.1 pp. 4-5;
the diagonal computation, Section 3.1 pp. 6-7; the zero-frequency
combination of both functional-equation pieces, Section 3.2.1
pp. 10-14; all relevant error cases in Sections 3.2.2-3.2.4,
pp. 14-15; and the two-polynomial replacement in Section 4.1 p. 19.
The large-frequency case uses smooth-weight integration by parts.
The nonzero small-frequency general-coefficient case uses Mellin
separation and Lemma 2.2, with the shift powers bounded on polynomial
ranges. The remaining Taylor error is separately bounded. These
operations use common coefficient bounds and smooth seminorms, not
fixed coefficient phases, weight positivity or vector limits. The
specialized Feng/Conrey cases are unnecessary and were not imported.
The deeper Kloosterman estimates remain part of the cited theorem.

### Applicability and qualifications for the later attempt

For a cross block indexed by s,r in {-1,1}, s!=r, the required
source substitutions are alpha=i*s/log T, beta=-i*r/log T.
The exact Hardy conversion uses the weight multiplier

    exp(i*(theta(t+s/log T)-theta(t+r/log T))).

This is the real-axis normalization of
[DLMF 25.10.1-3](https://dlmf.nist.gov/25.10#E3), with the smooth
phase convention already fixed in L637; it divides by no zeta value.
Retain it exactly. L637 Section 4's smooth phase-weight method and
L737's three comparable windows provide the existing applicability
framework. The later proof must display the scaled derivative bounds,
use a common compact smooth-weight family, and restore both coefficient
normalization factors after padding to one fixed source length. The
new cross term is not an entrywise estimate that can be summed for
free. These are explicit application obligations, not assumed joint
coercivity or an already established joint remainder.

The source's displayed auxiliary G divides by (alpha+beta)^2.
For these cross blocks delta=+/-2i/log T, so no uniform passage through
delta=0 is needed; logarithmic losses must remain inside the chosen
positive source error allowance. Equal-shift blocks should instead
use BCR Theorem 1 after the real translation t->t+s/log T, with the
translated smooth weight and corresponding unit-modulus coefficient
phases. That uses the ready unshifted coverage and avoids treating
the singular displayed G as a uniform zero-sum proof. The source's
Remark 1.1 describes the main-term collision limit, not by itself a
uniform operator remainder. No new endpoint theorem is requested.

The source supports general normalized coefficient sequences and
the needed smooth weights. It does not prove a lower bound for the
two-block main form. L926 must be used only in its unshifted scope
unless a later proof establishes the required new finite comparison.
It is acceptable for the bounded test to fail at that comparison.

### Search record and decision

Bounded queries included `shifted twisted second moment zeta arbitrary
coefficients Bettin Chandee Radziwill shifts theorem`, `Pratt Robles
2018 twisted second moment theorem 1.1 arbitrary coefficients shifts`,
`"shifted" "twisted second moment" "lower bound" arbitrary coefficients`,
and exact Hardy bump/joint dictionary projection terms. They led to
the primary Pratt--Robles theorem and its BCR reference. Searches also
returned shifted absolute-moment papers, special mollifiers and generic
projection material; those are unread leads, not evidence for a joint
lower bound. No conclusion rests on search snippets, unrelated online
research logs, or model memory. No exact joint projection theorem was
identified among the inspected sources; this does not certify novelty.

DECISION EXPLORE records sufficient source coverage for one later bounded
joint coercivity attempt, not an asserted specialization theorem.
The sought threshold is a lower bound for ||U||_T^2 with coefficient loss
N^(-1/4), matching the fixed L926 exponent used by L927, for the sum
of the two shifted blocks and arbitrary moving complex vectors. It
would support a subsequent bump-projection decision. A weaker estimate
must be compared honestly with the required numerator and error scales.
An explicit bad direction, or a demonstrated error/margin obstruction,
would instead stop this fixed test; failure of a crude triangle or row
bound alone would not disprove coercivity. Do not enlarge the length,
number of shifts or matrix pilot after an inconclusive result.

The newly prepared continuation assessment is
drafts/literature/2026-11-09-joint-two-shift-coercivity-test.md and awaits
the supervisor's separate approval before mathematical invocation.
This is difficult development of the covered moment route. No central
creative Xi-sign mechanism is ready: signed transfer remains unpaid,
and a routine shifted specialization must not be labeled creative.
Matching Mathlib coverage for the joint theorem or shifted moment
is not checked. No cross-notebook result, new lemma, mathematical
script, PROOF change or DAG edge is introduced in this review.
