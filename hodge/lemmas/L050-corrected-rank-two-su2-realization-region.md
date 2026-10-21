# L050 — Exact topological SU(2) region and symmetric exclusion

## Hypotheses

Retain L048 and L049's smooth projective K3 self-product X=S x S,
fixed ample chamber, and full integral mixed class tau_D. With eta
the integral point class of S, normalized to have integral one, set
e_1=eta tensor 1, e_2=1 tensor eta and P=eta tensor eta. For integers
a,b write

\[
p=4+a,\qquad t=4+b,\qquad
\beta_{a,b}=p e_1+t e_2+\tau_D,\qquad u=-\beta_{a,b}.
\]

The admitted correction region is a+b<=-13 and 6|pt, as established
by L048 and left unchanged by L049's product-line indices. The full
mixed square is integral_X tau_D^2=156, including the transcendental
contribution 120. The prospective complex bundle has rank two,
trivial determinant, and second Chern class u. Its higher characters
are forced, rather than taken from L045's excluded virtual class.

Here SU(2) is the bundle's compact structure group Sp(1). Existence
with this structure group is a topological assertion. It does not
give a connection invariant under the diagonal hyperkahler rotations
used elsewhere in the notebook.

## Conclusion

The exact subset of the admitted region realized by topological
complex rank-two SU(2) bundles is

\[
\boxed{\{(a,b)\in\mathbb Z^2:
 a+b\leq-13,\quad (a+4)(b+4)\equiv6\pmod{12}\}.}               \tag{1}
\]

Such a bundle has rational Chern character

\[
2+\beta_{a,b}+\frac{pt+78}{6}P,
\]

exactly L048's forced character. In particular it supplies an integral
topological K-class, with no specified holomorphic realization.

Every symmetric integer pair a=b fails topological SU(2) realization,
including all symmetric survivors of the earlier index tests. For
a=b=-10, the characteristic number required to vanish modulo 12 is
-30, with residue 6. Conversely (-7,-6), and its factor reversal,
lie on the admitted integer boundary and have topological SU(2)
realizations. Their forced fourth character is 14P and their
untwisted index is 12.

This is an informative NEGATIVE for the saved symmetric input and
the whole symmetric recipe, together with a positive topological
existence statement for the nonsymmetric region. The general
existence theorem is imported; its specialization is REPRODUCTION,
without a claim beyond the checked literature. No holomorphic
bundle, stability proof, new algebraic class or transverse RM
surface is supplied. The span remains 21 and the attained RM
directions three against four required. The universal Hodge gap
remains open.

## Proof

