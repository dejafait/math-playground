# L293 — Continuity of the normal-field planar surface response

## Hypotheses

Use exactly L292's SU(2) counting-measure relative half-space and slab,
with lattice spacing one, all normal links, pinned tangential links at
both end planes, and boundary-fixed gauge functions. Use L280's ambient
all-link Wilson tensors and complete density, on their own slice:
\[
 S=D-A/4+E/4,\quad A_{ij}=\sum_{kl}U_{ijkl}G_{kl},\quad
 E_{il}=\sum_{jkmn}T_{ijk}T_{lmn}G_{jm}G_{kn}.                 \tag{1}
\]
Keep every color and both Gaussian crossings. The Gaussian slab inverse
excludes exactly the three constant normal harmonic vectors. In
particular its normal mode at a nonzero tangential momentum is retained.

Let \(q\in\mathbb T^3\) be near zero and fix one unit color. The external
field \(u_q\) is \(e^{iq\cdot z}\) in that normal color at every depth,
and zero in tangential directions. Extend the real bilinear form
complex linearly and pair \(u_{-q}\) with \(u_q\). At periodic tangential
length \(\ell\), use a commensurate \(q_\ell\to q\) and set
\[
 Q_{M,\ell}(q_\ell)=\ell^{-3}u_{-q_\ell}^{T}S_{M,\ell}u_{q_\ell}.
                                                               \tag{2}
\]
Thickness \(M\geq2\) is even. Take \(\ell\to\infty\) before
\(M\to\infty\). All Fourier phases of raw edge slots remain in (1).
The full-lattice normal plane row at external momentum \(q\), denoted
\(b_\infty(q)\), is defined by the absolutely convergent row integrals
below. It is not assumed to vanish for nonzero \(q\).

L292's exact relative scalar kernels, its transverse construction and
its separately audited zero-momentum conclusion are inputs. L287(3),(13)
supply the complete differentiated cubic vertex and its normalization.
No external-curl term is replaced by L287's original-box remainder.

## Conclusion

The limits in the following definition exist and are independent of
the commensurate sequence in (2):
\[
 Q_M(q)=\lim_{\ell\to\infty}Q_{M,\ell}(q_\ell),\qquad
 \sigma(q)=\frac12\lim_{\substack{M\to\infty\\M\ {m even}}}
             \{Q_M(q)-M b_\infty(q)\}.                      \tag{3}
\]
The complete one-face response satisfies
\[
                         \lim_{q\to0}\sigma(q)=\sigma(0)=0. \tag{4}
\]
The proof gives absolute convergence of the half-space depth defect,
including both shifted soft regions, and a uniform integrable bound for
the slab-minus-bulk integrands. It retains all of \(D,-A/4,E/4\), in
particular the external-curl, internal-curl and mixed cubic pieces.

This is a local input toward tangentially varying normal-field
comparisons. It concerns the three groups selected by (1), not the
entire reflected coefficient. It gives no rate for the original box,
no control of depth-varying actual source fields, edges/corners or the
other groups, and no full-box \(o(N)\) error or higher perturbative
remainder. The even original mesh \(N\), \(a=8/N\), exact product
bump, both source orders and real source domain remain necessary for
any later use in the original coefficient. Interacting comparison,
continuum axioms, a nonzero physical sector and finite positive mass
are unresolved. The separate conceptual audit in section 6 accepts
(3)–(4) under the stated inputs and regulator order, without a stronger
rate or source-field transfer. No complete Yang–Mills candidate is claimed.

## Proof

### 1. Exact contractions and the two momenta

Write \(dp\) for normalized Haar measure on \(\mathbb T^3\), and put
\[
 d_j(p)=2\sin(p_j/2),\quad s(p)=\sum_jd_j(p)^2,\quad
 r=\kappa(p)=2\operatorname{arsinh}(\sqrt{s(p)}/2),\quad
 t=\kappa(p+q),\quad Q=\sqrt{s(q)}.                         \tag{5}
\]
The exceptional points \(p=0,-q\) are initially omitted. The function
\(\kappa\) is comparable to distance from zero on the torus and bounded
above by a fixed constant. The chordal triangle inequality gives
\[
                            Q\leq C(r+t).                  \tag{6}
\]
For example apply the Euclidean triangle inequality to the three
complex differences \(e^{iq_j}-1\), inserting \(e^{-ip_j}\), and
then use comparability of \(\sqrt{s}\) and \(\kappa\).

