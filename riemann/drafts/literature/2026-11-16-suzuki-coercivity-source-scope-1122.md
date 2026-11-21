# Remaining Suzuki coercivity steps — completed source comparison1123

TARGET: Assess the remaining Suzuki Theorem 4.2 decomposition and coercivity steps, resolving the multiplier line, gamma normalization and low-frequency lower-bound constants.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused assessment1121, C618a and the November1 screw source screen; targeted queries were Suzuki 2206.03682 erratum 4.2, Suzuki screw function C0 gamma correction, the exact article title with correction, and DLMF5.11 psi asymptotic expansion. No inspected erratum was found; absence of a search match is not evidence of novelty or correctness.
SOURCE_EVIDENCE: Read Suzuki2206.03682v4 PDF internal31May2023, Section2.1/(2.1)-(2.5), printed p6, and Theorem4.2/(4.2)-(4.11), pp12-15, including both one-sided inversion cases and the gamma contour passage; compared HTML conjugations and constants. Read NIST DLMF5.2(i)/(5.2.2) and 5.11(i)/(5.11.2), including its sector condition. Publisher correction comparison timed out; the controlling v4 remains accessible. Tao coverage is reused.
COMPARISON: The source already claims the small-window positivity sought by a later audit. Its C1 line, gamma threshold normalization, C0 convention and displayed I0+I1 inequality do not consistently match the subsequent lower-bound use. C618a repairs only the two previously audited form comparisons. These are source applicability issues, not a refutation of Theorem4.2 or a new positivity mechanism.
GAP: A bounded conceptual audit must verify the complete three-term identity for arbitrary complex L2 tests and obtain its small-window lower bound using constants on the actual contour, the actual (4.7) multiplier, a genuine lower-band loss constant and the correct inequality direction. No repaired estimate has been proved in this literature turn.
REASON: Exact primary comparison converts the prior flags into a complete, separately testable audit scope; unqualified verbatim import of the displayed constants is unsuitable. A reproduction is justified by suspect source steps and the need for full complex-test applicability, rather than by a claim of originality.
SCOPE: This completed turn is literature-only. Subsequent audit scope is specified in assessment1123; no numerical onset, all-window conclusion, Theorem4.3 Fourier-tail audit, blocked scalar-tail retrieval or new signed arithmetic claim is covered.

## Completed comparison, 16 November 2026

