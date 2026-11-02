# L611 bounded independent correctness audit

Completed target: Audit L611's parameter differentiation, shifted-Xi normalization and uniform remainder at a hypothetical double real zero, keeping its missing sign input explicit.

Decision: PASS in the approved SPECIALIZE scope. This verifies an existing
conditional diagnostic; it establishes no new actual-Xi sign or source-level
discovery. The full proof, including the explicit compact determinant error
constant added in this audit, remains canonical in
[L611](../../lemmas/L611-reciprocal-cutoff-double-zero-first-variation.md).

## Inputs and checks

Read L019/L020 completely, L016's theta normalization and L018's Xi
convention, and L610's family definition/qualification. Only L019/L020
are direct mathematical inputs to L611; the computational assertion of
L610 is not used. The ready assessment was supplied at invocation start.
The existing sign-development stop and prior calculation assessment were
checked before replay. No external source or preservation theorem was
needed, and no Mathlib coverage was newly checked.

1. Domination: for j<=2, the frequency derivative has absolute value at
   most u^j exp(Ru). The weight, its first right-parameter derivative and
   its second derivative are bounded respectively by 1, cosh(2u),
   cosh(4u). All resulting majorants are integrable by L019. In the tail,
   v=exp(2u) turns their largest exponential envelope into a constant
   multiple of v^(R/2+13/4)(log v)^j exp(-pi v) dv; near u=0 it is
   bounded. Thus frequency differentiation and the two one-sided
   parameter differentiations are justified. Negative epsilon is not
   required or admitted by this argument.
2. Normalization: the sum of the cosines at z+2i and z-2i is
   2 cos(zu) cosh(2u). L020 therefore gives exactly Q, with factor
   1/2, and the parameter derivative is -Q. The same identity can be
   differentiated j<=2 by the preceding domination with R+2. Reality
   of K gives conjugate shifted values for real t, so Q(t) is precisely
   Re Xi(t+2i); no Xi normalization or frequency rescaling intervenes.
3. Taylor bound: the nonnegative scalar remainder is <=x^2/2 for
   x>=0. Averaging the two weights gives epsilon^2 cosh(4u)/2,
   exactly the M_{j,R} in L611, for every epsilon>=0. This positivity
   is not passed through the cosine transform as a sign claim.
4. Determinant: expanding F'^2-FF'' gives exactly the linear coefficient
   Xi Q''+Xi'' Q-2Xi' Q'. The canonical proof now displays its exact
   remainder and the finite constant E_R. This checks uniform O_R(epsilon^2)
   on 0<=epsilon<=1, rather than assuming uniformity of a product error.
5. Double zero: setting f_0=f_1=0 and f_2=A in that exact remainder
   gives the displayed L611 remainder, bounded by C_a. For c=A q_0!=0
   and 0<epsilon<min(1,|c|/[2(C_a+1)]), the error divided by epsilon
   is <|c|/2. Thus c>0 and c<0 give their respective strict signs.
   For c=0 there is only the stated second-order bound. Constants depend
   on the fixed compact set and hence potentially on a and its shifted data.

All five tests pass. No script, numerical certificate, zero existence
claim, root-splitting theorem or parameter-holomorphic extension is used.
The hypothetical assumptions are Xi(a)=Xi'(a)=0 and Xi''(a)!=0 for real a.
Its existence and the sign of Xi''(a) Re Xi(a+2i) remain unresolved, as do
higher multiplicities, moving frequencies and independent higher signs.

## Relevance and disposition

The main gap is actual-Xi all-degree signs at unbounded heights. The
intermediate target was reliability of this diagnostic; its downstream
use is an exact statement of a missing sign input, not provision of that
input. Retention required domination, shift, remainder and both sign
thresholds to pass; an error would have required repair or rejection.
The diagnostic is retained. Its sign-development route stays parked.
Outcome ADVANCE means a previously unaudited conditional input now has
a completed bounded proof audit, with explicit uniform error accounting;
it does not mean progress beyond the mathematical conclusion already
in L611. No exploration counter is reset by a claimed new sign result.
