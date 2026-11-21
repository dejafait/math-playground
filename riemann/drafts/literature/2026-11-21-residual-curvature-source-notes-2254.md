# Fixed residual-curvature source review2254

Completed, 21 November2026. Literature only: no residual identity,
new inequality, calculation, lemma or mathematical script is established.

The startup target is review2253's fixed W_x>0 question. The main gap is
L030-L032/C032a actual-Xi all-degree mixed positivity. A direct curvature
condition might help define a residual shape class for later removal;
neither preservation nor an all-degree interface is supplied by decrease.
Continue only with a matching theorem or a bounded full-box test. A
certified nonpositive value defeats the stronger box, not necessarily
actual-root curvature; an enclosure meeting zero is inconclusive.

Read the supplied overview/DAG before detailed inputs. Narrow local reads:
L019, L058, C919m hypotheses/conclusions, source/normalization and full-tail
proof, origin compatibility and audit qualifications; C919r statement,
source section, complete derivative/index/spatial bounds(5)-(11); source
notes2230/2249 and2239's theorem comparison; stops2253 and408. Existing
changes remain intact. C919q is contrast only; no cross-notebook input.

## Primary statements and relevant proof cases

G. Csordas, *Convexity and the Riemann zeta-function*, Glasnik
Matematički33(53)(1998),37-50,
[Corollary2.11 and full proof, printed p43](https://web.math.pmf.unizg.hr/glasnik/33.1/33105.pdf).
The original theta kernel Phi is PF2: all two-by-two translation
determinants with ordered arguments are nonnegative. Its proof uses
the known square-coordinate concavity, even smooth extension, and
convexity of -log Phi on the real line. Both cases a=b and a<b in
the convexity comparison were read. This establishes no closure under
division of the Fourier transform by a real-zero factor. It is a
primary scope check of an already known input, not a new result.

G. Csordas, *Fourier transforms of positive definite kernels and the
Riemann xi-function*,
[arXiv:1309.0055v2,21February2014](https://arxiv.org/pdf/1309.0055v2),
Theorems3.5/3.7 and4.5, printed pp6-8,11. Reused2230/2239 coverage;
newly read3.5's complete proof, including s<t and s>t cases. It assumes
a strictly log-concave admissible kernel and concludes admissibility
of weighted product-correlation kernels. It does not conclude their
log-concavity or treat sine-resolvent division. The3.7 characterization
still requires positive definiteness of every such kernel. The4.5
theta specialization cannot supply W_x. Example3.12,p9, is only a
qualified warning: its log-concave Gaussian-polynomial kernel has
nonreal Fourier zeros but fails admissibility's stronger decay
condition(v). It is not an actual-Xi or quotient-kernel counterexample.
No fresh application of these theorems is made.

A. Prékopa, *On logarithmic concave measures and functions*, Acta
Sci.Math.(Szeged)34(1973),335-343,
[Theorems6-7 and full proofs, pp342-343](https://acta.bibl.u-szeged.hu/14411/1/math_034_335-343.pdf).
Also read the author's [retyped version](https://rutcor.rutgers.edu/Prekopa/pdf/SCIENT2.pdf),
pp8-9, and the nonnegative-function convention in the introduction.
Theorem6 preserves log-concavity under integration over a convex set
for a jointly log-concave nonnegative function. Theorem7 preserves it
under convolution of two log-concave nonnegative functions. The proofs
use zero-extended nonnegative sections and a product, respectively.
These hypotheses do not hold for the displayed sine-weighted
integrand. No representation by an eligible nonnegative integrand is
available in the local inputs. Thus neither theorem imports the
desired sign; this is a failed direct application, not a theorem that
no other representation or preservation law exists. Neither conclusion
alone supplies a strict uniform differential lower bound.

The exact mathematical comparisons above use the primary texts.
PDF screenshot calls yielded no inspectable image content; parsed
complete relevant proof ranges were read instead. Shell downloads
failed DNS for all three hosts. That did not block the primary web
text or justify treating an unread page as inspected.

Preserve the old source qualifications: Wintner/Spira originals unread;
optional Spigler access remains parked; reciprocal-density results are
not statements about G_x. No source miss establishes novelty.

## Bounded searches and optional lead

Queries actually run included these exact strings and close variants:

- `"sine transform" "log-concavity" kernel`;
  `"Riemann" "division" "kernel" "log-concavity"`;
  `"real zeros" "Fourier" "division" "log concave"`.
- `"Fourier" "real zero" "log-concavity" kernel division`;
  `"sine" "resolvent" "log-concavity"`;
  `"Fourier" "deconvolution" "log-concavity" zeros`;
  `log concavity sine integral shifted kernel real zero division preservation`.
- `Csordas 1998 Corollary 2.11 Riemann kernel log concavity`;
  `Prekopa 1973 On logarithmic concave measures and functions theorem 6 pdf`;
  `"Koumandos" "2016" "log-concavity" pdf sine`.

No matching residual theorem was identified in this bounded search.
Unrelated RH claims, aggregator summaries and search snippets are not
inputs. The reciprocal-density search hit merely reconfirmed2230's
different object; its primary source was not reopened. New optional
lead: S. Koumandos, *On the log-concavity of the fractional integral
of the sine function*, J.Approx.Theory210(2016),30-40,
[doi:10.1016/j.jat.2016.06.004](https://doi.org/10.1016/j.jat.2016.06.004).
The publisher abstract/metadata were read; its mathematical formula
was not rendered and its theorem/proof remain unread. No application,
parameter range or preservation theorem is attributed to it here.
It is optional for the explicit bounded test; no repeated access
attempt is required before using already covered calculus.

## Adequate tools and the remaining specialization

Reuse inspected source notes2249 and approved2251/2252: Conrad
Theorem12.3,p16 for dominated parameter differentiation, Tao's named
dominated convergence/Fubini/Tonelli statements, NIST DLMF3.5.6-8
for composite Simpson, Strang--Herman Calculus2 Theorem6.7 for real
Taylor remainders, and the Python Decimal contracts. Exact links and
hypotheses remain in2249/2251 and C919r. No new general theorem is
needed for interval addition/multiplication of certified real bounds.
Conrad refers out for the proof and Tao omits the general proofs;
these are named standard inputs, not independent recertifications.

C919m already supplies the half-line integral, its first derivative
and ODE second derivative, with complete qualitative tails. Its
smooth even inverse-quotient interpretation still requires an actual
root. C919r(5)-(11) supplies finite-order derivative/index/spatial
bounds, with orders0 through17, and its(12)-(14) signed jets were
read for applicability. They may support a later finite certificate;
neither the old cosine margins nor a preview of its saved certificate
is a curvature bound. No certificate was run or inspected for a new sign.

The later specialization must choose and save one finite setup before
its sign pass, verify every used derivative order is covered or pay
any extra one, and enclose G_x,G_x',G_x'' jointly enough to control
the nonlinear expression. Both omitted theta indices and spatial
tails, quadrature error, arithmetic error, and interpolation remainders
must enter before taking products or squares. Whole closed parameter
cells and all four boundary faces are required. At nonroots do not
set G_x'(0)=0 or use a smooth even extension; only right derivatives
are in scope there. At actual roots C919m supplies those interfaces,
with multiplicity allowed. No new identity or bound is derived here.

The copied numerical constants need not be adequate after multiplication
and cancellation. A failed enclosure is inconclusive. Any positive
claim needs an explicit rational lower bound on the entire unchanged
box; any rejection needs a rigorous value/enclosure proving W_x<=0.
Record failed bounds instead of shrinking the box or retuning repeatedly.
Arithmetic contracts remain assumptions, including integer/Fraction,
directed basic operations, representable neighbors and HALF_EVEN exp.
Neither runtime nor backend is independently verified in this review.

## Decision and limits

SPECIALIZE: the ordinary rigorous-quadrature technique and exact local
kernel inputs are covered. The fixed determinant sign and effective
error budget are unpaid specialization obligations. The proposed
calculation is reproduction/specialization, not a creative preservation
mechanism or a claim of progress beyond known sources. No essential
source is blocked. Full matching Mathlib coverage remains unchecked;
absence is not asserted.

Outcome EXPLORATION: a new scope comparison and bounded search select
an independently testable continuation; no mathematical advance or
impossibility is established. Stop408 concerns a coefficient sequence,
not continuous G_x curvature. Stops2238/2241/2243/2246/2248/2253 keep
their scopes. Success on this box would still leave exterior curvature,
later-removal preservation and actual-Xi all-degree transfer unresolved.
No justified central creative attempt is nominated: those two latter
interfaces lack a concrete discriminating mechanism. The finite test
may inform one; it must not be relabeled creative to fill a quota.

The exact calculation nomination is assessment2254. It is written ready
for a separate next-turn literature approval; no mathematical work is
invoked in this turn. PROOF and DAG are unchanged because the argument
is unchanged. No lemma, mathematical script or supervisor state changed.
