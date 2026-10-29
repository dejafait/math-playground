# L126 — Variable normalized norm fails an unramified cubic unit image

## Hypotheses

Let Omega be an algebraic closure of Q_3, with |3|=1/3, and let E/Q_3 be an embedded unramified extension of degree three. Write O_E for its valuation ring, and normalize v_E(3)=1. Thus the maximal ideal is 3O_E and its residue field has 27 elements. Put

\[
U_\Omega=\{x\in\Omega^\times:|x|=1\},\qquad
M=U_\Omega/\mu(\Omega),\qquad
M_E=\operatorname{Im}(O_E^\times\longrightarrow M),
\]

where mu(Omega) contains all roots of unity. Use L125's F_{Q_3}, with the same natural action of G=Gal(Omega/Q_3) on both copies of M. The index H_E=Gal(Omega/E) is retained, without taking a divisible hull of M_E.

## Conclusion

There exists u in O_E^times with N_{E/Q_3}(u)=4. Every such u satisfies

\[
F_{\mathbf Q_3}([u])=[4]^{1/3}\notin M_E.
\]

In particular, F_{Q_3}(M_E) is not contained in M_E. This excludes F_{Q_3} from Ism(G) in the ordinary realization and with the identity subgroup indexing in IUT II Example 1.8(iv) and Definition 4.9(i). It does not assert that the native IUT comparison is F_{Q_3}, that every norm operation must have this interpretation, or that E occurs in complete native initial data. No essential IUT flaw, native-pilot failure or failure of finite B>=A follows.

## Proof

### Imported local-field inputs

