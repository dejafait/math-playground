# Corollary C032q: signed width laws and the norm-closed cone alternative

## Hypotheses

Retain precisely C032j/k/m/p's actual-zero Gaussian half-variance
convention and their fixed-v1 preprint, divisor, multiplicity, counting,
finite-zero and heat-positivity qualifications. In particular, on
W=[1,2] and X=[0,infinity), C032j supplies Borel probability laws
nu_sigma satisfying

    integral_X exp(-s*u) dnu_sigma(u)=exp(-B_sigma(s)), s>0.

C032k identifies B_sigma(w^2)=b_sigma(w) for real w>0. C032m supplies
the entire lifts b_sigma=E_sigma+O_sigma, with E even and O odd, and
their joint continuity and common bounds on W times every complex
disk. C032p supplies weak continuity of sigma -> nu_sigma and Borel
measurability of sigma -> nu_sigma(A) for every Borel A in X.

All measures and functions below use the usual relative Euclidean
topologies and Borel sigma algebras. Width measures eta are real
finite signed Borel measures, with finite total variation
V=|eta|(W); their mass is unrestricted until explicitly normalized.
Atoms and singular continuous parts are allowed. No density, absence
of a zero atom, moment assumption, positivity of p_sigma, RH or
unsmoothed actual-Xi realization is imposed.

Set, using the full complex variable w,

    kappa_w(sigma)=exp(-E_sigma(w))*sinh(O_sigma(w)),
    J_eta(w)=integral_W kappa_w(sigma) deta(sigma).

Let S be the real linear span in real C(W) of all Re(kappa_w) and
Im(kappa_w), w in C. A span means finite real linear combinations;
no coefficient truncation is imposed. C032m makes these width
functions continuous. All closures below use the supremum norm
on real C(W).

## Conclusion

For every such eta there is a well-defined finite signed Borel law

    nu_eta(A)=integral_W nu_sigma(A) deta(sigma), A Borel in X.

It has mass eta(W) and total variation at most V. For every bounded
real Borel f on X, define

    Tf(sigma)=integral_X f(u) dnu_sigma(u).

Then Tf is Borel measurable, |Tf|<=||f||_infinity, and

    integral_X f dnu_eta=integral_W Tf deta.                 (1)

On C_b(X), T is a positive bounded real linear operator into C(W),
with T1_X=1_W and operator norm one. Moreover,

    nu_eta>=0 on all Borel sets
      iff integral_W Tf deta>=0 for every f in C_b(X), f>=0. (2)

Define the convex cone

    Q=S+{Tf : f in C_b(X), f>=0},
    C=closure(Q) in real C(W).

The following are equivalent:

1. There exists a real finite signed Borel eta on W with eta(W)=1,
   J_eta identically zero on C, and nu_eta nonnegative.
2. The constant function -1_W does not belong to C.

In case 1, nu_eta is a probability law. Its positive-real Laplace
transform has the entire lift F_eta from C032m, and J_eta=0 is
equivalent to evenness of that lift. This is an exact alternative,
not a decision of either side for the actual-zero family. No moments,
closed image, finite-grid certificate or actual-Xi all-degree sign
is concluded. The general tools are known; only their applicability
to this qualified joint constraint is established here.

## Proof

### Imported results and why a local specialization is needed

