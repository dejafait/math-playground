# L111 — Positive distance-product factors exist without capacities

## Hypotheses

Let V be all 68-subsets of a fixed 1024-point set, let
H=binomial(1024,68), and put i(A,B)=|A\B|. Use the exact data of
L021 and L098:

    N=floor(65537^28/2^128)+1, U=binomial(1024,64)/binomial(68,64),
    g_i=binomial(68,i)binomial(956,i), alpha=2(N-1)/(U-1),
    c_0=1, c_1=...=c_4=0, c_i=alpha*a_i/(2g_i) (5<=i<=68).

Here a_i is L021's exact rational vector. In particular N>2,
c_i>0 for 5<=i<=68, and sum_(i=0)^68 g_i*c_i=N, with g_0=1.
For every unordered distinct edge e={A,B} prescribe
d_e=(N-2)c_{i(A,B)}. A permitted triangle is an unordered triple of
distinct members of V whose three half-distances are all at least five.
Use every such actual triangle, not a formal set of distance triples.
Triangles incident with a distance-1,...,4 edge must have weight zero.
No upper capacities or other scalar/PSD conditions are hypotheses.

## Conclusion

There exist finite positive real factors f_i, 5<=i<=68, such that,
with x_i=c_i*f_i, the assignment

    z_{A,B,Z}=x_i*x_j*x_h  on every permitted triangle,
    z_{A,B,Z}=0           on every other distinct triangle

(where i,j,h are its three half-distances) satisfies, on every distinct
edge A,B,

    sum_(Z distinct from A,B) z_{A,B,Z}=(N-2)c_{i(A,B)}.       (1)

Every permitted triangle has strictly positive weight. All null-edge
demands remain zero. Restoring the two endpoint repetitions with value
c_i gives L098's full contraction N*c_i, and the coincident-support
row is its unchanged objective identity.

This is a REPRODUCTION/specialization of a known finite entropy-projection
theorem, with local support and symmetry proofs. It removes the existence
hypothesis from L110's ansatz. It neither establishes upper capacities
z<=min(c_i,c_j,c_h) nor Boolean lower scalar rows, a full feasible source
lift, PSD, an actual packing or RS realization. L110's excessive sufficient
allowance and ATTEMPTS/082,093 remain parked. The 955–957 bracket is
unchanged. The separate critical audit below retains this specialization,
conditional on its stated imported inputs, without a capacity conclusion.

## Proof

**Inputs and imported theorem.** L021 supplies a_i>0 and sum a_i=U-1;
L098 supplies the fixed pairs, exact N, and the homogeneous contraction
including repetitions. Thus sum_(i=1)^68 g_i*c_i=N-1. L108 supplies
coordinate-permutation transitivity on each edge-distance class and
actual equilateral triangles at every positive distance. Its cone
membership conclusion is not used as a strict-support assertion.
L109 supplies the full actual orbit ranges and their multiplicities;
L110 supplies the complete equilateral completion count used below.

