# L011 — Persistent-root pencils have at most twelve bad parameters

## Hypotheses

Let F=F_(97^20), let H be the order-sixteen subgroup of F_97^*, and let
\[
 C=\{(p(x))_{x\in H}:p\in F[X],\ \deg p<8\}.
\]
Fix arbitrary a,b in F^H. Use the event in
[the pinned affine-line model](../foundations/02-pinned-affine-line-model.md)
at 1/4<=delta<5/16; its agreement supports have size at least twelve.
Write B(a,b) for the original bad-parameter set.

Use the eight moments, determinant D(T), and locator L(T,X) defined
in L010. Assume D is a nonzero polynomial and that some fixed x_0 in H
satisfies L(T,x_0)=0 identically. Other coordinate locators may also
vanish identically, and individual values D(gamma)=0 are allowed.

Let H'=H minus {x_0}, let C'=C|_(H'), and let a',b' be the punctured
inputs. Write B'(a',b') for the pinned support event for C' at radius
3/15, so its supports also have size at least twelve. Smoothness of
this auxiliary domain is not assumed.

## Conclusion

Every parameter decodable in the original four-error cell is decodable
with at most three errors in C'. For the original bad set there is a
dichotomy:

1. B(a,b) is contained in B'(a',b'), and |B(a,b)|<=12; or
2. there are c_a,c_b in C for which the union of the supports of
   a-c_a and b-c_b has size at most four, and |B(a,b)|<=4.

The alternatives need not be exclusive. In particular,
\[
 |B(a,b)|\le12<15,\qquad |B(a,b)|/97^{20}\le2^{-128}.
\]
This covers only the stated persistent-root class. It does not give a
global bound for all pairs, settle nonpersistent sixteen-count equality,
treat D identically zero, or identify the pinned event with July ABF26.

## Proof

### Imported punctured-code bound and its applicability

Puncturing gives the ordinary length-15, dimension-8 RS code on H'.
This is the standard puncturing description in J. I. Hall,
[Notes on Coding Theory, Modifying Codes](https://users.math.msu.edu/users/halljo/classes/codenotes/Mod.pdf),
§6.1.2 and Theorem 6.2.1. Only coordinate restriction is used here;
no decoder based on unadjusted dual multipliers is asserted. The minimum
distance of C' is eight, and interpolation on any eight coordinates
is injective. All inputs and interpolating coefficients lie in F.

Import Ben-Sasson, Carmon, Haböck, Kopparty and Saraf,
[On Proximity Gaps for Reed–Solomon Codes](https://www.math.toronto.edu/swastik/rs-proximity-gaps-2025.pdf),
author manuscript dated November 11, 2025, Theorem 1.3 (printed p. 8)
and its common-affine-family conclusion in §2.3 (pp. 20–21).
For degree at most d on n' points, put Delta=1-d/n'. At radius
eta in [Delta/3,Delta/2-1/n'], a set of m close parameters with
\[
 m\ge\frac{\Delta-\eta}{\eta(\Delta-2\eta)}
\]
gives joint distance at most m*eta/(m-1) for the two inputs: there
are codewords c_a',c_b' whose residual inputs have a common support
of at most n'*m*eta/(m-1) coordinates. This is a cited proximity
input, not a theorem reproved here.

Here n'=15, d=7, eta=3/15=1/5, and Delta=8/15. Thus
\[
 \Delta/3=8/45\le1/5=\Delta/2-1/15,
 \qquad
 \frac{\Delta-\eta}{\eta(\Delta-2\eta)}=25/2.
\]
If thirteen parameters were bad for C', they would all be close.
The imported theorem would then give residual inputs supported on
at most floor(13*3/12)=3 common coordinates.

For completeness, the necessary same-support applicability argument
is as follows. For any code of minimum distance greater than 2r,
suppose residual inputs u,v are supported on a common set J of size
at most r. Replacing inputs by residuals preserves the support event.
At a bad parameter t, let c agree with u+t*v on a witnessing support
S of size at least n-r. The word u+t*v is already r-sparse; hence c
has weight at most 2r and must be zero. Thus u+t*v vanishes on S.
Input failure is equivalent to v|_S not belonging to the restricted
code, so v_y!=0 for some y in S. Necessarily y lies in J and
u_y+t*v_y=0. Each such coordinate supplies at most one parameter,
and there are at most r coordinates. The original same-support bad
count is therefore at most r, even if every parameter is decodable.

Apply this argument with r=3 and distance eight. The thirteen presumed
bad parameters would lie in a bad set of size at most three, a
contradiction. Consequently |B'(a',b')|<=12. This application agrees
with Chojecki's July 17, 2026-dated
[author TeX](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
`thm:literature-integral-completion`, LC1–LC2: R'=15-8=7,
3r'=9>=R'+1, 2r'=6<R', and
floor(max{15*(8-3)/(3*(8-6)),4})=12. That formula is a matching
auxiliary bound; BCHKS supplies the primary theorem used above.
Neither cited statement is a match for the original persistent-root transfer.

### All original decoded parameters remain three-error close

The kernel and Vandermonde identities in L010's proof hold without
its nonvanishing assumptions on the coordinate locators. In particular,
an original error representative e of weight at most four is unique,
because C has minimum distance nine. At weight exactly four, with
support A, that proof's identities (4)–(5) give
\[
 D(t)\ne0,\qquad L(t,X)=D(t)\prod_{y\in A}(X-y).
\]
These are algebraic identities for that representative, not an
application of L010's full theorem under violated hypotheses.
Since L(t,x_0)=0, every such four-error A contains x_0.
Deleting x_0 leaves three errors. If D(t)=0 at a decodable parameter,
the representative instead has weight at most three, so deleting
x_0 still leaves at most three errors. This includes every singular
bad parameter without assuming it uses the persistent coordinate.

### Transfer of failure or a fixed four-coordinate family

For an original bad parameter t, let e=a+t*b-c be its unique
representative, put A=supp(e), and let S=H minus A. Any original
witnessing support is contained in S. Since failure on a subset
persists when that subset is enlarged, b|_S is not in C|_S.
Here failure of either input is equivalent to failure of b, as the
combination is a code restriction.

Put S'=S minus {x_0}. If |A|=4, then x_0 is in A, so S'=S has
size twelve. If |A|<=3, S' has size at least twelve as well.
The punctured combination is in C'|_(S'). If b'|_(S') is not in
C'|_(S'), this very support witnesses t in B'(a',b'). This treats
both whether x_0 was an error and whether it was an agreement point.

Suppose instead that input failure disappears on S'. If x_0 were
not in S, the two restrictions and their codes would be identical,
so this is possible only when x_0 is in S. Choose p of degree less
than eight agreeing with b on S', and write c=ev(f). Then
\[
 v=b-\operatorname{ev}(p),\qquad
 u=a-\operatorname{ev}(f-tp)
\]
are both supported on J=A union {x_0}, of size at most four.
Thus one failed transfer supplies a fixed four-coordinate residual
family for the entire pair; it is not a separate exception to add
to the punctured count. Applying the preceding same-support argument
with r=4 and the original distance nine bounds the entire B(a,b)
by four. The nonzero D hypothesis additionally forces |J|=4:
a family supported on at most three coordinates would have Hankel
rank at most three over F(T), making D the zero polynomial.

If there is no failed transfer, every original bad parameter belongs
to B'(a',b'), whose imported bound is twelve. These two cases prove
the dichotomy and |B(a,b)|<=12. Only one persistent coordinate was
selected; any additional persistent roots impose no extra assumption.
Finally 15*2^128<=97^20<16*2^128 gives the claimed budget comparison.

The auxiliary command `python3 scripts/persistent-root/check.py`
tests the original and punctured support events independently over
F_97. A fixed four-coordinate family has all 97 parameters close,
four original bad parameters, and one failure lost at the removed
coordinate. A confluent-moment pencil has multiple persistent roots
and a singular bad parameter whose error omits the removed coordinate;
it tests the other transfer case. Codeword translations are included.
These checks validate the support reasoning, not an enumeration over
F_(97^20); the cited theorem and proof allow arbitrary extension-field inputs.

## Mathlib

Full persistent-root count and transfer: **not checked**. Supporting
RS puncturing, Vandermonde, unique-decoding and joint-proximity coverage
in Mathlib: **not checked**. No matching Mathlib theorem or formal
verification is claimed. The named primary citations cover the
punctured code and proximity input; they do not cover the full transfer.

The pinned ArkLib declarations
[`CoreDefinitions.IsMCA` and `CoreDefinitions.mcaError`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/ProximityGenerators.lean#L98)
support the event definition only. ArkLib is separate from Mathlib,
and these declarations do not certify correspondence with July ABF26.
The auxiliary bound is known; the full specialization is potentially
beyond the checked source statements, with no claim of established originality.
