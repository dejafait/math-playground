# L069 — Full ordered-independent-seven-torsion-pair domain

## Hypotheses

Use audited L067 and L068 for the exact curve
E: y^2+y=x^3+x^2-2x over Q, with short coordinates
X=36x+12, Y=216y+108 and c(X)=X^3-3024X+46224.
Retain the entire degree-48 nonzero-seven-torsion algebra
Q[X,Y]/(f(X),Y^2-c(X)) and all six geometric forward scalar maps.
Here f is L067's complete monic squarefree degree-24 polynomial,
with gcd(f,c)=1. No residual-image, L026, Selmer or rank premise is used.

Let C=Q[X]/f. For i=1,2,3 let r_i in C be the first component of
L068's X-coordinate of [i]P. The other component (the coefficient of Y)
is zero for these three maps; the complete replay checks that fact.

## Conclusion

The complete coefficient certificate
`scripts/seven-torsion/incidence-247/ordered-pairs.json` supplies a monic
g(U) in C[U] of degree 21 satisfying the entire identity

\[
 f(U)=(U-r_1)(U-r_2)(U-r_3)g(U).
\]

There is a faithful rational presentation of the Galois-equivariant
function algebra on all ordered independent pairs (P,Q) in E[7]^2:

\[
 S=C[U,Y,V]/(g(U),Y^2-c(X),V^2-c(U)).
\]

Its Q-basis is X^i U^j Y^e V^d, 0<=i<24, 0<=j<21,
e,d in {0,1}, ordered with i fastest, then j, then e, then d.
Thus dim_Q S=2016. P=(X,Y), Q=(U,V) in short coordinates retain
both signs and every independent pair, rather than one orbit or field.
The certificate also gives a full inverse of U-X in C[U]/g, hence
in S; the secant denominator is valid everywhere on this domain.

This establishes only a prequotient input to the approved incidence
construction. It does not supply B_inc, D, either incidence pullback,
a rank-seven multiplication representation, or a norm certificate.
Producer translation coordinates and any streamed action columns are
separate unfinished evidence, not covered by the independent domain replay
or this conclusion. No cohomology-image, global-class, Selmer or BSD
conclusion follows. The fixed full-action feasibility outcome is recorded
separately; no computational impossibility theorem is asserted here.

## Proof

**Imported construction and why this specialization is needed.**
Schaefer–Stoll, *How to do a p-descent on an elliptic curve*, Trans. AMS
356 (2004), 1209–1231, DOI 10.1090/S0002-9947-03-03366-X,
[author long version dated 13 June 2001](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
Section 7, Lemma 7.5 and Proposition 7.10, printed pp. 16 and 19,
define the affine-line and incidence Galois sets. They do not give this
fixed p=7 rational ordered-pair polynomial. Import the equivalence
between finite etale Q-algebras and finite continuous Galois sets from
[Stacks Lemma 58.2.2, tag 03QR](https://stacks.math.columbia.edu/tag/03QR).
The finite root identification and coefficient/unit checks below are the
necessary applicability argument, not a reproof of that theorem or a new
general incidence construction. Q is perfect and all the roots used here
are distinct, so its finite-etale hypotheses hold. No cyclotomic twist
or dual-to-point identification is introduced.

**All coefficients and the domain.** The producer performs three monic
synthetic divisions in C[U], using the audited scalar coordinates r_i;
it saves all 22 coefficients of g, including zero coefficients. The
independent verifier imports no producer arithmetic. Using only the old
independent verifier's rational polynomial convolution/remainder helpers,
it multiplies (U-r_1)(U-r_2)(U-r_3)g and checks equality with f(U)
coefficient by coefficient in C[U]. It checks the complete r_i against
the hashed audited action certificate, including their zero Y-components,
and independently checks f(r_i)=0. Three saved inverse identities for
r_i-r_j, i>j, check the separation on the full C-domain.

Fix any geometric point P=(X,Y) of the whole L067 algebra. Its order is
seven. The nonzero points on its F_7-line are precisely [i]P for
i=1,...,6. On a short Weierstrass curve, equal x-coordinates are exactly
equal or opposite points. Thus their distinct x-coordinates are the
three values r_1(P),r_2(P),r_3(P), each accounting for the signs i and
7-i. L068's geometric identification, rather than a root-polynomial
test alone, is essential here. Since f has 24 distinct geometric roots,
the full factorization shows that g has precisely the other 21 roots,
all distinct. For each U among them c(U) is nonzero by gcd(f,c)=1;
there are exactly two V-values. Therefore Q=(U,V) runs over all 42
nonzero seven-torsion points outside the line spanned by P.
These are exactly the Q independent of P. All 48 choices of P are
retained. There is no exceptional omitted component or assumption about
the actual Galois image.

Conversely every ordered independent pair has its U-coordinate among
those 21 roots and hence defines a point of S. The construction is
rational and therefore Galois-equivariant. After extending scalars to
Qbar it is the product algebra on exactly these 48*42 points, with
no nilpotents. This identifies the finite-etale algebra S with the
equivariant function algebra by the cited equivalence. The asserted
dimension and entire basis follow independently from successive monic
division by f, g, Y^2-c(X) and V^2-c(U): each monic quotient is free
on the displayed powers over the preceding coefficient algebra. Thus
dimension is not inferred from a selected numerical fiber alone.

**Full-domain denominator.** The saved values v=g(X) and w in C obey
vw=1. Let q(U) in C[U], degree at most 20, be the division quotient
with (U-X)q(U)=g(U)-g(X); the certificate stores the inverse as -wq(U).
(The verifier reconstructs the identity from the saved inverse rather
than needing q as an additional field.) Modulo g, this gives
(U-X)(-wq(U))=1. The replay checks the actual inverse directly by
forming the whole polynomial product with U-X and reducing its degree-21
term by the complete g. It separately checks v, w and vw=1 in C.
This proves the denominator is nonzero on every ordered independent
pair, with no numerical embedding or point sampling. The inverse stays
an inverse on adjoining Y,V.

**Reproduction and limits.** From the active notebook directory:

```bash
python3 scripts/seven-torsion/incidence-247/verify_pair_domain.py
```

The complete report `scripts/seven-torsion/incidence-247/domain-verification.json`
records 33 passing checks and no failures, including the full polynomial
identities, all three separations, both hashed input files, the full
inverse, and all 89 pre-existing non-cache upstream files unchanged.
All rational coefficient slots are read, not previewed or sampled.
The largest numerator/denominator bit lengths in the saved g and inverse
are respectively 172 and 304. Those are measured input sizes, not bounds
for subsequent quotient calculations. The producer command is
`python3 scripts/seven-torsion/incidence-247/build_pair_presentation.py`;
it also attempts later stages, whose evidence is explicitly outside this
lemma. This fixed reproduction has not received a separate critical audit.

The remaining incidence quotients, inclusions, bases, transports and norm
are not consequences of counting this domain. In particular this result
does not identify B_inc with the original point algebra, erase the
dual twist, or treat a norm as a Q-linear map. Complete global power
classes and all local and Selmer hypotheses remain independent.

## Mathlib

Full matching coverage for this fixed ordered-pair finite-algebra
certificate and its complete denominator replay was not checked.
No absence claim is made. The cited general finite-etale result and the
audited local inputs justify the informal proof; this is not a Lean
formalization or a new result beyond those methods.
