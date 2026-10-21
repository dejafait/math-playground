# L153 — Complete quartic residual: two universal scalars and three heat forms

## Hypotheses

Keep exactly L152's hypotheses, actual probes i=3,6, tau=1/16,
straight direction-1 lower-rooted forest and bare fixed-mesh coefficient
before refinement. In particular retain every force/vector degree
splitting, both insertion subtractions, all three colors and the full
interior prefix, including its constant axial mode. Use L008's compact
displacement u and w_mu=partial_mu u_mu,
s_mu nu=partial_mu u_nu+partial_nu u_mu. No affine-only restriction is
made. Let H_i be the color-diagonal exterior kernel in L152(6), and put

\[
 h_{i,\mu\eta}(x)=H_{i,\mu 1,\eta 1}(x,x),\qquad
 j_{i,\mu\eta;k}(x)=
  \partial_{x_k}H_{i,\mu 1,\eta 1}(x,y)|_{y=x}.             \tag{1}
\]

The color label 1 here selects one identical color copy, rather than
summing colors. Components mu,eta below are transverse: 2,3,4.
The derivative in (1) acts on the first argument alone. Set d=x_1+4.

For n in Z^3 define the infinite scalar Green kernel

\[
 G(n)=\int_{[-\pi,\pi]^3}
 \frac{e^{i n\cdot\theta}}{lambda(\theta)}
                  \frac{d\theta}{(2\pi)^3},\qquad
 \lambda(\theta)=\sum_{a=1}^3(2-2\cos\theta_a),
 \quad X=G(000)-G(110),\quad Y=G(110)-G(111).              \tag{2}
\]

The integral is absolutely convergent since lambda is comparable to
|theta|^2 near zero in dimension three. G(abc) denotes G(a,b,c);
cubic symmetry makes permutations and coordinate signs immaterial.
This is the scalar kernel of L114's phase-correct gradient projection,
not a new finite-box covariance approximation.

## Conclusion

Define the six full-probe heat forms

\[
\begin{aligned}
 T_{i,A}&=\int_D d u_1\sum_\mu j_{i,\mu\mu;1},&
 T_{i,B}&=\int_D u_1\sum_\mu h_{i,\mu\mu},\\
 T_{i,C}&=\int_D d\sum_r u_r j_{i,rr;r},&
 T_{i,D}&=\int_D d\sum_r u_r\sum_{\mu\ne r}j_{i,\mu\mu;r},\\
 T_{i,E}&=\int_D d\sum_{r\ne k}u_r j_{i,rk;k},&
 T_{i,F}&=\int_D d\sum_{r\ne k}u_r j_{i,kr;k}.
\end{aligned}                                                       \tag{3}
\]

All sums in (3) are transverse, and the unequal-index sums are ordered.
All integrals are ordinary real integrals over D. Then the **complete**
L152 limit is

\[
 \boxed{\Lambda_i=A T_{i,A}+B T_{i,B}+C T_{i,C}
                     +D T_{i,D}+E T_{i,E}+F T_{i,F}},       \tag{4}
\]

where

| Coefficient | Exact value |
| --- | --- |
| A | -8+60X-6Y |
| B | 10-42X+3Y |
| C | -4+60X+6Y |
| D | 3+24Y |
| E | 9/2-24X-12Y |
| F | -3/2+6X+3Y |

Equivalently, define

\[
\begin{aligned}
 T_{i,0}&=-8T_{i,A}+10T_{i,B}-4T_{i,C}+3T_{i,D}
                      +\tfrac92T_{i,E}-\tfrac32T_{i,F},\\
 T_{i,X}&=60T_{i,A}-42T_{i,B}+60T_{i,C}-24T_{i,E}+6T_{i,F},\\
 T_{i,Y}&=-6T_{i,A}+3T_{i,B}+6T_{i,C}+24T_{i,D}
                                      -12T_{i,E}+3T_{i,F}.
\end{aligned}
\]

Thus Lambda_i=T_(i,0)+X T_(i,X)+Y T_(i,Y). The universal coefficient
problem has been reduced to two scalar Green differences, and the
actual-probe problem to three combined heat forms per probe.
All these forms retain the full heat spectrum and converge absolutely.
**No value, sign or zero limit for either actual probe is established.**
No numerical quadrature is used here; the reduction does not compute
compensation with other response jets or any finer cutoff remainder.

## Proof

### 1. Contract ordered trace words with all colors and pairings

L149(4) expands each exponential word exactly. Restrict axial variables
to zero only after defining the full action force and generator, as
in L149(7). A remaining quartic trace monomial is
c Tr(Theta_a Theta_b Theta_c Theta_e), with rational coefficient c;
each index specifies a positive link, its position and its color.
Repeated link occurrences keep the same variable.

