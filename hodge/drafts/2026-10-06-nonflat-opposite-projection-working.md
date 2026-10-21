# Nonflat opposite-projection working checkpoint

Approved target: Test the opposite-projection character and polystable
cohomology constraints for the nonflat correction pair (-10,-11).
Prior SPECIALIZE coverage is the supplied nonflat-opposite assessment.
Preserve all prior changes and ATTEMPTS/041--043.

Inputs read: L044's exact chamber and invariant tensor, L048's full
forced character, L052's coefficient-independent connection/restriction
argument and exact line lattice, L056's preservation/base-change proof,
L057's first-projection filter, and L058 as a methodological contrast.

For the hypothetical F, p=-6,t=-7, so L048 gives
ch(F)=2-6e_1-7e_2+tau_D+20P, with ch_1=ch_3=0.
L056--L057 give G=R^1p_2*F, rank two, c_1=0,c_2=6.
G cannot split, since 6 is not 14r^2; it is stable with cohomology
(0,2,0). L052 gives stable charge-seven fibres for p_1 at every
point, since 7 is not 14r^2, and their cohomology is (0,3,0).
The approved base-change and preservation theorems then give actual
H=R^1p_1*F, rank three, polystable at h. Signed relative GRR yields
ch(p_1!F)=-3+8eta, hence ch(H)=3-8eta. Single-row Leray yields
cohomology (0,2,0) for H, consistent with chi(F)=2=-chi(H).

Remaining bounded obligation: check every polystable summand, allowing
its own first Chern class. A trivial line would violate h^0(H)=0;
a nontrivial zero-slope line of class rk has h^1=7r^2-2>=5,
exceeding h^1(H)=2. This should force the stable rank-three branch.
Verify in the canonical write-up, then stop this mechanism if the
stable branch has no negative required cohomology dimension. No
existence, symmetric pairing, spin lift, inverse or transport is assumed.
