# L554 — Nonzero-row presentation with a fixed ray modulus

## Hypotheses

Work in O=Z[omega], omega=exp(2pi i/3), lambda=1+2omega, and
F=Q(omega). O is a PID; its six units have distinct residues modulo
3. Each ideal prime to lambda therefore has a unique primary generator
(congruent to 1 modulo 3), and these generators multiply. Write q_a
for the norm and e(z)=exp(2pi i Tr(z/lambda)). Fix a finite set S of
prime ideals containing those above 6, and a finite family N of finite
ray characters. The supports of their entire defining moduli, including
redundant zero primes, lie in S. All these data are fixed before rows
or good primes vary. Fix a generator pi_l for each l in S. Good means
outside S; good prime generators are primary.

For a good prime p, chi_p(x) is the sixth root congruent to
x^((q_p-1)/6) modulo p when p does not divide x. Every integer power,
including exponent zero, is zero when p divides x. On primary good
A, define chi_A(x)=product_(p|A) chi_p(x)^(v_p(A)); chi_1(x)=1.
This definition permits nonsquarefree A. The square of the sextic
symbol is the ordinary cubic symbol. Import cubic reciprocity and its
supplementary laws from DR (1.4)–(1.5), and the fixed-numerator ray
character theorem from Milne VIII (5.3), (5.5), with domains below.

Use L555's independently checked quadratic evaluation on c=p or c=pq
for distinct good primary primes. On this domain put

\[
 H(c)=q_c^{-1/2}\sum_{x\bmod c}e(x^2/c)
     =\frac12\sum_{y\bmod2O}e(-cy^2/4)=:h([c]).
                                                        \tag{1}
\]

Define h for every odd argument by the finite expression on the right,
including arguments outside the good prime/product domain. In
G=(O/4O)^*/((O/4O)^*)^2 the representatives are
1,-1,lambda,-lambda. The values of h are respectively 1,1,i,-i;
h depends only on this square class. Consequently the table gives

\[
 R((-1)^a\lambda^b,(-1)^c\lambda^d)
 :=\frac{h((-1)^{a+c}\lambda^{b+d})}
          {h((-1)^a\lambda^b)h((-1)^c\lambda^d)}
 =(-1)^{ad+bc+bd}.                                      \tag{2}
\]

Here exponents in classes are modulo two. This sign bicharacter is
defined also for colliding primary good arguments using their residue
classes, never as a quotient of residue symbols. L555 proves (1)
on the needed domain and checks this full finite table and correction.
No Gaussian evaluation for other moduli or limit uniform in c is
needed in this proof.

Take k in O, k!=0; a squarefree good ideal f, identified with its
primary generator; and rho(A)=1_((A,rho_rad)=1), with rho_rad a fixed
squarefree ideal within the invocation. It may have S-primes, which
are immaterial on good A. Choose nu in N and, for primary good A, set

\[
 \Psi_k(A)=\nu(A)\rho(A)\chi_A(k)\chi_A(f)^4.              \tag{3}
\]

Finite mark lists are pairwise disjoint lists of good primes, with
one prime chosen from each, and literal product coefficients
product_i a_i(p_i). Retain their stipulated independence from row,
label and dual indices. No assertion for k=0 is included.

## Conclusion

There is a finite family X of ray characters and one integral ideal E
and element L!=0, all depending only on S, its chosen generators and
N, such that E and (L) have support exactly S, every character in X
has conductor dividing E, E divides (L), and (18) divides (L).
Members of X are extended by zero off primary E-units. For each such
member Psi_0 the function

\[
 \phi(x)=\begin{cases}
       \chi_x(\lambda)^2\Psi_0(x),&x\equiv1\ (3),\ (x,E)=1,\\
       0,&\text{otherwise}
       \end{cases}                                      \tag{4}
\]

is L-periodic. The zero branch is evaluated first.

Write k=u k_S k_g using the fixed S-generators and primary good
generators. One member Psi_0=Psi_0^[k,nu] in X satisfies, literally
on all primary good A,

