# Marked-family initialization — completed source comparison

TARGET: Audit the marked-family initialization of family 003 lem:marked at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a using L538, checking slot-overlap normalization, canonical margins and common-measure uniformity while retaining the single-Poisson arithmetic estimates as contracts.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched the family003 assessments, audit notes and October 31 histories for initialization, overlap, residual-column weights and lem:marked; exact family003/initial-overlap-polynomial/inverse-initial searches in ATTEMPTS found no matching failure. Existing canonical/Fourier assessments explicitly exclude this interface. Web queries for "Quasi-Riemann" "marked" "initialization" and "canonical-moment" "marked" OpenAI located manuscript mirrors and review leads, not an inspected independent matching theorem. No novelty is inferred.
SOURCE_EVIDENCE: Read pinned primary TeX at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a: full marked definitions/statement 8681–8730; complete initialization proof 10953–11662, with all gaps between retrieval windows filled; canonical coefficient/mark conventions 6832–6872; full masked-Poisson statement/proof and principal restoration 9150–9214; logarithmic Fourier and raw-tail conventions 9495–9558. Compared L538's full hypotheses/conclusion and L537's exact class; reused ready L535/L536 Fourier and canonical-closure assessments.
COMPARISON: The source explicitly claims the marked moment and supplies a complete single-initialization mapping with normalization, margins, fibre/quotient measures and order choices. L538 conditionally closes the canonical family but excludes this application. A separate REPRODUCTION audit can test the source-claimed mapping into L538 while retaining primitive arithmetic and uniformity contracts; importing lem:marked would assume the interface being tested.
GAP: Independently audit the complete marked-to-canonical mapping, both common signs and all overlap/empty/clipped cases, one normalized quotient count and label mass, two positive actual margins, zero additional Fourier scale exponent and the final epsilon/order schedule. Source scope is ready; none of these application checks is declared passed by this literature review.
REASON: The essential complete marked statement and initialization proof were previously unread. Their source comparison now permits a bounded conditional application audit rather than another source-discovery turn. Reproduction is justified by the retained external premise's unresolved trust qualification, not by an originality claim; separate next-turn approval remains required.
SCOPE: Exactly lem:marked's single-Poisson initialization into L538, with the source's row-independent product slot coefficients, full fixed ray presentation supported on S, all zero extensions, original nominal slot caps, actual rad(tj) puncture, full independent windows and structural source quotients. Retain L538's arithmetic/support/uniformity contracts plus the explicitly listed initial arithmetic inputs below; do not assume the marked conclusion, the initial common-density conclusion or the final admissibility/energy calculation. Exclude proof of the primitive arithmetic estimates, amplification, other measures/full coordinates, auxiliary accounting, bootstrap, H, import closure and actual-Xi signs. No cross-notebook input.
LITERATURE_REASON: The ready canonical-closure assessment excludes initialization; the exact marked input, overlap separation, initial single-Poisson branches and closing application were essential unread sources for this unchanged target.

