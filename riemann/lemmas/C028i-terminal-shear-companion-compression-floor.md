# Corollary C028i: one terminal shear preserves the companion compression floor

## Hypotheses

Use C028h's actual centered monic reciprocal Jensen polynomial Q_d and
real companion A_d, for every integer d>=3. Its subdiagonal entries
are 1, its last column is -c_(d,d-j+1), and its last three principal
coordinates have block

    M_0 = [ 0  0  -b; 1  0  a; 0  1  0 ],
    a=binom(d,2)S_2>0,  b=2binom(d,3)S_3>0,

where the actual constants S_2,S_3 are fixed, finite and strictly
positive as established in C028h. All the other actual coefficients
remain in A_d. Let

    T=E_(d,d-1),  S=I+tT,  t in R,
    D=diag(delta_1,...,delta_d),  delta_j>0,
    B=D S A_d S^(-1) D^(-1),
    H=(B-B*)/(2i),  K_d(D,t)=||H||_1.

The norm is the Schatten trace norm. Let E:C^3->C^d be inclusion onto
coordinates d-2,d-1,d, in that order. Put

    x=delta_(d-1)/delta_(d-2)>0,
    y=delta_d/delta_(d-1)>0.

The order D S A_d S^(-1) D^(-1) is fixed. Both D and t may depend
arbitrarily on d. No RH, root reality or simplicity, diagonalizability,
bounded t, bounded conditioning or positive symmetrizer is assumed.
H_d is C028h's complete imaginary root height, with algebraic
multiplicities; real centering does not change it.

## Conclusion

The characteristic polynomial of B is Q_d, and

    H_d <= K_d(D,t),
    ||E*HE||_1 = R_d(x,y,t),
    R_d(x,y,t)^2 = (x-bt/x)^2+(b/(xy)+txy)^2
                  +(a/y-y+at^2*y)^2.                         (1)

With C028h's fixed positive constant

    c=sqrt(min{4S_3/(27sqrt(S_2)), S_2/4}),

one has, for every d>=3 and all allowed D,t,

    K_d(D,t) >= R_d(x,y,t) >= c*d.                           (2)

In fact the infimum of this compression over all positive D and real t
equals C028h's unsheared compression minimum:

    inf R_d = sqrt{2b/y_*+(a/y_*-y_*)^2},
    y_*>0,  y_*^4-b*y_*-a^2=0.                              (3)

It is attained at t=0, y=y_* and x=sqrt(b/y_*). No nonzero t attains
this global minimum. No assertion about minimizing the full K_d is made.
Consequently this specified one-shear family cannot pay H_d=o(d) by
a sublinear full trace norm. This is a majorant obstruction, not a
lower bound on actual root heights or a resolution of RH.

## Proof

### Imported inputs and applicability

C028h supplies the actual block M_0, the companion convention, the
strict coefficient signs and the exact unsheared optimization. For
clarity the standard matrix inputs used after the new similarity are:

