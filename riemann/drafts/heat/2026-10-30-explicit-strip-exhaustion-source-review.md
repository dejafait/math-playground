# Explicit strip exhaustion: source comparison

2026-10-30. Literature only. The exact target and its approval are in
`drafts/literature/2026-10-30-explicit-strip-exhaustion-coverage.md`.
No numerical inversion, new estimate or exhaustion theorem is proved here.

## Gap, relevance and bounded test

The main gap is actual-Xi all-degree positivity; the heat-flow route also
lacks finite positive-time collision exclusion. The intermediate target
is to place every zero H_t(x+iy) in the checkpoint's closed time band
1/25<=t<=11/50 and assumed strip |y|<=1, with
x>=4*pi*exp(10000)+3, strictly inside an L492 disk whose center satisfies
X>=4*pi*exp(10000)+2. Use exactly L492's g(X,t) and radius
1/log(X/(4*pi)). The target and its proposed extra unit of padding have
not changed.

If established, this would let L492 supply reality and simplicity for
every such strip zero, rather than only count selected disks. Global
strip/normalization transfer, the finite interior, smaller positive
times and zero time remain separate. Continue only with a uniform proof
of the strict disk inclusion and center onset at every endpoint; a
failed edge inequality stops this numerical target without refuting the
qualitative theorem. Finite samples and unnamed asymptotic constants
cannot pass the test.

## Primary result and essential cases actually read