By L287, with the actual four signed slots of every plaquette,
\[
 DV(x)[u]=\mathsf A(u;x)+\mathsf B(u;x),\quad
 \mathsf A=\sum_P(Cu)_P\cdot\zeta_P(x),\quad
 \mathsf B=\sum_P(Cx)_P\cdot D\zeta_P(x)[u].                \tag{7}
\]
Only normal/tangential plaquettes enter for \(u_q\). Every coefficient
of \(\mathsf A\) is bounded by \(CQ\); every coefficient of
\(\mathsf B\) is bounded by \(C\). They are finite trigonometric
polynomials in \(q\), including the raw-edge phases. Both quadratic
polynomials are centered by their alternating color coefficients.
L287(13) says that the cubic term in (1) is exactly
\(\frac12\mathbb E[DV(x)[u_{-q}]DV(x)[u_q]]\).

Finite Fourier convolution puts the two Gaussian lines at \(p\) and
\(p+q\), after reversing a loop variable if necessary. Write
\(F=CG\) with its second slot any edge, and
\(H=CGC^*\) on normal/tangential plaquettes. The complete finite list
of crossing products is of the following types:
\[
 \begin{array}{c|c}
 \mathsf A\mathsf A&Q^2G_rG_t\\
 \mathsf A\mathsf B,\ \mathsf B\mathsf A&QG_rF_t, QF_rG_t\\
 \mathsf B\mathsf B&H_rG_t, G_rH_t, F_rF_t .
 \end{array}                                                \tag{8}
\]
This is a list of bounds on the exact products, not a replacement of
their signed coefficients. It retains both Wick crossings, all
directions/colors and the cross terms between all monomial types.
The number of types is finite, independent of \(M,q\). Edge selections
and averages shift depth by at most one and have bounded coefficients.

The complete density is L292(6): its diagonal Haar and \(P_{00}\)
terms are independent of \(q\), and its remaining plane contraction
is \(J_{00}(p;n,m)J_{00}(p+q;m,n)/4\), with the appropriate raw
phases. The quartic term is a finite sum of one-covariance contractions
on one plaquette, multiplied by external phases of modulus one.
Its two external normal slots have the same depth. Thus it is diagonal
in depth and continuous in \(q\). We use the full ambient quartic
polynomial in (1), not its already-collapsed constant-field formula.

Denote these exact loop integrands by \(s_H(p,q;n,m)\),
\(s_M(p,q;n,m)\), and \(s_\infty(p,q;n-m)\). Diagonal terms can be
included as diagonal kernels; the Haar constant is integrated against
the unit measure. Their coefficients and phases are fixed by (1),(7).
The bounds below hold term by term after the indicated bulk subtraction,
so they also hold for any consistent loop-variable convention.

### 2. Kernel bounds including arbitrary internal edge slots

For \(x=\kappa(p)>0\), L292(3)–(5),(16) and their scalar derivatives
give the following table. The second column bounds the full-line
kernel; the third bounds half-space minus full-line. All components
and the finitely many selected slot shifts are included.

| Kernel | Full line | Image difference |
| --- | --- | --- |
| \(G\) | \(Cx^{-1}e^{-cx|n-m|}\) | \(Cx^{-1}e^{-cx(n+m)}\) |
| \(F=CG\), \(J_{00}\) | \(Ce^{-cx|n-m|}\) | \(Ce^{-cx(n+m)}\) |
| \(H=CGC^*\) | \(C\delta_{nm}+Cx e^{-cx|n-m|}\) | \(Cx e^{-cx(n+m)}\) |
| \(P_{00}\) | \(C\delta_{nm}+Cx e^{-cx|n-m|}\) | \(Cx e^{-cx(n+m)}\) |

Here and below a contact symbol may be enlarged to a fixed-width
contact strip to cover shifts. This changes constants only. Pinned
tangential slots are zero, and are included by the same image formulas.

