# Fixed-profile Xi realization — completed source comparison

TARGET: Compare primary results and recorded failures for realizing C651a's fixed-profile detector in an actual-Xi logarithmic-derivative model with projection error o(exp(-n/32)*sqrt(D)).
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 221 completed the bounded actual-Xi logarithmic-derivative/rational-approximation search, reused the ready joint-space comparison, checked the local realization/norm/remainder stops, and followed the previously abstract-level Najnudel–Nikeghbali lead to its exact local factorization and off-critical correction. Queries, actual readings and limits are recorded below and in drafts/2026-11-03-fixed-profile-xi-source-working-221.md.
SOURCE_EVIDENCE: Baratchart–Chevillard–Qian arXiv:1501.01161v2 Section 3, Proposition 1/(8)–(12), and Theorem 4/proof; Green, The Prime Number Theorem (2018 course), Proposition 6.1 and Theorem 6.1 p.31 and Section 6.2 pp.32–33; Najnudel–Nikeghbali arXiv:2609.15862v1 Theorem 1.1/Section 1.1, Lemma 8.1 and Proposition 8.2 with complete proofs, and Proposition A.1 with complete proof (A.1)–(A.12), pp.32–35. Precise versions and qualifications are below.
COMPARISON: Free-pole rational approximation does not realize a prescribed integer-residue profile. The actual-zero local factorization retains multiplicities and complex displacements, has fixed microscopic radius and a different error observable, and gives neither C651a's fixed half-lattice nor its original diagonal and joint-projection error. The distributional collapse comparison is conditional and uses bounded-Lipschitz distance, not the required L2 norm.
GAP: No actual-Xi center/scale/anchor and complete block matching C651a's fixed profile has been supplied; no bound for the resulting complete joint-projection discrepancy or actual diagonal comparison is supplied. The required o(exp(-n/32)*sqrt(D)) remains a target. No map, approximation bound, sign or impossibility theorem is proved here.
REASON: The source test fails for this fixed-profile transfer. Park it on the explicit pole-data and norm/quantifier mismatch, preserve C651a, and nominate a different actual-product tail-normalization review. EXPLORE records a completed bounded comparison, not permission to pursue an unspecified realization proof or a novelty claim.
LITERATURE_REASON: The observable changes from an independently constructed finite rational family to actual Xi data. Essential actual-zero factorization and error hypotheses were outside the ready synthetic assessment; this step reads those cases rather than repeats its projection audit.

SCOPE: Completed literature comparison only. No theorem is installed in the mathematical assembly, and no new lemma, proof, mathematical script, numerical screen or Mathlib absence claim is made. The C651a-to-Xi transfer is parked unless materially new pole-matching and quantitative error input is supplied.

## Completed comparison — 3 November 2026, step 221

The main gap is actual-Xi all-degree mixed positivity. The intermediate
target is exactly TARGET above: transfer the paid synthetic detector
lower bound to an identified actual-Xi logarithmic derivative, keeping
the original diagonal and the full angular L2 projection error. A matching
detector upper bound and a sign implication would still be independent
unresolved obligations. The test is an applicable noncircular map with
complete error costs, or a specific unpaid term requiring a route change.
The latter outcome occurs here; this is NEGATIVE source-scope evidence,
not progress beyond the inspected mathematics or a theorem excluding
every possible Xi realization.

### Exact local interface and hypothesis mismatch

C651a's family consists of the anchor x=-5/4 and exactly 4q other poles
x+i*(27/(10n))*(m+1/2+e_m), with n=12q+3, M=n/3, unit original
residues and one fixed L703/L708 profile before n varies. That profile
has summable shifts, a specified Fourier support and a nonlinear profile
equation; |e_m|<=1/8 alone does not specify its scope. Read C651a in
full and L651's hypotheses, conclusions and complete component-response
setup, then L726's exact profile hypotheses and L666's rational pole
setup. No actual Xi zero block or scale is identified by these inputs.

