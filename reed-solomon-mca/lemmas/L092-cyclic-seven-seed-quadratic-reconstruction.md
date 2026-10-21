# L092 — Seven cyclic seeds admit at most two reconstructions

## Hypotheses

Use L089's setting: F=F_(97^20), H the order-sixteen subgroup of
F_97^*, a bijection h:Z/16Z -> H, and the full alternating kernel K
for the blocks B_t={t,t+1,t+4,t+6}. Indices are modulo sixteen.
Use D_t for L090's necessary third-gate determinant and S_t for
L091's necessary second gate. No actual errors, original finite chart,
error weights or locator assumptions are imposed.

## Conclusion

For any prescribed distinct seed labels at

    J={0,1,2,3,5,7,9},

there are at most two bijective labelings with K!=0 extending those
seeds. In fact the same bound holds for bijective labelings satisfying
only D_1,D_10,D_15,S_8,D_8,D_3,D_2,D_0,D_4. Each extension is obtained
by two single-label deductions, solving one genuine quadratic over
F_97, and five further single-label deductions. Every recovered value
must still pass all finite-label, H-membership and distinctness tests.

This overcomes L091's obstruction to the specified single-label-only
procedure by permitting a simultaneous two-label step. It supplies
neither an extending labeling nor uniform zero kernel. Every unused
gate and the full rank R test remain necessary. Rank R>=3, actual-error
applicability, arbitrary-family coverage and the global 11/q–16/q
interval remain unresolved. L090/L091 passed their separate audits;
this result passed the separate step-244 audit recorded below.

## Proof

### Inputs and the exact gate specialization

This is one analytic elimination on the unchanged target covered by
`drafts/literature/2026-10-14-cyclic-family-alternating-kernel.md`.
The earlier source comparison remains adequate; no external theorem
is newly imported or reproved. L090 supplies D_t and its unique
single-label recovery, and L091 supplies S_t. Their load-bearing
reductions can be checked directly against audited L089: for adjacent
circuit windows the ratio of coefficients at label l is
(l-h(t+8))/(l-h(t-1)) in the backward direction and
(l-h(t))/(l-h(t+9)) in the forward direction. The two-step forward
ratio is (l-h(t))(l-h(t+1))/((l-h(t+9))(l-h(t+10))).
All factors used in these ratios are nonzero by bijectivity.
Substitution in L089's second shared gate gives exactly S_t in L091;
its first normalized term is
(q-e)(z-a)/((q-a)(z-e)), and its second is
(q-b)(q-x)(d-k)(e-f)/((q-f)(q-k)(d-x)(e-b)), with precisely
L091's notation. For the third gate the two normalized terms are

    (d-e)(c-a)/((d-a)(c-e)),
    (d-b)(e-f)/((d-f)(e-b)).

Their sum being one is equivalent to
P(d)Q(e)-P(e)Q(d)=0, for P=(Z-a)(Z-b), Q=(Z-c)(Z-f).
Expansion gives (d-e) times D_t. Thus the necessary gates used here
have the original unshifted circuit convention. These checks do not
constitute a separate critical audit of either entire input lemma.

Write the assigned labels, before any change of coordinates, as

    b=h(0), c=h(1), d=h(2), e=h(3), f=h(5),
    p=h(7), g=h(9), j=h(10), k=h(14),
    X=h(8), Y=h(15).

D_1 has pairs (b,c),(f,j),(p,g). The two known disjoint pairs
(b,c),(p,g) determine their unique invertible involution by L090;
its image of f uniquely gives j. D_10 then has pairs
(g,j),(k,e),(b,d), so its two known pairs (g,j),(b,d) give k as
the unique image of e. If either deduction is a pole, outside H or
repeats an assigned label, no bijective extension exists. Otherwise
these nine labels are distinct fixed members of F_97.

At these labels D_15 has pairs (k,Y),(e,X),(f,p), while S_8 is

    (j-b)(Y-p)/((j-p)(Y-b))
      +(j-X)(j-g)(k-d)(b-c)/
          ((j-c)(j-d)(k-g)(b-X)) = 1.                  (1)

Every denominator is nonzero at a bijective extension. This is a
two-unknown system, with no assumption that either equation suffices
for K!=0.

### Coordinate normalization is only an algebraic device

