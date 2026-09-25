# Eisenstein coefficient reduction — 2026-09-25

One focused global factorization step, not a candidate resolution of Beal.

## Starting state and relevance

The shared guidance and prompt, local target and checkpoint, whole overview, DAG, existing changes, and the relevant factorization, restriction, and local-lift proofs were read. Earlier work is preserved. The accessible [Mauldin primary statement](https://sites.math.unt.edu/~mauldin/beal.html) was fetched again; the nominated AMS page still returned HTTP 403. The existing source qualification is retained.

The addressed gap is integer emptiness of the constrained repeated-cube system II at primes p >= 19 congruent to 1 modulo 3. The intermediate target is an exact Eisenstein-integer power extraction retaining the sum-power condition, followed by the coefficient equation and its common-factor valuations. A useful result would expose an explicit perfect-power condition in a coprime recurrence to which a global descent or divisor theorem could be tested. Failure to retain the coefficient condition, or merely reproducing the isolated norm condition, would abandon this proposed improvement. Uniform exclusion of the resulting coefficient equations and of other residual signatures would remain open.

L003 already allocates rational integer factors and reconstructs bases; it does not extract powers in the Eisenstein ring. Attempt 002 rules out excluding the quadratic factor alone, and L006 / Attempt 003 rule out the tested exceptional-prime lifting obstruction. Neither decides the simultaneous coefficient condition in a global algebraic integer. The notebook search found no prior Eisenstein or Lucas reduction.

## Unfinished reasoning saved before the full derivation

Write W=3^(p-2)u^p. System II becomes d^2+3W^2=4v^p, suggesting alpha=(d+W sqrt(-3))/2 in Z[(1+sqrt(-3))/2]. The two conjugates should be coprime because gcd(u,v)=1 and 3 does not divide v. Norm-Euclidean factorization and absorption of the six units for p prime at least five would then give alpha=gamma^p, with gamma=(r+t sqrt(-3))/2.

The prospective retained constraint is t U_p(r,v)=W, where U_0=0, U_1=1, and U_(n+2)=r U_(n+1)-v U_n. Needed checks: integrality and oddness of r,t; coprimality of r,t and r,v; the 3-adic valuation of U_p; the exceptional common factor at p; signs; and a converse preserving positivity and primitivity. No contradiction follows just from the existence of a prime divisor of U_p. This paragraph records a lead, not an established result.

## Completed assessment

[L007](../lemmas/L007-eisenstein-coefficient-reduction.md) supplies the full derivation and converse. Norm-Euclidean factorization is proved directly; all six units can be absorbed because p is prime to six. Odd half-integer coordinates are essential. The conjugates are coprime using gcd(v,3u)=1; rational primes are not incorrectly treated as prime in the Eisenstein ring.

The retained coefficient condition has 3 not dividing U_p, so v_3(t)=p-2+p v_3(u). Its two factors are coprime except possibly at p, and p divides U_p exactly when p divides t, then with valuation one. The two resulting shapes are U_p=sigma k^p and U_p=sigma p k^p. The sign sigma cannot be discarded. The trace equality reconstructs d, but its positivity bound must still be imposed. The recurrence also proves the converse's parity and coprimality conditions rather than assuming them.

The exact control p=5,r=5,t=1 reproduces L003's isolated quadratic-factor witness: U_5=149, T_5=-25, and (a,b)=(211,236). Its coefficient is not 3^3 times a fifth power. Thus the new test retains exactly the simultaneous condition missing in Attempt 002; this control is outside the full hypotheses and is not a counterexample.

The intermediate target was an exact parameterization exposing useful coefficient valuations, and it is achieved. The required family threshold remains zero complete solutions. The new inequality |t| >= 3^(p-2) is a lower bound and gives neither that threshold nor a finite search. A primitive prime divisor alone would be compatible with both allowed pth-power shapes. Its multiplicity is the discriminating issue for the proposed downstream test; no primitive-divisor theorem has been invoked, and no success of that test is assumed.

[Exact-arithmetic results](../scripts/eisenstein-coefficient/results.json) record 4708 coprime signed parameter cases at p=5,7,11,13,19,31. They compare ring multiplication, recurrences, and the binomial expansion, including 816 cases with p dividing t, 624 with large 3-adic valuation, and 2332 with v congruent to 1 modulo 12. The unit power maps and both displayed controls also pass. These are checks of formulas and valuations, not purported solutions of the simultaneous system. Reproduce with `python3 scripts/eisenstein-coefficient/check_coefficients.py`.

Outcome: ADVANCE, for the exact global extraction and valuation input, without any claim of family emptiness. Exploration turns used: 0/3. No complete candidate appeared. The reason to continue one bounded divisor test is that the recurrence now exposes an explicit multiplicity requirement; the sole current action is in PROGRESS.md.
