# L299 — Complete frozen anisotropic Wilson/density bulk cancellation

## Hypotheses

Work on the full lattice Z^4 with Euclidean counting measure and SU(2)
generators t^a=i sigma^a/2, as in L279/L280. Every positively oriented
link is variable. This is a bulk calculation, not a change to the
boundary conditions of the finite relative cube. Let B be the
vertex-to-link incidence (Bu)_mu(n)=u(n)-u(n+mu), let C be the
plaquette incidence, and keep the fixed, unweighted transverse slice
H=ker B*. Use the ambient all-link Wilson jets on this same slice;
do not transport nonlinear jets from a different gauge.

For a constant rho in [1/2,3/2], put w_12=rho and w_mu,nu=1 for
the other five unoriented plaquette types. All translates have the
same weight. The exact phase is

\[
 S_\rho(x)=\sum_p4w_p\left(1-\tfrac12
       \operatorname{Tr}\prod_{j=0}^3
          \exp(\epsilon_{p,j}x_{e_{p,j}}^a t^a)\right).
 \tag{1}
\]

Its degree-two, three and four polynomials have precisely the
normalization S_2=|w^{1/2}Cx|^2/2, S_3=T_rho[x,x,x]/6 and
S_4=U_rho[x,x,x,x]/24. These are local jet definitions; no infinite
sum of the nonlinear phase is required for a constant field.

The covariance G_rho is the inverse of C*wC on H, extended by zero
on gradients, with the color identity. The complete one-color bulk
density is exactly the infinite-lattice version of L282(6):

\[
 D=-\tfrac1{12}I-\tfrac16\operatorname{diag}(\Pi_{ee})
       +\tfrac14(J_{ef}J_{fe})_{ef},\qquad
 \Pi=B\Delta^{-1}B^*,\quad J=M\Delta^{-1}B^*,\quad
 \Delta=B^*B,
 \tag{2}
\]

where (Mv)_mu(n)=v(n)+v(n+mu). The inverse symbols are taken off
q=0; their values at that single point do not affect the kernels.
Both determinant terms in (2) and the Haar term are unchanged by
rho. In operators with colors, D means D tensor I_3.

Use the exact contraction convention of L297(6)--(7):

\[
 W_\rho=D+\tfrac14\mathcal E(T_\rho,T_\rho;G_\rho,G_\rho)
              -\tfrac14\mathcal A(U_\rho;G_\rho).
 \tag{3}
\]

In particular all local vertex slots, both crossing pairings and all
internal colors are retained. No counterterm, added longitudinal
Gaussian, ghost substitution or effective-action identification is
an assumption.

## Conclusion

Every kernel in (3) has absolutely summable rows. Uniformly in the
specified rho interval, their entries obey

\[
 |D_{ef}|+|\mathcal E_{ef}|+|\mathcal A_{ef}|
       \le C(1+|x_e-x_f|)^{-6}.
 \tag{4}
\]

Here the finite local terms are included by increasing C. The
complete one-color direction row-sum tensor exists and is zero:

\[
 \boxed{\displaystyle
 \mathsf W_\rho{}_{\mu\nu}
     :=\sum_{n\in\mathbb Z^4}
           (W_\rho)_{(0,\mu),(n,\nu)}=0
       \quad\text{for every }\rho\in[1/2,3/2].}
 \tag{5}
\]

Absolute convergence makes (5) independent of the exhaustion of the
row sum. The Fourier integral gives the same value. It is also the
limit obtained by either a positive transverse mass regulator or a
smooth infrared cutoff, precisely as specified in section 1 below.
No assertion about arbitrary uncontrolled regulators is intended.

This is an infinite-lattice, constant-weight, zero-external-momentum
identity. It does not prove source localization, estimates of the
remaining L297 residues, finite relative-cube transfer, a bounded
complete heat tail, an uncut coefficient bound, a uniform higher
remainder, an interacting reflection lower bound, continuum field
axioms, or positive mass. It is a local result under the prior
EXPLORE assessment, not a claim of originality beyond the sources
checked. The separate conceptual audit in section 6 accepts (4)--(5)
under these inputs, without auditing their upstream premises afresh.

## Proof

### 1. Exact covariance and convergence of the complete kernels

