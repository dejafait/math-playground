# Step 121 — bounded supplied-C elimination work

The ready 2026-10-10 ER-to-clause-product assessment is reused without further browsing. Main gap: unrestricted SAT decision/separation. Approved bounded target: supplied original-axiom affine-F₂ ABP C with both IPS identities and exactly one placeholder-bearing edge on each accepting path. General ER-to-C remains independent.

Proposed test: normalize affine labels and partition the placeholder-linear sector by a marked placeholder edge, using x-only prefix/suffix subgraphs. Multiply the substituted identity by ordered f_F. For a clause edge j, write f_F=L_j(1+c_j)R_j and try

    L_j W(R_j P,c_j) S + L_j B(c_j) R_j P S,

where W is L035 and B is L036. The prospective substituted value is f_F P c_j S; both operands of W and B are x-only. Boolean/commutator edges use f_F P times their original placeholder times S. Sum the branches; cancellation of C(x,0) must be handled explicitly when mixed affine labels introduce placeholder-free paths.

Continue only after checking exact factor order, all formal identities, endpoint/empty-clause cases and one fixed full-bit bound in Q=2+|F|+|C|+|A|. Stop/narrow if the split needs path enumeration, placeholder commutators or conversion of arbitrary circuits. No ER-to-C assumption, W/V/U premise, faithful representatives or polynomial ER boundedness is allowed.

Completed: the preliminary formula omitted s_j before W. Direct ordered expansion detects the error; canonical L045 corrects it to L_j s_j W(R_j P,c_j) S + L_j B(c_j) R_j P S. Both identities and a conservative KQ^20 full-bit bound are proved there. Mixed affine labels create a zero-placeholder sector, handled by the supplied formal C(x,0)=0 identity rather than deleting its polynomial without justification. No mathematical script or numerical certificate was needed: the evidence is the all-input algebraic/path decomposition proof. General ER-to-C is still unresolved. A separate critical audit is the next proposed target.
