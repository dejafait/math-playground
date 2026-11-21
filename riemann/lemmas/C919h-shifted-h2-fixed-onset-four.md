# Corollary 919h: shifted actual-zero H2 from onset four

## Hypotheses

Use the actual Xi of L018, opposite-class representatives alpha_j
with full multiplicities as in L024, beta_j=alpha_j^(-2), and the
absolutely convergent real power sums S_m of L025. For an integer
r>=4 set

    H_(2,r)=(S_(2r+i+j+2))_(0<=i,j<=2),
    D=diag(1,200,40000), b=4/2601.

Import David J. Platt, *Isolating some non-trivial zeros of zeta*,
Mathematics of Computation 86(307) (2017), 2449-2467,
DOI10.1090/mcom/3198, Theorem5.1, accepted manuscript printed p8
(PDF p9), with Sections4.1-4.2/5, pp6-8:
https://research-information.bris.ac.uk/ws/portalfiles/portal/78836669/platt_zeta_submitted.pdf.
The theorem certifies critical-line location and simplicity of every
nontrivial zero with |Im rho|<=3.0610046*10^10. Only its complete
critical-line location through height100 is used. This is an imported
published computational theorem; its computation is not replayed here.

Use the audited C919e closed-box real Gram bound and C919f at time0,
with L058's F(0,z)=Xi(z). Retain C919f's explicit correct CPython
integer/Fraction and reviewed Decimal/libmpdec arithmetic contracts,
including its correctly rounded HALF_EVEN exp contract. Correct
CPython integer/Fraction arithmetic is also assumed for the new exact
certificate below. Use L467's complete multiplicity-counted closed
unit-shell bound, under its stated Bellotti-Wong source import.
No RH, exact first-three zero census, exterior reality, global
simplicity or positive-time product theorem is assumed.

## Conclusion

For every integer r>=4, H_(2,r) is real symmetric positive definite.
More quantitatively, with k=r-4,

    lambda_min(D H_(2,r) D) >= b^(2k) (h4-t4)>0,
    h4=b^8/700000000
      =256/5727708301326206498092619377734375,
    t4=18*(1+1/2500+1/6250000)
           *(100^(-19)+100^(-18)/18)
      =368897559/312500000000000000000000000000000000000000000.

In L030's algebraic convention, Q(X^r p)>0 for every nonzero real
polynomial p of degree at most2 and every integer r>=4. This is a
qualified fixed-degree, shifted result at time0, accepted by the
separate step2202 critical audit under the stated contracts. It is a reproduction/specialization of known
head-dominance methods, not a general new theorem beyond the checked
sources or a candidate solution of RH. Shift removal, arbitrary
degree and all-degree mixed positivity remain unresolved. C919g's
separate qualified unshifted H2 result is overlap context, not an input.

## Proof

### Complete real head and selected margin

In L018's coordinate a zeta zero sigma+i gamma corresponds to
alpha=gamma+i(1/2-sigma), preserving its multiplicity. If gamma=0,
the imported symmetric Platt theorem places sigma=1/2, giving
alpha=0, which L024 excludes. Thus there is no exceptional purely
imaginary opposite class. Select the unique representative with
Re(alpha)>0 from every opposite pair, repeating it by multiplicity.
This selects precisely one occurrence per positive-ordinate zeta
zero, including distinct zeros with a shared ordinate. In particular
both members of a nonreal conjugate Xi pair with positive real part
are retained. No conjugate partner is identified with its opposite.

Let the finite head contain every occurrence with 0<gamma<=100,
including a possible endpoint occurrence. It is finite by entire
nonzero Xi and the bounded zeta strip in L018 (also by L467's finite
shell bounds). Platt's theorem applies at these heights and makes
every alpha in this head positive real. Consequently every head
beta is positive real. Its simplicity conclusion is unnecessary:
the argument would retain all orders if any were present.

C919f at lambda=0 and L058 supply at least one real Xi zero in each
of (14,29/2), (41/2,43/2), (49/2,51/2). Select one occurrence in
each open box. They are distinct opposite classes and belong to
the head; no assertion that they are exactly the first three is made.
For real x in these boxes put

    w(x)=(x^(-2),200*x^(-4),40000*x^(-6))^T.

