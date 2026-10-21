# L072 — Direct image excludes the sign-reversed five-charge slice

## Hypotheses

Retain L071's marked smooth projective complex K3 surface S, its real
Kähler class h and the identical common hyperkähler metric on
X=S x S. Put Omega=p_1^*h+p_2^*h. Write eta for the integral
point class, integral_S eta=1, e_1=eta tensor 1, e_2=1 tensor eta,
and P=e_1e_2. Retain its full integral mixed class tau_D, with
q-self-adjoint operator D and tau_D^2=156P (36 from divisors and
120 from the transcendental part).

Let b be any integer satisfying

\[
b\leq-9,\qquad -5(b+4)\equiv6\pmod{12}.                 \tag{1}
\]

Suppose F is a rank-two locally free holomorphic bundle on X,
slope-polystable at Omega, with

\[
c_1(F)=0,\qquad \operatorname{ch}_2(F)=-5e_1+(b+4)e_2-\tau_D.
                                                               \tag{2}
\]

Initial higher characters and the K-class are unrestricted. Neither
a presentation, equivalence, direct-image stability nor transverse
transport is assumed. The prescribed mixed tensor has the opposite
sign to L055's hypotheses; that exclusion is not imported verbatim.

## Conclusion

No such F exists for any integer b in (1). An actual F would give
a line bundle G=R^1p_2*F with

\[
\operatorname{ch}(G)=1-\frac{7b+106}{6}\eta,\qquad c_1(G)=0.
                                                               \tag{3}
\]

The line character identity requires b=-106/7, which is nonintegral.
The entire admitted domain is b=-10-12j, j an integer >=0, and
its forced second character is (14j-6)eta, never zero.

This is a NEGATIVE / REPRODUCTION application of previously assessed
base-change and GRR tools to changed data. It excludes this holomorphic
product-bundle recipe; it preserves L071's topological realization and
does not imply nonalgebraicity of a rational Hodge class. Larger charges,
other representatives, gluing and transverse transport remain open.
The separate critical audit below preserves this exact exclusion;
it finds no substantive defect or stronger conclusion.

## Proof

**Every-fibre cohomology uses the changed-sign input.** For each closed
y in S, put j_y(z)=(z,y) and E_y=j_y^*F. L071 proves for these exact
negative-mixed data that E_y is locally free and slope-polystable at
h, with c_1=0 and c_2=5. Its proof first establishes stable product F,
then imports the invariant connection and restricts its actual
curvature at every factor embedding. We use that established passage,
not ordinary restriction stability or L052's positive-sign hypotheses.

L071's exact-metric split alternative has charge 14r^2 for integer r.
Five is not such a value, so every E_y is stable. Its section/dual
stability and K3 Serre-duality argument gives H^0(E_y)=H^2(E_y)=0.
Surface RR gives chi(E_y)=4-5=-1, hence h^1(E_y)=1. There is no
cohomology above degree two. These facts hold at every closed fibre
independently of b; no stability of the opposite restrictions is needed.