**Import the finite-rank theorem.** Use Čadek--Crabb--Vanžura,
*Obstruction theory on 8-manifolds*, author's manuscript dated
5 December 2007 and corrected 8 July 2008,
[Corollary 8.4, manuscript p. 13](https://www.math.muni.cz/~cadek/papers/8_manifolds.pdf#page=13).
For a connected closed smooth eight-manifold M, a line lambda with
l=c_1(lambda) reducing to w_2(TM), and u in H^4(M,Z), an
H_lambda-line with second Chern class u exists if and only if

\[
\operatorname{Sq}^2\rho_2(u)=\rho_2(lu),\qquad
\frac14\langle p_1(TM)u+2u^2-l^2u,[M]\rangle\equiv0\pmod{12}.
                                                                    \tag{2}
\]

The numerical expression is integral under the cohomological
condition. This is a quaternionic line, of complex rank two;
it is not only the stable complex rank-four conclusion of that
paper's Proposition 3.2. The general theorem and its obstruction
theory proof are imported without reproof. Its statement and
Sections 7--8 were read for the ready SPECIALIZE assessment.

The K3 facts used below are supported by Huybrechts,
*Lectures on K3 Surfaces*, prepublication draft,
[Chapter 1, Definition 1.1, p. 7](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=7),
[Section 2.4, pp. 12--13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=12),
and [Section 3.2 and Proposition 3.5, pp. 15--17](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=15).
These give trivial canonical bundle, c_2(TS)=24eta, torsion-free
integral cohomology with zero odd groups, and the even K3 lattice.
These supporting statements were also read in the saved assessment.

**Check the manifold and determinant hypotheses.** The underlying
real manifold of X is connected, closed, smooth and oriented by
its complex structure, of dimension eight. The trivial canonical
bundle gives c_1(TX)=0, so w_2(TX)=rho_2(c_1(TX))=0. Choose
lambda trivial and l=0 in (2). An ordinary quaternionic line has
structure group Sp(1)=SU(2), hence gives a complex rank-two bundle
with trivial determinant. Conversely a complex SU(2) bundle has
its standard quaternionic structure. Thus (2) tests exactly the
stated finite-rank question. Integrality of u follows from L048's
full integral beta; no rational NS/transcendental splitting is
promoted to an integral one.

**The Steenrod condition is automatic on this product.** Since the
integral cohomology of S is torsion-free and concentrated in even
degrees, the integral Kunneth theorem and reduction modulo two give

\[
H^4(X,\mathbb F_2)=
\mathbb F_2\rho_2(e_1)\ \oplus\
\bigl(H^2(S,\mathbb F_2)\otimes H^2(S,\mathbb F_2)\bigr)
\ \oplus\ \mathbb F_2\rho_2(e_2),
\]

and every degree-two class on S has an integral lift. Naturality
and dimension give Sq^2 rho_2(e_i)=0, because the corresponding
operation on eta lies in H^6(S,F_2)=0. For any integral x in
H^2(S,Z), Sq^1 rho_2(x)=0 (its target H^3 vanishes) and the
degree-two square identity gives

\[
\operatorname{Sq}^2\rho_2(x)=\rho_2(x)^2
 =\rho_2(q(x,x)\eta)=0.
\]

The last equality uses evenness of the full K3 lattice, not only
the divisor lattice. For integral x,y in H^2(S,Z), the Cartan
formula now makes Sq^2 of their external product zero: the three
terms use Sq^2(x), Sq^1(x)Sq^1(y), and Sq^2(y), respectively.
External products of such lifts span the mixed summand. Additivity
therefore proves Sq^2=0 on all H^4(X,F_2), in particular on rho_2(u).
This proves the first condition of (2), whose right side is zero.
The argument works on the actual integral mixed tensor tau_D,
including any integral gluing between its rational projections.

**Evaluate the characteristic number with the full square.** The
standard realification identity p_1(TS_R)=c_1(TS)^2-2c_2(TS)
gives p_1(TS_R)=-48eta. Whitney additivity of p_1 for the tangent
sum of the product therefore gives

\[
p_1(TX_R)=-48(e_1+e_2).
\]

Pure point classes annihilate tau_D by factor degree, e_i^2=0,
and e_1e_2=P. Thus

\[
\langle p_1(TX_R)u,[X]\rangle=48(p+t),\qquad
\langle u^2,[X]\rangle=2pt+156,
\]

where the second identity is L048's full mixed-square computation.
The source theorem uses the tangent Pontryagin class, not that of
the sought bundle. Substitution into (2) with l=0 gives

\[
J(p,t)=\frac{48(p+t)+2(2pt+156)}4
       =12(p+t)+pt+78.                                         \tag{3}
\]

This is an integer for every pair. Since 78 is 6 modulo 12,
J vanishes modulo 12 if and only if pt is 6 modulo 12. The first
condition was automatic, so necessity and sufficiency in the cited
corollary both apply. This proves (1). In particular 6|pt follows
automatically; none of L049's product-line index conditions remains
an extra obstruction after topological realization.

For any resulting rank-two complex bundle, c_1=0 and rank
truncation gives c_3=c_4=0. The Chern-character identities reused
in L048 then give ch_2=-u=beta, ch_3=0 and
ch_4=u^2/12=(pt+78)P/6. Thus the theorem realizes the full proposed
rational character, not just an unrelated second Chern class.
There is no assertion of uniqueness or of a prescribed K-class
such as the failed V' in L045.

**Discriminate the symmetric data and preserve the survivors.**
For a=b, the product pt=(a+4)^2 is a square. Squares modulo 12
are 0,1,4,9, never 6. Hence no symmetric pair is realizable.
At (-10,-10), p=t=-6 gives J=-144+36+78=-30. Moving further
inside the symmetric Bogomolov region cannot repair this failure.
At (-7,-6), p=-3,t=-2 gives p+t=-5, pt=6 and J=-60+6+78=24.
Its sum a+b=-13 is the integer boundary of L048's admitted region.
The full character has ch_4=14P and untwisted index
8+2(-5)+14=12. The same holds with the factors reversed.

As a consistency check, L048's untwisted expression
I=8+2(p+t)+(pt+78)/6 is an even integer exactly when pt is 6
modulo 12. Thus this new filter is equivalent here to the even
spin index of a quaternionic bundle noted in Sections 7--8 of the
source. Ordinary index integrality alone misses it. This parity
observation is not used as a substitute for the corollary's
finite-rank sufficiency, and no evenness condition is imposed on
arbitrary complex product-line twists, which need not preserve
quaternionic structure.

The exact numerical verification is
`python3 scripts/cubic-kahler/check_corrected_rank_two_su2.py`.
It checks (3) and all 144 residue pairs modulo 12; the old
ordinary-index test admits 60 pairs and the new criterion admits
20. Each residue pair has integer representatives with a+b<=-13,
by decreasing a or b by multiples of 12. The program also checks
the symmetric input and the boundary survivor. Steenrod vanishing
and actual existence rely on the proof and imported theorem above,
not finite computation. Holomorphic realization, slope-polystability
at the fixed metric and transverse transport remain separate gaps.

## Mathlib

Coverage of the full specialized realization region: **not checked**.
No matching declaration or absence from checked Mathlib sources is
asserted. Čadek--Crabb--Vanžura Corollary 8.4 matches the general
finite-rank existence criterion; it does not evaluate this corrected
RM tensor. The directly linked Huybrechts statements support the
K3 inputs. Kunneth, Cartan, naturality, the degree-two Steenrod-square
identity and the Whitney/realification characteristic formulas are
supporting standard tools; L048 supplies the full mixed square and
character identities. This is a reproduction of covered tools,
with no certified originality or general Hodge resolution claim.
