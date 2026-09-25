# L006 — Fixed-slack differential interpolation

## Hypotheses

Fix a real number 0<gamma<1. Define the following real constants, depending
only on gamma:

\[
 \theta=\gamma/2,\quad u_0=(1-\theta)^{-1},\quad
 c=(1+u_0)/2,\quad s=(c+u_0)/2,\quad
 \delta=\min\{1,u_0-s\},\quad \tau=\delta/16,
\]
\[
 a_0=\tau^3,\qquad \eta=1-1/c>0,\qquad
 C_0=\frac{3e^{1/c}}{1-c/s}.
\]

Choose an integer r>=2 such that

\[
 \delta r^3\ge2,\qquad
 r^\eta\ge\frac{8C_0}{a_0\gamma}. \tag{1}
\]

Such an integer exists and can be fixed before n is given. Put

\[
 \mu=r^3,\qquad n_0=\lceil4r/\gamma\rceil,\qquad
 B_\gamma=\left\lceil\frac{2\mu}{1-\theta}\right\rceil. \tag{2}
\]

Let F be any field, let n>=n_0, let x_1,...,x_n be distinct elements of F,
and let y_1,...,y_n lie in F. Let k,A be integers satisfying

\[
 1\le k\le(1-\gamma)n,\qquad k+\lceil\gamma n\rceil\le A\le n.
\]

Set K=ceil((1-theta)A). Hasse derivatives are specified by
\(P(X+T)=\sum_j P^{[j]}(X)T^j\). The letter mu denotes interpolation
multiplicity, not interleaving width.

## Conclusion

There is a nonzero polynomial Q in F[X,Y_0,...,Y_r] such that

\[
 \deg_Y^{\rm tot}Q\le B_\gamma,\qquad
 \deg_{(1,K-1,\ldots,K-1)}Q<\mu A\le\mu n. \tag{3}
\]

In particular deg_X Q<mu n. Every P in F[X] of degree less than K,
and therefore every such P of degree less than k, with at least A
agreements P(x_i)=y_i satisfies the polynomial identity

\[
 Q(X,P,P^{[1]},\ldots,P^{[r]})=0. \tag{4}
\]

The same Q works for all candidates for this received word. There is no
characteristic restriction on this interpolation statement. The parameters
r,mu,B_gamma are independent of n,k,A,F and the received word.

