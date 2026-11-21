# Lemma 722: the actual signed remainder has a competing exponential limsup

## Hypotheses

Retain the original fixed L703 profile through the audited finite
identities of L714, the audited phase and saddle of L719, and the
audited signed support-edge limsup of L721. All limits are along
n=12q+3, q>=1. In particular

    U=121/64, A=27/10, d=5/4, c_0=1/8,
    u=(3+4i)/10, alpha=d+c_0=11/8, h=A/n,
    omega=A*[log(9/5)-4/5+(121/100)*log(201/121)],
    I=[omega-delta,omega+delta], 0<delta<1/3000.

The nonnegative smooth chi is unchanged, supported in I and equal to
one on [omega-delta/2,omega+delta/2]. Set b=sup supp(chi), not the
prescribed enclosure endpoint. Use exactly L714's signed quantities

    R_n=R_n(3/20)=P_n+K_n,
    K_n=integral_I chi(v)*p_n(v)dv,
    P_n=-W_n(u,i*c_0)/h*integral_I chi(v)*exp(n*c_0*v/A)dv,
    Q_t(u,y)=(d+u*t)*(U*u+(d-i*y)*t)
                       /[(U*u+d*t)*(d+u*t-i*y)],
    W_n(u,y)=product_(j=0)^(n-1) Q_(j/n)(u,y).

Write S for L719's phase and r(v)=Re S(v). Extended logarithms use
log(0)=-infinity. No statement from L713's absolute-envelope estimates,
L717 or L718 is a premise. No endpoint law, analytic continuation of
chi, change of width or size interpolation is permitted.

## Conclusion

The residue is nonzero for every allowed n, and its full rate is

    p(b):=lim log|P_n|/n
         =integral_0^1 log|Q_t(u,i*c_0)|dt+c_0*b/A
         <1/5000.                                             (1)

The actual signed shifted integral has the limsup

    limsup log|R_n|/n=r(b)>1/200,
    limsup log|R_n/P_n|/n=r(b)-p(b)>3/625.                      (2)

Thus an exponentially subordinate signed R_n cannot justify the
proposed positive-bump residue isolation at this fixed peak. There
are arbitrarily large permitted n with exponentially large |R_n/P_n|.
No full limit for R_n, eventual nonvanishing, sign or assertion about
every large n is made. The full response retains its other frequencies,
comb, physical tails and finite moments. No cancellation against those
terms, spatial Jensen defect, angular persistence, amplitude/full charge,
H/support, Xi realization or RH conclusion follows.

Status: derived in step 197; accepted by the separate step-199 audit
in Section 5 below.
This is a local rate comparison using the accepted support-transfer
input, not a new general signed-transform theorem or certified novelty.

## Proof

### 1. Source scope and the actual residue rate

