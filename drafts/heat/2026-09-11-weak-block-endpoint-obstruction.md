# Draft: weakly separated block endpoints — 2026-09-11

Test a_j=2^j, b_j=2^(j+1)-2 for j>=1, with extra mass
M_(a_j)=floor(4^j/j^2), zero elsewhere. These satisfy width <=2a_j
and a_(j+1)=b_j+2, with weighted sum <=sum 1/j^2.
If a nondecreasing finite-valued payoff F has generator <=C, the single
transition b_j -> a_(j+1) implies its interblock increase is at most
4C/M_(a_(j+1)). These upper bounds are summable. Thus an unbounded
payoff must have infinite total increase inside the blocks. A payoff
constant on blocks, even plus a bounded nondecreasing correction, fails.
The mass locations themselves are lacunary, so L113 supplies an actual
payoff: this is an obstruction to the endpoint-only method, not existence.

Checkpoint: unproved draft; resume by auditing floors, boundary j=1,
coverage of the intervening integers, the telescoping identity, and L113
hypotheses before promoting a result. The general adapted-ramp question
remains open.

Audit completed: Lemma 116 stores the proved result. Reciprocal masses
are summable using floor(t)>=t/2 for t>=1. Finite telescoping proves
that infinite total within-block variation is necessary and sufficient
for unboundedness when the generator is bounded. This also excludes a
bounded nondecreasing correction to block-constant growth. L113 applies
to these masses, so there is no counterexample to payoff existence.
