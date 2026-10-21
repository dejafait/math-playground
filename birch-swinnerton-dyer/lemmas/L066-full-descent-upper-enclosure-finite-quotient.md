# L066 — Full-descent upper-enclosure certificate for the finite quotient

## Hypotheses

Retain every L026 premise: E/Q is non-CM; p>=5 is good ordinary;
E[p] is surjective; p divides neither #E(F_p), the Manin constant
nor any Tamagawa factor; E(Q_p)[p]=0; a residual Kurihara number in
Sakamoto's N_(1,0) is independently nonzero with the compatible Neron
plus-period and discrete-logarithm conventions; L(E,1)=0; w(E)=+1;
and a_2 in the fixed primitive ordinary cyclotomic series is
independently certified nonzero. Keep its generator and coordinate.
Write D=Sel(Q,E[p^infinity]) and D_div for its maximal divisible
subgroup, as in audited L061. No equality D=D_div is assumed.

Use the full descent algebra and injective cohomology maps described
in audited L065, with the arithmetic evidence specified below. Only
its full-algebra setup and named descent imports are used, not its
localization conclusion or its additional D=D_div premise. The present
certificate concerns an upper bound for all classical Sel_p classes,
rather than membership or nonvanishing of one representative.

The prior IMPORT assessment is
[the approved upper-enclosure scope](../drafts/literature/2026-10-15-full-descent-finite-quotient-upper-enclosure.md).
All arithmetic certificates below are supplied hypotheses. No such
certificate or successful instance has been constructed here.

## Conclusion

A certificate satisfying items 1–5 below gives an injective linear map

\[
\operatorname{Sel}_p(E/\mathbf Q)\longrightarrow V,
\qquad \dim_{\mathbf F_p}V\le2.
\]

Consequently L021's existing finite-quotient criterion, with L026's
corank and L061's coefficient matching, gives

\[
\dim_{\mathbf F_p}\operatorname{Sel}_p(E/\mathbf Q)=2,
\qquad D/D_{\rm div}=0.
\]

This supplies L065's independent e=0 premise if the certificate is
actually produced. It supplies neither an actual class nor successful
localization. Divisible p-primary Sha, rational Kummer membership and
the arbitrary-curve complex-order/rank comparison remain unresolved.
Missing completeness evidence invalidates the certificate; an upper
enclosure of dimension greater than two is inconclusive. There is no
claim that the L026 premises guarantee a bound of two by this method.

## Proof

**Named imports and applicability.** Import Schaefer–Stoll, *How to do
a p-descent on an elliptic curve*, Trans. AMS 356 (2004), 1209–1231,
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X), using exclusively
the numbering of the
[author long version dated 13 June 2001](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf):
Proposition 4.6 (p. 7), Section 5, equation (5.1), algorithm steps 1–8
and its local completeness discussion (pp. 8–10), Proposition 6.4 and
Corollary 7.1 (pp. 12–13), and Corollary 7.9/Proposition 7.10
(pp. 18–19). These provide the finite-place Selmer intersection, full
global unit/class construction, local-image computation, injectivity,
and cohomology-image constraints. Essential proof-case coverage is
reused from the approved assessment; no general algorithm is reproved.
The only assembly below is their applicability and containment,
followed by L021's existing criterion.

Take K=Q, theta=[p], E'=E and the entire Galois-stable set
X=E[p] minus {O}. It spans E[p] and has p^2-1 elements, prime to p.
Thus the full-set global and local injections apply, including when
local Galois orbits are smaller. The origin supplies the base point.
These are precisely L065's audited descent choices; there is no
smaller isogeny or fake Selmer quotient. Write R for the finite etale
algebra of equivariant functions on X, of dimension p^2-1, and R_v for
R tensor Q_v. Denote the imported injections by

\[
\iota:H^1(\mathbf Q,E[p])\hookrightarrow R^*/R^{*p},
\qquad
\iota_v:H^1(\mathbf Q_v,E[p])\hookrightarrow R_v^*/R_v^{*p}.
\]

All power-class groups are written additively as F_p spaces below.
Fix a finite set S of rational finite primes containing p and every
bad prime. Write W=R(S,p): its classes have valuations divisible by p
at every prime of R outside S. This is the finite global group used
by the source; it is not all of R^*/R^{*p}. No equality between W and
the cohomology image is presumed.

