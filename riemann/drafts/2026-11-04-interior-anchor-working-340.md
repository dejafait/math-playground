# Interior-anchor quantitative attempt, step 340

Completed attempt; the preserved working notes below are superseded
by the full canonical write-up in L755. The prior EXPLORE assessment is
`literature/2026-11-04-adaptive-interior-anchor-minimum-modulus.md`.
Its exact target and fixed rational w are unchanged. No cutoff saving
has been established. Existing notebook changes are preserved.

The main gap is the missing initial Xi signs and all-degree mixed
positivity. The intermediate test is L266's complete circle/selected
anchor ratio for 0<b<=w-delta; a success would shorten the initial
sign workload only, leaving signs and the outer layer unresolved.

Read L018/L266, L461's full analytic-logarithm and complex-circle
argument, L468's hypotheses/conclusion, L462's fixed-parameter proof,
its preserved stop, and the October baseline/register. Reuse the
inspected Cartan sources and Stirling/logarithm mechanisms. L462 does
not settle this changed-domain selection. The external fixed-strip
manuscripts/formal import closures remain unaudited.

Original bounded calculation plan: normalize at a separately nonzero
exterior point, place a closed interval inside (b,w-delta/2), pay a
Cartan exceptional-disk budget smaller than that interval, and retain
the full complex-circle maximum in L266. Quantify the coefficient of
log T in the resulting ratio before claiming any saving. All fixed
geometry/constants must precede variation of a and b. No division by
Xi(a), central derivative, or zero simplicity assumption is allowed.

Continue only with a certified coefficient <=w/2-delta/8 and finite
uniform B_delta, or a precisely stated independently testable missing
input for separate review. A bound with an uncontrolled/wrong leading
coefficient parks this implementation; it is not an Xi counterexample.

Partial calculation saved before the full write-up:

- Put eta=w+delta/8, D=7delta and
  I=[w-7delta/8,w-5delta/8]. Then I lies strictly above every
  b<=w-delta and inside the permitted anchor interval, and
  |s-eta|<=delta<D/6. Scaling Goldstein--Schlag Lemma 2.4 requires
  h>=max(h0,log56); projected exceptional length is <2D exp(-h)
  <=delta/4=|I|. No height is discarded.
- Normalize phi_a(z)=exp(-Dz log T) H_a(eta+Dz)/H_a(eta), using
  the exterior nonzero H_a(eta), never H_a(0). The whole-strip
  growth envelope to prove carefully is
  log|H_a(u+iv)|<=[7/2+max(w,|u|)+epsilon]log T-pi|a|/2+O(1)
  for bounded u,v. Its normalized disk cost is
  E=max(55delta/8,55delta/4-2w).
- The source gives the paid exponent Q=(C h-1)E. Independently,
  any universal constant C in the source's precise unit-disk,
  radius-1/6 conclusion satisfies C>=1/log7: apply it to 1+r z,
  r>6, and use an interval of length 2exp(-h) about -1/r to
  find a point outside the exceptional disks, then let h grow and
  r decrease to 6. Thus C h>2 and Q>E>=55delta/8. This is a
  bound on a generic theorem's universal constant, not Xi's deficit.
- For the target c*=w/2-delta/8, any circle s<R<1/2 allows at
  most F=(w-delta/4)log(R/s)-max(w,R)+s additional anchor loss.
  For fixed s, F is maximized at R=w. On I this is at most
  49delta/8, using log(1+x)<=x and s>=w/8. Therefore this
  explicitly paid certificate misses the target by >3delta/4 in
  the numerator. This does not lower-bound the actual M/H_a(s).

The previous source's statement and one-variable proof were reopened
only to replay the already assessed CH-1 factor, radius and disk budget;
no additional source search or changed literature scope.

Completed mathematical reasoning has been moved to canonical L755,
including the changed-width logarithm/strip proof, constant calibration
and uniform coefficient comparison. It is unaudited. The outcome is
NEGATIVE for this sufficient certificate; no sharp optimal-Cartan
obstruction or actual-ratio lower bound is claimed. The implementation
is parked. The separate audit gate is REVIEW_REQUIRED. The compact
current state and sole continuation are in PROGRESS.md.
