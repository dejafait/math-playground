# L532 — Conditional uniform-margin selection: audit

## Hypotheses

Let beta_* be the supremum of {1/2} and the real parts in [1/2,1] of
zeros of primitive finite-order Hecke L-functions over Q(sqrt(-3)); poles
are excluded. Assume the source's earlier beta_*<=11/12 theorem, and the
contradiction beta_*>7/8. Set

\[
 \Delta=\beta_*-7/8\in(0,1/24],\quad \kappa=2\beta_*-1,
 \quad C(s)=s-11/16,
\]
\[
 h=13/16,\quad \ell=1/6,\quad l_x=17/48,\quad l_y=23/48,
 \quad d_{\min}=1/100,\quad \alpha=5/6.
\]

Here alpha is the row-bin endpoint, not a continuation abscissa.
Assume the following **unaudited arithmetic and analytic interfaces** of
the pinned manuscript cited in the proof. They are stronger than merely
having estimates separately for every fixed row or every fixed slot count.

1. After a fixed finite slot system and fixed arithmetic datum are chosen,
   the normalized functions J_eta and f_eta exist for all sufficiently
   large real Z and do not depend on the analysis cutoff T_1. The same
   nonzero scalar c_S A_T(Z) normalizes both sides. For every epsilon>0,
   the normalized low estimate is O_eta,epsilon(Z^(C(7/8)+epsilon)).
   For nonnegative nonzero smooth windows W_i and equal lengths ell/K,
   the normalizer has the asymptotic in part 3 below. Its reciprocal and
   the remaining fixed dyadic multiplicities cost arbitrarily small
   powers of Z. Adding fixed excluded primes changes thresholds only.
2. The normalized principal remainder is bounded by the sum of powers
   with exponents
   C(beta_*)+(1+h)e-m_w+epsilon_pr,
   C(beta_*)+e-m_z+epsilon_pr, and
   C(beta_*)+e-m_P+epsilon_pr, where
   m_w=23/960, m_z=13/9600 and any
   0<m_P<(7/8)min_i ell_i is allowed. This estimate already includes its
   normalizer loss. Its residue identities, local factor approximations
   and contour estimates are assumptions here.
3. For moderate rows U=Z^d, d_min<=d<=h+zeta, the original full dynamic-bin
   contribution is bounded by the supremum of the pointwise exponents
   C(7/8)+E(d), plus adjustable real losses and finite powers of 1+T_1.
   Empty bins contribute zero. For delta=2a-1 and 0<=q<=delta/2,
   the exponent supplied by `lem:high-bin` is

   \[
   E(d)=a-7/8+h(17/50-1/6)-a l_y-(1-a)\ell
       -(\delta/2-q)\ell+d(R+\delta/2-17/50).
   \]

   The bin ceiling is delta<=kappa<=alpha, except that the floor is
   delta=1/50 and uses R=1. For interior bins put x=q/delta and

   \[
   D_x=3-17x/9,\quad P_x=(2-8x/9)(1-x),
   \]
   \[
   R_{\rm short}(t)=1-\delta+\frac{\delta P_x}{D_x}(3/2-t),
   \qquad L(t)=1-\delta+(\alpha-\delta)(t-1).
   \]

   With available prime length strictly greater than 7/37, the count
   exponent is at most max(R_short(t),L(t))+Delta/4+epsilon_row for
   any t in [1,3/2]. The no-selected-prime estimate at t=1 is
   R<=1-2delta/3+epsilon_row without a supply condition. At delta=alpha,
   the separate no-slot amplified witness estimate is available:
   R<=e(r)-delta r+epsilon_row with e(r)=max(1,(1+5r)/6) and
   r>=1-O(epsilon_row), uniformly on the bounded witness range.
   This endpoint is not justified by the strict marked moment.
4. Small rows have relative exponent at most
   h(17/50-1/6)-l_y/2+2d_min+O(e+epsilon) relative to C(beta_*),
   with no height factor. For each fixed z_infinity>2 the absolute
   large-row sum, U>Z^(h+zeta), has exponent at most
   B_0+(h+zeta)(1+epsilon)-zeta z_infinity+epsilon,
   where B_0=l_x/2+1+l_y. These contracts include all nonprincipal
   physical rows, including the permitted principal-denominator cases.
