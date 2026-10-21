# L064 — Uniform two-row compatibility for the triangle table

## Hypotheses

Use audited L059's fixed field F=F_(97^20), F_0=F_97, order-sixteen
domain H and arbitrary nine distinct triangle labels. Write the three
singleton pairs as Y_0={y_1,y_2}, Z_0={z_1,z_2}, W_0={w_1,w_2},
and P={a,b,c}. The base supports are P's pairs together with Y_0,
Z_0,W_0 as in L057. All normalized weights belong to
G^3=(F_0 minus {0,1})^3. Use the complete L059 table, before deleting
the original infinity scalar, including both-zero projected rows and
zero fourth weights. Let K,L be two distinct four-subsets of H minus P.

For K put u_x=beta_x^Y/c_x and v_x=beta_x^Z/c_x for x in P;
use primes for L. These are L057's label coefficients. Call
(w,mu,nu) compatible if (w,mu,K) and (w,nu,L) are retained table rows,
mu!=nu, and mu,nu belong to F_0 minus {0,-1}.

## Conclusion

There are at most two compatible triples (w,mu,nu) for this fixed
ordered support pair. If either projected row is isolated, there is
at most one. If K and L both contain any one of Y_0,Z_0,W_0,
there are none. These claims are uniform over the nine labels.

The following exact elimination retains every singular case. Impose
each support's projected scalar test, mu,nu!=0,-1, mu!=nu and z=mu nu,
and solve
\[
\begin{split}
 u_c\mu-u'_c\nu&=v_c-v'_c,\\
 v'_b\mu-v_b\nu+(u_b-u'_b)z&=0,\\
 (u_a+v'_a-1)\mu+(1-v_a-u'_a)\nu+(u_a-u'_a)z&=v_a-v'_a.
                                                        \tag{1}
\end{split}
\]
Recover w from either row and retain exactly w in G^3. The resulting
solutions are precisely the compatible triples. No invertibility of
the three-by-three coefficient matrix is assumed.

For any given original chart impose both additional gates
rho-(1-rho)mu!=0 and rho-(1-rho)nu!=0. They only delete solutions.
The bound does not assert that the table has fewer than seven scalars
at a weight point: many different support pairs may meet at one point.
It supplies a finite pair-compatibility restriction, not the twelve
bound, a full M bound, or a global count improvement. A separate critical
audit on 2026-10-12 found no mathematical defect in this fixed-pair
restriction; it assumes none of L060–L063.

## Proof

### Exact weight elimination

L059's complete row formula is
\[
 p=\frac{1-v_a+\mu u_a}{1+\mu},\qquad
 q=u_b-v_b/\mu,\qquad r=v_c-\mu u_c.                 \tag{2}
\]
The primed formula uses nu. Equating r gives the first equation of
(1). Equating q and multiplying by mu nu gives the second. Equating
p and multiplying by (1+mu)(1+nu) gives the third. All multipliers
are nonzero by the scalar gates. Thus these operations are reversible.
Projected conditions and w in G^3 are still required, so L059 proves
the stated equivalence for isolated and both-zero rows alike. The
original finite-chart assertion follows from L059's exact formula.

### A forbidden common singleton pair

Suppose a compatible pair exists. Since its weights and scalars are
rational, choose rho in F minus F_0 and gamma=(0,1,rho), lambda=1.
By L059 and L041 this realizes the gated base errors and both relaxed
recoveries as actual errors at distinct original finite parameters.
Neither extra parameter is a base parameter; no fourth-weight gate is
needed. This auxiliary chart is used to test table compatibility, not
to replace a given original chart.

If K and L contain the same singleton pair B of one base support A_i,
then |K union L|<=6. Since A_i is B plus two labels in P, the union
A_i union K union L has size at most eight. The three errors at their
distinct parameters have a syndrome relation whose three coefficients
are nonzero (take the three pairwise parameter differences). The
corresponding word is in the moment kernel. At either P label of A_i
its coefficient is nonzero: the base weight is nonzero and both other
errors vanish there. It is therefore a nonzero kernel word supported
on at most eight labels, contrary to L010's eight-column independence.
This proves the exclusion, even for relaxed recovered errors.

