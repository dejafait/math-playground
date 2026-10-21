# L110 — Explicit hyperelliptic model of the unordered-pair curve

## Hypotheses

Use L109's geometrically integral curve B, its coordinates u,z, and
its exact polynomials H0,H1 for

    phi(t)=(3t²+t+1)^5(1−5t)=sum_(i=0)^11 c_i t^i,
    (c_0,...,c_11)=(1,0,0,−55,−165,−594,−1100,
                   −2145,−2475,−2970,−1782,−1215).

B is the smooth proper normalization of the specified open H1=0,
with z H0(H0−1) invertible, as defined in L109. All fields have
characteristic zero. No rational point or rational Weierstrass point
is assumed. The marked curve remains L109's extension v²=z.

## Conclusion

An explicit smooth proper Q-model of B is the completion of

    W²=f(T)=11(T²−4)(7+52T−6T²−64T³−25T⁴)
           =−275T⁶−704T⁵+1034T⁴+3388T³+341T²−2288T−308.    (1)

The sextic is squarefree. Define

    F=T⁵+T⁴−4T³−3T²+3T+1,
    K=T²−T−1,              L=T²+T−1,
    u=(F−11−K W)/(60F),    M=2−10u,
    z=−M² (T−2)L²/[300(T+2)K²].                            (2)

These are the original u,z, including the constant −1/300. In
particular an explicit rational function for the original scalar is

    s=sum_(i=0)^11 c_i sum_(j=0)^floor(i/2)
          binom(i,2j) u^(i−2j)(−3z)^j,                    (3)

where u,z are the functions (2). This finite expression, with all
coefficients specified above, is H0(u,z), not a new scalar coordinate.
The exact marked extension is v² equal to the right side of (2);
no constant twist is suppressed.

Conversely, in Q(B), set

    d=3u²+u+1−9z,       e=6u+1,
    T=2(d²−3ze²)/(d²+3ze²),
    W=(F(T)−11−60F(T)u)/K(T).                              (4)

Equations (2) and (4) are inverse Q-function-field maps. They extend
uniquely to an isomorphism of the smooth proper curves. Formula (3)
therefore retains B's original degree-55 map to the s-line.

This is a model construction only. It does not determine B(Q),
L109's marked rational points, degree-nine rational-root lifting,
remaining factors or either L095 integer system. Separate critical
audit of this instance was completed on 2026-10-20, as recorded below.

## Proof

### Exact elimination on the ordered-pair auxiliary cover

Work first with two ordered distinct roots a,b in the same regular
fiber of phi, over Q. This is the untwisted ordered-pair auxiliary
cover; it is not being identified with L109's minus-three marked
curve. L109 identifies its swap-invariant subfield with Q(B), using

    u=(a+b)/2,       z=−(a−b)²/12.                         (5)

The ordered cover is geometrically integral, as follows from the
actual pair-transitive monodromy established in L109. Thus identities
on its generic fiber are identities in its function field.

Put q(X)=3X²+X+1, x=1−5a, y=1−5b, and t=q(a)/q(b).
On the regular-fiber open q(a),q(b),x,y are nonzero. The equality
phi(a)=phi(b) gives y=t^5 x. Also

    25q(a)=3x²−11x+33,
    25q(b)=3y²−11y+33.

Substituting y=t^5x in q(a)=tq(b), and cancelling 1−t, gives

    3 S11(t)x²−11 S6(t)x+33=0,
    S_n(t)=1+t+...+t^(n−1).                               (6)

This cancellation is legitimate generically: t=1 would force y=x
and a=b. The function t is nonconstant. Indeed, if it were a
constant different from one, the uncancelled quadratic equation
has nonzero constant coefficient 33(1−t); it would force x algebraic
over the constants, hence also a,b and their common scalar algebraic,
contradicting this nonconstant cover of the scalar line.

The discriminant of (6) factors exactly as

    Delta=121 S6²−396 S11=(t−1)² P8(t),
    P8(t)=−275−704t−1166t²−1540t³−1705t⁴
                       −1540t⁵−1166t⁶−704t⁷−275t⁸.        (7)

Let Y=(6 S11 x−11 S6)/(t−1). Equation (6) gives Y²=P8(t).
Conversely x=(11 S6+(t−1)Y)/(6 S11), y=t^5x recover a,b.
These are inverse generic coordinate changes, retaining the original
fiber scalar. Their denominators are nonzero functions since t is
nonconstant. Thus this auxiliary ordered field is exactly Q(t,Y).

### The unordered quotient and the actual Q-form

Swapping a,b sends x to t^5x and t to 1/t. Since
S11(1/t)=t^(−10)S11(t) and S6(1/t)=t^(−5)S6(t), it sends

    (t,Y) -> (1/t,−Y/t⁴).

