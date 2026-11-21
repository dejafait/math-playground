# Corollary C874b: one positive extension does not sign the formal contact flux

## Hypotheses

Let S_1,...,S_8 be real numbers and set

    H_j=(S_(a+b+2))_(0<=a,b<=j),  j=2,3.

Assume H_3 is positive semidefinite and H_2 c=0 for a nonzero real
vector c=(c_0,c_1,c_2). Define p(x)=c_0+c_1 x+c_2 x^2 and the formal
heat derivatives, with precisely L874's normalization, by

    D_n=-2n(2n+1)S_(n+1)
        +4n sum_(a=1)^n S_a S_(n+1-a),  2<=n<=6,
    Phi=sum_(i,j=0)^2 c_i c_j D_(i+j+2).

For the actual L058 family at a slice lambda_*, L874 identifies
D_n=S_n'(lambda_*) and Phi=c^T H_2'(lambda_*)c. In the general
finite-data statement here, no actual-theta realization is assumed.

## Conclusion

If S_2=0, then S_2=...=S_7=0 and Phi=0.

If S_2>0, there are distinct real roots t of p and positive masses
w_t, with at most deg(p)<=2 atoms, such that

    S_k=sum_t w_t t^(k-2),  2<=k<=7,
    Phi=8 sum_t w_t t p'(t)^2 (w_t-t^2).                 (1)

In particular deg(p)=0 is impossible in this positive-mass branch.
The representation does not assert the same formula for prescribed
S_8, any flatness of H_3, or nonnegative support.

The finite premises alone do not force Phi<=0. Two exact examples,
both with arbitrary S_1, are:

* S_k=2 for 2<=k<=8, c=(-1,1,0). Then H_3 has all entries 2,
  H_2 c=0, and Phi=16>0. This retains lower-degree null vectors.
* S_2=3 and S_k=2 for 3<=k<=8, c=(0,-1,1). Here
  H_3=v_0 v_0^T+2v_1 v_1^T, where
  v_t=(1,t,t^2,t^3)^T, H_2 c=0, and Phi=16>0. This is a
  full-degree null vector and a rank-two example.

Consequently a sign proof using only this single-extension premise
and the L874 finite recurrence cannot work. For actual theta, (1)
is a conditional reduction if the contact premises hold; the examples
are not asserted to occur on its trajectory. No actual contact,
actual-theta counterexample, RH disproof, or invariant cone follows.
The parameter restriction 0<lambda_*<=1/8 does not enter the finite
algebra and provides no additional algebraic hypothesis used here.

## Proof

### Imported finite moment theorem and its scope

Use Raul E. Curto and Lawrence A. Fialkow, *Recursiveness, Positivity,
and Truncated Moment Problems*, Houston Journal of Mathematics
**17**(4) (1991), 603-635, Theorem 3.1, pp.611-612, specifically
the positive Hankel extension equivalence (vi), with the block range
criterion of Lemma 2.3, pp.607-608:
https://www.math.uh.edu/~hjm/v017n4/0603CURTO.pdf.
The prior source assessment is
`drafts/literature/2026-11-21-single-extension-contact-review-2126.md`.
This is an imported truncated Hamburger moment theorem; no moment
theory is reproved here.

For S_2>0 put gamma_j=S_(j+2). The theorem applies with k=2:
A(2)=H_2, its prescribed extension column is (S_5,S_6,S_7)^T,
and the supplied positive extension A(3) is H_3, whose last diagonal
entry is S_8. It supplies a positive representing measure mu for
gamma_0,...,gamma_5, that is, S_2,...,S_7. Singularity of H_2 is
allowed; a positive definite matrix or a flat given extension is
not a hypothesis. The theorem concerns a measure on R. Its odd
prefix conclusion does not prescribe the sixth moment S_8.

The moment identity through S_6 gives

    integral p(x)^2 dmu(x)=c^T H_2 c=0.

Since mu is positive, it is concentrated on the real roots of p.
For example the sets where |p|>=1/m each have zero measure,
which proves this assertion without a pointwise support assumption.
The nonzero polynomial p has degree at most two, so the measure is
the finite sum of its positive masses w_t at distinct roots t.
Its positive total mass S_2 excludes a constant nonzero p. This
proves the representation in the conclusion, including all singular
ranks and degrees one and two. Repeated roots are permitted, with
p'(t)=0 at a repeated root. Zero can be an atom.

### Exact contraction at the roots

