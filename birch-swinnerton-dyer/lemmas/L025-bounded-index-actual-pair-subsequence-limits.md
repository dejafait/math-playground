# L025 — Independent subsequential limits of the actual bounded-index pairs

## Hypotheses

Let E/Q be non-CM, and let p >= 5 be good ordinary. Assume surjective
E[p], p dividing neither #E(F_p), the Manin constant nor any Tamagawa
factor, and E(Q_p)[p] = 0. For the classical group
S = Sel(Q,E[p^infinity]), grant corank_Z_p S = 2 and a nonzero residual
Kurihara number in Sakamoto's N_(1,0). These are exactly L024's
arithmetic hypotheses. Put F = S/S_div and h = length_Z_p F.

Let I be any unbounded set of integers m > 2h. At each m in I choose
one actual ordered pair (c_(1,m), c_(2,m)) furnished by L024, with its
specified component tensor factors scalarized by generators. Put
M_m = Sel(Q,E[p^m]) and C_m = (Z/p^m)c_(1,m) + (Z/p^m)c_(2,m).
Thus length_Z_p(M_m/C_m) <= 3h. The selected primes and generators
may vary; no compatibility of these original pairs is assumed.

Use the classical coefficient identification justified in L023,
and let q_(m,k): M_m -> M_k, for m >= k >= 1, be the cohomology map
induced by [p^(m-k)]: E[p^m] -> E[p^k]. Define T_p S using transition
maps [p]: S[p^(k+1)] -> S[p^k]. The approved specialization and
inspected source coverage are in
[the assessment](../drafts/literature/2026-10-06-bounded-span-subsequence-limits.md).

## Conclusion

There are a strictly increasing subsequence m_j in I and elements
x_1, x_2 in T_p S such that, for every fixed k >= 1 and i = 1,2,

\[
q_{m_j,k}(c_{i,m_j})=(x_i)_k
\quad\text{for all sufficiently large }j,
\tag{1}
\]

where M_k is naturally identified with S[p^k]. Every (x_i)_k lies in
S_div[p^k]. The module T_p S is free of rank two, and

\[
x_1\wedge x_2\ne0,\qquad
[T_pS:\mathbf Z_p x_1+\mathbf Z_p x_2]\le p^{3h}.
\tag{2}
\]

More precisely, the exterior has valuation at most 3h in the free
rank-one module wedge^2 T_p S, so its reduction at k_0 = 3h+1 is
nonzero. This valuation is independent of a basis. When h=0 the limit
pair is a basis. The extraction is existential and not canonical.
It gives subsequential ancestry from the selected actual pairs, not a
fixed-prime auxiliary system or compatibility of the original pairs.
It establishes neither rational Kummer membership, finite p-primary
Sha, rational rank two nor a comparison with complex vanishing order.

## Proof

**Natural downward coefficient maps.** Put A = E[p^infinity]. Residual
surjectivity gives A(Q)=0. The exact sequence
0 -> E[p^n] -> A ->[p^n] A -> 0 therefore identifies H^1(Q,E[p^n])
with H^1(Q,A)[p^n] by the map induced by inclusion. L023 verifies
that its preimage of the infinite classical local condition is the
finite classical condition at every place, without assuming local
H^0 vanishing. This gives the identification M_n = S[p^n].

