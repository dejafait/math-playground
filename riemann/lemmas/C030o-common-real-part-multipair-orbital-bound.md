# Corollary C030o: a uniform common-real-part multipair orbital bound

## Hypotheses

Let m>=1 and n>=2m be finite integers. Let a,r,x>0, let
b_1,...,b_m be real, and assume x*sum_l |b_l|<=1/4. Put

    q=2m, S2=sum_l b_l^2, A=sum_l |b_l|,
    B=diag(b_1,-b_1,...,b_m,-b_m),
    D_bvec=diag(a+i*b_1,a-i*b_1,...,a+i*b_m,a-i*b_m,r,...,r).

For each rank j=0,...,n, use probability Haar on U(n) and define

    Z_(j,bvec)(x)=integral exp(-x*tr(D_bvec*V*P_j*V*))dV,
    G_(j,bvec)(x)=-Z'_(j,bvec)(x)/Z_(j,bvec)(x),
    E_(k,bvec)(x)=(G_(k+1,bvec)-G_(k,bvec))
                    -(G_(k+1,0)-G_(k,0)),  0<=k<n.

Here P_j is any rank-j orthogonal projection on C^n. The zero-phase
reference retains all q entries a. The derivative holds a,r,bvec fixed;
every rank and reference has its own partition function. At n=q there
are no r entries. Both signs of every b_l and a-r, a=r, zero phases,
repeated spectra and adjacent endpoint ranks are included.

Use C030l's full real tilted-array comparison for weak ordered top
rows, arbitrary fixed real fields and separate normalizers. It is
the comparison proved inside C030l, not merely its scalar rank bound.
The external degree-two Haar integration theorem is cited precisely
and specialized below. No complex stochastic order or independence
of disjoint two-dimensional corners is assumed.

## Conclusion

Every Z_(j,bvec)(x) is positive real on the full stated closed window,
and

    Z_(j,bvec)(x)/Z_(j,0)(x) >= 95/96,
    |G_(j,bvec)(x)-G_(j,0)(x)| <= (64/95)*x*S2.        (1)

Consequently an absolute constant, independent of m,n and all real
contrasts, is

    |E_(k,bvec)(x)| <= (128/95)*x*S2.                 (2)

At j=0,n the response in (1) is exactly zero. Thus 64/95 suffices
in (2) when k=0 or k=n-1. No sharpness is asserted; C030n has the
better constant 64/95 for the adjacent defect when m=1.

This is the result of bounded attempt1214; independent conceptual
audit1216 passes the full stated claim, as recorded below. The prior
EXPLORE assessment1212/coverage1213 did
not locate a matching bound. POTENTIALLY_NEW describes that limited
comparison, not certified originality. This is a finite-family input,
not a complete RH candidate. Unequal pair real parts, arbitrary
remaining backgrounds, actual-Xi degree/time transfer, all-degree
positivity, theta signing and graph realization are not proved.

## Proof

### The imported second moment and its specialization

