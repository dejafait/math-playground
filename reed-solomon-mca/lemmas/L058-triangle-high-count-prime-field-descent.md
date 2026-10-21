# L058 — Conditional high-count descent for the triangle

## Hypotheses

Use the full hypotheses and notation of audited L057: F=F_(97^20),
H the order-sixteen subgroup of F_97^*, C=RS[F,H,8], the pinned cell
1/4<=delta<5/16, and nine distinct labels with base supports
\[
 A_0=\{a,b,y_1,y_2\},\quad A_1=\{a,c,z_1,z_2\},\quad
 A_2=\{b,c,w_1,w_2\}.
\]
Put P={a,b,c}. The original finite gamma_0,gamma_1,gamma_2 are
distinct, lambda!=0, and the normalized weights obey
p(1-p)q(1-q)r(1-r)!=0. These data give the actual syndrome pencil
s(T) through audited L041's local converse, not its equality-conditioned
necessary direction. Neither the original chart nor p,q,r is assumed
prime-field valued.

Assume there are thirteen distinct original finite parameters T_j,
different from all three base parameters, each admitting a relaxed
L057 recovery on a nonbase four-subset K_j of H. Thus all L057 projected
and lifted equations and its original finite exclusions hold; recovered
weights are allowed to vanish at this stage. In particular E_j!=0,
mu_j!=0,-1. Both-zero projected systems are retained with their actual
finite lifts, including a priori nonprime mu_j. Count parameters, not
support witnesses. Existence of such thirteen parameters is only a
conditional premise.

## Conclusion

