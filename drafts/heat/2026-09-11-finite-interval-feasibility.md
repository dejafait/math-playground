# Finite-interval feasibility draft — 2026-09-11

For positive integer counts with sum m_l/l^2 finite, set
A_kn=sum_{l>n}m_l/(l-k)^2 for k<=n, and zero otherwise.
For increments supported on [1,N], the exact generator constraints are
A_N d<=1: destination tails must NOT be truncated at N.
Let C_N=max sum d_n under these constraints and d>=0.
Each d_n<=1/A_nn<=1, so this is a compact finite problem.

Candidate equivalence: an infinite feasible increment sequence of infinite
total mass exists iff sup C_N=infinity. Necessity is truncation;
sufficiency mixes finite feasible vectors of mass at least 2^j with
weights 2^-j. This avoids the loss of mass in a coordinatewise limit.
Finite linear-programming duality gives covering vectors y>=0,
sum_{k<=n}y_k A_kn>=1, of cost C_N. If capacities are bounded,
a diagonal limit yields a summable infinite covering vector, because
each fixed column uses only finitely many rows. Conversely a summable
cover bounds the total mass of every feasible increment vector by Tonelli.

Checkpoint: candidate statements remain unproved pending an audit of full
tail finiteness, dual attainment, diagonal limits, and weighted payoff
integrability. Resume by writing a self-contained finite duality argument
or citing the standard finite-dimensional linear-programming duality theorem.
Neither capacity divergence nor existence of a cover is established for
general summable counts.

Audit completed: the precise alternative and payoff equivalence are proved
in Lemma 118. Finite strong duality suffices; no infinite duality is used.
The bounded-capacity diagonal limit preserves each covering inequality
because its column has only finitely many nonzero entries. The first
primal row supplies weighted integrability. The unresolved question is
whether any admissible counts can admit a summable cover.