For m >= k the square with top row E[p^m] -> A and bottom row
E[p^k] -> A, both rows inclusions and both vertical maps [p^(m-k)],
commutes. Consequently its induced H^1 maps identify q_(m,k) with
multiplication by p^(m-k) on S[p^m]. These maps preserve classical
conditions: the finite Kummer sequences have vertical maps
[p^(m-k)] on their kernels and their middle E, and the identity on
their right E, since [p^k][p^(m-k)] = [p^m]. Their connecting maps
therefore send a point class modulo p^m to the same point modulo p^k.
The induced maps on H^1(E) are multiplication by p^(m-k). This is
also the coefficient diagram in Milne, *Elliptic Curves*, second
edition (2021), IV.5, pp. 128--129,
[including Proposition 5.1's preceding diagram](https://www.jmilne.org/math/Books/EC2.pdf#page=134).
We use the diagram, not that proposition's rational-image conclusion,
which has an additional no-infinitely-divisible-Sha hypothesis.

**Fixed coordinates and disappearance of the finite part.** L023's
structure gives a splitting S = D^2 direct sum F, where D = Q_p/Z_p;
fix one such splitting once, with the first summand equal to S_div.
It is not chosen separately at different depths. Identify D[p^n]
with R_n = Z/p^n by a -> a/p^n modulo Z_p in each of its two
coordinates. Multiplication by p^(m-k) is then reduction of those
coordinates modulo p^k. The finite group F is killed by p^h: each
of its cyclic elementary divisors has exponent at most its total
length h. This includes F=0 when h=0. For m >= h we have
S[p^m] = D[p^m]^2 direct sum F. At a fixed k, whenever m-k >= h,
q_(m,k) kills the F coordinate and lands in S_div[p^k].

This also identifies the Tate module without assuming exactness of
inverse limits. For any compatible sequence (t_k) in T_p S, its
image in F at level k equals p^h times its image at level k+h and
is therefore zero. Thus every t_k belongs to S_div[p^k], and the
inclusion T_p S_div -> T_p S is an isomorphism. In the fixed compatible
coordinates it identifies T_p S with Z_p^2 and evaluation at k with
reduction modulo p^k.

**Uniform exterior detection.** Discard the finitely many m <= 3h
from I. For each remaining m, let A_m be the two-column matrix over
R_m of the projections of the actual c_(i,m) to D[p^m]^2. Projection
induces a surjection

\[
M_m/C_m\longrightarrow R_m^2/\operatorname{im}(A_m).
\]

Hence the latter quotient has length at most 3h. Choose any lift
B_m in M_2(Z_p) of A_m. Import Smith normal form over a PID, Richard
Elman, *Lectures on Abstract Algebra*, preliminary UCLA author text,
[Theorems 43.5 and 43.8, pp. 255--258](https://www.math.ucla.edu/~rse/algebra_book.pdf#page=263).
Here Z_p is a PID; R_m is used only by reducing the integral normal
form. If b_1,b_2 are its invariant-factor valuations, allowing
b_i=infinity for a zero invariant, invertible integral changes of
basis remain invertible modulo p^m. Thus

\[
\operatorname{length}(R_m^2/\operatorname{im}(A_m))
=\min(b_1,m)+\min(b_2,m)\le3h<m.
\tag{3}
\]

Neither b_i can be at least m, since that term alone would contribute
m to the length. Therefore both are finite and
v_p(det B_m) = b_1+b_2 <= 3h. This conclusion holds for every lift;
changing a lift changes its determinant by a multiple of p^m, while
the valuation just established is less than m. In particular every
det B_m is nonzero modulo p^(3h+1). No scalar is divided by p^h,
and no freeness of M_m or C_m is assumed.

**Subsequence of the same ordered pairs.** Use compactness of
M_2(Z_p), as in Keith Conrad,
[*Maximal compact subgroups of GL_n(Q_p)*, Theorem 1.2 proof, p. 2](https://kconrad.math.uconn.edu/blurbs/gradnumthy/maxcompact.pdf#page=2),
and the finite-digit compactness in Manuel Breuning,
[*p-adic numbers*, LTCC 2010, Theorem 2.22 and Exercise 2.25, pp. 10--11](https://kconrad.math.uconn.edu/math5020f11/breuningnotes.pdf#page=11).
The following specialization records the actual-pair ancestry explicitly.
There are finitely many matrices modulo p. Restrict to an infinite
subset I_1 on which B_m modulo p is constant. Inductively restrict
I_k to an infinite subset I_(k+1) on which B_m modulo p^(k+1) is
constant. These infinite subsets of the integers remain unbounded.
Choose m_j in I_j strictly increasing. For each k, all j >= k lie
in I_k, so the reductions B_(m_j) modulo p^k stabilize to a matrix
B^(k). The stabilized matrices are compatible under reduction and
define a single B in M_2(Z_p). This is the countable finite-coordinate
application of compactness, not a reproof of Smith normal form or of
an arithmetic source construction.

Let x_1,x_2 be the columns of B in the identified T_p S = Z_p^2.
For fixed k, take j large enough that j >= k and m_j-k >= h. The
finite coordinate of c_(i,m_j) is killed, and its divisible coordinate
is the i-th column of B_(m_j) reduced modulo p^k. This equals the
i-th column of B^(k), namely (x_i)_k. Naturality proved above gives
(1) for the original actual pair, with its original order, simultaneously
for both entries. No compatibility of selected primes or generators
has entered this construction.

At k_0=3h+1, each B_(m_j) has nonzero determinant modulo p^k_0 by
(3). Stabilization of the full matrix makes det B congruent to this
same nonzero determinant modulo p^k_0. Therefore v_p(det B) <= 3h.
Its columns are Z_p-independent, their exterior is nonzero, and Smith
normal form over Z_p gives the span index p^(v_p(det B)) <= p^(3h).
This proves (2) and meets the fixed-depth continuation test. The
additional specialization is needed to track actual pairs and their
exterior; compactness alone would permit a dependent or zero limit.
The finite quotient F has disappeared from the coefficient limit,
not from S, and a divisible Sha direction can still survive in T_p S.

**Critical audit, 2026-10-06.** The passage above checks under the
stated hypotheses and the exact L024 index bound. For coefficient
naturality there are two distinct diagrams: inclusion in A identifies
the downward map with multiplication on S, while the finite Kummer
diagram has multiplication on the middle E and identity on the right
E. Thus it reduces point quotients and multiplies their Sha images;
it does not multiply both point quotients by the transition power.
The local preimage argument in L023 supplies the classical conditions
even at places with nonzero local invariants. Global A(Q)=0 supplies
the injectivity needed to regard the coefficient groups as subgroups
of S. No local-invariant vanishing has been added.

The fixed splitting in the proof is legitimate because S_div is
divisible and hence injective as an abelian group; L023 already gives
the resulting group structure. One splitting works at every depth.
Projection onto its divisible summand induces the displayed quotient
surjection even when the actual columns have nonzero F coordinates:
the image of C_m is exactly the column span of A_m. No assertion that
C_m splits, is free, or projects injectively is used. At fixed k the
inequality m-k >= h is essential to remove those finite coordinates.
Likewise, a compatible sequence in F is zero because its k-th entry
is p^h times its (k+h)-th entry, not because the individual finite
coefficient groups have zero finite part.

For the exterior test, m>3h is imposed only after restricting the
unbounded set of available depths; it is not a strengthening of the
initial existence hypothesis m>2h. A zero integral invariant factor,
or one divisible by p^m, would contribute m to the reduced quotient
length and contradict (3). Hence the determinant valuation bound is
valid for every integral lift. The integer detecting depth 3h+1 is
necessary for this stated bound: a determinant of valuation exactly
3h vanishes modulo p^(3h), so merely testing that latter level would
not suffice. The proof uses the former level throughout.

The nested infinite subsets stabilize the entire ordered matrix, not
two columns along potentially different subsequences. For fixed k,
eventually j>=k and m_j>=k+h; these are the two separate thresholds
needed to identify the stabilized matrix with the reductions of the
original pair. At k=3h+1 the stabilized determinant belongs to a fixed
nonzero residue class. Thus the proof does not use the false general
implication that a limit of nonzero determinants is nonzero. Changing
the noncanonical splitting can change the intermediate projections,
but equality (1) concerns the actual intrinsic coefficient maps.
Existence of one such splitting suffices for the claimed existential
subsequence, and the final exterior valuation is invariant under
integral changes of basis of T_p S. For h=0 all finite coordinates
are absent and the same test at k=1 gives a basis.

No error, new arithmetic assumption or compatibility requirement was
found. This verifies L025's conditional integral passage and its
finite-depth ancestry; it adds no bound or rationality statement.
In particular, the audit does not promote vanishing of T_p F to
vanishing of F or of T_p Sha. The direct mathematical inputs remain
L023 and L024; L021 enters through L023.

## Mathlib

Full matching actual-pair subsequence theorem: not checked. Supporting
p-adic compactness, Smith normal form, exterior powers and Selmer
coefficient naturality: Mathlib coverage not checked. No absence claim
or formal verification is made. This is a conditional reproduction and
specialization of the inspected standard inputs, not a novelty claim.
