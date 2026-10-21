# Independent thinning — primary source input

## Hypotheses

Let a random subset of a finite set have indicator vector Z. Given that
subset, mark its members independently with Bernoulli retention
probability p in [0,1]. Let Z' indicate the retained subset.

## Conclusion

The source's independent-marking definition specializes to
E[Z'_a]=p E[Z_a] and, for distinct a,b,
E[Z'_a Z'_b]=p^2 E[Z_a Z_b]. The diagonal is E[Z'_a], by Booleanity.
This describes thinning an existing distribution; it is no existence
theorem for a distribution with prescribed moments.

## Proof

Import Günter Last and Mathew Penrose, *Lectures on the Poisson Process*,
Cambridge University Press, DOI 10.1017/9781316104477,
[author-hosted version of 21 August 2017](https://stoch.math.kit.edu/img/Last/lastpenrose2017.pdf):
Definition 5.3 and probability-space extension (5.6), pp. 40–41;
Proposition 5.4 with complete product-integral proof, p. 41;
Definition 5.7, p. 43. A finite random subset is a proper simple point
process on a finite discrete space. Conditional independent Bernoulli
marks give the displayed one- and two-mark factors directly. No
Poisson hypothesis or Theorem 5.8 is used. No reproof is required.

## Mathlib

Full matching independent-thinning theorem and supporting finite
probability/indicator coverage: not checked. Unknown availability is
not evidence of absence.