### Constant coordinates of a both-zero row

Write V_x=(x,x^2,...,x^8)^tr for the moment column. For a both-zero
support K, L057 gives
Y+sum_(x in P) beta_x^Y V_x in span{V_k:k in K},
where Y=sum_(y in Y_0)c_y V_y; likewise for Z.
For any fixed x in P,
\[
 \beta_x^Y=0\quad\Longleftrightarrow\quad Y_0\subseteq K.
                                                        \tag{3}
\]
Indeed, if that coefficient is zero and a y label is outside K, the
displayed relation is nonzero on that label and is supported on
Y_0 union (P minus {x}) union K, of size at most eight. This contradicts
eight-column independence. Conversely, Y_0 contained in K makes
the Y recurrence zero, and independence of the three restored columns
forces all beta^Y to vanish. The same proof applies to Z.

Let W=sum_(w in W_0)c_w V_w. L041's moment-kernel identity for Q gives
Y+Z+W+sum_(x in P)c_x V_x=0. Thus W is also in span{V_x:x in P union K},
with restored coefficients
beta_x^W=c_x-beta_x^Y-beta_x^Z. The proof of (3) also applies to W.
Consequently the following are exact, including zeros:
\[
 u_c=0\iff Y_0\subseteq K,\qquad
 v_b=0\iff Z_0\subseteq K,\qquad
 u_a+v_a=1\iff W_0\subseteq K.                         \tag{4}
\]
A both-zero support containing Y_0 and Z_0 has beta^Y=beta^Z=0,
so (2) forces q=r=0 and has no gated row. In particular, if u_c=0
and a gated row exists, then v_b!=0. Statements (3)–(4) are only
used for both-zero rows, where the separate full restored systems exist.

### All two-row cases

If either row is isolated, its scalar is fixed by the projected test.
Formula (2) fixes w. L057 supplies at most one eligible scalar for
the other support at that w, including its both-zero pivot case.
Thus there is at most one compatible triple. Rows whose projected
tests reject contribute nothing. It remains to treat two both-zero rows.

If u_c=u'_c=0, (4) puts Y_0 in both supports, already excluded.
If u_c=0 and u'_c!=0, the r equation fixes nu. Any gated row has
v_b!=0, so the q equation q=u_b-v_b/mu then fixes mu uniquely.
The case u'_c=0 and u_c!=0 is the same argument with the two supports
interchanged. These cases have at most one compatible triple.

Now u_c u'_c!=0. Put
\[
 A=u_c/u'_c\ne0,\quad B=(v'_c-v_c)/u'_c,\quad
 \nu=A\mu+B.                                         \tag{5}
