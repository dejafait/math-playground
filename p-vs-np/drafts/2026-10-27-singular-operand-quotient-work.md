# Step 534 — singular operand-coordinate common quotient

## Saved starting scope

One mathematical attempt under the unchanged, pre-invocation EXPLORE
assessment `literature/2026-10-26-unary-product-sparse-quotient.md`.
No source refresh or approval of new mathematics is part of this turn.
The main gap remains uniform worst-case P versus NP. The intermediate
target is the checkpoint's common scalar quotient for independently
wrapped unary products, first F_r G and G F_r. A linear certificate here
could supply that sector of the fourth comparison; general F, mixed
letters, actual reception, complete costs and availability remain open.

Use A->Q<-B with alpha_H X_H=alpha_Q, M_H X_H=X_H M_Q,
X_H beta_Q=beta_H, and L110's right closure. Q must be an explicit acyclic
singleton graph; full scalar maps and all repeated graph costs count.
Try operand-state coordinates plus one boundary-delay chain, without
enumerating cut pairs, degrees at every operand state or full paths.
Continue only on a complete equation check and explicit universal C in
support(X_A)+support(X_B)+2g(Q)<=C*(g(A)+g(B)), or a concrete refined test.
A complete failed equation or forced superlinear count stops only this
template. An unfinished map is not an impossibility result.

Read L110 §§4,21; L115 §§1–6; L117 in full; Attempts 049–051;
history 533; and foundations/01-model-and-target.md. The exact target was
already reconfirmed against Clay/Cook today. L115 imports scalar-simulation
soundness from Esik–Maletti, 2010 manuscript, Definition 3.1 and soundness,
p.2. Reuse it, rather than reproving qualitative equivalence. L114's
coefficient support, L116's all-state delay and L117's invisible channel
remain scope comparisons. The supplied assessment and PROOF/DAG were
read directly; no unchanged startup file was reread. Existing notebook
changes are preserved.

## Preserved calculation before canonical write-up

The proposed Q keeps G and one suffix F_r delay chain, deleting only its
last redundant nonfinal vertex. It has vertices s,G,d_0,...,d_(r-1),t;
constants s->p and q->d_0, all original G occurrences, and r parallel
1/x layers from d_0 through the delay vertices to t. Thus
g(Q)=n+5r+2c+2d+6, while each original endpoint has g(Q)+3.

Work first with a pure x path P_r and H=T(G), where T replaces each x
edge by parallel x and 1 edges. Set K=(I+C_H)^(-1), N=D_H K,
a=e_p K, b=e_q^T, gamma=ab. With H coordinates and d coordinates on Q,
the complete candidate map from Prod(P_r,H) is:

    s -> s; t -> t; f_r -> 0;
    f_i -> a N^i on H + sum_(j=0)^i a N^(i-j)b d_j  (i<r);
    H rows -> N^r on H + sum_(j=0)^(r-1) N^(r-j)b d_j.

The map from Prod(H,P_r) identifies s,H,t and f_i->d_i for i<r,
and sends f_r to zero. The row equations check separately for s,t,f_r,
the first r-1 delay rows, the last delay row, and all H rows. Both initial
and final equations check. Applying T to all three graphs preserves
these scalar maps by L115 §2; T(T(G)) has exactly G's parity adjacency,
so the original endpoints and the directly built Q can be used. These
are rectangular maps, with no surjectivity or idempotence assertion.

On L117's fixture, H has N=D, N^2=Nb=0, a=p+q+u+v. For r=1 the H
block is D; for r>=2 it is zero. The f_0 row is a+d_0; for r>=2 f_1
maps to u+v+d_1, and f_i maps to d_i for 2<=i<r. This removes the
invisible channel without assuming invertible similarity.

The support test is negative even if these candidate maps are replaced
by arbitrary valid maps to the same Q. Take r=N=2^k and G the N-edge
pure-x path h_0,...,h_N. In Q the nonzero right-closed residuals are
z^(N-i)(1+z)^N at h_i (i<N), z(1+z)^(N-j-1) at d_j (j<N), and 1
at t. They have distinct degrees 2N,...,N+1,N,...,1,0. The other two
residuals, at s and h_N, are zero. In A the h_i residual is z^(N-i).
Consequently its image in Q must use the unique expansion
z^l=sum_(j=0)^(l-1) binom(l-1,j) z(1+z)^j for l=N-i.
The binary-support identity already proved in L114 §4 makes the sum
of these forced entries 3^k. The original S=16*2^k+20 and 2g(Q)=S-6.
Thus graph size is linear but every first map has an unbounded
support/S ratio. Only this operand-preserving suffix quotient is stopped.

The calculation above is the saved pre-write-up reasoning. Its final
full proof, equations and resource qualifications are canonical in
[L118](../lemmas/L118-singular-suffix-quotient-support-obstruction.md).
No mathematical script, finite-job receiver or source refresh was used.
L114 §4 was read in full and its exact binary-support identity is reused,
not claimed as new.
