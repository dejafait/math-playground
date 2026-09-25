# L008 — Primitive divisors do not supply the required multiplicity

## Hypotheses

For the application, take the parameters and sequences extracted in L007, with prime p >= 17. In particular r,t are odd and coprime, v=(r^2+3t^2)/4 is 1 modulo 12, gcd(r,v)=gcd(t,v)=1, and 3 divides t. The complete coefficient equality is retained when drawing conclusions about its positive integer k.

The separate multiplicity construction below assumes no solution of that complete equality. It uses p=31 and the same recurrence U_0=0, U_1=1, T_0=2, T_1=r, X_(n+2)=rX_(n+1)-vX_n.

## Conclusion

The pair gamma=(r+t sqrt(-3))/2 and its conjugate is a nondegenerate Lucas pair. The cited primitive-divisor results in foundations/05-primitive-divisor-theorem.md apply: U_p has a primitive prime divisor ell. Every such divisor satisfies

\[
\ell\nmid 6ptv,\qquad \ell\equiv 1\text{ or }-1\pmod{6p}.
\]

For either complete coefficient shape U_p=sigma k^p or sigma p k^p in L007, this yields ell dividing k and k >= 6p-1. It supplies no upper height bound or contradiction.

The absence of a valuation restriction is substantive even after retaining the parameter shape and trace inequality. For every positive integer M there are infinitely many positive odd coprime r,t, with

\[
t=3^{29}h^{31},\quad 31\nmid h,\quad
v=(r^2+3t^2)/4\equiv1\pmod {12},\quad
\gcd(r,v)=\gcd(t,v)=1,
\]

such that 373 is a primitive divisor of U_31 and

\[
v_{373}(U_{31})=M,\qquad
tU_{31}>0,\qquad |T_{31}|<3tU_{31}.
\tag{1}
\]

In particular M=31 is compatible with the multiplicity required of an individual divisor of a 31st power. This construction does **not** assert U_31=k^31. It refutes a universal claim that primitive divisors in this constrained parameter family have small or index-indivisible multiplicity. It does not refute a possible theorem guaranteeing that some other divisor has unsuitable multiplicity, nor does it settle the complete simultaneous equation.

## Proof

**Eligibility and theorem range.** The two conjugates are algebraic integers, being roots of X^2-rX+v. Their sum r and product v are nonzero coprime integers by L007. Since t is a nonzero multiple of 3, v>1. If xi=gamma/bar(gamma) were a root of unity, then xi+xi^(-1) would be an algebraic integer. But

\[
\xi+\xi^{-1}=r^2/v-2
\]

is rational, so would be an ordinary integer. This forces v to divide r^2, contradicting gcd(r,v)=1 and v>1. Thus the pair is nondegenerate. Theorem 1.4 supplies a primitive divisor for p>30; Theorem C and Table 1 cover the four prime indices from 17 through 29. The precise source and definition are recorded in the foundation cited above; the small-index range is not inferred from the large-index theorem.

**What a primitive divisor actually implies.** The discriminant is -3t^2, so primitivity excludes 3 and all factors of t. The recurrence modulo a prime factor of v gives U_n congruent to r^(n-1) for n>=1, excluding factors of v. Modulo 2 the U sequence has period three, with residues 0,1,1; hence U_p is odd. Finally L007 shows that p divides U_p only when p divides t, which is incompatible with primitivity. This proves ell does not divide 6ptv.

Over the field with ell elements or its quadratic extension, let alpha,beta be the two distinct nonzero roots of X^2-rX+v. The ratio alpha/beta has order exactly p: its pth power is one since ell divides U_p, while it is not one since the roots are distinct. Put epsilon=1 when -3 is a square modulo ell and epsilon=-1 otherwise. In the first case the ratio belongs to the multiplicative group of the base field, so p divides ell-1. In the second, Frobenius interchanges alpha,beta, so the ratio's ellth power is its inverse, and p divides ell+1. Thus ell is epsilon modulo p.

For ell>3, a square root of -3 exists precisely when the polynomial X^2+X+1 has its two nontrivial cube roots in the base field. The cyclic multiplicative group has such roots precisely when ell is 1 modulo 3. Consequently ell is also epsilon modulo 3. Combining the two congruences and the oddness of ell gives ell congruent to epsilon modulo 6p. Therefore ell>=6p-1. Since ell is not p, either complete shape from L007 forces ell to divide k, proving the claimed lower bound. All its valuations could still be multiples of p; finding one divisor has not produced the needed conflicting valuation.

**A simple primitive root at p=31.** Put q=373 and t_0=3^29. For fixed t define the integer polynomial

\[
F(X,t)=\sum_{j=0}^{15}\binom{31}{2j+1}X^{30-2j}(-3t^2)^j.
\]

The coefficient formula in L007 gives F(r,t)=2^30 U_31 when r,t are odd and v=(r^2+3t^2)/4. Polynomial evaluations at other residues do not require v to be an integer. Trial division by the primes at most 19 proves q prime. Modulo q,

\[
177^2=-3,\quad t_0=300,\quad 177t_0=134,
\quad 4+134=138,\quad4-134=243.
\]

The ratio 138/243 is 217. Successive squaring gives residues 217,91,75,30,154 at exponents 1,2,4,8,16, respectively, and 217^31=1; since 31 is prime and 217 is not one, its order is 31. Thus F(4,t_0)=0 modulo q. More explicitly, writing s=134 and using

