# Actual Fredholm norm at one fixed pair — completed source comparison

TARGET: Certify or refute ||A_(2,1024)||<1 for actual G using L776–L777, with independent contour zero count, multiplicity, factor/reciprocal and truncation enclosures.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step430 searched Platt–Trudgian exact theorem/count hypotheses, Arb/FLINT rigorous Xi evaluation, zero-count/isolation and complex integration APIs, and Riemann-Xi Toeplitz/Fredholm norm overlap; reused the audited conditional assessments and searched only the relevant local proofs/failures. Exact queries and read limits below. No matching fixed-pair norm certificate was located; no novelty inference.
SOURCE_EVIDENCE: Platt–Trudgian 2004.09765v1 Theorem1/Section2 p.2; Johansson 1802.07942v1 Section2/2.1 pp.2–4 and Section4 pp.7–8; archived Arb2.23.0 ball, acb_dirichlet, acb_calc and acb_poly contracts; pinned FLINT v3.3.1 xi.c and selected isolate_hardy_z_zero.c cases. Exact URLs, hypotheses and exclusions below. Reuse L776/L777 source coverage.
COMPARISON: Known ball integration, argument principle, Cauchy coefficient extraction and audited L777 error bounds cover a bounded certified implementation at the fixed pair; none supplies the actual count, factor lower bound or norm value. Platt–Trudgian alone is insufficient for these data. The remaining work is routine specialization/calculation of known methods, not a new norm theorem or coefficient-sign discovery.
GAP: Every actual enclosure remains unpaid: contour nonvanishing and count, root location/multiplicity, derivative residue, zero-free outer disk, positive factor lower bound, Laurent coefficients, Gram arithmetic and tail error. The source gate for obtaining these is paid, not the numerical hypotheses themselves.
REASON: Primary algorithm and implementation coverage now supports one independently checkable actual-G diagnostic using L776/L777; no need to reprove general counting, quadrature or Hankel theorems. A citation does not give this numerical norm or its needed constants.
LITERATURE_REASON: Changed target from auditing a conditional identity to certifying an actual fixed-pair norm; essential zero-count and rigorous function-evaluation hypotheses were expressly excluded from previous coverage.
SCOPE: Fixed pair (r,R)=(2,1024) only; a bounded rigorous enclosure calculation or certified admissibility failure. Use L018/L021/L776/L777, standard argument principle, Cauchy formula and norm triangle inequalities with complete error control. No RH, assumed real/simple roots, desired minor sign, floating-point SVD, changed operator or growing-r estimate. No mathematical calculation was performed in this literature turn.

## Original nomination — retained; source status superseded by step430

The main gap is actual-Xi all-degree mixed positivity. L776 now passes
its conditional sign audit, and L777 passes its conditional norm audit.
Neither has been tested against actual enclosure data. One fixed pair
offers an independently checkable diagnostic: does the sufficient norm
condition hold there at all? The rational radius 1024 is a test choice,
not a claimed admissible radius or an approximation to a certified zero.

The next source review should reuse the two existing Fredholm
assessments. Check only the additional primary hypotheses needed for
an independent complete zero count and multiplicities in |w|<1024,
contour nonvanishing, rigorous evaluation of G and its derivatives,
and lower bounds for the zero-free factor on a usable larger circle.
The completion and coefficient conventions remain those of L018/L021.
L466's finite-height source is a lead requiring its exact theorem and
relevant proof cases; finite-height RH alone is not a count, simplicity
certificate or numerical enclosure. Inspect exact fixed-order overlap
in L767–L771 as needed; a coefficient-sign proof cannot replace an
operator-norm computation. No cross-notebook input is proposed.

If the source gate is paid, a later calculation should supply either
a certified upper bound U_fin+E<1 by L777 or a rigorous lower bound
||A_(2,1024)||>=1. Every coefficient, zero, derivative, Gram, arithmetic
and tail error must be included. A norm interval crossing 1 is
inconclusive; a failed upper bound is not a lower bound. Failure of
admissibility also prevents this specific L776 test. Save the complete
certificate and report its actual/required bounds without dumping it.

A successful test validates one instance of the norm mechanism;
it does not improve the known coefficient signs or imply a uniform
estimate. A certified norm obstruction stops this pair, not RH or
all Fredholm methods. An inconclusive first test must identify the
dominant certified loss before any refinement; do not respond with
another identity audit or unbounded precision increases.

The shifted-boundary sign stop and L775's shrinking-core modulus stop
remain preserved. This diagnostic uses the original operator norm and
the exact finite representation, rather than either stopped transfer.
A justified creative growing-order attempt is still blocked by absent
actual F/reciprocal control. This fixed-pair benchmark is ordinary
calculation once covered, not a manufactured creative attempt. Full
Mathlib matching coverage remains unchecked. No mathematics for the
new target was derived or approved in step429.

