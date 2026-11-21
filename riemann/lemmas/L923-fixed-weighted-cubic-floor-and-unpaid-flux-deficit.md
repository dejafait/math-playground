# Lemma 923: a fixed weighted-cubic floor and the unpaid d=2 flux deficit

## Hypotheses

Use the exact positive theta kernel of L019 and the L058 heat family.
Let 0<lambda<=1/20 and use L874's local logarithmic coefficients S_n,
H2=(S_(i+j+2)) for 0<=i,j<=2. At the parameter in question suppose
H2 is PSD, c=(c0,c1,c2) is real with norm one, c2!=0, and H2*c=0.
All three null rows are required; no actual contact is asserted.
c0,c1 may vanish, and no uniform lower bound on abs(c2) is assumed.

Let mu be L874's full normalized theta law on u>=0, let x=u^2,
and let nu denote its pushforward to x>=0. Put

    y_j=E_mu[u^(2j)]=E_nu[x^j],  y0=1,
    q_j=(-1)^j y_j/(2j)!,
    W=(y_(i+j+1))_(0<=i,j<=2),  v=(y4,y5,y6)^T.

For the quantitative density bound use L917's audited full-band mass
enclosures, with exactly its conditional arithmetic contract (in
particular correctness of its directed operations and exponential
enclosures). Only the mass bounds and saved pi enclosure are imported;
no determinant box, parameter refinement or new moment evaluator is used.
The algebraic identities below do not depend on that arithmetic contract.

## Conclusion

Write p=c0/c2, q=c1/c2, b=S2, r=S3. The full three-row substitution is

    S4=-pb-qr,
    S5=pqb+(q^2-p)r,
    S6=(p^2-pq^2)b+(2pq-q^3)r.                         (1)

Define

    beta=-280p^2qb+124p^2r+148pq^3b-428pq^2r
         -8pqb^2-32pbr+148q^4r-8qr^2,
    T=(14!/7)(beta/156+sum_(k=1)^6 S_k q_(7-k)),
    D=T-v^T W^(-1)v,
    delta=inf_(P monic real cubic) integral x P(x)^2 dnu(x).

Then W is positive definite, and the exact contact comparison is

    delta=y7-v^T W^(-1)v,
    Phi=c^T H2'c=-(6c2^2/12!)(delta-D).                 (2)

Thus Phi<=0 is equivalent to delta>=D, not merely to delta>0.
On the single fixed interval I=[1/16,1/4], the actual full law obeys

    d(x nu)/dx >= 1/40,
    delta >= epsilon=(1/40)(3/16)^7/2800
                     =2187/30064771072000
                     >7.27*10^(-11).                  (3)

This leaves the sufficient comparison D<=epsilon **unpaid for the
actual theta contacts**. No actual flux sign follows from this attempt.

For clarity about the limitation, the enlarged class consisting only
of positive full-support laws with finite moments, the density floor
in (3), and the stated logarithmic PSD/null-row premises does not
imply D<=epsilon. The single law proportional to exp(-10u^2)du on
u>=0, with c=(0,0,1), has

    D=delta=63/16000000=0.0000039375,
    D/epsilon=1644167168/30375>54000,  Phi=0.            (4)

This is a counterexample to that enlarged sufficient comparison only.
It does not refute delta>=D or a flux sign. It is not an actual theta
law and in particular has S2=0, whereas L917 proves actual S2>0 in
this band. No inference about the existence or sign of actual contacts
is justified by (4). The completed outcome is EXPLORATION/REPRODUCTION:
a quantitative specialization and an inconclusive actual-family test,
not progress beyond the known norm theorems or a proof of RH.

## Proof

### Exact all-row reduction and the seventh raw moment

Dividing the three equations H2*c=0 only by c2 gives successively
S4=-pS2-qS3, S5=-pS3-qS4, S6=-pS4-qS5. Substitution proves (1),
without division by a logarithmic minor. Unit normalization gives
c2^2=1/(1+p^2+q^2)>0 but supplies no uniform lower bound. PSD remains
a premise locating the contact; no representing measure for H2 is used.

