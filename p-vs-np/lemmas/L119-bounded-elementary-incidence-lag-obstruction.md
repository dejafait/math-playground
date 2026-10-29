# L119 — Bounded elementary incidence chains fail on a long cancelling branch

## Hypotheses

Work over F₂ with finite acyclic occurrence graphs, every edge occurrence
labelled 1 or x. Parallel occurrences are retained, including ones that
cancel in parity. Use L110 §4's right closure

    K_H=(I+C_H)^(-1), alpha_H=e_s K_H,
    M_H=D_H K_H, beta_H=e_t^T,                            (1)

where C_H,D_H are the parity constant and x adjacencies and inverses are
finite sums. The original wrapped product Prod(U,V) has disjoint whole
operand copies, fresh s,t, and three constant connectors:
s->entry(U), exit(U)->entry(V), exit(V)->t.

For r>=1, F_r has vertices f_0,...,f_r and parallel 1/x occurrences
f_i->f_(i+1). For m>=1, G_m has distinct vertices p,u_1,...,u_m,q,
roots p,q, and precisely these occurrences:

* the m x edges p->u_1->...->u_m;
* one constant edge p->q;
* two separate constant edges u_m->q.

Set A=Prod(F_r,G_m), B=Prod(G_m,F_r), without trimming, coalescing their
records, or padding the denominator. Let g(H)=|V(H)|+2|E(H)|, counting
each singleton label entry, and S=g(A)+g(B).

An ordinary scalar arrow X: U->V, with U rows and V columns, satisfies

    alpha_U X=alpha_V, M_U X=X M_V, X beta_V=beta_U.       (2)

The **tested elementary-incidence template** additionally requires a
scalar companion Y, with V rows and U columns, satisfying

    XY=M_U, YX=M_V.                                      (3)

Y need not preserve accepting boundaries or be sparse; it is not a second
accepting arrow. Intermediates may be any finite acyclic singleton graphs,
with arbitrary sizes, constants and cancellation. Every arrow can point
either way. A chain of length ell must satisfy (2) and (3) at every arrow.
This specifies the extra template restriction without assuming that its
intermediate graphs or maps exist. The five-arrow orientation tested is

    A -> H1 -> H2 <- H3 -> H4 -> B.                       (4)

A projection killing a long unobservable nilpotent component need not
admit (3). Such ordinary scalar projections, higher-lag companions and
arbitrary scalar zigzags are outside this restriction.

## Conclusion

Both original products accept (1+x)^r. Every operand vertex lies on a
structural accepting path, and

    |V(A)|=|V(B)|=r+m+5, |E(A)|=|E(B)|=2r+m+6,
    S=10r+6m+34.                                        (5)

Nevertheless their positive nilpotency indices are

    nu(M_A)=r+m+1, nu(M_B)=max(r,m)+1.                    (6)

Every chain in the specified template has ell>=min(r,m). No fixed arrow
count works for all r,m, even with unlimited graph size and support.
In particular r=m=6 rules out (4): S=130, M_A^12 has exactly the single
nonzero entry (f_0,u_6), whereas M_B^7=0. The indices differ by six.

L115's actual single-layer construction has this additional structure:
its four outer arrows have companions (3), and its central arrow is
invertible, also after affine substitution. Thus this stops batching
that elementary-factor mechanism into a fixed number of arrows, not
L115 or ordinary scalar chains without (3). L116's all-port contract,
L117's invertible stabilization and L118's fixed suffix basis are distinct
restrictions, not hidden premises here.

This is REPRODUCTION/specialization of elementary matrix-product algebra
to a new local test family, not a new general shift-equivalence theorem
or an originality claim beyond the sources checked. It supplies no
fourth-comparison receipt, general lower bound or resolution of P versus NP.

## Proof

### 1. Source scope and the needed specialization

