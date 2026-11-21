# Frozen prime-times-M^2 fourth moment — source review1447

TARGET: Test whether the original frozen prime-times-M^2 polynomial has fourth moment O(Bq^2) on [X,sqrt(2)X], uniformly in its frozen heat height.
CHECKED: 2026-11-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused1402/1410/1436/1440 and checked the scoped stops1407/1408/1431/1437/1446; six new queries and inspected primary leads are recorded below. No adequate matching theorem was located in this bounded search; no absence or novelty inference follows.
SOURCE_EVIDENCE: Read Teravainen, Almost primes in almost all short intervals, Section2.4 Lemma9 and its complete reduction proof, printed p255 in the author-hosted2018 thesis PDF p80; Evans, Correlations of almost primes, Section7.5 Lemma7.12/(7.4) and both proof cases; Choi--Kumchev math/0412227v1 Theorems1.1/2.1 and definitions(2.1)-(2.2), PDF pp1,4; Bui--Hall--Subira Jorge2511.14415v1 Theorem1.1, amplifier definition and Section3 through(6). Reuse1402's BBLR and taper comparisons and1410's G.16 statement.
COMPARISON: Arbitrary coefficients in Watt-type estimates belong to the short twist, while the factor raised to the fourth power is a prescribed ordinary zeta sum. Neither these nor ordinary amplified zeta formulas cover the unchanged prime-supported heat factor. Bilinear first-absolute-moment estimates with their stated logarithmic losses do not supply the required fourth moment. No imported theorem proves or refutes the target.
GAP: A bounded direct signed finite-polynomial test must retain the full product support, original alpha/linear taper, hard high-height interval and uniform fixed-Z heat coefficients. The O(Bq^2) bound, including its unequal-frequency terms, remains unproved; no moving-height, real-channel or actual-Xi transfer is covered.
REASON: Nomination1446 lacked essential prime-versus-zeta coefficient coverage. That comparison is now complete for a bounded direct test using already inspected finite-frequency tools, with no inaccessible source assumed. EXPLORE permits an attempt, not the desired estimate or a source transplant; separate approval follows before research.
SCOPE: Original C019y integer-d scales, J=[X,sqrt(2)X], B=|J|, q=log X, L=floor(X^(1/1000)), alpha from the Euler-product branch of zeta^(-1/2) on Re(s)>1, omega(n)=log(L/n)/log L, M(t)=sum_(n<=L) alpha(n)omega(n)n^(-1/2-it), P_Z(t)=sum_(p in [sqrt(X)/10,sqrt(X)/5]) E_p(Z)p^(-1/2-it), Z fixed in J; Q_Z=P_Z M^2. One absolute constant and one existential original integer-d onset, uniform in Z. Only the displayed target is covered.
LITERATURE_REASON: The target changed from stopped whole-window energy to a direct high-height prime-polynomial fourth moment; its long coefficients and uniformity were outside prior inspected zeta-moment scopes. No repeat broad literature search is required after this assessment is separately approved.

## Purpose and exact boundary

The main gap remains actual-Xi all-degree positivity L030--L032/C032a
and the unbounded exceptional-root deficit. The intermediate target is
exactly

\[
 \int_X^{\sqrt2X}|P_Z(t)M(t)^2|^4\,dt\le C Bq^2
 \quad\text{for every fixed }Z\in J,
\]

with the original E_p(Z) of C019y/C020i. This is a desired inequality,
not a theorem established here. The heat variable is frozen at Z;
the integration variable t is a real height. No critical-line value of
an infinite reciprocal series is part of M's definition.

For source hypothesis comparison, Q_Z's formal support ceiling is
(sqrt(X)/5)L^2 and that of Q_Z squared is (X/25)L^4. The full
product cannot be declared short merely because each mollifier is
short. This is support bookkeeping, not a mean-value estimate.
Furthermore Q_Z squared contains four *unshifted* individual tapers.
C019y(1)'s c_s has two h-shifted factors. Its identities or coefficient
norms must not silently be substituted for the unshifted coefficients.
Repeated primes are present in P_Z squared and in this target.

A successful estimate could help control a frozen complex prime-pair
norm. It would still require a proved reduction with two distinct own
heat times, shifted integration ranges and equal-prime subtraction.
Those reductions are not carried out or preapproved here. Fixed-to-moving
transfer, the real nonconjugate channel, signed numerator, E_P, root
accounting and Xi transfer remain independent gaps.

## Reused coverage and recorded failures

Reuse [review1402](2026-11-17-jensen-paired-squared-mass-test-1402.md)
and its source notes: BBLR1609.02539v1 Theorems1.1--1.2 pp2--4 and
Section2.4 pp8--12 allow short arbitrary twists of four ordinary zeta
factors with small shifts and smooth height cutoff. Their six-term
assembly and holomorphy qualifications remain necessary. Those long
factors are not prime-restricted polynomials; no domination or
coefficient-replacement theorem was inspected. Bui--Hall2304.05178v1
Proposition2 uses mu and a double-zero taper. The Baluyot taper warning
and Gonek--Ivic's paired second moment keep their prior scopes; none
settles this finite prime fourth moment. The unread original Selberg
proof remains parked and is not an essential input.

