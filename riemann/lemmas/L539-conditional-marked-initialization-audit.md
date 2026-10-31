# L539 — Conditional marked-family initialization audit

## Hypotheses

Use the Eisenstein ring, norms q, primary representatives, fixed excluded
prime set S, zero-extended sixth-power residue characters, and the exact
canonical coefficient class of L538. Assume all the arithmetic, support
and adjustable-uniformity contracts of L538 on every bounded canonical
class used below. In particular its bound is uniform over the allowed
fixed punctures, finite ray characters, product marks, label-only weights,
fixed normalized supports and finite smooth seminorms. It has polynomial
norm-twist height cost, with thresholds uniform in heights apart from
these explicit factors. No marked-moment conclusion is assumed.

Fix bounded nonnegative m,r,z_i, at most K_s disjoint prime lists
P_i outside S with q_p comparable to Z^(z_i), coefficients |a_i(p)|<=1
independent of the row u, and smooth compact annular tests W,W_i.
The full defining modulus of a fixed finite-order ray character nu has
prime support in S. Fix one common sign e in {1,-1}, using conjugation
with the original zeros when e=-1. Set

\[
\begin{split}
 \psi_u(n)&=\nu(n)\chi_n(u)^e,\\
 M_u&=Z^{-r/2}\sum_n\mu(n)\psi_u(n)W(q_n/Z^r),\\
 Q_u&=\prod_i Z^{-z_i/2}\sum_{p\in P_i}a_i(p)\psi_u(p)W_i(q_p/Z^{z_i}),
 \qquad z=\sum_i z_i.
\end{split}                                                    \tag{1}
\]

All ideal sums have the source exclusions and representatives. The empty
product is one. Assume fixed positive margins c_1,c_2 with

\[
 r+2z\le m-c_1,\qquad 2r+8z\le3m-c_2.                    \tag{2}
\]

The following **initial arithmetic and support contracts** are additional
inputs. Their proof and simultaneous validity are not certified here.
They do not assume initial common Fourier measures, canonical
admissibility, the energy loss, or (1)'s desired moment bound.

1. The primitive masked-Poisson formula `lem:masked-poisson`, fixed Gauss
   phase/ray expansion, CRT extraction and product-slot priority identities
   hold with the source's original zero extensions and representative
   conventions. Poisson is applied only on the genuine coprime conductor
   before formal extension. In particular the pre-Fourier formulas
   `eq:initial-formal-component`, `eq:initial-common-extraction` and
   `eq:initial-outer-arithmetic` give their stated arithmetic coefficients
   and original masks. Finite ray factors are genuine characters on a
   common fixed group whose modulus has support in S. There is no extra
   bounded residual column coefficient.
2. The principal diagonal and principal nonzero restoration have bounds
   O(Z^(m+epsilon_p)) for every fixed epsilon_p>0, with uniform finite
   seminorm and polynomial-height cost, including bounded nonempty
   negative formal column-length windows. The restoration uses the
   original mask and the primitive lemma at scale Z^m>=1.
3. Choose all current, fresh, larger and clipped normalized supports in
   fixed compact subsets of (0,infinity) before the final Z threshold,
   with uniformly bounded smooth seminorms. Full quotient/product supports
   are included, not just points satisfying the old factorization.
   With the centers used below, full supports give
   |log_Z q_c-D'|<=eta, |log_Z q_j-G|<=eta;
   C,d',s,h' have their individual eta bounds;
   fresh independent n and f have respectively 3eta and 2eta bounds.
   Fresh column supports lie in [a,b], 0<a<=b, b>=1. Every quotient t
   used has an original source witness C,d' on these fixed dyads.
4. For the structural outer set before positive row/label enlargement,
   the map to (t,f,k) defined below has nonzero weighted fibre at most
   C D_init(f) C_init(t), where
   D_init(f)=d_O(f)^(1+2K_s) and C_init(t)=d_O(t)^(2K_s).
   The projection T_Sigma consists of distinct structural quotients t,
   taken once over all rows and labels. Its count is at most
   C Z^(P_1+2eta+pi_count), and C_init(t)<=C Z^pi_fib there.
   Assigned overlap tuples have count O(Z^G) with their adjustable
   divisor allowance. All bounded coefficients, branch/dyad sums and
   losses, including squaring a triangle bound, admit a single aggregate
   pi_init with count and fibre allocations included once.
