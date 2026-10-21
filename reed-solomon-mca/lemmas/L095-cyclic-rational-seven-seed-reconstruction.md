# L095 — A different seven-seed choice has at most one cyclic completion

## Hypotheses

Use L092's full alternating-kernel setting: F=F_(97^20), H the
order-sixteen subgroup of F_97^*, a bijection h:Z/16Z -> H, unshifted
moment columns v_i=(1,h(i),...,h(i)^7), and blocks
B_s={s,s+1,s+4,s+6}. Write K for the common exterior quotient kernel.
Use L090's D_t and L091's S_t with their exact index conventions.
There are no actual-error, weight, locator or original-chart assumptions.
The input specializations L090–L094 passed their separate critical audits.

## Conclusion

Prescribing the seven labels at

    J'={0,1,3,5,7,8,9}

leaves at most one bijective labeling with K!=0. The same uniqueness
holds for labelings satisfying just D_1,D_10,D_15,S_8,D_8,D_3,D_2,D_0,D_4.
This uses simultaneous equations, not L091's stopped single-unknown
propagation procedure. It changes L092's seed set by exchanging indices
two and eight; it does not strengthen the bound for L092's original seeds.

Normalize exactly as in L092, sending h(0),h(7),h(5) to infinity,0,1.
All letters in the formulas below denote transformed labels. Put

    c=h(1), e=h(3), g=h(9), X=h(8).

The four further labels are forced rationally, in the following order:

    j=h(10)=c(1-g)/(1-c),
    t=j/[c(j-e)],
    Y=h(15)=j+t(X-j),
    A_*=(X+e-1)Y-eX,
    k=h(14)=eX(Y-1)/A_*,
    B_*=k+e-g-j,
    d=h(2)=(ke-gj)/B_*.                              (1)

At any admitted bijective solution every displayed denominator is
nonzero. Poles, transformed H-membership, the inverse-projectivity pole
and collisions remain rejection tests after every deduction. The five
remaining labels are forced by L092's D_8,D_3,D_2,D_0,D_4 deductions.
No existence, full-kernel sufficiency or uniform exclusion is asserted.

This gives a rational parametrization of the necessary reconstruction
by c,e,g,X, with no division by rho_1 or sigma_1. Thus all residual-zero
branches of L093/L094 remain represented. Their unused D_6,S_0 gates
can be tested directly by the two rational equations (5) below; their
simultaneous incompatibility on actual transformed H seeds remains open.
The actual-error application, arbitrary-family and challenge-definition
gaps remain, and the global 11/q–16/q interval is unchanged.

## Proof

### Scope and why the changed elimination is needed

The unchanged EXPLORE assessment in
`drafts/literature/2026-10-14-cyclic-family-alternating-kernel.md`
covers this analytic attempt. It imports no new external theorem and
makes no certified originality claim. L090/L091 give the necessary
gates; L092 gives their projective-coordinate justification and the
five final involution deductions. L093/L094 supply the two unused
gates only for the last reformulation below. The new calculation
eliminates the quadratic variable in a different order so that the
joint-gate question can be studied without residual-slope divisions.
It does not claim that the original joint factorization was completed.

The prescribed seeds contain all three labels defining L092's
projectivity T. It is therefore fixed before any deduction. It is not
a symmetry of H. Every label except the one at index zero has a finite
image under T, because the only pole is h(0). Distinctness of transformed
labels is equivalent to distinctness of the original labels. Only
members of T(H), pulled back by T^{-1}, are admissible.

### Simplifying the affine coefficient without excluding a branch

In any bijective solution, D_1 and D_10 give precisely L093's identities

    j=c(1-g)/(1-c),
    k=(de+gj-d(g+j))/(e-d).                         (2)

All of c,d,e,g,j,k are distinct finite labels avoiding zero and one.
In particular the following cancellations have nonzero denominators:

    j-g=(c-g)/(1-c),
    j-c=c(c-g)/(1-c),
    k-d=(d-g)(d-j)/(e-d),
    k-g=(d-g)(e-j)/(e-d).

The first two identities follow by substituting j; expanding (2)
gives the last two. Consequently L092's affine coefficient simplifies
uniformly on the admitted domain to

    t=j(j-g)(k-d)/((j-c)(j-d)(k-g))
     =j/[c(j-e)].                                  (3)

