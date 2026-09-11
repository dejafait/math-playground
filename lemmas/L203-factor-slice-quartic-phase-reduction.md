# Lemma 203: factor-slice quartic phase reduction

**Hypotheses.** Use the box F_N of L202, with fixed t>0 and real N
sufficiently large. Fix any allowed integers a,c,d and put v=cd,
A=2N²-2tN^(3/2), B=2N²-tN^(3/2),

b0=ceil(A/a), M=floor(B/a)-b0, x0=sqrt(a b0 v).

Thus the allowed b are exactly b0+j for integers 0<=j<=M. Define

P4(j)=x0[1+j/(2b0)-j²/(8b0²)+j³/(16b0³)-5j⁴/(128b0⁴)].

For u=a(b0+j), let Q(j) be L201's phase.

**Conclusion.** Uniformly over these actual integer slices,

|Q(j)-P4(j)| <= C_t N^(-1/2).                         (1)

For any fixed 0<eta<1/8, and sufficiently large N, the number
of tuples in F_N passing frac(Q) in [5/8,7/8] lies between the
sums over the allowed triples (a,c,d) of the following two counts:

#{0<=j<=M: frac(P4(j)) in [5/8+eta,7/8-eta]},          (2)
#{0<=j<=M: frac(P4(j)) in [5/8-eta,7/8+eta]}.          (3)

No lower bound for (2) is asserted. If P2 is the degree-two Taylor
polynomial obtained by deleting the last two terms of P4, then

Q(M)-P2(M) is bounded above and below by positive
constants depending on t times sqrt(N).              (4)

Thus this quadratic Taylor approximation does not have o(1)
absolute phase error on the full slice.

**Proof.**

The interval count and uniform factor bounds of L202 give
b0 comparable to N, x0 comparable to N², and

M=tN^(3/2)/a+O(1),

where the absolute rounding error is at most two. Since a/N is
in [11/10,6/5], M is comparable to sqrt(N), with constants depending
on the fixed positive t. For 0<=j<=M put z=j/b0. Then
0<=z<=C_t N^(-1/2), in particular z<=1/2 for large N.

Taylor's theorem for sqrt(1+z) at zero gives

sqrt(1+z)=1+z/2-z²/8+z³/16-5z⁴/128+r5(z),
0<=r5(z)<=7z⁵/256.

Indeed its fifth derivative is (105/32)(1+z)^(-9/2), which is
positive and bounded above by 105/32 for z>=0. Multiplying by
x0 shows that x(j)=sqrt(a(b0+j)v) differs from P4 by a nonnegative
quantity at most (7/256)x0(M/b0)^5=O_t(N^(-1/2)).
L201 applies because u,v lie in J_N and |u-v|<=tN^(3/2).
It gives Q(j)=x(j)+E(j), with 0<=E(j)=O_t(N^(-1)).
This proves (1), including uniformity over all triples.

Choose N large enough that the bound in (1) is less than eta.
The intervals in (2) and (3) stay strictly inside (0,1).
Distance less than eta modulo one therefore sends (2) into
[5/8,7/8], and sends that latter interval into (3). This proves
the two inclusions for each slice. Every tuple has a unique triple
(a,c,d) and j, so summing counts introduces no multiplicity error.
This does not require any assertion about points near boundaries.

Finally at j=M, z is comparable to N^(-1/2) with a positive
lower constant. The same expansion gives

x(M)-P2(M)=x0[z³/16-5z⁴/128+r5(z)].

For 0<=z<=1/2 the bracket is at least z³/32 and at most z³
(the stated remainder bound suffices for both inequalities).
Thus this difference is comparable to N² N^(-3/2)=sqrt(N).
The nonnegative O_t(N^(-1)) correction E preserves these bounds,
proving (4).

## Qualifications and verification

This is a scoped reduction of the phase-selected population problem,
not a proof or disproof of its order N³ lower bound. A large absolute
Taylor error alone does not show fractional parts are poorly distributed;
it prevents using that truncation as a uniformly accurate substitute.
The polynomial coefficients depend on the actual integer triple and
rounding b0. No independence, equidistribution, coprimality, or totient
selection is assumed. The geometric cutoffs remain those already proved
in L202. The overall RH argument is unchanged.

`python3 scripts/heat/check_factor_slice_phase.py` checks the Taylor
remainder and cubic lower bound by exact rational squared inequalities.
These finite algebra checks are not population evidence. Formalization
requires Taylor's theorem with its signed remainder, uniform integer
rounding bounds, and the fractional-part interval inclusions above.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
