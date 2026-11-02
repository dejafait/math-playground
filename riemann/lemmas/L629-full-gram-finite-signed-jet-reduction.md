# Lemma 629: a uniform finite signed-jet reduction of the full Gram comparison

## Hypotheses

Use L622's exact Hermitian K_c(T,X), fixed nonnegative smooth w of
integral 1, T<=X<=2T, L=log T, N=floor(T^(1/100)), and real
c=(c0,c1) with c0^2+c1^2=1. Let a be any complex coefficient vector
of length N, fixed during shift differentiation. Put Gamma=a^*G_N a,
with the full Gram matrix of L623. Use the holomorphic arithmetic
form B_N(q;a), including its analytic C_N(q), from L624/L628:

    B_N(q;a)=C_N(q) sum_(r in S_N)
          A_(alpha,beta)(a;r) A_(gamma,delta)(conjugate(a);r).

Every coordinate r in S_N is retained, including r>N. In particular
B_N(0;a)=Gamma. The later audit in Section 5 checks this lemma's
transfer and finite extraction, using the audit of L628 (2) recorded
there. L623/L624's identities are checked at the used scope; unrelated
claims, including L627's first-jet estimate, retain their qualifications.
There is no zero-free, RH, sign, simplicity or spacing assumption.

The arithmetic factors and complete-sum holomorphy are the reused
imports from C. P. Hughes and M. P. Young, *The twisted fourth moment
of the Riemann zeta function*, J. reine angew. Math. 641 (2010),
203–236, [arXiv:0709.2345v2, Theorem 1.1/(12)–(17), printed
pp. 4–5 and the holomorphy remark](https://arxiv.org/pdf/0709.2345v2#page=4).
The phase estimate is the audited application in L619 Section 3;
the Laurent expansion of zeta at 1, with residue 1, and
zeta(2)=pi^2/6 are standard inputs. No moment theorem is reproved.
The new work is a coefficient-uniform specialization using L628,
and exact finite algebra for the resulting signed functional.

## Conclusion

For nu=(a,b,c,d) with a>=b>=0, c>=d>=0 and |nu|<=8, define

    h_nu=partial^nu B_N(0;a_vector)/(nu! L^|nu|),
    nu!=a!b!c!d!.

The coefficient vector in this formula is a_vector, to distinguish
it from the first integer component of nu. Define three rational
weights w_nu,0,w_nu,1,w_nu,2 by the finite polynomial prescription
(5)–(7) below. Then, uniformly in X,c and all coefficient vectors,

    a^*K_c(T,X)a
      = (6/pi^2) Re sum_nu h_nu
             [w_nu,0 c0^2+i w_nu,1 c0 c1+w_nu,2 c1^2]
          + O_w(Gamma/L).                                  (1)

The constant and onset are existential and independent of the vector.
Equation (1) does not truncate the divisor space. Arithmetic Taylor
degrees above eight contribute exactly zero to this signed extraction;
they are not discarded by an unproved small-remainder claim. The
O(Gamma/L) term comes from the regular zeta factors and phase, not
from arithmetic Taylor truncation.

There are 175 rows. For nu=0 the weights are

    (1/180,0,1/5040),                                     (2)

so the degree-zero part is precisely
B(c)Gamma=(28c0^2+c1^2)Gamma/(840pi^2). All six permutations,
normalization derivatives, and the possible degree-eight terms occur.

Writing h=h_(1,0,0,0), the complete arithmetic-degree-one part is

    (6/pi^2)[(c0^2/15+c1^2/315) Re h
                                      -(c0 c1/90) Im h].   (3)

For c=(0,1), its ratio to B(c)Gamma is 16 Re h/Gamma.
L627 (2) bounds its absolute value only by

    64/75+160/L,          required total budget: 1/2.       (4)

This is an upper-bound cost for one degree, not an attained defect,
lower bound, impossibility theorem, negative direction or sign of K_c.
Higher degrees can cancel it. Even an improved first-degree estimate
would leave degrees two through eight to control. Thus the original
relative half-budget is neither proved nor refuted.

This uniform reduction is a local intermediate result, audited at the
scope in Section 5, without a priority claim or a positive detector
margin by itself. Pointwise signs and RH remain open. It permits a
finite arithmetic-operator test in place of a singular-germ remainder
problem.

## Proof

### 1. Uniform leading-pole reduction in the full Gram norm

Put z_j=i b_j. For a two-element subset I={i<j} of {1,2,3,4},
write its complement as J={k<l}, and define

    D_I(z)=product_(u in I,v in J)(z_u-z_v),
    l_I(z)=(sum_(u in I)z_u-sum_(v in J)z_v)/2,
    q_I(z)=(z_i,z_j,-z_k,-z_l)/L,
    F_T(z)=sum_(|I|=2) exp(l_I(z)) B_N(q_I(z);a)/D_I(z).

The order inside each pair is immaterial. The arithmetic function
is symmetric in alpha,beta and in gamma,delta. At a generic collision
z_u=z_v, terms with u in I and v outside I pair with the exchanged
subset. Their arithmetic values and exponential numerators agree,
and the simple pole residues have opposite signs. Terms with u,v
on the same side have no such pole. Multiplication by
Delta(z)=product_(u<v)(z_u-z_v) gives a holomorphic numerator
vanishing on each collision hyperplane. Successive division by its
distinct linear factors, using continuity on their intersections,
proves removability everywhere near zero. This is the residue argument
of L624 applied to the actual pair-symmetric arithmetic form.

Compare F_T with L628 Section 4's complete exact H_a(b). On the
separated torus |b_j|=j/4 every difference z_u-z_v has modulus
between 1/4 and 7/4. All q_I satisfy

    sum|q_I,j|=5/(2L),
    (log N)sum|q_I,j|<=1/40<1/16.

Hence L628 (2), with M=log N<=L/100, gives

    |B_N(q_I;a)| <= exp(3+420/L) Gamma <= exp(4) Gamma

for L>=420. This is a uniform bound on the complete infinite-space
arithmetic form, not an entrywise error summed over N coefficients.

The product of four zeta factors in L622's J, divided by L^4,
equals 1/D_I+O(1/L) on this torus. Its reciprocal zeta denominator
equals 6/pi^2+O(1/L). These estimates follow from the Laurent
expansion at 1 and analyticity near 2; all scaled differences range
over fixed compact sets away from zero. They are uniform in I and T.

For ell=log(t/(2pi)), the exponential in the I term is
exp((ell/L)(sum_I z-z1-z2)). L619 Section 3 gives, uniformly on
the same complex torus and T<=t<=3T,

    Phi(t,b)=exp((ell/(2L))(z1+z2-z3-z4))
                                        (1+O(1/(TL))).

Their product is exp((ell/L)l_I(z))(1+O(1/(TL))). Since
ell/L=1+O(1/L), it is exp(l_I(z))+O(1/L), uniformly.
Multiplying by the preceding uniform arithmetic bound, summing the
six terms, and using T^(-1) integral w_XT=1 proves on the torus

    H_a(b)-(6/pi^2)F_T(i b)=O_w(Gamma/L).

Both complete expressions are holomorphic inside the torus. For H_a
this is the named source holomorphy import; for F_T it was proved
above. Cauchy's formula therefore gives the same relative order for
each fixed derivative used in D_c. Its total Cauchy cost is at most
70, as computed in L628: 28 for Q and at most 5/2 for the observer.
This proves the O_w(Gamma/L) term in (1), uniformly in real unit c.
For a=0 the statement is identically zero. No estimate in this argument
is divided by a possibly small Euclidean smallest eigenvalue.

### 2. Exact finite polynomial extraction

For integers a>=b>=0 define

    m_ab(u,v)=u^a v^b+u^b v^a if a>b,
    m_aa(u,v)=u^a v^a.

Pair symmetry gives the convergent Taylor expansion, near zero,

    B_N(q_I(z);a)
      =sum_(a>=b,c>=d) h_(a,b,c,d) (-1)^(c+d)
                         m_ab(z_i,z_j)m_cd(z_k,z_l).

Let epsilon_I be the sign of the permutation (i,j,k,l). Then
Delta/D_I=epsilon_I(z_i-z_j)(z_k-z_l). For an output degree
d_out in {2,3,4} and a basis index nu=(a,b,c,d) with
k_nu=|nu|<=d_out+4, set r=d_out+4-k_nu and form the polynomial

    P_(nu,d_out)(z)=sum_(|I|=2) epsilon_I (-1)^(c+d)
         (z_i-z_j)(z_k-z_l)m_ab(z_i,z_j)m_cd(z_k,z_l)
                                      l_I(z)^r/r!.        (5)

If k_nu>d_out+4, define it to be zero. Every P is alternating:
relabeling the variables permutes the six subsets; reordering within
a pair changes the corresponding difference sign and the permutation
sign consistently. Equivalently P=Delta times its symmetric six-term
quotient away from collisions. Since it is a polynomial, vanishing
on each collision hyperplane proves divisibility by Delta. Therefore

    S_(nu,d_out)=P_(nu,d_out)/Delta                        (6)

is an exactly defined symmetric polynomial of degree d_out (or zero).

To check that no Taylor remainder is hidden here, replace z by t z
with noncolliding fixed z and expand in t near zero. D_I contributes
t^4 in its denominator. An arithmetic term of degree k_nu and an
exponential term of degree r therefore contribute only to degree
k_nu+r-4. For a coefficient of degree d_out<=4, k_nu<=8 is necessary.
Both the analytic expansion and the finite calculation agree away
from collisions and extend holomorphically across them. Negative
homogeneous degrees cancel. Degrees above eight cannot contribute.
This uses fixed-N analytic convergence, already justified in L624;
no uniform radius or interchange of an uncontrolled N-dependent
remainder is required. The uniform error was proved separately in
Section 1 before any extraction.

For a polynomial S let [e]S denote its coefficient at z^e. Define

    w_nu,0=2[2000]S_(nu,2)-[1100]S_(nu,2),
    w_nu,1=4[2010]S_(nu,3)-2[1110]S_(nu,3),
    w_nu,2=-2[2011]S_(nu,4)+[1111]S_(nu,4).              (7)

These definitions include all factorials. Indeed partial_bj=i partial_zj,
and Q_b becomes (partial_z1-partial_z2)^2/2. Symmetry of S makes
Q_b S(0)=2[2000]S-[1100]S at degree two. At degree three, the
sum of the two observer derivatives gives
i(4[2010]S-2[1110]S). At degree four their product gives
-2[2011]S+[1111]S. Expanding the common observer now proves (1)
with exactly the rational prescription (5)–(7).

### 3. Rational verification and the first unresolved cost

The reproducible exact-arithmetic calculation is

    python3 scripts/full_gram/signed_germ.py

It writes the complete coefficient table and checks to
`scripts/full_gram/signed_germ_certificate.json`. No zeta values,
finite-tail approximation or floating matrix enters this calculation.
Its input coefficients h_nu remain symbolic, including their complex
parts. The 175 indices are precisely the two separately sorted pairs
of nonnegative integers of total degree at most eight.

Here is a finite algebraic explanation of the two implemented methods.
An alternating homogeneous polynomial of degree d_out+6 expands
uniquely in alternants with strictly decreasing nonnegative exponent
tuples. Such tuples are lambda+(3,2,1,0), with lambda a partition
of d_out into at most four parts. The coefficient of the descending
monomial is the coefficient of that alternant. Formula (5)'s coefficient
at any such tuple is obtained by summing the six subsets, the at most
four pair monomials, and the four terms in the two pair differences;
the remaining exponents have exponential coefficient
product_j (s_j/2)^r_j/r_j!, where s_j=1 on I and -1 outside I.
This is the first implementation; division of each alternant by Delta
gives its polynomial and hence (7). This argument is elementary
polynomial algebra; no unassessed Schur-function theorem is imported.

The independent replay constructs (5) as a whole polynomial using
rational convolution, divides it exactly by Delta with lexicographic
polynomial division, multiplies back to verify equality, and extracts
(7) directly. It checks all 175 rows at all three output degrees,
not a sample or a numerical preview. The untwisted row (2) and the
pair-interchange symmetry are also checked. All checks passed.

As a further normalization check, replace B_N(q_I(z);a) symbolically
by exp(s(sum_I z-sum_J z)). This changes exp(l_I) into
exp((1+2s)l_I). Rescaling the four variables shows that
the degree-two and degree-four outputs acquire factors (1+2s)^6 and
(1+2s)^8; the odd output stays zero. The table reproduces all nine
coefficients of these identities exactly. This is a polynomial check,
not an assertion that this symbolic function is an actual B_N.

For the only degree-one rows, the exact weights are

    nu=(1,0,0,0): (1/30,  1/180, 1/630),
    nu=(0,0,1,0): (1/30, -1/180, 1/630).

For real q, the full arithmetic identity gives
conjugate(B_N(alpha,beta,gamma,delta;a))
=B_N(gamma,delta,alpha,beta;a): C_N has real Taylor coefficients
and is invariant under pair interchange, and the two convolution
vectors exchange roles. Thus the second degree-one coefficient is
conjugate(h). Taking the real part yields (3), including its mixed
observer sign. The zero row gives exactly (2), reproducing L619's
untwisted normalization. The certificate's absolute sums of weights
at degree eight are (0,0,40); degree eight is not absent in general.

Finally L627 (2) gives |h|/Gamma<=4/75+10/L. For c=(0,1),
divide (3) by Gamma/(840pi^2) to obtain (4). The limit 64/75
exceeds 1/2 already at degree one. This only diagnoses the insufficiency
of this available termwise budget. It cannot rule out a sharper
first-jet estimate, cancellation between degrees, or the actual
full relative comparison. No actual arithmetic coefficients have
been chosen to attain these bounds.

### 4. Scope and continuation boundary

The main target still requires controlling the exact sum in (1)
relative to B(c)Gamma/2, with room for its uniform O(Gamma/L) error.
The all-degree norm majorant and a sum of absolute first-jet costs
do not supply that control. This attempt stops without a signed
estimate. Its material new input is the uniform finite-jet reduction
with exact coefficients, rather than a smaller unsupported constant.

A possible independently testable refinement is to bound the numerical
radius of L627's centered multiplier compressed to the rational basis
indices n<=N. Compression is exact for the scalar first jet
< (mu_N-H)f,f >, although it would not be exact for its full output
norm. A bound (2 log N+C)Gamma would reduce the c1-only first-degree
cost to 8/25+o(1). This bound is a proposal, not derived or approved
here; degrees two through eight and mixed-observer control remain.
Its changed exact target requires a separate source review.

### 5. Independent used-scope audit, 1 November 2026

The relative transfer (1) and the exact extraction (5)–(7) pass
this audit under the named Hughes--Young holomorphy and moment
imports. L628 Section 6 independently checks its load-bearing
bound (2); no unresolved local norm estimate is hidden in this
audit. Its other signed bound and L627's first-jet costs are not
needed. The audit does not verify the external manuscript proofs.

**Arithmetic identity and uniform norm.** Expanding the full
convolution at a pair m,n sets r=lcm(m,n)d, with
r/m=(n/g)d and r/n=(m/g)d. Thus the second divisor function is
incremented on the h=m/g side, and the first on k=n/g, as in
L622's source convention. The square-root factor is exactly
1/(sqrt(hk)d). The finite-prime product after multiplying by C_N
therefore gives the specified arithmetic entry in all six terms.
For a compact |Re q_j|<=rho<1/4, geometric series with polynomial
exponent factors dominate all fixed derivatives. This proves
fixed-N convergence and holomorphy; uniformity instead comes from
L628 (2), not from that fixed-N argument.

On the four-circle boundary |b_j|=j/4, every difference has
modulus in [1/4,7/4], while S=5/(2L), SM<=1/40. L628's bound
is exp(3+420/L)Gamma<=exp(4)Gamma for L>=420. All six
permutations preserve these facts. The zeta Laurent expansion,
the reciprocal zeta factor analytic near 2, and the L619 complex
phase estimate consequently give the claimed O_w(Gamma/L)
difference between H_a and (6/pi^2)F_T on this entire torus.
The sign in the exponent is checked directly: the source factor
contributes (ell/L)(sum_I z-z1-z2), and the exact Hardy phase
contributes (ell/(2L))(z1+z2-z3-z4)+O(1/(TL)). Their sum is
(ell/L)l_I+O(1/(TL)); ell/L=1+O(1/L) uniformly on [T,3T].
Nonnegative w with integral one normalizes the t-integral by T.

At a generic collision the exchanged subsets have identical
numerators and opposite residues. Multiplying F_T by Delta gives
a holomorphic alternating numerator; each collision linear factor
divides it. After dividing one factor, vanishing on the generic
part of every other hyperplane remains, and continuity extends it
to their intersections. Successive division therefore removes all
factors, including multiple collisions. H_a is holomorphic by the
named complete-sum import. Cauchy extraction applies to their
complete difference, with Q cost 8+16+4=28 and observer cost
(|c0|+4|c1|/3)(|c0|+|c1|)<=5sqrt(2)/3<5/2. Hence 70 is a
valid common bound, independent of c, X and the coefficient vector.
This proves (1). K_c is the exact six-term matrix of L622;
no absolute moment error is silently incorporated into its definition.

**Finite algebra.** For an arithmetic degree k and exponential
degree r the homogeneous quotient has degree k+r-4. Thus output
degrees 2,3,4 require k<=6,7,8 respectively. Alternation cancels
negative degrees, since no nonzero alternating polynomial in four
variables has degree below Delta's degree six. On any noncolliding
ray the convergent analytic expansion gives this coefficient
calculation directly; removability extends it to the germ at zero.
The Taylor coefficient is already partial^nu/(nu! L^|nu|).
In particular no further factorial or orbit multiplier is allowed.

The independent script
`scripts/full_gram/full_observer_row_budget_audit.py` imports no
notebook calculation module. It constructs Delta as its six linear
factors, divides it by each cross product D_I to obtain the signed
prefactor, builds each full homogeneous numerator and divides back
by Delta. It then applies the original differential operators,
including their factorials, without relying on the simplified
symmetric formulas in (7). All 525 complete quotients and all
three channel weights match the saved certificate for all 175
pair orbits. Thus the table covers all 495 multi-indices, and the
imaginary channel has been checked independently of the two even
channels. The constant row and all pair-exchange signs also pass.
Full evidence is in
`scripts/full_gram/full_observer_row_budget_audit_certificate.json`.

**Separate actual-Xi error.** To use (1) for the signed integral,
L622 (1) must still be applied. Its error for arbitrary a is
epsilon_T ||a||^2 by homogeneity. L623's lower bound was checked
directly: the finite convolution inverse has norm at most
2sqrt(N)(1+log N), while the positive product C_N is at least
2/[N^3(N+1)]. Discarding tail squares is used only for this
zero-shift lower bound. Therefore

    Gamma >= gamma_N ||a||^2,
    gamma_N >= T^(-1/20)/[4(1+L/100)^2],
    epsilon_T/gamma_N <= 4 C_w(1+L/100)^2
        [T^(-13/80)/L^4 + T^(-97/50)/L^2] = o(1/L).

The exponents are exactly 17/80-1/20=13/80 and
199/100-1/20=97/50. This is uniform in X and all vectors;
B(c)>=1/(840pi^2) also makes it uniform after division by B(c).
For a=0 every term vanishes. This conversion closes the absolute
versus relative error issue used in L635's actual-Xi application.
It supplies no effective onset and no pointwise positivity.

## Mathlib

Full matching coverage of this uniform full-Gram signed-jet reduction
and the numerical constants was not checked and is unknown. The
source holomorphy, phase and zeta facts are the named inputs above;
the rational polynomial construction and error specialization are
proved here. The certificate verifies finite algebra, not the named
analytic imports, actual arithmetic-jet bounds, positivity or RH.
There is no Lean certificate or independent critical audit claim.