D. H. J. Polymath, *Effective approximation of heat flow evolution of
the Riemann xi function, and a new upper bound for the de Bruijn–Newman
constant*, Research in the Mathematical Sciences **6** (2019), article 31,
[arXiv:1904.12438v2, 4 August 2019](https://arxiv.org/html/1904.12438v2)
([versioned PDF](https://arxiv.org/pdf/1904.12438v2)).

Theorem 1.5, pp.9–10, assumes 0<t<=1/2. Part (i) localizes all zeros
beyond exp(C/t) to real centers defined by (26); part (ii) counts a
zero in each sufficiently high center disk. Its C, c and implied
constants are absolute but unnamed. The theorem therefore supplies no
numerical onset for this target. Its discussion compares Ki–Kim–Lee
Theorems 1.3–1.4, whose stated conclusions are weaker in uniformity
and effectiveness; their original proof was not inspected here.

Read Proposition 9.1(i), pp.56–58, its conjugation case, Lemma 9.2
with (100)–(101), pp.58–59, the counting case (102)–(104), pp.59–60,
and the entire subsequent proof of (i) on p.60. Exhaustion first uses
the strip theorem, chooses a nearest phase center, compares summand
moduli at the zero, and then uses phase localization and nearest-center
restriction. This is a separate argument from the count. The global
strip input is unnecessary as a theorem input for our explicitly
strip-restricted target. The saddle estimates remain imported.

## Local coverage and the precise remaining specialization

Read L490's hypotheses, conclusion and exact imported inequalities;
L491's hypotheses, conclusion, fixed-branch proof and full unit-disk
range; L492's statement and normalization/reflection/count proof; and
L488's qualitative exhaustion proof. Their completed application audits
are reused. These inputs establish the following coverage, not the target:

- L490 gives an additive residual <153/10^6 relative to the source B_t
  for 0<=y<=1 and x>=4*pi*exp(10000), throughout the closed time band.
  It is not relative to the cancelling two-term sum. The reflected
  lower half requires the conjugation and denominator treatment already
  recorded in L492, or a justified reduction of a zero to the upper half.
- L491 controls its specified holomorphic log ratio on closed unit
  disks about arbitrary real X>=4*pi*exp(10000)+2. The center is not
  required to be a phase integer. Its error is at most (L+20)/X and
  strictly below 5010/10^12. The affine arguments must be written out:
  L490 and L491 use opposite s_+ labels.
- L492 counts multiplicity and excludes boundary zeros in disks about
  integer-phase centers. Its reality conclusion does not assume
  exhaustion. Its center onset and radius must be met before using it.
- L488 supplies an existing qualitative nearest-center exhaustion
  replay, including a phase restriction to select the correct sine
  zero. Its unspecified constants cannot certify the new edge.

The required numerical specialization is fully within the techniques
of these inputs and the inspected source case. The following are proof
obligations for a later RESEARCH turn, not assertions established now:

1. At an arbitrary zero, keep one valid B_t normalization and bound
   the corresponding gamma ratio near cancellation. Justify any
   logarithm and its branch; the fixed holomorphic log in L491 must
   not be replaced silently by a principal log of its exponential.
2. Control both imaginary displacement and phase modulo the correct
   integer. Small imaginary displacement alone does not locate a disk;
   small phase discrepancy alone does not control |z-X|. A nearest-center
   implementation must retain the quantitative phase restriction from
   L488. An inversion implementation must justify its integer choice.
3. Prove existence of a center with the required lower bound using
   the exact g and ordinary intermediate/mean value theorems. Quantify
   edge control, not just g's monotonicity, and compare logarithms at
   the arbitrary zero's real coordinate and the selected center.
4. Verify strict Euclidean inclusion in the requested disk for the
   entire unbounded range, both time endpoints, y=0 and |y|=1, and
   the spatial edge. Check all local-estimate domains before their use.

There is a domain hazard worth preserving for that attempt: nearest
center control of the real displacement and the initial hypothesis
|y|<=1 do not by themselves put the zero in L491's closed unit disk
about that center. The application must address this before invoking
the disk estimate there. L491 also permits a real center not satisfying
g(X,t) in Z; this available scope may be useful before choosing the
eventual L492 center. No quantitative consequence of it is derived here.

Source (76) remains excluded by L491's recorded countercheck. Neither
the coarse (104) error nor the strengthened real-part coefficient in
the asymptotic proof replaces the audited numerical inputs. No enlarged
|y|<=10 constants, new contour count, new strip theorem or zero-free
region is needed or approved. Full matching Mathlib coverage remains
unchecked; elementary logarithm/calculus support is not a matching
formalization of exhaustion.

## Search, duplicate/failure comparison and decision

Reuse the inspected searches in
`drafts/heat/2026-10-30-explicit-local-circle-source-review.md` and
`drafts/heat/2026-10-30-explicit-gamma-phase-source-review.md`, plus
the explicit-tail assessment. New queries actually submitted:

- `"H_t" "zeros" "explicit" "exhaustion"`
- `"1904.12438" "localization" zeros`
- `"heat flow" "xi" "zeros" "effective" "real" "simple"`
- `"1904.12438" "exhaustion"`
- `"H_t" "x_n" "zeroes" "Polymath"`
- `"heat flow" "Riemann" "explicit" "localisation" zeros`, restricted
  to arxiv.org.

Results included unrelated material, a secondary repository scoreboard,
a ResearchGate listing and early Polymath discussion threads. None was
used as a theorem input or a substitute for the primary proof. No
additional matching numerical theorem was inspected. These searches
establish neither novelty nor absence. No new essential unread lead
was identified. The previously compared Ki–Kim–Lee results are not
needed to supply a stronger effective statement for this specialization.

Scoped local checks found the qualitative exhaustion in L488 and the
existing nominations, not a duplicate numerical exhaustion result.
The stops in `ATTEMPTS/2026-10-30-direct-numerical-tail-extraction.md`
and `ATTEMPTS/2026-10-30-tail-approval-loop-recovery.md` concern extraction
of unnamed constants and repeated unchanged approval. This comparison
addresses a distinct, previously uncovered target using now-audited
numerical inputs. It does not reopen direct constant extraction or
repeat L492's completed audit.

Decision: SPECIALIZE. Essential source coverage is ready for one bounded
proof attempt on the unchanged exact target. No numerical conclusion
has been accepted. This is established-route development, classified as
reproduction/specialization, with no progress beyond the source's
qualitative localization claimed. No new theta-specific input overcoming
the generic collision obstruction emerged; it would be unjustified to
label this continuation creative merely to meet a scheduling preference.