The extension beyond L292's averaged tangential second slot of \(F\)
is explicit: \(CG=CL^{-1}\), so in midpoint phases
\[
 (CG)_{0j,0}=-i d_jR_N,\qquad
 (CG)_{0j,k}=\delta_{jk}\delta R_D .                        \tag{9}
\]
The first uses \(|d_j|\leq Cx\); the second is one normal difference
of the Dirichlet kernel. Both satisfy the displayed exponential bounds,
including their images. Returning to raw slots restores the unit
phases. The contact part of \(H\) is the one in L292(16); its image
has no extra contact term. Thus (9) retains internal normal lines
which were unnecessary in the frozen-field calculation.

### 3. Absolute surface sums and the merging soft regions

For a product kernel define its one-face defect by subtracting the
bulk kernel on the common domain and then including the missing bulk
second vertices. For the complete expression this is
\[
 \Phi_H(p,q)=
 \sum_{n,m\geq0}\{s_H(p,q;n,m)-s_\infty(p,q;n-m)\}
 -\sum_{\substack{n\geq0\\m<0}}s_\infty(p,q;n-m).           \tag{10}
\]
This definition does not subtract two infinite total quadratic forms.

The elementary geometric sums needed for the subtraction are
\[
 \sum_{n,m\geq0}e^{-cr(n+m)}e^{-ct|n-m|}
       \leq\frac{C}{r(r+t)},\qquad
 \sum_{\substack{n\geq0\\m<0}}e^{-c(r+t)|n-m|}
       \leq\frac{C}{(r+t)^2}.                              \tag{11}
\]
To verify the first, split into \(n\geq m\) and \(m\geq n\), and
write the larger index as the smaller plus a nonnegative increment.
The two sums have ratios \(e^{-2cr}\) and \(e^{-c(r+t)}\).
The second is the product of two geometric sums. Bounded shifts are
absorbed by changing \(C,c\), since \(r,t\) are bounded above.

Subtracting products puts an image in at least one slot. Use (11),
the missing-row tail and
\(1/[r(r+t)]+1/[t(r+t)]=1/(rt)\). The resulting bounds on the
sum of absolute defects, before inserting the vertex factors in (8),
are
\[
 \begin{array}{c|c}
 J_rJ_t, F_rF_t&C/(rt)\\
 G_rF_t&C/(r^2t)\\
 G_rG_t&C/(r^2t^2)\\
 H_rG_t&C/t^2 .
 \end{array}                                                \tag{12}
\]
For clarity, the noncontact part of the last line contributes at most
\((Cr/t)\{1/(rt)+1/(r+t)^2\}\leq C/t^2\).
Its contact times the image of \(G_t\) contributes
\((C/t)\sum_n e^{-ctn}\leq C/t^2\). Contacts in the missing-row
strip have finitely many depths and satisfy the same bound. These
estimates also bound products containing two images; each half-space
kernel is bounded by the bulk exponential plus its image.

The local \(P\) defect sums to \(C\), the Haar defect is zero, and
the local quartic defect sums to \(C/r^2\). Combining (8),(12) gives
\[
 \begin{split}
 |\Phi_H(p,q)|&\leq C\left\{r^{-2}+t^{-2}
  +\frac{Q}{r^2t}+\frac{Q}{rt^2}+\frac{Q^2}{r^2t^2}\right\}\\
 &\leq C(r^{-2}+t^{-2}).                                   \tag{13}
 \end{split}
\]
The stronger assertion used here is that the sum of the absolute
subtracted terms in (10) obeys the same bound. The last inequality
uses (6) and \(1/(rt)\leq(r^{-2}+t^{-2})/2\). In particular the
external curls have not been discarded: their factors \(Q,Q^2\)
are what control the extra inverse powers in (12).

For comparison, summing the absolute full-line row of each product
uses \(\sum_k e^{-c(r+t)|k|}\leq C/(r+t)\). The same calculation
gives
\[
 \sum_{m\in\mathbb Z}|s_\infty(p,q;-m)|
                         \leq C(r^{-1}+t^{-1}).             \tag{14}
\]
For instance the \(\mathsf A\mathsf A\) bound is
\(CQ^2/[rt(r+t)]\leq C(r^{-1}+t^{-1})\), and the contact
part of \(H_rG_t\) is \(C/t\). This defines
\(b_\infty(q)=\int\sum_m s_\infty(p,q;-m)\,dp\) absolutely.

