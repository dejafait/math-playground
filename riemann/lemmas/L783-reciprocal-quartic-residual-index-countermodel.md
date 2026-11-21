# Lemma 783: reciprocal local factors do not preserve the proposed residual index

## Hypotheses

This is a polynomial model, not the actual Xi function. Define

    G_0(z)=(z+4/5)(z+9/10)(1+4z^2/5), r=3, R=1, k=2,
    alpha_1=-4/5, alpha_2=-9/10,
    P(z)=(z-alpha_1)(z-alpha_2), F_0(z)=1+4z^2/5,
    p=z^-2 P, b=p/F_0, c=F_0/p, sigma=21/20.

Use one-based sequence coordinates. Q_3 deletes coordinates 1,2,3;
it is different from the finite matrix Q below. If beta_n denotes
the nth Laurent coefficient of b on its annulus containing the unit
circle, set H(b)_(l,h)=beta_(l+h-1), for l,h>=1. Define

    d_i=alpha_i^2 F_0(alpha_i)/P'(alpha_i), C=diag(d_i),
    V_(l,i)=alpha_i^(l-1), U=Q_3 H(b)V, Y=Q_3 V, S=Y*U,
    h_3(z)=sum_(n>=0) beta_(4+n) z^(n+1),
    K_ij=(h_3(alpha_i)-h_3(alpha_j))/(alpha_i-alpha_j) (i!=j),
    K_ii=h_3'(alpha_i), E_ii=sqrt(|d_i||alpha_i|^3),
    J=diag(sign(d_i)), Q=-E K E.

The inner product is conjugate-linear in its first argument; these
data are real. All infinite sums and boundedness are justified below.
Write inertia as (n_+,n_0,n_-), including multiplicities.

## Conclusion

G_0 has real nonnegative coefficients, G_0(0)>0, G_0(1)>0, exactly
two simple nonzero negative zeros inside the unit disk, and no zero
on its boundary. F_0 is entire and zero-free on a neighborhood of
the closed sigma disk. G_0 has a finite genus-zero product and order
zero, hence order at most one half. The complete reciprocal factors
satisfy bc=1 wherever defined. Their projected pairing and similarity
are exactly

    S=diag(alpha_i^3) K,
    E^-1 (I-C S) E=I-JQ, J=diag(1,-1).

Nevertheless,

    inertia(J-Q)=(2,0,0), inertia(J)=(1,0,1).

Thus n_0(J-Q)=0 holds but n_-(J-Q)=n_-(J) fails. These local
conditions, even with the stated coefficient/growth conditions, do
not suffice for the proposed residual-index bound. This is neither
an RH disproof nor an obstruction to an argument using additional
Xi structure. No actual theta/cosh-mixture realization, positive
infinite coefficient sequence, Xi strip geometry, asymptotic zero
count, global function-class premise, or other mixed-minor conclusion
is asserted. This new specialization awaits an independent audit.

## Proof