Write M=tr(B^2)=2*S2; tr(B)=0. Import B. Collins and P. Sniady,
*Integration with respect to the Haar measure on unitary, orthogonal
and symplectic group*, [arXiv math-ph/0402073v1, 26 February 2004](https://arxiv.org/pdf/math-ph/0402073v1),
Corollary 2.4, equations (11)-(12), p5, with the Weingarten function
in (9)-(10), pp4-5, and the dimension qualification in Proposition 2.5,
p6. The source gate1213 inspected these statements. The theorem
integrates monomials in unitary entries and conjugates with probability
Haar measure. We use degree two in each, in dimension q>=2, so the
two partitions of 2 are permitted and the following denominators
are nonzero. The two Weingarten coefficients are

    Wg_q(id)=1/(q^2-1),
    Wg_q((12))=-1/(q*(q^2-1)).

The four terms of Corollary 2.4 give, for any p,s,i,h in {1,...,q},

    E |W_pi|^2 |W_sh|^2
      = (1+delta_ps*delta_ih)/(q^2-1)
         -(delta_ps+delta_ih)/(q*(q^2-1)).             (3)

This includes coincident indices and q=2. No higher-degree rational
formula, pole limit or asymptotic approximation is being used.

Let beta_p be the diagonal entries of B and set

    H_i=(W* B W)_ii=sum_p beta_p |W_pi|^2.

Multiply (3) by beta_p*beta_s and sum over p,s. The constant term
and the delta_ih term without delta_ps vanish because sum_p beta_p=0;
the remaining two terms give exactly

    E H_i H_h = M/(q^2-1)*(delta_ih-1/q).             (4)

For any real vector lambda, define

    T_lambda=sum_i lambda_i H_i,
    phi(lambda)=E_W cos(T_lambda).

Equation (4) yields

    E H_i^2=M/(q*(q+1)),
    E T_lambda^2=M/(q^2-1)
                        *(sum_i lambda_i^2-(sum_i lambda_i)^2/q).
                                                               (5)

These are necessary finite contractions of the cited theorem, not a
reproof of Haar integration. All entries and integrands are bounded
on compact parameter sets, so the displayed integrations and finite
sums can be interchanged.

### A uniform coordinate gradient and a positive phase average

For U>0 and lambda in [0,U]^q, write s=sum_i lambda_i. Since
lambda_i^2<=U*lambda_i,

    sum_i lambda_i^2-s^2/q <= U*s-s^2/q
                           =q*U^2/4-(s-q*U/2)^2/q
                           <=q*U^2/4.              (6)

Differentiation under the compact Haar integral gives
partial_i phi=-E H_i*sin(T_lambda). Cauchy--Schwarz, |sin v|<=|v|,
and (5)-(6) imply, everywhere on this cube,

    |partial_i phi|
       <= sqrt(E H_i^2 * E T_lambda^2)
       <= M*U/(2*(q+1)*sqrt(q-1))
       = S2*U/((q+1)*sqrt(q-1))
       <= 2*S2*U/(3*q) =: L_U.                     (7)

For the last inequality, square the positive factors and use

    4*(q+1)^2*(q-1)-9*q^2
       =(q-2)*(4*q^2+3*q+2)>=0,  q>=2.

Thus the sum of the q coordinate costs is at most (2/3)*S2*U;
there is no factor growing with m. This estimate needs no small-phase
hypothesis. Trace zero and whole-block averaging supply its dimension
factor; independent subblocks were never used.

Also cos v>=1-v^2/2, so (5)-(6) give on [0,t]^q

    phi(lambda)>=1-q*S2*t^2/(4*(q^2-1))
                >=1-S2*t^2/6.                     (8)

Here q/(q^2-1)<=2/3 for q>=2, because
2*(q^2-1)-3*q=(q-2)*(2*q+1)>=0. If t*A<=1/4 then
S2<=A^2 implies phi(lambda)>=1-1/96=95/96. This includes the
closed boundary and the case S2=A=0.

### Whole-block orientation under the real reference

Fix j and put Q=V P_j V*, C=Q_[q] for its leading q-by-q corner,
S=tr(C), and delta=a-r. Then

    tr(D_bvec Q)=r*j+delta*S+i*tr(B*C).

The real-reference normalized law of Q has density proportional to
exp(-t*delta*S) relative to its Haar orbital law, with its own positive
denominator. The scalar exp(-r*t*j) cancels only in this rank's ratio.
Conjugation of Q by diag(W,I_(n-q)), W in U(q), preserves both its
Haar law and S. Hence it preserves this real tilted probability law.

Average the phase additionally over probability Haar W in that block.
If lambda(t,Q) is the ordered spectrum of t*C, invariance gives its
orientation average as E_W exp(-i*T_lambda). A permutation exchanging
the two coordinates in every pair conjugates B to -B. Left invariance
of Haar under that permutation makes this expectation real, equal to
phi(lambda). The same holds when some b_l vanish or have opposite signs.
There is no conditioning on a possibly null spectral event.

It follows, for all real t>0, that

    F_j(t):=Z_(j,bvec)(t)/Z_(j,0)(t)
       = [integral exp(-t*delta*S)*phi(lambda(t,Q))dV]
                    /[integral exp(-t*delta*S)dV].    (9)

Every lambda(t,Q) lies in [0,t]^q because 0<=Q<=I. Thus (8)
proves F_j(t)>=95/96 on t*A<=1/4, separately for each rank.
Z_(j,0)(t)>0, so the complex partition function itself is positive
real on this window. F_j is real and smooth for all t>0: in fixed
Haar variables the numerator can equivalently use
cos(t*tr(B*C)), and the denominator is positive. On compact t intervals,
S and tr(B*C) are bounded and every fixed derivative is dominated.
This proves smoothness without differentiating eigenvectors or
eigenvalue paths. Positivity and continuity also give a real nonzero
neighborhood of each point on the closed window.

### Fixed-field comparison pays the full physical derivative

Suppose first q<n. Under the scaled orbit Y=t Q, the real probability
law in (9) has the fixed field exp(-delta*tr(Y_[q])). In C030l's
notation this is c_q=-delta, with every other proper-corner field zero.
It does not become -t*delta on the already scaled orbit. Denote the
full corner-eigenvalue array law by nu_t. Its weak top row is

    Lambda_j(t)=(0^(n-j),t^j).

For eta>0 the top rows obey

    Lambda_j(t)<=Lambda_j(t+eta)<=Lambda_j(t)+eta*(1,...,1).

C030l's real-array comparison, at the same fixed field, therefore gives
in expectations of continuous increasing array tests

    nu_t <= nu_(t+eta) <= translation_eta(nu_t).      (10)

For the second comparison, adding eta*I to Y translates every corner
eigenvalue by eta. Its weight gains the constant exp(-delta*q*eta),
which cancels with that translated law's own normalizer. No different
rank or time normalizers have been equated. The repeated top rows,
both signs of delta and delta=0 are within C030l's established scope.

Let z_i, 1<=i<=q, be the coordinates of row q and let Delta denote
expectation at t+eta minus expectation at t. From (10), applied to
each coordinate, one has

    0<=Delta E z_i<=eta,
    0<=Delta E sum_i z_i<=q*eta.                     (11)

Although phi itself need not be increasing, (7) produces admissible
tests. Put U=t+eta and clip_U(v)=min(U,max(0,v)). On all of R^q define

    Psi_+(z)= phi(clip_U(z_1),...,clip_U(z_q))
                         +L_U*sum_i clip_U(z_i),
    Psi_-(z)=-phi(clip_U(z_1),...,clip_U(z_q))
                         +L_U*sum_i clip_U(z_i).

On [0,U]^q their coordinate derivatives are respectively
partial_i phi+L_U and -partial_i phi+L_U, all nonnegative by (7).
Each coordinate section is therefore nondecreasing on the cube;
composition with the increasing clipping maps makes Psi_+ and Psi_-
continuous increasing functions on all of R^q. As full-array tests
they simply ignore every row other than q. No ordering of disjoint
corners, simultaneous coupling or complex law is used.

Both nu_t and nu_(t+eta) have row-q support in [0,U]^q. The first
order in (10), applied to these two tests, gives

    -L_U*Delta E sum_i z_i <= F_j(t+eta)-F_j(t)
                             <= L_U*Delta E sum_i z_i.

By (11),

    |F_j(t+eta)-F_j(t)| <= q*L_U*eta
                        =(2/3)*S2*(t+eta)*eta.      (12)

Use the already proved smoothness of the fixed-Haar quotient (9),
divide by eta, and let eta decrease to zero. This proves

    |F_j'(t)| <= (2/3)*S2*t,   t>0.                 (13)

Both the observable and the real tilt in (9) vary with t, so this is
the full derivative holding a,r,bvec fixed. It is not a derivative
at frozen real contrast t*delta. Since (7) and (12) hold for every U,
the right difference quotient is valid also when t*A=1/4; no larger
phase-window nonvanishing or uniform Taylor remainder is assumed.

### Full block, endpoints and the separate logarithmic responses

If q=n, the corner is the whole matrix and tr(Y_[q])=t*j. The real
tilt is constant on this orbit, and cancels in its own normalizer.
Instead of using a nonexistent proper-corner field, (9) becomes

    F_j(t)=phi(0^(q-j),t^j).

Ordinary differentiation of this fixed spectrum and (7) with U=t give
|F_j'(t)|<=j*L_t<=q*L_t=(2/3)*S2*t. Thus (13) holds in this case
as well, including q=n=2. The lower bound (8) is unchanged. At rank
zero Q=0, while at rank n its q-corner is I_q and tr(B)=0. Hence
F_0=F_n=1 and their responses vanish exactly in every dimension.
If all b_l=0, every F_j=1. No division by S2, b_l or delta was used.

Finally at every point of the closed window,

    G_(j,bvec)-G_(j,0)=-F_j'(x)/F_j(x).

Equations (8)-(9) and (13) imply

    |G_(j,bvec)-G_(j,0)|
       <= ((2/3)/(95/96))*x*S2=(64/95)*x*S2.

The difference of the two adjacent responses satisfies (2) by the
triangle inequality; each has kept its own positive denominator.
At k=0,n-1 one response is zero, giving the endpoint improvement.

### Independent conceptual audit1216

The exact audit approved in assessment1214/approval1215 passes. This
audits the existing finite-family argument; it does not improve its
constants, extend its hypotheses or certify originality. The following
checks use the cited Haar theorem and C030l as qualified above, without
independently reauditing the external general integration theorem.

**All index cases and dimension factors.** The four permutation terms
in (3) have respectively the Kronecker factors 1, delta_ps*delta_ih,
delta_ps and delta_ih, with the displayed two Weingarten coefficients.
When both indices coincide (3) is 2/[q*(q+1)]; when just one pair
coincides it is 1/[q*(q+1)]; when neither coincides it is 1/(q^2-1).
Thus no exceptional q=2 or repeated-index case was discarded.
Contraction against beta_p*beta_s leaves M*delta_ih-M/q in the
numerator of (4), since the other terms contain (sum beta_p)^2=0.
Its row sums vanish, consistent with sum H_i=0. The diagonal moment
is M/[q*(q+1)], and the variance in (5) is nonnegative. Substituting
(6) into the product of these two moments gives exactly
M*U/[2*(q+1)*sqrt(q-1)], with no missing q or factor two.
The factorizations in (7) and (8) are exact, nonnegative at every
q>=2, and vanish at q=2. Using S2<=A^2 and t*A<=1/4 gives the
required 95/96 floor, including equality in the window condition.

**The real law and its order.** The block action preserves both the
Haar orbit and S, so it preserves the normalized weight for every real
delta. Averaging that one whole block is legitimate by compact Fubini;
it does not factor its smaller corners. The pair-exchange permutation
reverses B for arbitrary signed b_l. This proves the reality in (9),
not an assumption of positive complex weights. All later comparisons
are between the separately normalized real laws.

C030l's full-array comparison is sufficient: its finite-lattice
conditional CDF comparison allows either sign of each fixed real
field; its decreasing-coordinate connectivity argument supplies
irreducibility rather than assuming it. Its continuum limit first
uses strict rational rows and positive limiting normalizers. Its
ordered rational approximation and bounded Haar continuity then
include the repeated top rows here. No uniform mixing-time limit,
Lebesgue density on a collapsed polytope or scalar-rank-only inference
is needed. For q<n, c_q=-delta is indeed a proper-corner field.
Translation by eta changes that weight by exp(-delta*q*eta), which
cancels only in its own normalized law. This verifies both inequalities
in (10), and applying the upper one to each z_i gives (11).

**Global tests and physical differentiation.** Both clipped tests are
globally increasing: each coordinate section on the cube has derivative
at least zero, and clipping extends that section constantly beyond
its endpoints. Their continuity suffices for C030l; differentiability
at a clipping boundary is unnecessary. Applied to the lower comparison
in (10), the two tests give both signs of (12). The upper comparison
pays the entire q*eta bound for the trace change. At fixed positive t,
letting eta decrease to zero yields (13) by smoothness of (9).

For an explicit check of what is being differentiated, set
R=tr(B*C), and let E_t and Cov_t be expectation and covariance under
the normalized real-reference Haar law proportional to exp(-t*delta*S).
Differentiating its fixed-Haar quotient, with all parameters fixed,
gives

    F_j'(t)=-E_t[R*sin(t*R)]-delta*Cov_t(S,cos(t*R)).

Both terms are finite on compact time intervals. The comparison proof
bounds their sum, including the covariance term; it does not set that
term to zero or freeze t*delta. No separate covariance estimate is
asserted. The finite-difference bound holds for every U=t+eta, so using
eta>0 at t*A=1/4 does not assume positivity outside the window.
At the endpoint itself, (8)-(9) and continuity supply the neighborhood
needed for the real logarithmic derivative.

**Exceptional cases and final cost.** For q=n, the real trace is t*j,
constant on its orbit, so the deterministic whole-spectrum formula
replaces the proper-corner comparison. Its derivative has j coordinate
terms, each bounded by L_t, hence the same upper bound; this includes
q=n=2. At ranks0/n the phase is identically zero because the corner
is respectively0/I_q and tr(B)=0. At A=0 the same is true at every rank.
No division by a phase, contrast or S2 has been used. Repeated spectra
and either sign of a-r require no limiting complex-law argument.
Finally (2/3)*(96/95)=64/95 for each rank's own ratio; the adjacent
triangle inequality gives128/95, with64/95 when one rank is an endpoint.
The n=2 endpoint overlaps cause no exception. These checks retain every
claim of (1)-(2) without a new mathematical dependency.

### Source and downstream qualifications

C030l's full comparison uses the orbital-array law of G. Olshanski,
*Projections of Orbital Measures, Gelfand-Tsetlin Polytopes, and Splines*,
J. Lie Theory 23 (2013), 1011-1022,
[Corollary 3.2, p1017](https://www.heldermann-verlag.de/jlt/jlt23/olshla2e.pdf),
for strict real top rows, and supplies its own weak-row extension.
Its cited real rank-comparison source is S. Sra, *On some positivity
properties of the Riemann Xi function*,
[author v3, 2 November 2026](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf),
Lemma C.7/Theorem C.8, printed pp25-27. Those general source results
and the Haar integration theorem are imported, not independently
reproved here. The finite moment contraction, cube gradient estimate
and its fixed-field application are the work needed for this target.
C030m/n motivate the mechanism and compare scope/constants; their
single-pair inequalities are not applied under intermediate complex laws.

The common real part within the entire q-block is essential to the
orientation averaging under a trace-only real tilt. The common value r
outside it is what makes the remaining real field a single proper-corner
trace. Nothing here establishes the necessary estimates for unequal
real parts or arbitrary backgrounds. The phase restriction and cost
have not been verified for actual-Xi data at required degree/time scales.
The finite-reference factor budget and other signed-complement
hypotheses remain unproved, as do actual-Xi positivity and realization.

## Mathlib

Full matching coverage of (1)-(2), the nonlinear orientation-gradient
estimate, the real tilted-array comparison and the Haar-moment source
is unchecked. No absence claim is made. Haar invariance, finite sums,
Cauchy--Schwarz, bounded differentiation and elementary monotone-test
estimates support this proof; matching formal theorem names were not
checked and no formalization is claimed.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
