# Corollary 919i: frozen five-node shifted-H2 obstruction

## Hypotheses

This is a finite model, not the actual Xi zero multiset. Take exactly
five opposite-class representatives, each with multiplicity one,

    alpha=(57/4,21,25,101+i/4,101-i/4), beta_j=alpha_j^(-2).
    S_m=sum_(j=1)^5 beta_j^m,
    Q(q)=sum_(j=1)^5 beta_j^2 q(beta_j)^2,
    H_(2,r)=(S_(2r+i+j+2))_(0<=i,j<=2),
    P(X)=product_(j=1)^3 (X-beta_j).

Coefficients of q are real and squares are algebraic. Import the
audited C919e real-box Gram inequality. Correct CPython integer and
fractions.Fraction arithmetic is assumed for the exact witness
certificate described below. No Decimal arithmetic, theta sign,
actual-zero census, Platt theorem, RH or Xi realization is assumed.

## Conclusion

For every integer r>=4, H_(2,r) is real symmetric positive definite.
Nevertheless the prescribed real polynomial q=X^158 P has degree161
and satisfies Q(q)<0. Both assertions hold for this single frozen model.

Thus positivity on every X^r p with deg p<=2 and r>=4 does not,
for a general such finite model, imply all-degree mixed positivity,
even for the same range of shifts. This is a local known-method
specialization classified REPRODUCTION under the step2203 assessment;
no originality or result beyond the sources checked is claimed.
It neither refutes RH nor disproves a possible actual-Xi-specific
completion of C919h. The independent step2206 audit accepts both
assertions under exactly the stated hypotheses and arithmetic assumption.

## Proof

### Finite normalization and imported matrix facts

The three real representatives lie in C919e's respective closed boxes:
14<=57/4<=29/2, 41/2<=21<=43/2, 49/2<=25<=51/2. They are distinct.
All five representatives have positive real part, so no two are
opposites. The last two are distinct conjugates and each must be
retained. The finite polynomial

    F(z)=product_(j=1)^5 (1-z^2/alpha_j^2)

is even, has real coefficients and constant term1. Its ten roots are
the five displayed representatives and their negatives, all simple.
This checks the opposite-class convention without applying any
actual-Xi theorem to F. All sums below are finite. Conjugation pairs
make S_m and Q(q) real. Direct finite expansion gives
c^T H_(2,r)c=Q(X^r p) for p(X)=sum_(i=0)^2 c_i X^i.
This uses the same index shift two as L030, but none of that lemma's
actual-Xi hypotheses is a premise here.

Import the finite real matrix norm/order/congruence facts from
Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*, Cambridge
University Press2004, corrected seventh printing2009, A.1.1 pp633-634,
A.1.5 p636, A.5.2 pp646-647, A.5.4 pp648-649 and Section2.2.5 pp34-35:
https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf . Only finite real
quadratic-form inequalities and invertible congruence are used. C919e
supplies its weighted Vandermonde specialization and audited constant;
its inverse calculation is not repeated. Its precise Gautschi source
is *Norm Estimates for Inverses of Vandermonde Matrices*, Numerische
Mathematik23 (1975), 337-347, Section3(3.1)-(3.4), p339:
https://www.cs.purdue.edu/homes/wxg/selected_works/section_01/051.pdf .
These methods cover the finite ingredients, not the two frozen signs.
Their coverage was read in the supplied step2203 assessment and reused.

### Uniform head/error inequality

Put D=diag(1,200,40000), b=4/2601, and

    w(alpha)=(beta,200 beta^2,40000 beta^3)^T.

The exact finite identity is

    D H_(2,r) D=sum_(j=1)^5 beta_j^(2r) w(alpha_j)w(alpha_j)^T. (1)

The transpose in (1) is ordinary. For the three real nodes beta_j>=b>0.
C919e applies by the checked boxes and gives

    sum_(j=1)^3 w(alpha_j)w(alpha_j)^T > I/700000000.

Since each real summand is positive semidefinite, their contribution
to (1) is at least b^(2r) I/700000000. For either complex occurrence
|alpha|^2=163217/16>101^2. For a real vector c, Cauchy-Schwarz gives

    |beta^(2r)(c^T w(alpha))^2|
      <= ||c||_2^2 |alpha|^(-4r-4)
          *(1+40000 |alpha|^(-4)+1600000000 |alpha|^(-8)).

Only the error is bounded in modulus. No algebraic square has been
replaced in the defining moment form. The two exterior terms together
are real symmetric by conjugation, and at r=4 their quadratic form
has absolute value at most t4 ||c||_2^2, where

    C=1+40000/101^4+1600000000/101^8
      =10832731072320801/10828567056280801,
    h4=b^8/700000000
      =256/5727708301326206498092619377734375,
    t4=2*101^(-20)*C
      =21665462144641602
       /132129096689825080931822600853816049099831724850779782801.

