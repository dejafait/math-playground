# Conditional full-image normality attempt — step335

Invocation-start coverage:
`drafts/literature/2026-10-19-full-mod120-conditional-legendre-normality.md`
(SPECIALIZE). Work only on its exact target, retaining L078–L080's
auxiliary E,D,s,t,iota,G and fixed closure. No image occurrence is assumed
except the explicit additional hypothesis rho_(E,120)(G_Q)=GL_2(Z/120Z).

Main gap: original finite B>=A. Intermediate target: evaluate the full
ordered-model fixing subgroups under that hypothesis. Downstream use:
screen maximal-image choices for this exact initial-data field prescription.
Continue on a changing conjugate or subgroup-normality certificate; stop
if an essential radical action remains undetermined. The cyclic stop in
ATTEMPTS/034 remains intact. No new source search is required: the ready
assessment covers Yelton's general formula and the exact Galois/twist method.

Working calculation saved before the full write-up: use
M=F_aux(A,B,C)=Q(E[60]), with A^2=D, B^2=e_3-e_1,
C^2=e_3-e_2. Surjectivity restricts to GL_2(Z/4) x GL_2(Z/15).
For k=Q(E[2],zeta_60), its fixing subgroup is
P x SL_2(Z/15), where P={I+2X:tr(X)=0 over F_2}, of order eight.
Yelton's full field-generation formula makes the sign map
P -> {+1,-1}^3 faithful, hence bijective. This is a degree argument,
not a guessed matrix-to-radical dictionary. L080 then gives
H_A={(p,chi_A(p)Id):p in P}, and similarly H_B,H_C.
Their orders are eight, their pair intersections have order four,
and their total intersection has order two. All three are actual
conjugates because the mod-two image is S_3. Expected exact index
of the normal closure over G: 8/2=4, versus one required for normality.

Completed this bounded attempt: the full proof, hypotheses, source
qualifications and Mathlib coverage are now canonical in
[L085](../lemmas/L085-full-mod120-forces-exact-legendre-field-nonnormality.md).
The complete stabilizers give exact normal-closure index four. No
mathematical script was needed for the eight-element character count.
This working note is not a separate critical audit.
Occurrence of the added image, independent initial data, native input/action,
all-image factorization, pilot transport, essentiality and finite B>=A remain
open. No change to the auxiliary curve, G, H or N is proposed.
