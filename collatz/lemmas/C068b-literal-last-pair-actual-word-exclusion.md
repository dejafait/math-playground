# C068b — Literal last-pair actual-word exclusion

## Hypotheses

Let T(n)=n/2 for even positive integers and T(n)=(3n+1)/2 for
odd positive integers. O and E denote these branches at actual odd
and even inputs. Use exactly L055's complete indexed J_i,H_i table
in literal order i=0,...,24. For an integer 0<=t<=9250245 set

\[
a_{23}=2+18t,\qquad a_{24}=166504412-18t,
\qquad a_i=2\quad(0\le i<23).
\]

Put W_i=(OOEO)^{J_i}O^{H_i}E^{a_i} and D_i=4J_i+H_i+a_i.
Assume W_0...W_24 is actual at a positive integer n_0, with
n_i=T^{D_0+\cdots+D_{i-1}}(n_0), and is closed: n_25=n_0.
Each designated junction n_i, 0<=i<25, is positive, odd and
20 modulo 27. Each final even tail is exact. Repeated periods and
coincident junctions are allowed. No minimum, primitive-period,
least-root, first-return, H-guard or seed assumption is imposed.
Logarithms are natural.

## Conclusion

No such actual closed concatenation exists for any integer in the
specified closed parameter interval.

This is a local RESEARCH/REPRODUCTION application under the prior
SPECIALIZE assessment
`drafts/literature/2026-10-14-literal-family-actual-word-exclusion.md`.
It assembles existing necessary conditions and audited C068a, with no
new coding or arithmetic diagnostic. Its t=0 and t=1 conclusions overlap
C063a and C067b, which cover more orders for those allocations. The
present conclusion concerns literal order only. The separate critical
audit below found no defect; no unrestricted-cycle or universal-descent claim follows.

## Proof

Suppose such a concatenation exists. L055's full table has J_i>=2
and H_i>=3 at every position. Since 166504412=2+18*9250245,
the two varying tails can be written

\[
a_{23}=2+18t,\qquad a_{24}=2+18(9250245-t).
\]

Thus every tail is at least 2 and congruent to 2 modulo 18, including
both endpoints of the interval. In particular the final row still has
a permitted tail when t=9250245. These parameters and the actual closed
words meet L041's language hypotheses at r=25; n_0>1 follows from
the lower bound established next. Only its elementary wordwise
necessity is used, not its seed, length estimate or cycle-count inputs.

For each i, write n_i=20+27q_i. Positivity gives q_i>=0, and oddness
makes q_i odd. Hence q_i>=1 and n_i>=47. Define s_i=n_i+23/11,
including s_25=s_0. Consequently

\[
s_i\ge540/11,\qquad s_i-23/11=n_i\in\mathbb Z
\quad(0\le i\le24).
\tag{1}
\]

Fix any position 0<=i<=24, and keep that outgoing row's own
J=J_i,H=H_i,a=a_i. Let n=n_i, m=n_{i+1},
y=T^{4J}(n) and z=T^{4J+H}(n). L041's section “Each occurrence's
own prefix and the transfer to the next” supplies the actual-word
identities

\[
y+1=(27/16)^J s_i-12/11,\qquad
2^H(z+1)=3^H(y+1),\qquad z=2^a m.
\tag{2}
\]

Its own-input necessity, justified upstream by L031's arbitrary-tail
boundary passage, supplies v_2(11n+23)=4J+2. Its hypotheses here
are H>=3, a>=2 and a positive odd actual endpoint m, all verified
at this position; the necessity does not require a=2. More explicitly,
z+1 is odd, so (2) gives v_2(y+1)=H. With y+1=2^H u and u
positive odd, the already inspected identity
11y+23=4(11*2^(H-2)u+3) gives valuation 2. The wordwise identity
16^J(11y+23)=27^J(11n+23) then gives the stated input valuation.
These are applicability checks of the existing necessity, not a new
valuation theorem. Positivity yields 11n+23>=2^(4J+2); since
11n+23=11s_i, taking logarithms gives exactly

\[
4J_i\log2\le\log s_i+\log(11/4).
\tag{3}
\]

This is C068a's non-strict guard at the input of its own outgoing row.
No index is shifted to an incoming row or selected minimum.

Also (2) gives z=(3/2)^H(y+1)-1. Substituting its first identity,
dividing by the actual 2^a, and adding 23/11 gives

\[
s_{i+1}=2^{-a_i}\left((27/16)^{J_i}(3/2)^{H_i}s_i
 -(12/11)(3/2)^{H_i}-1\right)+23/11.
\tag{4}
\]

The varying row-23 and row-24 tails remain at their literal outgoing
positions. The calculation includes i=24, where m=n_25=n_0 and
s_25=s_0; thus the closing equation is verified as well.

Now the integer parameter, full literal table and both tail formulas
match C068a. Equation (1) verifies its lower domain and unshifted
integrality, (3) verifies all 25 own-input J guards, and (4) verifies
all 25 cyclic endpoints. These are every premise of that result.
Audited C068a says that no such tuple has all unshifted junctions
integral (indeed its n_0 is nonintegral). This contradicts (1), proving
the conclusion throughout the closed interval.

The underlying primary affine input is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The ready assessment records its inspected chronological affine formula
and essential induction cases. Existing local necessity and C068a are
reused; no general coding reproof or rational-parity sufficiency is
needed, since actual words are a hypothesis.