**Supplied upper-enclosure certificate.**

1. Supply the full R with its product-of-number-fields description and
   certified torsion-scheme identification, as well as all algebra
   embeddings and local factor identifications used. Use the same
   maps and divisor-evaluation functions as in L065, with their
   divisor identities and Galois compatibility. Any equation change
   must transport these data. Nothing is inferred from a software
   label for the algebra or a subset of the torsion points.

2. Supply a complete finite presentation of W with a certified F_p
   basis w_1,...,w_d and representatives in R^*. For each field factor
   this requires complete S-unit classes modulo p, complete S-class
   group p-torsion and lifts with verified ideal identities, as in
   Section 5's global construction. A certified finite-index S-unit
   subgroup with index prime to p suffices, provided its torsion
   contribution modulo p is retained. Complete p-primary class data
   suffice; unrelated prime-to-p class data are not required. For a
   p-torsion ideal class its lift must include the principal ideal
   identity for its p-th power over the S-integers. Include all field
   factors and all primes over S. Certify spanning and any relations
   used to obtain the stated basis, not merely that the displayed
   elements are units or that some ideal relations hold. Conditional
   unit/class completeness gives only a conditional result with that
   additional assumption, not an unconditional certificate here.

3. Optionally impose any of Corollary 7.9's cohomology-image conditions.
   If imposed, supply their exact matrices on all of W, using the
   identified scalar-action and incidence algebras and Proposition
   7.10's norm maps in faithful power-class coordinates. Denote the
   resulting homogeneous constraint matrix by C. It is also permitted
   to omit some or all of these conditions, taking C to have fewer
   rows or no rows. Such omissions enlarge the enclosure; they do
   not identify its survivors as actual cohomology or Selmer classes.
   Every imposed condition must be a proved necessary condition for
   the full cohomology image.

4. Choose a finite set J of places in S. For every v in J supply a
   faithful finite presentation L_v=R_v^*/R_v^{*p}, the exact
   restriction matrix r_v:W->L_v, and a certified subspace U_v of L_v
   containing the full classical image

   \[
   \iota_v\bigl(\delta_v(E(\mathbf Q_v)/pE(\mathbf Q_v))\bigr).
   \]

   For an exact local-image computation, supply good local divisor
   evaluations with rigorous local arithmetic and enough independent
   images to attain the known full quotient size, as justified by
   Section 5's local completeness test and local injectivity. Then
   their span is the full image and may be used as U_v. Sampled
   evaluations alone give a lower bound and cannot be used as an
   upper bound. Alternatively a separately proved larger U_v is
   permitted; U_v=L_v omits the constraint entirely. Supply exact
   quotient matrices q_v:L_v->L_v/U_v with kernel exactly U_v.
   Local points/divisors, power classes, independence and the claimed
   full size all need evidence; precision labels alone are not such
   evidence. A good rational divisor evaluation includes residue-field
   norms with multiplicities for nonrational support. No global
   rational point is required. Supports must avoid every zero, pole
   and undefined point of the chosen evaluation formulas, including
   any additional exclusions required by their representation.

5. Stack C and all q_v r_v into a matrix M on the entire global
   coordinate space F_p^d. Supply exact finite-field linear algebra
   verifying its rank rho, including witnesses for both rank bounds,
   and require d-rho<=2. Set V=ker M. For example, a nonzero rho-minor
   and a verified factorization of rank at most rho give such
   witnesses; empty and zero-dimensional cases must have correct
   shapes. An exact kernel basis with completeness witnesses is
   another format. A list of two independent survivors is not an
   upper-dimension certificate.

**Containment before dimension.** Let c be any classical Sel_p class.
Since S contains p and all bad primes, the imported unramifiedness
and finite-intersection results put c in H^1(Q,E[p];S). Corollary 7.9
then places iota(c) in W, so item 2 supplies its coordinates on the
entire global basis. No particular c needs to have been produced.
Every imposed global condition is necessary, hence C iota(c)=0.
For each v in J, naturality gives

\[
r_v(\iota(c))=\iota_v(\operatorname{res}_v c)\in U_v,
\]

