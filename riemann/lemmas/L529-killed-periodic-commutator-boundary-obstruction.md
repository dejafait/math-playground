# L529 — Boundary obstruction to the killed periodic commutator

## Hypotheses

Fix 0<a<A<infinity and ell=2a>log(2), I=(0,ell). Use complex
L2(I), with inner product conjugate linear in the first entry, zero
extension E, restriction R_I and Fourier transform
hat f(xi)=integral f(x)exp(-i xi x)dx. Retain L522's operator exactly:

    Psi(xi)=(1/2)log(1+xi^2), n(x)=exp(-|x|)/(2|x|),
    c=log(2pi), d_n=log(n), w_n=Lambda(n)/sqrt(n),
    mu=nu_rho+sum_(n>=2,d_n<=2A) w_n(delta_(d_n)+delta_(-d_n))
                         -2cosh(x/2)1_(|x|<=2A)dx,
    rho(x)=exp(-x/2)/(1-exp(-2x))-exp(-x)/(2x), x>0,
    A_I=G_I-cI-R_I K_mu E, Dom(A_I)=Dom(G_I).               (1)

Here nu_rho has even density rho, K_mu is whole-line convolution,
and G_I is the self-adjoint operator of the zero-extension
smooth-core logarithmic part form. It is the killed realization,
not a periodic multiplier or subordination of killed Brownian motion.
L514 supplies the finite-energy/core-domain identification used below;
L515 supplies bounded signed convolution and self-adjointness on the
displayed domain. Both shifts, cutoff equality and the signed pole
are retained. Unlike the nullvector applications in L522, this test
requires no nullvector, trace assumption or nonresonance assumption.

Let

    B=h(A_I), h(s)=s/(1+s^2),
    D=D_per=-i d/dx,
    Dom(D)={u in H1(0,ell): u(0)=u(ell)},
    Q_B(phi,psi)=<B phi,D psi>-<D phi,B psi>.               (2)

