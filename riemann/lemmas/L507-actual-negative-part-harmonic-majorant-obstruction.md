# Lemma 507: actual negative-part harmonic-majorant obstruction

## Hypotheses

Fix R>0 and T>exp(1), and use L504's definitions

    L=log T, a=log L/pi, b=a/4, B=L/(4pi),
    O=[-a,a] times [b,B],
    Omega={(x,y): y>0} minus O.

Thus 0<b<B: L>1 and log L<L. Conditional on its existence, fix
f in L504's H_a. In full, f is entire, even and real on the real axis,

    f(z)=integral_R phi(v) exp(2pi i v z)dv,
    phi in C_c^infinity(R), supp phi subset [-R,R],

and, writing u(x,y)=Re f(x+iy), it satisfies

    u(x,y)>=1 for |x|<=a and b<|y|<B.

The hypothetical majorant G is finite-valued, nonnegative and harmonic
on the open set Omega, with

    G(x,y)>=max(0,-u(x,y)) throughout Omega.          (1)

No boundary continuity, boundary values or growth bound is assumed
for G. The statement neither assumes nor proves H_a nonemptiness.

The imported classical inputs are:

- S. Axler, P. Bourdon and W. Ramey, *Harmonic Function Theory*,
  second edition, corrected 17 July 2020,
  [Theorem 7.26, printed pp. 158--159](https://www.axler.net/HFT.pdf).
  In dimension two, a positive harmonic function on t>0 has the form
  c t plus the Poisson integral of a positive measure on R, with
  c>=0 and finite integral against (1+s^2)^(-1). This includes its
  mass at infinity. Nonnegative functions will be handled by adding
  a positive constant and then taking a limit.
- L. F. Demkowicz, *Lecture Notes on Non-Self Adjoint Operators and
  Related Topics*, version 4 December 2024,
  [Theorem 3.9 and proof, printed pp. 42--43, PDF pp. 50--51](https://www.oden.utexas.edu/media/pending_reports/book.pdf).
  The sector Phragmen--Lindelof theorem applies to an analytic function
  continuous on the closed sector, bounded on its two rays, with
  exponential growth exponent strictly less than pi/(sector angle).

These theorem statements and their relevant proof cases were inspected
in the previously approved source assessment. They are imported here,
not reproved. The proof below checks their local applicability; it is
a classical specialization, not a claim of progress beyond the checked
source methods. ABR Theorem 3.4, also covered by that assessment, is
not needed. L506 is a contrast only, not a mathematical input.

## Conclusion

The existence of G satisfying (1) would force f to vanish identically.
This contradicts the defining rectangle positivity of H_a. Hence no
such G exists for any f in H_a, conditional on such an f being given.

This excludes a finite nonnegative harmonic majorant of the *actual*
linear negative part on this exterior domain, without a growth
restriction on the majorant. It is distinct from L506's prescribed
exponential-envelope obstruction. It does not prove divergence of
actual finite-truncation costs: extracting a majorant from bounded
costs would require a separately justified comparison and compactness
argument. It neither refutes the desired Q_a bound on H_a nor controls
the bottom kernel, gives T-uniform quantitative estimates, realizes
detectors for Xi, or proves any Xi signs or RH. The local application
passes the independent critical audit of 30 October 2026 recorded below;
this verifies the existing classical specialization, not a new bound.

## Proof

### Restriction and the term at infinity

Put h=B+1. The whole half-plane y>h lies in Omega. On t>0 set

    H_0(x,t)=G(x,h+t),
    H_1(x,t)=G(x,h+t)+u(x,h+t).

Both are finite and harmonic. They are nonnegative because G>=0 and
G>=-u. In particular no harmonic extension across O is being made.

For either H=H_0 or H_1 and any epsilon>0, ABR Theorem 7.26 applies
to the strictly positive function H+epsilon. With the standard
two-dimensional Poisson normalization it gives

    H(x,t)+epsilon
      =c_epsilon t+(1/pi) integral_R
                    t/((x-s)^2+t^2) dmu_epsilon(s),          (2)

where c_epsilon>=0, mu_epsilon is positive and
integral_R (1+s^2)^(-1)dmu_epsilon(s)<infinity. No assertion is made
that c_epsilon vanishes or that mu_epsilon is a finite measure.
At x=0 and t>=1, the pointwise inequality

    t/(s^2+t^2)<=t/(s^2+1)

and (2) at height one imply

    H(0,t)+epsilon<=t[H(0,1)+epsilon].

The linear term c_epsilon t is retained exactly. Letting epsilon
decrease to zero for fixed t gives

    H(0,t)<=t H(0,1) for every t>=1.                (3)

Only positivity and finiteness at the reference point have been used;
there is no extra bound on G at infinity or on the obstacle boundary.
With C_0=H_0(0,1)+H_1(0,1), which is finite and nonnegative, (3) gives

    |u(0,h+t)|=|H_1(0,t)-H_0(0,t)|<=C_0 t
    for t>=1.                                      (4)

### Symmetry supplies the modulus bound

Reality of f on R and the identity theorem give
f(conjugate z)=conjugate f(z). Evenness therefore implies, for real y,

    conjugate f(iy)=f(-iy)=f(iy).

Thus f(iy) is real and |f(iy)|=|u(0,y)|. This equality is used only
on the imaginary axis; no modulus bound is inferred from a real-part
bound elsewhere. By (4), |f(iy)|<=C_0(y-h) for y>=h+1. Continuity of
the entire f on the remaining compact interval 0<=y<=h+1 supplies a
finite constant C_1 such that

    |f(iy)|<=C_1(1+y) for every y>=0.               (5)

For example take C_1 to be the maximum of C_0 and
sup_{0<=y<=h+1}|f(iy)|/(1+y).

Let A=integral_R |phi(v)|dv. The defining Fourier integral yields

    |f(x+iy)|<=A exp(2pi R |y|).                    (6)

Also f(x) tends to zero as |x| tends to infinity: for x!=0, integrate
by parts once in that integral to obtain

    |f(x)|<=||phi'||_1/(2pi |x|).

There is no endpoint term because phi is globally smooth with compact
support. The bound |f(x)|<=A holds on all of R.

### A pole-free normalization in both upper quadrants

Define F(z)=f(z)/(z+i). Its only possible pole is at -i, outside the
closed upper half-plane. It is analytic on an open neighborhood of
each closed upper quadrant and continuous on their boundary rays,
including the origin. For y>=0 one has |x+i(y+1)|>=1, so (6) gives

    |F(x+iy)|<=A exp(2pi R |x+iy|).                 (7)

On the real axis |F(x)|<=A; on the positive imaginary axis (5) gives
|F(iy)|=|f(iy)|/(1+y)<=C_1. Take M=max(1,A,C_1).

Each upper quadrant has angle pi/2 and hence sector parameter 2.
The growth in (7) has exponent 1, strictly less than 2. If the sector
statement is phrased with a unit coefficient in a bound exp(r^rho),
(7) implies that bound for all sufficiently large r with rho=3/2<2.
Thus Demkowicz Theorem 3.9 applies to the first upper quadrant and,
by rotation, to the second. All their ray bounds are at most M.
It follows that

    |F(z)|<=M for Im z>=0,
    |f(z)|<=M|z+i|<=M(1+|z|) there.                (8)

This uses the strict quadrant theorem, not the order-one endpoint
in a half-plane. No pole lies on an integration domain or ray.

### Global growth forces the contradiction

For Im z<0, reflection gives |f(z)|=|f(conjugate z)|. Applying (8)
at conjugate z proves the same bound M(1+|z|) on the lower half-plane.
Hence the entire function has this bound on every circle |z|=r.
For every integer n>=2, the Cauchy coefficient estimate gives

    |f^(n)(0)|/n!<=M(1+r)/r^n.

Let r tend to infinity. Every Taylor coefficient of degree at least
two vanishes, so f is a polynomial of degree at most one. Evenness
makes it constant, and the real-axis decay proved above makes that
constant zero. But 0<b<B and a>0; at x=0 and y=(b+B)/2 the H_a
hypothesis requires Re f(iy)>=1. This contradiction proves the claim.

All constants here may depend on f,G,R,T. The proof is qualitative
at each fixed R,T and involves no limit in T, no unproved H_a
existence, and no sequence of finite-domain extensions. Its only
notebook input is L504's function-class and obstacle definitions.

### Independent critical audit, 30 October 2026

Verdict: the implication and its stated qualifications pass. The audit
reopened the two primary PDFs at the cited statements and relevant proof
cases, including ABR (7.25)--(7.26) and the complete sector damping
argument. No stronger theorem, new notebook input or mathematical repair
was required. The load-bearing checks were:

1. Restriction above h=B+1 uses a subset of Omega, not an extension.
   Finiteness and harmonicity of H_0,H_1 hold at every reference point.
   For H+epsilon, finiteness at (0,1) supplies precisely the weighted
   measure integrability required in (2). The comparison retains
   c_epsilon t on both sides. The limit in epsilon is only of the
   displayed scalar inequality at fixed t; no convergence of measures
   or constants c_epsilon is needed. This also covers H identically
   zero, without applying a strictly positive theorem to it directly.
2. Reflection and evenness both enter the imaginary-axis modulus
   identity. Bound (4) alone would not control the imaginary part of a
   general entire function. The compact-interval constant in (5) is
   legitimate even when G has no continuous boundary values.
3. The normalization is analytic near both closed quadrants, including
   zero. For an explicit check of the second rotation, apply the first
   quadrant theorem to F(i z); its possible pole is at z=-1, outside
   that quadrant. Its positive real ray maps to the imaginary ray and
   its positive imaginary ray to the negative real ray, both bounded.
   The source's asymptotic condition follows from
   log A+2pi R r<=r^(3/2) for sufficiently large r when A>0;
   A=0 already makes f=0. Thus 3/2<2 supplies strict sector slack,
   and no half-plane endpoint theorem is used.
4. Reflection of f, not of its meromorphic normalization, propagates
   (8) to the lower half-plane. Cauchy estimates hold on every circle;
   their limit eliminates all coefficients of degree at least two.
   Evenness and the justified real-axis decay then give f=0. For
   T>exp(1), the test point (0,(b+B)/2) is strictly within (H).
5. The only local input is L504's explicitly restated definitions.
   Positivity of (H) is used for the final contradiction, not to assume
   existence of a member or to control G outside its stated domain.
   Neither finite-domain compactness nor an actual-Xi specialization
   occurs. No numerical or formal verification is claimed.

The audit changes the provisional route stop to an audited one. It
finds no mathematical defect, additional estimate or progress beyond
the existing source specialization; repeating this implication is not
a new research result.

## Mathlib

Coverage of this full finite-obstacle specialization, ABR's positive
half-plane representation and the exact strict-sector theorem has
not been checked in Mathlib. The proof also uses the standard identity
theorem, Cauchy coefficient estimates and Fourier integration by parts;
no matching formal theorem names have been verified. Unknown coverage
is not an assertion of absence. No formal proof or numerical evidence
is claimed.
