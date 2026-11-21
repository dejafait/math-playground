# L913: exterior payment and proper crossing cuts; full reserve unpaid

## Hypotheses

Use L019's complete actual theta kernel, L898's marginal at x=16,y=0,
and exactly L905's lobes P_j,N_k, normalized resources r_j, demands d_k,
normalizer A0>0, and core F={-2,-1,0,1}. Put k(u)=K(|u|) and use raw
capacities R_j=A0 r_j and demands D_k=A0 d_k throughout this proof.
No theta index or transverse spatial direction is truncated.

Numerical comparisons reuse the audited L905/L912 results and assume
L037's outward Decimal arithmetic, widened correctly rounded exp,
Machin pi enclosure, rejection of exceptional arithmetic, and trusted
Python execution. The new certificate uses precision 70. These arithmetic
contracts are not independently formally verified. No total-transform
sign, zero location or infinite allocation is a premise.

This is the one specialization approved in
`drafts/literature/2026-11-09-hall-monotone-tail-boundary-reserve-test.md`.
The associated-kernel and Hall inputs are known results; the application
and reserve estimate below are local progress, not a claim of originality
beyond the inspected sources. The separate conceptual audit in step172
validates the stated partial reduction and scalar enclosure under the
same arithmetic contracts; it does not pay the full reduced reserve.

## Conclusion

1. Every exterior demand k>=2 can be paid entirely from R_k, and every
   exterior demand k<=-3 from R_(k+1), without exceeding capacity.
   The payments are absolutely summable. The exact raw charges against
   the two resources shared with the core are D_2 and D_-3=D_2.
2. Write C=D_2+D_-3 and subtract those charges from R_2 and R_-2.
   If all fifteen reduced core cuts are nonnegative, this payment extends
   to a conserved allocation of every demand. Every finite Hall cut,
   including a cut crossing either or both core boundaries, is at least
   its corresponding reduced core cut. This is a sufficient construction,
   not a necessary condition for all possible allocations.
3. The complete analytic bound proved below is C<=U, where, under L037,

   \[
     0.00004284047<U<0.00004284048.
     \tag{1}
   \]

   Thus every nonempty proper reduced core cut has raw margin greater
   than 196/10^6. In particular every finite cut whose intersection with
   F is nonempty and proper is strictly positive; exterior-only cuts
   are nonnegative. The sole unpaid core condition for this construction
   is A0 H(F)-C>=0.

The required discriminator was U<15/10^6. It fails by more than
27.84047/10^6, and even L912's stronger saved lower bound
0.0000159908498950 does not pay U. These facts concern the upper-bound
formula U, not a lower bound for C. They do not certify a negative Hall
cut, reject all possible allocations, establish infinite feasibility,
or prove a new actual-Xi sign. Stop this analytic closure attempt; no
new lobe integration, refinement or parameter sweep is implied.

## Proof

### Imported shape and exact normalization

