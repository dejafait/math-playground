# L048 — Corrected rank-two Chern truncation and untwisted Euler region

## Hypotheses

Retain L045's smooth projective fourfold X=S x S, final ample chamber,
integral second-character class beta=2[C]+B_c and full mixed tensor
tau_D. Write eta for the integral point class on S with integral one,
e_1=eta tensor 1, e_2=1 tensor eta and P=eta tensor eta. Thus

\[
\beta=4e_1+4e_2+\tau_D,\qquad
D|_N=2A_c+4\pi_K,\qquad D|_T=2U.
\]

The integer correction coefficients a,b satisfy L047's necessary
Bogomolov region a+b<=-13. Set

\[
p=4+a,\qquad t=4+b,\qquad
\beta_{a,b}=p e_1+t e_2+\tau_D.
\]

The putative locally free bundle F has rank two, c_1(F)=0 and
ch_2(F)=beta_(a,b) in cohomology. Its higher characters and K-class
are initially unrestricted; in particular the higher characters of
L045's excluded V' are not prescribed. Only cohomological Chern
truncation and the untwisted HRR index are tested here.

## Conclusion

For an actual F the rank-two identities necessarily force

\[
\begin{aligned}
c_2(F)&=-\beta_{a,b},& c_3(F)&=c_4(F)=0,\\
\operatorname{ch}_3(F)&=0,&
\operatorname{ch}_4(F)&=\frac{pt+78}{6}P,\\
\chi(X,F)&=8+2(p+t)+\frac{pt+78}{6}
          =\frac{ab+16a+16b+238}{6}.
\end{aligned}                                                    \tag{1}
\]

The exact region passing these necessary cohomological rank and
untwisted Euler tests, together with L047's integer inequality, is

\[
\{(a,b)\in\mathbb Z^2:
       a+b\leq-13,\quad 6\mid(a+4)(b+4)\}.                       \tag{2}
\]

Here passing means that the forced character has integral lower
Chern classes, zero higher Chern classes through the dimension of X,
and an integer untwisted HRR expression. It asserts neither the
existence of an integral K-class with that character nor a bundle.

The region is nonempty. For example (-13,0) has forced ch_4=7P
and chi=5. In the symmetric integer subfamily a=b=u, survival is
equivalent to u<=-7 and u congruent to 2 modulo 6. Thus the least
negative surviving symmetric correction is u=-10, with ch_4=19P
and chi=3. The previously allowed u=-7 fails this index test:
its forced ch_4=(29/2)P and chi=21/2.

This is a relevant local arithmetic ADVANCE, classified as
REPRODUCTION of the assessed Chern-character and HRR tools. It
isolates necessary data for further tests without claiming progress
beyond the checked literature. No algebraic class or transverse
surface is added: the known span remains 21, with three attained RM
directions against four required. The universal Hodge gap stays open.

## Proof