**Known methods and scope.** Use the invocation-start SPECIALIZE
assessment `drafts/literature/2026-11-05-reciprocal-quartic-inertia-test.md`.
The divided-difference/derivative convention is Carl de Boor,
*Divided Differences*, Surveys in Approximation Theory 1 (2005),
46–69, Example 2/(10), p.49; Proposition 25/(26) and proof,
pp.53–54 ([primary author PDF](https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf)).
Only this convention and its polynomial interface are imported;
the complete-series limit is checked here. The finite-rank determinant
interface is M. Duits, *Determinantal point processes*, Appendix A,
Lemmas 66 and 69, pp.51–52
([author PDF](https://people.kth.se/~duits/static/media/DPP2.44e051d148b79af222fa.pdf)).
The inertia interface is Sylvester's law of inertia; compare the
invertible-congruence step of G. Berkolaiko and P. Kuchment,
*Spectral shift via “lateral” perturbation*, J. Spectr. Theory 12
(2022), 83–104, Theorem 2.7/proof pp.88–91,
[DOI 10.4171/JST/395](https://ems.press/content/serial-article-files/33861).
No Schur residual-index estimate from that theorem is presumed.
The sources do not compute these prescribed factors or this matrix;
this exact rational specialization is necessary to test the premise.
No general source theorem is reproved, and no originality beyond the
sources checked is claimed.

The definitions follow L777's conventions. L782 is a fixed-actual-pair
comparison, not a theorem applied to G_0. L780's different balanced
block is also a comparison only. The present model calculation proves
its own analytic and algebraic identities without assuming any
actual-Xi input from those results.

**Admissibility, including exterior roots.** Expansion gives

    G_0(z)=18/25+(17/10)z+(197/125)z^2+(34/25)z^3+(4/5)z^4.

All five coefficients are positive, G_0(0)=18/25 and
G_0(1)=1539/250. Its four roots are exactly

    -4/5, -9/10, +i sqrt(5)/2, -i sqrt(5)/2.

They are distinct and nonzero. The last two have modulus sqrt(5)/2>1
and the first two lie in (-1,0), so the interior count and contour
nonvanishing hold. Since sigma^2=441/400<5/4, the exterior roots
also lie strictly outside the sigma disk, leaving a zero-free
neighborhood for F_0. More explicitly, for |z|<=sigma,

    |F_0(z)|>=1-(4/5)sigma^2=59/500>0.

As a polynomial with nonzero constant term, G_0 is its constant term
times the finite product of (1-z/zeta) over the four displayed roots;
this is a genus-zero representation. Its maximum modulus grows as
a degree-four polynomial, so its entire-function order is zero.
In particular it satisfies any order-at-most-one-half upper growth
requirement. This upper bound imposes no infinite zero-count law.

**Complete Laurent factors, with the analytic part of c retained.**
Since P'=2z+17/10, direct evaluation gives

    d_1=6048/625>0, d_2=-8343/625<0.

Exact rational identities are

    b(z)=18/(25z^2)+17/(10z)
           +(53/125-(34/25)z)/(1+(4/5)z^2),             (1)
    c(z)=(4/5)z^2-(34/25)z+342/125
           +d_1/(z-alpha_1)+d_2/(z-alpha_2).            (2)

Multiplication by z^2 F_0 and P respectively verifies them, with
no discarded scalar. In (2) the combined principal-part numerator
is -(459/125)z-6156/3125. In particular the polynomial analytic
part is present; it contributes no negative Laurent coefficients.

Put q=-4/5. Expanding the rational part of (1) on
0<|z|<sqrt(5)/2 gives the complete positive-index coefficients

    beta_(2m)=(53/125)q^m (m>=1),
    beta_(2m+1)=-(34/25)q^m (m>=0).                     (3)

The two explicit negative-power terms in (1) contribute no positive
coefficient. Expanding (2) for |z|>9/10 gives, for every n>=1,

    c_(-n)=d_1 alpha_1^(n-1)+d_2 alpha_2^(n-1).        (4)

Thus both expansions use their unique Laurent coefficients on the
common annulus 9/10<|z|<sqrt(5)/2, which contains the unit circle.
Equation (4), including c_(-1)=d_1+d_2, proves directly
H(tilde c)=VCV^T with the stated one-based Hankel convention.
The columns of V are square summable. The geometric coefficients
in (3) give sum_(n>=1) n|beta_n|^2<infinity, so H(b) is
Hilbert–Schmidt and all the projected operators are bounded.
Consequently A=Q_3 H(b)H(tilde c)Q_3=UCY^T is finite rank.

**Full-series pairing and diagonal limit.** Formula (3) sums exactly to

    h_3(z)=((848/3125)z-(544/625)z^2)/(1+(4/5)z^2),    (5)

for |z|<sqrt(5)/2. This is the whole tail, not a Taylor approximation.
To justify every reindexing, take sigma=21/20 and let
M=max_(|z|=sigma)|b(z)|<infinity. The Laurent Cauchy formula on
this punctured disk gives |beta_n|<=M sigma^-n. For every t<sigma,
the double series

    T(x,y)=sum_(u,v>=0) beta_(4+u+v)x^u y^v

converges absolutely and uniformly on |x|,|y|<=t, by the bound
M sigma^-4/(1-t/sigma)^2. The derivative series for h_3 also
converges locally uniformly. Regrouping by u+v and using the finite
geometric identity gives T(x,y)=(h_3(x)-h_3(y))/(x-y) off the
diagonal, and T(x,x)=h_3'(x) on it. This justifies both the complete
series and the coincident-argument case of the cited interface.

Directly from the Hilbert-space pairing and the surviving projection,

    S_ij=sum_(l>=4,h>=1)
             alpha_i^(l-1) beta_(l+h-1) alpha_j^(h-1)
        =alpha_i^3 sum_(u,v>=0) beta_(4+u+v)alpha_i^u alpha_j^v
        =alpha_i^3 K_ij.                               (6)

Both nodes have modulus at most 9/10<sigma, so the displayed sums
are absolutely convergent by the preceding bound. The substitutions
are l=4+u and h=1+v. The first term is alpha_i^3 beta_4; neither
beta_3 nor a fourth-power row factor occurs. Equation (6) includes
the diagonal by the established derivative limit.

Evaluating (5) and its derivative exactly yields

    K = [[3152/4725, 16/25], [16/25, 1576/2575]],
    S = [[-201728/590625, -1024/3125],
         [-1458/3125, -143613/321875]].

For a direct derivative check, if a=848/3125, b_0=-544/625 and
t_0=4/5, then h_3'(x)=(a+2b_0 x-a t_0 x^2)/(1+t_0 x^2)^2.
All denominators here are positive for real x, and alpha_1-alpha_2
=1/10 is nonzero. Hence there is no singular evaluation in K.

**Similarity, full inertia and nullity.** Set w_i=E_ii^2. The exact values are

    w_1=387072/78125>0, w_2=6082047/625000>0.

Since alpha_i<0 and r=3, d_i alpha_i^3=-J_ii w_i. Thus (6) gives
CS=-J E^2 K and E^-1 CS E=-J E K E=JQ. Subtracting from I
proves the stated invertible diagonal similarity with its minus sign.
This is not a congruence of CS or an assertion that CS is symmetric.

For inertia use the separate positive diagonal congruence

    T_0=E^-1(J-Q)E^-1=diag(1/w_1,-1/w_2)+K
       =[[44489/51200, 16/25],
         [16/25, 751808/1476225]].                       (7)

Its determinant and two LDL pivots are exactly

    det(T_0)=311063/9447840>0,
    p_1=44489/51200>0,
    p_2=det(T_0)/p_1=99540160/2627030961>0.             (8)

All integer denominators in (7)–(8) are strictly positive. For
complex x,y its quadratic form is

    p_1 |x+(T_0,12/p_1)y|^2+p_2 |y|^2.

It is strictly positive on every nonzero vector. Since E is invertible,
J-Q=E T_0 E is also positive definite. Thus it has two positive
eigenvalues, no zero eigenvalue and no negative eigenvalue, whereas
J=diag(1,-1) has one positive and one negative eigenvalue. This
establishes the full claimed index failure, rather than determinant
parity alone.

As an orientation check, finite diagonal algebra gives

    det(I-CS)=det(I-JQ)=det(J)det(J-Q)
              =-w_1 w_2 det(T_0)
              =-48443707368/30517578125<0.

If the operator determinant is used, A is finite rank as shown above;
restricting to its finite-dimensional invariant range and applying
the cited rectangular determinant identity gives det(I-A)=det(I-CS).
No Toeplitz prefactor, infinite determinant limit, or unverified
Fredholm sign identity is needed for the inertia conclusion.

**Exact evidence and limitations.** Reproduce the finite rational
checks with `python3 scripts/reciprocal-quartic/exact-inertia-450.py`.
The complete certificate is
`scripts/reciprocal-quartic/exact-inertia-450.json`: it retains the
polynomial identities, full coefficient formulas, residues, matrices,
weights, pivots, determinant orientation, actual/required indices and
all 18 checks (no failures). Load-bearing matrix/residue fields and
all check results were inspected in full. The proof of convergence,
root exhaustion and inertia is given above; a script success flag or
finite coefficient preview is not substituted for those arguments.
The script uses exact standard-library Fraction arithmetic; no new
independent executable audit is claimed.

The diagnostic therefore stops the implication from precisely these
local premises to this index bound. It does not stop indefinite
methods with additional independently proved Xi premises, and it
does not establish or refute all-degree mixed positivity for Xi.

## Mathlib

Full matching coverage is unchecked; no presence or absence claim is
made. The informal inputs are the precisely cited divided-difference
and finite-rank interfaces, the standard Laurent Cauchy formula and
Sylvester law of inertia, and exact rational/geometric-series algebra.
No formal verification or new general theorem beyond the inspected
sources is asserted.
