# C212b — The complete cubic endpoint response is cubic-bounded

## Hypotheses

Use exactly L212's SU(2) hypotheses: the relative box (-4,4)^4,
admitted even meshes a=8/N, the straight lower-rooted direction-1
forest, L008's complete displacement, both actual L010 probes
at tau=1/16, and the bare expansion at fixed mesh before refinement.
Use ordinary full variable-link coordinates, including every normal
end edge. All vertex potentials are zero on physical boundary vertices.
Constants may depend on the fixed probe and data, but not on N.

Keep L212's S=P Sigma P, Sigma=(L+DD^T)^(-1), A=PAP=A^T,
B=B_i=PBP, r=sum_c (z^c)^T A z^c and M=2SAS. The three colors
of z are independent with covariance S. A retains both insertion
subtractions. Phi is the actual pinned lower prefix, R=I-D Phi,
and c(z) is the entire cubic endpoint field L212(3).

For each positive variable edge e:v->w define scalar link-row maps

    (X_p z)_e=-(Phi z)_v,
    (X_u z)_e=(Rz)_e,
    (X_q z)_e=(Phi z)_w, X_j=X_p+X_u.                 (1)

They act identically on colors. The symbol X_q here is the head
endpoint map, not L212's endpoint-sum map q. Use the five ordered
triples and weights

    (X_p,X_p,X_u; 1/12), (X_u,X_u,X_p; 1/12),
    (X_q,X_p,X_u; -1/4), (X_j,X_j,X_q; 1/12),
    (X_q,X_q,X_j; 1/12).                             (2)

For a triple (X,Y,Z;omega), all maps are evaluated at the same output
edge. For any maps from (1) put

    C_XY(e)=(X S Y^T)_(ee), K_XY(e)=(X M Y^T)_(ee),
    E_X(e)=(X S B)_(ee), T_X(e)=(X M B)_(ee).         (3)

## Conclusion

The entire endpoint response has the exact signed contraction

    K^(c)_(i,N):=Cov_S(2<Bz,c(z)>,r)
      =12 sum_(X,Y,Z;omega in (2)) omega sum_e {
          T_Y(e) C_XZ(e)+E_Y(e) K_XZ(e)
         -T_Z(e) C_XY(e)-E_Z(e) K_XY(e)}.             (4)

Every sum includes all variable edges. For both actual probes,

    |K^(c)_(i,N)|<=C_i N^3.                          (5)

More precisely, the terms in (4) with T are O(1); the terms with
K have the stated O(N^3) bound. Neither estimate gives a limit
or a sign for their sum. In particular the complete quartic target
can be written, using C212a, as

    K_(i,a)=Cov_S(F_(i,4)(z)+dF_(i,3)(z)[b(z)],r)
                         +K^(c)_(i,N)+O(N^(5/2)).    (6)

Only the endpoint part in (6) is cubic-bounded here. The two remaining
complete flow polynomials retain their nested integrals down to zero;
no bound, separate convergence or cancellation for them is claimed.
The endpoint limit, full quartic limit and compensation, finer powers
and logarithms, finite matching, reflected error <=c_box/2, continuum
axioms and infrared finite positive mass remain unresolved. This is a
local specialization of existing estimates and standard Gaussian
contraction, not a claim of progress beyond the sources checked.

## Proof

### 1. Contract all colors before estimating the endpoint

Antisymmetry gives [[p,u],q]=-[q,[p,u]]. Thus L212(3) is exactly

    c(z)=sum_(X,Y,Z;omega in (2))
                         omega [Xz,[Yz,Zz]].        (7)

No endpoint term is omitted. In particular X_j is the actual sum
p+u, not an independent random field.

Here is the required four-Gaussian color contraction. Let w,a,b,d
be three-component centered jointly Gaussian vectors, whose scalar
component covariances are color diagonal and identical in each color.
Write rho_b=Cov(w^1,b^1), C_ad=Cov(a^1,d^1), and analogously for
other pairs. The SU(2) convention is [a,b]=-a cross b, so

    w dot [a,[b,d]]=(w dot b)(a dot d)-(w dot d)(a dot b).