In three dimensions the right side of (13) is integrable, uniformly
near the two moving singularities. More precisely, if \(U_\epsilon(q)\)
is the union of radius-\(\epsilon\) torus balls centered at \(0,-q\),
then
\[
 \sup_q\int_{U_\epsilon(q)}(r^{-2}+t^{-2})\,dp\leq C\epsilon.
                                                               \tag{15}
\]
For a ball not centered at a given pole, if the centers are within
\(2\epsilon\), enlarge to a radius-\(3\epsilon\) ball around the
pole. Otherwise distance to that pole on the ball is at least half
the center separation, giving \(C\epsilon^3/d^2\leq C\epsilon\).
The ball centered at the pole has radial integral \(C\epsilon\).
This proves (15) also when the two poles merge.

Away from those points, the exact kernels, their coefficients, and
the absolutely convergent depth sums in (10) are continuous in \(q\).
The exponential bounds make this continuity uniform on compact sets
away from the poles. Split off \(U_\epsilon(q)\), use (15), and then
let \(\epsilon\downarrow0\). Consequently
\[
                  \sigma_H(q):=\int\Phi_H(p,q)\,dp
                \quad\hbox{is continuous at }q=0.          \tag{16}
\]
Fubini for the depth defect is justified by the absolute version of
(13). This is control of the whole depth sum, not a fixed-depth limit.

### 4. Uniform slab control, including its soft normal mode

Set
\[
 F_M(p,q)=\sum_{0\leq n,m<M}s_M(p,q;n,m)
              -M\sum_{m\in\mathbb Z}s_\infty(p,q;-m).       \tag{17}
\]
We prove the uniform bound
\[
                  |F_M(p,q)|\leq C(r^{-2}+t^{-2}).           \tag{18}
\]
First suppose \(rM,tM\geq1\). L292(20)'s image sums have geometric
denominators bounded below. The difference of any slab kernel from
its full-line kernel is bounded by its image amplitude in section 2
times
\(e^{-cx(n+m)}+e^{-cx(2M-n-m)}\), up to bounded shifts.
The periodic images are covered by these two terms; differentiating
the sums adds polynomial factors absorbed by a smaller \(c\).
All slab kernels also have the full-line bounds in the table up to
constants. Subtract on the common domain in (17), and include bulk
rows \(m<0\) and \(m\geq M\). Apply (11)–(13) once at each end.
This proves (18) in this region, including the contact contributions.

For \(xM<1\) the uniform geometric denominator is unavailable.
The finite Dirichlet formula and cosine decomposition in L292 section
5 give instead
\[
 |G_x(n,m)|\leq\frac{C}{Mx^2},\quad
 |F_x(n,m)|\leq\frac{C}{Mx},\quad
 |H_x(n,m)|\leq C(\delta_{nm}+M^{-1}),\quad |J_x(n,m)|\leq C,
 \qquad |(P_x)_{nn}|\leq1.                                \tag{19}
\]
These bounds include arbitrary edge slots. In detail,
\(R_D=O(M)\), \(\delta R_D=O(1)\), \(R_D^2=O(M^3)\),
and \(\delta R_D^2=O(M^2)\). The nonconstant part of \(R_N\)
is \(O(M)\), and its constant part is exactly \(1/(Ms)\).
Thus \(G_{00}=sR_N^2\) has constant part \(1/(Ms)\) and remaining
part \(O(sM^3)\); all components are bounded as in (19).
Equation (9) bounds the normal second slot of \(F\) by
\(C(Mx+1/(Mx))\leq C/(Mx)\); tangential second slots are \(O(1)\).
Finally L292(16)'s noncontact \(H\) term is
\(O(x^2(M+1/(Mx^2)))=O(M^{-1})\). This proves (19) without
removing any nonzero-momentum normal mode.

