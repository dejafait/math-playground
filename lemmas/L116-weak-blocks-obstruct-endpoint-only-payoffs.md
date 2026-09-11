# Lemma 116: weak blocks obstruct endpoint-only payoffs

**Hypotheses.** For j≥1 set a_j=2^j and b_j=2^(j+1)−2.
Put M_(a_j)=floor(4^j/j²), put M_l=0 at all other positive
integers, and put m_l=1+M_l. For a finite-valued nondecreasing real
function F on the positive integers define the nonnegative generator

QF(k)=Σ_(l>k) m_l(F(l)−F(k))/(l−k)².

**Conclusion.** These blocks satisfy a_j≤b_j≤2a_j and
a_(j+1)=b_j+2, and Σ_l M_l/l²<∞. If sup_k QF(k)=C<∞, then

Σ_(j≥1) [F(a_(j+1))−F(b_j)]<∞.                    (1)

Such an F is unbounded if and only if

Σ_(j≥1) [F(b_j)−F(a_j)]=∞.                        (2)

In particular no nondecreasing unbounded payoff constant on each block
has bounded generator. Nor can one obtain a bounded-generator unbounded
payoff as F=P+B, where P is nondecreasing and constant on each block
and B is bounded and nondecreasing.

Nevertheless these same counts admit a positive strictly increasing
unbounded payoff with bounded generator and Σ_l m_l F(l)/l²<∞.

## Proof

The block inequalities follow directly from their formulas, including
the singleton first block [2,2]. The extra weighted mass is bounded by
Σ_(j≥1) 1/j²<∞. For every integer j≥1, 2^j≥j (by induction),
so 4^j/j²≥1. The elementary bound floor(t)≥t/2 for t≥1 gives

M_(a_j)≥4^j/(2j²)>0,
Σ_(j≥1) 1/M_(a_j)≤2Σ_(j≥1) j²/4^j<∞.

The last series converges, for example by the ratio test.
For each j the term with k=b_j and l=a_(j+1) in QF(k) has
denominator 4. Since all terms are nonnegative,

0≤F(a_(j+1))−F(b_j)≤4C/m_(a_(j+1))
 ≤4C/M_(a_(j+1)).

Summing proves (1). No interchange involving signed series occurs.
For every J≥1 the finite telescoping identity is

F(a_(J+1))−F(a_1)
 =Σ_(j=1)^J [F(b_j)−F(a_j)]
  +Σ_(j=1)^J [F(a_(j+1))−F(b_j)].

All summands are nonnegative, and the second sum stays bounded by (1).
Since a_J→∞ and F is nondecreasing, F is unbounded exactly when
F(a_J)→∞. This proves the equivalence with (2). It also controls the
single intervening integer b_j+1: its value lies between F(b_j) and
F(a_(j+1)), so no uncounted growth can hide in a gap. The finite
prefix before a_1 has no effect on unboundedness.

For block-constant F, the series in (2) is zero. If F=P+B as in
the conclusion, its within-block increments equal B(b_j)−B(a_j).
The ordered disjoint blocks and monotonicity give, for every J,

Σ_(j=1)^J [B(b_j)−B(a_j)]≤B(b_J)−B(a_1)
 ≤sup_l B(l)−B(a_1)<∞.

Thus (2) again fails, proving the claimed obstruction even with this
bounded correction.

Finally apply Lemma 113 with n_j=2^j and masses floor(4^j/j²).
The locations satisfy n_(j+1)=2n_j and the required weighted series
was checked above. Its conclusion supplies the asserted payoff,
including its weighted integrability and bounded generator. Therefore
this example does not obstruct payoff existence. ∎

## Qualifications

This is a scoped obstruction to transporting block-constant endpoint
constructions to additive separation. In particular it rules out a
nondecreasing unbounded sum of jumps after block endpoints plus a bounded
nondecreasing correction. It does not rule out growth inside blocks;
indeed such growth is necessary here and an existing construction
provides it. Arbitrary masses throughout weakly separated blocks,
unrestricted summable counts, general coordinate selection and RH remain
unproved. Lemma 115 is a comparison, not an input.

## Verification and formalization obligations

The proof is analytic and needs no numerical certificate. Check the
floor lower bound, summability of reciprocal masses, the distance-two
single-term bound, finite telescoping, the singleton first block, the
intervening integers and bounded-correction variation. Formalization
would require these elementary sequence arguments and the payoff
existence statement of Lemma 113. No claim about arbitrary adapted
ramps is used as an input.
