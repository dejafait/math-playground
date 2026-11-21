# Small-angle cubic — saved calculation

Approved target and coverage: the exact TARGET in
`literature/2026-11-06-small-angle-cubic-all-rays-finite-pf.md` (SPECIALIZE).
No changed hypotheses or new source input is used.

Put N=m+2, theta=pi/N, q=exp(i theta), s=sin(theta/2)>0.
The variables (1,q,q^(-1)) are distinct. Alexandersson Theorem 6
gives the shift-one terms with coefficients
1/(4s^2), -exp(3i theta/2)/(4s sin(theta)), and its conjugate.
Thus D_(r,1)=[cos(theta/2)-cos((r+3/2)theta)]/[2s sin(theta)]
=sin((r+1)theta/2)sin((r+2)theta/2)/[s sin(theta)].
Palindromicity gives the shift-two matrix as the transpose of
shift one. The product has period 2N in r, is positive on residues
0,...,2N-3, and zero on residues 2N-2,2N-1. Shifts 3 and >3
are respectively lower triangular with diagonal 1 and zero-first-row.

The known Schoenberg family as recorded in Adm–Garloff–Tyaglov
(5.9) has d=3, source order k=2m+2, phi=theta/2; its monic
polynomial has the same three factors, hence supplies PF_(2m+2),
and therefore PF_m. Roots -1,-q,-q^(-1) include a nonreal pair.
All ordinary coefficients are (1,1+2cos(theta),1+2cos(theta),1).

The complete specialization is now canonical in L840. This saved
scratch reasoning is retained as an intermediate artifact, not a
second proof or current continuation record. The work reproduces
known finite methods, with no actual-Xi or infinite-degree transfer.