The self-adjoint periodic generator is the rescaled closed operator
in Teschl, *Mathematical Methods in Quantum Mechanics*, GSM 99,
version 12 February 2009, Section 2.2, (2.35)--(2.39), printed
pp.62--63 ([author PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf)).
Only D is periodic. Definition 1.1 and its following bounded-form
criterion in Moller--Westrich, *Regularity of eigenstates in regular
Mourre-theory*, [arXiv:1006.0410v2](https://arxiv.org/html/1006.0410v2),
identify bounded extension of (2) with B in C1(D). We import that
criterion, not the source's higher regularity or positive estimate.

The attempt uses the pre-existing EXPLORE assessment
`drafts/literature/2026-10-30-l522-periodic-commutator-hypothesis-test.md`.
The local application passes the separate conceptual audit below,
under `drafts/literature/2026-10-30-l529-boundary-commutator-audit-coverage.md`.
The original POTENTIALLY_NEW classification meant only that the
assessed search found no matching application; the completed audit
is REPRODUCTION, not a new theorem or an originality assessment.
The functional-calculus tools and elementary compactness argument
are not claimed new. The complete-Weil identification and imported
source proofs retain their prior qualifications.

## Conclusion

There are explicit real unit vectors phi_e,psi_e in Dom(D), for
all sufficiently small epsilon=e>0, and a constant kappa>0 such that

    Q_B(phi_e,psi_e)
       = i kappa/[e log^2(1/e)] + o(1/[e log^2(1/e)]).       (3)

Consequently (2) has no bounded extension on L2(I) pairs and
B is not in C1(D). In particular, along e=exp(-j), for all sufficiently
large integers j the absolute form value is at least
kappa exp(j)/(2j^2), whereas boundedness would require one finite
constant on these unit pairs.

This obstructs this fixed h/D_per regular-Mourre implementation.
It proves no commutator sign for another generator, no H1 statement
about a nullvector, no inequality S<=P-H+K lambda, and no RH result.
The domain calculation does not use positivity of A_I or a spectral
gap and does not infer any endpoint trace from L2 resolvent control.

## Proof

### Explicit periodic and interior packets

Let f be the positive L2-normalized bump proportional to
exp(-1/(1-x^2)) for |x|<1 and zero otherwise. Set
g(v)=sqrt(2)f(2v-5). Thus f,g are real nonnegative smooth bumps,
||f||_2=||g||_2=1, f(0)>0, and supp(g) is contained in [2,3]
with g flat at its endpoints. Define on I, with e<ell/6,

    phi_e(x)=e^(-1/2)[f(x/e)+f((x-ell)/e)],
    psi_e(x)=e^(-1/2)g(x/e),
    alpha_e=e phi_e', beta_e=e psi_e', L=log(1/e).          (4)

These are smooth on the closed interval. At 0 and ell every
derivative of phi_e agrees, since the values from the two sides
are the derivatives of the same f at zero. The other packet is
compactly supported in I. Hence phi_e,psi_e belong to Dom(D),
have norm one, and phi_e(0)=phi_e(ell)=e^(-1/2)f(0).
The norms of alpha_e,beta_e are respectively ||f'||_2,||g'||_2.
All four families are supported in sets shrinking to the endpoints
as e decreases to zero and therefore converge weakly to zero in L2.

Their zero extensions are sums of translates of e^(-1/2)p(x/e),
where p ranges over the fixed profiles

    f 1_(0,infinity), f 1_(-infinity,0),
    f' 1_(0,infinity), f' 1_(-infinity,0), g, g'.           (5)

Each profile has compact support and is smooth on each side of its
finitely many jumps. Integration by parts on those pieces, retaining
the jump terms, and the L1 bound give

    |hat p(eta)|<=C_p min(1,|eta|^(-1)).                    (6)

For each fixed e this implies E p_e belongs to the whole-line
operator domain of G, since Psi hat(E p_e) is square integrable.
In particular its logarithmic form energy is finite. L514's
finite-energy/core-domain identification, obtained there by comparing
with Chen--Weth, *The Dirichlet Problem for the Logarithmic Laplacian*,
[arXiv:1710.03416v6, Theorem 3.1 and (3.2)](https://arxiv.org/html/1710.03416v6),
places its restriction in Q_I. For every v in Q_I the full-line
operator identity gives

    q_I(v,p_e)=<Ev,G E p_e>=<v,R_I G E p_e>.

The form characterization of G_I therefore proves
p_e in Dom(G_I) and G_I p_e=R_I G E p_e. This also proves membership
in Dom(A_I) for all four families. A nonzero periodic endpoint value
does not prohibit this logarithmic operator-domain membership.

### Uniform residuals, including the signed perturbation

For one scaled profile, Plancherel and eta=e xi give

    ||(G-L)e^(-1/2)p(./e)||_2^2
      =(1/(2pi)) integral |(1/2)log(e^2+eta^2)|^2
                                             |hat p(eta)|^2 d eta.
                                                               (7)

For 0<e<=1/2 and eta!=0 the logarithmic factor is bounded in
absolute value by |log|eta||+(1/2)log(2). Equation (6) makes
the resulting bound integrable, both at zero and infinity.
Translations do not alter (7), and the triangle inequality handles
the two separated pieces in phi_e and alpha_e. Since restriction
is a contraction and ||R_I K_mu E||<=||mu||_TV=M, (7) yields

    sup_(0<e<e_0) ||(A_I-L)p_e||_2 <infinity               (8)

for each of the four families in (4). The constants may depend on
the fixed a,A and profiles. No sign of mu is used or changed.

Write X_e=A_I-L. For chi in C_c^infinity(I), self-adjointness gives

    <chi,X_e p_e>=<A_I chi,p_e>-L<chi,p_e> ->0.            (9)

Indeed the second pairing is exactly zero for sufficiently small e,
by the supports; the first tends to zero by weak convergence of
p_e and A_I chi in L2. Density of these chi and (8) imply
X_e p_e converges weakly to zero in L2. This conclusion is about
bounded residuals, not convergence in the operator graph norm.

### Compact resolvent and an exact two-sided expansion

Here is the compactness verification for this realization, to avoid
assuming a periodic or positive model. On a set bounded in the graph
norm of A_I, ||G_I u||_2 is bounded by the bounded perturbation in
(1). Thus q_I(u,u)=<u,G_I u> is uniformly bounded. For R>0,

    (1/(2pi)) integral_(|xi|>R) |hat(Eu)(xi)|^2 dxi
                                      <=q_I(u,u)/Psi(R).   (10)

For fixed R the map from L2(I) to L2([-R,R],d xi/(2pi)) with
kernel exp(-i xi x) is Hilbert--Schmidt, since I and [-R,R]
have finite measure. Inverse Fourier transformation after extension
by zero in frequency preserves compactness. Consequently the
low-frequency projections of this bounded graph set are relatively
compact in L2(R). Equation (10), with Psi(R)->infinity, makes
their tails uniformly small; a finite-net argument proves relative
compactness of the whole zero-extended set. In particular

    R_z=(A_I-z)^(-1) is compact, z=i,-i.                    (11)

The resolvents map the L2 unit ball to a graph-bounded set:
||R_z||<=1 and A_I R_z=I+z R_z. This justifies the last assertion
without a sign or invertibility assumption at zero.

For any p_e,q_e among the four families, the resolvent identity,
applied twice and paired on Dom(A_I), is exactly

    <p_e,R_z q_e>
      =(L-z)^(-1)<p_e,q_e>
       -(L-z)^(-2)<p_e,X_e q_e>
       +(L-z)^(-2)<X_e p_e,R_z X_e q_e>.                  (12)

Only one A_I on each vector is required. For example, start from
R_z q=(L-z)^(-1)q-(L-z)^(-1)R_z X_e q and apply the same
resolvent identity to the first factor of the remaining pairing.
Equivalently use the exact scalar identity on the spectral measure;
the last pairing in (12) is well defined for p,q in Dom(A_I).

By (8)--(11), R_z X_e q_e tends strongly to zero and X_e p_e
stays bounded. The last inner product in (12) is therefore o(1).
Since B=(R_i+R_(-i))/2, averaging (12) proves

    <p_e,B q_e>
       =h(L)<p_e,q_e>+h'(L)<p_e,X_e q_e>+o(L^(-2)),
    h'(L)=(1-L^2)/(1+L^2)^2=-L^(-2)(1+o(1)).             (13)

This is a controlled matrix-element expansion, not an operator-norm
power series or an assumption that the low spectrum is absent.
It uses the full signed resolvents in its remainder. Compactness
is precisely what removes their possible low-spectral contribution
on the weakly vanishing residuals.

### The surviving boundary term

The real operator A_I commutes with conjugation, as does B. For the
real packets, (2) and (4) give

    Q_B(phi_e,psi_e)=-i J_e/e,
    J_e=<phi_e,B beta_e>+<alpha_e,B psi_e>.                 (14)

Inserting (13), the h(L) contribution vanishes because
<phi_e,beta_e>+<alpha_e,psi_e>=e[phi_e psi_e]_0^ell=0.
The scalar -L part of X_e vanishes for the same reason. Thus

    J_e=h'(L) K_e+o(L^(-2)),
    K_e=<phi_e,A_I beta_e>+<alpha_e,A_I psi_e>.             (15)

Since E psi_e is smooth and compactly supported in I, its full-line
image (G-c-K_mu)E psi_e is smooth, including at 0 and ell.
For G this follows from its smooth logarithmic multiplier on the
Schwartz Fourier transform; for K_mu it follows by differentiating
the smooth bounded input against the finite measure. Translation
invariance and zero extension of this interior input give
A_I psi_e'=(A_I psi_e)' on I. Integration by parts on the closed
interval, with the actual endpoint values of this smooth image,
then proves

    K_e=e phi_e(0)[(A_I psi_e)(ell)-(A_I psi_e)(0)].        (16)

No derivative or endpoint trace of B psi_e is taken.

We now evaluate (16), retaining all terms of (1). At x=0 and ell
the input psi_e is zero, so the scalar term contributes zero.
Choose e smaller, if necessary, than log(2)/4 and than
(ell-d_n)/4 for every member of the finite set with w_n>0 and
0<d_n<ell. Then every endpoint sample E psi_e(x-d_n) and
E psi_e(x+d_n), x=0,ell, is zero. If d_n=ell the sample is
the endpoint value psi_e(0)=0; if d_n>ell it is exterior.
Thus all atomic contributions are exactly zero at these two
points, including all equality atoms. The finite-set minimum is
unnecessary if that set is empty. This choice imposes no
nonresonance condition on ell.

The continuous density

    k_mu(t)=rho(|t|)-2cosh(t/2)1_(|t|<=2A)

is bounded: rho(t)=3/4+O(t) at zero and decays at infinity, and
the pole density is bounded on its fixed compact support.
Consequently its endpoint convolutions are O(sqrt(e)), since
||E psi_e||_1=sqrt(e)||g||_1. These are estimates of the full
signed terms, not replacements of the operator by a positive one.

For the G contribution at an endpoint outside the input support,
the jump kernel in (1) gives -integral n(x-y)psi_e(y)dy. Therefore

    (G_I psi_e)(0)=-(1/(2sqrt(e)))
                        integral_2^3 exp(-e v)g(v)/v dv,
    (G_I psi_e)(ell)=O(sqrt(e)).                           (17)

The second bound uses ell-y>=ell/2 for sufficiently small e.
Combining (16)--(17), including the continuous signed contribution,
gives

    K_e=(f(0)/2) integral_2^3 exp(-e v)g(v)/v dv+O(e)
          -> kappa=(f(0)/2) integral_2^3 g(v)/v dv>0.        (18)

Positivity here is only that of the chosen bumps and the principal
jump-kernel contribution: kappa>=f(0)||g||_1/6>0.
Finally (13)--(15) and (18) give (3), with its stated sign for
the convention (2). The unit norms in (4) prove unboundedness.
The imported C1 criterion then gives B not in C1(D).

This proof checks one necessary hypothesis and fails it. It does
not apply the regular-Mourre eigenstate theorem or its separately
assumed local positive estimate. Compactness, the matrix expansion
and the endpoint computation are included to justify this particular
signed killed specialization; no known general C1 theorem is reproved.
The separate audit below verifies this application, without auditing
the imported source proofs or extending the obstruction's scope.

### Separate conceptual application audit, 2026-10-30

The audit passes (3)--(18) with the stated fixed a,A, operator and
generator. The exact source scope was approved before this audit.
L514's bounded-interval density comparison, L515's bounded signed
perturbation, and L522's operator normalization are the local inputs;
L522's assumed nullvector, nonzero trace and nonresonance are not
used. No periodic replacement of G_I or positivity of A_I is needed.
The following checks verify the load-bearing estimates and signs.

**Packets and killed domains.** For e<ell/6 the two pieces of phi_e
are disjoint, and change of variables gives its squared norm as
integral_0^1 f^2+integral_(-1)^0 f^2=1. Likewise ||psi_e||_2=1,
||alpha_e||_2=||f'||_2 and ||beta_e||_2=||g'||_2. The matching jets
at the seam give the stipulated periodic H1 domain. Bounded L2
norms and supports of measure O(e) imply weak convergence to zero
by absolute continuity of the integral of |v|^2 for every v in L2.

Every profile in (5) is L1 and piecewise smooth of bounded variation.
Integrating on each piece gives (6), including the jumps at zero.
The square of log(1+xi^2)/(1+|xi|) is integrable at infinity.
Thus each zero extension is in Dom(G), for each fixed e. L514
(7)--(8) and Chen--Weth's bounded Lipschitz density theorem place
its restriction in Q_I; the whole-line form identity against every
Ev with v in Q_I then represents its G_I image in L2(I). This
establishes the operator domain, rather than only finite energy.
It applies to alpha_e and beta_e as well as to the unit packets.

**Residuals and compactness.** The bound in (7) is valid also at
small frequency. If e^2+eta^2<=1, its absolute logarithmic factor
is at most -log|eta|. If e^2+eta^2>1 and |eta|<1 it is at most
(1/2)log(2); if |eta|>=1 it is at most log|eta|+(1/2)log(2).
Consequently a constant times

    (1+|log|eta||)^2 min(1,|eta|^(-2))

is an integrable bound in (7). Translations only add Fourier phases;
the triangle inequality bounds the two-piece packets. The perturbation
adds at most (|c|+||mu||_TV)||p_e||_2. Compact interior tests belong
to Dom(A_I) by the same whole-line argument. For those tests the
scalar pairing in (9) is eventually exactly zero; density and the
uniform residual bound therefore prove weak convergence of X_e p_e.

For a graph-bounded family, ||G_I u||_2 is bounded and
q_I(u,u)<=||u||_2||G_I u||_2. The frequency restriction in (10)
is a Hilbert--Schmidt map of squared kernel norm ell R/pi. Its
inverse Fourier extension is compact, while the omitted L2 norm
is at most sqrt(q_I(u,u)/Psi(R)), uniformly tending to zero.
Finite nets for the compact low-frequency sets therefore prove
compactness of the graph embedding. Resolvents at both i and -i
map the unit ball to graph-bounded sets, establishing (11) for the
actual signed A_I, even if zero is an eigenvalue.

**Exact remainder and complex signs.** For real scalar t the identity

    1/(t-z)=1/(L-z)-(t-L)/(L-z)^2
                         +(t-L)^2/((L-z)^2(t-z))

gives (12) by the spectral theorem. For p,q in Dom(A_I), the last
term is <X_e p,R_z X_e q>/(L-z)^2; both X_e vectors are in L2,
so no second operator power on either vector is assumed. In
particular the complex coefficient is (L-z)^(-2), not its absolute
square. Compactness sends the weakly vanishing X_e q_e to a strongly
vanishing resolvent image, and the first residual stays bounded.
Averaging z=i,-i gives exactly h(L), h'(L) and the o(L^(-2))
remainder in (13). This does not discard the low spectrum.

Reality and self-adjointness of B give (14) with a minus i: the
second term of Q_B has conjugate scalar +i in its first entry.
The leading scalar pairings cancel by integration by parts. Since
psi_e has compact interior support, E psi_e is smooth and compact;
its Fourier transform is Schwartz, and multiplication by Psi
preserves that class. The finite-measure convolution is smooth by
differentiation of the bounded smooth input. Thus A_I psi_e has
a smooth representative up to both endpoints, and differentiation
commutes with the whole-line operations on this input. Formula (16)
therefore uses classical endpoint values only for this smooth image,
not a trace of B psi_e or of arbitrary L2 resolvent data.

**All signed endpoint contributions.** At x=0, samples at -d_n
are exterior and samples at +d_n exceed 3e once e<log(2)/4.
At x=ell, samples at ell+d_n are exterior. For d_n<ell, those
at ell-d_n exceed 3e under the finite-set condition in the proof;
for d_n=ell the sample is psi_e(0)=0; for d_n>ell it is exterior.
This accounts for both shifts. In particular cutoff equality
d_n=2A is exterior because ell=2a<2A, and a possible d_n=ell
requires no nonresonance assumption. The scalar term vanishes too.

Expansion at zero gives rho(t)=3/4+O(t), and its exponential tail
is integrable. The signed continuous density is therefore bounded
and integrable, and each of its endpoint contributions is O(sqrt(e)).
For the principal jump kernel, the input vanishes in neighborhoods
of both endpoints; its integral representation is absolutely
convergent there. At zero it is the negative expression in (17);
at ell it is O(sqrt(e)), since ell-y>=ell/2. Multiplication by
e phi_e(0)=sqrt(e)f(0) leaves exactly

    K_e=kappa+O(e),
    kappa=(f(0)/2) integral_2^3 g(v)/v dv
          >=f(0)||g||_1/6>0.

Together with h'(L)=-L^(-2)(1+o(1)), this yields
J_e=-kappa L^(-2)+o(L^(-2)), and Q_B=-i J_e/e has precisely
the positive-i leading coefficient in (3). The exact unit-pair
values diverge along e=exp(-j). The imported bounded-form criterion
then excludes C1(D_per). This completes the application audit.

The conclusion is a verified failure of this necessary regularity
hypothesis, not a failure of the desired signed flux inequality or
of RH. Other generators and regularizations require separate tests.
The cited density and C1 theorems are imported with their stated
hypotheses; their general proofs and any complete-Weil identification
were not independently audited here. No quantitative onset, numerical
certificate, family-uniform bound or new source-level advance is claimed.

## Mathlib

Full matching coverage has not been checked. No assertion of absence
is made. The imported commutator criterion, periodic generator and
the qualified domain/signed-operator inputs are cited above. No
formal proof or numerical verification is claimed.