Isserlis' fourth-moment theorem gives

    E[(w dot b)(a dot d)]
        =9 rho_b C_ad+3 rho_a C_bd+3 rho_d C_ab.

Indeed pairing the two factors in each dot product separately leaves
two free color sums and contributes 9; either crossing sets the two
colors equal and contributes 3. Exchanging b,d and subtracting
cancels the rho_a term and yields the exact formula

    E[w dot [a,[b,d]]]=6(rho_b C_ad-rho_d C_ab).       (8)

This includes every pairing, including internal contractions of the
three endpoint slots. Unlike an alternating cubic scalar, this
quartic does not have vanishing internal pairs by assumption.

At fixed mesh tilt the normalized Gaussian by exp(lambda r). On the
support of S it is integrable for sufficiently small real lambda:
|2lambda| ||S^(1/2)AS^(1/2)||<1 suffices. Its colors remain independent
with identical covariance S_lambda and S'_0=2SAS=M. This construction
also covers singular ambient S by writing z=S^(1/2)xi on its support.
Polynomial Gaussian domination on a smaller lambda interval justifies
differentiation. The interval may depend on the mesh; no uniform
exponential integrability is asserted.

Apply (8) with w=(Bz)_e, a=(Xz)_e, b=(Yz)_e, d=(Zz)_e under this
tilt, holding B,X,Y,Z fixed. The derivative of the normalized left
side is its covariance with r. On the right it differentiates both
covariance factors. At zero, rho_Y=(Y S B)_(ee) and rho'_Y=(Y M B)_(ee),
using symmetry of B,S,M. Multiply by the endpoint polynomial's factor
2 and sum (7). This proves (4), with coefficient 12, all four signed
products, and the original connected subtraction. Differentiating
the covariance of the fixed endpoint polynomial accounts for every
moving prefix in its directional derivative; no random prefix is
held fixed in that derivative.

### 2. Local prefix variances and the signed rough tilt

The positive comparisons in L182(10) and L186(4) give

    0<=S<=Sigma, 0<=Phi S Phi^T<=U tensor G,
    U_st=min(s,t), G=Delta_T^(-1).                    (9)

Here Delta_T is the full unscaled three-dimensional transverse
Dirichlet Laplacian on interior vertices. The same sine spectrum
used in L186(9) gives a uniform diagonal bound for G. Each normalized
three-dimensional product wave has square at most 8/N^3, while its
eigenvalue is at least 4|k|^2/N^2, with 1<=k_j<=N-1. A shell
max k_j=m has at most 3m^2 indices. Therefore, at every transverse
interior vertex,

    G_(vv)<= (2/N) sum_k |k|^(-2)
             <=(6/N) sum_(m=1)^(N-1) 1<=6.           (10)

Boundary potential values are zero. Equations (9)--(10) imply
Var((Phi z^c)_v)<=6N at every vertex. L026(11) and S<=Sigma also give
Var(z_e^c)<=8 at every variable link, including normal end links.
Each map in (1) is a sum of at most three of these scalar variables
with coefficients +/-1. The inequality E|sum_(j=1)^m v_j|^2
<=m sum_j E|v_j|^2 requires no independence and proves

    C_XX(e)<=C N, |C_XY(e)|<=C N.                    (11)

The second inequality is scalar covariance Cauchy--Schwarz. Both
pinned endpoints, including the upper prefix jump, are included.

L186(12)'s signed residual form bound is

    ||E||_op<=C N, E=S^(1/2)AS^(1/2).                (12)

For any rows x,y, the exact factorization M=2S^(1/2)E S^(1/2) gives

    |x M y^T|<=2||E||_op sqrt(x S x^T) sqrt(y S y^T).

Applying this with the rows of X,Y and (11) yields

    |K_XY(e)|<=C N^2.                               (13)

