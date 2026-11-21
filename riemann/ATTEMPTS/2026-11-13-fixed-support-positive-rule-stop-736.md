# Fixed35-label family: original-residual obstruction736

The approved fixed k10 support-label family fails at its first new
block k=11. See canonical [C998w Section7](../lemmas/C998w-support-grid-original-measure-residual-partial.md)
and `scripts/separation-seven/fixed-support-separator-replay-736.json`.
The Gram and residual-centered interpolation inclusions pass, but a
cardinal polynomial has negative ORIGINAL integral. Exact original-atom
verification gives every nonnegative rule on these35 nodes residual
epsilon>1/1000, versus the required epsilon<=5e-19.

WHY IT FAILS: Uniform invertibility and interval contraction do not
give a nonnegative moment representation on a prescribed square support.
The negative cardinal integral separates the original moment functional
from the cone of nonnegative weights on these SAME35 nodes, even with
the allowed tiny residual. More iterations, tighter interval arithmetic
or a different inverse cannot repair this support at k=11. The full129
grid, added nodes, changing supports and other mechanisms are not excluded.
The three k8-10 rules and all earlier stops remain valid. No RH inference.

An untested next nomination adds ONE common unused grid label, creating
a36-node moment problem with one weight degree of freedom. This changes
the feasibility mechanism; it is not another attempt to make the rejected
35-node rule positive. Exact source coverage, uniform feasibility and
the complete cost/storage gate remain unassessed. Separate literature
approval is required before any such calculation.
