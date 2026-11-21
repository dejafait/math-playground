# C998h: Six selected cosine-square entries by regularized boundary data

## Hypotheses

Put ell=log(3)/2, a=ell/2 and k_n=n*pi/ell, lambda_n=k_n^2.
Use the finite-cell kernel audited in C998g Section1:

    K_tau(s,u)=integral_tau^a dt/[(t+s)(t+u)], 0<tau<a.

At tau=0 use its almost-everywhere value for s,u>0. Define ONLY the
six entries with (n,m)=(0,0),(0,2),(2,2),(2,4),(1,1),(1,3) by

    I_nm=integral_(0,a)^2 cos(k_n*s) cos(k_m*u) K_0(s,u) ds du.

The normalization and parity map are those of C998a(4):
nu_0=ell^(-1/2), nu_n=sqrt(2/ell) for n>0. This result concerns the
square term in C998g, not either mixed term or the full residual Gram.
All frozen data, exact neutral completion, source-to-Xi and inverse
qualifications are unchanged. No witness array is used in this proof.

Source gate: invocation-start EXPLORE assessment
`drafts/literature/2026-11-12-finite-cosine-boundary-closure-test-review-675.md`.
It permits this six-pair calculus test, not general matrix assembly.
Its inspected Blower, arXiv:0712.1013v1, Theorem2.1/proof(2.3)-(2.5),
does NOT apply directly to this finite-cell cosine domain; no commutation
theorem is imported. The finite-boundary specialization is proved below.
Fubini/Tonelli use Folland, *Real Analysis*, second edition(1999),
Section2.5, Theorems2.37/2.39, pp67-68 (finite products p65), as already
checked in C998g Section1; [primary extract](https://people.math.sc.edu/girardi/m7034/1617/hw/FollandRA2edProdMsr.pdf).
Dominated convergence and local differentiation under an integral use
the same edition, Theorems2.24, pp54-55, and2.27, p56, including the
local-parameter-interval qualification; [primary book text](https://djvu.online/file/NPF4BEtSuqdFA).
These statements and proofs were inspected in source-notes677 before
independent audit678 under invocation-start EXPLORE assessment676.
They are imported standard tools, not six-entry closure theorems.

## Conclusion

All six entries reduce exactly to the formulas(7)-(12) below, using
shared one-variable weights and endpoint moments defined in(1)-(6).
Every moment is convergent. In particular, the formulas contain neither
a product of two unknown Carleman outputs nor an unknown Galerkin entry.
Finite upper-end and zero-axis terms are retained. The two nonzero
frequency-diagonal entries have independent differentiated identities;
no division by a vanishing frequency difference is used.

This is an analytic six-case closure, not an evaluated matrix, a
certified numerical oracle, a low-rank claim or an arbitrary-mode
closure theorem. It proves neither entry error<=1e-10 nor work<=20000000.
The earlier direct-contraction work stop is unaffected. Independent
conceptual audit678 below upholds exactly these six identities and
their normalization. No RH sign or inverse debt is paid.

## Proof

### 1. Shared weights and their definitions without Carleman outputs

All logarithms here are real. For x>=0 set

    D(x)=integral_0^x log(1+y)/y dy, D(0)=0.              (1)

The integrand extends continuously at zero with value1. This is a
specified one-variable logarithmic primitive; no dilogarithm branch
or external special-function identity is assumed. For 0<s<a, z=s/a,
define

    L(s)=log((a+s)/s),
    A1(s)=[L(s)-log(2)]/(a-s),
    A2(s)=[A1(s)-1/(2a)]/(a-s),
    Q(s)=log(1-z)*log((1+z)/z)
         +D((1+z)/(1-z))-D(z/(1-z))+D(1/z).             (2)

At s=a set A1(a)=1/(2a), A2(a)=3/(8a^2),
Q(a)=(log(2))^2/2+D(1). These endpoint assignments are also the limits.
The definitions are independent of n,m and all Carleman outputs. They
are mathematical identities, not stable finite-precision prescriptions.
In particular, cancellation near s=a has not been priced.

We will use, and now verify, the auxiliary representations

    Aj(s)=integral_0^a dt/[(t+a)^j*(t+s)], j=1,2,
    Q(s)=integral_0^a L(t)/(t+s) dt.                    (3)

Partial fractions give A1. The identity
1/[(t+a)^2(t+s)]=[1/((t+a)(t+s))-1/(t+a)^2]/(a-s)
gives A2. Direct integration at s=a gives the stated values.
For Q substitute x=t/a. The positive-log part has primitive
log(1-z)*log v+D(v/(1-z)), v=x+z, since its derivative is
log(1+x)/(x+z). For the other part, integration by parts gives

    integral_0^1 log(x)/(x+z) dx=-D(1/z).

Indeed log(x)*log(1+x/z) tends to zero at x=0, and its derivative is
log(1+x/z)/x+log(x)/(x+z). Evaluating both parts proves(2), including
the PLUS sign before D(1/z). At z=1 the positive-log part is
(log2)^2/2 and integration by parts gives the negative-log part D(1).
Dominated convergence in(3) for s near a proves continuity there.
Thus(3) verifies explicit shared weights; it does not leave a
two-variable correction in the final formulas.

As s decreases to zero, Aj(s)=O(1+|log(s/a)|), with constants depending
on a. Splitting Q's integral at t=s, using L(t)<=log(2a/t), gives
Q(s)=O(1+|log(s/a)|^2): on(0,s) bound 1/(t+s) by1/s, and on(s,a)
by1/t. In particular these weights are locally integrable at zero.

### 2. Only single-density moments and finite endpoint data

For n=0,1,2,3,4 put q_n(s)=cos(k_n*s)-1 and define

    H_n=integral_0^a q_n(s)*Q(s) ds,
    P_n=integral_0^a q_n(s)*A1(s) ds,
    T_n=integral_0^a q_n(s)*A2(s) ds.                   (4)

For n=1,2 only, define dot H_n,dot P_n,dot T_n by replacing q_n
in these definitions with chi_n(s)=-s*sin(k_n*s)/(2k_n).
The dot denotes differentiation with respect to lambda=k^2 at lambda_n,
not with respect to the discrete index. These are convergent one-variable
moments of the same shared weights. Since |q_n(s)|<=k_n^2*s^2/2 and
|chi_n(s)|<=s^2/2, their convergence follows from the bounds after(3).

Define endpoint data R_n(x),R_n'(x), for x=0,a only, by

    R_n(0)=integral_0^a q_n(s)/s ds,
    R_n'(0)=-integral_0^a q_n(s)/s^2 ds,
    R_n(a)=integral_0^a q_n(s)/(a+s) ds,
    R_n'(a)=-integral_0^a q_n(s)/(a+s)^2 ds.            (5)

Dot endpoint data for n=1,2 replace q_n with chi_n. All converge,
including the 1/s^2 weights. For a function defined on {0,a}, write
Delta B=B(a)-B(0), and set

    W_nm(x)=R_n'(x)*R_m(x)-R_n(x)*R_m'(x),
    V_n(x)=R_n'(x)*dot R_n(x)-R_n(x)*dot R_n'(x),
    J=2a*((log2)^2+D(1)).                              (6)

These are finite products of independently specified endpoint moments,
not products of outputs integrated over the cell. Mode0 has all R,H,P,T
equal to zero.

### 3. The six formulas

With precisely the definitions above the entries are

    I_00=J,                                            (7)
    I_02=J+H_2,                                        (8)
    I_22=J+Delta V_2+H_2+lambda_2*dot H_2
             -(a/2)*P_2-2*dot T_2,                    (9)
    I_24=J+[Delta W_24+lambda_4*H_4-lambda_2*H_2
             -2*T_4]/(lambda_4-lambda_2),              (10)
    I_11=J+Delta V_1+H_1+lambda_1*dot H_1
             +(a/(2k_1))*T_1+P_1/(2k_1)
             -dot T_1-k_1*dot P_1,                    (11)
    I_13=J+[Delta W_13+lambda_3*H_3-lambda_1*H_1
             +T_1-k_3*P_1-T_3-k_1*P_3]
             /(lambda_3-lambda_1).                    (12)

Only the two strictly positive denominators lambda_4-lambda_2 and
lambda_3-lambda_1 occur. The following proof supplies, in particular,
the independent frequency-diagonal identities(9),(11).

### 4. Positive cutoffs, differentiation and regularization

Fix tau>0 first. K_tau is smooth on the entire closed s,u square;
its derivatives of every fixed order are bounded there because t>=tau.
Fubini applies to the bounded triple integrand. If desired, spatial
cutoffs s,u>=delta can first be used; their removal at fixed tau is
justified by these same bounds. Thus

    I_nm(tau)=integral_tau^a F_n(t)*F_m(t) dt,
    F_n(t)=integral_0^a cos(k_n*s)/(t+s) ds, t>0.       (13)

On [tau,a], differentiation under the finite s integral is justified
by |partial_t^j (t+s)^(-1)|<=j!*tau^(-j-1). Twice integrating by parts
in s, with all endpoints retained, gives

    F_n''+lambda_n*F_n
       =1/t^2-cos(k_n*a)/(t+a)^2
                    +k_n*sin(k_n*a)/(t+a).             (14)

Specifically the endpoint bracket is
[cos(k_n*s)*(-1/(t+s)^2)+k_n*sin(k_n*s)/(t+s)]_0^a.
The s=0 contribution is +1/t^2; the s=a terms are both as displayed.
No cosine boundary condition is asserted for odd n at a.

Set R_n(t)=F_n(t)-L(t)=integral_0^a q_n(s)/(t+s) ds for t>0.
This notation agrees with the endpoint data in(5). Subtract(14) for
n=0 BEFORE removing tau. With
c_n=1-cos(k_n*a), b_n=k_n*sin(k_n*a), d_n(t)=c_n/(t+a)^2+b_n/(t+a),
the result is

    R_n''+lambda_n*R_n=d_n-lambda_n*L.                 (15)

Dominated convergence using |q_n|<=k_n^2*s^2/2 shows that R_n,R_n'
extend continuously to t=0 with exactly(5). Moreover
|R_n''(t)|<=k_n^2*integral_0^a s^2/(t+s)^3 ds
<=k_n^2*log(1+a/t). Thus R_n'' is integrable down to zero.
The same argument applies to dot R_n with |chi_n|<=s^2/2.
For n=1,2, permit lambda in a small positive neighborhood of lambda_n:
partial_lambda cos(s*sqrt(lambda))=-s*sin(s*sqrt(lambda))/(2sqrt(lambda))
is bounded by s^2/2. At positive t all its needed t derivatives are
dominated as in(13). This justifies differentiating(15) locally, including
the endpoint moments; it does not assume a frequency-diagonal limit of
unknown matrix entries. At lambda_n the differentiated identity is

    dot R_n''+lambda_n*dot R_n
                   =dot d_n-L-R_n,                    (16)
    dot c_n=a*sin(k_n*a)/(2k_n),
    dot b_n=sin(k_n*a)/(2k_n)+(a/2)*cos(k_n*a).

Every use of integration by parts below is first on [tau,a], where
these functions are smooth. The established continuity of R,R',dot R,
dot R' gives the limits of their complete Wronskian brackets. The
remaining terms have bounds by a constant times1+L(t), or products
of bounded continuous functions, hence are individually integrable.
There is no separated divergent F_n endpoint bracket in this argument.

Finally |F_n|<=L, so the omitted integral in(13) is bounded by
integral_0^tau L(t)^2 dt=O(tau*(1+log(a/tau)^2)), tending to zero.
C998g Section1's absolute triple-integral bound, or directly Tonelli
applied to L^2, identifies this limit with I_nm. This handles the
singular cutoff of the original K_tau, not only a formal ODE limit.

### 5. Boundary identities and elimination of single outputs

For (n,m)=(2,4),(1,3), subtract the two equations(15), multiplied by
R_m,R_n respectively. On [tau,a] one obtains

    (R_n'*R_m-R_n*R_m')'
       =(lambda_m-lambda_n)*R_n*R_m+d_n*R_m-d_m*R_n
           -lambda_n*L*R_m+lambda_m*L*R_n.             (17)

The cutoff limit is justified above. Fubini gives

    integral_0^a L(t)*R_n(t) dt=H_n,
    integral_0^a d_m(t)*R_n(t) dt=c_m*T_n+b_m*P_n.      (18)

For absolute convergence before swapping, use
integral_0^a |q_n(s)|/(t+s) ds<=k_n^2*a^2/4,
then integrate against L(t), (t+a)^(-1) or (t+a)^(-2).
For chi_n the corresponding integral is at most a^2/4. Thus(18), also
with dots, eliminates every single output via explicit weights(2).

For the base term, integration by parts with t*L(t)^2 tending to zero
at zero gives

    integral_0^a L(t)^2 dt
      =a*(log2)^2+2a*integral_0^a L(t)/(t+a) dt
      =2a*((log2)^2+D(1))=J.                           (19)

Since F_n*F_m=L^2+L*(R_n+R_m)+R_n*R_m, (17)-(19) yield, for the
two specified distinct positive pairs,

    (lambda_m-lambda_n)*(I_nm-J)
       =Delta W_nm+lambda_m*H_m-lambda_n*H_n
          +c_m*T_n+b_m*P_n-c_n*T_m-b_n*P_m.            (20)

For diagonal n=1,2, multiply(15) by dot R_n and(16) by R_n and
subtract. The derivative of V_n on the open interval is

    V_n'=d_n*dot R_n-R_n*dot d_n+L*R_n+R_n^2
                        -lambda_n*L*dot R_n.          (21)

Its justified cutoff limit, combined with
I_nn=J+2H_n+integral R_n^2, gives independently

    I_nn=J+Delta V_n+H_n+lambda_n*dot H_n
               +dot c_n*T_n+dot b_n*P_n
               -c_n*dot T_n-b_n*dot P_n.              (22)

This is a derived identity with finite endpoints, not a quotient
interpreted at zero denominator. Equations(7),(8) follow directly from
R_0=0 and(18),(19). At k_n*a=n*pi/2, the coefficients for n=1,2,3,4
are respectively (c_n,b_n)=(1,k_1),(2,0),(1,-k_3),(0,0).
For n=1, (dot c_n,dot b_n)=(a/(2k_1),1/(2k_1)); for n=2 they are
(0,-a/2). Substitution in(20),(22) gives precisely(9)-(12).
This checks all six cases and retains both Delta endpoints explicitly.

### 6. Parity normalization and scope

The image of a normalized full-cell mode e_n under C998a(4) is
sqrt(2)*(-1)^n*nu_n*cos(k_n*t), in its parity component only.
Consequently its K_0 pairing with mode m in the same parity is
2*(-1)^(n+m)*nu_n*nu_m*I_nm. With the square's coefficient1/4
from C998g, each of the six selected entries contributes
nu_n*nu_m*I_nm/2, because n+m is even. Opposite parities have separate
blocks. This is an entry convention, not a claim that the low modes
alone equal any frozen trial: neutral modes0,1 and all other free
coefficients remain mandatory in a later full assembly.

Only the six stated identities have been asserted and checked here.
Their proof suggests a later general-closure question, but that question,
stability near coincident frequencies/endpoints, finite arithmetic,
moment computation and complete work/error accounting are outside this
gate. The A-square, both mixed terms, projection/moments of the full
residual, inverse pairing, signed S3, higher/mixed signs and source-to-Xi
contracts remain unpaid. All older stops retain their prescription-specific
force; no claim about computational feasibility follows from closure.

### 7. Independent conceptual audit — 13 November 2026, step678

The invocation-start EXPLORE assessment676, approved in677, licenses
this six-case audit only. The source comparison675 and source-notes677
are reused: no applicable turnkey closure theorem was found there,
and Blower's half-line compact-support commutation theorem is not an
input. The work below checks the particular calculus application; it
does not reprove Folland's general theorems. All formulas(1)-(22) are
upheld without a changed hypothesis, numerical bound or direct input.
This audit is REPRODUCTION of the existing local result, not a claim
of progress beyond the inspected literature or an arbitrary-mode claim.

**Explicit weights and their endpoints.** For fixed 0<z<1, independent
differentiation in x gives

    d/dx {log(1-z)log(x+z)+D((x+z)/(1-z))}
      =[log(1-z)+log(1+(x+z)/(1-z))]/(x+z)
      =log(1+x)/(x+z).

The integration-by-parts boundary product log(x)log(1+x/z) vanishes
at zero and is zero at one. Substitution y=x/z in the remaining
integral therefore gives integral_0^1 log(x)/(x+z) dx=-D(1/z).
Subtracting this negative-log integral proves exactly(2), including
the PLUS D(1/z). The change t=ax has no extra factor: dt/(t+s)
=dx/(x+z). Every D argument in the displayed definition is positive;
no complex logarithm or branch convention is being used.

Independently, partial fractions give
A1=(L-log2)/(a-s), and subtracting integral_0^a(t+a)^(-2)dt=1/(2a)
gives A2. At s=a their integral representations give respectively
1/(2a) and3/(8a^2). For Q(a), the positive-log integral is
integral_0^1 log(1+x)/(1+x)dx=(log2)^2/2; its negative-log part
contributes D(1). For s in[a/2,a], the majorants for Aj and Q are
2a^(-j-1) and2L(t)/a respectively, integrable on(0,a).
Folland2.24 proves that these assigned values are the actual limits.

For a separate check at zero, put r=log(a/s)>=0. The positive
integral representations imply

    0<Aj(s)<=a^(-j)L(s),
    0<Q(s)<=1+log2+(1+log2)r+r^2/2.

The second bound follows by splitting at t=s: the two contributions
are at most log(2a/s)+1 and(log2)r+r^2/2. Thus all H,P,T moments
and their dotted versions are absolutely integrable. The weights
are explicit functions of s alone, independent of the mode indices
and of any unknown entry. Representation(3) is used to prove them,
not to define an oracle requiring two Carleman outputs.

**Original cutoff, regularized traces and spectral derivatives.**
For fixed tau>0 the kernel and its needed derivatives are continuous
and bounded on the closed finite square, so finite integration by
parts and Fubini in(13) are justified. For the Carleman factor
(t+s)^(-1), two derivatives in t equal two derivatives in s.
The integration-by-parts bracket is

    [cos(k*s)*(-1/(t+s)^2)+k*sin(k*s)/(t+s)]_0^a.

It contributes +1/t^2 at zero and BOTH displayed terms at a in(14).
In particular the sine term cannot be dropped at the odd modes.
Subtracting the k=0 equation gives(15) with the stated c,b signs.

For any compact positive lambda neighborhood needed at lambda_1 or
lambda_2, choose M with lambda<=M there. The uniform density bounds
|q_lambda(s)|<=M*s^2/2 and|partial_lambda q_lambda(s)|<=s^2/2 give

    |R_lambda(t)|<=M*a^2/4,   |R_lambda'(t)|<=M*a/2,
    |R_lambda''(t)|<=M*L(t),
    |dot R_lambda(t)|<=a^2/4, |dot R_lambda'(t)|<=a/2,
    |dot R_lambda''(t)|<=L(t),                 t>0.

For example s^2/(t+s)^3<=1/(t+s). For the zero traces, the
undifferentiated s integrands are bounded by M*s/2 and M/2 for
R and R'; the corresponding dotted bounds are s/2 and1/2.
These verify dominated convergence and give exactly(5), including
its negative derivative sign. At t=a the same formulas are ordinary
smooth endpoint values. No second derivative at zero is asserted.
Since L is integrable, the positive-cutoff derivative identities have
integrable limits even though R'' can grow logarithmically.

At t>=tau, each mixed t and lambda derivative has an integrable
majorant from the displayed density bounds and the denominators
bounded below by tau. Folland2.27 thus justifies differentiating(15)
with respect to lambda, giving(16). Its application to H,P,T uses
s^2Q/2,s^2A1/2,s^2A2/2. At the zero endpoint the same theorem uses
s/2 and1/2 for R(0) and R'(0); at a the denominators are bounded.
Thus the dotted moments and traces are independent parameter
derivatives as defined, not limits postulated for matrix entries.

All measures are finite Lebesgue products, hence sigma-finite, and
the integrands are Borel measurable away from irrelevant null axes.
Tonelli applied to the positive triple majorant gives

    integral_(0,a)^3 1/[(t+s)(t+u)] dt ds du
      =integral_0^a L(t)^2 dt
      <=a*((log2)^2+2log2+2)<infinity.

Folland2.37/2.39 therefore apply to each signed cosine product before
any interchange. For 0<tau<a the error of the ORIGINAL cutoff obeys

    |I_nm-I_nm(tau)|
      <=tau*((log(2a/tau))^2+2log(2a/tau)+2) -> 0.

This follows by integrating log(2a/t)^2 over(0,tau), and proves that
the regularized ODE calculation computes the specified K_0 pairing.
It is not merely an existence statement for a different regularization.

**Wronskian orientation and independent diagonals.** With the
orientation in(6), differentiating W directly gives

    W_nm'=R_n''R_m-R_n R_m''
      =(lambda_m-lambda_n)R_n R_m+d_n R_m-d_m R_n
         -lambda_n L R_m+lambda_m L R_n.

The zero and a traces just checked retain the complete difference
W_nm(a)-W_nm(0). Every term is integrable, bounded by a constant
times1+L(t). In(18), the absolute integral of the inner q density
is at most lambda_n*a^2/4; for the dotted density it is at most
a^2/4. Integration against L,(t+a)^(-1),(t+a)^(-2) is finite.
Thus Fubini separately verifies all three single-output eliminations
and their dotted versions. Also tL(t)^2->0, while
L'(t)=-a/[t(t+a)], so

    integral_0^a L^2=a*(log2)^2+2a*Q(a)
                    =2a*((log2)^2+D(1))=J.

Solving the integrated W identity for integral R_n R_m, then adding
H_n+H_m, gives exactly(20); in particular its H coefficients are
-lambda_n on H_n and+lambda_m on H_m.

For a diagonal, differentiate V=R' dot R-R dot R' directly and use
(15),(16). The result is

    V'=d dot R-R dot d+LR+R^2-lambda L dot R.

It integrates with BOTH finite endpoints. Solving for integral R^2
and adding2H gives(22), with+dot c*T+dot b*P-c*dot T-b*dot P.
This derivation uses neither a divided frequency difference nor an
unknown diagonal entry as additional input.

The independent substitutions needed for ALL six entries are:

| mode n | c_n | b_n | dot c_n | dot b_n |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | not used | not used |
| 1 | 1 | k_1 | a/(2k_1) | 1/(2k_1) |
| 2 | 2 | 0 | 0 | -a/2 |
| 3 | 1 | -k_3 | not used | not used |
| 4 | 0 | 0 | not used | not used |

R_0=0 gives I_00=J and I_02=J+H_2. In(22) the n=2 correction
is-(a/2)P_2-2dot T_2, exactly(9); for n=1 it is
(a/(2k_1))T_1+P_1/(2k_1)-dot T_1-k_1dot P_1, exactly(11).
In(20), the (2,4) correction is-2T_4, exactly(10), and the
(1,3) correction is T_1-k_3P_1-T_3-k_1P_3, exactly(12).
The only divided gaps are12*pi^2/ell^2 and8*pi^2/ell^2, both
strictly positive. This checks the two zero-mode cases, both positive
diagonals and both distinct-frequency cases individually.

**Parity and final scope.** Substituting
e_n(ell-t)=(-1)^n*nu_n*cos(k_n*t) in C998a(4) gives
sqrt(2)nu_n*cos(k_n*t) for even n in the plus component, and
-sqrt(2)nu_n*cos(k_n*t) for odd n in the minus component.
The other component vanishes. Multiplication by C998g's square
coefficient1/4 gives nu_n*nu_m*I_nm/2 in every selected pair.
This includes nu_0=ell^(-1/2); it does not silently use the
positive-mode normalization at zero. For complex coefficient
combinations, the second-slot coefficient is conjugated in the
inherited first-slot-linear convention; the real basis entries here
are unchanged. Opposite parity blocks are separate.

The continuation test passes for these six cases only. H,P,T and
their dots are fixed-weight single-density moments; R and its dots
in the final formulas occur only as separately specified endpoint
data. There is no hidden integrated product of unknown outputs.
No witness or numerical certificate is needed for these identities,
and none was loaded. Full finite-mode closure, stable evaluation,
actual entries, the1e-10/20000000 square service, A-square, both
mixed terms, projection, full100million work, residual/inverse debt,
signed S3 and actual-Xi/global contracts remain unresolved. Existing
source and prescription stops are unchanged. No new mathematical
dependency was introduced; C998a and C998g remain the direct inputs.

## Mathlib

A full matching theorem for these six finite-cell identities and their
regularized boundary formulas was not checked. Fubini/Tonelli and
ordinary differentiation/integration by parts are supporting inputs,
not a full formalization. Unknown Mathlib coverage is not absence.
The cited primary Folland theorems supply only the interchanges,
dominated limits and parameter derivatives whose hypotheses are
verified above. The original construction676 was POTENTIALLY_NEW only
relative to the bounded search recorded675; independent audit678 is
REPRODUCTION. Neither classification certifies originality or
mathematics beyond all literature.
