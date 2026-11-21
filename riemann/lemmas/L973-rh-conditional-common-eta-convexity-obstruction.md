# Lemma 973: an RH-conditional obstruction to common-eta convexity

## Hypotheses

Use the actual Xi paired zeros alpha_j of L024, with every
multiplicity, and beta_j=alpha_j^(-2). Use L026's geometry and choose
one finite A>0 with sum_j |beta_j|<=A. For integers m>=1 set

    a_m(z)=P_m(z)(1+z/4)^(-m/2),
    P_m(z)=sum_{k=0}^{floor((m-1)/2)}
                 (-1)^k binom(m,2k+1)(z/4)^k,
    Q_u(m)=sum_j beta_j^2 a_m(beta_j)^2/(beta_j+u), u>0.

The analytic branch is L964(5)'s branch, with a_m(0)=m. Squares
are algebraic. For n>=2 put eta_n=1/(64*9^n) and

    D_n=Q_{eta_n}(n+1)-2Q_{eta_n}(n)+Q_{eta_n}(n-1).       (1)

The same eta_n occurs in all three terms. **For the sign conclusion
only, assume RH**, equivalently that all alpha_j are real by L018.
No simplicity, numerical zero data, rational independence of zero
ordinates, or unconditional positive Stieltjes law is assumed.

## Conclusion

Unconditionally, with x(z)=(1-z/4)/(1+z/4), the complete identity is

    D_n=2 sum_j beta_j^2 T_n(x(beta_j))
                   /((beta_j+eta_n)(1+beta_j/4)).           (2)

Every sum in (1)-(2) is absolute and real at each fixed n.

Under the additional RH diagnostic hypothesis there exists delta>0
such that D_n<-delta for infinitely many positive integers n>=2.
Consequently RH implies that the proposed inequality D_n>=0 for
every n>=2 is false. This is a conditional obstruction to this
convexity component, not an unconditional negative actual-Xi
certificate, a disproof of RH, or a failure of Q_{eta_n}(n)>=0.

Written in step198 and independently conceptually audited in step200,
10 November 2026. The statement and constants survived unchanged.
This validates the local specialization, not originality beyond the
sources checked or an unconditional actual-Xi negative sign.

## Proof

### Imported identities and the complete common-parameter expression

