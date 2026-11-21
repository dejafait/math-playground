# Corollary C028y: two-site diffuse spectral envelope and actual-target overlap

## Hypotheses

Use the full even theta probability mu_0, its monic polynomials p_j,
positive squared norms k_j and beta_j=k_j/k_(j-1) from C028x. Use
its audited conclusion

    max_(1<=j<=n) beta_j / sum_(j=1)^n beta_j -> 0.

For integer d>=4 and arbitrary real a<b, let pi_j and eta_j be the
monic polynomials and squared norms for mu_0+delta_a+delta_b, exactly
as in C028w. Write lambda_1,...,lambda_d for the real zeros of pi_d,
m=(sum_i lambda_i)/d, and

    E=(1/2)*sum_i (lambda_i-m)^2,
    G=-(1/3)*sum_i (lambda_i-m)^3/E^(3/2),
    L=1/2-(1/4)*sum_i (lambda_i-m)^4/E^2.

These equal C028w's centered coefficient invariants. The sites may
depend arbitrarily on d, become unbounded, or coalesce in a limit;
each finite pair still satisfies a<b. Define base-only quantities

    T_d=sum_(j=1)^(d-1) beta_j,
    M_d=max_(1<=j<=d-1) beta_j, r_d=2*sqrt(M_d).

For the application to actual coefficients, use C028w's b_j,v>0,
tau>0,omega and set kappa=(3*v^2-omega)/6. The actual-target overlap
statement below additionally uses C028c's already audited enclosures
for v=S_2,tau=S_3,kappa=S_4. It inherits that result's L778 entire
evaluator and Python3.15.2/Decimal1.70/libmpdec4.0.1 contracts,
including allcr=1. Backend correctness is not independently attested.
The spectral statements do not need this numerical assumption.

No root-reality assumption for the actual P_d, RH, compact-site
assumption, individual recurrence asymptotic, moving-atom limit, or
small full residual cost is imposed.

## Conclusion

For every finite d and a<b,

    E >= T_d-2*r_d^2*(1+1/(d-2)).                         (1)

At most two zeros of pi_d lie outside [-r_d,r_d]. For all sufficiently
large d, uniformly in a<b, E>=T_d/2. Put

    epsilon_d=2*sqrt(8*M_d/T_d)+2/(d-2) -> 0.

There are real u_1,u_2 with u_1^2+u_2^2<=2 such that

    |G+(u_1^3+u_2^3)/3| <= 2*epsilon_d/3,
    0 <= 1/2-(u_1^4+u_2^4)/4-L <= epsilon_d^2/2.         (2)

They are the centered zeros outside the displayed interval, divided
by sqrt(E), padded by zeros when there are fewer than two. Thus the
two-site shape image approaches, uniformly, the compact set

    K_2={(-(u_1^3+u_2^3)/3,
                    1/2-(u_1^4+u_2^4)/4): u_1^2+u_2^2<=2}.       (3)

Consequently a feasible sequence in C028w with d->infinity and
B_d/d^2->0 requires real x_1,x_2 satisfying

    x_1^2+x_2^2<=v,
    x_1^3+x_2^3=tau,
    x_1^4+x_2^4=kappa.                                  (4)

If (4) had no solution, this would prove an eventual uniform retained
floor B_d>=c*d^2 for some c>0. For the actual coefficients, however,
the inherited C028c enclosures prove

    v^2>2*kappa>0, kappa^3<tau^4<2*kappa^3.              (5)

These imply that (4) has a solution x_1>x_2>0 with
x_1^2+x_2^2<v. Hence the actual pair

    G_*=(tau/3)/(v/2)^(3/2), L_*=omega/(6*v^2)

belongs to K_2. Separation using only this necessary spectral envelope
fails. Membership in K_2 is not realization by the shared Uvarov system.
Neither a retained floor nor a feasible vanishing-cost sequence is
proved. Even realized limiting shapes would require weighted residual
rates or exact cancellation; all omitted full costs and H_d=o(d)
remain open. Independent conceptual audit of the full result is pending.
The separate audit1942 in C028z accepts the finite compression (6)
and the strict-solution construction from (5), under the inherited
C028c contracts. The other uniform envelope claims remain unaudited.