Use normalized Brillouin measure dq/(2pi)^4. In midpoint coordinates
put

\[
 d_\mu=2\sin(q_\mu/2),\quad c_\mu=\cos(q_\mu/2),\quad
 \lambda=|d|^2,\quad P=I-dd^{\mathsf T}/\lambda,
 \delta=\rho-1,\quad v=d_1e_2-d_2e_1,
 \quad\kappa=\lambda+\delta(d_1^2+d_2^2).
 \tag{6}
\]

The raw-edge symbol is related by the diagonal unitary with entries
exp(iq_mu/2). Thus midpoint formulas retain the original edge phases;
raw symbols, which will be used for kernel estimates, are periodic.
Since v is orthogonal to d, the quadratic symbol and its inverse are

\[
 K_\rho=\lambda P+\delta vv^{\mathsf T},\qquad
 \Gamma_\rho=\frac P\lambda
       -\frac{\delta vv^{\mathsf T}}{\lambda\kappa}.
 \tag{7}
\]

Multiplication on d-perp verifies the inverse directly. The three
positive eigenvalues of K_rho are lambda, lambda, kappa, including
their coincident cases. In particular

\[
 \tfrac12\lambda\le\kappa\le\tfrac32\lambda,
 \qquad 0\le\Gamma_\rho\le2P/\lambda,
 \qquad \operatorname{pdet}K_\rho=\lambda^2\kappa.
 \tag{8}
\]

All bounds below are uniform in rho. In a fixed small neighborhood
of q=0, every derivative of order j of the raw covariance symbol is
bounded by C_j |q|^(-2-j). This follows by differentiating (7), using
lambda,kappa comparable to |q|^2, v=O(|q|), and their smooth
numerators. Away from zero the raw symbols are smooth and periodic.
A curl or an ordinary link difference multiplies a symbol vanishing
to first order at zero. Thus k such differences, for k=0,1,2, have
symbol derivative bounds C_j |q|^(-2+k-j).

Here is the kernel consequence, including the borderline order-zero
symbol. Split a neighborhood of zero into smooth annuli |q| comparable
to r=2^(-j). A symbol of order -beta, with beta=2,1,0, contributes
on each annulus a Fourier coefficient bounded by

\[
 C_M r^{4-\beta}(1+r|n|)^{-M}.
 \tag{9}
\]

Indeed the bound without oscillation uses its volume and supremum;
integration by parts M times in a coordinate with |n_mu|>=|n|/2
gives the other bound. Derivatives of the annular cutoff have exactly
the corresponding powers of r^-1. Sum separately over r<=1/(1+|n|)
and larger r, taking M>4-beta. Both geometric sums are bounded by
C(1+|n|)^(beta-4). The smooth remainder has faster decay. This proves

\[
 |G_\rho(n)|\le C(1+|n|)^{-2},\quad
 |\nabla G_\rho(n)|+|(CG_\rho)(n)|
                  \le C(1+|n|)^{-3},
 \quad
 |\nabla^2G_\rho(n)|+|(CG_\rho C^*)(n)|
                  \le C(1+|n|)^{-4},
 \tag{10}
\]

with the corresponding mixed derivatives and right curls. Fixed
stencil shifts only change C. The same argument gives J(n)=O((1+|n|)^-3),
so (2) has the claimed decay. The quartic contraction has both
external slots in a common plaquette, and its internal covariance
entries are bounded by C integral lambda^-1. It therefore has finite
range and bounded coefficients, just as in L283(8)--(10).

For the complete cubic operator, retain L287's exact split

\[
 D S_3(x)[u]=\mathsf A_\rho(u;x)+\mathsf B_\rho(u;x),
 \quad
 \mathsf A_\rho=\sum_p w_p(Cu)_p\cdot\zeta_p(x),\quad
 \mathsf B_\rho=\sum_p w_p(Cx)_p\cdot D\zeta_p(x)[u].
 \tag{11}
\]

The polynomial zeta is the signed four-slot bracket polynomial of
L287/L289, unchanged by the scalar weight. Its two field colors are
different, so the within-vertex pairing is zero. Each entry of the
crossing contraction is a fixed finite sum of shifted covariance
products with bounded coefficients. Translation invariance and the
constant weights allow external C or C* factors to remain exact
differences of the plaquette anchors.