L018 identifies the actual zeros as alpha=gamma+i*(1/2-beta), with the
original multiplicities. The proposed translation, rotation and scaling
would have to account for these complex locations; neither a selected
critical-line subset nor horizontal projection accounts for omitted
zeros or multiplicities. Assuming a block is simple is an additional
unproved hypothesis, even under RH. No assertion is made that the
particular finite spacing profile cannot occur. Its occurrence with
the fixed-profile quantifiers is simply unsupported by the checked
theorems. The n-dependent relation to height is also unspecified.

C645y's exact residue split identifies F_u with the analytic component
of the stipulated finite P'/P after all grid residues are kept. L651's
small correction belongs to that finite symbol. It does not bound an
additional analytic term, an omitted-zero contribution or the change
of residues induced by replacing P'/P with an actual-Xi function.
C651a's zero correction for its constant dual remains valid as written;
it does not identify a different input function or its diagonal.
There is thus no candidate complete projected discrepancy to estimate
at the requested scale. These are missing application inputs, not new
lemmas or a claimed universal obstruction.

### Primary statements and essential proof cases

L. Baratchart, S. Chevillard and T. Qian, *Minimax principle and lower
bounds in H2-rational approximation*, J. Approx. Theory 206 (2016),
17–47, [arXiv:1501.01161v2, 24 March 2015](https://arxiv.org/html/1501.01161v2).
Section 3 sets the L2 rational/meromorphic minimization problems.
Proposition 1, (8)–(12), treats strictly negative Hardy f and minimizes
||P_-(f b)||_2 over all degree-at-most-n Blaschke products. Its proof
uses orthogonal Hardy decomposition. Theorem 4 additionally assumes a
continuous f and an orthonormal family of Hankel singular vectors;
its lower approximation bound includes their sup norms. Its zero-bound
case and nonzero-bound proof were read. These optimize an approximation
observable without enforcing logarithmic-derivative residues or a fixed
pole profile. Reuse the ready joint-space assessment for Theorem 7,
finite model spaces, fixed-symbol Nehari convergence and the 2026
Blaschke-product sequel. No general approximation theorem is reproved.

Ben Green, *The Prime Number Theorem*, Oxford C3.8 course (Hilary 2018),
[author PDF](https://people.maths.ox.ac.uk/greenbj/papers/primenumbers.pdf),
Proposition 6.1/Theorem 6.1, printed p.31, Section 6.2 pp.32–33.
The regularized partial fraction formula is

    zeta'(s)/zeta(s) = C - 1/(s-1)
        + sum_rho [1/(s-rho)+1/rho].

It uses all trivial and nontrivial zeros, counted with multiplicity,
away from the meromorphic singularities. The Hadamard product has
reciprocal-square summability; Section 6.2 explains completion and removal
of the gamma factors. These are exact expansions, without a local
projection-remainder estimate. The source assigns infinite-product
differentiation to an exercise; no independent proof audit is claimed.
L024 already supplies the notebook's unconditional paired Xi product,
so a second product proof or a new canonical lemma would be redundant.

Joseph Najnudel and Ashkan Nikeghbali, *Cauchy laws for zeta logarithmic
derivatives and stationary Stieltjes transforms*,
[arXiv:2609.15862v1, 14 September 2026](https://arxiv.org/pdf/2609.15862v1),
internal date 5 September 2026. Lemma 8.1/Proposition 8.2, pp.20–21,
and Proposition A.1/proof, pp.32–35, were read completely. With L=log T,
t in [T/L,T], zeta(1/2+it)!=0 and fixed r, A.1 factors the normalized
zeta ratio on |w|<=r into exp(i*pi*w), all actual complex zeros with
|(gamma-t)L/(2pi)|<=L^2, and a holomorphic relative error
O_r((1+log(T/t))/L). Multiplicities are retained. Its proof checks
cutoff recentering, Stieltjes/dyadic tails, complex-zero correction,
locally uniform logarithmic convergence, gamma normalization and Cauchy
differentiation. Equation (A.12) is the completed-xi version with error
O_r(1/L). Proposition 8.2 retains an explicit signed off-critical
correction. Theorem 1.1's actual-derivative Cauchy limit assumes H(T)=o(T);
(1.4) controls bounded-Lipschitz law distance. No L2 detector bound,
fixed-profile spacing, uniform growing-r assertion or sign is supplied.
This is theorem-scope reading, not independent manuscript verification.

In particular the last result is useful actual-zero information, but
its error is not a statement about C651a's full joint projection. The
symbol, measure, diagonal, pole census and radius quantifiers must first
be matched. There is no justified comparison of O_r(1/L) with
exp(-n/32)*sqrt(D) without that map and an n-to-height relation. An
upper bound in a different norm cannot certify that comparison. The
source's normalization excludes central zeros, whereas the global
goal includes them; no denominator-free extension is assumed.

### Duplicates, failures, search limits and route decision

Reused the fixed-profile projection-audit and joint-full-grid assessments.
Read the relevant local-L2 signed-remainder, tilted-Xi norm and
collective-kernel assessments and the vanishing-amplitude and local-L2
stops. They already warn that a generic analytic error tool does not
pay an actual-Xi relative error or other-zero contribution. The exact
finite polynomial ODE stop is a different class, not a ban on finite
local factors. The mesoscopic signed-truncation assessment had read only
Najnudel–Nikeghbali Section 1/Theorem 1.1. Its later-section coverage
was expressly missing; the A.1/8.1/8.2 reading above is new to this
comparison and is relevant to actual-zero realization.

Queries were `Riemann xi logarithmic derivative rational approximation
Blaschke Hardy space zeros` and `Riemann zeta logarithmic derivative
local partial fraction zeros uniform approximation error`. Followed the
primary author notes and arXiv texts, not snippets, secondary primers
or search-result claims. The ready assessment's stronger-approximation
searches are reused without another broad search. No failed search
establishes novelty or nonexistence. No essential source-access blocker
remains for this bounded scope. Full matching Mathlib coverage is
unchecked; supporting Hardy results do not identify actual Xi.

Decision: park this fixed-profile transfer, retaining C651a unchanged.
The new independently testable nomination asks about the analytic tail
of the actual local product, with actual zeros retained, on a fixed
physical disk after explicit quadratic normalization. It does not
assume the synthetic profile or promote a distributional theorem to
L2 control. Its changed-radius estimate, counterterm effect and signed
margin require separate review; no bound or mathematical mechanism is
approved by this turn. See
`2026-11-03-actual-xi-quadratic-tail-scope.md`. Until those inputs are
specified, a central creative proof attempt is not source-ready.

## Preserved nomination (source status superseded above)

The main gap remains actual-Xi all-degree mixed positivity. Step 220
completes the approved synthetic projection application, leaving no
reason to repeat its scalar or Gram audits. Assess whether that
application has a concrete route to actual Xi before spending more
turns strengthening this synthetic profile.

Start with C651a, the realization qualifications in L651/L726 and the
actual-Xi definitions in L018; use the supplied overview and narrowly
search their relevant source/failure references. L030--L032 supply the
known positivity/real-node interface only if that exact interface is
needed. Do not read a broad archive or assume an unspecified transfer.
Check precise primary theorem hypotheses before any proof attempt.

The source review must specify which actual-Xi function or finite block
would correspond to the rational symbol, how translation/scaling and
the anchor are chosen, and whether all original residues, full grid,
finite endpoints, conjugated angle, normalized measures and D survive.
It must retain omitted zeros and analytic terms in an explicit error
norm, rather than assert they are small. An identification presupposing
RH, arbitrary zero placement, simple zeros or an unproved sign is not
an unconditional input. The proposed small-error threshold refers to
the L2 angular norm of the complete joint projection; it is not a
pointwise or finite-height numerical test. The diagonal must either
remain exactly D or have a proved comparison with all constants given.

Acceptance for this source task is an applicable named theorem with
the remaining difference explicitly stated, or a precise incompatible
hypothesis/unpaid term that changes the route decision. A merely
analogous kernel or positive Gram matrix supplies no realization.
If no noncircular map is supported, park this proposed transfer and
nominate a materially different, independently testable central target.
Do not keep developing it through repeated source summaries.

No actual-Xi model, error estimate, new lemma or mathematical script is
constructed here. No source sufficiency, novelty or global obstruction
is claimed. A later creative attempt requires a concrete mechanism,
a discriminating test and separate source approval; this nomination
does not manufacture one to satisfy a scheduling preference.