If both \(rM,tM<1\), double summation of (19) bounds
\(G_rG_t,G_rF_t,F_rF_t,H_rG_t\), respectively, by
\[
 C/(r^2t^2),\quad C/(r^2t),\quad C/(rt),\quad C/t^2.
\]
For the last expression use
\(\sum_{n,m<M}(\delta_{nm}+1/M)\leq2M\).
The density product sums to \(CM^2\), the quartic to \(C/r^2\),
and the diagonal density to \(CM\). After multiplication by the
vertex factors these are all bounded by \(C(r^{-2}+t^{-2})\).

If \(rM<1\leq tM\), the hard-kernel row sums are
\[
 \sum_m|G_t(n,m)|\leq C/t^2,\quad
 \sum_m(|F_t(n,m)|+|J_t(n,m)|)\leq C/t,\quad
 \sum_m|H_t(n,m)|\leq C,
 \qquad |G_t(n,n)|\leq C/t.
\]
They give the same displayed bounds for \(G_rG_t,G_rF_t,F_rF_t\)
and \(G_rH_t\) (the last is \(C/r^2\)). The other mixed cubic product
\(F_rG_t\) sums to \(C/(rt^2)\), since its soft supremum is
\(C/(Mr)\) and the hard total sum is \(CM/t^2\). The remaining product
\(H_rG_t\) sums to at most \(C(M/t+t^{-2})\).
The density product is at most \(CM/t\). Here
\(M/t\leq1/(rt)\), so these are acceptable. The local quartic is
\(C/r^2\) if its line is soft and \(CM/t\) if its line is hard.
Interchange \(r,t\) for the other mixed case. Using (6), every cubic
term, both mixed crossings included, is again bounded by the right
side of (18). This bounds the absolute slab sum whenever either
momentum is soft, not merely its signed value.

In that same region the absolute bulk term in (17) obeys
\(CM(r^{-1}+t^{-1})\leq C(r^{-2}+t^{-2})\), by (14) and
\(M\leq1/\min(r,t)\). This completes (18) on all regions.

### 5. The two prescribed regulator limits and the value at zero

At fixed \(M\), finite Fourier convolution expresses (2) as the
normalized momentum-grid sum of \(\sum_{n,m<M}s_M\), using the
actual harmonic-excluded inverse at the exceptional grid points.
Away from \(p=0,-q\), the integrand is continuous. At fixed \(M\)
it has an absolute majorant \(C_M(r^{-2}+t^{-2})\), by section 4
near the poles and the smooth finite kernels elsewhere. Counting
three-dimensional grid shells bounds each punctured radius-\(\epsilon\)
sum by \(C_M\epsilon\), uniformly along commensurate \(q_\ell\).

Exactly at internal momentum zero the excluded normal harmonic block
has no inverse. The remaining finite-dimensional inverse has bounded
entries for fixed \(M\). There are at most two exceptional loop grid
points. When the other momentum also tends to zero, its worst inverse
is \(C_M/t^2\); its smallest nonzero grid distance is of order
\(\ell^{-1}\). Thus the exceptional contribution after division by
\(\ell^3\) is at most \(C_M/\ell\), or \(C_M/\ell^3\) if both
lines are exactly zero. Curl entries are no worse, and the factors
\(Q,Q^2\) in (8) remain. The finite \(P,J\) matrices at zero use
the Dirichlet vertex inverse. No zero-mode limit is substituted for
the prescribed inverse. It follows that
\[
 Q_M(q)=\int\sum_{n,m<M}s_M(p,q;n,m)\,dp,
 \qquad Q_M(q)-M b_\infty(q)=\int F_M(p,q)\,dp.             \tag{20}
\]
The shell estimate also handles commensurate sequences tending to
zero; in particular (20) agrees with L292's exactly constant probe.
At exactly \(q=0\), \(\mathsf A\) vanishes before contraction; no zero
factor is multiplied by an undefined two-propagator integral.