Reuse [source-notes1410](2026-11-18-jensen-real-prime-witness-source-notes-1410.md),
Montgomery--Vaughan's author-hosted Multiplicative Number Theory II,
G.16/(G.25)--(G.28), printed pp426--427, with its individual nearest
frequency separations. Equal frequencies must first be grouped.
This finite-frequency inequality is available, not a promised sharp
bound for the current coefficients. Review1402's Koesters0803.1141v2
Appendix A.1--A.3 tools retain their monotonicity, derivative,
separation and amplitude-variation requirements. Reuse1436/1440 for
absolute-neighbor and whole-window inequalities, whose sufficient
budgets have now been stopped. No theorem is reproved here.

Read the precise failure paragraphs in attempts1407/1408/1431/1437.
C019w's unweighted variation and C019x's separate G-diagonal stops
concern different sufficient payments. C020g's three-attempt G--J
completion remains parked. C020h stops the full absolute neighbor
budget. C020k's already supplied result stops the hard-window *whole*
energy using heights outside J. These do not prove growth of the
present integral. The new test must exploit or test the actual signed
high-height correlations, rather than repeat those sufficient budgets
or claim that finite regrouping alone pays them.

## Newly inspected primary comparisons

### Watt-type finite zeta-sum moment

J. Teravainen, *Almost primes in almost all short intervals*,
Section2.4, Lemma9 (Watt), printed p255, reproduced in the
[author-hosted2018 thesis](https://users.utu.fi/jopete/wp-content/uploads/sites/195/2018/08/PhD_thesis_Teravainen.pdf),
PDF p80. Read the full statement and reduction proof on that page.
Writing source height S to avoid the notebook's T, the statement has
S>=S_0>=S^epsilon, lengths A,N>=1 bounded by S^(1+o(1)),
N(s)=sum_(n~N)n^(-s) or sum_(n~N)(log n)n^(-s), and
A(s)=sum_(m~A)a_m m^(-s), arbitrary complex a_m. Its bound is

\[
 \int_{S_0}^{S}|N(1+it)|^4|A(1+it)|^2dt
 \ll\left(\frac{S}{AN^2}(1+A^2S^{-1/2})+S_0^{-3}\right)
 S^{o(1)}\max_{m\sim A}|a_m|^2.
\]

The proof removes log n by partial summation, treats N>=t using the
ordinary zeta-sum bound, and reduces N<=t on dyadic height ranges to
Watt's twisted zeta moment via its cited Baker--Harman Lemma2.
The underlying Watt proof and that additional lemma were not read;
no use of their uninspected content is proposed. Watt's original
bibliographic lead is J. Number Theory53(1995),179--210,
[*Kloosterman Sums and a Mean Value for Dirichlet Polynomials*](https://doi.org/10.1006/jnth.1995.1086).
The publisher abstract was insufficient to supply its full formula.
This does not block the present review: the inspected finite version's
coefficient restriction already prevents a direct import.

The arbitrary a_m do not make the fourth-power N factor arbitrary.
Prime restriction and E_p(Z) are absent from N(s). Partial summation
can address a smooth weight after suitable norm control, but cannot
be assumed to remove the prime indicator. Moving the prime factor
into the arbitrary twist does not leave the source's prescribed
zeta-sum factor in our integrand. In addition S^{o(1)} is not a
stated fixed logarithmic bound. No new specialization is made.

Natalie Evans, [*Correlations of almost primes*](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/correlations-of-almost-primes/08F8E4E4C36F68ED6DDA373CCAF7A221),
publisher version, DOI10.1017/S0305004122000251, Section7.5,
Lemma7.12/(7.4). Read its definitions, statement and both proof cases.
For Q_0<=S^epsilon, S^epsilon<=S_0<=S, 1<=A,N<=S^(1+o(1)),
it averages over characters of moduli q<=Q_0, with weight1/phi(q),
and bounds the corresponding |N(1+it,chi)|^4|A(1+it,chi)|^2 integral by

\[
 \left(\frac{Q_0S}{AN^2}(1+A^2(Q_0S)^{-1/2})+S_0^{-1}\right)
 (Q_0S)^\epsilon\max|a_m|^2.
\]

Here N has coefficients chi(n) or chi(n)log n, and A has arbitrary
complex coefficients times chi(m). The small qt<=N proof uses a
partial-character-sum estimate and retains its S_0^-1 term; the
N<=qt case invokes Harman--Watt--Wong Theorem2. That underlying theorem
was not inspected or imported. The character variant preserves the
same long-coefficient restriction and an epsilon loss; it does not
provide the target by a modulus-one citation. Neither exclusion is
an obstruction theorem for the target itself.

### Bilinear prime mean-value lead

S. K.-K. Choi and A. V. Kumchev,
[*Mean Values of Dirichlet Polynomials and Applications to Linear Equations
with Prime Variables*, math/0412227v1](https://arxiv.org/pdf/math/0412227v1),
12 December2004, Theorem1.1 p1 and Section2, definitions(2.1)--(2.2),
Theorem2.1 p4. The PDF version header was checked; the generated HTML's
extraneous2026 draft date is not used. Theorem1.1 is a first absolute
moment of a von-Mangoldt polynomial averaged over the specified
character family H(m,r,Q), with bound (N+HN^(11/20))log(HN)^C,
H=mr^(-1)Q^2S. Its Remark1 gives C=1100 as a possible choice.
Theorem2.1 concerns a product of three dyadic polynomials with lengths
N_i, product V=N_1N_2N_3>=10, coefficient bounds tau_kappa,
tau_nu,1, kappa,nu>=2, and either max(N_1,N_2)<<V^(11/20) with
the third coefficients all1, or that same maximum condition with
N_3<<V^(8/35). It gives (V+HV^(11/20))log(2HV)^c,
c=3max(kappa^2,nu^2)+kappa+nu+20.

These statements were inspected to classify the lead, not applied to
a newly constructed product. No grouping or conversion into the
current fourth moment was proved. The stated first-absolute-moment
conclusion and its logarithmic losses do not constitute the requested
O(Bq^2) assertion. Their full proofs were not audited; the lead
introduces no essential unread input for the proposed finite test.

### Recent amplified fourth moment

H. M. Bui, R. R. Hall and M. Subira Jorge,
[*Amplified fourth moment of the Riemann zeta-function and applications*,
arXiv:2511.14415v1](https://arxiv.org/html/2511.14415v1),
18 November2025, Section1 amplifier definition and Theorem1.1;
Section3's initial six-term BBLR application through(6) was read.
The amplifier has d_r(n) times a polynomial logarithmic taper,
r a positive integer (footnote extends to positive real r), length
y=S^vartheta with vartheta<1/8. The formula is for four shifted
ordinary zeta factors and four shifted amplifier factors, small
O(1/log S) shifts, and smooth height cutoff. Section3 keeps all six
terms and factors the arithmetic using d_r. It is not a formula for
a prime-supported long factor or for our eight alpha-taper factors.
Negative-r analytic continuation is not a stated hypothesis. No
extension, full coefficient asymptotic or source reproof is attempted.

## Search evidence, bounded handoff, and stopping test

Queries actually issued (18 November2026):

- `"fourth moment" "Dirichlet polynomial" primes mollifier`
- `Watt mean value Dirichlet polynomials arbitrary coefficients prime fourth moment twisted`
- `"prime" "polynomials" "mollifier" "fourth" moment`
- `"twisted" "fourth moment" "prime" "Dirichlet polynomials" -site:researchgate.net -site:kokunoyumeto.github.io`
- `"fourth moment" "prime sums" "Dirichlet"`
- `"Dirichlet polynomials" "fourth moment" "arbitrary coefficients" Watt`

Search summaries were discovery only. Other hits on character-family
moments, additive prime exponential sums, random matrices, general
surveys and third-party RH/repository pages were not used as theorem
evidence. No new zero-free region or reciprocal continuation is
proposed, and no cross-notebook theorem is used.

EXPLORE is justified for one direct finite-sum attempt, not for an
unproved Watt/BBLR replacement. A later attempt should group exact
integer frequencies of Q_Z squared and test its signed high-height
moment, retaining repeated primes, all four unshifted individual
tapers, endpoint phases and exact E_p(Z). Finite multiplication and
integration are available elementary operations; any use of the
reused G.16 or derivative tools must verify their stated hypotheses.
No new expansion, coefficient bound or cancellation is proved here.

The decisive success evidence is a uniform C Bq^2 upper bound for
this exact moment; decisive negative evidence is an incompatible
rigorous lower bound for it. A bounded method may instead identify
its first unpaid signed correlation with its required scale. An
upper envelope exceeding C Bq^2, an unevaluated identity or failure
of a stronger whole-energy bound is inconclusive. Do not revive
absolute-neighbor1437, hard-window1446 or completion1431 without a
materially different quantitative mechanism. Preserve partial work
if the direct signed test is inconclusive; the supervisor owns budgets.

No essential inaccessible source is assumed. Full matching Mathlib
coverage is unchecked; general supporting inequalities do not
formalize this target. This literature step supplies no mathematical
advance, originality certification or complete RH candidate. PROOF
and DAG need no change. No justified source-supported central creative
mechanism emerged: a genuinely new all-degree/Xi mechanism remains
unavailable, and this test is established-route development. This
newly completed assessment receives separate approval next turn;
no additional browsing or dependent mathematics is performed now.
