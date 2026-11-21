# Lemma 782: exact fixed-pair projection weighting

## Hypotheses

Use the actual pair (r,R)=(3,2048), k=2, and all analytic and
arithmetic qualifications of L779. In particular its two normalized
interior zeros alpha_1,alpha_2 are distinct, simple, nonzero and negative,
with |alpha_i|<1; their complete residues satisfy d_1>0>d_2.
These are certified local inputs, not a premise about other Xi zeros.
Use L777's exact normalization and one-based Hilbert-space coordinates:

    P(z)=(z-alpha_1)(z-alpha_2), F(z)=G(Rz)/P(z),
    p(z)=z^-2 P(z), b=p/F, c=F/p,
    C=diag(d_1,d_2), V_(l,j)=alpha_j^(l-1),
    U=Q_r H(b)V, Y=Q_r V, S=Y*U, A=U C Y*.

Here Q_r deletes coordinates 1,...,r. The Hankel entries are
H(b)_(l,h)=beta_(l+h-1), where beta_n is the nth positive Laurent
coefficient of b. All these coefficients, columns and matrices are real,
so Y*=Y^T. The operator A is still on the original complex Hilbert
space. F is entire and zero-free on a neighborhood of |z|<=sigma,
where sigma=9/8 is available from L779. E below is a new diagonal
matrix, not any truncation error denoted E in earlier results.

## Conclusion

Define exactly the objects proposed in step443:

    h_r(z)=sum_(n>=0) beta_(r+1+n) z^(n+1),
    K_ij=(h_r(alpha_i)-h_r(alpha_j))/(alpha_i-alpha_j)  (i!=j),
    K_ii=h_r'(alpha_i),
    E=diag(sqrt(|d_i| |alpha_i|^r)),
    J=diag(sign(d_i))=diag(1,-1), Q=(-1)^r E K E.

The power series is holomorphic on |z|<sigma. Its divided-difference
kernel has a locally uniformly convergent double-series extension,
including coincident evaluation arguments. With the actual projected
pairing, the exact identities are

    S=diag(alpha_i^r) K,
    E^-1 (I-C S) E=I-JQ,                                  (1)
    det(I-A)=det(I-C S)=det(I-JQ).                         (2)

E is real positive diagonal and invertible; K and Q are real symmetric.
The similarity (1) concerns the signed pairing, not a Gram matrix or
L777's singular-value compression. Here (-1)^r=-1. No inertia or
nullity estimate for J-Q, global function-class membership, uniform
order/radius estimate, or mixed-minor positivity is asserted. This
exact known-method specialization passes the separate step447 audit
below, retaining all inherited input qualifications.

## Proof

