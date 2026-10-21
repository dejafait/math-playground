# L046 — Exact conductor-eleven degree-five quotient and normalization

## Hypotheses

Let E0/Q be L039's audited global minimal curve
\(y^2+y=x^3-x^2-10x-20\). Use L043's audited entire integral relative
module M at level 11, oriented generators g_0,...,g_11, functional
\(\phi=(5/2,5,1)\), and normalization \(F_0=I/\Omega(E0)=\phi/5\).
Here I is the real integral of the common normalized newform and
\(\Omega(A)=\int_{A(\mathbf R)}|\omega_A|\) is the total real period.
Retain L043's published optimality/complete-isogeny-class and two-period
computational qualifications; this instance does not reprove that import.
Use audited L045's prime-degree period and full-relative transfer theorem.

All new arithmetic uses rational numbers. Full evidence is in
`scripts/conductor-eleven/five-isogeny/`. Reproduce from the notebook root:

```bash
python3 scripts/conductor-eleven/five-isogeny/build_certificate.py
python3 scripts/conductor-eleven/five-isogeny/verify_certificate.py
```

The fixed producer and distinct full verifier supply instance witnesses,
not universal software correctness. The separate critical audit below
passes. No infinite-order point, coefficient, central vanishing,
Sha or rank premise is assumed.

## Conclusion

The point P=(5,5) has exact order five on E0. Its quotient is the global
minimal nonsingular curve
\[
E:\quad y'^2+y'=x'^3-x'^2-7820x'-263580.
\]
There is a Q-rational degree-five isogeny \(\psi:E0\to E\) with geometric
kernel \(\{O,(5,5),(16,-61),(16,60),(5,-6)\}\). On the affine complement
of this kernel put
\[
L=x^2-21x+80=(x-5)(x-16),
\]
\[
N=x^5-42x^4+2163x^3-30420x^2+170498x-324599,
\]
\[
M_1=x^6-63x^5+x^4+1977x^3+7626x^2+11654x+6682.
\]
The complete rational map is
\[
x'=N/L^2,\qquad y'=(y+1/2)M_1/L^3-1/2.                 \tag{1}
\]
Every kernel point, including infinity, maps to [0:1:0]. For the
specified minimal differentials \(\omega_0=dx/(2y+1)\) and
\(\omega_E=dx'/(2y'+1)\),
\[
\psi^*\omega_E=\omega_0,\qquad
\Omega(E0)/\Omega(E)=5,\qquad F_E=\phi\quad\text{on all }M. \tag{2}
\]
In the unchanged twelve-generator order the target values are
\[
(-1,1,0,5,5/2,-5/2,-5,-5,-5/2,5/2,5,0).               \tag{3}
\]
Their exact common denominator is two. Thus every oriented rational-cusp
symbol belongs to (1/2)Z, and the least nonnegative all-module p-adic
denominator constant is \(C_E=v_p(2)\), in particular zero at every odd
prime. Any downstream use of L027 still requires its separate non-CM,
good-ordinary p>=5, primitive-branch and finite enclosure hypotheses.
This is a fixed known-algorithm reproduction, with no BSD resolution or
new result beyond the assessed sources.

## Proof

