# Oscillation-preserving continuation: completed source comparison

TARGET: Assess source coverage for fixed-cap validated Filon quadrature of L814's F,G and first two derivatives on [6.5,40], retaining L815's full tails and every unresolved cell.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step585 searched explicit and validated Filon errors, Filon–Clenshaw–Curtis bounds, and the exact-family queries recorded below; searched local polya assessments/attempts/histories for duplicates and reused the step578 inclusion assessment and step584 audit. No matching inspected event census was found; no novelty inference.
SOURCE_EVIDENCE: NIST DLMF3.3(i)–(ii), equations3.3.1–5,3.3.11–13,3.3.16–18 https://dlmf.nist.gov/3.3 ; Gao–Iserles2017 DOI10.1186/s40687-017-0110-4 Section1 Theorem1/(1.5)–(1.6), definition of the Filon integral, and Section2.1/(2.3) https://link.springer.com/article/10.1186/s40687-017-0110-4 ; Kim2012 thesis printed149,153–157, Theorem5.17/proof, Remark5.22 and Corollary5.25 (qualifications below); reuse step578's primary interval-inclusion coverage and L815 step584.
COMPARISON: Explicit real interpolation remainders plus exact polynomial-times-trigonometric integration support a three-node composite Filon inclusion test for the finite smooth amplitudes. They supply no actual derivative bounds, narrower interval-frequency output, event signs or full census. General FCC asymptotics and unspecified constants alone do not certify finite caps.
GAP: Source coverage is sufficient for the bounded three-node specialization, not arbitrary FCC implementations. Panel derivative bounds, outward moment evaluation, actual error budgets and additional closed-cell exclusions remain research obligations; no gain is established today.
REASON: Replace the failed whole-u-box evaluator by a source-supported polynomial-amplitude evaluator; derive only its application and explicit finite certificates in a later research step. The newly saved implementation assessment requires separate next-turn approval.
SCOPE: Essential inputs L016/L019/L020/L021/L814/L815 and preserved census579/audit581/exact-machin583/audit584 artifacts; real derivative orders0–2, u in [0,3], theta n<=4, full L815 errors and every undecided x cell. No all-real reference, cross-notebook input, sign theorem or global extrapolation. Full matching Mathlib coverage unchecked.

The paragraphs below through the original nomination's last sentence
record the question at entry, before the step585 comparison. Their
prospective source requirements are resolved only to the extent stated
in the completed comparison afterward.

The main gap remains actual-Xi all-degree mixed positivity. This nomination
concerns only a finite collision test useful to the deformation route.
No justified signed central mechanism is currently prepared: L814's
compensated square still needs an independent relative bound, and merely
choosing its coefficients existentially restates the desired sign. That
is the concrete blocker to creative routing, not a ban on later discovery.

The independently testable proposed improvement is to preserve oscillatory
cancellation in the finite [0,3] integrals, instead of increasing Decimal
precision or repeating interval-box summation. Inspect a primary validated
Filon error statement and its relevant proof cases for the real smooth
amplitudes u^j times the finite theta sum or Q. Establish the exact source
scope for sine/cosine factors, frequency intervals including shared x
endpoints, and explicit amplitude/interpolation errors. Existing tails
and normalization may be reused only with their complete qualifications.
This describes the question to assess, not a derivation or ready theorem.

Continue only if a specific theorem and executable bounded error budget
support a materially different finite-integral certificate for this exact
family. Otherwise park this evaluator and nominate an independently
testable mechanism; do not answer an inaccessible theorem with indefinite
search or another precision scan. Any later attempt needs declared caps
and must preserve all unresolved common/multiple/edge cases. A favorable
finite exclusion still leaves signed compensation and unbounded x open.
This assessment is newly written and requires separate approval; no new
mathematical lemma or script for this continuation was produced in step584.

## Completed comparison — step585, 5 November 2026

