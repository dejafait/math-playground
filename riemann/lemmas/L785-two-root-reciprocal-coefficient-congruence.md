# Lemma 785: explicit two-root reciprocal coefficient congruence

## Hypotheses

Let sigma>1. Let g be holomorphic on a neighborhood of the closed disk
|z|<=sigma, real on its real diameter, with g(0)>0. Suppose its only
zeros in that closed disk are two distinct simple roots a,b in (-1,0).
Put alpha_1=a, alpha_2=b and

    P(z)=(z-a)(z-b), F=g/P, p=z^-2 P, b_fun=p/F,
    d_i=alpha_i^2 F(alpha_i)/P'(alpha_i),
    E=diag(sqrt(|d_i| |alpha_i|^3)), J=diag(sign(d_i)).

Removable values of F are understood. Write beta_m for the complete
Laurent coefficients of b_fun on 0<|z|<sigma, and define

    h_3(z)=sum_(n>=0) beta_(4+n) z^(n+1),
    K_ij=(h_3(alpha_i)-h_3(alpha_j))/(alpha_i-alpha_j), i!=j,
    K_ii=h_3'(alpha_i), R=J+E K E.

Use u_j, the coefficient of z^j in 1/g, only locally at zero; it is
not assumed to converge at either selected root. All matrices below
are real. Inertia means (n_+,n_0,n_-).

## Conclusion

Define the root-independent two-by-two Hankel block and root-dependent
evaluation matrix

    H=[[u_2,u_3],[u_3,u_4]], W=[[1,-b],[1,-a]].

Then every defining expression above exists and

    E^-1 R E^-1 = W H W^T,
    R=(E W) H (E W)^T.                                  (1)

An explicit real invertible change of basis is

    C=E^-1 W^-T
     =E^-1 * [[-a,-1],[b,1]]/(b-a),
    C^T R C=H.                                          (2)

In particular inertia(R)=inertia(H), including nullity, also when H
is singular or zero. No inverse of H or R is used. The block uses only
u_2,u_3,u_4 among the permitted u_0,...,u_5. This is an interface,
not a sign theorem: no sign of H, index equality with J, actual-Xi
global grouping, other order or mixed-minor positivity is asserted.
The separate step460 conceptual audit validates this conditional statement,
including singular and zero coefficient blocks; see the audit below.

## Proof

**Inputs, comparison and scope.** The prior EXPLORE assessment is
`drafts/literature/2026-11-05-two-root-reciprocal-coefficient-interface.md`.
L784(6)-(8) motivates this calculation but supplies no general premise;
L781 concerns different coefficients and L783 is a contrast, not an
input here. We prove all required analytic cancellation for these
arbitrary data rather than importing the fixed example.

