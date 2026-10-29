# L127 — Paired reachable generators already require superlinear support

## Hypotheses

Work over F₂. For every k>=0 let N=2^k and retain L122 §2's entire
original right-closed endpoints A=Prod(F_N,G_N), B=Prod(G_N,F_N).
Both coordinate orders are `s,f0,...,fN,h0,...,hN,t`, including all
zero-residual coordinates and three constant product connectors.
Use their literal alpha_A,alpha_B,M_A,M_B,beta_A,beta_B. Define

    v_ell=(alpha_A M_A^ell,alpha_B M_B^ell),
    K_N=span_F₂{v_ell:ell>=0}.

A finite generating family H consists of rows of K_N spanning K_N.
Its total expanded scalar support is sum_(h in H) wt(h) in the two
original endpoint blocks, with no coordinate quotient or compressed
XOR charging. The endpoint occurrence size is S=16N+20.

## Conclusion

Every such H satisfies

    sum_(h in H) wt(h) >= 2(1+sqrt(2))^k.                 (1)

In particular, total generator support/S is unbounded; there is no O(N)
total expanded-support generating family for this K_N. This stops the
assessed linear-generator proposal, without assuming K_N=E_N or importing
L126's full-basis conclusion for a smaller space.

At N=4, exact complete evidence gives dim(K_4)=9, A_f parameter-projection
rank 4, exact weight-0-through-4 counts `[1,0,1,6,8]`, threshold-span ranks
`[0,0,1,4,7]` and minimum basis support 38. These finite statements do not
prove the uniform bound; (1) rests on the proof below.

This is a local POTENTIALLY_NEW obstruction relative to the bounded
source comparison, not a certified originality claim. The uniform argument
was written at step 549; its separate conceptual audit passes in §7
(step 551, REPRODUCTION).
It is not a complete P versus NP candidate. No conclusion about arbitrary
chains, changed endpoint coordinates, general operands, mixed letters,
or unrestricted complexity is claimed. This lemma quantifies generators
of K_N; any application to another row space requires its own justification.

## Proof

### 1. Coverage, imported input and scope

Use the unchanged pre-invocation EXPLORE assessment
`drafts/literature/2026-10-28-paired-reachable-generator-support.md`
and its step-548 source notes. The qualitative paired reachable
common-source construction is known: Ésik–Maletti, *Simulation vs.
Equivalence*, 2010 author manuscript, Definition 3.1/Theorem 4.2, pp.2–3
([primary manuscript](https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf)).
F₂ satisfies its Noetherian-semiring hypothesis: subsemimodules of finite
free F₂ modules are finite-dimensional vector subspaces. That theorem
supplies no original-coordinate expanded-support estimate. Its existence
construction is downstream motivation, not a premise proving (1), and is
not reproved here.

The quantitative input is L126 §3, equations (5)–(7), whose induction,
coordinate identification and cancellation cases were separately audited
in L126 §7. For every row h=(u,v) of E_N={uR_A=vR_B}, let

    r_j=u_(f_(N-1-j))   (0<=j<N).

L125 §2 and L126 §1 identify this as the reversed A_f parameter block.
The core is `(r,(r+b)P_N; b,rP_N)` for some b, while the other original
coordinates are disjoint. Consequently their established individual-row
bound says

    r_j=1  ==>  wt(h)>=2*(sqrt(2))^popcount(j).          (2)

Only this individual-row inequality is used. The full-E_N determinant
conclusion is not used. The new obligations are membership in E_N,
full rank of this one projection for K_N, and distinct-row charging.
No surjectivity of the combined (r,b) projection is needed or asserted.

### 2. Membership in the residual relation

L122 §2's original endpoints have the same accepted polynomial
`z^N(1+z)^N=z^N+z^(2N)`. In particular, for every q>=0,

    alpha_A M_A^q beta_A=alpha_B M_B^q beta_B.

For a fixed ell, the coefficient of z^m in
`alpha_A M_A^ell R_A(z)` is `alpha_A M_A^(ell+m) beta_A`,
and the analogous coefficient for B is equal, for every m>=0.
All series here are finite, because the occurrence graphs and right-closed
letter transitions are acyclic. Thus v_ell belongs to E_N. By linearity
K_N is a subspace of E_N and every generator h in H obeys (2).
Equality of accepted polynomials is used only for this residual membership;
it does not assert a sparse simulation or a support bound by itself.

