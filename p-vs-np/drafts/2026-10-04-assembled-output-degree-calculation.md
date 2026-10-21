# Assembled output-degree test: working reasoning

The saved SPECIALIZE assessment in `drafts/literature/2026-10-04-assembled-certificate-formal-degree.md` approves this exact test. No additional literature is needed. The local gap is converting L021's shared output to trees; the main uniform decision gap is unchanged. Success requires a surviving component of degree superpolynomial in L019's T_m, not another unfolding count.

Retain x,y and the first original-clause placeholder t_1; set every other original placeholder to zero. All Boolean/commutator witnesses and normalization corrections then vanish. Write W_0=x, W_1=y, W_i=W_(i-1)W_(i-2). The positive-unit roots project to t_1 R_i, with R_0=1, R_1=0 and the proposed recurrence

R_i=(R_(i-1)W_(i-2)+R_(i-2))(1+W_i).

The negative-unit roots should all project to zero: their ancestry uses only extension witnesses and the third original clause. The final unit resolution should therefore project to t_1 R_m. These claims still need checking against the actual pivot and sorted-clause orders in `check_assembly.py`, not just L021's abstract identities.

Tentative degree argument: R_2=1+W_2; thereafter the first summand dominates in degree. The proposed unique leading word is H_2=W_2 and H_i=H_(i-1)W_(i-2)W_i. This would give degree(t_1 R_m)=Fib_(m+3)+Fib_(m+1)-4, obstructing small trees for the exact output. Full other-placeholder terms need not be expanded if the projection is proved. This is unfinished reasoning, not yet a lemma or a claimed lower bound. L019's constant alternative certificate prevents any optimal-certificate or P-versus-NP inference.

Next within this step: verify the actual projected roots and independent word expansions in small cases, prove leading-word survival for all m, then save the result and continuation decision.

Completed: [L022](../lemmas/L022-assembled-output-surviving-exponential-degree.md) checks the actual orders, proves the proposed recurrence, verifies that every negative-unit root vanishes under the projection, and proves a unique leading word at every index. The projected degree is Fib_(m+3)+Fib_(m+1)-4; the full degree is at least this, without an asserted exact upper bound for the other sectors. Exact free-word checks through m=10 and full-placeholder checks through m=6 agree; the [saved diagnostic](../scripts/shared-extension/output-degree-results.json) distinguishes large upper-bound checks from word expansion. The tentative reasoning above is retained as the pre-calculation record; the lemma is the completed proof.

Decision: stop polynomial-size tree conversion of this exact polynomial, including attempts to reorganize it without changing its output. This is NEGATIVE local evidence, with the degree/size theorem imported and the family-specific result potentially beyond the checked full-statement comparison, not certified originality. Any degree-reduction continuation must permit a different certificate and pass its changed-target literature gate. The main goal remains unresolved; mathematical exploration turns used is 0 after this informative negative result.
