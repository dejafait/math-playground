# Finite-family cycles and the ideal of norms

Primary statements read on 2026-10-03. These are known
inputs imported by citation in a literature-only turn.

## Hypotheses

For the determinant statement let A be a commutative ring,
B an A-algebra, and M a B-module finite locally free over
A of constant rank d. For the cycle statements let X be
a separated algebraic space over a base, with characteristic
zero retained when identifying divided powers with symmetric
products. For the norm-ideal statement let F be an A-algebra
and n a positive integer; retain n! invertible in A when
using the symmetric-tensor identification.

## Conclusion

The action of B on M followed by determinant defines a
homogeneous multiplicative polynomial law B -> A of degree d.
Rydh supplies its associated canonical family, addition of
families, and the characteristic-zero identification with
the symmetric product.

Ekedahl--Skjelnes define the ideal of norms using all
generators delta(x,y). Under their canonical homomorphism
alpha_n into symmetric tensors,

\[
\alpha_n(\delta(x,y))=\nu(x)\nu(y),
\qquad \nu(x)=\det((x_i)_{[j]}).
\]

Here x,y are n-tuples in F and (x_i)_[j] denotes x_i in
tensor factor j. Their section 7.24 gives the global ideal
sheaf. These are the source's formulas and definitions;
no pullback for a particular map is evaluated.

## Proof

Import [David Rydh, *Families of zero cycles and divided
powers: II. The universal family*, author version dated
11 April 2008, section 3 through Definition 3.1, p. 6](https://davidrydh.se/papers/famzerocyclesII-20080411.pdf#page=6),
with [Theorem 2.3, p. 5](https://davidrydh.se/papers/famzerocyclesII-20080411.pdf#page=5).
Only its locally free case is needed here; its additional
normal-base construction is not required as a new premise.

Import [Rydh, *Families of zero cycles and divided powers:
I. Representability*, arXiv:0803.0618v1, 4 March 2008,
Definition-Proposition 4.1.1, p. 39](https://arxiv.org/pdf/0803.0618v1#page=39),
and [Corollary 4.2.5, pp. 42--43](https://arxiv.org/pdf/0803.0618v1#page=42).

Import [Torsten Ekedahl and Roy Skjelnes, *Recovering the
good component of the Hilbert scheme*, Annals of Mathematics
179 (2014), 805--841, Definition 2.7, p. 811](https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n3-p01-p.pdf#page=7),
[sections 3.1--3.3 and Proposition 3.4, pp. 813--814](https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n3-p01-p.pdf#page=9),
and [section 7.24, p. 834](https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n3-p01-p.pdf#page=30).

Use these statements by citation without reproof. They are
supporting inputs for the dihedral-plus-diagonal review;
they do not assert its regularity, the invertibility of its
image ideal, a stable lift, or a transverse deformation.

## Mathlib

Coverage: **not checked** for these full statements or for
the proposed degree-three map. The direct references match
the stated framework parts; no Mathlib match, absence or
new mathematical result is claimed.
