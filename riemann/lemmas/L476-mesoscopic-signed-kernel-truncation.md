# Lemma 476: mesoscopic truncation of the weighted signed zero kernel

## Hypotheses

Use the actual Xi function and multiplicity-preserving zero correspondence
of L018. In particular Xi is a nonzero real entire even function, and
every zero z=gamma+i delta has |delta|<1/2. Let nu_z denote its
multiplicity; sums below are over distinct zeros with this coefficient.
Use L471's normalization

    A(t)=(t^2+1/4) pi^(-1/4)|Gamma(1/4+it/2)|/2,
    Z(t)=-Xi(t)/A(t),
    D_1(Xi;t)=Xi'(t)^2-Xi(t)Xi''(t),
    N(T)=integral_T^(2T) (-D_1(Xi;t)/A(t)^2)_+ dt.

Here x_+=max(x,0), A(t)>0, T>=e and logarithms are natural.
Set L=log T and h=L^(-1/4). For real t in [T,2T] with Xi(t)!=0,
define the finite sum and its amplitude-weighted version by

    K_h(t)=sum_(|t-Re z|<=h) nu_z/(t-z)^2,
    W_h(t)=Xi(t)^2 K_h(t)/A(t)^2.

Select all zeros satisfying the closed cutoff, including all
multiplicities; thus every conjugate pair is selected together.
At each real Xi zero r in this interval define

    W_h(r)=Xi'(r)^2/A(r)^2.

Finally put N_h(T)=integral_T^(2T) (-W_h(t))_+ dt. No RH,
simplicity, spacing, density saving, short-interval count asymptotic,
external half-plane premise or differentiated-error estimate is assumed.

## Conclusion

The assigned value of W_h at each real zero is its continuous extension
there, for arbitrary multiplicity, even if another zero's cutoff
membership switches at that height. W_h is real, measurable and
integrable on [T,2T]. It need not be continuous at other cutoff switches.
Both integrals are finite, and there are absolute C and T_0 such that

    |N(T)-N_h(T)| <= C T(log T)^(5/2),  T>=T_0.             (1)

This is an approximation error o(T(log T)^3), not a bound of that size
for either N or N_h. The size and sign cancellation of the retained
local expression, individual-height signs, higher signs and RH remain
unresolved. This is a specialization of known product, shell-count and
zeroth-moment inputs, without a claim of progress beyond those sources.
The separate critical application audit in Section 5 finds no repair
necessary. It does not independently audit the imported source theorems
or improve the approximation error.

## Proof

### 1. Known inputs and their precise use

L471 Section 1 establishes, away from real zeros, the absolutely
convergent identity over all Xi zeros

    D_1(Xi;t)/Xi(t)^2=sum_z nu_z/(t-z)^2.                  (2)

