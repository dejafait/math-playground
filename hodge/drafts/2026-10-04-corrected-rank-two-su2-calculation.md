# Corrected rank-two SU(2) specialization — working calculation

Reuse the ready SPECIALIZE assessment
[saved finite-rank review](literature/2026-10-04-corrected-rank-two-topological-realization.md).
The bounded target is its unchanged topological realization test.
The local gap is an actual compatible representative that could reach
the fourth RM direction. A finite-rank obstruction can reject character
data before holomorphic construction; passing will leave local freeness
in the holomorphic category, stability and transverse transport open.

Retain the full integral class beta=p e_1+t e_2+tau_D from L048,
p=4+a, t=4+b, and u=-beta. The source theorem uses p_1(TX),
not p_1 of the proposed bundle. Since c_1(TS)=0 and c_2(TS)=24eta,
p_1(TX)=-48(e_1+e_2). L048 gives beta^2=(2pt+156)P.
Thus the characteristic number is

    J = <p_1(TX)u+2u^2,[X]>/4 = 12(p+t)+pt+78.

For (-10,-10), p=t=-6 and J=-30, whose residue modulo 12 is 6,
against zero required. This excludes the saved symmetric input.

Sq^2 vanishes on all of H^4(X,F_2): use the full integral Kunneth
lattice, not its rational NS/T decomposition. The pure point classes
have zero Sq^2 by dimension. For integral degree-two classes on either
K3, Sq^1 vanishes and Sq^2 is the mod-two square, which vanishes
because the K3 lattice is even. Cartan handles every mixed term.
These classes generate H^4(X,F_2), by torsion-freeness and vanishing
odd cohomology. Hence the source criterion is equivalent to
pt=6 modulo 12. No square has that residue, so every symmetric pair
fails, even arbitrarily far inside the numerical Bogomolov region.

The nonsymmetric boundary pair (-7,-6) has p=-3,t=-2, J=24,
forced ch_4=14P and index 12. The criterion therefore supplies a
topological quaternionic line, hence a complex rank-two SU(2) bundle,
for this pair. It does not supply a holomorphic or stable bundle.
The exact region is a+b<=-13 and (a+4)(b+4)=6 modulo 12.

Canonical proof and qualification will be stored in L050. Verify
the arithmetic across all residue pairs modulo 12; the Steenrod
and sufficiency arguments are mathematical, not computational.