Its invariant functions

    T=t+1/t,             W=Y(t²−1)/t³                    (8)

satisfy W²=(T²−4)R4(T), where

    P8(t)/t⁴=R4(t+1/t),
    R4(T)=77+572T−66T²−704T³−275T⁴.

This proves (1) with its exact constant. Conversely t satisfies
t²−Tt+1=0 and Y=W t³/(t²−1). Hence Q(t,Y) has degree at most
two over Q(T,W). The nontrivial swap fixes the latter and changes
t, so the degree is exactly two and Q(T,W) is the entire fixed
field. L109's unordered-pair identification (5) therefore identifies
it with Q(B), over Q and with the correct Q-form. No conic splitting
or rational-point assumption enters this argument.

The ordinary polynomial Euclidean algorithm gives
gcd(f,f')=1 over Q; its exact value and complete coefficients are
in the certificate below. Thus (1) is a geometrically integral
smooth affine hyperelliptic curve. Its degree-six completion is
smooth using the infinity chart below and has genus two, also
consistent with L109. In particular f is not a square in Q(T),
so no extra component is introduced by the displayed equation.

### Explicit inverse functions and scalar transport

Write C_n=t^n+t^(−n), so C_0=2, C_1=T and
C_(n+1)=T C_n−C_(n−1). Directly from these identities,

    S11/t⁵=F(T),
    (1+t⁵)S6/t⁵=F(T)+1,
    (1+t⁵)/(t²(t+1))=K(T).

Together with (8) and the formula for x, they give

    x+y=[11(F+1)+K W]/(6F)=M.

Since u=(2−x−y)/10, this is precisely the first formula (2).
Furthermore

    (t⁵−1)²/t⁵=(T−2)L²,
    (t⁵+1)²/t⁵=(T+2)K².

Therefore (x−y)²=M²(T−2)L²/[(T+2)K²]. Equation (5), and
a−b=(y−x)/5, give the exact formula for z in (2).

For the reverse expression, if delta=(a−b)/2 then delta²=−3z
and a=u+delta, b=u−delta. Consequently

    q(a)=d+e delta,       q(b)=d−e delta.

Taking q(a)/q(b)+q(b)/q(a) gives the expression for T in (4).
Solving the already established u formula for W gives the other
expression (4). This proves both compositions in the actual
ordered field, and hence in its swap-invariant subfield Q(B).
Independently, the complete substitution H1(u,z)=0 and both model
coordinate compositions were checked directly in Q(T)[W]/(W²−f).
The certificate also checks (6), q(a)=tq(b), phi(a)=phi(b), the
relation (1), the reverse pair-coordinate compositions and
H0(u,z)=phi(a) in Q(t)[Y]/(Y²−P8). All are full rational-function
identities, with zero numerators in both basis components.

Formula (3) follows by expanding phi(u+delta), using delta²=−3z
and H1=0 to remove its odd part. Thus it is the common value
phi(a)=phi(b), not merely a function with the same branch data.
The coordinate z is itself identified, not just its square class;
therefore the extension v²=z is preserved exactly, including −3
in the marking interpretation of L109.

### Dense opens and exceptional charts

All inversions above are in function fields of integral curves.
For (2) one may use the finite chart with F K(T+2) nonzero.
For (4) one may use B's original open with d²+3ze², F(T) and
K(T) nonzero. The denominator d²+3ze² equals q(a)q(b), nonzero
on a regular fiber. The other polynomial denominators are nonzero
functions because T=t+1/t is nonconstant. Also z,s,s−1 are
nonzero functions: this follows from the regular-fiber description
and is checked by complete substitution. Thus intersecting these
conditions and their inverse images gives nonempty dense opens
on which both maps and both compositions are defined.

No excluded coordinate value is removed from the proper curve.
Its complete smooth charts are the finite equation (1) and

    h=1/T, V=W/T³,
    V²=−275−704h+1034h²+3388h³+341h⁴−2288h⁵−308h⁶.         (9)

At a finite point with W nonzero, T−T0 is a local parameter over
its residue field. At W=0, squarefreeness gives f'(T0) nonzero,
so W is a local parameter. At h=0, V²=−275 and V is nonzero;
h is a local parameter. This gives the full infinity fiber,
one degree-two Q-point with residue field Q(sqrt(−11)), or two
geometric points. It also identifies the normalized charts at
all finite denominator zeros F=0, K=0 and T=−2.

For example the apparent K-denominator of z can be removed
identically. With J=(T+2)(T²−1), one has F+1=KJ and

    N=11J+W,   M=K N/(6F),
    z=−N²(T−2)L²/[10800(T+2)F²].                           (10)

At the point T=−2,W=0 even the remaining T+2 denominator
is removable: W is the parameter, J is divisible by T+2,
and W²/(T+2)=(T−2)R4(T). Substitution gives u=1/5 and
z=11/75 there. This calculation uses the normalized local ring,
not substitution into a zero-over-zero expression. At T=2,W=0,
the first formulas give u=z=0; its proper image is a boundary
point, not a point of the localized affine open B°. Points at
F=0 or infinity are likewise retained through their DVRs, allowing
poles of u,z,s. No assertion that their affine formulas are regular
there is needed.

Import Stacks, Theorem 53.2.6, tag 0BY1,
<https://stacks.math.columbia.edu/tag/0BY1>, in its function-field/
normal-projective-curve equivalence. The verified inverse Q-field
maps identify the smooth proper model covered by (1),(9) with B.
On exceptional points this extension is exactly the one specified
by their normalized valuations; it is not an identification of
singular plane closures. At every zero or pole of z, the marked
fiber must still be evaluated by L109's unit-residue rule after
removing its even order. Equations (2),(10) are not instructions
to replace that rule by evaluation of zero or infinity.

### Source scope, checks and limitations

The ready assessment is
`drafts/literature/2026-10-20-pair-genus-two-explicit-model.md`.
The general construction methods are imported from van Hoeij,
*An algorithm for computing the Weierstrass normal form of
hyperelliptic curves*, arXiv:math/0203130v1, Sections 1–4, pp.1–4,
and Poonen, *Computational aspects of curves of genus at least 2*,
ANTS-II, LNCS 1122 (1996), pp.283–306, author Sections 2–3,
pp.2–4. Their inverse-function-field and square-completion method
is specialized here by exact elimination using phi's displayed
factorization. No general algorithm is reproved or assumed to
have run in a missing curve backend. Canonical differentials are
not guessed: the verified smooth squarefree model and inverse
field maps bypass that implementation. The existence theorem
alone would not supply these maps or certify this instance.

Run `python3 scripts/pair-genus-two/model.py`.
The full output is `scripts/pair-genus-two/model-certificate.json`.
It retains the source hash, exact Delta,P8,R4,f,F,K,L coefficients,
full reduced rational functions u,z,s, and every coefficient of
each identity residual. All 31 checks pass, with no failures;
the achieved degree is six (required five or six) and the
squarefree gcd is one. Both entire input invariant polynomials
are reconstructed and compared coefficient by coefficient.
The proof above supplies the dense-open, invariant-field and
proper-normalization arguments, which finite calculations alone
do not establish. The expanded s coefficients are optional output;
the load-bearing definition is the complete finite expression (3).

This is a local reproduction/specialization of assessed methods,
not a novelty certification or progress beyond the inspected
general methods. It supplies the requested exact model and maps,
but no rational-point determination, rank bound, rational-root
recovery or Beal signature exclusion.

### Independent critical audit, 2026-10-20

The audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-20-explicit-pair-model-critical-audit.md`.
It confirms the stated model and maps without a correction to their
mathematical conclusions. The following checks concern this instance,
not a reproof of the imported curve-extension theorem.

First, the auxiliary ordered field is over Q: it is the function
field of ordered distinct roots a,b, not the field obtained by
adjoining L109's v. Its geometric integrality follows from L109's
actual pair transitivity. Nonconstant t and the inverse formulas
for x,y identify it with Q(t,Y); independently P8 is squarefree,
so the displayed quadratic field is integral even after extending
constants. The swap acts by t -> 1/t, Y -> −Y/t⁴. Direct substitution
checks both its action on x and its invariance on W. Since t is
nonconstant, t!=1/t as functions. Adjoining t to Q(T,W) recovers
Y=W t³/(t²−1), and t satisfies a quadratic. Thus the nontrivial
swap proves that this is the entire index-two fixed field. The
invariant coordinates (5) identify it with L109's Q(B), without
changing the constant field or the marking. In particular the
ordered field adjoins a square root of −3z, while the marked field
adjoins a square root of z; these are not silently identified.

Second, expansion of phi from its factors reconstructs every
coefficient of L109's H0,H1. In the two quadratic fields the audit
checks both basis components of H1(u,z), both model inverse
compositions, both pair inverse compositions, and
H0(u,z)−phi(a). It also compares the full saved rational functions
u,z,s with independent recomputations, including every coefficient
of the expanded scalar. Thus the exact s and z, rather than
only their branch data or square classes, agree. The factor
−1/300 in z is retained. Squarefreeness of f and the inverse
field maps supply the actual genus-two Q-model. All denominators
used generically are nonzero functions: t,T are nonconstant,
q(a)q(b) is nonzero on the regular-fiber open, and the other
denominators are nonzero polynomials in these coordinates.
The resulting dense opens are nonempty; no pointwise inversion
at a boundary point is used.

Here is a complete check of the exceptional coordinate charts.
The exact polynomial gcds show that F,K,L are squarefree,
pairwise coprime, and each is coprime to f. Therefore none of
their zeros is a branch point of the hyperelliptic projection.
The finite smoothness test and infinity chart (9) cover the
whole proper model. At finite branch points W is a uniformizer;
elsewhere T−T0 is a uniformizer over the geometric residue field.
At infinity h is a uniformizer and V0²=−275. These two geometric
points form one degree-two Q-point, since −275=25(−11) is
nonsquare in Q.

To check F=0 explicitly, set Nbar=11J−W. Exact polynomial
reduction gives

    N Nbar=396(T+2)F.

In the function field this supplies the alternate formulas

    u=1/5−33K(T+2)/(5 Nbar),
    z=−363(T²−4)L²/(25 Nbar²).                            (11)

At a root alpha of F, neither K,J nor T+2 vanishes, since
KJ=F+1=1 there. Also f(alpha)=121J(alpha)² is nonzero.
On the sheet W=−11J, Nbar=22J is a unit, and N has a
simple zero by the displayed product and the simple zero of F.
Formula (11) is regular there and z is nonzero. On the sheet
W=11J, N=22J is a unit; (2),(10) show that u has a simple
pole and z a double pole. In particular the cancelled sheet
is not lost, and a pole on the other sheet is allowed by the
proper isomorphism.

At K=0, F=−1, and T+2,L are nonzero. Formula (10) is regular.
Its N is nonzero because N Nbar=396(T+2)F is nonzero; thus
z is a unit. At T=−2 the only point has W=0,
F=−1,K=5,L=1,R4=−99. Here W is a uniformizer,
T+2 has order two, and J has order two. Hence N has order
one and N²/(T+2) has residue

    W²/(T+2)=(T−2)R4(T) -> 396.

Formula (10) therefore gives z=11/75, and (2) gives u=1/5,
as originally claimed. At T=2 one has F=11,K=1,L=5,
R4=−9075 and f'(2)=−36300. The original formula is regular,
with u=z=0. More precisely, z/(T−2) has residue −1/12,
and z/W² has residue 1/435600=1/660². This verifies order
two in the genuine parameter W, not merely the zero value
of the affine discriminant.

At either point at infinity, rewrite (2),(10) in h,V.
The denominators after removal of their common powers of h
are units. The limiting values are

    u=(1−V0)/60,       z=−(11+V0)²/10800,   V0²=−275.

In particular z is a unit at both points. Finally, a zero of
L gives two unramified finite points, and (10) has a unit
factor times L² there. These are four geometric zeros of
order two. Together with T=2 they account for five order-two
zeros; the five pole sheets at F=0 account for five order-two
poles. The product identity for N and all the coprimality
checks above exclude any additional zeros or poles. This
agrees with L109's full divisor orders and checks that no
exceptional denominator has created or removed a marked branch.
At every rational point the exact normalized unit must still
be tested using L109; no rational-point classification follows.

Apply the already cited Stacks Theorem 53.2.6, tag 0BY1,
over the perfect field Q to these inverse fields and their
smooth proper models. Its hypotheses are now met; it extends
the inverse maps uniquely, including all the charts just
checked. It does not assert that the original affine functions
are everywhere regular. The full fixed-field argument, rather
than an invariant match or a numerical calculation, identifies
the proper Q-form and degree-55 scalar map.

Reproduce the independent arithmetic with
`python3 scripts/pair-genus-two/audit_model.py`.
It uses integer polynomial triples (A+B Y)/C with one common
denominator, imports neither the original producer nor its
arithmetic classes, and checks the complete original certificate.
All 86 checks pass, with empty failure list; the actual degree
is six against required five or six, and gcd(f,f')=1.
The full coefficients, independently reduced maps, both
components of all residuals and check results are in
`scripts/pair-genus-two/model-audit-certificate.json`.
The original certificate SHA-256 is
`e2f28571f082dd0c1e810d4a4b44e57e356eded950b5f33ca7d5da46b3cfc639`.
The initial audit implementation's singleton-gcd sign error and
its failed report are preserved in the working record and
`scripts/pair-genus-two/model-audit-initial-sign-failure.json`;
repairing that checker did not change the mathematics.

This verifies the existing specialization and its exceptional
charts; it establishes no new result beyond the inspected
general methods. Rational points, rank, degree-nine root
recovery, compatible factors, both L095 integer systems and
the minus-eleven alternative remain unresolved.

## Mathlib

Full matching theorem and supporting results have not been checked.
No absence claim is made. The exact model, reciprocal elimination,
inverse identities and scalar transport are certified here over Q;
no Lean formalization or library-based verification is claimed.
