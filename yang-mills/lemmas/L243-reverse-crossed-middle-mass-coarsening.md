# L243 — Middle-mass coarsening in the reduced reverse trace

## Hypotheses

Use exactly L242's reduced trace B_(i,N;epsilon,eta,delta) and its
relative transverse vertex, edge and plaquette spaces V,E,F. Retain
the all-face relative SU(2) cube, straight lower-rooted direction-1
forest, sufficiently large admitted even N, a=8/N, tau=1/16,
stored coordinates, bare-first order and both actual probes i=3,6.
All coefficient levels, generator/path filters, source/end rows,
constant component indices and the complete exterior heat sum remain.
The subtraction for the eventual remainder is exactly L107(2)'s
a^-3 K_(i,R), without an outside factor 3. This is not G_R or R_L.

Write n=N-1, G=Delta_0^-1, G_eta=(Delta_0+eta I)^-1,
U_t^eta=T G_eta W_t^T, and Z_k=Zeta_k/a, as in L242. The mass
eta=0 denotes G. For 0<epsilon<=1, 0<=eta<=h<=1 and
0<=delta<=1, set Q_0=Q and otherwise use Q_delta of L242.
Require N sqrt(h)>=1 for the middle-mass estimate below. In all
axial sums keep S_st=1_(t<s)+delta_st/2.

## Conclusion

Uniformly in these parameters and N,

    |B_(i,N;epsilon,eta,delta)-B_(i,N;epsilon,h,delta)|
      <=C_i N^3 h^(3/4)
                    [log(e/epsilon)+epsilon^(-1/2)]
      <=C'_i N^3 h^(3/4)epsilon^(-1/2).                 (1)

There is no inverse power of eta in this bound. In particular, under
the additional conditions N sqrt(epsilon)>=1, delta>0 and
N sqrt(delta)>=1, the original full reverse trace satisfies

    |R_R-B_(i,N;epsilon,h,delta)|
      <=C_i {N^2+N^3[sqrt(epsilon)
                  +delta^(3/4)log(e/epsilon)
                  +h^(3/4)epsilon^(-1/2)]}.             (2)

Consequently the finite-inequality choices

    epsilon=N^-1, h=N^(-4/3), delta=N^(-2/3)             (3)

give an O_i(N^(5/2)log(eN)) comparison with R_R. The previous
middle mass N^-2 is no longer necessary for this reduced approximant.
The inverse square-root mass scales in (3) are N^(1/2), N^(2/3)
and N^(1/3), all sublinear. This numerical comparison of scales is
not a proof of a finite-range or relative-boundary approximation.
Quantitative localization, ordered coefficient freezing and comparison
with exactly L107(2) remain unproved. The complete registered
O(N^(5/2)log(eN)^2) reverse remainder is therefore still open.

The separate critical audit in proof section 5 accepts (1)--(2)
relative to their imported inputs, including L242's still-qualified
reduction/projection comparison. Independent
component rates, complete quantitative L011 assembly, interacting
reflected error <=c_box/2, continuum axioms, infrared control and
finite positive mass remain unresolved. No solution candidate follows.

## Proof

### 1. A middle-mass difference in its original energy order

Import L103(13) and L242(14) on the identical full relative spaces:

    ||T G^(1/2)||=1, ||W_t G^(1/2)||<=C,
    ||Z_k(s)||<=C p(k),
    sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i.                  (4)

The same fixed enlarged mode polynomial p applies to both probes.
Since dim E,dim F<=C N^3 and ||D||<=sqrt(12), it also gives

    ||Z_l(t)^T||_HS+||D^T Z_l(t)||_HS
                                      <=C N^(3/2)p(l). (5)

For any 0<=eta<=h, define the scalar spectral multiplier on V

    J_(eta,h)=Delta_0(G_eta-G_h),
    j_(eta,h)(lambda)
      =lambda(h-eta)/[(lambda+eta)(lambda+h)].           (6)

All vertex eigenvalues are strictly positive, including when eta=0.
The multiplier obeys 0<=j_(eta,h)(lambda)<=h/(lambda+h).
L103(16)'s second shell estimate, with its parameter replaced by h,
therefore gives

    ||J_(eta,h)||_HS<=C N^(3/2)h^(3/4),
                                              N sqrt(h)>=1.       (7)

