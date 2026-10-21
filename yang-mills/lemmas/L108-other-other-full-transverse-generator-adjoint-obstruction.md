# L108 — Full-generator adjoint symmetrization does not gain a mesh power

## Hypotheses

Use L095/L099's actual transverse-displacement generator G=G_tr,
straight lower-rooted direction-1 forest, relative all-face pinned box
(-4,4)^4, admitted even N, a=8/N, and the actual L008 displacement.
Coordinates, adjoints and norms are ordinary stored ones. On each
interior axial level let D be the dimensionless transverse circulation,
P the orthogonal relative gradient projection, and Q=I-P. Let Pcal,Qcal
be their levelwise extensions. All components and endpoint/clover
filters of G are retained. Put S=(G+G^T)/2 and T=(G-G^T)/2.

For the trace statement retain both L010 probes i=3,6, tau=1/16,
all heat modes, all pinned rows and all interior axial levels. Import
L099(2), with A_k=Pcal Omega_k Qcal and symmetric real c_(i;kl,a).
The fixed-mesh bare small-coupling coefficient precedes refinement.

## Conclusion

For all sufficiently fine admitted meshes,

    1/(16a) <= ||Qcal S Qcal|| <= C/a.                    (1)

This concerns the complete generator on exact co-closed inputs.
It is different from the individual transport/projection commutator
obstruction in L096. Thus full-generator adjoint symmetrization alone
does not give a uniformly bounded symmetric generator on that range.

There is also the exact pinned identity

    B_i=sum_(k,l)c_(i;kl,a) A_l^T K_g A_k,  B_i^T=B_i,
    R_H,tr=Tr(K_h B_i G)
      =1/2 Tr((K_h B_i+B_i K_h) S)
       +1/2 Tr((K_h B_i-B_i K_h) T).                    (2)

The first term cannot be controlled by replacing Qcal S Qcal with
an O(1) operator bound. No lower bound for either term of (2), either
actual probe response, or the complete other/other cumulant follows.
A signed identity retaining the actual B_i and its covariance order
can still gain a mesh power. The a^3 limit, compensation with L084,
finer powers/logarithm, other jets, interacting matching/error,
continuum axioms, reflection positivity and infrared/mass control
remain unresolved. This is a route obstruction, not a disproof of
the finite-limit target or of Yang–Mills existence.

## Proof

### 1. Keep the full finite adjoint identity

L099(2) gives the middle expression of (2); no Wick contraction is
rederived. Transposing B_i and exchanging k,l proves symmetry because
K_g is symmetric and the complete exterior coefficient sum is
symmetric. Also Qcal B_i Qcal=B_i and Qcal K_h Qcal=K_h.
All sums here are finite at each mesh. For real symmetric matrices
K,B and real S^T=S,T^T=-T, transposition and cyclicity give

    Tr(K B S)=Tr(B K S),
    Tr(K B T)=-Tr(B K T).

Adding G=S+T proves (2) on the actual finite spaces. It keeps
min(s,t) in K_g and the two separate coefficient levels in B_i.
It neither commutes a transverse multiplier past P nor replaces
the covariance by a static, periodic or massive one.

### 2. Choose an exact co-closed compact packet

Fix a nonzero real smooth eta supported in

    (-1,1) x (-1,1) x (1/2,3/2)

in coordinates (x_2,x_3,x_4), and put J=integral eta^2>0.
Use the axial level s=N/2, whose physical coordinate is x_1=0.
Every relevant coefficient/stencil lies in L008's affine core for
small a; there u_(a,T)=(x_2,-x_3,-x_4) exactly.

Use component-center phases at the carrier

    theta=(pi/3,pi,0), d=(1,2,0),
    e=(2,-1,0), f=(0,0,1), z=e-i f=(2,-1,-i).

Both e and f are perpendicular to d. In plane order 23,24,34,
L088(11)'s circulation symbol is

    D_theta=[[-2i,i,0],[0,0,i],[0,0,2i]].

Set p=(-i,1/5,2/5). Direct multiplication gives

    D_theta^* p=z,  ||z||^2=6.                          (3)

On each transverse plaquette center xi sample

    (psi_N)_(mu nu)(xi)
       =a^(3/2) p_(mu nu) eta(xi) exp(i theta dot j(xi)),

where j(xi)=(xi+4)/a has the usual half-integer offsets in that
plaquette's two directions. Set y_N=D^T psi_N on the actual relative
edge space, and set all other axial levels to zero. The compact
support and a fixed extra stencil collar are strictly inside the box.
The cochain identity D grad=0 implies grad^T y_N=0 exactly. Hence
Qcal y_N=y_N, without approximating the nonlocal projection.
Tangential boundary values and normal end rows are retained; the
packet is zero in their neighborhoods.

For reference define the edge packet

    (v_N)_nu(xi)=a^(3/2) z_nu eta(xi) exp(i theta dot j(xi)).

All the stencils in D^T have fixed range. Replacing an envelope at a
shifted point by its value at the output costs at most C a. Their
carrier phases transform exactly, with symbol (3). There are O(a^-3)
support rows and bounded repetitions, so

    ||y_N-v_N|| <= C a,  ||y_N||^2 -> 6J.                (4)

