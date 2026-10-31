# Lemma 569: absolute compensation at a multiple zero

## Hypotheses

Let a be real and let F be a nonzero real analytic function on an open
real interval containing a. Suppose a is a zero of exact finite
multiplicity m>=2. Let P and R be real analytic there with F=P+R.
For any twice differentiable real function h define

    D(h)=h'^2-h h'',
    B(P,R)=2P'R'-P R''-R P''.

The predicate to be audited is, at a only,

    D(P)(a)>=|B(P,R)(a)|+|D(R)(a)|.                 (1)

Put c=F''(a), x=P(a), y=P'(a), z=P''(a), and A=y^2-xz.
Exact multiplicity implies F(a)=F'(a)=0; c!=0 if m=2 and c=0
if m>=3. No Laguerre-Polya membership, simplicity, nonvanishing
truncation jet, Xi realization, or restriction on the sign of c is
assumed. The real triples (x,y,z) are initially arbitrary.

L564 fixes the actual Hermite normalization and supplies absolute
C^2 tail bounds; L568 records the full mixed-plus-quadratic expansion
for those actual remainders. Those facts motivate the test, but their
coefficient certificates and analytic estimates are not mathematical
premises of the arbitrary-jet result below. In an actual application,
one would take F=Xi, P=P_N and R=Xi-P_N with precisely L564's cutoff.
No such application or multiple Xi zero is asserted here.

## Conclusion

For every fixed allowed c, (1) holds if and only if

    A>=0 and -2A<=cx<=-A.                           (2)

Consequently the complete classification is as follows.

* If m=2, hence c!=0, the admissible triples are exactly

      x=0, y=0, z arbitrary,

  together with

      cx<0 and -cx/2<=y^2-xz<=-cx.

  There are no admissible triples with cx>0. In the second case,
  cx=-2A gives B(P,R)(a)=0 and D(R)(a)=-A; cx=-A gives
  B(P,R)(a)=-A and D(R)(a)=0. Both are included. At the first
  branch A=B(P,R)(a)=D(R)(a)=0.
* If m>=3, the admissible triples are exactly

      y^2=xz.

  All three contributions D(P)(a), B(P,R)(a), D(R)(a) then vanish.

Whenever (1) holds it is equality: a strict surplus is impossible
at the multiple zero. In every case it forces both signed remainder
contributions B(P,R)(a)<=0 and D(R)(a)<=0, not just smallness.

For each fixed F as above, every compact neighborhood I of a inside
its interval of analyticity, and every epsilon>0, there exist real
analytic R and P=F-R such that

    max_(0<=j<=2) sup_(t in I) |R^(j)(t)|<epsilon

but (1) fails strictly at a. One may choose R(t)=delta(t-a),
with delta>0 explicitly chosen below. Thus even preserving the zero
value F(a)=P(a)=0 does not make an absolute C^2 error bound sufficient
for (1). Taking F(t)=(t-a)^m makes the entire example polynomial.

This is a local obstruction to the implication from small generic
absolute errors to the proposed absolute budget. It is not an actual
Hermite remainder, a negative value of D(Xi), a multiple Xi zero,
or a refutation of an actual-coefficient compensation theorem.
No originality beyond the sources checked is claimed.

## Proof

### Complete jet substitution and both implications

