# L541 — Conditional terminal reflected-energy application audit

## Hypotheses

Work in the Eisenstein ring O=Z[omega], with ideal norm q, lambda above
3, and zero-extended sextic symbols chi. Primary representatives, units,
ramified valuations and source dual support have the conventions of the
pinned primary manuscript cited in the Proof. All sums exclude the zero
element or zero ideal. Fix its finite excluded set S, fixed finite ray
character, radical puncture r_rho and disjoint product-form prime slots.
Their number is bounded, and their coefficients, character and puncture
are independent of the element row k and squarefree good ideal f.
The defining character modulus is supported on S. Fix Z>=2 and bounded
log-length ranges. The norm windows have fixed compact logarithmic
supports and uniform seminorms at each requested finite order.

Use exactly `par:reflected-energy-data`, as follows. In the original
element row ball 0<q_k<=C_k Z^M split

\[
 (k)=k_{\rm pow}k_{\rm sup}R.
\]

The first factor contains all prime valuations at least two; k_sup is
the valuation-one part supported on S f r_rho; and R is the remaining
squarefree part. These supports are disjoint. Freeze the unit, the
actual first two ideals, and all nonresidual local choices. In particular
all nonresidual exponent-four primes are frozen, even when their labels
vary between invocations. Keep actual annuli
q_(k_pow) asymp Z^O and q_R asymp Z^H, with nonnegative centers and

\[
 q_{k_{\rm pow}}\ge Z^O/C_O,\qquad q_R\ge Z^H/C_H.       \tag{1}
\]

The upper annular constants are fixed as well. Fix separate classes of
R and the active slot product P modulo the full M_ref^2, with
M_ref=lambda^12 L^4 for the source's one fixed modulus L. The original
row restrictions are independent of P and the dual indices, except for
the explicit mask 1_(P,R)=1. Additional support restrictions on P or
the dual variables are fixed independently of the other moving indices.

Write F_act for the frozen active non-slot product, F_sm for its small
Ramanujan and active zero-mask factors, and N_F,B_F for its exponent-four
divisibility assignments. The assignment identity is

\[
 1_{p\mid n_0b_0^3}=1_{p\mid n_0}+1_{p\nmid n_0}1_{p\mid b_0},
 \qquad n_0=N_Fn,\quad b_0=B_Fb.                         \tag{2}
\]

Set A_0=log_Z q_(F_act), S_0=log_Z q_(F_sm),
N_0=log_Z q_(N_F), B_0=log_Z q_(B_F). These are actual nonnegative
log-norms, not freely enlarged centers. Let z_a be the sum of nominal
active slot lengths, so q_P/Z^z_a stays in a fixed compact interval.
The active list may be empty. Fix the dual unit and h>=-4, and use

\[
 \mu=u\lambda^hN_Fn(B_Fb)^3,\quad
 q_n\asymp Z^v,\quad q_b\asymp Z^{\ell_b},\quad
 e_\lambda=\log_Zq_{\lambda^h},\quad v,\ell_b\ge0.          \tag{3}
\]

The ideal n is squarefree; b is unrestricted. Both retain all allowed
source primes of S other than lambda. They may share primes with each
other, and b may share primes with N_F. Original zeros and all fixed
extraction restrictions are retained. Put X=Z^(N_*).

Retain the following **conditional primitive inputs** at their exact
source hypotheses, uniformly on these bounded ranges:

1. `prop:completed-reflection`, `cor:marked-reflection`, the algebraic
   identity `eq:unmarked-structural-block`, and the canonical dependence
   of the cusp coefficient and additive factor on h_0 and the active
   radical modulo M_ref^2. Retain the canonical cusp/finite Gauss and
   marked-branch inputs specified in L546, including its sigma,
   epsilon and omega formulas, all local factors and zero extensions.
   L546 derives `eq:reflection-cross-prime-phase`,
   `eq:reflection-pair-phase` and their coefficient separation under
   these inputs; those two phase identities are no longer independent
   premises here. L546 now uses L547 for the finite canonical cusp
   construction, which has passed independent critical review. The
   raw theta theory and finite Gauss bounds remain retained inputs.
   L548 now supplies fixed-arithmetic-data Mellin reflection, zero-term
   removal and entire/polynomial-strip continuation, conditional on
   L547 and the coefficient/Gauss inputs. Its independent analytic review
   has passed at fixed arithmetic data. L549 verifies the uniform
   transformed-test kernel seminorms, fixed logarithmic derivatives,
   one-variable annular Fourier norms and polynomial pure-twist cost.
   L550 now verifies the joint profile and common Bochner density; the
   concrete specialization below checks all moving norm coordinates.
   Marked expansion and broader arithmetic uniformity remain separate
   retained inputs.
   The source coefficient bound, in particular
   |d(mu)|/sqrt(q_mu)<=27 q_lambda^(4/3), is also retained uniformly.