The standard analytic inputs are the disk Taylor theorem and removable
singularity theorem, NIST DLMF [1.10(i)](https://dlmf.nist.gov/1.10.i),
equation1.10.1 and Zeros, and [1.10(iii)](https://dlmf.nist.gov/1.10.iii),
including Laurent equations1.10.6-7. The divided-difference convention,
including the diagonal derivative, is Carl de Boor, *Divided Differences*,
Surveys in Approximation Theory1 (2005),46-69, Example2/(10), p.49
and Proposition35 with proof and Definition37, pp.58-59
([primary PDF](https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf)).
The latter passages extend polynomial divided differences to functions
with the required derivatives by Hermite interpolation; our functions
are holomorphic near the nodes.
For coefficient/evaluation comparison the inspected primary reference is
G. Heinig and K. Rost, *Bezoutians*, Chemnitz preprint2008-09,
Proposition7.15/(7.11), p.45 and Proposition9.1/(9.3)-(9.4), p.54
([primary PDF](https://www.tu-chemnitz.de/mathematik/preprint/2008/PREPRINT_09.pdf)).
Their rational expansion at infinity is not identified with the local
u_j. Instead we calculate the precise small analytic residual below;
neither general rational congruence theorem is reproved. Equality of
inertia under the explicit real congruence uses Sylvester's law of
inertia, specifically Yuji Nakatsukasa and Vanni Noferini, *Inertia laws
and localization of real eigenvalues for generalized indefinite
eigenvalue problems*, arXiv:1711.00495v1, Theorem1 and proof, p.1
([primary PDF](https://arxiv.org/pdf/1711.00495v1#page=1)). Its Hermitian
forms may be singular; only the congruence map must be invertible.
Real symmetric forms and our real invertible map meet those hypotheses.
These are known methods; no originality beyond the inspected
sources is claimed. The assessment did not locate this exact interface.

**Analytic definitions and complete tail.** Simplicity of a,b makes F
holomorphic with F(alpha_i)=g'(alpha_i)/P'(alpha_i)!=0 at those points.
Elsewhere in the closed disk it is nonzero by the zero hypothesis.
Thus F is zero-free on a neighborhood of the closed disk after possibly
shrinking that neighborhood, by compactness and continuity. Reality
of g gives reality of F and its Taylor coefficients. In particular
d_i is real and nonzero, and E is real positive and invertible.

Set B=P/F. It is holomorphic on a neighborhood of the closed disk and
agrees with P^2/g off the two removed zeros. Therefore

    b_fun=z^-2 B, beta_m=0 for m<-2.

For example, on |z|=sigma the Laurent Cauchy bound gives
|beta_m|<=M sigma^-m for m>=0, with
M=max_(|z|=sigma)|b_fun(z)| finite. It follows that the series for h_3
and its derivatives converge locally uniformly on |z|<sigma. All node
values, off-diagonal quotients and diagonal derivatives defining K
are consequently legitimate.

Near zero, g is nonzero. Let B_5=sum_(j=0)^5 c_j z^j be the degree-five
Taylor polynomial of B. Local multiplication, followed by uniqueness
of Taylor coefficients of the canceled B, gives

    c_j=sum_(l=0)^min(4,j) [z^l]P^2 u_(j-l), j=0,...,5.  (3)

This uses only a local inverse at zero. It does not continue that
uncanceled inverse to a root. On the full disk the holomorphic remainder
B-B_5 vanishes to order at least6 at zero. Thus, initially for z!=0,

    T=z^-2 B_5=sum_(m=-2)^3 beta_m z^m,
    h_3=z^-3(b_fun-T)=(B-B_5)/z^5.                      (4)

The right side is removable at zero and has exactly the complete
convergent series defining h_3. No Laurent tail has been truncated in
(4); the finite B_5 is an exact subtraction from the canceled function.

At each node x=alpha_i, differentiation of b_fun=P/(z^2 F) yields

    b_fun(x)=0, b_fun'(x)=P'(x)/(x^2 F(x))=1/d_i.

Let f(z)=-B_5(z)/z^5=-T(z)/z^3, defined away from zero. Equation(4)
therefore gives

    h_3(x)=f(x), h_3'(x)=1/(d_i x^3)+f'(x).

Because x<0,

    (E^-1 J E^-1)_ii=1/(d_i |x|^3)=-1/(d_i x^3).

It follows that M=E^-1 R E^-1 is exactly the two-node divided-difference
matrix of f, including M_ii=f'(alpha_i). This cancels the residue
contribution on the diagonal without dropping it from K. Nonzero
nodes and d_i justify every reciprocal used so far.

**Finite coefficient identification.** Write s=a+b and t=ab, so

    P^2=z^4-2s z^3+(s^2+2t)z^2-2st z+t^2.

For j=0,...,5 let R_j be the contribution to f from coefficient u_j
in (3). Directly retaining the terms of degree at most5 gives

    R_0=-P^2/z^5,
    R_1=-P^2/z^4,
    R_2=-P^2/z^3+z,
    R_3=-P^2/z^2+z^2-2sz,
    R_4=-P^2/z+z^3-2sz^2+(s^2+2t)z,
    R_5=-t^2,
    f=sum_(j=0)^5 u_j R_j.                             (5)

Every term P^2/z^m in (5) has value and derivative zero at both a,b,
since the nodes are nonzero and P^2 has double zeros there. Constant
terms also have zero divided differences and derivatives. Consequently
R_0,R_1,R_5 contribute zero to M. The remaining polynomial terms have
the following exact contributions:

| Coefficient | M_11 | M_12=M_21 | M_22 |
|---|---:|---:|---:|
| u_2 | 1 | 1 | 1 |
| u_3 | -2b | -s | -2a |
| u_4 | b^2 | t | a^2 |

For completeness, the middle row follows from the derivative 2x-2s
and the off-diagonal quotient a+b-2s=-s. For the last row the derivative
is 3x^2-4sx+s^2+2t, equal to b^2 at x=a and a^2 at x=b using
a^2-sa+t=b^2-sb+t=0. Its off-diagonal quotient is
a^2+ab+b^2-2s(a+b)+s^2+2t=t. Thus no special model coefficients
or numerical roots enter the table. We obtain

    M_11=u_2-2b u_3+b^2 u_4,
    M_12=u_2-(a+b)u_3+ab u_4,
    M_22=u_2-2a u_3+a^2 u_4.

Multiplying W H W^T proves (1). Since det(W)=b-a!=0 and E is
positive invertible, the displayed C in (2) exists and satisfies
C^T E W=I and (E W)^T C=I. This proves (2) without any division by
det(H), an entry of H, or det(R). Sylvester's law gives the full
inertia equality, including all singular cases. Explicitly,
R C=C^-T H. Thus H v=0 implies R(C v)=0, and if R y=0, then
H(C^-1 y)=C^T R y=0. The invertible map C therefore carries the
kernel of H bijectively onto the kernel of R. This uses only C^-1,
never an inverse of either form. If H=0, equation(1) also gives R=0.
As a consistency identity,

    det(M)=(a-b)^2 (u_2 u_4-u_3^2).

This determinant identity alone would not prove equality of full inertia;
the explicit congruence is the proof.

**Exact symbolic check and qualifications.** Run

    python3 scripts/reciprocal-quartic/two-root-interface-458.py

The complete certificate is
`scripts/reciprocal-quartic/two-root-interface-458.json`. Its standard-
library arithmetic expands exact formal Laurent polynomials in
a,b,u_0,...,u_5, with integer coefficients and potentially negative
powers only of a,b. It constructs (3) from P^2, then independently
checks both diagonal derivatives, the off-diagonal identity multiplied
by a-b, and the determinant identity. All four expanded residuals are
identically zero; actual nonzero residuals0, required0, no failures.
The complete residual, check and form fields were inspected. The analytic
proof above pays the nonzero denominators and convergence; the script
does not assert or test those analytic hypotheses. SymPy was unavailable;
no dependency was installed, and exact standard-library algebra sufficed.
This is supporting reproducible algebra, not an independent proof audit
or formal verification. There is no model sweep or sign calculation.

The conditional two-root interface is now obtained. Its use for actual
Xi still requires the exact grouping hypotheses and independently paid
sign information for H; global grouping, every required order, and the
other mixed minors remain open. No automatic index conclusion is revived.

**Separate conceptual audit, 2026-11-05, step460.** Reused the approved
`drafts/literature/2026-11-05-two-root-interface-critical-audit.md`.
The complete proof and implementation were inspected. The disk hypothesis
justifies nonvanishing of F on a neighborhood of the closed disk, so the
circle |z|=sigma used for the Laurent bound lies in the analytic domain.
The tail in(4) subtracts exactly the powers beta_-2 through beta_3
from the canceled function. The local inverse supplies coefficients
only at zero; no evaluation of its series at a root occurs. In the
diagonal derivative, the term from differentiating z^-3 b_fun involving
b_fun(x) vanishes, while x^-3 b_fun'(x)=1/(d_i x^3) remains and is
exactly canceled by E^-1 J E^-1. Thus neither a residue nor a tail
has been silently omitted.

Each of the six contributions in(5) was checked against(3): for u_0,u_1
the entire shifted P^2 fits in B_5, for u_2,u_3,u_4 the omitted higher
powers give exactly the displayed polynomial corrections, and for u_5
only t^2 z^5 survives before division by -z^5. Double zeros of P^2
remove both node values and derivatives of the rational parts. The
three polynomial rows consequently give precisely W H W^T. The explicit
inverse transpose W^-T and both identities C^T E W=I and (E W)^T C=I
were checked; the kernel argument above pays nullity in both directions.
No assumption about a sign, rank, nonzero entry or determinant of H or R
is used. Root order is unrestricted: only a!=b matters for W.

All four residual fields and check values, the entire form field,
coefficient construction, excluded analytic hypotheses, failure list
and actual/required residual counts in the existing certificate were
read in full. Exact replay of the displayed command passes 4/4 checks,
with nonzero residuals actual 0, required 0, failures none. The certificate
is byte-for-byte unchanged, SHA256
`2bada4ef37dc69b127248aeb314bd0dc2302618fd721b452b96ab68482ef41b4`.
Its monomial arithmetic was checked against formal Laurent addition,
multiplication, evaluation and differentiation; it is supporting algebra,
not an analytic proof or a Lean verification. No mathematical defect
was found and no theorem hypothesis or conclusion was changed. The
audit reproduces and validates a local conditional input using the cited
standard methods; it establishes no new Xi sign or literature novelty.

## Mathlib

Full matching coverage has not been checked; no presence or absence
claim is made. The informal inputs are the cited Taylor/Laurent and
removable-singularity theorems, divided-difference convention and
Sylvester's law. The explicit two-root identification is proved here;
it is not claimed to be beyond all existing literature.
