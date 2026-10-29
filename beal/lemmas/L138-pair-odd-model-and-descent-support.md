# L138 — Odd model, actual quartic descent factor and sufficient support

## Hypotheses

Use L110's smooth proper genus-two curve B over Q and its exact model

    W²=f(T)=11(T²−4)Q4(T),
    Q4(T)=7+52T−6T²−64T³−25T⁴.

Keep L110's original functions u,z,s and marked extension v²=z, including
all their constants. Use L133's number field K=Q(alpha), where

    A(U)=U⁴+64U³+150U²−32500U−109375,
    alpha=25theta, Q4(theta)=0.

Use audited L134's maximal order O_K with basis (1,alpha,beta,gamma),
and audited L137's ordinary class-group bound
dim_F2 Cl(O_K[1/330])/2Cl(O_K[1/330])<=2. No complete class presentation,
unit basis, Selmer computation, rank, analytic hypothesis or rational-point
classification is assumed.

## Conclusion

Put c=−36300. A monic integral odd model of this same Q-curve is

    Y²=G(X),
    G=X⁵−76835X⁴+2196150000X³−29655931140000X²
       +191519916588000000X−477484407427500000000,
    X=c/(T−2), Y=c²W/(T−2)³,
    T=2+c/X, W=cY/X³.

These maps extend to inverse isomorphisms of smooth proper curves.
All original functions are transported by the inverse substitution;
the twist and the marking v²=z are preserved exactly.
There is an exact factorization G=(X−9075)H, with

    H=X⁴−67760X³+1581228000X²−15306287040000X
      +52615361700000000.

H is irreducible. For K_eta=Q[eta]/H, the identification with K is

    eta=−907500/(alpha−50), alpha=50−907500/eta.

Thus Q[X]/G is Q×K, with X mapping to (9075,eta). The full polynomial
discriminant is disc(G)=2³² 3²¹ 5²⁷ 11³⁵.

Let S consist of infinity and 2,3,5,11, using every place over these
rational places in every algebra factor. For L=Q[X]/G, define L(S,2)
to be the square classes in L*/L*² with even valuations at every finite
prime outside S, using the maximal integer ring Z×O_K. The Jacobian
Kummer image of B is contained in

    ker(N:L(S,2) -> Q*/Q*²).

This is a supported ambient-group containment, not a Selmer or local-image
computation. There is no scalar quotient in this odd-degree Jacobian map.
The quartic localized ordinary class quotient used here has dimension at
most two by L137, in precisely the transported field and maximal order.
No further localization is needed. No strict improvement on that bound,
rank bound, point determination or Beal exclusion follows.

## Proof

### Reused model and inverse maps, including exceptional points

The quintic and maps already occur in the complete `/model` of
`scripts/pair-genus-two/rank-lower-certificate.json` and the 2026-10-20
pair-rank-lower working record. ATTEMPTS/050 parks its point/divisor
detector. This proof independently certifies only its model interface,
then supplies the missing field/support interface; no search is rerun.

The Taylor coefficients of f(2+t), through degree six, are

    (0,−36300,−76835,−60500,−22506,−4004,−275).

They give the entire identity

    X⁶ f(2+c/X)=c²G(X).                                      (1)

Thus c=f'(2)!=0. Exact Euclidean algorithms give
gcd(f,f')=gcd(G,G')=1 over Q. G is monic integral of degree five.
Since Y=X³W/c, (1) proves exactly Y²=G. Substitution in both orders
recovers the coordinates: for example

    2+c/[c/(T−2)]=T,
    c[c²W/(T−2)³]/[c/(T−2)]³=W.

Conversely c/(T−2)=X and c²W/(T−2)³=Y after the inverse substitution.
The denominators are nonzero functions since T and X are nonconstant
and c!=0. These are inverse Q-field maps on dense opens.

At P_+=(2,0), W is a uniformizer and T−2 has order two, because
f'(2)=c!=0. Thus X,Y have orders −2,−5. The odd infinity chart
h=1/X, Z=Y/X³ has equation

    Z²=h−76835h²+2196150000h³−29655931140000h⁴
       +191519916588000000h⁵−477484407427500000000h⁶.

