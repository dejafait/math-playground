# L055 — Relative direct image excludes the five-charge coefficient slice

## Hypotheses

Retain exactly L044's smooth projective complex K3 surface S, real
Kahler class h and full integral mixed tensor tau_D on X=S x S.
The product polarization is Omega=p_1^*h+p_2^*h. Write eta for
the integral point class with integral_S eta=1, e_1=eta tensor 1,
e_2=1 tensor eta and P=eta tensor eta. As in L052, the mixed
operator is D=2A_c+4pi_K on NS(S)_Q and D=2U on T(S), and
the full class is invariant at the common hyperkahler metric.

Let b be an integer such that (a,b)=(-9,b) is an L052 survivor:

\[
b\leq-9,\qquad (-5)(b+4)\equiv6\pmod{12}.                 \tag{1}
\]

Suppose F is a rank-two locally free holomorphic bundle,
slope-polystable at Omega, with cohomological data

\[
c_1(F)=0,\qquad
\operatorname{ch}_2(F)=-5e_1+(b+4)e_2+\tau_D.             \tag{2}
\]

Initial higher characters and the K-class are unrestricted.
Neither stability of the other factor restrictions, a presentation,
a Fourier--Mukai equivalence, nor transverse transport is assumed.
All characters below are in rational cohomology.

## Conclusion

No F satisfying these hypotheses exists, for any integer b in (1).
Writing t=b+4 and pi=p_2, an actual F would give a line bundle
G=R^1 pi_*F with

\[
\operatorname{ch}(G)=1-\frac{7t+78}{6}\eta
                    =1-\frac{7b+106}{6}\eta,
\qquad c_1(G)=0.                                       \tag{3}
\]

The line character identity would require b=-106/7, which is
not an integer. Equivalently, the complete survivor slice is
b=-10-12j for integers j>=0, and (3) becomes

\[
\operatorname{ch}(G)=1+(14j-6)\eta.                     \tag{4}
\]

No nonnegative integer j makes its second character zero.
The rational exceptional value in (3) is recorded only as a formal
compatibility value for the character test, not as bundle existence.

This is an informative NEGATIVE, classified as REPRODUCTION of
the assessed base-change, relative GRR and character tools. It widens
L054's fixed-pair exclusion to an infinite slice, without claiming
progress beyond the checked sources or an originality result.
L050's topological existence and L053's individual factor existence
are preserved. Other correction slices and other representatives
remain open; no algebraic Hodge class or transverse surface is added.

## Proof

**Check the approved restriction input for every coefficient.**
The sum -9+b is at most -18, hence satisfies the weaker sum
condition in L052's hypotheses, and (1) supplies its topological
congruence. Its coefficient-independent restriction conclusion
therefore applies to every first-factor embedding
j_y:S -> X, z -> (z,y). It gives a locally free rank-two
slope-polystable E_y=j_y^*F at h with c_1(E_y)=0 and c_2(E_y)=5.
This uses L052's hyperholomorphic curvature restriction, not a
generic restriction theorem. L044 fixes the invariant mixed class;
varying b changes only the invariant pure point coefficient.

L052's zero-slope line lattice makes every split polystable factor
have c_2=14r^2 for an integer r. Since five is not of this form,
every E_y is stable. L052's stable surface cohomology calculation
(equation (4), with its section, dual stability and Serre duality
argument) then gives

\[
H^0(S,E_y)=H^2(S,E_y)=0,\qquad
\chi(S,E_y)=4-5=-1,\qquad h^1(S,E_y)=1.                 \tag{5}
\]

There is no cohomology above degree two on S. These statements
hold at every closed fibre, independently of b. The other factor
has no role in (5), and its stability is not asserted.