This proves the scalar fixed-slack input needed here. Its construction is
the mechanism of [TR26-169, Proposition 3.7 (Fixed-shape sparse interpolant),
printed pp. 14–15](https://eccc.weizmann.ac.il/report/2026/169/download#page=14),
with the interface and padding discussed in [Corollary 3.9
(Specialization-compatible interpolation) and Lemma 4.1 (Uniform fixed-slack
parameters), printed pp. 16–17](https://eccc.weizmann.ac.il/report/2026/169/download#page=16).
The September 5, 2026 version was read September 25.
The proof below supplies its own constants and all required estimates;
the optimized order bound and the rest of that preprint are not inputs.
No novelty is claimed for hidden-derivative interpolation.

## Proof

**Padding and degree bounds.** Since A is an integer and 0<theta<1,
K<=A. Also

\[
 K-k\ge A-\theta A-k\ge\gamma n-\theta n=\gamma n/2>0.
\]

Using n>=4r/gamma and r>=2 gives

\[
 K-1\ge(1-\theta)A-1\ge\gamma n/2-1
       \ge\gamma n/4\ge r,
\]

so 2<=K and r<K. The strict ceiling inequality K-1<(1-theta)A gives
u:=A/(K-1)>u_0. Moreover (1-theta)A>=2, hence
K-1>=(1-theta)A/2 and

\[
 B:=\lceil\mu A/(K-1)\rceil\le B_\gamma. \tag{5}
\]

**A monomial space with many coefficients.** For v=(v_2,...,v_r) in
the nonnegative integer lattice, put

\[
 |v|=\sum_{j=2}^r v_j,\qquad
 \omega(v)=\sum_{j=2}^r(j-1)v_j,\qquad
 W=\left\lfloor\frac{cr\mu}{\log(er)}\right\rfloor,
\]
\[
 \mathcal T=\{v:\omega(v)\le W,\ |v|\le\lceil s\mu\rceil\}.
\]

Let V_Q be the F-span of all distinct monomials
X^a Y_0^b Y_1^h product_(j=2)^r Y_j^(v_j) satisfying

\[
 v\in\mathcal T,\quad 0\le h\le\mu,\quad
 b+h+|v|\le B,\quad
 a+(K-1)(b+h+|v|)<\mu A. \tag{6}
\]

Its elements satisfy (3). For each v in T, choose independently integers
0<=b,h<=floor(tau mu). Since |v|<=s mu+1 and delta mu>=2,

\[
 u\mu-|v|-b-h\ge\delta\mu-1-2\tau\mu\ge4\tau\mu.
\]

All integers 0<=a<4 tau(K-1)mu then satisfy (6); its strict weighted
inequality also implies the total-degree condition in (6). Each b or h
interval contains at least tau mu integers, and the a interval contains
at least 4 tau(K-1)mu integers. Distinct exponent tuples are linearly
independent over every field. In particular,

\[
 \dim_F V_Q\ge a_0|\mathcal T|(K-1)\mu^3. \tag{7}
\]

**Counting the derivative-tail enlargement.** Write
Lambda(z)=#{v>=0:omega(v)<=z}, and put J=r(r-1)/2. The real simplex
S_z={t>=0:sum_(j=1)^(r-1)j t_j<=z} has volume
z^(r-1)/((r-1)!)^2, by diagonal scaling of the ordinary simplex.
Unit cubes based at the counted lattice points are contained in S_(z+J).
Consequently

\[
 \Lambda(z)\le\frac{(z+J)^{r-1}}{((r-1)!)^2}. \tag{8}
\]

For a uniform point in S_W, diagonal scaling and symmetry of the simplex
give expected coordinate sum
W(1+1/2+...+1/(r-1))/r<=W log(er)/r<=c mu.
Markov's inequality shows that the region with coordinate sum at most
s mu has at least (1-c/s) of the volume. Taking coordinatewise floors
places that region in unit cubes based at T. Thus

\[
 |\mathcal T|\ge(1-c/s)\frac{W^{r-1}}{((r-1)!)^2}.
\]

This use of real volume estimates an integer monomial count; it makes no
assumption on the coefficient field. With ell=log(er), W>0. In fact

\[
 c\bigl(\mu-(r-1)J\bigr)\ge\ell
 \quad(r\ge2),
\]

because mu-(r-1)J>=r^3/2 and ell<=r. Hence
W>=cr mu/ell-1>=c(r-1)(mu+J)/ell. Applying log(1+t)<=t to the
quotient of (8), with z=W+mu, and the preceding lower bound gives

\[
 \frac{\Lambda(W+\mu)}{|\mathcal T|}
 \le\frac{1}{1-c/s}
       \left(1+\frac{\mu+J}{W}\right)^{r-1}
 \le\frac{e^{1/c}}{1-c/s}\,r^{1/c}. \tag{9}
\]

**Local conditions and their rank.** Fix a received pair (alpha,y).
Make the substitution

\[
 X=\alpha+T,\qquad
 Y_0=y+\sum_{j=1}^r(-1)^{j+1}T^jY_j+TE.
\]

Require every coefficient of T^i E^b product Y_j^(e_j) with
i+rb<mu to vanish. These are homogeneous linear conditions on V_Q;
let Phi_(alpha,y) be the map recording those coefficients.

To bound its rank, first substitute X=alpha+T, Y_0=y+TU and reduce
modulo T^mu. The image is contained in the space V with monomial basis

\[
 T^\rho U^aY_1^b\prod_{j=2}^rY_j^{v_j},\quad
 0\le\rho<\mu,\quad 0\le a\le\rho,\quad0\le b\le\mu,
 \quad\omega(v)\le W+\rho. \tag{10}
\]

Indeed, a power U^a from Y_0=y+TU contributes at least T^a, while
the original tail weight is at most W. Rewrite

\[
 E=U-\sum_{j=1}^r(-1)^{j+1}T^{j-1}Y_j,
\]

and let Gamma on V record the coefficients of weight i+rb<mu after
this rewrite. Then Phi factors through Gamma.

For each rho let h_rho=ceil((mu-rho)/r). If rho>=h_rho, consider
the following vectors, expanded in U and reduced modulo T^mu:

\[
 T^\rho E^{h_\rho}U^aY_1^b\prod_{j=2}^rY_j^{v_j},\quad
 0\le a\le\rho-h_\rho,\quad0\le b\le\mu-h_\rho,
 \quad\omega(v)\le W+\rho. \tag{11}
\]

Otherwise take no vectors at rho. Every surviving term in (11) lies
in V: choosing a Y_j with j>=2 from E increases both its T exponent
and tail weight by j-1, while its U exponent is at most rho and its
Y_1 exponent at most mu. On rewriting in E again, (11) is divisible
by T^rho E^(h_rho); since rho+r h_rho>=mu it is in ker Gamma.

At its lowest T exponent rho the vector has coefficient
(U-Y_1)^(h_rho) times a distinct monomial in U,Y_1,...,Y_r.
Multiplication by this nonzero polynomial is injective over every field.
For different rho, taking the least T exponent in a relation proves
independence of all the vectors together. This remains true when
binomial coefficients in E^(h_rho) vanish in small characteristic.

At each rho the dimension of (10) is
(rho+1)(mu+1)Lambda(W+rho). Subtracting the independent kernel vectors
therefore shows

\[
 \operatorname{rank}\Phi_{\alpha,y}
 \le\sum_{\rho=0}^{\mu-1} b_\rho\Lambda(W+\rho),
\]
\[
 b_\rho=(\rho+1)(\mu+1)
   -\max\{0,(\rho-h_\rho+1)(\mu-h_\rho+1)\}
 \le h_\rho(\rho+\mu+2).
\]

For rho<h_rho the last inequality follows from rho+1<=h_rho;
otherwise expand the product. Since mu=r^3 is divisible by r,

\[
 \sum_{\rho=0}^{\mu-1}h_\rho
 =r\sum_{j=1}^{r^2}j
 =\frac{r^5+r^3}{2}\le\frac{\mu^2}{r}.
\]

Also rho+mu+2<=3mu. Monotonicity of Lambda and (9) now give

\[
 \operatorname{rank}\Phi_{\alpha,y}
 \le\frac{3\mu^3}{r}\Lambda(W+\mu)
 \le C_0|\mathcal T|\mu^3 r^{-\eta}. \tag{12}
\]

**A common nonzero kernel.** Stack these maps for all n received pairs.
Its rank is at most the sum of their ranks, regardless of overlap among
constraints. By (1), (7), (12), and K-1>=gamma n/4,

\[
 \operatorname{rank}(\Phi_{x_1,y_1},\ldots,\Phi_{x_n,y_n})
 \le\frac{a_0\gamma n}{8}|\mathcal T|\mu^3
 \le\frac12 a_0(K-1)|\mathcal T|\mu^3
 <\dim V_Q.
\]

Rank–nullity over F supplies a nonzero Q satisfying all local conditions.
No root enumeration or field-size-dependent bound was used.

**Agreement forces multiplicity.** The Hasse identity
\(P(\alpha)=\sum_{j\ge0}(-T)^j P^{[j]}(\alpha+T)\) holds over every field by
substituting -T into the defining Taylor identity. If P(alpha)=y, it
implies that

\[
 E_P(T)=\frac{P(\alpha+T)-y-
             \sum_{j=1}^r(-1)^{j+1}T^jP^{[j]}(\alpha+T)}{T}
\]

is a polynomial divisible by T^r. Substitute \(Y_j=P^{[j]}(\alpha+T)\)
and E=E_P(T) in the local expansion of Q. The imposed equations
eliminate all terms with i+rb<mu; every remaining term is divisible
by T^mu. Thus each agreement gives a root of multiplicity at least mu
of G(X)=Q(X,P,...,P^[r]).

For deg P<K, (3) gives deg G<mu A unless G=0. Distinct agreement
points give pairwise coprime factors (X-x_i)^mu. If there are at least
A such points their product, of degree at least mu A, divides G.
The degree inequality forces G=0, proving (4).

**Boundary checks.** At r=2, mu=8, rho=4, the kernel vector T^4E^2
has weight rho+r h_rho=8 exactly and is not recorded. In characteristic
two, E=U-Y_1+TY_2 gives T^4E^2=T^4(U-Y_1)^2+T^6Y_2^2; the nonzero
lowest coefficient still proves independence. The ceiling choices retain
K-1<(1-theta)A even when (1-theta)A is an integer. All degree bounds
in the multiplicity comparison are strict. No restriction p>r, p>mu,
or p>B_gamma was introduced. This proves interpolation only; a
small-characteristic solution-cover theorem does not follow.

## Mathlib

Full statement (1)–(4): **not checked** in Mathlib. Supporting Hasse
identities, rank–nullity, multiplicity divisibility, simplex volume, and
Markov's inequality: **not checked** in this step. The named TR26-169
results above are mathematical sources matching the qualitative
interpolation conclusion, not Mathlib matches or certifications of the
whole preprint. The explicit proof does not rely on a library lookup.