L874 gives Phi=-156c2^2 S7+B. Its b_n/c2^2 for n=2,...,6 are
p^2,2pq,q^2+2p,2q,1. Before (1) is inserted, B/c2^2 is exactly

    -20p^2S3-84pqS4-72(q^2+2p)S5-220qS6
    +24pqS2^2+32(q^2+2p)S2S3+80qS2S4+40qS3^2
    +48S2S5+48S3S4.

Inserting all three equations (1) and collecting terms gives beta
as stated. This retains the third row as well as the first two.
The S1 terms have canceled by L874's full null-vector identity.

The finite Taylor coefficients of g=F(lambda,z)/F(lambda,0), in
t=z^2, are q_j. L058 justifies this extraction. From g'=g(log g)'
one gets the finite identity

    S_n=-nq_n-sum_(k=1)^(n-1) S_k q_(n-k).

For n=7, q7=-y7/14!, so

    S7=7y7/14!-sum_(k=1)^6 S_k q_(7-k).

Consequently Phi/c2^2=-(156*7/14!)(y7-T), where
156*7/14!=6/12!. All moments in T and W,v have index at most six;
the coefficient of y7 has not been dropped or estimated. This proves
the flux part of (2) once the stated norm identity is justified.

### Known norm theorem and its actual-measure hypotheses

The weighted measure x dnu has a strictly positive density on every
positive interval by L019, and finite moments of every order by L058.
For every nonzero real polynomial Q of degree at most two,
integral x Q(x)^2 dnu>0: Q has finitely many roots and is nonzero
on some positive interval. Thus W is positive definite for a reason
independent of the logarithmic H2. No singular-inverse assumption is
being imposed on H2 or silently transferred from it.