### 3. Full rank of the original A_f projection

For 0<=i<N, write a_ell(i) for the f_i coordinate of alpha_A M_A^ell.
By L122 §2, alpha_A has coefficient 1 at every f_i, and the only
transitions entering f_i in A are from f_j with 0<=j<i, each with
coefficient 1. Neither h, s, t nor f_N contributes an incoming entry.
Therefore

    a_0(i)=1,
    a_(ell+1)(i)=sum_(j=0)^(i-1) a_ell(j) in F₂.

Induction on ell, using the integer hockey-stick identity reduced modulo
two (with binom(i,ell)=0 for ell>i), gives

    a_ell(i)=binom(i,ell) mod 2.                         (3)

The sum is empty for i=0, so this also handles all edge cases. The N by N
matrix with rows ell=0,...,N-1 and columns i=0,...,N-1 has entries (3).
It is upper triangular, with diagonal 1, and hence invertible over F₂.
Reversing its columns to the r_j order is a permutation and preserves rank.
These are projections of actual rows v_0,...,v_(N-1) in K_N. Thus the
projection pi:K_N->F₂^N, pi(h)=r, is surjective. This conclusion includes
N=1, where the matrix is [1]. It requires neither dim(K_N)=dim(E_N)
nor an assumption about a basis of the full relation.

### 4. An N-column minor charges different generators

Since H spans K_N and pi is linear and surjective, the projected rows
{pi(h):h in H} span F₂^N. Extract N independent projected rows, retaining
their distinct original generators h_1,...,h_N. Their N by N parameter
matrix Q is invertible. Its nonzero determinant has at least one nonzero
Leibniz term: if every term vanished, its determinant would vanish.
Fix such a term. It selects one nonzero r_j in each selected generator,
using every j=0,...,N-1 exactly once. Apply (2) to that selected entry in
each row. No row is charged twice. The unselected generators have
nonnegative weights, so

    sum_(h in H) wt(h)
      >= sum_(j=0)^(2^k-1) 2*(sqrt(2))^popcount(j)
       = 2 sum_(d=0)^k binom(k,d)(sqrt(2))^d
       = 2(1+sqrt(2))^k.

This proves (1), including k=0. For all k>=0,
S=16*2^k+20<=36*2^k, so

    sum_(h in H) wt(h)/S
      >= (1/18)*((1+sqrt(2))/2)^k -> infinity.           (4)

The base is strictly greater than one. Arbitrarily many redundant
generators cannot evade the projection minor or reduce their total
nonnegative support. No finite threshold-rank extrapolation enters (4).

### 5. Complete N=4 discriminant and its independent receipt

`scripts/batched-incidence/check_paired_reachable.py` reuses the literal
endpoint constructor of `check_weight_filtration.py`: it saves every
occurrence, topological order, constant closure, letter action, boundary
and residual column. It constructs all paired Krylov rows through the
first zero, checks residual membership, and tests every original-coordinate
subset of weight at most four by exact binary reduction. There are
12,951/12,951 subsets, with exact passing counts `[1,0,1,6,8]`.

The complete nonzero Krylov sequence, in bit order consisting of the
stated A coordinate order followed by B, is

    [266367,524436,1048856,2097680,12840032,
     82048,98560,66048,8522752],

followed by zero. Its rank is 9. Its reversed r projections are
`[15,5,3,1,0,0,0,0,0]`, of rank 4. Every one of the 512 linear
combinations is saved; there are no omitted coordinate factors.
The ranks of spans of ALL vectors of weight <=w are

    w:     0 1 2 3 4 5 6 7 8 9   (rank remains 9 thereafter)
    rank:  0 0 1 4 7 7 8 8 8 9.

Greedy insertion by weight attains total basis support 38. For a lower
bound, any 9-row basis has at most r_w rows of weight <=w, so its support
is at least sum_(w=0)^23 (9-r_w)=38. A generating family contains a basis
subset and cannot have smaller total support. This proves the finite
minimum, separately from the uniform bound (1).