This application uses precisely the pinned transverse vertex
spectrum; it changes no edge boundary condition or allowed constant
edge index. The estimate is uniform in eta because (6) is dominated
by the same spectral multiplier h/(lambda+h), rather than by an
inverse norm depending on eta.

With Delta U_t=U_t^eta-U_t^h, exact spectral factorization gives

    Delta U_t=(T G^(1/2)) J_(eta,h) (W_t G^(1/2))^T,
    ||Delta U_t||_HS<=C N^(3/2)h^(3/4).                 (8)

Indeed G^(1/2)J_(eta,h)G^(1/2)=G_eta-G_h. The displacement
inside W_t has not crossed an inverse or a spectral multiplier.
Formula (8) does not treat W_t as a gradient map. Also
||Q_delta||<=1 for every allowed delta: on gradients its eigenvalues
are delta/(lambda+delta) when delta>0, on their orthogonal
complement they are one, and Q_0 is an orthogonal projection.
No positive-mass projection is assumed idempotent.

### 2. Sum the one-circulation covariance before estimating the trace

In addition to L242(5)'s already proved two-circulation sum, we need

    sum_(s,t=1)^n ||R_ts^epsilon D^T||_op
                                      <=C n epsilon^(-1/2).       (9)

Use the exact heat representation L242(9)--(10), writing
H_ts(r)=[exp(-r L_D)]_ts. It has H_ts(r)>=0 and
sum_st H_ts(r)<=n on the full pinned interval. On E,
D^T D=Delta_T Q, and Delta_T commutes with Q. Thus

    ||exp(-r Delta_T)D^T||_op
      <=sup_(0<=lambda<=12) sqrt(lambda)exp(-r lambda)
      <=(2 e r)^(-1/2), r>0.                            (10)

This follows by maximizing lambda exp(-2r lambda) on the larger
half-line lambda>=0. It remains valid if F has an additional zero
curvature complement. The finite-dimensional Laplace representation,
triangle inequality and nonnegativity of H_ts now give

    sum_st ||R_ts^epsilon D^T||_op
      <=n (2e)^(-1/2) integral_0^infinity
                                    e^(-epsilon r)r^(-1/2)dr
      <=C n epsilon^(-1/2).                             (11)

For the last bound substitute v=epsilon r: the integral on [0,1]
is at most 2 and the one on [1,infinity] is at most e^-1. This
also proves integrability at zero and infinity. Every axial source
and both end rows stay in the sum. There is no full-matrix norm
substituted for an n^2 block sum. Together with the imported L242(5),
we have

    sum_st ||D R_ts^epsilon D^T||_op<=C n log(e/epsilon),
    sum_st ||R_ts^epsilon D^T||_op<=C n epsilon^(-1/2).  (12)

### 3. Bound both ordered trace differences

Subtract L242(3) at middle masses eta and h, changing no other
factor. In the first term, rectangular trace cyclicity yields

    Tr_E[R_ts^epsilon D^T Z_k(s) Delta U_t
                                         Q_delta Z_l(t)^T D]
      =Tr_F[(D R_ts^epsilon D^T) Z_k(s) Delta U_t
                                                 Q_delta Z_l(t)^T].       (13)

The Hilbert--Schmidt norms in (5),(8), together with (4), give

    |(13)|<=C N^3 h^(3/4)p(k)p(l)
                                      ||D R_ts^epsilon D^T||_op.  (14)

In the second term do not move a circulation through Z or W. Its
literal edge trace is

    Tr_E[(R_ts^epsilon D^T) Z_k(s) Delta U_t D^T Z_l(t)].            (15)

Apply trace Cauchy--Schwarz to
(R_ts^epsilon D^T)Z_k(s)Delta U_t and D^T Z_l(t). Their dimensions
are E-by-E, and their Hilbert--Schmidt bounds imply

    |(15)|<=C N^3 h^(3/4)p(k)p(l)
                                           ||R_ts^epsilon D^T||_op.       (16)

Thus each circulation used in (12) is actually adjacent to the
covariance in its displayed ordered term. Neither estimate commutes
a coefficient, a component filter, a projection or a Green inverse.
The factors at s and t remain distinct.

