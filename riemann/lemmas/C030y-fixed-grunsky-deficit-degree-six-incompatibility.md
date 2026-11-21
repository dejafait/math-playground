# Corollary C030y: fixed inverse-Grunsky deficit fails by mixed degree five

## Hypotheses

Let S_k be the actual reciprocal-Xi-zero sums of L025. Let tau>0 be
real, and let

    f(z)=z+a_2*z^2+...+a_7*z^7+O(z^8)

be a real normalized formal Taylor jet, without an oddness assumption.
Define the symmetric coefficients c_mn by the normalized formal logarithm

    log((f(z)-f(w))/(z-w))=-sum_(m,n>=0) c_mn*z^m*w^n.

The zero-index coefficients are those determined by f, not additional
free data. Only coefficients with m,n>=1 and m+n<=6 are prescribed.

## Conclusion

There is no such jet satisfying

    c_mn=delta_mn/m-tau*S_(m+n),  m,n>=1, m+n<=6.

In fact the requirements with m+n<=5 already contradict the
unconditional L027 signs S_2,S_3>0. This stops only the fixed linear
diagonal-deficit representation. It says nothing against RH or the
positivity of the actual L030 forms, and does not exclude a different
Grunsky representation.

For completeness, if S_2,...,S_6 are arbitrary real parameters instead
of the actual Xi sums, compatibility through mixed degree six for any
fixed tau>0 holds if and only if S_2=S_3=S_4=0. There is no restriction
on S_5,S_6 at this degree. This finite formal assertion supplies no
unit-disk univalence, convergence of a prescribed infinite jet, or
Grunsky contraction.

## Proof

