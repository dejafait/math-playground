# L037 — Exact-conductor good-prime full-relative termination

## Hypotheses

Retain L029's non-CM global minimal E/Q of exact conductor N, its
normalized rational weight-two newform f, and the complete torsion-free
relative module M with independently certified presentation and rational
basis of V=M tensor Q. In particular V_R is the entire
H_1(X_0(N),Cusps;R), not just absolute homology. Retain its geometric
reflection j{alpha,beta}={-alpha,-beta}, with path orientation preserved,
and the good-prime path operators of L029 equation (1).

Enumerate every prime ell not dividing N, in increasing order
ell_1,ell_2,... . Grant exact independently certified matrices H_ell on
all of V and J for j, and exact a_ell(E)=ell+1-#E(F_ell), whenever needed.
Each finite matrix construction and rational rank computation is assumed
to finish. Operator construction, point-count algorithms and presentation
certification are premises; they are not proved here. No finite prime
cutoff, full Hecke algebra generation bound, q, central nonvanishing,
period scale, finite Sha, or BSD assertion is assumed.

For m>=0 and k=Q or R set
\[
 K_m(k)=\{\lambda\in V_k^*:\lambda\circ j=\lambda,
       \ \lambda\circ T_{\ell_i}=a_{\ell_i}(E)\lambda\ (1\le i\le m)\},
 \qquad K_\infty(k)=\bigcap_{m\ge0}K_m(k).
\]
In coordinates this is exactly the kernel of the transpose blocks in
L029 equation (3), for the first m good primes. Non-CM and minimality
are retained for downstream compatibility; the proof uses the rational
newform at its exact level, not a CM exclusion mechanism.

## Conclusion

There exists a finite m_0 with
\[
 \dim_Q K_m(Q)=\dim_R K_m(R)=1\quad(m\ge m_0).
\]
Writing I=Re(2 pi i integral f), one has
K_infinity(R)=R I on the entire relative space. A nonzero rational vector
in the first dimension-one kernel therefore supplies L029's certified
full-relative real-integration line, after exact rank evidence is saved.
Thus enumeration with exact rank checks terminates at dimension one,
conditional on the specified constructions finishing.

This removes the granted *eventual existence* of a dimension-one witness
from that exact-level test. It supplies no explicit m_0, largest prime,
runtime bound, actual general-curve matrices, independent q, normalized C,
nonzero coefficient, rational Kummer membership, or complex-order/rank
comparison. This is a known-source specialization, not a new multiplicity
one theorem or a BSD candidate. The separate critical audit of 2026-10-08
passes under precisely these conditional premises; its verification
details appear at the end of the proof.

## Proof