\]
Substitution into the last two equations of (1) yields the polynomials
\[
\begin{split}
 Q_2(X)&=(u_b-u'_b)X(AX+B)-v_b(AX+B)+v'_b X,\\
 P_2(X)&=(u_a-u'_a)X(AX+B)+(u_a+v'_a-1)X\\
       &\qquad +(1-v_a-u'_a)(AX+B)+v'_a-v_a.
                                                        \tag{6}
\end{split}
\]
Both have degree at most two. If either is a nonzero polynomial,
its at most two field roots bound compatible triples: each mu determines
nu by (5) and w by (2). No assertion about splitting is required.

It remains essential to handle Q_2=P_2=0 identically. The quadratic
coefficient of Q_2 gives u_b=u'_b since A!=0. Its other coefficients
then give v'_b=A v_b and v_b B=0. If v_b=0, then v'_b=0, so (4)
puts Z_0 in both supports and excludes any compatible pair. Otherwise
B=0. The quadratic and constant coefficients of P_2 now give
u_a=u'_a and v_a=v'_a. Its linear coefficient becomes
(1-A)(u_a+v_a-1)=0. If A=1, (5) forces nu=mu, which is excluded.
If A!=1, (4) puts W_0 in both supports, again excluded. Thus the
identically-zero branch has no compatible triples. This completes
every case and proves the bound two.

### Source reuse and limitations

The pre-existing EXPLORE assessment
`drafts/literature/2026-10-10-triangle-twelve-recovery-bound.md` covers
this bounded simultaneous-recovery restriction under the unchanged
triangle target. The recurrence is imported through audited L057 from
Przemek Chojecki, *Shortening Bounds for Reed–Solomon MCA*, live author
TeX v9.2, July 17, 2026, DR2 and DR6–DRC, lines 2785–2935 of the
[author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
Its unchanged specialization has R=8,t=4, distinct labels, multiplier x
and eta_j=s_(j+1); the mutable source is not identified with ePrint
2026/1463. No recurrence theorem is reproved. L041 supplies the actual
base triples and kernel word Q, L010 supplies column independence, and
L059 supplies the table and nonprime-chart realization. The new work is
the simultaneous elementary elimination and its complete degeneracy
analysis. The inspected literature does not certify originality.

An algorithm may now enumerate compatible pairs through (1), using
the case analysis (4)–(6) for both-zero rows, without dropping a
singular coefficient matrix or searching all G^3. A seven-scalar fiber
would require compatible pairs for every two of its seven distinct
support witnesses. Nothing here bounds how many pair solutions share
one w. No such compatibility graph, seven-row exclusion or full M
test was computed in this step.

### Separate critical audit (2026-10-12)

The audit reused the exact EXPLORE coverage in
`drafts/literature/2026-10-12-triangle-two-row-critical-audit.md` and
checked the full argument against the relevant L010/L041/L057/L059
proofs. No formula, hypothesis, bound or direct mathematical input
required repair. The normalized weights here are rational; no assertion
for arbitrary normalized extension-field weights is added. The actual
base-error factors lambda/alpha_i and original finite chart remain
unrestricted in F.

**Reversible equations and counting unit.** For r, equality in (2) is
exactly the first row of (1). For q, its difference multiplied by
mu nu is
(u_b-u'_b)mu nu-v_b nu+v'_b mu. For p, cross multiplication gives
\[
 (v'_a-v_a)+(u_a+v'_a-1)\mu
 +(1-v_a-u'_a)\nu+(u_a-u'_a)\mu\nu=0.
\]
These are precisely the remaining two rows, since mu,nu,1+mu,1+nu
are all nonzero. The auxiliary variable z is still constrained to
mu nu. Conversely each solution passing both projected tests and G^3
recovers the same unique w from both formulas. L059's table equivalence
then provides both actual lifted rows, including a nonzero pivot for
each successful both-zero system. Rejected projected cases supply none.
No rank assumption on the displayed linear system in mu,nu,z is used.

**Auxiliary and original finite charts.** Choose rho outside F_97,
gamma=(0,1,rho), lambda=1 only to realize a putative table pair in a
single auxiliary pencil through L041's local converse. This invokes no
sixteen-count premise. For every rational eligible scalar mu, E(mu)=0
would imply rho=mu/(1+mu) in F_97, a contradiction. In any original
chart with the gates retained,
\[
 T(\mu)-T(\nu)=
 \frac{g\rho(1-\rho)(\mu-\nu)}{E(\mu)E(\nu)}\ne0.
\]
Moreover T(mu) differs from gamma_0 because g rho/E(mu) is nonzero;
T(mu)=gamma_1 would imply mu=0, and T(mu)=gamma_2 would imply mu=-1.
Thus the auxiliary construction yields distinct actual finite errors
away from all three base parameters. For a given original pencil,
both E gates remain necessary and only delete compatible triples.
The proof does not change that pencil's chart.

If K,L share singleton pair B belonging to A_i, then
|K union L|<=6 and |A_i union K union L|<=8. With the actual recovered
parameters T,T', the word
\[
 (T-T')e_i+(T'-\gamma_i)e_K+(\gamma_i-T)e_L
\]
has zero moment: the three coefficients and their parameter-weighted
sum both vanish. At either P label of A_i its entry is
(T-T')e_i(x), nonzero. All three coefficients are nonzero, and no
coefficient of e_K or e_L is required to be nonzero. L010's independence
of at most eight columns contradicts this word. This is the same
common-pair mechanism already audited in L065, not a new input from it.

**Both-zero constant coordinates.** L057 supplies the separate full
restored Y and Z systems only in the both-zero branch. If beta_x^Y=0
but a y label is outside K, the resulting nonzero relation is on
Y_0 union (P minus {x}) union K, at most eight labels; its coefficient
at that y is c_y!=0. Conversely Y_0 contained in K puts Y itself in
the K span. Independence of the seven columns on P union K forces
every restored beta^Y to vanish. The same proof applies to Z.
Since the degree-seven word Q is in the moment kernel,
W+sum_(x in P)(c_x-beta_x^Y-beta_x^Z)V_x equals
minus the two restored Y,Z vectors. It is in the K span, so the same
argument applies to W. This proves all three iff statements in (4),
including their zero cases. No individual full system is assumed for
an isolated row. If both Y_0 and Z_0 lie in K, all beta^Y,beta^Z
vanish and q=r=0, outside G^3.

**Complete scalar case split.** An isolated row fixes its scalar and
then w. At that w, L057's pivot theorem fixes at most one scalar for
the other support, even if it is both-zero. If both rows are both-zero
and u_c=u'_c=0, they share Y_0 and cannot coexist. If only u_c vanishes,
the first equation fixes nu; any gated K has v_b!=0 by the preceding
iff argument, so q=u_b-v_b/mu fixes at most one mu. Swapping the
supports proves the remaining one-zero case without dividing by zero.

Otherwise A!=0 in (5), so substitution gives exactly (6). If either
polynomial is nonzero, the degree-at-most-two root bound permits at
most two mu, each fixing nu and w; linear and nonzero constant cases
are included. The supporting standard result is J. Thaler,
*Proofs, Arguments, and Zero-Knowledge*, July 18, 2023 manuscript,
Fact 2.2, printed p. 16 of the
[author manuscript](https://people.cs.georgetown.edu/jthaler/ProofsArgsAndZK.pdf),
as inspected in the reused coverage. It applies over F_97 and needs
no splitting hypothesis. The zero polynomial is handled separately.

If both polynomials vanish identically, Q_2's coefficients are
\[
 A(u_b-u'_b)=0,\quad B(u_b-u'_b)-A v_b+v'_b=0,
 \quad -B v_b=0.
\]
They force u_b=u'_b, v'_b=A v_b, and B v_b=0. If v_b=0,
then v'_b=0 and both supports contain Z_0, already forbidden.
If v_b!=0, then B=0. Now P_2's quadratic and constant coefficients
force u_a=u'_a and v_a=v'_a; its remaining coefficient is
(1-A)(u_a+v_a-1). For A=1, nu=mu violates distinctness. For A!=1,
both supports contain W_0 by (4), again forbidden. This exhausts
every polynomial-identity and zero-leading-coefficient branch.

The audit validates only the existing fixed-ordered-pair count. It
does not bound the number of different supports compatible at one w,
prove a seven-scalar exclusion, or resolve a full M count. No new
enumeration, certificate replay or mathematical script is needed for
this uniform algebraic proof; no new source-overlap or originality
claim is made.

## Mathlib

Full matching theorem: **not checked**. Supporting finite-field,
Vandermonde independence, polynomial root bounds and elimination
coverage: **not checked** in this step. No absence claim or Lean
verification is asserted.
