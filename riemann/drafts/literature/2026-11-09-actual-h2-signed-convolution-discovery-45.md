# Parameter sign variation through a signed convolution measure: source comparison

TARGET: Assess primary coverage for a fixed signed-convolution Laplace representation of a positive normalization of actual det H2(lambda) on [0,1/20], and nominate one bounded test of an at-most-one-sign-change criterion or retire this mechanism.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Step46 checked notebook-local Laplace/Descartes/signed-convolution terminology and relevant contact/H2 failures; inspected primary sources below and searched exact actual-theta/logarithmic-Hankel variants. No inspected result supplies this actual energy-density crossing bound; no novelty claim follows.
SOURCE_EVIDENCE: Tokarev, J.Aust.Math.Soc.91(2011),415–420, Definition5, Theorems1/7, Remark8 and proofs pp418–419, DOI10.1017/S144678871100156X; Bhaskar–Song, Ann.Statist.42(2014),2469–2493, arXiv:1309.5056v3, Definition3, Theorem4 and complete proof (reprint pp7–9,14); NIST DLMF1.14.30–31. Links and qualifications below.
COMPARISON: A known density-level Laplace zero-count theorem covers multiplicities after explicit convergence checks; it supplies neither the actual representation nor its crossing bound. L917 fixes finite-log algebra. Spatial contact one-crossing, generic Stein, derivative-sign and shared-Taylor stops concern different premises and remain intact.
GAP: Proposed normalization M_0^12, exact fixed density, regularity, nonzero interval, absolute exponential moments and sign variation require proof. Endpoint signs, other degrees, realization and global continuation remain unpaid.
REASON: Completed one bounded source review and nominated one actual-law ordered-energy-mass obstruction test. This is EXPLORATION with method coverage, not a representation proof, sign result or advance beyond checked literature.
LITERATURE_REASON: Startup REVIEW_REQUIRED scope lacked inspected Laplace zero-count coverage; spatial-contact assessments do not cover this changed parameter mechanism.
SCOPE: Completed literature-only comparison for actual d=2 on [0,1/20]. No mathematical derivation, lemma or script. The new fixed-cell continuation requires separate next-turn approval. Full/supporting Mathlib coverage remains unchecked.

## Original nomination — step45, preserved

Pre-review coverage statements below describe nomination status; the
completed comparison and top fields supersede them.

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. The proposed intermediate input is an independently sufficient
bound on parameter zeros for this actual finite determinant. A successful
at-most-one-sign-change result, together with separately justified endpoint
signs and the precise zero-counting qualifications, might exclude an
intermediate negative region. Other degrees, tangency, initialization and
global continuation would remain independent gaps. This is not yet a
proof that a suitable measure or low sign variation exists.

The new discriminant is the sign variation of an explicitly specified
signed measure on total squared spatial energy, rather than the sign of
a pointwise score-corrected polynomial or independent moment intervals.
The source review must first determine whether products of the actual
unnormalized moments can be assembled into the required *fixed* measure
without losing positivity of the normalization or exponential integrability.
It must retrieve primary theorem hypotheses and relevant proof cases for
any proposed Laplace variation-diminishing implication, including treatment
of zero masses, support endpoints, repeated zeros and signed densities.
No such implication is imported from memory here.

Continue only if the review can nominate one finite, falsifiable test of
the necessary signed-measure premise under those hypotheses. Retire this
mechanism if the premise is already refuted, circular, unsupported by the
representation or merely another independent-box/pointwise-score condition.
An inaccessible essential source must be recorded as SOURCE_BLOCKED;
repeated access failure does not justify another source loop. The review
may instead identify a precise already-covered alternative, while preserving
all original stop evidence. No research calculation is authorized by this file.

Known contrasts checked at nomination: L937's fixed coefficient-box stop;
the audited generic monotone-Stein counterexample in L607; the whole-support
Gaussian-derivative stop in L806; and L916's global inverse-score convexity
stop, through their concise ATTEMPTS records. They do not automatically
ban other actual-theta mechanisms. The existing H2 shared-Taylor comparison
is already SPECIALIZE and cannot count as newly discovered here. These
contrasts do not substitute for the next turn's theorem-level comparison.

Essential prospective inputs: L019, L058 and L874; exact normalized-moment
and finite-log conventions must be read before any later derivation.
L936/L937 are contrasts, not premises of actual positivity. No cross-notebook
input. Full and supporting Mathlib coverage for this target is unchecked.

## Completed source review — step46, 9 November 2026

### Relevance and exact object

The main gap is L030–L032/C032a actual-Xi all-degree mixed positivity.
The intermediate target is a parameter zero-count bound for actual
L874 H2, not a raw moment Gram determinant. Read L019/L058, L874's
definitions and finite-log/response proof, and L917's audited six
coefficient polynomials and determinant formulas. A successful full
crossing bound could combine with independent strict endpoint signs
to support finite-degree contact exclusion. Other degrees,
initialization, realization and global continuation would remain open.
No representation or sign was derived here.

### Primary hypotheses and proof cases actually read

