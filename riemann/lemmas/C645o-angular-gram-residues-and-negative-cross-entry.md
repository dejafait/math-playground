# Corollary 645o: exact angular Gram residues and a negative cross entry

## Hypotheses

Let n>=5, x=-5/4, R=11/8, U=R^2, eta=1/100 and t_j=j/n.
Let Z be a finite set of distinct points a with Re(a)=x and
|a|<=R-eta, containing x. Give each pole a positive integer original
simple-pole residue r_a, with M=sum_a r_a<=n/3. The same Z and residues
are used at every angle. Retain the product and symbol

    B_theta(v)=product_(j=0)^(n-1)
        R*(v-i*exp(i*theta)*t_j)/(U+i*exp(-i*theta)*t_j*v),
    q_theta(zeta)=sum_a r_a*B_theta(x)/(R*B_theta(a))
                                      *1/(zeta-a/R).

Use C645g's normalized circle measure, H^2 with nonnegative modes,
H^2_- with strictly negative modes, and H_q f=P_-(q*f). Its norm is
the largest operator norm. There is no separation, symmetry or
positivity assumption on the complex weighted amplitudes.

Write u=i*exp(i*theta) and define, for |u|=1,

    W_a(u)=(x/a)*product_(j=1)^(n-1)
              (x-t_j*u)/(a-t_j*u)*(U*u-t_j*a)/(U*u-t_j*x),
    I(a,b)=mean_u W_a(u)*conjugate(W_b(u)),
    K(a,b)=I(a,b)/(U-a*conjugate(b)).

The mean uses normalized angular measure. The conjugated denominator
angle in B is essential to these definitions.

## Conclusion

The exact constant-input reduction is

    mean_theta ||H_q_theta||^2
       >= mean_theta ||q_theta||_2^2
        = sum_(a,b in Z) r_a*r_b*K(a,b).                         (1)

Every I(a,b) is given by the finite residue formula (4) below, retaining
the common interior poles and the interior poles of the reflected
factor. K is Hermitian positive semidefinite, but its real entries need
not be nonnegative. In particular the admissible family

    n=12, Z={x,a}, a=x+i/2, r_x=r_a=1                            (2)

satisfies the exact strict bounds

    -141/1000 < Re K(x,a) < -140/1000 < 0.                       (3)

Thus dropping the cross terms in (1) as nonnegative is invalid, even
with positive integer original residues and the common anchor line.
This is a failure of that sufficient method, not a counterexample to
the uniform angular norm bound c*exp(-n/32). No estimate at the squared
threshold c^2*exp(-n/16), full-operator countersequence, Xi realization,
or RH conclusion is obtained. The calculation has not had an independent
audit, and no certified novelty is claimed.

## Proof

### Source scope and purpose

The unchanged invocation-start
[EXPLORE assessment](../drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md)
covers this exact common-pole angular target and Fourier/residue test.
Its theorem comparisons and duplicate searches are reused. The relevant
saved working note and C645l/C645m/C645n failure records were also
checked. Those results are contrasts, not mathematical premises of (1)--(3).
C645g supplies the spaces and scaling; its small-census bound is not used.

Import the projection convention from L. Baratchart, S. Chevillard and
T. Qian, *Minimax principle and lower bounds in H2-rational approximation*,
J. Approx. Theory 206 (2016), 17--47, preprint v2 (24 March 2015),
[Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004). Import scalar Fourier
orthogonality/Parseval from A. Levitt, *Analyse de Fourier et applications*,
[author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf),
version retrieved 2 November 2026, Theorem 1.3/Exercise 1.2 and Theorem
1.11/Corollary 1.12, printed pp.6,8 (PDF pp.12,14). The normalization
here divides Lebesgue measure by 2*pi, so every circle exponential has
norm one. No Parseval identity for the operator norm is assumed.

Import the residue theorem and simple-pole rule from R. W. Howell and
J. H. Mathews, *Complex Analysis*, online edition (front matter updated
22 August 2025),
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
as inspected in the reused assessments. The standard theorems are not
reproved. The product-specific residues and their exact sign are
calculated because none of those identities supplies a sign for K.

### 1. Normalization and the exact quadratic form

