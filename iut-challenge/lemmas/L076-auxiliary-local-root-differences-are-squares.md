# L076 — Two auxiliary root differences are squares in the fixed completion

## Hypotheses

Fix the same L073 auxiliary witness E_aux and L074's arbitrary labelling
of the distinct roots r_1,r_2,r_3 of its original monic integer cubic

    g_aux(X)=X^3+cX^2+dX+e.

Keep the actual embedding into Omega and the induced completion
F_aux,u=H=Q_3(zeta_60). Put a=r_2-r_1 and b=r_3-r_1, as in L074.
The precision and original-model congruences are those of L048 and
L073; no coordinate scaling, curve reselection or field extension is made.

## Conclusion

At least two of a,b,b-a are nonzero unit squares in H. More precisely,
exactly one labelled root has residue -1 and the other two have residue
0 in the residue field of H. The two differences involving the root
of residue -1 are squares in H, with the signs specified below.

Thus the approved existential local square-class test passes. This
does not determine the third difference's square class. L074's global
nonsquareness in F_aux remains valid: square roots in a completion
are not asserted to belong to that number field. No changed global
field, preservation of its 7-division completion, native model or IUT
numerical comparison is established. The separate step299 critical
audit below validates this local specialization.

## Proof

### Imported theorem and scope

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-18-auxiliary-local-legendre-square-class.md`.
Import J.S. Milne, *Algebraic Number Theory*, v3.08, 19 July 2020,
[section 7, complete-DVR convention p.119 and Proposition 7.31,
including its proof p.120](https://www.jmilne.org/math/CourseNotes/ANT.pdf):
for a polynomial over a complete discrete valuation ring, each simple
root of its residue polynomial lifts to a root in that ring with the
specified residue. No proof of Hensel's theorem is repeated here.
H is a finite extension of Q_3, so its valuation ring O_H is a complete
DVR with residue field k_H of characteristic 3. The specialization
must identify actual integral roots and unit differences before this
theorem can be applied. No Tate-coordinate theorem is needed.

### Actual roots and their complete residue multiplicities

L074 identifies every r_m with the x-coordinate of the nonzero
2-torsion point (r_m,0), so every r_m belongs to F_aux. L073's actual
embedded completion therefore places each r_m in H. L048's
family-wide congruences apply to this same original auxiliary cubic:

    c=1 mod 3, d=e=0 mod 3.

In particular its coefficients lie in O_H. To check root integrality
directly, suppose v_3(r_m)<0. The leading term r_m^3 has valuation
3v_3(r_m), strictly less than the valuations of each nonzero term
c r_m^2, d r_m, e, since their coefficients are integral. A sum with
one strictly least-valuation term cannot vanish. This contradicts
g_aux(r_m)=0. Thus every r_m lies in O_H.

The exact split factorization may now be reduced in k_H[X]:

    product_(m=1)^3 (X-bar(r_m)) = X^3+X^2 = X^2(X+1).

Here the original congruence modulo 3 implies the displayed residue
identity even though 3 need not be a uniformizer of H. Since 0 and
-1 are distinct in characteristic 3, uniqueness of polynomial
factorization over the field k_H gives precisely two residues 0 and
one residue -1, counted among the actual three labelled roots.
Distinct roots in H can share a residue; no simple-root lifting of
the double root 0 is being claimed.

### Both possible unit residues have simple square roots

Let i=zeta_60^15 in H. It has order four, hence i^2=-1 and
v_3(i)=0. Consequently bar(i) is nonzero and bar(i)^2=-1 in k_H.

For any D in O_H with residue 1, the polynomial P_D(T)=T^2-D
has residue root 1, with derivative 2 nonzero in k_H. Proposition
7.31 gives s in O_H with s^2=D and residue 1. For any D with
residue -1, its residue root bar(i) has derivative 2bar(i), again
nonzero in k_H. The same proposition gives s in O_H with s^2=D
and residue bar(i). In both cases D and s are units. These applications
use the actual full difference D, rather than a finite approximation
or an assertion that every unit of H is square.

### Arbitrary labels and the three prescribed signs

There are exactly three possibilities for the isolated residue -1:

| Root of residue -1 | Prescribed unit differences | Their residues |
| --- | --- | --- |
| r_1 | a=r_2-r_1, b=r_3-r_1 | 1, 1 |
| r_2 | a=r_2-r_1, b-a=r_3-r_2 | -1, 1 |
| r_3 | b=r_3-r_1, b-a=r_3-r_2 | -1, -1 |

The remaining root residues in each row are 0, so every entry follows
by subtraction in k_H. The preceding simple-root applications show
that both listed differences are squares in H. All differences are
nonzero because the original roots are distinct. This proves the
existential target, and in fact supplies two squares, for every initial
labelling. No conclusion is drawn for the difference between the two
roots reducing to 0.

### Relevance and limits

The local pass removes this particular square-class obstruction to
a separately assessed global modification retaining H. It constructs
no such modification and does not show that N would be preserved.
L074's fixing element is not assumed to belong to the chosen local
decomposition group; its global radical exclusion cannot obstruct
these local lifts. L075's fixed-global-field screen is a contrast,
not an input to Hensel lifting or a result reopened here.

Retained E_0,F,K_glob,Omega,embedding,u,w,H,N,q_0 remain unchanged.
No equality q_aux=3^30 or q_aux=q_0 is used. Native T/model, retained
scalar occurrence and memberships, exact generation, independent
initial data, marked all-image factorization, pilot transport,
essentiality and the original finite B>=A comparison remain open.
This is a reproduction/specialization of the assessed known methods,
not a claimed result beyond the literature checked or an IUT flaw.

### Separate critical audit — 2026-10-18, step 299

The unchanged invocation-start SPECIALIZE assessment covers this same
local target, including the complete-DVR theorem and its simple-root
proof. This audit imports Milne Proposition 7.31 as stated above; it
does not introduce a stronger lifting or descent theorem.

**Same model and embedding.** L073's hypotheses fix the original
integer cubic in precisely L048's coefficient neighborhood, and its
retention argument and separate audit give the embedded completion
F_aux,u=H for that same witness. L048's integral Tate coefficients
give c=1/4 modulo 3 and d=e=0 modulo 3; since 4=1 in the residue
field these are the congruences used here. No short-coordinate model
from the sieve is substituted. L074 identifies the actual roots with
the three nonzero two-torsion x-coordinates in F_aux. Thus all three
roots, not just a chosen simple root, are in the specified H.

**Integrality and multiplicities.** For a hypothetical root of
valuation t<0, the four term valuations are 3t, at least 2t, at
least t, and at least 0, with zero terms omitted. The first is
strictly least, contradicting the ultrametric inequality for a zero
sum. This establishes integrality without a Hensel hypothesis on
the cubic. Reducing its exact monic factorization therefore is
legitimate. The factors X and X+1 are distinct in k_H[X], so their
multiplicities 2 and 1 force exactly the residue distribution stated
above. Reducing a congruence modulo 3 further modulo the maximal
ideal is valid in this ramified completion; equality of those two
ideals is neither asserted nor needed.

**Signs and exact lifts.** The table exhausts the three possible
positions of the unique root of residue -1. Direct subtraction gives
(1,1), (-1,1), and (-1,-1) for the displayed differences respectively.
The element i has valuation zero since i^4=1, and its residue obeys
bar(i)^2=-1. Consequently the residue roots 1 and bar(i) are nonzero,
and 2 and 2bar(i) are units in characteristic 3. Applied to each
actual polynomial T^2-D over the complete DVR O_H, Milne's theorem
gives an exact root with nonzero residue. The two listed differences
are units; the unlisted difference has residue zero and receives no
square-class verdict. The argument never lifts the double root of
the reduced cubic, and needs no computation of the full residue field.

**Verdict and scope.** Both unit-square conclusions, and hence the
approved existential threshold, pass independently of the labels.
The direct mathematical inputs in the DAG remain L048, L073 and L074;
L075 and the recorded route failures are contrasts only. No repair
of the proof, extra hypothesis, mathematical script or new theorem
was required. This validates a known-method local specialization,
not progress beyond the sources checked. An element fixing F_aux
globally is not thereby in its selected decomposition group; nothing
here conflicts with L074's exclusion of global square roots. The
third class, any changed global field and its division completion,
native identification and the original finite B>=A remain unresolved.

## Mathlib

Full matching and supporting Mathlib coverage for this combined
specialization has not been checked. No absence or formal-verification
claim is made. The complete-DVR lifting input is precisely cited above;
the actual roots, residues, signs and derivatives are checked explicitly.