5. Requested moment/count/capacity losses can be made arbitrarily small
   with exponent coefficients uniform in eta and the moving labels on
   the stated bounded real ranges. The moment mesh for `lem:plain`
   depends on those ranges and the requested loss, **not on slot count**,
   uniformly for kappa in [3/4,1]. The detector selection and rounding
   contracts have fixed positive width/supply margins; zero capacities
   use their no-slot estimates with O(capacity decrement) loss. These
   count losses are available before K is chosen. Other high-bin losses
   may have coefficients depending on a subsequently fixed K, and can
   then be reduced without requiring a new moment mesh. Positive
   amplitude width, e and preliminary powers can be chosen arbitrarily
   small subject to their positive fixed upper bounds. The internal
   amplifier pool has the source's fixed exponent separation from slots
   (mesh<sigma_width/6, pool exponent sigma_width/3). This pool assertion
   and the fourth-moment proof establishing the mesh are not audited.
6. For fixed eta and structural data, all retained internal profile and
   height orders are finite, uniform in moving rows, masks and frozen
   labels. Their product is dominated by (1+T_1)^A_eta, A_eta>=0.
   The discarded pieces have a common finite scale degree B_eta and,
   for every fixed integer N>=0, bounds O_eta,N(Z^B_eta T_1^(-N)).
   **A_eta and B_eta are independent of N and the later choice of tau.**
   Auxiliary external orders may be chosen after tau,N; changing them
   changes only seminorm constants and thresholds, not these degrees,
   internal orders, or real losses. A single fixed finite coordinate
   allocation includes the physical Im(z) coordinate. Each estimate
   holds at T_1=Z^tau once the detector height conditions hold and Z is
   large enough; its threshold may depend on eta,tau,N. The finitely many
   detector conditions are T_1<=U^(1/100) and
   (1+T_1)^A_j<=U^(epsilon_j/10), with positive epsilon_j fixed with
   the real choices. No internal moment is reapplied to an externally
   differentiated profile.

The hypotheses include the original common zero extensions, row masks,
fixed-ray coefficients, disjoint prime supports and inducing-character
exclusions of the moment/count interfaces. In particular, applying the
positive-slot plain moment requires induction outside its fixed group
Theta. Their arithmetic validity is not proved here. The fixed shared
Euler cutoff and its compatibility with later exclusions are also assumed;
neither construction nor nonvanishing of H_eta is established here.

## Conclusion

Under precisely these interfaces, the real choices can be made before eta,
including a fixed even K, so that

\[
 m=\frac14\min\left\{
       \min\left(\frac{51}{64}\Delta,\frac{63}{800}\right),
       \frac{23}{960},\frac{13}{9600},\frac7{96K}\right\}>0.
\]

For each eta there are tau_eta>0, an integer N_eta>=0 and a threshold
Z_0,eta such that

\[
 |J_\eta(Z)|\ll_\eta Z^{C(7/8)+\Delta/2},\qquad
 |J_\eta(Z)-f_\eta(Z)|\ll_\eta Z^{C(\beta_*)-m/2}
 \quad(Z\ge Z_{0,\eta}).
\]

**Audit verdict: conditional pass.** This reproduces the source's real-loss
and late-height argument. It supplies the exponent format needed downstream
by L531, but does not establish the input interfaces, H construction,
manuscript/import closure, Hecke-to-Dirichlet transfer, a new half-plane,
initial Xi signs or RH. No margin uniform as Delta tends to zero, or
uniform constants/thresholds in eta, is asserted. L531 is downstream context,
not a premise of this parameter calculation.

## Proof