For each theta, all B denominators are nonzero on |v|<=R, since
their modulus is at least U-t_j*R>0. Each pole a avoids the rotated
zeros because |a|>=5/4>1>t_j. Thus W_a is continuous and finite on
the angular circle. The change u=i*exp(i*theta) preserves normalized
angular measure and gives exactly the product in the hypotheses;
the j=0 factor is x/a.

Put rho=(R-eta)/R<1. For fixed n and Z, all angular weights are
uniformly bounded on this compact circle. On |zeta|=1,

    q_theta(zeta)=sum_(k>=0) c_k(theta)*zeta^(-k-1),
    c_k(theta)=sum_a r_a*W_a(u)*a^k/R^(k+1).

The expansion converges absolutely and uniformly in both angular
variables because |a|/R<=rho and the sum over Z is finite. It contains
only negative modes, so H_q_theta 1=q_theta and ||1||_2=1.
Scalar Parseval gives ||q_theta||_2^2=sum_k |c_k(theta)|^2.

Expanding each square and summing the geometric series gives

    ||q_theta||_2^2
      =sum_(a,b) r_a*r_b*W_a(u)*conjugate(W_b(u))
                                      /(U-a*conjugate(b)).

All interchanges are justified by the uniform geometric majorant
rho^(2k) times a finite, family-dependent constant. This step does not
assert that this constant is uniform in n or Z; no such estimate is
needed for the exact identity. Angular integration proves (1).
Applying the same identity with arbitrary complex coefficients in
place of r_a proves Hermitian positive semidefiniteness of K.
That property alone says nothing about entrywise real signs.

### 2. All interior angular residues

For a rational function W_b define its reflection

    W_b^#(u)=conjugate(W_b(1/conjugate(u)))
      =(x/conjugate(b))*product_(j=1)^(n-1)
        (x*u-t_j)/(conjugate(b)*u-t_j)
                    *(U-t_j*conjugate(b)*u)/(U-t_j*x*u).

On |u|=1 this is conjugate(W_b(u)). Define

    p_j=t_j*x/U,                 s_j(b)=t_j/conjugate(b).

When a!=x let R_j(a)=Res_(u=p_j) W_a(u); when b!=x let
S_j(b)=Res_(u=s_j(b)) W_b^#(u). Their full product formulae are

    R_j(a)=(x/a)*(x-t_j*p_j)/(a-t_j*p_j)*t_j*(x-a)/U
          *product_(k!=j, 1<=k<n)
             (x-t_k*p_j)/(a-t_k*p_j)
                      *(U*p_j-t_k*a)/(U*p_j-t_k*x),

    S_j(b)=(x/conjugate(b))*(x*s_j-t_j)/conjugate(b)
                         *(U-t_j*conjugate(b)*s_j)/(U-t_j*x*s_j)
          *product_(k!=j, 1<=k<n)
             (x*s_j-t_k)/(conjugate(b)*s_j-t_k)
                      *(U-t_k*conjugate(b)*s_j)/(U-t_k*x*s_j),

where s_j means s_j(b) in the second expression. Then

    I(a,b)=x^2/(a*conjugate(b))
        +sum_(j=1)^(n-1) R_j(a)*W_b^#(p_j)/p_j       [if a!=x]
        +sum_(j=1)^(n-1) W_a(s_j(b))*S_j(b)/s_j(b)   [if b!=x]. (4)

A bracketed sum is omitted when its condition fails. In particular,
I(x,x)=1 and I(a,x)=x/a+sum_j R_j(a)/p_j for a!=x.

Here is the complete pole check for (4). The poles a/t_j of W_a
lie outside the circle because |a|/t_j>5/4. Its common poles p_j
are distinct, real, nonzero and have |p_j|<|x|/U=80/121<1.
The poles s_j(b) of the reflected factor have modulus <1/|b|<=4/5.
Its remaining poles U/(t_j*x) have modulus >U/|x|=121/80>1.
When b!=x, its ordinate is nonzero, so s_j(b) is nonreal and cannot
coincide with any p_k; the s_j(b) are pairwise distinct. Thus every
listed nonzero interior pole is at most simple. Product zeros can
cancel a pole, in which case its displayed residue is zero and the
formula still holds. No unlisted interior pole is possible.

