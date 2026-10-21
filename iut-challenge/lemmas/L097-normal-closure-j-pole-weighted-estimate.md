# L097 — Normal closure preserves the explicit j-pole weighted allowance

## Hypotheses

Fix any survivor E/Q of audited L089, with its same c,h,d_*,e_*,
both fixed domains and algebraic closure. Retain audited L090's
six full-coordinate ordered-root Legendre models and embedded fields

    T=Q(E[2])=Q(t_o),
    G_o=T(iota,E_o[15]), iota^2=-1, C_o=G_o^nor.

Normal closure is over Q. All torsion fields contain both coordinates
of all geometric torsion points. Use the conclusions of audited
L094, L095 and L096 at every actual extending pair w|v of C_o/T.
No native initial theta-data or selected-support identification is
assumed. In particular C_o is not asserted to satisfy the native
exact-generation prescription.

Put S={p : v_p(j(E))<0}, with v_p(p)=1. The same nonzero rational
j(E) is used for all six models, so S is a finite set of rational
primes. For a number field L and each finite place z over p write

    e_z=e(L_z/Q_p), f_z=[k_z:F_p],
    Different_(L_z/Q_p)=m_z^(a_z), d_p(L_z)=a_z/e_z.

Define, with natural logarithms,

    D(L)=[L:Q]^(-1) sum_(z finite) a_z f_z log(p_z),
    R_S(L)=[L:Q]^(-1) sum_(z finite, p_z in S) f_z log(p_z).

Thus R_S uses the complete inverse image of S with coefficient one
at each place; it is a reduced divisor, not a pullback with
ramification multiplicities. D uses the absolute different, not the
relative different of C_o/T. These sums are finite: the absolute
different is supported at the finitely many primes dividing the
number-field discriminant, and S is finite.

## Conclusion

For every such survivor and every ordering o,

    D(C_o)+R_S(C_o)
      <= D(T)+R_S(T)+log(2^11*3^3*5^2).

This is a known-method specialization (REPRODUCTION), with no
sharpness claim. It closes the explicit-support weighted assembly,
not the native support, exact generation or complete repair questions.
The original finite B>=A gap remains open. The separate step388
critical audit below validates this specialization at its stated scope.

## Proof