\[
 \begin{split}
 P&=\{p\notin S:p\mid k_g f\rho_{\rm rad}\},\\
 j_p&=v_p(k)+4\,1_{p\mid f}\pmod6,\qquad 0\le j_p<6,\\
 \Psi_k(A)&=\Psi_0(A)\prod_{p\in P}\chi_p(A)^{j_p}.       \tag{5}
 \end{split}
\]

No prime is removed from P when j_p=0. The member is determined by
nu, u, the S-valuations of k modulo six, and [k_g] in G. Neither
good primes of k, f or the puncture nor their sizes enter E or L.
The unit row and empty good radical are included.

For n squarefree primary good and b arbitrary primary good, with
shared primes permitted, (5) gives the exact whole-index identity

\[
 \Psi_k(nb^3)=\Psi_k(n)\Psi_k(b)^3
 =\Psi_0(n)\Psi_0(b)^3
       \prod_{p\in P}\chi_p(n)^{j_p}\chi_p(b)^{3j_p}.
                                                        \tag{6}
\]

Thus this supplies the row-presentation premise of L548 and L553
for these data. Apply their fixed-data identities only under their
remaining hypotheses and L547's canonical conventions. A marked
tuple meeting P contributes zero to the primal sum, even at j_p=0;
noncolliding tuples meet L553's disjointness hypothesis. No raw theta,
coefficient or other Gauss bound, arithmetic-uniform estimate, varying-S
claim, effective conductor bound, global closure or Xi sign follows.
This is a reproduction of the cited source claim. The presentation
implication passed the separate critical review below; L555 subsequently
discharged its quadratic premise on exactly the prime/product domain used.
The Milne/DR imports and remaining analytic inputs retain their qualifications.

## Proof

### Precise imports and why the application is checked