Put b_n=sum_(i+j=n-2)c_i c_j for 2<=n<=6, so

    P(x)=sum_(n=2)^6 b_n x^n=x^2 p(x)^2.

The endpoint terms of the convolution contribute
8S_1 sum_n n b_n S_n. They vanish because

    sum_n n b_n S_n
      =sum_(i,j)(i+j+2)c_i c_j S_(i+j+2)
      =2 sum_i (i+1)c_i (H_2 c)_i=0.

Thus the finite recurrence, or L874 on the actual trajectory, gives

    Phi=-2 sum_(n=2)^6 n(2n+1)b_n S_(n+1)
        +4 sum_(n=2)^6 n b_n
                         sum_(a=2)^(n-1) S_a S_(n+1-a). (2)

Every coefficient here lies in the represented range S_2,...,S_7;
S_8 is not used in (2). All sums and subsequent integrals are finite.

For the linear term observe

    sum_n n(2n+1)b_n x^(n-1)=2xP''(x)+3P'(x).

At any root t of p, P'(t)=0 and P''(t)=2t^2 p'(t)^2.
Inserting the atomic moment representation therefore makes the
linear term of (2) equal to -8 sum_t w_t t^3 p'(t)^2.
These polynomial identities remain valid at t=0; no division by t
has occurred.

For the quadratic term define the polynomial

    Q(x)=sum_n n b_n x^(n-2)=2p(x)^2+2x p(x)p'(x).

The finite double-moment kernel in that term is

    sum_n n b_n sum_(a=2)^(n-1) x^(a-2)y^(n-1-a)
       =(Q(x)-Q(y))/(x-y)  if x!=y,

with diagonal value Q'(x). The empty sum for n=2 is zero;
the equality is the elementary difference-of-powers identity for
each n>=3. At two distinct roots of p this kernel vanishes,
since both Q values are zero. At a root t its diagonal value is
Q'(t)=2t p'(t)^2. Thus the quadratic term of (2) is
8 sum_t w_t^2 t p'(t)^2. Combining the terms proves (1).

This derivation covers c_2=0 as well as c_2!=0. It does not replace
a lower-degree p by an artificial quadratic or divide by its leading
coefficient. For a double root the derivative factor in (1) is zero.

### Zero mass and explicit violations

For any real positive semidefinite matrix, a zero diagonal entry
forces its entire row to vanish: each two-by-two principal minor
implies |h_ij|^2<=h_ii h_jj. Apply this first to the (0,0) entry
S_2 of H_3, giving S_2,...,S_5=0. Its (1,1) entry S_4=0 then gives
S_6=0. Its (2,2) entry S_6=0 gives S_7=0. Hence H_2=0 and all
D_n for 2<=n<=6 vanish: their linear terms use S_3,...,S_7,
and every product has a zero factor from S_2,...,S_6, including
the terms involving S_1. Therefore Phi=0 for every c. The last
entry S_8 can remain positive; no positive-mass moment theorem
was applied in this case.

For the first example the measure 2 delta_1 represents even the
prescribed S_8 and proves H_3>=0 by its rank-one Gram form.
The first three entries of v_1 have dot product zero with
(-1,1,0). Formula (1), with p(x)=x-1 and w_1=2, gives
Phi=8*2*1*(2-1)=16, exceeding the required upper bound zero.

For the second example use delta_0+2 delta_1. Its moments are
S_2=3 and S_k=2 for k>=3; the displayed Gram form proves H_3>=0.
The polynomial p(x)=x(x-1) vanishes at both atoms. The atom zero
contributes zero in (1), and p'(1)=1 gives the same Phi=16.
These examples are formal logarithmic coefficient data equipped
with the local heat recurrence. No theta realization or prescribed
probability density is constructed. In particular their algebraic
violation cannot refute a sign claim using additional actual-theta
structure. The unchanged main gap is L030-L032/C032a.

### Verification and remaining obligations

`python3 scripts/heat/single_extension_contact_2128.py` writes the
exact rational checks to
`scripts/heat/single-extension-contact-2128.json`. It computes the
recurrence directly, cancels arbitrary S_1 symbolically as an affine
parameter, verifies the null vectors and complete Gram matrices,
compares with (1), and checks the zero-mass branch. All eight exact
cases pass with zero failures; the complete cases and failures arrays
were inspected with `../scripts/loop/inspect_json.py`. The handwritten
proof above establishes the general result; finite checks alone
would not do so. This is a specialization of imported moment theory
and a finite obstruction calculation, not a claim of new moment
theory or certified originality. The independent critical audit is
recorded below.