This is a bound on a signed contraction. It neither assigns positive
covariance to M nor smoothness to any rough tilted slot. All modes
and both insertion subtractions remain in (12).

### 3. Contract the smooth external leg in its original position

Use exactly L185(3)--(6)'s full relative heat expansion and smooth
column estimate:

    B=a^2 sum_(k,l) d_(i;kl) e_k e_l^T,
    e_k=a^2 f_k, ||e_k||_infinity<=C a^2,
    sum_(k,l)|d_(i;kl)|p(k)p(l)<=C_(i,p),
    ||m_k||_infinity<=C a^2 p(k), m_k=M e_k.         (14)

The weighted summability holds for each fixed polynomial p. All
component product modes, including the constant own-direction
cosine modes, occur. The physical one-form eigenvalues lambda_k
have a positive mesh-uniform lower bound, and f_k has uniformly
bounded amplitude. Consequently

    h_k=Sigma e_k=lambda_k^(-1) f_k,
    ||h_k||_infinity<=C.                             (15)

There is no assertion that S e_k is a product mode. Instead B=PBP
and commutation of P with Sigma give the exact identities

    S B=Sigma B,
    S B=a^2 sum_(k,l)d_(i;kl) h_k e_l^T,
    M B=a^2 sum_(k,l)d_(i;kl) m_k e_l^T.             (16)

This replacement is made only on the already contracted external B
leg. It is not a transfer of the endpoint polynomial or a replacement
of S in its internal covariance.

On any deterministic full-link field h, Phi sums at most N entries
with coefficient one and is then pinned to zero on the boundary.
All maps in (1) therefore satisfy

    ||Xh||_infinity<=C N ||h||_infinity.              (17)

The estimate deliberately retains the full possible upper jump.
Applying (17) to (15) and (14), and then using (16), yields at every
variable output edge

    |E_X(e)|<=C_i a^4 N<=C_i' N^(-3),
    |T_X(e)|<=C_i a^6 N<=C_i' N^(-5).               (18)

For the first bound, the factors are a^2 from the spectral expansion,
a^2 from e_l, and N from Xh_k. For the second there is the additional
a^2 from m_k. Weighted summability in (14) absorbs its polynomial
p(k). This uses smooth consistency only on the external M e_k column,
where L185 proves it. No prefix commutes through P, M, or a heat
operator. Every heat mode remains in the summation.

### 4. Count the full output set and return to the original response

There are at most C N^4 variable edges. For each ordered triple in
(2), equations (11), (13) and (18) give

    sum_e |T_Y(e) C_XZ(e)|<=C_i N^4 N^(-5) N=O(1),
    sum_e |E_Y(e) K_XZ(e)|<=C_i N^4 N^(-3) N^2=O(N^3).

The other two products obey the identical estimates. The five
coefficients in (2) have total absolute value 7/12. Formula (4)
therefore proves (5), without requiring cancellation of any of its
signed products or discarding any face or corner row. The achieved
bound gives bounded a^3 K^(c) only. The potentially cubic products
E K have not been evaluated and are not o(N^3) by this argument.

L212(4),(9) and C212a(4) now give (6) by covariance linearity.
No flow polynomial was estimated, and no zero-time limit was taken.
In particular the bound cannot be applied to either remaining flow
term by replacing its internal heat time with tau. No numerical
experiment or synthetic fixture is used to infer this all-mesh bound.

## Mathlib

Full matching result: **not checked**. Supporting coverage of
Isserlis' theorem, normalized quadratic Gaussian tilts and finite
cochain covariance bounds: **not checked**; unknown availability is
not absence. The named standard input is Isserlis' fourth-moment
theorem, specialized with its complete color factors in (8). The
prefix comparison, heat expansion, smooth external M-column estimate
and signed form bound are imported from the cited local results,
with their unchanged hypotheses. The reused
[coverage assessment](../drafts/literature/2026-10-16-complete-quartic-probe-jet-scale.md)
approves the complete response target but imports no theorem for a
limit of this selected bare cumulant. No general flow theorem is
reproved here.