The target is OpenAI, *The Quasi-Riemann Hypothesis*, 30 September
2026, commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a,
[pinned primary TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
`lem:reflection-row-sectors`, complete statement/proof 2320–2380,
and application definitions 6825–6907. The defining-zero conventions
are 540–588; common E,L hypotheses are 1561–1588 and their
periodicity check is 1873–1880. These final presentation assertions
are being checked, rather than imported as their own proof.
The source of (1), its table and (2) is
`lem:quadratic-four-term`, `eq:reciprocity-four-class`, 772–799.
Their independent fixed-modulus Poisson/Gaussian application audit is L555.
The relevant CRT and cubic reciprocity argument is 899–927; no
other Gauss-phase identity from that lemma is needed.

Import J. S. Milne, *Class Field Theory*, v4.03 (6 August 2020),
[author's PDF](https://www.jmilne.org/math/CourseNotes/CFT.pdf),
Chapter VIII Section 5, printed pp. 244–245, power-residue definition,
(5.3) and (5.5), including their proofs (PDF page indices 252–253).
For K containing mu_m and d in K^*, the ideal argument avoids all
primes dividing m or having nonzero valuation of d. On this domain
the m-th power symbol is arithmetic Frobenius acting on d^(1/m),
and is a finite ray character with some modulus supported at those
primes. Take K=F, m=6 and only the fixed numerators used below.
Its defining root is the same residue-field power as chi; no inverse
Frobenius or complex conjugation is introduced. Milne prescribes no
value on excluded ideals and no uniform conductor exponent for
moving numerators. We use neither such extension nor such bound.

Import Dunn–Radziwill, *Bias in cubic Gauss sums: Patterson's
conjecture*, Annals of Mathematics 200 (2024), 967–1057,
[arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3),
Section 1.2, (1.4)–(1.5). On coprime primary a,b, cubic reciprocity
interchanges (a/b)_3 and (b/a)_3. For primary
d=1+alpha_2 lambda^2+alpha_3 lambda^3 modulo 9, their supplementary
law is (lambda/d)_3=omega^(-alpha_3). In particular it depends only
on d modulo 9. These arithmetic inputs do not assume the paper's
GRH-dependent prime asymptotics. The remaining work is their precise
finite-family and zero-preserving specialization, not a reproof of
class field theory; the quadratic identity is checked separately in L555.

### Reciprocity on the coprime domain

For a good prime p, chi_p^3 is its quadratic residue character.
The additive character x -> e(x/p) on O/(p) is nontrivial: writing
p=a+b omega, e(1/p)=exp(-2pi i b/q_p) and
e(omega/p)=exp(2pi i a/q_p). If both were one, q_p would divide
a and b, impossible since q_p=a^2-ab+b^2>1. Thus its full sum
is zero. Counting the roots of x^2=y in the odd residue field gives

\[
 H(p)=q_p^{-1/2}\sum_{y\bmod p}\chi_p(y)^3e(y/p).
\]

For a unit t modulo p, substitution y -> t^(-1)y shows that
q_p^(-1/2) sum_x e(t x^2/p)=chi_p(t)^3 H(p). For distinct
good p,q use the CRT representatives qx+py. Cross terms in
(qx+py)^2/(pq) are integral and e is one on O. Norms multiply,
so the preceding twist identity yields

\[
 H(pq)=\chi_p(q)^3\chi_q(p)^3 H(p)H(q).
\]

L555's nonzero table and (2) identify the quotient with
R([p],[q]). Put z=chi_q(p)/chi_p(q), which is defined here because
p,q are distinct. Cubic reciprocity gives z^2=1. Its cube is
chi_q(p)^3 chi_p(q)^(-3)=chi_q(p)^3 chi_p(q)^3, since both
cubed factors are signs. Therefore z=z^3=R([p],[q]).
Multiplying this equality over the disjoint prime supports, with
their arbitrary positive multiplicities, proves

\[
 \chi_b(a)=R([a],[b])\chi_a(b)
       \quad ((a,b)=1,\ a,b\text{ primary good}).           \tag{7}
\]

There is no prime-pair division at a shared prime. For such pairs
R is still defined by (2), and uses no residue symbol quotient.

### The residue class is an ideal ray datum

For every good ideal a, [a] is the class of its primary generator
in G. Multiplicativity of primary generators makes this a monoid
homomorphism, extending to fractional ideals prime to S by inverses.
The same formula is defined for every ideal prime to 6, not merely
the good ideals, since its primary generator is then a unit modulo 4.
It factors through the ideal ray group modulo (12). Indeed, if
a b^(-1)=(t) with t=1 modulo 12 locally at 2 and 3, the quotient
of their primary generators is u t for a unit u. Its reduction
modulo 3 is one, so u=1 by the distinct six unit residues. Hence
the two generators have the same residue modulo 4, and the same
class in G. This argument also works for fractional generators by
using local units at these primes. Thus A -> R([A],g), for fixed
g in G, is a finite ray character of modulus dividing (12).
There are at most four such characters. In particular the class
-1 here belongs to G; it is not the ideal ray class of the unit
ideal (-1). No ideal character taking a nontrivial value on a unit
ideal has been introduced.

### Finite numerators, common modulus and supplementary factor

Write v_l(k)=6t_l+e_l, 0<=e_l<6. On good A, all factors
u, pi_l and their products are units modulo A; their symbols are
sixth roots. Thus, with d=u product_(l in S) pi_l^(e_l),

\[
 \chi_A(u k_S)=\chi_A(d).
\]

There are at most 6^(|S|+1) such d, each nonzero and supported
in S. For each one, Milne's theorem applies to all good ideals A:
the primes dividing 6d are in S. Its ray character r_d(A) agrees
with chi_A(d) by the matched prime definitions and multiplicativity.
This does not require k_g to be fixed, because k_g never occurs
in d. Take products of the finitely many r_d, the base characters
nu in N, and the at most four characters R([A],g). These are the
finite family X on good ideals.

Choose an integral ideal E divisible by all their conductors, by
their fixed defining moduli, by (12), and by product_(l in S) l.
All these supports are contained in S, and the last factor makes
its support exactly S. Extend each member by zero off primary
E-units. This preserves its values on all primary good A and
retains the entire required S-mask, even where a primitive
conductor omits a prime. Because O is a PID, choose L generating
the ideal E(18). Then E divides (L), (18) divides (L), and (9)
divides (L); its support is S. No numerical conductor exponent
has been asserted.

If x,y have the same residue modulo L, the primary condition and
the E-unit condition in (4) agree. On their common nonzero branch
x/y=1 modulo E locally at its primes, so their principal ideals
have the same ray class for every conductor dividing E. Hence
Psi_0(x)=Psi_0(y). The supplementary law from DR gives equality
of chi_x(lambda)^2=(lambda/x)_3 and its y counterpart because
x=y modulo 9. This proves (4)'s periodicity. If either condition
fails both function values are defined as zero before symbols
are evaluated. In particular x=0 causes no undefined symbol.
E and L were chosen before k_g, f or rho_rad; the sector modulus
lambda^12 L^4 and its square in L547 are consequently fixed too.

### Literal row presentation and all overlaps

First suppose (A,k_g)=1. Multiplicativity in the numerator and
(7), with a=A and b=k_g, give

\[
 \chi_A(k)=\chi_A(u k_S)R([A],[k_g])
                 \prod_{p\mid k_g}\chi_p(A)^{v_p(k)}.      \tag{8}
\]

The reciprocal orientation is harmless because R takes values
in {+1,-1}. If p divides both A and k_g, chi_A(k)=0 by its
definition; the displayed local factor is also zero even if
6 divides v_p(k). The other factors are defined and finite,
so (8) holds on that case as well. For A=1 or k_g=1 the
corresponding products and classes are identities; the proof
needs neither a nonempty prime set nor a nonunit row.

Define Psi_0 on the primary good branch to be
nu(A)r_d(A)R([A],[k_g]), with the zero extension already chosen.
It belongs to X. For coprime A,f, (7) gives
chi_A(f)^4=R([A],[f])^4 chi_f(A)^4=chi_f(A)^4.
If A and f meet, both fourth powers vanish. This proves on
every primary good A that

\[
 \chi_A(f)^4=\prod_{p\mid f}\chi_p(A)^4.
\]

The puncture equals product_(p|rho_rad, p notin S) chi_p(A)^0
on this same domain; its S-primes impose no further restriction.
Combine this identity and (8). At each p in their union, for
p not dividing A multiplication adds the ordinary integer
exponents and reduction modulo six is valid. For p dividing A,
at least one prescribed local factor is zero, and the combined
factor remains zero for every j_p, including zero. Thus the
pointwise product is exactly (5) on both cases. Examples covered
without exceptions include v_p(k)=6t>0, the cancellation
v_p(k)=2 modulo 6 with p|f, a puncture prime occurring nowhere
else, and all double or triple intersections. Dropping a zero
power from P would fail these identities; it is never done.

### Whole indices and mark collisions

The ray factor is multiplicative on good ideals. For every local
factor in (5), if p divides nb^3 then p divides n or b. Its value
on nb^3 and the product of its values on n and b^3 are both zero.
If p divides neither, usual character multiplicativity proves
the equality. This applies when p divides both n,b and at j_p=0.
It also applies to the additional cube of a zero value, which is
an ordinary positive third power. Multiplying these equalities
gives (6), for nonsquarefree b and all shared primes. The E-mask
on nb^3 is precisely the conjunction of the masks on n and b.

In the L548 theta multiplier, the supplementary factor causes
no extra discrepancy: on the good domain,
chi_(nb^3)(lambda)^2=chi_n(lambda)^2 chi_b(lambda)^6
=chi_n(lambda)^2. Off that domain the piecewise E-mask is used
first. Thus (4)–(6) are literally the presentation required in
L548, not only an equality on coprime n,b.

For a marked tuple let Q be its chosen primes. Pairwise disjoint
lists make them distinct. If Q meets P, choose p in the intersection.
The mark requires p|nb^3 and the local factor of (6) then vanishes,
including at exponent zero. The marked summand is zero for every
n,b; its entire tuple contribution is zero. Otherwise Q and P
are disjoint and L553 applies with base set P and the same fixed
Psi_0,E,L. Multiplying by the tuple's original coefficient and
summing a finite set of tuples preserves the identity. No
row-dependent replacement for a product coefficient is made.
The existing analytic and branch hypotheses of L547/L548/L553
remain inputs to their application; this arithmetic verification
does not replace them or prove a uniform bound for their sums.

### Independent presentation review, 2026-10-31

The fixed-data presentation and its stated application passed this review
conditional on the explicit Gaussian input (1) and its table. That
review did not certify the input or the remaining analytic imports.
The later L555 audit discharges precisely the quadratic input used here;
the following records the earlier presentation review without broadening it.
The following are the load-bearing checks, rather than an import of
the source's final row-sector lemma.

Milne VIII Section 5 defines the symbol by the unique sixth root
congruent to d^((Np-1)/6). His (5.3) uses Frobenius x -> x^(Np),
not its inverse, and (5.5) gives support within the primes dividing
6d. Thus the imported character is r_d(A)=chi_A(d) on every good
ideal, including prime powers; no conjugation or extra local factor
is required. Each d is nonzero and S-supported. The finite choice of
d precedes the choice of every moving prime, so taking a common
modulus is legitimate. Retaining all defining-modulus primes in E
preserves imprimitive zero masks without changing good values.

In the CRT argument, e is trivial on O, and e(x/p) is nontrivial:
if q_p divided both coordinates a,b of p, writing a=q_p a',
b=q_p b' would give 1=q_p(a'^2-a'b'+b'^2), impossible for
q_p>1. Hence the unweighted additive sum vanishes. Distinct-prime
quadratic twisting and cubic reciprocity give z^2=1 and z^3=R,
so z=R with exactly the orientation of (7). Multiplicative extension
uses disjoint supports only. At collisions the proof instead uses
the zero definitions, never division of residue symbols.

The generator-class map is an ideal ray datum: for a ray-principal
quotient modulo (12), its primary-generator quotient is u t with
t=1 locally modulo (12). Reduction modulo (3) forces u=1, and
reduction modulo (4) then identifies the generator classes. The
same reasoning applies to fractional ideals prime to 6. In particular
the ideal (1)=(-1) has primary generator 1 and gives the trivial
class; the residue class [-1] used in R is not assigned to that
ideal. Every R-character therefore has a modulus supported in S.
Taking E as in the proof and (L)=E(18) preserves this support, and
the DR supplementary law makes (4) periodic because (9)|(L).
The zero branch deals with all nonprimary or non-E-unit inputs first.

For each union prime p, there are just two cases. If p does not
divide A, all factors are roots of unity, exponents add, and reduction
modulo six is valid. If p divides A, at least one original row,
label or puncture factor is zero, and the combined local factor is
zero for every residue j_p. This covers six-divisible row exponents,
row-label cancellation, puncture-only primes and every intersection;
the fourth-power label correction is one on the coprime domain.
For A=nb^3, p divides A iff it divides n or b; both sides of (6)
then vanish, even when n,b share p or j_p=0. Otherwise ordinary
multiplicativity applies. Unit rows and empty P use empty products,
and the supplementary b-factor is a sixth power of a nonzero value
on the good branch. Finally every marked collision forces that same
zero; noncolliding tuples satisfy L553's disjointness hypothesis
without changing their product coefficients or the fixed modulus.

Primary statements rechecked: Milne v4.03 printed pp. 244–245,
DR v3 Section 1.2 (1.4)–(1.5), and the pinned source's four-term
statement 772–800, reciprocity case 899–927, row lemma 2320–2380
and application 6873–6907. Those checks established the conditional
presentation already claimed, not progress beyond those sources.
That presentation review added no new mathematical dependency or stronger
uniformity claim; the subsequent quadratic input is supplied by L555.

## Mathlib

Full matching coverage has not been checked. The imported arithmetic
theorems are precisely Milne VIII (5.3)/(5.5) and DR (1.4)/(1.5).
L555 supplies the needed Gaussian evaluation with its own precise
analytic citations and Mathlib qualifications. No assertion of a matching
Mathlib theorem, or of its absence, is made. This finite application does
not formalize class field theory or the Gaussian calculation.
