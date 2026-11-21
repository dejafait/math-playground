# Coverage: a local terminal-root discriminator

TARGET: Test whether, near one arbitrary interior critical-line zero of xi', the u->1- left-half-plane branch count is exactly L958's kappa after retaining any persistent common-zero factor, under Re(H'/H)>0.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step128 searched completion-parameter zero crossings and Kim critical multiplicities/perturbation, and checked relevant local xi/critical/boundary assessments and failures. No matching already completed local branch test was found; this is a standard local-zero specialization, with no novelty claim.
SOURCE_EVIDENCE: Gantumur2015 author notes Theorem15 p8 (Rouche, weighted full-order count), its complete homotopy proof, Theorem18 p8 and Section5 p9 local multiplicity argument; DLMF5.11(i) equation5.11.2 with sector condition and 5.11(ii) complex remainder qualification. L958's canonical kappa definition and common-zero conventions were read.
COMPARISON: Known local factorization and Rouche supply multiplicity-preserving small-disk tools without a global parameter-boundary exclusion. Neither their generic statements nor L958 explicitly performs the actual completion-family orientation and kappa comparison; only that local specialization is to be derived, not a new root-count theorem.
GAP: Determine the one-sided half-plane allocation for all finite local orders and compare with kappa, retaining common factors. No full interval index, uniform height-scale perturbation, signed saving, K bound or Xi critical sign is covered or assumed.
REASON: Replace the unsuccessful global-index import by an independently checkable terminal-root test. Equality with the existing weight would stop this local mechanism as a source of independent sign control; a demonstrably different datum would need separate assessment before further work.
LITERATURE_REASON: The fixed-interval index search exposed missing intermediate-boundary coverage. This narrower local continuation uses directly inspected small-disk theorems and can be tested without constructing the missing index.
SCOPE: One arbitrary fixed interior critical-line point s0=1/2+ix, a<x<b, with xi'(s0)=0 of finite positive order; use actual H and explicitly assume Re(H'/H)(s0)>0. Include xi(s0)!=0 and common-zero cases of every finite order. No claim about interval endpoints, all u, or uniform choices as height varies is covered.

## Sources actually inspected

Tsogtgerel Gantumur, *Isolated singularities and meromorphic functions*,
16 April2015, [author notes](https://www.math.mcgill.ca/gantumur/math249w15/residue.pdf),
Theorem15 p8: meromorphic f,g on Omega and a null-homologous cycle
gamma, with |f-g|<|g|<infinity on its trace, have the same
index-weighted sum of orders. Its proof keeps the entire linear
homotopy nonzero there. Theorem18 p8 requires a bounded subdomain
compactly inside Omega, locally uniform convergence, and a zero-free
limit on its boundary. Section5 p9 factors a finite-order zero and
uses small circles to give the exact local number of nearby preimages.
These statements retain full multiplicities; they assert no
half-plane allocation at a boundary point. That allocation is the
specific specialization left for the mathematical turn.

For the completion coefficient use the
[DLMF5.11(i) sector condition and equation5.11.2](https://dlmf.nist.gov/5.11#E2):
psi(z) has its stated logarithmic asymptotic expansion as z tends
to infinity with |arg z|<=pi-delta, fixed delta>0.
[Section5.11(ii)](https://dlmf.nist.gov/5.11#ii) separately qualifies
complex remainders by an angular secant factor; a positive-real-axis
remainder sign is not available off that axis. This source is
support for a later applicability check of the explicit local
Re(H'/H)>0 assumption, not a derived sign statement in this review.
No effective universal onset or low-height coverage is imported.

The Luxembourg local-normal-form PDF timed out, and a large Favre
lecture PDF was rejected by the web fetcher for size. Neither snippet
is used. Those sources are unnecessary: local Taylor factorization
and the inspected Rouche theorem provide the required tools.
Delay-equation Puiseux papers remain unread, nonessential leads.

## Bounded mathematical test after separate approval

Use the exact G_u and H of the completed step128 assessment, L018's
coordinate change and completion, and L958's full-order kappa
conventions. Fix the point before choosing neighborhoods or taking
u->1-. For a noncommon critical root, justify isolation, obtain
all nearby branches with their orders, establish their side of the
critical line for sufficiently close u<1, and compare that count
with kappa for every parity and permitted sign. A leading picture
or a finite numerical root plot is insufficient: small-circle
error control must justify the claimed allocation and exclude
unaccounted local branches. Do not assume simplicity.

For a common zero, factor its persistent local divisor before any
division and retain its full order in the original family. Report
boundary branches as boundary branches. The noncommon definition
of kappa must not silently absorb a common-root contribution.
The local Re(H'/H)>0 hypothesis remains explicit unless its
large-height applicability is separately justified from the cited
digamma expansion within this bounded specialization.

Continue toward a new mechanism only if this comparison exposes an
additional independently measurable local term. If it exactly
recovers the old weight, record that obstruction and stop this
local-sign route; it does not establish K=0 or refute RH. An
unresolved local case stays unfinished rather than being replaced
by a generic transverse-crossing assumption. Local scale and
perturbation thresholds may depend on the fixed point and its
order; summing them or taking height-uniform limits is outside scope.

This ready continuation was written during step128 and requires
the supervisor's separate approval on a later turn. No local
splitting formula is derived or approved as proved here. A subsequent
mathematical step is a REPRODUCTION/specialization, not creative
new mathematics. Full matching Mathlib coverage is unknown; no
cross-notebook input. The central mixed-positivity and independent
critical-sign gaps remain open.