It has a unique smooth rational point at h=Z=0, with Z a uniformizer;
this is P_+'s image. At T=−2 the map is regular and gives
(X,Y)=(9075,0), with regular inverse since 9075!=0.

At sextic infinity set k=1/T, V=W/T³, with V²=−275 at k=0. Then

    X=ck/(1−2k), Y=c²V/(1−2k)³.

The two geometric infinity points give X=0,Y=c²V. Conversely
k=X/(2X+c), V=cY/(2X+c)³ are regular there. The common residue field
is Q(sqrt(−11)), and G(0)=−275c⁴!=0. These exhaust the fibers where
an affine map has a zero denominator. Squarefreeness proves smoothness
on finite charts; V!=0 proves it at sextic infinity, and the nonzero
h-derivative proves it at odd infinity. The two charts for each model
give its complete smooth hyperelliptic model.

Import [Stacks Theorem 53.2.6, tag 0BY1](https://stacks.math.columbia.edu/tag/0BY1),
the function-field/normal-projective-curve equivalence already qualified
in L110. Over the perfect field Q the verified inverse field maps extend
uniquely to inverse isomorphisms of smooth proper curves. The calculations
above specify their exceptional points; affine denominators remove none.

Retain L110's functions by setting T_X=2+c/X, W_X=cY/X³ in its formulas.
Explicitly, with F=T⁵+T⁴−4T³−3T²+3T+1, K0=T²−T−1, L0=T²+T−1,

    u_X=[F(T_X)−11−K0(T_X)W_X]/[60F(T_X)], M_X=2−10u_X,
    z_X=−M_X²(T_X−2)L0(T_X)²/[300(T_X+2)K0(T_X)²],
    s_X=H0(u_X,z_X).

H0 is exactly L110's finite expression (3), with its stated coefficients.
The inverse compositions recover u,z,s. In particular −1/300 and v²=z_X
have not changed. At poles or zeros these are rational functions on the
proper curve; L110's normalized residue rule for marked lifting remains
necessary. No boundary point is thereby accepted as an integer solution.

### Actual quartic field and full basis transport

Polynomial division proves G=(X−9075)H. Coefficient comparison also gives

    X⁴ Q4(2+c/X)=−825H(X), Q4(2)=−825.                       (2)

In K, theta=alpha/25, so X=c/(theta−2)=25c/(alpha−50).
The denominators alpha−50 and eta are nonzero since A(50)!=0 and H(0)!=0.
Their inverses reduced in the respective quotient algebras give

    eta=18304+(10296/25)alpha+(5016/625)alpha²+(44/625)alpha³,
    alpha=−214+(3/110)eta−(7/5989500)eta²+eta³/57978360000.     (3)

H(eta) modulo A and A(alpha) modulo H are zero. Substituting (3) in
both orders and reducing gives the respective generator. These statements
follow from the rational maps and (2) and are also independently checked
by complete polynomial reductions.

The full matrix with columns (1,eta,eta²,eta³) in the alpha power basis is

    M = [[1,18304,342652640,6682714614400],
         [0,10296/25,87143232/5,587730500544],
         [0,5016/625,59990832/125,495738169344/25],
         [0,44/625,596288/125,5297933696/25]].

The reverse matrix, with alpha powers in the eta power basis, is

    N = [[1,−214,21046,−1407344],
         [0,3/110,−563/165,53601/220],
         [0,−7/5989500,4217/23958000,−52823/3993000],
         [0,1/57978360000,−41/14494590000,2141/9663060000]].

Every column is verified by reducing the respective power. MN=NM=I4,
with det(M)=260770151043072, det(N)=1/260770151043072. These are inverse
algebra isomorphisms. Since Q[alpha]/A is a field by L133, H is irreducible.
The nonzero resultant below proves the linear factor is distinct, giving
L=Q×K with its specified coordinate, rather than an unbound abstract field.

L134's entire maximal-order basis becomes the eta-coordinate matrix

    B_eta = [[1,−214,723/2,859/6],
             [0,3/110,−2/33,−19/792],
             [0,−7/5989500,17/5324000,181/143748000],
             [0,1/57978360000,−1/19326120000,−7/347870160000]].

Its columns are the preimages of (1,alpha,beta,gamma). Multiplying by M
recovers L134's complete alpha-coordinate basis; its determinant is
nonzero. A Q-field isomorphism preserves and reflects satisfaction of
monic Z-polynomials, so it identifies full integer rings. This lattice
is therefore O_eta, not an assumed monogenic order Z[eta]. It identifies
O_eta[1/330] with O_K[1/330] as well.

### Polynomial discriminant, sufficient support and class input

Exact Sylvester determinants, using
disc(P)=(-1)^(n(n−1)/2) Res(P,P')/lc(P), give

    disc(H)=171826489180225573676544821428224000000000000000
           =2³² 3¹¹ 5¹⁵ 11²¹,
    Res(X−9075,H)=H(9075)=73990352390625=3⁵ 5⁶ 11⁷,
    disc(G)=940676528946413053932596972960349467971634808096000000000000000000000000000
           =2³² 3²¹ 5²⁷ 11³⁵.

The factor-product identity disc(G)=disc(H)H(9075)² agrees with the
independent direct quintic calculation. The replay also checks
disc(H)=det(M)² disc(A), using audited L134's
disc(A)=2526820312500000000, binding the polynomial discriminant to the
same field. Every prime factor and final cofactor one are certified by
successive exact division and complete trial data: all integer divisors
through 11 are tested, with primality checked separately. A field
discriminant has not substituted for disc(G).

Import Michael Stoll, *Implementing 2-descent for Jacobians of
hyperelliptic curves*, Acta Arith. 98 (2001), 245–277, DOI 10.4064/aa98-3-4,
[Sections 2–4, pp.247–250, Lemma 4.1, Proposition 4.2; Proposition 4.6
and Corollary 4.7, pp.252–253](https://www.impan.pl/shop/en/publication/transaction/download/product/83397).
For squarefree monic integral odd-degree G, the Jacobian two-descent
map takes values in the norm kernel of L*/L*². Its rational image has
even valuations outside infinity, 2 and primes p with p²|disc(G), in the
product of maximal integer rings. Proposition 4.6 includes both good
reduction and discriminant valuation one. These are imported statements,
already inspected in the ready assessment, with no reproof of the theory.

Here the curve is exactly B over Q, with degree G=5=2g+1 and g=2, and
all squarefree/monic/integral hypotheses are certified. The complete
factorization gives sufficient S={infinity,2,3,5,11}; every odd prime
outside it has discriminant valuation zero. All primes above the four
finite rational primes are permitted in both factors. No minimality of
support is needed for the stated containment.

L137's bound applies to O_eta[1/330] through the verified field/lattice
transport. Its group is ordinary, without a narrow-class or positivity
condition. The rational factor Z[1/330] is a PID, so has class group zero.
No further localization occurs here. For any later enlargement of S,
the inspected [Claborn, Pacific J. Math. 15 (1965), Corollary 1.4 and
Proposition 1.5, p.800](https://msp.org/pjm/1965/15-3/pjm-v15-n3-p06-p.pdf),
equivalently [Clark, Enseign. Math. 55 (2009), Theorem 5,
pp.217–218](https://ems.press/content/serial-article-files/44188), gives
surjectivity to the ordinary class group of the further Dedekind
localization. Tensoring over Z with F_2 preserves it by
[Stacks Lemma 10.12.10, tag 00DF](https://stacks.math.columbia.edu/tag/00DF),
so the upper bound at most two persists. This concerns class groups
modulo doubles; no surjectivity on their two-torsion subgroups is needed
or asserted. No such enlargement or improved bound is calculated here.

### Evidence, scope and remaining gaps

The prior ready assessment is
`drafts/literature/2026-10-25-pair-genus-two-odd-model-support.md`.
The general normalization, proper extension, Kummer/support and
localization results are known. This supplies the fixed-instance model
certification, field binding and support specialization missing from the
earlier record. It is local progress using these known methods, with no
claim of originality or progress beyond their general conclusions.

Run `python3 scripts/pair-genus-two/odd_model_support.py`, followed by
`python3 scripts/pair-genus-two/verify_odd_model_support.py`.
Complete evidence is in
`scripts/pair-genus-two/odd-model-support-certificate.json` and
`scripts/pair-genus-two/odd-model-support-verification.json`.
The producer passes 22 checks; the replay passes 82; both failure lists
are empty. The complete saved model and its source hash are bound.
All coefficients, both full power-basis maps, the whole order basis,
all Sylvester matrices and every factorization trial/division are saved.
The replay consumes the complete objects and imports no producer math.
It uses sparse polynomials with separate power summation, Taylor
expansion instead of homogeneous substitution, Gaussian determinants
instead of Bareiss, and Euclidean resultants as well as full Sylvester
determinants. It checks all four curve-coordinate compositions as Laurent
monomials, both field relations/compositions and every basis column.
These are exact arithmetic checks, not a separate critical proof audit
or formal verification; both scripts share Python rational arithmetic.

Degree and matrix-size actual/caps are 6/12 and 9/12 in both scripts.
Observed numerator/denominator bits are 417/4096 for the producer and
250/4096 for the replay. Factor trials end at 11 against cap 100000,
with no cofactor or cap failure. These are observed size and fixed-domain
bounds, not counts of all elementary operations or internal Fraction
steps. No relation box, point search, unit basis, backend probe or
upstream arithmetic rerun is hidden here.

This prepares an actual descent interface only. Units or justified bounds
avoiding explicit generators, full global/local descent, ranks, rational
points, marked lifts, degree-nine/integer recovery, both L095 systems and
other signatures remain open. The ambient norm kernel is not asserted
equal to the Selmer group. ATTEMPTS/050,059–060 and unfinished L108
remain preserved. Beal stays unresolved.

### Separate critical proof audit — 2026-10-26

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-25-pair-odd-model-support-audit.md`.
The audit accepts precisely the stated model, field/order transport,
support containment and ordinary class quotient bound. It finds no
mathematical correction or additional direct input. This is validation
of a known-method specialization, not a new general result, a Selmer
bound or a Beal resolution. The source hypotheses are unchanged; reuse
the approved primary statements cited above rather than reprove them.

The complete producer and replay implementations were reviewed. Their
coefficient conventions agree with the canonical polynomials. Taylor
expansion gives the coefficient of X^j as f^(6-j)(2)/(6-j)! times
c^(4-j), including the vanishing X^6 term and monic X^5 term. This
checks the whole identity (1), not selected evaluations. The four Laurent
compositions restore both horizontal and vertical coordinates. The
Euclidean algorithms establish squarefreeness; the nonconstant coordinate
functions and nonzero c justify all generic divisions.

The exceptional-point argument also survives review. In the odd infinity
chart h=1/X and Z=Y/X^3, the forward maps are simply
h=(T-2)/c and Z=W/c. Their inverses T=2+ch, W=cZ are regular. The
full chart equation is f(2+ch)/c^2=h^6G(1/h); its h coefficient is one.
Thus both charts are smooth at the corresponding branch point, and the
orders of X,Y there are exactly -2,-5. At the sextic infinity fiber,
k=1/T is a parameter since V is nonzero. The displayed forward chart
map and its inverse have unit denominators at k=0 and X=0 respectively.
The identity

    (1-2k)^6 G(ck/(1-2k)) = c^4 k^6 f(1/k)

checks every coefficient of their chart equations. The residue field is
Q(sqrt(-11)), since -275=-11*5^2 and c is rational and nonzero.
Hence this is one degree-two closed point, or two geometric points,
on either model. At T=-2 the denominators are nonzero and the image
is (9075,0). There are no other affine denominator zeros. These checks,
together with the imported proper-curve equivalence, account for the
entire smooth proper curve, not a singular plane closure.

The formulas for u_X,z_X match L110 coefficient for coefficient, with
K0,L0 merely renamings of its K,L. The finite expression H0 is unchanged,
including its c_i and (-3z)^j factors. Substitution through inverse field
isomorphisms preserves this expression, the exact scalar s and the
extension v^2=z; no square-class-only comparison is used. Zeros and
poles still require the original normalized-residue lifting rule. The
audit does not reinterpret branch or infinity points as integer solutions.

The input review binds A to L133 and all four columns of the maximal
basis to L134, in their stated alpha coordinates. The relations
(alpha-50)eta=25c and eta(alpha-50)=25c hold in their respective quotient
algebras, and the complete reductions give both defining equations and
both inverse generator compositions. The full M,N matrices therefore
represent inverse algebra maps, not merely vector-space maps. L133's
irreducibility makes H a field polynomial. The matrices carry every
element of L134's basis to the printed B_eta and back. Satisfaction of
monic integer polynomials is preserved in both directions, so this
identifies the entire maximal orders and their localizations at 330.
No power-order maximality, matching discriminants alone, or matching
ideal norms is used to identify the arithmetic inputs.

For discriminants the reviewed replay independently rebuilds every
Sylvester row, performs Gaussian elimination, and compares with a
Euclidean resultant recurrence. For degrees m,n and nonzero remainder
r of degree k that recurrence is
Res(a,b)=(-1)^(mn) lc(b)^(m-k) Res(b,r); its constant-terminal and
zero-remainder cases are implemented separately. This checks the signs
as well as the magnitudes. The full prime-factor lists, every trial and
division, and terminal cofactors one were inspected and replayed.
All three printed positive integers agree with the prime powers. The
direct quintic discriminant, factor-product identity and quartic
power-basis discriminant identity agree. No untested cofactor or field
discriminant substitutes for the polynomial support calculation.

Stoll's Lemma 4.1 and Proposition 4.2 apply to this monic integral
squarefree degree-five model over Q. Proposition 4.6 and Corollary 4.7
apply at every odd prime outside the displayed support: the complete
polynomial discriminant factorization gives valuation zero there. Its
valuation-one case is covered by the source but is not needed for this
instance. The valuation condition uses every prime of Z times O_eta,
not a polynomial order. All finite allowed primes are exactly those
inverted by 330; infinity imposes no ordinary-class positivity condition.
Consequently L137 applies to the identical ordinary localized class
group through the verified field isomorphism. No further localization
or surjectivity on class two-torsion is required. The upper bound on the
class quotient alone supplies neither unit square classes nor the local
conditions defining Selmer. No even-degree scalar quotient is introduced.

One complete additional replay passes all 82 checks and reproduces the
entire prior output, including all resultant chains and bounds. The
prior output is preserved in
`scripts/pair-genus-two/odd-model-support-preaudit-verification.json`.
The supplement `python3 scripts/pair-genus-two/audit_odd_model_support.py`
passes 30 checks; full evidence is
`scripts/pair-genus-two/odd-model-support-audit.json`. It binds the
reviewed canonical input texts, printed polynomials, all four displayed
matrices, discriminant values and powers, full replay objects, and both
exceptional chart identities. Its source hashes record the reviewed
pre-audit lemma texts; appending this audit does not change their inputs.
Reproduction may update those text hashes without altering the mathematics.

Replay actual/caps remain degree 6/12, matrix size 9/12 and observed
rational bits 250/4096. The supplement has seven coefficient slots per
chart (cap seven), 64 matrix entries (cap 64), chart degree 6/6 and
73/4096 observed rational bits in its chart/basis arithmetic. These are
fixed-domain and observed-size bounds, not elementary-operation or
internal Fraction cost counts. Both implementations and supplement share
Python exact arithmetic; this is not formal verification. There was no
new arithmetic failure or cap stop, and no upstream search was rerun.

The interface is now accepted for later use with its stated limitations.
Units or substitutes, full global/local descent, ranks, points, marked
lifts, degree-nine/integer recovery, L095's systems and the other
signatures remain unresolved. ATTEMPTS/050,059–060 and unfinished L108
are unchanged. The mathematical argument and its direct inputs are
unchanged, so this audit adds no DAG row or edge.

## Mathlib

Full matching Mathlib coverage for this exact model, field transport and
Jacobian support theorem has not been checked. Reuse L137's recorded
supporting class-group/ideal-factorization coverage; no full localization
coverage or absence claim is made. The certificates are exact Q-arithmetic,
not Lean formalizations.
