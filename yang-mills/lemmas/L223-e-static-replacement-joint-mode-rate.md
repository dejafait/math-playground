# L223 — A joint-mode rate for the full E static replacement

## Hypotheses

Use exactly L101's R_E, finite static expression, coordinates and
operators for the two actual probes i=3,6: SU(2), the relative pinned
box (-4,4)^4, straight lower-rooted direction-1 forest, admitted even
N, a=8/N and tau=1/16. Take the small-coupling coefficient at fixed
mesh before refinement. The triplet is L008's average of squares and
the shear retains its clover factors. All axial levels, transverse end
rows, constant input modes and exterior heat modes remain.

In L101's notation let

    H_k=Zeta_k U B,  B_(s,r)=1_(r<s), 1<=s<N, 0<=r<N,
    Y_k=K_h^(1/2) Cc^T H_k-K_h^(1/2) F_k U B,
    Y_(k,*)=L_* H_k,  F_11=H_T^(-1/2) A_11 H_T^(-1/2).

U acts only transversely and has norm one. F_k is the exterior-
circulation map; it is distinct from the scalar residual F_11.
Import L065's ||F_11||<=C, L101(6)–(8)'s exact trace and actual
coefficient bounds, and L097/L101's full joint spectral comparison.
In particular, for the same fixed polynomial p(k), uniformly in N,

    ||Zeta_k(s)||<=C a p(k),
    ||Zeta_k(s+1)-Zeta_k(s)||<=C a^2 p(k), 1<=s<N-1,
    sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i.                 (1)

These are bounds between existing interior levels, justified by the
actual exterior coefficients and L028's lift estimates as imported
in L101. No smooth extension across the upper pin is assumed.

## Conclusion

Let T_(i,N) denote exactly the finite static sum in L101(3), namely

    T_(i,N)=sum_(k,l)c_(i;kl,a) sum_(s=1)^(N-1)
      Tr_T[T G A_<s G T^T Zeta_k(s)^T S_T Zeta_l(s)].

There is C_i independent of sufficiently large admitted N such that

    |R_E-T_(i,N)|<=C_i N^(5/2).                       (2)

This improves L101's O(N^(27/10)) allowance and is stronger than the
requested O(N^(5/2) log(eN)^2). The cubic-scaled replacement error is
O_i(N^(-1/2)). The moving-cut term of A_<s in L101(13) is unchanged.

This is a local quantitative refinement using standard finite spectral
and summation methods; no originality beyond the checked sources is
claimed. The separate critical audit in proof section 4 accepts this
rate relative to the stated imported inputs. It does not
bound T_(i,N)-a^(-3)K_(i,E), give a complete-response rate, discharge
L220's separate audit, or improve the interacting reflected-error
threshold <=c_box/2. Continuum axioms and finite positive mass remain
unproved; there is no complete-solution candidate.

## Proof

### 1. Import the scalar spectrum and retain the endpoint in each prefix

The Dirichlet axial path spectrum is

    phi_m(s)=sqrt(2/N) sin(pi m s/N),
    mu_m=4 sin^2(pi m/(2N)), 1<=m<N.

