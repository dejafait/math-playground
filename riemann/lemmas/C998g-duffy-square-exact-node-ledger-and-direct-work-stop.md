# C998g: Finite-cell Duffy square ledger and direct contraction stop

## Hypotheses

Use the three exact real C998a columns, C999q's exact neutral completion
Z, ell=log(3)/2 and a=ell/2. The free q coefficients have modes2..255
and are the binary rationals in `free_middle_dyadics` of
`scripts/separation-seven/frozen-reference-proposal-652.npz`, SHA256
`2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6`.
No coefficient or parameter is retuned. C998a/audit655 supplies its
unitary parity map, real finite cosine densities v_epsilon,j and
the coefficient-sum amplitude envelope V_j<14, not merely a sampled
supremum. Its full654/655 rational evidence is checked below.

The object is ONLY the last term of C998e(7), with both parities,
all column products and factor1/4. C998e(6)-(8) is independently
audited in Section1 before use. All original analytic-response,
arithmetic, source-to-Xi, whole-core and c_* contracts are retained;
this assertion does not validate them. C998f/audit669's separate
diagonal setup reserve is not part of this square-service count.

Invocation-start SPECIALIZE assessment670 permits this one quantitative
specialization. For substitution use Mousavi--Sukumar, *Generalized
Duffy transformation for integrating vertex singularities*, Computational
Mechanics45(2010),127-140, Section2/(1a)-(1b) and Appendix A, p137,
[primary repository PDF](https://escholarship.org/content/qt3fk9s522/qt3fk9s522.pdf).
Our nonpolynomial numerator needs its own bounds: their polynomial
radial exactness claim is not used. For interior quadrature import
Trefethen, *Approximation Theory and Approximation Practice*(2013),
Chapter19 Theorem19.3/(19.8),
[book PDF](https://people.math.ethz.ch/~hiptmair/Seminars/RAP_22/TRE13.pdf):
on[-1,1], a bounded holomorphic continuation to E_rho, bound M,
gives error <=(64/15)M*rho^(-2n)/(rho^2-1) for the(n+1)-point
Gauss rule, n>=1. Its positive weights sum to2. On an interval of
length d multiply the bound and weights by d/2. This is the source
and point-count convention already assessed655/656. No general
quadrature theorem, singular tensor theorem or complex divided-difference
theorem is reproved or inferred. Local holomorphic bounds are proved below.

Prescribe ONE rule: omit angular y<eta=2^-48; use321-point Gauss
on radial x in[0,1]; on panel y in[b_j,2b_j], b_j=2^-j, j=1..48,
use(n_j+1)-point Gauss, n_j=32+ceil(144b_j). For the contemplated
finite implementation propose256 fractional bits, with every constant,
node, weight, coefficient and arithmetic error still requiring enclosure.
The pre-batch work check is performed before constructing those enclosures.

The prescribed contraction directly sums the normalized cosine
coefficients at each ordered scaled-node key(x_r,y_jk). Precombine the
normalization factors into the coefficients; share each cosine basis
across all six outputs; cache all unscaled v_epsilon,j(ax_r) across
all angular panels and both triangles. At each scaled-node key,
evaluate all six v_epsilon,j(ax_r*y_jk) by direct coefficient-times-basis
accumulation. There is no mode pruning, transform, polynomial surrogate
or merging of different ordered keys. Even if a further algebraic
reuse were possible it is a different prescription. Count one real
addition, subtraction, multiplication, division, comparison or assignment
as one scalar operation. The lower count here includes only one
multiplication per nonzero free coefficient at each scaled-node key;
it omits elementary-function and all other work, at every precision.

## Conclusion

The product, conjugation, absolute-integrability and projection identities
C998e(6)-(8) pass this scoped audit. C998e's later quantitative ledger,
inverse assertions and other unaudited corollaries are not audited here.

For the complete finite-cell square contribution S_ij, the exact
transformation(1)-(2) below and the prescribed exact-node Gauss rule
give total corner-plus-quadrature error at most

    E_analytic = 18063793/1729382256910270464 < 1.1e-11.    (A)

This is below the requested1e-10 entry tolerance, but is NOT a
finite-arithmetic certificate. Nodes, weights, constants, coefficient
enclosures, the near-diagonal evaluator and their error propagation
remain unpaid. In particular no actual S_ij interval has been computed.

The direct contraction fails its work cap before those tasks:

    321*1770 = 568170 scaled-node keys,
    568170*762 = 432945540 mandatory real multiplications
                  > 20000000 allowed total scalar operations.       (B)

This is a lower count for the specified implementation, not a complexity
lower bound for the square problem or an actual error lower bound. No
batch or parameter sweep is run. The prescription is stopped. This is
a local REPRODUCTION under the assessed methods; the specialization
and its finite checks are independently upheld by audit674 in Section7. It supplies no
residual size, inverse debt, signed S3 comparison or RH candidate.

## Proof

### 1. Independent audit of C998e(6)-(8)

Write C v(t)=integral_0^a v(s)/(t+s) ds. For s,u>0 and tau>=0,
tau<a, partial fractions give

    integral_tau^a dt/[(t+s)(t+u)]
      = [log((a+s)/(tau+s))-log((a+u)/(tau+u))]/(u-s)

when s!=u. At s=u direct integration gives
1/(tau+s)-1/(a+s). The integral representation is continuous on
positive compact s,u ranges, including s=u; for tau>0 it also extends
to the axes. For tau=0 the axes may be left undefined as null sets.
Thus the sign, cutoff and finite upper-limit correction in(6) are correct.

C998a(4) has v_+=[q(ell-t)+q(t)]/sqrt(2) and
v_-=[q(ell-t)-q(t)]/sqrt(2), with unitary norm and the stated odd
reflection sign. Each Carleman block has coefficient1/2. Consequently
expanding g_epsilon,j=A_epsilon,j-(1/2)Cv_epsilon,j yields the
A-square, BOTH mixed products with coefficient-1/2 and their indicated
conjugations, and the square with coefficient1/4 in C998e(7).
There is no orthogonality of these terms. The bounded A expression
retains its translation indicators; no translation kernel is invented.

Here is the absolute convergence check, independently of cancellation.
C998a's audited envelopes give F+H<26,V<14. The finite forcing,
diagonal, h_m and E bounds used in C998e(3) give
|A|<1.5[17*26+21*14]+21.5*14=1405<1500.
The A-square has bound1500^2; each mixed double integrand has
bound1500*14/(t+s), with integral1500*14*2a log2.
The absolute singular triple integrand is at most
196/[(t+s)(t+u)]. Integrating its nonnegative bound in s,u gives
196*log(1+a/t)^2. Its t integral is <=196*5a, because
log(1+a/t)<=log(2a/t) and
integral_0^a log(2a/t)^2 dt=a[(log2)^2+2log2+2]<5a.
Finite Lebesgue products are sigma-finite and the representatives are
Borel measurable. These are exactly the hypotheses of Folland,
*Real Analysis*,2nd ed.(1999), Section2.5, Theorems2.37/2.39,
pp67-68 and finite products p65,
[primary extract](https://people.math.sc.edu/girardi/m7034/1617/hw/FollandRA2edProdMsr.pdf).
Tonelli applies to the bounds and Fubini to the absolutely integrable
complex products. This proves the required interchange, rather than
assuming it from existence of signed iterated integrals.

Finally put w_+(x)=exp(x/2),w_-(x)=exp(-x/2). C998a(23) gives the
real symmetric positive moment Gram

    G_w=[[exp(ell)-1,ell],[ell,1-exp(-ell)]],
    det(G_w)=2cosh(ell)-2-ell^2>1/192.

In the first-slot-linear convention, mu_c,j=<g_j,w_c>, exactly the
integrals in C998e(8); the transformed w_c are real and bounded by3.
Their mixed integral is absolutely bounded by42/(t+s). If W maps a
two-vector to its linear combination of the w_c, then C(Wz)=G_w z,
where Cg=(<g,w_c>)_c. The orthogonal projection is
P0g=g-WG_w^-1 Cg. Orthogonality, or direct expansion, now gives

    <P0g_j,P0g_i>=<g_j,g_i>-mu_i^*G_w^-1 mu_j.

This is C998e(8), including conjugation order. It remains valid for
complex combinations of the real columns. It concerns the moment
projection, not an unrestricted inverse compressed to H0. All identities
audited here are exact full actions; no forcing series has to be expanded
for this check. The square-only work below does not need A or its scalar
evaluation, and does not inherit a certificate for them.

### 2. Exact finite-cell transformation

Put h(y)=-log(y)/(1-y), h(1)=1. Split the(s,u) square, up to its
null diagonal, into its two triangles. On s>=u use s=ax,u=axy,
0<x,y<1; the other triangle swaps s,u. The Jacobian is a^2 x.
Substitution in the audited finite-cell formula gives

    a*x*K_0(ax,axy)=W(x,y),
    W(x,y)=[-log(y)-log((1+x)/(1+xy))]/(1-y)
           = integral_0^1 dt/[z(1+xz)],
    z=y+(1-y)t.                                         (1)

Indeed the logarithmic numerator equals
integral_y^1 [1/z-x/(1+xz)] dz=integral_y^1 dz/[z(1+xz)].
This also identifies the value at y=1 as1/(1+x), and the value at
x=0 as h(y). It proves removable extension on the closed radial edge
and the angular diagonal for y>0. The logarithm at y=0 remains.
For real0<=x<=1,0<y<=1, we have0<W(x,y)<=h(y).
There is no omitted radial strip, diagonal strip or output cutoff.
The finite upper endpoint a is retained by the second logarithm in(1);
the half-line Carleman square would wrongly omit that correction.

For real fixed columns, define

    F_ij(x,y)=(a/4) W(x,y) sum_epsilon [
         v_epsilon,j(ax) v_epsilon,i(axy)
        +v_epsilon,j(axy) v_epsilon,i(ax)],
    S_ij=integral_0^1 integral_0^1 F_ij(x,y) dx dy.       (2)

The four products in the sum are the two triangles and two parities;
no factor2 is imposed on an off-diagonal product. Their absolute real
bound is196a h(y). Absolute integrability follows from Section1 or
the bound below, so the triangle substitution is legitimate. For complex
column combinations the resulting real symmetric matrix is extended
sesquilinearly. For quadrature we use the displayed entire real-trace
products, not conjugation of a complex argument. No polynomial radial
exactness or unproved all-derivative Gevrey estimate is invoked.

### 3. Paid angular corner

For0<y<=1, -y log y<=1-y, hence h(y)<=1-log y. Therefore omitting
0<y<eta loses at most, per entry including all four products,

    E_corner <=196a*eta*(2-log eta)
              <196*(3/10)*50*2^-48=2940*2^-48.          (3)

Here1/4<a<3/10 is already audited655 and log2<1. This pays the
coincident corner and both asymmetric input strips through the same
triangle map; their overlap is counted by the change of variables,
not dropped. It is an entrywise bound even when a product changes sign.

### 4. Uniform one-variable ellipse bounds

For a completed finite cosine density the coefficient-sum proof of
C998a(7), including its neutral0/1 modes, gives

    |v_epsilon,j(a z)| <=14 exp(510 |Im z|).             (4)

To see why this is a complex bound rather than a real-supremum inference,
the sum of absolute normalized parity coefficients is <=6 times the
free absolute mass=V_j<14. Each cosine has modulus at most
exp((n*pi/2)|Im z|), and n<=255,pi<4 give n*pi/2<510.
The same bound covers both parities and all three exact completions.

The Bernstein ellipse with rho=2 on[0,1] has real part in[-1/8,9/8]
and imaginary part of magnitude at most3/8. Fix real y in[eta,1].
Then z in(1) is real in[y,1], so Re(1+xz)>=7/8 throughout this
radial ellipse. The integral in(1) is holomorphic in x on a
neighborhood of its closed ellipse, uniformly dominated there, and

    |W(x,y)| <=(8/7)h(y)<=(8/7)*49.

By(4), the product of two densities is <=196 exp(765/2).
Consequently on every such radial ellipse

    |F_ij| <3300 exp(765/2) <3300*2^574 = M_x.          (5)

The last inequality uses log2>2/3, from the first term of
2*atanh(1/3)=log2, since765/2<574*(2/3).
This argument bounds each individual product before summing; no
complex-phase cancellation is assumed.

For angular panel[b,2b],0<b<=1/2, its rho=2 ellipse has
Re y>=7b/8, |Im y|<=3b/8. Fix real0<=x<=1. For every t in[0,1],
z=t+(1-t)y satisfies Re z>=7b/8 and Re(1+xz)>=1. Thus the
same integral defines a holomorphic W on a neighborhood of that
closed ellipse with |W|<=8/(7b)<2/b. The unscaled v(ax) is bounded
by14; the scaled v(axy) is bounded by14 exp(765b/4). Hence

    |F_ij| <(118/b) exp(765b/4)<(118/b)*2^(288b)=M_y(b). (6)

Indeed765/4<288*(2/3). These are separate one-variable estimates,
uniform in the other REAL coordinate, which is sufficient for the
tensor error decomposition below. A joint complex neighborhood or
conjugate-holomorphic trace is not silently assumed. In particular(6)
includes y=1 and controls the removable diagonal, but does not yet
implement a stable finite-arithmetic diagonal evaluator.

### 5. Exact-node quadrature ledger

Apply Trefethen19.3 with rho=2,n=320 and radial length1. The uniform
radial error, also after integration over the retained y interval of
length<1, is at most

    E_x <=(32/45)*3300*2^(574-640)
         = (32/45)*3300*2^-66.                         (7)

On panel j the affine length is b_j. Since2n_j>=64+288b_j,
the angular rule has error uniformly in real x at most

    (32b_j/45)*(118/b_j)*2^(288b_j-2n_j)
       <84*2^-64.

Summing all48 panels gives E_y<=48*84*2^-64. To check tensor use
I_y I_x-Q_y Q_x=I_y(I_x-Q_x)+(I_y-Q_y)Q_x. The first term has
bound(7); Q_x has positive real weights of total1, so the second has
bound E_y from the uniform angular estimate. This pays both orders
without a hidden amplification by the number of radial nodes.

Combining(3),(7) and E_y gives exactly the rational upper bound(A).
This is an ideal rule with exact nodes, weights and function values.
The proposed256-bit grid is a design parameter only. An inclusion proof
for its constants, node/weight construction, elementary values,
near-diagonal kernel, neutral coefficients, products and accumulation
has not been supplied. Reserving the remaining tolerance cannot pay it.

### 6. First failure: mandatory direct-contraction work

The first seven angular panels have ceil(144b_j)=72,36,18,9,5,3,2;
the remaining41 panels have ceiling1. Thus their total point count is

    sum_j(n_j+1)=48*33+(72+36+18+9+5+3+2+41)=1770.

There are321*1770=568170 ordered scaled-node keys. Complete exact
comparison with the pinned archive shows that every one of the762
free coefficients is nonzero:127 even and127 odd in EACH of three
columns. Each appears in precisely one parity density, with a nonzero
normalization. Under the stated direct accumulation prescription it
therefore causes at least one real multiplication at every scaled-node
key. Shared cosine generation does not eliminate those three separate
column multiplications. The unscaled values are already cached and
are not counted; both triangle uses of a scaled density share it.
This proves(B). Even granting cost-free cosine values, kernels and
all preprocessing cannot bring this prescribed count below20million.

This is the first decisive execution failure. No need to complete
finite-arithmetic enclosures or run a batch remains under this rule.
The ideal-node bound is not called a certified finite computation.
The degree choices came from(5)-(7); they are sufficient and not
asserted optimal. Smaller degrees, structured contraction, low-rank
kernel approximation and other methods are not excluded, but are
not authorized retunings of this stopped prescription. This result
does not extend657/660/662's stops into a ban on direct square methods.

Reproduce only the meaningful finite planning checks with

    python3 scripts/separation-seven/duffy-square-ledger-672.py

The full certificate is
`scripts/separation-seven/duffy-square-ledger-672.json`. It reads all
654/655 checks and rational ledgers, pins the complete654 certificate
through655, compares all762 dyadics to the original archive, recomputes
each amplitude envelope, saves all48 panels and exact error/cost
values, and checks preservation of all loaded inputs. No mathematical
identity, ellipse proof, source contract or actual integral is verified
by this integer/rational script. Their separate critical review is below.

### 7. Independent conceptual audit — 12 November 2026, step674

Invocation-start SPECIALIZE assessment673 covers precisely this audit.
The primary substitution, Fubini and analytic Gauss hypotheses quoted
above are reused from assessments670/655; no general theorem is reproved.
All assertions(A),(B),(1)-(7) survive unchanged. This is verification of
the existing specialization, not a new theorem or affordable evaluator.

**Definitions and absolute integrability.** C999q's exact moment ratio
gives C998a(6), for both signs of the moment and each parity. In the
unitary map(4), the odd cosine receives the minus sign, but its block
still has Carleman coefficient1/2. Expansion therefore gives exactly
both mixed terms and the1/4 square in C998e(7). The bounds in Section1
hold for the absolute complex products before any interchange. In
particular the triple integral is bounded by196a[(log2)^2+2log2+2],
which is finite and less than980a. This verifies the sigma-finite
Folland hypotheses, rather than relying on conditional cancellation.
The moment Gram is real symmetric: direct integration gives its three
entries, and its determinant exceeds ell^4/12>1/192, since ell>1/2.
With first-slot-linear inner products and real representers,
C(Wz)=G_w z; the removed pairing is mu_i^*G_w^-1 mu_j. Thus the
projection order and complex extension in C998e(8) are correct. This
check does not import C998e's later quantitative or inverse claims.

**Finite-cell transformation and corner.** Substituting s=ax,u=axy
in the positive integral defining K_0, its Jacobian a^2x leaves exactly
aW. Evaluating the integral from y to1 of1/[z(1+xz)] yields the two
logarithms in(1), including the finite-end correction. At y=1 its value
is1/(1+x), and at x=0 it is h(y); the only remaining singular boundary
is y=0. The two triangles each retain their own ordered column product;
together with two parities these give four products and total bound
196a h(y). For0<y<=1, the inequality -y log y<=1-y implies
h(y)<=1-log y. Integrating gives eta(2-log eta). With eta=2^-48,
log2<1 and a<3/10, the stated corner allowance follows without
omitting an axis strip, changing the upper endpoint or assuming a sign.

**Holomorphy and tensor error.** The bound14 is a coefficient-sum
envelope, including the neutral modes0/1, because r_n<1 and
sqrt(2)nu_n<3. Thus each parity sum is bounded by its coefficient mass
times exp(510|Im z|); a real supremum is not used as a complex bound.
For radial rho=2, Re x>=-1/8 and |Im x|<=3/8. Since the integration
variable z in W is real in[y,1], |1+xz|>=7/8, uniformly for real
y>=eta. The two exponential factors sum to at most765/2.
For angular rho=2 on[b,2b], Re y>=7b/8, |Im y|<=3b/8 and
Re[t+(1-t)y]>=7b/8; with real x>=0 also Re(1+xz)>=1.
These strict bounds extend to neighborhoods of the closed ellipses
and justify holomorphy under the finite t integral. They yield the
prefactors3292.8<3300 and117.6/b<118/b, respectively, with the
exponents in(5)-(6). The real-trace products are holomorphic; conjugating
a complex quadrature argument would not be licensed.

Trefethen19.3's affine multiplier is d/2, so at rho=2 its constant
is32d/45. Its n is points minus1, giving radial n=320 and the stated
angular n_j. The retained y-length is less than1, and the exact radial
Gauss weights are positive with total1. Therefore the displayed tensor
decomposition uses only the separately uniform one-variable bounds;
neither a joint complex estimate nor a node-count amplification is
needed. The rational sum is exactly(A). No finite-arithmetic error
has been paid by this conclusion.

**Complete finite evidence and work scope.** The independent verifier
does not import or run either previous generator:

    python3 scripts/separation-seven/duffy-square-audit-674.py

Its full certificate is `scripts/separation-seven/duffy-square-audit-674.json`.
It checks the full654/655/672 check lists and empty failure lists,
all recorded input and generator hashes, all762 archive dyadics against
654 and672, all33 rational ledger entries independently from the exact
arrays, all48 panel records and the complete error/work ledger. All89
checks pass; every loaded input is preserved. The exact corner, radial
and angular bounds are respectively735/70368744177664,
55/1729382256910270464 and63/288230376151711744.

There are127 nonzero even and127 nonzero odd free coefficients in
each column. By the explicitly prescribed direct coefficient-times-basis
accumulation, each ordered scaled-node key incurs all762 multiplications;
the unscaled cache, shared cosine basis and shared triangle uses already
remove those duplicate costs. The rule expressly excludes merging keys,
mode pruning or a structured coefficient contraction. Hence321*1770*762
is a valid lower count for this rule, and it exceeds the20million cap.
It says nothing about necessary complexity for another rule. This audit
does not revive the stopped prescription or pay finite arithmetic,
actual entries, residual/inverse debt, signed S3 or the original
analytic/arithmetic/source-to-Xi/whole-core/c_* contracts. The existing
direct mathematical inputs C998a,C998e,C999q suffice; no DAG edge changes.

## Mathlib

Full matching coverage for this fixed-data Duffy identity, quantitative
ellipse ledger and prescription-specific work result was not checked.
Unknown coverage is not evidence of absence. Product integration,
orthogonal projection, finite cosine bounds and analytic Gaussian
quadrature are supporting mathematics; the exact imported theorem
versions and local applicability arguments are given above. No formal
proof or result beyond the checked standard methods is claimed.
