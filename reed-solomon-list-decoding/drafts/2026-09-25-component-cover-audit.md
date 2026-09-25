# Component-cover audit — 2026-09-25

## Gap, target, and discriminating test

The missing quantitative input is a list bound that improves L001's
exponential dependence on n. This step audits the geometric route in
[TR26-169](https://eccc.weizmann.ac.il/report/2026/169/download), September 5,
2026, rather than reusing the rejected q-polynomial transfer. The prize
website was rechecked on September 25; its base-field threshold and existence
proviso agree with the frozen model, whose ABF comparison remains qualified.
Existing local changes and prior evidence were inspected and preserved.

The intermediate target is a justified passage from a cover of candidate
coefficient vectors, of dimension at most s and total cumulative degree
Delta, to at most Delta times sum_{a=0}^s n^a singleton-list candidates.
The proposed downstream use is a polynomial bound at fixed s whenever Delta
is polynomial in n. Cover construction, its characteristic restrictions,
concrete exponents, and the sharp finite-code boundary remain separate issues.

The discriminating test is whether the full agreement equations cut out a
singleton over the algebraic closure, and whether following only proper cuts
permits a uniform count of all resulting points. A surviving positive-
dimensional branch or a missing multiplicity/degree budget would reject this
passage. A proof would isolate the remaining obligation in the cover itself.
This is a review of an existing source argument, with no novelty claim.

## Result

The working target and partial reasoning were saved before completing the
review. The result is now proved in
[L002](../lemmas/L002-agreement-isolation-in-a-geometric-cover.md), using the
standard [proper-section input](../foundations/03-proper-hyperplane-sections.md).
Both parts of the discriminating test pass. Full support isolates the
coefficient vector over the algebraic closure. For each ordered tuple of
hyperplanes, total degree cannot increase along proper sections; summing
over the possible tuples counts every candidate, even when its support and
the length of its chosen path differ from those of other candidates.

This checks the scalar counting passage already stated in Lemma 6.2 and
Theorem 6.3 of the source. It is a documented import with an expanded
informal proof, not a new theorem or a verification of the entire preprint.
The jet-cover construction underlying its Corollary 6.1 remains unverified
in this notebook. The count needs both dimension and cumulative degree:
an arbitrary number of isolated points still has dimension zero. Passing
the support test cannot substitute for proving the required degree bound.

## Actual threshold and limitations

Write beta=Delta sum_{a=0}^s n^a. Uniform scalar covers give
B_m((n-A)/n)<=floor(beta)^m and hence a safe radius whenever
q>=epsilon^{-1} beta^m. If Delta<=C n^c, this sufficient field condition is
q>=epsilon^{-1}[C(s+1)]^m n^{m(c+s)}. Its polynomial dependence would improve
L001's capacity-grid binomial condition at fixed positive slack, but only
after establishing fixed s and polynomial Delta for the candidate sets.
The two certificates concern different radii; this is not a proof of a
polynomial bound at A=k or of safety from epsilon q>=1 alone.

There is no new unconditional numerical radius bound in this step. The
construction and scope of the cover, its concrete exponents, and the sharp
boundary for the given field remain unresolved, as does the ABF comparison.
No complete proof or disproof candidate for the grand challenge appeared.

## Review checks and assessment

The symbolic review checked algebraic-closure uniqueness, existence of a
proper cut on every positive-dimensional branch through a candidate,
degree accounting on reducible covers, zero-dimensional initial components,
overlapping covers, and stopping at different depths. Hyperplanes containing
a branch are not counted as dimension drops. Intersection multiplicities
and components at infinity cannot increase the reduced affine point count.
Interleaving uses an injection into row lists, so the target remains epsilon
times q, not epsilon times q^m. No numerical experiment is needed to test
these symbolic implications, and no computational verification of the
geometric cover is claimed.

The result is ADVANCE as a checked conditional mathematical input that
removes the support-isolation/counting passage from the remaining source
review. The exploration streak is zero. The bounded test is complete and
the geometric route is retained: the unresolved degree bound, rather than
support uniqueness or the rejected q-polynomial transfer, is the relevant
place for subsequent scrutiny. L002 has no local lemma input; it proves
its interpolation uniqueness directly and uses standard projective Bezout.