Daniel V. Tokarev, *A generalisation of Descartes' rule of signs*,
J. Aust. Math. Soc.91 (2011),415–420,
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CB397B7DDF0A79680D67334501C2ADDB/S144678871100156Xa.pdf/div-class-title-a-generalisation-of-descartes-rule-of-signs-div.pdf),
DOI10.1017/S144678871100156X. Read Definition5, Theorem1,
Theorem7/Remark8 and both proofs, pp416–419. Theorem1 integrates a
Descartes kernel over ordered, disjoint positive measures. Theorem7
uses ordered sign regions of a signed measure; Remark8 identifies
the Laplace kernel. The proof uses Fubini and determinant sign
regularity. Do not import an unrestricted multiplicity-counting or
arbitrary-null-set formulation: use a continuous density and the next
source for the future application.

Anand Bhaskar and Yun S. Song, *Descartes' rule of signs and the
identifiability of population demographic models from genomic variation
data*, Ann. Statist.42(6) (2014),2469–2493,
DOI10.1214/14-AOS1264,
[arXiv:1309.5056v3](https://arxiv.org/pdf/1309.5056v3), 1 December2014.
Read Definition3 (reprint pp7–8), Theorem4 (p9), and its complete proof
(p14). The theorem concerns nonzero piecewise-continuous densities with
finitely many sign changes and counts real Laplace zeros with
multiplicity. Zero intervals are ignored. The proof treats the
constant-sign base case, removes a first crossing by multiplying by
t0-t after exponential conjugation, and uses Rolle's theorem.
The printed assumptions do not ensure convergence or differentiation
under an infinite integral. Restrict use here to a continuous density,
nonzero on an interval, with integral (1+E)^r exp(bE)|v(E)|dE finite
for every finite b>=0 and integer r>=0. Later work must verify this
domination explicitly; joint continuity alone is inadequate.

[NIST DLMF1.14.30–31](https://dlmf.nist.gov/1.14#E30), accessed
9 November2026, defines one-sided convolution and states its Laplace
product identity for piecewise-continuous functions; read the adjacent
hypotheses. This is method coverage only. Singular square-coordinate
factors require Tonelli/Fubini with absolute integrability; do not
silently apply the displayed continuity condition at their origin.
These are standard named integration theorems, not a new representation.

Primary extracted text was legible. Screenshot requests returned image
placeholders, not inspectable images; no screenshot-only passage is
used. Jameson [15], Lemma4.5, is an antecedent acknowledged by
Bhaskar–Song, not an independently read input. No essential access
blocker remains. No source theorem is reproved in this turn.

### Reuse, duplicates and failures

Reused `2026-11-09-low-time-h2-contact-exclusion-review.md`, including
the inspected Choi theorem: its lower-time Gram/Stieltjes argument
assumes the unavailable real-zero premise. Its a=0 low-order
calibration is not det H2. The known cutoff at lambda=1/20 does not
cover the interior. Koide's derivative-kernel lead remains optional
and unread, not a blocker to this test.

Read the contact-variation assessment and L915 ATTEMPTS record.
The audited spatial-residual one-crossing obstruction uses contact
cancellations; it does not count crossings of the proposed fixed
measure in total squared energy. Reused the shared-Taylor assessment
and L922 stop: its fixed constant-coefficient uncertainty is unpaid;
do not rename or enlarge that implementation. Read the concise L607,
L806, L916 and L937 failure records. Their generic Stein,
whole-support derivative, inverse-score and coefficient-box premises
differ from this proposed energy-density premise. Preserve each stop.

Notebook-local Tokarev/Bhaskar/Jameson/Descartes,
Laplace-plus-sign-change and signed-convolution searches found no
existing assessment of this H2 energy test. Other signed convolutions
concern different variables/operators. No sibling notebook was read.
This duplicate check does not establish originality.

External queries included `Laplace transform signed measure number
sign changes generalized Descartes rule theorem`, `Schoenberg variation
diminishing Laplace transform sign changes theorem 1930`, `Laplace
transform sign changes zeros theorem Descartes integral`, `Bhaskar Song
generalized Descartes rule signs Laplace transform Theorem 4 2014`,
`Jameson zeros Laplace transforms Descartes rule signs 2006`,
`Riemann Hankel Laplace cumulant determinant sign changes`,
`theta signed convolution determinant`, and `logarithmic Hankel
Descartes`; further exact convergence/actual-object queries supplied
no inspected stronger matching result. Schoenberg convolution articles
and a newly indexed Thorin/Levy/Mobius preprint are optional unread
leads, not positivity inputs. Reused Choi coverage instead of browsing
its unchanged theorem again.

### Discriminator and route decision

Nominate one fixed signed-energy obstruction test in
`drafts/literature/2026-11-09-actual-h2-energy-cell-test-46.md`.
M_0^12 is a proposed normalization to verify, not a result derived here.
A later attempt must use L917's exact finite algebra, construct the
fixed convolution density, and justify normalization, origin regularity
and exponential moments. An optional positive parameter factor is
excluded because it would change the measure being tested.

The finite discriminator is a certified alternating triple of masses
on 32 prescribed ordered energy cells. If established, it would retire
this normalization's at-most-one-crossing premise. Failure to find a
triple proves no upper crossing bound or endpoint sign. Stop after one
bounded attempt without refinement. A global crossing proof would
still require the entire half-line. This is a falsifiable obstruction
test, not an approved low-variation hypothesis.

Outcome EXPLORATION: primary method coverage and a testable continuation,
with no new actual mathematical input for the RH argument. The new
continuation requires separate approval next turn. No lemma, mathematical
script, DAG edge or PROOF argument changed; Mathlib coverage is unchecked.