Import Imre Csiszár and Paul C. Shields, *Information Theory and
Statistics: A Tutorial*, Foundations and Trends in Communications and
Information Theory **1**(4) (2004), 417–528, DOI 10.1561/0100000004,
[author PDF](https://www.renyi.hu/~csiszar/Publications/Information_Theory_and_Statistics:_A_Tutorial.pdf),
Theorems 3.1–3.2 with proofs, pp.440–443; Remark 3.1, p.444.
For a strictly positive reference probability Q on a finite alphabet,
a nonempty closed convex family has a unique relative-entropy projection,
whose support is the support of that family. For a linear family with
full support the projection belongs to the associated finite-parameter
exponential family; with smaller support only its closure is guaranteed
in general. In particular, with features a_e and prescribed expectations,
full support gives real multipliers lambda_e and

    P*(T)=Q(T)*exp(sum_e lambda_e*a_e(T))/Z,                 (2)

where Z is the positive normalizing constant. No independence of the
features is required. These exact support, dependent-feature and boundary
cases were inspected in the prior SPECIALIZE assessment
`drafts/literature/2026-10-23-positive-triangle-factor-existence.md`.
We import this theorem, not an iterative-scaling convergence claim.
What follows verifies its finite local hypotheses and specialization;
there is no reproof of entropy duality.

**Full feasible support, before using entropy.** Let E_+ be the set of
unordered edges at distances 5,...,68, and let T_+ be all permitted
triangles. For an edge e of distance i>=5, let k_i be the number of
T in T_+ containing e. This is independent of the chosen edge: a
coordinate permutation transports both endpoints and all completions.
It is finite. The number of its equilateral completions is, by L110,

    E_i=sum_(t=max(0,2i-68))^i
        binomial(i,t)^2 binomial(68-i,i-t)binomial(956-i,t).

In particular E_i>=binomial(956-i,i)>0, using the t=i summand.
All these completions are permitted when i>=5. Hence k_i>=E_i>0.
Set d_i=(N-2)c_i>0 and choose the single positive real number

    eta=(1/2)*min_(5<=i<=68) d_i/k_i,
    r_i=d_i-eta*k_i >= d_i/2 > 0.                         (3)

Give every T in T_+ the baseline weight eta. In addition, give every
equilateral distance-i triangle weight r_i/E_i. Equivalently define

    w_T=eta+r_i/E_i  if all three sides have distance i,
    w_T=eta          otherwise.

There is at most one such i for a triangle. A distance-i edge receives
eta*k_i from the baseline and exactly E_i copies of r_i/E_i from
the correction; equilateral triangles of other distances do not contain
that edge. Its marginal is d_i. Give every triangle outside T_+ weight
zero. No permitted triangle contains a null edge, so every null-edge
marginal is zero as required. This is a strictly positive feasible
weighting on the entire alphabet T_+, not just cone membership or a
boundary-limit construction. It asserts no capacity bound on w.

**Mass and reference normalization.** Every triangle in T_+ has exactly
three distinct edges in E_+. For any feasible weighting its total mass
is therefore forced to be

    S=(1/3)*sum_(e in E_+) d_e
     =H*(N-2)/6 * sum_(i=5)^68 g_i*c_i
     =H*(N-2)*(N-1)/6 > 0.                              (4)

The second equality uses H*g_i/2 unordered distance-i edges, as in
L108. There is no integrality requirement on S. For T in T_+ put
b_T=product_(e in T)c_{i(e)}>0, B=sum_(T in T_+) b_T, and Q(T)=b_T/B.
The alphabet is finite and nonempty, so 0<B<infinity and Q is a strictly
positive probability distribution. On this alphabet take the features
a_e(T)=1 if e belongs to T and 0 otherwise, one for each e in E_+.
The desired linear family L consists of probabilities P satisfying

    sum_T P(T)*a_e(T)=d_e/S  for every e in E_+.           (5)

It is a closed convex linear family in the finite probability simplex.
The probability w/S constructed above belongs to it and is strictly
positive at every T. Thus L is nonempty and has full support. The
identity sum_e a_e(T)=3 agrees with sum_e d_e/S=3 by (4);
dependent features create no extra hypothesis in the imported theorem.
Null edges have feature identically zero on this alphabet and expectation
zero; removing those vacuous features loses no full-model equation.

Apply the imported theorem to obtain its unique positive projection P*
and real potentials in (2). Put z*_T=S*P*(T). Then (5) gives every
positive-edge demand exactly, and

    z*_T=K*b_T*exp(sum_(e in T) lambda_e),
    K=S/(B*Z)>0.                                        (6)

All sums, potentials and constants are finite; no infinite-alphabet
limit, attainment inference from cone membership, or numerical solve
is being used.

**Distance factors from log potentials.** Let G=S_1024 act by coordinate
permutation on actual supports, edges and triangles. This action preserves
T_+, all distances, b_T, Q, S and d_e, so it preserves L and relative
entropy to Q. Uniqueness of P* therefore implies P*(sigma T)=P*(T)
for every sigma in G. In particular z* and b are invariant.

Start with any real potential representation (6) and set

    lambda_bar(e)=(1/|G|)*sum_(sigma in G) lambda_(sigma e).

For each fixed T, the logarithm of (6) on sigma T gives

    sum_(e in T) lambda_(sigma e)
      =log(z*_(sigma T)/(K*b_(sigma T)))
      =log(z*_T/(K*b_T)).

Averaging this equality over G shows that replacing lambda by
lambda_bar in (6) leaves every weight unchanged. This averages real
log potentials, not positive factors, and does not require uniqueness
of the multiplier representation. Edge transitivity from L108 makes
lambda_bar(e)=ell_i depend only on the edge's distance i. Set

    f_i=K^(1/3)*exp(ell_i)>0, x_i=c_i*f_i (5<=i<=68).

Every actual triangle has three edges, even when some distances coincide.
Thus (6) becomes z*_T=x_i*x_j*x_h exactly; the three factors absorb K
once. Extension by zero outside T_+ proves (1) on all distinct edges.
The averaging applies to this ordinary unlabeled finite marginal problem
only; it asserts no symmetry of actual-label RS restrictions.

**Original orbits, repetitions and null demands.** At a fixed edge of
distance i, L098 and L109 give, for every actual (i,j,t,s),

    D(i,j,t,s)=binomial(i,t)binomial(68-i,j-t)
              binomial(i,s)binomial(956-i,j-s),
    max(0,i+j-68)<=t<=min(i,j),
    max(0,i+j-956)<=s<=min(i,j), h=i+j-t-s,

with 0<=i,j<=68. These count individual third supports once each.
Assign each distinct orbit its just-constructed value x_i*x_j*x_h when
all sides are permitted, and zero otherwise. Consequently, for every
i>=5, equation (1) is precisely

    sum_(actual j,t,s with j,h>=5) D(i,j,t,s)*x_i*x_j*x_h
      =(N-2)c_i.                                        (7)

This sum retains every t,s and its full coefficient; no distance-only
multiplicity replaces D. Different actual t-s classes can receive equal
values in this ansatz, but are not identified as source variables.
L109's eight-atom permutation argument retains all six presentations
and t-s. The ordered count at an index is H*g_i*D; after summing over
all distinct indices, division of the total by six counts unordered
triangles. An individual index need not contain all six presentations.
Coinciding distance keys do not change the six orders of distinct
supports. Equation (7) itself is at a fixed edge and requires no division
by six.

For i>0 the two removed terms Z=A and Z=B have respectively
(j,t,s)=(0,0,0),(i,i,i), coefficient D=1 each. Assign them c_i as
Boolean repetitions, adding exactly 2*c_i. For i=1,...,4 both repeated
terms and all distinct incident triangles are zero, so their full rows
are zero identities. For i=0 there is no distinct edge: t=s=0, D=g_j,
and every term is the repeated value c_j (including c_0=1). That row
is sum_j g_j*c_j=N, already true. No zero c_i has been divided out.
All original contraction rows and required presentation equalities are
therefore respected by this orbit array. This conclusion concerns those
rows only: no upper/lower scalar inequalities, remaining source matrices
or representing distribution follow from it.

The continuation test is met: full support and normalization have been
verified, and the imported finite theorem gives the requested positive
distance factors. This separates existence from the unresolved true
capacity problem; it does not rescue L110's equilateral-only capacity
certificate or enlarge its conclusion.

**Independent critical audit (2026-10-23, step 418).** The approved
assessment is `drafts/literature/2026-10-23-l111-positive-factor-critical-audit.md`.
This audit checks the complete specialization above, using L021's exact
positive vector and sum as an established input; it does not rerun or
claim a fresh audit of the Delsarte LP. It imports the same inspected
Csiszar–Shields Theorems 3.1–3.2 and Remark 3.1, with the citation and
qualifications given above. No convergence theorem or entropy reproof
is substituted for them. All checks below are symbolic and cover their
entire stated finite ranges; no sampled enumeration or approximate
factor residual is used.

First, N>2 follows already from 65537>2^16, so the threshold exceeds
2^320. Since U-1=sum a_i>0, alpha and each permitted c_i are positive,
and direct substitution gives sum_(i>=5) g_i*c_i=N-1. Thus each d_i
is strictly positive. The distinct-edge stabilizer count k_i is finite
and invariant because its coordinate permutation transports the whole
permitted completion set, not just one orbit. For the equilateral count,
fix A,B at distance i and choose r points of A intersection B in Z.
Equal distances require 68-i-r points in each pair-only region and
2i+r-68 points outside A union B. Setting r=68-2i+t gives exactly
the displayed E_i term and the full interval max(0,2i-68)<=t<=i.
Its t=i term chooses all the common core and i outside points, and is
positive because 956-i>=i. This proves k_i>=E_i>0 for every permitted
distance, including i=68. No repeated support is counted here.

The minimum in (3) is over precisely 64 positive finite ratios. Therefore
eta>0 and eta*k_i<=d_i/2 for every i. An equilateral correction for i
affects only distance-i edges. Each such edge sees E_i corrected
triangles, so its total is eta*k_i+E_i*r_i/E_i=d_i. This establishes
strict positivity at every alphabet element before applying the source;
having some equilateral support alone would not have sufficed.

Second, count ordered distinct edges from each of H supports to its
g_i distance-i neighbors, divide by two, and then sum each triangle's
three edge incidences. This gives 3*sum_T w_T=
H*(N-2)*(N-1)/2, proving (4) without an unstated normalization factor.
It follows that w/S is a probability with all the required expectations
d_e/S. The reference is separately Q=b/B, not b/S. Both S and B are
finite positive reals. The closed finite linear family is nonempty and
its union of supports is the entire alphabet. These are exactly the
full-support hypotheses of the imported projection theorem. In
particular sum_e a_e=3 is an allowed feature dependence; no independent
constraint basis or interior in the ambient simplex is assumed.

Third, the finite group action preserves both the constraint vector
with permuted edge indices and the reference probability. Uniqueness
of the projected probability therefore gives its invariance. For any
one finite real multiplier representation, evaluating its log formula
at sigma T and averaging yields the same log weight at T. Reindexing
the group average shows that lambda_bar is constant on each edge orbit.
There is no inference that the original multiplier vector is unique,
and no averaging of products is used. Equation (6) has K=S/(B*Z),
so three factors K^(1/3)*exp(ell_i) reproduce exactly K, also on
equilateral triangles. All factors remain finite and strictly positive.

Finally reconstruct the source indexing directly from named atoms.
For an ordered triple A,B,Z of 68-sets, its eight regions are

    A only: t;       B only: i-s;       Z only: j-s;
    AB only: j-t;    AZ only: i-t;      BZ only: s;
    ABZ: 68-i-j+t;   outside: 956-i-j+s.

Their nonnegativity is exactly the two displayed t,s ranges. Conversely
any such partition gives three 68-sets with distances i,j,h=i+j-t-s.
For fixed A,B, choose the removed points in A\\B and A intersection B,
then the added points in B\\A and outside A union B. The respective
choice counts are binomial(i,t), binomial(68-i,j-t), binomial(i,s),
binomial(956-i,j-s), giving every D in (7) once, including zero atoms.
For each possible anchor, singleton-minus-opposite-pair atom size is
respectively t-s, (i-s)-(i-t), or (j-s)-(j-t), always t-s. Swapping
the two other supports only interchanges their distances. Thus all six
presentations preserve the source equality invariant and the product
weight. Their total ordered count is H*g_i*D=1024!/product(atom!),
so summing over the full distinct-index set and dividing by six counts
unordered triangles exactly. Repeated distance keys do not reduce the
six orders of three distinct supports, and this division is not used
in a fixed-edge contraction. Different t-s classes keep their own D.

The excluded positive distances 1,...,4 have zero incident distinct
weights. At every i>0, Z=A and Z=B give the two different indices
(0,0,0) and (i,i,i), each with D=1; their Boolean values add 2*c_i,
including c_i=0. At i=0 the two endpoints coincide and must not be
removed twice: all entries have t=s=0, D=g_j and value c_j, so the
row is exactly sum_j g_j*c_j=N. This verifies all original contraction
rows and required presentation equalities without dividing by a null
pair. It asserts only an orbit array satisfying these equations, not
a probability distribution on codes or a fully feasible source lift.

No failed equality or unmet imported hypothesis was found. The critical
audit retains positive-product existence and all original contractions;
it supplies no bound on x_i*x_j*x_h/min(c_i,c_j,c_h). L110's excessive
allowance, ATTEMPTS/082,093, the independent capacity/Boolean/PSD/RS
gaps and the 955–957 bracket remain unchanged. No numerical solve,
capacity recomputation, new lemma or mathematical script was needed.

## Mathlib

Full matching finite entropy-projection theorem and this positive
distance-product specialization: not checked. Supporting finite
probability, convexity, coordinate-group averaging and subset-counting
coverage: not checked. Unknown coverage is not evidence of absence;
no Mathlib theorem is assumed.