Indeed each error entry is O(a^(5/2)); its squared sum is O(a^2).
The norm limit follows by ordinary staggered-grid Riemann sums.
No spectral cutoff, inverse approximation or boundary extension
error is present in this fixed-stencil calculation.

### 3. Compute the full generator, including the cross terms

Import L088(14), restricted exactly as in L099(8) to transverse
displacements. At this carrier its complete frozen symbol is iW/a,

    W=E[ sigma I-d v^T ],
    E=diag(3/4,0,1),
    v=(sqrt(3)x_2/2,0,-x_4), sigma=v^T d=sqrt(3)x_2/2.

Here v is only a three-component coefficient vector, distinct from
the edge packet v_N. All nine component entries of the generator
are included. They reduce at this carrier to

    W_24=3x_4/4, W_44=sqrt(3)x_2/2,
    every other W_(nu rho)=0.                           (5)

The zeros follow from the carrier's eta_3=0 and d_4=0 and from
the exact diagonal/cross cancellation in component 2; they are not
deleted input or output components. In particular the surviving
W_24 is a cross-component curvature term of the full generator.
Consequently

    Re(z^* iW z)=e^T W f-f^T W e=3x_4/2.                (6)

The diagonal W_44 contributes only an imaginary scalar to z^* iW z.
Thus the symmetric generator has a nonzero co-closed quadratic
form even though G annihilates gradients exactly.

For a finite-mesh error estimate, L009(3) is a fixed sum of
incidences, clover/output averages and one smooth u_a multiplier,
with one factor 1/a. All coefficients have uniformly bounded
physical first derivatives on the packet support. Changing their
or eta's evaluation point by a stencil offset costs O(a), including
the coefficients in the adjoint. Applied to v_N, each remainder
entry is O(a^(3/2)); summing O(a^-3) entries gives O(1) norm.
The same finite-stencil estimate gives ||G||<=C/a. Therefore (4)
also controls G(y_N-v_N) by O(1), and

    (G y_N)_nu(xi)
       =a^(1/2)(iW(xi)z)_nu eta(xi)
                    exp(i theta dot j(xi)) + r_N,
    ||r_N||<=C.                                        (7)

The leading coefficient at an edge midpoint is evaluated in the
affine core. Choosing any of its adjacent coefficient vertices
changes it by O(a), already covered in (7). Outside the fixed
packet/stencil support both sides vanish. Thus (7) is a global
finite-domain norm estimate, not an infinite-grid approximation
with unbounded boundary error.

Since S is real symmetric, y_N^* S y_N=Re(y_N^* G y_N).
Using (4),(6),(7), Cauchy–Schwarz for their errors, and staggered
Riemann sums yields

    a y_N^* S y_N -> (3/2) integral x_4 eta^2,
    lim a (y_N^* S y_N)/||y_N||^2
       = (integral x_4 eta^2)/(4J) >= 1/8.              (8)

In the first pairing, replacing y_N by v_N costs O(a) after
multiplication by a, since ||y_N-v_N||=O(a) and ||G y_N||=O(1/a).
The r_N contribution is O(a). This accounts for every discarded
order. The last inequality uses x_4>=1/2 on the support.

Because Qcal y_N=y_N, (8) implies the lower bound in (1), with
1/16 in place of the limiting lower bound 1/8 for all sufficiently fine meshes.
Complex packets do not change the real operator bound: write
y_N=x_N+i w_N. The real symmetric quadratic form and norm are
respectively the sums of their values on x_N and w_N, so one
nonzero real part has at least the same Rayleigh quotient. Both
parts are exactly co-closed. Finally ||Qcal S Qcal||<=||G||<=C/a
proves the upper bound and completes (1).

### 4. Scope of the failed gain

The hoped-for O(1) symmetric-generator bound would have supplied
one cubic estimate in (2): L095(7) gives
||(B_i)_st||<=C_i min(s,t)a^2<=C_i a, and L095(14) gives
sum_st ||(K_h)_st||_1<=C N^4. A bounded level-diagonal symmetric
generator would therefore make the corresponding trace O(a N^4),
which is O(N^3). Equation (1) refutes that particular sufficient
shortcut. The commutator term of (2) would still need an estimate
even if that shortcut were valid.

Crucially, y_N in (8) is a probe-independent oscillatory test vector,
not an exterior column in B_i. No inequality relates its quadratic
form to Tr(K_h B_i G). The latter retains signed alternating factors,
the full prefix covariance and the external heat coefficients.
The packet therefore proves no signed trace growth, no stronger
power and no failure of its a^3 limit. L099's zero quartic-scale
result and its legitimate frozen trace cancellation are unchanged.

This is RESEARCH / REPRODUCTION under the unchanged approved complete-
group EXPLORE assessment. The fixed contraction and generator symbols
are imported; the new local specialization tests their complete
adjoint on exact pinned co-closed packets. It is new local decision
evidence, with no claim of originality beyond the sources checked.
No reproof of a literature theorem or numerical value of D_i is used.
Any later numerical comparison retains L082's IEEE qualifications
through L084.

## Mathlib

Full matching obstruction: **not checked**. Supporting finite trace,
cochain complex, real symmetric quadratic-form, finite-stencil and
Riemann-sum coverage: **not checked**. Unknown coverage is not absence.