Reuse the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-signed-bump-remainder-rate.md`.
It approves precisely this actual signed remainder/residue comparison.
The earlier step-175 reduction could not pay K_n's outer cancellation;
L721 is the materially new input. The common-phase, gamma/Rice and
absolute-horizontal-envelope failures do not decide this comparison.
No additional general saddle or support theorem is imported or reproved.
L714 already imports finite rational inversion/residues from NIST DLMF
1.10(iv), (1.10.8), and 1.14(i), (1.14.1), (1.14.3), under explicitly
checked hypotheses. Here its audited signed identity is used directly.

First independently verify the previously unaudited L714 (6). At
y=i*c_0 all four affine factors in Q_t have strictly positive real
parts for 0<=t<=1: d+u*t, U*u+alpha*t, U*u+d*t and alpha+u*t.
They are nonzero and have bounded logarithmic derivatives on this
compact interval. The real function f(t)=log|Q_t(u,i*c_0)| is C^1.
If |f'|<=M, each left-cell Riemann-sum error is at most M/(2*n^2).
Consequently

    log|W_n(u,i*c_0)|=n*integral_0^1 f(t)dt+O(1).              (3)

The bump integral B_n=integral_I chi(v)*exp(n*c_0*v/A)dv is positive
and at most ||chi||_1*exp(n*c_0*b/A). Given epsilon>0, the definition
of b as the support supremum and continuity/nonnegativity yield a
closed interval of positive length in (b-epsilon,b) on which chi>=a
for some a>0. To see this, first take a point with chi>0 sufficiently
close to b, then shrink its positivity neighborhood. The integral over
that interval is at least its length times a*exp(n*c_0*(b-epsilon)/A).
Taking lower/upper limits, then epsilon down to zero, proves

    lim log B_n/n=c_0*b/A.

Every factor in W_n is nonzero, so P_n!=0. Since log(1/h)=O(log n),
this proves the equality in (1). The endpoint need not itself be a
positivity point. No endpoint asymptotic or transform nonvanishing
theorem is assumed.

### 2. A rigorous lower phase bound without a sampled saddle

For Re(s)>0 define the L719 phase

    T(s;v)=ell_D+(u*s-d)*v/A
                       +integral_0^1 [Log(U+s*t)-Log(s+t)]dt,
    ell_D=integral_0^1 [Log(d+u*t)-Log(U*u+d*t)]dt.

All logarithms are right-half-plane branches. L719 gives
T(s_v;v)=S(v), T_s(s_v;v)=0 and

    9/5<Re(s_v)<37/20, -37/20<Im(s_v)<-9/5.

Set a=73/40 and s0=a*(1-i), the center of this rectangle. Every
straight segment from s_v to s0 stays in Re(s)>=9/5. On it,

    |T_ss(s;v)|
      <=integral_0^1 [t^2/|U+s*t|^2+1/|s+t|^2]dt
      <=1/(3*U^2)+25/81 <1/2.

The segment lies in the domain of the stated logarithms. Taylor's
formula along that segment, centered at its exact stationary endpoint,
therefore gives

    |T(s0;v)-S(v)| <=(1/4)*|s0-s_v|^2 <1/3200,              (4)

because |s0-s_v|^2<2*(1/40)^2=1/800. This uses the audited rectangle,
not a numerical Newton iterate.

At v=omega let r0=Re T(s0;omega). Taking real parts of these legal
logarithms expresses it as a fixed real integral plus a linear term:

    r0=integral_0^1 log| (d+u*t)*(U+s0*t)
                                  /[(U*u+d*t)*(s0+t)] |dt
                              +(11/400)*omega/A.             (5)

The exact certificate below proves r0>11/2000 and, more directly,
r0-1/3200>1/200. Thus (4) proves r(omega)>1/200. L721 gives
r'(v)>1/270 on I. Since b>=omega+delta/2>omega,

    r(b)>r(omega)>1/200.                                    (6)

### 3. Complete rational rate certificate

This finite calculation is necessary to separate the actual rates;
it does not reprove a general asymptotic theorem. It also checks the
residue upper bound independently of L713's unaudited certificate.
For rational 0<=t<=1, the squared modulus in (5) is exactly

    Z_s(t)= [((d+3*t/10)^2+(2*t/5)^2)
                  *((U+a*t)^2+(a*t)^2)]
             / [((3*U/10+d*t)^2+(2*U/5)^2)
                  *((a+t)^2+a^2)].

The squared modulus for the residue's product integral is

    Z_p(t)= [((d+3*t/10)^2+(2*t/5)^2)
                  *((3*U/10+alpha*t)^2+(2*U/5)^2)]
             / [((3*U/10+d*t)^2+(2*U/5)^2)
                  *((alpha+3*t/10)^2+(2*t/5)^2)].

Both integrands are (1/2)log of these positive rational functions.
For a nonzero affine factor A0+B0*t, the absolute fourth derivative
of log|A0+B0*t| is at most 6*|B0/(A0+B0*t)|^4. For Z_s the four
lower moduli can be taken as d, U/2, U, 9/5, respectively, with
upper slope moduli 1/2, d, 3, 1; here |s0|<3. Hence the fourth
derivative of (1/2)log Z_s is bounded by

    6*[(1/(2*d))^4+(d/(U/2))^4+(3/U)^4+(5/9)^4]<100.

For Z_p use lower moduli d,U/2,U/2,alpha and slopes
1/2,d,alpha,1/2, obtaining the bound

    6*[(1/(2*d))^4+(d/(U/2))^4
                       +(alpha/(U/2))^4+(1/(2*alpha))^4]<100.

All these are uniform on [0,1]. Import the standard composite Simpson
rule, [NIST DLMF 3.5(ii), (3.5.6)--(3.5.8)](https://dlmf.nist.gov/3.5.ii).
For real C^4 data, even N and mesh 1/N on [0,1], its error has modulus
at most K/(180*N^4) when |f''''|<=K. Both present real log-modulus
integrands are C^4 because their affine factors are nonzero. Take
N=64, K=100. The original certificate's error K/(45*N^4) is four
times this valid bound, so remains conservative. The standard rule
replaces the unnecessary general quadrature reproof from step 197;
the original calculation and its wider bounds are preserved.

The script extracts only the four exact arithmetic helper definitions
from the preserved step-166 script, without executing its calculations.
They enclose log of each positive rational by reciprocal/range reduction
to [1,2] and

    log x=2*sum_(j=0)^39 z^(2*j+1)/(2*j+1)+tail,
    z=(x-1)/(x+1), 0<=z<=1/3,
    0<=tail<=8/[3*81*2^81].

Every multiplication/division in that helper is rounded outwards at
scale 2^100. The displayed tail also covers z<=1/2 and is conservative.
The same routine encloses omega. All decisions compare exact integers
or fractions; decimals are previews only.

Reproduce with

    python3 scripts/one-sided-hankel/signed-remainder-rate-gap-197.py

The full certificate, including all 65 quadrature rows for each
integrand, helper/script hashes, errors, actual/required bounds and
failures, is
`scripts/one-sided-hankel/signed-remainder-rate-gap-197.json`.
All ten comparisons pass; the entire `/checks` object was inspected
using the scoped JSON inspector with `--full`. The resulting exact
fractions certify

    r0-1/3200 >1/200,
    integral_0^1 log|Q_t(u,i*c_0)|dt
                 +c_0*(omega+1/3000)/A <1/5000.

Since b<=omega+delta<omega+1/3000, this proves the strict upper
bound in (1). As previews, the lower phase bound is about 0.00539317
and the upper residue bound about 0.000183812; no displayed decimal
is a proof input. The failed preliminary mpmath diagnostic was only a
missing local module; an elementary floating diagnostic suggested the
thresholds but supplies no certified bound.

### 4. Transfer the strict gap through the actual signed sum

L721, including its entire exponential error, gives

    limsup log|K_n|/n=r(b)=:k.

Equations (1) and (6) give p:=p(b)<1/5000<1/200<k. The identity
R_n=P_n+K_n is signed and exact; neither original defining integral
is replaced by its absolute integral. The following inequalities act
only on those completed complex numbers.

The triangle inequality and the two rate upper bounds imply
limsup log|R_n|/n<=k. For any epsilon with 0<epsilon<(k-p)/2, the
definition of limsup supplies infinitely many permitted n with
|K_n|>=exp(n*(k-epsilon)); the full residue limit gives
|P_n|<=exp(n*(p+epsilon)) for all sufficiently large n. On that
infinite subsequence,

    |R_n|>=|K_n|-|P_n|
      >=exp(n*(k-epsilon))
                    *[1-exp(-n*(k-p-2*epsilon))].

The bracket tends to one. Letting epsilon decrease to zero proves
the reverse limsup bound, including the possibility of zero R_n
on other subsequences. Since P_n!=0 and log|P_n|/n converges to p,
subtracting that convergent sequence gives
limsup log|R_n/P_n|/n=k-p>1/200-1/5000=3/625. This proves (2).

Only the exponentially subordinate signed-remainder certificate at
this fixed peak is excluded. The full response and the complementary
spatial Jensen integral can still involve other contributions and
cancellations. No failure of RH or of every fixed-profile strategy
has been inferred.

### 5. Separate critical audit — 3 November 2026, step 199

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-03-signed-remainder-rate-gap-audit.md`,
whose covered audit target is unchanged. This step checks the existing
application and reproduces its finite evidence; it claims neither a
new general theorem nor originality beyond the checked sources.
The accepted interfaces are precisely L714's signed R_n=P_n+K_n,
L719's legal T, stationary s_v and exact phase identity, and L721's
signed limsup and r'>1/270. L715/L716/L720 remain inherited.
L713's envelope, L717 and L718 are not inputs.