Use 0<=S_st<=1, (12), the original a prefactor in L242(3), and
the full heat majorant (4). The difference of the two responses is
at most

    C_i a n N^3 h^(3/4)
                         [log(e/epsilon)+epsilon^(-1/2)].          (17)

Since an<=8, this proves the first bound of (1). For
0<epsilon<=1, log(e/epsilon)<=2 epsilon^(-1/2): writing
x=epsilon^(-1/2)>=1, the inequality is 1+2 log x<=2x,
which follows from its value at 1 and derivative 2/x<=2.
This proves the second bound of (1).

### 4. Combine only uniform finite inequalities

First apply only L106 proof section 2, equation (8), to replace
the axial covariance by R^epsilon while keeping the original G
in the middle. This costs C_i N^3 sqrt(epsilon) under
N sqrt(epsilon)>=1. L106 section 4 removes the exterior-circulation
pieces with error C_i N^2 uniformly, including middle mass zero.
L242's exact reduced identity identifies the remaining trace with
B_(i,N;epsilon,0,0). Its projection estimate (4), explicitly valid
at eta=0, changes this to B_(i,N;epsilon,0,delta) with error
C_i N^3 delta^(3/4)log(e/epsilon). Finally (1) with eta=0
changes only the middle mass to h. The triangle inequality gives
(2). This does not invoke L106's less favorable eta^(3/4)/epsilon
bound, and no fixed-mass limit receives varying parameters.

At (3) the three spectral conditions are respectively
N^(1/2)>=1, N^(1/3)>=1 and N^(2/3)>=1. The covariance
and middle-mass errors in (2) are each O(N^(5/2)); the projection
error is O(N^(5/2)log(eN)). This proves the asserted comparison.
Both reduced ordered terms still contain every original row, level,
filter and heat label. The triangle inequality has estimated errors,
not deleted S_st or its diagonal half from the retained trace.

The new input removes the need to localize a middle inverse of
mass N^-2. It supplies no polynomial error, finite-to-bulk identity,
coefficient-freezing rate or comparison to the unregularized torus
functional. These remain distinct obligations for the unchanged
registered remainder target. This is REPRODUCTION under its prior
EXPLORE assessment: local progress using established finite spectral
and trace-ideal methods, without a claim beyond sources checked.

### 5. Separate critical audit of the middle-mass comparison

On 2026-10-20, a separate proof audit under the unchanged SPECIALIZE
assessment `drafts/literature/2026-10-20-reverse-crossed-middle-mass-audit.md`
checked (1)--(2). The verdict is acceptance relative to L103's energy
and shell estimates, L106's covariance-only and exterior estimates,
and L242's reduced identity and projection comparison. This is local
verification of the existing rate, not a new estimate, an upstream
audit, or progress beyond the sources checked. In particular L242's
independent critical-audit qualification remains.

**Energy order and endpoints.** The compatible maps are T,W_t:V->E,
D:E->F, Z_k:E->F and U_t:E->E. On V the pinned Delta_0 is strictly
positive. For 0<=eta<=h its scalar multiplier satisfies

    0<=lambda(h-eta)/[(lambda+eta)(lambda+h)]
      <=h/(lambda+h).

Indeed lambda(h-eta)<=h(lambda+eta). At eta=0 the upper bound is
an equality, so this endpoint is included without a limiting argument.
At eta=h the difference is zero. With M=N sqrt(h)>=1, the complete
pinned shell sum of [h/(lambda+h)]^2 is bounded by

    C sum_(r<=M) r^2 + C h^2 N^4 sum_(r>M) r^-2
      <=C N^3 h^(3/2),

where both sums are restricted to the actual shells and an empty
high range is zero. This is exactly L103(16)'s second bound; it is
not an inverse-eta bound or an assertion about small operator norm.
The exact identity G^(1/2)J_(eta,h)G^(1/2)=G_eta-G_h places the
unchanged W_t G^(1/2) at the right of the HS factor. L103(13) thus
gives (8) in its original coefficient order, with every pinned vertex
and transverse normal end edge retained. Q_delta is a contraction
also for delta=0; positive delta is never treated as a projection.