No H guard, seed, aggregate count ray, global minimum, primitive count
or published computational cutoff is invoked. Every verification is at
a time occurrence, so repetitions and coincident values retain every
premise. Both rational witnesses and Attempts 027–031 remain valid;
real feasibility does not imply integer realization. Other allocations,
nonliteral orders for the larger-t family, entry, unrestricted cycles,
divergence and universal eventual descent remain unresolved.

### Separate critical audit — 2026-10-14

The prior SPECIALIZE assessment
`drafts/literature/2026-10-14-literal-family-actual-word-critical-audit.md`
approved exactly this audit. Independent premise matching found no defect
in C068b. This verifies an existing local reproduction; it neither
strengthens the conclusion nor repairs a mathematical error.

**Literal parameters and full interval.** The complete L055 table contains
exactly the rows 0 through 24, with every J_i>=8>=2 and every H_i>=40>=3.
Its J,H entries are unchanged here; its old tails are not imported.
The equality 18*9250245=166504410 verifies both varying-tail formulas.
At t=0 their values are (2,166504412), and at t=9250245 they are
(166504412,2), at rows (23,24) respectively. For every intermediate
integer, both are at least 2 and congruent to 2 modulo 18. The other
23 tails are exactly 2. Thus L041 applies with r=25 once the actual
junction domain is checked, including the endpoint where row 24 has
only two final halvings. No tail cap or tail-2 transport identity is used.

**Actual domain at every occurrence.** Positivity and integrality of
n_i=20+27q_i imply integer q_i>=0: q_i<=-1 would give n_i<=-7.
Oddness of n_i forces q_i odd, so q_i>=1. Consequently every n_i>=47,
including n_0>1, and s_i=n_i+23/11>=540/11. Every unshifted s_i-23/11
is integral. Closure supplies the same statements for i=25 and
s_25=s_0. No shifted integrality, minimum location or distinctness of
junction values has been inferred.

**Own-input necessity without a hidden tail restriction.** Fix any
i in {0,...,24}, with n=n_i and m=n_(i+1). Actuality gives all the
intermediate integer states and prescribed parities. The actual E^a
tail gives z=2^a m, hence z+1 odd. L041's inspected finite identities
give 2^H(z+1)=3^H(y+1) and
16^J(11y+23)=27^J(11n+23). Their use is legitimate for this one
word, independently of the number of other words. The first gives
v_2(y+1)=H. With positive odd u=(y+1)/2^H, the bracket
11*2^(H-2)u+3 is odd because H>=3. Therefore
11y+23=4(11*2^(H-2)u+3) has valuation exactly 2, and the second
identity gives v_2(11n+23)=4J+2. Positivity then implies
2^(4J+2)<=11n+23=11s_i. Taking natural logarithms yields
4J_i log2<=log s_i+log(11/4), with precisely the non-strict sign
and own outgoing row required by C068a. The upstream L031 passage
supports this arbitrary-tail necessity; its two-word closure converse
and its separate 3-adic conclusion are not invoked.

**Exact endpoints, including the cut.** L041 gives
y+1=(27/16)^J s_i-12/11 and z+1=(3/2)^H(y+1).
Substitution into m=z/2^a yields exactly C068a (1) after adding
23/11. In particular the term -(12/11)(3/2)^H and the term -1
are both divided by the same actual 2^a; the outer +23/11 is not.
This calculation covers each i=0,...,23 and also i=24, where the
actual endpoint is n_25=n_0. Neither varying tail moves to another
row, and neither the closing equation nor an input guard is omitted.

**Conjunction and limits.** C068a's integer parameter, literal table,
both tail formulas, all 25 endpoint equations, lower domain and all
25 non-strict J guards are now supplied simultaneously. Its excluded
condition is integrality of all n_i, which the actual orbit supplies;
indeed integrality at n_0 already contradicts its stronger conclusion.
The audited C068a is reused without rerunning its t=2 certificate or
the two survivor modular evaluations. Repeated periods and coincident
junctions retain all indexed equations and guards. No H guard, seed,
primitive count, count ray, global minimum or computational cutoff is
needed. The direct inputs remain L041, L055 and C068a, so the DAG and
assembled argument do not change. The precise primary citation and
Mathlib qualifications are retained, with no fresh source or formal
verification claim. C063a/C067b already cover the two survivor allocations
in more orders. Both rational witnesses, Attempts 027–031, other
allocations/orders and every universal-descent gap remain unchanged.

## Mathlib

Full matching Mathlib coverage and a Lean build of this application
were not checked; unknown coverage is not evidence of absence.
C068a records supporting valuation/rational-reduction declarations
`padicValRat.defn`, `padicValInt_dvd_iff` and
`Rat.num_or_den_zero_padicVal` with their prime, nonzero and coprimality
qualifications in
[PadicVal.Basic, commit 2da3ab0a20dc0c66f56a557e37df39f7d36cb953](https://github.com/leanprover-community/mathlib4/blob/2da3ab0a20dc0c66f56a557e37df39f7d36cb953/Mathlib/NumberTheory/Padics/PadicVal/Basic.lean).
These supporting declarations are not a full theorem for this literal
family; the present proof invokes existing necessity and nonintegrality.