For t_c=i sigma_c/2, direct Pauli multiplication gives

\[
 \operatorname{Tr}(t_a t_b t_c t_e)
 =\frac{\delta_{ab}\delta_{ce}-\delta_{ac}\delta_{be}
                         +\delta_{ae}\delta_{bc}}8.        \tag{5}
\]

After selecting two exterior positions from the four, the internal
pair and exterior pair are separately color-diagonal. Their summed
color factor in (5) is 9/8 for the partitions (12)(34) and (14)(23),
and -3/8 for (13)(24). There are six exterior selections. For any
quartic polynomial q, its two-pair expectation has coefficient
6 K:H:P, where K is the symmetric fourth-derivative tensor of q.
L149's connected covariance uses 12 K:H:P. Consequently each exterior
selection in a trace monomial has weight **9/4 or -3/4**, respectively.
This includes the connected factor twelve and all three colors once.
It is valid for distinct or repeated links and does not assume
positivity of the exterior matrix.

### 2. Exact finite contraction, offsets and integration by parts

Here is an explicit rational procedure for computing the coefficient
table, including enough intermediate detail to reproduce it without
symbolically differentiating a large quartic.

For a central positive edge of direction nu put its tail at the origin
in lattice units. Construct all four ordered clovers at the tail and
head and all incident action plaquettes exactly as in L149(4)–(6).
For each rho!=nu and each endpoint epsilon=0,1, form the trace-word
polynomial

\[
 q_{\nu\rho\epsilon}
 =-2\sum_{m=1}^3\operatorname{Tr}
                    (G_{\nu,m}X_{\nu\rho\epsilon,4-m}),     \tag{6}
\]

with the endpoint factor 1/2 retained and the outside 1/a removed.
In X, set the selected endpoint displacement component to one, all
other endpoint components to zero. The head term has every term of
exp(Theta_e) C(head) exp(-Theta_e), including r+s+t=4-m, s>=1.
The tail term is just C(tail)/2. Expand using the composition formula
L149(4); discard only monomials containing a positive power of an axial
coordinate. Combine trace monomials by cyclic rotation, which preserves
their trace and the sum over all six exterior selections. No reversal
of a noncommuting word is used in this combination.

For a selected exterior pair a,b and internal pair c,e, let
mu_a,mu_b be the exterior component labels and let
h_a=x_a+e_(mu_a)/2-e_nu/2 be its midpoint offset, and similarly for b.
If v is the monomial coefficient times its weight from (5), enter
the following coefficients, each multiplying the internal projection
entry P(c,e):

| Contribution | Coefficient and placement |
| --- | --- |
| d partial_nu u_rho h_(mu_a mu_b) | v(epsilon-1/2) |
| d u_rho j_(mu_a mu_b;k) | v h_(a,k), for k=1,...,4 |
| d u_rho j_(mu_b mu_a;k) | v h_(b,k), for k=1,...,4 |
| u_rho h_(mu_a mu_b) | v(h_(c,1)+h_(e,1))/2 |

These are exactly F^1, H^1 and S in L152(8). In the first and last
rows use symmetry of the diagonal exterior h to order its components;
do not impose that symmetry on its separate derivative j.

Next expand both insertion subtractions in L149(7). For each plane
mu<nu, 4 Tr W_(p,4) contributes to the coefficient of
d partial_mu u_mu h and d partial_nu u_nu h. For every alpha and
m=1,2,3, 2 Tr(C_(mu alpha,m) C_(nu alpha,4-m)) contributes to
d partial_mu u_nu h and d partial_nu u_mu h. Contract their six
exterior choices with precisely the same weights (5). Both signs
are the signed subtraction signs already incorporated in L149(7).

At this stage every displacement-derivative contribution has the form
D_(r,k;mu eta) integral d(partial_k u_r)h_(mu eta). Since u is smooth
and compactly supported, integration by parts gives exactly

\[
 \int_D d(\partial_k u_r)h_{\mu\eta}
 =-\int_D d u_r(j_{\mu\eta;k}+j_{\eta\mu;k})
                -\delta_{k1}\int_D u_r h_{\mu\eta}.       \tag{7}
\]

Here H(x,y)=H(y,x)^T follows from its symmetric quadratic probe.
It implies partial_k h_(mu eta)=j_(mu eta;k)+j_(eta mu;k).
The second term in (7) retains the derivative of the lower-prefix
weight d. There is no boundary term because u has compact support.

### 3. Phase-correct projection entries and the complete table

For transverse positive-edge tails x,y, directions a,b and delta=y-x,
L114's multiplier t_a conjugate(t_b)/lambda gives the real covariance