## Completed primary comparison — step430, 2026-11-04

This is a literature-only step. It approves implementation of known
methods for the unchanged TARGET; it establishes no zero count, numerical
bound, new lemma or sign. The conditional identities are reused from
2026-11-04-zero-winding-fredholm-certificate-specialization.md and
2026-11-04-interior-zero-fredholm-norm-compression.md, and their local
step428/429 audits. No repeat discovery of those identities was needed.

### Searches, overlap and recorded failures

External queries: `Platt Trudgian Riemann hypothesis true up to 3 10 12
theorem 1 simple zeros 2004.09765`; `Arb acb_dirichlet zeta xi rigorous
evaluation zeros complex argument documentation`; `site:flintlib.org/doc
acb_dirichlet zeta_nzeros simple zeros xi`; `site.flintlib.org doc arb
rigorous error bounds ball arithmetic input enclosures`; `"G" "Fredholm"
"Riemann xi" norm Toeplitz`; and `"Borodin" "Okounkov" "xi" Riemann`.
Search snippets were leads, not evidence for the mathematical inputs.

Local comparison used the two ready Fredholm assessments, the step423
shifted-boundary ATTEMPTS record, steps427–429 notes/history, the exact
L776/L777 definitions and certificate, and the conclusion/scope ranges
of L767–L771. Those smoothing statements neither enclose this operator
nor imply that its sufficient norm test holds. L775's scalar-modulus
stop and the unpaid shifted inverse-boundary sign remain preserved;
neither is a stop for the original-norm test. No global notebook search,
cross-notebook input or zero-free-region proposal was made.