For fixed \(p\ne0,-q\), split the slab into lower and upper halves.
The image sums show that lower-half rows differ from half-space rows
only by upper-end images and omitted second vertices. Summing those
terms tends to zero exponentially in \(M\), with polynomial factors
absorbed, since both \(r,t>0\). The tail of (10) beyond \(M/2\)
also tends to zero. Normal reflection sends \(n\) to \(M-1-n\)
on external normal edges and reverses both external signs. It preserves
the Wilson action, full density and harmonic exclusion. Hence the
upper-face contribution equals the lower-face contribution. All raw
slots are reflected together; no isolated phase or crossing is changed.
Consequently
\[
                         F_M(p,q)\longrightarrow2\Phi_H(p,q).
                                                               \tag{21}
\]
Equations (13),(18) and (15) justify integrating this limit. Equivalently,
first cut out the two small balls, pass by the uniform exponential
bounds on their complement, and then remove them using the common
\(C\epsilon\) estimate. This argument controls the merger of the soft
regions as well: the estimates in (15),(18) are independent of their
separation and of the growing thickness. It proves (3) with
\(\sigma(q)=\sigma_H(q)\). No reversal of the tangential-volume and
thickness limits is used.

By L292(2),(25), this same normalization and harmonic prescription
give \(\sigma_H(0)=0\). Equation (16) now proves (4). Pairing opposite
momenta is the complexification of a real statement: writing
\(u_q=u_c+i u_s\), symmetry gives
\(u_{-q}^{T}S u_q=u_c^T S u_c+u_s^T S u_s\), with no extra factor.
Thus the result applies to the stipulated paired real probes and
retains the unit constant-probe normalization at zero.

### 6. Separate conceptual audit (2026-10-27)

This audit accepts (3)–(4), conditional on the stated L280, L287 and
L292 inputs. It checks the extension from the audited constant probe,
including all external curls, rather than assuming a nonzero-momentum
Ward identity. No new external theorem is imported. The earlier
original-box errors are not used at surface scale.

**Exact products, anchors and normalization.** A plaquette containing
an external normal edge is a normal/tangential plaquette. Both normal
slots have the same depth anchor n, even when their tangential phases
differ. Its tangential slots are at n and n+1, including pinned zero
slots. Differentiating the full cubic polynomial gives (7) exactly.
The external curl has size at most CQ, whereas each coefficient of
D zeta[u_q] is a finite sum of unit phases. Alternating color factors
make each quadratic derivative centered. The first Wick crossing of
two B terms pairs their curls together and their remaining edge slots
together, giving HG; the other gives FF with the actual transposed
slots. AA gives GG, and AB/BA gives GF/FG. This verifies the complete
list (8), including normal internal edge slots and cross-directions.
There is no additional HH product or discarded internal contraction.
L287(13) gives E[DV[u] DV[v]]=u^T E v/2; multiplying by 1/2 is
exactly the E/4 normalization in (1).

The full density has the two diagonal terms and the J_00 J_00
product of L292(6). The quartic has only one internal covariance and
two external normal slots at the same depth; its phases vary smoothly
with q. These facts justify treating it as a local term in the bounds,
without using its constant-probe simplification. Finite Fourier
contraction fixes the two line momenta at p and p+q up to reversal.
Unit raw-edge phases and the bounded slot shifts do not alter any
absolute estimate. They remain in the signed integrands.

**Arbitrary slots and absolute half-space subtraction.** From CB=0
and L292(5), CG=CL^{-1}. Since L^{-1} has R_N in the normal component
and R_D in tangential components, its normal second slot is precisely
-i d_j R_N, and its tangential second slot is delta_jk delta R_D.
This proves (9), including the endpoint n=0. The normal slot is O(1)
times its exponential because |d_j|<=C r. The tangential slot is one
normal difference of R_D. Neither produces a contact term. The H
identity is delta_jk I+(d_j d_k-s delta_jk)R_N, so its only contact
is the common identity; the boundary image has size O(r). Likewise
P_00=I-sR_N. Differentiating the scalar image formulas bounds every
component of G by r^{-1} times its exponential, as in L292. Polynomial
factors in r times the image distance are absorbed by reducing the
exponential constant. Thus the full table applies to all slots in (8).

For two noncontact exponential factors, put
K(r,t)=sum_{n,m>=0} exp(-c r(n+m)-c t|n-m|).
Splitting at n=m gives K(r,t)<=C/[r(r+t)]. The missing-row sum is
bounded by C/(r+t)^2. In a product difference at least one line is
an image. Its double sum is therefore bounded by its amplitude times