Both denominators are positive. The exact cross product proving h4>t4 is

    256*denominator(t4)-21665462144641602*denominator(h4)
      =33825048628501773340614204837476958493862762733806493928306>0.

Let k=r-4>=0. The head bound gains b^(2k); each exterior bound gains
at most101^(-4k). The exact ratio is

    101^(-4)/b^2=6765201/1664966416<1.

It follows for every real c that

    c^T D H_(2,r) D c
      >=b^(2k)[h4-t4*(6765201/1664966416)^k] ||c||_2^2
      >=b^(2k)(h4-t4) ||c||_2^2.

This is strictly positive for c!=0 for each integer r>=4. Invertible
real congruence by D proves H_(2,r)>0. This argument covers every shift;
the finite witness search below is not evidence for this quantifier.

### Exact prescribed negative witness

The complete beta list is

    (16/3249,1/441,1/625,z,conj(z)),
    z=(2611440-12928 i)/26639789089.

Multiplication of the three prescribed linear factors gives

    P(X)=X^3-(874826/99500625)X^2
              +(4061/179101125)X-16/895505625.

In particular the real-node contributions to Q(X^r P) vanish exactly.
Write d=3386028897813546182502688387904073865125. Exact substitution gives

    P(z)=(-53254884017141348482037596182944
           -34473439179388475382824589440 i)/d.

For r=158, the requested exact value is the real rational number

    Q(X^158 P)=2 Re[z^318 P(z)^2].                         (2)

The rational-complex certificate evaluates (2) and proves the stronger
strict rational comparison

    (163217/16)^318 * Q(X^158 P) < -1/10^30 < 0.           (3)

This is an exact negative value specified by rational operands and
finite integer powers, not a phase plot or floating-point sign.
The fully expanded reduced numerator and positive denominator of
(2) are retained at /selected/Q in the certificate. The exact rational
(3), including its positive normalizing factor, is retained there too.
The three zero real-node terms and both complex terms are stored,
and the program checks the unreduced five-term identity
sum beta^2*(beta^158 P(beta))^2 against (2) term by term.

For reproducibility the certificate generator implements complex
addition as (a,b)+(c,d)=(a+c,b+d), multiplication as
(a,b)(c,d)=(ac-bd,ad+bc), inversion as (a,-b)/(a^2+b^2), and nonnegative
integer powers by repeated squaring. All components are Fraction
objects. P is generated by multiplying the three real linear factors
and evaluated by Horner's rule. It searches only integers4..1000,
stops at a negative value, and records r=158. No assertion about the
minimal possible negative exponent is needed. (3) is checked by a
Fraction comparison; no floating-point value enters a certificate
assertion. Its sign conclusion is conditional on the explicitly stated
correct-arithmetic assumption, and is not a formal Lean verification.

Run from the active notebook:

    python3 scripts/h2-head/five_node_2204.py

Full evidence is `scripts/h2-head/five_node_2204.json`: model, all
occurrences, beta values, boxes, all head/error operands, exact margin,
extension ratio, P coefficients and values, searched values, selected
five terms, full Q value, positive normalization, checks and failures.
The complete head/error/comparison operands, all beta and P values,
P coefficients, full selected Q numerator/denominator, and all check
flags were inspected. All failures are empty. Explanatory printed
decimals are not proof. The head/error ratio is about2.72577*10^8;
the required threshold is1, while (3) is the strict negative threshold.

### Scope and unresolved inputs

This supplies both assertions of the single gate-approved frozen
test without changing nodes, range or witness. It is informative
negative evidence against a generic fixed-degree all-shift completion.
The source review distinguished Hermite-Sylvester's unrestricted
interpolation witness and cutoff-dependent finite-prefix models;
neither was substituted for this prescribed witness. No new theorem
reproof was needed. Actual-Xi realization and actual-Xi higher-degree
signs remain independent missing inputs. The all-degree matrix family
from L030-L032/C032a is not settled. No complete RH candidate is claimed.

### Independent conceptual and arithmetic audit, 21 November 2026 (step2206)

**Verdict.** Accepted without changing the model, constants, witness,
range or direct mathematical input C919e. This is the first independent
audit of the saved known-method specialization, classified REPRODUCTION
under the unchanged ready step2204/2205 assessment. It verifies a local
input; it supplies no stronger theorem or originality claim.

