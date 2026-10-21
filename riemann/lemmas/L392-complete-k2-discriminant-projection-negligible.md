# Lemma 392: the complete k=2 projection is lower order

## Hypotheses

Use the fixed actual functions and ordinary height jets of L390:

    f=F_0/A, L=log(2+t), x=f, y=f'/L, z=f''/L^2,
    M=(z^2+3xz/2+x^2/16-y^2)/2,
    K=((z-x/4)-iy)^2/2,
    E=R^2=pi^(-it) Gamma(1/4+it/2)/Gamma(1/4-it/2),
    Z=zeta(5/2+it), c=1/(4pi), U=x^2+y^2+z^2.

Let Delta be the complete actual normalized discriminant of L390.
Write ell=log H, with real H tending to infinity. There is no RH,
zero simplicity, noncoincidence, phase independence, eventual sign,
or growing-twist assumption. Fixed response heads precede height limits.

## Conclusion

The complete sharp-interval k=2 projection satisfies

    I_2(H)=(1/(2H)) integral_[H,2H] Re(K^2 E^2 Z^4) dt
           =o(ell^4).                                      (1)

For each fixed N, replacing Z by Z_N=sum_(n<=N)n^(-5/2-it)
gives I_(2,N)(H)=O_N(1). Each connector in the proof has absolute
integral O_N(H^(2/3)); the shifted horizontal edge costs O_N(H).

Together with the separately audited L390/L391, this yields

    (1/H) integral_[H,2H] Delta^2 dt
      =(c^4/H) integral_[H,2H] (M^2+|K|^2/2)|Z|^4 dt
          +o(ell^4).                                      (2)

The remaining balanced integral has no evaluated leading coefficient
here. In particular (2) does not establish beta>0 or the requested
complete asymptotic. No sign-set improvement, pointwise discriminant
sign, common-zero upper count, actual-theta positivity or RH consequence
follows. The separate critical audit below validates this specialization
without changing its hypotheses or conclusions.

## Proof

This is a local REPRODUCTION under the unchanged prior EXPLORE
assessment `drafts/literature/2026-10-10-discriminant-second-moment-leading-scale.md`.
The four-factor contour application is necessary: L390's previous
coarse connector certificate exceeded the required scale. We reuse
L391's audited sharper jet estimates, not that failed certificate.
No new moment or subconvexity theorem is claimed or reproved.

### Imported bounds and exact ordinary jets

