# Actual b_m lower-envelope feasibility — source comparison, step208

TARGET: Assess whether Pringsheim's theorem and actual-xi logarithmic zero singularities obstruct L975's every-delta one-sided b_m lower envelope, without assuming RH.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step208 reused the signed-bump Pringsheim assessment and step205 inverse/source-failure comparison; searched Pringsheim with actual-xi/Coffey coefficients, exact arXiv0912.2390 with error/correction, and eventual coefficient signs. No inspected source states the exact actual-b_m compatibility result; no novelty inference. Primary boundary-theorem statement and full two-case proof were read, with the precise source passages below.
SOURCE_EVIDENCE: Flajolet-Sedgewick, Complex Asymptotics, zeroth edition 8May2004, TheoremIV.3(i)-(ii) and complete proof, printed pp15-16/PDF23-24; DLMF1.10(i) Taylor/zero order, 1.10(ii) continuation, 1.9.53-57 local reciprocal/logarithm, and 25.10(i) zero existence/symmetry; Coffey arXiv0912.2390v1 (1.3), Proposition6/Corollary7, source statements only; local L013/L018/L021/L024/L026/L968/L975 as qualified below. Online sources accessed 2026-11-10.
COMPARISON: Pringsheim supplies a positive-real singularity only for a nonnegative-coefficient germ of finite positive radius; it does not apply directly to signed b_m. The inspected analytic and xi inputs suffice to pose a positive-correction/radius test, but neither that specialization nor an obstruction is proved in this literature turn. Coffey's advertised asymptotic remains unimported and unaudited.
GAP: Verify the candidate corrected series' coefficient signs and exact finite radius, the effect of mapped xi zeros with arbitrary multiplicities, and continuation of the same logarithm germ across its positive-radius point. Those are mathematical obligations, not missing essential sources for this bounded test.
REASON: Complete the startup REVIEW_REQUIRED comparison before any envelope-payment attempt; known generic tools cover the proposed test while their actual-xi specialization still needs a separate mathematical step. The step207 nomination is superseded as coverage, with its original unresolved obligations retained below.
SCOPE: Source comparison for L975's actual b_m, every delta in (0,1), and eventual-prefix version. No RH, radius-two logarithm, simple zeros, cancellation, coefficient positivity or asymptotic is approved as a premise. The separate next assessment nominates one bounded application, subject to separate approval before invocation.
LITERATURE_REASON: Essential unread Pringsheim hypotheses and actual-xi singularity/continuation comparison were explicitly required by the saved continuation; this does not repeat the already ready interior-inverse audit or reopen the parked 2007 source retrieval.

## Named gap and discriminating test

The main gap remains actual-Xi all-degree positivity and the unpaid
all-index Li lower bound. L975 has supplied only a sufficient transfer.
The intermediate target now concerns feasibility of that hypothesis,
so it can prevent work on an impossible or unnecessarily strong
coefficient payment. It is distinct from the completed interior audit.

The source task was to check the theorem after a proposed coefficient
correction, rather than infer compatibility from L975's sufficiency.
The continuation test is now precise: test a corrected germ against
Pringsheim only after proving its finite radius is strictly smaller
than the correction's radius and verifying continuation at the former
positive-real point. If these hypotheses cannot be established, report
the failed hypothesis, not an obstruction. A successful obstruction
would stop this particular payment hypothesis, not L975's inverse or RH.

No new lemma, mathematical script, coefficient estimate, radius bound
or incompatibility is established here. The result is source coverage
and a testable continuation, recorded as literature EXPLORATION rather
than mathematical progress beyond the sources.

## Inspected theorem and essential proof cases

