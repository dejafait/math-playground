# Lemma 918: tail compatibility of the fixed row-resolved density dual

## Hypotheses

Use the exact K, F and normalized density of L019/L058/L874,

    rho_lambda(u)=exp(lambda*u^2)K(u)/F(lambda,0),  u>=0,
    g_lambda(z)=F(lambda,z)/F(lambda,0),
    log g_lambda(z)=-sum_(n>=1) S_n(lambda)z^(2n)/n,
    H2=(S_(i+j+2))_(0<=i,j<=2).

Fix an actual contact with 0<lambda<=1/20, H2 positive semidefinite,
real c=(c0,c1,c2), sum c_i^2=1, c2!=0 and all three rows H2*c=0.
No contact is asserted to exist. Coordinates c0,c1 may vanish.
Let a_n=[z^(2n)]1/g_lambda(z), with a_0=1, and use L874's

    T_n(u)=sum_(k=0)^n a_(n-k)(-1)^k u^(2k)/(2k)!,
    R(u)=-sum_(i,j=0)^2 (i+j+2)c_i c_j T_(i+j+2)(u),
    V_i(u)=sum_(j=0)^2 c_j T_(i+j+2)(u),  i=0,1,2,
    Phi=c^T H2'(lambda)c=E[u^2 R(u)].

