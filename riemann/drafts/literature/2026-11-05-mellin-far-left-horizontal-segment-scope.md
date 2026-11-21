# Far-left horizontal theta-Mellin segment: completed source comparison

TARGET: Assess the standalone far-left theta-Mellin segment from i y_L to u/2+i y_L against 600u^(5/2)sqrt(47Q/(20pi))(1+10u/Q)exp(-Q/(20u)) on all D, including the h=0 improper endpoint.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step530 searched exact Mellin/far-left/theta/600 phrases, weighted Gaussian-sum bounds, unimodal sum-integral comparison and complex-theta derivatives; narrow local searches in Mellin assessments, histories and the global-import stop found no completed matching segment bound. Primary sources below supply effective methods, not the nominated constant. No novelty inference from search failure.
SOURCE_EVIDENCE: Reinspected bramble_trace paper23 v1 (18 October 2026), Section3 Lemma2 (10)–(14), https://rstation.ai/problems/riemann_hypothesis/papers/23; NIST DLMF v1.2.8 (2026-09-15), 20.2.3/20.2(ii), 2.10(i)/2.10.1, 5.9.1 with its following hypotheses, 5.2.1 and 2.5(i)/2.5.1, accessed 2026-11-05. Reuse the limited Devroye comparison in the finite-left assessment; exact links and applicability below.
COMPARISON: Effective Euler–Maclaurin and gamma-integral methods cover real Gaussian-moment majorants and endpoint convergence conditionally; theta analyticity is available inside the strip. They supply no uniform far-left phase loss, angular cancellation, chosen split or 600,Q/(20u) payment. L802's concavity and tau>3 are not extended to zero.
GAP: Establish the improper limit and a uniform full-series majorant, retain the complex-power angular factor, bound the entire interval relative to the saddle and pay the exact normalization on both closed boundaries, both signs of h, h=0 and unbounded u; or isolate a rigorous obstruction to the sufficient majorant method.
REASON: Accessible primary effective methods remove the essential source-method blocker for this independently defined integral. A separate known-method specialization attempt is justified; neither the source budget nor unread global-contour supplements are premises, and no far-left inequality is proved by this review.
LITERATURE_REASON: The lower real endpoint changes from u/2 to 0; full-segment angle and theta-amplitude coverage is absent, and an improper-endpoint case is introduced. This is new essential source scope, not further browsing on the already audited L802 target.
SCOPE: Completed literature-only step530. Partial method coverage supports a separate known-method research test, not its hypotheses or bound. The newly written research continuation receives separate supervisor approval next turn. No new lemma, mathematical script or mathematical estimate was produced. The original nomination is retained below as historical specification.

## Completed review — step530, 5 November 2026

### Primary statements and essential cases inspected