`audit_paired_reachable.py` imports no constructor module. It receives the
entire literal occurrence multiset, computes constant closure by powers
and right closure by set symmetric differences, and compares every M row
against L122 §2's explicit formulas. It regenerates the Krylov sequence,
checks rank and every residual equality, and enumerates its entire span
by symmetric differences. Filtering all 512 codewords by weight gives
exactly the constructor's complete low-weight buckets. Independent
lowest-pivot elimination checks every threshold rank, projected rank,
witness independence and basis optimality. Both scripts complete with
empty failure lists. Full certificates are
`scripts/batched-incidence/output-549/paired-reachable.json` and
`scripts/batched-incidence/output-549/audit.json`.

Reproduction commands (each run independently):

```bash
python3 scripts/batched-incidence/check_paired_reachable.py \
  --output /tmp/p-vs-np-paired-549/paired-reachable.json
```

```bash
python3 scripts/batched-incidence/audit_paired_reachable.py \
  /tmp/p-vs-np-paired-549/paired-reachable.json \
  --output /tmp/p-vs-np-paired-549/audit.json
```

### 6. Limitations and audit scope

The finite rank deficit 7<9 does not itself refute O(N). The uniform
obstruction uses the proved projection surjectivity, the previously
audited row inequality and the one-entry-per-row minor. The separate
conceptual review in §7 checks these bridges and every original-coordinate
qualification. No sparse shift, literal common-source realization,
actual-input reception, general certificate availability or total
interpreter bound is established. No failure of an approach resolves
P versus NP. Attempts 058/059 retain their original scopes; this is the
distinct paired-reachable proposal's obstruction, now separately audited.

### 7. Separate conceptual audit — 2026-10-29, step 551

**Verdict: the stated K_N generator obstruction passes.** This is an
independent audit/reproduction of the existing argument, not a stronger
theorem or a claim of progress beyond the checked sources. The unchanged
ready EXPLORE assessment
`drafts/literature/2026-10-29-paired-reachable-support-conceptual-audit.md`
and its step-550 primary-source comparison are reused. The standard
qualitative common-source theorem in §1 supplies no quantitative premise.
The quantitative premise is precisely L126 §3's individual-row bound,
whose proof and separate §7 audit were checked, together with L125 §2's
original-coordinate parametrization and L122 §2's literal closed rows.

**Membership uses every residual coefficient.** A right-closed letter
step follows a forward letter edge and then a constant tail. Thus it
still moves forward in the graph's topological order; M_A and M_B are
nilpotent, even though B's displayed coordinate order is not topological.
With the unchanged beta, the full residual column is
`R_H(z)=sum_(m>=0) z^m M_H^m beta_H`. All these sums are finite.
The literal path products have accepted polynomial
`z^N(1+z)^N=z^N+z^(2N)` over F₂. Hence, for every ell,m>=0, the
coefficient at z^m in the residual of alpha_H M_H^ell is the common
accepted coefficient at z^(ell+m). This proves v_ell is in E_N for
every ell, including ell=0 and the zero rows after nilpotence. Linearity
then proves K_N is contained in E_N. Equality of the accepted polynomials
alone has not been mistaken for a coordinatewise transition equality.

**The projection uses incoming entries and the original indexing.**
In A, the f_i column, 0<=i<N, receives exactly the entries from
f_j with j<i. No h row enters this block; s,f_N,h_N,t have zero
closed rows. Although alpha_A includes f_N, that coordinate contributes
nothing to any later f_i. Its inclusion, and all other zero-residual
coordinates, are retained in the full rows and in the support count.
Thus the recurrence in §3 holds literally. Starting with
`a_0(i)=1=binom(i,0)`, the integer hockey-stick identity gives
`sum_(j=0)^(i-1) binom(j,ell)=binom(i,ell+1)`; reduction modulo two
commutes with this finite sum. The zero convention covers ell>i, and
the sum at i=0 is empty. Therefore the first N projected Krylov rows
have entries binom(i,ell), zero below the diagonal and one on it.
They are invertible over F₂. Replacing column i by column j=N-1-i
is exactly the reversal required by L125, not a transpose or an
unverified change of coordinates. It preserves rank, so pi(K_N)=F₂^N.
No inference about the other parameter block or dim(E_N) is needed.