* Nicholas J. Higham, *What Is a Companion Matrix?*, 23 March 2021,
  updated 9 April 2021, [identity (*) and alternative placements](https://nhigham.com/2021/03/23/what-is-a-companion-matrix/):
  the Frobenius companion's characteristic polynomial is Q_d.
* Gerhard Schmeisser, *Estimates for the Imaginary Parts of the Zeros
  of a Polynomial*, Mathematica Balkanica 16 (2002), 203-217,
  [Section 3, Lemma 1, printed pp.211-212](https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf):
  for any square complex matrix, absolute imaginary eigenvalue parts
  are weakly majorized by singular values of its Hermitian imaginary
  part. The full sum yields H_d<=K_d(D,t), including multiplicities,
  once the similarity below is verified.
* John Watrous, *The Theory of Quantum Information*, 2018 author-hosted
  pre-publication version, [Section 1.1, (1.165)-(1.175) and (1.179)-(1.181), pp.32-34](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf):
  the Schatten ideal inequality for compatible rectangular operators
  gives ||E*HE||_1<=||E*||_infinity ||H||_1 ||E||_infinity=||H||_1.

These are imports under the unchanged scope of assessment1587 and
assessments1523/1524. They need no normality, real eigenvalues or
orthogonal-polynomial premise. No generic theorem is reproved here.
Only the newly specified finite multiplication and optimization are
needed; the earlier diagonal-only formula cannot be assumed for S.

### Similarity, compression and its exact norm

Since d and d-1 are distinct, T^2=0. Therefore
(I+tT)(I-tT)=(I-tT)(I+tT)=I for every real t. D is invertible by
positivity, so B=(DS)A_d(DS)^(-1) has characteristic polynomial Q_d.
Higham's identity and real centering then identify all eigenvalue
heights, proving the stated application of Schmeisser.

S is the identity on the exterior d-3 coordinates and has terminal
block S_3=I_3+t E_(3,2). In particular E*S=S_3 E* and
S^(-1)E=E S_3^(-1). Thus even when A_d has exterior couplings,

    E*S A_d S^(-1)E = S_3 M_0 S_3^(-1)
      = [ 0  tb       -b;
          1  -ta       a;
          t  1-at^2    ta ].

The first multiplication adds t times row 2 to row 3; the second
subtracts t times column 3 from column 2. Compressing the diagonal
scaling next gives

    M:=E*BE = [ 0    tb/x          -b/(xy);
               x    -ta            a/y;
               txy  y(1-at^2)       ta ].

This remains exact at d=3, when the terminal block is the full matrix.
Because all entries are real and compression commutes with adjoints,
E*HE=(M-M^T)/(2i). Its real diagonal is zero; the three independent
skew entries have magnitudes given by the three expressions squared
in (1). A three-by-three real skew matrix N with independent entries
u,v,w has det(lambda I-N/(2i))=lambda*(lambda^2-(u^2+v^2+w^2)/4).
This follows by expanding that determinant; the cubic cross terms cancel.
Thus this Hermitian compression has eigenvalues 0,R_d/2,-R_d/2
and trace norm R_d, proving (1), including the factor of two. Watrous's
inequality gives K_d(D,t)>=R_d.

### Unrestricted shear optimization

For all real t and positive x,y, cancellation of the opposite cross
terms -2bt and +2bt gives the exact identity

    (x-bt/x)^2+(b/(xy)+txy)^2
       =(1+t^2*y^2)*(x^2+b^2/(x^2*y^2)).                   (4)

The two positive terms in the last parentheses have product b^2/y^2,
so their sum is at least 2b/y, with equality exactly at x^2=b/y.
Set

    k=sqrt(1+t^2*y^2)>=1,  r=y/k>0.

Combining (1) and (4), without any bound on t,y or their dependence on d,
gives

    R_d^2 >= 2b*k^2/y+(a*k^2/y-y)^2
           = 2b*k/r+k^2*(a/r-r)^2
           >= 2b/r+(a/r-r)^2 =: f_d(r).                    (5)

C028h proves that the minimum of f_d on r>0 is f_d(y_*), with the
unique positive quartic solution in (3). It also proves the uniform
bound f_d(r)>=c^2*d^2: take its unsheared ratios
(sqrt(b/r),r), whose squared block cost is exactly f_d(r).
Hence (5) proves (2) with the same constant and onset d=3.

Conversely t=0, y=y_* and x=sqrt(b/y_*) attain f_d(y_*).
Every such positive pair is realizable by D: choose terminal entries
1,x,xy and arbitrary positive earlier entries. This proves (3).
If t!=0, then k>1 and the difference in the last inequality of (5) is

    2b*(k-1)/r+(k^2-1)*(a/r-r)^2 > 0,

because b,r>0. Thus a nonzero shear cannot attain the global minimum.
No compactness of the unrestricted parameter space is assumed.

The required threshold was a compression cost divided by d tending to
zero; (2) instead supplies a uniform positive lower bound, even for
unbounded degree-dependent parameters. This meets the abandonment test
for precisely the specified shear family. Exterior coordinates were
omitted only through a contraction lower comparison. The inequalities
H_d<=K_d and K_d>=c*d provide no lower bound on H_d. In particular this
does not produce a nonreal zero or the missing actual-Xi positivity,
compact-mass cancellation or full-height upper payment. This is a local
specialization of assessed matrix methods, not a novelty claim.

### Independent finite audit1590 (2026-11-18)

Replayed the full calculation under assessment1588, separately approved
in approval1589. All displayed identities, inequalities and attainment
claims pass without correction. This is an audit of the existing
specialization, not a stronger theorem or a new general matrix result.

For the full-size support check, S is block diagonal relative to the
first d-3 and last three coordinates. Hence E*S=S_3 E* and
S^(-1)E=E S_3^(-1) hold as rectangular identities; neither requires
that A_d preserve the terminal subspace. T^2=0 gives both inverse
products, and (DS)^(-1)=S^(-1)D^(-1) verifies the specified order.
Left multiplication sends the last row of M_0 to (t,1,ta).
Right multiplication changes only column 2, to
(0,0,1)^T-t*(-b,a,ta)^T=(tb,-ta,1-at^2)^T.
Multiplication of entry (j,k) by delta_j/delta_k then gives exactly M.
At d=3 there is no exterior subspace; the same identities hold.

Set u=x-bt/x, v=b/(xy)+txy and w=a/y-y+at^2*y. Direct subtraction gives

    N:=2i E*HE = [ 0 -u -v; u 0 w; v -w 0 ].

Writing X=N/(2i), one has tr X=0, det X=0 and
tr(X^2)=(u^2+v^2+w^2)/2: each off-diagonal conjugate pair contributes
twice its squared modulus. Thus
det(lambda I-X)=lambda^3-(u^2+v^2+w^2)*lambda/4.
Its Hermitian spectrum is 0,+R_d/2,-R_d/2, giving trace norm R_d.
This checks signs and the factor 1/(2i) independently of a choice of
signs for the individual skew entries. The cited contraction inequality
is for the Schatten trace norm and has factor one.

Expanding u^2 and v^2 gives opposite terms -2bt,+2bt, and remaining
terms x^2+b^2*t^2/x^2+b^2/(x^2*y^2)+t^2*x^2*y^2.
This is exactly (4). Equality in its positive two-term lower bound
requires and is achieved by x^2=b/y, with no restriction on t.
For k=sqrt(1+t^2*y^2) and r=y/k, the third entry is
w=k*(a/r-r) and 2b*k^2/y=2b*k/r. This proves both equalities in (5).
Every original admissible pair (y,t) maps to r>0 and k>=1; the lower
comparison with f_d(r) therefore holds without assuming the new
variables independent or restricting unbounded parameter sequences.
Sharpness needs no converse parametrization: t=0 permits every r=y>0.

C028h's audited f_d has its unique positive minimizer y_*, its quartic
equation and its uniform bound f_d(r)>=c^2*d^2 for all r>0,d>=3.
Consequently the same c and onset apply here. To attain its exact
minimum, (5) must have equality at both comparisons. If t is nonzero,
then k>1 and its difference 2b*(k-1)/r+(k^2-1)*(a/r-r)^2 is strictly
positive, since b>0 and r>0. Thus equality forces t=0, then r=y=y_*
and x^2=b/y_*. These ratios are realized by the stated positive D.
In particular d=3 has b=2S_3>0 and supplies no exceptional equality.
No compactness, bounded conditioning or parameter limit is used.

The resulting floor holds for this compression and hence for the full
majorant K_d(D,t). It cannot be combined with H_d<=K_d(D,t) to give
a lower bound on H_d. The audit accepts and parks only this one-shear
payment route; general basis changes, actual compact nonreal mass,
H_d=o(d), S_F=0 and RH remain undecided. C028h remains the sole local
direct mathematical input; the existing standard imports and DAG are
unchanged. No numerical calculation is needed for this finite replay.

## Mathlib

Full matching coverage is not checked and is unknown. No absence or
formal verification is claimed. The cited standard matrix inputs are
imported; the actual terminal-shear calculation is proved above. The
result received the separate finite audit1590 above; this is informal
verification, not a Mathlib formalization.