Since F=P+R and the first two F jets vanish,

    (R(a),R'(a),R''(a))=(-x,-y,c-z).

Direct substitution, retaining all mixed and quadratic terms, gives

    D(P)(a)=A,
    B(P,R)(a)=-2y^2-x(c-z)+xz=-2A-cx,
    D(R)(a)=y^2+x(c-z)=A+cx.                       (3)

Their sum is zero, as also follows from D(F)(a)=0 and the exact
expansion D(P+R)=D(P)+B(P,R)+D(R). This elementary expansion is
included because the present functions are arbitrary; no actual-Xi
sign certificate or known Laguerre theorem is being reproved.

Write b=B(P,R)(a), q=D(R)(a). Thus b+q=-A. If (1) holds then
A>=0 because its right side is nonnegative. Moreover

    |b|+|q|>=-(b+q)=A.

Combining with (1) forces equality. The identity

    (|b|+b)+(|q|+q)=0

then has two nonnegative summands, so each is zero. Hence b<=0
and q<=0. Substitution of (3) gives cx>=-2A and cx<=-A,
proving (2) without division by a vanishing jet.

Conversely suppose (2). Equation (3) gives b<=0 and q<=0, so
|b|+|q|=-b-q=A. This proves (1), its equality, and the asserted
signs. In particular these are necessary and sufficient conditions,
not merely sufficient bounds obtained by discarding a contribution.

If c!=0 and x=0, (2) forces A=0, and A=y^2 then forces y=0;
z is unrestricted. If cx>0, (2) is incompatible with A>=0.
If cx<0, solving -2A<=cx<=-A for A gives exactly
-cx/2<=A<=-cx, with A automatically positive. This proves all
branches in the double-zero classification and excludes all others.
The two boundary values of b and q follow directly from (3).

If c=0, (2) reads A>=0, -2A<=0<=-A, and hence A=0. Conversely
A=0 satisfies (2) and makes b=q=0. This proves the classification
for every m>=3; higher jets of F do not enter the predicate.

For completeness, these classifications have no hidden realizability
restriction at the level being tested. For any prescribed real
(x,y,z), set P(t)=x+y(t-a)+z(t-a)^2/2 and R=F-P. Both are analytic
near a and have exactly the jets substituted above. This statement
is about arbitrary local decompositions only, not Hermite truncations.

### Arbitrarily small violations for each allowed F

Fix I and epsilon as in the conclusion. Compactness gives a finite
number M=max_(t in I)|t-a|. Set

    K=max{1,M}, delta=epsilon/(2K),
    R(t)=delta(t-a), P(t)=F(t)-delta(t-a).

These functions are analytic on the same interval as F, delta>0,
and the exact uniform bounds are

    sup_I |R|=delta M<=epsilon/2,
    sup_I |R'|=delta<=epsilon/2,
    sup_I |R''|=0.

Thus the stated strict C^2 smallness holds. At a the jets of P
are (0,-delta,c), and those of R are (0,delta,0). Therefore

    D(P)(a)=delta^2,
    B(P,R)(a)=-2delta^2,
    D(R)(a)=delta^2.

The required bound would be delta^2>=3delta^2, which is false
because delta>0. Its exact deficit is 2delta^2. The full signed sum
is still zero, equal to D(F)(a); the failure is the separation into
absolute losses. The calculation works for c!=0 and c=0, and F
itself has not changed, so its exact multiplicity is preserved.
For the polynomial example F(t)=(t-a)^m, its m-th derivative at a
is m! (nonzero) and all lower derivatives vanish, verifying multiplicity
directly; P and R are also polynomials.

### Consequence and remaining limitations

The proposed small-error-only sufficiency route fails even for
arbitrarily accurate C^2 approximations to a fixed analytic F with
a multiple zero. At an actual hypothetical double Xi zero, an
argument using (1) would have to establish the double-zero jet
conditions above for the actual P_N; at multiplicity at least three
it would have to establish D(P_N)(a)=0 exactly. This proof supplies
neither actual condition. It also does not exclude their holding
because of actual coefficient correlations.

L564's error bound alone therefore cannot establish this budget
in the presence of admissible multiple zeros. This logical limitation
does not assert the existence of multiple Xi zeros or make a claim
about what extra information the actual Hermite expansion supplies.
Actual polynomial margins, complete signed cancellation, moving
heights/cutoff jumps, higher forms, and RH remain unresolved. No
numerical experiment, sampled positivity or infinite interchange is
used in this finite-dimensional proof.

### Independent critical replay, 2026-10-31

The separately approved audit passes without a change to the statement
or argument. The following exhaustive scalar check verifies necessity,
sufficiency and the equality boundaries independently of solving (2).
Set u=cx and v=A+u. Direct recomputation of the remainder jets gives
b=-A-v and q=v. Thus (1) is exactly

    A>=|A+v|+|v|.

If A<0 this is impossible. For A>=0 the complete right-hand-side
classification is

    v<-A:        -A-2v>A,
    -A<=v<=0:     A,
    v>0:          A+2v>A.

The middle closed interval is therefore necessary and sufficient,
including A=0, when it reduces to v=0. Translating back gives precisely
-2A<=u<=-A. No positive-surplus case or omitted zero jet survives.
At u=-2A, (b,q)=(0,-A); at u=-A, (b,q)=(-A,0). For c!=0,
u=0 forces x=0 and A=y^2=0, so z is free. For u<0 the interval is
-u/2<=A<=-u, and u>0 is excluded. For c=0 the same calculation
forces A=b=q=0. These exhaust m=2 and m>=3, respectively, because
exact multiplicity supplies exactly the stated alternatives for c.
Arbitrary prescribed triples are realized by the quadratic P in the
proof and R=F-P, with F and its multiplicity unchanged; no additional
jet restriction is implicit in that converse.

The quantifiers in the perturbation test also pass: fix F, a compact
I in its analytic domain and epsilon>0 before choosing delta. The
finite K=max{1,max_I|t-a|} is positive, so delta=epsilon/(2K)>0.
All three uniform errors are at most epsilon/2, epsilon/2 and zero,
respectively, hence their maximum is strictly less than epsilon.
The exact two-jets give (D(P),b,q)=(delta^2,-2delta^2,delta^2),
so the actual right-hand side is 3delta^2 and the required left-hand
side is delta^2. The positive deficit 2delta^2 holds for every such
delta and for both multiplicity cases. It does not require F'' to
be bounded away from zero. Choosing F=(t-a)^m additionally verifies
the polynomial examples through F^(m)(a)=m! and the vanishing of
each lower derivative. None of these examples asserts actual Hermite
coefficients or a multiple Xi zero.

No analytic estimate or numerical certificate is an input to this
replay. L564's absolute tail theorem and L568's actual decomposition
were checked only for the stated contextual normalization; their
proofs and certificates are not used. The empty-input DAG row remains
correct. This audit verifies the existing generic obstruction, not a
new mathematical theorem or a newly discovered obstruction beyond
the assessed sources. The actual-coefficient and higher-form gaps
remain exactly as stated above.

## Mathlib

The full classification and analytic perturbation statement have not
been checked in Mathlib; availability is unknown. Polynomial algebra,
absolute-value sign identities, and derivatives of affine functions
would be supporting facts, not a checked matching theorem. No formal
verification is claimed. General reference:
https://leanprover-community.github.io/mathlib4_docs/
