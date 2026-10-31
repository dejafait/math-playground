# Explicit local circle count: completed source review

2026-10-30. Literature only; no new inequality, lemma, zero count or
mathematical script is established. Assessment:
`drafts/literature/2026-10-30-explicit-local-circle-count-coverage.md`.

Main gap: actual-Xi all-degree positivity; the heat-flow route also
lacks finite positive-time collision exclusion. The exact intermediate
target is the checkpoint's one-real-simple-zero count at every real
phase center on 1/25<=t<=11/50 and X>=4*pi*exp(10000)+2, in the open
disk of radius 1/log(X/(4*pi)). A successful selected-disk count could
support a later numerical real/simple tail. Exhaustion, edge transfer,
finite collisions and control as t decreases to zero remain independent.

## Primary coverage and its limit

D. H. J. Polymath, *Effective approximation of heat flow evolution of
the Riemann xi function, and a new upper bound for the de Bruijn–Newman
constant*, Research in the Mathematical Sciences **6** (2019), article 31,
[arXiv:1904.12438v2, 4 August 2019](https://arxiv.org/html/1904.12438v2).
[Versioned PDF](https://arxiv.org/pdf/1904.12438v2): Theorem 1.5 pp.9–10;
Proposition 9.1 pp.56–58; Lemma 9.2 pp.58–59; counting cases pp.59–60.

Inspected source facts: (4) gives an entire conjugation-symmetric H_t.
(6)–(11) specify a nonzero holomorphic M_t on C minus (-infinity,1],
its fixed logarithm and B_t. Theorem 1.3, (5),(13)–(24), applies only
for 0<t<=1/2, 0<=y<=1, x>=200, with explicit additive normalized error.
Its floor-dependent f_t is not a global holomorphic comparison.
Theorem 1.5(ii), with (26), counts one zero near x_n where g(x_n,t)=n,
for n>=exp(C/t), on radius c/log x_n with unnamed absolute C,c.
The proof following (104) uses c/log n. Proposition 9.1(i) assumes
|y|<=10, x>=200 and x>=exp(C/t); its proof treats negative y by
conjugation of H_t and M_t. Lemma 9.2 and (102)–(104) provide the local
two-term phase comparison with unnamed errors. The subsequent case
of 1.5(i) separately localizes arbitrary high zeros using a strip
theorem and a nearest center. These statements do not specify the
requested numerical onset, radius or strict margin.

No source saddle proof is audited. The quantitative application should
use L490, rather than assign numerical values to the Section 9 errors.

## Existing inputs and exact application obligations

L490's hypotheses, conclusion and imported inequalities were read,
together with its independent application audit. Its additive residual
<153/10^6 holds on the CLOSED upper strip in the required time band
and x>=4*pi*exp(10000). It is relative to B_t, not to the cancelling
sum. It is neither a full-disk residual in a chosen normalization nor
a strict boundary comparison.

L491's hypotheses, conclusion, branch/conjugation argument and center
phase were read together with the completed independent audit. It
controls the specified log ratio on CLOSED unit disks, by
(L+20)/X<5010/10^12, L=log(X/(4*pi)), on the exact padded X range.
Its audit supplies the local component, not the count. L490 and L491
use opposite s_+ labels: the future application must write the affine
arguments explicitly and verify the ratio against source (16).

L488's strict-circle proof, including its common holomorphic factor,
was read. Its qualitative comparison already counts multiplicity and
uses conjugation for reality; it supplies no numerical onset. Its
smaller d/log X circles do not approve the radius requested here.
This is a quantitative specialization, not a new counting mechanism.

The following are future proof obligations, NOT results of this review:

1. Check disk containment and the padded spatial edge for every X and
   t, including endpoints; keep the exact source M_t normalization.
2. Choose a single nowhere-zero holomorphic factor on a neighborhood
   of the closed disk using the fixed source logarithms. Verify its
   relation to the local two-term model. A modulus factor alone cannot
   justify a holomorphic Rouche comparison.
3. Transfer the upper-half residual to the lower half by the source's
   conjugation symmetry and explicitly track the change in normalizing
   factor. Do not simply extend L490's upper-strip inequality unchanged.
4. At the stated radius, give a complete uniform boundary lower bound
   for a holomorphic model and compare it strictly with the TOTAL
   reflected residual plus gamma-model error in the SAME normalization.
   Use a standard named Rouche theorem counting multiplicity; verify
   its neighborhood and boundary hypotheses. Then justify the real,
   simple conclusion from multiplicity one and conjugation.

The fixed-branch source formulas and the existing audits cover the
techniques required for this attempt. No essential unread theorem was
identified for these obligations. They are not approved conclusions.
Source (76) remains excluded as recorded in L491. Source (104)'s coarse
error is not a strict numerical margin; retain a holomorphic factor
as in L488 or verify an equivalent normalization directly. Do not use
the stronger real-part coefficient printed in the asymptotic proof
in place of the literal residual inputs already audited in L490.

## Searches, duplicates and route decision

Reused `drafts/heat/2026-10-30-explicit-gamma-phase-source-review.md`
and its phase/count and explicit-cutoff searches; no unchanged audit
was repeated. Supplementary queries actually submitted were:
`"H_t" "Rouche" "Polymath"`;
`"heat flow" "xi" "explicit" "simple" "zeros" Polymath`;
`"1904.12438" "circle" "zeros"`;
and, restricted to arxiv.org, `"1904.12438" "real" "simple" "explicit"`
and `"H_t" "Rouché" "zeros"`. The restricted queries returned no hits.
Other results were unrelated or secondary portfolios, not theorem
inputs. No additional matching numerical theorem was inspected; failed
searches establish neither novelty nor absence. The earlier comparison
already records the source's comparison with Ki–Kim–Lee; no new
inspection of that paper or claim about all subsequent literature is made.

Read the precise stops in
`ATTEMPTS/2026-10-30-direct-numerical-tail-extraction.md` and
`ATTEMPTS/2026-10-30-tail-approval-loop-recovery.md`. They stop direct
extraction of unnamed constants and repeated unchanged approval, not
the present quantitative use of newly audited components. No source
blocker persists. No numerical margin is calculated here.

Decision: SPECIALIZE for the unchanged exact target. Continue with one
bounded proof attempt using L490 and L491. Accept only a strict uniform
full-disk boundary margin and count with multiplicity; otherwise retain
the exact failed comparison and distinguish failure of an estimate
from failure of the claimed zero count. No global strip input is
necessary for this selected-disk task; exhaustion must be separately
assessed before claiming a tail. Full matching Mathlib coverage is
unchecked. No new theta-specific mechanism for the central collision
gap is justified by this source review, so this established-route
specialization is not classified creative. The main argument is unchanged.