The source comparison for this target is
`drafts/literature/2026-11-10-fixed-eta-second-difference-review-196.md`.
Import the standard Chebyshev identities
[NIST DLMF 18.5.1](https://dlmf.nist.gov/18.5.E1) and
[18.9.1 with Table 18.9.1](https://dlmf.nist.gov/18.9.i):

    T_m((w+w^(-1))/2)=(w^m+w^(-m))/2, w!=0,
    T_0=1, T_1=x, T_{m+1}+T_{m-1}=2xT_m.                (3)

The Laurent-polynomial version in (3) follows from those initial
values and recurrence, so it applies to complex w as well. This
use imports a standard identity, not a new recurrence theorem.

For an actual alpha, t=1/(2alpha), z=alpha^(-2), and
w=(1+it)/(1-it), L964(5)-(6)'s finite algebra gives

    z a_m(z)^2=2-w^m-w^(-m)=2-2T_m(x(z)).                (4)

Indeed t^2=z/4 and (w+w^(-1))/2=(1-t^2)/(1+t^2)=x(z).
The denominators and w are nonzero since |t|<1/8 by L026.
Only L964's unconditional definitions and algebra are used, not
its supplied-negative-Li hypothesis or conclusion. Subtracting
(4) at indices n+1,n,n-1 and using (3) gives

    z[a_{n+1}(z)^2-2a_n(z)^2+a_{n-1}(z)^2]
      =4(1-x(z))T_n(x(z)),
    1-x(z)=z/(2(1+z/4)).                                (5)

Multiply (5) by z/(z+u), for the same u in every term.
Summation with u=eta_n yields (2).

Here all complete-sum operations are justified at each fixed index,
without an n-uniform interchange. L026 gives |beta|<c=1/16,
Re(beta)>0, |beta+u|>=u, and |1+beta/4|>=63/64.
L964(9)'s unconditional bound |a_m(beta)|<=3^m gives

    sum_j |beta_j^2 a_m(beta_j)^2/(beta_j+u)|
      <=9^m c A/u<infinity.                             (6)

Also |x(beta)|<=65/63. Since T_n is a polynomial, its supremum
B_n on |x|<=65/63 is finite. The absolute sum on the right of
(2), at any u>0, is at most (128/63)B_n c A/u. Thus finite
subtraction and summation preserve the full series. Conjugation
preserves the beta multiset and the rational summands, so the
absolute sums are real. No off-diagonal theta identity, distant-h
deletion, or replacement by real ordinates is made here.

### The RH diagnostic gives a summable spectral sequence

For the rest of the proof impose RH explicitly. Then beta_j>0,
beta_j<1/16 and sum_j beta_j<=A. Define

    theta_j=2 arctan(sqrt(beta_j)/2),
    c_j=2 beta_j/(1+beta_j/4),
    S(k)=sum_j c_j cos(k theta_j), k in Z,
    M=sum_j c_j.                                       (7)

We have 0<theta_j<1/4, because arctan(t)<t for t>0 and
sqrt(beta_j)/2<1/8. Also 0<c_j<=2beta_j, so M<=2A.
The series for S is real and uniformly absolutely convergent on Z,
with |S(k)|<=M. The same sum converges uniformly for real k, and
its finite heads are trigonometric polynomials. The standard named
Bohr uniform approximation theorem therefore makes it a Bohr
almost-periodic function on R. Its restriction is in AP(Z) by
the restriction characterization in the inspected Section 3/(3.6)-(3.8)
of Batchenko-Gesztesy cited below. The sign proof below uses the
explicit means instead of depending on an abstract AP recurrence.

The node set is nonempty without consulting any zero list.
L021 gives Xi''(0)=-M_2<0, hence Xi is nonconstant. If L024's
paired node set were empty, its product would make Xi constant.
Thus at least one c_j exists, and M>0.

Since cos(theta_j)=x(beta_j), (2) under RH becomes

    D_n=sum_j c_j beta_j/(beta_j+eta_n) cos(n theta_j).

For arbitrary u>0 and integer k, the corresponding regularized
spectral sequence differs from S(k) in modulus by at most

    E(u)=sum_j c_j u/(beta_j+u).                          (8)

This includes every node and multiplicity. To prove E(u)->0,
choose a finite head of J nodes with beta-tail mass
R_J=sum_{j>J} beta_j. Termwise on the head,
c_j u/(beta_j+u)<=2u; on the tail it is <=2beta_j.
Consequently

    E(u)<=2Ju+2R_J.                                     (9)

First choose J so that R_J is arbitrarily small, then choose u
small. This proves E(u)->0 with a bound uniform in k. In
particular |D_n-S(n)|<=E(eta_n)->0. No effective rate or uniform
rate over all possible node laws is asserted or needed.

### Mean, nonresonance, and negative margins on positive indices

For a bounded sequence f write its one-sided Cesaro mean, when
it exists, as lim_{N->infinity} N^(-1)sum_{k=1}^N f(k).
For real theta not in 2pi Z the finite geometric sum gives

    |N^(-1)sum_{k=1}^N exp(ik theta)|
       <=2/(N |1-exp(i theta)|) ->0.                    (10)

Every theta_j is in (0,1/4), so none is resonant on Z. The
uniform absolute tail in (7) lets (10) pass from finite heads
to S; its one-sided mean is zero.

The double series for S(k)^2 is uniformly absolutely convergent,
since sum_{j,l} c_j c_l=M^2<infinity. The cosine product identity
and (10) show that the mean of
cos(k theta_j)cos(k theta_l) equals 1/2 if theta_j=theta_l,
and zero otherwise. In fact theta_j+theta_l is in (0,1/2),
and a nonzero difference has modulus <1/4; neither is in 2pi Z.
Thus no arithmetic independence assumption is being hidden.
Taking means through finite rectangles and their uniform tails gives

    mean(S^2)=V:=(1/2)sum_{theta} C_theta^2>0,
    C_theta=sum_{j: theta_j=theta} c_j.                  (11)

Grouping equal frequencies retains repeated zeros and all
multiplicities. The sum is over the countable distinct frequencies;
0<V<=M^2/2, with strict positivity because the node set is nonempty.

The discrete positivity-of-mean theorem, V. Batchenko and F. Gesztesy,
*On the spectrum of Jacobi operators with quasi-periodic algebro-geometric
coefficients*, [arXiv:math/0506138v2, 30 November 2005, Section 3,
Theorem 3.1(viii)](https://arxiv.org/html/math/0506138v2#S3),
states that a real nonnegative, nonzero AP(Z) sequence has positive
mean, with the mean defined in (3.8). Its preceding recalled
AP results do not require the later Jacobi/curve hypotheses.
It diagnoses the incompatibility of a nonzero zero-mean sequence
with nonnegativity on all Z. For the needed fixed negative margin
at arbitrarily large positive indices, use the following direct
calculation of the first two means; it avoids an additional
recurrence theorem and proves exactly the one-sided assertion needed.

Set delta=V/(4M)>0. If S(k)>=-2delta for all sufficiently large
positive k, then -2delta<=S(k)<=M there, and

    (S(k)+2delta)(M-S(k))>=0,
    S(k)^2<=(M-2delta)S(k)+2delta M.                     (12)

The finitely many exceptional indices vanish on Cesaro averaging.
Equations (10)-(11) then give V<=2delta M=V/2, a contradiction.
Hence S(n)<-2delta for infinitely many n tending to infinity.
By (8)-(9), E(eta_n)<delta for every sufficiently large n, so
on an infinite subset of those indices

    D_n<=S(n)+E(eta_n)<-delta.                           (13)

This completes the conditional test. It supplies a recurrent fixed
negative margin in the sense of arbitrarily large positive indices;
no claim of a computed index, effective onset or bounded gaps is made.

### Scope and use toward the main gap

Xiao, *Recurrence relations of Li coefficients*,
[arXiv:2006.13103v1, Theorem 3.2/(3.10), p.4](https://arxiv.org/pdf/2006.13103v1),
supplies the ordinary-Li signed recurrence, and Corollary 3.3,
pp.4-5, supplies an RH-conditional absolute bound. These are
background comparisons, not a source of a sign or of the common-u
regularization. No source's conjectural convexity is imported.
The present calculation specializes standard trigonometric identities
and mean arguments to the actual paired-node series, and retains
the full regularization error. Its local addition is the complete
common-u formula and conditional obstruction, classified REPRODUCTION;
the bounded search does not certify originality or priority.

Under RH each Q_u(m) is nonnegative termwise, yet its common-u
index second difference can have either sign; the negative conclusion
here is compatible with that positivity. The failed component is
therefore convexity as proposed signed forcing. L966's unconditional
R_n<=N_n, L968's all-n sign premise, initialization, movement of
eta between different indices, and cumulative induction margins
remain unresolved. This proof does not extend the trigonometric
or error argument off RH: complex phases need not stay bounded.

### Independent conceptual audit — step200

The audit reuses the separately approved source/scope assessment
`drafts/literature/2026-11-10-common-eta-obstruction-audit-review-198.md`.
The following checks address the complete sums, rather than sampled
nodes or a finite numerical prefix. No general AP theorem is reproved:
the explicit means are needed because the cited symmetric-mean theorem
alone does not give this positive-index margin after regularization.

**Normalization and unconditional scope.** Starting from L964(5)-(6),
the second difference of 2-2T_m(x) is
-2(T_{n+1}-2T_n+T_{n-1})=4(1-x)T_n. Multiplication by z/(z+u)
then gives exactly 2z^2 T_n/((z+u)(1+z/4)); no pair is counted
again. The sign choice of the representative alpha replaces w by
w^(-1) and does not change this expression. At n=2, putting q=z/4
also checks the lowest permitted index directly:

    a_3(z)^2-2a_2(z)^2+a_1(z)^2
      =2(1-6q+q^2)/(1+q)^3=2T_2(x(z))/(1+q).

All m in (1) are at least one. L026 gives Re(beta)>0 as well as
|beta|<1/16, so beta+u never vanishes; 1+beta/4 never vanishes
either. The squares a_m(z)^2=P_m(z)^2/(1+z/4)^m are rational
with real coefficients. Thus conjugation gives reality without
having to assign a new square-root branch to any summand.
Equations (6) and the following polynomial bound prove absolute
convergence of both sides before subtraction. Their growth with n
is harmless for this fixed-index identity. Only L964's unconditional
algebra and analytic estimate are used, not its negative-Li premise.

**Complete one-sided means.** Under the explicitly separate RH
assumption, set M_J=sum_{j<=J}c_j, t_J=M-M_J and
S_J(k)=sum_{j<=J}c_j cos(k theta_j). Then

    sup_k |S(k)-S_J(k)|<=t_J<=2R_J,
    sup_k |S(k)^2-S_J(k)^2|<=2M t_J.

For each fixed finite J, (10) gives mean(S_J)=0 and

    mean(S_J^2)=V_J
      =(1/2)sum_{j,l<=J: theta_j=theta_l} c_j c_l.

The phase bounds rule out all nonzero integer resonances, including
sum frequencies; simply being distinct real frequencies would not
have sufficed. First let the averaging length tend to infinity
with J fixed. Then let J tend to infinity. The two displayed uniform
tail bounds justify both means even when distinct frequencies get
arbitrarily close. Since all c_j c_l are positive, the finite
rectangles increase to the complete equal-frequency double sum.
Grouping it gives exactly V=(1/2)sum_theta C_theta^2 in (11), with
every multiplicity retained. Also V<=M^2/2 and V>0: L021's
Xi''(0)=-M_2<0 together with L024's exact product rules out an
empty node set. This does not assume a known numerical zero.

**Fixed margin and moving regularization.** M>0 makes
delta=V/(4M) well-defined, with 0<delta<=M/8. Under the proposed
eventual lower bound S(k)>=-2delta, the pointwise inequality (12)
averages to V<=2delta M=V/2. The finite initial exceptions contribute
zero in the limit because S is bounded. Its negation supplies
arbitrarily large positive n with S(n)<-2delta, not merely a negative
index somewhere on Z.

For the last transfer choose a finite nonempty head J with
R_J<delta/4; then for every u<delta/(4J), (9) gives E(u)<delta.
The estimate is uniform in the oscillatory index. Since eta_n->0,
it applies to every sufficiently large n, including an infinite
subset of those negative-margin indices. Hence D_n<-delta there.
No effective onset or frequency-separation bound is required, and
no n-uniform complex-phase estimate has been used off RH.

No mathematical defect was found in the stated identity or conditional
conclusion. Direct mathematical inputs remain L018, L021, L024, L026
and the unconditional parts of L964, as recorded in the existing DAG.
L966/L968 and L972 are context, not additional premises for this proof.
The audit removes the pending qualification on this conditional
obstruction; it supplies no sign for the unresolved mixed forms.

## Mathlib

Full matching coverage of this conditional actual-Xi obstruction
has not been checked and remains unknown. No Mathlib theorem is
imported. Supporting Chebyshev, geometric-sum, summability or
Cesaro-mean results alone would not certify the common-parameter
normalization, integer nonresonance and complete eta error here.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