**Residue and endpoint.** At y=i*c_0 the four real parts are at
least d, 3*U/10, 3*U/10 and alpha, respectively. Thus the product
has no zero or pole at any quadrature or product node, including
j=0, and f in (3) is C^1. Compactness bounds f'; summing its
per-cell M/(2*n^2) integral error gives (3). The standard compact
Riemann-sum input is [DLMF 1.4(v), (1.4.18)](https://dlmf.nist.gov/1.4#E18).
Because chi is nonnegative, continuous, nonzero on its plateau and
compactly supported, b is finite and positive. For each small epsilon,
some point in (b-epsilon,b) has chi>0; otherwise b would not be
the support supremum. A smaller closed positivity interval gives
the lower bound for B_n in Section 1. Together with its L1 upper
bound this proves the full rate, including flat or disconnected
support edges. It never assumes chi(b)>0. The factor 1/h contributes
only log(n/A)/n, and every P_n is nonzero.

**Phase and quadrature applicability.** Every segment from s_v to
s0 lies in Re(s)>9/5, so U+s*t and s+t stay in the right half-plane.
Differentiation under the compact t integral is therefore valid.
The exact second-derivative estimate is
476617/1185921<1/2. For g(tau)=T(s_v+tau*(s0-s_v);v), use the
integral Taylor formula componentwise,
[DLMF 1.4(vi), (1.4.35)--(1.4.37)](https://dlmf.nist.gov/1.4#E37).
Here g'(0)=0 and |g''|<=|s0-s_v|^2/2. Integration of (1-tau)
g'' gives (4), without a common-point complex Lagrange remainder.
The linear real part is exactly 11/400. The four modulus lower
bounds in Section 3 follow from their positive real parts, except
|U*u+d*t| and |U*u+alpha*t|, whose squared moduli increase with
t>=0 and start at U^2/4. For each factor,
(d/dt)^4 log|A0+B0*t|=-6*Re((B0/(A0+B0*t))^4).
Thus the two displayed fourth-derivative bounds apply to the actual
integrands. They equal, respectively,
16732369711884962/293001795466875<100 and
6090405972576/133974300625<100. Simpson's hypotheses hold on the
entire closed interval, with the factor 1/2 and weights as recorded.
The standard error is 5/150994944; the saved conservative error is
5/37748736. No sampled saddle enters these bounds.

**Logarithm implementation and complete evidence.** Import the
odd-power identity [DLMF 4.6(i), (4.6.4)](https://dlmf.nist.gov/4.6#E4)
for positive real arguments. In log_unit, z=(a-b)/(a+b) is in
[0,1/3]. Its floor/ceiling fixed-point endpoints bracket z; squaring
and multiplying nonnegative interval endpoints preserves enclosure.
Induction gives pl/SCALE<=z^(2k+1)<=pu/SCALE at every term. The
rounded divisions and sums therefore bracket the first 40 terms.
The exact remaining positive tail is at most
2*z^81/[81*(1-z^2)]<=8/[3*81*2^81], using even the weaker z<=1/2.
ceildiv rounds this upper tail outwards. For logq, inversion when
q<1 followed by denominator doubling reduces the argument to [1,2];
adding the nonnegative integer multiple of the enclosed log(2) and
then reversing endpoints under negation gives the correct interval.
Their nonbuiltin globals are only F, SCALE, TERMS, LOG2 and each other.
The extracted functions use the original SCALE=2^100, TERMS=40 and
a freshly computed LOG2; fixed is extracted but unused by this script.

Reproduce the independent audit with

    python3 scripts/one-sided-hankel/signed-remainder-rate-gap-audit-199.py

The full evidence is
`scripts/one-sided-hankel/signed-remainder-rate-gap-audit-199.json`;
the separate replay is
`scripts/one-sided-hankel/signed-remainder-rate-gap-replay-199.json`.
The original script, helper and certificate are unchanged. Original
hashes match current files, and executing the actual original code
with only its output destination redirected reproduces the complete
saved JSON exactly, including both complete sets of 65 nodes.

Independently, the audit constructs each squared modulus by exact
complex-pair multiplication of its four factors; it does not reuse
the original squared-modulus functions. Each of the 130 saved node
intervals contains a separately computed rational logarithm interval.
For this second computation, multiply or divide the argument by 2
to reach [1,2], sum 80 odd-power terms exactly, and bound the tail by
2*z^161/[161*(1-z^2)]. Add the corresponding signed log(2) interval,
then round outwards at scale 2^180. For a negative binary exponent,
the log(2) endpoints are reversed before multiplication. This proves
enclosure independently of the original fixed-point implementation.
The full finite sums, tails, exact factors, arguments, weights and
both enclosures are saved for every node. Both weighted sums and
all ten actual/required comparisons were reconstructed exactly;
all 163 audit checks pass and the failure list is empty.

Using the sharper imported Simpson bound, the independent lower
phase and upper residue enclosures are, as previews, 0.00539327419461
and 0.000183712479164. Their complete fractions and exact comparisons
with 1/200 and 1/5000 are saved and were inspected, along with the
original complete /checks object. Both node sets were checked in full
by the independent rational computation, not accepted from previews.
The original wider bounds alone already establish (1)--(2).

**Signed limsup and scope.** L721 gives finite k=r(b), a limsup only.
Its plateau implies b>=omega+delta/2, so r'>1/270 makes (6) strict.
The residue full limit p is finite and p<1/5000<1/200<k.
For each epsilon in Section 4 the reverse triangle inequality is
applied only after completing the actual complex sums. On infinitely
many permitted n its positive bracket tends to one; the ordinary
upper triangle inequality bounds the full-sequence limsup by k.
Letting epsilon tend to zero proves precisely the claimed limsup.
Subtracting log|P_n|/n is legitimate because this sequence converges
and P_n never vanishes; extended log values at zeros of R_n are
retained. The strict arithmetic gap is 1/200-1/5000=3/625.

Sections 1--4 pass this separate audit. The signed subordination
certificate at these unchanged data is stopped. No full R_n limit,
eventual nonvanishing, full-response cancellation verdict, spatial
Jensen estimate, realization or RH conclusion is accepted. Direct
mathematical inputs remain L714, L719 and L721; the DAG is unchanged.

## Mathlib

Full matching coverage is not checked. No formalization is claimed
for the actual finite array, the L721 support transfer or (1)--(2).
Compact Riemann sums, elementary Taylor bounds, positive real Laplace
endpoint bounds and limsup arithmetic are supporting tools, not a
matching theorem for this signed profile. No Mathlib absence is inferred.