This scalar diagonalization is imported from J. S. Dowker,
[*Heat-kernels on the discrete circle and interval*](https://arxiv.org/pdf/1207.2096v2),
v2, 31 August 2012, section 7, printed pp. 10–11, equations (30)–(31),
with p=N. Its domain has zeros at both axial vertices 0,N and exactly
N-1 interior rows, agreeing with L101's L_D. It is applied only to
the axial factor in the already established cochain comparison, not
to every gauge component. The source was inspected in the approved
assessment; no scalar kernel theorem is reproved here.

For any 1<=u<=v<N, a finite geometric sum gives

    |sum_(s=u)^v phi_m(s)|
      <=sqrt(2/N)/sin(pi m/(2N))
      =2 sqrt(2)/(sqrt(N) sqrt(mu_m)).                (3)

Indeed the modulus of a sum of exp(i theta s) is at most
2/|1-exp(i theta)|=1/sin(theta/2), and the sine sum is its
imaginary part. This holds also at the largest m, without a
small-frequency approximation.

Fix any unit transverse curvature vector e, not necessarily a mode,
and put v_s=e^* Zeta_k(s)U, a row on the transverse scalar input.
For input increment r the (phi_m,e) output row of H_k has block

    h_(m,e;r)=sum_(s=r+1)^(N-1) phi_m(s) v_s.        (4)

For r=N-1 this is the zero row. For other r, set
P_t=sum_(s=r+1)^t phi_m(s). Finite Abel summation gives exactly

    h_(m,e;r)=P_(N-1) v_(N-1)
        +sum_(s=r+1)^(N-2) P_s(v_s-v_(s+1)).        (5)

In particular the upper term is present even if the forest potential
has a nonzero upper limit. No difference to an artificial smooth
value at level N is taken. Equations (1), (3), ||U||=1 and Na=8 give

    ||h_(m,e;r)||
      <=C/(sqrt(N) sqrt(mu_m))
          [a p(k)+N a^2 p(k)]
      <=C' a p(k)/(sqrt(N) sqrt(mu_m)).              (6)

The N increment blocks are orthogonal coordinate blocks on the
input side, so their squared row norms add. Consequently

    ||(phi_m^* tensor e^*)H_k||^2
       =sum_(r=0)^(N-1)||h_(m,e;r)||^2
       <=C a^2 p(k)^2/mu_m.                         (7)

The lower prefix start and the nonzero upper endpoint have both been
included. This estimate does not bound a derivative of a rough
column or commute Zeta_k with a transverse projection. It uses only
the total axial variation of its actual operator coefficients.

### 2. Sum the joint spectral error before making a transverse cutoff

Let D=K_h^(1/2) Cc^T-L_*. Choose an orthonormal eigenbasis e_j in
im D_T of transverse curvature space, induced from the co-closed
transverse edge eigenbasis by e_j=D_T f_j/sqrt(lambda_j), where
lambda_j>0. L101(9) gives on each (phi_m,e_j) mode

    D^*D=(1-sqrt(lambda_j/(mu_m+lambda_j)))^2
         <=mu_m/(mu_m+lambda_j).                    (8)

D vanishes on the orthogonal curvature complement ker D_T^T.
Using the complete orthogonal output expansion and (7),

    ||D H_k||_HS^2
      <=C a^2 p(k)^2 sum_(m,j) 1/(mu_m+lambda_j)
      = C a^2 p(k)^2 Tr K_h
      <=C' p(k)^2 N^2.                              (9)

The equality uses the same co-closed spectrum as K_h; it introduces
no new scalar boundary prescription. The final bound is precisely
the full relative spectral estimate Tr K_h<=C N^4 imported in
L101 section 1 and L097(10). Its tensor counting retains all relative
component multiplicities and normal end rows. Equivalently, its
positive joint energies are bounded below by c|n|^2/N^2 with at
most C q^3 labels in max-coordinate shell q; their inverse sum is
at most C N^2 sum_(q=1)^N q=O(N^4). There is no omitted zero joint
mode because the axial Dirichlet index is positive. Constant modes
in allowed individual transverse coordinates remain in the count.

Thus ||D H_k||_HS<=C p(k)N. This improves the O(p(k)N^(6/5))
factor error in L101. The mu_m denominator in (7) is used jointly
with the multiplier numerator in (8); replacing either one first by
its worst norm would lose this gain. No varying-mass limit or
coefficient freezing occurs.

### 3. Restore the exterior-circulation terms and the full signed pairing

L101(7)–(10) already establish

    ||K_h^(1/2) F_k U B||_HS<=C p(k)N,
    ||H_k||_HS<=C p(k)N^(3/2).

For clarity, the first bound follows from ||F_k||<=C a^2 p(k),
||UB||<=CN and ||K_h^(1/2)||_HS<=CN^2. Both the dynamic
curvature map K_h^(1/2)Cc^T and L_* are contractions. Together
with (9), these give

    ||Y_k-Y_(k,*)||_HS<=C p(k)N,
    ||Y_k||_HS+||Y_(k,*)||_HS<=C p(k)N^(3/2).         (10)

Use the exact telescoping identity

    Y_k F_11 Y_l^T-Y_(k,*) F_11 Y_(l,*)^T
      =(Y_k-Y_(k,*))F_11 Y_l^T
        +Y_(k,*)F_11(Y_l-Y_(l,*))^T.

Hilbert–Schmidt Cauchy–Schwarz and L065's signed scalar form bound
then bound its trace in absolute value by

    C p(k)p(l) N^(5/2).                              (11)

No positivity of F_11, no level-diagonal residual, and no cancellation
between distinct exterior pairs is assumed. L101(6) is exactly the
sum of the first pairings. L101 section 2 identifies the complete
static pairing with T_(i,N), using the real symmetric c_(i;kl,a)
sum. Apply (1) to (11) to obtain (2), for i=3 and i=6. This sums
every exterior heat label with the same previously available
polynomial, so there is no additional unsummed frequency dependence.

The static expression has not been altered. In particular the
quarter-weight layer and the term
(2a)^(-1) sum_mu T_mu^T M_(u_(a,1)(s)) T_mu in L101(13)
remain at every moving cut s. The estimate concerns only replacing
the original covariance factors by that exact finite expression.
All subsequent continuum and interacting comparisons are separate.

### 4. Separate critical audit, 2026-10-17

This audit checks the new estimates (3)–(11) relative to L101's
exact finite contraction and spectral identification. It imports,
rather than re-audits, L008's probe definitions and heat framework,
L028's pre-retraction regularity, L065's scalar form theorem and
L097/L101's coefficient and cochain identities. The approved scope
is `drafts/literature/2026-10-17-e-static-joint-mode-rate-audit.md`.
The result of the audit is acceptance of (2) under precisely these
inputs; no extra smoothness or commutation hypothesis is needed.

**Axial row and endpoints.** In ordinary stored coordinates the
input to B is the direct sum of N copies of the transverse vertex
space. For a fixed transverse unit vector e, the output row after
the normalized sine transform is exactly (4), with r=0 included
and r=N-1 empty. The geometric identity underlying (3) is

    sum_(s=u)^v exp(i theta s)
      =exp(i theta u)[1-exp(i theta(v-u+1))]/[1-exp(i theta)].

Here theta=pi m/N lies strictly between 0 and pi, so its denominator
is nonzero and its modulus is at most 1/sin(theta/2). There is no
unjustified low-frequency approximation. Writing phi_m(s)=P_s-P_(s-1)
with P_r=0 telescopes to (5); its sign and its v_(N-1) endpoint are
therefore correct. The variation has at most N-2 terms. Its bound is

    ||v_(N-1)||+sum_(s=r+1)^(N-2)||v_s-v_(s+1)||
       <=C p(k)[a+N a^2]<=9C a p(k).

L097(9) explicitly covers N-2,N-1. No value v_N or difference to it
enters. For a block row [h_0 ... h_(N-1)], its squared Euclidean
row norm is sum_r ||h_r||^2 because its input summands are orthogonal.
This is not an assertion that different prefix outputs or Gaussian
fields are independent. Combining this identity with (3) verifies
the factor N and hence (7), uniformly for every transverse unit e.
Thus the estimate also applies to the eigenvectors used in section 2,
even though Zeta_k mixes transverse frequencies.

**Co-closed spectrum and joint count.** Write

    d_(m,j)=1-sqrt(lambda_j/(mu_m+lambda_j)).

For the maps with their common partial isometry in L101(9),
D^*D is diagonal with eigenvalues d_(m,j)^2 on im D_T, and is zero
on ker D_T^T. If t=mu_m/(mu_m+lambda_j), then
(1-sqrt(1-t))^2<=t for 0<=t<=1, proving the inequality in (8).
The finite-dimensional trace identity is therefore exactly

    ||D H_k||_HS^2
      =sum_(m,j) d_(m,j)^2
                    ||(phi_m^* tensor e_j^*) H_k||^2.

Inserting (7) bounds each summand by
C a^2 p(k)^2/(mu_m+lambda_j). The cancellation of mu_m occurs
inside this joint sum, before any separate operator-norm bound.
The transverse co-closed modes and curvature modes have identical
positive multiplicities through D_T/sqrt(lambda_j), as imported
in L101; this is why the sum is Tr K_h rather than the trace of a
different scalar covariance. For an upper bound it is also bounded
by the full relative transverse-edge tensor spectrum. In a joint
max-index shell q that spectrum has at most C q^3 labels and each
positive energy is at least c q^2/N^2. Thus the entire inverse sum
is at most C N^2 sum_(q=1)^(N-1) q<=C' N^4. Allowed zero own-coordinate
indices remain; the positive axial sine index precludes a zero joint
energy. No transverse end row is removed. With a=8/N, the squared
error is O(p(k)^2 N^2), as claimed, not merely a cutoff-dependent
estimate. The zero curvature complement contributes exactly zero.

**Full pairing, normalization and heat sum.** The elementary bound
||B||<=||B||_HS=(N(N-1)/2)^(1/2)<=N applies before tensoring
with U; ||UB||<=N follows. Consequently the complete F_k term costs
at most C N^2 a^2 p(k)N=O(p(k)N) in Hilbert–Schmidt norm. It is
not dropped. Independently,

    ||H_k||_HS^2
      =sum_(s=1)^(N-1) s ||Zeta_k(s)U||_HS^2
      <=C p(k)^2 a^2 N^2 (N-1)^3
      <=C' p(k)^2 N^3.

This uses rank U=(N-1)^3 and no axial smooth extension. Both
curvature-to-link maps are contractions on the stated domains, so
these inequalities give both bounds (10). L065's real symmetric
form inequality yields ||F_11||<=C by the spectral theorem after
conjugation with H_T^(-1/2); it supplies no positivity. Applying
|Tr(X F_11 Z^T)|<=||X||_HS ||F_11|| ||Z||_HS to the two displayed
telescoping terms gives N times N^(3/2)=N^(5/2) in each placement.
In particular all F_k/F_l cross terms are included through the
unchanged Y_l in the first placement and the complete difference
in the second. Neither residual order nor off-diagonal axial
entries have been altered.

The exact coefficients c_(i;kl,a) are still those of L101(6).
L008(2)'s average of squares for i=3 and clover products for i=6
remain inside them, and no outside other/other assembly factor 3
is introduced. The audit's constants have only the original
p(k)p(l) dependence. Thus L101(8)'s uniform absolute heat sum
applies directly to (11), with no new frequency cutoff, unsummed
factor or illicit limit interchange. Cycling the finite static
pairing selects (B F_11 B^T)_ss as in L101 section 2; its exchange
of k,l uses the complete real symmetric coefficient sum, not a
termwise identity for an individual ordered heat pair. This checks
that the subtracted expression is exactly T_(i,N). L101(13)'s
quarter layer and moving-cut endpoint are retained unchanged.

**Decision and limits of the audit.** All three load-bearing stages
close with the stated imported hypotheses. The achieved replacement
bound is O(N^(5/2)), hence O(N^(-1/2)) after multiplication by a^3;
there is no logarithmic loss in this comparison. The static expression's
continuum rate is still unproved. ATTEMPTS/024–025 concern a different
axial-profile replacement or trace bound, ATTEMPTS/030 prohibits an
uncontrolled varying-mass limit, and ATTEMPTS/045 prohibits smoothness
of a rough projection-side prefix. None of those steps is used here.
This is verification of the existing standard-method rate, not a
new theorem beyond the checked literature or an audit of upstream
construction claims. All limitations in the conclusion remain.

## Mathlib

Full matching actual-probe static-replacement theorem: **not checked**.
Supporting finite sine diagonalization, Abel summation, spectral
calculus, Hilbert–Schmidt trace inequalities and heat summability:
**not checked**. No absence claim is made. The precise scalar spectral
input above is a literature import; the new work is its quantitative
application to the ordered variable-coefficient full prefix.