**Known formal input and normalization.** Import the symmetric
Grunsky/Faber coefficient identities from L.-P. Teo, *Analytic functions
and integrable hierarchies—characterization of tau functions*,
Lett. Math. Phys. 64 (2003), 75–92,
[arXiv:hep-th/0305005v2](https://arxiv.org/html/hep-th/0305005v2),
Section 2.1 and Section 2.2, equations (2.3)–(2.4), (2.8)–(2.12),
preprint pp. 2–6, in particular the displayed low-coefficient formulas
on p. 5. The end of Section 2.2 states their formal-series validity.
Here the leading coefficient is 1, so Teo's b is 1. The symmetric
interior b_(-m,-n) are our c_mn; these are not the nonsymmetric Faber
coefficients m*c_mn. No analytic univalence theorem is being invoked
or reproved.

Put

    g(Z)=1/f(1/Z)=Z+b_0+b_1/Z+...+b_5/Z^5+O(Z^(-6)).

The mixed exterior coefficients of g equal those of f, as in Teo's
(2.12). In this specialization the identity is also visible directly:
at Z=1/z,W=1/w the exterior divided difference equals

    (z/f(z))*(w/f(w))*(f(z)-f(w))/(z-w).

The first two factors add only single-variable terms to the normalized
formal logarithm. Thus they change no coefficient with m,n>=1.
The coefficient b_0 cancels from the exterior divided difference and
is unrestricted. Each b_j through b_5 depends only on a_2,...,a_7.
Conversely, these six real b_j determine a unique real normalized
Taylor jet through a_7 by taking the formal reciprocal again.

**All mixed coefficients through degree six.** The first-row and
c_22,c_23,c_33 formulas are precisely the cited known identities. The
one further entry c_24 follows by the permitted finite extraction below:

    c_1n=b_n, 1<=n<=5,
    c_22=b_3+b_1^2/2,
    c_23=b_4+b_1*b_2,
    c_24=b_5+b_1*b_3+b_2^2/2,
    c_33=b_5+b_1*b_3+b_2^2+b_1^3/3.

These nine entries and symmetry exhaust m,n>=1,m+n<=6. To check c_24
and truncation, in variables x=1/Z,y=1/W write the exterior divided
difference as 1-D, where

    D=sum_(k=1)^5 b_k*sum_(i=1)^k x^i*y^(k+1-i)
      + terms of total degree at least 7.

Then -log(1-D)=D+D^2/2+D^3/3+... . The coefficient of x^2*y^4 is
b_5 from D, b_1*b_3+b_2^2/2 from D^2/2, and zero from every higher
power, since every monomial of D has both exponents at least 1.
No term omitted at total degree at least 7 can affect any displayed
coefficient. For the interior divided difference, a_k first appears at
total degree k-1; hence a_7 suffices and O(z^8) is harmless. This is
finite coefficient specialization, not a reproof of a general theorem.

**Prescribed-deficit equations and the actual contradiction.** The
first row forces

    b_1=1-tau*S_2, b_2=-tau*S_3, b_3=-tau*S_4,
    b_4=-tau*S_5, b_5=-tau*S_6.

Set X=b_1,Y=b_2,Z=b_3. Subtracting the prescribed values from the
four remaining displayed entries yields exactly

    (X^2-1)/2=0,
    X*Y=0,
    X*Z+Y^2/2=0,
    X*Z+Y^2+(X^3-1)/3=0.                         (1)

The first equation uses mixed degree four; the second uses degree
five. For actual Xi, L027 gives S_2>0 and S_3>0 without RH. The two
branches of the first equation are X=1 and X=-1. The first branch
would require tau*S_2=0, impossible. The second requires
tau*S_2=2, but the second equation of (1) would then force Y=0,
whereas Y=-tau*S_3<0. Both branches are excluded. Alternatively,
Y<0 makes X*Y=0 force X=0, directly contradicting X^2=1. There is
no division by S_2, S_3 or a possibly zero jet parameter.

The only input about actual Xi beyond the definition and reality of
the sums in L025 is L027's strict positivity. Its proof uses the
unconditional localization Re(alpha)>4 and |Im(alpha)|<1/2 for the
positive-real representatives, so |arg(alpha)|<1/8 and the real parts
of alpha^(-2k) are positive for 1<=k<=6. Absolute convergence and
reality give the signs; neither an RH premise nor a new numerical
enclosure is needed here. We import that existing result rather than
reprove an actual-Xi estimate.

**Degree-six elimination and exceptional cases.** For arbitrary real
S_k, (1) implies X^2=1 and X*Y=0, hence Y=0. The third equation
then gives X*Z=0, hence Z=0. The fourth gives X^3=1; together with
X^2=1 this forces X=1. Since tau>0, the first-row equations now give
S_2=S_3=S_4=0. These implications retain both original X branches;
the negative branch is eliminated only by the last equation. They
are also valid polynomial consequences: Y=X*(X*Y)-Y*(X^2-1),
Z=X*(X*Z)-Z*(X^2-1), and
X-1=(X^3-1)-X*(X^2-1).

Conversely, when S_2=S_3=S_4=0 choose any real b_0 and set
b_1=1,b_2=b_3=0,b_4=-tau*S_5,b_5=-tau*S_6. Substitution verifies
all nine entries. The real formal jet can be obtained, for example,
by expanding

    f(z)=z/(1+b_0*z+z^2-tau*S_5*z^5-tau*S_6*z^6)

through z^7. The denominator has constant term 1, which justifies
the formal reciprocal. This proves sufficiency at the stated finite
degree and no analytic assertion on the unit disk. The excluded case
tau=0 is formally compatible (take f=z/(1+b_0*z+z^2)); the argument
does not discard it through an unjustified division.

**Exact verification.** Reproduction command, from this notebook:

    python3 scripts/grunsky/degree-six-deficit-1253.py

The self-contained rational-polynomial calculation extracts all nine
interior/exterior entries, checks the reciprocal transformation and
symmetry, compares the cited identities, substitutes the fixed deficit,
and checks the elimination identities and degenerate sufficiency.
Its complete output is
[certificate1253](../scripts/grunsky/degree-six-deficit-certificate-1253.json).
The full exterior coefficients, substituted residuals and every
verification residual were inspected. All verification residuals are
exactly zero. The actual required condition S_3=0 contradicts L027's
S_3>0, rather than a floating approximation. The displayed proof gives
the mathematical justification independently of the program.

The result is a decided specialization absent from the inspected
source comparisons, not a claim of certified originality. L030's
index shift explains the motivation for prescribing S_(m+n), but no
positivity, contraction or RH-equivalent input is used in this proof.

**Independent proof audit1255, 17 November 2026.** Retain the stated
fixed-ansatz stop. This audit confirms an existing finite specialization;
it establishes no additional actual-Xi sign or new obstruction. The
normalization identity above has positive sign on both divided
differences. Its two extra logarithms contain only pure powers, and
the leading coefficients are both one. Thus neither a sign change,
a Faber factor m, nor a free zero-index coefficient enters (1).
There are exactly nine unordered mixed entries: (1,1) through (1,5),
(2,2),(2,3),(2,4),(3,3). In -log(1-D), the minimum exterior degree
is two. The degree-six contributions therefore come only from
D,D^2/2,D^3/3; for (2,4) the last is zero because its first exponent
would be at least three. The interior logarithm has minimum degree
one, so its powers through six suffice. Higher unspecified jet
coefficients cannot enter these entries. The formal reciprocal is
invertible because its denominator has constant term one; b_0 is
free rather than an additional compatibility equation.

The complete first row cancels the linear b_3,b_4,b_5 terms from the
four remaining prescribed entries exactly as in (1). The two
degree-four branches, their degree-five exclusion for actual Xi,
and the degree-six elimination were checked without dividing by X,
Y, Z or any S_k. In the arbitrary-parameter case, using X^2=1 first
justifies Y=0; the third residual then gives XZ=0 and hence Z=0;
only then does the last residual reduce to (X^3-1)/3. Thus the
displayed polynomial identities are used in their stated order,
not as unconditional identities for the unreduced third/fourth
residuals. Substituting the proposed sufficient reciprocal verifies
every entry, with S_5,S_6 unrestricted. The tau=0 solution is retained
as an excluded case, not silently contradicted.

The inherited sign proof was checked through the needed local
arguments. L018 maps the open zeta strip to |Im(alpha)|<1/2.
L026 uses |cos(zu)|<=exp(u/2) in that strip and obtains
|J(z)|<1/72. On |Re(z)|<=4 this gives
|Xi(z)-1/2|<11/24<1/2; hence every zero has |Re(alpha)|>4.
Choosing its positive-real representative gives |arg(alpha)|<1/8.
Consequently for 1<=k<=6 the angle of alpha^(-2k) has absolute
value <k/4<=3/2<pi/2, and its real part is strictly positive.
L025's absolute convergence and reality justify summing real parts.
The sum is not empty: L019/L020/L021 give strictly positive moments
of every order and hence a nonpolynomial Xi; L023's growth bound and
the named Hadamard theorem used in L024 would make a finite zero set
a finite polynomial product (evenness removes the linear exponential).
This is the nonempty-zero argument needed by L027, with no RH
assumption. The lower strict moment inequality in L027 is not used.
These checks retain the earlier named theta, completion and
Hadamard inputs; they are not a fresh audit of every earlier
foundational lemma. L019/L023 were read only to verify these inherited
premises. They add no direct mathematical premise beyond L025/L027.

The entire rational-polynomial program was inspected, including its
positive-degree truncation, reciprocal recurrence, deficit substitution
and exceptional-case elimination. Replay reproduced certificate1253
byte for byte. All nine interior/exterior entries, all six reciprocal
coefficients, all nine deficit residuals, all branches, and all 38
verification residuals were inspected in full. The residual groups
have sizes 9 reciprocal, 9 symmetry, 8 cited-source, 3 elimination
and 9 degenerate-sufficiency; every verification residual is exactly
zero. This is hand verification plus replay, not a second independent
software implementation or formal verification. The audit record is
[audit1255](../scripts/grunsky/degree-six-deficit-audit-1255.json);
the original certificate is preserved as
[before-audit1255](../scripts/grunsky/degree-six-deficit-certificate-before-audit-1255.json).
The unchanged certificate SHA256 is
`750d2c5313344d178c52901f1882a69f275afd18047492dbb5c006bb54f56c20`.

## Mathlib

Full matching coverage is not checked. No Mathlib verification or
absence claim is made. The proof uses cited formal identities and
finite rational polynomial algebra; the script is not a formal proof.