**Full axial block norm sum.** The finite Dirichlet axial heat matrix
has nonnegative entries and total entry sum <=n, including the first
and last rows, as proved in L242(9). The singular-value identity
D^T D=Delta_T Q gives

    ||exp(-r Delta_T)D^T||^2
      =||exp(-r Delta_T)Delta_T Q exp(-r Delta_T)||
      <=sup_(lambda>=0) lambda exp(-2r lambda)=1/(2er).

Zero singular values on any curvature complement cause no loss.
Inserting this into the exact Laplace formula and summing every s,t
before integration gives (11). The scaled integral is finite because
integral_0^1 v^(-1/2)e^-v dv<=2 and
integral_1^infinity v^(-1/2)e^-v dv<=e^-1. The same calculation with
the two-circulation bound min(12,1/(er)) gives L242(12)'s logarithm.
These are sums of block operator norms; no norm of the complete axial
matrix replaces that sum. Positivity is used only for the scalar
heat kernel, not for either signed response. Both estimates hold for
every epsilon>0 in the stated range before choosing masses.

**Both rectangular words and the complete count.** Rectangular trace
cyclicity in (13) yields an F-space trace with the factor D R D^T.
The factors Z_k Delta U_t and Q_delta Z_l^T are respectively
F-by-E and E-by-F. HS trace duality bounds their product by
C N^3 h^(3/4)p(k)p(l), multiplied by ||D R D^T||. In (15),
(R D^T)Z_k Delta U_t and D^T Z_l are both E-by-E; their HS product
has the same N^3 h^(3/4)p(k)p(l) bound, now multiplied by
||R D^T||. The latter has only one adjacent circulation, so the
epsilon^(-1/2) cost is necessary in this proof and has not been
replaced by the two-circulation logarithm. All deterministic filters
remain inside Z or W, at their original s and t levels.

The dimensions of E,F are O(N^3), independently of mode labels.
After summing the two block estimates, the remaining level count is
n, and the actual prefactor is a, so a n<=8 gives (17) with N^3,
not N^4. The imported polynomial envelope is absolutely summable
against the complete c_(i;kl,a) series for each actual probe. Thus
the bounds hold before the full heat sum, including constant allowed
indices and both probe polarizations. Using |S_st|<=1 bounds only
the error; S_st and its diagonal half stay in the retained trace.
Finally log(e/epsilon)<=2epsilon^(-1/2) on (0,1], as checked in
section 3, proves both inequalities in (1).

**Original middle mass zero and assembly.** The first comparison is
specifically L106 proof (8), whose target R_(i,N;epsilon,0) keeps G
unchanged. Its sole spectral condition is N sqrt(epsilon)>=1;
L106's combined positive-eta conclusion is not evaluated at zero.
In its section 4, Delta_0/(Delta_0+eta) has norm <=1 also at eta=0,
and the covariance trace domination is independent of eta. The
exterior-circulation difference is therefore O(N^2) at this endpoint.
This checks the claimed applicability without extending a bound
containing eta in a denominator. L242's imported exact reduction at
eta=delta=0 and its projection comparison at eta=0 then supply the
two next steps in section 4. The just-audited (1) supplies the last.
Their triangle inequality proves (2) with all original coefficient
levels, source/end rows, signs and heat labels retained.

At epsilon=N^-1, h=N^(-4/3), delta=N^(-2/3), the three conditions
N sqrt(epsilon), N sqrt(h), N sqrt(delta)>=1 hold. The covariance
and middle differences are each O(N^(5/2)), and the projection
difference is O(N^(5/2)log(eN)); the O(N^2) exterior term is smaller.
This meets the asserted comparison threshold using uniform finite
inequalities only. No localization or fixed-mass limit is invoked
at varying mass. No unsupported assertion was found in this
specialization. It does not independently verify L242 or infer the
complete reverse remainder, other component rates, L011 assembly,
an interacting reflected estimate or a Yang--Mills construction.
No numerical or mathematical-script evidence is used.

## Mathlib

Full matching reduced reverse-trace middle-mass estimate: **not
checked**. Supporting finite spectral calculus, matrix heat kernels,
rectangular trace cyclicity and Hilbert--Schmidt inequalities:
**not checked**. Unknown coverage is not evidence of absence. The
local inputs above are imported in their stated relative spaces;
no external Ward/flow theorem or continuum construction result is
claimed to give this isolated bare-trace rate.
