# L538 — Conditional canonical finite-depth closure audit

## Hypotheses

Use the arithmetic datum and exact canonical coefficient class of L537,
including its inherited L535/L536 contracts. Fix bounded nonnegative
starting ranges for M,N,V,z_0, a slot cap K_s, c_*>0 and epsilon_c>0.
Write F=N+V and Q=log_Z q_(r_rho). At the starting node require

\[
 F-M-Q-z_0\ge c_*,\qquad 4F-3M-6z_0\ge c_* .                 \tag{1}
\]

The label f is squarefree outside S in a fixed full normalized annulus.
Its nonnegative weight w(f) depends on f alone, is independent of Z
and all other averaged variables, and satisfies w(f)<=C d_O(f)^C for
one fixed C. The column coefficient is exactly bar(alpha)(n) gamma_2(n)
times a genuine fixed finite ray character, the fixed radical puncture,
chi_n(k) chi_n(f)^4, the product mark and a smooth annular test W.
The full defining ray modulus has prime support in S. Slot lists are
disjoint, their coefficients are bounded independently of k,f, and every
subcollection keeps the original nominal cap z_0. There is no additional
residual coefficient b(n). The energy is

\[
 \mathcal E=Z^{-V}\sum_f w(f)\sum_{0<q_k\ll Z^M}
 \left|Z^{-N/2}\sum_{n\ {\rm sf}}
 \bar\alpha(n)\gamma_2(n)\nu(n)\rho(n)
 \chi_n(k)\chi_n(f)^4\mathfrak d(n)W(q_n/Z^N)\right|^2 .     \tag{2}
\]

The implied row-ball constant is fixed. The following remain explicit
**conditional arithmetic and support inputs**, uniformly over the bounded
ranges and all moving/frozen labels. They do not assume (2)'s desired
bound or a smaller-row estimate for the initial parent.

1. All extraction, Poisson, source-witness, support, fibre/count,
   principal and raw-tail contracts in L535–L537 hold for every permitted
   canonical node, with adjustable small exponents uniform on the fixed
   ranges. Tests have fixed normalized supports and uniform seminorm
   bounds at every requested finite order; arbitrary twists cost only
   fixed polynomials in their heights. Input thresholds are uniform in
   those heights and labels, apart from the displayed seminorm/height
   factors. These uniformities are essential, not consequences of a
   pointwise estimate at each individual node.
2. The primary source's `eq:marked-completion-inversion` and
   `eq:canonical-block` are valid with their original masks and product
   marks. The former uses weights mu(h) bar(alpha)(h)^3 Psi_k(h)^3/q_h
   and actual completed scale N_*=N-3 log_Z q_h. The factor Psi_k(h)^3
   has absolute value at most one. Its completed coefficients meet
   `par:reflected-energy-data` after fixing h,f and the row parts.
   Annular sum_(h) 1/q_h is uniformly bounded; slot assignments, label
   divisor mass and dyadic recombination admit the source's adjustable
   small losses. No coprimality of the remaining cube and column ideals
   is added. All raw-tail removal precedes formal extension and Fourier
   absolute values.