2. `lem:hybrid-energy`, `old-eq:4.6b`: for K,N,B,L_1>=1, squarefree
   good rows R and squarefree good P, squarefree primary n (allowed
   S-primes retained), arbitrary primary b, q_R<=C K, q_n asymp N,
   q_b asymp B, q_P asymp L_1, and |a|,|beta|<=1,

   \[
   \begin{split}
   &\sum_R\left|\sum_P\frac{a(P)}{\sqrt{q_P}}1_{(P,R)=1}
       \sum_{n,b}\beta(n,b)\chi_R(nb)^3
                    \chi_P(n)^{-2}1_{(P,b)=1}\right|^2\\
   &\quad\ll_\delta(KNBL_1)^\delta
          (K+NB)B\{N+L_1+(NL_1)^{2/3}\}.               \tag{4}
   \end{split}
   \]

   Here a is independent of R,n,b, and beta of R,P. Fixed sectors
   and restrictions must preserve these independences. No arbitrary
   pair-dependent mask is allowed. The divisor reductions and sieve
   theorems behind (4) remain contracts.
3. Ideal counts # {a:q_a<=Y}<=C Y for Y>=1, divisor bounds
   d_O(a)<=C_delta q_a^delta hold uniformly. Inactive slot masses
   sum_(p in a fixed slot) q_p^(-1) have adjustable small-power bounds.
   Fixed-support dyadic partitions have bounded absolute overlap and
   finitely many labels on the bounded original row ranges. Their
   values and the other original windows are uniformly bounded.
   These inputs do not assume the desired energy estimate or a full
   raw-total bound. Standard local branch counts follow from the
   retained finite formulas and the divisor estimate.

L551 verifies `lem:lattice-kernel-tail` and its conditional original-row
application, using L549. L552 supplies the positive full original total
in L551 (2), including 1+(X/q_c^2)^(-1), under the same retained
coefficient and marked-reflection inputs. On upper ranges
q_k<=C Z^m, q_f<=C Z^v, q_rho<=C Z^q, total slot upper length z,
and X^(-1)<=Z^nu, it gives B_tail=m+z+(7/2)(m+v+q+z)+nu,
independent of kernel/Fourier orders. Independent replay of this total
and its substitution here has passed under L552's stated hypotheses.
Test seminorms and their
height costs stay outside B_tail. A per-row count alone does not
suffice. The joint profile
and its common-density norm consequence use L550 and the finite-block
specialization below.

## Conclusion

Define

\[
 \begin{split}
 T_d&=2H+2A_0+2z_a-N_*-N_0-3B_0,\\
 u_*&=\min\{v,z_a,(v+z_a)/3\},\qquad
 D=T_d-v-3\ell_b-e_\lambda,\\
 E_{\rm fix}&=\max(H,v+\ell_b)-S_0-B_0+z_a-u_*-\ell_b
                  -2e_\lambda/3-D_+/2,\\
 E_{\rm ref}&=O/2+E_{\rm fix}.                            \tag{5}
 \end{split}
\]

For the source's reflected linear row vector U, including its active
tuple sum and actual row cutoff, every retained dyad
v+3ell_b+e_lambda<=T_d+tau_ref, tau_ref>0, satisfies

\[
 \sum_R|U(R)|^2\ll_\epsilon Z^{E_{\rm fix}+\epsilon}.     \tag{6}
\]

The bound is uniform in the moving/frozen labels under the retained
inputs, with finitely many smooth seminorms and fixed polynomial
norm-twist height cost. Whole discarded dyads have arbitrary negative
power savings on the original sums. Bounded/unit dyads, empty supports,
empty slot lists and negative h down to -4 are included.