### Imports, scope and bounded test

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-21-normal-closure-j-pole-weighted-estimate.md`.
Its checked scope is exactly the displayed conclusion. The scoped
duplicate check found the local inputs and source definitions, but
no prior proof of this weighted specialization. ATTEMPTS/035's source
authentication/repeated-approval route is not reopened.

Import the following assessed results without reproof:

- Mochizuki, *Inter-universal Teichmuller Theory IV*, April 2020
  [inspected reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf),
  Proposition 1.3(i), printed pp.11–12, including the tame equality:
  for a finite tame extension L/K of finite extensions of Q_p,

      d_p(L)-d_p(K)=1/e(K/Q_p)-1/e(L/Q_p).

  The absolute normalization is v_p(p)=1. Unramified extensions
  are included. The assessment records inspection of the statement
  and full proof. The upper estimates from Proposition 1.3(ii)
  have already been specialized in L094–L095.
- Milne, *Algebraic Number Theory*, v3.08 (19 July 2020),
  [Proposition 8.2 and proof, printed p.136](https://www.jmilne.org/math/CourseNotes/ANTc.pdf):
  for a finite separable number-field extension L/K and a place v,
  L tensor_K K_v is the product of the actual L_w for w|v.
  Taking dimensions gives sum_(w|v)[L_w:K_v]=[L:K]. All number
  fields here have characteristic zero, so separability holds.

The standard local degree identity [K:Q_p]=e_K f_K and ramification
tower identity are used with these actual places. The assessment
also fixes the translation from IV Definition 1.9, pp.21–22,
and Theorem 1.10(ii), pp.23–24, to the displayed definitions.
No theorem about native selected support is imported or claimed.

The main gap is original finite B>=A. This intermediate bound tests
whether normal closure preserves the stated numerical allowance on
full rational j-pole support. The continuation test is the exact
constant with every place and all four prime/support cases included;
a failed term or hypothesis must be isolated without enlarging it.
That test passes as follows.

### Completion weights and exact regrouping

Fix one survivor and ordering, and abbreviate C=C_o. For each finite
place z of any number field L above p define

    lambda_(L,z)=[L_z:Q_p]/[L:Q]=e_z f_z/[L:Q].

Applying Milne 8.2 to L/Q at p gives sum_(z|p)lambda_(L,z)=1.
Let s_p be one if p belongs to S and zero otherwise, and put

    F_(L,z)=d_p(L_z)+s_p/e_z.

The definitions imply exactly

    D(L)+R_S(L)
      =sum_p log(p) sum_(z|p) lambda_(L,z) F_(L,z),

since lambda_(L,z)d_p(L_z)=a_z f_z/[L:Q] and
lambda_(L,z)s_p/e_z=s_p f_z/[L:Q].

For an actual base place v|p of T, apply Milne 8.2 to C/T at v.
The local and global degree towers give

    sum_(w|v)lambda_(C,w)
      =([T_v:Q_p]/[C:Q]) sum_(w|v)[C_w:T_v]
      =[T_v:Q_p]/[T:Q]=lambda_(T,v).

This is a sum over every actual extending w, without an assumption
that their degrees agree. Consequently the exact coefficient at p
in the difference of the two global quantities is

    Delta_p=sum_(v|p) sum_(w|v) lambda_(C,w)
      * (d_p(C_w)-d_p(T_v)+s_p(1/e_w-1/e_v)).

Here e_v=e(T_v/Q_p), e_w=e(C_w/Q_p). Their tower relation is
e_w=e(C_w/T_v)e_v, and both are positive integers. The support
indicator is the same at v and w because S is fixed over Q.

### All four prime/support cases

First let p be outside {2,3,5} and belong to S. L096 makes every
C_w/T_v tame. The imported tame equality gives

    d_p(C_w)-d_p(T_v)+(1/e_w-1/e_v)=0.

Thus every summand of Delta_p vanishes in this case.

Next let p be outside {2,3,5} and outside S. Then the rational
j(E) has v_p(j(E))>=0. L096 makes every C_w/T_v unramified, so
e_w=e_v and the same tame equality gives d_p(C_w)=d_p(T_v).
Both reduced terms are absent. Every summand again vanishes.
In particular Delta_p=0 at every prime outside {2,3,5}, including
primes where T/Q itself is ramified.

For the two remaining cases let p belong to {2,3,5}, and set

    b_2=10, b_3=2, b_5=1.

L094 at two and L095 at three and five give, for every actual w|v,

    d_p(C_w)-d_p(T_v)<=b_p+1/e_v.

If p belongs to S, add the reduced-term difference to obtain

    d_p(C_w)-d_p(T_v)+1/e_w-1/e_v
      <=b_p+1/e_w<=b_p+1.

If p is outside S, the reduced terms are both zero and instead

    d_p(C_w)-d_p(T_v)<=b_p+1/e_v<=b_p+1.

These estimates require no small-prime good reduction or tameness
assumption. Using nonnegative weights and their total sum one at p,
both support cases give Delta_p<=b_p+1.

### Global bound and qualifications

All sums above are finite. Substituting the four cases into the
exact regrouping yields

    D(C)+R_S(C)-D(T)-R_S(T)
      =sum_p Delta_p log(p)
      <=11 log(2)+3 log(3)+2 log(5)
      =log(2^11*3^3*5^2),

as required. The survivor and ordering were arbitrary; the local
inputs hold at every actual place for each of them. No new general
different or completion theorem has been reproved.

The full-support cancellation is essential to this proof. It does
not identify S with native selected support or apply a native
initial-data theorem to C. L092's factor-four relative degree excess
is untouched; exact field generation after normal closure and a
complete repair remain separate. April-reproduction authentication/
current-version and the def= boundary, the height-selected prime,
independent initial data, native input/action/factorization/pilot,
essentiality and original finite B>=A remain unresolved. This is
local progress using checked known methods, with no claimed advance
beyond those sources and no complete-solution candidate.

### Separate critical audit — 2026-10-21, step388

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-21-normal-closure-weighted-estimate-critical-audit.md`.
The complete proof above was checked against the hypotheses,
conclusions and relevant audited applications in L090 and L094–L096.
The precise primary imports above are reused from step385's inspected
readings; no new authentication or general theorem reproof is claimed.

**Fields, support and quantifiers.** L090 constructs finite embedded
fields T subset G_o subset C_o for an arbitrary L089 survivor and
ordering. Its actual pointed geometric comparison identifies j(E_o)
with the same rational j(E); its formula gives 0<j(E)<1728. Thus S
is precisely the finite set of prime divisors of the denominator of
this nonzero rational number in lowest terms. L094 and L095 concern
these same C_o and T at every actual place above their respective
small primes. L096 concerns these same fields at every remaining
prime, and its integral-j clause uses this same rational invariant.
No selected completion, older witness or assumed native initial data
is needed to invoke any of these conclusions.