**Imported inputs.** Use Atkin–Lehner–Li decomposition and multiplicity
one in Stein, *Modular Forms, a Computational Approach*, online v0.1,
[Computing with Newforms, Theorem 9.4 and its Gamma_0 paragraph](https://www.wstein.org/books/modform/modform/newforms.html).
Its decomposition has summands alpha_d(S_2(Gamma_0(M))_new), M dividing N,
d dividing N/M, with good-index Hecke action. Import the distinct-orbit
character separation from Ribet–Stein, *Lectures on Modular Forms and
Hecke Operators*, January 12, 2017,
[Definition 9.4.2 and Proposition 9.4.3, printed pp. 80–81](https://wstein.org/books/ribet-stein/main.pdf#page=89):
the rational anemic algebra on the cusp-form space is the product of the
coefficient fields of newform orbits at levels dividing N, with T_n sent
to their a_n for gcd(n,N)=1. Old multiplicities are not removed by this
algebra; see Remark 9.4.5. Use both inputs, not new-subspace uniqueness
alone.

Use Cremona, *Algorithms for Modular Elliptic Curves*, corrected second
edition (1997), [Chapter 2, Proposition 2.2.3, pp. 16–17](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=10)
for cusp equivalence, and Section 2.1.3, equation (2.1.4), pp. 11–12,
for real-period duality. Use Hasse's named theorem in
[Sutherland, MIT 18.783, Spring 2017, Lecture 8, Theorem 8.1, p. 1](https://math.mit.edu/classes/18.783/2017/LectureNotes8.pdf#page=1),
and Dirichlet's theorem on primes in coprime arithmetic progressions.
L029's proof supplies full-relative Hecke adjointness, geometric sign and
nonzero I on absolute cycles without using its granted dimension-one
hypothesis. The source theorems are imported, not reproved; only their
relative-boundary and finite-kernel specialization is supplied below.

**1. Boundary scalar, including reduced fractions.** Dirichlet supplies
a prime ell=1 modulo N, necessarily good. Let C be the finite set of
Gamma_0(N) cusp classes. The endpoint map partial sends
{alpha,beta} to [beta]-[alpha]. On Q[C], the path formula induces
\[
 U_\ell[\alpha]=[\ell\alpha]
              +\sum_{r=0}^{\ell-1}[(\alpha+r)/\ell].
\]
We show that every summand is [alpha]. For a finite cusp write alpha=a/c
in lowest terms with c>0. Put g=gcd(c,N). Cremona's criterion says a
reduced a'/c' is equivalent to a/c if there is a unit u modulo N with
c'=u c modulo N and u a'=a modulo g. We will always take u=1.

If ell divides c, then ell does not divide a. The first transformed
fraction ell a/c reduces to a/(c/ell); as ell=1 modulo N and is invertible
modulo N, c/ell=c modulo N. Its numerator is a. For every r, a+r c is
prime to c and not divisible by ell, so (a+r c)/(ell c) is already
reduced. Its denominator equals c modulo N and its numerator equals a
modulo g. The criterion applies to each fraction.

If ell does not divide c, ell a/c is reduced; its denominator is c and
ell a=a modulo g. For (a+r c)/(ell c), gcd(a+r c,c)=1, so the only possible
common factor is ell. There is exactly one r_0 in [0,ell-1] for which ell
divides a+r_0 c. For r different from r_0 the fraction is reduced with
denominator ell c=c modulo N and numerator a+r c=a modulo g. At r_0 it
reduces exactly by ell to
\[
  \frac{(a+r_0c)/\ell}{c}.
\]
Here (a+r_0c)/ell=a modulo g, because ell is invertible and equals one
modulo g. The criterion again applies. This includes alpha=0 (a=0,c=1);
the zero numerator at r_0 gives 0/1 after the same reduction. No other
cancellation is possible. At infinity every representative maps infinity
to infinity, so all ell+1 terms give [infinity] directly.

Consequently U_ell=(ell+1)Id on Q[C], and the same holds over R. Set
B_R=im(partial:V_R -> R[C]); no surjectivity onto all cusp divisors is
needed. Endpoint compatibility gives
\[
 \partial T_\ell=U_\ell\partial,
 \qquad T_\ell|_{B_R}=(\ell+1)\operatorname{Id}.
\]
In this last formula T_ell denotes the induced quotient operator.

**2. Restriction is injective without splitting the relative extension.**
Let H_R=H_1(X_0(N),R). The exact sequence of the pair (X_0(N),C), with
H_1(C;R)=0 since C is finite, gives
\[
 0\longrightarrow H_R\longrightarrow V_R
   \mathop{\longrightarrow}^{\partial}B_R\longrightarrow0.
\]
Both j and the good-prime operators preserve H_R by their endpoint
compatibility. Restriction sends K_infinity(R) into the geometric-plus
good-prime eigenfunctionals on H_R. If lambda in K_infinity(R) restricts
to zero, it factors through B_R. By step 1 and its ell equation,
\[
 (\ell+1)\lambda=\lambda\circ T_\ell=a_\ell(E)\lambda.
\]
Since E has good reduction at ell, Hasse gives
\[
 |a_\ell(E)|\le2\sqrt\ell<\ell+1;
 \quad \ell+1-2\sqrt\ell=(\sqrt\ell-1)^2>0.
\]
Thus lambda=0. This proves injectivity using a scalar on the actual
boundary image. It assumes neither a Hecke-equivariant splitting nor
semisimplicity of V_R or its extension.

**3. Exact-conductor geometric-plus cuspidal multiplicity is one.**
Let S_R be the real Fourier-coefficient subspace of S_2(Gamma_0(N)).
The imported real-period duality identifies S_R with (H_R^+)^* by
\[
 h\longmapsto \left(x\longmapsto 2\pi i\int_x h(z)\,dz\right).
\]
Here H_R^+ uses j, and the integrals displayed are real on H_R^+.
The pairing is Hecke adjoint in the normalization of L029. A functional
lambda on H_R with lambda j=lambda vanishes on H_R^- and is determined
by its restriction to H_R^+. The good-prime operators commute with j:
in the path formula reflection replaces r by -r, and replacing this by
its residue modulo ell differs by an integral translation in Gamma_0(N).
Hence they preserve H_R^+, and the pairing identifies the desired
functional eigenspace with the a_ell(E) eigenspace in S_R.

To bound this eigenspace, first work over C. The Hecke relations of Ribet–Stein,
[Section 8.2.2, printed p. 68](https://wstein.org/books/ribet-stein/main.pdf#page=77),
for trivial character and weight two are
\[
 T_{\ell^{t+1}}=T_\ell T_{\ell^t}-\ell T_{\ell^{t-1}}\ (t\ge1),
 \qquad T_{ab}=T_aT_b\quad(\gcd(a,b)=1).
\]
Thus agreement with f at every good prime implies agreement at every
index prime to N. The anemic algebra's product-of-fields description
separates different newform orbits and their coefficient-field embeddings:
its coordinate projection for f cannot coincide with a character of
another factor, since the product's idempotents distinguish factors.
Within one factor the good-index eigenvalues generate that factor by
surjectivity of the described algebra map, so distinct embeddings are
also distinguished. The f factor is Q because f has rational coefficients.
Therefore only degeneracy copies of this particular newform can have
all the specified good eigenvalues.

The newform has exact level N. In the imported decomposition its allowed
degeneracy indices divide N/N=1, so its single summand has dimension one.
No lower-level newform contributes this character, by the preceding
separation. It follows that the simultaneous eigenspace in the entire
complex cusp space is C f, and in S_R it is R f. Exact conductor is
essential here: at a raised level there may be several degeneracy
copies with the same away-from-level character. This conclusion uses
semisimplicity only in the imported cusp-form theory.

The geometric sign agrees with L029's real integral, not a software
plus label. Stein's weight-two star is -j (General Modular Symbols,
Remark 1.43); no replacement of j by that star has occurred.

**4. The infinite full-relative eigenspace is exactly R I.**
Step 2 embeds K_infinity(R) into the one-dimensional space of step 3.
By the portions of L029's proof preceding its dimension argument, I is
nonzero on H_R^+, satisfies I j=I, and satisfies I T_ell=a_ell(E)I on
all of V_R for every good prime. These statements use integration and
period duality, not L(E,1) or a twist value. Therefore I belongs to
K_infinity(R) and is nonzero. The upper and lower bounds give
\[
 K_\infty(R)=R I,\qquad \dim_R K_\infty(R)=1.
\]
In particular this does not assert that every cuspidal eigenfunctional
extends across the boundary; existence is supplied by the actual integral,
and injectivity supplied uniqueness.

**5. Finite intersection and rational scalar extension.**
The spaces K_m(R) form a descending sequence in a finite-dimensional
space. The set of their dimensions is a nonempty finite subset of
{0,...,dim V}; choose m_0 where its least element occurs. For m>=m_0,
inclusion and equal dimensions imply K_m(R)=K_m_0(R). Every earlier
space contains this one, so their infinite intersection is K_m_0(R).
Step 4 then makes that minimum dimension one. This argument does not
infer stabilization from a single unchanged dimension: decreases can
occur after arbitrarily many intervening equations.

For each finite m the stacked matrix has rational entries, including
J and the integer a_ell(E). Its rank over Q equals its rank over R,
because nonzero minors remain the same rational numbers. Consequently
K_m(Q) tensor_Q R=K_m(R), and at m>=m_0 its rational dimension is one.
Choose a nonzero v in K_m_0(Q). Viewed over R it lies in R I and hence
satisfies every later equation as well; those equations are rational,
so v belongs to K_infinity(Q). Thus there is no unproved interchange
of tensor product with an infinite intersection.

Exact enumeration reaches the finite m_0, or stops earlier at another
dimension-one kernel. At any such stop I already lies in the real
kernel, so the rational line is precisely its real line; L029 applies
with an exact rank/nullvector certificate. A minor or reversible rational
elimination must still be saved for the actual stop. Existence of m_0
alone is not an instance's rank witness.

**Qualifications and downstream use.** The boundary proof and rational
finite-intersection argument are the explicit specialization missing
from the source statements, justifying this write-up rather than a
reproof of their modular-form theorems. The ready assessment authorizes
precisely this threshold. Historical calibration-production stops
ATTEMPTS/022--024 remain applicable to repetitions of conditional audits;
this result addresses a different granted input. It can supply the line
premise of L028/L036 under the retained complete operator constructions,
while independent q and all subsequent arithmetic certificates remain
unresolved. No progress beyond the known theory checked is claimed.

**Separate critical audit, 2026-10-08.** All five steps pass. The proof
and conclusion above are unchanged. These checks concern the conditional
theorem, not an instance certificate or the BSD target.

For step 1, the cusp criterion was checked in its reduced-fraction domain
against Cremona Proposition 2.2.3, including its proof. In the first
denominator case gcd(a,c/ell)=1 and ell does not divide a+rc. In the
second case gcd(a+rc,c)=1 excludes any cancellation other than one
factor ell from the denominator ell c, even if the numerator contains
a higher power of ell. Division at the unique r_0 preserves the
numerator congruence since ell=1 modulo g. At a=0,c=1 the cancelling
term is precisely 0/1. Negative numerators cause no change to the
criterion, and infinity is checked directly. The scalar conclusion
concerns the cusp-class module and hence its actual boundary image,
without boundary surjectivity.

For step 2, exactness identifies the quotient by absolute cycles with
B_R, so a vanishing restriction factors through that quotient. The
good prime supplied by Dirichlet occurs in the enumeration. Its scalar
ell+1 differs strictly from a_ell(E) by Hasse; there is no exceptional
prime at equality and no splitting is used.

For step 3, Cremona equation (2.1.4) is duality for all real-coefficient
forms. Its preceding single-form iff shorthand is not used to detect
an arbitrary cycle's sign. Reflection commutes with every operator:
replacing -r by its residue r' modulo ell translates both endpoints by
the same integer (r+r')/ell, acting trivially on quotient symbols.
Adjointness identifies the functional equations with the form equations
on H_R^+. The good-index recurrences specialize Ribet--Stein Section
8.2.2 at weight two, trivial character and good primes. Proposition
9.4.3's coordinate map separates orbits and embeddings but does not
count degeneracy copies. Stein Theorem 9.4 supplies that count: the
rational f factor has one copy because its new level is N. Non-CM
and minimality do not substitute for exact level.

For step 4, only L029's integration, reflection and nonzero-cycle
arguments before its dimension calculation are used. Stein Proposition
1.38, Remark 1.41 and Theorem 1.42 cover cusp-to-cusp integration;
their weight-two determinant factor agrees with the path operators.
Geometric j has the positive real sign, whereas Stein's star is -j.
Nonzero real integration supplies existence on all of V_R independently
of central or twist nonvanishing. L029's granted dimension-one kernel
is excluded throughout the audit.

For step 5, finite dimensionality makes the least attained dimension
a true minimum. Nesting then makes all later kernels equal; a single
plateau cannot do this. Each finite rational rank is unchanged over R
by its minors. A nonzero rational vector in the stabilized line
satisfies every later rational equation because the real line does,
without an infinite-intersection base-change rule. Stopping at dimension
one is valid because actual integration belongs to every finite kernel.
Only finitely many certified constructions are needed to reach the
existential m_0; their finishing remains granted. No bound, general
construction or arithmetic witness has been added.

The cited primary theorem domains and essential proof cases were
rechecked, without reproof of named results. No mathematical dependency
changes: the direct local input remains L029. Full matching Mathlib
coverage remains not checked. This validates a local conditional input,
with no progress beyond the known source theory and no removal of
independent q or subsequent BSD gaps.

## Mathlib

Full matching eventual full-relative termination theorem: not checked.
Supporting exact-conductor newform decomposition, anemic algebra,
cusp equivalence, real-period duality, full-relative Hecke matrices,
Hasse, Dirichlet and descending-kernel APIs: not checked. Unknown
availability is not absence. The precise mathematical sources and the
scalar-extension argument used here are given above.
