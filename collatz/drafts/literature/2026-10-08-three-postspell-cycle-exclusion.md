# Three-word cycle exclusion — approved application scope

TARGET: Exclude actual closed concatenations of exactly three postspell words by combining L041 with the published primitive odd-count lower bound, retaining repetitions and independent exact tails.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the four recorded general-cycle queries and primary coverage in 2026-10-08-two-postspell-cycle-length-comparison.md and the multiword audit assessment; narrowly checked L040/L041, histories 093–097, Attempt 019 and history 069 for overlap and failures; no renewed discovery search.
SOURCE_EVIDENCE: Reopened the published Simons–de Weger Acta Arith. 117 (2005) PDF, sections 1.1–1.3 pp. 51–53, including period/count definitions, Lemma 1, Corollary 2 and its complete proof; reused coverage of L041’s inherited cycle estimates and correction qualifications.
COMPARISON: Corollary 2 covers the nontrivial primitive cycle independently of the full minimum count; L041 supplies the audited r=3 represented ceiling and count scaling. A local application remains to be written; neither the source nor L040 is a ready proof of this exact three-word application.
GAP: Write the restricted exclusion from L041 and the cited primitive odd-count bound, retaining count conversions and source qualifications; no three-word closure converse or universal descent is supplied.
REASON: Essential coverage matches the exact target and unchanged L041 hypotheses; approve one RESEARCH/REPRODUCTION application, importing the general theorem without reproof or a novelty claim.
SCOPE: Exactly r=3 under all L041 hypotheses: integer J_i>=2,H_i>=3,a_i>=0 congruent to 2 modulo 18; actual positive closed concatenation from n_0>1 with positive odd residue-20 junction occurrences; arbitrary independent exact tails, repeated periods and coincident junction values.

The main gap remains universal eventual descent. The intermediate target
is exclusion of this exact three-word cycle language; a successful result
would remove one additional restricted cyclic itinerary, leaving entry,
other word counts, arbitrary cycles and divergence unresolved. Continue
only if the sourced lower bound applies to the nontrivial primitive
cycle and is incompatible with the represented ceiling under precisely
these hypotheses; otherwise state the mismatch and stop this comparison.

Essential local input: L041's audited N<11000 bound and its
primitive/represented occurrence argument. Proposed external input:
Simons and de Weger, *Theoretical and computational bounds for m-cycles
of the 3n+1-problem*, [Acta Arithmetica 117 (2005), Corollary 2 and
proof, p. 53](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
Reuse the primary-source notes in
`drafts/literature/2026-10-08-two-postspell-cycle-length-comparison.md`
and the approved L041 audit assessment before considering any refresh.
The intended comparison must preserve K_0<=K<N, rather than identify
primitive odd count with total length or the full minimum count with 3.

The published height x_min>301*2^50 and continued-fraction denominators
225644606 and 397573379 remain imported computational inputs. Rhin's
original proof and underlying computation certificates are not locally
certified. External Lean build/version and full Mathlib coverage remain
unchecked. No least-root or global-minimum identification, tail cap,
primitive-word assumption or three-word closure/divisibility converse
may be added silently. L031's two-word converse is not such a converse.

Attempt 019's guard-only failure and history 069's full-minimum-count
mismatch remain preserved; neither prevents this independent length
comparison. No new lemma or exclusion is established here. The exact
application scope is now approved; the completed audit remains valid.

## Completed source-scope review — 2026-10-08

LITERATURE_REASON: The saved application target was REVIEW_REQUIRED; this separate scope comparison resolves its essential approval gap using ready source coverage, without repeating discovery or performing the application.

The published PDF was reopened only for its essential theorem hypotheses
and proof cases. Sections 1.1–1.2 use the same shortcut map, define K as
odd inputs, permit a nonminimal period and define trivial cycles as
repetitions of {1,2}. Corollary 2, printed p. 53, gives K>225640000 for
nontrivial cycles without a fixed m restriction. Its full proof invokes
Lemma 1, the computational height input and the two continued-fraction
denominators recorded above. These are imported published inputs;
Crandall’s original proof remains unread rather than silently certified.
No stronger theorem or independent reproof is needed.

For the local scope comparison, L041’s Hypotheses, Conclusion,
“Occurrence counts and the sourced cycle estimates,” relevance section,
primitive-period audit passage and Mathlib section were read. The prior
audit covers its ceiling derivation; it was not redone here. L041
expressly records nontriviality, represented K<N and primitive scaling
independently of word count. These established passages supply the
planned bridge to Corollary 2. The application must explicitly invoke
them and retain all three word occurrences even when values coincide.
It must apply the source to the actual primitive orbit with its full
minimum count, rather than set m=3 or identify a designated junction
with the global minimum. This approves applicability, without deriving
the exclusion.

L040’s inspected hypotheses and imported-theorem section concern two
words and include an arithmetic converse furnished by L031. They are a
method comparator, not a duplicate three-word result or a converse
available here. The scoped histories record a proposed three-word
application, not a completed one. Attempt 019 and history 069 were read:
they stop guard-only and count-only mechanisms, respectively, and do
not block this represented-length application. The ready assessment’s
June 2026 Hercher correction review is reused; Theorem 21 is outside
L041’s load-bearing inputs. No priority inference follows.

Continue with the exact application only while its hypotheses and
primitive-to-represented bridge remain those audited in L041. If a
missing guard or mismatched count is discovered, preserve the ceiling
and record the precise failure; do not add an uncovered closure converse
or least-root assumption. The source threshold and recorded ceiling
pass the scope comparison, so the next turn defaults to mathematics.
Entry, other word counts, arbitrary cycles, divergence and universal
descent remain independent gaps. Full matching Mathlib coverage and
the external Lean build remain unchecked. No cross-notebook input is used.

This is EXPLORATION, LITERATURE/NOVELTY_UNCHECKED: a new application
scope was reviewed and approved without a lemma, mathematical script,
exclusion proof or progress beyond the checked sources. It spends no
mathematical exploration turn and claims no counter reset.