\[
F(X,t_0)=\frac{(X+s)^{31}-(X-s)^{31}}{2s}\pmod q,
\]

both numerator powers at X=4 are 285. Differentiation at this root gives

\[
F_X(4,t_0)=-\frac{31\cdot285}{138\cdot243}=90\ne0\pmod q.
\tag{2}
\]

These modular identities are finite integer calculations; no factorization of a large Lucas number is presumed.

**Exact arbitrary multiplicity.** Starting from the root 4 modulo q, lift uniquely to a root a_M modulo q^M, taking 0<=a_M<q^M. This can be proved without citing a lifting theorem: if F(a,t_0)=0 modulo q^j, then

\[
F(a+cq^j,t_0)\equiv F(a,t_0)+cq^j F_X(a,t_0)
\pmod {q^{j+1}}.
\]

The derivative stays 90 modulo q, so exactly one c modulo q lifts the root. At the next digit choose any of the other q-1 residues. This gives b_M modulo Q=q^(M+1) with exact valuation v_q(F(b_M,t_0))=M. The term "exact" refers to every integer representative of that class; adding Q cannot alter the first nonzero q-adic digit.

**Retaining the norm restrictions and trace inequality.** Choose a positive integer D by the Chinese remainder theorem such that

\[
D\equiv b_M-33t_0\pmod Q,\qquad
D\equiv5-33t_0\pmod {24}.
\]

For each positive integer N put

\[
h=1+24\cdot31\cdot QDN,\qquad
t=t_0h^{31},\qquad r=33t+D.
\tag{3}
\]

Then h is odd, is 1 modulo 31QD, and is 1 modulo 24. Thus t is t_0 modulo Q and 24, and r is b_M modulo Q and 5 modulo 24. In particular 3 does not divide D, because D is 2 modulo 3. Also gcd(D,h)=1. Therefore gcd(r,t)=gcd(D,t)=1. The same norm argument as in L007 gives gcd(r,v)=gcd(t,v)=1, since 3 does not divide r. Here v is an integer because r,t are odd. Since t_0 is 3 modulo 24, squares modulo 48 give r^2=25 and 3t^2=27, whence v is 1 modulo 12. Increasing N produces infinitely many distinct pairs.

The congruences modulo Q preserve the exact valuation M of F(r,t), hence of U_31. Modulo q the two characteristic roots have ratio 217 as above. Their product is nonzero and their discriminant is nonzero. Since the ratio has order 31, no U_j with 1<=j<31 vanishes modulo q. Thus q is primitive, regardless of M.

It remains to prove the actual strict trace inequality, rather than assuming positivity from the norm. Formula (3) gives t>D>0, hence 33<r/t<34. Write gamma=sqrt(v) exp(i theta), with theta=arctan(sqrt(3)t/r). The inequalities 5/3<sqrt(3)<7/4 and x-x^3/3<arctan x<x for x>0 give

\[
31\left(\frac5{102}-\frac13\left(\frac7{132}\right)^3\right)
<31\theta<\frac{217}{132}.
\]

The left bound exceeds 3/2 and the right is less than 2. Since 3<pi<4, this interval lies inside (pi/3,2pi/3). Consequently sin(31 theta)>0 and |cos(31 theta)|<sqrt(3) sin(31 theta). Now

\[
T_{31}=2v^{31/2}\cos(31\theta),\qquad
tU_{31}=\frac{2v^{31/2}}{\sqrt3}\sin(31\theta),
\]

which proves (1). No perfect-power condition on U_31 was used.

**Discriminating test and qualification.** A direct contradiction from primitive-divisor existence would need the theorem's supplied divisor to have valuation not divisible by p. The construction proves that primitivity, the norm conditions, the exact first-case shape of t, and even the trace inequality do not individually force this property of a given divisor. At M=31 that divisor has exactly the allowed multiplicity. This does not prove that every primitive divisor has allowed multiplicity, and does not assert that the whole U_31 is a 31st power. Therefore the complete coefficient system remains open; only the direct existence-to-forbidden-multiplicity inference is stopped.

The exact controls in scripts/primitive-divisors/check_multiplicity.py use M=1,2,31 and N=1. They check the recurrence, polynomial congruence, absence from earlier terms, exact valuation, coprimality, norm identity, and strict trace bound. All three controls fail the complete power condition already modulo 311, whose 31st-power residues are explicitly enumerated in scripts/primitive-divisors/results.json. Thus these controls are not Beal solutions. Reproduce with `python3 scripts/primitive-divisors/check_multiplicity.py`. These finite checks support the explicit construction; the argument above proves it for every M and N.

The achieved application is divisor existence and the lower bound k>=6p-1. The required family threshold is zero complete solutions, or a global obstruction forcing an unsuitable valuation for every candidate pair. Neither follows from a lower bound or the multiplicity controls.

## Mathlib

Coverage of the full statement: **not checked**. Supporting declarations for Lucas primitive divisors, finite-field orders, polynomial lifting, and the Chinese remainder theorem: **not checked**. No absence or formal-verification claim is made. The imported named theorems and their direct source links are in foundations/05-primitive-divisor-theorem.md; the multiplicity construction and congruence deduction are proved above.
