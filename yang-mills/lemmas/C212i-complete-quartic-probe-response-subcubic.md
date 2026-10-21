# C212i — The complete quartic probe response has zero cubic limit

## Hypotheses

Use exactly L212 and C212b's SU(2) hypotheses: the relative box
(-4,4)^4, admitted even meshes a=8/N, straight lower-rooted direction-1
forest, complete L008 displacement, both actual L010 probes i=3,6
at tau=1/16, and the bare expansion before mesh refinement. All
coordinates are ordinary dimensionless full variable-link coordinates.
Keep every normal end edge; potentials are zero at all boundary vertices.

Use S=P Sigma P, A=PAP=A^T with both insertion subtractions,
B=B_i=PBP, M=2SAS and r=sum_c (z^c)^T A z^c. The three colors of
z have independent identical covariance S. Set phi=Phi z with the
actual pinned lower prefix. The cubic field c is the complete L212(3),
equivalently all five triples of C212b(2). No prefix is independent
of z. Constants may depend on the fixed data, but not N.

## Conclusion

For both actual probes the entire cubic endpoint satisfies

    |Cov_S(2<Bz,c(z)>,r)| <= C_i N^(5/2).             (1)

Consequently C212h(6) gives for the complete original forest response

    |kappa_0(f_(i,2),r_0)| <= C_i N^(5/2) log(eN),
    a^3 kappa_0(f_(i,2),r_0) -> 0,  i=3,6.          (2)

The achieved bound is subcubic; the scaled error is
O(N^(-1/2)log(eN)). This does not give an O(N^2) bound, finer powers
or logarithms, compensation of other response groups, finite matching,
the interacting reflected error <=c_box/2, continuum axioms or infrared
finite mass. This is a local specialization of the previously assessed
Gaussian contraction and finite summation methods, not a claim of
progress beyond the sources checked. Its endpoint argument is new to
this notebook. The separate critical audit in section 6 validates this
endpoint argument with the cited upstream results retained as inputs.

## Proof

### 1. Separate the pure-prefix polynomial only after restoring all triples

At an edge e:v->w write vphi=phi_v, wphi=phi_w and

    h=(vphi+wphi)/2, d=wphi-vphi,
    p=-vphi, q=wphi, u=z_e-p-q, j=z_e-q.

These are identities on full fields, including normal end rows. Let
u_0=-p-q and j_0=-q. In the five-bracket expression C212b(7), set
the explicit z_e to zero while keeping the two potential arguments.
Its resulting polynomial is

    c_0= -[p,[p,q]]/6 + [q,[p,q]]/6
       = -[vphi+wphi,[vphi,wphi]]/6
       = -[h,[h,d]]/3.                              (3)

For the first equality the first two triples contribute
-[p,[p,q]]/12-[p+q,[p,q]]/12, the third contributes
+[q,[p,q]]/4, and the last two vanish since j_0=-q.
Thus no triple has been omitted. The remainder c_+=c-c_0 is exactly

    [p,[p,z_e]]/12
    +([z_e,[u_0,p]]+[u_0,[z_e,p]]+[z_e,[z_e,p]])/12
    -[q,[p,z_e]]/4
    +([z_e,[j_0,q]]+[j_0,[z_e,q]]+[z_e,[z_e,q]])/12
    +[q,[q,z_e]]/12.                                (4)

Every displayed bracket has a direct z_e slot; one identically zero
bracket has deliberately been left in the expansion. Equations (3)
and (4) are polynomial identities. They do not change the Gaussian
law or treat phi as independent when differentiating that law.

For row maps X,Y define E_X=(XSB)_(ee) and K_XY=(XMY^T)_(ee),
as in C212b(3). Its full color and normalized-tilt contraction gives
12 omega(E_Y K_XZ-E_Z K_XY) for the internal-tilt part of a bracket
omega[Xz,[Yz,Zz]]. The sum of all external-tilt terms of c remains
O(1) by C212b, proof sections 3--4; no new estimate on them is needed.

### 2. All terms with a direct link slot are subcubic

C212b(9)--(13) give, uniformly on all variable edges and vertices,

    Var(z_e^1)<=C, Var(phi_v^1)<=C N,
    ||S^(1/2) A S^(1/2)||<=C N.

They include the upper pinned layer and all covariance source modes.
The same variance bound O(N) holds for any of p,q,u_0,j_0,h,d.
For the direct link row I_e and any two such prefix rows X,Y,
the signed whitened-tilt inequality therefore gives

    |K_II|<=C N, |K_IX|<=C N^(3/2), |K_XY|<=C N^2. (5)

C212b(14)--(17), without applying a prefix when X=I, give

    |E_I|<=C_i a^4=O(N^-4),
    |E_X|<=C_i a^4 N=O(N^-3).                       (6)

In each internal-tilt product for (4), either the external E slot
is direct, so (5)--(6) give O(N^-2) per edge, or a direct slot
remains in K, giving at worst O(N^(-3/2)) per edge. There are
O(N^4) edges and finitely many brackets. Thus the complete
internal-tilt contribution of c_+ is O(N^(5/2)). Multiple direct
slots only improve this count. No smoothness of M is used.