**Import base change to obtain an actual line bundle.**
By Serre's GAGA theorem, F is an algebraic vector bundle on the
projective complex X with the same fibre cohomology. The morphism
pi is smooth projective of finite presentation. F[0] is a bounded
coherent complex, flat over S, with proper support, and O_X is
perfect. These discharge the hypotheses of
[Stacks Lemma 36.30.1, Tag 0A1H](https://stacks.math.columbia.edu/tag/0A1H):
K=Rpi_*F is perfect and commutes with arbitrary derived base change.
In particular, its derived fibre at a closed y is R Gamma(S,E_y).

By (5) these fibres are rank-one vector spaces in degree one.
Apply [Stacks Lemma 36.31.3, Tag 0BDH](https://stacks.math.columbia.edu/tag/0BDH)
with i=1,r=1. The open locus where K is locally free of rank one
in degree one contains all closed points. Its closed complement
is empty because S is of finite type over C and every nonempty
closed subset contains a closed point. Consequently

\[
K\simeq G[-1],\qquad G=R^1\pi_*F\text{ is a line bundle},
\qquad R^i\pi_*F=0\ (i\ne1),\qquad \pi_![F]=-[G].      \tag{6}
\]

The fibre concentration, rather than perfectness or virtual rank
alone, is what licenses the finite-rank comparison. These general
theorems are imported, not reproved.

**Retain the full variable character.** With p=-5 and t=b+4,
L048 forces the character of any actual rank-two F in (2):

\[
\operatorname{ch}(F)
 =2-5e_1+t e_2+\tau_D+\frac{-5t+78}{6}P,
\qquad \operatorname{ch}_1(F)=\operatorname{ch}_3(F)=0.  \tag{7}
\]

Specifically, its full mixed square is tau_D^2=156P, comprising
36 from divisors and 120 from T. The pure/mixed cross terms
vanish by factor degree, e_1^2=e_2^2=0, and e_1e_2=P. Hence

\[
\operatorname{ch}_2(F)^2=(-10t+156)P,
\qquad \operatorname{ch}_4(F)
       =\operatorname{ch}_2(F)^2/12
       =\frac{-5t+78}{6}P.                              \tag{8}
\]

Thus no part of the transcendental square is discarded, and
the higher characters are forced afresh rather than inherited
from an earlier virtual K-class.

**Import and evaluate relative GRR for the whole slice.**
Use Fulton, *Intersection Theory*, second edition (1998),
[Theorem 15.2, pp. 286–287, and Example 15.2.8, pp. 291–292](https://djvu.online/file/87GFN2nbfbdF7).
The proper morphism pi between nonsingular projective varieties
satisfies its hypotheses. Its smooth relative formula, passed
through the rational cycle-class map, is

\[
\operatorname{ch}(\pi_![F])
 =\pi_*\bigl(\operatorname{ch}(F)\operatorname{td}(T_{X/S})\bigr).
                                                               \tag{9}
\]

Here T_{X/S}=p_1^*T_S and td(T_{X/S})=1+2e_1.
Only terms of degree four on the first surface survive pi_*.
In particular pi_*e_1=1, pi_*P=eta, while pi_*1,
pi_*e_2 and pi_*tau_D vanish. Also e_1 tau_D=0 and
e_1^2=0 by factor degree. Substituting (7) in (9) gives rank
4-5=-1, degree-two character zero (both ch_3 and ch_1 vanish),
and degree-four character

\[
\left(\frac{-5t+78}{6}+2t\right)\eta
 =\frac{7t+78}{6}\eta.
\]

The negative alternating sign in (6) therefore yields precisely
(3). There is no unaccounted mixed term in this pushforward;
the mixed class contributes through (8).

The evaluated substitution is required because the imported
general theorems do not decide the parameter-dependent finite-rank
compatibility. Their proofs are not reproduced here. The ready
SPECIALIZE assessment covers exactly this projection and slice.

**Compare with the line identity and retain the exceptional value.**
For any actual line bundle, ch(G)=exp(c_1(G)), the standard
identity in [Stacks Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM).
Equation (3) makes c_1(G)=0 in H^2(S,Q), so its second character
must be c_1(G)^2/2=0. Since eta has integral one, (3) forces
7t+78=0. Thus t=-78/7 and b=t-4=-106/7. Neither is integral,
contradicting the hypotheses. No stability or integral triviality
of G is needed for this contradiction.

For completeness, -5 is invertible modulo 12, with inverse 7.
The congruence in (1) therefore forces t=6 modulo 12 and
b=2 modulo 12. The bound b<=-9 makes the full set exactly
b=-10-12j, j an integer >=0. Substitution gives (4), whose
zero would require j=3/7. Thus every allowed coefficient is
excluded, including arbitrarily negative b; there is no missed
exceptional integer.

As a sign and index consistency check, (7) and the K3-product
Todd class give

\[
\chi(X,F)=8+2(-5+t)+\frac{-5t+78}{6}
         =11+\frac{7t}{6}=4-14j.
\]

Surface HRR applied to the hypothetical G in (3) gives
chi(S,G)=2-(7t+78)/6=-11-7t/6, whose negative agrees by
(6). These integral indices already passed the earlier filter;
the obstruction is the line character, not the scalar index.
All calculations are exact symbolic equalities, so no numerical
sampling or additional mathematical script is needed.

This completes only the stated integer slice exclusion. The
formal rational compatibility value has not been assigned a
bundle. Global realizations at larger factor charges, other
representatives, transverse transport, and universal primitive
Hodge algebraicity remain independent unresolved questions.

## Mathlib

Coverage of the full slice exclusion and of its coherent
base-change/relative-GRR inputs: **not checked**. No matching
declaration or absence from checked sources is asserted.
The directly linked Fulton and Stacks results supply the general
tools; L048 and L052 supply the full fixed-tensor character and
the coefficient-independent all-fibre restriction calculation.
This is a REPRODUCTION under the prior SPECIALIZE assessment,
with a new local exclusion and no certified originality or
Hodge resolution claim.