This was one literature-only step. No lemma, mathematical script,
quadrature, amplitude derivative bound or new numerical inequality was
produced. The outcome is EXPLORATION/REPRODUCTION: adequate coverage for
a concrete standard specialization, not a mathematical discovery or an
extension of the excluded region. The main gap remains actual-Xi
all-degree mixed positivity; the intermediate finite test could reject a
local deformation rule through a certified adverse event, or supply
limited exclusions useful for later deformation tests. Favorable finite
output would still leave the independent signed and infinite-domain gaps.

### Primary inputs actually inspected

[NIST DLMF §3.3](https://dlmf.nist.gov/3.3), online version inspected
2026-11-05, equations 3.3.1–5, 3.3.11–13 and 3.3.16–18: interpolation
uses distinct real nodes and a real function with continuous derivative
of order n+1 on the closed hull of nodes and evaluation point. The
remainder is f^(n+1)(xi) times the nodal product divided by (n+1)!.
For the three equally spaced nodes, t in [-1,1], equation 3.3.18 gives
the explicit coefficient c_2=1/(9 sqrt(3)) in the h^3 remainder bound;
h is adjacent-node spacing, not the entire panel length. The endpoints
are interpolated exactly. These are imported formulas, not reproved
interpolation theory. DLMF cites Davis1975 pp56,67–68 for the general
real remainder; those book pages were not independently retrieved.

[Gao–Iserles, *Error analysis of the extended Filon-type method for
highly oscillatory integrals*](https://link.springer.com/article/10.1186/s40687-017-0110-4),
Research in the Mathematical Sciences4,21 (2017), published1 November2017:
Section1 defines Filon evaluation by integrating the interpolating
polynomial against the oscillator. Theorem1, (1.5)–(1.6), states the
Peano-kernel error representation and L1-kernel/derivative bound for a
bounded linear error functional annihilating polynomials through degree m.
Section1 also gives the absolute interpolation-error integral bound.
Section2.1 (2.3) retains an O(omega^(-s-2)) remainder: its displayed
leading constant is not a complete finite-frequency certificate.
Section3's zero-frequency tables are not certificates for frequency
intervals. Only the exact method/error framework is used here.

The three-node Lagrange variant requires no endpoint amplitude
derivatives for interpolation. It is within the polynomial-amplitude
Filon framework; it need not adopt the paper's higher-order Hermite
choice. DLMF supplies the specific explicit remainder. The Peano-kernel
approach is an alternative, not a second compulsory implementation.
No reproof or new general error theorem is justified.

[Tatiana Kim, *Asymptotic and numerical methods for high-frequency
scattering problems*, Bath PhD, March2012](https://purehost.bath.ac.uk/ws/portalfiles/portal/187936078/UnivBath_PhD_2012_T_Kim.pdf):
inspected Theorem5.17 on printed149 (PDF page165), the end of Lemma5.21,
Remark5.22 and the theorem proof on printed153–155, and the statement
and rescaling in Corollary5.25 on printed156–157. The smooth-amplitude
FCC estimate uses a weighted derivative norm and constants sigma_m,N.
The proof also invokes a prior constant C_m0. The factorial expression
in Lemma5.21/Remark5.22 alone was not verified as a complete numerical
error constant. This is comparison evidence, not an imported executable
bound. Its remaining proof cases and stability algorithm are not relied on.

Domínguez–Graham–Smyshlyaev, IMA J. Numer. Anal.31(4),1253–1280
(2011), DOI10.1093/imanum/drq036, is a relevant stronger FCC lead.
The author PDF search result exposed its first page, but opening
`people.bath.ac.uk/masigg/publications/preprints/CleCur0810_final.pdf`
redirected to the university home page. No theorem from that manuscript
is treated as inspected or as finite-cap coverage. There is no essential
source blocker for the simpler explicitly covered variant. Plukas–
Plukienė's n-th order Filon paper was located at DOI10.15388/LMR.2005.29206;
only metadata/abstract and the PDF landing page were reached. It is an
unread lead, not an input. No further access loop is needed.

### Exact application scope and unpaid implementation work

L814 and L815 step584 supply the precise real transforms, derivative
integrands and complete tails. For j=0,1,2 the finite amplitudes are
u^j times the n<=4 theta sum or Q. Each is real and smooth on [0,3],
being a finite combination of polynomials and elementary entire
functions. Thus the C^3 hypothesis for three-node interpolation holds
on every closed panel, including the first and last. The correct signs
and sine/cosine choices remain those of L815. Smoothness is applicability;
it is not a numerical supremum for the third u derivative. That
supremum must be enclosed on each whole panel in later research.
These finite-amplitude derivatives introduce no new improper-integral
claim; the original derivative-integral tails still need to be added.

The cited remainder is frequency-independent for real x. Whole x-cell
validation therefore requires interval inclusion for the finite
polynomial-oscillator integrals as well as the panel error; a midpoint
frequency cannot stand for a cell. Finite quadratic moments may be
evaluated using integration by parts and the fundamental theorem of
calculus, with outward arithmetic throughout. Those are standard named
calculus inputs. Any apparent singularity of a divided formula at x=0
must be bypassed by ordinary polynomial integration or by reusing the
audited normalization. At x>=6.5 division by x is safe; it may still
produce wide intervals through cancellation. No small-frequency
asymptotic or point-sampled Peano norm is an acceptable remainder.

Reuse step578's primary inclusion assessment rather than rederive
interval analysis. L815 step584 permits the saved positive c enclosure
and step583's independently justified pi endpoints. The known raw
Decimal integer-power failure persists: replace a used power by
outward multiplication or independently certify it. Reusing the exp
and trigonometric evaluator requires checking the actual new argument
ranges; an audit of old ranges is not a blanket backend guarantee.
All outward arithmetic, exact grid construction and moment formulas
must be documented before their output is relied on.

This suffices for an executable bounded attempt, not a prediction that
the bounds will meet a sign threshold. The next test is confined to
1024 equal closed u panels on [0,3], 50-digit working precision, and
the original67 closed x cells of width1/2 covering [6.5,40]. No adaptive
or increasing-cap loop is included. Save separately interpolation,
rounding/moment and L815 tail errors, derivative bounds and complete
cell output. Compare against the stored census579 intervals. Continue
this evaluator only if it certifies a previously unresolved whole-cell
exclusion; otherwise park this fixed variant and retain the failure
budget. Smaller radii alone do not imply absence of an event.

The historical [0,6.5] exclusion is reused with its backend/execution
qualification; the shared6.5 endpoint remains excluded there. The edge40,
all gaps between exclusions, common zeros, higher multiplicities and
every unresolved interval must remain in the output. A new exclusion
uses the existing strict F,G same-sign or nonzero-W tests. No additional
root isolation or claim about event orientation is part of this test.
No favorable result supplies the missing relative signed remainder,
unbounded x coverage, or all-degree positivity. Matching Mathlib coverage
was not checked, and absence from Mathlib is not asserted.

### Search extent, duplicate check and route

Queries included `Filon quadrature explicit error bound interpolation
derivative validated oscillatory integral`, `Filon Clenshaw Curtis
quadrature error bounds Dominguez Graham Smyshlyaev 2011 theorem`,
`Filon quadrature rigorous error bound explicit constant fourth derivative`,
the DGS title/PDF filename, and exact-family searches
`"Pólya" "Wronskian" "Filon"` and
`"Riemann" "xi" "validated" "Filon"`.
Only the primary material identified above was inspected for theorem
coverage. Local searches were restricted to polya literature assessments,
attempts and histories. No prior inspected Filon implementation was
identified there. The direct-box cap and power counterexample are
retained, not contradicted or deleted; no novelty is inferred.

The completed target is SPECIALIZE: explicit interpolation coverage
supports a standard three-node Filon test with a later application proof
and certificate. The newly written continuation assessment is
`2026-11-05-polya-filon-bounded-test.md` and needs separate approval
before invocation. No extra discovery is needed for this unchanged
scope. A justified central creative target is still absent: L814's
relative signed compensation remains unpaid, and existential selection
of its coefficients is equivalent to the desired event sign. The
numerical evaluator is ordinary implementation, not relabeled creativity.
