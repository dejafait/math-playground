# C068a — Literal last-pair family integer exclusion

## Hypotheses

Use exactly L055's complete indexed table of pairs J_i,H_i in literal
order i=0,...,24. For an integer 0<=t<=9250245 put
a_23=2+18t, a_24=166504412-18t and a_i=2 for 0<=i<23.
Require real s_0,...,s_25 with s_25=s_0, s_i>=540/11, and every
cyclic endpoint and own-input J guard

\[
s_{i+1}=2^{-a_i}\left((27/16)^{J_i}(3/2)^{H_i}s_i
 -(12/11)(3/2)^{H_i}-1\right)+23/11,
\qquad 0\le i\le24,
\tag{1}
\]
\[
4J_i\log2\le\log s_i+\log(11/4),\qquad 0\le i\le24.
\tag{2}
\]

Logarithms are natural. Define n_i=s_i-23/11. No minimum location,
H guard, seed, parity, residue, exact valuation or primitive-orbit
realization is assumed. The integer condition to be excluded is that
all n_i, 0<=i<=24, are integers, rather than that all s_i are integers.

## Conclusion

There is no tuple satisfying these hypotheses with all unshifted
junctions n_i integral. In fact, every tuple satisfying (1)–(2) has
n_0 nonintegral.

This is a local RESEARCH/REPRODUCTION assembly under the prior SPECIALIZE
assessment `drafts/literature/2026-10-14-uniform-last-pair-integer-assembly.md`.
It organizes known local exclusions, without a new modular computation
or a claim of progress beyond the inspected sources. C063a and C067a
already exclude every intact order separately for the two surviving
allocations; their identity-order cases overlap this result. Neither
rational witness is refuted. Other allocations, arbitrary orders of the
larger-t family, actual-word applications and universal eventual descent
are outside this conclusion. The separate critical audit below found no
defect within this literal-family scope.

## Proof

The tails, literal table, domain, all 25 endpoints including the closing
edge, and non-strict guards are exactly L068's hypotheses. In particular
each guard uses the input of its own outgoing row. L068 gives a unique
real cyclic endpoint tuple for each permitted t, and proves that precisely
t=0,1 satisfy all guards. If 2<=t<=9250245, its row-24 guard is strictly
violated, contradicting (2). This includes the upper interval endpoint.
It remains to identify the two surviving endpoint roots.

At t=0 the tails are a_i=2 for i<24 and a_24=166504412. Thus (1)
is exactly the endpoint system of L055's literal tuple used by L056.
That known tuple satisfies every endpoint with these same parameters.
By L068's endpoint uniqueness, the tuple under consideration equals
that tuple, in particular at index 0. Its unshifted n_0=s_0-23/11
is therefore L056's root, not the shifted s_0. L056 identifies this
root as Phi/Delta for its complete chronological integer affine pair,
with Delta=2^630138897-3^397573379>0, Phi=4 modulo 5 and Delta=0
modulo 5. If n_0 were an integer m, Phi=m Delta would give Phi=0
modulo 5, a contradiction. Hence n_0 is nonintegral at t=0.

At t=1 the tails are a_23=20, a_24=166504394 and all others 2.
These match exactly L064's j=23 endpoint tuple used in L066, with
the same complete literal J,H table. L064's tuple satisfies every
endpoint including the modified closing edge. L068's endpoint uniqueness
therefore identifies the present tuple with that exact tuple. Thus
n_0=s_0-23/11 is precisely L066's unshifted root. L066 identifies it
as Phi/Delta for the changed-tail chronological integer pair, with
Phi=21 and Delta=5 modulo 25, and Delta>0. Reducing these residues
modulo 5 gives Phi=1 and Delta=0. An integer n_0=m would again force
Phi=m Delta, an impossibility modulo 5. The old-tail numerator is not
used in this case. Hence n_0 is nonintegral at t=1 as well.

The three cases exhaust the closed integer parameter interval. In either
surviving case, integrality of all n_i implies integrality of n_0, which
has just been contradicted. This proves the conclusion; it does not
assert that each individual n_i is nonintegral.

All affine-coordinate and residue results are imported from the audited
inputs rather than reproved or recomputed. Their standard affine input
is Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239, DOI
10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Only formal composition and the nonzero-denominator fixed-point formula
are used there: the words are nonempty, their counts are the stated N,K,
and positive Lambda ensures Delta!=0. Integer-itinerary sufficiency is
unused. The necessary specialization here is the exact tail and root
identification in each surviving case, not a reproof of that theorem.
Attempts 027–031 concern different orders and remain preserved; this
proof neither restarts their stopped prime diagnostics nor transfers
fixed-allocation rigidity to changed allocations.

### Separate critical audit — 2026-10-14

The prior SPECIALIZE assessment
`drafts/literature/2026-10-14-literal-family-integer-exclusion-audit.md`
approved this audit. The review found no defect in the existing
conjunction. It verifies the local reproduction; it adds no parameter
range, modular computation or theorem beyond the inspected inputs.