\[
 K(r,t)+K(t,r)+C/(r+t)^2\leq C/(rt).
\]

The two-image term obeys this bound too, since n+m>=|n-m|. Applying
the amplitudes 1, r^{-1}, (rt)^{-1}, r/t gives, respectively, the
FF or JJ, GF, GG and noncontact HG powers in (12). A contact of H
times an image of G_t contributes
t^{-1} sum_n exp(-c t n)<=C/t^2. A shifted contact in a missing-row
strip permits only boundedly many pairs and contributes O(1/t),
which is also O(1/t^2) on the bounded momentum range. The diagonal
P image sums to O(1), and a local G_r image sums to O(r^{-2}).
This checks the complete subtraction (10), including all missing
second vertices. It bounds the sum of absolute subtracted terms,
not just a signed sum whose depth convergence was assumed.

Inserting the exact vertex bounds uses
Q/(r^2 t)<=C(r^{-2}+(rt)^{-1}) and
Q^2/(r^2 t^2)<=C(r^{-2}+t^{-2}); the reversed mixed term is the
same with r,t exchanged. These prove (13). A full-line exponential
row costs only C/(r+t); its HG contact costs C/t. Thus (14) holds
for the complete bulk row. The local terms obey it as well. The
radial integral of |p|^{-2} over a three-dimensional ball is O(epsilon),
and the displaced-ball argument in (15) handles both approaching
poles. Hence the absolute defect is uniformly integrable. Off the
poles, the geometric depth sums and all phase coefficients are
uniformly continuous on compact sets. This proves the depth Fubini
step and continuity in (16), rather than only fixed-depth continuity.

**Soft modes and every mixed slab regime.** For xM<1, s is comparable
to x^2. The normalized nonconstant normal cosine modes have squared
amplitude at most 2/M and eigenvalues at least 4 k^2/M^2. Summing
k^{-2} and k^{-4} therefore gives

\[
 |R_N^{\rm nc}|\leq CM,\qquad
 |(sR_N^2)^{\rm nc}|\leq CsM^3.
\]

The constant parts are 1/(Ms) for R_N and for sR_N^2. They are
retained for every nonzero internal tangential momentum. The finite
Dirichlet formula gives |R_D|<=CM and |delta R_D|<=C; composition
over at most M vertices gives |R_D^2|<=CM^3 and
|delta R_D^2|<=CM^2. In particular the transverse formulas give
|G_ij|<=CM and |G_0j|<=C x M^2<=CM. Together with G_00=sR_N^2
these are all bounded by C/(Mx^2). Formula (9) bounds the normal
second slot of F by C(xM+1/(Mx))<=C/(Mx), and the other slots by
C<=C/(Mx). The formula for H gives a contact plus O(1/M).
J_00=-2 mathsf a R_D delta^* is O(1), and the projection P has
diagonal at most one. This proves all of (19) with constants uniform
in M and without assigning the soft normal mode a gap.

For transparency, the following are bounds on double sums of absolute
products, before vertex factors. In the second column both momenta
are soft; in the third rM<1<=tM. Every entry has a common fixed
constant multiplier, and contact strips may have fixed width.

| Product | Both soft | r soft, t hard |
| --- | --- | --- |
| G_r G_t | 1/(r^2 t^2) | 1/(r^2 t^2) |
| G_r F_t | 1/(r^2 t) | 1/(r^2 t) |
| F_r G_t | 1/(rt^2) | 1/(rt^2) |
| F_r F_t | 1/(rt) | 1/(rt) |
| H_r G_t | 1/t^2 | M/t+1/t^2 |
| G_r H_t | 1/r^2 | 1/r^2 |
| J_r J_t | M^2 | M/t |

The soft/soft column follows by summing (19), using total contact
mass O(M). In the mixed column, multiply the soft entry supremum
by M hard row sums: these are O(t^{-2}), O(t^{-1}) and O(1)
for G_t, F_t or J_t, and H_t respectively. For H_r G_t retain
its contact separately: the hard diagonal bound gives CM/t, and
the soft 1/M part times the hard total G sum gives C/t^2.
This verifies the asymmetric entry rather than treating H as a
bounded supremum. Interchanging r,t covers the other mixed regime.

