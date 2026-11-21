# Actual-theta specialization of the abstract Fabry obstruction — source coverage

TARGET: Assess paper20 v2 Section3's actual-theta specialization of L828, including Fourier normalization, the Taylor-radius endpoint and the inverse-square moment asymptotic, to prepare one independent audit.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step644 reused steps508/642/643, searched exact xi/Fabry/Bernstein and xi/moment/Romik terminology, and read paper20 Section3, KPS(2.7), DLMF theta identities and Romik Theorem6.1; narrow local checks found no completed actual-theta Fabry application.
SOURCE_EVIDENCE: bramble_trace paper20 v2 (18Oct2026), Theorem1/Section3/(17)–(25); KPS AIF74(2024), Section2.1/(2.7), pp384–385; DLMF20.2.2–4,20.7.28,20.7.31–33; Romik arXiv:1902.06330v3 (5May2019), Section6.1/Theorem6.1/(6.1)–(6.8), pp62–63. Precise links and reading limits below.
COMPARISON: KPS supplies the exact normalized Fourier law; L019 and step508 fix P=K/2. DLMF supplies the theta identities. Paper20 claims the full application; Romik gives sharper integer coefficient asymptotics, not a directly stated real-s inverse-square ratio. The remaining work is a known-source application audit, not a new mechanism.
GAP: Independently verify all actual-density hypotheses of L828, including endpoint continuation and weighted moment tails; no actual-theta obstruction is certified by this literature review and no ordinary-Bernstein sign transfer is covered.
REASON: Essential primary inputs are accessible and the application has a bounded proof to audit. Reproduction is justified by the requested independent reliability check of paper20's delicate endpoint and moment arguments; an automatic import would bypass it.
LITERATURE_REASON: Section3's actual-theta hypotheses lie outside the ready abstract assessment; their primary Fourier, theta and moment-source comparison was essential before mathematical specialization.
SCOPE: Ready source coverage only for the COVERED_TARGET below, retaining all L828 hypotheses. This newly completed coverage receives separate supervisor approval next turn; this turn performs no specialization proof.
COVERED_TARGET: Independently audit paper20 v2 Section3's actual-theta application of L828, checking Fourier normalization, radius R=pi^2/16 with continuation near +R, and the real-s inverse-square moment asymptotic.

## Preserved nomination — step643

The main gap remains actual-Xi all-degree mixed positivity. The
intermediate target would make L828's representation restriction
applicable to the actual density. Its downstream use is to distinguish
an excluded complete-Bernstein mechanism from the still-open ordinary
Bernstein representation/sign question. It does not itself supply signs.

Use L828 as the established abstract input. Read only the needed
Fourier-kernel definition and normalization in L019 (and L018 only if
that normalization requires it); their precise hypotheses must be
checked locally rather than inferred from identifiers. Reuse
2026-11-05-actual-xi-levy-certificate-comparison.md for class comparison
and 2026-11-05-fabry-zero-string-audit-scope.md for the now-audited
abstract imports. The actual source is bramble_trace, paper20 v2,
18 October 2026,
https://rstation.ai/problems/riemann_hypothesis/papers/20,
Theorem1, Section3, equations(17)–(25).

The source review must distinguish the theta cusp at \(i\pi/4\)
from the regular real endpoint, and verify that the moment estimates
cover the inverse-square contribution near zero as well as probability
concentration. Record the primary theta/Fourier inputs and any existing
local duplicate before approving the exact audit scope. No need to
re-audit L828 or repeat the KPS range-access search.

Continue only if all essential sources and exact normalizations support
one bounded application audit. An inaccessible essential input or a
scope mismatch must be named, and the dependent import parked if the
blocker persists. No actual-theta hypothesis has been certified here.
Paper23's supplement blocker and the finite-moment/L822/L825 stops
remain recorded and are not reopened. No cross-notebook input.

Creative-route blocker: this obstruction supplies no assessed condition
on an ordinary Bernstein factor that would yield actual all-degree
mixed signs. A new central sign mechanism therefore has no justified
bounded test in the present source scope; do not label the application
audit creative. Full matching Mathlib coverage remains unchecked.

## Completed source review — step644, 5 November 2026

This literature-only step closes missing source coverage. It does not
verify the theta application or repeat the abstract proof. The main gap
is actual-Xi all-degree mixed positivity. The intermediate target is
reliable application of L828 to the actual Fourier density; its plausible
downstream use is excluding one stronger representation class before
seeking a sufficient sign mechanism in a different class. Actual ordinary
Bernstein membership and sign transfer remain independent unresolved gaps.

### Primary sources and exact scope

