# Target, source, and conventions

## Primary statement audit — 2026-09-24

The mathematical target is: for positive integers A,B,C,x,y,z with x,y,z > 2 and A^x + B^y = C^z, prove gcd(A,B,C) > 1, or exhibit and rigorously check a counterexample with gcd(A,B,C) = 1. The bases may equal one in the statement. No upper bound on any variable is imposed.

The [primary page maintained by Daniel Mauldin at UNT](https://sites.math.unt.edu/~mauldin/beal.html), fetched on the audit date, states precisely this assertion using the equivalent conclusion that the three bases share a prime divisor. The [sponsor's problem page](https://www.bealconjecture.com/) agrees, but the fetched content contains a 2016 archive banner, so it is corroboration rather than evidence of a recent update.

The [AMS page named in GOAL.md](https://www.ams.org/profession/prizes-awards/ams-supported/beal-prize) and its rules endpoint returned HTTP 403. Search-indexed [AMS Council minutes, January 2014, Attachment W, printed page 82](https://www.ams.org/about-us/governance/council-meetings/council-minutes0114.pdf) reproduce the same mathematical formulation; direct PDF retrieval failed. This is an explicitly historical cross-check, not a claim that the current AMS page was read. The accessible primary formulation matches the local target; prize administration is not a mathematical hypothesis.

Rechecked on 2026-09-25: Mauldin's accessible primary page still gives the same positive-integer formulation. The nominated AMS page again failed retrieval; no claim about a change in its contents is made.

## Primitivity and local terminology

A positive integer solution is **primitive** when gcd(A,B,C) = 1. For this coefficient-one equation, this is equivalent to pairwise coprimality: a prime dividing any two bases divides their corresponding powers and hence the remaining power by the equation, so it divides the third base. Thus a shared divisor of any pair in an actual solution contradicts primitivity. This equivalence would not hold for arbitrary triples without the equation.

A signature is the ordered exponent triple (x,y,z). Interchanging the two summands is harmless; moving the right-hand term to a summand needs a separate sign justification. The global signature reduction uses signed auxiliary bases only when the exponent being moved is odd; the target itself always retains positive bases.

For a prime p, v_p(n) denotes the exponent of p in a nonzero integer n. The ring Z_p is the completion of the integers for this valuation, or equivalently their compatible residues modulo p^n. A unit has valuation zero. A triple in Z_p is **pairwise locally coprime** if each pair contains a unit. This is a local condition and does not produce three ordinary integers satisfying the equation.

No base-one cases have been discarded. The local constructions happen to avoid one, but that is not a global exclusion of the base-one cases.