If a=x, cancel the entire identity W_x=1 before listing its poles;
the same applies to W_x^#. Both W_a(0) and W_a(infinity) equal x/a,
as seen by evaluating each nonzero-grid factor. Consequently the
residue of W_a*W_b^#/u at zero is x^2/(a*conjugate(b)). The residue
theorem on |u|=1 now proves (4), with no pole on the contour.
The formula is not the invalid holomorphic mean-value substitution
I(a,x)=W_a(0); it includes every nonzero interior residue.

### 3. A rational sign certificate

For (2), M=2<=12/3, a!=x, and

    |a|^2=29/16 < (273/200)^2=(R-eta)^2.

The anchor also has the required clearance, and all original residues
are one. No separation or symmetry has been added to the target.

Set z_0=x/a and z_j=R_j(a)/p_j for 1<=j<=11. All real and imaginary
parts in (4) are rational. The following table gives integers L_j,T_j
such that, with D=10^9,

    L_j/D <= Re z_j < (L_j+1)/D,
    T_j/D <= Im z_j < (T_j+1)/D.

| j | L_j | T_j |
| ---: | ---: | ---: |
| 0 | 862068965 | 344827586 |
| 1 | 45226522 | 527542484 |
| 2 | -41297164 | 837217306 |
| 3 | -689103514 | 1279556866 |
| 4 | -2318064882 | 1054951580 |
| 5 | -3933558371 | -1662522085 |
| 6 | -1121903761 | -6497086318 |
| 7 | 7619281988 | -4816207492 |
| 8 | 7186637664 | 7460917183 |
| 9 | -6667270256 | 6387968866 |
| 10 | -2840127579 | -4752013762 |
| 11 | 1611563631 | -126970120 |

These are directed rational enclosures, not decimal quadrature values.
They can be reproduced by the displayed finite products using ordinary
Gaussian-rational multiplication
(p+iq)(r+is)=(pr-qs)+i(ps+qr) and division by
r+is=(r-is)/(r^2+s^2). The script
`scripts/one-sided-hankel/angular-constant-gram-certificate.py` uses
exact integer fractions throughout. For each rational v it computes
floor(D*v) by integer division, verifies the two inequalities in the
table, and saves the full fractions as well as these compact enclosures
in `scripts/one-sided-hankel/angular-constant-gram-certificate.json`.
There is no floating point or quadrature premise in this certificate.

Summing all twelve enclosures gives, for A=I(a,x),

    -286546757/D <= Re A < -286546745/D,
      38182094/D <= Im A <   38182106/D.

Hermitian symmetry gives I(x,a)=conjugate(A), while

    U-x*conjugate(a)=21/64-5i/8,
    Re K(x,a)=[(21/64)*Re A+(5/8)*Im A]
                                      /[(21/64)^2+(5/8)^2].

Both coefficients in this real linear expression are positive.
Substitution therefore gives the exact enclosure

    -4490198137/31890625000 <= Re K(x,a)
                               < -898039481/6378125000.

Integer cross multiplication places this interval strictly inside
(-141/1000,-140/1000), proving (3). In addition to the required
anchor calculation, the script independently evaluates I(x,a) using
the reflected poles and checks its exact equality with conjugate(I(a,x)).
This guards against silently losing the second residue sum in (4).
It also checks the two-pole Gram's real diagonal and positive determinant;
none of those checks is substituted for the uniform target estimate.

Reproduce with
`python3 scripts/one-sided-hankel/angular-constant-gram-certificate.py`.
The complete selected `/compact_anchor_residue_enclosures`,
`/compact_totals` and `/checks` fields were inspected using the shared
JSON inspector. All 16 exact checks passed. The separate exploratory
angular screen has no error enclosure and is not used in this proof.

The negative cross entry precludes an entrywise-positivity proof of
(1)'s lower bound. The full quadratic form remains nonnegative by
the exact norm identity. A negative summand cannot establish either
an upper bound for the operator or an asymptotic countersequence.

## Mathlib

Full matching coverage for the angle-dependent rational Gram identity,
the complete product-specific residue formula, and this exact negative
entry has not been checked. No absence claim is made. Parseval,
orthogonal projection, rational arithmetic and the residue theorem are
standard supporting inputs imported by the precise citations above;
their availability would not by itself settle the uniform exponent.