### 3. The pure-prefix contraction is an exact diagonal difference

Let V=Phi M Phi^T, a signed symmetric matrix on interior vertices,
extended by zero to boundary vertices. Write k_v=V_vv. From (5),

    |V_vw|<=C N^2, |k_v|<=C N^2.                   (7)

Symmetry, not positivity or translation invariance, gives exactly

    K_hd=(k_w-k_v)/2,
    K_hh=(k_v+2V_vw+k_w)/4.                         (8)

The internal-tilt part of (3) is therefore

    -4 sum_e (E_h(e) K_hd(e)-E_d(e) K_hh(e)).        (9)

The coefficient is 12 times -1/3, using the same factor 2 in
2<Bz,c> as C212b. Internal pairs are retained. It remains to estimate
the two sums in (9); no limit of V or its diagonal will be assumed.

### 4. Only the contracted external coefficients need smoothness

Use L185(3)--(4)'s complete heat expansion and C212b(15)--(16):

    SB=Sigma B=a^2 sum_(k,l) d_(i;kl) h_k e_l^T,
    h_k=lambda_k^-1 f_k, e_l=a^2 f_l,
    sum_(k,l)|d_(i;kl)|p(k)p(l)<=C_(i,p)             (10)

for every fixed polynomial p. L028, proof sections 1--2, specify the
relative product modes as samples of smooth sine/cosine products,
with C^1 norm bounded by a polynomial in the mode label and a
uniform positive physical eigenvalue gap. Consequently h_k has a
polynomially bounded C^1 extension, e_l has amplitude O(a^2), and
same-component neighboring entries of e_l differ by O(a^3 p(l)).
All allowed constant own-direction modes are included.

Put t_k(v)=(Phi h_k)_v. It is the actual unscaled sum of at most N
component-1 entries, pinned to zero on the physical boundary. Hence
|t_k(v)|<=C N p(k) everywhere. If neighboring vertices are both
interior, then

    |t_k(w)-t_k(v)|<=C p(k).                        (11)

For an axial edge the difference is one entry of h_k. For a
transverse edge the two sums have the same length, and each of at
most N summands differs by at most C a p(k); Na=8. These two
arguments establish (11) directly without extending the prefix
through its upper pin. For a boundary edge use only the global
bound C N p(k).

Formula (10) now gives the exact coefficients

    E_h(e)=a^2 sum_(k,l)d_(i;kl)
                     (t_k(v)+t_k(w)) e_l(e)/2,
    E_d(e)=a^2 sum_(k,l)d_(i;kl)
                     (t_k(w)-t_k(v)) e_l(e).        (12)

Call an edge a boundary edge if at least one endpoint lies on the
physical boundary. There are O(N^3) such variable edges, including
every normal end row. Equations (10)--(12) give

    |E_d(e)|<=C_i a^4        off the boundary edges,
    |E_d(e)|<=C_i a^4 N      on the boundary edges.  (13)

For the divergence D^T E_h, call an interior vertex a collar vertex
if any incident edge has a boundary endpoint. There are O(N^3)
collar vertices. At any other vertex, consider its incoming and
outgoing edges in one direction mu. In a single (k,l) summand of
(12), their difference is bounded by

    C (N p(k) a^3 p(l) + p(k) a^2).

Indeed subtract the two edge values by first subtracting their
e_l factors, and then subtracting their endpoint averages of t_k.
The latter averages differ by half of
t_k(v+mu)-t_k(v-mu), bounded using (11) twice. After the outside
a^2 and full heat sum, Na=8 makes this O(a^4). All eight incident
variable edges exist at an interior vertex, so this incoming/outgoing
pairing covers its complete incidence divergence. At collar vertices
the coarse bound on each E_h suffices. Thus

    |(D^T E_h)_v|<=C_i a^4       off the collar,
    |(D^T E_h)_v|<=C_i a^4 N     on the collar.      (14)

This estimates the deterministic, already contracted external field.
Neither V, a projection prefix nor a rough tilted column has been
declared smooth. The bounds hold for the complete heat sum because
all mode losses in (11)--(14) are polynomial and (10) is uniform.

### 5. Sum by parts with the full pinned incidence

Since k is zero at boundary vertices, ordinary finite-matrix
transposition gives the exact identity

    sum_e E_h(e)(k_w-k_v)=sum_(v interior) k_v(D^T E_h)_v. (15)

The sign is fixed by Dk(e)=k_w-k_v. There is no omitted boundary
flux: all normal end edges occur on the left and their contributions
are included in D^T on the right. In particular upper pinning is
not replaced by a smooth extension. By (7), (14), and the cardinalities
of the bulk and collar,

    |sum_e E_h K_hd|
       <= C_i [N^4 N^2 a^4 + N^3 N^2 a^4 N]
       <= C_i N^2.                                 (16)

Equations (7)--(8) and (13) similarly give

    sum_e |E_d K_hh|
       <= C_i [N^4 a^4 N^2 + N^3 a^4 N N^2]
       <= C_i N^2.                                 (17)