**Independent normalization check.** Write n=[C:T], m=[T:Q] and
n_(w/v)=[C_w:T_v] for each actual extending pair. The local tower
and [K:Q_p]=e_K f_K give

    e_w f_w=n_(w/v)e_v f_v,
    lambda_(C,w)=n_(w/v)e_v f_v/(nm).

Milne 8.2 applies to the characteristic-zero separable extension
C/T and yields sum_(w|v)n_(w/v)=n. Hence

    sum_(w|v)lambda_(C,w)=e_v f_v/m=lambda_(T,v).

Applying the same theorem to T/Q gives sum_(v|p)e_v f_v=m,
so the weights at each rational prime have total mass one.
The argument uses all actual extending places; neither Galoisness
nor equality of their degrees is needed for this regrouping.

For the absolute different ideal m_z^(a_z), the valuation of a
uniformizer is 1/e_z. Consequently the source's absolute order is
a_z/e_z, and multiplying it by lambda_(L,z) gives exactly
a_z f_z/[L:Q]. The reduced divisor's coefficient one instead gives
lambda_(L,z)/e_z=f_z/[L:Q]. In particular its contribution is not
lambda_(L,z), which would insert an extra ramification multiplicity.
Both coefficients use the absolute index over Q_p, not e(C_w/T_v).
Since support is the full inverse image of rational S, the same s_p
appears for each w and its v. Subtraction using the preceding weight
identity proves exactly the displayed Delta_p formula in the proof.
There is no missing field-degree multiplier or residue-degree factor.

**Complete local test.** Put

    H_(w/v)=d_p(C_w)-d_p(T_v)+s_p(1/e_w-1/e_v).

The following four checks use the same absolute valuations throughout.

| Prime/support case | Input and exact local test | Bound on H_(w/v) |
| --- | --- | --- |
| p outside {2,3,5}, p in S | L096 gives tame C_w/T_v; IV 1.3(i) gives d_p(C_w)-d_p(T_v)=1/e_v-1/e_w. | 0 |
| p outside {2,3,5}, p outside S | L096 gives unramified C_w/T_v; the relative index is one, so e_w=e_v and IV 1.3(i) gives equal absolute different orders. | 0 |
| p in {2,3,5}, p in S | L094/L095 give d_p(C_w)-d_p(T_v)<=b_p+1/e_v; adding the reduced difference cancels the base reciprocal. | b_p+1/e_w<=b_p+1 |
| p in {2,3,5}, p outside S | Both reduced coefficients vanish; L094/L095 apply directly. | b_p+1/e_v<=b_p+1 |

Here (b_2,b_3,b_5)=(10,2,1). Both reciprocal bounds follow from
positive integral absolute ramification indices. The tame case does
not require T_v/Q_p to be tame; the unramified case does not require
its absolute different to vanish. At small primes no reduction or
tameness premise is added. Local degree one is allowed in every
case. The four rows exhaust all finite places.

**Finite assembly and verdict.** For each fixed survivor, the primes
supporting either absolute different or S form one finite set. Each
has finitely many places in these finite number fields. Thus all
regroupings and subtractions are finite operations; there is no
interchange of infinite sums or requirement of a uniform finite
support across the infinite family. Nonnegative weights of total
mass one give Delta_p=0 outside {2,3,5} and, respectively,
Delta_2<=11, Delta_3<=3, Delta_5<=2. Multiplication by positive
log(p) and finite summation give precisely log(2^11*3^3*5^2),
the required allowance. No constant is enlarged and no equality
or sharpness claim follows from the small-prime upper estimates.

The audit passes without a mathematical correction or new theorem.
It certifies the existing known-method application, not progress
beyond the checked sources. Direct mathematical inputs remain L090,
L094,L095,L096; L089 and the local degree calculations are inherited
through those inputs. L092 is mentioned only as a preserved independent
obstruction, not used to redo a local bound in this assembly. The DAG
therefore needs no change. This audit supersedes the pending-audit
wording for L097 in the unchanged overview; the argument is unchanged.

Native selected support has not been identified with S. Normal closure
still does not meet the asserted exact-generation prescription merely
by passing this bound; L092's factor-four relative excess persists.
The April reproduction/current-version qualification, def= boundary,
height-selected prime, independent initial data, native input/action/
factorization/pilot and essentiality remain unresolved. Original
finite B>=A is open and there is no complete-solution candidate.

## Mathlib

Full matching and supporting coverage have not been checked. Unknown
availability is not absence. This is an informal application of the
precisely cited different and completion results; no formal
verification or numerical certificate is claimed.