P. Flajolet and R. Sedgewick, *Analytic Combinatorics — Complex
Asymptotics*, zeroth edition, 8 May 2004,
[Theorem IV.3 and proof, printed pp.15-16](https://algo.inria.fr/flajolet/Publications/ch4567.pdf#page=23)
(PDF pp.23-24), is the precise boundary input. An analytic germ with
finite Taylor radius R has a boundary singularity. If its Taylor
coefficients are nonnegative, R itself is singular. The first proof
case uses a larger analytic disk and Cauchy's estimate to contradict
the radius. The second assumes regularity at R, recenters just to its
left and rearranges nonnegative terms to force convergence beyond R.
Thus nonnegativity is load-bearing, and neither assertion locates the
radius of an arbitrary signed germ. We import the named theorem, not
a reproof. This is the 2004 numbering, not 2009 Theorem IV.6.

The same draft's printed p.24 explicitly labels its general
singularity-composition rules as heuristic, without detailed validity
conditions. Those rules are not imported as a logarithmic-singularity
theorem. The next application must justify the actual composition and
its logarithm directly from the local analytic tools.

[NIST DLMF 1.10(i)](https://dlmf.nist.gov/1.10.i) states Taylor's
theorem and defines zero multiplicity by the first nonzero Taylor
coefficient. [1.10(ii)](https://dlmf.nist.gov/1.10.ii) states equality
and continuation of analytic elements on overlapping domains.
[1.9(vi), (1.9.53)-(1.9.57)](https://dlmf.nist.gov/1.9.vi) gives local
reciprocal and logarithm expansions for a nonzero constant term, with
the logarithm normalized to constant term 1. These are local tools;
they do not assert a disk-wide logarithm in the presence of zeros.
The local multiplicity/composition and branch application is reserved
for research. No global principal branch is silently imported.

## Xi inputs, stronger claims and applicability

[NIST DLMF 25.10(i), Distribution](https://dlmf.nist.gov/25.10.i)
records infinitely many zeros in 0<Re(s)<1, their reflection symmetries,
and infinitely many critical-line zeros. Only unconditional existence
is needed; neither a first-zero computation nor RH is needed. This is
an inspected authoritative handbook statement, not a claim to have
read Hardy's original proof. A Rutgers-hosted Titchmarsh PDF timed out;
that optional lead is not imported and is not an essential blocker.

Local L018 supplies the entire completion, symmetries and exact
nontrivial-zero correspondence. L026 supplies low-height exclusion,
not existence. L013 supplies the real-strip nonvanishing input that
L026 alone does not supply at arbitrary real arguments. L021's
imaginary-axis positivity and L024's paired product are also available
if an entirely local zero-existence check is preferred. Their relevant
proofs were read to identify the inputs, without relabeling them as a
new result or carrying out that check in this source turn.

L975 fixes the actual germ and all coefficient quantifiers, already
on a justified radius-3/2 disk. It does not fix its maximal radius.
The prospective substitution is w=z+1 and s=1/(2-w). The next test
must examine images of actual zeros, not replace them by ordinates.
It must retain multiplicity, establish nonremovability and match the
continued logarithm with the Taylor germ. Positive-real nonvanishing
and a local analytic branch have different roles from disk-wide
nonvanishing; neither may be substituted for the other.

[M. W. Coffey, arXiv:0912.2390v1](https://arxiv.org/pdf/0912.2390v1#page=2),
(1.3), printed pp.2-3, agrees with L975's coefficient definition.
Proposition 6 and Corollary 7, printed p.7, explicitly assume RH.
Their asymptotic is not an unconditional payment, and this review
does not certify even its conditional derivation. Reuse step205's
recorded forward-exchange/domain concerns; no contradiction with that
asymptotic or correction to the paper is asserted here. The proposed
test would require a separate proof before such a comparison.

## Search record, duplicates and approval boundary

Queries included `Flajolet Sedgewick Analytic Combinatorics Theorem
IV.6 Pringsheim pdf`, `Pringsheim xi coefficients Coffey`,
`Coffey b_n Pringsheim`, `0912.2390 error coefficients asymptotic`,
`Coffey On certain sums correction`, and `Pringsheim eventually
coefficients theorem`. Hardy-original queries produced reference
leads, not an inspected original article; no such source is imported.
No exact stronger applicable coefficient theorem was inspected.
Search failure is not evidence of novelty or of mathematical absence.

Scoped searches covered the bn assessments, November10 attempt
records and bn histories, plus specific Pringsheim references in local
literature/attempt/foundation files. The signed-bump generating-function
assessment already has the generic boundary theorem, but lacks the
present actual-xi germ and envelope. Step205's direct-import stop and
step207's inverse are distinct; neither proves the proposed obstruction.
No sibling notebook was read. No new zero-free region is proposed.

## Reuse and boundary of approval

The next target is nominated in
`2026-11-10-bn-envelope-pringsheim-test-review-208.md`. Its mathematical
claim is unproved, and its newly prepared coverage receives separate
approval before invocation. The unchanged inverse assessment remains
reusable for its own scope. All prior stops and the 2007 source blocker
remain recorded. No PROOF or DAG update is warranted by a source review.

No justified creative actual-coefficient payment mechanism is presently
identified. Testing the admissibility of the existing hypothesis is
a standard theorem application, not a creative central mechanism.
Full Mathlib coverage remains unchecked/unknown; no Mathlib result is
imported. The main RH and signed-forcing gaps remain unpaid.
