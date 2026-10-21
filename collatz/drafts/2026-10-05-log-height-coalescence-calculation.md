# Log-height coalescence calculation — working record

The approved target is exactly the TARGET in
`drafts/literature/2026-10-05-residue47-log-height-coalescence.md`.
The main gap remains universal eventual descent. The intermediate test
is a height-controlled selection of L026 roots, useful for excluding
small logarithmic companion clocks while leaving larger clocks,
other cylinders and termination open.

Essential input: audited L026, with all original-root, actual-path and
zero-clock guards unchanged. L025 enters only through L026. Named CRT
applies because 81 is invertible modulo the binary modulus and the
binary and ternary moduli are coprime. No convergence or least-root
assumption is available or needed.

Saved calculation before final documentation: for integer L>=6 put
H=12^L and M=2^(L+1)3^(L+4)=162*6^L. Choose the first member of the
CRT class strictly above H. Then H<n<=H+M, and
M/H=162/2^L<=81/32, so n<4H. Thus log(n)<L log(12)+log(4).
For fixed 0<C<1/log(12), B>=0, let delta=1-C log(12)>0 and take
L>=max(6,ceil((C log(4)+B)/delta)). This gives C log(n)+B<L.
All L026 guards therefore imply the desired exclusion on both clocks.

The continuation test succeeds if the representative construction and
these inequalities hold for every such integer L, including strict
size and integer horizons. An exponential selection cost larger than
12^L would have stopped this mechanism. Unboundedness at fixed L alone
would not have passed the test. The complete proof is now stored in
`lemmas/L027-subcritical-log-height-residue47-coalescence-obstruction.md`;
no numerical computation is required for these bounds. All guards pass
the analytical calculation; independent critical audit remains pending.