Its cited input is George Csordas, *Fourier transforms of positive
definite kernels and the Riemann xi-Function*, arXiv:1309.0055v2,
Definition 1.1 and proof of Proposition 2.2, (2.3), printed pp. 3--4
([primary source](https://arxiv.org/html/1309.0055v2)). Only the identity
is used; the proposition's additional zero-free interval hypothesis
is not assumed. L471 justifies the actual-Xi product and convergence
application; no first reciprocal sum is split or differentiated here.

L467 gives, for the multiset Gamma of positive real parts of Xi zeros,

    # {gamma in Gamma: v<=gamma<=v+1} <=18 log(v+2), v>=0. (3)

It counts both zeros of each nonreal pair separately and every
multiplicity, with both endpoints included. This is its specialization
of Chiara Bellotti and Peng-Jie Wong, *Improved estimates for the
argument and zero-counting function of the Riemann zeta-function*,
arXiv:2412.15470v2 (7 July 2025), Theorem 1.1, printed p. 1, with
Section 5, printed pp. 23--24
([primary source](https://arxiv.org/pdf/2412.15470v2)). The source's
computations and full manuscript are not independently rerun here.
We use its unit-scale upper bound, never a count proportional to h.

L471 (8) at j=0 gives

    integral_T^(2T) Z(t)^2 dt=T log T+O(T).                (4)

Its source is H. M. Bui and R. R. Hall, *On the derivatives of Hardy's
function Z(t)*, arXiv:2304.05178v1 (11 April 2023), introduction,
definition of Z and (1)
([primary source](https://arxiv.org/html/2304.05178v1)). The derivative
orders used here are only (0,0); L471 already checks the exact Xi
completion normalization and dyadic specialization. These imports
are not reproved. L464 Section 3 is the earlier fixed-radius shell
implementation; the changed cutoff and weighted clipping are proved
below rather than asserted to be that result.

### 2. Uniform discarded-tail bound, including both ordinate tails

For t>=2 and any fixed 0<h<=1 put

    R_h(t)=sum_(|t-Re z|>h) nu_z/(t-z)^2.

Every summand satisfies

    |(t-z)^(-2)|=1/((t-gamma)^2+delta^2)
                <=1/(t-gamma)^2.                         (5)

First consider gamma>0. The discarded zeros with h<|t-gamma|<1
are covered by [t-1,t] and [t,t+1]. By (3) their total multiplicity
is at most 36 log(t+3). Their contribution to the absolute tail is
at most 36 h^(-2) log(t+3). If h=1 this set is empty and the bound
still holds. No separation between zeros is needed.

For every integer k>=1, the positive gamma with
k<=|t-gamma|<k+1 lie in the two intervals
[t+k,t+k+1] and [t-k-1,t-k], intersected with gamma>0.
Each nonempty intersection is contained in a closed unit interval
starting at v>=0 with v+2<=t+k+3: for the left interval take
v=max(0,t-k-1). Thus (3) bounds its total multiplicity by
36 log(t+k+3), and (5) bounds each weight by k^(-2).
The use of closed covering intervals may overcount endpoints and
can only enlarge the upper bound.

Write the finite absolute constants

    S_0=sum_(k>=1) 1/k^2,
    S_1=sum_(k>=1) log(k+3)/k^2.

Their convergence follows from the integral test. Since
t+k+3<=(t+2)(k+3), the positive-ordinate contribution is at most

    36 h^(-2)log(t+3)+36 S_0 log(t+2)+36 S_1.             (6)

By evenness in L018 the negative real parts are exactly -gamma
for gamma in Gamma, with the same multiplicities. All are discarded
when t>=2 and h<=1. Their weights are bounded by (t+gamma)^(-2).
For each k>=1, k<=t+gamma<k+1 gives a positive-gamma interval
contained in a unit interval starting at v=max(0,k-t), if nonempty.
Here v+2<=k+3, so (3) bounds its count by 18 log(k+3).
These shells cover all t+gamma>t; allowing every k>=1 yields the
upper bound 18 S_1 for the entire negative-ordinate tail, including
arbitrarily remote zeros. No height-dependent upper truncation occurs
in either tail.

For completeness no assertion about absence of zeros on Re z=0 is
needed. They lie in the compact segment Re z=0, |Im z|<=1/2.
Since Xi is nonzero entire their total multiplicity Q is a finite
absolute constant. They contribute at most Q/t^2 by (5).
Combining these bounds proves absolute convergence and

    |R_h(t)| <= sum_(|t-Re z|>h) nu_z/|t-z|^2
       <=36 h^(-2)log(t+3)+36 S_0 log(t+2)+54 S_1+Q/t^2
       <=C_0 h^(-2)log(t+2),  t>=2, 0<h<=1.              (7)

For example one valid absolute constant is
C_0=72+36 S_0+54 S_1/log 4+Q/(4 log 4): use
log(t+3)<=2 log(t+2), log(t+2)>=log 4 and h^(-2)>=1.
Only finiteness of C_0 is required; no numerical onset is claimed.

### 3. Central-zero extension, measurability and cutoff endpoints

Over the whole integration interval only zeros in the compact
rectangle T-h<=Re z<=2T+h, |Im z|<=1/2 can be retained. There
are finitely many, with finite multiplicities. For nonreal z the
corresponding weighted summand has no real pole; its membership
indicator is the Borel function 1_(|t-Re z|<=h). Conjugation preserves
both membership and multiplicity, so K_h and W_h are real wherever
originally defined.

Let r be a real zero of multiplicity nu>=1. Locally
Xi(t)=(t-r)^nu g(t), with g real analytic and g(r)!=0. The zero r
itself is retained throughout a neighborhood of r of radius less
than h. The other finitely many potentially retained zero terms have
bounded denominators on a sufficiently small real neighborhood of r;
shrink this neighborhood to avoid every other real zero in that
finite set. Their indicators may switch there but remain bounded.
Consequently on the punctured neighborhood

    W_h(t)=nu (t-r)^(2nu-2)g(t)^2/A(t)^2
             +Xi(t)^2 B(t)/A(t)^2,                       (8)

where B is bounded. The second term tends to zero even if a cutoff
switch occurs at r. The first tends to g(r)^2/A(r)^2 when nu=1
and to zero when nu>1. These values are exactly Xi'(r)^2/A(r)^2,
as assigned. Also D_1(Xi;r)=Xi'(r)^2, so full and truncated weighted
expressions agree at every central zero and their negative parts
there vanish.

Each real-pole summand multiplied by Xi^2 has an analytic removable
singularity. Thus W_h is a finite sum of bounded continuous factors
times interval indicators on [T,2T], with the extensions just checked.
It is measurable and bounded on this compact interval, hence
integrable. Only finitely many cutoff endpoints occur. Including
them does not change an integral; all tail estimates already allow
the chosen closed convention. Continuity across other switches is
neither assumed nor needed. The full D_1/A^2 is continuous and
integrable because A is positive and smooth.

### 4. Weighted clipping error and the achieved threshold

Away from real zeros, absolute convergence in (2) permits splitting
off the finite retained sum. Hence, with W=D_1(Xi;t)/A(t)^2,

    W(t)-W_h(t)=Z(t)^2 R_h(t).                            (9)

At each real zero both sides are zero by the preceding extension:
R_h is defined there and bounded by (7), since no retained real pole
appears in its discarded sum. Equation (9) therefore holds with the
assigned values everywhere. The real map x -> (-x)_+ is 1-Lipschitz,
so (7), followed by (4), gives

    |N(T)-N_h(T)|
       <=integral_T^(2T) |W(t)-W_h(t)| dt
       <=C_0 h^(-2)log(2T+2) integral_T^(2T) Z(t)^2 dt
       <=C T h^(-2)(log T)^2
        =C T(log T)^(5/2)

beyond an absolute onset. Here h=(log T)^(-1/4)<=1 and
log(2T+2)=O(log T). This proves (1). No infinite-sum/integral
interchange, signed-term cancellation, moment differentiation or
conditional first-power truncation is used. Dividing the error by
T(log T)^3 gives O((log T)^(-1/2)); the retained N_h has not been
shown to have any such saving.

### 5. Separate critical application audit, 29 October 2026

The invocation-start approval is
`drafts/literature/2026-10-29-l476-critical-audit-coverage.md`.
This audit checks the specialization (5)--(9), reusing L471's audited
product identity, exact A/Z normalization and zeroth moment, and L467's
audited closed unit-shell count. L018 supplies zero geometry and
symmetries. The primary source versions, theorem locations and retained
qualifications are those in Section 1; no new source input is needed.
L464's fixed-radius argument is comparison only. The following replay
finds no change to the hypotheses, conclusion, constants or proof.

For (5), taking the modulus of the reciprocal square gives exactly
1/((t-gamma)^2+delta^2), not the square of this expression. The
discarded condition |t-gamma|>h therefore gives the claimed h^(-2)
bound independently of delta. The two near intervals each have length
one and nonnegative starting point for t>=2. Their total count is at
most 36 log(t+3); no factor h in that count is available or used.

For the far positive shells, the right interval begins at t+k. A
nonempty left intersection is contained in
[max(0,t-k-1),max(0,t-k-1)+1], including the case crossing zero.
Both starting points obey v+2<=t+k+3. Half-open distance shells
partition the relevant zeros; the closed counting covers only add
possible endpoint overcounts. At h=1 the near shell is empty and
the far cover may also include retained distance-one zeros, which
only enlarges the bound. For negative real parts, evenness maps each
positive-real-part zero to its negative with the same order. The
interval k<=t+gamma<k+1 is covered by
[max(0,k-t),max(0,k-t)+1] when nonempty. Its start satisfies
v+2<=k+3. Thus the entire reflected tail, without a remote cutoff,
is bounded by 18 S_1. Both S_0 and S_1 converge. The finite set with
Re z=0 is disjoint from these two tails; compactness and isolation
justify Q<infinity with all orders counted. The constant is absolute
for the one fixed actual Xi function, without needing Q=0.

In (7), use h^(-2)>=1, log(t+2)>=log 4 and t^2>=4.
The four terms are bounded, respectively, by h^(-2)log(t+2)
times 72, 36 S_0, 54 S_1/log 4 and Q/(4 log 4).
This verifies the displayed C_0 uniformly in both t and h; no limit
in h or interchange of non-absolutely convergent series is involved.
Conjugation preserves the discarded condition as well as the retained
one, so R_h is real even at a real Xi zero, where its series has no
singular summand. All orders enter only as positive coefficients in
these absolute bounds.

For (8), fix T and its h>0 before taking t to a real zero r. The finite
compact-rectangle zero set contains every possible retained term on
[T,2T]. The term at r stays selected near r. After removing that one
distinct zero with its full order nu, all remaining denominators are
bounded away from zero in a sufficiently small neighborhood of r;
this includes any other real zero whose distance from r is exactly h.
Its cutoff can switch, but its denominator at r is nonzero. Thus B
in (8) is bounded on both sides of r without having to be continuous.
Multiplication by Xi(t)^2 kills every such switch in the limit. The
remaining term tends to g(r)^2/A(r)^2 for nu=1 and zero for nu>1,
exactly Xi'(r)^2/A(r)^2. The same statement holds with a one-sided
limit at an integration endpoint. No uniform spacing assumption is
hidden in this fixed-compact-set local argument.

Globally on [T,2T], extend each factor nu_z Xi(t)^2/(t-z)^2
at its possible real pole before multiplying by its closed interval
indicator and by A(t)^(-2). These finitely many continuous bounded
factors give precisely the assigned W_h, including at real zeros.
This proves boundedness and Borel measurability; continuity is claimed
only at real zeros, not at arbitrary indicator switches. A is positive
and smooth and has a positive minimum on this fixed compact interval.

For (9), away from real zeros the complementary closed/strict cutoff
conditions split the absolutely convergent identity exactly, also when
|t-Re z|=h. At a real zero the left side vanishes since
D_1(Xi;r)=Xi'(r)^2; the right side vanishes since Z(r)=0 and (7)
bounds R_h(r). This establishes the equality everywhere without taking
a limit of R_h across any cutoff switch. The negative-part map is
1-Lipschitz on the real line, so the integral error is at most
C_0 h^(-2)log(2T+2) times the nonnegative zeroth moment. L471 (8)
at j=0 gives T log T+O(T). With h^(-2)=(log T)^(1/2), the error is
O(T(log T)^(5/2)); divided by T(log T)^3 it is O((log T)^(-1/2)).
The order and the vanishing normalized error are therefore correct.
No estimate for N_h itself enters this calculation or follows from it.

The audit accepts the existing approximation input, without a new
bound, obstruction or progress beyond the known-tool specialization.
There is no infinite-sum/integral interchange, density or simplicity
assumption, external half-plane premise, differentiated remainder or
sign cancellation in this application. Individual heights, higher
signs and global mixed positivity remain independent unresolved gaps.

## Mathlib

Full matching coverage for this weighted clipped shrinking-window
statement is not checked. No formal proof is claimed. Supporting
facts are absolute convergence of reciprocal-square zero sums, finite
zero sets on compact sets, interval-indicator measurability and the
Lipschitz property of positive part; these are not a matching theorem
for the actual-Xi statement. Mathlib availability is unknown rather
than asserted absent. The primary citations and exact local
specializations above remain the mathematical inputs.