Apply the projective transformation over F_97

    T(z)=(z-p)(f-b)/((z-b)(f-p)),

which sends b to infinity, p to zero and f to one. Its determinant
is nonzero since b,p,f are distinct. All other labels of a bijective
extension have finite, distinct transformed values. In the rest of
this paragraph and the next two, the same letters mean the transformed
values. Thus b=infinity, p=0, f=1, and c,d,e,g,j,k are distinct
finite elements, none equal to zero or one. X,Y are likewise finite
and distinct from all assigned labels and each other.

This transformation need not preserve H. At the end candidates are
tested in the transformed set T(H) and pulled back by T^{-1}; it is
not a claimed symmetry or normalization of the subgroup-label problem.

The common-involution formulation of D_15 is preserved under
conjugation by T, so its determinant still vanishes. All six labels
in D_15 are finite after T. Equation (1) is preserved as well:
its first summand is a cross ratio, and its second is the product

    [(j-X)(b-c)/((j-c)(b-X))]
    [(j-g)(k-d)/((j-d)(k-g))].

Each factor is invariant under a common projective transformation.
For finite nonpole arguments this follows immediately from
T(u)-T(v)=det(T)(u-v)/((C u+D)(C v+D)); cancellation gives the
same identity on P^1 whenever the original cross-ratio denominators
are nonzero. In particular the factors involving b=infinity are
evaluated projectively, by cancelling their common b coefficients.
No choice of finite characteristic limit is being invoked.

### A genuine quadratic, with no coincident-map branch

In the transformed coordinates D_15 is

    det [[kY,k+Y,1],[eX,e+X,1],[0,1,1]]=0,

or, after expansion,

    ((k-e)X+k(e-1))Y=e(k-1)X.                         (2)

Put

    alpha=e(k-1), beta=k-e, gamma=k(e-1).

All three are nonzero, since e,k,0,1 are distinct. Thus (2) is the
graph of the invertible projectivity Y=alpha X/(beta X+gamma),
with a genuine finite pole at -gamma/beta. At this pole its right
side numerator is nonzero. Equivalently (2) has no finite Y there.
This also follows from the disjoint-pair involution test; no singular
involution has been allowed.

In the same coordinates (1) becomes

    Y/j+C(j-X)=1,
    C=(j-g)(k-d)/((j-c)(j-d)(k-g)).                    (3)

The coefficient C is nonzero and finite, and j!=0. Define

    t=j C, u=j(1-t).

Then t!=0 and (3) is the invertible affine relation Y=tX+u.
The case u=0 is allowed. Combining with (2) gives exactly

    Q(X)=beta t X^2+(beta u+gamma t-alpha)X+gamma u=0. (4)

Its leading coefficient beta t is nonzero for every admitted seed
assignment, including those for which u=0. Consequently Q is a
polynomial of degree exactly two, not an identity or a degree-drop
branch. The two projectivities cannot coincide: (2) has a finite
pole, whereas (3) is affine with nonzero slope.

There are at most two roots of Q in F_97, because a nonzero degree-two
polynomial over a field has at most two distinct roots. Multiple roots,
a nonsquare discriminant and roots outside the admitted label set only
decrease the number. Even over F there are at most two roots; only
F_97 roots in T(H) could come from the required labelings.

For completeness no denominator root was spuriously added in (4):
at X_0=-gamma/beta,

    Q(X_0)=-alpha X_0=alpha gamma/beta !=0.

For every root of (4) the finite value Y=tX+u therefore satisfies
(2), hence the normalized D_15 equation. Conversely any finite pair
satisfying (2),(3) gives a root of (4). This proves the precise
two-equation correspondence before label restrictions. Discard any
root for which X or Y is outside T(H), equals a used value or equals
the other. In particular T^{-1}'s pole is inadmissible: it is not
in T(H), since the original infinity does not belong to H. Pulling
back the survivors gives at most two possible original ordered pairs
(h(8),h(15)). All original gate denominators are then again nonzero.

The prior gates D_1,D_10 were used only to determine j,k, not to
assume any extra relation when proving beta t!=0. Thus no hidden
exception to the quadratic bound is created by those deductions.

### Each admitted pair determines the remaining five labels

After any admitted pair, the known abstract indices are
{0,1,2,3,5,7,8,9,10,14,15}. Apply the following D gates in order:

