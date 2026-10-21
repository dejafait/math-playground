# L048 — A shared outside label of two d-tag recoveries lies in W

## Hypotheses

Use the full gated tau=1 local setup of L043 over F=F_(97^20),
with H of order sixteen in F_97, k=8 and the pinned radius cell.
In particular the nine distinct labels give

    A_0={h,d,y_1,y_2}, A_1={h,d,z_1,z_2}, A_2={h,w_1,w_2,w_3},
    B={h,d,y_1,y_2,z_1,z_2}, O=H minus B,
    W(X)=product_(i=1)^3(X-w_i),
    Y_2(X)=(X-y_1)(X-y_2), Z_2(X)=(X-z_1)(X-z_2).

Retain distinct original finite gamma_i, lambda!=0,
p*q*(1-p-q)*r*(1-r)!=0, arbitrary extension-field weights and chart,
and every quotient and finite-parameter gate of L043 (4)–(7).
Consider two distinct nonuniversal candidate parameters, different
from the stipulated parameters, with witnesses

    K={d} union S, K'={d} union S', S,S' subsets of O, |S|=|S'|=3,

and quotient scalars mu,nu. Thus mu,nu are nonzero prime-field scalars,
neither is -1, E(mu),E(nu) are nonzero, and mu!=nu. The recovered
fourth weights may vanish: L043 (9) is not a hypothesis. No twelve
count, equality, rational original chart or finite universal lift is
assumed.

## Conclusion

The outside triples meet in at most one label. If S intersect S'={s},
then s is one of w_1,w_2,w_3. Moreover the three pairs

    S minus {s}, S' minus {s}, {w_1,w_2,w_3} minus {s}

are pairwise disjoint. Consequently K,K',A_2 have union nine, common
intersection {s}, and their only double-only label is d. If both
candidate errors have full recovered weights, these are three actual
full four-error supports at distinct original finite parameters in
the tau=1 pattern (2,2,3), with common label s and double-only label d.

There are also exact quadratic identities. Write f and f' for the
monic cubics with roots S and S'. L046's five-value equations give
nonzero u,u' such that

    a_x(mu) f(x)=u W(x), a_x(nu) f'(x)=u' W(x), x in B minus {d},
    a_yi(t)=-t, a_zi(t)=1, a_h(t)=q-p*t.

There exist nonzero a,v in F such that, when S intersect S'={s},

    f(X)/u  =(X-s)*(v Y_2(X)-a nu Z_2(X))/(mu-nu),       (1)
    f'(X)/u'=(X-s)*(v Y_2(X)-a mu Z_2(X))/(mu-nu),       (2)
    W(X)    =(X-s)*(v Y_2(X)+a mu nu Z_2(X))/(mu-nu).    (3)

In particular

    v/a=(q/p)*Z_2(h)/Y_2(h).                            (4)

Every displayed denominator is nonzero. This conditional restriction
leaves disjoint d-tag triples and profiles having fewer than two
d-tagged candidates open. It supplies no count eleven, twelve-candidate
counterexample, universal extraction or global improvement to
11/q–16/q. A separate scoped critical audit on 2026-10-08 found no
defect; its checks appear below. POTENTIALLY_NEW describes the original
local result beyond the assessed inputs, not certified originality or
a new discovery made by auditing it.

## Proof

### Full-moment input and distinct scalars

L043 (4)–(7) supplies all-eight-moment span membership before the
fourth-weight gate. L046 derives from this membership the five-value
cubic equations stated above, with u,u' nonzero, even for relaxed
recovered weights. Its proof uses L010's kernel identity on a word
supported on B union S, vanishing at the seven labels O minus S.
Thus no additional assumption on a truncated recurrence, splitting of
a locator, full weights or prime-field chart is being introduced.

The standard recurrence input remains Przemek Chojecki, *Shortening
Bounds for Reed–Solomon MCA*, live author TeX v9.2, July 17, 2026,
source lines 2785–2935, `drc:lem-locator-recurrence` (DR2) and
`drc:thm-exact-compiler` (DR6–DRC), inspected and specialized in L043
([author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex)).
This mutable source is not certified identical to ePrint 2026/1463.
Its fixed-support compiler does not supply the two-cubic coupling here;
we use the already justified specialization, without a recurrence reproof.

L043 (5) makes distinct candidate parameters have distinct mu,nu:
equality of gamma_0+g*rho/E(mu) and gamma_0+g*rho/E(nu) would imply
equal E, then mu=nu, since g*rho and rho-1 are nonzero. L046 excludes
coincident outside triples and says a double outside intersection
requires opposite y/z tags. Both present tags are d, so their outside
intersection has size at most one. Only L046's five-value equations and
same-d intersection exclusion are needed here. They are independently
checked in the scoped audit below; L046's remaining conclusions still
await their full separate audit.

### Couple the two cubics at the four singleton labels

Assume S intersect S'={s}. Put

    F(X)=f(X)/u, G(X)=f'(X)/u',
    U(X)=F(X)-G(X), V(X)=mu F(X)-nu G(X).

