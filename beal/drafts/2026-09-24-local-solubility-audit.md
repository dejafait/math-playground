# Initial source and local-solubility audit — 2026-09-24

This is the working record of one bounded route test, not a candidate proof of Beal.

## Starting state and relevance

The notebook initially had no lemmas, previous attempts, or local uncommitted changes. The shared overview and empty DAG were read before choosing the test. Changes in other notebooks and shared infrastructure are outside this step and are preserved.

The exact gap is nonexistence of positive integer solutions of A^x + B^y = C^z with x,y,z > 2 and gcd(A,B,C) = 1, uniformly in all three exponents. The accessible primary statement at Daniel Mauldin's UNT page agrees with the local target. The nominated AMS prize page returned HTTP 403; the sponsor page delivered an archived-looking page. Source qualifications will be retained in foundations/01-target-and-scope.md.

Three mechanisms considered were a congruence obstruction for each signature, exponent reduction followed by known global theorems, and a radical/height inequality. No existing local branch duplicates them. The first receives the bounded test because it can decide whether building an unrestricted residue sieve could ever eliminate an entire signature. The other two remain untested here; a radical bound would need an unconditional, quantitative input rather than an assumed abc statement.

## Target and discriminating test

Seek, for a fixed signature (x,y,z), a modulus with no primitive admissible residue triple. Such a modulus would rigorously exclude that signature and could support a covering of all signatures. Conversely, a primitive admissible triple for every modulus rules out this unrestricted route. Strengthen the negative test by asking for nonzero primitive p-adic solutions for every prime, so that survival is not explained only by an exactly zero coordinate.

The required sieve threshold is zero surviving classes. A nonempty set for every modulus, even with bases greater than one and pairwise coprime integer representatives, is a decisive negative for that threshold. This does not test sieves combined with a global height bound, descent, or other restrictions on actual integer solutions.

## Reasoning saved before the detailed check

For M >= 1 set t = 2M, A = t, B = t+1, C = t(t+1)+1. The bases are pairwise coprime, greater than one, and reduce to (0,1,1) modulo M. Thus every signature survives every finite collection of congruences.

For a prime p put s = v_p(z), K = 2s+1, A = p^K, B = 1+p^K, and U = A^x+B^y. Then U = 1 modulo p^K. Seek a compatible root C of C^z = U starting at 1. At precision k+s with k >= s+1, the correction C + d p^k changes C^z by z C^(z-1) d p^k modulo p^(k+s+1); higher binomial terms vanish because 2k >= k+s+1. The coefficient (z/p^s) C^(z-1) is invertible modulo p. This should lift uniquely one digit at a time, including p dividing z and p = 2. The limiting C is a unit and cannot equal 1, since U is an ordinary integer greater than one.

## Completed assessment

The indexing and binomial remainder check succeeded, including p = 2 and p dividing z. The full proof is [L001](../lemmas/L001-primitive-local-solubility.md); it also allows the finite integer representatives to exceed any prescribed lower bound. The exact-arithmetic implementation passed 170 finite-representative and 1,625 lifting cases; its scope and output are recorded in scripts/local-solubility/results.json.

The outcome is an informative NEGATIVE: unrestricted local-solubility tests never reach the zero-survivor threshold. The test is complete and is not an unfinished search. No inference from these local solutions to an integer counterexample is made. An additional global restriction would be needed to make a residue sieve decisive; finding one was not part of this step.