**Import perfect base change and concentration.** By Serre's GAGA
theorem F is an algebraic vector bundle with the same fibre cohomology.
The projection pi=p_2 is smooth projective of finite presentation.
F[0] is bounded coherent, flat over the base and has proper support;
O_X is perfect. Thus
[Stacks Lemma 36.30.1, Tag 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
makes K=Rpi_*F perfect and compatible with arbitrary derived base change.
Its derived fibre at each closed y is R Gamma(S,E_y), a rank-one
vector space concentrated in degree one.

Apply [Stacks Lemma 36.31.3, Tag 0BDH](https://stacks.math.columbia.edu/tag/0BDH)
with i=1 and r=1. The open concentration locus contains every closed
point. Its closed complement is empty since a nonempty closed subset
of the finite-type complex variety S has a closed point. Consequently

\[
K\simeq G[-1],\qquad G=R^1\pi_*F\text{ is a line bundle},
\qquad R^i\pi_*F=0\ (i\ne1),\qquad \pi_![F]=-[G].       \tag{4}
\]

These general theorems are imported without reproof. Perfectness or
virtual rank alone would not establish the actual line bundle.

**Keep the full changed character.** Put t=b+4. L071's forced
rank-two character, unrestricted initially, is

\[
\operatorname{ch}(F)=2-5e_1+t e_2-\tau_D
                        +\frac{-5t+78}{6}P,
\qquad \operatorname{ch}_1(F)=\operatorname{ch}_3(F)=0.    \tag{5}
\]

Indeed e_i tau_D=0 and e_i^2=0 by factor degree, so the full
second-character square is (-10t+156)P. Both mixed-square
contributions survive sign reversal. Rank truncation with c_1=0
forces ch_4=ch_2^2/12, not ch_4=0. Equation (5) uses L071's
changed-sign conclusion, not an old virtual K-class.

**Import and evaluate relative GRR.** Use Fulton, *Intersection
Theory*, second edition (1998),
[Theorem 15.2, pp. 286–287, and Example 15.2.8, pp. 291–292](https://djvu.online/file/87GFN2nbfbdF7).
The linked scan's host labels it 1997; the edition citation follows
the saved assessment. The proper projection is between nonsingular
projective varieties and F is locally free. Its smooth relative
formula in rational cohomology, via the cycle-class map, is

\[
\operatorname{ch}(\pi_![F])
 =\pi_*\bigl(\operatorname{ch}(F)\operatorname{td}(T_{X/S})\bigr).
                                                               \tag{6}
\]

Here T_{X/S}=p_1^*T_S, so td(T_{X/S})=1+2e_1. Only first-factor
degree four survives pi_*: pi_*e_1=1, pi_*P=eta, while pi_*1,
pi_*e_2 and pi_*tau_D vanish. Also e_1 tau_D=0. Thus the changed
linear mixed term contributes neither directly nor via the Todd
product; its square has already been retained in (5). Substitution
gives rank 4-5=-1, zero degree-two character and degree-four character

\[
\left(\frac{-5t+78}{6}+2t\right)\eta
 =\frac{7t+78}{6}\eta.
\]

The negative alternating sign in (4) yields (3). This explicitly
justifies why L055's general mechanism has the same numerical
output for the opposite tensor. Its old sign-specific hypotheses
are not used to establish (4). The general GRR theorem is imported;
the substitution is necessary since it does not decide this slice.

**Compare the actual finite rank and the complete integer domain.**
For a line bundle ch(G)=exp(c_1(G)), as in
[Stacks Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM).
Equation (3) gives c_1(G)=0 in rational cohomology, so
ch_2(G)=c_1(G)^2/2=0. Because integral_S eta=1, it forces
7t+78=0, hence t=-78/7 and b=-106/7. This contradicts integrality.
No stability or integral triviality of G is required. The rational
exception is only formal character compatibility, with no realization.

To check the entire domain rather than a finite sample, -5 has
inverse 7 modulo 12. Thus (1) gives t=6 modulo 12 and b=2
modulo 12. The bound b<=-9 gives exactly b=-10-12j, j>=0.
Equation (3) becomes ch(G)=1+(14j-6)eta. Its vanishing second
character would require j=3/7, not a nonnegative integer.

As an independent alternating-index consistency check, (5) with
td(X)=1+2(e_1+e_2)+4P gives

\[
\chi(X,F)=8+2(-5+t)+\frac{-5t+78}{6}
         =11+\frac{7t}{6}=4-14j.
\]

Surface RR gives chi(S,G)=2-(7t+78)/6=-11-7t/6, whose
negative agrees with (4). These indices are integers, so the
obstruction is the line character rather than the old scalar index
filter. All equalities are exact; no mathematical script or numerical
scan is needed. This completes only the approved slice test.

**Separate critical audit, 2026-10-08.** Under the prior SPECIALIZE
audit assessment, the following independent checks preserve the
statement. This audit is REPRODUCTION with outcome EXPLORATION:
verification found no substantive error to repair, no new exclusion
and no existence conclusion.

The hypotheses match L071 exactly with a=-9. In particular the
mixed class is the full integral -tau_D, and both factors carry the
same metric; neither a rational replacement polarization nor the
positive-sign restriction conclusion of L055 is used. L071 first
excludes the product's two-line alternative by its nonzero mixed
action on sigma, then obtains an invariant unitary connection from
the cited Verbitsky Theorem 3.9. Equivariance of every factor
embedding preserves that actual curvature's invariance. Surface
zero contraction and the real-metric Hermite--Einstein correspondence
therefore give every-fibre polystability. This bridge does not
deduce restriction stability from product stability alone.

At charge five the only nonstable polystable possibility would
have charge 14r^2, by the exact-metric lattice imported in L071;
there is no such integer r. A nonzero section of the resulting
stable slope-zero rank-two fibre would inject O_S with equal
slope, contradicting stability. The same argument on the stable
dual, with K_S trivial and Serre duality, kills H^2. K3 RR gives
chi=-1 and h^1=1. This verifies all closed fibres, with no condition
on stability in the opposite projection.

For the derived step, GAGA preserves local freeness and fibre
cohomology. Smoothness of pi makes O_X base-flat, and local freeness
makes F base-flat. Properness, finite presentation and coherence
put O_X and F[0] within the cited Stacks 0A1H hypotheses. Thus the
derived fibres of the perfect K are the actual fibre cohomologies.
Stacks 0BDH applies to degree one and rank one; its concentration
locus is open, and a nonempty closed complement on S would contain
a closed complex point. The complement is therefore empty. A complex
with just this one cohomology sheaf is G[-1], so the sign in K-theory
is negative. No inference from constant Euler characteristic, virtual
rank or generic-fibre information replaces this argument.

Independently expand the full square using the factor bidegrees:
e_1 and e_2 have degrees (4,0) and (0,4), while every summand of
tau_D has degree (2,2). The pure squares and pure/mixed products
vanish; the cross product is -10tP and the mixed square is 156P.
The latter is L071's audited 36+120, not just its divisor part.
For actual rank two, c_3=c_4=0 and c_1=0 force ch_3=0 and
ch_4=(-10t+156)P/12. In particular sign reversal cannot change
that term, and unrestricted initial higher characters cannot
serve as adjustable parameters.

The integrand for relative GRR, with A=(-5t+78)/6, is exactly
2-e_1+t e_2-tau_D+(A+2t)P. Its first-factor degree-four
part is -e_1+(A+2t)P. There is no bidegree (4,2) term to produce
a first character on the base. Thus ch(K)=-1+(7t+78)eta/6,
and ch(G)=1-(7t+78)eta/6 with rational c_1(G)=0. This also
checks that no ambient Todd factor or surviving linear mixed term
has entered the calculation. The cited smooth-proper GRR hypotheses
hold for the actual algebraic projection and bundle; the general
theorem needs no new proof or mixed-sign assumption.

Finally a line with rational c_1=0 has ch_2=0 even without invoking
Picard torsion-freeness or image stability. This forces t=-78/7.
Solving the original congruence gives t=6 modulo 12, and the bound
t<=-5 gives exactly t=-6-12j for all integers j>=0. The second
character is then (14j-6)eta, nonzero throughout that infinite set.
The independent total Euler values are chi(X,F)=4-14j and
chi(S,G)=14j-4, consistent with the alternating sign and showing
why an integer scalar index alone misses the contradiction.

All required bounds and identities have been checked symbolically;
there is no sampling-based inference or uninspected certificate.
The direct mathematical input remains L071; L055 is only a method
comparison. The audit preserves topological realization and the
scope restrictions on rank, local freeness, product polystability,
the fixed metric and the full tensor. It supplies neither a new
cycle nor a conclusion about larger charges or transverse transport.

## Mathlib

Full changed-sign slice exclusion and supporting coherent base-change
and relative-GRR coverage: **not checked**. No declaration match or
absence is asserted. The precise cited primary tools and L071's
canonical full-character/every-fibre input supply this informal
REPRODUCTION under the prior SPECIALIZE assessment. The local exclusion
is no claim of progress beyond those sources or a Hodge resolution.
