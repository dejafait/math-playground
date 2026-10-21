# Ordinary first-height and coefficient-tower audit

The ready SPECIALIZE coverage is the exact COVERED_TARGET in
[the prior assessment](literature/2026-10-04-cyclotomic-selmer-height-radical.md).
No additional literature is needed for this formal calculation.

Gap: the proposed arithmetic assertion is that the first ordinary
cyclotomic height radical surjects onto V_p Sha. Its possible use is
to combine that surjection with full-Selmer nondegeneracy and eliminate
the divisible quotient. Neither arithmetic premise is established.
The test here is whether the already existing L013 package, including
L018's tower shape, forces that surjection. The required rational
bound is r >= 2; the current bound is only r <= 2.

Working calculation (saved before completion): L013's ordinary
differential is t times the identity, whereas its relaxed differential
is the row (0,t). Dividing the ordinary differential by t gives the
identity S -> S^dual. Evaluation therefore gives a first height with
matrix identity, up to the common comparison sign, and zero radical.
Its marked quotient S/W has dimension one. The relaxed Bockstein's
kernel W is not the ordinary height radical.

At t = 0 the integral ordinary complex has zero differential, so
H^1 after reducing modulo p^m is (Z/p^m)^2. Reduction maps correspond
to multiplication by p on D^2[p^(m+1)] after embedding a coordinate
v modulo p^m as p^(-m)v modulo Z_p^2. The marked Kummer line and
Sha quotient are the first and second coordinates, respectively.
Any GL_2(Z/p^2) prescribed basis has one GL_2(Z_p) lift and hence a
compatible basis at every depth. The marked Sha is D with zero
Cassels--Tate pairing. Thus the additional tower appears compatible
without altering any local triangles of L013.

Continuation test: verify the integral identifications and the ordinary
height, keeping their distinction from an arithmetic realization. If
they hold, stop the formal radical-surjectivity inference and isolate
the arithmetic input missing from the model. This does not refute an
arithmetic theorem or BSD. A full actual Kurihara/Stark family,
production of the two-prime premise from analytic rank two, analytic
comparison, and higher ranks remain outside the calculation.

Completion: the proof and all-depth coefficient identifications are
now in [L019](../lemmas/L019-ordinary-height-radical-with-compatible-sha-tower.md).
The ordinary Bockstein has rank two and the relaxed one rank one;
the former gives zero height radical. The tower, prescribed bases,
marked quotient and divisible pairing kernel are compatible. The
formal radical-surjectivity mechanism therefore stops with NEGATIVE,
classified REPRODUCTION. The working calculation above is preserved;
no actual arithmetic surjectivity theorem is refuted.
