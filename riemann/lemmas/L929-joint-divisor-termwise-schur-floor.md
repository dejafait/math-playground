# Lemma 929: a unit floor for the termwise-modulus joint Schur test

## Hypotheses

Use exactly L928's fixed nonnegative smooth weight w, Hardy phase,
L=log T, N=floor(T^(1/5)), T<=X<=2T, and arbitrary complex coefficient
vectors c_-,c_+. All assertions below are for sufficiently large T,
uniformly in X. L737's finite divisor identities apply at this N;
its original shorter-length analytic projection claim is not used.
Write * for conjugate transpose, superscript T for transpose, and
|B| for entrywise modulus of a matrix. Matrix norms are Euclidean
operator norms. Square roots of positive Hermitian matrices are their
positive square roots. No positivity of complex Jordan weights is assumed.

The standard finite tools are imported, not reproved:

* Mika Mattila, *On the eigenvalues of combined meet and join matrices*,
  Linear Algebra Appl. 466 (2015), 1-20,
  [arXiv:1403.5907v2, Section 2, Proposition 2.5, pp. 5-6](https://arxiv.org/pdf/1403.5907v2).
  For complex f on a locally finite lattice and a meet-closed finite
  ordered set, the meet matrix has the incidence factorization E D E^T
  with the specified convolution weights. Here the divisor lattice and
  factor-closed prefix [1,N] fit these hypotheses, with f(n)=n^(1+/-2i/L).
  This is a transpose identity, not a positive Gram factorization.
* Rajendra Bhatia, *Positive Definite Matrices* (2007),
  [Propositions 1.3.1-1.3.2 and Theorem 1.3.3, pp. 13-14](https://assets.press.princeton.edu/chapters/s8445.pdf).
  For positive-definite diagonal blocks, the finite block criterion is
  the norm bound for the cross matrix conjugated by the inverse square
  roots of the two energy matrices. Only this nonsingular case is used.
* L. Grafakos and R. H. Torres, *A multilinear Schur test and multiplier
  operators*, author manuscript, 9 February 2000,
  [Section 2, classical Schur theorem, p. 2](https://grafakos.missouri.edu/preprints/multilinear_schur.pdf).
  Use the nonnegative-kernel p=2 case on finite counting measure, with
  strictly positive weights on both index sets. Its finite weighted
  Cauchy-Schwarz form is also established in L737.

For the scalar limit only, use the standard residue-one simple pole of
zeta at 1, equivalently
[NIST DLMF 25.2(i) and 25.2.4](https://dlmf.nist.gov/25.2#E4):
zeta(1+u)=1/u+O(1) near u=0. This is a starting zeta input, not a new
shifted-moment theorem or an approximation to the full matrix operator.

The invocation-start EXPLORE assessment is
drafts/literature/2026-11-09-joint-divisor-contraction-test-9.md.
Its general tools are reused for this local obstruction test. Written
9 November 2026, step 11; the separate audit in step 113 below
validates the stated finite obstruction and scalar pairing.

## Conclusion

There is an exact common-coordinate expression for L928's cross form
with both full diagonal metrics retained. In that expression, the
nonnegative majorant obtained by taking the two conjugate zeta terms'
moduli separately has norm at least

    r_(T,X)=1+O(1/L), uniformly in X.                         (1)

Consequently every valid weighted Schur upper bound for that majorant
is at least 1-C/L for one common C, and cannot be <=1-eta eventually
for any fixed eta>0. This includes arbitrary T,X-dependent positive
Schur weights; improving the weights cannot remove this floor.

The exact divisor-1 direction, in the same full energy metrics, has
combined relative cross pairing

    sin(1)+O(1/L).                                           (2)

Thus the termwise majorization loses at least 1-sin(1)+O(1/L) on
this direction; this is not an asymptotic equality for the norm of P.
The required strict contraction is NOT disproved: (1) concerns a
majorant, and (2) is only one test direction, not the operator norm.
No joint coercivity, joint bump projection, Xi sign, or RH conclusion
follows. No bound for a possibly vanishing adequate joint margin is
established either. This is a local negative diagnostic using known
tools; the checked search did not establish prior coverage of this
exact diagnostic, and no certified originality is claimed.

## Proof

### 1. Both complete diagonal forms in common divisor coordinates

Let phi be Euler's totient, phi(1)=1, and define the invertible real
upper triangular matrix

    G_(d,n)=1_(d|n)*sqrt(phi(d)/n), 1<=d,n<=N.

Its diagonal entries are positive. With L928's coefficient rotations
D_s=diag(n^(i*s/L)), put y_s=G D_s c_s. These are arbitrary complex
vectors in the same indexed Euclidean space: G D_s is invertible.
Use L737's kappa(d)=sum_(p|d)log(p)/(p-1) and real matrix

    K_(d,n)=Lambda(n/d)*sqrt(phi(d)/phi(n)) if d|n and n>d,
    K_(d,n)=0 otherwise.

Define real scalars and real symmetric matrices

    a_s=T^(-1) integral w_XT(t) A_(t,s) dt,
    H_s=a_s I+2 diag(kappa(d))-K-K^T.                         (3)

L737 (6)-(7), applied to D_s c_s and integrated, gives exactly

    D_s(c_s)=T y_s^* H_s y_s,                                (4)

where the left side denotes the integrated diagonal form in L928(11),
not the coefficient rotation matrix. In particular no logarithmic
cross term has been discarded. L737 (10) gives
H_s >= (a_s-4log N) I. On the common support t in [T,3T],
a_s=L+O(1), uniformly in X,s. Hence H_s is positive definite eventually,
since 4log N<=4L/5. Its square roots and inverses therefore exist.
Since kappa(1)=K_(1,1)=0,

    e_1^* H_s e_1=a_s.                                     (5)

Equation (5) is a quadratic-form evaluation, not an assertion that
e_1 is an eigenvector or that H_s can be replaced by a_s I.

### 2. Exact complex incidence factors and the time integral

For complex z write J_z(d)=sum_(r|d)mu(r)(d/r)^z, using real logarithms
of positive integers. Define

    j_+(d)=J_(1+2i/L)(d)/phi(d), j_-(d)=conjugate(j_+(d)),
    M=G diag(n^(-2i/L)) G^(-1),
    W_+=M^T diag(j_+) M, W_-=diag(j_-),
    beta_±=zeta(1±2i/L)*T^(-1)
       *integral w_XT(t) exp(i epsilon_t) exp(±i ell_t/L) dt,
    V=beta_+ W_+ + beta_- W_-.                              (6)

All matrices and scalars in (6) are exact; in particular the Hardy
phase epsilon_t and both time integrals remain present.

Apply the cited incidence identity to the first summand of L928's R_t.
Its spatial kernel, excluding exp(i ell_t/L)zeta(1+2i/L), is

    gcd(m,n)^(1+2i/L) (m*n)^(-1/2-i/L).

The divisor sums on the plus vector and the conjugated minus vector
are respectively G D_- c_+ and conjugate(G D_+ c_-), with weight j_+.
In the coordinates already chosen, they equal M y_+ and
conjugate(conjugate(M) y_-). Their bilinear pairing is consequently
y_-^* M^T diag(j_+) M y_+. This verifies the transpose, rather than
an adjoint, in W_+. The second spatial kernel has conjugate exponent
and divisor sums G D_+ c_+=y_+, conjugate(G D_- c_-)=conjugate(y_-);
it gives y_-^*diag(j_-)y_+. Integration yields exactly

    C(c_+,c_-)=T y_-^* V y_+.                               (7)

There is no assertion that either W_+ or W_- is positive Hermitian.
The reversed block in L928 is the adjoint of the complete block (7).

Set

    B_±=H_-^(-1/2) W_± H_+^(-1/2),
    B=beta_+ B_+ + beta_- B_-,
    P=|beta_+| |B_+| + |beta_-| |B_-|.                       (8)

By (4),(7), the exact supremum of the relative pairing in L928(11)
is ||B||. This is precisely the positive-definite case of Bhatia's
criterion; all vectors remain arbitrary after the invertible changes.
The nonnegative matrix P satisfies |B|<=P entrywise, hence ||B||<=||P||.
This is the selected termwise-modulus majorant, after exact normalization
by both full energy matrices. No nonunitary change was treated as unitary.

### 3. Weighted Schur estimate and its unavoidable floor

For any strictly positive finite vectors p=(p_i),q=(q_j), define

    R(p,q)=max_i sum_j P_(i,j) q_j/p_i,
    S(p,q)=max_j sum_i P_(i,j) p_i/q_j.                      (9)

These are both weighted orientations. The cited finite Schur bound is

    ||B|| <= ||P|| <= sqrt(R(p,q)*S(p,q)).                  (10)

For example p_i=q_j=1 is an admissible positive choice with finite
R,S; the following lower bound rules out every such choice at once.

Because G e_1=e_1 and G^(-1)e_1=e_1, M e_1=e_1. Also j_±(1)=1.
It follows directly from (6), including the transpose, that

    e_1^* W_+ e_1=e_1^* W_- e_1=1.                         (11)

Define unit vectors u_s=H_s^(1/2)e_1/sqrt(a_s), using (5).
Their entries need not be nonnegative. Exact cancellation of the
positive square roots on the two sides gives

    u_-^* B_± u_+=1/sqrt(a_- a_+).                          (12)

For each of the two matrices, the triangle inequality bounds the
modulus of its pairing in (12) by |u_-|^T |B_±| |u_+|. Summing
with the nonnegative scalar coefficients in (8) proves

    ||P|| >= |u_-|^T P |u_+|
           >= (|beta_+|+|beta_-|)/sqrt(a_- a_+) =: r_(T,X). (13)

The first inequality uses that entrywise modulus preserves the
Euclidean norms of these two unit vectors. Equations (10),(13) imply
sqrt(R S)>=r_(T,X) for every positive p,q. More generally the same
floor holds for any entrywise nonnegative majorant of P. This is a
lower bound on the proposed upper-bound certificate, not on ||B||.

### 4. Scalar asymptotics and the charged cancellation loss

L928 proves epsilon_t=O(1/(T L)), uniformly on [T,3T]. Also
ell_t/L=1+log(t/(2pi T))/L=1+O(1/L). The bound
|exp(i v)-exp(i v_0)|<=|v-v_0| for real v,v_0, integrated against
w_XT/T of mass 1, therefore gives

    T^(-1) integral w_XT exp(i epsilon_t)exp(±i ell_t/L) dt
         =exp(±i)+O(1/L), uniformly in X.                   (14)

This estimate is used only for the scalar limits in (13) and (16)
below; no matrix entry or operator has had its phase deleted. The
residue-one pole gives

    zeta(1+2i/L)=L/(2i)+O(1),
    zeta(1-2i/L)=-L/(2i)+O(1).

Thus

    beta_+=L exp(i)/(2i)+O(1),
    beta_-=-L exp(-i)/(2i)+O(1),
    |beta_+|+|beta_-|=L+O(1),
    beta_++beta_-=L sin(1)+O(1).                            (15)

Since a_s=L+O(1), sqrt(a_- a_+)=L+O(1). Equations (13),(15) give
r_(T,X)=1+O(1/L). For a common C and any fixed eta>0, all sufficiently
large T have r_(T,X)>=1-C/L>1-eta, uniformly in X. By (10),(13),
no weighted Schur bound for P can then certify the requested strict gap.

In contrast (12) and (15) yield the exact-direction limit

    |u_-^* B u_+|=|beta_++beta_-|/sqrt(a_- a_+)
                 =sin(1)+O(1/L).                          (16)

Subtracting (16) from (13)'s scalar r gives a guaranteed loss tending
to 1-sin(1). The pairing with P may be larger than r. This comparison
quantifies the cancellation
destroyed by the chosen majorant even before any Schur row estimates
are loosened. It gives no upper bound for the full B on other vectors.

### 5. Scope of the stop and remaining operator

The unresolved operator is exactly B in (8), with the two terms added
before taking norms. The achieved certificate floor is 1-O(1/log T);
the required fixed-gap upper bound is 1-eta. Even exact optimization
of (9)'s weights cannot bridge this discrepancy for P. The proof does
not exclude a cancellation-preserving comparison of B or an adequate
weaker joint margin. In particular it cannot be combined with L928(3)-(5)
to obtain a positive joint lower bound: it supplies no margin to absorb
their error, whose available relative size is O(T^(-9/80)/log T).

The earlier L928 unpaid-coercivity and step226 stops are unchanged.
This informative obstruction stops the present termwise-modulus Schur
estimate, including repetitions with different positive weights.
A later attempt would need to control the combined operator's
cancellation, with the full metrics and phases, rather than repeat this
majorant or infer a full bound from (16). All local sums are finite;
no infinite divisor limit, RH-equivalent premise or cross-notebook input
has been used.

### Separate finite-matrix and scalar audit — 9 November 2026, step 113

The prior SPECIALIZE assessment is
drafts/literature/2026-11-09-l929-termwise-floor-audit-112.md.
Reused its inspected primary statements and the separate source
approval in the divisor-contraction assessment. The audit object is
the proof above; it is not an input to its own verification. L928's
audited cross kernel, L737's finite identities (6)-(10) and L637's
fixed Hardy/weight conventions suffice. No older short-length
projection assertion or unaudited joint estimate is used.

**Complete energies.** For v=D_s c_s, L737 has
sqrt(phi(d)) B_d=(Gv)_d=y_(s,d) and
sqrt(phi(d)) C_d=(K y_s)_d. Its real Hermitian expression (6)
is therefore exactly y_s^*[A I+2 diag(kappa)-K-K^T]y_s.
Integration has mass T, giving (3)-(4), including all logarithmic
terms. The finite Schur bound ||K||<=2 log N holds at every N>=2;
its proof does not depend on an analytic length restriction.
Consequently H_s>=(L/5-C)I eventually, uniformly in X and both s.
All square roots are positive Hermitian square roots. The zero
diagonal of K and kappa(1)=0 give (5), despite nonzero off-diagonal
entries in H_s. No eigenvector assertion is needed.

**Complex orientations.** Finite convolution gives
sum_(d|m,d|n)J_z(d)=gcd(m,n)^z. For the plus exponent in (6),
the plus coefficient channel is G D_- c_+=M y_+; the conjugated
minus channel before conjugation is G D_+ c_-=conjugate(M)y_-.
Conjugating that channel turns its pairing into
y_-^* M^T diag(j_+) M y_+, with exactly a transpose.
For the minus exponent the channels are y_+ and conjugate(y_-),
giving diag(j_-). The factors exp(i epsilon_t)exp(±i ell_t/L)
belong to the time integrals beta_±. This checks (6)-(7) directly
against L928(1)-(2); no term's phase is removed. As G D_s is
invertible, every energy-normalized vector pair is admissible.
Setting x_s=H_s^(1/2)y_s verifies the norm statement in (8),
with H_-^(-1/2) on the left and H_+^(-1/2) on the right.
The cited block theorem applies to these strictly positive blocks.

**All Schur weights.** For the p,q in (9), weighted Cauchy-Schwarz
is the assessed finite Schur specialization and uses both bounds:
sum_i |(Pz)_i|^2<=R sum_j |z_j|^2/q_j sum_i p_i P_(i,j)
<=R S ||z||^2. This checks their orientations, without imposing a
common weight or parameter-independent weights. Since M e_1=e_1,
(11) holds for both W matrices. The u_s in (12) have norm one
by (5). Cancelling the inverse square roots proves (12) even though
neither u_s need be entrywise nonnegative. Taking their entrywise
moduli preserves their norms, so (13) and sqrt(R S)>=r hold for
every positive p,q, including arbitrary moving choices. They provide
no lower bound r for the combined operator B.

**Uniform scalar limit.** On every weight support t/T is in [1,3].
L928's phase estimate is O(1/(T L)), and log(t/(2pi T)) is bounded
there by an absolute constant. The normalized nonnegative measure
w_XT(t)dt/T has mass one. Thus the error in each time integral in
(14) is uniformly O(1/L). Multiplication by the scalar pole terms
±L/(2i)+O(1) costs only O(1), giving all four statements in (15).
Also a_s=L+O(1), with common constants and positive a_s eventually.
It follows that |r-1|<=C/L and that (16) holds uniformly in X.
One onset, depending on a fixed eta, makes r>1-eta for every X;
none depends on coefficient vectors or Schur weights.

Audit result: (3)-(16) pass under the stated named imports. The
loss wording above is made explicitly a guaranteed lower bound:
r-|u_-^*B u_+|=1-sin(1)+O(1/L), whereas the pairing with P can
be larger than r. The proof never determines ||P|| asymptotically.
No other formula or direct mathematical dependency changes.
This first separate validation is REPRODUCTION, not a new theorem
beyond the checked sources. The stopped majorant, possible shrinking
joint margins, signed realization and actual-Xi all-degree signs
retain their original qualifications. No numerical evidence or
infinite limiting divisor rearrangement is used.

## Mathlib

Full matching coverage of this joint divisor-coordinate specialization
and majorant obstruction has not been checked and is unknown. Finite
matrices, positive square roots, complex modulus, Möbius convolution
and Schur bounds are supporting topics, not a verified matching theorem.
The cited general results remain named imports. The separate informal
audit above is not formal verification or a new Mathlib coverage search.
