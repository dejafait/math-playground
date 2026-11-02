# Lemma 617: localized potential cusp at a finite real heat multiple zero

## Hypotheses

Let F(lambda,z) be the exact theta heat family of L058, with the kernel
and zero-time convention of L019/L020. Thus F is jointly entire,
F_lambda=-F_zz, and its real-time slices are not identically zero.
Suppose lambda_*>0, x_* is real, and F(lambda_*,.) has a zero of exact
finite multiplicity m>=2 at x_*. Existence of such a zero is assumed,
not asserted. All constants below may depend on this zero and the test.

Choose a sufficiently small disk D centered at x_* and a fixed real
phi in C_c^infinity(D), nonnegative and equal to one on a neighborhood
of x_*. The precise allowed size of D is the preparation neighborhood
chosen in the proof; D isolates this zero at lambda_*.
With planar Lebesgue area dA=dx dy, set

    U_0(lambda)=(1/2) integral_D phi(z) log|F(lambda,z)| dA(z),
    U_epsilon(lambda)=(1/4) integral_D phi(z)
                              log(|F(lambda,z)|^2+epsilon^2) dA(z).

Time, D and phi remain fixed when epsilon decreases to zero.

## Conclusion

For some real b and a sufficiently small two-sided real time interval,
writing t=lambda-lambda_*,

    U_0(lambda_*+t)
      =U_0(lambda_*)+b t+(pi/2)m(m-1)|t|+O(|t|^(3/2)).           (1)

In particular, for h>0 decreasing to zero,

    U_0(lambda_*+h)+U_0(lambda_*-h)-2U_0(lambda_*)
      =pi m(m-1)h+O(h^(3/2)),                                  (2)

so the proposed liminf is the limit pi m(m-1)>0. This holds for every
finite m>=2, including odd multiplicities, without radial symmetry of
phi. The coefficient uses phi=1 near the zero and the stated area and
one-half-logarithm conventions.

For each fixed time in this interval, U_epsilon tends to U_0.
Consequently there cannot exist finite C and positive h_0,epsilon_0,
all independent of h and epsilon, such that

    U_epsilon(lambda_*+h)+U_epsilon(lambda_*-h)
                  -2U_epsilon(lambda_*) <= C h^2                (3)

for every 0<h<h_0 and 0<epsilon<epsilon_0. This is a conditional
incompatibility at the assumed multiple zero, not a proof that an
upper bound holds elsewhere or that a multiple zero exists.

## Proof

### Known inputs, source scope and the required specialization

Use L058 for joint holomorphy and its heat normalization; use L059
for the double-zero splitting and L060 for higher finite multiplicity.
These are conditional local inputs, not new splitting results here.
The primary comparison for finite-multiplicity splitting is
D. H. J. Polymath, *Effective approximation of heat flow evolution of
the Riemann xi function, and a new upper bound for the de Bruijn-Newman
constant*, Research in the Mathematical Sciences 6 (2019), article 31,
[arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2),
Proposition 3.1(ii), equations (29)-(30) and its repeated-zero proof.
The local inputs already express the splitting in F_lambda=-F_zz
coordinates; no external time or spatial scale is substituted here.

The planar fundamental-solution identity used below is

    Delta_a log|a-w|=2pi delta_w.                               (4)