3. Assume the primitive structural/phase, hybrid-norm, coefficient/count
   contracts and analytic inputs of L541 for the terminal data here.
   Its conditional audit supplies the `lem:reflected-energy` interface,
   including original source dual ideals and allowed S primes. Use a
   common upper exponent when summing parts with different actual
   log-norms, as specified in L541. After fixing f, the puncture, the
   powerful row part and the supported valuation-one part, the actual
   residual-row dyad is kept.
   Row restrictions are independent of active slot and dual variables
   except the stated zero mask. Product slot coefficients and disjoint
   lists are required. Its nonnegative centers are O,H,v,ell_b; its
   actual non-slot log-norms A_0,S_0,N_0,B_0 are nonnegative. With the
   active nominal slot cap 0<=z_a<=z_0 and h_lambda>=-4, put

   \[
   \begin{split}
   T_d&=2H+2A_0+2z_a-N_*-N_0-3B_0,\\
   u&=\min\{v,z_a,(v+z_a)/3\},\\
   E_{\rm ref}&=O/2+\max(H,v+\ell_b)-S_0-B_0+z_a-u-\ell_b
        -2e_\lambda/3-(T_d-v-3\ell_b-e_\lambda)_+/2 .       \tag{3}
   \end{split}
   \]

   A retained dyad has v+3ell_b+e_lambda<=T_d+tau_ref. Its fixed-row-part
   energy is O(Z^(E_ref-O/2+epsilon)); summing those fixed parts and
   local choices gives O(Z^(E_ref+epsilon)), with uniform finite
   seminorm and polynomial-height cost. Whole discarded dyads have the
   stated raw-tail estimates. The actual row and width charges are

   \[
   H\le M-O+\frac{\log C_{\rm res}}{\log Z},\qquad
   T_d-S_0-B_0\le2M-O+Q+V-N_*+2z_a+
                              \frac{\log C_{\rm width}}{\log Z}. \tag{4}
   \]

   Constants depend on fixed supports, not moving rows. In particular
   H=M-O is not assumed. The already summed O/2 cost in (3) is never
   paid again. The aggregate terminal small loss pi_ref includes the
   reflected input exponent, weighted f-mass and all terminal
   assignment/recombination losses, each with its needed multiplicity.
4. The raw arithmetic count bounds B_crude,B_ref described in the source
   closing passage are finite uniformly on the bounded ranges, before
   selecting any tail or Fourier order. They include the raw exterior
   normalizations, coefficients and nonfrequency counts, but exclude
   the frequency kernel. For the reflected tail they bound the remaining
   factors after using the source bound on |d(mu)|/sqrt(q_mu); discarded
   dual indices are summed over the whole fixed lattice lambda^(-4) O,
   not counted at a retained dual length. Their arithmetic validity, and
   the local estimates' adjustable-exponent uniformity, remain contracts.

## Conclusion

For this exact conditional canonical class and every epsilon_c>0,

\[
 \mathcal E\ll Z^{F+\epsilon_c},                           \tag{5}
\]

uniformly over the stated data, with finitely many smooth seminorms and
fixed polynomial height cost. All internal orders can be chosen before
the final scale threshold and before any external height cutoff.

More precisely, the source's depth/parameter schedule gives terminal
retained contributions O(Z^(F-c_*/3)), before adding the already
controlled discarded tails, and total recursive loss at most
3 epsilon_c/4. Equality cases, empty supports, M=0 and the empty mark
are included. This audits the finite-depth implication under the listed
contracts. It is reproduction of a source-claimed conclusion, not a
new moment estimate. The arithmetic contracts, marked-family
initialization, other measures/orders, full-coordinate and later global
interfaces, manuscript/import closure and actual-Xi signs are not proved.

## Proof

