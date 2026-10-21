# Supported Kummer containment — audit scope approved

TARGET: Critically review L075's full global Kummer containment in L074's W_S for the fixed model and complete support above 2 and 11.
CHECKED: 2026-10-15
DECISION: IMPORT
SEARCH_EVIDENCE: Reused the exact searches and duplicate checks in drafts/literature/2026-10-15-supported-kummer-containment.md; compared L075 in full, L033 hypotheses and field/curve definitions, L069 hypotheses and integral-model/irreducibility proof, L074 supported-space definitions, history/239 and ATTEMPTS/032–033. No fresh external search was necessary or performed.
SOURCE_EVIDENCE: Reused the previously inspected primary theorem and complete relevant proof cases in Simon, Computing the rank of elliptic curves over number fields, LMS J. Comput. Math. 5 (2002), Propositions 1.1–1.2 and 1.4, printed pp.8–9; precise source and read scope are recorded below and in the prior assessment.
COMPARISON: The proposed audit remains inside the previously covered global irreducible integral-cubic theorem, on the identical K, g, theta and complete support. O, coordinate denominators, square norm and absence of sign conditions are already covered; no split-local-algebra extension, sharper support theorem or new theorem is required.
GAP: Essential source coverage is ready; the independent critical application review of L075 itself is still outstanding. No correctness verdict, dimension, class computation or rank conclusion is supplied by this scope approval.
REASON: Approve only a separate KNOWN_IMPORTED application audit against the reused theorem and canonical inputs; reproof and additional discovery would duplicate adequate coverage.
LITERATURE_REASON: The supervisor required separate approval of the newly proposed critical-review scope; this turn compares that scope with ready coverage rather than repeating source discovery.
SCOPE: Exactly TARGET, for L033's entire K and E0, L069's fixed integral irreducible g and theta, L074's maximal-ring W_S and all primes above two and eleven; only a critical audit of the known-result application is approved.

## Source coverage and reuse

Denis Simon, *Computing the rank of elliptic curves over number fields*,
LMS J. Comput. Math. **5** (2002), 7–17, published 17 April 2002,
[DOI](https://doi.org/10.1112/S1461157000000668),
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8FAFF26D93D01A154C51CF897E4BE6CD/S1461157000000668a.pdf/computing_the_rank_of_elliptic_curves_over_number_fields.pdf).
The prior [assessment](2026-10-15-supported-kummer-containment.md)
records inspection of printed pp.8–9, including the complete support
proof: negative valuations, odd nonnegative valuations away from the
derivative, and the discriminant-valuation-one case. This turn reuses
that evidence, without claiming a new primary-source read.

The source setting is a number field k and y²=P(x), with P a monic
integral irreducible cubic and L=k(theta). Propositions 1.1–1.2 give
O -> 1, finite points -> [x-theta], kernel 2E(k), and square norm.
Proposition 1.4 permits infinite places and finite primes of L dividing
P'(theta) whose underlying prime p has p² dividing disc(P). Its
supported square classes impose even valuations elsewhere, without
sign conditions. This statement and all needed proof cases were already
covered; no new source hypothesis was introduced by asking for an audit.

## Exact audit boundary

The later audit must independently verify the canonical application:
L033's entire degree-twelve field and E0; L069's same theta, model
X=4x, Y=8y+4, g=X³−4X²−160X−1264, irreducibility and polynomial
discriminant −256·11^5; and L074's supported field square-class groups,
normalized maximal-prime valuations and norm kernel. The two uses of
theta must be distinguished: L033's named dual five-isogeny is not the
cubic generator theta in L069/L074/L075. L075's delta_2 is two-descent,
not L033's fifth-power connecting map. These are audit checks, not new
mathematical claims or a completed application verdict.

Check origin preservation and the transported formula [4x−theta],
nonzero evaluation at every finite global point, the kernel/injection,
every outside-support maximal prime, denominators and square norm.
Use the polynomial discriminant in O_K, not the field discriminant or
a polynomial-order maximality assumption. Retain every prime over two
and eleven. Do not extend the irreducible global statement to split
completions. The current task does not require reauditing the whole
L074 quotient proof or recomputing L069 certificates; inspect their
load-bearing interfaces and any specific suspected defect.

ATTEMPTS/032 still parks the unfiltered rank shortcut. ATTEMPTS/033
still parks deletion of eleven by universal local evenness. Neither
stop prohibits this retained-support application. L075 is the existing
canonical application; another lemma would duplicate it. No cross-notebook
input is used. Full matching and supporting Mathlib coverage remains
not checked; no absence or novelty is inferred.

## Relevance and continuation test

The main gap remains primitive integer emptiness, including ordered
(3,4,11). The intermediate target is a critical verdict on L075's full
global containment. A successful audit would secure the ambient-space
interface needed before S-unit/S-class arithmetic and simultaneous local
pruning can support a useful descent bound. It would not supply that
bound or resolve the independent integer-lifting gaps.

Pass only if every cited theorem hypothesis and transported map covers
O and all finite global points at every outside-support maximal prime.
If a mismatch appears, isolate its precise premise and withhold dependent
use pending correction or separately assessed work. No new valuation
lemma or mathematical script is approved. Unresolved work includes this
audit, complete S-unit and S-class data, global odd-class realization,
simultaneous filtering, useful dimension, rank, subgroup indices/cosets
and primitive integer lifting. No complete candidate exists.

This is scope approval only. It adds no source theorem or mathematics
beyond the ready import assessment; the independent audit is the next
research step.