The diagonal density sum is O(M). A soft one-line quartic sum is
O(r^{-2}) or O(t^{-2}); a hard one is O(M/t) or O(M/r). If r
is soft, M/t<=1/(rt), and if both are soft M^2<=r^{-2}. With
Q<=C(r+t), the entire table and these local terms are bounded by
C(r^{-2}+t^{-2}). The absolute bulk subtraction is bounded by
CM(r^{-1}+t^{-1}); writing h=min(r,t) and using M<=1/h proves
the same bound when at least one line is soft.

If both lines are hard, the image sums have denominators bounded
away from zero. Every reflected distance is at least the direct
distance up to the fixed slot shifts. Differentiation introduces
only polynomial distance factors, absorbed in smaller exponentials.
Thus the slab kernels have the hard full-line bounds, and their
differences are controlled by lower and upper images. Apply the
previous absolute subtraction argument at each face, including both
missing-row tails. The diagonal Haar term cancels exactly. This
proves (18) in all four regimes.

**Exceptional grid blocks, ordered limits and the two faces.** At
fixed M, both poles belong to the momentum grid because q_ell is
commensurate. On the punctured grid a shell of radius j/ell contains
O(j^2) points, each contributing at most C_M ell^2/j^2 before the
ell^{-3} normalization. Summation to epsilon ell gives O(C_M epsilon).
The same count applies around the translated pole. Off these balls,
the finite matrices converge uniformly as q_ell tends to q. This
justifies the moving punctured Riemann sums, including q=0.

At an exactly zero internal momentum, the prescribed inverse has
the three constant normal vectors removed. The remaining transverse
precision has a positive gap for fixed M, so inverse entries are bounded by
C_M. This is a separate finite block, not the limit of G_00 as
p tends to zero. The other line is bounded by C_M dist(q_ell,0)^{-2}
when nonzero, hence by C_M ell^2. There are at most two exceptional
loop points, whose normalized contribution is O(C_M/ell). When
both lines are exactly zero it is O(C_M/ell^3). P and J use the
finite Dirichlet inverse and remain bounded there. This proves (20)
with the actual harmonic prescription. At q=0 the A polynomial
vanishes before any contraction.

For the thickness limit, keep p away from both poles and use the
loop variables in the finite Fourier contractions before reflecting
depth. Upper images on lower-half rows and omitted second vertices
decay exponentially in M, as does the discarded half-space defect
tail. Normal reflection acts on depth and link orientation, leaving
tangential momenta unchanged. It preserves the full action, density
and harmonic-excluded inverse. Both external normal signs reverse,
so their quadratic product is unchanged. This verifies (21) for
the complete signed integrand in this common convention, including
its factor two. The integrable bounds (13),(18) allow the thickness
limit after the tangential-volume limit. Their uniform small-ball
bound also allows the poles to merge when proving continuity.
No simultaneous finite-volume limit is substituted for this order.

Finally (20) at q=0 is L292's same constant probe, so L292(2),(25)
give sigma_H(0)=0 in the normalization of (3). The identity
u_{-q}^T S u_q=u_c^T S u_c+u_s^T S u_s follows from the symmetry
of the real finite S; at q=0 the sine vector is zero. There is no
additional color, cosine, or face factor. This accepts the stated
continuity and absolute surface convergence. It does not justify
replacing actual depth-varying source fields by these probes, or
give a quantitative full-box remainder, the other groups/strata,
the uniform higher expansion, or a Yang–Mills construction.

## Mathlib

Full coverage of this Wilson-specific surface continuity theorem:
**not checked**. No absence claim is made. The proof uses L280's ambient
tensors, L287's complete cubic derivative and L292's exact kernels and
zero-momentum result, retaining their stated qualifications.
Finite Fourier convolution, Gaussian pairing,
geometric sums and dominated integration are used in their explicit
forms above. No new external renormalization, boundary Ward or
zero-momentum power-counting theorem is imported. The prior EXPLORE
assessment permits this specialization of the exact kernels; it does
not certify originality beyond the checked literature. Section 6 is
the separate critical audit, reusing the ready audit assessment.