The unchanged source assessment1542 covers this target. Use the
standard Jordan decomposition theorem, as stated in Richard F. Bass,
*Signed measures*, Chapter 12, version 4 November 2011,
[Theorem 12.8, printed p.97](https://webspace.science.uu.nl/~kraai101/SignedMEasures).
It writes eta=eta^+-eta^- with positive mutually singular parts and
eta^++eta^-=|eta|; finite variation makes both parts finite.

For positive measure/kernel composition use Kyle Siegrist,
*Probability, Mathematical Statistics, and Stochastic Processes*,
Expected Value, Section 13,
[Kernels and Operators, Basic Theory](https://www.randomservices.org/random/expect/Kernels.html),
accessed 18 November 2026. The unnumbered measure-transformation
statement and its countable-additivity proof give
mu K(A)=integral K(x,A) dmu(x) for a positive measure and a kernel.
For a finite input and a probability kernel this is a finite measure
with the same mass. Only that positive result is imported; below the
two signed-input parts and all bounded integration claims are checked.
The source's misprinted function-norm equality is not used.

For regularity and signed representation use the standard Riesz
representation theorem for C_0, as stated in Lewis Bowen,
*Lecture Notes in Real Analysis*, 8 December 2014,
[Theorems 28.1/28.2, p.60, and Section 28.1, pp.61-62](https://web.ma.utexas.edu/users/lpbowen/m381c/lecture-notes.pdf).
Finite Borel measures on the locally compact Polish spaces used here
are regular. For positive Radon existence and uniqueness on C_c use
Terence Tao, *245B, Notes 12*, 2 March 2009,
[Theorem 24](https://terrytao.wordpress.com/2009/03/02/245b-notes-12-continuous-functions-on-locally-compact-hausdorff-spaces/),
including its sigma-compact existence case. The compact signed Riesz
version is also stated there in Exercise 31; ledger1532 inspected
the positive construction and signed-functional decomposition. We
import the standard signed Riesz theorem, not the erroneous signed
inequality in that text's Lemma 29 proof. No general representation
or regularity theorem is reproved here.

For separation use Theo Bühler and Dietmar A. Salamon,
*Functional Analysis*, version 11 May 2016,
[Corollary 2.3.19, printed p.68](https://math.jhu.edu/~js/Math637/eth.functionalanalysis.pdf).
Disjoint nonempty convex sets in a real normed space, one closed
and the other compact, have strict uniform separation by a bounded
real linear functional. We apply it to an explicitly closed cone
and a singleton. No closed-range theorem is imported or needed.

These sources give the general tools but do not identify the present
kernel, construct its signed output, or match positivity, complex
cancellation and mass normalization simultaneously. The remaining
proof checks those applications. Their inspected proof cases and
typographical qualifications are retained in source ledger1542.

### Signed construction and the bounded integral identity

For each sigma, A -> nu_sigma(A) is a probability measure; for each
Borel A, sigma -> nu_sigma(A) is Borel measurable by C032p. Thus this
is exactly a probability kernel from W to X. For the Jordan parts
of eta apply positive kernel composition separately to obtain

    mu_+(A)=integral_W nu_sigma(A) deta^+(sigma),
    mu_-(A)=integral_W nu_sigma(A) deta^-(sigma).

They are finite positive Borel measures, with masses eta^+(W) and
eta^-(W). Their difference defines nu_eta and agrees with its stated
setwise signed integral. The output measures mu_+ and mu_- need not
be mutually singular and are not claimed to be the Jordan parts
of nu_eta. Total variation of their difference is bounded by their
sum: on any finite Borel partition, sum |mu_+(A_i)-mu_-(A_i)| is
at most sum (mu_+(A_i)+mu_-(A_i)). Taking the supremum gives
|nu_eta|(X)<=V. Evaluation at X gives nu_eta(X)=eta(W).

For a bounded real Borel simple function f, Tf is a finite linear
combination of measurable kernel evaluations, and (1) holds first
for each of the two positive input/output pairs by their defining
setwise formulas. Choose bounded Borel simple f_n converging
uniformly to an arbitrary bounded real Borel f. Since every nu_sigma
has mass one,

    sup_sigma |Tf_n(sigma)-Tf(sigma)|<=||f_n-f||_infinity -> 0.

Thus Tf is Borel measurable. Uniform convergence passes through
all four finite positive measures mu_+, mu_-, eta^+, eta^-.
The two positive-pair identities therefore hold for f; subtracting
them proves (1). The same probability bound gives |Tf|<=||f||.
All integrals involved are absolutely integrable against the
corresponding total variation. No interchange with an unbounded
test or an infinite-moment integral has occurred.

For f in C_b(X), C032p already proves Tf continuous on the closed
interval W, including its endpoints. Linearity and positivity follow
from integration against nu_sigma. The norm bound gives ||T||<=1;
T1_X=1_W, and both constants have norm one, so ||T||=1.

### Continuous tests detect positivity on the noncompact half-line

If nu_eta is nonnegative, (1) immediately proves the right side of
(2). Conversely suppose that side holds. By (1), integration against
nu_eta is a positive functional on real C_c(X), since C_c(X) is
contained in C_b(X). It is bounded by V times the supremum norm.
X is locally compact Hausdorff and sigma-compact. Tao's positive
Riesz theorem therefore gives a positive Radon measure rho with

    integral_X f drho=integral_X f dnu_eta, f in C_c(X).

If the cited construction initially provides only local finiteness,
global finiteness follows here: for integers n>=1 set

    chi_n(u)=max(0,min(1,n+1-u)), u>=0.

These continuous compactly supported functions increase to 1_X
and lie between zero and one. Hence

    integral_X chi_n drho=integral_X chi_n dnu_eta<=V.

Monotone convergence on the positive measure rho gives rho(X)<=V.
The possibly signed measure nu_eta is not used for this monotone
limit. Both mu_+ and mu_- are finite Borel measures on the locally
compact Polish X, hence regular by the cited regularity theorem.
Thus rho+mu_- and mu_+ are positive Radon measures. For every real
f in C_c(X), the preceding identity and nu_eta=mu_+-mu_- give

    integral_X f d(rho+mu_-)=integral_X f dmu_+.

Positive Riesz uniqueness makes these two measures equal on all
Borel sets. Subtracting mu_- yields nu_eta=rho>=0, proving (2).
This argument includes a possible atom at zero and uses neither a
density nor positivity inferred from a finite list of Laplace tests.

### Full cancellation and the forward implication

For any eta, integration defines a bounded real functional
L_eta(g)=integral_W g deta on C(W), with norm at most V. Since eta
is real, the real and imaginary parts of J_eta(w) are respectively
L_eta(Re(kappa_w)) and L_eta(Im(kappa_w)). Therefore

    J_eta(w)=0 for every w in C iff L_eta vanishes on S.     (3)

No restriction to real w, to selected widths, or to finitely many
Taylor coefficients is made.

Suppose eta satisfies conclusion 1. Equation (3) makes L_eta zero
on S. Equations (1)-(2) make L_eta(Tf)>=0 whenever f>=0. Thus
L_eta is nonnegative on Q and, by norm continuity, on C. But
L_eta(-1_W)=-eta(W)=-1. It follows that -1_W cannot lie in C.

### Separation and positive mass normalization

The set T(C_b(X)_+) is a convex cone, and S is a real linear
subspace. Thus Q is a convex cone containing zero, and so is its
norm closure C. Suppose -1_W is outside C. In the real normed
space C(W), C and the compact convex singleton {-1_W} satisfy
all hypotheses of Bühler-Salamon Corollary 2.3.19. Reverse the
functional's sign if necessary. The resulting bounded real linear
functional ell has a real number a such that

    ell(-1_W)<a<=ell(q) for every q in C.

Because 0 belongs to C, a<=0. Because t*q belongs to C for every
t>=0, ell(q)<0 for any q in C would contradict the displayed
lower bound as t tends to infinity. Consequently

    ell(q)>=0 for q in C, and ell(1_W)=-ell(-1_W)>0.

Both s and -s lie in Q for every s in S (take f=0), so ell(s)=0.
Also ell(Tf)>=0 for every nonnegative f in C_b(X). Normalize by
the strictly positive number ell(1_W), obtaining

    L(g)=ell(g)/ell(1_W), L(1_W)=1.

W is compact metric, so C_0(W)=C(W). The real signed Riesz
representation theorem gives a real finite signed regular Borel
measure eta representing L on all of C(W). In particular
eta(W)=1. Equation (3) gives J_eta identically zero, while (1)-(2)
give nu_eta>=0. Its mass is one by the signed construction.
This proves conclusion 1. Positivity of eta itself was neither
obtained nor required; it is the output law that is nonnegative.

### Laplace interpretation and scope limits

For s>0 the function f_s(u)=exp(-s*u) is in C_b(X). Equation (1)
and C032j/k yield

    integral_X exp(-s*u) dnu_eta(u)
      =integral_W exp(-B_sigma(s)) deta(sigma)
      =F_eta(sqrt(s)),

where sqrt(s)>0. C032m supplies the entire F_eta and the exact
identity F_eta(w)-F_eta(-w)=-2*J_eta(w). This proves the stated
parity equivalence, with no exchange involving exponential growth
on X. Extending a finite-mixture moment argument to this continuum
law is not part of this result.

The closure in the criterion is essential to this proof. Q itself
has not been shown closed, and no claim concerns closedness of a
signed-measure image. In the forward implication passage to a
uniform limit is legitimate for each fixed finite-variation eta.
A fixed nonzero approximation error, however, pairs with its
unknown variation V, so a finite tolerance alone is not an
infeasibility certificate over the unrestricted class of eta.

The criterion supplies neither a separator for this actual Q nor
a uniform approximation of -1 by its elements. It leaves cone
membership, feasible positive mixed laws, moments and unsmoothed
actual-Xi transfer unresolved. In particular it changes no known
finite-width or direct-growth stop and proves no RH-equivalent
positivity. This is a local reproduction/specialization of the
cited functional analysis, not a result beyond the sources checked.

### Conceptual audit1546 (18 November 2026)

The local proof above has been checked independently under the unchanged
SPECIALIZE scope of assessment1544. The primary-source inspections in
ledgers1542/1532 are reused; this is not a source-wide audit of the
inherited preprints. No mathematical correction was required. The
following checks establish the interfaces needed for this criterion,
without deciding either side for the actual family.

1. **Kernel and signed integration.** C032p gives exactly Borel set
   evaluations and continuous bounded-test evaluations, not continuous
   set evaluations. Each of eta^+ and eta^- is finite. Positive kernel
   composition gives two countably additive finite measures with the
   respective input masses. They may overlap completely; only the
   input decomposition is a Jordan decomposition. For any Borel set A,
   the partition estimate gives |nu_eta|(A)<=mu_+(A)+mu_-(A), hence
   the claimed total bound V. Uniform simple approximation has error
   at most ||f_n-f|| times the mass of each of these four positive
   measures. All four errors tend to zero before subtraction. This
   verifies (1), including signed real tests, without a signed version
   of monotone convergence or any moment interchange. On C_b, C032p
   supplies precisely the required continuity into C(W).

2. **Noncompact positivity.** The proposed right side of (2), together
   with (1), makes the C_c functional positive and bounded by V||f||.
   The half-line is locally compact, Hausdorff and sigma-compact, so
   positive Riesz existence applies. For its positive measure rho,
   chi_n equals one on [0,n], decreases linearly on [n,n+1], and is
   zero afterwards. Thus chi_n is compactly supported in the relative
   half-line topology, increases with n and converges to one everywhere,
   including at zero. Its integral is nonnegative and at most V.
   Monotone convergence is applied only to rho, proving rho(X)<=V.
   Each finite positive Borel component mu_+, mu_- is regular on this
   locally compact Polish space. Their sum with rho is therefore Radon.
   For every f in C_c the equality

       integral f d(rho+mu_-)=integral f dmu_+

   follows from finite signed subtraction. Positive Riesz uniqueness
   then identifies these positive measures on all Borel sets. Hence
   nu_eta=rho is positive. In particular no mass at zero or at large
   finite u is lost. No representation on the dual of C_b(X), which
   could introduce a different measure space, is used.

3. **Complex constraints and topology.** C032m gives continuity and
   boundedness of kappa_w on W for each complex w. Integrating its real
   and imaginary parts against a real finite eta is therefore legitimate.
   Vanishing on S is exactly vanishing of J_eta at every complex w;
   the condition has not been weakened to a finite Taylor list. The
   functional has norm at most V, so its nonnegativity passes from Q
   to the supremum-norm closure. This passage fixes eta first; it does
   not give a common finite-error tolerance for unbounded V.

4. **Separation and normalization.** Q contains zero, is closed under
   addition and nonnegative scaling, and contains s and -s for every
   s in S. These properties pass to its norm closure C. When -1 is
   outside C, the two nonempty convex sets C and {-1} are respectively
   closed and compact in the real normed space C(W). Corollary2.3.19
   therefore gives the displayed strict separator. Evaluation at zero
   gives a<=0. Scaling any hypothetical q with ell(q)<0 contradicts
   the same fixed lower bound a, so ell is nonnegative on C. Strictness
   at -1 now gives ell(-1)<0, not merely ell(-1)<=0; consequently
   ell(1)>0. Both signs of S force annihilation. Signed Riesz on compact
   W represents the normalized real functional by a finite real signed
   Borel eta with mass one. Items1-2 give positivity of its output,
   not positivity of eta. Conversely any feasible eta evaluates -1
   to -1 while being nonnegative on C. Both directions are verified.

5. **Analytic interpretation and retained limits.** For s>0 the only
   law test used is exp(-s*u), bounded by one on X. The positive-ray
   equality in C032k and the diskwise finite-variation bounds and parity
   identity in C032m identify this integral with F_eta(sqrt(s)) and
   F_eta(w)-F_eta(-w)=-2J_eta(w). No holomorphic extension of a growing
   integral on X is inferred. C032j's fixed-v1 probability, heat,
   divisor, multiplicity, counting and finite-zero inputs remain
   qualified imports. Neither Q's closedness, an actual separator,
   moments, nor unsmoothed Xi realization has been established.

The result is now a checked conditional criterion in the notebook.
The actual cone membership problem and the main all-degree positivity
gap remain open. This audit validates a specialization of known tools;
it establishes no progress beyond those source theorems.

## Mathlib

Full matching coverage of this qualified signed-kernel/cone result
is unchecked and unknown. Source ledger1542 inspected supporting
[MeasureComp documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Kernel/Composition/MeasureComp.html):
`MeasureTheory.Measure.instIsFiniteMeasureBindCoeKernelOfIsFiniteKernel`
and `MeasureTheory.Measure.instIsProbabilityMeasureBindCoeKernelOfIsMarkovKernel`
provide positive-composition infrastructure. They are not a full
formalization of the signed law, positivity detection, normalized
separator or inherited preprint inputs. No Mathlib theorem is used
as a substitute for those checks.