Use the [v4 PDF](https://arxiv.org/pdf/2206.03682v4), with printed
page and equation numbers above. The [HTML formulas](https://arxiv.org/html/2206.03682v4#S4.SS3)
confirm the conjugations but retain the previously recorded date anomaly.
The [journal reference](https://doi.org/10.1112/jlms.12785) remains
Suzuki, JLMS108(2023),1448-1487. No publisher-text correction is assumed.

The source's three multipliers are

    P(s) = 1/(s-1) + 1/s,    Z(s) = zeta'(s)/zeta(s),
    W(r) = Re[(1/2)psi(1/4-ir/2) - (1/2)log(pi)].

In (4.5)-(4.6), z=r+ic, s=1/2-iz, and each multiplier is
paired with the sum of
Phi(phi,z) conjugate(Phi(phi,conjugate(z))) and
Phi(phi,-z) conjugate(Phi(phi,-conjugate(z))). Equation(4.7)
uses W on the real line and the two modulus squares. All three
integrals have measure dr/(2pi). These are source identities to be
audited, not identities independently established here.

Four exact applicability discrepancies are now located:

1. The p14 definition of C1 uses Re(s)=1+c, while the specified
   change of variables puts (4.5)-(4.6) on Re(s)=1/2+c. A bound
   valid only on the printed C1 line cannot simply be substituted.
2. Equation(4.7) contains the factor1/2 multiplying psi. The
   later threshold and C0 displays omit that factor. Their constants
   must be tied to W itself before the following estimate is used.
3. The printed C0 is a maximum of that differently normalized
   expression. The next integral estimate instead needs W(r)>=-D
   on |r|<=T, with a specified nonnegative finite D. This comparison
   does not claim that the printed inequality fails for a particular
   test or a particular choice of its existential parameters.
4. The I0+I1 display is an upper bound; (4.11) needs a lower bound.
   A future audit must retain the preceding absolute-value estimates
   and establish the required direction for the real form.

The relevant source proof cases have been read. Section2.1 gives
the one-sided transforms separately for the poles, prime terms,
linear term and Lerch/digamma term; the latter uses its full series
calculation (2.4)-(2.5). In the Theorem4.2 proof, the pole inversion
distinguishes positive and negative spatial arguments, then combines
the two exponentials for the even kernel. The prime and gamma
identities are referred back to those transforms; the gamma integral
is moved to the real axis. The later proof uses Cauchy--Schwarz,
the two form bounds, gamma growth, and small-window absorption.
Thus absence of gamma poles alone is not a completed local audit:
vertical-edge decay, removable zero frequencies and absolute Fubini
for the full complex L2 class still need written justification.

The supporting standard input is
[DLMF5.11.2](https://dlmf.nist.gov/5.11#E2): the digamma expansion
holds as the argument tends to infinity in |arg(w)|<=pi-delta for
fixed delta>0. The fixed positive-real-part lines and bounded
positive-real-part strips needed here lie within such a sector;
no assertion uniform up to the negative real axis is imported.
[DLMF5.2(i),5.2.2](https://dlmf.nist.gov/5.2#E2) identifies psi,
gamma's nonvanishing and its poles; it supplies no contour decay
by itself. These standard inputs require only their stated
specializations; they need not be reproved. No effective T has
been extracted or calculated.

The bounded subsequent test is recorded in
[assessment1123](2026-11-16-suzuki-full-decomposition-coercivity-audit-1123.md).
It asks whether the cited decomposition and coercivity argument can
be fully justified with consistent constants and C618a. Continue if
the identity, all integrability/domain cases and a positive uniform
small-window coefficient are established. Otherwise preserve the
specific unresolved obligation or rigorous counterexample; do not
declare the theorem false from the display discrepancies. No
additional discovery is needed for that unchanged audit scope.

The earlier screen already covers the small-window theorem as a known
weaker result. Parameter descent, realization-only signing and scalar
square-order stops concern other mechanisms and are not reopened.
C618a is the sole local mathematical input proposed for the audit;
L030/L032/C032a give main-gap context only. All-support arithmetic
signs and Xi/common-graph transfer remain independent. No cross-notebook
input is used; full matching Mathlib coverage remains unchecked.

## Original nomination (historical; superseded by comparison above)

The main gap remains L030/L032/C032a actual-Xi all-degree positivity.
A correctly qualified local coercivity input could support subsequent
arithmetic/complement work, but cannot settle the missing all-support
signs, low-block coupling or Xi/common-graph realization.

The exact controlling primary source is Suzuki, *Aspects of the screw
function corresponding to the Riemann zeta-function*, JLMS108 (2023),
1448–1487, [DOI10.1112/jlms.12785](https://doi.org/10.1112/jlms.12785),
[v4 PDF](https://arxiv.org/pdf/2206.03682v4), Theorem4.2.
Use the PDF version for numbering; the HTML rendering's inconsistent
internal date was already recorded in the existing assessments.

One bounded source-comparison task: check (4.5)–(4.8)'s full
pole/prime/gamma decomposition and the passage to (4.11), for the
same arbitrary complex L2 tests. Essential points to resolve are the
relation between the displayed line in C1 and s=1/2-iz on Im(z)=c;
the coefficient 1/2 in the gamma multiplier; and whether the named
low-frequency constant supplies the lower bound actually required.
These are audit flags, not a verdict that the source theorem is false.
Retrieve the exact primary identities and their essential contour and
integrability cases before approving any repair. Do not promote a
normalization warning into an independently derived result this turn.

Reuse [assessment1121](2026-11-16-suzuki-form-domination-audit-1121.md)
and canonical C618a for the now completed two-form gate, with
C2=exp(2ca1), C3=2T/pi and the non-mean-zero primitive retained.
Do not redo that proof. The November1 screw screen is the qualification
record for what small-window positivity does and does not give. The
November16 arithmetic-to-square comparison1120/1121 and stop1117
remain evidence against automatic finite-window propagation; they
are contrasts, not mathematical premises. No cross-notebook input.

Continue only if exact source hypotheses and a complete list of
remaining analytic obligations permit one bounded separately approved
audit/import. If a required primary passage is unavailable, name it
and park dependent work; if the comparison supplies no new obligation
or applicable input, do not repeat this audit under a new name.
Any eventual reproduction is local source verification, not progress
beyond the cited mathematics. Matching Mathlib coverage is unchecked.

No new central creative mechanism is nominated: C618a is arithmetic-free,
and no signed prime/complement resource has emerged. The next source
comparison should remove a concrete applicability uncertainty, not
use the creative-routing preference to relabel a source audit.
