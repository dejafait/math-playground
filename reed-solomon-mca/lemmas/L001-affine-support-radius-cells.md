# L001 — Affine-support error has right-open radius cells

## Hypotheses

Let \(F\) be a finite field, \(I\) a finite set of size \(n>0\), and
\(C\le F^I\). Let \(E_C\) be the exact support-event error defined in
[the pinned affine-line model](../foundations/02-pinned-affine-line-model.md).
Let \(\varepsilon\in[0,1]\).

## Conclusion

The function \(E_C\) is nondecreasing on \([0,1]\) and is constant when
\(\lfloor n\delta\rfloor\) is constant. If
\[
 E_C(0)\le\varepsilon<E_C(1),
\]
there is a least integer \(j\in\{1,\ldots,n\}\) with
\(E_C(j/n)>\varepsilon\), and
\[
 \{\delta\in[0,1]:E_C(\delta)\le\varepsilon\}=[0,j/n).
\]
Consequently the safe real radii have no largest element. Their supremum is
\(j/n\), which is unsafe; the largest safe grid radius is \((j-1)/n\).
This statement concerns \(E_C\). Its application to ABF26's exact target
requires the unresolved source correspondence in the foundation.

## Proof

For a fixed pair \((a,b)\), challenge \(\gamma\), and support \(S\),
the only part of the bad-event definition involving \(\delta\) is
\(|S|\ge n(1-\delta)\). Since \(n-|S|\) is an integer, this is equivalent
to
\[
 n-|S|\le\lfloor n\delta\rfloor.
\]
All other membership conditions are unchanged. Thus two radii with equal
floors have identical bad-challenge sets for every pair and hence equal
maximized errors. Increasing the radius only adds possible supports, so it
cannot decrease the error. This proves the first assertions, including at the
two endpoints of \([0,1]\).

The set of unsafe grid indices is a nonempty subset of \(\{0,\ldots,n\}\)
because \(n\) is unsafe. Its least element \(j\) is positive because zero
is safe. For \(0\le\delta<j/n\), put \(r=\lfloor n\delta\rfloor\).
Then \(0\le r\le j-1\), so minimality of \(j\) and the equal-floor
property give
\(E_C(\delta)=E_C(r/n)\le\varepsilon\).
For \(j/n\le\delta\le1\), monotonicity gives
\(E_C(\delta)\ge E_C(j/n)>\varepsilon\). This proves the exact safe set.

For every safe \(\delta\), the midpoint \((\delta+j/n)/2\) is another
safe radius strictly larger than \(\delta\). Thus no safe radius is largest.
The stated supremum and largest safe grid point follow from the same interval
description. No conclusion is asserted here when all radii are safe or when
the safe set is empty.

## Mathlib

Full statement in core Mathlib: **not checked**. Supporting results are
**present in the pinned ArkLib sources checked**, which are a separate library:

- [`CoreDefinitions.mcaError_mono` and
  `CoreDefinitions.mcaError_eq_of_floor_eq`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/ProximityGenerators.lean#L179)
  match the monotonicity and equal-floor components, for general generators.
- [`ProximityGap.GrandChallenges.GrandMcaResolution.sublevel_iff`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/GrandChallenges.lean#L224)
  matches the conditional sublevel assertion after an adjacent-grid resolution
  is supplied. It does not supply a crossing for an arbitrary code or identify
  that grid formulation with the literal real-maximum challenge.

The proof above is independent of a Lean build. The source declarations were
read, but their transitive axiom closures were not checked in this notebook.