Actual H_3 positivity/contact existence, actual realizability or
exclusion of these atomic configurations, actual flux signs,
initialization, non-strict equality handling and global/all-degree
continuation remain unproved. A larger positive extension alone
does not repair these examples: both already have positive atomic
extensions at every order. This last observation concerns auxiliary
moment data only, not the actual theta hierarchy.

### Independent critical audit — 21 November 2026, step2130

No mathematical error was found within the stated finite-data scope.
The argument and its hypotheses are unchanged. This validates a local
specialization and obstruction, not progress beyond the checked sources
in moment theory, and not an actual-theta signed result.

The primary Curto-Fialkow PDF was reopened at Theorem 3.1,
Lemma 2.3 and Corollary 3.4's proof, pp.615-616. In the latter, the
first invertible corner supplies the measure and the forced recurrence
propagates its moments through the odd endpoint. This confirms that
singular H_2 is covered. Here the given PSD block supplies the required
range condition with column (S_5,S_6,S_7), and S_2>0 is the initial-mass
hypothesis. No assertion about prescribed S_8, flatness or positive
support has been imported. Screenshot requests returned no inspectable
page images; the audit uses the legible theorem/proof text and the
previous saved extraction, without claiming visual verification.

The normalized logarithm calculation in L874 was checked against
L058's backward heat sign: the derivative of log F(lambda,0) contributes
only the constant spatial coefficient. The positive coefficients
therefore give exactly the displayed D_n. At contact the two endpoint
terms give 8S_1 sum_n n b_n S_n, which vanishes by H_2 c=0, including
lower-degree c. The remaining indices end at S_7. There is no
coefficient-range extension hidden in the contraction.

For the root calculation, the following identities check both the
diagonal and the off-diagonal cases without a division by a root:

    P''-2x^2(p')^2 = p(2p+8xp'+2x^2p''),
    Q'-2x(p')^2 = 2p(3p'+xp'').

Also P'=2xp^2+2x^2pp'. Thus at a root, P'=0 and the first
identity gives the claimed linear term. The difference-of-powers
identity gives the off-diagonal kernel; since Q is zero at both
distinct roots, that contribution vanishes. On the diagonal the
second identity gives Q'(t)=2t p'(t)^2. Zero roots therefore contribute
zero, and repeated roots contribute zero through p'(t). None of these
arguments assumes c_2!=0, distinct roots of the entire polynomial,
or nonnegative roots. A nonzero constant p is excluded only in the
positive-mass branch by its positive integral square.

The zero-mass argument was checked independently of moment theory:
successive zero rows 0,1,2 in the PSD H_3 force exactly S_2,...,S_7
to vanish, and leave S_8>=0 unrestricted. Every D_n, 2<=n<=6,
is then zero for arbitrary S_1 and every null vector. In particular
the constant-polynomial case is retained here. This proves the whole
branch, not just the two sampled zero-mass cases.

`python3 scripts/heat/single_extension_audit_2130.py` independently
checks six polynomial identities by exact coefficient arithmetic,
all eight original cases, every one of the 15 principal minors of
each H_3, null equations and moment/root residuals. It computes the
recurrence without importing the original program. Since that
recurrence is affine in S_1, its evaluations at 0 and 1 certify the
constant and slope in these cases. All residuals and failures in
`scripts/heat/single-extension-audit-2130.json` were inspected in full
using `../scripts/loop/inspect_json.py` at the selected fields.
The original program was also inspected and replayed. Both obstruction
fluxes equal 16, exceeding the required upper bound zero; all checks
pass. The general proof above, rather than these finite cases, supplies
the arbitrary-data identity and singular branches.

Finally, auxiliary atoms here represent logarithmic coefficients
S_2,...,S_7. They are not the u-variable probability law of L058.
Positive extensions of these auxiliary examples at every order do
not certify ordinary moment positivity of a cosine density, the exact
theta kernel, a heat trajectory, or RH. Retain the finite-premise stop;
reopening actual-theta signing requires an independently testable new
restriction. The remaining obligations and Mathlib qualifications below
are unchanged.

## Mathlib

Full matching coverage is not checked, including the precise odd
singular truncated-moment theorem and this heat specialization.
Supporting formal coverage of PSD row cancellation, polynomial
identities and atomic integration is also unchecked. No absence is
claimed. Reference: https://leanprover-community.github.io/mathlib4_docs/.