because c satisfies the classical Kummer condition there. Therefore
q_v r_v iota(c)=0 and iota(c) lies in V. Global injectivity of iota
makes this an injection of Sel_p into V. The argument uses upper
bounds at the local step, not equality inferred from sampled points.

Every omitted condition has the correct direction: finite places in
S outside J, omitted cohomology-image constraints and any enlargement
of U_v can only enlarge V. Outside S the source identifies the good
prime-to-p classical condition with unramifiedness. At the real place
positive-degree p-primary cohomology is zero since p is odd. Thus
nothing omitted invalidates containment; imposing fewer conditions may
only prevent the desired dimension bound. V is not claimed to equal
the Selmer group unless all required conditions are imposed exactly.

Item 5 gives dim V=d-rho<=2, so this is a genuine upper bound for
the entire classical Sel_p, independent of exhibited rational points
or a residual two-prime unit. Complete units/classes and exact
restrictions are arithmetic obligations, not consequences of the
symbolic matrix notation or of citing the descent algorithm.

**Existing finite-quotient handoff.** L026 gives corank D=2 under
exactly the retained premises. Audited L061 supplies finite generation
of D^vee and the natural equality Sel_p(E/Q)=D[p], with all classical
local conditions retained, including local torsion away from p.
L021 applies with S there equal to D here: the arithmetic and residual
hypotheses are unchanged and its corank-two premise has just been
supplied by L026. Its existing formula is

\[
\dim_{\mathbf F_p}\operatorname{Sel}_p(E/\mathbf Q)=2+2t,
\qquad
D/D_{\rm div}\simeq\bigoplus_{j=1}^t
                         (\mathbf Z/p^{a_j}\mathbf Z)^2,
\quad a_j>0.
\]

Apply that criterion to the certified upper bound: t=0 and the
residual dimension is exactly two. This is an application of L021,
not a new dimension lemma or an inference from residual primitivity
alone. In particular D=D_div was not used to certify W, U_v, M or
containment. L065's additional premise becomes available only after
this handoff. No localized nonzero class follows from that equality.

The independent residual-family nonvanishing and nonzero quadratic
coefficient remain supplied L026 premises. Nothing here removes the
possible divisible Sha contribution in L026's rank-plus-corank sum.
ATTEMPTS/021/032/033/034 and their respective stops are preserved.
This conditional known-method import changes no theorem beyond the
checked sources and produces no arithmetic upper bound for a curve.
Its containment/certificate assembly passes the separate critical audit
below under the unchanged supplied-input hypotheses.

**Separate critical audit (2026-10-15).** The
[prior IMPORT scope](../drafts/literature/2026-10-15-full-descent-upper-enclosure-critical-audit.md)
authorizes exactly this audit. No failed implication or new arithmetic
premise was found. Item 4 now spells out the existing good-divisor
qualification; this is not an additional nonvanishing or completeness
assumption. The proof and conclusions remain conditional on every
certificate obligation above. The primary citations and version are
those in the named-import paragraph, whose inspected proof cases are
reused rather than reproved.

The specialization uses theta=[p], its dual [p], and E'=E. The full
X is stable and spanning over Q and every completion, and p does not
divide p^2-1. Proposition 6.4/Corollary 7.1 therefore apply even when
the local Galois action is not surjective. Corollary 7.9 supplies the
unramified intersection and necessary global constraints; Proposition
7.10 fixes the norm map. Section 5 supplies the componentwise unit/class
sequence and local completeness test. Its pp. 9--10 warning requires
avoiding extra undefined points of the chosen function expressions.
L065's audited evaluation setup already retains these qualifications.

Here are the completeness checks for this certificate, with no use of
L065's D=D_div hypothesis. Item 2 requires an isomorphism

\[
b:\mathbf F_p^d\xrightarrow{\sim}W,\qquad e_i\longmapsto w_i,
\]

not a map onto the span of an uncertified collection. In each field
factor the unit contribution includes torsion modulo p; the ideal-class
contribution includes every S-class killed by p and its principal-power
lift. A finite-index unit subgroup is adequate only with the stated
prime-to-p index certificate. The chosen lifts need not split the
unit/class sequence canonically, but they and the units must give the
proved full presentation. Specifying an ideal whose p-th power is
principal does not prove that the listed ideal classes exhaust the
p-torsion. Nor does counting displayed generators establish their
independence. These are explicit requirements of item 2, so no missing
global factor can be excused by a later low kernel dimension.