5. Raw nonfrequency factors in the genuine initial Poisson expansion
   obey the source bound B_crude,init specified below, independently of
   tail/Fourier orders. Local input exponents are adjustable uniformly
   over the fixed ranges and supports, before orders and Z are chosen.
   The raw tail is removed before formal extension or absolute Fourier
   integration. This arithmetic count and its uniformity remain inputs;
   only the application of the generic lattice-tail bound is checked.

## Conclusion

Under exactly these conditional inputs, for every epsilon>0,

\[
 \sum_{0<q_u\le C_{\rm row}Z^m}|M_u Q_u|^2
       \ll Z^{m+\epsilon},\qquad Z\ge2,                  \tag{3}
\]

for every fixed row-ball constant C_row. Constants have finite test
seminorm and polynomial norm-twist height dependence and are uniform in
the prime lists and bounded coefficients as in the hypotheses. Either
common sign, every slot subcollection, empty products, and a fixed finite
sum of whole products with a common nu within each product are included.
No positive lower slot length or mesh condition is added.

The initialization has zero additional Fourier scale exponent at every
fixed height order. Its canonical children have actual margins at least
c_*=min(c_1,c_2)/2 under the choices below. The retained energy exponent
is at most m+11eta+pi_init+epsilon_c; there is no additional tau_init
energy factor or second quotient/label count. Empty row/column components
and clipped nonempty formal windows are covered.

This is a conditional reproduction of the source's claimed initialization,
not a stronger moment theorem or an unconditional validation of the
external zero-free premise. Primitive arithmetic, its uniformity,
amplification and other later interfaces, import closure and actual-Xi
all-degree positivity remain open.

## Proof

Primary source: OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re(s)>7/8*, September 30, 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[pinned build/paper.tex](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
The exact statement is `lem:marked` (retrieval lines 8681–8730);
its complete initialization proof is 10953–11662. Stable labels below
identify the source claims. The generic logarithmic Fourier inversion,
weighted Fourier moment estimate and lattice-tail bound are imported from
`eq:inverse-log-fourier`, `eq:inverse-fourier-moment` and
`eq:inverse-raw-tail` (9500–9558), with the normalized radial kernel
input `lem:kernel-seminorms`. These are used with their explicit
fixed-support, smoothness, order and positivity conditions below.
L538 supplies the conditional canonical bound; `lem:marked` itself is
not an input. Reproduction tests this application because the manuscript
remains a qualified external premise. It does not claim originality.

### Overlap reduction and the first common measure

For a tuple of distinct slot primes let P be their product and set
j=(n,P). Fix which slots occur in j and then their actual tuple. Write
n=jn_0, P=jP_0, c=n_0P_0. Since both original factors are squarefree,
c is squarefree, (c,j)=1, and (n_0,P_0)=1. Conversely c and a surviving
tuple P_0|c uniquely recover n=j(c/P_0) with exactly this overlap.
The identities mu(n_0)=mu(c)mu(P_0) and
psi_u(n)psi_u(P)=psi_u(j)^2 psi_u(c) retain their zeros.
If I_0 is the surviving set, put

\[
 G=\sum_{i\notin I_0}z_i,\quad z_0=z-G,\quad
 D'=r+z-2G,\qquad Z^{-(r+z)/2}=Z^{-G}Z^{-D'/2}.           \tag{4}
\]

For y_j=q_j/Z^G, y_c=q_c/Z^D' and y_i=q_(p_i)/Z^(z_i),
the old test argument is y_j y_c/product_(i in I_0)y_i. This follows
by substituting n=jc/P_0 and D'+G-z_0=r. Thus the coefficient for
this assigned tuple is exactly its assigned scalar
mu(j) product_(i notin I_0)a_i(p_i)W_i(y_i), times

