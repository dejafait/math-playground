# Collision strata and regular K3 maps: cited inputs

Primary statements read on 2026-10-03. These are known inputs
imported by citation during a literature-only turn.

## Hypotheses

For the stratum input let X be an irreducible nonsingular
quasi-projective surface over C, and write a partition of n
as 1^{a_1} ... n^{a_n}. Give its stratum closure in X^{(n)}
the reduced structure. Set X^{(a)}=product_i X^{(a_i)}, with
X^{(0)} a point.

For the scheme input let u:V -> W be finite and birational
between integral schemes, with W normal. For the geometric
input let S be a smooth projective complex K3 surface and
h:S -> S a dominant algebraic morphism. For the Hodge inputs
use the rational transcendental Hodge structure T(S); the
isometry restriction assumes its full endomorphism field is
totally real.

## Conclusion

The weighted addition morphism X^{(a)} -> X^{(n)}, sending
(z_i)_i to sum_i i z_i, is the normalization of the indicated
stratum closure. Its image includes further collisions.

The morphism u is an isomorphism. Normalizations of complex
algebraic varieties are finite.

The dominant regular self-morphism h is an automorphism.
This statement does not concern dominant rational maps.

The Hodge structure T(S) is irreducible. A Hodge endomorphism
of it vanishing on T(S)^{2,0} vanishes everywhere. When its
full endomorphism field is totally real, its rational Hodge
self-isometries are precisely +id and -id.

These separate source conclusions do not assert scalarity
for a map S -> M_H(2,0,-1), factor a prescribed support map,
or compute a universal-sheaf action.

## Proof

For the normalization import [de Cataldo--Migliorini,
*The Douady Space of a Complex Surface*, Advances in
Mathematics 151 (2000), Lemma 3.3.1 and proof, printed
p. 299, PDF p. 18](https://www.math.stonybrook.edu/~mde/MyPublishedPapers/DouadySpaceCplexSfceAdvances.pdf#page=18).
Its algebraic formulation is stated in [their *The Chow
Groups and the Motive of the Hilbert Scheme of Points on
a Surface*, Journal of Algebra 251 (2002), section 2,
printed p. 827, PDF p. 4](https://www.math.stonybrook.edu/~mde/MyPublishedPapers/MotiveHilbSchJournOfAlg.pdf#page=4).
No reproof or application to a parameter map is made here.

Import [Stacks, Lemma 29.55.8, Tag 0AB1](https://stacks.math.columbia.edu/tag/0AB1)
for u, and [Lemma 33.27.1, Tag 0BXR](https://stacks.math.columbia.edu/tag/0BXR)
for finite normalization; the tag identifies the statement
if section numbering changes.

For h import [Thomas Dedieu, *Severi varieties and self
rational maps of K3 surfaces*, arXiv:0704.3163v1, 24 April
2007, introduction 0.2, PDF pp. 1--2](https://arxiv.org/pdf/0704.3163v1#page=2).
This unnumbered statement and its argument apply to every
complex projective K3 surface. The adjacent conjecture for
rational maps uses additional genericity hypotheses; those
are not a substitute for the regular-morphism statement.

For the Hodge conclusions import [Huybrechts, *Lectures on
K3 Surfaces*, 449-page author draft, Chapter 3, Lemma 2.7,
PDF p. 48](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=48),
[Lemma 3.3, PDF p. 52](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=52),
and [section 3.5, PDF p. 59](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=59).
The last restriction already supports L004; it is reused,
rather than recorded as a new scalarity calculation.

## Mathlib

Coverage: **not checked** for these inputs or the full
boundary-action target. The direct references match their
respective source statements, rather than a Mathlib theorem
or a theorem covering the proposed universal-sheaf action.