bramble_trace, [paper20 v2](https://rstation.ai/problems/riemann_hypothesis/papers/20),
18 October 2026, Theorem1 and Section3, (17)–(25): read the entire
specialization, including both tail cases. It claims the normalized
density satisfies L828, with Taylor radius R=pi^2/16, continuation at +R,
and phi_p(s)~16s/(log s)^2. Its cusp argument uses the alternating
theta transform at t=a+i; its moment proof separately treats inverse-square
mass near zero. These claims remain to be audited. The rendered primary
mathematical body was used; the appended reviewer report was not evidence.

T. Konstantopoulos, P. Patie and R. Sarkar, *A new class of solutions to
the van Dantzig problem, the Lee–Yang property, and the Riemann hypothesis*,
Ann. Inst. Fourier74(2024),377–421,
[Section2.1, (2.7), pp384–385](https://www.numdam.org/item/10.5802/aif.3600.pdf).
Read the displayed Fourier law and following normalization paragraph.
Their eta is the notebook's xi, and their xi is the notebook's Xi.
The displayed density Phi is the source's P and the step508 comparison's
K/2. In these conventions the primary identity is

    Xi(t) = integral_R exp(itx) P(x) dx,
    integral_R P(x) dx = Xi(0),   p(x)=P(x)/Xi(0).

Thus the exact normalized Fourier statement is available by citation;
no frequency dilation or recurrence interpolation is needed. This is
known-source normalization coverage, not a fresh theorem. L018 fixes
the notebook's xi/Xi convention, and L019 supplies the positive kernel
and real tail bound. Their proofs were read for the necessary definitions;
L016's real theta transformation and convergence proof were also inspected.
No Fourier identity was inferred merely from an identifier or DAG row.

NIST DLMF, [20.2.2–4](https://dlmf.nist.gov/20.2#i) and
[20.7.28,20.7.31–33](https://dlmf.nist.gov/20.7#viii):
read the theta2/3/4 series, tau-half-plane domain, translation identity,
and inversion identities with tau'=-1/tau and principal square roots.
In particular the available zero-argument identities are

    (-i tau)^(1/2) theta3(0|tau) = theta3(0|-1/tau),
    (-i tau)^(1/2) theta4(0|tau) = theta2(0|-1/tau),  Im(tau)>0.

The application audit should identify Theta(t)=theta3(0|it), and use
tau=ia, a>0, for the alternating transform. All these substitutions
remain in the specified half-plane. The differentiated estimates needed
at the boundary require an actual convergence argument in the audit;
the transformation formula alone is not that estimate. L016 supplies
supporting real Gaussian-series arguments, not a proved complex cusp.

D. Romik, *Orthogonal polynomial expansions for the Riemann xi function*,
[arXiv:1902.06330v3](https://arxiv.org/pdf/1902.06330v3), 5 May 2019,
Section6.1, Theorem6.1, pp62–63, (6.1)–(6.8): read the moment identity,
full theorem statement, and the proof's changed amplitude and remainder
discussion. The theorem gives an integer-indexed Taylor-coefficient
asymptotic with relative error O(log log n/log n) and Lambert W in its
main term. It is stronger in coefficient precision than the leading-scale
estimate required here. It does not directly state the real-s ratio
M(s-1)/M(s) needed by L828; no ratio or real-parameter extension is
imported from it in this review. Its Chapter2 proof is not fully reread
or independently audited, and this source is comparison evidence only.
The source's cited Griffin–Ono–Rolen–Zagier expansion is an unread lead,
not an extra premise or an essential missing input for paper20's explicit
real-moment argument. No claim of the strongest theorem in the literature
is made.

### Duplication, failures and remaining audit

Reused the class comparison in step508's assessment and the abstract
coverage in step642's assessment. L828's hypotheses, qualification and
Mathlib section were read; its completed string/Fabry proof was not
re-audited. Narrow searches for Fabry, root-zero complete factors,
Taylor radius and inverse-square moments in local lemmas and the relevant
November5 Fabry/Levy assessments, histories and actual-theta/Mellin attempt
records found L828 and the earlier nominations, not a completed application.
The other inverse-square matches concern different variables and were
not loaded. This bounded duplicate check does not establish novelty.

External queries were `"Riemann" "xi" "Fabry" "Bernstein"` and
`"Riemann xi" "moments" "Romik" asymptotic`. Relevant results led to
paper20 and its cited moment literature. Discussion pages, search snippets,
other proposed RH proofs and automatic reviewer reports were not used
as mathematical inputs. The paper23 supplement blocker, ordinary-versus-
complete distinction, and finite-moment/L822/L825 stops remain in force
with their original scopes; none is a proof input to the application.
No cross-notebook source was read.

The next audit is bounded to checking the hypotheses of L828 for this
specified p. It must retain evenness, normalization, positivity near zero,
analyticity and every absolute exponential moment. It must then check
normal convergence in the claimed strip, differentiation of the transformed
theta series along the cusp path, the identity-theorem argument, the
exact squared Taylor radius, and agreement of the local square-root
continuation with the original series. The nonreal cusp and positive
real endpoint must be distinguished throughout.

For the real-s moment part, check the n=1 separation and uniform bounds,
the lower moment estimate's interval and error terms, the denominator
and eventual positivity in the high-tail integration bound, and the
low-tail estimate after division by M(s)/L^2, L=(log s)/2. Check both
weighted tails before using the central interval, take limits for fixed
epsilon before epsilon decreases to zero, and verify all three asymptotic
hypotheses of L828 from the resulting factor. Probability concentration
alone is below the required threshold. No numerical script is needed.

Continue only if every required hypothesis and limit follows with the
stated normalization; then record a known-source reproduction/application,
not a new obstruction or a proof of RH. If any implication fails, preserve
its exact claim and park the unconditional application; a conditional
result must name the unpaid premise. No source blocker currently prevents
this bounded audit. There is no need to repeat supplement access or the
abstract audit. Direct import of paper20 Theorem1 alone would not meet
the requested independent reliability check.

Full matching Mathlib coverage is not checked. L016 records supporting
Gaussian/Poisson and smooth-series results only; no matching formal
theta/Fabry application is claimed. No lemma, mathematical script, PROOF
or DAG was changed in this turn. Source coverage is ready for the named
audit, subject to separate supervisor approval; its truth remains open
locally. No assessed ordinary-Bernstein condition with a sufficient actual
sign bridge supports a creative nomination in this scope.