**The row inequality survives cancellation and projection.** In the
reversed original core, h has blocks `(r,(r+b)P_N;b,rP_N)` for some b.
These blocks occupy distinct coordinates. Consequently
`wt(h)>=wt(r)+wt(rP_N)` irrespective of b or cancellation inside
(r+b)P_N. If r_j=1, the multilinear polynomial f_r is nonzero and
has degree at least popcount(j). L126's support-product inequality
gives `wt(r)*wt(rP_N)>=2^deg(f_r)`. AM–GM yields (2). The six
zero-residual coordinates and the paired final coordinate cannot cancel
a core entry. They only increase the full row weight. This is the
individual-row inequality, not L126's full-E_N generating-set theorem.

**The minor transfers the quantifier to every finite generating family.**
Since pi(H) spans F₂^N, select N independent projected rows from H.
Their selected original generators are distinct occurrences in the
family; repeated or zero projected rows cannot form an independent
selection. The resulting N-square matrix has nonzero determinant.
The Leibniz formula therefore has a nonzero permutation term, also in
characteristic two: if every term were zero then their sum would be
zero. Such a term uses every parameter column and every selected row
once. Applying (2) to its chosen entry in each row charges N different
generators, never adding several column bounds on one generator.
Unselected generators have nonnegative weight. Summing by the number
of set bits proves (1), and S<=36*2^k proves (4). Redundant generators
cannot defeat either step. At k=0, N=1, P_N=[1] and the projection
minor is [1]; empty sums, the bound 2 and S=36 all remain valid.
The all-k ratio diverges because (1+sqrt(2))/2>1, independently of
any finite threshold-rank calculation.

**Complete finite replay, including optimality.** Both producing scripts
were read in full, as were the imported act, insert, rank and endpoint
helpers in `check_weight_filtration.py`. The constructor uses highest
pivots; the receiver uses lowest pivots and set symmetric differences.
The receiver checks every occurrence, the topological order, finite
constant powers, every right-closed row and boundary, every residual,
and the entire paired Krylov sequence against the literal formulas.
It reconstructs all 512/512 codewords, so filtering by weight receives
all low-weight vectors rather than just a supplied witness list.
All 12,951/12,951 coordinate subsets through weight four are checked
by the constructor. The dimension and reversed projection rank are
9/9 and 4/4; counts and every threshold rank agree with §5.

For completeness, if a basis has weights d_1,...,d_9, then
`sum_i d_i=sum_(w=0)^23 #{i:d_i>w}` because each row has at most 24
coordinates. At most r_w independent basis rows can lie in the span
of all weight-at-most-w vectors. Thus each summand is at least 9-r_w.
The receiver checks every r_w and a nine-row independent witness of
total weight 38, exactly equal to this lower bound. Any generating
family contains a basis subset, so its total weight is at least 38.
This proves the finite optimum without an unsupported greedy-optimality
assumption and without extrapolating rank 7<9 to large N.

Both scripts were rerun into `scripts/batched-incidence/output-551/`.
`compare_paired_replay.py` compared the entire decoded constructor
certificate with step 549 and the entire audit certificate except its
input-path field. Both old and new input-path bindings were checked
explicitly; no mathematical field was excluded. All 10/10 comparison
and count checks pass, and all four failure lists are empty. The full
regenerated certificates and `replay-comparison.json` are retained in
that directory. This receives complete evidence rather than relying
on previewed fields, successful status flags or hashes.

Reproduce the first two commands in §5 with the output directory
`scripts/batched-incidence/output-551/`, then run separately:

```bash
python3 scripts/batched-incidence/compare_paired_replay.py \
  --old scripts/batched-incidence/output-549 \
  --new scripts/batched-incidence/output-551 \
  --output scripts/batched-incidence/output-551/replay-comparison.json
```

The audit validates Attempt 060's provisional stop, with exactly its
K_N/original-coordinate/expanded-support hypotheses. It does not prove
that another invariant space or an arbitrary zigzag has the same
projection obstruction. No fitting graph/work/live/wire bound, fourth
comparison receipt, mixed-letter extension, general certificate existence
or unrestricted complexity conclusion is added. No new mathematical
input or lemma is introduced.

## Mathlib

Full matching coverage has not been checked. Binomial sum identities,
triangular-matrix invertibility, finite-dimensional projection rank and
the Leibniz determinant formula are supporting ingredients, not a
received Mathlib theorem for (1). No Mathlib theorem certifies the finite
artifacts. Unknown availability is not evidence of absence.
