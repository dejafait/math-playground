# L044 — Five relaxed candidates force prime-field normalized weights

## Hypotheses

Use L043's entire local tau=1 setup over F=F_(97^20), with prime
subfield F_0=F_97, H of order sixteen, k=8 and the pinned cell
1/4<=delta<5/16. In particular the nine labels in

    A_0={h,d,y_1,y_2}, A_1={h,d,z_1,z_2}, A_2={h,w_1,w_2,w_3}

are distinct in H. The three original finite gamma_i are distinct,
lambda is nonzero, and p*q*(1-p-q)*r*(1-r) is nonzero. Retain the
definitions c_x, g, rho, Y, Z, v_x and K_* from L043. In particular
g!=0 and rho is in F minus {0,1}; none of gamma_i, rho or lambda is
assumed rational over F_0. L041's local converse and L042 apply,
without a sixteen-count or completion premise.

Let R be the set of distinct original finite parameters admitted by
L043 (4)–(7) for at least one four-set K other than A_0,A_1,A_2,K_*.
Thus both projected vectors must be nonzero and proportional with
mu in F_0^* minus {-1}, E=rho-(1-rho)*mu!=0, and all applicable
missing-shared-coordinate equations (7) must hold. The recovered
fourth-weight nonvanishing gates (9) are deliberately not required.
Both-zero, one-zero and independent projected systems remain excluded
exactly as in L043. The selected gamma_i are not counted.

## Conclusion

If |R|>=5, then p,q,r all belong to F_0. Consequently any gated local
pencil with at least one of p,q,r outside F_0 has |R|<=4, independently
of the labels and the original finite chart.

For a fixed labeling and gated p,q,r in F_0 define the finite set M
as follows. For every eligible nonuniversal four-set K, retain its
nonzero proportional quotient scalar mu if mu!=-1 and (7) holds;
do not impose E!=0 or the fourth-weight gates. M is the set of
distinct retained mu values, not the number of supports. Then

\[
 |R|=|\{\mu\in M:\rho-(1-\rho)\mu\ne0\}|.             \tag{1}
\]

At most one element of M is lost in (1). None is lost if rho is
outside F_0. Therefore the approved assertion |R|<=11 for every
gated local pencil over F is equivalent to the finite assertion

\[
 |M|\le11\quad\text{for every nine-label choice and every gated }
                  (p,q,r)\in F_0^3.                         \tag{2}
\]

This is a reduction, not a proof or refutation of (2). It does not
assert that the original affine parameters or the excluded direction
are rational. Any hypothetical |R|>=12 pencil has no finite error of
weight below four, and every witness counted in R then passes its
fourth-weight gates. Thus omission of those gates cannot by itself
create a counterexample to eleven through lower-weight errors.

The uniform nonrational-weight bound is a local advance under the
saved EXPLORE assessment, not a claimed discovery beyond all known
sources. This result awaits a separate critical audit. The numerical
eleven threshold, other triple patterns, universal extraction and
identification with ABF26 remain open; the global interval is unchanged.

## Proof

### Relaxed candidates still have actual sparse representatives

L043 proves, before its last nonvanishing test, that equations (4)–(7)
put N_K in the span of the four moment columns indexed by K. It
recovers all eight moments, not just their first four. Its formula
s(T_K)=lambda*N_K/(gE) has nonzero scalar factor. Hence every T in R
has an actual error representative of weight at most four, supported
in every witnessing K. L010 gives uniqueness, since two such words
would differ by a codeword of weight at most eight whereas the code
has distance nine. A vanishing recovered coefficient causes a lower
weight, not loss of this span-membership conclusion.

L042 supplies nonzero D and every nonzero coordinate polynomial ell_x;
L010 bounds each degree by four. At a full-weight error supported on K,
L010's pointwise identity says

\[
 \ell_x(T)=D(T)\prod_{z\in K}(x-z),\qquad D(T)\ne0.     \tag{3}
\]

At any error of weight at most three, all ell_x(T) vanish, by L010's
rank/minor identity (indeed it proves the stronger multiplicity bound).
It follows that if a witnessing K contains x, then ell_x(T)=0,
whether or not the recovered coefficient at x itself is nonzero.
This checks the relaxed cases that a full-weight-only argument would miss.

### Two candidates outside the shared locator roots

The three stipulated full errors contain h, so ell_h has the three
distinct roots gamma_0,gamma_1,gamma_2. Its nonzero degree-at-most-four
polynomial has at most one further distinct root in F. Similarly ell_d
has roots gamma_0,gamma_1 and at most two further distinct roots outside
the three selected parameters. In fact d is absent from A_2, so (3)
also shows ell_d(gamma_2)!=0, though only the two prescribed roots are
needed for the bound.