This is a bound on the signed diagonal-difference sum after exact
summation by parts, not a pointwise bound on differences of k.
It requires neither convergence of k/N^2 nor covariance commutation.
The pure-prefix internal tilt (9) is O(N^2). Adding section 2's
O(N^(5/2)) remainder and C212b's complete O(1) external tilt proves
(1). Finally use C212h(6) without separating any original forest
flow summand to obtain (2). Both residual subtractions remain in M.

The proof uses exact bracket expansion, the previously proved full
Gaussian contraction and the complete finite incidence transpose;
no numerical approximation, mode truncation or exchange of limits is
needed. The full quartic zero coefficient is a local intermediate
result, not a candidate resolution of the Yang--Mills problem.

Reproduction check:
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/quartic_endpoint_diagonal_identity.py`.
The certificate is
`scripts/combined-ward-response/quartic-endpoint-diagonal-identity-certificate.json`.
Exact rational free-associative expansion checks all 27 cubic words
in z,vphi,wphi, verifies (3)--(4), and confirms that every nonzero
remainder word contains z. All four checks pass. This checks the
complete algebra, not the analytic covariance or boundary estimates.

### 6. Separate critical audit, 2026-10-16

The audit rederived the five-triple expansion and color contraction,
checked the external mode normalization against L185(3)--(6) and
L028(5)--(8), and verified the complete pinned transpose. No missing
term or incorrect exponent was found. The prior required audit of
this endpoint argument is discharged; this is not a recursive audit
of every upstream lemma or a complete Yang--Mills candidate review.

In particular, Sigma e_k=lambda_k^(-1)f_k, not a^2 times this vector.
The outside a^2 in (10) and the amplitude a^2 of e_l are both needed
for (12)--(14). The physical eigenvalue gap and polynomial bounds
for sampled product modes are uniform even at high frequencies.
Their polynomial losses are absorbed by the full two-mode heat sum
before any mesh limit. No supremum estimate for P on product modes
is used: SB=Sigma B removes that projection only on the external leg.

For an admitted N>=4 the full variable-edge count is exactly
4N(N-1)^3. There are 8(N-1)^3 normal end edges and
(N-1)^4-(N-3)^4 collar vertices. Thus both exceptional sets really
have O(N^3) size, including their intersections. At each noncollar
vertex, every incoming/outgoing same-component pair in (14) exists.
The bulk estimate and the unreduced collar estimate in (16) are
respectively N^4 O(N^2) O(N^-4) and
O(N^3) O(N^2) O(N^-3), both O(N^2). This does not estimate a
neighbor difference of the rough k. At a pinned endpoint the pure
polynomial (3) is itself zero because h and d are proportional;
the two terms of (9) then cancel exactly. The proof's separate
boundary bounds are therefore conservative and do not need this
additional cancellation.

The independent reproduction command is
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/audit_quartic_endpoint.py`.
Its complete certificate is
`scripts/combined-ward-response/quartic-endpoint-critical-audit-certificate.json`.
It expands the three color components using minus the cross product,
then differentiates all three fourth-moment pairings directly. It
does not call the previous word-check script or use the contracted
formula as the polynomial evaluator. Correlated full-rank, singular,
pinned-tail and pinned-head fixtures give complete responses -78,
42, -46 and -89. Each equals (4) of C212b, and each rejects a missing
factor two. Their pure-prefix internal responses are 220, 196, 0
and 0, exactly matching (8)--(9). The singular tilted fixture is
support-compatible: S=LL^T and M=LHL^T with symmetric H.

Full four-dimensional incidence fixtures at N=4 and N=6 verify (15)
with 216 and 1000 normal end edges respectively. Their normal-row
contributions are -84831/5 and -1628275/6, so omitting those rows
would fail these checks. All 22 exact checks pass; every fixture
record was inspected in full. These synthetic values certify the
stated finite algebra only, not actual-probe values or mesh bounds.
The latter follow analytically from sections 2--5 and the cited
inputs. Finally C212h(6), with its complete comparison error retained,
gives (2) without a further factor: a^3=512/N^3 and
N^(-1/2)log(eN) tends to zero. No finer-scale or compensation
conclusion follows.

## Mathlib

Full matching theorem: **not checked**. Supporting coverage of
Isserlis' theorem, finite incidence summation by parts and sampled
sine/cosine estimates: **not checked**; no absence claim is made.
The standard Isserlis fourth-moment and normalized Gaussian-tilt
specializations, including all color and factor conventions, are
imported precisely as C212b(4), proof section 1. L185(3)--(4) and
L028, proof section 2, supply the exact external mode normalization
and full-spectrum estimates. The short polynomial and incidence
calculations here are necessary specializations to the actual pinned
endpoint field; no general flow-renormalization theorem is reproved.
The unchanged [coverage assessment](../drafts/literature/2026-10-16-complete-quartic-probe-jet-scale.md)
approves this complete quartic target and supplies no theorem deciding
this selected bare response on its own.