After summing frozen parts in one O-dyad and recombining the permitted
local choices the charge is **one** O/2 plus adjustable small losses.
Precisely, if E_fix<=E_* uniformly over the parts being summed, their
aggregate energy is O(Z^(O/2+E_*+epsilon)). One may take E_* to be
the supremum of their fixed-part exponents. When actual A_0,S_0,N_0,B_0
vary, a particular part's smaller exponent cannot bound the whole sum.
Thus the source shorthand O(Z^(E_ref+epsilon)) means a common exponent
bound or this supremum; it is not an additional uniformity assumption.

With q_f<=C_f Z^V and Q=log_Z q_(r_rho), the actual charges are

\[
 \begin{split}
 H&\le M-O+\frac{\log C_{\rm res}}{\log Z},
 &C_{\rm res}&=C_HC_kC_O,\\
 T_d-S_0-B_0&\le2M-O+Q+V-N_*+2z_a+
                    \frac{\log C_{\rm width}}{\log Z},
 &C_{\rm width}&=C_H^2C_SC_k^2C_OC_f .                  \tag{7}
 \end{split}
\]

Here C_S is the fixed excluded-prime factor from the structural data.
No equality H=M-O is asserted. This is a reproduction of the source's
terminal application under explicit smaller inputs. It can supply the
terminal interface of L538 under these inputs; L538 is not a premise.
Primitive arithmetic, other canonical contracts, full external import
closure and actual-Xi positivity remain unresolved.

## Proof