At either z-label, F(z)=G(z)=W(z); at either y-label,
F(y)=-W(y)/mu and G(y)=-W(y)/nu. All W-values at B are
nonzero, since the w-labels are distinct from B. Also F(s)=G(s)=0.
Hence U vanishes at the three distinct labels s,z_1,z_2, and V
vanishes at s,y_1,y_2. Both polynomials have degree at most three.
Neither is zero: U=0 would force mu=nu using any y-value, and V=0
would force mu=nu using any z-value. The factor theorem therefore gives

    U(X)=a (X-s)Z_2(X), V(X)=v (X-s)Y_2(X), a*v!=0.

Solving the two equations defining U,V, with mu-nu!=0, gives
F=(V-nu U)/(mu-nu) and G=(V-mu U)/(mu-nu). These are (1)–(2).

At a z-label one has V(z)=(mu-nu)W(z). At a y-label one has
U(y)=(mu-nu)W(y)/(mu*nu). Thus the degree-at-most-three polynomial

    W(X)-(X-s)*(v Y_2(X)+a mu nu Z_2(X))/(mu-nu)

vanishes at the four distinct singleton labels. The polynomial root
bound makes it identically zero, proving (3). In particular W(s)=0.
Since W is the product of three distinct linear factors, s is one
of the w-labels. This use of four evaluations is a polynomial identity
with a proved degree bound, not a four-moment substitute for L043's
full span test.

At h the five-value equations give
(q-p*mu)F(h)=(q-p*nu)G(h)=W(h). Subtraction yields
q*U(h)=p*V(h). Substituting their factorizations and cancelling
h-s!=0 gives q*a*Z_2(h)=p*v*Y_2(h). All p,a,Y_2(h) are
nonzero, so (4) follows. No division by the candidate's d coefficient
or recovered tag weight occurs; d was omitted from the five equations.

### The three residual pairs and the actual-support qualification

Let A=v Y_2-a nu Z_2, A'=v Y_2-a mu Z_2,
and C=v Y_2+a mu nu Z_2. Equations (1)–(3) identify their roots
with the three residual pairs in the conclusion, up to nonzero scalar
factors. In particular all three have degree two: f,f',W are monic
cubics divisible by X-s, and u,u',mu-nu are nonzero.

The polynomials Y_2,Z_2 have no common root, because all four singleton
labels are distinct. If A and C had a common root x, subtracting their
values would give a*nu*(mu+1)*Z_2(x)=0. The coefficient is nonzero
by the candidate gates. Hence Z_2(x)=0; A(x)=0 would then give
v*Y_2(x)=0, a contradiction. The same argument for A' and C uses
a*mu*(nu+1)!=0. For A and A', subtraction uses a*(mu-nu)!=0
and yields the same contradiction. Thus all three residual pairs are
pairwise disjoint. This proves their disjointness using the excluded
mu=-1 and nu=-1 cases essentially, not a presumed support packing.

The outside union has seven labels: s and these six residual labels.
Adding h,d gives nine. The common triple intersection is {s}; d lies
only in K,K'; all other labels are singletons, with two in each of
K,K' and three in A_2. This is the stated tau=1 incidence pattern.
The support-set conclusion holds even if a recovered coefficient
vanishes. It becomes a statement about actual four-error supports
only when both recovered words are full. Then L043 supplies their
unique actual errors and same-support badness, and their parameters
differ from gamma_2. No full-weight conclusion is inferred from the
polynomial identities alone.

This proof establishes a conditional intermediate restriction under
the unchanged counting assessment. It neither forces two d-tagged
candidates to exist nor forces them to intersect. Those alternatives,
other tag pairings and the count threshold remain unresolved.

### Separate scoped critical audit (2026-10-08)

The audit found no defect in the stated conditional result. It checked
the essential parts of L046 directly, without assuming that its complete
statement had already been certified. No twelve-count premise or L045
conclusion is used. The field remains F, and all parameters remain in
the original finite chart.

First, L043 (4)–(7) gives the full eight moments of N_K, not just the
four equations used to recover its coefficients. For K={d} union S,
form n on B with entries c_x*a_x(mu) and let omega be those recovered
coefficients on K. All four singleton entries of n-omega are nonzero:
K contains none of them, Q has no root in B, and mu!=0. Thus n-omega
is a nonzero word in ker(sigma). L010's kernel proof applies to the
shifted moments 1,...,8 on this H: its kernel is precisely evaluation
of polynomials of degree at most seven. On the seven labels O minus S
the word vanishes. The factor theorem and degree bound give exactly
P=u*product_(o in O minus S)(X-o), with u!=0. No full-weight condition
on omega is needed. Multiplying P(x)=Q(x)*a_x(mu) by f(x) at
x in B minus {d}, and using
product_(o in O)(X-o)=Q(X)W(X), gives
a_x(mu)f(x)=u W(x), since Q(x)!=0. This verifies the scale and signs
of the five-value input. The same reasoning applies to nu and f'.