This is independent of d. No zero factor was discarded: c,g,j,d,e
refer to distinct indices, c!=0, and e!=d. Moreover j!=e and j!=0,
so (3) is finite and nonzero. L092's normalized S_8 is
Y=j+t(X-j). It therefore determines Y from the four given finite
seeds before d or k has been recovered. The case t=1 is retained.

### Recovering k and d with every denominator-zero case resolved

L092's normalized D_15 equation is

    ((k-e)X+k(e-1))Y=e(k-1)X.

Regrouping, without division, gives

    k A_*=eX(Y-1).                                 (4)

In a bijective solution e!=0, X!=0 and Y!=1, because the corresponding
indices three,eight,fifteen differ from seven,seven,five, respectively.
Thus the right side is nonzero. If A_*=0, (4) is impossible for any
finite k. Hence every admitted solution has A_*!=0 and its k is
exactly (1). This is not an open-chart assumption leaving an unexamined
branch; the zero-denominator branch contradicts distinctness.

Rearranging D_10 in (2), again without division, gives

    d(k+e-g-j)=ke-gj.

If B_*=k+e-g-j=0, substitute k=g+j-e. Then

    ke-gj=-(e-g)(e-j)!=0,

since e,g,j are distinct. This contradicts the rearranged equation.
Therefore B_*!=0 and d is exactly (1). The deduction does not assume
rho or sigma nonzero, and does not invert a quadratic discriminant.

Starting with J', first compute j. Reject it if it is inadmissible;
otherwise j!=e justifies (3). Compute and test Y, then compute and test
k and d, with the two impossible pole branches just proved. At this
point precisely the eleven indices

    {0,1,2,3,5,7,8,9,10,14,15}

are assigned. They are L092's known indices before its five final
deductions. D_8 gives h(12), D_3 gives h(11), D_2 gives h(6), D_0 gives
h(4), and D_4 gives h(13). In each step L090's involution is determined
by two disjoint label pairs. Its invertibility gives a unique projective
answer; an infinity value, a value outside T(H), or a repeated label
cannot yield a bijective completion. Thus every prescribed J' has at
most one admitted completion. K!=0 implies all the gates used, so the
same uniqueness holds for the full kernel target.

### The remaining joint test, without residual-slope divisions

For completeness the needed rational functions can be specified without
expanded multivariate numerators. With (1), put

    ell=c-k, m=k(c-X)/ell,
    n=de(g-m)/((d+e-m)g-de),
    A_2=c+d-X-j, B_2=Xj-cd,
    C_2=cd(X+j)-Xj(c+d),
    z=(-B_2 n-C_2)/(A_2 n+B_2).

These are exactly L093's h(12),h(11),h(6). Its proof shows every
denominator here is nonzero at any admitted reconstruction; the
denominators in the last two formulas correspond to O/ell and W/O.
All additional membership and collision tests remain required.

L093's direct D_6 determinant and L094's cleared S_0 equation are
therefore, respectively,

    G=z[j-k+(1-j)Y+(k-1)m]
        +jY(m+k-1)+mk(1-j-Y)=0,
    J=d(Y-X)(d-g)(d-j)(z-c)
        +(d-c)(z-j)(X-g)X(d-Y)=0.                  (5)

The S_0 denominator cleared is
X(d-Y)(d-g)(d-j)(z-c), all of whose factors are nonzero by distinctness.
Hence both tests are equivalent to those two gates on the admitted
domain. In L093/L094's notation G=E/(ell W) and J=P/W after evaluation
at (1). The reconstruction already satisfies Q(X)=0 as a consequence
of (3),(4) and (2), so these tests retain Delta,Psi,Xi's necessary
compatibility without solving either linear residual. In particular
rho=sigma=0 has not been excluded or mistaken for a contradiction.

Equations (5) are still only necessary gates for K!=0. No factorization,
uniform nonvanishing or actual-H obstruction for them is established
here. The unexpanded rational formulation and its complete pole check
are the partial result, not a solution of the full kernel problem.
The proof is algebraic; no numerical diagnostic or incomplete symbolic
expansion is an input.

### Separate critical audit — October 16, 2026, step 250

The pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-16-cyclic-rational-seven-seed-critical-audit.md`
covers exactly this audit. Full L095 and the needed audited L090–L094
gate, normalization and reconstruction passages were checked. No
mathematical defect was found. The verified conclusion is at most one
completion for J', even under the nine listed gates, together with the
necessary reformulations (5). This neither improves the original-seed
bound two nor asserts a solution, a sufficient gate test or uniform rank.

**Inputs and source scope.** The direct inputs remain L090/L091/L092/
L093/L094, with L089 and L010/L087/L088 retained through them. Reuse
Nguyen, [*Projective Line Revisited*](https://www.heldermann-verlag.de/jgg/jgg25/j25h2phat.pdf),
J. Geometry and Graphics 25(2) (2021), Section 2, pp. 188–189,
Proposition 1, p. 191, for projective involutions; characteristic 97
meets its characteristic-not-two hypothesis. Reuse Bobenko,
[*Projective Geometry*](https://page.math.tu-berlin.de/~bobenko/Lehre/Skripte/projective_part.pdf),
December 12, 2019, Definition 2.19, Remark 2.20, Lemma 2.21 and
Corollary 2.22, pp. 21–22, for arbitrary-field homogeneous cross-ratio
invariance, including infinity. L090/L092 already check these exact
cyclic involutions and normalizations. Reuse
[Stacks Project Proposition 10.9.3, tag 00CP](https://stacks.math.columbia.edu/tag/00CP)
for specialization of a localization when its inverted denominators
evaluate to units. The following checks establish that condition here;
none of these sources supplies the changed-index formulas by itself.
Their inspected coverage is reused, with no fresh source retrieval or
reproof of general projective or localization machinery.

**Changed seeds, indices and cancellations.** The three prescribed
labels at 0,7,5 fix T before any reconstruction. Its only pole on H is
h(0), and T^{-1}'s pole is outside T(H). Thus every other transformed
label of an actual bijection is finite and different from 0 and 1.
The D-template pairs are (s-1,s),(s+4,s+9),(s+6,s+8), modulo sixteen.
D_1 has pairs (infinity,c),(1,j),(0,g); its determinant is
(c-1)j+c(1-g), giving (2)'s j. D_10 has pairs (g,j),(k,e),
(infinity,d); its determinant is
gj-d(g+j)-ke+d(k+e), giving (2)'s k.

Subtracting g and c from j gives exactly the first two differences
printed above. Subtracting d and g from k gives numerators
(d-g)(d-j) and (d-g)(e-j), respectively, over e-d. Hence

    (j-g)/(j-c)=1/c,
    (k-d)/((j-d)(k-g))
       =(d-j)/((j-d)(e-j))=1/(j-e).

Every canceled factor is nonzero at an admitted labeling: 1-c, e-d,
c-g, c, d-g, d-j and e-j compare distinct assigned labels. Together
with j!=0 this proves exactly (3), including its sign and t!=0.
The use of d,k here is a necessary identity for any possible completion,
not a premature assignment of their values to arbitrary seeds.

For S_8, L091's first term becomes Y/j; the second becomes
(j-X)(j-g)(k-d)/((j-c)(j-d)(k-g)). Its infinity ratios equal one
homogeneously. Consequently S_8 is exactly Y=j+t(X-j). No factor
1-t is canceled or inverted; the saved t=1 case is retained. At this
stage j,Y depend only on the prescribed labels. A rejected image means
no completion; subsequent cancellations are used only on accepted
distinct values.

**Both exceptional branches.** D_15 has pairs (k,Y),(e,X),(1,0).
Expanding gives the displayed equation preceding (4). Moving its
terms, its coefficient of k is (X+e-1)Y-eX=A_* and its other side
is eX(Y-1). The latter is nonzero since indices 3,8,15 differ from
the indices carrying 0,0,1. Thus A_*=0 has no finite solution k;
A_*!=0 forces the stated k, which must then pass all label tests.
D_10 rearranges to dB_*=ke-gj without division. If B_*=0 then
k=g+j-e and ke-gj=-(e-g)(e-j)!=0. This excludes that branch without
assuming any residual slope. Otherwise d is forced and tested. No
unexamined infinite k or d remains: index zero already carries infinity.

**The five final deductions.** The assigned index set is now exactly
{0,1,2,3,5,7,8,9,10,14,15}. The following is the direct template check:

| Gate | Two known pairs | Remaining pair | Forced index |
| --- | --- | --- | --- |
| D_8 | (7,8), (14,0) | (12,1) | 12 |
| D_3 | (2,3), (7,12) | (9,11) | 11 |
| D_2 | (1,2), (8,10) | (6,11) | 6 |
| D_0 | (15,0), (6,8) | (4,9) | 4 |
| D_4 | (3,4), (10,12) | (8,13) | 13 |

Each row has six distinct indices, and previous accepted deductions
make the two known pairs disjoint. L090's unique invertible involution
therefore applies in the original finite coordinates; conjugation by T
handles the rows containing normalized infinity. Each possible image
is checked for T(H)-membership, inverse-map finiteness and collision
with every assigned label. Thus each stage leaves at most one choice,
independently of unused gates or K. This verifies the stronger nine-gate
uniqueness assertion as well as its consequence for K!=0.

**Rational functions and the two unused gates.** D_8's involution
exchanges 0,X and infinity,k, so m=k(c-X)/(c-k), with ell=c-k!=0.
D_3's map is v -> de(v-m)/((d+e-m)v-de); its determinant is
-de(d-m)(e-m)!=0. This includes d+e-m=0. Its denominator at g is
O/ell, and its numerator de(g-m) is nonzero. Thus O=0 would send g
to infinity and is rejected. The D_2 map has coefficients A_2,B_2,C_2
as printed, with A_2 C_2-B_2^2!=0 by its disjoint pairs. Substitution
n=N/O gives z=Z/W. Its denominator is W/O; invertibility ensures
(Z,W)!=(0,0), so W=0 also forces the forbidden infinity. This verifies
all three saved expressions without omitting an affine or zero-pole case.

D_6 has pairs (1,z),(j,Y),(m,k). Direct expansion of its three pair
rows is

    z[(j+Y-m-k)-jY+mk]
       -jY+mk+jY(m+k)-mk(j+Y),

which is exactly G in (5). Substitution m=M/ell,z=Z/W gives
ell W G=ZU+WV=E, with ell W!=0. S_0, using L091 at index zero,
is Y(d-X)/(X(d-Y))+(d-c)(z-j)(X-g)/((d-g)(d-j)(z-c))=1.
Subtracting one from its first summand gives d(Y-X)/(X(d-Y)).
Multiplication by X(d-Y)(d-g)(d-j)(z-c) gives exactly J, with both
plus signs in (5). Every factor is nonzero by distinctness. Replacing
z by Z/W gives WJ=P, with W!=0. Thus both gate equivalences are
reversible on the stated admitted domain; clearing has added no branch.

**Original-seed polynomials and zero residuals.** For any admitted
changed-seed reconstruction, freeze its recovered c,d,e,g and use a
fresh polynomial indeterminate U in L092–L094. Their denominators
are nonzero by the checks above, and q_2=(k-e)t!=0. Their Q(U), E(U),
P(U) and remainder identities therefore specialize legitimately.
The prescribed X is an evaluation point, not a replacement seed
variable when taking these remainders. Equations (2)–(4) give

    Q(X)=((k-e)X+k(e-1))(tX+j(1-t))-e(k-1)X=0.

The D_15 denominator cannot vanish there: its numerator e(k-1)X
is nonzero. When the two extra gates hold, E(X)=P(X)=0, hence
rho_0+rho_1 X=sigma_0+sigma_1 X=0. Eliminating X from these equalities
with Q gives the already audited necessary Delta,Psi,Xi conditions,
with no new division by either slope. In particular if all four
residual coefficients vanish, both remainder equations impose no
further restriction, and the changed-seed rational construction still
covers that possible completion. It asserts neither existence of this
branch nor contradiction. There is no claim that substituting the
rational d(X) preserves a quadratic degree in the changed seed X.

No numerical certificate is required by this proof. The incomplete
expansion and stopped joint-gate calculation in ATTEMPTS/033–034 are
not inputs and were not rerun. No mathematical statement or direct
dependency changed in this audit. Uniform rank, rank-27 existence,
arbitrary families and challenge qualifications remain unresolved;
the global interval is still 11/q–16/q. This is verification of a saved
local restriction, not a new theorem beyond the sources checked.

## Mathlib

Full matching coverage for this cyclic rational reconstruction has not
been checked. No absence or formal-verification claim is made. The
source assessment's exterior-algebra inputs remain unchanged; the
elementary identities, exceptional cases and specialized gate uses
needed here are written out above. The separate step-250 audit found
no mathematical defect; it supplies no formal-verification claim.