The live HTML of [paper23 v1](https://rstation.ai/problems/riemann_hypothesis/papers/23),
Section3 Lemma2 (10)–(14), was inspected again. Its contour has the
outward left height and (14) prints the nominated allowance. The body
does not specify this split at u/2 or prove this standalone bound.
Its circle estimate and continued endpoint are assigned to Derivation87;
neither is imported. The Markdown tool rejected its content type; one
direct curl attempt failed DNS. Readable primary HTML suffices for this
independent review. No blocked-supplement search was repeated.

[DLMF20.2.3 and 20.2(ii)](https://dlmf.nist.gov/20.2) supply the
theta3 series and analyticity for Im(tau)>0, equivalently |q|<1.
Parameter differentiation and weighted sums require local convergence
control. This is interior analyticity, not a uniform boundary estimate.
L799 already proves convergence of the actual complete P series; no
reproof is needed. Its diameter eta bound does not cover this interval.

[DLMF2.10(i), (2.10.1)](https://dlmf.nist.gov/2.10#i) is finite
Euler–Maclaurin with integral remainder: integers a,N,m, N>a, m>0,
and absolutely integrable f^(2m) on [a,N]. In addition to the integral,
half endpoint values and Bernoulli derivative corrections, it retains

    integral_a^N [B_(2m)-Btilde_(2m)(t)] f^(2m)(t)/(2m)! dt.

Smooth real Gaussian-moment functions are the proposed use. A future
proof must check derivative integrability, all boundary terms and the
infinite-N limit, and evaluate an effective remainder bound. This is an
exact identity, not a large-parameter asymptotic. No evaluated weighted
sum bound is derived here. Abel–Plana is not imported; its complex-strip
growth hypotheses would be additional obligations.

[DLMF5.9.1](https://dlmf.nist.gov/5.9#E1), including the line after
the formula, gives

    integral_0^infinity exp(-z t^mu)t^(nu-1)dt
        = Gamma(nu/mu)/(mu z^(nu/mu)),
    Re(nu)>0, mu>0, Re(z)>0,

with principal fractional powers. It supplies exact Gaussian-moment
integrals under these hypotheses, without the complex Mellin phase
loss. [DLMF5.2.1](https://dlmf.nist.gov/5.2#E1) separates Euler's
integral for Re(z)>0 from continuation outside that domain. Cite these
known formulas; no new moment theorem is needed.

[DLMF2.5(i), (2.5.1)](https://dlmf.nist.gov/2.5#i) defines the
Mellin transform only when the improper integral converges. Local
integrability on positive compact intervals does not pay zero. L802's
existing h=0 calculation gives y_L=0 and s=u(Q-c)>0; the future proof
must explicitly use this relation at zero. For h nonzero, check the
actual endpoint, branch and continuity using the saved geometry.
A fixed-h argument alone gives no uniform bound as h approaches zero.
No Taylor-subtracted continuation of M replaces the nominated integral.

All DLMF passages are v1.2.8, released 15 September 2026, accessed
5 November 2026. They supply effective standard methods, leaving their
actual-theta specializations and constants for future mathematics.

### Overlap, failures and search limitations

Reuse the finite-left assessment's primary comparison with Devroye,
*Non-Uniform Random Variate Generation* (1986), ChapterVII Section2.6,
pp299–300: left tangent envelope and reflected proof case. Only its
conditional principle is covered. Its real log-concavity premise does
not establish concavity of P or the new phase. L802's angle argument
uses v>=u/2; it cannot be extended to zero by citation. A single tangent
envelope is not a preapproved sufficient estimate for the new interval.

Queries included: "Mellin" "far left" "theta" "600";
"far-left" "Mellin" theta; theta Gaussian sum bound complex right
half plane sum n^4 exp -t n squared Poisson Mellin endpoint;
"Gaussian sum" "integral test" bound; and complex-theta derivative
bounds. No inspected matching theorem was found. Hiary's truncated-theta
algorithm, higher-rank theta-sum bounds, FLINT algorithm documentation,
forum discussions and a Mathlib Gaussian-Poisson search hit are leads
only; none is an input. A Tao exposition was opened but no theorem from
it is used. No novelty or Mathlib-absence inference follows.

Narrow local searches covered Mellin-named assessments/histories and
the global-import stop. Relevant proof reads covered L797–L799 and
L802 through its finite-segment concavity argument. No completed T_F
proof was identified in this limited scope. L800/L801 are downstream
context only; no other notebook was read. Full matching Mathlib coverage
is unchecked; no formal verification is claimed.

### Decision and bounded continuation

Prepare a separately approved attempt with complete-series, effective
real Gaussian-sum majorants and endpoint/phase case analysis. This is a
known-method reproduction of a nominated source component. No explicit
majorant, split threshold, convergence proof or phase inequality is
established here. Finite Gaussian moments alone do not establish the
required decay after saddle normalization.

The attempt must prove the limit and exact bound uniformly on all D,
or isolate a rigorous obstruction to its chosen sufficient method.
Method failure does not refute T_F or RH. Preserve any failed estimate;
repetition needs materially new input. The separate research nomination
retains the exact observable, essential IDs and boundary checklist.

The main gap remains actual-Xi all-degree mixed positivity. Success
could pay one component for separately assessed assembly with
L800/L801/L802. Vertical endpoint, global contour identity, full budget,
quotient/inversion, certificates and sufficient signs stay open. No
justified central creative sign mechanism follows from this comparison;
the missing sufficient-sign connection blocks that nomination. No
target is invented for scheduling. The global-import stop is preserved.

## Original nomination, retained as history

Use the exact D, saddle x=u+ih and branches of L797/L798, the
normally convergent P of L799 and the left endpoint z_L=x-da=v_L+i y_L
of L802. Thus Q=pi exp(2u), d=3/(16u), a=exp(-i Arg A/2),
S_s(z)=2s Log z+(9/2)z-pi exp(2z), and C=sqrt(2pi/A).
Define the proposed observable, with existence of the limit part of
the target, by

    J_F(s;epsilon)=integral_epsilon^{u/2}
        exp(2s Log(v+i y_L))P(v+i y_L) dv,
    T_F(s)=|lim_(epsilon down to 0) J_F(s;epsilon)|
              /|4pi^2 exp(S_s(x)) C|.

Assess the uniform target

    T_F(s)<=600u^(5/2)sqrt(47Q/(20pi))
              (1+10u/Q)exp(-Q/(20u)),  s in D.

The rational factor 47/(20pi) is exactly the recorded 4.7/(2pi),
not a strengthened allowance. The choice of the interval [0,u/2]
is explicit and local; the earlier inspected source passage did not
specify its split. No identification with an unprinted source contour
piece or analytic continuation of M(s) is assumed.

Main gap: actual-Xi all-degree mixed positivity. A verified far-left
component could later be joined with L800/L801/L802 after a separate
assembly assessment. The continued vertical endpoint, contour equality,
full error budget, quotient/inversion, certificates and sufficient signs
would remain independent gaps. No complete RH route or candidate is
asserted. No justified new central creative sign mechanism emerged
from the finite-component audit; the missing sufficient-sign connection
remains the reason for pursuing this limited prerequisite instead.

The essential local input IDs are L797, L798, L799 and L802.
L800/L801 are downstream context only. Do not import any other notebook.
The recorded stop in `ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md`
remains valid: its unread supplement and global identities are not
premises. Avoid another search for those supplements; compare accessible
primary effective methods with the explicit independently defined
integral above. Reuse adequate earlier source comparisons only for the
hypotheses they actually cover.

Continue to a separately approved mathematical attempt only if the
source review supplies adequate method coverage or an adequately
searched independent test for the stated uniform threshold. A future
attempt must establish convergence and the bound on both closed
boundaries, both signs of h, h=0 and all u>3, or isolate a rigorous
failure of its proposed sufficient method. A method failure is not a
counterexample to T_F or RH. If essential coverage remains blocked,
park the dependent target and select an independent mechanism rather
than repeating the global-import search. Full matching Mathlib coverage
is unchecked. No approval is inferred from writing this nomination.
