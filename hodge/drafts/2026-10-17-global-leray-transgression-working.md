# Global Leray test — unfinished checkpoint

2026-10-17. Approved target: determine the actual Leray transgression
H^0(B,W)->H^2(B,M) and test whether it strengthens |Z|<=800.
Use the prior SPECIALIZE assessment
`drafts/literature/2026-10-17-equality-global-leray-transgression.md`.
Main universal gap remains primitive rational Hodge realization; this
conditional kernel test supplies no cycle or transport.

Inputs read: L108 actual truncation/trace and splitting; L109 actual
normalized alpha and b; L111 M=E and W length one at every split point;
L115 actual normal polystability and 0<=s<=800. ATTEMPTS/047/067
warn against assigning section multiplicities or confusing local gamma
with the global Leray differential.

Candidate calculation (not yet finalized): alpha:C[2]->D C and
j:M[-1]->C give rho=(b^{-1}[-1]) (D j[-2]) alpha[-2]:C->M[-1].
Here b:M->M* is the global extended Serre-form adjoint, hence invertible
by L111/L108, and rho j=id. This should force the actual truncation
class W[-2]->M and global d_2 to vanish. Must check all global maps,
shift signs and Serre adjoint, rather than substitute a split model.

If valid, h^1(X,V)=t, h^3(X,V)=t and
h^2(X,V)=h^1(B,M)+s=724+2t. With M=T_B plus N,
h^1(N)=704-s+2t and t=h^0(N) is still unknown. L115 polystability
at degree zero makes all global sections trivial parallel summands,
so 0<=t<=48; t=47 is impossible since the remaining rank-one summand
has determinant O, while t=48 forces N=O^48 and s=800. Tentative
extra exclusion: s=797,798,799 require t>=47 and hence are impossible.
This is a constraint on the same approved cohomology test; no actual
N or F existence follows for the remaining values. Check source scope
and derive only this bounded consequence. No prescribed acyclicity,
strict normal stability, section count or nonempty Z is assumed.

Continuation/abandonment test: establish the actual maps and their
constraints; park this mechanism once the remaining possibilities need
an independently determined section count or a new geometric input.

Completed: the full proof and qualifications are canonical in L116;
ATTEMPTS/068 records the remaining compatibility and stop decision.
The canonical conclusions supersede the tentative calculations above.