**Imported interfaces and reason for specialization.** Reuse the
invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-04-exact-projection-similarity-review.md`.
The two-node divided difference and its diagonal derivative convention
are Carl de Boor, *Divided Differences*, Surveys in Approximation Theory
1 (2005), 46–69, Example2/(10), printed p.49
([author PDF](https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf);
[arXiv:math/0502036v1](https://arxiv.org/pdf/math/0502036v1)).
Proposition25/(26) and its proof, pp.53–54, give the polynomial
divided-difference matrix interface. No use is made of the assessment's
ambiguous extracted display(27), or any half-plane membership theorem.
These known interfaces do not determine this projection's offset or
diagonal weights. The calculation below checks just those factors and
the convergence needed to apply the interface to the present series;
it does not reprove a general divided-difference theorem.

For the determinant use M. Duits, *Determinantal point processes*,
AppendixA, Lemmas66 and69, pp.51–52 of the
[DPP2 author PDF](https://people.kth.se/~duits/static/media/DPP2.44e051d148b79af222fa.pdf),
in the finite-rank specialization already justified in L779. Arbitrary
compatible rectangular factors and dependent columns are allowed.
Only determinant transfer is imported; neither positivity nor inertia
control follows from this theorem.

**Convergence before regrouping.** Put a=max_i |alpha_i|<1 and
m_sigma=min_(|z|=sigma)|F(z)|>0. L777's Laurent Cauchy estimate gives

    |beta_n|<=M_b sigma^-n (n>=1),
    M_b=(1+a/sigma)^2/m_sigma < infinity.                 (3)

This estimate is valid despite the pole of p at zero; it is a Laurent
estimate on the circle, not an assertion that b is holomorphic there.
For any 0<t<sigma and |x|,|y|<=t, define

    T(x,y)=sum_(u,v>=0) beta_(r+1+u+v) x^u y^v.

The sum of absolute values is at most

    M_b sigma^(-r-1) sum_(u,v>=0)(t/sigma)^(u+v)
      = M_b sigma^(-r-1)/(1-t/sigma)^2.                 (4)

Thus the double series converges absolutely and uniformly on every
such closed bidisk. In particular it is continuous on the diagonal,
and regrouping by n=u+v is valid. The series defining h_r and its
termwise derivative converge uniformly on compact subdisks of
|z|<sigma, by (3) and the convergent geometric derivative series.
Consequently h_r is holomorphic with the stated derivative.

For x!=y in this disk the finite identity

    sum_(u=0)^n x^u y^(n-u)=(x^(n+1)-y^(n+1))/(x-y)

and the justified regrouping show that
T(x,y)=(h_r(x)-h_r(y))/(x-y). On x=y, either the double
series itself or its continuous limit gives

    T(x,x)=sum_(n>=0)(n+1) beta_(r+1+n) x^n=h_r'(x).     (5)

This is a diagonal limit of evaluation arguments; it does not presume
that any actual zero is multiple. The double series also gives
T(x,y)=T(y,x), and real coefficients make K real symmetric when
evaluated at the certified real nodes. Equations (4)–(5) verify the
analytic conditions needed for the cited divided-difference convention.

**Exact projected pairing.** From L777, for l>r,

    U_(l,j)=sum_(h>=1) beta_(l+h-1) alpha_j^(h-1).

The other rows of U and Y vanish. Therefore, retaining both projection
factors in S=V^T Q_r H(b)V and using Q_r^2=Q_r,

    S_ij=sum_(l>=r+1) sum_(h>=1)
              alpha_i^(l-1) beta_(l+h-1) alpha_j^(h-1).

The outer product pairing is well defined by L777's bounded operators
and square-summable columns. Its displayed double sum is absolutely
convergent by (4) with a<=t<1 (or any a<t<sigma), multiplied by
|alpha_i|^r. Hence it equals that Hilbert-space pairing and may be
reindexed. Set l=r+1+u and h=1+v. The coefficient is
beta_(r+1+u+v), not beta_(r+u+v), and the remaining row factor is
alpha_i^(r+u), not alpha_i^(r+1+u). Thus

    S_ij=alpha_i^r T(alpha_i,alpha_j)=alpha_i^r K_ij.    (6)

For example the first retained row l=r+1 and column h=1 contribute
alpha_i^r beta_(r+1); this agrees with the constant term of T.
Equation (5) makes (6) valid also for i=j, with precisely the proposed
diagonal derivative. No conjugation of alpha_i occurs because these
particular nodes and columns are real; no extension to complex-node
grouping is inferred.

**Signs, similarity and determinant.** Since every alpha_i<0,

    d_i alpha_i^r
      =(-1)^r sign(d_i)|d_i||alpha_i|^r.

All d_i and alpha_i are nonzero. Thus E is invertible, C commutes
with the diagonal row factors, E commutes with J, and (6) gives

    C S=(-1)^r J E^2 K,
    E^-1 (C S) E=(-1)^r J E K E=JQ.

Subtracting this equality from I proves the orientation of (1).
In particular for r=3 the sign is minus: C S=-J E^2 K and
Q=-E K E. This is a similarity, not a congruence or a symmetry
assertion about C S. It uses the exact residues and the actual b=p/F.

L777 supplies A=U C Y*, a finite-rank operator of rank at most two.
The cited finite-rank determinant identity, with the same adjoint
convention as L779, gives det(I-A)=det(I-CY*U). Applying the finite
diagonal similarity proves (2). No infinite determinant limit, norm<1,
selfadjointness of A, inverse Gram matrix, or minor sign is needed.

The adverse scalar block of L780 belongs to its different balancing
W=diag(sqrt(|d_i|)); this proof imposes no positive-block condition
and does not contradict that evidence. All fixed-pair arithmetic and
analytic input qualifications remain inherited, without a new
certificate replay. Establishing the identity pays a normalization
bridge only; the prescribed J-Q inertia/nullity control and all global
steps remain independent research obligations.

**Independent critical replay, 2026-11-05 (step447).** The statements
(1)–(2) pass the fixed-pair audit; no correction or strengthening is
needed. Start afresh with the Hilbert-space pairing rather than the
claimed divided difference. Because Y=Q_r V and U=Q_r H(b)V,
Y*U=V^T Q_r H(b)V; Q_r^2=Q_r removes a duplicated projection,
not the surviving row cutoff. For l-1=r+u and h-1=v, with u,v>=0,
the Hankel index is l+h-1=r+1+u+v. The first three homogeneous
shells of S_ij/alpha_i^r are exactly

    beta_(r+1),
    beta_(r+2)(alpha_i+alpha_j),
    beta_(r+3)(alpha_i^2+alpha_i alpha_j+alpha_j^2).

At r=3 the first term is beta_4, and the first retained row factor
is alpha_i^3. Neither beta_3 nor alpha_i^4 is admissible. These
shells check the offset; the proof for the entire series uses (3)–(4),
not a finite truncation. The Laurent integral on |z|=sigma is legitimate
in the punctured zero-free disk. Its geometric majorant is uniform on
each closed bidisk of radius t<sigma and bounds all shells. Absolute
convergence permits the change from row/column indices to shells;
locally uniform convergence and the geometric derivative majorant
give the diagonal value sum_(n>=0)(n+1)beta_(r+1+n)x^n=h_r'(x).
Thus no value at zero of the meromorphic b, or unproved interchange,
enters the pairing or its diagonal limit.

Independently, set E_i=sqrt(|d_i||alpha_i|^r)>0. Each entry satisfies

    (E^-1 C S E)_ij
      =E_i^-1 d_i alpha_i^r K_ij E_j
      =(-1)^r sign(d_i) E_i K_ij E_j=(JQ)_ij.

This checks both off-diagonal weights and both residue signs, without
assuming that E commutes with K. Subtracting from I checks the displayed
similarity orientation. At r=3 the factor is -1 and Q=-EKE;
symmetry of K comes from the complete double series. No signed square
root, congruence, or positive-block premise has been substituted.

For the determinant, U and Y are bounded maps from C^2 into l2 and
C is finite, so A=UCY* is finite rank and trace class. Its range lies
in ran(U); restriction to that finite-dimensional invariant space and
the cited rectangular determinant identity give det(I-A)=det(I-CY*U),
even if U has dependent columns. This is the same adjoint and minus
sign as L779; an infinite-dimensional limiting determinant is unnecessary.
The subsequent similarity uses invertible E, not an inverse Gram matrix.
L777 and L779 are the direct inputs already recorded in the DAG; L780
is a consistency comparison, not a further premise. The old positive-
block and Taylor-index stops remain unaffected.

This replay independently validates the normalization bridge by known
methods, not a new sign or inertia theorem. It does not recertify L779's
arithmetic, audit all of L776, extend real/simple grouping, or control
nullity, growing orders/radii or actual-Xi all-degree mixed positivity.

## Mathlib

Full matching coverage has not been checked; no presence or absence
claim is made. The cited divided-difference and finite-rank determinant
interfaces, Laurent Cauchy bound, locally uniform power series and
finite diagonal algebra are the informal inputs. This is not formal
verification or a new general theorem beyond the sources checked.