\[
 P_{ab}(\delta)=G(\delta+e_b-e_a)-G(\delta-e_a)
                                  -G(\delta+e_b)+G(\delta). \tag{8}
\]

This uses the original tail phases. In particular no edge-center
phase is dropped. Under a signed coordinate permutation, reverse each
edge with negative direction sign by shifting its positive tail by
-e_(new direction); multiply its covariance by the two direction
signs. Translation invariance and exchange of the two edges complete
the symmetry reduction of (8).

Carrying out the finite entries of section 2 with these symmetries
leaves precisely the six placements in (3). The following complete
table gives their coefficients in scalar Green entries; an absent
entry is zero. The table includes (7), every central-edge direction,
both endpoints and both insertion subtractions.

| | G000 | G100 | G110 | G111 | G200 | G210 | G211 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | 18 | 6 | -24 | 0 | 6 | -6 | 0 |
| B | 9 | -3 | 0 | 0 | -9 | 3 | 0 |
| C | 42 | -6 | -48 | 0 | 6 | 6 | 0 |
| D | 15 | 6 | -9 | -12 | -3 | 6 | -3 |
| E | -3/2 | -3 | 9/2 | 6 | -9/2 | -3 | 3/2 |
| F | -3/2 | 0 | 3/2 | 0 | 3/2 | 0 | -3/2 |

For clarity, the finite table is verified exhaustively by the exact
rational script
`scripts/combined-ward-response/contract_quartic_residual_joint.py`.
Its `jet`, `force`, `clover` and `generator` routines implement precisely
the word compositions and placements above. `pairings` implements all
six exterior selections and (5); `projection_key` implements the signed
tail transformation; `green_coefficients` implements (8). The complete
post-(7) coefficient arrays, not selected previews, are saved in
`scripts/combined-ward-response/quartic-residual-joint-contraction-certificate.json`.
There are 57,696 nonzero collected force trace monomials over the 24
edge/displacement/endpoint placements, and 36,330 insertion monomials
with derivative labels. After symmetry reduction, all 201 separate
exterior-derivative rows and all 18 slope rows are reconstructed by
the six placements (3), with exact coefficient equality and no omitted
rows. The frozen force array is exactly zero, a consistency check with
L152 rather than a new argument for discarding first-order terms.

The finite computation involves integers and `Fraction` arithmetic
only. Its recurrence enumerates every weak composition of each word
degree; tensor differentiation, numerical Gaussian sampling and torus
quadrature are unnecessary. Separate matrix-series convolution on a
deterministic noncommuting link packet agrees with the word expansion
at all 24 force placements and all 16 insertion derivative placements;
all three Pauli color sums are checked separately. These packet checks
test the implementation and do not by themselves prove a polynomial
identity. The exhaustive rational recurrence and full array equality
supply the finite-table verification. Reproduce with
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/contract_quartic_residual_joint.py`.
Actual failures: zero; required failures: zero. There is no floating
rounding qualification for this algebraic table.

### 4. Reduce the seven Green entries and preserve every heat mode

From (2), multiplying by lambda proves Delta_inf G=delta_0 entrywise.
The Fourier numerator is bounded and integrable, so this entails no
application of an unbounded inverse to an arbitrary l2 vector. At
000,100,110,111 respectively, coordinate symmetries give

\[
\begin{aligned}
 G100&=G000-1/6,\\
 G200&=6G100-G000-4G110,\\
 G210&=3G110-G100-G111,\\
 G211&=2G111-G110.
\end{aligned}                                                       \tag{9}
\]

Substitute (9) into the full table. Its G000 dependence cancels when
G110=G000-X and G111=G000-X-Y; the coefficients are exactly those
in (4). The script checks this substitution by exact rational equality
for all six rows. This proves (4) and its equivalent three-form version.

L152 establishes absolute convergence of H and its first derivatives
uniformly on the compact insertion support. Multiplication by bounded
d and compact u, finitely many component selections and the integration
by parts (7) preserve that convergence. Thus all forms in (3), and the
three combined forms, retain every heat mode and the constant axial
prefix. None has been evaluated or bounded with a numerical sign
threshold. In particular a nonzero coefficient in the table does not
establish a nonzero Lambda_i: the actual six heat forms may cancel.

## Mathlib

Full matching theorem and supporting SU(2) word, relative-forest and
heat-series coverage: **not checked**; unknown is not absence. This
specialization uses the already-established L149 contraction and L152
limit, L114's projection convention and L008's precise strains.
The Pauli and discrete Green identities are elementary finite/Fourier
algebra, proved here to fix the signs and phases. No full renormalized
Ward result is reproved or imported as an isolated-jet estimate. The
unchanged approved source assessment supplies no exact matching result.
This is local reduction of an existing limit functional, without a
certified originality claim or a Yang–Mills resolution.
