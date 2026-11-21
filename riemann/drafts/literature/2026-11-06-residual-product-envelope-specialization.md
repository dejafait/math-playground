# Residual-product effective envelope — proposed specialization

TARGET: Construct an explicit unconditional bound for L835's log(M_s/m_1) at k=6002 using the first omitted pole and L467's zero-count envelope, with a certified finite-data interface and the overlap test left explicit.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step675's exact quotient/product-tail searches and duplicate/failure comparison in 2026-11-06-residual-product-contour-ratio-scope.md; no changed analytic hypotheses or new source claim.
SOURCE_EVIDENCE: L832 genus-zero product and audited L834/L835; Katkova https://arxiv.org/pdf/math/0505174v1 (6) p.3 and pp.5–6; audited L467 and Bellotti–Wong https://arxiv.org/pdf/2412.15470v2 Theorem1.1 p.1, Section5 pp.23–24; optional Brent–Platt–Trudgian https://arxiv.org/pdf/2009.13791v1 Theorem1 p.2, Lemma3 pp.6–7, limiting proof/Example1 pp.8–9, under the previously recorded weight and endpoint hypotheses.
COMPARISON: Known inputs supply convergence, the actual zero map and explicit unconditional counts. They do not supply this quotient bound, certified zero enclosures or overlap. Only the local effective specialization is proposed; no general theorem needs reproof.
GAP: Produce an evaluable expression B for log(M_s/m_1), isolate the first omitted factor, prove tail/endpoint estimates and specify the rational data and separation conditions needed for certified evaluation. No expression or numerical data is supplied in this literature turn.
REASON: Essential source coverage is inspected. A bounded standard construction tests effectiveness without inverse Vandermonde norms, residual PF_infinity or an assumed lower contour bound. Separate literature-only recovery review on 2026-11-06 repaired direct primary URLs and confirmed unchanged scope; no mathematical construction performed.
SCOPE: One fixed-k effective-envelope construction and comparison with L835(4), initially s=(1+q)/2. No sweep, extra shift, enlarged PF theorem, zero-data implementation or general product/count theorem reproof.

The main gap is actual-Xi all-degree mixed positivity. Essential inputs
are audited L832/L834/L835 and count input L467, retaining inherited
L018/L021/L776 conventions. Keep k=6002, actual distinct simple
p_1,...,p_(k+1), R=(p_k+p_(k+1))/2 and q=p_k/R<s<1. Use exactly
L835's quotient g; no analytic model replacement is allowed.

Seek a finite evaluable upper bound B for log(M_s/m_1), first at the
exact s=(1+q)/2. Specify a finite-data interface, for example rational
enclosures of the two endpoint ordinates with certified indices and
separation. Additional finite records require explicit justification;
none is assumed present. R is defined by exact zeros: any interval
evaluation must enclose it, not replace it by an unrelated radius.
The full packet's finite factors remain payable for overlap.

Separate the first omitted simple factor and bound the rest through an
explicit count tail or a specified convergent majorant with a certified
truncation error. An unknown convergent sum, supremum or minimum is not
effective. Preserve multiplicities, endpoint conventions and the square
map's positive-height representatives; retain possible off-line zeros
above H. A complex logarithm branch cannot replace a justified modulus
estimate and compact-limit argument.

The plausible downstream use inserts B into L835(4). Retain the entire
finite-product cost and integer m, stating precisely the inequality a
numerical certificate must satisfy. Only PF6001 is currently established.
A larger m needs separate applicability justification. Even successful
overlap covers just this fixed shift; growing shifts, other minors and
RH remain open.

Continue if the formula is computable from the stated finite data and
explicit unconditional sources without assumed contour lower bounds or
hidden high-zero data. A rigorously evaluated majorant missing L835(4)
fails this sufficient certificate, not positivity. An unevaluated B
proves no overlap. Preserve failures and require materially new input
before repeating an unsuccessful bound. This nomination authorizes no
numerical zero computation or sweep.

This is a routine quantitative specialization, not a creative mechanism.
The missing actual bound supplies no evidence for a new central sign
mechanism. Full matching Mathlib coverage remains unchecked. No lemma,
proof or mathematical script is modified in this nomination.

## Direct-source recovery review — 6 November 2026

The source-URL defect is repaired in SOURCE_EVIDENCE above. Opened the
versioned [Bellotti–Wong primary PDF](https://arxiv.org/pdf/2412.15470v2)
and checked Theorem 1.1 on printed p.1: the first bound holds for every
T>=e, with constants 0.10076, 0.24460 and 8.08344 and positive-height
upper-inclusive counting. Reuse the inspected Section5 cases and the
multiplicity/endpoint treatment recorded in L467 and the step675 source
comparison; no source computation or full-manuscript audit is claimed.
The product and optional sharper-tail primary passages remain those
already inspected in that comparison; they were not rederived or
retrieved again. The optional sharper tail is not needed for readiness.

This separate review approves exactly TARGET above under the unchanged
SPECIALIZE scope. It adds no mathematical evidence beyond step675:
no quotient estimate, certified finite zero records, lower contour bound,
PF enlargement or overlap is established. The existing duplicate and
step659/667 failure comparison remains applicable. Full matching Mathlib
coverage is unchecked. The calculation is ready for the next research
turn; its hypotheses and continuation/abandonment test above remain paid
only when explicitly verified in that calculation.