**Complete hypotheses and interval.** The complete 25-row J,H table
in L055 is the table used by all three direct inputs. C068a and L068
have identical literal indexing, both tail formulas, all 25 endpoint
equations, the lower domain and the same non-strict own-input J guards.
At the upper endpoint, 18*9250245=166504410, so the tails are
a_23=166504412 and a_24=2. At the lower endpoint they are 2 and
166504412. Throughout the closed interval their sum is 166504414;
the other 23 tails sum to 46. Thus neither the final tail nor an
endpoint of the permitted interval disappears from the comparison.
The integers in the interval partition into {0}, {1} and
{2,...,9250245}, with no omitted boundary or fractional parameter.

**Uniqueness before guards.** In L068's notation, every row in the
shifted system is exactly n_(i+1)=c_i(n_i+eta_i) after
n_i=s_i-23/11. This includes row 24 and s_25=s_0. The full
composition multiplier is P=3^K/2^N<1, from the unchanged counts
and the audited positive Lambda bound. L068's formula
n_25=P(n_0+B) therefore has the unique fixed point B/(1/P-1).
Equivalently, the difference of two endpoint solutions satisfies
d_25=P d_0 and d_25=d_0, forcing d_0=0 and then every d_i=0.
This is uniqueness among all real endpoint tuples, before imposing
domain, minimum or guard conditions. Consequently using a known tuple
to identify an arbitrary tuple does not transfer its extra H/seed or
minimum properties as premises.

For t>=2, L068's audited formula
n_24=eta_24/D+CA(1+D)2^(-18t)/D has positive coefficients and
D>0. Its row-24 right-minus-left margin strictly decreases. The
imported t=2 bound is less than
-474883782659/125000000000<-3.79<0, so the non-strict guard fails
at that same outgoing input for every remaining integer, including
9250245. No growth estimate for row 23 at large t, fixed minimum,
or sampling of the parameter interval is used. The audit reuses
L068's already audited boundary and uniform proof; it does not rerun
or extend its arithmetic certificate or its failed optional <-4 probe.

**Both survivor identifications.** At t=0 every row, including the
closing row, has exactly L055's original tail. The exact root in
L055 (3) satisfies this entire system. Endpoint uniqueness identifies
its index-0 shifted value with the current s_0. L056 (3) then gives
precisely n_0=s_0-23/11=Phi_0/Delta, where Phi_0 is an integer,
Delta=2^630138897-3^397573379>0, Phi_0=4 modulo 5 and
Delta=0 modulo 5. Thus an integer n_0 would contradict
Phi_0=n_0 Delta modulo 5. No claim about integrality of s_0 is used.

At t=1 the tails are exactly a_23=20 and a_24=166504394, with
all other tails 2. These are L064's j=23 tails at the same literal
rows, including the altered closing edge. Its exact root (3) is a
solution of the whole system, and uniqueness again identifies the
index-0 value. L066's coordinate passage explicitly gives
Phi_1/Delta=B/(2^N/3^K-1)=s_0-23/11 for these tails. Its changed
prefix t_24=306970766 and closing exponent D_24=323168131 sum to
the full N=630138897. Here Phi_1=21 modulo 25, so Phi_1=1
modulo 5, whereas Delta=5 modulo 25 gives Delta=0 modulo 5.
The identity Phi_1=n_0 Delta is again impossible for an integer n_0.
Phi_1 is not replaced by Phi_0. L066's reference to L065 identifies
the tuple; its proof and audit require no H guard, seed or parity
assumption for this coordinate match and nonintegrality conclusion.

**Conclusion and scope.** The rejected interval supplies no tuple;
in each survivor case the same cut n_0 is nonintegral. Since the
all-integral condition includes that cut, its exclusion follows.
It is unnecessary to show that every individual junction is
nonintegral. The direct mathematical inputs remain exactly L068,
L056 and L066; L055's table/root and L064's changed root are retained
through them. The DAG and assembled argument require no change.
The precise primary affine citation and Mathlib qualifications above
and below are retained without a new source claim or general reproof.
Both rational witnesses, the overlap with C063a/C067a, and Attempts
027–031 remain valid. Other orders/allocations, an actual-word
application, and universal eventual descent are not established here.

## Mathlib

Full matching coverage of this family conjunction was not checked; no
absence claim or formal verification is made. The ready assessment records
supporting valuation declarations `padicValRat.defn`, `padicValInt_dvd_iff`
and `Rat.num_or_den_zero_padicVal` in
[PadicVal.Basic at commit 2da3ab0a20dc0c66f56a557e37df39f7d36cb953](https://github.com/leanprover-community/mathlib4/blob/2da3ab0a20dc0c66f56a557e37df39f7d36cb953/Mathlib/NumberTheory/Padics/PadicVal/Basic.lean),
with prime, nonzero and coprimality qualifications. This assembly invokes
the existing nonintegrality results and needs no new valuation theorem.
