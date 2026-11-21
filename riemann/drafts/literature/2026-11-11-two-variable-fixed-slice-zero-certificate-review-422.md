# Two-variable theta family: fixed-slice certificate source gate

TARGET: Assess a rigorous fixed-slice certificate for an off-center zero of Lagarias–Rains's xi_Q(3/2,s) in 40<Im(s)<45 and 0<|Re(s)-3/4|<2, without assuming branch connectivity or transferring the result to w=1.
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step423 searched exact Lagarias/Rains/rigorous/3/2, xi_Q/zeros/interval and two-variable-zeta/certified-zero terms; no matching finite certificate was located. Reused the ready bulk-haar-integral-enclosure and theta-integrated-layer-compensation assessments; narrow local reciprocal-theta/Lagarias checks found reconstruction and contour-import stops, not this enclosure. No novelty inferred.
SOURCE_EVIDENCE: Directly inspected Lagarias-Rains math/0104176v5 Theorem2.1 and proof (2.6)-(2.10), printed pp8-9, and Section8 Lemma8.1/whole proof p44; Rump corrected ActaNumerica2010 author PDF Theorem13.3/(13.8) and proof, internal p89; Johansson 1802.07942v1 Sections2/2.1 pp2-3 and3.2 p6; Johansson 1806.06725v1 Section1.4.2 (1.18)-(1.20)/Algorithm1 pp12-13; archived Arb2.23.0 acb_calc and python-flint0.9.0 acb.integral contracts. Details and links below.
COMPARISON: Known Krawczyk existence and validated quadrature/theta-series methods cover a finite reproduction attempt, not the asserted off-center zero. The source's numerical departure supplies a lead only; its asymptotic O-term is not an effective error certificate. Center Re(s)=3/4 and s->w-s come from Theorem2.1; Section8's printed 1-rho symmetry must not be applied at w=3/2.
GAP: A future calculation must supply an exact evaluator, effective full spatial and theta tails, whole-box Jacobian enclosure, branch checks and strict Krawczyk inclusion inside the requested domain. No numerical root, disk, error constant or existence margin was calculated. Backend availability is unresolved; default python3 lacks flint.
REASON: Essential finite-existence coverage is now identified and a bounded independently checkable test is specified. This is local source progress using known methods, not a new zero theorem, an independently bounded Li cost, branch transport or RH progress beyond the inspected sources.
LITERATURE_REASON: The changed target requires finite complex-zero enclosure and error coverage absent from the completed generator/Li comparison. Reuse ready general interval and complex-analysis coverage where applicable; do not repeat generic probability or reconstruction searches.
SCOPE: Completed literature-only assessment of the displayed finite domain at fixed w=3/2. No mathematical script, root search, new zero theorem, parameter sweep, branch tracking or transport to w=1 was performed. The separate continuation assessment specifies the mathematical test and remains subject to next-turn approval.

Essential local input is L018 only for identifying the w=1 slice and
keeping the RH target distinct. L019 fixes the theta convention. The
entire two-variable family is an external source input, not an already
installed local lemma. L984/C984a are motivation/contrast, not premises
for the finite zero test. No cross-notebook theorem is proposed.

The proposed mathematical test is existence of ONE disk with rational
center/radius, lying strictly inside the stated domain, on which a
rigorous method certifies a zero of xi_Q(3/2,s). The source's approximate
heights are leads only; no particular disk or positive margin is known.
Any successful test must save the complete analytic tail, integration
and root-count/existence evidence. A sampled winding number, a small
floating-point residual or a plot is insufficient. Count and simplicity
must be distinguished; a certificate need not establish simplicity.

The downstream use is a precise limitation on universal preservation
of center-line zeros in the same theta family used by the generator.
It supplies no positive theorem for w=1 and no rejection of methods
using additional arithmetic at that distinguished parameter. Do not
upgrade this finite check into a proof of the source's connectivity
claim; that would need collision/branch analysis and separate coverage.

Continue if inspected primary results and available rigorous arithmetic
specify an independently checkable finite calculation with strict
error margins and a bounded search. Otherwise park this finite lead
with the exact missing hypothesis rather than repeat the generator
question. No bound on zero motion is an available premise. Full
matching Mathlib coverage is unchecked and unknown.

The preferred next mathematical classification, if this source gate
becomes ready, is REPRODUCTION/calculation. No justified creative target
is nominated: independent signed Li cost and collision-aware zero
transport remain missing. The finite lead is chosen for an actual
discriminating test, not a lemma or scheduling quota.

## Completed source comparison — step423