Primary source: OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re(s)>7/8*, September 30, 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[build/paper.tex](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
Stable input locators are `par:reflected-energy-data`,
`lem:reflected-energy`, `eq:actual-residual-row-dyad`,
`eq:common-width-charge`, `lem:finite-seminorm-propagation`,
`cor:indexed-seminorm-propagation`, `eq:inverse-raw-tail`, and the proof
of `lem:canonical-moment`, especially `eq:inverse-parameter-order`.
Retrieval ranges: 7200–7339, 7518–7559, 8753–8994, 9230–9487,
9541–9558 and 10834–10952. The generic propagation theorem and raw
lattice-tail bound are imported at their stated hypotheses; they are
not reproved here. L535/L536 provide the already audited conditional
Fourier applications, and L537 provides the canonical nonterminal step.
L541 supplies the terminal application from its explicit primitive
contracts; no unconditional terminal arithmetic estimate is claimed.
The parent canonical theorem itself is not an input: importing it would
bypass this audit of its application and termination.

### Terminal specialization and all three exponent cases

At a node with positive margin c, assume V<d and an h-dyad center
ell_1<d. Freeze h in the completion identity. Assign its prime slots
by the exact priority identity. On the remaining slots the coefficient
is a_i(p)1_(p does not divide h); it is still bounded, on its original
list, independent of k,f, and in product form. Assigned-slot divisor
costs belong to pi_ref. Their deletion decreases the active nominal cap,
so z_a<=z_0 even for empty lists. Triangle inequality uses the joint
(f,k) Hilbert space with the nonnegative measure Z^(-V)w(f).
The factor Psi_k(h)^3 is a contraction and can be removed in this
upper bound; the annular sum of 1/q_h is O(1). Consequently it introduces
no active-slot-dependent residual-row restriction. Fixing f before the
reflected input respects that input's row/slot independence hypotheses.

Choose the final threshold so that, on the fixed full supports,

\[
 \widehat h=\log_Zq_h<d+\eta,\quad
 H\le M-O+\eta,\quad e_\lambda\ge-\eta,
\]

and the width error in (4) is at most eta. The completed N_* may be
negative; it stays in a fixed bounded range, which is what the reflected
contract requires. From Q<=F-M-z_0-c, N_*=N-3 h_hat and F=N+V,

\[
 \begin{split}
 T_d-S_0-B_0
 &\le M-O+2z_a-z_0-c+2V+3\widehat h+\eta\\
 &\le M-O+2z_a-z_0-c+5d+4\eta .                         \tag{6}
 \end{split}
\]

If the maximum in (3) is H, discard the nonpositive terms, use
e_lambda>=-eta and then (4). This gives

\[
 E_{\rm ref}\le M-O/2+z_a+5\eta/3
             \le F-c+5\eta/3.                           \tag{7}
\]

For the other maximum, v+ell_b, (3) is at most
O/2+v-S_0-B_0+z_a-u-2e_lambda/3. If u=z_a, the retained-dual
inequality v<=T_d+tau_ref-3ell_b-e_lambda gives

\[
 \begin{split}
 E_{\rm ref}&\le O/2+(T_d-S_0-B_0)+5\eta/3+\tau_{\rm ref}\\
 &\le M-O/2+2z_a-z_0-c+5d+17\eta/3+\tau_{\rm ref}\\
 &\le F-2c+5d+17\eta/3+\tau_{\rm ref}.                 \tag{8}
 \end{split}
\]

The last step uses 2z_a-z_0<=z_0 and M+z_0<=F-c.
If u is not equal to z_a, then u>=v/2: if the minimum is v this is
immediate; otherwise (v+z_a)/3<z_a implies v<2z_a, and that minimum
exceeds v/2. Ties with z_a were already included in (8). Therefore

\[
 \begin{split}
 E_{\rm ref}
 &\le O/2+v/2-S_0-B_0+z_a-2e_\lambda/3\\
 &\le O/2+(T_d-S_0-B_0)/2+z_a+7\eta/6+\tau_{\rm ref}/2\\
 &\le M/2+3z_0/2-c/2+5d/2+19\eta/6+\tau_{\rm ref}/2\\
 &\le F-M/4-3c/4+5d/2+19\eta/6+\tau_{\rm ref}/2 .       \tag{9}
 \end{split}
\]

In the second line we dropped -(S_0+B_0)/2 and -3ell_b/2;
the negative e_lambda term costs at most 7eta/6. The third uses (6)
and z_a<=z_0. The final line is exactly the second margin
4F-3M-6z_0>=c. Thus no unproved stronger width estimate entered.

Take c>=c_*/2, d<=c_*/200 and eta,tau_ref,pi_ref<=c_*/1000.
After adding the single aggregate pi_ref, the deficits below F in
(7),(8),(9) are at least, respectively,

\[
 \frac{373}{750}c_*,\qquad \frac{1451}{1500}c_*,\qquad
 \frac{2147}{6000}c_*+M/4 .                              \tag{10}
\]

All exceed c_*/3 since M>=0. These three cases exhaust the maximum
and minimum choices, including ties. For z_a=0 the u=z_a case applies.
The reflected estimate has already summed the fixed row parts. Summing
over f cancels its Z^V mass against the exterior Z^(-V); its divisor
exponent is part of pi_ref, not a second pi_ref. The same convention
includes the h-dyad and reflected-dyad recombination losses, including
the squaring of a triangle bound. This proves the asserted terminal
bound under the stated arithmetic contracts.

### Exhaustive partition and fixed class through the recursion

If V>=d, use the original canonical block with ell=0,b=1,r=N.
If V<d, the fixed h-dyad partition consists of ell_1<d, treated above,
and ell_1>=d. For the latter reopen the contracted completion and write
b=hh', with ell=ell_1+ell_2 and ell_2>=0. Its normalization is
Z^(-r-2ell-V), since r=N-3ell and
Z^(-N/2)q_b^(1/2) is a fixed annular multiple of Z^(-r/2-ell).
In both remaining cases ell+V>=d. Thus V=d and ell_1=d belong to the
recursive side. There is no discarded intermediate range.

All original cube masks and independent slot choices in the two copies
of a square stay in this partition. Common primes of b and n are
allowed. Its source extraction and finite dyadic assembly remain the
stated contracts, with assembly losses included in the single pi of
L537. No new coefficient class is introduced by treating the branches.
L537 proves that each retained nonempty child is canonical, has

\[
 0\le M'\le M-d,\quad N',V'\ge0,\quad F'\le F+11\eta,
 \quad\text{both child margins}\ge c-7\eta,               \tag{11}
\]

and a weight depending only on its new f with a fixed divisor bound.
Use the maximum of that fixed divisor exponent and the initial one
throughout the depth. The common fixed ray modulus can likewise be
chosen once, since extraction adds only the fixed source ray factors.
The slot cap never increases. Empty row/column/label sets contribute
zero. At M<d, (11) permits no nonempty child, but the principal and
tail terms still have L537's asserted bound; no positive M is assumed.

### Uniform ranges and the order of analytic choices

Let M_max,N_max,V_max,z_(0,max) bound the starting data. Choose

\[
 \begin{gathered}
 0<d\le c_*/200,\qquad
 D=\left\lceil(M_{\max}+2)/d\right\rceil+1,\\
 0<\eta\le\min\{d/16,c_*/(14D),\epsilon_c/(160D),c_*/1000,1/100\},\\
 0<\tau\le\min\{\epsilon_c/(4D),c_*/1000,1/100\},\qquad
 0<\pi\le\epsilon_c/(4D),\qquad
 0<\tau_{\rm ref},\pi_{\rm ref}\le c_*/1000 .             \tag{12}
 \end{gathered}
\]

Each upper bound is positive. One common tau serves the two Poisson
comparisons. For depth h the class to be estimated has

\[
 M\le M_{\max}-hd,\quad F\le N_{\max}+V_{\max}+11h\eta,
 \quad c_h=c_*-7h\eta .                                 \tag{13}
\]

These ranges are chosen before proving the estimates. Equations (11)
show that the child geometry maps this class into depth h+1 without
using any energy bound. Also Q<=F and z_0 is unchanged. Hence the
punctures and all child column/label lengths stay bounded.

Choose the full supports for all factorization types through depth D,
including quotient, product, larger, fresh and clipped supports, before
the Z threshold. Products and quotients of fixed positive endpoints
remain fixed positive endpoints. The clipped child family in L537
has Z^delta_N bounded by its fixed upper endpoint, with uniformly
bounded Euler derivatives. It can therefore be enclosed in one fixed
support at each type. There are finitely many types per passage and
finitely many passages; the number of actual ideals or dyad centers
need not be fixed. Uniform supports and derivative bounds, not an
enumeration of those ideals, give the finite support family I_D.

Set F_max=N_max+V_max+11D eta. The source's retained-length bound is
L_all=100(1+M_max+F_max+z_(0,max)+c_*). The arithmetic count contracts
are used on these bounded ranges. Nonempty original column windows
give r>=-eta and ell<=(F_max+eta)/3; extracted divisors are bounded by
their source products. The retained first frequency has the source
bound 7F_max+18eta+tau. For the terminal branch the row, f, puncture
and slot lengths bound its active conductor, and (4), the retained
dual inequality and N_*=N-3 h_hat give a finite dual bound. These
geometric bounds have no derivative or height order in them. The exact
arithmetic product/count bounds, including B_crude,B_ref, are retained
as contracts rather than claimed as separately audited here.

Choose all adjustable arithmetic exponents now, using L_pow=L_all
and the fixed maximum number of uses per passage. L537's allocation
<=pi/(2 J_step max(1,L_pow)) and the remaining pi/2 for logarithmic
factors gives one pi, including the assembly multiplicities. Use the
same convention for pi_ref. This is possible uniformly because the
contracts hold with arbitrary positive input exponents on the fixed
ranges. The allocation is independent of the subsequently requested
Fourier moments.

With nonnegative B_crude,B_ref fixed, select

\[
 T>1+B_{\rm crude}+B_{\rm ref},\quad
 A>1+(B_{\rm crude}+T)/\tau,\quad
 A_{\rm ref}>1+2(B_{\rm ref}+T)/\tau_{\rm ref}.             \tag{14}
\]

Import `eq:inverse-raw-tail` for a>0,Y>=1,A>1. Its application to
Y=Z^tau gives exponent B_crude-tau(A-1)<-T; on the reflected whole-dyad
tail, Y=Z^(tau_ref/2) gives B_ref-(tau_ref/2)(A_ref-1)<-T.
The second application uses the full fixed lattice lambda^(-4) O.
The contracted bound on its coefficient is uniform over discarded dual
indices. No retained-length count for those indices is used. These
choices establish the required tail saving from the raw contracts;
their finite seminorm and height costs are inputs to the next stage.
Original nonnegative canonical F is positive by its margin, so these
tails fit the terminal/edge allowances. They have already been removed
at the raw stage specified in the hypotheses.

For the internal finite-order propagation use the cited indexed
corollary, with normalized canonical quantity Z^(-F) E. L537's
normalization restores H_(a,gamma)=Z^(F_child) E_(a,gamma), so its
exponent identity has two F_child contributions: the normalization
and the target exponent. Its normalized one-passage defect, including
the contracted discrete mass, is at most

\[
 L=40\eta+\tau+\pi .                                    \tag{15}
\]

This is independent of every requested seminorm and height order.
The label measure is exactly L536's normalized distinct-triple measure.
Its weighted joint Fourier moments are bounded by finite parent
seminorms times Z^(pi_count+pi_fib) at every fixed pair of height orders.
That exponent is part of pi; the continuous Fourier loss is zero.
The density is common to current rows and labels. The current f,k
sums stay inside the child norm, not inside a second index measure.

Apply the indexed corollary to each positive Cauchy-side integral.
The geometric means are taken after those bounds, as in L537 (13).
Explicitly, for a fixed first side put
dmu(t,zeta)=|Fhat_1(t)| |Fhat_(2,t)(zeta)| dt dzeta and
B_a(t,zeta)=integral H_(a,gamma) dnu_sigma(gamma). Weighted Cauchy gives

\[
 \int (B_1B_2)^{1/2}\,d\mu
 \le\left(\int B_1\,d\mu\right)^{1/2}
      \left(\int B_2\,d\mu\right)^{1/2}.                 \tag{16}
\]

Each positive integral on the right uses exactly the joint measure
in L536 (18). The already selected child bound and that lemma's moment
bound establish its finiteness; alternatively use nonnegative truncated
integrals and monotone convergence. The outer first-side Cauchy then
takes another geometric mean, without identifying the two first-side
measures. This supplies precisely positive indexed integrals to which
the corollary applies.
Thus the two roots contribute one total discrete mass and one copy of
the exponent (15). No common product density for different positive
sides is postulated. Auxiliary positive-side quantities can be treated
as intermediate vertices in the source propagation theorem; there are
only a fixed finite number per canonical passage. The analytic order
propagation depth is therefore finite even though D counts canonical
passages, not every Cauchy operation. The net loss per passage remains
(15), already computed with the roots.

For every finite requested child order, L537's clipped profiles and
L535/L536's normalized kernels give finite parent seminorm requirements
and polynomial Fourier-height requirements with no scale exponent.
Each passage adds only finitely many height coordinates (the two
internal transforms have dimensions nine and six); the fixed depth
therefore bounds the total dimension. The maps on heights are fixed
coordinate selections and signed additions. The corollary's moment
order is the finite sum of the child polynomial orders weighted by
their Cauchy powers. Its all-fixed-order moment hypothesis is exactly
what L535/L536 provide. Starting above the terminal and raw-tail orders
in (14), take finite maxima backwards over the depths and types.
This gives finite J,B,H for the root without a height cutoff, without
Z-dependent orders and without changing (12) or (15).

Only now choose a common Z_0. It enforces the full-support logarithmic
bounds from I_D, the C_res,C_width errors in (4), the reflected kernel
support bound log Z>=2 log(C_ker)/tau_ref, e_lambda>=-eta from
log Z>=4 log(q_lambda)/eta, the fixed h-annulus bound, input thresholds
and all logarithmic-loss bounds. These are finitely many uniform
requirements. A larger finite order may increase Z_0 or a constant,
but not a scale exponent or an earlier support/range choice. Later
external height truncation is outside this construction. For bounded
2<=Z<Z_0, the original finite column, label and row sums have uniformly
bounded norm ranges; their divisor/character bounds and the supremum
of W increase only the final constant. Thus this range does not require
reusing the large-Z recursion.

### Backwards closure and edge cases

By (12), c_h>=c_*/2 for 0<=h<=D. For h<D,
c_h-7eta=c_(h+1)>0, precisely the strict condition needed in L537.
Moreover

\[
 M_{\max}-Dd\le-2-d<0 .                                \tag{17}
\]

There are no nonnegative row parameters in the depth-D class, so the
induction statement there is vacuous. This is not an assumed estimate
at M=0 or at a negative parameter.

Assume uniformly at depth h+1 that
E'<<Z^(F'+(D-h-1)L), with the finite profile/height dependence selected
above. Every possible smaller-row energy required by L537 lies in
that next class by (11)–(13). Its one-step bound is therefore
Z^(F+(D-h)L). The terminal terms satisfy (7)–(10); the first principal
term fits because M<F, and the second fits because
26eta+tau+pi<=L. Empty child families leave only these terms.
Finite type sums and the already budgeted dyadic assembly do not change
the exponent. This proves the assertion at depth h. All steps concern
the whole uniform next-depth class, not a choice of an estimate after
observing a particular child.

At h=0 the cumulative loss is

\[
 DL=40D\eta+D\tau+D\pi\le3\epsilon_c/4<\epsilon_c .       \tag{18}
\]

This proves (5). It uses the terminal arithmetic estimate and the
nonterminal arithmetic contracts, but never the parent canonical bound.
There is no RH-equivalent positivity input or conclusion. In particular,
the conditional audit cannot remove the notebook's external premise
or validate its later initialization and global applications.

## Mathlib

Full matching Mathlib coverage has not been checked. Finite backwards
induction, elementary inequalities, Cauchy–Schwarz and weighted integral
bounds are supporting facts only; they do not establish the arithmetic
contracts, their uniformity, or this application. No formal verification
or absence claim is made.