George Csordas, *Fourier transforms of positive definite kernels and the
Riemann xi-function*, [arXiv:1309.0055v2](https://arxiv.org/pdf/1309.0055v2),
21 February 2014, Definition1.2 p2, Theorem3.5/(3.7)-(3.9) pp6-7,
(4.2)/Theorem4.1 p10, Theorem4.2/Remark4.3(a)/Theorem4.5 p11.
For a smooth positive even admissible kernel with strictly concave
logarithm on (0,infinity), Theorem3.5 makes its associated kernels
admissible, hence strictly decreasing on (0,infinity). Theorem4.5 verifies
this for the source theta kernel phi_C. Its proof uses Theorem4.1's
even smooth extension and derivative decay, and Theorem4.2/Remark4.3(a)'s
logarithmic concavity. Both derivative-sign cases in Theorem3.5, on
0<s<t and s>t, were checked in the reused assessment and at application.
We import this result, not a convexity or positive-definiteness assertion.

Comparison of the complete series (4.2) with L019 gives
k(u)=4 phi_C(u/2) for every real u, using the source's even extension.
L905's full density, expressed as a whole-line integral, is

\[
 \rho(q)=\int_{\mathbb R}t^2k(t+q/2)k(t-q/2)\,dt.
\]

Substitute t=2s. The factors from t^2, dt and the two kernels are
4, 2 and 16, respectively. Therefore

\[
 \rho(q)=128J_1(q/4),\qquad
 J_1(v)=\int_{\mathbb R}s^2\phi_C(s+v)\phi_C(s-v)\,ds.
 \tag{2}
\]

Consequently rho is positive, smooth, even and strictly decreasing for
q>0. At q=0 it is smooth with derivative zero, not a reflected finite
head. The source supplies smoothness and derivative domination for (2);
L898 supplies absolute Fubini and total mass integral rho=A0<infinity.
No differentiation of K_4(|u|) at zero is used.

### Exterior payment and reduction of every finite cut

Put a=pi/16. For k>=2, translation q -> q-a maps N_k bijectively onto
P_k. Both intervals lie in (0,infinity), and
cos(16(q-a))=-cos(16q). Since rho(q-a)>rho(q) and -cos(16q)>0 in
the interior of N_k, integration gives

\[
 D_k=\int_{N_k}[-\cos(16q)]\rho(q)\,dq<R_k.
 \tag{3}
\]

Evenness gives D_k=D_(-k-1) and R_j=R_-j. For k<=-3, apply (3) to
-k-1>=2 to obtain D_k<R_(k+1). Set the exterior flow equal to D_k on
these single edges and zero on all other exterior edges. Each resource
is used by at most one exterior demand. The two payer ranges j>=2 and
j<=-2 are disjoint; only j=2 and j=-2 also neighbor core demands.
The exact charges there are D_2 and D_-3. Reflection equates their
values but does not duplicate either capacity.

Let e_j denote all exterior expenditure from resource j:
e_j=D_j for j>=2, e_j=D_(j-1) for j<=-2, and e_j=0 otherwise.
Define R'_j=R_j-e_j>=0. L898 implies
sum_j R_j+sum_k D_k=integral |cos(16q)|rho(q)dq<=A0, so all these
payments, residual capacities and subsequent sums converge absolutely.

For any finite set S of demand indices, let S_c=S intersect F and
T(S)=union_(k in S){k,k+1}. Every exterior demand in S has its assigned
payer in T(S). Hence

\[
 \begin{aligned}
 \sum_{j\in T(S)}R_j-\sum_{k\in S}D_k
 &\geq\sum_{j\in T(S)}R'_j-\sum_{k\in S_c}D_k\\
 &\geq\sum_{j\in T(S_c)}R'_j-\sum_{k\in S_c}D_k
 =:\mathcal H'(S_c).
 \end{aligned}
 \tag{4}
\]

The first inequality follows from sum_(T(S)) e_j>=sum_(S outside F) D_k;
the second uses nonnegative residual capacities and T(S_c) subset T(S).
This includes disconnected S and cuts crossing one or both boundaries.
For S_c empty the last expression is zero. In particular no exterior
capacity is silently reused to pay a core demand.

For nonempty S_c subset F, exactly

\[
 \mathcal H'(S_c)=A0H(S_c)
 -D_{-3}\,1_{\{-2\in T(S_c)\}}-D_2\,1_{\{2\in T(S_c)\}}.
 \tag{5}
\]

If all such reduced cuts are nonnegative, finite core allocation follows
from Twan Koperberg, *Couplings and Matchings: Combinatorial notes on
Strassen's theorem*, [arXiv:2202.02092v1](https://arxiv.org/pdf/2202.02092v1),
Proposition4, pp5-6. To meet its equal-side-total hypothesis, use the five
residual core resources as one side, and adjoin a dummy demand connected
to all five resources with weight sum_(j=-2)^2 R'_j-sum_(k in F)D_k.
This weight is nonnegative precisely because the full reduced cut passes.
The sides now have equal totals. A subset without the dummy satisfies
the stipulated reduced cut inequality. A subset containing it has all
resources as neighbors and demand at most the full demand total. These
verify every hypothesis; Proposition4 supplies nonnegative edge weights.
Discard its dummy edges as unused surplus, and combine the core edges
with the exterior flows (3). This is a conserved, absolutely summable
allocation on the original countable graph. No countable Hall theorem
or equality of unknown positive/negative lobe totals is assumed.

### One full-kernel analytic reserve bound

We sharpen L312's positive summand majorant only by retaining exact pi.
For u>=0, dropping the negative term in each positive summand of L019
gives

\[
 K(u)\leq8\pi^2 e^{9u/2-\pi e^{2u}}
       \sum_{n\geq1}n^4e^{-\pi(n^2-1)e^{2u}}
 \leq c e^{9u/2-\pi e^{2u}},
 \tag{6}
\]

where

\[
 r=\frac{81}{16}e^{-5\pi}<1,\qquad
 c=8\pi^2\left(1+\frac{16e^{-3\pi}}{1-r}\right).
\]

Indeed e^(2u)>=1, the n=2 term of the remaining series is at most
16e^(-3pi), and successive ratios for n>=2 are at most
(3/2)^4 e^(-5pi)=r. This bounds the entire theta series; there is no
unpaid finite-head error. The inequality r<1 follows already from pi>3
and the positive series for e^15, or from the saved interval evaluation.

Set

\[
 Q=9\pi/32,\quad E=e^Q,\quad h=Q/2,\quad
 \beta=2\pi E-9/2,\quad D=\pi(E^2+1),\quad\lambda=2D-9.
 \tag{7}
\]

Here E>2: Q>27/32 and 1+27/32+(27/32)^2/2>2. Thus beta>0 and
lambda>0. For t>=0 and q>=Q, put m=max(t,q/2), n=min(t,q/2).
The product in the half-line density is bounded by

\[
 G(q,t)=c^2\exp\{9m-2\pi e^{2m}\cosh(2n)\}.
 \tag{8}
\]

This follows from |t+q/2|+|t-q/2|=2m and
e^(2|t+q/2|)+e^(2|t-q/2|)=2e^(2m)cosh(2n).
For q>2t, the q derivative of log G is
9/2-2pi e^q cosh(2t)<=-beta. For q<2t it is
-2pi e^(2t)sinh(q)<=-pi(e^(2q)-1)<=-pi(E^2-1)<-beta.
The last strict comparison follows because
pi(E^2-2E-1)+9/2>9/2-pi>0 for E>2 and pi<4.
G is continuous at q=2t. Integrating these bounds on each side of the
possible corner gives G(q,t)<=G(Q,t)e^(-beta(q-Q)) for every t>=0.

For 0<=t<=h, cosh(2t)>=1+2t^2 bounds (8) by
c^2 exp(9Q/2-2pi E) exp(-4pi E t^2). Enlarge this positive integral
to t>=0 and use the standard Gaussian moment identity
integral_0^infinity t^2 exp(-A t^2)dt=sqrt(pi)/(4A^(3/2)), A>0.
It follows, including the density's factor two, that the inner part is
at most

\[
 R_{\rm in}=\frac{c^2}{16\pi}\exp(3Q-2\pi E).
 \tag{9}
\]

For t=h+s, s>=0, the exponent of G(Q,t) is
9Q/2+9s-D e^(2s)<=9Q/2-D-lambda s. Therefore the complete remaining
transverse contribution is at most

\[
 R_{\rm out}=2c^2e^{9Q/2-D}
       \left(\frac{h^2}{\lambda}
             +\frac{2h}{\lambda^2}+\frac{2}{\lambda^3}\right).
 \tag{10}
\]

The inner Gaussian enlargement is only an upper estimate; (10) still
pays the actual outer domain. Both are nonnegative and integrable.
Combining (8)-(10) proves, on the entire required half-line,

\[
 \rho(q)\leq(R_{\rm in}+R_{\rm out})e^{-\beta(q-Q)}
       =R e^{-\beta(q-Q)}\quad(q\geq Q).
 \tag{11}
\]

Now N_2=[Q,Q+a] and -cos(16(Q+w))=sin(16w)>=0 for 0<=w<=a.
Reflection gives C=2D_2, so (11) and elementary integration yield

\[
 C\leq U:=2R\int_0^a e^{-\beta w}\sin(16w)dw
   =\frac{32R(1+e^{-\beta a})}{\beta^2+256}.
 \tag{12}
\]

The endpoint identity uses 16a=pi. This is a bound for integrated raw
charges, with no division by A0. It includes all theta indices, both
transverse directions, both boundary demands and the full q intervals.
No numerical lobe integration or total cosine sign was used.

### Arithmetic, all proper cuts and the stopped condition

Reproduce the single evaluation of (6)-(12) with

```
python3 scripts/theta-marginal/boundary_reserve_170.py
```

The script imports only L037's arithmetic/pi helpers, runs their existing
self-check, and writes every evaluated constant, bound and comparison to
`scripts/theta-marginal/boundary-reserve-170.json`. All arithmetic uses
outward intervals, exact integers and rational inputs; exp is widened.
It performs no quadrature. Complete `/constants` and `/bounds` were
inspected, including the unrounded load-bearing value U. There are no
failed verification checks; the reserve requirement itself fails.
The separate independent replay and analytic audit are recorded below.

The strict rational enclosure (1) follows from the full certificate.
For every nonempty proper S_c, L905's audited table gives
A0H(S_c)>0.00023960. By (5) and C<=U,

\[
 \mathcal H'(S_c)>0.00023960-U
 >0.00019675952>196/10^6.
 \tag{13}
\]

For F itself, (5) gives exactly H'(F)=A0H(F)-C. L912 proves
A0H(F)>0.0000159908498950>15/10^6, but the evaluated difference of
this stronger lower bound and U lies strictly between
-0.00002684963 and -0.00002684962. This is merely a negative lower
estimate for H'(F), not a negative upper estimate or a negative cut.
Together with C>=0 and L912's upper bound it leaves the sign unresolved.
No inference C>=15/10^6 follows from U>15/10^6.

Equations (3)-(5) and (13) retain meaningful partial information: all
exterior demands are paid, all fourteen reduced proper cuts pass, and
all finite cuts with a proper nonempty core intersection pass. Only the
full reduced core condition is missing for this particular construction.
Its failure to be certified stops the proposed sufficient closure at
the declared analytic test. Other parameters, higher mixed signs and
L030-L032/C032a remain independent unresolved gaps.

### Separate conceptual audit, 9 November 2026 — step172

The unchanged approved scope is
`drafts/literature/2026-11-09-monotone-reserve-reduction-audit.md`.
The audit reuses the inspected Csordas and Koperberg primary hypotheses
and essential proof cases cited above. It neither reproves their general
theorems nor imports positive definiteness from monotonicity. The exact
full kernel satisfies Csordas's smoothness, evenness, positivity,
strict logarithmic concavity and derivative-decay requirements. In
Theorem3.5 the range 0<s<t uses phi'<0 at the positive arguments t+s
and t-s after even reflection; s>t uses the decreasing logarithmic
derivative. These are the hypotheses needed for J_1, not a condition
on a finite theta head.

The source series has coefficients 2pi^2 n^4 exp(9v) and
-3pi n^2 exp(5v), with exp(-pi n^2 exp(4v)). Substituting v=u/2
and multiplying by four gives L019 exactly. In the marginal, the
Jacobian of (t,q) -> (u,v) is -1, and p^2=4t^2 cancels the two
factors 1/2 in Phi. The subsequent substitution t=2s contributes
4*2*4*4=128, and q/2 inside k becomes q/4 inside phi_C. This verifies
(2), including both transverse directions and the full smooth seam.
L898's polynomial-exponential domination supplies the total mass and
all changes of variables; no unexplained contour or limiting argument
enters the normalization.

For k>=2, subtracting a from the two endpoints of N_k gives exactly
the endpoints of P_k, with both intervals strictly positive. Reflection
maps N_k to N_(-k-1) and P_j to P_-j. Consequently the payer for k<=-3
is k+1, and the only shared core resources are -2 and 2. For arbitrary
finite S, each exterior demand in S contributes once to sum_(T(S)) e_j;
all other terms there are nonnegative. Subtracting the demand total
gives the first inequality of (4). The second follows from R'_j>=0,
not from the sign of any unproved cut. This argument includes arbitrary
disconnected sets and crossings at both boundaries. Absolute summability
follows from integral |cos(16q)|rho<=A0; no infinite flow theorem is
being inferred from finitely many numerical tests.

There are precisely fifteen nonempty subsets of F. Within the five
core resources, e_-2=D_-3, e_2=D_2, and every other e_j is zero. Thus
(5) deducts each shared capacity exactly once. Under the explicit full
reduced-cut condition the dummy demand is nonnegative. Subsets without
the dummy are covered by the assumed cuts; subsets containing it have
all five neighbors and mass at most the equal side total. This verifies
the sufficient direction of Koperberg Proposition4 with its exact
finite, nonnegative, equal-total premises. Removing dummy edges leaves
resource inequalities and demand equalities, so unused surplus is
allowed. No unknown total-transform sign is used to create the dummy.

For (6), the successive ratios after the n=2 term are bounded by
(1+1/n)^4 exp(-pi(2n+1)exp(2u))<=r on the entire u>=0 domain.
The bound therefore covers the infinite theta series. In (8), the
absolute-value formulas are valid in both regions t<=q/2 and t>=q/2.
For q<2t, e^(2t)>=e^q gives the displayed derivative bound, and
pi(E^2-1)-beta=pi((E-1)^2-2)+9/2>9/2-pi>0.
For q>2t the other derivative is at most -beta. Continuity of G
at the possible corner suffices to integrate these two inequalities;
no differentiability at that corner is assumed.

The half-line density includes a factor two. Its inner Gaussian
integral contributes
2*sqrt(pi)/(4*(4pi E)^(3/2))=1/(16pi E^(3/2)); multiplying by
exp(9Q/2) gives exp(3Q)/(16pi), as in (9). For the actual outer
region t=h+s, the exponent is 9Q/2+9s-D exp(2s), and
exp(2s)>=1+2s gives (10). The integrals of s^j exp(-lambda s)
for j=0,1,2 are j!/lambda^(j+1); expanding (h+s)^2 verifies all
three coefficients. Enlarging the inner integral does not replace
or omit the outer region. The sine primitive is
exp(-beta w)(-beta sin(16w)-16cos(16w))/(beta^2+256).
Its endpoints 0 and pi/16 give (12), with two boundary demands and
no factor A0. Thus the complete tails and all analytic regions are paid.

Reproduce the independent scalar/accounting replay with

```
python3 scripts/theta-marginal/audit_boundary_reserve_172.py
```

It reads the original certificate without changing it and imports only
L037's arithmetic helpers. At precision100 it independently assembles
every constant and bound, using reciprocals for exp(-3pi), exp(-5pi)
and exp(-beta a), the unsimplified Gaussian factor above, and the
factorial formula for the three outer moments. Every resulting interval
is contained in its saved precision70 interval; overlap alone is not
accepted. All eleven original verification claims and the failed
requirement flag are rechecked. The audited raw table in L905 is
expanded to all fourteen proper subsets, all fifteen neighbor unions
are generated, and the two charge indicators are checked separately.
Each proper reduced lower estimate still exceeds 196/10^6. This is
arithmetic on the existing enclosures, with no new integral evaluation.

All 70 checks pass. The complete constants, bounds, cut table, check
results and source hash are saved in
`scripts/theta-marginal/boundary-reserve-audit-172.json`. The complete
bound and cut fields were inspected, including U and the negative full
lower estimate. The higher precision verifies the same formula U; it
does not sharpen the analytic majorant. Decimal/exp and Python execution
remain trusted, as do the explicitly reused audited L905/L912 inputs.

The audit finds no error requiring a change to the conclusions or their
mathematical inputs. It validates a local known-method partial reduction,
not a stronger theorem or progress beyond the inspected general sources.
The failed 15/10^6 discriminator and the original stop remain intact.
In particular the negative estimate lower_bound(A0H(F))-U cannot sign
H'(F), and U>15/10^6 cannot be used as a lower bound for C. The full
reduced reserve, infinite feasibility, other parameters and mixed-sign
transfer remain open. No further reserve campaign is licensed here.

## Mathlib

Full matching theorem, associated-kernel shape, finite weighted-Hall
formalization, Gaussian integral support and interval implementation
coverage were not checked; availability is unknown, not asserted absent.
The mathematical inputs are the precise primary citations above and
the stated standard Gaussian integral. L037 retains its trusted
arithmetic qualifications. No formal proof or complete RH candidate is
claimed.