**Imports and specialization.** Import Jacques Vélu, *Isogénies entre
courbes elliptiques*, C. R. Acad. Sci. Paris Sér. A 273 (1971), A238--A241,
[Ghitza's English translation, §§2--3, equations (7)--(13), Remarks 2--3,
pp.2--4](https://aghitza.github.io/publications/translation-velu.pdf).
For a nonsingular Weierstrass curve and finite subgroup, equation (7)
constructs the quotient by summing over every nonidentity point; the
expanded coefficient formulas use one representative of each inverse
pair, plus all order-two points. Remark 2 concerns the normalized
differential and Remark 3 descent for a separable Galois-stable subgroup.
Import also [Sutherland, MIT 18.783 Fall 2025, Lecture 5, Corollary 5.2,
Theorems 5.8, 5.11, 5.15 and Remark 5.16, pp.2--8](https://math.mit.edu/classes/18.783/2025/LectureNotes5.pdf)
for the projective quotient/isogeny, descent and characteristic-zero
degree/kernel statements. Their characteristic restrictions hold over Q.
The finite rational calculations below establish the exact hypotheses and
identify (1) with that projective quotient; affine substitution alone is
not the proof that it is an everywhere-defined isogeny.

Import [Sutherland, Lecture 2, §2.2, pp.3--4](https://math.mit.edu/classes/18.783/2025/LectureNotes2.pdf)
for addition, doubling, inverses and infinity on a short model. The
checked coordinate change and inverse are
\[
X=x-1/3,\quad Y=y+1/2,\qquad x=X+1/3,\quad y=Y-1/2,
\]
giving \(Y^2=X^3-(31/3)X-2501/108\), with differential
\(dX/(2Y)=dx/(2y+1)\). Equivalently, on the long source equation,
a secant/tangent slope s gives
\(x(P+Q)=s^2+1-x(P)-x(Q)\) and
\(y(P+Q)=-y(P)-1+s(x(P)-x(P+Q))\).
For doubling s=(3x^2-2x-10)/(2y+1). These are exactly the cited
short-model formulas transported by the displayed inverse.

Import [Cremona, *Algorithms for Modular Elliptic Curves*, corrected
second edition (1997), §3.1, equations (3.1.2)--(3.1.3), Proposition 3.1.1,
pp.62--64](https://johncremona.github.io/book/fulltext/chapter3.pdf)
for invariants and integral-model discriminant transformation. The
already audited source is nonsingular and minimal by L039. No general
quotient, minimal-model or period theorem is reproved here: exact finite
arithmetic and polynomial identities are necessary to certify this
candidate, guard the source-extraction inconsistencies recorded in the
assessment, and verify the final model/differential conventions.

**Candidate and subgroup.** At x=5 the source cubic is 30, with ordinates
5,-6. At x=16 it is 3660, with ordinates -61,60. Starting at P, the
three nonvertical slopes are 5 for doubling, -6 for adding P to 2P,
and 5 for adding P to 3P. The formulas above give respectively
\[
2P=(16,-61),\quad3P=(16,60),\quad4P=(5,-6)=-P,
\quad5P=O.
\]
All four affine multiples are distinct and nonidentity. Hence P has
exact order five and they exhaust the finite subgroup minus O. The
separate verifier instead performs every addition on the displayed short
model, checks every multiple's equation and then transports back. All
points are rational, so the full subgroup is Galois-stable and real;
characteristic zero supplies separability. This is a finite-order kernel
witness, with no positive rational-rank implication.

**Vélu sum and full identities.** For centered ordinate Y=y+1/2, write
\(f(x)=x^3-x^2-10x-79/4=Y^2\). The two representatives (q,r) in
centered coordinates are (5,11/2) and (16,-121/2). The paired x-sum
from equation (7), using the addition law just given, contributes
\[
\frac{2(f(x)+r^2)}{(x-q)^2}+2-2x-4q
=\frac{t_q}{x-q}+\frac{u_q}{(x-q)^2},
\quad t_q=6q^2-4q-20,\quad u_q=4r^2.
\]
The two pairs give (t_q,u_q)=(110,121),(1452,14641). Therefore
\[
h(x)=x+\frac{110}{x-5}+\frac{121}{(x-5)^2}
       +\frac{1452}{x-16}+\frac{14641}{(x-16)^2}=N/L^2.
\]
For the same inverse pair, the centered ordinate equation-(7) contribution
divided by Y is
\[
-2+\frac{2(2x+q-1)}{x-q}
   -\frac{2(f(x)+3r^2)}{(x-q)^3}.
\]
Adding the initial Y and both pairs gives
\[
v(x)=1-\frac{110}{(x-5)^2}-\frac{242}{(x-5)^3}
       -\frac{1452}{(x-16)^2}-\frac{29282}{(x-16)^3}
=h'(x)=M_1/L^3.
\]
Thus (1) is the full equation-(7) quotient in our long coordinates,
rather than a different map selected by a software normalization flag.
The coefficient witnesses are
\[
\sum t_q=1562,\quad
\sum(u_q+q t_q)=671+37873=38544,
\]
so the expanded general-model formulas give
\(a'_4=-10-5(1562)=-7820\) and
\(a'_6=-20+4(1562)-7(38544)=-263580\), retaining a1=0,a2=-1,a3=1.
As independent complete identity checks, direct multiplication gives
\[
M_1=N'L-2NL',
\]
\[
(4x^3-4x^2-40x-79)M_1^2
=4N^3-4N^2L^2-31280NL^4-1054319L^6.                    \tag{4}
\]
The first identity proves the derivative equality. The second is exactly
the target equation after substituting (1) and multiplying by 4L^6;
it checks every coefficient, not sampled points. In `certificate.json`
the producer retains all map coefficients and rational-function residuals.
The distinct verifier uses sparse polynomial multiplication and cleared
cross products, computes both sides from the map and target, and checks
every coefficient is zero. It independently reconstructs both paired
equation-(7) expressions, rather than importing the producer's rational
function arithmetic or accepting its zero/success claims. Complete
zero-coefficient evidence is in `verification.json`.

**Exceptional points and degree.** L has exactly the two simple rational
roots 5,16. At q=5 or 16, the leading term of h is
\(u_q/(x-q)^2\), with u_q=121 or 14641, both nonzero. The leading term
of v is \(-2u_q/(x-q)^3\). At each of the two points over q, Y=±r!=0;
the centered equation shows x-q is a uniformizer. Thus x' has pole order
two and Y'=Yv has pole order three at each of the four points. In the
target projective chart [x'/Y':1:1/Y'] both nonconstant entries tend to
zero, giving [0:1:0] (centering Y' is a projective coordinate change
fixing infinity). At source infinity x,Y have poles two,three,
h/x tends to one and v tends to one, giving the same image. The
verifier checks all finite leading coefficients, nonzero source ordinates,
the full denominator factorizations, degrees and leading coefficients
at infinity. Away from these points the denominators are nonzero, so
(1) is finite and cannot have image infinity. There are no omitted
exceptional points. The cited projective quotient theorem therefore
identifies the everywhere-defined Q-map with this quotient. Its kernel
is exactly the five listed points, and separability gives degree five by
the cited Corollary 5.2. The target's nonsingularity is checked next.

**Target minimality and final differential.** Exact invariants are
\[
(b_2,b_4,b_6,b_8)=(-4,-15640,-1054319,-60098081),
\quad c_4=375376,\quad c_6=229985128,\quad\Delta=-11.
\]
The producer uses the b-invariant discriminant formula; the separate
verifier uses \((c_4^3-c_6^2)/1728\). Both yield -11, and trial division
through sqrt(11) verifies the complete prime factorization. In particular
the target is nonsingular and integral. Its discriminant valuations are
one at 11 and zero elsewhere. By the cited transformation formula a
strict decrease to another integral local equation changes the valuation
by a positive multiple of twelve; the new integral discriminant must
have nonnegative valuation. None is possible here, so this very equation
is globally minimal. No further minimalizing isomorphism occurs: the
final long-model transformation witness is (u,r,s,t)=(1,0,0,0).
On the open complement of the kernel,
\[
\frac{dx'}{2y'+1}=\frac{h'(x)dx}{2Yv(x)}
=\frac{dx}{2Y}=\omega_0.
\]
The exact derivative identity (4) proves scalar one between the final
specified minimal differentials; both regular differentials extend,
so their equality holds globally. The short/centered transformations
were calculation coordinates only and each has differential scale one.

**Period and all twelve values.** Apply L045, importing its
[Dokchitser--Dokchitser, *Local invariants of isogenous elliptic curves*,
arXiv:1208.5519v4, Lemma 7.4 and Proposition 7.6, pp.15--16](https://arxiv.org/pdf/1208.5519v4#page=15).
Its supplied-witness premises now hold: specified minimal models,
Q-rational prime-degree map, d=1, and the entire geometric kernel real.
The odd-prime case gives k/c=5; since all five kernel points are real,
k=5 and c=1. Hence R=5 in the source/target direction in (2). The
isogeny supplies the common newform and conductor under L045's audited
applicability argument; source N=11 comes from L039. No nonoptimal
Manin constant or component-count guess is made. The same I on the
entire relative module therefore gives \(F_E=5F_0=\phi\).

From L043, D0=10 and the complete integer source numerators are
\[
(-2,2,0,10,5,-5,-10,-10,-5,5,10,0).
\]
L045's individual denominator formula \(10/\gcd(|5t_i|,10)\), including
gcd(0,10)=10, gives
\[
(1,1,1,1,2,2,1,1,2,2,1,1).
\]
Thus (3) is fully reduced and their lcm is exactly two, with a half-integer
generator establishing necessity. Integral generation, already audited
in L043/L039, gives the uniform bound on all M and every rational-cusp
path. The verifier binds the actual L043 certificate bytes, checks all
twelve source values against the canonical conclusion, and independently
reduces every target value and denominator, including both zeros. No
selected absolute-cycle test replaces the whole relative module.

**Verification and limitations.** Full production and independent replay
pass: 56 checks, no failures; exact order 5/5; finite kernel points 4/4;
minimality valuation 1<12; generator values 12/12; d=1, R=5 and denominator
two. The complete certificate and fresh report retain the polynomial
identities, exceptional witnesses, invariants, input hash and all values.
The published Sage 10.8 manual already exhibits this source and target;
agreement is a comparison after independent construction, not a premise
or certificate. The separate critical audit below validates this assembly.
The normalization only addresses a finite input-production gap: no
quadratic coefficient, infinite-order rational point, Sha result,
complex-order comparison or arbitrary-curve rank equality follows.

**Separate critical audit (2026-10-11).** The prior SPECIALIZE assessment
`drafts/literature/2026-10-11-five-isogeny-critical-audit.md` covers exactly
this instance. The entire proof, producer and distinct verifier were read,
with L039's source arithmetic, L043's normalization and L045's theorem
application. The primary source coverage above is reused; no new quotient
or period theorem is asserted. Reproduce the audit from the notebook root:

```bash
python3 scripts/conductor-eleven/five-isogeny/audit_certificate.py
```

The complete report is
`scripts/conductor-eleven/five-isogeny/critical-audit/audit.json`.
Before replay the audit hashes and copies the original certificate,
verification, both original programs, the new audit program, the current
L043 certificate and its separately audited archived original. The latter
two are byte-identical and match the source binding. Fresh production
agrees with the entire original certificate; the distinct verifier again
passes all 56 checks. Outputs go to the new audit directory. All seven
original inputs remain byte-identical afterwards.

The audit independently tests the **unpaired** equation-(7) sum without
importing either program's polynomial helpers. In the algebra
Q(x)[Y]/(Y^2-f(x)), for each of the four centered kernel points (q,r), put
s=(Y-r)/(x-q). The transported addition law gives

\[
X_Q=s^2+1-x-q,\qquad Y_Q=-Y+s(x-X_Q).
\]

The two sums are x+sum_Q(X_Q-q) and Y+sum_Q(Y_Q-r). Express each in
the basis 1,Y. Clearing L^2 in the first sum and L^3 in the second
gives polynomials: every individual term has denominator dividing
(x-q)^2 or (x-q)^3, respectively. In the first sum the constant
coefficient has numerator degree at most five and the Y coefficient at
most three. For the second, both degrees are at most six: before clearing,
s(x-X_Q) has numerator degree at most three over (x-q)^3 in either
basis coefficient, using Y^2=f of degree three. Multiplication by the
other cubic denominator adds at most three. The initial Y and the
subtracted constants also obey this bound.

Comparing these sums with N/L^2 and YM_1/L^3 therefore gives four
polynomial residuals of degrees at most (5,3,6,6). The two stored
denominator comparisons have degrees at most four and six; the derivative
identity M_1=N'L-2NL' has degree at most six. Equation (4)'s target
residual has degree at most fifteen, since deg N=5, deg M_1=6 and
deg L=2. The audit checks all eight residuals at the sixteen distinct
rational arguments -10,-9,...,4,6; none is a pole. Every exact value is
zero. A nonzero polynomial of degree at most fifteen cannot have sixteen
distinct roots, so these are complete identity checks, not sampling
evidence or a floating-point test. All evaluations and the bounds are
retained in `critical-audit/independent-identities.json`.

The projective reasoning was checked separately from the executable
labels. At each point (q,r), 2r is nonzero, so s0=x-q is a uniformizer
on the smooth centered source. The leading terms are
x'=4r^2 s0^(-2) and Y'=-8r^3 s0^(-3). For the four points in the
kernel order above the respective Y' leading coefficients are
(-1331,1771561,-1771561,1331), all nonzero. In the target chart
[x'/Y':1:1/Y'], its two variable coordinates belong to the source local
ring: they have leading terms -s0/(2r) and -s0^3/(8r^3). Thus the map
extends algebraically with image [0:1:0] at each point, not merely as
a limit along real points. At source infinity the standard parameter
t=-x/Y has x leading t^(-2), Y leading -t^(-3). Monic degrees give
h/x and v leading one, hence the same chart coordinates have leading
-t and -t^3. They again extend to zero. The factorization of L excludes
other affine poles. These checks validate identification with the cited
projective quotient, including its exact five-point geometric kernel.
Characteristic zero and the verified rational subgroup satisfy the
separability and descent hypotheses, giving degree five.

A third discriminant computation uses the centered target cubic
x^3+b x^2+c x+d, with b=-1, c=-7820, d=-263580+1/4:
16(b^2 c^2-4c^3-4b^3d-27d^2+18bcd)=-11. Thus target nonsingularity,
integrality and the valuation threshold 1<12 hold independently of the
producer's invariant formula. Source minimality is L039's audited input.
There is no subsequent coordinate change on either final model.
The derivative identity proves equality of differentials in the function
field; regularity extends it through zeros of v as well as the kernel.
It supplies d=1 between the final minimal differentials.

L045's odd-prime theorem applies because all five geometric kernel
points are real. It gives k/c=5, with k=5 and c=1; the executable
`real_map` label is checked against this mathematical application, not
used to prove it. The source/target ratio is k/(c|d|)=5. Its common
normalized newform argument preserves the numerator on the entire
relative module. Every one of L043's twelve values is multiplied and
reduced independently; both zero positions 2 and 11 remain zero, while
position 4 is 5/2 and forces the least denominator two. This retains
L043's published optimality and complete-isogeny-class qualifications.

Twelve altered copies test an opposite kernel ordinate, each map
numerator, a finite leading coefficient, the infinity pole order, the
target equation, the purported minimal-model change, differential scalar,
reciprocal period ratio, source hash, last zero value and a half-integer
denominator. All are rejected. Each seeded stale success report is
overwritten with a fresh nonempty failure report; all altered inputs
and reports are retained under `critical-audit/altered/`.

All 41 audit comparisons pass with no unexpected failure or mathematical
correction. This establishes a checked fixed normalization input within
known mathematics, not a result beyond the assessed sources. It does not
settle the coefficient, rational-rank, Sha or complex-order gaps. The
audit and finite tests do not constitute universal program verification.

## Mathlib

Full matching fixed degree-five quotient/minimal-differential and
total-real-period normalization certificate: not checked. Supporting
Weierstrass group law, Vélu quotient, minimality, polynomial identities,
isogeny degree/kernel and period theorem coverage: not checked. Unknown
availability is not absence. Precise imported results above and audited
L039/L043/L045 supply the inputs; no formal verification of these new
program artifacts is claimed.
