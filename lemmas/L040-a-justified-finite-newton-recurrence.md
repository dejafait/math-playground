# Lemma 40: a justified finite Newton recurrence

**Hypotheses.** e_0=1 and e_j=M_{2j}/((2j)!M_0) for j≥1. S_k are as in Lemma 25.

**Conclusion.** For every fixed integer k≥1,

S_k=Σ_{j=1}^{k-1}(-1)^{j-1}e_jS_{k-j}+(-1)^{k-1}ke_k.

For H_2 the three leading principal minors are S_2, S_2S_4-S_3², and

D_2=S_2S_4S_6+2S_3S_4S_5-S_2S_5²-S_6S_3²-S_4³.

If all three are positive, H_2 is positive definite.

**Proof.** The even entire series makes F(t)=Σ_{j≥0}(-1)^j e_jt^j entire in t: its absolute series at |t| equals that of Ξ at |z|=sqrt(|t|). Near 0, Lemma 25 gives log F(t)=-Σ_{k≥1}S_kt^k/k. Therefore F'(t)=-F(t)Σ_{k≥1}S_kt^{k-1} there, with both series convergent. Comparing the coefficient of t^{k-1} gives (-1)^k ke_k=-Σ_{j=0}^{k-1}(-1)^j e_jS_{k-j}; isolate S_k to obtain the recurrence. The determinant formula is the direct 3-by-3 determinant expansion for [[S_2,S_3,S_4],[S_3,S_4,S_5],[S_4,S_5,S_6]]. Positive leading principal minors imply positive definiteness by the standard named Sylvester criterion for real symmetric matrices. Alternatively eliminate the first coordinate and then the second: the diagonal pivots are S_2, (S_2S_4-S_3²)/S_2, and D_2/(S_2S_4-S_3²), all positive. ∎