J. Bourgain, *Decoupling, exponential sums and the Riemann zeta
function*, [arXiv:1408.5794v2, Theorem 5 (0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2),
gives the unconditional bound t^(13/84+epsilon). L391 specializes it
with epsilon=1/168 to the weaker t^(1/6) bound, interpolates by
Phragmen--Lindelof to the absolutely bounded line sigma=11/10,
and applies Cauchy's derivative estimate on disks of radius 1/ell.
Its complete argument, including disks left of sigma=1/2 and at the
sharp height endpoints, proves for h_p(s)=zeta^(p)(s), p<=2,

    |h_p(sigma+it)| <= C_p ell^p H^B(sigma),
    B(sigma)=(5/18)(11/10-sigma),
    1/2<=sigma<=21/20, H<=t<=2H.                     (3)

Superscripts on zeta mean complex s derivatives. The bounds hold in
the slightly enlarged height intervals needed for the Cauchy disks.
Thus (3) is an already proved supporting input, not an assumption
about a four-factor mean. No modified-Gonek input is needed for the
present horizontal edge, because its gamma carrier cancels exactly.

For tau in the closed rectangle H<=Re tau<=2H,
-11/20<=Im tau<=0, put s=1/2+i tau and L=Log(2+tau).
L391's exact holomorphic ordinary-jet identities are

    (x,y,z)=-R(D_0,D_1,D_2),
    D_0=h_0(s),
    D_1=i(h_1(s)+Omega h_0(s))/L,
    D_2=(-h_2(s)-2Omega h_1(s)-Omega^2 h_0(s)
                                      +i Omega' h_0(s))/L^2,
    Omega=[Psi(1/4+i tau/2)+Psi(1/4-i tau/2)-2log pi]/4.
                                                               (4)

Here R'/R=i Omega and Omega' is a tau derivative. On this rectangle
Omega=O(ell), Omega'=O(H^(-1)), |L| comparable to ell.
All factors are holomorphic on a neighborhood of the rectangle.
Gamma and polygamma poles, and the zeta pole, have real height zero;
the logarithm has no cut or zero here. The nonvanishing E admits its
holomorphic root R, chosen to agree with the actual carrier on the
real interval. These are the same rectangle and branch as in L391.

### Exact cancellation and complete finite expansion

On the real line x,y,z are real and |E|=1. Therefore

    conjugate(K^2 E^2 Z_N^4)
       =[(z-x/4)+iy]^4 E^(-2) conjugate(Z_N)^4/4.

Define the entire fixed head V_N(tau)=sum_(n<=N)n^(-5/2+i tau)
and B_*(tau)=D_2-D_0/4+iD_1. Substitution of (4) gives exactly

    [(z-x/4)+iy]^4 E^(-2) V_N^4/4
       =R^4 E^(-2) B_*^4 V_N^4/4
       =B_*^4 V_N^4/4.                              (5)

The equality uses R^4=E^2; there is no residual fast gamma phase.
Equation (5) supplies the holomorphic extension of the conjugated
real-line integrand. It is not complex conjugation off the real line.
In particular no modulus-square replacement is made.

Every summand of B_* is a constant times
Omega^b (Omega')^e L^(-m) h_p(s), with p<=2 and
m=p+b+2e. This follows directly by inspecting (4): D_0 has tuple
(p,b,e,m)=(0,0,0,0); D_1 has (1,0,0,1),(0,1,0,1);
D_2 has (2,0,0,2),(1,1,0,2),(0,2,0,2),(0,0,1,2).
Multiplication by the constants -1/4 and i changes none of these
relations. Consequently every monomial in B_*^4 has the form

    w(tau) product_(j=1)^4 h_(p_j)(s),
    d=sum_j p_j<=8,
    w=C Omega^b (Omega')^e L^(-m), m=d+b+2e,
    |w|<=C ell^(-d).                                (6)

There are only finitely many such monomials, with fixed coefficients.
The bound includes all Omega' terms and remains valid if Omega or
Omega' vanishes. Ordinary differentiation was done before dividing
the jets by L^j; no derivative of a pointwise divisor was discarded.

Expanding V_N^4 gives finitely many terms a_q q^(i tau), where
q=n_1 n_2 n_3 n_4<=N^4 and a_q is the sum of the coefficients
(n_1 n_2 n_3 n_4)^(-5/2) having that product. On the whole fixed
rectangle |q^(i tau)|=q^(-Im tau)<=q^(11/20), so each such factor
is bounded by a constant depending on N. No growing-head estimate
is required or asserted.

### Sharp horizontal edge and both connectors

Move the real-height segment to tau=t-i11/20, H<=t<=2H.
There Re s=21/20. For every p<=2, the absolute derivative series
gives

    |h_p(21/20+it)| <= sum_(n>=1)(log n)^p n^(-21/20)<infinity,

with (log n)^0 interpreted as 1. From (6), each monomial has bounded
modulus there; each fixed head is bounded as above. Hence the
horizontal integral of B_*^4 V_N^4/4 is O_N(H).

At either connector tau=t_0-i v with t_0=H or 2H and
0<=v<=11/20, write sigma=1/2+v. Applying (3) to all four factors
in (6) cancels the factor ell^d against ell^(-d), giving

    |w product_j h_(p_j)(s) q^(i tau)|
       <= C_N H^(4B(sigma)) <= C_N H^(2/3).          (7)

Indeed B decreases across this interval and 4B(1/2)=2/3.
There is no extra power from a carrier, by (5). The fixed connector
length is 11/20, so both absolute connector integrals are
O_N(H^(2/3)). The rectangle contains no pole or branch cut.
Cauchy's theorem bounds the original integral by the horizontal and
both connector budgets, yielding

    |integral_[H,2H] conjugate(K^2 E^2 Z_N^4) dt|
       <= C_N(H+H^(2/3))=O_N(H).                    (8)

Conjugation and taking one half of the real part recover precisely
the physical k=2 term in L390 (2). Thus I_(2,N)(H)=O_N(1).
This controls sharp endpoints directly, without smoothing or an
unstated endpoint limit. Its ratio to the required ell^4 scale tends
to zero at each fixed N.

### Uniform complete-tail transfer and assembly

Set eta_N=sum_(n>N)n^(-5/2) and M_0=zeta(5/2). On the real line
|Z|,|Z_N|<=M_0, |Z-Z_N|<=eta_N and |E|=1. Telescoping four
factors gives |Z^4-Z_N^4|<=4M_0^3 eta_N. Also L390 proves
|K|<=C U. Hence pointwise

    |Re(K^2 E^2 (Z^4-Z_N^4))/2| <= C eta_N U^2.      (9)

L390's complete sharp fourth-jet budget is
H^(-1) integral U^2=O(ell^4), imported through L389 from
H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function
Z(t)*, [arXiv:2304.05178v1, Theorem 3 and its defining asymptotic](https://arxiv.org/html/2304.05178v1),
for fixed ordinary orders zero through two. We use its already
justified nonnegative sharp-interval restriction and Hardy
normalization in L390, not a twisted version of that theorem.
Thus (9) gives

    |I_2(H)-I_(2,N)(H)| <= C eta_N ell^4,

uniformly in N and sufficiently large real H. Dividing by ell^4,
taking the height limsup for each fixed N using (8), and then letting
N tend to infinity gives

    limsup_(H->infinity) |I_2(H)|/ell^4 <= C eta_N ->0.

This proves (1). It does not interchange uncontrolled limits or use
a constant uniform in N in (8). Response-derivative errors and tails
were already retained in L390's physical replacement; only the value
Z is truncated in this separate projection estimate.

Finally L390 gives the complete square replacement error O(ell^3)
and exactly its k=0, k=1, k=2 decomposition. L391 proves the complete
k=1 mean o(ell^4), and (1) supplies the k=2 mean. Adding these
three justified error estimates gives (2), with c^4 unchanged.
The surviving integral is nonnegative, but nonnegativity alone
does not give a nonzero coefficient at scale ell^4. Its coefficient
evaluation and noncancellation remain independent obligations.

### Separate critical audit — 2026-10-11, step 53

This REPRODUCTION audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-11-complete-discriminant-second-moment-audit.md`.
It checks the existing specialization, reusing the audited L390/L391
inputs rather than reproving Bourgain or the Hardy fourth-moment theorem.

**Carrier and ordinary jets.** On the real interval, conjugation changes
the sign of i in K and replaces E by E^(-1). Since
z-x/4+iy=-R(D_2-D_0/4+iD_1), its fourth power contributes R^4,
with positive sign. R^4 E^(-2)=1 exactly. Thus (5) is the holomorphic
extension of the conjugated integrand, including the factor 1/4 from
K^2; the additional factor 1/2 in I_2 is applied only after integration.
The exact D_2 contains i Omega', and no differentiation of L^(-j) is
intended: these are ordinary f derivatives divided by L^j.

In B_*, each term has p+b+2e=m, as explicitly listed above. Hence
its coefficient is O(ell^(-p)); an Omega' term has still more decay.
Products of four such terms have coefficient O(ell^(-sum p_j)),
uniformly throughout the rectangle. No division by Omega, Omega',
f or a zero-dependent quantity is used.

**Both edges and endpoints.** The fixed V_N head is holomorphic and
bounded by an N-dependent constant on this rectangle. The displaced
critical factors have real part 21/20, where all derivatives through
order two have absolutely convergent Dirichlet series. Their normalized
coefficients are bounded, so the long edge costs O_N(H). On the two
connectors, audited L391 (11) bounds the four factors by
O(ell^d H^(4B(sigma))). Cancellation of ell^d leaves exponent at most
4B(1/2)=2/3. The Cauchy disks in that input include H and 2H and
the small left extension of the critical line. The connectors have
fixed length. No carrier remains to increase this exponent, and no
pole or logarithmic cut intersects the rectangle. Consequently the
full complex integral, before taking its real part, is O_N(H).
This verifies sharp endpoints directly, and is a different certificate
from the preserved historical coarse O(H^2) estimate.

**Full tail and physical assembly.** The four-factor telescoping bound
uses |Z|,|Z_N|<=zeta(5/2) with constants independent of N. Since
|K|^2<=C U^2 and L390 supplies integral U^2/H<=C ell^4,
the complete k=2 mean differs from its fixed-head mean by at most
C eta_N ell^4. At each fixed N, O_N(1)/ell^4 tends to zero;
only afterward is eta_N sent to zero. The result is o(ell^4), not a
uniform O(1) bound for the infinite head. Adding this to L391's
complete k=1 estimate and L390's O(ell^3) square-replacement error
gives exactly (2). Those inputs already retain response-derivative
errors and envelope curvature. No new mathematical dependency is needed.

The k=2 estimate and the balanced reduction pass unchanged. The
coefficient is verified separately in L393's audit; this audit itself
supplies neither a sign theorem nor a common-zero estimate.

## Mathlib

Full matching coverage for the physical k=2 estimate, Bourgain's
subconvexity theorem and these Hardy fourth moments has not been
checked. Supporting Cauchy, contour, finite-polynomial and norm facts
would not by themselves formalize the imported analytic inputs.
No Lean verification, library absence or novelty beyond the checked
sources is asserted. This is a local known-tool specialization, not
a complete RH candidate.
