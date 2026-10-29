# Split stabilizer invariance — source review working record

2026-10-26, step 576; literature-only. No lemma, mathematical script,
counterexample, or invariance calculation is authorized by this review.

Exact invocation-start target: Assess whether the split-fibre stabilizer
action ad(h_0) preserves the actual section image rho_z(H), before
attempting to constrain its bracket rank.

Local inputs inspected: L164 hypotheses and actual restriction/form
statements; L170 hypotheses and incoming-plane comparison; L172
hypotheses and fixed normal evaluation; L116 hypotheses and global
cohomology statement. Reused the step-540 harmonic-operator/formality
warning and ATTEMPTS/092–094. Existing notebook changes are preserved.

Primary sources retrieved: Buchdahl–Schumacher, arXiv:2002.03548v1,
Theorem 1, PDF p. 2; Section 5 action and Lemma 5.1, pp. 14–15;
Corollary 5.3, p. 16. Chen–Pertusi–Zhao, author-hosted 15-page
Formality.pdf, Lemmas 2.3–2.4/Remark 2.5, p. 6, and Section 2.3,
pp. 6–7, including the invariant-splitting argument. Sources act by
automorphisms of the object whose deformation complex is considered;
no inspected statement equips the image of an unrelated restriction
map with the larger target object's group action.

Access qualifications: the journal Buchdahl–Schumacher PDF at d-nb
returned HTTP 429 and the publisher PDF returned 405; the complete
2020 primary preprint is accessible, and its version/page numbers must
be distinguished from the 2022 article. PMC returned a challenge;
the author-hosted Chen–Pertusi–Zhao PDF supplied the needed statements.

Completed: inspected the conjugation/harmonic proof in Corollary 4.3,
the same-object invariant-splitting construction, and Proposition 6.1's
Ext decomposition. The canonical completed comparison is
`drafts/literature/2026-10-26-split-stabilizer-section-image-invariance.md`;
the independent metric-star continuation remains REVIEW_REQUIRED. L116's
H^0(X,End_0(F))=0 remains in force. Absence of a supplied global
automorphism is not a proof that the actual image fails invariance.
