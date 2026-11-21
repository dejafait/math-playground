# Count-only overlap test — step104 working record

Invocation-start gate: SPECIALIZE assessment
`drafts/literature/2026-11-07-count-only-overlap-obstruction-scope.md`.
Target is exactly its count/product class and unrounded H_m; no actual-Xi
replacement theorem is assumed. Main gap remains L030–L032/C032a.

Candidate: k=6002, J=6003, K=12363153437138,
H=3000175332800, delta=10^(-12).
For 1<=j<=k set gamma_j=10000-(k-j)/k;
gamma_J=10000+delta; for 1<=l<=K-J set
 gamma_(J+l)=H-1+l/(K-J); for n>=1 set gamma_(K+n)=H+n.
All regimes need certification; no success is asserted yet.

Preliminary decimal diagnostic: U(9999)>10152 and
U(H-1)-K is about11.95. These are previews, not certificates.
Proposed rigorous checks: rational logarithm enclosures and Machin-series
pi enclosure prove the endpoint margins and U'(9999)>1. Then U'>1
above9999, U>=d-1>0 below first zero, and each packet/tail jump is paid.
Finite packet plus linear tail gives reciprocal-square summability;
apply the already assessed DLMF product M-test, then check simple zeros.

Exact epsilon=1-q=(T^2-10000^2)/(T^2+10000^2)<10^(-15).
If V(T)>0 is checked, every H_m term except its final logarithm is
positive; log s>-epsilon, m+k+2<10^13, log2>1/2 would give
H_m>k/2-1/100>3000. Need verify all domains and preserve every term.
No further mechanism or parameter sweep is authorized in this attempt.

Completed: see canonical L897 and scripts/count-only-overlap/countermodel-104.json.
The14 exact-rational checks pass, including U(H-1)-K>11 and the
uniform derivative bound obtained by dropping b/t. The complete model
has exact H_m>300099/100>3000. Separate critical audit remains pending.
