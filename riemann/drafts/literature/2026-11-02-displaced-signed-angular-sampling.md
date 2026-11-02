# Signed angular sampling after the anchor-transfer obstruction

TARGET: Test whether a finite nonharmonic sampling lower bound controls the full signed response of the independently displaced delta=1/4 family strongly enough to prove H >= (log D)/2-n/32+log n-C uniformly.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: On 2026-11-02 searched finite/discrete Ingham inequalities, separated Vandermonde conditioning, Kadec perturbation leads and rational-circle sampling/quadrature. Read the primary statements and relevant proof cases below. Scoped local searches found L649's deweighting stop, C645o's signed-Gram stop, L650's pole-isolation stop and L665's displacement stops; no matching rational sampling application was identified. This bounded comparison does not certify novelty.
SOURCE_EVIDENCE: Moitra arXiv:1408.1681v4 (29 April 2015), Sections 2.1--2.3, printed pp.5--7, Theorems 2.2--2.3 and complete finite majorant/minorant argument (https://arxiv.org/pdf/1408.1681v4); Negreanu--Zuazua, C. R. Math. 338 (2004), 281--286, Theorem 2.1 and inverse/alias proof pp.283--284 (https://www.numdam.org/item/10.1016/j.crma.2003.11.033.pdf); Danchenko--Semin arXiv:1503.06476v1, Section 1.1 Theorems 1--2 and complete Theorem 2 proof, PDF pp.1--2,6--7 (https://arxiv.org/pdf/1503.06476v1). Reuse the prior contour/Mahler assessments. No new theorem is imported into the RH argument.
COMPARISON: The finite exponential theorem permits complex coefficients but requires unit-circle exponential columns and an observation/separation budget; no exact map from W_a is supplied. Rational quadrature measures the combined signed response with pole-dependent nodes/weights, not a lower bound against the original-residue D. Neither statement supplies H. L664's existing constant-coefficient Jensen bridge offers a narrower exact rational sampling test without assuming a general L2-to-log transfer.
GAP: Prove or obstruct a uniform signed rational sampling lower bound with the actual diagonal and the total n/32 logarithmic budget, retaining all moments and endpoints. Exact rational membership, pole orders, sample weights, cancellations and constants require mathematical work; separation of ordinates alone verifies none of these. No new specialization or inequality is proved in this review.
REASON: Primary source scope and the known mismatches are now sufficiently assessed for one bounded attempt at the unchanged TARGET. EXPLORE covers the exact rational transfer gap; it does not approve an exponential replacement or assert the desired bound. No selected essential source is blocked. The newly ready continuation receives separate approval next turn.
LITERATURE_REASON: The proposed mechanism changes from an inherited-anchor perturbation estimate to a signed angular sampling lower bound after L665's informative obstruction; exact nonharmonic sampling hypotheses and the rational-weight transfer are essential unread coverage.
SCOPE: Exactly TARGET for L649's admissible independently displaced L664 family, n=12q+3, q>=1, h=27/(5n), delta=1/4, fixed anchor, independent real |epsilon_y|<=h/16, all 4q+1 original unit residues, the full conjugated-angle product and all M=n/3 moments. One later exact rational sampling/observation test is covered, preferably on c_0 with L664's existing Jensen bridge; no inherited anchor approximation, positive complex amplitudes, changed original residues or exponential surrogate is assumed.

## Proposed comparison and bounded decision

The main gap remains actual-Xi mixed positivity and unbounded-height
signs. This intermediate target would give the paid-arc criterion for
a less rigid dense family through L658; arbitrary support, realization
and signs remain separate. The target permits an absolute constant C
and uniform onset, and retains log n from angular localization.

At nomination, primary finite nonharmonic Fourier/sampling lower bounds
were required before specialization; Ingham/Kadec were only search leads.
The completed comparison below supplies the selected finite statements.
Check the observation interval, separation,
finite versus infinite index set, the extra anchor, permitted coefficient
weights, constants and any required positivity. Then compare with the
actual rational angular functions W_a(u), not merely their local phases.

The decisive comparison must either identify an applicable theorem with
its remaining exact transfer cost, or document why its hypotheses or
quantitative threshold do not reach the stated H bound. Termwise
exponential approximation does not control a cancelling signed sum.
An L2 bound alone does not automatically lower-bound the complete spatial
logarithmic mean. These transfers must be covered explicitly before
dependent mathematics is approved. Repeating the stopped pure-power
inverse transfer in L649 or L665's absolute-error subtraction is not a
new sampling mechanism.

Essential inputs to any later continuation are L649 definitions, L658's
full-root localization and inherited L657 integrability, L661's general
squared-residue envelope, L664's exact-grid baseline and L665's qualified
obstructions. L665 is not separately audited. No symmetry, positivity
of complex amplitudes or inherited anchor approximation is assumed.
The completed comparison below supersedes the initial unread-lead status.

## Completed source comparison, 2 November 2026

### Primary statements and proof scope

**Finite nonharmonic samples.** A. Moitra, *Super-resolution, Extremal
Functions and the Condition Number of Vandermonde Matrices*,
[arXiv:1408.1681v4](https://arxiv.org/pdf/1408.1681v4),
Sections 2.1--2.3, printed pp.5--7. For unit-circle nodes
alpha_j=exp(2pi i f_j), take wrap-around separation strictly greater
than Delta>0. With m=2L+1 rows and arbitrary complex b, the proof gives

    (m-1-Delta^(-1)) sum_j |b_j|^2 <= ||V_m b||_2^2
        <= (m-1+Delta^(-1)) sum_j |b_j|^2,
    (V_m)_(ell,j)=alpha_j^ell, 0<=ell<m.

Theorem 2.3 bounds the squared condition number by the ratio of these
constants when m>1+Delta^(-1). The inspected proof uses both interval
majorants/minorants, compact Fourier support, exclusion of every
off-diagonal integer alias, and a modulus-one coefficient shift from
centered samples. The extremal-function theorem is cited, not reproved
or independently audited. These are exponential samples with fixed
coefficients; no rational-weight or logarithmic conclusion is stated.
The observation count m here is unrelated to notebook M until a map
is proved. We do not identify their frequencies with the ordinates.

**Discrete Ingham cross-check.** M. Negreanu and E. Zuazua,
*Discrete Ingham inequalities and applications*, C. R. Math. 338(4)
(2004), 281--286,
[DOI 10.1016/j.crma.2003.11.033](https://www.numdam.org/item/10.1016/j.crma.2003.11.033.pdf),
Theorem 2.1, pp.283--284: besides gap gamma>0, the sampled frequencies
obey a diameter cutoff (2pi-(Delta t)^p)/(Delta t), 0<=p<1/2;
the time threshold is 2pi/gamma+epsilon(Delta t), and the finite sum
has 2N<M. Read the sine-window inverse estimate and the two alias
cases (9)--(13). The printed globally indexed infinite sequence with
bounded diameter cannot literally satisfy both hypotheses; the proof
uses a finite truncated band. That indexing qualification is unresolved
here, so this theorem is not an input. Its role is only to check that
sampling cannot ignore aliases or observation length. Moitra supplies
the unambiguous finite comparison actually selected above.

**Exact rational observation.** V. I. Danchenko and L. A. Semin,
*Sharp quadrature formulas and Nikol'skii type inequalities for rational
functions*, [arXiv:1503.06476v1](https://arxiv.org/pdf/1503.06476v1),
22 March 2015, Section 1.1, Theorems 1--2 (PDF pp.1--2).
Let Z be finite distinct points inside |z|<r including 0, with their
reflections r^2/conjugate(z), including infinity. Rational F has poles
only in this union; ordinary pole orders are <=s, and the combined
orders at 0/infinity are <=2s-1. With B its Blaschke product and
mu(zeta)=sum_(z in Z)(r^2-|z|^2)/|zeta-z|^2, Theorem 2 states

    integral_(|zeta|=r) |F(zeta)|^2 |d zeta|
        = (pi*r/s) sum_(B(zeta_k)^(2s)=exp(i phi))
                         |F(zeta_k)|^2/mu(zeta_k).

Read its complete proof (PDF pp.6--7): reflect/conjugate F, retain
the doubled finite poles and the 0/infinity polynomial parts, then
use Theorem 1 and the polynomial identity. Theorem 1's full proof
was not independently audited. This is an exact observation identity,
not coercivity of signed amplitudes or a logarithmic lower bound.

### Exact family comparison and bounded continuation

The rational functions remain

    W_a(u)=B_u(x)/B_u(a),
    c_0(u)=R^(-1) sum_a W_a(u),
    G(u,zeta)=sum_(0<=k<M)c_k(u) zeta^k.

L649, L658, L661 and L664 fix the meanings of B, c_k, H and D;
the original residues remain one. The independent displacements and
fixed additional anchor are those in L665's hypotheses. No symmetry
of the displaced set is imposed. Our comparisons are source-scope
inferences, not a new mathematical obstruction:

1. **Direct exponential import:** small ordinate displacement is not
   verification of a frequency perturbation, real linear angular phase,
   fixed amplitude, wrap-around gap or observation budget. Neither
   source supplies an exact identity for W_a. Rescaling an imagined
   frequency does not create more observations. Termwise approximation
   must control the signed sum and its error relative to the required
   response; L665 excludes the nominated o(1) anchor approximation.
2. **Exact rational observation:** Danchenko--Semin allows complex F,
   so positive amplitudes are unnecessary. Its weights concern angular
   observation, and must not replace the original simple-pole residues.
   Before application, account for the full angular pole set, reflected
   completion, multiplicities, cancellations and possible degree drops.
   An exact quadrature formula still requires a lower bound for the
   combined signed samples relative to D. Off-diagonal terms cannot be
   dropped: the recorded C645o witness has a negative real cross entry.
3. **Scalar coefficient route:** L664, proof Section 5, already records
   the full-root Jensen inequality m(theta)>=log|c_0(e^(i theta))|
   when c_0 is nonzero. Thus a later attempt may test c_0 itself by exact
   rational angular observation instead of converting a spatial energy
   lower bound into a log mean. Proposed benchmark: compare its angular
   maximum, or its normalized angular L2 norm, to
   n*exp(-n/32)*sqrt(D), up to an absolute factor. This is a proposed
   sufficient test using the existing bridge, not an estimate established
   here. If it fails, H may still satisfy TARGET through other moments.

The third option is the most focused next test within TARGET. It uses
the small displacements as family information without forcing an
inherited anchor value, changing residues, or isolating close poles
one at a time. It must permit order-one signed changes. The earlier
L650 example stops polewise duals for exponentially close poles; it
does not decide joint observation for this specific displaced family.
L649's ambient inner-input inverse loss must not be recycled as a new
sampling theorem. L661/L665 absolute contour costs remain recorded.

Continue only if an exact observation identity yields a verified
family-uniform lower bound with constants sufficient for TARGET, or
identifies a concrete remaining cost with a discriminating bound.
Abandon this scalar route if an admissible countersequence defeats
its benchmark, or if its proved observation/transfer cost exhausts
the n/32 budget. Neither result alone refutes the full H criterion.
An unexplained positive Gram matrix, formal quadrature identity or
finite numerical preview is insufficient. If a full spatial L2 route
is used instead, its logarithmic transfer must be justified separately;
L658 localizes an already large log mean and does not provide it.

### Search record, reuse and limits

Queries included `finite Ingham inequality rational functions sampling
nonharmonic Fourier Kadec theorem`, `discrete Ingham Theorem Moitra pdf`,
`Montgomery Vaughan Hilbert inequality separated frequencies Ingham`,
and `rational functions unit circle exact quadrature lower norm sampling
prescribed poles Danchenko Semin theorem`. These located the primary
papers above, not a matching resolution. Liao--Fannjiang, *MUSIC for
Single-Snapshot Spectral Estimation*, 9 November 2014 author PDF,
Theorem 2 was screened for finite gap/row-count scope; its full Appendix B
proof was not read and it is not an input. Kadec's original theorem and
the broader orthogonal-rational quadrature leads were not inspected;
they are not essential to the selected finite comparison or direct
rational test. Any later reliance on them requires new coverage.

Reuse `2026-11-02-independent-grid-displacement-paid-arc.md` for the
Austin--Trefethen changed-weight and Dimitrov--Habegger growing-term
comparisons, and `2026-11-02-two-offset-anchor-audit.md` for finite
residues, full-root means (Brunault--Zudilin Proposition 1.4, all modulus
cases) and L658 localization. No reproof of these inputs is proposed.
Scoped searches and the relevant proof ranges, including L664 Section 5,
were inspected; this does not independently audit unaudited L649/C645o/
L650/L665 arguments. Their method stops are contrasts, not new premises
for a response lower bound. General support, Xi realization and all-degree
signs remain independent gaps. No RH candidate exists.

Text retrieval of the selected sources succeeded; shell download failed
at DNS resolution and screenshots were unavailable. There is no persistent
essential-source blocker. Full matching Mathlib coverage for the finite
sampling, rational observation or proposed transfer is not checked;
unknown availability is not absence. Existing supporting Fourier/Mahler
coverage is reused. This literature-only turn writes no lemmas or
mathematical scripts and establishes no new response bound.