**Uniformity and conventions.** The five representatives are nonzero
and distinct, all have positive real part, and the last pair is closed
under conjugation. Including their negatives gives ten distinct roots;
each opposite class is counted once, and neither conjugate class can
be dropped. The three real nodes satisfy C919e's closed boxes exactly.
Expanding Q(X^r p) gives the exponent 2r+i+j+2. Multiplication on both
sides by the real D gives precisely (1), with ordinary transpose.
The real head terms are positive semidefinite and beta_j>=b, so their
weighted sum is at least b^(2r) times C919e's Gram matrix. This is the
correct direction of the matrix inequality.

For a complex w and real c, |c^T w|^2<=||c||_2^2 sum_i |w_i|^2.
Also |(c^T w)^2|=|c^T w|^2, while the defining square remains algebraic.
With |beta|=|alpha|^(-2), this yields exactly the displayed error bound.
The two terms are conjugates, making their sum real symmetric; their
absolute quadratic-form bounds add, explaining the factor two in t4.
The independent reconstruction checks h4, t4, C, their cross product
and 0<101^(-4)/b^2<1. For every integer k>=0 the latter ratio has kth
power at most one. Consequently the displayed lower bound is strictly
positive for every nonzero c and each integer r=4+k. The lower bound
may tend to zero with r; no uniform positive eigenvalue floor is
claimed or needed. Real invertibility of D transfers positive
definiteness to H_(2,r). No finite shift sample proves this step.

**Independent exact witness replay.** Run from the active notebook:

    python3 scripts/h2-head/five_node_audit_2206.py

The full certificate is `scripts/h2-head/five_node_audit_2206.json`.
The original generator is neither imported nor rerun, and its
certificate is unchanged. The audit derives beta from
((x^2-y^2),-2xy)/(x^2+y^2)^2 for alpha=x+iy. It constructs the cubic
coefficients by elementary symmetric functions and evaluates P by
its three factors, independently of the original coefficient-product
and Horner evaluation. For z=(A+iB)/D it expands z^318 by the finite
integer binomial sums, separating even and odd powers of i. A second
method uses 158 successive multiplications to form z^158 P(z), then
multiplies its algebraic square by z^2. These two computations agree
with each other and with every saved real and imaginary component of
both five-term lists. The three real-node terms are exactly zero;
the last two have equal negative real parts and opposite imaginary
parts. Their sum agrees with the full reduced rational Q in (2).

The certificate's field `normalizing_positive_factor` is a positive
divisor f=(163217/16)^(-318), not the multiplier in (3). The audit
checks normalized_Q=Q/f=(163217/16)^318 Q, so the two conventions
agree. If normalized_Q=N/D in reduced form with D>0, the strict
comparison is exactly -10^30 N-D>0. The complete integer comparison
is positive and stored at /thresholds/strict_normalized_cross_product
in the audit certificate. Thus neither sign relies on a printed
decimal or a misleading normalization label.

All 32 complete field comparisons and all 65 audit checks pass; no
failures are recorded. The original head/error/comparison operands,
beta values, coefficients, P values, five terms, full Q, normalized Q
and divisor were inspected as complete selected values, and both
five-term lists were compared in full by the independent program.
The nine displayed scalar/formula checks agree as well. All 229 saved
rational records have positive denominators and coprime numerator and
denominator. That format check includes earlier search entries; their
signs were not replayed or used. No minimality of r=158 is asserted.
The only shift tested in this witness audit is the prescribed r=158;
no model tuning or witness search was restarted.

**Arithmetic contract.** The original helpers implement ordinary
complex-pair addition, multiplication and reciprocal; the reciprocal
denominator is a strictly positive sum of squares at all five nodes.
Repeated squaring preserves out*z^n at each iteration and terminates
at n=0; Horner's rule processes the increasing-degree coefficient list
in reverse. Integer and Fraction operands are retained through every
assertion and comparison; the sole float conversion is explanatory
printing. Serialization retains the reduced integers exactly. The
independent binomial/finite-product replay uses no floating-point or
built-in complex arithmetic. The supporting documented interface is
Python3.15, *fractions — Rational numbers*, Fraction construction,
operations, numerator and denominator:
https://docs.python.org/3.15/library/fractions.html , and *Built-in
Types*, Numeric Types (unlimited-precision integers):
https://docs.python.org/3.15/builtins/stdtypes.html#numeric-types-int-float-complex .
These primary contracts were inspected in step2205 and reused here.
Correct execution remains assumed; this does not verify CPython itself.

The audit accepts the scoped generic obstruction. It imports no actual
theta sign, zero census or Xi realization and establishes no missing
all-degree positivity. The mathematical argument and direct input are
unchanged; no additional DAG edge is warranted.

## Mathlib

Full matching coverage of this frozen finite model has not been checked.
The cited sources supply supporting finite-matrix methods; no matching
Mathlib theorem or absence claim is asserted. The rational certificate
and its stated arithmetic contract are an informal reproducibility aid.