Choose seven real symmetric matrices A_0,...,A_6 and real matrices
B,C of size three, with all 60 independent entries in [-16,16].
The entries are constants independent of lambda, c, moments and u.
Use the ordinary quadratic form convention, and put

    p_k=c^T A_k c,   P(u)=sum_(k=0)^6 p_k u^(2k+1),
    s_lambda(u)=2lambda*u+K'(u)/K(u),
    W(u)=u^2 R(u)+P'(u)+s_lambda(u)P(u)
         +sum_(i,j=0)^2 c_i(B_ij V_j(u)+C_ij u V_j'(u)).

All coefficients below are evaluated at this fixed actual contact.
Their dependence on its unknown parameter and null vector is retained.

## Conclusion

The three separate row corrections and the density correction have
zero mean, with absolute integrability, so

    E[V_i]=E[u V_i']=0  (i=0,1,2),
    E[P'+s_lambda P]=0,              E[W]=Phi.            (1)

The complete theta score, with no omitted summands, satisfies

    s_lambda(u)<-4 exp(2u),  u>=1.                       (2)

Set alpha=6c2^2/12!>0 and write the even polynomial

    Q(u)=u^2 R(u)+P'(u)
             +sum_(i,j) c_i(B_ij V_j(u)+C_ij u V_j'(u))
        =-alpha*u^14+sum_(k=0)^6 q_k u^(2k),
    M_Q=sum_(k=0)^6 |q_k|,
    U_Q=max(1,sqrt(2M_Q/alpha)).

At this contact the following is an exact tail dichotomy.

* If P is zero, then W(u)<=-alpha*u^14/2 for u>=U_Q.
* Otherwise let m=max{k:p_k!=0} and M_P=sum_(k<m)|p_k|.
  If p_m>0, the same bound holds for

      u>=U=max(U_Q,sqrt(2M_P/p_m)).                      (3)

  If p_m<0, W is strictly positive for all sufficiently large u,
  and therefore cannot be a nonpositive half-line residual at this
  contact. This is a conditional restriction on the evaluated P;
  it is not an obstruction to all coefficient tuples.

In particular any complete certificate W<=0 on the half-line would
give the strictly negative, rather than merely nonpositive, flux

    Phi<=-(alpha/2) integral_U^infinity u^14 rho_lambda(u)du<0. (4)

For P=0 take U=U_Q. The cutoff U depends on the actual coefficients;
no common cutoff over all contacts or lower bound for |c2| is claimed.
No complete W<=0 certificate, actual contact, or flux sign has been
established by (1)-(4). A zero-flux actual contact, if one exists,
would exclude this entire finite class at that contact; its existence
is not proved or assumed.

A concrete tuple passing the origin-value and tail compatibility
tests is A_6=diag(0,0,1), A_0=...=A_5=0, B=0, C=I. Its residual is

    W_*(u)=u^2 R(u)+c2^2(13u^12+s_lambda(u)u^13)
                                      +sum_i c_i u V_i'(u).

It has W_*(0)=0 and obeys (3). Its first nonzero-order candidate
coefficient at the origin is

    lim_(u->0+) W_*(u)/u^2 = -J(lambda,c),
    J(lambda,c)=sum_(i,j=0)^2 c_i c_j
               ((i+j+2)a_(i+j+2)+a_(i+j+1)).            (5)

Nonpositivity requires J>=0. This requirement has not been proved
from the actual contact premises. Even J>=0 would not alone certify
the remainder of the compact interval. The bounded attempt stops
at this first unpaid sign; it neither asserts J<0 nor rejects other
tuples in the fixed class. The all-degree positivity gap is unchanged.

## Proof

### Known density rule and every contact row

The density-method rule is imported from C. Ley and Y. Swan,
*Stein's density approach and information inequalities*, Electronic
Communications in Probability 18 (2013), paper 7, Definition 2.1 and
Theorem 2.2, pp. 2-3, including the forward integration-of-a-derivative
proof: https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/2578/2199.pdf.
For a positive differentiable density on an interval, its operator is
T_rho P=(P rho)'/rho; the test class requires differentiability of
P rho and vanishing endpoint limits. We use only its zero-mean
direction, with absolute integrability verified here. The prior
assessment is `drafts/literature/2026-11-09-d2-row-resolved-density-dual.md`;
there is no claim of a new density identity or imported sign theorem.

L019 gives K>0. L058 and L874 give smoothness, positivity of the
normalizing mass, integrability of every polynomial times
exp(lambda*u^2)K and exp(lambda*u^2)|K'|, and decay of every
polynomial times exp(lambda*u^2)K at infinity. Consequently P rho
vanishes at infinity; at zero it vanishes because P is odd and
rho is finite. Its derivative is absolutely integrable: multiplying
the score term by rho cancels K in K'/K and leaves the cited |K'|
bound. The imported density rule therefore applies without an
uncontrolled reciprocal-K estimate or an unpaid endpoint term.

Individually L874 proves E[T_n]=0 and E[u T_n']=-2S_n. Hence

    E[V_0]=E[V_1]=E[V_2]=0,
    E[u V_0']=-2(S2*c0+S3*c1+S4*c2)=0,
    E[u V_1']=-2(S3*c0+S4*c1+S5*c2)=0,
    E[u V_2']=-2(S4*c0+S5*c1+S6*c2)=0.

These are finite polynomial sums and use each null row separately.
There is no division by a coordinate or minor. Integrating W now
gives (1), with L874 fixing Phi's orientation. PSD is retained as a
contact hypothesis; the zero means do not infer a sign from PSD.

### Full-series score and tail sign

L874 justifies differentiation of the entire theta series and gives,
with v_n=pi*n^2 exp(2u) and K_n=4v_n(2v_n-3)exp(u/2-v_n),

    K'/K=sum_(n>=1) (K_n/K)
                    (9/2+6/(2v_n-3)-2v_n).

Every weight is positive and their sum is one. Since pi>3,
v_n>3exp(2u) and 2v_n-3>3 on u>=0. Each summand score is less than
13/2-6exp(2u), and the same bound holds for the weighted sum. Thus

    s_lambda(u)<u/10+13/2-6exp(2u).

For u>=1 the positive exponential series gives
exp(2u)>=1+2u+2u^2>=5u; the last inequality is
(2u-1)(u-1)>=0. Consequently 2exp(2u)>=10u>=13/2+u/10.
This proves (2) for every allowed lambda and every theta summand,
without replacing K by its first term.

L874 gives R's leading coefficient -6c2^2/12!. Each V_i and uV_i'
has degree at most twelve, as does P'. This proves the displayed
form of Q and alpha>0. For u>=1 its lower terms have absolute sum
at most M_Q*u^12. For u>=U_Q this is at most alpha*u^14/2,
so Q<=-alpha*u^14/2.

For nonzero P, its lower terms have absolute sum at most
M_P*u^(2m-1) on u>=1 when m>=1. For m=0 the lower sum is zero.
If p_m>0 and u>=max(1,sqrt(2M_P/p_m)), it follows that
P(u)>=p_m*u^(2m+1)/2>0. Combining this with (2) and W=Q+s_lambda P
proves (3); the case P=0 follows directly from Q.

If p_m<0, the corresponding cutoff instead gives
P(u)<=-|p_m|u^(2m+1)/2. Set C_Q=alpha+M_Q and r=14-2m,
a positive integer. On u>=1, |Q(u)|<=C_Q*u^14, while (2) and
exp(2u)>=(2u)^r/r! give

    W(u)>=-C_Q*u^14+2|p_m|exp(2u)u^(2m+1)
          >=u^14(-C_Q+2^(r+1)|p_m|u/r!).

This is strictly positive when u exceeds both the cutoff for P's
negative sign and C_Q*r!/(2^(r+1)|p_m|). Thus the claimed failure
is on the entire far tail of this very contact, not a sampled
noncontact or an arbitrary substitute moment law.

If W<=0 everywhere, the negative-leading case is excluded and
(3), or its P=0 version, applies. Integrating its strict tail with
the positive full-support density, and using nonpositivity on the
remaining compact interval, proves (4). The integral is finite and
strictly positive. No existence of such a W has been used in proving
the tail dichotomy itself.

### One admitted tuple and the first unpaid compact estimate

The specified A,B,C entries are all zero or one, with the required
symmetry and constant dependence. P=c2^2*u^13, so its leading
coefficient is strictly positive for every stipulated contact; all
three row derivative corrections remain in W_*. Smoothness and
K(0)>0 make s_lambda bounded near zero. L874's finite expansion gives

    T_n(u)=a_n-a_(n-1)u^2/2+O(u^4),  n>=2,
    u V_i'(u)=-u^2 sum_j c_j a_(i+j+1)+O(u^4).

The density correction contributes only O(u^12) near zero. Inserting
these expansions into W_* proves (5) and W_*(0)=0. If J<0 at an
actual contact, continuity of W_*/u^2 would make this particular
residual positive near zero. No such contact or sign of J has been
certified. The null equations involve S2,...,S6, whereas the written
origin coefficient uses the actual inverse coefficients a_n; no
positivity of that new quadratic expression is supplied by (1).
This identifies an unpaid estimate, not an impossibility theorem
for obtaining it. The bounded attempt makes no further coefficient
change, band enlargement or compact sign claim.

These exact finite expansions and inequalities require no numerical
certificate. The original step199 specialization was unaudited; the
separate audit below verifies only (1)-(4). The residual test remains
incomplete and classified REPRODUCTION, with no claimed progress beyond
the checked sources and no actual-contact sign result.

### Independent analytic audit of (1)-(4), 9 November 2026 (step219)

The audit passes for exactly the stated hypotheses and the analytic
claims (1)-(4). Its prior SPECIALIZE assessment is
`drafts/literature/2026-11-09-l918-analytic-tail-audit.md`. The density
rule is the cited Ley-Swan Definition 2.1/Theorem 2.2, using only its
forward direction. The checks below verify applicability and the written
elementary estimates; they do not reprove a general density theorem.
L019, L058 and L874 are the mathematical inputs. Their relevant complete
proofs, including L874's existing audit, were checked. No numerical
certificate, actual contact or additional sign premise is used.

**Density, endpoints and absolute integrability.** Each full theta
summand K_n is positive, since v_n>=pi>3/2. Thus K>0, and L058 gives
0<F(lambda,0)<infinity. The normalized rho is positive and integrates
to one on (0,infinity); the value at the endpoint has no effect on its
law. K and K' are continuous at zero, K(0)>0, and rho is differentiable
in the interior. Direct differentiation gives precisely

    K_n'=(60pi^2 n^4 exp(9u/2)-30pi n^2 exp(5u/2)
                 -16pi^3 n^6 exp(13u/2))exp(-pi n^2 exp(2u)).

L874's majorization bounds the sum of absolute derivatives, not just
the absolute value of their sum:

    sum_n |K_n'(u)| <= C exp(13u/2-pi exp(2u)),
    C=(60pi^2+30pi+16pi^3)
                          sum_n n^6 exp(-pi(n^2-1))<infinity.

Indeed n^2,n^4<=n^6, both smaller exponential prefactors are at most
exp(13u/2), and exp(-pi(n^2-1)exp(2u))<=exp(-pi(n^2-1)). The last
series converges by comparison with n^6 exp(-pi(n-1)). On each compact
u interval this gives a summable uniform bound, so differentiating the
full series is legitimate. L058's analogous bound for K has prefactor
exp(9u/2). For either prefactor and any fixed polynomial, multiplication
by exp(lambda u^2) remains integrable and tends to zero at infinity.
To check this last assertion without assuming it from linear-exponential
decay alone, use u^j<=j!exp(u) for every integer j>=0. Beyond a finite
cutoff, (pi/2)exp(2u) dominates lambda u^2+(13/2+1)u; the resulting
bound is a constant times exp(-(pi/2)exp(2u))<=exp(-pi u). A finite
sum handles every polynomial. All factors are bounded near zero.

P is odd, hence P(0)=0. Therefore P rho tends to zero at the left
endpoint and, by that bound, at infinity. Moreover

    |(P rho)'| <= exp(lambda u^2)/F(lambda,0)
                  ((|P'|+2lambda*u*|P|)K+|P| |K'|),

which is integrable. This verifies the density theorem's interior
differentiability and both endpoint conditions, and independently the
required absolute integrability. In particular no lower bound for K
on the entire half-line is being assumed: multiplying (K'/K)P by rho
cancels K pointwise before taking an absolute integral. The density
correction has mean zero. Every other term of W is a finite polynomial
under rho, so W and all row corrections are absolutely integrable too.

**Every row and the flux orientation.** Because g_lambda(0)=1 and g
is analytic near zero, all the finitely used a_n are well defined and
real. L874's coefficient identities are E[T_n]=0 and
E[u T_n']=-2S_n for n>=1. The indices used here range from 2 through 6.
Consequently E[V_i]=0 and

    E[u V_i']=-2 sum_(j=0)^2 c_j S_(i+j+2)
              =-2(H2*c)_i=0,                 i=0,1,2.

This checks each separate row, including when c0 or c1 vanishes.
B,C and c are constants in the u integration. Thus their contractions
have zero mean. L874's normalized time-response identity is
S_n'=-n E[u^2 T_n]; contracting it with the fixed c_i c_j gives
E[u^2R]=c^T H2'c=Phi, with exactly the displayed minus sign in R.
No derivative of an expectation containing a varying R is substituted
for this identity. This proves (1). PSD is retained but supplies no
additional sign or vanishing expectation in this argument.

**Full-series score and strictness.** Differentiating log K_n gives
9/2+6/(2v_n-3)-2v_n. The bound on sum_n |K_n'| proves absolute
convergence of its weighted average, since K(u)>0 at every fixed u.
The positive weights K_n/K sum to one, so the displayed formula for
K'/K uses the entire series. Put E=exp(2u). Since v_n>3E and
2v_n-3>3 for u>=0, every summand score is strictly less than
13/2-6E. Strictness survives the infinite sum: the nonnegative gaps
have a strictly positive n=1 contribution with positive weight. Their
sum is finite by the absolute convergence just verified. With
2lambda*u<=u/10, this gives s_lambda<u/10+13/2-6E.

For u>=1, E>=1+2u+2u^2>=5u because
1-3u+2u^2=(2u-1)(u-1)>=0. Also
10u-(13/2+u/10)=(99/10)u-13/2>=17/5>0.
Hence 2E>13/2+u/10 on this whole range, and s_lambda<-4E.
This proves (2), including u=1 and lambda=1/20. No truncation,
asymptotic replacement or interchange of a conditionally convergent
score series occurs.

**Degree, all leading-sign cases and cutoffs.** The degree-twelve
term of R comes only from i=j=2 and a_0=1; it is
-6c2^2*u^12/12!. P' and every V_j or uV_j' have degree at most twelve
and are even. Therefore Q has exactly degree fourteen and leading
coefficient -alpha, with alpha>0. For u>=1,

    |Q+alpha*u^14|<=M_Q*u^12,
    |Q|<=(alpha+M_Q)u^14=C_Q*u^14.

Thus Q<=-alpha*u^14/2 whenever u>=U_Q. This includes M_Q=0 and
needs no lower bound for alpha uniform in c. If P=0, W=Q and the
first case follows without defining a leading index m.

If P is nonzero, 0<=m<=6. When m>=1 its lower sum is bounded in
absolute value by M_P*u^(2m-1) on u>=1. For m=0 that sum is empty,
M_P=0 and P=p_0 u exactly. In either case, beyond
max(1,sqrt(2M_P/|p_m|)), P has its leading sign and magnitude at least
|p_m|u^(2m+1)/2. For p_m>0, (2) makes s_lambda P negative, and the
Q bound proves (3), including the cutoff endpoints.

For p_m<0, multiplication of (2) by P reverses its inequality. It
gives s_lambda P>=2|p_m|exp(2u)u^(2m+1) after that cutoff. The
integer r=14-2m is in {2,4,6,8,10,12,14}, so the positive exponential
series implies exp(2u)>=(2u)^r/r!. Consequently

    W>=u^14(-C_Q+2^(r+1)|p_m|u/r!).

The bracket is strictly positive for
u>C_Q*r!/(2^(r+1)|p_m|). Taking u beyond this threshold and the
sign cutoff proves positivity on the entire far tail. This includes
m=0 and allows all lower coefficients to vanish. The divisions here
are only by alpha or |p_m| at a contact where they are nonzero; there
is no division by c0, c1 or a Hankel minor. All cutoffs are finite
at that fixed contact. They are not uniform as c2 or p_m tends to zero.

**Conditional strictly negative flux.** If W<=0 on the full half-line,
the negative-leading case is impossible. For P=0 or positive-leading
P, the relevant finite U gives W<=-alpha*u^14/2 on [U,infinity).
Absolute integrability allows splitting its expectation at U; the
compact part is nonpositive. The tail integral in (4) is finite by
the polynomial domination above and strictly positive because rho
is positive and continuous on, for example, [U+1,U+2]. Equation (1)
then gives exactly (4). This is an implication from a complete residual
certificate, not construction of such a certificate. In particular
Phi=0 at an actual contact would rule out this class at that contact,
but this audit proves neither such a contact nor its flux.

No mathematical error was found in (1)-(4). The local gain is a checked
analytic interface, classified REPRODUCTION, not a new density theorem
or a signed theta estimate beyond the sources checked. The origin
calculation (5) is outside this audit; L921's finite origin interface
does not fill the compact-sign gap. Contact existence, J's actual
contact sign, the remaining compact residual, initialization/equality,
other degrees and global continuation all remain unresolved. The
degree/box/band and all prior stops are unchanged. No new mathematical
dependency is added to the existing DAG row.

## Mathlib

Full matching coverage and supporting formal coverage of the theta
score, this density-operator specialization and the tail dichotomy
have not been checked. Availability is unknown, not asserted absent.
No formal contact-sign theorem is imported. General reference:
https://leanprover-community.github.io/mathlib4_docs/.