Reuse the pre-invocation EXPLORE assessment
`drafts/literature/2026-10-27-batched-incidence-zigzag.md` and scalar
simulation convention/soundness from Ésik–Maletti, *Simulation vs.
Equivalence*, [2010 author manuscript, Definition 3.1 and soundness,
p.2](https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf).
F₂ and finite accepting boundary vectors fit that convention; it supplies
no linear-size existence assertion.

The assessed elementary splitting comparison is Béal–Berstel–Eilers–
Perrin, *Symbolic dynamics*, [arXiv:1006.1265v3, §§3.1–3.2,
Propositions 3.5–3.6, inspected within printed pp.12–18](https://arxiv.org/pdf/1006.1265v3).
The inspected version is the 45-page text retrieved 27-Oct-2026, with PDF
header 6-Feb-2011 and separate title page 26-Nov-2024. Its ND/DN factors
for labeled splits motivate the explicitly imposed scalar equations (3).
No bi-infinite-path theorem, division-matrix conclusion or conversion to
accepting F₂ boundaries is imported. Allowing arbitrary companions and
intermediate graphs relaxes an incidence implementation of this factor
pattern. It does not claim that every incidence simulation has this pattern.

The short finite-product calculation is given because its right-closed
endpoint application and preservation by L115's substitution are the
particular quantitative test. No qualitative simulation, conjugacy or
minimization theorem is reproved. The prior assessment's elementary
factorization scope covers this bounded test; no new source is assumed.

### 2. The complete equation obstruction for elementary factors

For a positive-dimensional nilpotent matrix M, nu(M) is the least positive
k with M^k=0. From M_U=XY and M_V=YX, associativity gives, for k>=1,

    M_U^(k+1)=X M_V^k Y,
    M_V^(k+1)=Y M_U^k X.                                (7)

Thus nu(M_U)<=nu(M_V)+1 and conversely. The absolute index difference
is at most one, without rank, sparsity, trimness or boundary assumptions.
All acyclic right-closed intermediate matrices are nilpotent, so along
ell arrows, regardless of orientation,

    |nu(M_A)-nu(M_B)|<=ell.                              (8)

An invertible intertwiner gives equal indices and contributes zero to
this bound. A violation of (8) means that the full system (2)–(3) has no
solution. It is not an inference that (2) alone fails or that a missing
proposed map constitutes an impossibility proof.

### 3. All four outer L115 arrows have elementary companions

Use L115 §§3–4's pure-letter notation for arbitrary H:
K=(I+C)^(-1), W=I+C, N=DK, a=e_p K, b=e_q^T, gamma=ab.
Its graphs/maps are A_x->A0->Q<-R->B0->B_x, with arrows X1,...,X5.
The following are complete row descriptions of companions; unlisted
rows are zero, and block rows use the indicated matrices:

    Y1: A0 -> A_x (as a matrix, not an accepting arrow)
        a0 -> f1 + a on H + gamma t;
        H rows -> N on H + Nb on t.
    Y2: Q -> A0
        V rows -> K on H + Kb on t.
    Y4: B0 -> R
        H rows -> K on U + N on V + b on t.
    Y5: B_x -> B0
        H rows -> N on H;
        f0 -> t.                                        (9)

Every nonzero row in the products is checked as follows. All other rows
are zero on both sides, by these formulas and L115's complete maps.

* X1Y1 has f0 row f1+a+gamma*t and H rows N+Nb*t: M_Ax.
  Y1X1 deletes f1, leaving a0 row a+gamma*t and H rows N+Nb*t: M_A0.
* X2Y2 has a0 row a+gamma*t and H rows D(K on H+Kb*t)
  =N on H+Nb*t: M_A0. Y2X2 has V rows K on U+KD on V+Kb on t:
  M_Q.
* X4Y4 has V rows K on U+N on V+b on t: M_R. Y4X4 deletes U
  and has H rows N on H+b on t: M_B0.
* X5Y5 has H rows N on H+b on t, and its t row is zero because
  both f1,t have zero Y5 rows: M_B0. Y5X5 has H rows N on H+Nb on
  f0 and f0 row f1+t: M_Bx.

X3 is block diagonal with W on both operand blocks and identity on s,t,
hence invertible. Its transition equation gives the optional elementary
companion Y3=X3^(-1) M_R, with X3Y3=M_R and Y3X3=M_Q. L115 already
proves both accepting boundary equations for every X_i. No boundary
claim is made for the Y_i, nor is K or N assumed sparse.

L115 §2's affine substitution sends M_U to M_U J_U, J_U=(I+M_U)^(-1),
and retains the same X. Intertwining gives J_U X=X J_V. If Y satisfies
(3), set Y'=Y J_U. Then

    XY'=M_U J_U, Y'X=Y X J_V=M_V J_V.                   (10)

So the companions persist, and X3 remains invertible. L115 §5 identifies
the transformed and original 1+x endpoints by exact vertex-indexed
adjacency equality, preserving these claims. The companions are only
algebraic witnesses, not additional stored accepting maps. This verifies
the link to L115 and identifies an extra restriction a different batching
mechanism may abandon.

### 4. The cancelling operand and complete original endpoints

Let D be the shift along p,u_1,...,u_m, zero on q. The two constant
u_m->q occurrences cancel in parity, giving

    C=e_p^T e_q, C^2=0, CD=DC=0,
    K_G=I+C, N_G=D, a=e_p+e_q, b=e_q^T,
    ab=1, Db=0, D^(m+1)=0, D^m=e_p^T e_(u_m),
    aD^m=e_(u_m).                                     (11)

Every state still lies on a structural accepting path in the ORIGINAL
graph. Its three accepting paths have weights 1,x^m,x^m, hence polynomial
1. All occurrences, including both cancelling edges, remain charged.

On F_r set J_(i,i+1)=1 and all other entries zero, T=J(I+J)^(-1),
and h=T e_(f_r)^T. Then

    T^r=J^r, T^(r+1)=0, T^r h=0,
    T^(r-1)h=e_(f_0)^T.                               (12)

Indeed the constant term of (I+J)^(-r) is I and J^r kills every positive
power, proving the first identity; the rest follow directly. These hold
also for r=1.

Relabel independent copies for display only into the common order
s,F_r,G_m,t. The s row and column are zero. On the remaining blocks the
ENTIRE right-closed transitions are

    M_A = [ T   h a   h ]       M_B = [ T   0   h ]
          [ 0    D    0 ]             [ 0   D   0 ]
          [ 0    0    0 ],            [ 0   0   0 ].    (13)

For A, an F letter has constant tails through later F states, the
connector to p, and p->q->t, giving its F blocks. A G letter's tails
to q,t occur in equal pairs and cancel, leaving D by (11). For B, a G
letter similarly has zero constant tail through q into F,t, by Db=0;
F letter rows have only later F states and t. This checks all connectors
and every block without deleting original occurrences.

The complete initial and final vectors are

    alpha_A=alpha_B=e_s+sum_(i=0)^r e_(f_i)+e_p+e_q+e_t,
    beta_A=beta_B=e_t^T.                               (14)

No u_i is reached from s by constants alone. Constants run through F
and p,q in opposite orders, giving exactly the displayed coordinates.
Thus (13)–(14), not just the accepted polynomial, describe both endpoints.

### 5. Exact powers, the mandatory tests and the failed threshold

For ell>=1 the F-to-G block of M_A^ell is

    sum_(j=0)^(ell-1) T^(ell-1-j) h a D^j.              (15)

A contributing product enters G once, after ell-1-j F steps, and then
takes j G steps. The other blocks are T^ell on F, D^ell on G, and
T^(ell-1)h from F to t; all remaining blocks vanish. This also proves
the formula by induction from (13).

At ell=r+m, only the j=m summand of (15) survives: larger j vanish by
D^(m+1)=0, and smaller j have at least r powers of T multiplying h.
Its value is

    T^(r-1)h aD^m=e_(f_0)^T e_(u_m).                   (16)

All other blocks vanish at that exponent. At ell=r+m+1 every block
vanishes, proving nu(M_A)=r+m+1. For M_B the F-to-G block is always
zero and the other block formulas are unchanged. Its index is
max(r,m)+1: the next power is zero, while T^r and D^m are nonzero.
This proves (6), with gap min(r,m).

Both mandatory earlier fixtures were tested against this necessary
condition; neither alone rejects the template:

* L117's four-state cancelling fixture has indices r+2 and r+1,
  a gap of one (L117 §§3–4). This is compatible with (8), not a
  construction of a batched chain for that fixture.
* With r=N=2^k and G the N-edge pure-x path, both indices are
  r+N+1. No path consumes more than r+N letters, while the accepted
  polynomial has coefficient 1 in degree r+N, so each M^(r+N) is
  nonzero. The gap is zero. This does not repair L118's suffix-map
  support or establish new maps.

The long cancelling family (11) is the refined test, within the approved
arbitrary-cancellation scope. For r=m=6 each endpoint has 17 vertices
and 24 edges, g=65 and S=130. Five elementary arrows would force
nu(M_A)<=nu(M_B)+5=12, hence M_A^12=0, contradicting the single entry
(16). This is a complete inconsistency of the template equations, not
an unsuccessful attempt to find matrices.

For any fixed arrow limit ell_0, choose r=m=ell_0+1. The gap exceeds
ell_0 and S=16(ell_0+1)+34. The template fails before any inequality
support+twice-counted intermediate size<=C*S can be attained. No actual
intermediate ledger, boundary/index encoding or checking-work bound is
claimed: even unrestricted costs cannot repair the equations. Original
boundaries and every original occurrence are accounted for above.

Crucially, (3) is NOT implied by (2). Unbounded-lag companions, arbitrary
singular simulations or removal of long unobservable kernels might evade
the obstruction; none is constructed here. General F, mixed letters,
actual job binding, Boolean/K/H/nonzero-fJ reception, full wire/work/live
costs, availability, L087 W₂ and unrestricted ER/Frege/SAT remain open.

### 6. Exact finite replay and its limits

The script `scripts/batched-incidence/check_elementary_gap.py` builds
the complete occurrence lists independently of (13), forms parity
adjacencies, computes finite constant closure by matrix powers and checks
all transition/boundary coordinates against (13)–(14) on the cancelling
fixtures. It retains every transition power through the first zero matrix
and every accepting coefficient through the dimension. The full graphs,
matrices, powers, checks and failure list are in
`scripts/batched-incidence/output-536/elementary-gap.json`.

The three completed cases are the original L117 fixture at r=6
(indices 8,7; S=106), the required x-path with r=N=8 (indices 17,17;
S=148), and the new family at r=m=6 (indices 13,7; S=130). Every
finite check passed; the last case FAILS the proposed arrow bound 5,
with required minimum 6. A necessary-bound pass on the first two cases
is expressly not a construction or a verification of their chains.
The complete selected witness matrices, their vertex order, A's next
zero power, B's preceding nonzero power and the original occurrences
were inspected using the shared JSON inspector with `--full` on those
values. This is finite corroboration of the symbolic proof, not its
substitute or a claimed receipt for an actual production input.

Reproduce into a fresh directory, preserving existing evidence:

```bash
python3 scripts/batched-incidence/check_elementary_gap.py \
  --output scripts/batched-incidence/output-536-replay
```

## Mathlib

Full matching coverage for this endpoint family and elementary-chain
obstruction is **not checked**; no absence claim is made. The source
conventions and matrix-factor comparison are cited in §1. Associativity
of rectangular matrix products, finite nilpotence and geometric sums
are supporting ingredients, not a matching theorem giving the endpoint
specialization and its restricted scope.
