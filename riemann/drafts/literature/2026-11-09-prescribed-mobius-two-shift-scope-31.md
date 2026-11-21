# Prescribed multiplicative profile after the arbitrary-pair source limit

TARGET: Assess source coverage for the signed two-by-two form integral w_XT W |M_N(t)(a_- Z(t-1/log T)+a_+ Z(t+1/log T))|^2, with the prescribed normalized quadratic-taper Mobius mollifier at N=floor(T^(1/5)), seeking a sign decision above all absolute errors.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed bounded prescribed-Mobius, shifted mollified fourth-moment and Hardy-sign searches; inspected primary BBLR, Bui--Hall, Bui, Bui--Milinovich and Baluyot scopes below. Reused the November1 stronger-sign exclusions and step31 arbitrary-pair comparison. No full matching signed theorem was identified; no novelty claim.
SOURCE_EVIDENCE: BBLR arXiv:1609.02539v1 Theorems1.1--1.2 and holomorphy remark pp2--4; Bui--Hall arXiv:2304.05178v1 Proposition2 and opening proof through (13) pp9--11; Bui arXiv:1410.2433v1 Section2.1/(10)/Lemma3.1; Bui--Milinovich arXiv:1410.3635v1 (2)/Lemma3.1; Baluyot author PDF Theorems1.2--1.3/(1.4)--(1.8) pp3--5. Exact links and qualifications below.
COMPARISON: BBLR covers the bounded unnormalized half-line coefficients q_N and complex shifts at this length; b_N must be restored exactly. Checked explicit mollified formulas use a fourth power, inverse-square coefficients, or positive divisor coefficients. None imports the signed two-by-two answer. Existing phase/jet tools support a bounded application rather than a new moment theorem.
GAP: Evaluate the complete prescribed-profile two-by-two main form and establish a signed margin exceeding the full source, subdivision, exact-phase/jet and Xi-curvature costs. No signed main form, normalization asymptotic, margin or sign has been established. These are mathematical application obligations, not an essential unread arithmetic source.
REASON: Essential source coverage now permits one same-profile specialization. Import BBLR and retain all six terms; do not reprove its divisor theorem or silently substitute a different mollifier. A positive family margin or negative direction must be proved against absolute errors, with no assumed main scale.
SCOPE: L637's actual W,Z,w; T<=X<=2T; L=log T; N=floor(T^(1/5)); only shifts +/-1/L; complex scalars |a_-|^2+|a_+|^2=1; the exact M_N below. No optimization over profiles, microscopic bump realization, extra shifts, pointwise sign assertion or RH candidate.

This is a future source question, not a second completed step or ready
mathematical continuation. The exact TARGET is the sole Next action.

For N>1 define the profile by

    q_N(n)=mu(n)*(log(N/n)/log N)^2, 1<=n<=N,
    b_N=(sum_(n<=N)|q_N(n)|^2/n)^(1/2),
    M_N(t)=b_N^(-1) sum_(n<=N)q_N(n)n^(-1/2-it).

Here mu is the usual Mobius function. These are definitions of the
prospective target, not a derived asymptotic. The scalar pair may
move with T,X. In L934's notation the intended coefficients are
c_(s,n)=a_s q_N(n)/(b_N sqrt(n)); verify normalization and all source
constants explicitly in the source comparison. Do not treat the full
arbitrary-pair class as approved by approving this particular profile.

Main gap: L030--L032/C032a actual-Xi all-degree mixed positivity.
Intermediate target: determine whether multiplicative cancellation in
this prescribed same-length profile admits a source-controlled signed
average. A negative direction with a rigorously smaller complete error
would yield first-sign evidence requiring separate critical review; a
uniform positive margin would stop this profile only. Pointwise signs,
higher orders and a rigorously certified off-line zero remain separate.

Continuation/abandonment test: reuse step31's exact BBLR scope and
November1 source records. First check primary theorems for this
mollifier square, finite translated observers and smooth support;
do not substitute an amplifier fourth-power or derivative observer.
Import an exact known answer if available. Otherwise approve one
bounded specialization only if coefficient normalization, complex
shifts, all six terms, weight subdivision, exact phase, fixed Cauchy
extraction and Xi curvature provide an absolute-error versus signed-
margin test. If an essential source or sufficient error is missing,
record that precise obstruction and park the profile; do not optimize
the taper or move the length as a replacement attempt.

L399's mean concerns a physical discriminant with an extra response
at Re(s)=5/2 and a shorter sharp-window mollifier. Its negative mean
is not a sign assertion for W. L621's growing-prime/common derivative
observer and L622/L623's row/freezing failures also do not settle this
prescribed arithmetic profile. The local search used two-shift/joint
with Mobius/mollifier terms in drafts/literature, ATTEMPTS and history;
a missing matching record is not a novelty claim.

