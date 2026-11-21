# Approved degree-five attempt — partial reasoning

The invocation-start SPECIALIZE assessment is
`literature/2026-11-06-adjacent-shift-degree-five-test.md`.
One ansatz only:
P(z)=(1+4z)(1+3z)(1+2z)(1+z+z^2), with Widom variables
4,3,2,omega,conj(omega), omega=(1+i sqrt(3))/2.
The polynomial roots are -1/4,-1/3,-1/2,exp(+-2pi i/3),
so Katkova Theorem B's open excluded sector for PF2 is respected.
For shift3 the unique largest product is 24; every other triple has
modulus at most12. For shift4 the largest products are 24 omega and
24 conj(omega); the other products have modulus at most12.

Still to check: every coefficient, all cross-difference denominators,
exact coefficients of all ten/five terms in Alexandersson Theorem6,
positive leading coefficient at shift3, a strict negative period-six
residue at shift4, and explicit onset bounds controlling all remainders.
No unbounded sign claim has yet been certified. This is a reproduction
of assessed methods, with no Xi realization or higher-PF implication.

Completion: the preceding text preserves the pre-calculation checkpoint.
All listed obligations were subsequently discharged in
[L837](../lemmas/L837-degree-five-pf2-adjacent-shift-countermodel.md),
with the complete exact certificate in
`scripts/fixed-shift-overlap/adjacent-degree-five-exact.json`.
Both rays hold with onset16; the negative residue is5 modulo6.
This completed specialization has not yet received its separate audit.