For item 3, every row is a necessary condition on the same power class
in R. Faithful target coordinates must detect its image on all of W;
an unverified projection cannot impose a valid row. For item 4, put
K_v=iota_v(delta_v(E(Q_v)/pE(Q_v))). A span B_v of good evaluations
initially satisfies B_v subset K_v. It qualifies as U_v only after the
claimed independence and known full size prove B_v=K_v, or after a
separate proof of K_v subset U_v. Thus the test cannot substitute a
sampled lower bound for an upper bound. Nonrational divisor support is
handled by norms and multiplicities, and every formula must be defined
on that support. None of these local witnesses needs to come from a
global rational point. The exact quotient map must have kernel U_v,
not a smaller guessed subspace.

To check containment without assuming the conclusion, take an arbitrary
c in Sel_p. The chosen S includes p and all bad primes, hence includes
every place required by Proposition 4.6. Its unramifiedness conclusion
and Corollary 7.9 give iota(c) in W. There is a unique x=b^{-1}(iota(c)).
The global necessary conditions give Cx=0. Naturality gives, for each
v in J,

\[
r_v(x)=\iota_v(\operatorname{res}_v c)\in K_v\subset U_v,
\qquad q_vr_v(x)=0.
\]

Here r_v denotes the restriction matrix in the b-coordinates, as in
item 4. Thus x lies in ker M. If x=0, then iota(c)=0 and global
injectivity gives c=0. This proves the asserted injection before any
dimension bound. Removing rows, enlarging U_v or omitting a place
preserves every such x. At the omitted real place the cohomology is
both p-primary and killed by two, hence zero. No all-place equality
from Proposition 7.11 is used to justify a finite sampling rule.

The lower rank witness in item 5 proves rank M>=rho; the upper witness
proves rank M<=rho on the full d-dimensional domain. In the suggested
format these are a nonzero rho-minor and a factorization through
F_p^rho. A complete kernel computation is equivalent evidence. Thus
rank-nullity supplies dim V=d-rho, and the asserted threshold is
d-rho<=2. This audit supplies no actual d, rho or matrices. A bound
above two is inconclusive; two exhibited survivors do not certify an
upper bound. Under all the other hypotheses a sound certificate cannot
have d-rho<2, because the following handoff supplies the lower bound.

Finally, all L021 arithmetic and residual premises occur in L026, and
L026's proved conclusion supplies its corank-two premise. In particular,
the independently nonzero residual family and a_2 have not been
replaced by the upper-bound test. Audited L061 gives finite generation
of D^vee and the natural Sel_p=D[p]. Its global H^0(Q,E[p^infinity])
vanishes by residual surjectivity; preimages of the infinite Kummer
conditions are the finite Kummer conditions at every place. No local
H^0 vanishing away from p is needed or asserted. We therefore apply
L021 to this very D, not to a strict, relaxed, isogeny or fake group.
Its existing formula gives

\[
2+2t=\dim_{\mathbf F_p}D[p]
     =\dim_{\mathbf F_p}\operatorname{Sel}_p
     \le d-\rho\le2.
\]

Hence t=0, dim Sel_p=dim V=2, and D/D_div=0. Every operation producing
the upper enclosure precedes this conclusion and uses only L065's
setup, so there is no circular dependence. No Tate-module surjectivity,
point basis, residual two-prime unit or successful localization enters.

The audit validates a conditional known-result application. It neither
constructs its arithmetic certificate nor guarantees that one can
achieve the threshold on the L026 premises alone. Zero finite quotient
does not remove divisible Sha or identify rational Kummer directions;
it supplies L065's independent e=0 premise only upon actual certificate
production. The main arbitrary-curve rank gap and all recorded route
stops remain unchanged. No result beyond the checked sources is claimed.

## Mathlib

Full Schaefer–Stoll global/local descent algorithms, unit/class-group
completeness certification, and the combined arithmetic handoff: not
checked. Supporting finite-field kernels/ranks, Kummer maps and
finite-etale-algebra power classes: not checked. Unknown availability
is not evidence of absence. The named results are imported rather
than reproved; the argument above justifies their specialization,
containment direction and use of the existing L021 criterion.