Source: OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane
Re(s)>7/8*, September 30, 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[primary TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
The audited results are `prop:parameter-order` (rendered lines
15331–15576) and `lem:late-height-closure` (6129–6187). Relevant source
interfaces are `lem:plain` (11803–11894), `prop:detector-counts`
(14370–14405, with no-slot/zero-capacity and height cases through 14665),
`lem:principal-residue-interface`, the final principal normalization
(14715–14844), `lem:high-bin` (14858–14993), and all final row/frequency
cases (14994–15324). These are rendered retrieval coordinates; the labels
are the stable citations. Reproduction is justified by the external
input's unresolved parameter-uniformity qualification, not by novelty.

### 1. Balanced endpoint and the correct baseline

Substituting a=(1+delta)/2 into the assumed exponent gives exactly

\[
 E(d)=-1/48+2\delta/3+q/6-h(1-R)
          +(d-h)(R+\delta/2-17/50).                 \tag{1}
\]

For x in [0,1/2], D_x decreases from 3 to 37/18. Also
P_x=2-26x/9+8x^2/9 decreases from 2 to 7/9, since its derivative
(-26+16x)/9 is negative. Consequently

\[
 \mathcal J=(\alpha-\delta)D_x+\delta P_x
       \in[35/54,5/2]\quad(0\le\delta\le5/6).
\]

For interior delta set t=1+delta P_x/(2 J). Then 1<t<3/2, and
D_x(R_short(t)-L(t))=delta P_x/2-J(t-1)=0. Thus their common value is

\[
 R_*=1-\delta+\frac{(5/6-\delta)\delta P_x}{2\mathcal J}.
\]

Let E_* denote (1) at d=h, R=R_* and q=x delta. Put y=1/2-x and
v=51+41y. Direct substitution gives

\[
 -E_*={1+(3+8y)\delta\over48}
       -{13\over32}{(5/6-\delta)\delta P_x\over\mathcal J},
\]
\[
\begin{split}
 10368v\mathcal J(-E_*)={}&(3+5y)\{(4v\delta-79)^2+49\}\\
 &+4y\{4v\delta[(1+3y)(15+32y)\delta+9-13y]+265+3485y\}. \tag{2}
\end{split}
\]

For a check by coefficients, before multiplication by v the polynomial
on the left of (2) has coefficients in ascending powers of delta

\[
 10(37+34y),\quad -8(237+377y+26y^2),\quad
 48(51+131y+94y^2+32y^3).
\]

Expansion of the right side gives v times those same coefficients.
Every term in (2) is nonnegative: y,delta>=0 and 9-13y>=5/2.
Since v<=17(3+5y) and J<=5/2, division by positive denominators proves

\[
 -E_*\ge {49\over176256\mathcal J}\ge{49\over440640}>1/10000.
\]

The actual count adds Delta/4 and arbitrarily small row losses to R_*.
The coefficient of R at d=h is h. Since C(beta_*)-C(7/8)=Delta,

\[
 E_{\rm actual}(h)-\Delta
 \le-{49\over440640}-{51\over64}\Delta+\epsilon_{\rm total}. \tag{3}
\]

This checks the crucial subtraction. No claim E_actual(h)<0 is needed.
The uniformity of epsilon_total follows here from the assumed count and
loss interfaces, not merely from the positivity of the denominators.

### 2. Remaining endpoints and all row ranges

At the floor delta=1/50, R=1 and q<=delta/2 give
E(h)<=-1/48+3delta/4=-7/1200. At delta=alpha, the no-slot contract
gives R<=1-delta+O(epsilon): for r>=1 its exponent equals 1-delta;
for r<1 and r>=1-O(epsilon), 1-delta r<=1-delta+O(epsilon).
Inserting the ideal R=1-delta into (1) yields
E(h)<=-1/48-delta/16<0. This includes the live equality endpoint,
which occurs only when the bin ceiling allows it.

For 1/2<=d<=h, replace R by its permitted ideal upper value (R_*+Delta/4
in the interior, 1-delta at the upper endpoint, 1 at the floor).
This increases E because its R coefficient is d>0. Each resulting
frequency slope is positive: in the first two cases R>=1-delta implies
R+delta/2-17/50>=33/50-delta/2>=73/300>0; the floor is positive too.
Thus d=h bounds the whole interval. In the extension h<d<=h+zeta,
R_*<=1-delta+(alpha-delta)/2<=17/12 and
R_*+Delta/4<=137/96<139/96. Hence its slope is at most
139/96+1/2-17/50=3859/2400<2. The other cases have smaller slopes.
The extension costs at most 2 zeta; row-count losses remain in the
separate adjustable allowance since d<h+1/48<1.

For d_min<=d<=1/2 use no selected primes. The common upper exponent
R=76/75-2delta/3 dominates the ideal no-slot bound and equals 1 at the
floor. After q<=delta/2 is inserted, the slope is
101/150-delta/6>0, and substitution at d=1/2 gives

\[
 E(d)\le-529/2400+25\delta/96\le-49/14400<0.
\]

All these nonpositive ideal endpoint exponents acquire a saving at least
Delta when compared with C(beta_*); (3) gives the common smaller saving
m_hi=51Delta/64. This argument bounds every pointwise exponent uniformly,
so it bounds their supremum even when the sets vary with Z and the retained
tuple. It never integrates the individual pointwise pieces or declares
them holomorphic.

For small rows the assumed expression equals
-79/800+2/100=-63/800 before losses. For large rows B_0=53/32.
Fix any positive zeta and a small epsilon<1. The large-row exponent tends
to minus infinity as z_infinity tends to infinity, because its coefficient
is -zeta. Therefore choose z_infinity>2 making that exponent strictly
less than C(beta_*)-m_high, where m_high=min(m_hi,63/800).
The condition epsilon<z_infinity-1 then holds. Fixed equality boundaries
of row dyads can be assigned to either adjacent valid bound; the moderate
range includes both endpoints. These cases exhaust the contracted rows.

### 3. Real choices, mesh and five loss allocations

All choices in this paragraph may depend on fixed Delta>0 but precede eta.
Choose the count/moment/capacity losses with total high exponent cost below
m_high/8. This is possible by hypothesis 5. Obtain the positive moment
mesh and a positive rounding tolerance whose exponent cost is below
m_high/8. Both precede K. Choose a finite even K with

\[
 2\ell/K<\min(\eta_{\rm mesh},b_{\rm round},1/185),
 \qquad \ell_i=\ell/K.
\]

There is no circular refinement here precisely because the contracted
mesh is independent of K. Choose W_i nonnegative, smooth and nonzero
inside I_i=(1+(2i-1)/(2K+1),1+2i/(2K+1)). These intervals are contained
in (1,2) and pairwise separated by positive gaps. Equal scales
P=Z^(ell/K) preserve disjointness before masks or exclusions.

For selected rows d>=1/2, each base-U slot length satisfies
w_i=ell_i/d<=2ell/K<eta_mesh and delta max_i w_i<b_round.
Available length is ell/d>=8/39 for d<=h, whose excess over 7/37 is
23/1443. If 0<zeta<1/48, then ell/(h+zeta)>1/5; the remaining excess
over 7/37 is >2/185, more than twice the chosen maximum slot length.
The assumed selection/rounding interface therefore applies throughout.
Nominal versus actual annular lengths differ by O_K(1/log U); since
U>=Z^(1/2) here, the fixed strict margins absorb this uniformly by a
larger threshold. Likewise the assumed amplifier exponent gap implies
2 U^eta_mesh<U^(sigma_width/3)/2 eventually. No conductor-uniform
threshold is needed. Zero-capacity neighborhoods retain their no-slot
bounds and adjustable O(decrement) losses.

Write c_i=integral W_i(y)y^(-5/6)dy>0. The assumed ray-prime asymptotics
give S_i(Z)~P^(1/6)c_i/(|T|log P). Multiplying the fixed K factors and
using the normalizer (-1)^K Z^(-ell/6) product S_i yields

\[
 A_T(Z)\sim \left({K\over |T|\ell}\right)^K
                  \left(\prod_i c_i\right)(\log Z)^{-K}>0.
\]

Thus fixed finite exclusions and the finite number of windows affect
thresholds and constants, not an exponent margin. Set m_P=7/(96K),
which is half the admissible upper bound (7/8)ell/K=7/(48K).
Narrow windows can increase seminorm constants and finite orders; neither
requires m_P or K to be changed after eta.

After K is fixed, reduce the amplitude width, the remaining preliminary
powers and e so their high exponent cost is below m_high/8 and

\[
 (1+h)e+\epsilon_{\rm pr}<m_w/4,\qquad
 e+\epsilon_{\rm pr}<m_z/4,\qquad
 e+\epsilon_{\rm pr}<m_P/4.
\]

All right sides are positive. Intersecting finitely many such open upper
bounds, including e<10^(-3) and the contracted e_0>0, leaves positive
choices. K-dependent coefficients of these later losses are harmless;
K-dependent coefficients of an earlier required mesh would not be.
Next choose 0<zeta<min(1/48,m_high/16), so its cost 2zeta<m_high/8.
Choose the large-row line as in part 2 and the assumed shared Euler cutoff.
Additional target-dependent fixed exclusions are permitted by the contracted
compatibility statement; this audit does not prove that statement.

There are four high allocations so far: moment/capacity, rounding, later
real losses, and frequency extension. Each is <m_high/8. Spend one further
allowance <m_high/8 on the nonprincipal/outer normalizer and the remaining
fixed dyadic multiplicities. The surviving high margin is >3m_high/8.
The principal estimate includes its own normalization allowance and retains
>3/4 of each of m_w,m_z,m_P. Therefore the asserted quarter-minimum m
is strictly positive and no larger than every remaining margin. The
large-row bound had a strict saving >m_high before these later costs.
Finally the normalized low contract with epsilon=Delta/2 gives
omega=Delta/2, strictly between 0 and Delta.

### 4. Target-dependent heights and external orders

Fix eta only now. Choose its fixed datum and excluded set, and fix all
internal orders in hypothesis 6. Let A_eta dominate all retained height
powers and A_ht,eta dominate the detector orders, with A_ht,eta<=A_eta.
Let epsilon_ht be the positive minimum of their finite list of already
chosen detector allowances. Put

\[
 \tau_{0,\eta}={d_{\min}\epsilon_{\rm ht}\over20(A_{{\rm ht},\eta}+1)}.
\]

For 0<tau<=min(d_min/100,tau_0,eta), Z>=1 and U>=Z^d_min,
T_1=Z^tau<=U^(1/100), and

\[
 (1+T_1)^{A_{{\rm ht},\eta}}
 \le2^{A_{{\rm ht},\eta}}Z^{d_{\min}\epsilon_{\rm ht}/20}
 \le U^{\epsilon_{\rm ht}/10}
\]

eventually. The last inequality follows by absorbing the fixed factor
2^A_ht into the spare power Z^(d_min epsilon_ht/20). This includes
A_ht=0. It enforces each detector condition; the stated crude detector
error U^(-189/100+o(1)) T_1^2 is at most U^(-187/100+o(1)) and tends
to zero. Finite thresholds may now be enlarged for the fixed target.

The assumed uniform internal/external-order contracts, the bounds above
and finite summation give, for every fixed N and each admissible tau,

\[
 |J_\eta-f_\eta|\ll_{\eta,N,\tau}
 Z^{C(\beta_*)-m}(1+T_1)^{A_\eta}+Z^{B_\eta}T_1^{-N}.
\]

No independence of the implicit constants from tau is needed. Crucially,
A_eta, B_eta and tau_0,eta have been fixed before tau and N. Choose

\[
 0<\tau_\eta\le\min\{d_{\min}/100,\tau_{0,\eta},m/[4(A_\eta+1)]\}.
\]

Then the first term is O_eta(Z^(C(beta_*)-3m/4)). Choose any integer
N_eta>=0 strictly larger than
(B_eta-C(beta_*)+m/2)/tau_eta. Such an integer exists because tau_eta>0
and B_eta is finite. The second term has exponent <C(beta_*)-m/2.
After enlarging the threshold, their sum is O_eta(Z^(C(beta_*)-m/2)).
Since J_eta and f_eta do not depend on T_1, the estimate concerns the
same functions as the low bound. Thus omega=Delta/2 and sigma=m/2 are
common to all targets, although all subsequent choices can depend on eta.

If the internal orders or scale degree were allowed to increase with N,
this last selection would not follow. That independence is a substantive
remaining hypothesis, not something established by taking a sufficiently
large N. Similarly, the dynamic plain-moment hypothesis is satisfied by
beta_*=(1+kappa)/2 with kappa in (3/4,5/6]; this algebra does not assume
the desired beta_*<=7/8, but also does not audit the moment theorem.

### 5. Exact arithmetic evidence and limits

Run `python3 scripts/family003/uniform-margin-audit.py` from this notebook.
It expands both sides of (2) over exact rational coefficients, starting
from D_x, P_x, J and R_*, and checks the listed endpoint, supply and
margin constants. The complete certificate is
`scripts/family003/uniform-margin-certificate.json`. All polynomial
coefficients match, the residual is zero and all eight rational checks
pass. The complete identity object was inspected using
`python3 ../scripts/loop/inspect_json.py scripts/family003/uniform-margin-certificate.json --pointer /identity --full`.
This computation supports the identities; positivity on the full parameter
domain and quantifier order are proved above, not inferred from sampling.

No logical cycle or omitted endpoint remains within the stated contracts.
This conclusion is narrower than an audit of the source proposition with
all its upstream proofs: the bootstrap, moments, witnesses, row counts,
normalizer/local correction, global bounds and independence of external
orders remain assumed. No new result beyond the cited source is claimed.

## Mathlib

Full matching coverage for this conditional Hecke parameter-selection
argument and its arithmetic interfaces has not been checked. The exact
rational polynomial replay is a standalone Python certificate, not a Lean
proof. L531's previously cited Fourier-inversion theorem supports the
downstream analytic step only; it supplies none of these arithmetic or
uniformity contracts. No formal build or import-closure verification is
claimed.