For the B/B part these products are CGC* times G or CG times GC*;
(10) bounds each by C(1+|n|)^-6. Before the external differences,
the A/B and B/A products have one internal curl and decay of order
(1+|n|)^-5; their remaining external difference raises this to
(1+|n|)^-6. The A/A products start as G times G, of order
(1+|n|)^-4, and have two external differences. The exact finite
difference product rule distributes the two differences among the
two factors, giving again order (1+|n|)^-6 by (10). For example
Delta_j(fg)(n)=(Delta_j f)(n)g(n+e_j)+f(n)Delta_j g(n);
apply it twice for A/A. The external incidence differences act on
fixed orientation components at translated anchors, so this rule
does not subtract different unpaired components. This accounts for
all four parts of (11), not only the internal-curl operator. The
bounded number of slots, orientations and colors proves (4).

There are O((1+r)^3) edges in a unit radial shell in four dimensions,
so (4) is absolutely summable, even with one extra factor 1+r.
It already proves that the ordinary complete row sum exists.

For clarity, a positive transverse mass regulator has midpoint symbol

\[
 \Gamma_{\rho,\epsilon}
   =\frac P{\lambda+\epsilon}
       -\frac{\delta vv^{\mathsf T}}
                    {(\lambda+\epsilon)(\kappa+\epsilon)},
 \qquad\epsilon>0.
 \tag{12}
\]

It is the inverse of K_rho+epsilon on d-perp and zero on d. Its
symbol derivative bounds above are uniform in epsilon, using
kappa+epsilon >= (lambda+epsilon)/2. Alternatively multiply (7)
by a smooth scalar chi_epsilon, zero on |q|<=epsilon and one on
|q|>=2epsilon, with 0<=chi<=1 and derivative bounds
|partial^alpha chi_epsilon|<=C_alpha epsilon^(-|alpha|).
Take this cutoff periodic and equal to one outside the fixed
coordinate neighborhood. It has the same uniform symbol bounds.

Both regulated covariances are positive and have square-integrable
symbols for fixed epsilon. Their kernel coefficients and differentiated
coefficients converge to (10) by dominated Fourier integration.
The complete contracted kernels obey (4) uniformly, so their row
sums converge by dominated summation, for either regulator. D is
unchanged. This establishes the stated regulator independence.

For fixed epsilon, Parseval applies to the crossing covariance
products. The external-curl pieces have zero row sum: the products
before the external differences are summable, by Cauchy--Schwarz
and the square-integrable regulated symbols, and their differences
telescope. Equivalently, a constant external field has Cu=0 in
(11). After this simplification the constant-field cubic vertex is
O(|q|), so its contraction with two unregulated covariances is bounded
by C/lambda. The quartic constant-field contraction is also bounded
by C/lambda. These functions are integrable in dimension four.
Consequently the unregulated Fourier contraction represents exactly
the complete ordinary row sum, not just a formal internal-curl limit.

### 2. Identifying the requested coefficient by finite matrix algebra

Fix a unit color generator t^A and an arbitrary real direction vector
u in R^4. The external field is x_mu(n)=t u_mu t^A. It is transverse
and commuting, and every plaquette is the identity for every t.
We use its local Taylor coefficients only.

At a nonzero q, let Q(q) be an orthonormal inclusion of
ker b(q)*, with raw symbol b_mu(q)=1-exp(iq_mu). It is fixed as t
varies. Denote the compressed Wilson Hessian at this constant field
by H(t,q), including colors. If A=H(0,q), its expansion is

\[
 H(t,q)=A+tT_\rho[u;q]+\tfrac{t^2}{2}U_\rho[u,u;q]+O_q(t^3).
 \tag{13}
\]

The tensors in this equation are compressed in their internal slots;
their extended inverse is exactly G_rho. Expanding Tr log after
conjugation by A^-1/2 gives

\[
 [t^2]\{-\tfrac12\log\det H(t,q)\}
  =\tfrac14\operatorname{tr}(G_\rho T_\rho[u]
                              G_\rho T_\rho[u])
       -\tfrac14\operatorname{tr}(G_\rho U_\rho[u,u]).
 \tag{14}
\]