Import the quadratic minimization identity from S. Boyd and
L. Vandenberghe, *Convex Optimization*, CUP (2004), corrected seventh
printing (2009), [Appendix A.5.5, pp.650-651](https://stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf).
Here the positive definite block is W, the off-diagonal block is v,
and the scalar block is y7. The monic-cubic coefficient vector is
(a0,a1,a2,1), so its squared norm is
y7+2a^T v+a^T W a. The imported identity gives its minimum
y7-v^T W^(-1)v, attained at a=-W^(-1)v. The actual positive density
has settled the inverse case; the singular range condition from the
same theorem is therefore not needed. This proves the norm assertion
of (2) and its sign equivalence. L043 is an overlap comparison, not
a sign input for the logarithmic matrix.

The equivalent orthogonal-polynomial extremal result is
W. Gautschi, *Orthogonal Polynomials: Computation and Approximation*,
OUP (2004), [Theorem 1.24, pp.8-9](https://csclub.uwaterloo.ca/~pbarfuss/Walter_Gautschi_-_Orthogonal_Polynomials_-_Computation_and_Approximation_%282004%29.pdf).
Its positive measure, infinite support and all-finite-moment hypotheses
hold here. These general minimum-norm theorems are imported, not reproved.

### Full-theta density payment on the fixed interval

Every saved full moment M0 upper endpoint in L917 is below 499/1000,
hence below 1/2. The exact-rational extraction in the certificate below
checks all 256 panels, their indices and their closed endpoints
[j/5120,(j+1)/5120]. The maximum upper endpoint is on panel255 and
is less than 0.498274. This is a consequence of L917's complete mass
enclosures, with its retained arithmetic qualification, not an estimate
for a truncated or first-summand-normalized probability.

For L019's positive first summand put v=pi exp(2u). Then

    K1(u)=4v(2v-3)exp(u/2-v),
    (log K1)'=9/2+6/(2v-3)-2v.

For u in [1/4,1/2], v>9/2 follows from pi>3 and exp(1/2)>3/2.
The displayed derivative is less than or equal to 9/2+1-9=-7/2.
Thus K1(u)>=K1(1/2). The scalar rational enclosures in the certificate
give 17/2<pi e<43/5 and exp(167/20)<4500. They imply

    K1(1/2)=4pi e(2pi e-3)exp(1/4-pi e)
            >476/4500=119/1125>1/10.

For completeness those exponential enclosures use only the positive
Taylor sum P_N(x)=sum_(j=0)^N x^j/j!, N=100. For 0<=x<102,

    P_100(x)<=exp(x)
      <=P_100(x)+(x^101/101!)/(1-x/102).

The upper bound follows since every subsequent ratio in the tail is
at most x/102. Apply it at x=1 and x=167/20; multiply the former by
the imported pi endpoints. All comparisons are exact rational ones.

Changing variables from u to x=u^2 gives the weighted density

    rho_lambda(x)=sqrt(x) exp(lambda x) K(sqrt(x))/(2M0).

On I, sqrt(x)>=1/4, exp(lambda x)>=1 and K>=K1. Therefore
rho_lambda> (1/8)(119/1125)/(1/2)=119/4500>1/40.
All higher theta terms remain in M0 and the law. Dropping them is
used only as a positive lower bound in the numerator.

Import the shifted-Legendre data from
[DLMF 18.3, Table 18.3.1](https://dlmf.nist.gov/18.3#T1)
and Gautschi's extremal theorem just cited. On [0,1] the degree-three
shifted Legendre polynomial is 20t^3-30t^2+12t-1, with squared
norm 1/7. Its monic normalization has squared norm 1/2800, the
minimum among *all* monic cubics. If ell=3/16 and a=1/16, then
P(a+ell t)/ell^3 is monic whenever P is. Hence

    integral_I P(x)^2 dx >= ell^7/2800.

Combining with rho_lambda>=1/40 gives (3) uniformly for every
monic cubic, and hence for its minimum. No particular trial cubic
is substituted for this universal lower bound. This bound alone
would certify the contact sign only after D<=epsilon is established.

### One diagnostic for that first unpaid sufficient estimate

This paragraph concerns an explicitly enlarged class, not theta.
Put Z=integral_0^infinity exp(-10u^2)du and dmu_G=exp(-10u^2)du/Z.
It is a positive full-support probability with every finite moment.
On u>=1/4, 10u^2>=(5/2)u. Thus

    Z<=1/4+(2/5)exp(-5/8)
       <1/4+16/65=129/260<1/2,

using exp(5/8)>1+5/8=13/8. Its weighted x-density is
sqrt(x)exp(-10x)/(2Z). The function u exp(-10u^2) decreases on
[1/4,1/2], since its derivative has sign 1-20u^2<0 there.
Consequently this density exceeds (1/2)exp(-5/2)>1/30>1/40
on I. The scalar bound exp(5/2)<15 is verified with the same
positive-series remainder. The diagnostic satisfies the precise
density minorization being tested, not just ordinary Gram positivity.

Integration by parts of u^(2j-1)exp(-10u^2), j>=1, has zero
boundary terms and gives y_j=((2j-1)/20)y_(j-1). Hence
y_j=(2j)!/(j!40^j). Its finite transform through order seven is
exp(-t/40)+O(t^8); thus S1=1/40 and S2=...=S7=0.
For c=(0,0,1), H2=0 is PSD and all three null rows vanish.
This is an allowed case of the enlarged hypotheses; it is expressly
excluded by stronger actual-theta information such as L917's S2 bound.

The derivative notation Phi has a concrete local interpretation here:
fix lambda_*=1/40 and K_G(u)=exp(-(10+lambda_*)u^2), and tilt by
exp(lambda u^2) near lambda_*. Gaussian domination justifies all
derivatives locally. The same moment recurrence, with 10 replaced by
10+lambda_*-lambda, makes S_n=0 for n>=2 throughout this neighborhood.
Thus H2'=0 and Phi=0. No joint entirety in all complex lambda or
identification of K_G with the theta kernel is asserted.

In this diagnostic beta=0, T=y7=27027/256000000. The monic cubic

    P_G(x)=x^3-(21/20)x^2+(21/80)x-21/1600

has integral x^(j+1)P_G(x)dnu_G=0 for j=0,1,2, by the displayed
moment formula. The same exact substitution gives its squared
weighted norm 63/16000000. The imported extremal theorem therefore
identifies this as delta, and v^T W^(-1)v=26019/256000000.
It follows that D=delta=63/16000000 and Phi=0, proving (4).

The density floor is smaller than D by
14797231137/3758096384000000>0. This disproves D<=epsilon in
the explicitly enlarged class, while leaving delta>=D true there.
It cannot disprove the actual-theta sufficient comparison, since
that class omits the exact kernel, its tilt relations and other
actual moment restrictions. No negative actual flux or actual
contact was obtained. This is the first unpaid estimate, so the
fixed-interval test stops without tuning, refinement or a new model
search. Initialization, equality/tangency, the compact residual,
other degrees, endpoint/global continuation and RH remain open.

### Verification and status

Run `python3 scripts/heat/weighted-cubic-floor-222.py` from this notebook.
The full certificate is `scripts/heat/weighted-cubic-floor-222.json`.
It records all imported mass endpoints and their source hash, exact
exponential endpoints, full all-row algebra, the seventh-moment
logarithm polynomial, the diagnostic moments and cubic, actual and
required bounds, and every check. There are 281 checks and no failures.
Independent finite-log expansion agrees with the coefficient recurrence
through seven; full heat-recurrence contraction agrees with beta-156S7.
This is local verification, not an independent critical audit of this
new write-up or of the arithmetic-library premise in L917.

An initial script invocation stopped at an unavailable symbolic-library
import before performing calculations or producing a certificate. The
saved producer instead uses self-contained exact rational arithmetic;
no numerical result from that failed invocation is used. The source
gate is `drafts/literature/2026-11-09-d2-flux-weighted-cubic-test.md`.
The known norm theorems and the Gaussian computation are reproduced/
specialized for this comparison; no originality claim is made.

### Independent conceptual audit, 9 November 2026 (step224)

**Verdict.** Accept (1)--(4), including their actual-versus-enlarged-law
qualifications, conditional on precisely the stated L917 arithmetic
contract. No correction to the mathematical claims was required.
This validates the local specialization; it adds no actual contact,
flux sign, sharper floor or result beyond the cited norm theorems.
The original EXPLORATION outcome of the sign attempt is unchanged.

**Analytic and algebraic bridge.** L058's compact derivative majorants
justify the normalized finite Taylor coefficients through seven; only
the local logarithm is used. L874's heat recurrence has the stated
negative S_(n+1) term. In its d=2 contraction the S1 terms vanish by
all three null rows, with c fixed during differentiation. Solving the
rows uses c2!=0 alone. The displayed S4,S5,S6 and beta agree with
the complete contraction, including coefficients when c0 or c1 vanish.
There is no uniform division estimate as c2 tends to zero.

The independently expanded coefficient of y7 in S7 is
1/12454041600=7/14!, positive. Hence the coefficient of y7 in
Phi/c2^2 is -156*7/14!=-6/12!, and the required raw threshold is T
with the plus sign on sum S_k q_(7-k). Since
delta-D=y7-T exactly, the sign equivalence in (2) is correct even
if D is negative. The tensor-grid check described below verifies an
algebraic identity, not hypothetical contact existence or PSD feasibility.

For the norm, x dnu has positive density on every positive interval
and all finite moments, by L019/L058. Thus its polynomial Gram W is
strictly positive definite independently of H2. The quadratic form for
a monic cubic has off-diagonal vector (y4,y5,y6), scalar y7 and block
W=(y_(i+j+1)); these indices include the extra x in the measure.
The cited positive-definite case of Schur minimization applies. There
is no singular raw block, inverse of H2, or representing-measure premise
for H2. Gautschi's infinite-support hypothesis is satisfied as well.

**Complete mass and fixed floor.** All 256 full M0 records agree with
the L917 certificate, cover the closed band without gaps and have
positive lower endpoints and upper endpoints below 499/1000. The
maximum is panel255 and is below 0.498274. The L917 inclusion proof
and library contract are imported; this audit does not replay its
quadrature or remove that contract. All three scalar exponential pairs
were independently reconstructed as exact rationals, including their
full positive-series remainders and the imported pi endpoints.

On [1/4,1/2], v>9/2 gives (log K1)'<-7/2. At the right endpoint,
17/2<pi e<43/5 gives 4pi e(2pi e-3)>476 and
1/4-pi e>-167/20; hence K1>119/1125. The change of variable
du=dx/(2sqrt(x)) gives precisely the displayed weighted density.
Its lower bound 119/4500 exceeds 1/40 using the full M0<1/2;
the omitted positive theta terms only enlarge the numerator.
The Legendre normalization is 1/(7*20^2)=1/2800 and the affine
change contributes ell^7. Thus the uniform infimum is indeed at
least 2187/30064771072000>7.27*10^(-11), without substituting a
trial polynomial for the minimum.

**Gaussian scope.** The stated split at u=1/4 bounds the complete Z
by 129/260<1/2. On the fixed interval u exp(-10u^2) is decreasing,
so its weighted density exceeds exp(-5/2)/2>1/30. Integration by
parts has zero boundary terms for every j>=1 and gives the recorded
moments. The cubic's three orthogonalities and exact norm have been
independently checked without invoking the producer's matrix solver.
The local Gaussian tilt keeps every S_n, n>=2, zero and therefore
really has Phi=0. Only local Gaussian domination is required; L058's
global theta entirety is not transferred to this different kernel.
Its S2=0 excludes it from the actual L917 family. The factor greater
than 54000 refutes only D<=epsilon in the stated enlarged class;
it neither refutes delta>=D nor shows a negative actual flux.

**Complete finite evidence.** Run
`python3 scripts/heat/weighted-cubic-audit-224.py`. The separate
certificate `scripts/heat/weighted-cubic-audit-224.json` passes 27
aggregate checks with no failures and records all 256 mass checks,
complete scalar endpoints, input hashes and actual/required bounds.
The original producer and certificate are preserved.

For beta, the independent check contracts the heat recurrence directly
on c/c2=(p,q,1), with S4,S5,S6 given by (1). Both expressions have
separate degrees at most (2,4,2,2,1) in (p,q,b,r,S1). Equality is
checked on the complete 3*5*3*3*2=270 rational tensor grid; these
distinct nodes determine the polynomial, by successive univariate
interpolation. The separately inspected S7 term is exactly -156S7.
For the raw logarithm, the checker uses all multiplicity partitions
sum j*m_j=7 in the finite logarithmic series, including each multinomial
coefficient, and compares every resulting coefficient to the saved
S7 polynomial. These are complete exact identities, not numerical
samples. Analytic hypotheses and sign interpretation were checked
above, independently of the finite check flags.

The approved source scope is
`drafts/literature/2026-11-09-weighted-cubic-floor-audit.md`.
L019/L058/L874/L917 are precisely the direct mathematical inputs
already recorded in the DAG. L043 is only a contrast. The actual
deficit, contact existence, initialization/equality, compact signs,
other degrees and global continuation remain unresolved; the fixed
floor signing route stays parked pending a materially new actual bound.

## Mathlib

Full matching coverage for the actual-theta contact/norm comparison
has not been checked. Supporting formal coverage for Schur minimization,
orthogonal-polynomial extremality, the Legendre normalization and these
theta bounds is also not checked here; unknown availability is not
absence. The precise mathematical sources used are cited above.