A. Gershon, *The De Bruijn-Newman Constant Is Zero*, Preprints.org v1,
22 April 2026, [primary text](https://www.preprints.org/manuscript/202604.1513),
Section11.4 Proposition15, equation(48), complete displayed proof read.
It claims a fixed-shift large-size positive tail for z^(-n)g and a small
trace correction, while taking g zero-free in the disk. The zero-index
hypothesis required by the already assessed Böttcher–Widom formula is
not established for that shifted symbol; the existing nonzero-index
comparison retains a boundary factor. No explicit certificate for our
A_(2,1024), normalization or constants is supplied there. Do not import
(48) as a norm/sign shortcut. This is an applicability comparison with
existing sources, not a full audit or a disproof of the preprint's global
claims. Its other asserted RH mechanisms/caches remain unread/unverified
and are not inputs here.

### Primary inputs and exact applicability limits

D. Platt and T. Trudgian, *The Riemann hypothesis is true up to
3 times 10^12*, [arXiv:2004.09765v1](https://arxiv.org/pdf/2004.09765v1),
Theorem1 and Section2, printed p.2, read directly. The theorem verifies
critical-line location up to height 3,000,175,332,800; the method counts
sign changes and accounts for the total by Turing's method. It does not
print the local root enclosures, derivative bounds or contour minimum
needed here. Its finite-height conclusion alone is not a supplied count
inside the w-circle or a simplicity certificate. A later calculation
may use the theorem only with an explicit coordinate/count argument;
the approved direct contour method below needs no such import.

F. Johansson, *Numerical integration in arbitrary-precision ball
arithmetic*, [arXiv:1802.07942v1](https://arxiv.org/pdf/1802.07942v1),
22 February2018. Read Section2's complete direct-box/Gaussian/bisection
algorithm (p.2), Section2.1 including evaluation-limit handling
(pp.3–4), and Section4 (pp.7–8): Cauchy coefficient extraction and
argument-principle zeta counting. The evaluator must enclose the
function on whole complex boxes and verify analyticity when requested;
branch cuts need explicit treatment. Gaussian error uses a finite
magnitude bound on an enclosing analytic ellipse. Direct box enclosures
remain the fallback; tolerances and completion flags do not substitute
for the final ball radius. Section4's zeta contour includes a pole
correction; it must not be copied unchanged for entire G. These known
methods, together with the standard named argument principle and Cauchy
integral formula, cover contour counts and coefficient/derivative
extraction. They do not supply any values at this fixed pair. No general
quadrature or counting theorem needs reproof.

Arb2.23.0 archived primary documentation, read named contracts:
[Using ball arithmetic](https://arblib.org/using.html), Ball semantics,
Binary and decimal, Quality of enclosures. Inclusion is setwise;
rounding and input uncertainty must both be retained. Decimal printing
must preserve enclosure (arb_printn/get_str), rather than display only
an approximate midpoint. Overestimation may prevent a decision.

[acb_dirichlet](https://arblib.org/acb_dirichlet.html), Riemann zeta
function and Riemann zeta function zeros: xi matches L018's normalization;
zeta_jet gives factorial-normalized Taylor coefficients, with optional
pole deflation. zeta_nzeros counts all positive-height zeros with
multiplicity; Hardy-Z isolation requires positive indices and the
Gram/Rosser subroutines have explicit index ranges. An isolated Hardy-Z
root is not a complete disk count. No actual routine was invoked.

[acb_calc](https://arblib.org/acb_calc.html), Types/macros/constants and
Integration: order=0 permits pointwise evaluation; positive order must
verify holomorphicity throughout the input box. Ordinary principal
square roots cannot silently satisfy this contract across their cut.
The integrator encloses straight-segment integrals; a circle needs a
justified parameterization/partition. Caller truncations and input
errors remain caller obligations.

[acb_poly](https://arblib.org/acb_poly.html), Zeta function,
acb_poly_zeta_series and its Euler–Maclaurin bound/deflation contracts,
read for a derivative/series implementation alternative. Setting the
Hurwitz parameter to 1 selects zeta; deflation handles its pole in the
stated convention. A finite Taylor polynomial alone is not an enclosure
of its infinite tail. L777 supplies the relevant Laurent tail estimate,
conditional on its positive factor lower bound.

The current [FLINT3.7.0-dev count API](https://flintlib.org/doc/acb_dirichlet/acb_dirichlet_zeta_nzeros.html)
and xi/integration pages were also read. They announce an October2026
documentation rewrite with partially generated text. The approved input
is cross-checked against archived contracts and the primary paper, not
that announcement or search metadata. Record the installed version in
any later certificate; availability of a particular wrapper is not yet
checked.

Pinned implementation checks (source reading only): FLINT v3.3.1
[xi.c](https://raw.githubusercontent.com/flintlib/flint/v3.3.1/src/acb_dirichlet/xi.c),
complete 66-line function including nonfinite input, exact s=1 and
reflection/removable-value branches. This corroborates the intended
entire completion but is no guarantee of a sharp bound on a wide box.
[isolate_hardy_z_zero.c](https://raw.githubusercontent.com/flintlib/flint/v3.3.1/src/acb_dirichlet/isolate_hardy_z_zero.c),
opening algorithm/index comments and selected count cases near
exact_zeta_multi_nzeros, _acb_dirichlet_exact_zeta_nzeros and
acb_dirichlet_zeta_nzeros (lines1245–1371) read. Exact/inexact height
cases differ, with endpoint counts enclosed for ball input. The opening
comments explicitly allow nontermination if a counterexample prevents
sign separation. Thus no total termination or global RH assumption is
imported. The attempted separate zeta_nzeros.c URL returned 404; the
implementation is in this retrieved file, so that failure is resolved.
The full Turing/separated-list implementation was not audited or
reproved. The direct contour method is independently covered and is the
preferred count certificate for this test.

### Approved calculation and acceptance conditions

Only the following established-method specialization is approved, within
the unchanged fixed-pair target. This describes future work, not results.

1. Use L018/L021's actual G and L776's exact normalization. Implement a
   rigorous evaluator, with local square-root charts/reflection or the
   entire series and certified tails; prove compatibility of charts and
   removable values wherever used. Save complete input boxes and bounds.
2. Enclose G away from zero on every part of |w|=1024 and use the argument
   principle to certify the count with multiplicity. Locate the interior
   zero(s) independently of minor signs and resolve multiplicity before
   using L777. A finite list of critical-line zeros is insufficient.
3. Choose an explicit sigma>1 only after certifying the required
   zero-free F disk; count/control any additional zeros up to that
   boundary. Enclose the factor on its whole outer circle, with a
   strictly positive m_sigma. F at an enclosed zero requires a removable
   evaluation/derivative certificate, not division of two zero balls.
4. Enclose the residues, Laurent coefficients and finite Gram/norm data
   exactly as L777(2),(6)–(11); include quadrature, root, derivative,
   coefficient, arithmetic and infinite-tail errors. Its proof's full
   product difference bound also supports a lower certificate through
   the standard reverse triangle inequality. Do not treat a large
   upper bound as a lower bound or change the Hilbert norm.
5. Report an actual interval and threshold1 with the complete certificate
   on disk. Upper endpoint<1 supports this pair's conditional sign use;
   lower endpoint>=1 stops its sufficient norm test. A failed admissible
   zero count stops this particular application; an unresolved count or
   interval crossing1 is inconclusive and must identify the dominant
   loss. Bound the first implementation attempt; do not launch a radius
   sweep or automatic unbounded precision refinement.

The result sought is a local feasibility diagnostic, not a new sign
criterion, RH proof or uniform growing-order estimate. Remaining
independent gaps include all-r admissible radii, tied moduli, other
indices and positivity assembly. No justified creative nomination is
available from this review: a growing-order mechanism still lacks an
independent actual F/reciprocal budget. This is a concrete blocker to
that nomination, not a historical ban. Mathlib coverage of the full
numerical/Fredholm certificate is unchecked; no formal result is claimed.