Import Kedlaya, [*Notes on class field theory*, section 4.2, Proposition 4.2.5](https://kskedlaya.org/cft/sec_localcomp.html): for a finite unramified extension of local fields, the norm on full unit groups is surjective. It includes extensions whose degree equals the residue characteristic. Here E/Q_3 is finite and unramified, and 4 is a Q_3-unit. Therefore choose u in O_E^times with N_{E/Q_3}(u)=4. This existential specification of u is sufficient: the proof below applies to every unit in that nonempty norm fiber. We do not reprove norm surjectivity or assume surjectivity of a rational power on E-units.

Import Zhou, *Local Fields*, Michaelmas 2022, notes by Tomczak, [Proposition 6.14, printed p.28](https://math.berkeley.edu/~ltomczak/notes/Mich2022/LF_Notes.pdf#page=28): for a finite extension of Q_p with absolute ramification index e, and integral r>e/(p-1), exponential is a group isomorphism from pi^r O to 1+pi^r O; its proof supplies logarithm as inverse. In E we have p=3, e=1, and pi=3; r=1 satisfies 1>1/2. Consequently 1+3O_E is torsion-free, since its logarithm is isomorphic to an additive subgroup of the characteristic-zero field E. This imports the logarithm theorem, without any logarithm calculation or extension to Omega. The same source's Proposition 6.15, pp.28–29, identifies O_E^times/(1+3O_E) with the multiplicative residue group. These are exactly the inputs covered by the invocation-start assessment; the specialization below is ordinary local unit theory, with no originality claim.

### Torsion in E and the representative obstruction

Every root of unity t in E is a unit. Its residue has order dividing 26, so t^26 lies in 1+3O_E. It is still torsion, hence the preceding torsion-freeness gives

\[
t^{26}=1\qquad(t\in\mu(E)). \tag{1}
\]

For the unit u just chosen, evaluate L125 with k=Q_3 and L=E. Its exponent is [Q_3:Q_3]/[E:Q_3]=1/3. Hence

\[
F_{\mathbf Q_3}([u])=[N_{E/\mathbf Q_3}(u)]^{1/3}=[4]^{1/3}. \tag{2}
\]

Suppose this class belongs to M_E. Then some w in O_E^times satisfies [w]=[4]^{1/3}. Cubing in M gives [w^3]=[4], so

\[
t=w^3/4\in\mu(\Omega)\cap E=\mu(E).
\]

Equation (1) now gives the exact equality

\[
w^{78}=4^{26}. \tag{3}
\]

Reduction of w in the multiplicative group of the 27-element residue field gives w^26=1+3a for some a in O_E. Therefore

\[
w^{78}=(1+3a)^3=1+9a+27a^2+27a^3
\equiv1\pmod{9O_E}. \tag{4}
\]

But 4^3 is 1 modulo 9 and 26 is 2 modulo 3, so

\[
4^{26}\equiv4^2\equiv7\pmod{9O_E}. \tag{5}
\]

These residues are different: v_E(7-1)=v_E(6)=1, whereas membership in 9O_E requires valuation at least 2. Equations (3)–(5) contradict each other. Thus there is no E-unit representative of the output class. This also excludes representatives obtained by multiplying a chosen cube root of 4 by any root of unity outside E: if the resulting w belonged to E, its cube would still produce exactly the torsion element w^3/4 in E used above. Merely exhibiting a chosen cube root outside E would not have sufficed.

### Precise source relevance and limitations

In the ordinary realization of the reconstructed unit module in Mochizuki, [*IUT II*, December 2020, Example 1.8(ii)–(iv), printed pp.36–39](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20II.pdf#page=36), the full units are U_Omega and their full torsion quotient is M. By the fundamental theorem of infinite Galois theory, the fixed field of H_E is E, so the H_E-invariants of the full units are O_E^times. Their image in M is exactly M_E, rather than all of M^{H_E}. Example 1.8(iv), p.39, defines Ism(G) to preserve this image for every open subgroup. [Definition 4.9(i), printed pp.153–154](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20II.pdf#page=153), uses these indexed images in a chosen Kummer structure. With the ordinary marking and identity indexing fixed, (2)–(5) violate even containment at H_E, so F_{Q_3} cannot be an element of Ism(G). In particular, its G-fixed output classes from L125 must not be confused with images of actual E-units.

This is a necessary-condition test for one proposed structured use, not an objection to the source definition. We neither identify arbitrary reconstructed Kummer markings with this one nor require every possible norm to be a same-index endomorphism. IUT III Remark 3.9.5(x) supplies no such universal requirement, as recorded in the assessed source dictionary. The result stops this proposed use of L125 only. Determinant comparison, native-pilot membership, complete initial data and essentiality remain unresolved.

### Critical audit, step522

The separate audit passes within the unchanged hypotheses and ordinary marking. No mathematical defect was found. The citation above now distinguishes the exponential statement from its inverse in the proof; no mathematical hypothesis or conclusion changed. This validates a local known-method specialization, not progress beyond the sources checked or an essential IUT flaw.

- **Existence and the exponent.** E and Q_3 are complete local fields and E/Q_3 is finite unramified. Kedlaya Proposition 4.2.5 therefore applies to the full units, including degree three at residue characteristic three. Since 4 is a Q_3-unit, the norm-4 fiber is nonempty. In L125, k=Q_3 has degree one and L=E has degree three, so the exponent is exactly 1/3. Every member of this fiber has the same output (2); no explicitly selected algebraic root or surjectivity of division on E-units is used.
- **Strict depth and all torsion.** The normalized uniformizer is 3, the absolute ramification index is one, and the positive integer r=1 strictly exceeds 1/(3-1). Thus Proposition 6.14 applies inside the finite complete field E. Its additive target has no nonzero finite-order element. For every t in mu(E), reduction in F_27^times puts t^26 in this torsion-free principal-unit group, proving (1). This includes any potential 3-power torsion; no assertion about a logarithm on Omega is needed.
- **All representatives.** Membership in M_E means an actual w in O_E^times exists. Equality of its quotient class with the unique cube root of [4] implies w^3/4 is in the *full* torsion subgroup. Because w and 4 lie in E, this torsion element lies in E regardless of any root of unity used to construct w in Omega. Raising it to 26 gives (3). The proof excludes every such w, not merely one chosen cube root.
- **Exact contradiction and threshold.** Reduction gives w^26=1+3a with a integral. Its cube is 1+9a+27a^2+27a^3, so its difference from 1 has valuation at least two. On the other side, 4^3=64=1+63 is 1 modulo 9 and 26=3*8+2, so 4^26 is 7 modulo 9. More precisely, 4^26-1 is 6 modulo 9O_E and has valuation exactly one: 6=3*2 and adding an element of valuation at least two cannot change it. This is the required contradiction in O_E, not just an integer residue heuristic.
- **Source interpretation.** Example 1.8(ii)–(iv) permits the ordinary unit realization with its natural G-action and the quotient by all torsion. H_E is open of index three and its fixed field is E; hence U_Omega^{H_E}=O_E^times. Example 1.8(iv), p.39, requires preservation of its image in M^{H_E}, while Definition 4.9(i), pp.153–154, transports that image under a specified Kummer marking. At the retained ordinary marking this is precisely M_E. Failure of containment at this single index suffices to exclude membership in Ism(G), with no need to settle invertibility or topology. L125's G-fixed output classes are not thereby E-unit representatives. Other markings or index transports, or a native operation distinct from F_{Q_3}, are not excluded.

Only L125 is a direct local mathematical input; the norm, unit-structure and ordinary fixed-field inputs are standard cited results. No new local dependency or numerical experiment is used.

## Mathlib

Full matching Mathlib coverage of this finite-level nonpreservation statement has not been checked. The finite-norm supporting declarations recorded in L125 do not establish this representative obstruction or the source dictionary. No absence claim or formal verification is made.