Primary citation: OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re(s)>7/8*, 30 September 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[pinned build/paper.tex](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
Stable locators are `par:reflected-energy-data`, `lem:reflected-energy`,
`old-eq:4.4`–`old-eq:4.7`, `eq:reflection-actual-annuli`,
`eq:actual-residual-row-dyad`, `eq:common-width-charge` and the primitive
labels in the Hypotheses. Retrieved passages were 7200–7581 (complete
terminal application), 6890–7030 (marked sectors, phases and zeros),
7054–7084 (exact hybrid statement), 2714–2866 (structural extraction),
and 2386–2469 (analytic inputs). The prior SPECIALIZE assessment reuses
the completed literature comparison. The terminal conclusion is not
imported: checking this particular implication is needed to reduce a
retained external-manuscript contract. No stronger bound or novelty is
claimed.

### Coefficients, collisions and separation

First delete primal marked collisions with the base local set: the
whole-index mark forces divisibility while the zero-extended local
factor vanishes, including exponent zero. No symbol is divided at a
zero. An inactive marked prime contributes q_p^(-1); triangle inequality
in the row Hilbert space and the inactive mass bound remove its sum at
an arbitrarily small power cost. Fix it before the remaining norm.
Its collision condition is now a fixed row restriction. Its own
branch conductor omits that prime; one does not use the active branch's
kernel scale for it. The bounded number of slot-pattern choices is
harmless. Product-form coefficients make these operations legitimate.

For each frozen branch, the structural coefficient normalization is

\[
 Z^{-v/2-\ell_b-e_\lambda/3-(S_0+B_0)/2}.                \tag{8}
\]

Indeed, the retained source factorization before extraction has
q_(lambda^h)^(-1/3) q_(N_F n)^(-1/2) q_(B_F b)^(-1), times a uniformly
bounded dual coefficient. A small Ramanujan or active zero-mask term
contributes q_p^(-1/2). An N_F divisibility term contributes q_p^(1/2)
and cancels its squarefree denominator; a B_F divisibility term cancels
only half of its cube denominator, leaving q_p^(-1/2). Equation (2)
extracts nothing from b when p is assigned to N_F, so every shared cube
power stays in b and in that same bounded dual coefficient. These facts
give (8) times the smooth normalized inverse roots. The active marked
product contributes q_P^(-1/2), retained inside the tuple sum. Its
per-tuple scale exponent is consequently
-v/2-ell_b-e_lambda/3-(S_0+B_0+z_a)/2.

By L546, the full separate sectors of R and P fix the class of F_act R P
and hence the common source coefficient and additive factor, without
imposing a coupled sector constraint. The conditionally audited pair-phase
identity gives, for residual exponent one and active-mark exponent zero, a cubic symbol
to exponent 1+0+2=3, hence one. Row-row interactions depend only on R,
slot-slot interactions only on the tuple, and interactions with frozen
primes only on one of these variables. The angular conductor scalar
separates by multiplicativity. Exponent-four base primes have been
frozen; allowing them to move would instead leave a nontrivial cubic
row-slot phase and would invalidate this application.

For x_F=u lambda^(h+4) N_F B_F^3, the remaining columns are

\[
 \begin{split}
 \chi_R(x_Fnb^3)^3&=\chi_R(x_F)^3\chi_R(nb)^3,\\
 \chi_P(x_Fnb^3)^{-2}
   &=\chi_P(x_F)^{-2}\chi_P(n)^{-2}1_{(P,b)=1}.          \tag{9}
 \end{split}
\]

On units these follow by reducing exponents modulo six; on nonunits
both sides have the same zero, so the equalities include every collision.
The factors at x_F are fixed row-only or tuple-only contractions. The
primal row-slot exclusion gives 1_(P,R)=1. The remaining frozen local
factors, source coefficient and extraction restrictions depend on (n,b)
alone. Thus a(tuple) is independent of R,n,b, and beta(n,b) of R,P.
Both are bounded after (8) and the stipulated small losses are extracted.
No (n,b)=1 condition or extra S-mask has entered. The separated a may
have lost product form; (4) requires only its boundedness and independence.
For disjoint labelled lists a product P determines its tuple uniquely;
any permitted representative multiplicity is at worst divisor-bounded
and tuple-only. Aggregation by P therefore preserves the hypothesis of
(4), after normalizing out any adjustable small loss.

### One profile, actual scales and discarded dyads

Let y_R=q_R/Z^H, y_n=q_n/Z^v, y_b=q_b/Z^ell_b and
y_i=q_(p_i)/Z^z_i. With the actual frozen products, norm multiplicativity
gives, even for overlapping N_F and b,

\[
 \begin{split}
 c&=c_F F_{\rm act}RP,\\
 \frac{q_\mu X}{q_c^2}
 &=Y y_n y_b^3 y_R^{-2}\prod_i y_i^{-2},\qquad
 Y=q_{c_F}^{-2}Z^{-D}.                                  \tag{10}
 \end{split}
\]

The finitely many c_F and all norm windows put the kernel argument
between C_ker^(-1) Z^(-D) and C_ker Z^(-D) on this product of actual
annuli. Every moving norm is a coordinate of one smooth profile W;
the row norm is not an external parameter of a row-specific measure.

L550 proves that for logarithmic dimension
d, compact box Omega, fixed monomial h(y), and F_Y=W V^sharp(Y h(y)),
the weighted Fourier L1 norm of order J is at most

\[
 C\min\{Y^{1/4},(1+Y)^{-A}\}
 p_{J+d+2}(W)\mathfrak M_{A,\lceil4A\rceil+J+d+4}(V).
                                                               \tag{11}
\]

Constants are independent of Y and actual labels, with exactly the
displayed cutoff and input norms. Here d=3+s for s active slots and
the monomial exponents, in coordinate order (R,n,b,p_1,...,p_s), are
(-2,1,3,-2,...,-2). Empty active lists have d=3, not dimension zero.
The finite range of possible s permits a maximum of the finitely many
constants; no unbounded-dimension assertion is needed.

To verify commonness rather than assume it, write the smooth norm part
after (8) as W. In particular its dual inverse-root factor is
y_n^(-1/2)y_b^(-1); the exact q_P^(-1/2) stays in the tuple coefficient.
All remaining normalized smooth norm windows are included in W.
Their log supports lie in one fixed compact box Omega containing the
original row, dual and individual slot annuli. Multiplication by those
inverse roots preserves smoothness and bounds each p_j(W) by finitely
many stipulated window seminorms, since y_n,y_b are bounded away from
zero in that box. If there are joint smooth windows they remain joint
factors of W; product factorization of W is unnecessary. Sharp row
cutoffs stay in the original row set I. Arithmetic masks and support
restrictions stay in the coefficients or domains. No derivative is
applied to a residue symbol or arithmetic indicator.

All frozen products occur in the scalar Y of (10), in the extracted
normalization, or in the already separated arithmetic coefficients.
They do not change W row by row. The window hypotheses provide uniform
finite seminorms even if the permitted window is selected by the block.
Without those hypotheses the dependence on p_j(W) cannot be suppressed.

Fix this block before inversion. The row set I is finite. Let T be
the full finite active-tuple support and C the full finite (n,b)
support in the fixed annular boxes, retaining every stipulated fixed
restriction. Their support sets are independent of R; the two moving
collision masks in (9) remain explicit. Keep these finite boxes when
removing the smooth windows by Fourier inversion: inversion does not
authorize an unrestricted infinite dual sum. For the empty active list,
T consists of the one empty tuple with P=1.

After the coefficient normalization already established in (8)–(9),
one component of U has the exact form

\[
 U(R)=s_d r(R)\sum_{\boldsymbol p\in T}
 \frac{a(\boldsymbol p)}{\sqrt{q_P}}1_{(P,R)=1}
 \sum_{(n,b)\in C}\beta(n,b)\chi_R(nb)^3\chi_P(n)^{-2}
                1_{(P,b)=1}F_Y(y_R,y_n,y_b,\boldsymbol y_p).
                                                               \tag{11a}
\]

Here s_d is the scalar (8), with its previously allowed fixed constants
and small losses extracted; r is a row-only contraction. The normalized
a and beta satisfy the bounds and independences proved above. This
display retains the coefficient/marked contracts used to obtain U;
it verifies their analytic use, not those raw identities anew.

For t=(t_R,t_n,t_b,t_1,...,t_s), define

\[
 \begin{split}
 r_t(R)&=r(R)y_R^{it_R},\\
 a_t(\boldsymbol p)&=a(\boldsymbol p)\prod_i y_i^{it_i},\\
 \beta_t(n,b)&=\beta(n,b)y_n^{it_n}y_b^{it_b},\\
 B_R(t)&=r_t(R)\sum_{\boldsymbol p\in T}
       \frac{a_t(\boldsymbol p)}{\sqrt{q_P}}1_{(P,R)=1}
       \sum_{(n,b)\in C}\beta_t(n,b)\chi_R(nb)^3
                         \chi_P(n)^{-2}1_{(P,b)=1}.
 \end{split}                                                   \tag{11b}
\]

All inserted norm powers have modulus one. In particular a_t is still
independent of R,n,b and beta_t of R,P. Separate slot frequencies do
not have to coincide: disjoint labelled lists make a tuple a function
of its product P, as already checked above. Any retained representative
multiplicity is tuple-only and has the same stipulated small cost.
The row-only factor can be removed from a norm upper bound. Collision
zeros, including unit and bounded cases, are unchanged.

This is a finite sum of continuous phase vectors in C^I, so it is
strongly measurable and bounded in norm for this block even before a
sieve estimate. L550 (7) applies to (11a) with its ONE joint density.
At A=0, m_0(Y)=min(Y^(1/4),1)<=C m for m=Z^(-D_+/4), because
Y=q_(c_F)^(-2)Z^(-D) and c_F belongs to a fixed finite set. Thus

\[
 U=\frac{s_dm}{(2\pi)^d}\int_{\mathbb R^d}
                       \widehat{F_Y/m}(t)B(t)\,dt,
 \qquad
 \|U\|_{\ell^2(I)}\le\frac{|s_d|m}{(2\pi)^d}
        \int|\widehat{F_Y/m}(t)|\|B(t)\|_{\ell^2(I)}\,dt.
                                                               \tag{11c}
\]

The integral is absolutely Bochner integrable by finite boundedness
of B and (11) at J=0. This integrability proof uses no prospective
uniform arithmetic estimate. Its density includes the row coordinate
and is common to the entire tuple/dual sum, rather than being chosen
separately for each row.

Only now enlarge I inside the positive norm to the permitted good
rows q_R<=C Z^H, extending (11b) with the same coefficients and phases.
The original row-only contraction can be extended by zero or discarded
in this upper bound. The retained hybrid input (4) then bounds B's
squared norm uniformly in t: all its arbitrary-coefficient hypotheses
still hold. Here its Fourier-height degree is zero, so J=0 in (11)
suffices and the cost is p_(d+2)(W) mathfrak M_(0,d+4)(V).
If a separately specified bound has degree H_t instead, J must be an
integer at least H_t, with the corresponding larger displayed orders.
An external pure twist of V costs (1+|u_0|)^(d+4) at J=0 by L549;
this cost and any window cost remain explicit, and are squared in an
energy bound. No kernel value on the added rows is compared with Y.
Squaring (11c) supplies m^2=Z^(-D_+/2) exactly once, as used below.

Before Fourier inversion remove the whole discarded dyads. If
log Z>=2 log C_ker/tau_ref, their actual argument exceeds
U=Z^(tau_ref/2). The source lattice-tail bound on lambda^(-4) O is

\[
 \sum_{0\ne\mu,\ a q_\mu>U}|K(aq_\mu)|
 \ll_A C_A(1+a^{-1})U^{1-A},\quad A>1,                  \tag{12}
\]

when |K(x)|<=C_A x^(-A) for x>=1; L549 (2) bounds the kernel constant
for V^sharp by a fixed multiple of mathfrak M_(A,ceil(4A)+2)(V).
L551 proves (12), including subunit disk counts and both convergent
geometric series. Apply it at a=X/q_c^2 on each original branch.
The actual-annulus comparison puts the union of whole discarded
supports in the strict tail a q_mu>U, including equality in the stated
log Z threshold. Before Fourier inversion, bounded absolute cutoff
overlap and L552's full raw TOTAL over original rows/tuples/branches
give, with b_A=ceil(4A)+2,

\[
 \|U_{\rm disc}\|_{\ell^2}\le\|U_{\rm disc}\|_{\ell^1}
 \ll_A \mathfrak M_{A,b_A}(V)
       Z^{B_{\rm tail}+(\tau_{\rm ref}/2)(1-A)}.       \tag{12a}
\]

For any D_tail>0, take A>1+2(B_tail+D_tail)/tau_ref to obtain
O(mathfrak M_(A,b_A)(V) Z^(-D_tail)). The squared energy has the
square of this bound. L551 gives the complete positive domination:
all nonzero indices of lambda^(-4)O are counted, retaining the original
masks until the absolute bound and allowing all stated shared primes.
No retained-length count or finite count of infinitely many dyads is
used. The coefficient/marked inputs remain contracts; L552 now fixes
B_tail before A. Independent replay verifies this substitution under
the stated finite-original-support and bounded-overlap hypotheses.
For an external pure twist x^(iu_0)V, L549 (5) makes the linear cost
(1+|u_0|)^b_A and the energy cost its square. These finite test norms
and their height growth are explicit, so no unrestricted height-uniform
saving is inferred. No row is enlarged for this discarded contribution.

### Fixed-part exponent and single aggregation charge

In (4) take K=Z^H, N=Z^v, B=Z^ell_b, L_1=Z^z_a; all are at least
one. The dual/tuple supports and masks just checked match (4), with
fixed annular constants. Its non-small exponent is

\[
 \max(H,v+\ell_b)+\ell_b+
             \max\{v,z_a,2(v+z_a)/3\}.                 \tag{13}
\]

The last maximum equals v+z_a-u_*, since subtracting the three terms
of u_* from v+z_a gives z_a,v,2(v+z_a)/3. Adding the exponent of the
square of (8), namely -v-2ell_b-2e_lambda/3-S_0-B_0, cancels v and
one ell_b. Adding -D_+/2 from the profile yields exactly E_fix in
(5). This proves (6). The O/2 term has not yet occurred.

To count powerful parts, every ideal with all positive valuations at
least two is uniquely x^2 y^3 with y squarefree: an even valuation goes
entirely into x^2, and an odd valuation at least three contributes one
factor to y^3. For norm at most C Z^O, ideal counting gives

\[
 \#\{k_{\rm pow}\}\le C'Z^{O/2}\sum_y q_y^{-3/2}
                    \ll Z^{O/2}.                      \tag{14}
\]

Convergence follows directly from the assumed O(Y) ideal count by
dyadic shells, whose contributions are O(2^(-j/2)). The supported
squarefree part divides rad(S f r_rho), so its count is Z^delta for
arbitrarily small delta on the bounded ranges, by the retained divisor
bound. Local choices have the same adjustable bound. At a given row,
Cauchy bounds the square of its local branch sum by the branch count
times the sum of branch squares. Sum this positive expression over
rows, then over their unique powerful/supported parts. The powerful
parts partition the rows; they are not another sum inside each row's
square. Thus (14) incurs O/2 only once. Inactive slot masses were
already removed by triangle inequality, and active tuples were already
inside (4); neither receives a further polynomial count here.

Apply (6) uniformly to each part. If its exponent is E_fix(part), the
positive outer sum is bounded using sup_part E_fix(part), or any
uniform upper bound E_*. This proves the aggregate assertion with its
stated qualification. A supremum does not require attainment. All
divisor, recombination and hybrid losses can be made smaller than a
prescribed epsilon: the number of operations and all log-lengths are
bounded, so choose their finitely many positive exponents after fixing
that epsilon. Powers of log Z from retained dyads are absorbed likewise.

### Actual row and width charges; empty cases

The inequalities q_k<=C_k Z^M, q_(k_pow)>=Z^O/C_O,
q_R>=Z^H/C_H and q_(k_sup)>=1 prove the first part of (7) by
multiplication. There is no need to enlarge H to M-O.

For the second part, the local weights in 2A_0-N_0-S_0-4B_0 are

| Active non-slot local case | Weight of log_Z q_p |
| --- | ---: |
| Odd exponent, or exponent two | 2 |
| Exponent zero, active | 1 |
| Exponent four, small term or assigned to n | 1 |
| Exponent four, assigned to b | -2 |
| Exponent zero, inactive | 0 |

These follow directly from membership in the four frozen products.
Outside S a residual prime contributes two through q_R^2. A row prime
of valuation e>=2 has available weight e>=2 in q_k^2/q_(k_pow);
a valuation-one row prime has available weight two. If a prime does
not divide k and occurs only in f, its exponent is four and every
weight above is at most one; if it occurs only in the puncture its
exponent is zero, also of weight at most one. Intersections with f or
the puncture increase the available weight. Thus every good-prime
valuation of the left side is bounded by that of the right side in

\[
 q_R^2 Z^{2A_0-N_0-S_0-4B_0}
 \le C_S(q_k^2/q_{k_{\rm pow}})q_fq_{r_\rho}.           \tag{15}
\]

Fixed excluded primes are accounted for by C_S. Substitution of the
actual support bounds in (1), q_k<=C_k Z^M, q_f<=C_f Z^V and
q_(r_rho)=Z^Q gives
2H+2A_0-N_0-S_0-4B_0<=2M-O+Q+V+log_Z C_width.
Adding 2z_a-N_* proves the second part of (7), with its stated constant.

For the empty active list P=1 and z_a=u_*=0. Equation (4) includes
this singleton and L_1=1; no positive slot length is needed. If a dual
or row support is empty its contribution is zero. Unit/bounded ranges
are admitted by the fixed annular constants. Since h>=-4,
e_lambda>=-4 log q_lambda/log Z. Fix eta>0 and take the threshold
so the two logarithmic errors in (7) are at most eta and e_lambda>=-eta.
On a retained empty-slot dyad the H-branch of E_ref-O/2 is at most
H+2eta/3; the (v+ell_b)-branch is at most
T_d-S_0-B_0+tau_ref+5eta/3, using
v<=T_d-3ell_b-e_lambda+tau_ref. The dropped terms are nonpositive.
Therefore

\[
 E_{\rm ref}\le O/2+\max\{H,T_d-S_0-B_0\}
                         +5\eta/3+\tau_{\rm ref}.      \tag{16}
\]

Equation (7), monotonicity of this maximum and adjustable small losses
recover the source empty-slot estimate, on one powerful O-dyad,

\[
 \sum_{0<q_k\le C_k Z^M}'|\mathcal T_1(Z^{N_*};k)|^2
 \ll Z^{O/2+\max\{M-O,2M-O+Q+V-N_*\}+\epsilon}.        \tag{17}
\]

The prime denotes that dyadic restriction. Retention, nonnegative v,
ell_b and h>=-4 bound the retained dual lengths and give only
logarithmically many ramified/dual annuli. Constants at endpoints are
kept until choosing eta; (17) never substitutes an exact H=M-O.

Finally choose raw counts first, then kernel and Fourier orders, then
the scale threshold. The logarithmic dimension is at most three plus
the fixed slot cap. Formula (11) supplies finite orders for every
weighted Fourier norm required by the separated estimate. Norm twists
on fixed supports cost a polynomial of fixed degree in their heights;
all label/height uniformities needed from arithmetic remain explicit
hypotheses. No extra scale exponent arises from the common Fourier
measure. This completes precisely the conditional terminal application.

## Mathlib

Full matching coverage was not checked. This file does not assert that
Mathlib contains the marked Eisenstein reflection, the masked hybrid
norm, or this terminal application. The cited analytic statements and
conditional arithmetic contracts are the inputs used here; generic
norm inequalities or Fourier lemmas alone would not cover the result.