Adding the quadratic log-density coefficient gives precisely the
quadratic form u^T mathsf W_rho u of (3), after integration.
The tensor contraction equality follows directly from L297(6).
The two crossing Gaussian pairings also give the same normalization
via L287(13). Their standard input is Bauerschmidt--Brydges--Slade,
*Introduction to a Renormalisation Group Method*, LNM 2242 (2019),
[arXiv:1907.05474v2](https://arxiv.org/pdf/1907.05474v2),
Propositions 2.1.6 and 2.1.9 and Corollary 2.1.11, pp. 31--33.
The positive transverse regulators satisfy these finite polynomial
pairing hypotheses; section 1 justifies their limit.

Equation (14) is a finite-symbol log-determinant Taylor identity.
It makes no identification of W with a self-energy or an effective
action and invokes no infinite-dimensional determinant. The full
Fourier trace counts both q and -q; for real fields their two real
modes give exactly this trace convention, with the displayed -1/2.

### 3. Exact flat Wilson Hessian and the unchanged density

On the neutral color the adjoint action of t^A is zero. On the two
complex charged sectors it has eigenvalues i s, s=+1,-1. Put

\[
 p=q+s t u,\qquad
 R_s(t)_{\mu\mu}=\frac{e^{ist u_\mu}-1}{ist u_\mu},
 \qquad
 z_s(t,q)=b(q)^*R_s(t)^{-1}b(p).
 \tag{15}
\]

The ratio defining R has its analytic value one when its argument
is zero. For small t it is invertible. It is the right-trivialized
derivative (delta exp x)exp(-x) of exponential link coordinates.
The exact logarithmic derivative of the gauge action, L280(9), is
R_s^-1 b(p). In particular the gauge determinant on the fixed slice
has charged scalar factor z_s/lambda(q).

To compute the phase Hessian, write z_mu for a right-trivialized
link fluctuation. On a mu,nu plaquette the linearized curvature is

\[
 z_\mu(n)+e^{ist u_\mu}z_\nu(n+\mu)
       -e^{ist u_\nu}z_\mu(n+\nu)-z_\nu(n).
 \tag{16}
\]

Its Fourier symbol is b_nu(p)z_mu-b_mu(p)z_nu. At the flat plaquette
the first derivative of the Wilson function is zero and its Hessian
is the identity curvature quadratic form, with normalization (1).
There is therefore no contribution from a second derivative of the
coordinate map in the phase Hessian. The charged compressed Hessian
is exactly

\[
 H_s(t,q)=Q(q)^*R_s(t)^*K_\rho(p)R_s(t)Q(q).
 \tag{17}
\]

Here K is in raw coordinates; its pseudodeterminant remains (8).
The neutral block is independent of t. This derivation uses the
actual local Wilson plaquette, including its weights, rather than
an assertion of gauge equivalence for the requested covariance slots.

The Haar density on one SU(2) link is det of its exponential
derivative. Accordingly its two charged factors contribute
sum_s log|det R_s| over directions. Together with the gauge
determinant, the relevant real log-density symbol is

\[
 \sum_{s=\pm1}\left\{\log|\det R_s(t)|
                   +\log|z_s(t,q)/\lambda(q)|\right\}.
 \tag{18}
\]

This statement concerns its Taylor coefficients at zero. For each
q!=0 all factors are nonzero for a sufficiently small neighborhood
of t=0, which may depend on q. Complex phases cancel in the real
trace under (q,s) -> (-q,-s); equivalently one takes real parts of
the local logarithms. No uniform finite-t chart near q=0 is assumed.

One can check explicitly that (18) retains both density determinant
jets. Write h=sum_mu u_mu sin q_mu and
a=sum_mu u_mu^2 |b_mu(q)|^2. From L280(10), or directly from (15),

\[
 \frac{z_s(t,q)}{\lambda}
    =1+\frac{s t h}{\lambda}-\frac{t^2a}{12\lambda}+O_q(t^3).
\]

Thus the total coefficient of t^2 in (18) is

\[
 \mathfrak d_u(q)=-\frac{|u|^2}{12}
                     -\frac{a}{6\lambda}-\frac{h^2}{\lambda^2}.
 \tag{19}
\]

The three terms are respectively the Haar term, Tr A_2 and
-Tr(A_1^2)/2. Its integral is the quadratic form of (2), as follows
also by L282(15)'s raw-edge Fourier product. It is integrable since
the only possibly unbounded term is O(|q|^-2).

### 4. The compressed determinant identity and full cancellation

We give the required determinant identity, including its projection
factors. Let K be a positive semidefinite four by four Hermitian
matrix with rank three and null vector b_p, let R be invertible,
and let Q_0 include b_0-perp orthonormally. Then

\[
 \det(Q_0^*R^*KRQ_0)
   =|\det R|^2\operatorname{pdet}K\,
      \frac{|b_0^*R^{-1}b_p|^2}{|b_0|^2|b_p|^2}.
 \tag{20}
\]

For a proof, adj K=(pdet K)b_p b_p*/|b_p|^2. Applying
det(M)M^-1 to R*(K+eta I)R and taking eta to zero gives
adj(R*KR)=|det R|^2 R^-1(adj K)R^-*. In the orthonormal basis
[Q_0,b_0/|b_0|], the last diagonal cofactor of R*KR is the
determinant on the left of (20). Substitution proves the formula.
In our application its overlap is nonzero at t=0, so it is positive
for the required pointwise Taylor expansion. No changing transverse
projection has been suppressed.

Apply (20) with b_0=b(q), b_p=b(p), R=R_s(t) and K=K_rho(p).
Combining (17) with (18), for each charged sector the real expression
whose quadratic coefficient is needed becomes exactly

\[
 \begin{split}
 &\log|\det R_s|+\log|z_s/\lambda(q)|
                         -\tfrac12\log\det H_s(t,q)\\
 &\hspace{12mm}=-\tfrac12\log
          \frac{\operatorname{pdet}K_\rho(p)}{\lambda(p)}
                    -\tfrac12\log\lambda(q).
 \end{split}
 \tag{21}
\]

Both the exponential-coordinate determinant and the fixed-slice
overlap have canceled. The factor lambda(p) is essential: removing
it would give the wrong coefficient. By (8) put

\[
 F_\rho(q)=\log(\lambda(q)\kappa(q)).
 \tag{22}
\]

The neutral sector has no t-dependence. The two charged sectors in
(21) have p=q+tu and p=q-tu. Their combined quadratic coefficient
is consequently -1/2 (u dot partial_q)^2 F_rho(q). Equations
(14),(18)--(21) prove the complete identity

\[
 u^{\mathsf T}\mathsf W_\rho u
   =-\tfrac12\int (u\cdot\partial_q)^2
                         F_\rho(q)\,\frac{dq}{(2\pi)^4}.
 \tag{23}
\]

All individual coefficients used in this identity are integrable:
(19) treats the density; (16)--(17) give T[u]=O(|q|) and
U[u,u]=O(1), while G=O(|q|^-2), so the two terms of (14) are
O(|q|^-2). Section 1 identified their integrals with the complete
ordinary row sums. Thus (23) does not interchange a nonuniform
finite-t logarithm with integration. It integrates the already
computed, integrable Taylor coefficients at t=0.

The periodic function F is smooth away from zero. Uniformly in rho,
|partial F|<=C/|q| and |partial^2 F|<=C/|q|^2 near zero, by (8).
Integrate partial_mu partial_nu F on the Fourier torus with a ball
of radius r about zero removed. Opposite torus faces cancel by
periodicity. The remaining sphere flux has absolute value at most
C r^3/r=C r^2, which tends to zero. The second derivative is
integrable, so this proves

\[
 \int\partial_\mu\partial_\nu F_\rho(q)\,dq=0
                    \quad\text{for every }\mu,\nu.
 \tag{24}
\]

There is no surviving point mass at zero in four dimensions.
Equation (23) is zero for every real u. The row-sum matrix is real
symmetric because (3) is a translation-invariant real symmetric
kernel with absolutely summable rows. Polarization therefore makes
the one-color direction tensor zero. Global adjoint SU(2) rotations
force the operator to be scalar in external color: rotations by pi
kill mixed color entries and rotations interchanging color axes
make the diagonal color blocks equal. This proves (5) for the full
color tensor as well.

### 5. Independent normalization diagnostic and scope of the result

The following explicit diagonal formulas connect the determinant
argument back to the original contraction formulas. For u=e_mu put

\[
 H_\mu=c_\mu\sum_{\nu\ne\mu}w_{\mu\nu}
   \left[d_\mu e_\nu e_\nu^{\mathsf T}
      -\tfrac{d_\nu}{2}
        (e_\mu e_\nu^{\mathsf T}+e_\nu e_\mu^{\mathsf T})\right].
 \tag{25}
\]

The weighted version of L289(5)--(8) gives the cubic contribution
2 tr(H_mu Gamma H_mu Gamma). Its factor is the two crossing
pairings together with Tr J_A^2=-2 and the factor 1/4 in (3).
The complete L283(13) plaquette contraction gives the quartic
contribution before its minus sign as

\[
 \mathfrak a_\mu(q)=\sum_{\nu\ne\mu}w_{\mu\nu}
 \left[-\frac{d_\nu^2}{12}\Gamma_{\mu\mu}
       +(1-\tfrac12d_\mu^2)\Gamma_{\nu\nu}
       +\frac{d_\mu d_\nu}{3}\Gamma_{\mu\nu}\right].
 \tag{26}
\]

For example the raw-edge combination
-g_01+g_03+g_12-g_23 contributes
4 sin(q_mu/2)sin(q_nu/2) Gamma_mu,nu, while g_02 and g_13
retain their cos q_nu and cos q_mu offsets. Thus the phases in
(26) have not been dropped. Formula (19) supplies its density partner.
The pointwise identity proved by (20)--(23) is

\[
 -\tfrac1{12}-\frac{d_\mu^2}{6\lambda}
       -\frac{d_\mu^2c_\mu^2}{\lambda^2}
       +2\operatorname{tr}(H_\mu\Gamma H_\mu\Gamma)
       -\mathfrak a_\mu
          =-\tfrac12\partial_\mu^2\log(\lambda\kappa).
 \tag{27}
\]

The exact-rational diagnostic is reproduced by

```bash
python3 scripts/anisotropic-bulk/check-symbol.py
```

It checks (27) at 80 selected rational half-angle parameter points,
including all four directions, both endpoint weights, rho=1 and
two interior weights. All actual-minus-required differences were
exactly zero. The full cases and failures are saved in
`scripts/anisotropic-bulk/symbol-certificate.json`. The program is
a normalization diagnostic, not a proof of a continuum of identities
or of the convergence estimates. Those are proved above.

This mechanism specifically uses the local weighted Wilson Hessian
at a flat commuting field and the explicit fixed-slice density.
It does not reopen ATTEMPTS/049's failed inference from generic
orbit identities to a logarithmic finite-box bound. In particular
(5) supplies only the frozen constant-field cancellation that a
future, separately assessed localization estimate might use.

### 6. Separate conceptual audit (2026-10-28)

**Scope and decision.** This audit accepts (4)--(5), including the
ordinary absolutely convergent row sum and the two specified regulator
limits, uniformly for constant rho in [1/2,3/2]. It checks the local
proof against L279's Wilson normalization, L280's own-slice density,
L282's raw-edge density product, L283's local quartic contraction,
L287's full cubic split and pairing convention, L289's real/color
normalization, and L297(6)--(7)'s exact tensor definition. Those inputs
retain their upstream premises. No finite relative-cube or variable-source
estimate is accepted by this audit. The prior EXPLORE assessment covers
this audit; its inspected Gaussian propositions are reused, not reproved.

**All cubic placements and ordinary convergence.** In raw coordinates
the only singular point of (7) is zero. Its rational-symbol derivatives
of order j obey the order -2-j bound; either a left or right curl, or a
translation difference, raises the symbol order by one. The annular estimate (9) works
also at order zero: its small-annulus sum is a geometric sum of r^4,
not a logarithmic divergence. This verifies all mixed versions of (10).
The constants are uniform since kappa/lambda lies in [1/2,3/2].

For detail about the external differences, index a plaquette by its
anchor and orientation alpha. Set
Z_alpha(n)=w_alpha zeta_alpha(x;n), and collect the coefficients of the
external edge field in B as Y_mu(n). Translation invariance makes
their crossing covariances fixed finite sums of shifted products.
Before the common factor two converting these covariances to E,
the A/A block is C* Cov(Z,Z) C; each of its scalar orientation
components has two anchor differences on a product G G. The A/B
and B/A blocks are C* Cov(Z,Y) and Cov(Y,Z) C; each has one
anchor difference on products G(CG) or their right-curl versions.
The B/B block consists of (CGC*)G and (CG)(GC*) products.
Weights are constant bounded coefficients in these formulas.

In particular C* takes the difference of two translates of the SAME
plaquette-orientation component. In Y, external slots may shift its
anchor by a fixed stencil displacement, which does not change this
fact. No subtraction of unrelated orientation components is used as
a derivative estimate. Applying the discrete product rule distributes
the two A/A differences with derivative orders (2,0), (1,1), or
(0,2), and the single mixed-block difference with orders (1,0) or
(0,1). Every resulting product has decay (1+|n|)^-6. Within-vertex
pairings vanish because the two internal colors differ, with a
color-diagonal covariance. This accounts for every cubic placement.
The quartic external slots share one plaquette, so that kernel is
finite range; J has order -1 and decay (1+|n|)^-3, giving the same
bound for the nonlocal density product. The radial sums for (4)
and for its first absolute moment are bounded respectively by
constant multiples of sum_{r>=1} r^-3 and sum_{r>=1} r^-2.

For (12), the inequalities lambda+epsilon>=lambda and
kappa+epsilon>=(lambda+epsilon)/2 preserve these symbol bounds
with constants independent of epsilon. Derivatives of P remain
controlled by the same order -2 bound, even though P has no limit
at zero. The stated cutoff has the same bounds on its transition
annulus. For each fixed positive regulator both symbols are in L2;
their kernels and curl/difference kernels converge coefficientwise
by an integrable C/lambda majorant. Dominated summation using (4)
then identifies their limiting complete row sums with the ordinary
unregulated ones. Before taking the limit, products preceding an
external difference are in l1 by Cauchy--Schwarz, so that difference
has exactly zero row sum. This establishes the use of Cu=0 on a
constant field without treating that field as an l2 vector or assuming
absolute convergence of the unregulated undifferentiated A/A product.

**Contraction and real trace factors.** In finite real coordinates,
D S_3(x)[u]=T[u,x,x]/2. The finite Gaussian identity gives
E[D S_3(x)[u]^2]=tr(T[u]G T[u]G)/2: the factors 1/2 from the
two derivatives and the two crossing pairings are all included.
Thus u*E u=tr(T[u]G T[u]G), precisely L297(6), with no additional
factor two in (14). Also u*A u=tr(U[u,u]G). Expanding
H=A+tT[u]+t^2 U[u,u]/2 gives exactly +1/4 and -1/4 in (14).
The Wilson normalization 4(1-Tr/2) gives curvature Hessian one,
as follows from L279(10); the weighted Hessian is consequently K_rho,
not a scalar multiple of it.

These traces can be checked on a finite periodic real Fourier space
with zero mode removed, solely to fix normalization. For a constant
external field, normalize these traces by the lattice volume. A q,-q pair of
real modes becomes the direct sum of their complex Fourier blocks
on complexification; its real trace equals the sum of those two
complex traces. Diagonalizing the real color generator likewise
retains both charged eigenvalues +i and -i, plus the neutral color.
Therefore the full Brillouin trace has the Gaussian prefactor -1/2
and includes both charged sectors. No half-zone or extra color
factor is allowed. No finite-volume convergence theorem is imported
by this normalization check; the kernel argument above supplies the
infinite-volume identification.

**Own-slice Hessian and both density jets.** The derivative of the
actual exponential link coordinate is R_s. At a commuting constant
field the linearized plaquette is exactly (16), and its background
plaquette is identity. The Wilson first derivative there is zero,
so the second derivative of the coordinate map contributes nothing
to the phase Hessian. Compressing the resulting quadratic form with
the unchanged Q(q) proves (17); a moving transverse space has not
been substituted.

Independently expand (15), with m_mu(q)=1+exp(iq_mu):

\[
 (R_s^{-1}b(q+stu))_\mu
 =b_\mu(q)-\frac{ist u_\mu}{2}m_\mu(q)
           -\frac{t^2u_\mu^2}{12}b_\mu(q)+O_q(t^3).
 \tag{28}
\]

Since conjugate(b_mu)m_mu=2i sin q_mu, multiplication by b(q)*
gives z_s=lambda+s t h-t^2 a/12+O_q(t^3), with exactly the a,h
of (19). The two log z_s coefficients sum to
-a/(6 lambda)-h^2/lambda^2. Each charged Haar logarithm has quadratic
term -t^2|u|^2/24, so their sum supplies -|u|^2/12. These are respectively
Tr A_2, -Tr(A_1^2)/2 and Haar in L280(4), not two independent
copies of a ghost correction. For the product term in D, the
reversed-displacement Fourier contraction is
m_mu conjugate(b_nu)m_nu conjugate(b_mu)/lambda^2
=-4 sin q_mu sin q_nu/lambda^2. Multiplication by 1/4 and
contraction with u_mu u_nu gives -h^2/lambda^2, including every
off-diagonal entry. The diagonal projection and Haar terms give
the other two terms of (19). This verifies that (18) computes the
specified unchanged D, with the raw-edge phases retained.

**Projected determinant and infrared passage.** For q!=0 and t near
zero (with its neighborhood allowed to depend on q), K_rho(p) has
rank three. Conjugating the adjugate as in (20) and taking its
b(q)/|b(q)| cofactor gives

\[
 \det H_s(t,q)=|\det R_s|^2
       \lambda(p)\kappa(p)\frac{|z_s(t,q)|^2}{\lambda(q)}.
 \tag{29}
\]

The overlap at t=0 is lambda(q)>0. Hence the logarithms and their
pointwise Taylor coefficients exist. In (29) the denominator
lambda(p) in the cofactor formula has removed one of the two
lambda(p) factors of pdet K; omitting it would replace
log(lambda kappa) by log(lambda^2 kappa). Subtracting half the
logarithm of (29) from (18) gives (21), including the remaining
-log(lambda(q))/2, which is independent of t. This verifies the
fixed-slice determinant rather than invoking gauge invariance as
a substitute for matching the coefficient.

For arbitrary real u the two charged shifts give the coefficient
-(u dot partial)^2 F_rho/2. Individually T[u]=O(|q|) and
U[u,u]=O(1), from differentiation of (17); the two action traces
in (14) are therefore O(|q|^-2). The density has this same integrable
majorant. Thus the previously identified row sums are the integrals
of these Taylor coefficients. No integral of a finite-background
logarithm is differentiated through a shrinking chart.
On the punctured torus the inner boundary flux of each
partial_mu partial_nu F has absolute value <=C r^2, uniformly in
rho. Since the second derivatives are locally integrable and
opposite outer faces cancel, their integrals vanish. This verifies
off-diagonal as well as diagonal entries and excludes a residual
point mass. The absolutely summable real symmetric kernel gives a
real symmetric row-sum tensor; polarization and global color
rotations then establish the full zero tensor in (5).

**Evidence and limitations.** The saved exact-rational diagnostic was
replayed: 80/80 selected diagonal cases passed, maximum absolute
difference 0 against required 0, and no failures. Its complete
certificate remains `scripts/anisotropic-bulk/symbol-certificate.json`.
This is only an ancillary consistency check; the audit's conclusion
rests on the full kernel, determinant and flux arguments above,
including arbitrary u. It supplies an accepted local input, not
progress beyond the literature established by a novelty review.
Constant rho and translation invariance are essential to this proof.
Source localization, finite-box pins/end links, other L297 residues,
a bounded complete tail, the uncut coefficient and higher remainder,
the interacting continuum theory and positive mass remain open.

## Mathlib

Full matching coverage for this weighted Wilson tensor, fixed-slice
determinant cancellation and lattice kernel estimates is **not checked**.
No matching Mathlib theorem or formal verification is asserted.
The finite covariance-addition/Wick input is cited above; the exact
weighted specialization, projection factors, kernel convergence and
singular-momentum flux are justified here rather than imported from
the different background-gauge results in the literature assessment.