Essential prospective inputs: L637 for W and normalization; L934 only
for the exact dictionary interpretation; L622 Sections1--2 for the
existing phase-weight interface, whose applicability must be checked.
L399 is a contrast, not a mathematical input. No cross-notebook input.
Full matching Mathlib coverage is unchecked. BBLR's arithmetic theorem
remains an import; neither its proof nor a new moment theorem is proposed.
A creative central mechanism is not yet justified by merely choosing
this standard mollifier. Complete the missing comparison before choosing
between routine specialization and a genuinely new mechanism.

## Completed source comparison — 9 November 2026, step32

The nomination above is preserved. Its pending-review statements are
superseded by this comparison, not by a mathematical sign result.
Outcome EXPLORATION; LITERATURE / NOVELTY_UNCHECKED. No lemma,
mathematical script, dependency or argument overview was changed.

### Primary arithmetic scope and coefficient convention

S. Bettin, H. M. Bui, X. Li and M. Radziwill, *A quadratic divisor
problem and moments of the Riemann zeta-function*, JEMS 22 (2020),
3953--3980, [arXiv:1609.02539v1, Theorems1.1--1.2 and remarks,
printed pp2--4](https://arxiv.org/pdf/1609.02539v1#page=2).
The theorem permits complex shifts O(1/log Y), polynomials
A(s)=sum alpha_n/n^s and B(s)=sum beta_n/n^s of length at most
Y^vartheta with alpha_n,beta_n bounded by n^epsilon, and smooth
Phi supported in [1,2] with each fixed derivative O_j(Y^epsilon).
Its remainder is

    O_epsilon(Y^(1/2+2vartheta+epsilon)
                         +Y^(3/4+vartheta+epsilon)).

Read the complete six-term formula, both prime-power orientations,
and the remarks extending its total error holomorphically through
shift collisions. Theorem1.2 is the alternate smoothed-diagonal
expression, not a positivity assertion. The divisor and holomorphy
proofs remain named imports. The useful length range is vartheta<1/4.

For this profile use the unnormalized source coefficients q_N, then
restore b_N^(-2) in every term and every error. The defining taper
has modulus at most one and q_N(1)=1, so there is no hidden growing
half-line coefficient constant and b_N is nonzero. The relation to
L934's coefficients is exactly the one recorded above; no asymptotic
for b_N is needed to retain it symbolically. A claimed logarithmic
normalization or signed scale would still require proof. This is
an applicability check, not a newly established mean-value theorem.

The original weight is supported in [X,X+T], not always [Y,2Y]
for one source height Y. A later application must use a fixed finite
smooth partition on the compact scaled interval [1,3], with each
piece supported inside a dyadic interval [Y,2Y], Y comparable to T.
The standard smooth partition of unity theorem is sufficient; no
new short-window theorem is proposed. Track uniform derivatives and
constants, retain the original N and log T, and choose a fixed source
length exponent strictly between 1/5 and 1/4 to absorb the bounded
height rescaling. Do not redefine the mollifier on individual pieces.
This is a permitted application plan; its complete error is not proved
in this literature turn.

### Explicit mollifier formulas and why they do not supply the sign

H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1, Proposition2 and Section4.1/(10)--(13), pp9--11](https://arxiv.org/pdf/2304.05178v1#page=9).
The proposition assumes P(0)=P'(0)=0 and exponent<1/8, and averages
four shifted zeta factors against |M|^4. The opening proof retains
six terms, uses collision-safe annuli and introduces four Mobius
variables. The quadratic taper meets its vanishing conditions but
our exponent and mollifier power differ. It does not cover our
|M|^2 observable. Its Proposition1, Section3, has a second-moment
integrand, so its wider length range cannot be used for four factors.
No long expression from Proposition2 is imported or recomputed.

H. M. Bui, *Critical zeros of the Riemann zeta-function*,
[arXiv:1410.2433v1, Section2.1, (10) and Lemma3.1/(13)](https://arxiv.org/html/1410.2433v1#S3.SS2).
Read the coefficient definitions and exact shifted integral before
its main coefficient: the relevant fourth moment uses mu_2, the
coefficients of 1/zeta^2, and P_3 vanishing through the third derivative
at zero. This is not the prescribed mu, P(u)=u^2 square. The note's
Remark1.2 explicitly leaves another twisted-third-moment input
unproved; its overall critical-zero claim is not imported here.

H. M. Bui and M. B. Milinovich, *Large gaps between consecutive zeros
of the Riemann zeta-function. III*,
[arXiv:1410.3635v1, (2), Theorems2.2--2.3 and Lemma3.1](https://arxiv.org/html/1410.3635v1#S3).
The amplifier coefficients are d_r(n)P(log(y/n)/log y), r a positive
integer. Small shifts and exponent<1/4 match part of our setup, but
this source does not assert continuation to r=-1 or give the Mobius
signed kernel. In particular its factorial-integral formula is not
licensed by replacing d_r with mu. No such substitution is made.
BBLR reference3, Bui--Heap--Turnage-Butterbaugh arXiv:1410.3888,
was identified by title only and remains an unread Dedekind-zeta lead;
it supplies no theorem claim or essential premise here.

S. A. C. Baluyot, *On the zeros of Riemann's zeta-function on the
critical line*, [author-hosted PDF, (1.4), Theorems1.2--1.3/(1.6)--(1.8),
printed pp3--5](https://sieg-baluyot.github.io/criticalline.pdf#page=3),
retrieved 9 November 2026; no version identifier is displayed in the
inspected opening. Its exact quadratic Mobius profile is relevant,
but Theorem1.2 is a two-factor phase-matched translated Hardy mean,
whereas Theorem1.3 uses |M|^4, exponent<1/22 and a common real shift.
Its p5 comparison explicitly distinguishes the mu_2 square from its
own mu fourth power. Neither gives our four-factor |M|^2 signed
matrix, and a two-factor translated mean cannot replace it. The
52-page proof was not read: no theorem from it is an input.

Reuse the November1 collective-arithmetic and independent-two-height
assessments for Bui--Hall--Subira Jorge's prescribed divisor-amplifier
fourth power and the untwisted filtered sign results. Their scopes
have not changed. No new source claim from those manuscripts is used.

### Analytic interface and bounded continuation

Read L637's exact W,Z and w definitions, L934's dictionary statement,
and L622 Sections1--4, especially exact phase, all-orders smooth
weight estimates, complex-weight extension, holomorphy, fixed Cauchy
costs and zero-safe curvature. Reuse its separately audited phase/jet
method and underlying gamma inputs. Its old Hughes--Young length
and summed remainder are not an input for this longer mollifier.

Keep the mollifier and scalar pair fixed during shift extraction.
Both observer factors are evaluated at the actual +/-1 scaled shifts;
only the two Laguerre factors are differentiated at zero. Bounded
complex neighborhoods fit the source's small-shift range. Preserve
the conjugate mixed orientations and all gcd multiplicities. Keep the
analytic Hardy phase in the smooth weight and use holomorphy of the
complete sum, not isolated singular terms. The exact Xi-curvature
term in L622 Section4 must still be paid. These are instructions for
the separate mathematical application, not a derived new identity or
an error bound for this profile.

An absolute-error comparison is possible in source format without a
new arithmetic estimate: restore b_N exactly, pay subdivision and
fixed-jet costs, and bound curvature by the imported fourth-moment
or coarse amplifier envelope. Then compare against the actual signed
main value. No presumed T(log T)^6 scale, effective source constant,
finite-height sign certificate or positive spectral margin is imported.
The future test must establish the error as well as the margin.

Continue only if one negative unit scalar direction, or a uniform
positive smallest eigenvalue for all unit scalar pairs, has a proved
margin dominating every absolute cost, uniformly in X. An asymptotic
ratio of total error to margin tending to zero suffices for an
eventual statement; numerical main-term signs alone do not. If the
margin cannot be separated, preserve that exact failure and park
this profile without changing taper, length or shifts. No alternate
profile is approved. Pointwise signs, realization and higher mixed
positivity remain independent gaps even after a positive family test.

The local duplicate/failure comparison used the November1 assessments,
step31 arbitrary-pair source comparison and L934's fixed-bump stop.
The prescribed profile changes the coefficient convention, not the
unsigned realization stop; L399 remains a different-observable contrast.
There is no cross-notebook input. Full matching Mathlib coverage is
unchecked. No new known-result reproof is justified or proposed.

Queries issued included “mollified fourth moment zeta function Mobius
polynomial shifted derivatives Bui 2010”, “Hardy Z Laguerre inequality
mollifier shifted fourth moment signed”, “fourth moment mollifier
mu(n) zeta”, and “mollified fourth one-piece zeta”. Search hits were
leads only; the inspected theorem statements above, not snippets,
support the comparison. This bounded review establishes no novelty.

A separate assessment nominates one mathematical specialization,
requiring the supervisor's next-turn approval. No justified creative
central mechanism emerged from this scoped source review; choosing
this standard mollifier must not be labeled creative.
