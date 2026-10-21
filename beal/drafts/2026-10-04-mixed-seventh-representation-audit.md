# Weight-two representation applicability audit — 2026-10-04

The saved SPECIALIZE assessment is reused unchanged. This is a mathematical applicability audit, not new literature discovery. Only the previously screened versioned PVT, Golfieri–Pacetti and BCDF statements/proofs were reopened to check their exact formulas.

The gap is the original-solution interface to L017. The proposed intermediate target is simultaneous determinant, finite-flatness, ramification and conductor control for one weight-two plus representation. Continue if the geometric lattice and all coordinate-valuation cases match; stop the implication if an unsupported Tate twist or irreducibility assumption is necessary. Success still gives no irreducible-packet exhaustion or original exceptional-algebra/global descent.

Working calculation: put (a,b,c)=(X,-Z,Y), t=-X^5/Y^3. Then t-1=-Z^7/Y^3. At 7 the four exhaustive valuation patterns for (t,t-1) are (0,0), (5v_7(X),0), (-3v_7(Y),-3v_7(Y)), and (0,7v_7(Z)). The plus Euler curve has exponents (2,-8,8,-3) with covering degree 15, exactly the q=5,r=3,s=1 case in GP's finite-flat proof. PVT's quotient by the two involutions has degree four, so its Jacobian component can be extracted at 7 by pullback/norm and averaging; neither 4 nor 15 is divisible by 7. Use the geometric Tate module from the outset, not an arbitrary twist of a finite-flat residual module.

Conductor passage: the inertia-fixed sublattice is saturated, so its reduction injects into residual inertia invariants. Wild inertia at 3 or 5 has finite image of order prime to 7, and averaging preserves invariant dimensions after reduction on every ramification subgroup. Thus tame conductor cannot increase and Swan conductor is unchanged. Global semisimplification cannot increase conductor either. This requires no residual irreducibility.

Result and precise citations are recorded in L019. No original-source theorem, MAGMA quotient construction, general finite-flat theorem or modularity proof is independently reproved. The specialization is REPRODUCTION of the inspected interface claim.

Validation note: SymPy was unavailable. A standard-library exact polynomial-coefficient calculation verified the derivative/common-root identities and inertness at 7. The proof itself contains the complete identities; no finite search is used for the universal valuation cases.