Among distinct T in R at most three can therefore satisfy ell_h(T)=0
or ell_d(T)=0, by the union bound on these two finite root sets. This
uses distinct roots, so repeated roots and possible lower degrees can
only reduce the number. If |R|>=5 choose two distinct T_1,T_2 outside
that union. Every witnessing K_i omits both h,d, by the preceding
paragraph. Such candidates also have full weight, since a smaller
weight would make all coordinate locators vanish.

Let mu_i be their quotient scalars. The parameter map in L043 is

\[
 T(\mu)=\gamma_0+g\frac{\rho}{\rho-(1-\rho)\mu}.       \tag{4}
\]

It is injective on the permitted scalars: equality of its values,
after cancellation of the nonzero g*rho and the nonzero denominators,
gives equality of the denominators and then equality of mu because
1-rho!=0. Thus mu_1!=mu_2, and both lie in F_0^* minus {-1}.

For each i, L043 (6) gives beta_(i,h), beta_(i,d) in F_0. Since both
shared labels are absent, both recovery equations hold. With
a_i=beta_(i,h)/c_h and b_i=beta_(i,d)/c_d in F_0, they read

\[
 q-\mu_i p=a_i,\qquad 1-(1+\mu_i)r=b_i.              \tag{5}
\]

The nonzero c_h,c_d are prime-field elements. Subtracting the two
first equations gives

\[
 p=\frac{a_1-a_2}{\mu_2-\mu_1}\in F_0,
 \qquad q=a_1+\mu_1p\in F_0.
\]

The second equation for i=1 gives r=(1-b_1)/(1+mu_1) in F_0; its
denominator is nonzero because mu_1!=-1. This proves the descent of
the three normalized weights and its stated contrapositive. Nothing
in this argument divides by a recovered fourth weight or forces rho
into F_0. L016's fixed-label row count and L034's different union-six
equality hypotheses are not inputs.

### Exact remaining finite test, with the original chart retained

For rational p,q,r all quotient vectors, beta values and equations (7)
are defined over F_0 and independent of rho, gamma_0, g and lambda.
L043's exhaustive quotient classification leaves exactly the scalars
used to define M, subject only to E!=0 for a finite parameter. Equation
(4) gives that parameter, is injective as proved above, and L043 verifies
it differs from all three gamma_i. Multiple eligible supports with the
same mu therefore contribute just one parameter. This proves (1),
including supports containing a shared label and all rejected quotient
cases; no disjointness restriction is added to the definition of M.

For any mu in M, E=0 is equivalent to

\[
 \rho=\frac{\mu}{1+\mu}\in F_0.                      \tag{6}
\]

The denominator is nonzero. Conversely the linear equation
rho-(1-rho)*mu=0 has at most one solution mu for fixed rho!=1.
This proves both deletion claims. It does not count the excluded
original infinity as a finite parameter.

If (2) holds, (1) bounds R for all rational normalized weights;
the already proved bound four covers every other gated choice.
Conversely, if a rational gated labeling has |M|>=12, select any
rho in F minus F_0, which exists since [F:F_0]=20, and set
gamma_0=0, gamma_1=1, gamma_2=rho and lambda=1. L041's local converse
constructs the actual pencil with precisely these labels and normalized
weights, and L042 gives its nonpersistent locators. All triple gates
are retained. Equation (6) excludes no mu, so (1) gives |R|=|M|>=12
for this allowed pencil. This establishes the equivalence, not a
construction of such a labeling or a change to a given pencil's chart.

Finally, if any original pencil has |R|>=12, its sparse/bad set has at
least fifteen distinct finite elements: these twelve plus the three
stipulated parameters. If any finite representative had weight at most
three, L010's weighted bound would instead give |B|<=13 (and a still
smaller bound for weights below three). Hence there are no such lower
weights. Every witnessing four-set has four nonzero recovered weights,
and uniqueness makes it the actual support. This argument is conditional
on a violation of eleven and does not discard lower weights in defining
or proving (1) and (2).

The proof uses the audited local recurrence/recovery input L043 and the
proved locator identities of L010; it does not reprove the primary
recurrence theorem imported there. No numerical sample, finite certificate,
rationality of original parameters or completion premise is used. The
unresolved work is to prove (2) or exhibit a gated counterexample.

## Mathlib

The full five-candidate implication and uniform finite reduction:
**not checked**. Supporting polynomial root bounds, finite-field linear
equations and subfield closure: **not checked** in Mathlib for this step.
L010, L041, L042 and L043 are the informal inputs, including L043's
precise imported recurrence citation. No matching Mathlib theorem,
absence result, formal verification or certified originality is claimed.