It is the one-variable Lelong-Poincare formula. A precise primary
reference is El Amrani-Jeddi, *A geometric proof of the Lelong-Poincare
formula*, Proyecciones 32(1) (2013), 1-13, unnumbered theorem p. 2,
local preparation/integrability proof pp. 4-5 and repeated-factor
case p. 8, DOI 10.4067/S0716-09172013000100001,
[primary PDF](https://www.scielo.cl/pdf/proy/v32n1/art01.pdf).
The normalization agrees with L616; that finite quartic result is
comparison evidence, not a mathematical premise of this proof.

We also use the standard named Weierstrass preparation theorem,
holomorphic residue theorem and harmonic-conjugate theorem on a disk.
Their local hypotheses are verified below. The gate assessment is
`drafts/literature/2026-11-01-actual-heat-multiple-zero-potential-diagnostic.md`.
This is a reproduction/specialization of these tools: the sources do
not supply the full compact-test expansion (1). The missing factor,
cutoff and real-time limiting arguments are supplied here; splitting
and general current theory are not reproved.

### Fixed preparation neighborhood and complete potential

Translate the spatial coordinate by x_* and time by lambda_*:
f(t,w)=F(lambda_*+t,x_*+w). Exact finite multiplicity means
f(0,w)=a w^m+O(w^(m+1)), a nonzero. Weierstrass preparation at (0,0)
gives a complex polydisk and a factorization

    f(t,w)=E(t,w) W(t,w),
    W(t,w)=w^m+a_(m-1)(t)w^(m-1)+...+a_0(t),                   (5)

where E is holomorphic and nowhere zero, the a_j are holomorphic,
and every a_j(0)=0. Before fixing D, shrink the polydisk so that
|E(t,w)/E(0,0)-1|<1/2 throughout it. Choose D with
closure inside its spatial disk. All m roots of W lie in any prescribed
smaller disk about 0 for sufficiently small complex |t|: on the
boundary circle W(t,w) tends uniformly to w^m, so Rouche's theorem
counts all m roots there. There are no other zeros of f in D, by (5).
In particular D isolates the assumed zero at t=0. Choose phi as in
the hypotheses and put psi(w)=phi(x_*+w), extended by zero to C.

E has a holomorphic logarithm L on this already chosen polydisk:
use the convergent logarithm series for E/E(0,0), plus any logarithm
of E(0,0). All subsequent shrinkings are in time or in the root and
trace disks; the integration disk D and the test remain fixed. Set

    A(t)=(1/2) integral_C psi(w) L(t,w) dA(w),
    V(a)=(1/2) integral_C psi(w) log|w-a| dA(w).                 (6)

A is holomorphic in complex t: the compact spatial support lies
strictly inside the polydisk, where L and its time derivatives are
uniformly bounded on smaller time disks; integration preserves
holomorphy by dominated differentiation or Cauchy's formula.

Let w_1(t),...,w_m(t) denote the roots of W at a fixed time, repeated
according to multiplicity. No holomorphic labeling in t is assumed.
Factorization and local logarithmic integrability give the exact identity

    U_0(lambda_*+t)=Re A(t)+sum_(j=1)^m V(w_j(t))               (7)

for every sufficiently small real t, including 0. Indeed log|E|
is bounded on the support, while each root factor has the integrable
singularity log|w-w_j|: its absolute area integral near the root is
bounded by a constant times integral_0^r u|log u| du, which is finite.
Thus the pointwise factorization off the finite zero set can be
integrated; it omits neither the nonzero factor nor the part of the
test away from the root.

### Harmonic part of the spatial potential

V is C^infinity as a function of the two real coordinates of a.
To see this directly, change variables to obtain
V(a)=(1/2) integral log|u| psi(u+a) dA(u). For a in any fixed compact
set, all differentiated test functions have support in one compact
set. Local integrability of log|u| permits every derivative to fall
on psi, proving the assertion. Identity (4) gives

    Delta_a V(a)=pi psi(a).

Choose a disk |a|<rho on which psi=1. Since Delta |a|^2=4, the
real function V(a)-(pi/4)|a|^2 is harmonic there. The disk is simply
connected, so a holomorphic H on it satisfies

    V(a)=(pi/4)|a|^2+Re H(a),       |a|<rho.                    (8)

This retains the entire cutoff in H; it does not replace phi by a
radial test. Fix 0<r<rho and shrink the complex time disk again so
that all roots of W lie in |w|<r/2 and W has no zero on |w|=r.
Define

    B(t)=(1/(2pi i)) integral_(|w|=r)
                             H(w) W_w(t,w)/W(t,w) dw.          (9)

The integrand is holomorphic in t near the fixed contour, with its
denominator bounded away from zero on smaller closed time disks.
Therefore B is holomorphic, including at t=0. The residue theorem
counts every root with its multiplicity and yields

    B(t)=sum_(j=1)^m H(w_j(t)),        B(0)=m H(0).

This proves holomorphy of the symmetric sum despite the branching
of individual roots. Combining (7)-(9) yields, for real t,

    U_0(lambda_*+t)=R(t)+(pi/4)sum_(j=1)^m |w_j(t)|^2,
    R(t)=Re(A(t)+B(t)),      R(0)=U_0(lambda_*).                (10)

In particular R is real analytic and R(t)=R(0)+b t+O(t^2) for a
real b. Hence both the nonzero factor and the full harmonic cutoff
contribution have symmetric time difference O(h^2).

### Root-square term and every finite multiplicity

For m=2 take alpha_1=-sqrt(2), alpha_2=sqrt(2) from L059. For
m>=3 use the real simple roots alpha_j of L060's monic polynomial

    P_m(v)=sum_(k=0)^floor(m/2)
                   m!(-1)^k v^(m-2k)/(k!(m-2k)!).

The same formula is v^2-2 when m=2. The coefficient of v^(m-1)
is zero and that of v^(m-2) is -m(m-1). Vieta's identities give

    sum_j alpha_j=0,
    sum_(i<j) alpha_i alpha_j=-m(m-1),
    sum_j alpha_j^2=2m(m-1).                                  (11)

L059/L060 supply all m roots in a fixed neighborhood in the form

    w_j(s)=alpha_j s+r_j(s),  |r_j(s)|<=C|s|^2,   t=s^2,       (12)

uniformly for complex s near 0. Shrinking the neighborhoods places
these in the disks already chosen, so they exhaust the roots used
in (10). For each j,

    ||w_j(s)|^2-alpha_j^2|s|^2|
       <=2|alpha_j|C|s|^3+C^2|s|^4.                           (13)

Choose s=sqrt(t) for t>0 and s=i sqrt(|t|) for t<0. The uniform
complex bound in (12) applies on both rays, and (11)-(13) give

    sum_j |w_j(t)|^2=2m(m-1)|t|+O(|t|^(3/2)).                 (14)

For odd m the unique alpha_j=0 has |w_j|^2=O(|s|^4)=O(t^2);
it cannot cancel the leading term. No assumption of simplicity at
t=0, choice of a real branch below zero, or inference from an
O(t) location error to reality is used. The known reality of all
alpha_j and the absolute-square estimate are sufficient.

Equations (10) and (14) prove (1). Adding the expansions at +h and
-h cancels b h, and dividing the remaining O(h^(3/2)) error by h
makes it tend to zero. This proves (2) and its strict threshold.
For m=2 the cusp coefficient in (1) is pi, agreeing with the finite
calibration in L616; the proof here addresses every finite actual-
family multiplicity and the full local potential independently.

### Fixed-time regularization limit and its permitted consequence

Fix any one real t in the chosen interval. Away from its finite
zero set, for 0<epsilon<=1,

    0 <= (1/4)log(|f(t,w)|^2+epsilon^2)-(1/2)log|f(t,w)|
       = (1/4)log(1+epsilon^2/|f(t,w)|^2)
       <= (1/4)log(1+1/|f(t,w)|^2).                            (15)

The upper bound is integrable on the test support. At any zero r
of exact order q, write f(t,w)=(w-r)^q g(w) with |g| bounded below
by a positive constant on a small disk. There (15) is at most
C+(q/2)|log|w-r||; off such disks it is bounded. The previous
polar-coordinate integral proves the required integrability also
at t=0, where q=m. Dominated convergence after multiplication by
the bounded compact test proves U_epsilon -> U_0 at this fixed
real time. Nothing is inferred by restricting an almost-everywhere
complex-time statement, and no derivative in time is interchanged
with this limit.

If (3) held on fixed h and epsilon intervals, take epsilon to zero
at the three fixed times lambda_*+h, lambda_*-h and lambda_*.
Their limits would give the same upper bound for U_0. Then divide
by h and let h decrease to zero. Equation (2) gives pi m(m-1)>0
on the left, while C h tends to zero, a contradiction. Independence
of both C and the time interval from epsilon is essential to this
argument; no such contradiction is claimed for a shrinking interval.

### Qualifications and verification

This is conditional local progress, with no height-uniform constants,
global product, infinite sum or global zero labeling. Positive time
ensures that the small two-sided interval may be kept positive; no
theta-specific coercivity enters. The same proof uses only the local
heat splitting and analyticity. It supplies the actual-family bridge
for this diagnostic, but neither the assumed collision nor a way of
excluding it. The earlier upper-curvature source stop is sharpened
conditionally: proving such a bound at a prospective collision would
already rule out that collision. The bound itself remains unproved.

All verification here is analytic: (4) fixes the area constant,
Delta |a|^2=4 fixes (8), (11) fixes the coefficient for arbitrary m,
(13) bounds both time-ray errors, and (15) verifies the only epsilon
passage used. No numerical check can certify the hypothetical zero.
The independent conceptual audit below verifies this specialization
under its stated conditional hypotheses; it changes no conclusion.
Collision exclusion, all-height Xi signs, tails and zero time remain
open; this is not a complete candidate proof or disproof of RH.

### Independent conceptual audit — 1 November 2026

Rechecked the complete proof against L058/L059/L060 and the separately
approved source scope in
`drafts/literature/2026-11-01-l617-local-potential-cusp-audit.md`.
The primary citations above are reused, not newly audited manuscripts.
No theorem is being imported for the full compact-test conclusion.

The spatial neighborhood choices are compatible. Prepare f and choose
the logarithm polydisk first, then fix D and psi. Choose rho inside the
region where psi=1 and r<rho. Continuity of the Weierstrass coefficients
and Rouche counting allow one further time shrinking that puts every
root in |w|<r/2. Intersect this time disk with those of the finitely many
splitting branches, and for real times with |t|<lambda_*/2. No subsequent
restriction changes the test support or depends on epsilon. The minor
ordering clarification above makes this simultaneous choice explicit.

The cutoff and factor contribute exactly Re(A+B), not an uncontrolled
remainder. On |w|=r the denominator in (9) stays uniformly nonzero on
a smaller closed complex time disk. This makes B holomorphic at t=0
as well as away from it. A root of multiplicity q contributes residue
q H(root), so the coalesced zero at t=0 contributes m H(0); no trace
term is lost there. Smooth convolution and (4) give Delta V=pi psi;
thus (8) has coefficient pi/4 with dA=dx dy and U_0's factor 1/2.
In particular arbitrary nonradial parts of psi remain in H. A bounded
second derivative of Re(A+B) on a fixed smaller real interval gives
an O(h^2) symmetric difference for this complete contribution.

For all m the coefficients of P_m give sum alpha_j^2=2m(m-1).
The common finite branch bound in (12) yields the explicit estimate

    |sum_j |w_j(s)|^2-2m(m-1)|s|^2|
       <=2 C (sum_j |alpha_j|)|s|^3+m C^2 |s|^4.

This bound applies on both the real and imaginary s rays. When m is
odd the alpha_j=0 term has bound C^2|s|^4, so it is included without
asserting that an O(t) location error alone proves reality. L060's
separate central-branch argument is consistent, but its reality is
unnecessary for this absolute-square calculation. Multiplying by pi/4
and adding the two time expansions verifies both claimed coefficients
and the O(h^(3/2)) symmetric error; m=2 gives 2pi h in (2).

At each fixed time there are finitely many roots in D, the analytic
factor is nonzero, and a sufficiently small neighborhood of a root of
order q gives the integrable bound C+(q/2)|log|w-r|| in (15).
Outside these root neighborhoods compactness bounds the integrand.
The bound may depend on the fixed time; this is sufficient. For any
fixed h in the common interval apply dominated convergence separately
at -h, 0 and h, then pass the finite inequality (3) to the limit.
Only afterwards let h tend to zero. Its two sides divided by h tend
respectively to pi m(m-1) and 0. No uniform-in-time domination,
epsilon differentiation, nonlinear current product or inference from
an almost-everywhere complex-time statement is used.

Audit result: the stated all-finite-multiplicity conditional cusp and
fixed-interval uniform-epsilon obstruction pass. No coefficient,
hypothesis or claimed consequence required correction. L058 supplies
the family; L059 and L060 supply its local splitting. L019/L020 enter
through L058, and L616 is comparison only. The existing direct-input
DAG row therefore remains correct. This verifies a local known-tool
specialization, not progress beyond the cited general theory or an
independent theta sign estimate. No mathematical script was needed.

## Mathlib

Full matching coverage and supporting formalizations of Weierstrass
preparation, the planar logarithmic fundamental solution, harmonic
conjugates and holomorphic root traces were not checked in this step.
Availability is unknown, not asserted absent. The proof uses the
named classical inputs and the canonical local splitting results
specified above; it makes no claim of a Lean verification.