## Proof

### Finite source interfaces and what is being specialized

Reuse the positive-measure monic recurrence, norm-ratio and Jacobi-zero
identification in NIST [DLMF18.2(iv),(vi), equations18.2.11_4-8 and
18.2.18](https://dlmf.nist.gov/18.2), as assessed in source-notes1931.
The full theta density is positive with all moments; adding positive
atoms preserves positive definiteness in every degree. The base is
even, so its Jacobi diagonal is zero. Both reference zero statements
apply, with no hypothesis about actual P_d zeros.

The same modified measure is given by A. M. Delgado, L. Fernandez,
T. E. Perez and M. A. Pinar, *Multivariate Orthogonal Polynomials and
Modified Moment Functionals*, SIGMA12(2016),090,
[Theorem3.1,(3.1)-(3.14),pp8-10](https://www.emis.de/journals/SIGMA/2016/090/sigma16-090.pdf),
under original and modified quasi-definiteness, verified here by
positivity. Its two-unit-atom specialization is C028w's shared system
(5)-(7). Those source formulas are imported, not reproved. We express
the finite multiplication form of exactly that measure in an enlarged
Euclidean space to obtain a bound uniform in both sites. No update
coefficient is varied independently, and no asymptotic mass-point
theorem is imported. The elementary block calculations below establish
the needed constants and centering control rather than replacing a
known general Uvarov theorem with a new proof.

C028x supplies M_d/T_d->0 under its named Levin--Lubinsky and Szego
imports; their specializations are not repeated. C028w supplies the
exact cost identities and the implication B_d/d^2->0 => (G,L)->(G_*,L_*).
Its used scalar step is checked below. The additional actual coefficient
enclosures are imported from C028c with their stated contracts, not
computed again from a finite theta approximation.

### Exact compression and the count of exceptional zeros

In the degree<d space use the base orthonormal basis
phi_j=p_j/sqrt(k_j), 0<=j<d. Its multiplication form is the symmetric
matrix J with zero diagonal and adjacent entries sqrt(beta_j).
For every real vector c,

    |c^t J c| <= sqrt(M_d)*sum_(j=1)^(d-1)(c_(j-1)^2+c_j^2)
                <=r_d*||c||^2.

Thus ||J||<=r_d and tr(J^2)=2*T_d. Let V be the 2-by-d matrix with
rows (phi_j(a))_j and (phi_j(b))_j, and D=diag(a,b). In this basis the
modified inner product and multiplication form are exactly

    G_0=I_d+V^t V, H_0=J+V^t D V.

G_0 is positive definite. With its positive inverse square root put

    Q=[I_d; V]*G_0^(-1/2),
    A=G_0^(-1/2)*H_0*G_0^(-1/2).

Then Q^t Q=I_d and

    A=Q^t diag(J,a,b) Q.                                (6)

Changing between this modified orthonormal basis and the orthogonal
polynomial basis is orthogonal. The imported Jacobi identification
therefore gives the eigenvalues of A as exactly the lambda_i.
This is a finite compression identity, not a limit of Jacobi matrices.

Here is the precise spectral dimension check. If diag(J,a,b) has
s_+ eigenvalues greater than r_d, any subspace on which its quadratic
form minus r_d times the squared norm is positive definite has
dimension at most s_+: otherwise it intersects the span of the
nonpositive eigenvectors. Q maps the corresponding positive spectral
subspace of A isometrically to such a subspace. Therefore A has at
most s_+ eigenvalues above r_d. The identical argument applied to
-A bounds the number below -r_d by s_-. Only the two scalar entries
a,b can contribute to s_++s_-, since ||J||<=r_d. Hence at most two
lambda_i lie outside [-r_d,r_d], counted with multiplicity. This
checks the finite spectral theorem consequence needed for (6);
there is no assumption that exceptional zeros converge to the sites.

### Uniform lower bound on the centered variance

The two rows of V are independent: their first two entries are
(1,a/sqrt(k_1)) and (1,b/sqrt(k_1)), since k_0=1 and p_1(x)=x.
Thus W=ker V has dimension d-2. On W, G_0 and G_0^(-1/2) act as
the identity, and the compression of A is the compression K of J.
Decompose the base space as W plus its two-dimensional orthogonal
complement, writing

    J=[K C; C^t D_0].

The bound ||J||<=r_d gives

    ||C||_F^2+tr(D_0^2)<=2*r_d^2,
    tr(K^2)=2*T_d-2*||C||_F^2-tr(D_0^2)
                    >=2*T_d-4*r_d^2,
    |tr K|=|tr D_0|<=2*r_d.

The first inequality follows by evaluating J^2 on an orthonormal basis
of the two-dimensional complement. The trace identity uses tr J=0.
Compressing A-m*I to W gives K-m*I_(d-2). Squared Frobenius norm
cannot increase under compression, by writing the omitted blocks as
sums of squares. Completing the square in the scalar m yields

    2E=tr((A-m*I)^2)
       >=tr((K-m*I_(d-2))^2)
       >=tr(K^2)-(tr K)^2/(d-2)
       >=2*T_d-4*r_d^2-4*r_d^2/(d-2).

This proves (1) for d>=4. Since r_d^2=4*M_d and M_d/T_d->0,
there is an onset depending only on the base beyond which E>=T_d/2.
In particular, uniformly in the sites,

    rho:=r_d/sqrt(E)<=sqrt(8*M_d/T_d).                   (7)

There is no restriction on the magnitudes or separation of a,b in
this estimate. Invertibility or conditioning of the evaluation matrix
does not enter any constant.

### Centering and the two-variable envelope

Let O be the set of exceptional zero indices and ell=|O|<=2. Put
z_i=(lambda_i-m)/sqrt(E), so sum_i z_i=0 and sum_i z_i^2=2.
Using d*m=sum_i lambda_i and writing lambda_i=m+sqrt(E)*z_i on O,

    (d-ell)*m=sum_(i notin O) lambda_i+sqrt(E)*sum_(i in O) z_i.

For the other zeros |lambda_i|<=r_d, and Cauchy--Schwarz gives
|sum_(i in O)z_i|<=sqrt(2*ell)<=2. Consequently

    |m|/sqrt(E)<=rho+2/(d-2),
    |z_i|<=2*rho+2/(d-2)<=epsilon_d, i notin O.           (8)

Choose u_1,u_2 to be the z_i on O, padded by zeros. Their squared
sum is at most 2. Every omitted term satisfies (8), and hence

    |sum_(i notin O) z_i^3|<=2*epsilon_d,
    0<=sum_(i notin O) z_i^4<=2*epsilon_d^2.

Newton's identities for the centered characteristic polynomial give
G=-sum_i z_i^3/3 and L=1/2-sum_i z_i^4/4, with the signs and factors
as stated in C028w. These prove (2). The disk u_1^2+u_2^2<=2 is
compact and its displayed map is continuous, so K_2 is compact.
The finite errors tend to zero by C028x. This proves (3) as a uniform
necessary shape description; no converse or site limit has been used.

### Consequence for the retained cost

C028w's exact positive-cost identity has weights Lambda_2>=1,
Lambda_3>=4,Lambda_4>=27. Its scale x=s*sqrt(E)/d satisfies
R_2=x^2-binom(d,2)*v/d^2. If B_d/d^2->0, then R_2/x->0 and
x->sqrt(v/2)>0. The other two weighted squares give R_3,R_4->0.
The lower-degree centering factors satisfy |U|<=2, |V|<=2 and
|W|<=sqrt(6), so the mixed terms R_2*x*U,R_2*x^2*V,R_3*x*W vanish.
The exact cubic and quartic residual equations therefore give
(G,L)->(G_*,L_*). These are the uses of C028w's finite reduction;
no unproved shape separation from that result is assumed.

Along any such sequence, take a subsequence of the bounded pairs
(u_1,u_2) converging in the closed disk. Equations (2) give

    u_1^3+u_2^3=-3*G_*,
    u_1^4+u_2^4=2-4*L_*.

Set x_i=-sqrt(v/2)*u_i for this limiting pair. Substituting the exact
values of G_*,L_* gives (4), including

    (v^2/4)*(2-4*L_*)=v^2/2-omega/6=kappa.

If (4) were impossible, the actual shape pair would lie outside the
compact K_2 at positive distance. Uniform (2) and C028w's necessary
limit would contradict any sequence with d->infinity and B_d/d^2->0.
The negation of an eventual uniform positive floor supplies just such
a sequence, by choosing d_n>=n and cost ratio<1/n. Thus the claimed
conditional floor follows without restricting escaping parameters.

### The actual target satisfies the necessary condition

C028c's local logarithm convention is

    log F(z)=b_1*z-v*z^2/2+tau*z^3/3-kappa*z^4/4+O(z^5).

The coefficient of z^4 in F(z)*exp(-b_1*z) is both omega/24 and
v^2/8-kappa/4. Thus its S_4 equals the kappa defined here. This
finite coefficient comparison avoids any assumed positive zero law.

Reuse precisely C028c's audited enclosures (8):

    3.7172599285269686e-5 < v < 3.7172599285269687e-5,
    1.4417393140097327e-7 < tau < 1.4417393140097329e-7,
    6.6303168025299086e-10 < kappa < 6.6303168025299088e-10.

The canonical analytic transfer there includes the full complex-disk
remainder E_G<3.141e-48 on radius1600, Cauchy coefficient errors
E_G/1600^j before division, and the normalization f_j=4^j*A_j/A_0.
Audit1506 independently checks the finite rational interval propagation.
The complete relevant saved endpoints were inspected at
`scripts/jacobi-reference/penultimate-cost-1504.json`, pointers
`/reciprocal_sums/2`, `/reciprocal_sums/3`, `/reciprocal_sums/4`, and
the corresponding complete `/actual_and_required_bounds/S_2`,
`/actual_and_required_bounds/S_3`, `/actual_and_required_bounds/S_4`
values in `scripts/jacobi-reference/audit-penultimate-1506.json`.
This reuses the audited input under its full arithmetic contracts;
it is not a new transcendental evaluation or a replay of that audit.

Let sigma=1/200, V_0=v/sigma^2, T_0=tau/sigma^3 and Q_0=kappa/sigma^4.
The imported bounds imply the deliberately weaker rational inequalities

    V_0>37/25, 23/20<T_0<29/25, 53/50<Q_0<107/100.

All three needed strict comparisons have exact terminating-decimal
margins, equivalently rational margins:

    (37/25)^2-2*(107/100)=0.0504>0,
    (23/20)^4-(107/100)^3=0.52396325>0,
    2*(53/50)^3-(29/25)^4=0.57139264>0.

They prove respectively v^2>2*kappa, tau^4>kappa^3 and
tau^4<2*kappa^3, since the comparisons scale by sigma^4 or sigma^12.
Positivity is inherited, proving (5) without a new numerical script.

For completeness define the continuous function

    f(r)=(1+r^3)^4/(1+r^4)^3, 0<=r<=1.

It has f(0)=1 and f(1)=2. By (5), the intermediate value theorem
gives some r in (0,1) with f(r)=tau^4/kappa^3. Set

    x_1=(kappa/(1+r^4))^(1/4), x_2=r*x_1.

Then x_1>x_2>0, their fourth powers sum to kappa, and their positive
cubic sum has fourth power tau^4, so the cubic sum equals tau.
Finally

    (x_1^2+x_2^2)^2<=2*(x_1^4+x_2^4)=2*kappa<v^2.

This proves the strict variance slack. It proves actual membership in
the necessary envelope, not existence of sites a,b producing these
values. In particular it supplies no values of the modified norms or
of the weighted residuals. A separate moving-site realization result
would be needed before any countersequence conclusion. The negative
decision is restricted to separation by this envelope; the two-site
family and the requested retained-floor question remain undecided.

## Mathlib

Full matching coverage is not checked. DLMF's recurrence and Jacobi
theorems, the imported Uvarov formula, and the finite spectral theorem
are supporting mathematical inputs, not a formal proof of the complete
uniform envelope or actual-target specialization. No absence from
Mathlib or certified novelty is inferred. C028c's numerical qualifications
remain explicit. No formal audit is claimed; conceptual audit1942
accepts only the portions used by C028z, as qualified above.
