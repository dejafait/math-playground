# C998i: Finite cosine block by regularized boundary data

## Hypotheses

Fix ell=log(3)/2, a=ell/2, k_n=n*pi/ell and lambda_n=k_n^2.
Throughout this result 0<=n,m<=255 and n,m have the same parity.
Use the finite-cell kernel of C998g Section1/audit674,

    K_tau(s,u)=integral_tau^a dt/[(t+s)(t+u)], 0<tau<a,
    I_nm=integral_(0,a)^2 cos(k_n*s) cos(k_m*u) K_0(s,u) ds du. (1)

K_0 has its integral value for s,u>0; its values on null axes are
irrelevant. The scalar product convention is linear in the first
slot. Use C998a(4)/audit655's unitary parity map and normalized modes
e_n(x)=nu_n*cos(k_n*x), where nu_0=ell^(-1/2) and
nu_n=sqrt(2/ell) for n>0. C998g supplies the coefficient1/4 of the
Carleman square in the residual Gram expansion. This result addresses
only that square, with the finite upper endpoint a retained.

The shared weights, endpoint assignments and their integral
representations from C998h Sections1-2/audit678 are used unchanged.
They do not require a witness or a neutral-completion assumption.
Later use with the frozen trials must retain all their coefficients
and C999q's exact completion; no trial is assembled here.