**Family input.** Lagarias–Rains, *On a Two-Variable Zeta Function for
Number Fields*, [math/0104176v5](https://arxiv.org/pdf/math/0104176v5),
7 July 2002, Theorem2.1/proof, printed pp8–9, gives entireness and the
functional equation. The evaluator source is their exact (2.9):

\[
 Z_{\mathbb Q}(w,s)=-\frac1s+\frac1{s-w}
 +\int_0^1[\theta(1/t^2)^w-1]
       [t^{-s}+t^{-(w-s)}]\,\frac{dt}{t}.
\]

Use their (1.2) theta series and completion
\(\xi_{\mathbb Q}(w,s)=s(s-w)Z_{\mathbb Q}(w,s)/(2w)\).
No uncompensated Mellin integral is licensed. The proof's endpoint
estimate (2.7) has an unspecified O-constant; it establishes compact
convergence, not numerical error bounds. Section8 Lemma8.1, printed p44,
reports numerical departure; its connectivity argument is outside this
test. Its printed reflection by 1 contradicts the general-w formula;
use Theorem2.1's reflection by w. Equation(1.2), rather than the
following printed nome conversion, fixes the exponential sign.

**Existence input.** S. M. Rump, *Verification methods: Rigorous results
using floating-point arithmetic*, Acta Numerica19 (2010), 287–449,
[corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
Theorem13.3, internal p89, (13.8), with complete proof inspected.
For continuously differentiable \(f:D\to\mathbb R^n\), an interval
box X containing0, a point c with c+X inside D, and a real matrix R,
the sufficient condition is

\[
 -Rf(c)+(I-RJ_f(c+X))X\subset\operatorname{int}X.
\]

The Jacobian set contains every derivative matrix on the whole box;
a computed interval superset suffices by inclusion. The theorem gives
existence and its stated uniqueness/non-singularity conclusions. Its
proof uses Brouwer's theorem and interval-matrix regularity. Use n=2
for the real and imaginary parts of the exact fixed-slice function.
The real scalar Theorem6.2 from prior coverage alone is insufficient.
Multiple roots can defeat this sufficient test; failure is not
nonexistence. No theorem is reproved here.

**Integration input.** Reuse the inspected hypotheses recorded in
[bulk-haar-integral-enclosure](2026-10-17-bulk-haar-integral-enclosure.md)
and [theta-integrated-layer-compensation](2026-11-01-theta-integrated-layer-compensation-scope.md).
Directly rechecked F. Johansson,
[*Numerical integration in arbitrary-precision ball arithmetic*,
1802.07942v1](https://arxiv.org/pdf/1802.07942v1), 22 February2018,
Sections2–2.1 pp2–3: whole-input-box inclusion is required; the Gaussian
branch additionally requires a certified analytic ellipse and modulus
bound. Section3.2 p6 requires manually bounded omitted infinite or
singular-endpoint pieces. Requested tolerances do not replace the
returned enclosure radius. An evaluation-limit exit can remain valid
but too wide. Outer complex-s parameters must stay interval parameters
throughout the inner integral; midpoint substitution loses the Jacobian
certificate. A validated integral of a theta truncation still needs a
uniform bound for the omitted theta contribution.

**Theta input.** F. Johansson,
[*Numerical Evaluation of Elliptic Functions, Elliptic Integrals and
Modular Forms*, 1806.06725v1](https://arxiv.org/pdf/1806.06725v1),
18 June2018, Section1.4.2, (1.18)–(1.20) pp12–13 and Algorithm1.
The series uses q=exp(pi*i*tau), Im(tau)>0, and its geometric majorant
requires a strictly positive denominator, including the extra derivative
factor when applicable. For evaluating the source's theta(v), use
Jacobi theta3 at z=0, tau=i*v, on boxes with Re(v)>0. These z-derivative
bounds are not derivative bounds in s or in v. The future test must
justify its s-differentiated integrand and its weighted endpoint tail.
The same source bounds support complex callback boxes; they do not
automatically justify a fractional power across a branch cut.

**Executable contracts and limits.** Inspected archived
[Arb2.23.0 acb_calc](https://arblib.org/acb_calc.html), callback and
integration sections, and
[python-flint0.9.0 acb.integral](https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.integral).
Their analytic flag requires rejection of a box meeting a log/sqrt/power
branch cut even if the real integration path avoids it. A finite
enclosure must include all input and rounding errors. The current
FLINT3.7.0-dev acb_calc landing page discloses an ongoing LLM-assisted
documentation revision; it is not an additional proof input.
Default /opt/homebrew/bin/python3 has no flint module; uv and Homebrew
executables are present, but no backend was installed, loaded or
attested. A later implementation may use a temporary local environment
without credentials; failure to obtain a rigorous backend is an
implementation failure, not evidence against a zero. Library versions
and exact rational input conversion must be saved with a certificate.

## Decision and bounded continuation

The primary results suffice for one SPECIALIZE/REPRODUCTION attempt;
they supply no preexisting certificate in the requested domain. Deriving
effective constants for this exact integral is the application difference,
not a reason to reprove Krawczyk, ball integration or the family theorem.
The bounded test and all its proof obligations are in
[the continuation assessment](2026-11-11-two-variable-fixed-slice-krawczyk-test-423.md).
It permits a finite locator stage only as a lead, followed by ONE
validated candidate box and enclosing disk. An inclusion must establish
the exact function's zero, with every tail and branch error paid. An
unvalidated locator, wide enclosure or failed sufficient inequality is
inconclusive and ends this bounded attempt.

Full matching Mathlib coverage for the two-variable family, numerical
enclosure and Krawczyk application has not been checked; availability is
unknown. No new lemma, mathematical script, root search or mathematical
certificate was produced. The local source improvement is an exact
existence criterion and complete error obligations; the main RH gap is
unchanged. Additional reconstruction browsing is not a continuation.
