# Attempt: force critical-line zeros from reflection symmetry

Date: 2026-09-09

Outcome: failed inference; baseline lemmas retained in PROOF.md.

The candidate argument was to combine the conjugation identity and Riemann's functional equation and infer that every zero in the open critical strip must satisfy ρ=1-conj(ρ), hence Re(ρ)=1/2. The valid conclusion is only that these maps preserve the zero set and multiplicities.

For a=1/4+i, the polynomial

P(s)=(s-a)(s-conj(a))(s-(1-a))(s-(1-conj(a)))

has exactly the same two symmetries. Its zeros have real parts 1/4 and 3/4. Moreover P(x)>0 for real x, since P(x)=((x-1/4)²+1)((x-3/4)²+1). With d=1/4 it satisfies P(1/2+it)=(t²-(1-d²))²+4d²>0 for all real t. These are exact identities, not numerical observations.

**WHY IT FAILS.** Invariance of a zero set under reflection does not imply that each zero is fixed by reflection: off-line zeros can occur in four-element orbits. This explicit polynomial satisfies both symmetries and even positivity on the real axis and critical line while having four off-line zeros. It refutes the proposed implication, not RH itself; extra properties specific to ζ would need a separate argument. No such argument was established in this attempt.

Next lemma: establish nonvanishing on Re(s)=1 away from the pole using the classical nonnegative trigonometric-polynomial Euler-product argument, with absolute convergence and local zero orders explicit.