Source gate: the invocation-start EXPLORE assessment
`drafts/literature/2026-11-13-finite-block-boundary-closure-review-678.md`,
separately approved in source-notes679, covers this finite-block
extension. General tools are imported from Folland, *Real Analysis*,
second edition, Wiley1999: Theorem2.24, pp54-55 (dominated convergence),
Theorem2.27, p56 (parameter integration/differentiation, including the
local-interval qualification), and Theorems2.37/2.39, pp67-68
(Fubini/Tonelli, with finite product measures on p65).
The inspected primary texts are the
[book text](https://djvu.online/file/NPF4BEtSuqdFA) and
[product-measure extract](https://people.math.sc.edu/girardi/m7034/1617/hw/FollandRA2edProdMsr.pdf).
Their hypotheses are checked below; their general proofs are not
repeated. The source comparison did not identify a matching closure
theorem. Half-line commutation and structured-matrix reconstruction
theorems are not imported: their boundary/coincident-entry hypotheses
do not supply the present data.

## Conclusion

Every same-parity entry in(1) has formula(6), (7) or(8) below. All
data in those formulas are explicit convergent moments of ONE density
against fixed one-variable weights, or finite products of separately
defined endpoint moments. Both endpoint brackets survive. Every
positive frequency diagonal uses its own independently defined
parameter-derivative data; none is recovered by dividing by a zero
frequency difference. Mode zero is treated without a spectral derivative.

With the prescribed unitary map and square coefficient, the entry
between normalized full-cell modes n,m of the same parity is

    B_nm=(nu_n*nu_m/2)*I_nm.                              (2)

This supplies finite-block analytic coverage, extending the six cases
of C998h. It does not evaluate the moments or entries, establish stable
arithmetic, certify error<=1e-10 or work<=20000000, or claim low rank.
No A-square, mixed term, projection, residual/inverse debt, signed S3
or Xi positivity is paid. This is an established-method extension
(REPRODUCTION), not a claim of originality or progress beyond all
sources. Independent conceptual audit682 in Section7 upholds this
finite-block analytic conclusion without a changed formula or hypothesis.

## Proof

### 1. Shared weights and all required independent data

For clarity the definitions imported from C998h are reproduced here.
All logarithms and arguments are real. Put

    D(x)=integral_0^x log(1+y)/y dy, x>=0, D(0)=0,
    L(s)=log((a+s)/s), z=s/a, 0<s<a,
    A1(s)=[L(s)-log(2)]/(a-s),
    A2(s)=[A1(s)-1/(2a)]/(a-s),
    Q(s)=log(1-z)*log((1+z)/z)
          +D((1+z)/(1-z))-D(z/(1-z))+D(1/z),
    J=2a*((log2)^2+D(1)).                               (3)

At a use A1(a)=1/(2a), A2(a)=3/(8a^2) and
Q(a)=(log2)^2/2+D(1). C998h proves these are the actual endpoint
limits and that

    Aj(s)=integral_0^a dt/[(t+a)^j*(t+s)], j=1,2,
    Q(s)=integral_0^a L(t)/(t+s) dt,
    integral_0^a L(t)^2 dt=J.

For r=log(a/s)>=0 its audit also proves
0<Aj(s)<=a^(-j)L(s) and
0<Q(s)<=1+log2+(1+log2)r+r^2/2. Thus the weights are integrable
and at most logarithmic or logarithm-squared at zero. Their explicit
definitions(3), rather than an unevaluated output of a second
Carleman operator, specify the weights used in the answer.

For each n=0,...,255 define q_n(s)=cos(k_n*s)-1 and

    H_n=integral_0^a q_n(s)*Q(s) ds,
    P_n=integral_0^a q_n(s)*A1(s) ds,
    T_n=integral_0^a q_n(s)*A2(s) ds,
    R_n(0)=integral_0^a q_n(s)/s ds,
    R_n'(0)=-integral_0^a q_n(s)/s^2 ds,
    R_n(a)=integral_0^a q_n(s)/(a+s) ds,
    R_n'(a)=-integral_0^a q_n(s)/(a+s)^2 ds.             (4)

The primes in the last four definitions specify endpoint data, whose
agreement with derivatives is proved below. For EACH n=1,...,255,
independently define chi_n(s)=-s*sin(k_n*s)/(2k_n) and define
dot H_n, dot P_n, dot T_n, dot R_n(x), dot R_n'(x), x=0,a,
by replacing q_n with chi_n in every integral in(4), including the
minus signs in the primed data. No dotted datum is defined or used
at n=0. These definitions contain no matrix entry or integrated
product of outputs.

The inequalities |q_n(s)|<=lambda_n*s^2/2 and
|chi_n(s)|<=s^2/2, together with the weight bounds after(3), prove
absolute convergence of all these moments. At the singular endpoint
the quotient densities are bounded respectively by lambda_n*s/2,
lambda_n/2, s/2 and1/2. Mode zero has H_0=P_0=T_0=0 and all
undotted endpoint data zero, directly from q_0=0.

Let Delta denote the value at a minus the value at0. Define

    W_nm(x)=R_n'(x)*R_m(x)-R_n(x)*R_m'(x),
    V_n(x)=R_n'(x)*dot R_n(x)-R_n(x)*dot R_n'(x), n>0,
    c_n=1-cos(n*pi/2), b_n=k_n*sin(n*pi/2),
    dot c_n=a*sin(n*pi/2)/(2k_n), n>0,
    dot b_n=sin(n*pi/2)/(2k_n)+(a/2)*cos(n*pi/2), n>0.   (5)

The W and V data are finite products of the endpoint moments in(4).
In particular V_n is independently specified for every positive
diagonal, including n divisible by4.

### 2. Formulas covering the block

For m even, 0<=m<=254, the zero-mode entries are

    I_00=J,
    I_0m=I_m0=J+H_m.                                  (6)

For 1<=n<m<=255 with equal parity put delta_nm=lambda_m-lambda_n>0.
Then

    I_nm=I_mn=J+[Delta W_nm+lambda_m*H_m-lambda_n*H_n
                     +c_m*T_n+b_m*P_n-c_n*T_m-b_n*P_m]
                    /delta_nm.                        (7)

For every 1<=n<=255 the independent diagonal formula is

    I_nn=J+Delta V_n+H_n+lambda_n*dot H_n
                  +dot c_n*T_n+dot b_n*P_n
                  -c_n*dot T_n-b_n*dot P_n.             (8)

The following exact table makes all endpoint coefficient cases
explicit. The table applies only to positive n; mode zero uses(6).

| n mod4 | c_n | b_n | dot c_n | dot b_n |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | a/2 |
| 1 | 1 | k_n | a/(2k_n) | 1/(2k_n) |
| 2 | 2 | 0 | 0 | -a/2 |
| 3 | 1 | -k_n | -a/(2k_n) | -1/(2k_n) |

Thus the last four terms of(8), in the same residue order, are

    (a/2)*P_n;
    (a/(2k_n))*T_n+P_n/(2k_n)-dot T_n-k_n*dot P_n;
    -(a/2)*P_n-2*dot T_n;
    -(a/(2k_n))*T_n-P_n/(2k_n)-dot T_n+k_n*dot P_n.

For distinct positive even indices the correction in(7) is
c_m*T_n-c_n*T_m. For distinct odd indices, with
sigma_j=(-1)^((j-1)/2), it is
T_n-T_m+sigma_m*k_m*P_n-sigma_n*k_n*P_m.
These cover all equal-parity residue combinations; no odd-mode
upper-end sine contribution has been discarded. In particular a
positive mode divisible by4 has d_n=0 below but dot b_n=a/2,
so its diagonal still requires the displayed P_n term.

### 3. Original cutoff and regularized endpoint traces

For tau>0 the kernel and all needed spatial derivatives are bounded
on the closed square, since the integration variable is at least tau.
All finite products are Lebesgue products and hence sigma-finite.
Their integrands are measurable. Fubini at positive cutoff gives

    I_nm(tau)=integral_tau^a F_n(t)*F_m(t) dt,
    F_n(t)=integral_0^a cos(k_n*s)/(t+s) ds.

For the singular limit, the absolute triple integrand is at most
1/[(t+s)(t+u)]. Tonelli gives its integral as integral_0^a L(t)^2 dt=J,
finite by(3). Hence signed Fubini also applies at cutoff zero. Since
|F_n(t)|<=L(t), the same cutoff estimate as C998h holds for each pair:

    |I_nm-I_nm(tau)|
      <=integral_0^tau L(t)^2 dt
      <=tau*((log(2a/tau))^2+2log(2a/tau)+2) ->0.         (9)

This is the original t-cutoff of K_tau; it is not an alternative
regularization of the endpoint ODE. If s,u cutoffs are introduced
first, boundedness at fixed tau removes them, and the same absolute
triple majorant justifies their removal at zero cutoff.

For t>0 set R_n(t)=F_n(t)-L(t)=integral_0^a q_n(s)/(t+s) ds.
For a positive parameter lambda near lambda_n, n>0, similarly put
q_lambda(s)=cos(s*sqrt(lambda))-1 and R_lambda(t) its integral.
Take the positive compact interval [lambda_n/2,3lambda_n/2], and
write M=3lambda_n/2. Its density and derivative satisfy

    |q_lambda(s)|<=M*s^2/2,
    |partial_lambda q_lambda(s)|<=s^2/2.

Dominated differentiation for t>=tau>0 follows, for every derivative
order j needed here (j<=2), from the bounds j!*(M*s^2/2)/(t+s)^(j+1)
and j!*(s^2/2)/(t+s)^(j+1). They have integrable majorants with
t>=tau. Folland2.27 and2.24 therefore justify the needed t and
lambda differentiations and continuity. At t>0 the resulting bounds
are

    |R_lambda(t)|<=M*a^2/4,   |R_lambda'(t)|<=M*a/2,
    |R_lambda''(t)|<=M*L(t),
    |dot R_lambda(t)|<=a^2/4, |dot R_lambda'(t)|<=a/2,
    |dot R_lambda''(t)|<=L(t).                           (10)

Here dot denotes partial_lambda; the last bound uses
s^2/(t+s)^3<=1/(t+s). The endpoint integrands for R,R' are dominated
by M*s/2,M/2, and their lambda derivatives by s/2,1/2. Consequently
R,R',dot R,dot R' extend continuously to zero with exactly the
definitions(4). For example R'(t)=-integral q_lambda(s)/(t+s)^2 ds;
the continuous limit is also the right derivative of the continuous
extension, by integrating this bounded derivative from a positive
cutoff and letting the cutoff decrease to zero. The same argument
applies to dot R. At a the endpoint denominators are bounded away
from zero. No value of R'' or dot R'' at zero is asserted.

Applying Folland2.27 directly to(4) also shows that the dotted
endpoint data are its lambda derivatives. For H,P,T the respective
parameter-derivative majorants are s^2Q/2,s^2A1/2,s^2A2/2, integrable
by(3). Thus all dotted quantities are independently defined moments
and are the asserted derivatives locally at EACH positive lambda_n.
Nothing in this argument differentiates through lambda=0.

### 4. Endpoint ODEs and the distinct-frequency identity

On [tau,a] two integrations by parts in s give

    F_n''+lambda_n*F_n
      =1/t^2-cos(k_n*a)/(t+a)^2+k_n*sin(k_n*a)/(t+a).

The full bracket is
[cos(k_n*s)*(-1/(t+s)^2)+k_n*sin(k_n*s)/(t+s)]_0^a;
in particular the lower endpoint contributes +1/t^2. Subtract the
n=0 equation before taking a cutoff limit. The result is

    R_n''+lambda_n*R_n=d_n-lambda_n*L,
    d_n(t)=c_n/(t+a)^2+b_n/(t+a).                       (11)

The same equation holds for the positive parameter lambda, with
c(lambda)=1-cos(a*sqrt(lambda)) and
b(lambda)=sqrt(lambda)*sin(a*sqrt(lambda)). Their derivatives give
exactly(5). Smoothness and(10) justify this equation at every required
mode and its later parameter differentiation.

For distinct positive n,m, differentiating the Wronskian on [tau,a]
and substituting(11) gives

    W_nm'=(lambda_m-lambda_n)*R_n*R_m+d_n*R_m-d_m*R_n
                         -lambda_n*L*R_m+lambda_m*L*R_n. (12)

All terms are integrable down to zero: R and R' are bounded, d is
bounded, and L is integrable. Both endpoint traces of W exist by(10).
Therefore integration on [tau,a] followed by its justified limit
retains precisely Delta W_nm, including its zero-end contribution.

The following eliminations use only the shared weights(3):

    integral_0^a L(t)*R_n(t) dt=H_n,
    integral_0^a R_n(t)/(t+a) dt=P_n,
    integral_0^a R_n(t)/(t+a)^2 dt=T_n.                 (13)

For the absolute Fubini check, integral_0^a |q_n(s)|/(t+s) ds
<=lambda_n*a^2/4. Multiplying by L(t), (t+a)^(-1) or (t+a)^(-2)
and integrating gives a finite bound. Replacing q_n by chi_n changes
lambda_n*a^2/4 to a^2/4, so(13) also holds for all dotted quantities.
This proves that no integral of an unknown output remains in the
final data.

Writing S_nm=integral_0^a R_n(t)*R_m(t) dt only within the derivation,
the integrated identity(12) is

    delta_nm*S_nm=Delta W_nm-c_n*T_m-b_n*P_m+c_m*T_n+b_m*P_n
                                     +lambda_n*H_m-lambda_m*H_n.

The original integral is I_nm=J+H_n+H_m+S_nm, by(9), (13) and
F_n=L+R_n. Substitution and collection of the H terms proves(7).
Since k_j=j*pi/ell and n<m, the denominator is strictly positive.
Symmetry I_mn=I_nm follows from the absolutely integrable symmetric
kernel, so no ordered pair is lost by imposing n<m. No assertion is
made by assigning a value to this quotient on the frequency diagonal.

### 5. Independent positive diagonals and the zero cases

Differentiate(11) on the positive local parameter interval used in
Section3. The already proved domination permits this operation:

    dot R_n''+lambda_n*dot R_n=dot d_n-L-R_n,
    dot d_n=dot c_n/(t+a)^2+dot b_n/(t+a).              (14)

Multiplying(11) by dot R_n, multiplying(14) by R_n, and subtracting
gives the identity for independently defined data

    V_n'=d_n*dot R_n-R_n*dot d_n+L*R_n+R_n^2
                                                 -lambda_n*L*dot R_n.

It is first integrated on [tau,a]. Bounds(10), boundedness of d and
dot d, and integrability of L justify all terms separately at zero;
the complete bracket tends to V_n(a)-V_n(0). Using(13) and its dotted
versions yields

    integral_0^a R_n^2
      =Delta V_n-c_n*dot T_n-b_n*dot P_n
                   +dot c_n*T_n+dot b_n*P_n-H_n+lambda_n*dot H_n.

Adding J+2H_n proves(8) for each n=1,...,255. This uses the ODE of
an independently specified parameter derivative, not a differentiated
unknown matrix or a postulated diagonal limit. The table in Section2
is exact substitution of sin(n*pi/2),cos(n*pi/2) in(5); it verifies
all four positive-diagonal cases, including the new residue classes
0 and3 absent from C998h's tested diagonals.

Finally R_0=0 and F_0=L, so the same absolutely convergent integrals
give I_00=J and I_0m=J+H_m directly. Symmetry gives I_m0. Only even
m are needed with mode zero. These formulas never refer to chi_0,
dot c_0, dot b_0 or any lambda derivative at zero. Together with
(7),(8) they exhaust the stated same-parity block. Substituting the
six pairs from C998h recovers its formulas(7)-(12), with unchanged
endpoint orientation and signs.

### 6. Normalization, finite-block scope and limitations

C998a(4) sends e_n to sqrt(2)*(-1)^n*nu_n*cos(k_n*t)
in its parity component and to zero in the other. The K_0 pairing
of the nonzero components is thus
2*(-1)^(n+m)*nu_n*nu_m*I_nm. Equal parity makes (-1)^(n+m)=1.
C998g's square coefficient1/4 then proves(2), including the distinct
value of nu_0. Opposite parity components belong to separate blocks;
the raw half-cell integral of two opposite-parity cosines is not
asserted to vanish. For later complex coefficient combinations, the
second-slot coefficient is conjugated; the real basis entries here
need no alteration. No full trial contraction is performed.

The continuation test passes at the analytic level for the finite
block0..255: the same three weights and explicit logarithmic primitive
serve every entry, independent endpoint data cover every positive
diagonal, both cutoff endpoints are accounted for, and no integrated
product of unknown outputs remains in(6)-(8). The proof asserts no
unbounded-index theorem, stability result, moment evaluation or work
count. Cancellation in the explicit weights near a and cancellation
in the entry formulas still require numerical analysis if used.

The prescribed direct-method failures652/657/660/662/672 and source
stops673/675 are unaffected. A later residual certificate still needs
actual square entries, its1e-10/20000000 service, A-square, both mixed
terms, projection, and the full100000000 work bound. Reference-inverse
and source-to-Xi contracts, signed S3, higher/mixed signs, C744q/H2,
non-neutral and global assembly remain independent open requirements.

### 7. Independent conceptual audit — 13 November 2026, step682

Invocation-start EXPLORE assessment680, separately approved681, covers
exactly this audit. Source-notes681/679 and C998h/audit678 are reused;
Folland's general theorems cited above are not reproved. This audit
checks their particular hypotheses and the expanded finite-block cases.
Equations(1)-(14) and the residue table survive unchanged. The result
is local independent validation (REPRODUCTION), not a new theorem
beyond the sources checked, a numerical certificate or a sign result.

**Shared weights.** The full definitions and proof in C998h were
checked, including their endpoint limits. Independently differentiating
the positive-log primitive gives, for fixed 0<z<1,

    d/dx [log(1-z)log(x+z)+D((x+z)/(1-z))]
       =log(1+x)/(x+z).

Its difference at x=1 and x=0 gives the first three terms of Q.
For the remaining term, log(x)log(1+x/z) tends to zero at x=0
and vanishes at x=1; integration by parts yields
integral_0^1 log(x)/(x+z) dx=-D(1/z). Thus the plus sign before
D(1/z) is correct. Substitution t=ax introduces no scale factor
in dt/(t+s). The A1 partial fraction identity and subtraction of
integral_0^a(t+a)^(-2)dt=1/(2a) give exactly A1 and A2 in(3).
At s=a direct integration gives 1/(2a), 3/(8a^2), and
(log2)^2/2+D(1) respectively. For s in[a/2,a], majorants
2a^(-j-1) and 2L(t)/a justify the endpoint limits of Aj and Q
by Folland2.24; L is integrable.

At zero, Aj<=a^(-j)L. Splitting the Q integral at t=s bounds
the two pieces by log(2a/s)+1 and (log2)r+r^2/2, where
r=log(a/s); their sum is the stated bound after(3). It is integrable
as a function of s. Finally L'=-a/[t(t+a)] and tL(t)^2->0 give

    integral_0^a L^2=a*(log2)^2+2a*integral_0^a L/(t+a)
                    =a*(log2)^2+2a*Q(a)=J.

This verifies the imported identities actually used in the expanded
block, including their scales. The explicit weights involve only s
and the prescribed primitive D; no unknown pair integral is an input.

**Original cutoff and endpoint/parameter operations.** All product
spaces here are finite Lebesgue products and the integrands are Borel
off null axes. Tonelli applied to the positive triple majorant gives
integral_(0,a)^3[(t+s)(t+u)]^(-1)=J<infinity. Signed Fubini therefore
applies to each cosine product even at cutoff zero. The positive-cutoff
factorization is the same one whose omitted t integral is bounded by

    integral_0^tau log(2a/t)^2 dt
      =tau*((log(2a/tau))^2+2log(2a/tau)+2) ->0.

Thus(9) identifies the answer with the ORIGINAL K_tau limit. Introducing
s,u cutoffs does not change it: at positive tau boundedness suffices,
and at zero the same integrable triple majorant permits removal of
the axis cutoffs. No cancellation is used to establish this convergence.

For each positive n separately use [lambda_n/2,3lambda_n/2] and
M=3lambda_n/2. The inequalities |q_lambda|<=M*s^2/2 and
|partial_lambda q_lambda|<=s^2/2 hold throughout this positive interval.
At t>=tau>0, j! tau^(-j-1) times these densities is integrable for
j=0,1,2. Applying Folland2.27 to these derivatives, and2.24 for
their continuity, justifies both orders of the mixed operation
partial_lambda partial_t^2 at t>0. Pointwise smoothness in lambda
has no singularity on the chosen interval. In particular the
parameter differentiation of the ODE is licensed before taking
any zero-end limit.

The sharper t>0 bounds(10) follow from s^2/(t+s)<=s,
s^2/(t+s)^2<=1 and s^2/(t+s)^3<=1/(t+s), with the factor2
from the second derivative included. At t=0 the s-integrands for
R,R',dot R,dot R' are dominated respectively by M*s/2,M/2,s/2,1/2.
These verify continuity of all four traces and their exact signs in(4).
For completeness, R(t)-R(epsilon)=integral_epsilon^t R'(v)dv;
boundedness and continuity of the limiting R' allow epsilon->0.
Dividing the resulting identity by t and letting t->0 proves that
the assigned R'(0) is the actual right derivative. The identical
argument applies to dot R. No second derivative at zero is required.

Folland2.27 at the endpoint integrals uses the dotted majorants
s/2 and1/2 at zero, and bounded denominators at a. For H,P,T
it uses s^2Q/2,s^2A1/2,s^2A2/2, all integrable by the weight check.
Consequently every dotted moment and trace is both independently
specified and the claimed lambda derivative. These statements hold
at EACH positive mode through255; they neither differentiate at
lambda=0 nor assert uniformity over an unbounded set of modes.

**Boundary signs and the distinct-frequency formula.** On positive
cutoffs, partial_t^2(t+s)^(-1)=partial_s^2(t+s)^(-1).
Two integrations by parts against cos(k*s) give the complete bracket

    [ -cos(k*s)/(t+s)^2+k*sin(k*s)/(t+s) ]_0^a.

The lower endpoint contributes +1/t^2. Subtracting the k=0 equation
leaves c/(t+a)^2+b/(t+a)-lambda*L, verifying(11); no odd-mode sine
term at a may be omitted. Direct differentiation of W, with the
orientation in(5), gives

    W_nm'=R_n''R_m-R_n R_m''
      =delta_nm R_n R_m+d_n R_m-d_m R_n
         -lambda_n L R_m+lambda_m L R_n.

Every term is integrable at zero because R is bounded, d is bounded,
and L is integrable. The endpoint traces verified above retain
W_nm(a)-W_nm(0), not just the upper value. In the eliminations(13),
the absolute inner q integral is at most lambda_n*a^2/4 and its
dotted counterpart at most a^2/4. Integration against each of
L,(t+a)^(-1),(t+a)^(-2) is finite. Fubini is therefore justified
separately for all six eliminations; no conditionally convergent
product is being exchanged.

Solving the integrated W equation gives

    delta_nm*integral R_n R_m
      =Delta W_nm+c_m*T_n+b_m*P_n-c_n*T_m-b_n*P_m
         +lambda_n*H_m-lambda_m*H_n.

Adding delta_nm*(H_n+H_m) changes the H coefficients to
-lambda_n*H_n+lambda_m*H_m, exactly(7). The remaining constant is
J. This independently checks the potentially confusable H indices
and signs. For n<m the gap (m^2-n^2)*pi^2/ell^2 is strictly positive.
Symmetry follows from the absolutely integrable original kernel,
not an assumed symmetry of the derived data. Both endpoint brackets
in Delta W remain explicit inputs.

**Positive diagonals and exhaustion.** Differentiating(11) on its
positive parameter interval yields(14), including BOTH -L and -R_n.
For the independently defined V, direct differentiation gives

    V_n'=R_n''dot R_n-R_n dot R_n''
      =d_n dot R_n-R_n dot d_n+L R_n+R_n^2
         -lambda_n L dot R_n.

All terms again have bounds by a constant times1+L(t), and both
traces exist. Solving for integral R_n^2 gives the terms
Delta V_n-c_n dot T_n-b_n dot P_n+dot c_n T_n+dot b_n P_n
-H_n+lambda_n dot H_n. Adding J+2H_n proves precisely(8).
There is no limiting division by a zero gap or differentiation
of an unknown matrix entry.

The derivatives of c(lambda)=1-cos(a sqrt(lambda)) and
b(lambda)=sqrt(lambda)sin(a sqrt(lambda)) give(5) directly.
The full positive-index check is:

| modes | (sin(k_n a),cos(k_n a)) | diagonal endpoint correction |
| --- | --- | --- |
| 4,8,...,252 | (0,1) | (a/2)P_n |
| 1,5,...,253 | (1,0) | a*T_n/(2k_n)+P_n/(2k_n)-dot T_n-k_n*dot P_n |
| 2,6,...,254 | (0,-1) | -(a/2)P_n-2*dot T_n |
| 3,7,...,255 | (-1,0) | -a*T_n/(2k_n)-P_n/(2k_n)-dot T_n+k_n*dot P_n |

In the first row b_n=c_n=0 but dot b_n=a/2; deleting that term
would be invalid. These rows exhaust1..255 and confirm the table
and every diagonal correction in Section2. For distinct positive
even modes b=0, so only c_m*T_n-c_n*T_m remains. For distinct odd
modes c=1 and b=sigma*k, giving exactly the correction stated there,
including pairs from different odd residue classes.

For mode zero, q_0=0, R_0=0 and F_0=L directly. Hence I_00=J
and I_0m=J+H_m for every required even m, with symmetry giving
I_m0. At m=0 the latter agrees with I_00 since H_0=0. No dotted
zero datum is used. These zero cases, all positive diagonals and
all ordered n<m same-parity pairs exhaust the stated block.
Substitution of(0,0),(0,2),(2,2),(2,4),(1,1),(1,3) recovers
C998h's six formulas with the same signs and brackets.

**Normalization and verdict.** Substituting
e_n(ell-t)=(-1)^n*nu_n*cos(k_n*t) into C998a(4) puts
sqrt(2)*nu_n*cos(k_n*t) in the plus component for even n and
-sqrt(2)*nu_n*cos(k_n*t) in the minus component for odd n.
The other component is zero. This map is unitary: the sum of the
two squared component norms equals the full-cell squared norm by
the two-point parallelogram identity and reflection. Equal-parity
pairing thus contributes 2*nu_n*nu_m*I_nm. C998g Section1's square
coefficient1/4 yields exactly(2); nu_0 is its distinct prescribed
value. The raw opposite-parity half-cell integral need not vanish;
the two components are separate. Complex coefficient contraction
would conjugate the second-slot coefficient under the stated
convention, but the present basis entries are real.

The analytic test passes without repair for all stated indices.
The only non-endpoint data are the independently specified
single-density moments; W,V are finite products of endpoint data.
Neither the derivation nor its normalization requires the frozen
witness or neutral completion. Their exact coefficients and C999q
remain necessary for a later frozen-column contraction. No numerical
calculation or witness read was performed. Stable moment evaluation,
actual entries, the1e-10/20000000 square service, A-square, both
mixed terms, projection, full100000000 work, residual/inverse debt,
signed S3 and the higher/mixed/non-neutral/global Xi claims remain
open. Earlier prescription and source stops are unaffected.
The direct mathematical inputs remain C998a,C998g,C998h; no new
edge, stronger hypothesis or hidden positivity assumption was added.

## Mathlib

A full matching theorem for this finite-block closure, its independent
diagonal moments and normalization has not been checked. Dominated
convergence, Fubini/Tonelli and integral differentiation are supporting
standard results, not a formalization of this conclusion. Unknown
coverage is not evidence of absence. The precise Folland citations
above are the imported general calculus tools. The existing C998h
shared-weight proof is reused, while the expanded index and endpoint
cases are justified here rather than assumed from its six-case scope.
