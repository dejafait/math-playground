# Lemma 977: finite-zero contour sign and horizontal-majorant audit

## Hypotheses

Use the actual Riemann zeta function, with its simple pole at 1,
the outside-strip classification in L009, and the nontrivial-zero
correspondence and symmetries in L018. Count all zero multiplicities.
No RH, simple-zero condition, sign of a Li coefficient or quantitative
zero clearance is assumed.

Let n>=1 be an integer, -3<a<-2, b=2*sqrt(n), and
sqrt(n)<T<sqrt(n)+1, where neither T nor -T is a zero ordinate.
Let C be the positively oriented rectangle with real sides a,b and
imaginary sides -T,T. Define

    k_n(s)=(1+1/s)^n-1=sum_(j=1)^n binom(n,j)s^(-j),
    H(s)=-zeta'(1+s)/zeta(1+s),
    H(s)-1/s=sum_(j>=0) eta_j s^j                 near s=0,
    S_f(n)=sum_(j=1)^n binom(n,j) eta_(j-1),
    lambda_n(T)=sum_(rho: |Im rho|<T) [1-(1-1/rho)^n],
    J_n(T)=(1/(2*pi*i)) integral_C k_n(s)H(s) ds.       (1)

The zero sum is finite. Its strict cutoff agrees with a weak cutoff
because T avoids zero ordinates. These are the ordinary, undivided
zeta conventions of Lagarias, Definition4.3/(4.5), Lemma4.4/(4.8),
and (6.1); the trivial GL(1) representation is self-dual. L968 and
L975 are downstream normalization context, not inputs to this proof.

## Conclusion

The exact finite-contour identity is

    J_n(T)=S_f(n)+lambda_n(T).                         (2)

In particular, the finite-zero residue has the opposite sign to the
one printed between (6.5) and (6.6), and in (6.7), of Lagarias's
published proof of Theorem6.1. Restoring the missing normalization of
the displayed rectangle integral does not remove the sign mismatch.
The pole at s=0 contributes S_f(n), with no extra residue from k_n(s)/s.

Independently, the horizontal geometric-decrease inference following
(6.12) does not follow from (6.10)-(6.12): the advertised upper-bound
factors are e for k_n+1 and 1/2 for the Dirichlet majorant, with
e/2>1. This is a failure of the printed inference. It does not prove
that the actual absolute integral is too large, that no better
majorant exists, or that the oscillatory integral bound is false.

Accordingly this audit does not certify the stated
O(sqrt(n)*log n) residual, with either sign. It neither proves
Theorem6.1 false nor supplies a repaired theorem or an RH result.
Classification: REPRODUCTION, a bounded verification of known residue
calculus and a suspect source inference, with no novelty claim.
Written in step214, 10 November 2026; no subsequent independent audit
is claimed.

## Proof

### Source contract and imported tool

