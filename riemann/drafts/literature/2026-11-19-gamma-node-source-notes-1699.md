# Gamma midpoint node approximation: primary source review1699

Completed task: literature_comparison under assessment1698. The main gap
remains L030-L032/C032a actual-Xi all-degree positivity; the intermediate
target is only the fixed gamma node evaluator. Its plausible use is one
component of dictionary1570's variation-2 residual calculation. The
independent coefficient propagation and residual<1/2 gaps remain open.

## Primary theorem and relevant proof cases inspected

The author-hosted online *Complex Analysis* textbook at
[ComplexAnalysis.org](https://complexanalysis.org/), maintained by
Russell W. Howell (site copyright2024; HTML version accessed19 November2026),
[Section7.2](https://complexanalysis.org/web/sec_taylor-series.html),
Theorem7.2.3 assumes f analytic on a domain containing the open disk
D_R(alpha). For |z-alpha|<=r<rho<R, its proof(7.2.3)-(7.2.7) bounds the
degree-N Taylor remainder by

    M*rho/(rho-r)*(r/rho)^(N+1),
    M=max_(|z-alpha|=rho)|f(z)|, N>=1.

Read the whole relevant proof: the circle lies inside the analytic
domain, Lemma7.2.2 expands the Cauchy kernel, and the reverse triangle
inequality followed by ML gives this bound. It covers complex values
without a mean-value point. At the center the Taylor remainder is zero.
The printed r-definition has an isolated a in(7.2.4); surrounding text
and the kernel use alpha consistently. No estimate for the gamma family
or perturbed denominators is in this theorem.

The same textbook's [Section4.3](https://complexanalysis.org/web/sec_convergence-theorems.html),
Corollary4.3.3, gives the finite geometric identity for z!=1;
its proof refers to(4.3.4), obtained by multiplying and subtracting the
finite sum. Read that proof and the separate |z|<1 convergence case.
The finite identity needs only z!=1; a decaying geometric remainder
additionally needs |z|<1. No gamma-specific reciprocal expansion is
imported or derived here.

NIST *Digital Library of Mathematical Functions*, version1.2.8,
release15 September2026, [4.2.19](https://dlmf.nist.gov/4.2.E19)
defines exp by its factorial-coefficient series; Section4.2(iii) states
entireness, and [4.2.22](https://dlmf.nist.gov/4.2.E22) gives
|exp z|=exp(Re z). [4.28.2](https://dlmf.nist.gov/4.28.E2) gives
cosh z=(exp z+exp(-z))/2 for complex z. These inspected identities
support rational Taylor coefficients and complex modulus bounds.
They do not themselves certify a finite truncation at1/64. Generic
Taylor proof coverage comes from the preceding textbook, not from an
unread DLMF reference.

An initial DLMF1.10(i) read gives convergence but no explicit remainder
bound; it is insufficient alone. Dragomir's RGMIA22(2019), paper2,
[author PDF](https://www.rgmia.org/papers/v22/v22a02.pdf), p.2(1.3),
also states an analytic convex-domain integral remainder. Only that
introductory statement was inspected; its proof and later examples
were not read and are not needed or used. Other search snippets are
unread leads. The failed guessed textbook frontmatter URL is
nonessential; direct theorem pages and the site's home page opened.

## Applicability boundary, duplicates and failures

Read C033b's full exact integrand and its completed critical audit1616,
assessment1614 and ATTEMPTS/gamma-source-review-loop-closed1616.
C033b fixes all4096 positive rational midpoints on[0,16] and exact
function values. Its proof§2 already establishes B(v)>=1/(1+2v)
for real v>=0, with B(v)=(1-exp(-2v))/(2v) for v>0.
This is an available exact-denominator input, without a zero assumption.
It does not bound any perturbed denominator. C033b's derivative1139
and quadrature error are retained; no quadrature reproof is proposed.

Narrow filename and content searches in active drafts/literature,
ATTEMPTS and foundations used gamma/node, gamma/Taylor,
gamma/rational-approximation, node arithmetic and rounded-node terms.
The relevant hits continue to exclude node arithmetic. The older
shared-endpoint-node and Gaussian-node titles concern different
integrands or prescribed nodes and were not imported. No matching
certified formula was located; this is a bounded screen, not a
novelty claim. External queries included complex exponential Taylor
integral remainder, primary complex Taylor error bounds, and
"gamma" "midpoint" "rational" "4096" approximation; no exact
matching full-family result was identified. Standard Taylor tools,+rather than new approximation theory, suffice for the next test.

Stop1616 forbids repeating the completed exact-node quadrature source
question. The present target pays an explicitly excluded component.
Earlier literal-cost1586 and unsupported-contour1608 stops remain
preserved in their recorded scopes; no contour or large-height
analytic continuation is used by this finite compact approximation.
No zero-free-region claim is made, so the quasi-RH baseline is not
being reopened.

## Concrete continuation, without performing it

Candidate mechanism: replace the exponential factors, including those
defining cosh, by fixed factorial Taylor truncations and form a finite
rational-coefficient quotient at every prescribed rational node. The
source theorem supplies an explicit remainder test on any closed
argument disk strictly within a chosen larger disk. This is a
nomination of a construction, not its derived formula or certification.
No reciprocal-series route is essential: exact rational division is
permitted, provided its denominator separation is proved. If a
geometric truncation is used instead, its strict ratio bound must
also be checked. No new family-specific inequality is asserted here.

The research obligations are fixed degrees and rational upper bounds
on all actual argument ranges; full product, reciprocal and weighted
sum error propagation; a positive rational lower bound on every
approximating denominator; and final uniform error<=1/64. A poor
constant may demand a large degree; computational efficiency and
floating-point stability are not established by symbolic certification.
Continue only if all of those obligations can be certified with the
unaltered domain, nodes and panel count. Abandon this construction
upon a failed separation/error bound rather than replacing it with
samples, adaptive panels or unstated precision. The whole closed
complex w disk, w=0 and both sigma endpoints must be covered.

This is SPECIALIZE/REPRODUCTION coverage for later work; no local
approximation bound has been proved. It does not supply coefficient
amplification, gamma-tail recombination, pole/prime/O terms, actual
residual<1/2, signed theta upper control, unsmoothed Xi realization or
all-degree positivity. Spectral use retains C033b/C033a's divisor,
multiplicity, no-ordinate-zero, strip/counting and finite-zero/heat/
fixed-v1 qualifications. The compact approximation itself needs no RH.
Full matching Mathlib coverage is unchecked and unknown. No
cross-notebook mathematical input was read or used.