The original parameter formula has numerator g*rho!=0 and denominator
E(t)=rho+(rho-1)t, whose slope rho-1 is nonzero. Hence distinct admitted
finite parameters imply mu!=nu. If S=S', a z-evaluation of the two
five-value equations forces u=u', because W(z)!=0. A y-evaluation
then forces mu=nu, a contradiction. If S and S' share two labels,
write f=R(X)(X-c), f'=R(X)(X-e) with R their common monic quadratic
and c!=e. At both z-labels the equations give
(z-c)-(u/u')*(z-e)=0; R(z), W(z) and u' are nonzero there.
A polynomial of degree at most one with these two distinct roots is
zero. Its leading and constant coefficients give u/u'=1 and c=e,
contradicting the assumption. This independently establishes exactly
the same-d intersection bound used here, even for relaxed candidates.
The opposite-tag cross-ratio and matching assertions of L046 are not
needed and are not certified by this audit.

For a single shared label s, independently set F=f/u, G=f'/u',
U=F-G and V=mu F-nu G. At z_1,z_2, U vanishes and
V=(mu-nu)W. At y_1,y_2, V vanishes and
U=(mu-nu)W/(mu*nu). In particular neither U nor V is zero.
Each also vanishes at s, a label outside B. Their degree is at most
three, so their three distinct specified roots yield exactly
U=a(X-s)Z_2 and V=v(X-s)Y_2, with a,v nonzero. Solving the two
linear equations gives (mu-nu)F=V-nu U and
(mu-nu)G=V-mu U, checking both signs in (1)–(2).

To verify (3) without presuming s lies in W, consider
R_0=(mu-nu)W-V-mu*nu*U. Its degree is at most three. At each
z-label its last term vanishes and the first two cancel; at each
y-label its middle term vanishes and the other two cancel. These
are four distinct labels, so the polynomial root bound gives R_0=0.
Evaluating at s now proves W(s)=0. This is the first point at which
s is identified as a w-label. At h, subtraction of
(q-p*mu)F(h)=W(h)=(q-p*nu)G(h) gives q U(h)=p V(h).
Cancelling h-s and then p*a*Y_2(h), all nonzero, proves (4).
In fact the five-value equations also force q-p*mu and q-p*nu
nonzero, but the displayed calculation never divides by either.

For completeness, set A=vY_2-a*nu Z_2, A'=vY_2-a*mu Z_2,
C=vY_2+a*mu*nu Z_2. The already verified identities show that these
are nonzero scalar multiples of f/(X-s), f'/(X-s), W/(X-s).
Thus each has degree exactly two and exactly the claimed two distinct
roots; no leading-coefficient cancellation is silently excluded.
The differences are
C-A=a*nu*(mu+1)Z_2, C-A'=a*mu*(nu+1)Z_2,
and A-A'=a*(mu-nu)Z_2. Every displayed scalar is nonzero by the
finite-candidate gates. A shared root of any two would consequently
annihilate Z_2 and then Y_2, impossible because their root sets are
disjoint. This checks the residual-pair statement, including the
essential exclusions mu,nu!=-1.

Finally the residual pairs supply six distinct labels outside B,
in addition to s. The three witnessing sets have common intersection
{s}, double-only intersection {d}, and singleton counts 2,2,3; h is
one of the third set's singletons. Their union therefore has nine
labels. They are actual full four-error supports only if every recovered
coefficient for both candidates is nonzero. L043 then rescales these
coefficients by lambda/(gE), a nonzero scalar, and supplies uniqueness
and same-support badness. The original A_2 was already full by the
triple gates, and both new parameters differ from gamma_2 and each
other. This verifies the conditional actual-support conclusion, with
no assertion that recentered normalized weights or parameters are
rational. A candidate with a zero recovered coefficient retains only
the witnessing-set conclusion. The audit neither forces the two
d-tagged candidates to exist or intersect nor excludes either twelve
profile, and does not improve the global interval.

## Mathlib

The full same-d restriction and support qualification: **not checked**
for a matching Mathlib theorem. Supporting factor and root bounds were
inspected in the prior assessment (2026-10-08, mutable master source):
`Polynomial.mul_divByMonic_eq_iff_isRoot` and
`Polynomial.dvd_iff_isRoot` in
[Div.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Polynomial/Div.lean),
source lines 566–576 under `[CommRing R]`; `Polynomial.card_roots`,
`Polynomial.card_roots'`, `Polynomial.mem_roots` and
`Polynomial.card_le_degree_of_subset_roots` in
[Roots.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Polynomial/Roots.lean),
lines 65–74, 98–99 and 121–123 under `[CommRing R] [IsDomain R]`.
F is a field, so these hypotheses hold; all uses of the root bound
above either exclude a nonzero polynomial or first establish nonzero
status. These standard inputs are cited, not claimed as new results.
No pinned Mathlib commit, Lean compilation or full-result coverage or
absence claim is asserted. L043 and the essential L046 uses now have
scoped informal checks; L046's full separate audit remains outstanding.
