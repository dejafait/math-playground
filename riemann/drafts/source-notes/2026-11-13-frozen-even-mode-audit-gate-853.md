# C759n audit gate853 — 2026-11-13

LITERATURE_REASON: Separate approval of nominated audit852 is required;
compare its actual exact-moment/Taylor and Decimal implementation with
ready850 rather than repeat general quadrature discovery.

## Scope, relevance and bounded test

Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
Intermediate target: independently audit C759n's single complete scalar
certificate. Its downstream use is to validate or withdraw the rejection
of one negative matrix indication; ground-state signs, simplicity, parity
and Xi/global assembly remain unresolved. Continue only if all terms,
input identity, positive denominator and full error accounting survive.
An unpaid term invalidates the certificate without proving negativity.
The audit must assess the claimed strict positive lower endpoint; this
source review does not independently establish it.

Used supplied overview/DAG/checkpoint without rereading them. Read all
of C759n, C759a hypotheses and Proof1 domain passage, C759h Proof2's
H1 action passage, script852's interval class and definition locations.
Reused assessment850, source-notes850, approval851 and history/stop852.
No script run, certificate evaluation, mathematical derivation, lemma
edit or cross-notebook read occurred. Python version only was queried:
the present executable reports Python3.15.2; this does not attest which
interpreter produced the old certificate.

## Inspected primary inputs and retained hypotheses

[Connes--Consani--Moscovici, Zeta Spectral Triples, v1,
27November2025](https://arxiv.org/html/2511.22755v1): reread Lemma3.1,
(3.14)-(3.20), Proposition3.2 and its complete logarithmic-isometry,
translation and convolution proof, and the exterior integral preceding
(4.4). The proposition assumes lambda>1, L=2log(lambda) and smooth
inputs on [0,L]. Formula(4.4) is printed for basis entries; (3.15) is
the general functional. The exterior subtraction survives compact
support. This covers the source formula, not C759n's nonsmooth extension
or constants. Audit the smooth-to-H1 passage using the local closed
domain rather than silently enlarge the proposition's hypotheses.

[Suzuki, Weil's quadratic form via the screw function, v2,
arXiv17August2026](https://arxiv.org/html/2606.09096v2): reread
Sections2.3-2.4, the entire cutoff/integration-by-parts case of (2.4),
shift terms/(2.5), zero-extension Fourier case/(2.7), and the
regularized digamma comparison following it. The stated input domain
is H1_0(-a,a); zero boundary traces and the cutoff cancellation matter.
The polar contribution is distinguished in the Fourier comparison.
No small-window positivity or heuristic Section7 is imported. Existing
closed-realization coverage850 and C759a is reused, not independently
reproved or certified by this review.

[NIST DLMF, Section1.9(iii), (1.9.30)-(1.9.31)](https://dlmf.nist.gov/1.9.E31):
read the Cauchy integral and derivative formulas and hypotheses:
continuity inside/on a simple closed contour, analyticity inside,
evaluation point in the interior. This named theorem covers the
coefficient-estimate method. C759n's removable origin, pole-free disk,
boundary bound, finite order and integrated remainder remain audit
obligations; no bound is derived here. This supplies precise coverage
for the actual Taylor method in place of the earlier quadrature lead.

[Conrad, The Remainder in Taylor Series, Theorems1.1-1.2,
PDFp1](https://kconrad.math.uconn.edu/blurbs/analysis/TaylorRemainder.pdf):
read both statements and derivative-bound consequence; reuse850's
previous complete proof coverage. Smoothness on the connecting real
interval and a derivative bound are required. It supports the real
exponential remainder method, not an unchecked C759n constant.

[Python3.15.2 Decimal documentation](https://docs.python.org/3.15/library/decimal.html):
read Context/rounding, Decimal exp/ln/sqrt entries, Context methods,
next_minus/next_plus and ROUND_FLOOR/ROUND_CEILING. Precision, exponent
range and exceptional signals are part of the contract. ln and exp
are documented as correctly rounded with ROUND_HALF_EVEN; a directed
context name alone does not assert directed transcendental rounding.
Adjacent representable endpoints are separately documented. The audit
must check actual calls and widening, sqrt's contract, input domains,
conversion and context use, including operations outside Context methods.
These documentation contracts are software trust, not formal verification.

[Python3.15.2 Fraction](https://docs.python.org/3.15/library/fractions.html#fractions.Fraction):
read constructor, rational arithmetic and exact-value qualification for
as_integer_ratio inputs. [Built-in numeric types](https://docs.python.org/3.15/builtins/stdtypes.html#numeric-types-int-float-complex)
is the primary integer/float contract lead; its detailed arithmetic
subsections were not inspected here. Exact input loading and integer
packing still require implementation review. No library theorem
certifies the packed convolution or the NPZ hash.

## Comparison, duplicates, failures and decision

Scoped searches: frozen-even-mode November13 assessments, histories and
stop, for frozen, convolution, Taylor, decimal and Cauchy. No second
completed audit appeared in this family. General source queries and
Zhu's scalar-certification overlap are already recorded in source-notes850;
reuse that inspected comparison, with no new claim of novelty. Its
Arb/Petras and Trefethen coverage is optional background: script852
does not call those algorithms. No further quadrature search is needed.
Stops823/829/831/838/843/849 and the exact scope of rejection852 stand;
the proposed audit neither repeats their tests nor reopens them.

SPECIALIZE: ready for one independent conceptual/implementation audit.
Exact finite polynomial identities and standard analytic remainder
methods need input-specific checking, not a new general theorem or a
reproof of imported formulae. Check the complete saved arrays, norm,
errors, prime delays/weights, poles and input identity in research;
none was evaluated in this literature turn. Existing certificate and
lemma remain pending review. Matching Mathlib coverage is unchecked.

Outcome EXPLORATION: completed a bounded source comparison and added
precise coverage for the actual Cauchy/Decimal implementation; no new
mathematical advance, independently verified sign or error was obtained.
No creative central mechanism is justified by this audit nomination;
finish the essential audit before selecting further work. The approval
applies to the unchanged exact target in assessment852.