C919e, on its entire closed box, gives

    sum_(j=1)^3 w(x_j)w(x_j)^T >= (1/700000000) I.

Here and below real matrix inequalities mean inequalities of
quadratic forms on every real vector. This imports the audited margin
rather than rederiving its Vandermonde inverse or constants. Each
x_j<=51/2, hence beta_j=x_j^(-2)>=b>0. The contribution of these
three occurrences to D H_(2,r) D is exactly

    sum_(j=1)^3 beta_j^(2r) w(x_j)w(x_j)^T
      >= b^(2r)/700000000 I.                         (1)

Indeed beta_j^(2r)>=b^(2r), and each w w^T is real positive
semidefinite. Every unselected head occurrence contributes another
beta^(2r) w w^T with beta>0, so retaining the entire head preserves
(1). This pays the inserted shift weights explicitly; the old
unshifted margin is not used unchanged.

For precision on the matrix facts, import Boyd and Vandenberghe,
*Convex Optimization* (2004), corrected seventh printing (2009),
A.1.1 pp633-634, A.1.5 p636, A.5.2 pp646-647, A.5.4 pp648-649,
Section2.2.5 pp34-35:
https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf.
Only finite real Gram/matrix order, Euclidean norm and congruence
facts are used. Their source coverage and C919e's Gautschi1975
inverse specialization were assessed in step2198/2199; they are not
new source audits here. The displayed quadratic-form inequalities
also specify exactly how these facts are applied.

### Complete complex exterior

For a remaining representative write alpha=gamma+i eta with gamma>100.
No reality or critical-line location is assumed here. Set

    w(alpha)=(alpha^(-2),200*alpha^(-4),40000*alpha^(-6))^T.

L025/L030 give the absolutely convergent algebraic identity

    D H_(2,r) D = sum_j beta_j^(2r) w(alpha_j) w(alpha_j)^T. (2)

The transpose in (2) is ordinary, not conjugate transpose. For any
real coefficient vector c, complex Cauchy-Schwarz gives

    |beta^(2r) (c^T w(alpha))^2|
      <= ||c||_2^2 |alpha|^(-4r-4)
            *(1+40000 |alpha|^(-4)+1600000000 |alpha|^(-8))
      <= ||c||_2^2 gamma^(-4r-4) C,
    C=1+40000/100^4+1600000000/100^8
      =1+1/2500+1/6250000=6252501/6250000.             (3)

The last inequality uses |alpha|>=gamma>100 and positive exponents.
The modulus is used solely to bound the error; it does not replace
the algebraic square in (2) by a modulus-square moment matrix.

Partition positive ordinates above100 by unit shells contained in
the closed shells [n,n+1], integer n>=100. L467 bounds the number
of occurrences in each such closed shell by18 log(n+2), counting
multiplicity and both conjugate partners. Using all the closed
shells can count an integer endpoint twice, and can include a
height100 head occurrence. Both are harmless overcounts only in
this absolute upper bound. Nothing is subtracted from a signed sum.
At r=4, (3) yields the complete scalar budget

    ||c||_2^(-2) sum_exterior |beta^8 (c^T w(alpha))^2|
       <=18 C sum_(n>=100) log(n+2) n^(-20)
       <=18 C sum_(n>=100) n^(-19)
       <=18 C (100^(-19)+100^(-18)/18)=t4,            (4)

with the zero vector treated directly. To justify the second step,
for n>=2 one has n+2<=2n, log2<1 and log n<=n-1, so
log(n+2)<=n. The last step follows because x^(-19) decreases:
for n>=101, n^(-19)<=integral_(n-1)^n x^(-19) dx.
The integral from100 to infinity is100^(-18)/18. Thus (4)
is a summable majorant for the complete exterior, with no truncated
zero table, uncharged remainder, real-tail substitution or limiting
cancellation. L467 imports Bellotti-Wong, arXiv:2412.15470v2
(7July2025), Theorem1.1 p1 and Section5 pp23-24:
https://arxiv.org/pdf/2412.15470v2.
Its audited conversion to closed shells is reused without reproof.