| Gate | Fully known pairs | Pair with one unknown | New index |
|---|---|---|---|
| D_8 | (7,8), (14,0) | (12,1) | 12 |
| D_3 | (2,3), (7,12) | (9,11) | 11 |
| D_2 | (1,2), (8,10) | (6,11) | 6 |
| D_0 | (15,0), (6,8) | (4,9) | 4 |
| D_4 | (3,4), (10,12) | (8,13) | 13 |

In every row the six abstract indices are distinct and the two known
pairs have four distinct finite labels. L090's involution therefore
gives a unique projective value for the unknown. Reject poles,
values outside H and repetitions immediately. Each admitted pair
has at most one bijective completion, proving the bound two.

All other D/F/S gates and rank R=2 must still be tested for a completed
labeling; no sufficiency is asserted. No assignment has been enumerated,
no rank has been sampled and no certificate is needed for this algebraic
proof. The result is a local restriction within the source-assessed
target, not certified originality or progress beyond all literature.

### Separate critical audit — October 16, 2026, step 244

The pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-15-cyclic-quadratic-reconstruction-critical-audit.md`
covers precisely this audit. Full L092 and the relevant definitions,
gate formulas and separate audits of L089/L090/L091 were checked.
No mathematical defect was found. This verifies the existing conditional
bound, without establishing existence, sufficiency or uniform rank.
There is no numerical certificate obligation for this analytic proof.

**Inputs and cited machinery.** L089's unshifted circuit convention and
necessary shared gates, L090's determinant and unique involution, and
L091's second-gate equation are the direct mathematical inputs.
The closure census in L091 is motivation only; its bound nine is not
needed to prove this bound two. L010/L087/L088 enter through the audited
inputs. No L093–L096 conclusion, actual-error hypothesis or rational
original chart is used. K!=0 is used only to obtain the necessary gates;
the stronger gate-only assertion is checked independently below.

For projective invariance import Alexander I. Bobenko,
[*Projective Geometry*](https://page.math.tu-berlin.de/~bobenko/Lehre/Skripte/projective_part.pdf),
draft December 12, 2019, Definition 2.19, Remark 2.20 and Lemma 2.21
with its determinant proof, printed pp. 21–22. Remark 2.20 permits
arbitrary fields, and the homogeneous definition includes infinity.
The displayed cross-ratio factors here are ordered instances of that
definition, so its invariance applies over F_97 and F_(97^20).
For the distinct-root bound import J. S. Milne,
[*Fields and Galois Theory*](https://www.jmilne.org/math/CourseNotes/FT.pdf),
v5.10, September 2022, Sections 1.6–1.7, printed p. 10.
It needs only a nonzero polynomial over a field, with no separability
assumption. These sources were inspected in step 243 and are reused;
the following local checks fix the cyclic substitution and exceptional
branches, rather than reprove either general theorem.

**Initial deductions and S_8.** The D_t pair template is
{t-1,t}, {t+4,t+9}, {t+6,t+8}, modulo sixteen. At t=1 it is
{0,1}, {5,10}, {7,9}; at t=10 it is {9,10}, {14,3}, {0,2}.
Thus the first deduction adds precisely j=h(10), and the second adds
k=h(14), each using five distinct known labels. Audited L090 handles
both affine involutions and finite poles. A rejected image means zero
extensions, while acceptance gives nine fixed distinct F_97 labels.
At t=15 the pairs are {14,15}, {3,8}, {5,7}, as asserted.

For S_8, L091's symbols (a,b,x,q,d,z,e,f,k) become, in L092's
pre-normalization notation, (p,X,g,j,k,Y,b,c,d). Substitution gives
exactly (1). Its denominator factors are j-p, Y-b, j-c, j-d, k-g,
b-X, each nonzero for a bijection. The displayed circuit-window
ratios agree with L089's reciprocal products and the audited L090/L091
reductions; there is no shifted-moment or sign change in this use.

**Projective normalization, including infinity.** A matrix for T is

    [[f-b, -p(f-b)], [f-p, -b(f-p)]],

with determinant (f-b)(f-p)(p-b), nonzero by the original distinctness.
Its unique pole is the original b. Hence b alone becomes infinity,
p becomes zero, f becomes one, and every other admitted label remains
finite and distinct. D_15 is preserved through conjugation of its
common involution; its six labels omit b and are all finite afterwards.
For S_8 the first summand and both factors of the second summand are
cross ratios with nonzero homogeneous denominators. Setting the
representative of transformed b to (1,0) makes the first summand Y/j
and the b-dependent factor (j-X)/(j-c). The other factor stays
(j-g)(k-d)/((j-d)(k-g)). Thus (3) follows, without a limit argument
or a new denominator-zero branch at infinity.

This projectivity need not preserve H. Its inverse pole is T(infinity),
computed from the original labels as (f-b)/(f-p). It cannot belong to T(H), by
injectivity and infinity not belonging to H. Transformed infinity is
T(b), already assigned, so it too is excluded for X,Y. Testing finite
X,Y in T(H), excluding all assigned labels and their mutual collision,
therefore restores exactly the required original finite label domain.

**Quadratic and every denominator branch.** Direct expansion of the
normalized D_15 determinant is

    kY(e+X-1)-eX(k+Y-1)
      = ((k-e)X+k(e-1))Y-e(k-1)X.

This verifies (2) with the stated signs. The quantities alpha=e(k-1),
beta=k-e, gamma=k(e-1) are nonzero because e,k,0,1 are distinct.
The fractional-linear matrix [[alpha,0],[beta,gamma]] has determinant
alpha gamma!=0 and finite pole X_0=-gamma/beta!=0. At this pole
alpha X_0 is nonzero, so there is no finite solution of (2).

In (3), the factors j-g, k-d, j-c, j-d, k-g and j are nonzero.
Consequently C and t=jC are nonzero. Solving (3) gives
Y=j-jC(j-X)=tX+j(1-t), exactly the stated u=j(1-t).
Substituting in (2) yields

    (beta X+gamma)(tX+u)-alpha X = Q(X).

The leading coefficient beta t is nonzero for every accepted initial
assignment, not just generically. There is no degree-drop case.
At X_0 the polynomial is alpha gamma/beta, nonzero. Thus multiplying
by the fractional-linear denominator has introduced no root there;
every Q root yields exactly one finite Y satisfying both normalized
equations, and every finite pair satisfying them is obtained this way.
This correspondence precedes, and does not replace, the label tests.

If u=0, Q=X(beta t X+gamma t-alpha) still has degree two; its zero
root collides with the assigned label p and is rejected. Repeated roots
are counted once; a nonsplit polynomial has no F_97 roots; extension
roots outside F_97 cannot be labels in T(H). Any root yielding a used
label, X=Y, an inverse pole or a non-H pullback is rejected. Milne's
bound therefore gives at most two admitted ordered pairs in all cases.
No discriminant or affine intercept is inverted. The two earlier D
equations impose no additional assumption needed for nonvanishing.

**Final deductions and counting.** Checked against the same D template,
the five successive rows use precisely these known indices and outputs:

    D_8: known 7,8,14,0,1;  output 12;
    D_3: known 2,3,7,12,9; output 11;
    D_2: known 1,2,8,10,11; output 6;
    D_0: known 15,0,6,8,9; output 4;
    D_4: known 3,4,10,12,8; output 13.

In each row the two fully known pairs are disjoint and its fifth known
label is distinct. All are seeds or earlier accepted outputs. L090
therefore forces a unique projective image; infinity, a collision or
failure of H membership rejects that branch. The five output indices
are exactly the remaining indices. Induction gives at most one full
bijection per admitted pair. Every full bijection satisfying the nine
specified gates follows this reconstruction and survives its rejection
tests. Hence their number is at most two; K!=0 labelings form a subset.
Unused gates and rank R remain untested, so no existence or sufficient
criterion is inferred. This audit changes neither the theorem nor its
direct dependencies and does not reopen ATTEMPTS/032–034.

## Mathlib

Full matching coverage for this cyclic two-label elimination and
seven-seed branching reconstruction has not been checked. No absence
or formal-verification claim is made. The inputs are L089's audited
moment gates and the separately audited specializations in L090/L091.
The projective-coordinate and quadratic calculations required for this
particular specialization are written out above and checked in step 244.
The cited standard results are informal source inputs; no full matching
Mathlib theorem or formal verification has been asserted.