The source being audited is J. C. Lagarias, *Li coefficients for
automorphic L-functions*, Ann. Inst. Fourier **57**(5) (2007),
1689-1740, DOI 10.5802/aif.2311:
[Definition4.3 and Lemma4.4, pp.1708-1709](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=21),
and [Theorem6.1, (6.1)-(6.12), pp.1721-1725](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=34).
The [arXiv math/0404394v4 Section6, 4 May2005](https://arxiv.org/html/math/0404394v4#S6)
has the same relevant signs and inference, numbered (6.106)-(6.117).
Published PDF text extraction and v4 HTML agree on these passages;
the screenshot tool returned placeholders, so no visual PDF check is
claimed. The published numbering is used below.

Import the finite residue theorem,
[NIST DLMF1.10(iv), (1.10.8)](https://dlmf.nist.gov/1.10.E8),
with the local zero-order and Laurent-series conventions of
[DLMF1.10(i),(iii)](https://dlmf.nist.gov/1.10.i).
Its application requires a positively oriented finite contour,
regularity on that contour and only finitely many interior isolated
singularities. No infinite-contour limit or asymptotic estimate is
imported. Replaying this elementary tool is necessary to verify the
source's suspect sign, rather than assuming its stated conclusion.

### Contour regularity and the origin

The only pole of zeta is at 1. L009 places all other zeros outside
the open critical strip at -2,-4,..., so their shifted positions for
H are -3,-5,..., all strictly to the left of a. The shifted nontrivial
zeros lie in -1<Re(s)<0. Hence no zero lies on a vertical side of C;
the choice of T excludes zeros on its horizontal sides. The kernel
has no pole except at 0. The finitely many relevant zeros are isolated
and lie in a compact set. These observations verify the finite
residue theorem's hypotheses. A permitted T exists for every n by
discreteness; this assertion provides no lower bound for its distance
from a zero ordinate.

At the simple pole of zeta, H(s)=1/s+sum_(r>=0) eta_r s^r.
Therefore

    k_n(s)/s=sum_(j=1)^n binom(n,j)s^(-j-1)

has zero residue: its exponents are at most -2. The coefficient of
s^(-1) in the product of k_n and the analytic part of H is precisely
S_f(n). Thus (6.5)'s small-circle formula survives the zeta pole
subtraction. Removing the pole from H in the whole contour would
not change its integral either, since the subtracted rational
function k_n(s)/s has no other pole and zero residue. This last
observation is only about the finite contour, not its bounds.

### Each zero, reflection, and the sign

If rho is a zero of order m, write locally

    zeta(u)=(u-rho)^m g(u),       g(rho)!=0.

The analytic logarithmic derivative of g then gives

    H(s)=-m/(s-(rho-1))-g'(1+s)/g(1+s).

Since rho!=1 and k_n is regular at rho-1, the residue there is

    -m*k_n(rho-1)
      =m*[1-(rho/(rho-1))^n].                         (3)

This formula includes a possible removable singularity when the
kernel vanishes there. There is no change in sign for multiplicity
greater than one.

L018 gives the multiplicity-preserving reflection rho -> 1-rho.
It preserves the cutoff |Im rho|<T, and

    rho/(rho-1)=1-1/(1-rho).

Consequently summing (3) over the finite multiset gives lambda_n(T),
with a plus sign. There are no enclosed trivial zeros for the zeta
rectangle chosen here. Adding the origin residue proves (2).
Equivalently, S_f(n)=J_n(T)-lambda_n(T). No estimate for J_n(T) has
been used or proved.

The published rectangle display after (6.5) writes an unnormalized
integral as a sum of residues and gives +k_n(rho-1) for each zero.
Even if its missing factor 1/(2*pi*i) is restored, the zero residue
must still be (3). Both contours are stated to be counterclockwise;
reversing only the zero contribution cannot be justified by orientation.
Nor does changing from lambda_n to lambda_(-n) fix this in the
self-dual zeta case: the same finite reflection equates these sums.
Equation (6.7) therefore has the wrong sign as an exact residue identity.
This is not by itself a counterexample to an asymptotic theorem whose
error could absorb a difference between particular sums.

For completeness, (4.12) agrees with Definition4.3's eta convention,
whereas (4.13) inserts an alternating factor absent from (4.8).
At n=2 its expression is 2*eta_0-eta_1, while (1), (4.8) and the
origin residue give 2*eta_0+eta_1. Their difference is -2*eta_1.
No value or nonvanishing estimate for eta_1 is required here: this
comparison shows exactly what an attempted change of convention
would need to justify. We use (4.5)/(4.8), not the alternating remark,
and do not add a separate claim about that numerical coefficient.

### What the horizontal inequalities actually provide

Put A_n(s)=k_n(s)+1. For s=sigma+i*T with sigma>=3, direct algebra
gives

    A_n(s+1)/A_n(s)=(s*(s+2)/(s+1)^2)^n
                   =(1-1/(s+1)^2)^n.

Thus the upper bound by (1+1/T^2)^n<=e appearing at the end of
(6.12) is valid on this segment. This does not validate every
intermediate displayed inequality, and none is needed for the
following failure of inference.

Let C_2=sum_(m>=2) Lambda(m)*m^(-2)<infinity, the absolute
Dirichlet-series value used in (6.10), specialized to zeta. Applying
that bound to the actual argument s+1 gives

    |H(s)| <= C_2*2^(-(sigma-1))=:D(sigma),
    D(sigma+1)=D(sigma)/2.                            (4)

Using s rather than s+1 changes a fixed factor in (4), not its
ratio. Even for |A_n|, the product of the stated stepwise bounds
has factor e/2>1, not a factor less than one. For the actual kernel
the triangle inequality only provides

    |k_n(s)|*|H(s)| <= (|A_n(s)|+1)*D(sigma).

No contraction for this quantity follows from the two stated factors
either. A pointwise Dirichlet upper bound is also not a comparison
of the actual values of H at successive complex arguments. The
assertion of geometric decrease after (6.12) is therefore unjustified
by the displayed estimates. An O(1) starting bound at sigma=3 does
not turn a factor greater than one into decay.

This finding concerns the offered majorization argument. It gives
no lower bound on the actual integrand and no lower bound on the
modulus of its integral. Cancellation on a horizontal segment or
between segments has not been analyzed. The audit stops at these
decisive defects: it does not repair the horizontal argument, vary
the cutoff, or certify the remaining clearance, endpoint comparison
and left-side estimates needed for a complete remainder theorem.

## Mathlib

Full matching coverage of (2) in these Li conventions, or of this
source audit, has not been checked and is unknown. L009 records
supporting zeta-zero facts, including `riemannZeta_neg_two_mul_nat_add_one`
and `riemannZeta_ne_zero_of_one_le_re`, in the
[RiemannZeta documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/RiemannZeta.html).
Those facts are not a formalization of this contour identity or the
claimed remainder. No new Mathlib search or Lean verification was
performed for this bounded audit.