By L025 the matrix in (2) is real symmetric. Its finite head is real,
so the complete exterior matrix E_r is real symmetric as well,
even though individual exterior terms need not be real. Absolute
convergence justifies this subtraction and the error sum in (4).
It follows that c^T E_4 c>=-t4 ||c||_2^2 for every real c.
This is an estimate of the actual algebraic exterior, not an assertion
that its terms are Gram-positive.

### Exact onset comparison and every larger integer

One frozen rational certificate evaluates (1) and (4), with no
parameter sweep or new zero computation:

    python3 scripts/h2-head/shifted_h2_2200.py

Its full exact evidence is `scripts/h2-head/shifted_h2_2200.json`.
Using the reduced h4 and t4 fractions in the conclusion, the exact
integer numerator of the cross-multiplied strict comparison is

    numerator(h4)*denominator(t4)
       -numerator(t4)*denominator(h4)
      =79997887062388976725960123694555637690112109375 >0. (5)

Both denominators are positive. Thus h4>t4>0. For orientation only,
h4 is approximately4.46950135258678e-32, t4 is the exact finite
decimal1.1804721888e-36, and h4/t4 is approximately37861.9793.
No rounded number proves (5).

Let k=r-4 be any nonnegative integer. Each term of the complete
exterior estimate at r gains |alpha|^(-4k)<=100^(-4k), while the
head bound (1) becomes h4 b^(2k). Therefore

    |c^T E_r c| <=t4*100^(-4k) ||c||_2^2,
    c^T D H_(2,r) D c
      >=[h4 b^(2k)-t4*100^(-4k)] ||c||_2^2
      =b^(2k)[h4-t4*(51/200)^(4k)] ||c||_2^2
      >=b^(2k)(h4-t4)||c||_2^2>0                    (6)

for c!=0. The identity uses b=(51/2)^(-2); the one-step tail/head
ratio is exactly6765201/1600000000=(51/200)^4<1. It holds for
every k>=0, not a finite list of sampled shifts. Equation(6) gives
the quantitative conclusion. D is real invertible, so congruence
implies positive definiteness of H_(2,r). For a nonzero p of degree
at most2, L030 identifies Q(X^r p) with its nonzero coefficient
vector's quadratic form in H_(2,r), proving the final sign claim.

The complete load-bearing rational head/tail values, comparison
cross product, component bounds, summable shell bound and all-r
factors were inspected from the saved certificate, together with
all eight checks and the empty failure list. The script uses exact
integer/Fraction arithmetic for proof values; Decimal is display
only. The analytic justification above is necessary: a PASS flag or
finite certificate alone cannot prove (2)-(4) or the uniform-in-r
argument. This paragraph records the original step2200 verification;
the separate step2202 critical audit is below. C919f's inherited
backend trust remains.

The continuing main gap is positivity on all real polynomials for
the actual Xi nodes. This argument controls only X^r p with fixed
degree at most2 and integer r>=4. There is no mechanism here to
remove X^r, make the degree arbitrary, or infer RH from this family.
The historical finite-to-all-degree and algebraic/modulus-square
stops remain unchanged. Positive-time signs are outside this proof.

### Independent conceptual audit, 21 November 2026 (step2202)

The approved audit scope2200/2201 is reused unchanged. The complete
proof and generator were inspected, with the accepted hypotheses and
conclusions of C919e/f and the complete local conventions of L018,
L024/L025/L030, L058 and L467. No new source theorem, component
computation, cutoff, onset or degree is substituted. The audit accepts
the stated conclusion under precisely its retained source imports
and arithmetic contracts; this is local verification of a known-method
specialization, not a new general result or an RH candidate.

**Occurrences and the real head.** The coordinate map in L018 is
injective and preserves orders. An opposite Xi pair corresponds to
opposite zeta ordinates. The only obstruction to choosing a unique
positive-real-part representative would have ordinate zero; the
symmetric Platt import and Xi(0)!=0 exclude it. For a positive
ordinate gamma, the reflected zeta zeros sigma+i gamma and
(1-sigma)+i gamma, if distinct, give the two distinct Xi nodes
gamma+i eta and gamma-i eta. They are both counted, not merged.
Thus L467's positive-ordinate multiset is exactly the one needed here.
The full head includes gamma=100 and every order. Its reality is
provided by the finite-height source, not inferred from the three
brackets. C919f supplies distinct selected occurrences at time0;
L058 supplies the Xi normalization and continuity used there. C919e's
closed-box bound applies to their open boxes. Additional head zeros
can be kept because their individual contributions are real positive
semidefinite. No claim of exactly three low zeros is necessary.