Primary source: OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re(s)>7/8*, September 30, 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[pinned build/paper.tex](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
Stable labels below identify the statements; retrieval line numbers are
locators only. The complete initialization passage, not a preview, was
read. Direct shell download failed DNS; web access succeeded throughout.
This is source comparison, with no new lemma or mathematical script.

## Exact marked input and claimed conclusion

`lem:marked` uses the Eisenstein ring O, the fixed excluded set S and
primary-ideal conventions of the source. The full zero-extended defining
modulus of the fixed finite-order ray character nu has prime support in
S. For one common sign e_chi in {1,-1}, it defines

    psi_u(n)=nu(n) chi_n(u)^(e_chi),
    M_u=Z^(-r/2) sum_n mu(n) psi_u(n) W(q_n/Z^r),
    Q_u=prod_i [Z^(-z_i/2) sum_(p in P_i)
                         a_i(p) psi_u(p) W_i(q_p/Z^z_i)],
    z=sum_i z_i.

There are boundedly many disjoint prime lists outside S, with fixed
annular q_p comparable to Z^z_i and bounded coefficients |a_i|<=1,
independent of the row u. The tests are smooth annular functions. The
parameters m,r,z_i are nonnegative in bounded ranges, and c_1,c_2>0
are fixed. The two hypotheses are

    r+2z<=m-c_1,       2r+8z<=3m-c_2.

The claimed conclusion is sum_(0<q_u<<Z^m)|M_u Q_u|^2<<Z^(m+epsilon)
for every epsilon>0. Constants may depend on the fixed arithmetic datum,
positive margins, ranges and finitely many test seminorms, uniformly in
prime supports and bounded coefficients. It includes either common sign,
slot subcollections, the empty product, and polynomial norm-twist height
cost, without a mesh or positive lower slot-length condition beyond
existence of the supports. A fixed finite sum of whole products is
allowed, each with a common nu in its inverse and all its slots.
These qualifications must not be weakened to pointwise divisor bounds.

## Overlap and initial Poisson cases now covered

The following are assertions and proof cases in the primary source,
not calculations established in this review.

At `eq:initial-overlap-polynomial`, freeze the subset of slot primes in
j=(n,P), with n=jn_0, P=jP_0 and c=n_0P_0 squarefree, prime to j.
The nominal lengths are G=sum_(assigned i) z_i, z_0=z-G and
D'=r+z-2G. The displayed normalization is
Z^(-(r+z)/2)=Z^(-G)Z^(-D'/2). The source counts O(Z^G) assigned tuples
and uses row-Hilbert-space triangle inequality before squaring; the
factor psi_u(j)^2 is a bounded row contraction including its zeros.
The residual puncture is 1_(c,j)=1. The tuple/c reconstruction, signs
mu(j),mu(P_0), and the fixed-j ordering are explicitly given.

The first profile is H_(ov,j)=Omega_c prod_i Omega_i times
W(y_j y_c/prod_i y_i). Its independent coordinates are the column and
surviving slot norms. The current column/slot cutoffs remain outside its
transform. Its single measure may depend on already frozen j, uniformly
for y_j in its fixed product interval, but not on a current tuple or row.
Surviving coefficients are mu(p)a_i(p)W_i(y_i)y_i^(i upsilon_i), bounded
and row independent. For sign +1 the whole residual polynomial,
including character, mark and test, is conjugated. The resulting
`eq:initial-residual-polynomial` has exactly mu(c)nu_0(c) bar(chi_c(u))
times the j puncture, product mark and smooth annular W_0. D' may be
negative on a bounded nonempty formal window; it is not yet canonical.

The square uses a fixed nonnegative radial Schwartz row majorant at
Z^m, c_i=Cz_i and the genuine coprime primitive character
bar(chi_(z_1))chi_(z_2), of modulus z_1 z_2, with residual mask C.
`lem:masked-poisson` requires a primitive finite character extended by
zero, any ideal mask R, a radial Schwartz test, self-dual measure and
K>0. Its full statement/proof retains the divisor of rad(R), including
its character zero; the principal convention m=1 includes h=0. Its
principal nonzero restoration bound is used only with K=Z^m>=1 here.
Ray restrictions are expanded into genuine characters and removed
local zero extensions remain masks. These arithmetic assertions remain
contracts, rather than a newly audited single-Poisson theorem.

For d'|C, centers B,theta and P_1=B-theta>=-2eta, the source uses

    M_c=2D'-m-2P_1,       M_init=M_c+6eta+tau_init,
    kappa_c=m-2D'+P_1.

The actual row mask is B_init(h')=1_(0<q_(d'h')<=Z^M_init), outside
the profile. Its complement is removed on the genuine coprime sum by
an actual-ratio raw tail before extension or Fourier absolute values.
M_init<0 has an empty nonzero row ball. The original principal diagonal
and principal restoration are separately bounded, also for negative D'.
The retained bare h' dyads use one partition common to d', not a
label-dependent partition. The exact formal component and finite-ray
orientation are at `eq:initial-formal-component`.

The complete mutual-gcd Mobius identity is inserted before bounds.
After z_a=sn_a, `eq:initial-common-extraction` keeps the CRT fourth power
and every common-prime zero. Set t=C/d', k=d'h', f=d's. The claimed
canonical coefficient is precisely bar(alpha)(n)gamma_2(n)nu_*(n),
chi_n(k)chi_n(f)^4, and rho_(t,j)(n)=1_(n,rad(tj))=1. No extra b(n)
is permitted. Slot priority on t,d',s,n is retained; surviving slots
are original subcollections of nominal cap z_0. Formal off-coprime
extension does not apply primitive Poisson to noncoprime conductors.

## Canonical mapping and common measures to audit

`eq:initial-canonical-lengths` and the nonempty/clipping passages give

    N_c=D'-B-v,       V_c=theta+v>=0,       F_c=D'-P_1,
    N_init=max(0,N_c), delta_init=N_init-N_c in [0,3eta],
    F_init=N_init+V_c.

The full fresh column and label windows are included before the final
scale threshold; their bounds are |log_Z q_n-N_c|<=3eta and
|log_Z q_f-V_c|<=2eta. Empty full column windows and empty retained row
balls are separate gates. Nonempty negative-center windows satisfy
1<=Z^delta_init<=b, b>=1, so the source uses rescaled smooth tests
omega_(n,a)(Z^delta_init y)y^(epsilon_a i xi_a), epsilon_1=1,
epsilon_2=-1. No real inverse roots appear a second time in those tests.

`eq:initial-joint-profile` uses the six independent coordinates
(x_C,x_d,x_s,x_h,x_1,x_2), full larger cutoffs and

    Z^(-3eta) x_d^(-1) x_s^(-1)(x_1 x_2)^(-1/2)
    W_0(x_C x_s x_1) bar(W_0(x_C x_s x_2))
    K_init(A_ker x_h/(x_d x_s^2 x_1 x_2)),
    K_init=Fourier(Phi_init), A_ker=Z^(m+H-theta-2(D'-B)).

Its exterior factor is Z^(kappa_c+3eta)(2pi)^(-6).
`eq:initial-outer-weight` retains both Mobius factors, one ray
coefficient, all outer masks including (s,h')=1, assigned coefficients
and priority masks, four current cutoffs, label cutoff and outer modes,
and Z^(i delta_init(xi_1+xi_2)). The exact complex identity
`eq:initial-separated-identity` precedes positive enlargement.
The transform is chosen before current C,d',s,h', hence before t,k,f;
it may depend on frozen j, sector, Z, tests and the earlier mode upsilon.

The source asserts every fixed xi-weighted Fourier moment is bounded by
a fixed polynomial in upsilon; the corresponding upsilon moment of the
overlap transform is bounded by a finite test seminorm, uniformly in
frozen j. Its generic `eq:inverse-fourier-moment` requires fixed compact
log boxes, 2m_0>J+d and Euler derivatives through order 2m_0. The uniform
Schwartz-kernel Euler bound is for every A_ker>0. Thus the proposed
additional Fourier scale exponent is zero, independently of the fixed
height orders. This is an audit threshold, not a pass inferred here.

For `eq:initial-fibre`, the displayed reconstruction uses d'|f,
s=f/d', C=td', h'=k/d', and assigned residual primes divide tf. The
precise retained fibre/count contracts are

    D_init(f)=d_O(f)^(1+2K_slot), C_init(t)=d_O(t)^(2K_slot),
    dnu_init=Z^(-P_1-2eta) sum_(t in T_Sigma) C_init(t) delta_t,
    ||nu_init|| << Z^(pi_count,init+pi_fib,init).

T_Sigma is the distinct structural quotient projection before positive
row/label additions, common to all current k,f. Each t has a source
witness on the C,d' dyads; the containing norm ball is only a count,
not a replacement canonical domain. The source's positive child H is
Z^F_init E, with D_init(f) inside the label average and the same row
ball. Weighted Cauchy is on the whole outer set before fixing t.
There is one Z^(P_1+2eta) count and one normalized quotient mass;
no second d',s,frequency, witness or label count is allowed.
D_init is a fixed function of f alone independent of Z and all other
averaged variables, as required by L538; C_init stays in the quotient
measure. Checking this application is distinct from reproving those
arithmetic fibre/count contracts.

## Source's margins, loss and order schedule

For each structural t, `old-eq:4.13` bounds the actual puncture length
Q_init<=P_1+G+3eta. This persists after positive additions because t,j
and the inner puncture remain fixed. The displayed actual margins in
`eq:inverse-initial-margins` are

    F_init-M_init-Q_init-z_0 >= c_1+delta_init-9eta-tau_init,
    4F_init-3M_init-6z_0 >= c_2+4delta_init-22eta-3tau_init.

The energy identity kappa_c+P_1+2F_c=m is explicitly stated. Together
with normalized children and the source measure, the asserted loss in
`eq:inverse-initial-energy` is at most

    11eta+pi_init+epsilon_c,

where pi_init aggregates overlap divisor, dyadic/separation, count and
fibre allocations once. The source claims no additional tau_init energy
factor: row enlargement is inside the child and already charged to its
margins. These exact identities and inequalities are future audit tasks.

The closing proof sets bar_c=min(c_1,c_2), c_*=bar_c/2,
epsilon_c=epsilon/2, D_max=r_max+z_max, and bounded canonical ranges
M_max=2D_max+1, N_max=V_max=D_max+1. It requires

    eta,tau_init<=min(1/100,bar_c/100),
    eta<=epsilon/88, pi_init<=epsilon/8,

in addition to the canonical schedule. It asserts margins at least
3bar_c/4>c_* and initial extra loss at most epsilon/4.
Initial subsidiary exponents are chosen before initial tail/Fourier
orders and before the final Z threshold. The separate initial crude
raw exponent is explicitly

    B_crude,init=10[1+m_max+(s_slot+1)(D_max+1)].

The source itemizes normalization, column, divisor, kernel scale, mark,
overlap and Poisson costs. With T_init>1+B_crude,init and
A_init>1+(B_crude,init+T_init)/tau_init, it invokes the raw-tail bound
sum_(a q_h>Y)|K(aq_h)|<<_A(1+a^(-1))Y^(1-A), Y>=1, A>1, a>0,
on the original lattice sum. It then takes larger finite Fourier orders
and finally enforces all full initial support ratios. These raw arithmetic
cost bounds and adjustable uniformity remain contracts. The generic
Fourier/raw-tail estimates are reused with these stated hypotheses;
their initial application and order dependence are the audit target.

## Decision, qualifications and continuation test

SPECIALIZE approves source scope for the exact unchanged TARGET only.
The source claims the entire estimate; this review does not derive it.
L538's conditional canonical conclusion is the allowed input, not the
parent marked conclusion. Retain its terminal/arithmetic/extraction,
support, witness, principal/tail, fibre/count and adjustable-uniformity
contracts for every required bounded canonical class. Additional initial
contracts are primitive masked-Poisson/Gauss/CRT extraction with original
zeros and ray conventions, slot priority, principal diagonal/restoration,
raw nonfrequency arithmetic bounds, fixed full supports, structural
source witnesses, and the explicit initial fibre/count bounds above.
Do not assume the initial common Fourier identity/mass application,
marked-to-canonical admissibility or final energy/margin loss as inputs
to their own audit. Full matching Mathlib coverage was not checked;
generic Fourier support is not a matching arithmetic theorem.

The targeted searches located the source's exact result and its own
references to Heath-Brown/Goldmakher–Louvel recursion; no separate
stronger theorem was inspected for this exact marked class. Mirrors and
the Math Referee panel were search leads only, not theorem evidence or
independently verified failures. Ready local assessments were reused;
no prior stop was reversed and no absence/novelty inference was made.

Continue with one exhaustive conditional application audit, including
empty marks, both signs, all overlap subsets, nonempty negative D' and
clipped N_c windows, empty rows/columns, fixed rad(tj), normalized
measures and finite orders. Narrow or stop on an uncovered branch,
residual bounded column coefficient, moving row-dependent puncture,
insufficient margin, missing source witness, non-common density or
height-order-dependent Z loss. Preserve L538 if the interface fails.
No central creative sign mechanism is justified by these inputs: the
actual-Xi sign bridge, alongside independent arithmetic/import closure,
remains absent. Newly completed ready coverage receives the separate
next-turn approval before dependent mathematics.