All three normalized pair weights p,q,r belong to F_97. Among the
thirteen additional recoveries at least three have nonzero proportional
projected vectors (L057's isolated case). For each x in P at least one
such isolated recovery misses x, although no one recovery is asserted
to miss all of P.

Consequently every additional scalar mu_j is in F_97, including those
from both-zero systems. The normalized fourth weights omega_xi of
L057 (13) are also prime-field valued. The actual weights include the
possibly nonprime factor lambda/(gE_j); the original gamma_i, T_j, rho,
lambda and excluded direction are not asserted rational.

This establishes conditional descent only. It proves neither a
thirteen-parameter construction nor its impossibility, a finite count,
arbitrary-family extraction, a global improvement of 11/q–16/q, or a
challenge-level result. A separate critical audit on 2026-10-10 found
no mathematical defect in this conditional implication.

## Proof

### Establish equality before using incidence

Audited L041's local converse supplies the three actual full-weight
base errors and their same-support badness. Because the triangle has
no coordinate common to all three supports, its coordinate locators
are all nonzero polynomials; its Hankel determinant is nonzero at the
base parameters. These are precisely the hypotheses needed for L010,
and are also explicitly retained in L057. No equality assumption was
used to construct the pencil or certify these polynomial conditions.

For each T_j, L057 supplies all eight moments and same-support failure
on H minus K_j even if a recovered weight vanishes. Thus the thirteen
distinct T_j and three distinct base parameters are sixteen actual bad
parameters in the original finite chart. L010 bounds their total by
sixteen. Its weighted inequality therefore forces every error to have
weight exactly four: the presence of any lower-weight error would make
the upper bound at most fifteen. Its equality conclusion then gives
sixteen unique errors with distinct four-supports, each coordinate of
H used exactly four times. In particular each K_j is now the actual
full support, so counting its incidences involves no artificial padding
or duplicate support witnesses.

Each of a,b,c appears in exactly two of A_0,A_1,A_2. Hence it appears
in exactly two of the thirteen additional supports, and
\[
             \sum_{j=1}^{13}|K_j\cap P|=6.             \tag{1}
\]
This equality is justified by the actual high count, not by abstract
support balance assumed in advance.

### Isolated recoveries cover the missing shared labels

L057 exhausts the eligible projected cases. Exactly-one-zero vectors
and independent nonzero vectors give no recovery. Thus each K_j is
either isolated (two nonzero proportional vectors) or both-zero with
a successful lift. L057 proves both-zero is possible only when
m=|P minus K_j|=3, so those supports contribute zero to (1).
It also proves that m=0 permits no eligible recovery. Every isolated
support therefore contains at most two shared labels. If I is the
set of isolated additional recoveries, (1) yields
\[
                6=\sum_{j\in I}|K_j\cap P|\le2|I|,
                \qquad |I|\ge3.                      \tag{2}
\]
This does not bound the number of both-zero label systems or discard
their nonprime lifts.

Fix x in P. Exactly two additional supports contain x. Since at least
three additional recoveries are isolated, at least one isolated K_j
misses x. Apply this separately for a, b and c. The selected isolated
recoveries can be different, and may contain the other shared labels.
Thus the proof does not assume an isolated support disjoint from P.

### Apply the actual missing-coordinate equations

In each isolated case, L057 (7) gives mu in F_97^*, from the ratio
of two nonzero projected label vectors. Its finite gates give mu!=-1
and E!=0. All c_x and beta_x^Y,beta_x^Z in its missing-coordinate
equations are prime-field scalars, with c_x!=0. Apply L057 (11) at
the isolated recovery missing each corresponding label:
\[
 \begin{split}
 p&=\frac{1-(\beta_a^Z-\mu\beta_a^Y)/c_a}{1+\mu},
                       &&\text{at a recovery missing }a,\\
 q&=\frac{\beta_b^Y-\beta_b^Z/\mu}{c_b},
                       &&\text{at a recovery missing }b,\\
 r&=\frac{\beta_c^Z-\mu\beta_c^Y}{c_c},
                       &&\text{at a recovery missing }c.
 \end{split}                                          \tag{3}
\]
The mu and beta data in different rows need not coincide. Every
denominator shown is nonzero by the unchanged L057 gates. Each right
side belongs to F_97, proving p,q,r in F_97. These are restored
shared-column equations, not just projected compatibility.

For a both-zero recovery, all A_x,B_x of L057 (9) are now in F_97.
An eligible lift has a nonzero B pivot and mu=-A_x/B_x. It therefore
also has mu in F_97. The inconsistent all-B-zero case and the entirely
free case have already been excluded in L057; no division by a zero
pivot is introduced. Formula (13) there uses only prime-field labels,
c_x, p,q,r and mu, with nonzero label denominators, so omega_xi is
prime-field valued for every additional recovery.

The parameter remains T=gamma_0+g*rho/E, and the actual weight remains
lambda*omega_xi/(gE). The proof imposes no rationality on rho or the
other original chart data, and includes only E!=0 finite recoveries.
It does not add original infinity or any excluded base parameter to
the count. This completes the exact conditional implication.

### Citation reuse and scope of the new argument

Essential local inputs are L010's weighted bound and equality incidence,
audited L041's local converse/nonpersistence, and audited L057's complete
criterion, including its m=0 exclusion and m=3 both-zero restriction.
Their proofs and precise primary citations remain canonical in those
files. In particular L057 imports Przemek Chojecki, *Shortening Bounds
for Reed–Solomon MCA*, author TeX v9.2 (July 17, 2026), DR2
(`drc:lem-locator-recurrence`) and DR6–DRC (`drc:thm-exact-compiler`),
lines 2785–2935, at R=8,t=4 with multiplier x and eta_j=s_(j+1), from
the [author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
This mutable source is not certified identical to ePrint 2026/1463.
No recurrence, distance or shortening theorem is reproved here.

The pre-existing EXPLORE assessment is
`drafts/literature/2026-10-10-triangle-high-count-descent.md`. Its
inspected confinement theorem assumes already-subfield generators and
does not establish this conclusion. The step supplied here is the
incidence bridge (1)–(2) to the separately missing-label equations (3).
Its recorded search did not establish coverage; this is local progress,
not a certified originality claim. No finite sample, mathematical
script or numerical certificate is used in the proof.

### Separate critical audit (2026-10-10)

The separate audit used the pre-existing EXPLORE assessment
`drafts/literature/2026-10-10-triangle-high-count-descent-audit-scope.md`.
It checked the complete argument above, L010's hypotheses, weighted
inequality and equality proof, L041's local converse and pointwise
nonpersistence proof, and L057's projected classification, restored
equations, finite parameter map and same-support converse. No mathematical
defect or additional premise was found. The checks below validate the
existing conditional result; they supply no new counting theorem.

1. The use of L041 is noncircular. Its local converse constructs full
   base errors without equality. For every x in H some base support
   misses x, since the triangle has empty triple intersection. At that
   base parameter the pointwise locator formula in L010 gives
   ell_x!=0, while full weight gives D!=0. Thus the polynomial
   hypotheses of L010 hold before its global bound is invoked.
   L057's recurrence and restored lift recover all eight moments even
   when fourth weights vanish. Its same-support argument uses sparse
   uniqueness and K!=A_0, not a prior fullness assumption. Each of the
   thirteen distinct original finite parameters therefore is actually
   bad, independently of any support counting.
2. Together with the three bases these are sixteen distinct bad
   parameters. In L010's inequality, N_4+N_3+N_2+N_1+N_0 is at least
   sixteen and at most sixteen minus nonnegative extra costs. Every
   lower-weight count must vanish. Its equality proof then makes all
   actual supports distinct and each coordinate occur four times.
   Consequently each four-set K_j is its error's full support; padded
   supports and multiple witnesses for one parameter do not contribute
   to (1). Each shared label occurs twice among the bases and exactly
   twice among the additional supports.
3. L057's both-zero restriction is valid over F before any descent:
   for m<=2 its zero-vector proof uses at most 4+m+2<=8 moment columns.
   Both projected vectors zero would force K to contain both singleton
   pairs, contradicting m<=2. Hence both-zero supports miss every
   shared label. Its m=0 exclusion also uses at most eight columns,
   so an isolated recovery contains at most two shared labels. Thus
   all six additional shared incidences are supplied by isolated
   recoveries and require at least three. For any specified shared
   label, only two additional supports can contain it; at least one
   isolated recovery misses it. This is a separate existence argument
   for each label, not an assertion about a single common witness.
4. For each chosen isolated witness a nonzero coordinate of the two
   prime-field projected vectors gives mu in F_97^*. The beta scalars
   use only labels with nonzero denominators x*f_K(x) and label
   differences. The combined vector beta^Z-mu*beta^Y solves the full
   restored system, as required by L057; neither beta vector is
   assumed to solve it separately in the isolated case. Equation (3)
   has exactly the signs of L057 (10), and divides only by c_x!=0,
   mu!=0 and 1+mu!=0. Its three separately chosen rows therefore
   prove p,q,r in F_97.
5. Only after that conclusion are all entries A_x,B_x of a both-zero
   lift known to be prime-field. L057 excludes an entirely free lift
   by sparse uniqueness: it would represent the full base A_0 error
   on K disjoint from P. An all-B-zero system is consequently
   inconsistent. An admitted lift has a nonzero B pivot, so
   mu=-A_x/B_x lies in F_97 and still satisfies all other lift rows.
   Formula (13) of L057 then proves rationality of each normalized
   omega_xi; actual weights retain their possibly nonprime common scale.
6. The finite change of variables has E=rho/t and t=rho/E, with
   rho!=0,1. Thus mu=0 and mu=-1 correspond to the excluded bases
   t=1 and t=rho; t=0 has no finite mu and E=0 is original infinity.
   On the retained domain the map is injective: equal t implies equal
   E and hence equal mu because 1-rho!=0. Descent adds no parameter
   and never reinstates E=0. No rationality of rho, gamma_i, lambda,
   T or the original excluded direction is used.

No finite certificate is an input to L058. L057's selected regression
was neither replayed nor substituted for its audited symbolic criterion.
The mathematical inputs remain exactly those in the existing DAG row.
The argument and its conclusion are unchanged; the audit makes the
conditional descent usable for subsequent work, while its high-count
premise, the finite count and arbitrary-family extraction remain open.
Coverage reuse is not an originality finding or an advance beyond all
known literature. Full and supporting Mathlib coverage remain not checked.

## Mathlib

The full conditional high-count triangle descent result: **not checked**.
Supporting finite-set incidence counting and prime-subfield closure under
field operations: **not checked** in Mathlib for this step. The proof
uses the three stated canonical local inputs and elementary counting;
no matching Mathlib theorem, absence claim or Lean verification is made.