**Algebraic sum and complete error.** The (i,j) summand in (2) is
200^(i+j) beta^(2r+i+j+2), which agrees with the scaled Hankel
entry, including its index shift two. For real c, the modulus of the
algebraic square (c^T w)^2 is |c^T w|^2. Cauchy-Schwarz bounds this
by ||c||^2 sum_i |w_i|^2; it does not change the original summand
into a Hermitian Gram contribution. The three squared component
weights are 1,40000,1600000000 and the leading exponent is4r+4.
Every remaining representative has |alpha|>=gamma>100. Assigning
each to a closed unit shell and retaining possible endpoint overcounts
therefore gives an upper bound for the sum of absolute values, with
the factor18 and both nonreal conjugate occurrences already included.
There is no factor-of-two loss or omitted signed middle interval.

At r=4, log(n+2)<=n for every integer n>=100 follows from the
inequalities displayed in the proof; the exponent changes from20
to19. The integral comparison accounts for every n>=101 and adds
the n=100 term separately. Its integral is exactly100^(-18)/18.
This finite bound proves summability of the entire error. L025/L030
independently justify the algebraic power sums and finite polynomial
expansion. Subtracting the finite real head from the real symmetric
full matrix gives a real symmetric error, so its absolute quadratic
bound legitimately supplies a lower bound. No limit in r or sign
assumption on individual exterior terms is used.

**Independent exact reconstruction.** Run

    python3 scripts/h2-head/shifted_h2_audit_2202.py

The saved report is `scripts/h2-head/shifted_h2_audit_2202.json`.
The new script does not import or execute the original generator and
does not overwrite its evidence. It reconstructs h4 from(2/51)^16,
the three component tail budgets separately, and the shift factors
from fourth powers. All18 saved arithmetic fields/subfields checked
agree exactly; all27 audit checks pass, with an empty failure list.
The original generator and certificate hashes are retained in the
report. The complete selected load-bearing values, checks and failure
lists of both certificates were inspected, not just previews.

In particular the fractions for h4,t4 in the conclusion and the
positive integer in (5) are reproduced exactly. The required
comparison is h4-t4>0, not merely h4>0. Their exact difference is

    204794590879715780418457916658062432486687 /
    4582166641060965198474095502187500000000000000000000000000000000000000000.

Only CPython integer/Fraction arithmetic is used in this reconstruction;
the original Decimal values are explanatory and not compared as proof.
This does not remove C919f's distinct Decimal/libmpdec trust assumption.

**Every integer shift and congruence.** For arbitrary k>=0, each
exterior absolute value gains at most100^(-4k); the selected real
head gains at least b^(2k). Their ratio is exactly
(100^(-4)/b^2)^k=(51/200)^(4k), with base
6765201/1600000000 strictly between0 and1. Thus (6) holds for each
nonnegative integer k, not just checked samples. The positive margin
varies with k and may tend to zero; no uniform positive lower bound
in r is claimed. If a is the coefficient vector of p, put c=D^(-1)a.
Then a^T H_(2,r) a=c^T D H_(2,r) D c=Q(X^r p), and c is nonzero
exactly when a is. This checks the direction of the final congruence.

There is no in-scope defect to repair and no changed dependency.
Acceptance covers only time0, degree at most2 after factoring X^r,
and integer r>=4. The inability to remove the shift or control
arbitrary degree remains. Repeating this audit or enlarging its
parameter sweep supplies no such bridge. Source computations and
arithmetic backends are still imported, not formally verified here.

## Mathlib

Full matching coverage of this qualified shifted actual-Xi result
has not been checked. Supporting finite real matrix facts are cited
above, and C919e/f and L467 retain their own coverage qualifications.
No formal Lean verification of the source computations, backend or
new rational certificate is claimed. Unknown availability is not
evidence of absence.