**Import the character identities and HRR.** Use the rank-two Chern
truncation in Fulton, *Intersection Theory*, second edition (1998),
[Theorem 3.2(a), pp. 50--52](https://djvu.online/file/87GFN2nbfbdF7),
also reflected in
[Stacks Definition 42.37.1, Tag 02TZ](https://stacks.math.columbia.edu/tag/02TZ).
Import the universal character expansion through ch_4 from
[Stacks Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM).
For the Euler characteristic use the smooth proper HRR statement in
[Stacks Section 42.66, Tag 02UO](https://stacks.math.columbia.edu/tag/02UO),
with the Todd expansion in
[Section 42.65, Tag 02UN](https://stacks.math.columbia.edu/tag/02UN).
These statements were already read for the ready SPECIALIZE
assessment. Their general proofs are imported; only the substitution
for the corrected family is reproduced here. X is smooth and proper
over C, so HRR to a point applies to a locally free F and its Euler
characteristic is an integer. No projective-space Schwarzenberger
condition or Fourier--Mukai hypothesis is used.

**Keep the full mixed square.** L045 computes
integral_X tau_D^2=tr_N(D^2)+tr_T(D^2)=36+120=156.
The contribution 120 from T is essential even though it has zero
contraction with L047's product polarization. The pure/mixed products
vanish: multiplying e_i by a degree-two class on the same surface
would exceed that surface's top degree. Also e_1^2=e_2^2=0 and
e_1e_2=P. Consequently, since H^8(X,Q)=Q P,

\[
\beta_{a,b}^2=(2pt+156)P.                                      \tag{3}
\]

This reuses L045's mixed-tensor computation, without carrying over
the old pure coefficients or its fixed fourth character. The class
beta_(a,b) is integral: 2[C] is integral, B_c is the integral divisor
tensor in that chamber, and a,b,e_1,e_2 are integral. Thus its negative
is an admissible integral *cohomological* second Chern class.

**Force higher characters afresh.** For rank two, the imported
truncation gives c_3=c_4=0. With c_1=0, the character polynomials give

\[
\operatorname{ch}_2=-c_2,\quad
\operatorname{ch}_3=c_3/2=0,\quad
\operatorname{ch}_4=(2c_2^2-4c_4)/24=c_2^2/12.
\]

Substituting (3) proves the character assertions in (1). At this
cohomological level these identities are consistent for every
integer a,b: choose the displayed character with c_2=-beta_(a,b)
and c_3=c_4=0. There are no higher cohomological components on a
fourfold. This consistency supplies no K-theory or locally free
realization. In particular rank truncation does not require ch_4=0,
and a Chern character need not itself be integral.

**Evaluate the untwisted Euler expression for the whole region.**
Reuse L045's K3-product Todd class

\[
\operatorname{td}(X)=1+2(e_1+e_2)+4P.
\]

The top-degree part of ch(F) td(X) is
ch_4(F)+2 beta_(a,b)(e_1+e_2)+8P. Its integral is therefore

\[
\chi(X,F)=\frac{pt+78}{6}+2(p+t)+8
         =\frac{pt+12p+12t+126}{6}.                            \tag{4}
\]

Substitution p=4+a, t=4+b gives (1). Because p,t are integers,
the last numerator in (4) is congruent to pt modulo 6. Thus (4)
is an integer if and only if 6 divides pt. This proves the exact
congruence across the infinite integer region, rather than merely
testing finitely many correction pairs. Equivalently at least one
of p,t is even and at least one is divisible by three; those two
factors may differ. L047 supplies the independent inequality
p+t<=-5. Their conjunction is exactly (2).

For a=b=u, divisibility of (u+4)^2 by 6 is equivalent to divisibility
of u+4 by both 2 and 3, hence by 6. Thus u is congruent to 2 modulo
6, and the largest such u with u<=-7 is -10. Substituting the three
listed pairs in (1) gives their exact fourth characters and indices.
These examples distinguish nonempty arithmetic consistency from
the newly excluded symmetric boundary data.

The exact verification command is
`python3 scripts/cubic-kahler/check_corrected_rank_two_untwisted.py`.
It checks the character and index polynomials using rational sparse
polynomials, exhausts all 36 residue pairs modulo 6 (15 survive),
and checks the stated examples. The proof of (2) is the algebraic
congruence argument above; computation certifies neither a bundle
nor stability or transverse transport. Product-line-twisted indices
and further realization conditions remain untested in this step.

## Mathlib

Coverage of the full corrected-data arithmetic region: **not
checked**. No matching Mathlib declaration or absence from checked
Mathlib sources is asserted. The named and directly linked Fulton
and Stacks statements support rank truncation, character identities,
Todd classes and HRR; they do not match the evaluated region (2).
Kunneth and cup-product contraction are standard supporting tools,
with the fixed full mixed-square computation supplied by L045.
This is a reproduction of known tools, with no certified originality
or Hodge resolution claim.