\[
 Z^{-G}\psi_u(j)^2 Z^{-D'/2}
 \sum_{\substack{c\ {\rm sf}\\(c,j)=1}}\mu(c)\psi_u(c)
 \sum_{P_0\mid c}\prod_{i\in I_0}\mu(p_i)a_i(p_i)W_i(y_i)
                 W\left(y_jy_c/\prod_{i\in I_0}y_i\right).       \tag{5}
\]

This verifies `eq:initial-overlap-polynomial` without adding or deleting
a coprimality constraint. Each assigned scalar is uniformly bounded by
the fixed tests. In the whole row Hilbert space multiplication by
psi_u(j)^2 is a contraction. Triangle inequality is taken over these
fixed tuples **before** squaring: Z^(-G) cancels their O(Z^G) count.
If the tuple count has a small divisor allowance, twice its exponent is
charged to pi_init. It is never charged again as an outer quotient count.
There are finitely many overlap subsets, even when a slot length is zero.

Let omega_c equal one on the full quotient support, and let larger
cutoffs Omega_c,Omega_i equal one on its full support and on the
surviving slot supports. For fixed j use the single ambient profile

\[
 H_{{\rm ov},j}(y_c,(y_i))=
 \Omega_c(y_c)\prod_i\Omega_i(y_i)
 W\left(y_jy_c/\prod_i y_i\right).                       \tag{6}
\]

The variables here are independent. On its fixed compact logarithmic box,
all Euler derivatives are bounded uniformly for y_j in the fixed product
interval. At each prescribed J, the imported Fourier moment estimate
applies with dimension d=1+|I_0| and integer 2m_0>J+d. It bounds
integral |Hhat_ov,j(upsilon)|(1+|upsilon|)^J by finitely many W
seminorms, uniformly in j and Z. Inversion of (6) converts (5) into one
integral of residual polynomials with test
omega_c(y)y^(i upsilon_c) and product slot coefficients
mu(p)a_i(p)W_i(y_i)y_i^(i upsilon_i). Their bounds are uniform over
prime choices, and their coefficients are independent of the row u;
dependence on the earlier mode is permitted. The cutoff omega_c and W_i
remain outside the transform. No measure depends on a surviving tuple.

For sign e=1, conjugate the entire residual polynomial, including nu,
mark and test; for e=-1 leave it unchanged. Both give a row norm of

\[
 R_0(u)=Z^{-D'/2}\sum_{c\ {\rm sf}}\mu(c)\nu_0(c)
 1_{(c,j)=1}\overline{\chi_c(u)}\mathfrak d_0(c)W_0(q_c/Z^{D'}).
                                                               \tag{7}
\]

The ray character retains its full defining modulus in S. D' is a
formal bounded length and need not be nonnegative. Empty supports give
zero. For I_0 empty the transform has dimension one and the same argument
applies. Once (7) has the polynomial-mode bound proved below, Minkowski
for the common measure (6) and its sufficiently high finite moment
justifies the row integral and the final overlap triangle.

### Genuine Poisson input, row mask and canonical coefficients

Majorize the original ball by a fixed nonnegative radial Schwartz test
Phi_init(q_u/Z^m); this adds only positive terms. Write the two columns
c_a=C z_a, with z_1,z_2 coprime and squarefree. By the retained arithmetic
contract the primitive row character has conductor z_1 z_2 and mask C.
Apply masked Poisson there, with d'|C, before any formal extension.
Let B,theta be the respective nonnegative centers of C,d', and put

\[
 P_1=B-\theta,\quad M_c=2D'-m-2P_1,\quad
 M_i=M_c+6\eta+\tau_i,\quad \kappa=m-2D'+P_1.             \tag{8}
\]

Here tau_i=tau_init. Actual divisibility and the full eta bounds imply
P_1>=-2eta. The actual conductor length differs from 2(D'-B) by
at most 4eta. If the genuine kernel ratio
Z^m q_(h')/(q_(d') q_(z_1 z_2)) is <=Z^tau_i, adding twice the actual
logarithm of q_(d') shows log_Z q_(d'h')<=M_i. Thus the complement
of the outer mask

\[
 B_i(h')=1_{0<q_{d'h'}\le Z^{M_i}}                       \tag{9}
\]

lies in the genuine ratio tail. The tail application is justified below
on this original sum. The full kernel remains inside (9); no sharp
column-dependent ratio cutoff enters a Fourier profile. If M_i<0 the
nonzero ball is empty. The principal diagonal and principal nonzero
restoration use contract 2, with Z^m>=1, also for negative D'. Bare h'
dyads come from one partition common to d'.

The contracted Gauss/ray identities orient each residual side as
A_*(z)=bar(alpha)(z) gamma_2(z) nu_*(z), with nu_* a genuine fixed ray
character. Insert the complete mutual-gcd identity in z_1,z_2, then
write z_a=s n_a. This formal extension agrees with the genuine coprime
sum; it asserts no primitive Poisson formula on noncoprime conductors.
The retained extraction gives, for (s,n)=1,

\[
 A_*(sn)\overline{\chi_{sn}(d')}\chi_{sn}(h')
 =A_*(s)\overline{\chi_s(d')}\chi_s(h')
       A_*(n)\chi_n(d'h')\chi_n(d's)^4.                  \tag{10}
\]

The CRT fourth power and all zeros in this arithmetic identity remain
contracts. Its common scalar squared is the indicator
\(1_{(s,h')=1}\), since (s,C)=1 and d'|C; its possible zero is retained.
The resulting outer weight has one mu(d'), one mu(s), one
fixed ray Fourier coefficient, B_i, and the masks
1_(C,j)=1, 1_(s,Cj)=1, 1_(s,h')=1. Keep them through Cauchy.
Put

\[
 t=C/d',\quad k=d'h',\quad f=d's,\qquad
 \rho_{t,j}(n)=1_{(n,\operatorname{rad}(tj))=1}.           \tag{11}
\]

The exclusions at C,s,j are now exactly supplied by rho_(t,j) and
chi_n(f)^4; the numerator zero at h' is in chi_n(k).
No character division is used at a zero. The source slot-priority
identity on t,d',s,n leaves assigned primes and their coefficients
outer. On each surviving p|n the avoidance of t,j is already enforced
by rho and avoidance of d',s by chi_n(f)^4. Thus the surviving mark
has its original lists and product coefficients, independent of k,f,
and an original subcollection of nominal cap z_0. There is no additional
b(n). The fixed puncture is rad(tj), independent of k,f; it is not
absorbed into a moving ray modulus.

### Clipping and exact six-coordinate separation

Let v>=0 be the s-center and H>=0 the bare h'-center. Define

\[
 N_c=D'-B-v,\quad V_i=\theta+v,\quad F_c=D'-P_1,\quad
 N_i=\max(0,N_c),\quad \delta=N_i-N_c,\quad F_i=F_c+\delta.
                                                               \tag{12}
\]

Only a nonzero retained row component invokes a child, hence M_i>=0.
If either full fresh column window is empty its polynomial vanishes.
Otherwise q_n>=1 and |log_Z q_n-N_c|<=3eta imply 0<=delta<=3eta.
For a negative-center window its upper endpoint gives Z^delta<=b;
for N_c>=0 the same follows from delta=0 and b>=1. Thus
omega_(n,a)(Z^delta y) has support in [a/b,b] and uniformly bounded
Euler derivatives. V_i>=0 and F_i=N_i+V_i. These facts concern the
full independent windows, including terms later added by positivity.

Set the six independent coordinates

\[
 (x_C,x_d,x_s,x_h,x_1,x_2)=
 (q_C/Z^B,q_{d'}/Z^\theta,q_s/Z^v,q_{h'}/Z^H,
                   q_{n_1}/Z^{N_c},q_{n_2}/Z^{N_c}).     \tag{13}
\]

The pre-Fourier root and kernel argument supplied by Poisson are

\[
\begin{split}
 \frac{Z^{m-D'}}{q_{d'}q_s\sqrt{q_{n_1}q_{n_2}}}
    &=Z^\kappa x_d^{-1}x_s^{-1}(x_1x_2)^{-1/2},\\
 \frac{Z^m q_{h'}}{q_{d'}q_s^2 q_{n_1}q_{n_2}}
    &=A\frac{x_h}{x_dx_s^2x_1x_2},\quad
 A=Z^{m+H-\theta-2(D'-B)}>0.                             \tag{14}
\end{split}
\]

Indeed the first central exponent is m-D'-theta-v-N_c=kappa;
the second is m+H-theta-2v-2N_c. The old test arguments are
x_C x_s x_a. With larger cutoffs equal to one on full current/fresh
supports, the common profile is

\[
\begin{split}
 H_{i,\Sigma,\upsilon}(x)={}&Z^{-3\eta}\prod_\alpha\Omega_\alpha(x_\alpha)
 x_d^{-1}x_s^{-1}(x_1x_2)^{-1/2}\\
 &\times W_0(x_Cx_sx_1)\overline{W_0(x_Cx_sx_2)}
 K_i\left(Ax_h/(x_dx_s^2x_1x_2)\right),\quad K_i=\mathcal F\Phi_{\rm init}.
\end{split}                                                    \tag{15}
\]

It is chosen for frozen j, sector Sigma, Z, tests and earlier mode
upsilon before current C,d',s,h', hence before t,k,f. All roots are
in this profile. The current four dyad cutoffs, row mask and label
cutoff stay outside inversion. The latter equals one on all original
f=d's products and has a fixed full support I_f.

For eps_1=1, eps_2=-1 define

\[
\begin{split}
 W_a^i(y)&=\omega_{n,a}(Z^\delta y)y^{\varepsilon_a i\xi_a},\\
 Q_{a,t}(k,f)&=\sum_{n\ {\rm sf}}A_*(n)\rho_{t,j}(n)
          \chi_n(k)\chi_n(f)^4\mathfrak d'_a(n)W_a^i(q_n/Z^{N_i}).
\end{split}                                                    \tag{16}
\]

In the original outer weight multiply the masks and arithmetic factors
following (10), the assigned slot product (conjugated on side two), the
four current cutoffs and label cutoff, by

\[
 x_C^{i\xi_C}x_d^{i\xi_d}x_s^{i\xi_s}x_h^{i\xi_h}
                     Z^{i\delta(\xi_1+\xi_2)}.           \tag{17}
\]

Call the result V_Sigma(omega;xi). On the outer set Omega_Sigma
of (C,d',s,h'; assigned primes), inversion yields exactly

\[
 T_\Sigma=Z^{\kappa+3\eta}(2\pi)^{-6}
 \int \widehat H_{i,\Sigma,\upsilon}(\xi)
       \sum_{\omega\in\Omega_\Sigma}V_\Sigma(\omega;\xi)
             Q_{1,t}(k,f)\overline{Q_{2,t}(k,f)}\,d\xi.   \tag{18}
\]

To check the modes, x_a=Z^delta(q_(n_a)/Z^N_i), and side two's
opposite exponent is conjugated. Thus (17) restores x_1^(i xi_1)
x_2^(i xi_2) as well as the four outer modes. Inversion restores the
old coupled windows, and (14) restores the root and kernel. The fresh
cutoffs equal one wherever the old windows are nonzero; extra independent
combinations cancel through those windows before any positive bound.
For each Z all pre-enlargement sums are finite. Absolute integrability
follows from the estimates next, justifying this termwise inversion.
Relations such as C=td' restrict evaluation points, not the density.

### Uniform Fourier bounds at every fixed order

The imported normalized radial Schwartz kernel bound applies to K_i
because Phi_init is fixed on R^2 and smooth. All fixed Euler derivatives
(x partial_x)^j K_i(x) are bounded for x>=0, covering both small and
large positive A. The monomial exponent vector in (15) is
(0,-1,-2,1,-1,-1); Euler differentiation of its kernel gives the
corresponding constant times (x partial_x)^j K_i at that monomial,
without an exterior power of A. Real inverse roots and cutoffs have
bounded Euler derivatives on the fixed box. Derivatives of W_0 cost
only fixed polynomials in upsilon. Therefore at every finite order J
there are finite orders L,b and a finite test-seminorm factor S_b such
that, by `eq:inverse-fourier-moment` with 2m_0>J+6,

\[
 \int|\widehat H_{i,\Sigma,\upsilon}(\xi)|(1+|\xi|)^Jd\xi
       \le C_J S_b(1+|\upsilon|)^L.                     \tag{19}
\]

We only use Z^(-3eta)<=1; its gain is not counted or squared elsewhere.
The overlap profile (6) has every fixed upsilon-moment with no scale
power. The clipped tests (16) have seminorm cost polynomial in xi and
uniform bounded real dilation. Original test norm twists contribute
finite polynomial height factors. Hence (19), followed by the required
moment of (6), controls all the orders requested by L538. There is zero
additional power of Z, independently of those finite orders. The fixed
supports, not merely eta-wide logarithmic estimates, are essential here.

### Positive fibres, a single quotient measure, and actual margins

Apply weighted Cauchy to the whole omega-sum in (18), before fixing t:
its absolute value is bounded by product_a(sum_omega |V||Q_a|^2)^(1/2).
Now use the arithmetic fibre contract. Its nonzero terms have squarefree
f=d's outside S, and reconstruct d'|f, s=f/d', C=td', h'=k/d'
when the last quotient is an element. The at most 2K_s assigned residual
primes divide tf. This explains which variables the retained fibre bound
counts; no second d',s,h' or overlap count is permitted.

On the distinct structural projection T_Sigma, use

\[
 d\nu_\Sigma(t)=Z^{-P_1-2\eta}\sum_{t\in T_\Sigma}C_{\rm init}(t)\delta_t,
 \qquad \|\nu_\Sigma\|\ll Z^{\pi_{\rm count}+\pi_{\rm fib}}.       \tag{20}
\]

This measure is fixed before current k,f and modes and is not replaced
by its containing count ball. D_init(f) stays inside the label average;
it is a fixed function of f alone, independent of Z and every other
averaged variable. Let

\[
 H_{a,t}=\sum_{\substack{f\ {\rm sf}\\q_f/Z^{V_i}\in I_f}}
 D_{\rm init}(f)\sum_{0<q_k\le Z^{M_i}}|Q_{a,t}(k,f)|^2
              =Z^{F_i}E_{a,t}.                          \tag{21}
\]

The equality follows from the two canonical normalizations Z^(-V_i)
and Z^(-N_i) in its squared column. With a larger fixed canonical row
ball it is an upper inequality. Positive enlargement changes only the
outer summation windows, keeping the same inner puncture and polynomial.
It need not reconstruct an original tuple. The fibre bound and (20) give

\[
 \left|\sum_\omega V Q_1\overline{Q_2}\right|
 \ll Z^{P_1+2\eta}\prod_{a=1}^2
           \left(\int H_{a,t}\,d\nu_\Sigma(t)\right)^{1/2}.      \tag{22}
\]

For every t choose its structural source witness, only to bound its
fixed puncture. Since log_Z q_t<=P_1+2eta and
log_Z q_j<=G+eta, its actual radical length satisfies

\[
 Q_i=\log_Z q_{\operatorname{rad}(tj)}\le P_1+G+3\eta.   \tag{23}
\]

This is valid for all added k,f because neither changes t or j. From
(4),(8),(12), direct substitution gives

\[
\begin{split}
 F_c-M_c-(P_1+G)-z_0&=m-r-2z+2G,\\
 4F_c-3M_c-6z_0&=3m-2r-8z+10G+2P_1.                   \tag{24}
\end{split}
\]

Use (2), G>=0, P_1>=-2eta, M_i=M_c+6eta+tau_i and
F_i=F_c+delta. The exact lower bounds are

\[
\begin{split}
 F_i-M_i-Q_i-z_0&\ge c_1+\delta-9\eta-\tau_i,\\
 4F_i-3M_i-6z_0&\ge c_2+4\delta-22\eta-3\tau_i.          \tag{25}
\end{split}
\]

The second 22eta consists of 18eta from the row enclosure and 4eta
from the possible negative 2P_1. Both clipping signs are favorable.
The canonical coefficient is exactly A_*(n), its fixed ray character,
rho_(t,j), chi_n(k)chi_n(f)^4, product mark and smooth test; no residual
coefficient or root was introduced. Thus all the L538 class conditions,
including the full defining ray modulus and label-only weight, hold
provided the margins (25) exceed its requested c_*.

### Energy restoration, parameter order and edge cases

L538 with loss epsilon_c and (21) gives
H_(a,t)<<C(upsilon,xi) Z^(2F_i+epsilon_c).
Consequently the two roots in (22) use one total mass (20), not its
square. With (18),(19), the exact exponent identity is

\[
 \kappa+P_1+2F_c=m.                                    \tag{26}
\]

Restoring the exterior factors, count, child normalization and canonical
bound gives

\[
 m+3\eta+2\eta+2\delta+\pi_{\rm init}+\epsilon_c
       \le m+11\eta+\pi_{\rm init}+\epsilon_c.           \tag{27}
\]

One delta comes from each of the two F_i occurrences in (21) and its
bound. The row enclosure is already inside E_(a,t) and paid in (25),
so it contributes no extra tau_i here. The outer overlap norm triangle
was already canceled by Z^(-G). Its allowed divisor/squaring loss and
all dyadic recombination costs are included once in pi_init. Polynomial
mode factors are integrated by (19) and then (6); Minkowski uses their
square roots for the row norm, controlled by increasing a finite order.
No quotient, witness, frequency or label mass remains outside (20)–(22).

Set bar_c=min(c_1,c_2), c_*=bar_c/2, epsilon_c=epsilon/2, and
D_max=r_max+z_max. The initial ranges are bounded independently of all
orders: M_i<=2D_max+10eta+tau_i, F_i<=D_max+5eta. Once
eta,tau_i<=1/100, the fixed bounds
M_max=2D_max+1, N_max=V_max=D_max+1 therefore suffice.
Choose L538's canonical schedule for these bounds and also impose

\[
 \eta,\tau_i\le\min(1/100,\bar c/100),\qquad
 \eta\le\epsilon/88,\qquad \pi_{\rm init}\le\epsilon/8.  \tag{28}
\]

One can decrease its eta and take tau_i equal to its sufficiently small
tau; every upper bound is positive. Equation (25) then gives at least
9bar_c/10 and 3bar_c/4, both exceeding c_*. Equation (27) is at most
m+3epsilon/4. The remaining slack accommodates a strict final exponent;
principal estimates may use epsilon_p<=epsilon/2. Empty sectors,
quotient projections or label sums contribute zero. M_i=0 is allowed.
A negative D' is handled by the original principal/tail contracts and
the same retained-component gates and clipping argument, without applying
L538 at a negative canonical length. No assumption of a nonempty mark
or a positive lower bound for its slot lengths has entered.

Choose the adjustable arithmetic exponents realizing pi_init after
these bounded ranges, but before orders. Contract 5 uses

\[
 B_{{\rm crude},i}=10[1+m_{\max}+(K_s+1)(D_{\max}+1)].     \tag{29}
\]

For completeness, the ratio in the original raw sum has
A_raw=Z^m/(q_(d')q_(z_1z_2))>0 and
A_raw^(-1)<=q_(c_1)q_(c_2)/q_C<<Z^(2D_max), since m>=0
and d'|C. That factor is already included in (29), not added again.
The imported tail bound holds for a>0, Y>=1 and order A_tail>1:
sum_(h nonzero, a q_h>Y)|K_i(aq_h)|<< (1+a^(-1))Y^(1-A_tail).
Use it with a=A_raw, Y=Z^tau_i and

\[
 T_i>1+B_{{\rm crude},i},\qquad
 A_{{\rm tail},i}>1+(B_{{\rm crude},i}+T_i)/\tau_i.        \tag{30}
\]

The complement of (9), already shown to be in this raw tail, has exponent
B_crude,i-tau_i(A_tail,i-1)<-T_i. It is discarded on the genuine
coprime sum, before formal extension and inversion. Its seminorm costs
are finite. No count at a retained frequency length is used for that
unbounded sum. The arithmetic validity of (29) is still a contract.

Take maxima of these and the canonical tail orders, then the finite
Fourier and smooth orders required for (19), L538 and the overlap
Minkowski integral. Increasing those orders changes constants and
seminorm requirements, not (25),(27),(28) or their scale losses.
Only then choose a common Z threshold enforcing every full initial and
canonical support ratio and contracted uniform threshold. These supports
include complete fresh windows and all clipped families. Later external
height cutoffs play no role. Bounded 2<=Z<Z_0 has uniformly bounded
original sums and is absorbed by the final constant, uniformly in the
bounded coefficients. Fixed finite sums of whole products follow from
row-space triangle inequality, squared once. This proves (3) under the
stated contracts and completes the initialization application audit.

## Mathlib

Full matching coverage has not been checked. Fourier inversion,
Cauchy–Schwarz, Minkowski and finite elementary inequalities are supporting
facts only; they do not verify the primitive arithmetic, uniformity or
this entire application. No absence or formal-verification claim is made.
